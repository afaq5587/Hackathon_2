"""Contract tests for the ToDo CLI API."""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from todo.task_manager import TaskManager
from todo.task import Task


class TestAPIContract:
    """Test suite for API contracts defined in contracts/api.md"""
    
    @pytest.fixture
    def manager(self):
        """Create a fresh TaskManager for each test."""
        return TaskManager()
    
    # Contract 1: Add Task
    def test_api_add_task_success(self, manager):
        """Test add task contract - success case."""
        task = manager.add_task("Buy milk")
        
        # Output: Success with task details
        assert isinstance(task, Task)
        assert task.title == "Buy milk"
        assert task.id is not None
        assert task.completed is False
    
    def test_api_add_task_with_description(self, manager):
        """Test add task contract - with description."""
        task = manager.add_task("Buy groceries", "Milk, bread, eggs")
        
        assert task.title == "Buy groceries"
        assert task.description == "Milk, bread, eggs"
    
    def test_api_add_task_empty_title_error(self, manager):
        """Test add task contract - error with empty title."""
        with pytest.raises(ValueError):
            manager.add_task("")
    
    # Contract 2: List Tasks
    def test_api_list_tasks_empty(self, manager):
        """Test list tasks contract - empty list."""
        tasks = manager.list_tasks()
        assert tasks == []
    
    def test_api_list_tasks_success(self, manager):
        """Test list tasks contract - with tasks."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        
        tasks = manager.list_tasks()
        assert len(tasks) == 3
        assert all(isinstance(t, Task) for t in tasks)
    
    def test_api_list_tasks_shows_completion_status(self, manager):
        """Test list tasks contract - shows completion status."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.complete_task(1)
        
        tasks = manager.list_tasks()
        assert tasks[0].completed is True
        assert tasks[1].completed is False
    
    # Contract 3: Update Task
    def test_api_update_task_success(self, manager):
        """Test update task contract - success case."""
        manager.add_task("Old title")
        task = manager.update_task(1, "New title")
        
        # Output: Updated task
        assert task.title == "New title"
        assert task.id == 1
    
    def test_api_update_task_with_description(self, manager):
        """Test update task contract - with description."""
        manager.add_task("Title", "Old description")
        task = manager.update_task(1, "Title", "New description")
        
        assert task.description == "New description"
    
    def test_api_update_task_invalid_id_error(self, manager):
        """Test update task contract - error with invalid ID."""
        with pytest.raises(ValueError):
            manager.update_task(999, "New title")
    
    def test_api_update_task_empty_title_error(self, manager):
        """Test update task contract - error with empty title."""
        manager.add_task("Task")
        with pytest.raises(ValueError):
            manager.update_task(1, "")
    
    # Contract 4: Delete Task
    def test_api_delete_task_success(self, manager):
        """Test delete task contract - success case."""
        manager.add_task("Task to delete")
        result = manager.delete_task(1)
        
        # Output: Success message, task removed
        assert result is True
        assert manager.get_task(1) is None
    
    def test_api_delete_task_invalid_id_error(self, manager):
        """Test delete task contract - error with invalid ID."""
        with pytest.raises(ValueError):
            manager.delete_task(999)
    
    # Contract 5: Complete Task
    def test_api_complete_task_success(self, manager):
        """Test complete task contract - success case."""
        manager.add_task("Task to complete")
        task = manager.complete_task(1)
        
        # Output: Success message, task marked complete
        assert task.completed is True
        assert task.id == 1
    
    def test_api_complete_task_invalid_id_error(self, manager):
        """Test complete task contract - error with invalid ID."""
        with pytest.raises(ValueError):
            manager.complete_task(999)
