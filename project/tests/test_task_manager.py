"""Unit tests for TaskManager class."""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from todo.task_manager import TaskManager


class TestTaskManager:
    """Test cases for the TaskManager class."""
    
    @pytest.fixture
    def manager(self):
        """Create a fresh TaskManager for each test."""
        return TaskManager()
    
    # Test add_task
    def test_add_task(self, manager):
        """Test adding a task."""
        task = manager.add_task("Buy groceries")
        assert task.id == 1
        assert task.title == "Buy groceries"
        assert task.completed is False
    
    def test_add_task_with_description(self, manager):
        """Test adding a task with description."""
        task = manager.add_task("Buy groceries", "Milk, bread, eggs")
        assert task.title == "Buy groceries"
        assert task.description == "Milk, bread, eggs"
    
    def test_add_task_increments_id(self, manager):
        """Test that IDs are incremented."""
        task1 = manager.add_task("Task 1")
        task2 = manager.add_task("Task 2")
        assert task1.id == 1
        assert task2.id == 2
    
    def test_add_task_empty_title_raises_error(self, manager):
        """Test that adding task with empty title raises error."""
        with pytest.raises(ValueError, match="cannot be empty"):
            manager.add_task("")
    
    def test_add_task_none_title_raises_error(self, manager):
        """Test that adding task with None title raises error."""
        with pytest.raises(ValueError, match="cannot be empty"):
            manager.add_task(None)
    
    def test_add_task_whitespace_title_raises_error(self, manager):
        """Test that adding task with only whitespace raises error."""
        with pytest.raises(ValueError, match="cannot be empty"):
            manager.add_task("   ")
    
    def test_add_task_strips_whitespace(self, manager):
        """Test that task title whitespace is stripped."""
        task = manager.add_task("  Buy groceries  ")
        assert task.title == "Buy groceries"
    
    # Test list_tasks
    def test_list_tasks_empty(self, manager):
        """Test listing tasks when empty."""
        tasks = manager.list_tasks()
        assert tasks == []
    
    def test_list_tasks(self, manager):
        """Test listing multiple tasks."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        
        tasks = manager.list_tasks()
        assert len(tasks) == 3
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"
        assert tasks[2].title == "Task 3"
    
    def test_list_tasks_sorted_by_id(self, manager):
        """Test that list_tasks returns tasks sorted by ID."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        
        tasks = manager.list_tasks()
        ids = [t.id for t in tasks]
        assert ids == sorted(ids)
    
    # Test get_task
    def test_get_task(self, manager):
        """Test getting a specific task."""
        task = manager.add_task("Test Task")
        retrieved = manager.get_task(1)
        assert retrieved is not None
        assert retrieved.id == task.id
        assert retrieved.title == task.title
    
    def test_get_task_nonexistent(self, manager):
        """Test getting a nonexistent task."""
        result = manager.get_task(999)
        assert result is None
    
    # Test update_task
    def test_update_task(self, manager):
        """Test updating a task."""
        manager.add_task("Old Title")
        task = manager.update_task(1, "New Title")
        assert task.title == "New Title"
    
    def test_update_task_with_description(self, manager):
        """Test updating task with description."""
        manager.add_task("Title", "Old description")
        task = manager.update_task(1, "Title", "New description")
        assert task.description == "New description"
    
    def test_update_task_empty_title_raises_error(self, manager):
        """Test that updating with empty title raises error."""
        manager.add_task("Test Task")
        with pytest.raises(ValueError, match="cannot be empty"):
            manager.update_task(1, "")
    
    def test_update_task_nonexistent_raises_error(self, manager):
        """Test that updating nonexistent task raises error."""
        with pytest.raises(ValueError, match="not found"):
            manager.update_task(999, "New Title")
    
    # Test delete_task
    def test_delete_task(self, manager):
        """Test deleting a task."""
        manager.add_task("Task to delete")
        result = manager.delete_task(1)
        assert result is True
        assert manager.get_task(1) is None
    
    def test_delete_task_nonexistent_raises_error(self, manager):
        """Test that deleting nonexistent task raises error."""
        with pytest.raises(ValueError, match="not found"):
            manager.delete_task(999)
    
    def test_delete_task_removes_from_list(self, manager):
        """Test that deleted task is removed from list."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.delete_task(1)
        
        tasks = manager.list_tasks()
        assert len(tasks) == 1
        assert tasks[0].id == 2
    
    # Test complete_task
    def test_complete_task(self, manager):
        """Test marking a task as complete."""
        manager.add_task("Task to complete")
        task = manager.complete_task(1)
        assert task.completed is True
    
    def test_complete_task_nonexistent_raises_error(self, manager):
        """Test that completing nonexistent task raises error."""
        with pytest.raises(ValueError, match="not found"):
            manager.complete_task(999)
    
    def test_complete_task_already_completed(self, manager):
        """Test that completing already complete task works."""
        manager.add_task("Task")
        manager.complete_task(1)
        task = manager.complete_task(1)
        assert task.completed is True
    
    # Test get_stats
    def test_get_stats_empty(self, manager):
        """Test stats with no tasks."""
        stats = manager.get_stats()
        assert stats["total"] == 0
        assert stats["completed"] == 0
        assert stats["pending"] == 0
    
    def test_get_stats_with_tasks(self, manager):
        """Test stats with mixed task states."""
        manager.add_task("Task 1")
        manager.add_task("Task 2")
        manager.add_task("Task 3")
        manager.complete_task(1)
        manager.complete_task(2)
        
        stats = manager.get_stats()
        assert stats["total"] == 3
        assert stats["completed"] == 2
        assert stats["pending"] == 1
