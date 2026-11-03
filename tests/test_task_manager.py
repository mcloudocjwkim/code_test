
import tempfile
import unittest
from pathlib import Path

from app.task_manager import TaskManager


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        data_file = Path(self.temp_dir.name) / "tasks.json"
        self.manager = TaskManager(data_file)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_add_task(self):
        task_id = self.manager.add("온라인 디스크 테스트")
        self.assertEqual(task_id, 1)
        self.assertEqual(len(self.manager.list_all()), 1)

    def test_complete_task(self):
        task_id = self.manager.add("빌드 테스트")
        self.assertTrue(self.manager.complete(task_id))
        self.assertTrue(self.manager.list_all()[0]["completed"])

    def test_delete_task(self):
        task_id = self.manager.add("Git 테스트")
        self.assertTrue(self.manager.delete(task_id))
        self.assertEqual(len(self.manager.list_all()), 0)

    def test_missing_task(self):
        self.assertFalse(self.manager.complete(999))


if __name__ == "__main__":
    unittest.main()
