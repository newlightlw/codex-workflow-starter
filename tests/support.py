import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

PROJECT = Path(__file__).resolve().parents[1]


class CliCase(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.store = Path(self.directory.name) / "tasks.json"

    def cli(self, *args, ok=True):
        result = subprocess.run(
            [sys.executable, str(PROJECT / "taskbox.py"), "--store", str(self.store), *args],
            text=True, encoding="utf-8", capture_output=True,
            env={**os.environ, "PYTHONIOENCODING": "utf-8"}, timeout=10,
        )
        self.assertEqual(result.returncode, 0 if ok else 2, result.stderr)
        if ok:
            self.assertEqual(result.stderr, "")
            return json.loads(result.stdout)
        self.assertEqual(result.stdout, "")
        return json.loads(result.stderr)
