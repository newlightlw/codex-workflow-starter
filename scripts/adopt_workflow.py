"""Preview or install the standalone workflow Skill in an existing project."""

import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills" / "codex-workflow"


def installation_plan(project):
    project = project.expanduser().absolute()
    # Resolve only after checking ancestors, so links cannot redirect the install.
    for path in (project, *project.parents):
        if path.is_symlink():
            raise ValueError(f"symbolic-link project path is not supported: {path}")
    if not project.is_dir():
        raise ValueError("target project must be an existing directory")
    project = project.resolve()
    parent = project
    for name in (".agents", "skills"):
        parent = parent / name
        if parent.is_symlink():
            raise ValueError(f"symbolic-link destination is not supported: {parent}")
        if parent.exists() and not parent.is_dir():
            raise ValueError(f"destination parent is not a directory: {parent}")
    destination = parent / SOURCE.name
    if destination.exists() or destination.is_symlink():
        raise ValueError(f"Skill already exists; compare and merge manually: {destination}")
    files = sorted(path for path in SOURCE.rglob("*") if path.is_file())
    if not files or not (SOURCE / "SKILL.md").is_file():
        raise ValueError("source Skill is missing")
    return destination, files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--apply", action="store_true", help="install after previewing; never overwrite")
    args = parser.parse_args()
    try:
        destination, files = installation_plan(args.project)
        print(f"{'Install' if args.apply else 'Preview only'}: {destination}")
        for path in files:
            print(f"  {path.relative_to(SOURCE).as_posix()}")
        if args.apply:
            shutil.copytree(SOURCE, destination)
            print("Installed. Ask Codex to read .agents/skills/codex-workflow/SKILL.md in this project.")
        else:
            print("No files changed. Add --apply to install this Skill.")
    except (ValueError, OSError) as error:
        parser.exit(2, f"{error}\n")


if __name__ == "__main__":
    main()
