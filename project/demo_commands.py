#!/usr/bin/env python3
"""
Single-session demo showing todo commands with persistent state.
This demonstrates all commands working in one session.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src'))

from todo.task_manager import TaskManager


def print_header(title):
    """Print a formatted header."""
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}\n")


def print_tasks(manager):
    """Display current tasks."""
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks found. Use 'todo add <title>' to create a task.\n")
        return
    
    print(f"Tasks ({len(tasks)} total):")
    print("-" * 70)
    for task in tasks:
        status = "✓ DONE" if task.completed else "○ TODO"
        desc = f" - {task.description}" if task.description else ""
        print(f"{status:8} [{task.id:2}] {task.title}{desc}")
    
    stats = manager.get_stats()
    print("-" * 70)
    print(f"Total: {stats['total']} | Completed: {stats['completed']} | Pending: {stats['pending']}\n")


def main():
    """Run the demo."""
    manager = TaskManager()
    
    print_header("ToDo CLI - Command Demo (Single Session)")
    
    # Demo: Add commands
    print("$ todo add \"Buy groceries\"")
    task = manager.add_task("Buy groceries")
    print(f"✓ Task added (ID: {task.id})")
    
    print("\n$ todo add \"Study Python\" -d \"Learn argparse\"")
    task = manager.add_task("Study Python", "Learn argparse")
    print(f"✓ Task added (ID: {task.id})")
    
    print("\n$ todo add \"Exercise\" -d \"30 min run\"")
    task = manager.add_task("Exercise", "30 min run")
    print(f"✓ Task added (ID: {task.id})")
    
    # Demo: List
    print("\n$ todo list")
    print_tasks(manager)
    
    # Demo: Complete
    print("$ todo complete 1")
    manager.complete_task(1)
    print("✓ Task 1 marked as complete\n")
    
    print("$ todo list")
    print_tasks(manager)
    
    # Demo: Update
    print("$ todo update 2 \"Study Python & Testing\"")
    manager.update_task(2, "Study Python & Testing", "Learn argparse and pytest")
    print("✓ Task 2 updated\n")
    
    print("$ todo list")
    print_tasks(manager)
    
    # Demo: Delete
    print("$ todo delete 3")
    manager.delete_task(3)
    print("✓ Task 3 deleted\n")
    
    print("$ todo list")
    print_tasks(manager)
    
    # Demo: Help
    print_header("Command Help")
    print("$ todo --help")
    print("""
Usage: todo <command> [arguments]

Commands:
  add <title> [-d DESCRIPTION]     Add a new task
  list                             List all tasks
  update <id> <title> [-d DESC]   Update a task
  delete <id>                      Delete a task
  complete <id>                    Mark task as complete
  --help, -h                       Show this help
    """)
    
    print_header("Summary")
    print("✅ All commands demonstrated:")
    print("   • todo add \"Task title\"             → Add a task")
    print("   • todo add \"Task\" -d \"Description\" → Add with description")
    print("   • todo list                         → Show all tasks")
    print("   • todo complete 1                   → Mark as complete")
    print("   • todo update 1 \"New title\"        → Update a task")
    print("   • todo delete 1                     → Delete a task")
    print("   • todo --help                       → Show help")
    print("\n✨ Use these exact same commands in Command Prompt/PowerShell!")
    print("\n   Example:")
    print("   cd C:\\locale files D\\Q5\\ToDo_Cli1\\project")
    print("   todo add \"My first task\"")
    print("   todo list")
    print("   todo complete 1\n")


if __name__ == "__main__":
    main()
