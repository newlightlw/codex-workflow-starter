from support import CliCase


class BaselineTests(CliCase):
    def test_new_list_is_empty_and_does_not_create_store(self):
        self.assertEqual(self.cli("list"), [])
        self.assertFalse(self.store.exists())

    def test_add_trims_title_and_persists_across_processes(self):
        expected = {"id": 1, "title": "读规格", "status": "pending"}
        self.assertEqual(self.cli("add", "  读规格  "), expected)
        self.assertEqual(self.cli("list"), [expected])

    def test_multiple_tasks_keep_order_and_unique_ids(self):
        self.cli("add", "first")
        self.cli("add", "second")
        self.assertEqual(self.cli("list"), [
            {"id": 1, "title": "first", "status": "pending"},
            {"id": 2, "title": "second", "status": "pending"},
        ])

    def test_empty_title_does_not_create_store(self):
        self.assertIn("title", self.cli("add", "  ", ok=False)["error"])
        self.assertFalse(self.store.exists())

    def test_title_boundaries(self):
        for length in (1, 80):
            with self.subTest(length=length):
                self.assertEqual(self.cli("add", "中" * length)["title"], "中" * length)
        before = self.store.read_bytes()
        self.assertIn("title", self.cli("add", "中" * 81, ok=False)["error"])
        self.assertEqual(self.store.read_bytes(), before)

    def test_malformed_json_is_reported_without_overwrite(self):
        self.store.write_text("{broken", encoding="utf-8")
        self.assertTrue(self.cli("add", "new", ok=False)["error"])
        self.assertEqual(self.store.read_text(encoding="utf-8"), "{broken")

    def test_invalid_store_structure_is_preserved(self):
        fixtures = [
            '{}', '[null]', '[{"id": 1}]',
            '[{"id":true,"title":"a","status":"pending"}]',
            '[{"id":1,"title":"a","status":"succeeded"}]',
            '[{"id":1,"title":" ","status":"pending"}]',
            '[{"id":1,"title":"a","status":"pending"},'
            '{"id":1,"title":"b","status":"pending"}]',
        ]
        for payload in fixtures:
            with self.subTest(payload=payload):
                self.store.write_text(payload, encoding="utf-8")
                self.assertEqual(self.cli("add", "new", ok=False)["error"], "invalid task store")
                self.assertEqual(self.store.read_text(encoding="utf-8"), payload)

    def test_unavailable_parent_is_reported_without_creating_directories(self):
        self.store = self.store.parent / "missing" / "tasks.json"
        self.assertTrue(self.cli("add", "new", ok=False)["error"])
        self.assertFalse(self.store.parent.exists())
