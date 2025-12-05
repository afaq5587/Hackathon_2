#!/usr/bin/env python3
"""Demo script for ToDo CLI application.

This script demonstrates all the features of the ToDo CLI application
in a single session with persistent in-memory storage.
"""

import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from todo.task_manager import TaskManager


def print_separator(title=""):
    """Print a formatted separator."""
    if title:
        print(f"\n{'='*70}")
        print(f"  {title}")
        print(f"{'='*70}\n")
    else:
        print(f"\n{'-'*70}\n")


def main():
    """Run the demo."""
    manager = TaskManager()
    
    # Demo 1: Add tasks
    print_separator("1. Adding Tasks")
    
    task1 = manager.add_task("Buy groceries")
    print(f"✓ Added task: {task1}")
    
    task2 = manager.add_task("Study Python", "Learn argparse and testing")
    print(f"✓ Added task: {task2}")
    
    task3 = manager.add_task("Exercise", "Morning jog")
    print(f"✓ Added task: {task3}")
    
    task4 = manager.add_task("Read book", "Finish chapter 5")
    print(f"✓ Added task: {task4}")
    
    # Demo 2: List tasks
    print_separator("2. Listing All Tasks")
    tasks = manager.list_tasks()
    print(f"Total tasks: {len(tasks)}\n")
    for task in tasks:
        desc = f" - {task.description}" if task.description else ""
        status = "✓ DONE" if task.completed else "○ TODO"
        print(f"{status:8} [{task.id:2}] {task.title}{desc}")
    
    stats = manager.get_stats()
    print(f"\nStats: Total={stats['total']}, Completed={stats['completed']}, Pending={stats['pending']}")
    
    # Demo 3: Mark tasks as complete
    print_separator("3. Marking Tasks as Complete")
    manager.complete_task(1)
    print(f"✓ Marked task 1 as complete")
    
    manager.complete_task(3)
    print(f"✓ Marked task 3 as complete")
    
    # Demo 4: Update a task
    print_separator("4. Updating a Task")
    updated = manager.update_task(2, "Study Python & Testing", "Learn argparse, unittest, pytest")
    print(f"✓ Updated task 2:")
    print(f"  Title: {updated.title}")
    print(f"  Description: {updated.description}")
    
    # Demo 5: List tasks again
    print_separator("5. Updated Task List")
    tasks = manager.list_tasks()
    for task in tasks:
        desc = f" - {task.description}" if task.description else ""
        status = "✓ DONE" if task.completed else "○ TODO"
        print(f"{status:8} [{task.id:2}] {task.title}{desc}")
    
    stats = manager.get_stats()
    print(f"\nStats: Total={stats['total']}, Completed={stats['completed']}, Pending={stats['pending']}")
    
    # Demo 6: Delete a task
    print_separator("6. Deleting a Task")
    manager.delete_task(4)
    print(f"✓ Deleted task 4 (Read book)")
    
    # Demo 7: Final list
    print_separator("7. Final Task List")
    tasks = manager.list_tasks()
    for task in tasks:
        desc = f" - {task.description}" if task.description else ""
        status = "✓ DONE" if task.completed else "○ TODO"
        print(f"{status:8} [{task.id:2}] {task.title}{desc}")
    
    stats = manager.get_stats()
    print(f"\nStats: Total={stats['total']}, Completed={stats['completed']}, Pending={stats['pending']}")
    
    # Demo 8: Error handling
    print_separator("8. Error Handling")
    
    # Try to add task with empty title
    try:
        manager.add_task("")
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")
    
    # Try to update non-existent task
    try:
        manager.update_task(999, "Non-existent")
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")
    
    # Try to delete non-existent task
    try:
        manager.delete_task(999)
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")
    
    # Try to complete non-existent task
    try:
        manager.complete_task(999)
    except ValueError as e:
        print(f"✓ Caught expected error: {e}")
    
    print("\n" + "="*70)
    print("  Demo Complete!")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
