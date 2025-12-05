"""Task model for ToDo application."""

from datetime import datetime
from typing import Optional


class Task:
    """Represents a single to-do item.
    
    Attributes:
        id: Unique identifier for the task
        title: The task title (required)
        description: Optional description of the task
        completed: Whether the task is marked as complete
        created_at: ISO timestamp of when the task was created
    """
    
    def __init__(
        self,
        id: int,
        title: str,
        description: Optional[str] = None,
        completed: bool = False,
        created_at: Optional[str] = None,
    ):
        """Initialize a Task.
        
        Args:
            id: Unique identifier for the task
            title: The title of the task
            description: Optional description of the task
            completed: Whether the task is completed (default: False)
            created_at: ISO timestamp (auto-generated if not provided)
        """
        self.id = id
        self.title = title
        self.description = description or ""
        self.completed = completed
        self.created_at = created_at or datetime.utcnow().isoformat()
    
    def to_dict(self) -> dict:
        """Convert task to dictionary representation.
        
        Returns:
            Dictionary containing all task attributes
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
        }
    
    def __repr__(self) -> str:
        """Return string representation of task."""
        status = "✓" if self.completed else "○"
        return f"{status} [{self.id}] {self.title}"
    
    def __str__(self) -> str:
        """Return human-readable string representation."""
        return self.__repr__()
