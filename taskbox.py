"""A small, local-only task list with a JSON command-line interface."""

import argparse
import json
import os
from pathlib import Path
import sys
import tempfile


def load_tasks(path):
    if not path.exists():
        return []
    tasks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tasks, list):
        raise ValueError("invalid task store")
    ids = set()
    for task in tasks:
        if (
            not isinstance(task, dict)
            or set(task) != {"id", "title", "status"}
            or type(task["id"]) is not int
            or task["id"] <= 0
            or task["id"] in ids
            or not isinstance(task["title"], str)
            or not 1 <= len(task["title"]) <= 80
            or task["title"] != task["title"].strip()
            or task["status"] not in ("pending", "completed")
        ):
            raise ValueError("invalid task store")
        ids.add(task["id"])
    return tasks


def save_tasks(path, tasks):
    # Write beside the destination so replacement stays on the same filesystem.
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, delete=False
        ) as stream:
            temporary = Path(stream.name)
            json.dump(tasks, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--store", type=Path, default=Path(".taskbox.json"))
    commands = parser.add_subparsers(dest="command", required=True)
    add = commands.add_parser("add")
    add.add_argument("title")
    commands.add_parser("list")
    complete = commands.add_parser("complete")
    complete.add_argument("id", type=int)
    args = parser.parse_args()

    try:
        tasks = load_tasks(args.store)
        if args.command == "list":
            result = tasks
        elif args.command == "add":
            title = args.title.strip()
            if not 1 <= len(title) <= 80:
                raise ValueError("title must contain 1 to 80 characters")
            result = {"id": max((t["id"] for t in tasks), default=0) + 1,
                      "title": title, "status": "pending"}
            tasks.append(result)
            save_tasks(args.store, tasks)
        else:
            # COMPLETE_IMPLEMENTATION_START
            result = next((task for task in tasks if task["id"] == args.id), None)
            if result is None:
                raise ValueError("task not found")
            if result["status"] != "completed":
                result["status"] = "completed"
                save_tasks(args.store, tasks)
            # COMPLETE_IMPLEMENTATION_END
        print(json.dumps(result, ensure_ascii=False))
        return 0
    except (ValueError, OSError) as error:
        print(json.dumps({"error": str(error)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
