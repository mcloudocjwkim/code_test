
import json
from pathlib import Path


class TaskManager:
    def __init__(self, data_file):
        self.data_file = Path(data_file)
        self.data_file.parent.mkdir(parents=True, exist_ok=True)

        if not self.data_file.exists():
            self._save([])

    def _load(self):
        if not self.data_file.exists():
            return []

        with self.data_file.open("r", encoding="utf-8-sig") as file:
            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    def _save(self, tasks):
        with self.data_file.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)

    def add(self, title):
        tasks = self._load()

        next_id = max(
            (task["id"] for task in tasks),
            default=0
        ) + 1

        tasks.append({
            "id": next_id,
            "title": title,
            "completed": False
        })

        self._save(tasks)
        return next_id

    def list_all(self):
        return self._load()

    def complete(self, task_id):
        tasks = self._load()

        for task in tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self._save(tasks)
                return True

        return False

    def delete(self, task_id):
        tasks = self._load()
        remaining = [
            task for task in tasks
            if task["id"] != task_id
        ]

        if len(tasks) == len(remaining):
            return False

        self._save(remaining)
        return True
