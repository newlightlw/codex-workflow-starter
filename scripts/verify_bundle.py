"""Verify that the distributed Skill snapshot includes its locked files."""

import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / "skills-lock.json").read_text(encoding="utf-8"))
    errors = []
    count = 0
    for name, entry in manifest["skills"].items():
        folder = ROOT / ".agents/skills" / name
        actual = {p.relative_to(folder).as_posix() for p in folder.rglob("*") if p.is_file()}
        expected = set(entry["files"])
        if actual != expected:
            errors.append(f"{name}: file set differs from lock")
        for filename, digest in entry["files"].items():
            path = folder / filename
            if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != digest:
                errors.append(f"{name}/{filename}: missing or changed")
            count += 1
    for required in ("LICENSE", "THIRD_PARTY_NOTICES.md", "LICENSES/mattpocock-skills-MIT.txt",
                     "LICENSES/karpathy-guidelines-NOTICE.md", "AGENTS.md", "docs/requirements.md"):
        if not (ROOT / required).is_file():
            errors.append(f"missing required file: {required}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Bundle verified: {len(manifest['skills'])} skills, {count} locked files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
