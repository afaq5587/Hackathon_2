"""Integration tests for the CLI."""

import sys
import os
import pytest

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from todo.task_manager import TaskManager


class TestCLIIntegration:
    """Integration tests for the task manager workflow."""
    
    def test_complete_workflow(self):
        """Test complete workflow: add, update, complete, delete."""
        manager = TaskManager()
        
        # Add tasks
        task1 = manager.add_task("Buy milk")
        task2 = manager.add_task("Study", "Python")
        task3 = manager.add_task("Exercise")
        
        assert len(manager.list_tasks()) == 3
        
        # Update
        updated = manager.update_task(1, "Buy milk and bread")
        assert updated.title == "Buy milk and bread"
        
        # Complete
        manager.complete_task(1)
        assert manager.get_task(1).completed is True
        
        # Delete
        manager.delete_task(3)
        assert manager.get_task(3) is None
        
        # Final state
        tasks = manager.list_tasks()
        assert len(tasks) == 2
        stats = manager.get_stats()
        assert stats["total"] == 2
        assert stats["completed"] == 1
        assert stats["pending"] == 1
    
    def test_add_multiple_and_list(self):
        """Test adding multiple tasks and listing them."""
        manager = TaskManager()
        
        for i in range(5):
            manager.add_task(f"Task {i+1}", f"Description {i+1}")
        
        tasks = manager.list_tasks()
        assert len(tasks) == 5
        assert all(t.description for t in tasks)
    
    def test_error_handling_workflow(self):
        """Test error scenarios during workflow."""
        manager = TaskManager()
        manager.add_task("Task 1")
        
        # Invalid operations
        with pytest.raises(ValueError):
            manager.add_task("")
        
        with pytest.raises(ValueError):
            manager.update_task(1, "")
        
        with pytest.raises(ValueError):
            manager.delete_task(999)
        
        with pytest.raises(ValueError):
            manager.complete_task(999)
        
        # Original task should still exist
        assert len(manager.list_tasks()) == 1
