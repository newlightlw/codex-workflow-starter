import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class AdoptionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        # Resolve macOS /var -> /private/var for the target-path guard.
        self.base = Path(self.temporary.name).resolve()
        self.project = self.base / "existing 项目 with spaces"
        self.project.mkdir()
        (self.project / "AGENTS.md").write_bytes(b"existing project rules\n")
        (self.project / "user.txt").write_bytes(b"uncommitted user changes\n")

    def cli(self, *args, project=None):
        return subprocess.run(
            [sys.executable, str(ROOT / "scripts/adopt_workflow.py"), str(project or self.project), *args],
            capture_output=True, text=True, encoding="utf-8", timeout=10,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )

    def snapshot(self):
        return {p.relative_to(self.project).as_posix(): p.read_bytes()
                for p in self.project.rglob("*") if p.is_file()}

    def link_directory(self, link, target):
        try:
            link.symlink_to(target, target_is_directory=True)
        except NotImplementedError:
            self.skipTest("directory symlinks are unsupported on this platform")
        except OSError as error:
            if getattr(error, "winerror", None) == 1314:
                self.skipTest("Windows account lacks the privilege to create symlinks")
            raise

    def test_preview_writes_nothing(self):
        before = self.snapshot()
        result = self.cli()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Preview only", result.stdout)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.project / ".agents").exists())

    def test_apply_is_complete_and_preserves_existing_project(self):
        other = self.project / ".agents/skills/existing/SKILL.md"
        other.parent.mkdir(parents=True)
        other.write_text("existing skill", encoding="utf-8")
        before = self.snapshot()
        result = self.cli("--apply")
        self.assertEqual(result.returncode, 0, result.stderr)
        for name, content in before.items():
            self.assertEqual((self.project / name).read_bytes(), content)
        installed = self.project / ".agents/skills/codex-workflow"
        for required in ("SKILL.md", "LICENSE.txt", "assets/TASK.md", "assets/STATE.md",
                         "assets/VALIDATION.md", "references/state-and-recovery.md"):
            self.assertTrue((installed / required).is_file(), required)
        for doc in installed.rglob("*.md"):
            for target in re.findall(r"\]\(([^)]+)\)", doc.read_text(encoding="utf-8")):
                if "://" not in target:
                    self.assertTrue((doc.parent / target).is_file(), (doc, target))
        for added in set(self.snapshot()) - set(before):
            self.assertTrue(added.startswith(".agents/skills/codex-workflow/"), added)

    def test_second_install_does_not_overwrite_local_edits(self):
        self.assertEqual(self.cli("--apply").returncode, 0)
        local = self.project / ".agents/skills/codex-workflow/SKILL.md"
        local.write_text("my customization", encoding="utf-8")
        before = self.snapshot()
        result = self.cli("--apply")
        self.assertEqual(result.returncode, 2)
        self.assertIn("already exists", result.stderr)
        self.assertEqual(self.snapshot(), before)

    def test_missing_project_is_not_created(self):
        missing = self.base / "missing"
        result = self.cli("--apply", project=missing)
        self.assertEqual(result.returncode, 2)
        self.assertFalse(missing.exists())

    def test_file_blocking_destination_is_preserved(self):
        (self.project / ".agents").write_bytes(b"not a directory")
        before = self.snapshot()
        result = self.cli("--apply")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(self.snapshot(), before)

    def test_linked_destination_does_not_write_outside_project(self):
        outside = self.base / "outside"
        outside.mkdir()
        self.link_directory(self.project / ".agents", outside)
        result = self.cli("--apply")
        self.assertEqual(result.returncode, 2)
        self.assertIn("symbolic-link", result.stderr)
        self.assertEqual(list(outside.iterdir()), [])

    def test_linked_project_is_rejected(self):
        alias = self.base / "alias"
        self.link_directory(alias, self.project)
        result = self.cli("--apply", project=alias)
        self.assertEqual(result.returncode, 2)
        self.assertFalse((self.project / ".agents").exists())
