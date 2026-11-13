"""Create a standalone exercise in a new directory; never modify global config."""

import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def create_exercise(destination):
    destination = destination.expanduser().resolve()
    if destination.exists():
        raise ValueError(f"destination already exists: {destination}")
    if destination == ROOT or ROOT in destination.parents:
        raise ValueError("choose a directory outside this reference repository")
    if not destination.parent.is_dir():
        raise ValueError("destination parent directory must already exist")

    destination.mkdir()
    for name in (".agents", "LICENSES", "templates"):
        shutil.copytree(ROOT / name, destination / name)
    for name in ("LICENSE", "THIRD_PARTY_NOTICES.md", "skills-lock.json", ".gitignore", ".gitattributes"):
        shutil.copy2(ROOT / name, destination / name)
    (destination / "tests").mkdir()
    for name in ("support.py", "test_baseline.py"):
        shutil.copy2(ROOT / "tests" / name, destination / "tests" / name)
    source = (ROOT / "taskbox.py").read_text(encoding="utf-8")
    start = source.index("            # COMPLETE_IMPLEMENTATION_START")
    end = source.index("            # COMPLETE_IMPLEMENTATION_END")
    end += len("            # COMPLETE_IMPLEMENTATION_END")
    source = source[:start] + '            raise ValueError("complete is not implemented yet")' + source[end:]
    (destination / "taskbox.py").write_text(source, encoding="utf-8")
    for item in (ROOT / "exercises" / "complete-task" / "project").iterdir():
        if item.is_dir():
            shutil.copytree(item, destination / item.name)
        else:
            shutil.copy2(item, destination / item.name)
    shutil.copy2(ROOT / "exercises" / "complete-task" / "test_complete.py",
                 destination / "tests" / "test_complete.py")
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path)
    args = parser.parse_args()
    try:
        created = create_exercise(args.destination)
    except (ValueError, OSError) as error:
        parser.exit(2, f"{error}\n")
    print(f"Created: {created}")
    print("Baseline: python3 -m unittest discover -s tests -p test_baseline.py -v")
    print("Expected RED: python3 -m unittest discover -s tests -p test_complete.py -v")
    print("Open this directory in Codex, read README.md, and start the exercise.")


if __name__ == "__main__":
    main()
