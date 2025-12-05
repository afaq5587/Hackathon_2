import pytest
from src.models.task import Task, TaskStatus

def test_task_creation():
    task = Task(id=1, title="Test Task")
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.status == TaskStatus.PENDING
    assert task.description is None

def test_task_creation_with_description():
    task = Task(id=1, title="Test Task", description="Description")
    assert task.description == "Description"

def test_task_validation_empty_title():
    with pytest.raises(ValueError, match="Title cannot be empty"):
        Task(id=1, title="")

def test_task_validation_invalid_status():
    with pytest.raises(ValueError, match="Invalid status"):
        Task(id=1, title="Task", status="invalid_status")

def test_task_to_dict():
    task = Task(id=1, title="Test Task")
    data = task.to_dict()
    assert data["id"] == 1
    assert data["title"] == "Test Task"
    assert data["status"] == "pending"

def test_task_from_dict():
    data = {
        "id": 1,
        "title": "Test Task",
        "status": "completed",
        "description": "Desc",
        "created_at": "2023-01-01T12:00:00"
    }
    task = Task.from_dict(data)
    assert task.id == 1
    assert task.title == "Test Task"
    assert task.status == TaskStatus.COMPLETED
