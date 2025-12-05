from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, Any

class TaskStatus(str, Enum):
    PENDING = "pending"
    COMPLETED = "completed"

@dataclass
class Task:
    """
    Task model representing a single todo item.
    """
    id: int
    title: str
    status: TaskStatus = TaskStatus.PENDING
    description: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validate task attributes."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")
        
        if isinstance(self.status, str):
            try:
                self.status = TaskStatus(self.status.lower())
            except ValueError:
                raise ValueError(f"Invalid status: {self.status}. Must be 'pending' or 'completed'")

    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary for storage."""
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status.value,
            "description": self.description,
            "created_at": self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        """Create task from dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            status=TaskStatus(data["status"]),
            description=data.get("description"),
            created_at=datetime.fromisoformat(data["created_at"])
        )
