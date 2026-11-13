from support import CliCase


class CompleteTaskTracerTest(CliCase):
    def test_complete_is_visible_after_reopening(self):
        self.cli("add", "读规格")
        expected = {"id": 1, "title": "读规格", "status": "completed"}
        self.assertEqual(self.cli("complete", "1"), expected)
        self.assertEqual(self.cli("list"), [expected])
