import json
import os
from typing import List
from ..models.task import Task

class JsonStorage:
    """
    Handles persistence of tasks to a JSON file.
    """
    def __init__(self, filepath: str = "tasks.json"):
        self.filepath = filepath

    def load_tasks(self) -> List[Task]:
        """Load tasks from the JSON file."""
        if not os.path.exists(self.filepath):
            return []
        
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, OSError):
            return []

    def save_tasks(self, tasks: List[Task]) -> None:
        """Save tasks to the JSON file."""
        data = [task.to_dict() for task in tasks]
        try:
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2)
        except OSError as e:
            raise OSError(f"Failed to save tasks: {e}")
