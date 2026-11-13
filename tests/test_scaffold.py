from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ExerciseTests(unittest.TestCase):
    def test_fresh_exercise_runs_red_then_reference_runs_green(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "practice with spaces"
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/new_exercise.py"), str(target)],
                capture_output=True, text=True, encoding="utf-8", timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            command = [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"]
            baseline = subprocess.run(command + ["-p", "test_baseline.py"], cwd=target,
                                      capture_output=True, text=True, timeout=30)
            self.assertEqual(baseline.returncode, 0, baseline.stderr)
            red = subprocess.run(command + ["-p", "test_complete.py"], cwd=target,
                                 capture_output=True, text=True, timeout=30)
            self.assertEqual(red.returncode, 1, red.stderr)
            self.assertIn("complete is not implemented yet", red.stderr)
            self.assertIn("FAILED (failures=1)", red.stderr)
            # Oracle check only: a reader implements the feature in Codex instead.
            shutil.copy2(ROOT / "taskbox.py", target / "taskbox.py")
            green = subprocess.run(command, cwd=target, capture_output=True, text=True, timeout=30)
            self.assertEqual(green.returncode, 0, green.stderr)

    def test_existing_destination_is_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            sentinel = target / "keep.txt"
            sentinel.write_text("keep", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(ROOT / "scripts/new_exercise.py"), str(target)],
                capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(result.returncode, 2)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")
            self.assertEqual(list(target.iterdir()), [sentinel])
