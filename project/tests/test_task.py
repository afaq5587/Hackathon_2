"""Unit tests for Task model."""

import pytest
import sys
import os
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from todo.task import Task


class TestTask:
    """Test cases for the Task class."""
    
    def test_task_creation(self):
        """Test creating a basic task."""
        task = Task(id=1, title="Test Task")
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.completed is False
        assert task.created_at is not None
    
    def test_task_creation_with_description(self):
        """Test creating a task with description."""
        task = Task(id=1, title="Test Task", description="A test task")
        assert task.title == "Test Task"
        assert task.description == "A test task"
    
    def test_task_creation_with_completed(self):
        """Test creating a completed task."""
        task = Task(id=1, title="Test Task", completed=True)
        assert task.completed is True
    
    def test_task_creation_with_created_at(self):
        """Test creating a task with specific created_at."""
        iso_time = "2025-12-05T10:00:00"
        task = Task(id=1, title="Test Task", created_at=iso_time)
        assert task.created_at == iso_time
    
    def test_task_to_dict(self):
        """Test converting task to dictionary."""
        task = Task(id=1, title="Test Task", description="A test", completed=True)
        task_dict = task.to_dict()
        
        assert task_dict["id"] == 1
        assert task_dict["title"] == "Test Task"
        assert task_dict["description"] == "A test"
        assert task_dict["completed"] is True
        assert "created_at" in task_dict
    
    def test_task_repr(self):
        """Test string representation of task."""
        task = Task(id=1, title="Test Task")
        assert "Test Task" in repr(task)
        assert "1" in repr(task)
    
    def test_task_repr_completed(self):
        """Test string representation of completed task."""
        task = Task(id=1, title="Test Task", completed=True)
        assert "✓" in repr(task)
    
    def test_task_repr_pending(self):
        """Test string representation of pending task."""
        task = Task(id=1, title="Test Task", completed=False)
        assert "○" in repr(task)
