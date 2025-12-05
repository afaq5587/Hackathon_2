from typing import List, Optional
from ..models.task import Task, TaskStatus
from ..storage.json_storage import JsonStorage

class TaskService:
    """
    Business logic for managing tasks.
    """
    def __init__(self, storage: JsonStorage):
        self.storage = storage
        self.tasks: List[Task] = self.storage.load_tasks()
        self._next_id = max([t.id for t in self.tasks], default=0) + 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task."""
        task = Task(id=self._next_id, title=title, description=description)
        self.tasks.append(task)
        self._next_id += 1
        self.storage.save_tasks(self.tasks)
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a task by ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_tasks(self, status: Optional[TaskStatus] = None) -> List[Task]:
        """List tasks, optionally filtered by status."""
        if status:
            return [t for t in self.tasks if t.status == status]
        return self.tasks

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """Update an existing task."""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        
        if title:
            task.title = title
        if description is not None:
            task.description = description
            
        self.storage.save_tasks(self.tasks)
        return task

    def delete_task(self, task_id: int) -> None:
        """Delete a task by ID."""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
        
        self.tasks.remove(task)
        self.storage.save_tasks(self.tasks)

    def complete_task(self, task_id: int) -> Task:
        """Mark a task as complete."""
        task = self.get_task(task_id)
        if not task:
            raise ValueError(f"Task with ID {task_id} not found")
            
        task.status = TaskStatus.COMPLETED
        self.storage.save_tasks(self.tasks)
        return task

    def search_tasks(self, keyword: str) -> List[Task]:
        """Search tasks by title or description."""
        keyword = keyword.lower()
        return [
            t for t in self.tasks 
            if keyword in t.title.lower() or (t.description and keyword in t.description.lower())
        ]
        
    def clear_completed(self) -> int:
        """Remove all completed tasks. Returns number of removed tasks."""
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.status != TaskStatus.COMPLETED]
        removed_count = initial_count - len(self.tasks)
        if removed_count > 0:
            self.storage.save_tasks(self.tasks)
        return removed_count
