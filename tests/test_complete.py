from support import CliCase


class CompleteTests(CliCase):
    def test_complete_is_visible_in_a_new_process(self):
        self.cli("add", "读规格")
        expected = {"id": 1, "title": "读规格", "status": "completed"}
        self.assertEqual(self.cli("complete", "1"), expected)
        self.assertEqual(self.cli("list"), [expected])

    def test_repeated_completion_preserves_content(self):
        self.cli("add", "read")
        first = self.cli("complete", "1")
        before = self.store.read_bytes()
        self.assertEqual(self.cli("complete", "1"), first)
        self.assertEqual(self.store.read_bytes(), before)

    def test_only_the_selected_task_changes(self):
        self.cli("add", "one")
        self.cli("add", "two")
        self.cli("complete", "2")
        self.assertEqual(self.cli("list"), [
            {"id": 1, "title": "one", "status": "pending"},
            {"id": 2, "title": "two", "status": "completed"},
        ])

    def test_missing_id_keeps_existing_data(self):
        self.cli("add", "read")
        before = self.store.read_bytes()
        for task_id in ("99", "0", "-1"):
            with self.subTest(task_id=task_id):
                self.assertEqual(self.cli("complete", task_id, ok=False)["error"], "task not found")
                self.assertEqual(self.store.read_bytes(), before)

    def test_completion_on_empty_store_does_not_create_file(self):
        self.assertEqual(self.cli("complete", "1", ok=False)["error"], "task not found")
        self.assertFalse(self.store.exists())
