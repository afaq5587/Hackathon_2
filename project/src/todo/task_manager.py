"""TaskManager class for managing tasks."""

from typing import List, Optional
from .task import Task


class TaskManager:
    """Manages task operations with in-memory storage.
    
    Provides methods for adding, listing, updating, deleting, and completing tasks.
    """
    
    def __init__(self):
        """Initialize TaskManager with empty task storage."""
        self.tasks: dict = {}  # id -> Task
        self.next_id: int = 1
    
    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """Add a new task.
        
        Args:
            title: The title of the task (required)
            description: Optional description of the task
            
        Returns:
            The created Task object
            
        Raises:
            ValueError: If title is empty or None
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(
            id=self.next_id,
            title=title.strip(),
            description=description,
        )
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task
    
    def list_tasks(self) -> List[Task]:
        """Get all tasks.
        
        Returns:
            List of all tasks sorted by ID
        """
        return sorted(self.tasks.values(), key=lambda t: t.id)
    
    def get_task(self, task_id: int) -> Optional[Task]:
        """Get a specific task by ID.
        
        Args:
            task_id: The ID of the task to retrieve
            
        Returns:
            The Task object if found, None otherwise
        """
        return self.tasks.get(task_id)
    
    def update_task(self, task_id: int, title: str, description: Optional[str] = None) -> Task:
        """Update an existing task.
        
        Args:
            task_id: The ID of the task to update
            title: The new title for the task (required)
            description: Optional new description
            
        Returns:
            The updated Task object
            
        Raises:
            ValueError: If title is empty, None, or task_id doesn't exist
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        
        task = self.tasks[task_id]
        task.title = title.strip()
        if description is not None:
            task.description = description
        return task
    
    def delete_task(self, task_id: int) -> bool:
        """Delete a task.
        
        Args:
            task_id: The ID of the task to delete
            
        Returns:
            True if task was deleted, False otherwise
            
        Raises:
            ValueError: If task_id doesn't exist
        """
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        
        del self.tasks[task_id]
        return True
    
    def complete_task(self, task_id: int) -> Task:
        """Mark a task as complete.
        
        Args:
            task_id: The ID of the task to complete
            
        Returns:
            The completed Task object
            
        Raises:
            ValueError: If task_id doesn't exist
        """
        if task_id not in self.tasks:
            raise ValueError(f"Task with ID {task_id} not found")
        
        task = self.tasks[task_id]
        task.completed = True
        return task
    
    def get_stats(self) -> dict:
        """Get task statistics.
        
        Returns:
            Dictionary with total, completed, and pending task counts
        """
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks.values() if t.completed)
        pending = total - completed
        return {
            "total": total,
            "completed": completed,
            "pending": pending,
        }
