#!/usr/bin/env python3
"""ToDo CLI - A simple command-line task management application.

Main entry point for the ToDo CLI application using argparse for command-line
argument parsing and task management.
"""

import argparse
import sys
import os

# Add src directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from todo.task_manager import TaskManager


# Global task manager instance
task_manager = TaskManager()


def cmd_add(args):
    """Handle 'add' command to add a new task."""
    try:
        task = task_manager.add_task(args.title, args.description)
        print(f"✓ Task added successfully!")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        if task.description:
            print(f"  Description: {task.description}")
        print(f"  Created: {task.created_at}")
    except ValueError as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_list(args):
    """Handle 'list' command to display all tasks."""
    tasks = task_manager.list_tasks()
    
    if not tasks:
        print("No tasks found. Use 'todo add <title>' to create a task.")
        return
    
    print(f"\nTasks ({len(tasks)} total):")
    print("-" * 70)
    
    for task in tasks:
        status = "✓ DONE" if task.completed else "○ TODO"
        print(f"{status:8} [{task.id:3}] {task.title}")
        if task.description:
            print(f"         └─ {task.description}")
    
    print("-" * 70)
    stats = task_manager.get_stats()
    print(f"Total: {stats['total']} | Completed: {stats['completed']} | Pending: {stats['pending']}\n")


def cmd_update(args):
    """Handle 'update' command to update an existing task."""
    try:
        task = task_manager.update_task(args.id, args.title, args.description)
        print(f"✓ Task updated successfully!")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        if task.description:
            print(f"  Description: {task.description}")
    except ValueError as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_delete(args):
    """Handle 'delete' command to delete a task."""
    try:
        task_manager.delete_task(args.id)
        print(f"✓ Task {args.id} deleted successfully!")
    except ValueError as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


def cmd_complete(args):
    """Handle 'complete' command to mark a task as complete."""
    try:
        task = task_manager.complete_task(args.id)
        print(f"✓ Task {task.id} marked as complete!")
        print(f"  Title: {task.title}")
    except ValueError as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


def interactive_menu():
    """Display interactive menu and get user choice."""
    print("\n" + "="*70)
    print("  ToDo CLI - Interactive Menu")
    print("="*70 + "\n")
    print("1. Add a task")
    print("2. List all tasks")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark a task as complete")
    print("6. Exit")
    print("\n" + "-"*70)
    
    choice = input("Enter your choice (1-6): ").strip()
    return choice


def handle_add_interactive():
    """Interactively add a task."""
    title = input("\nEnter task title: ").strip()
    if not title:
        print("✗ Error: Task title cannot be empty")
        return
    
    description = input("Enter task description (optional, press Enter to skip): ").strip()
    
    try:
        task = task_manager.add_task(title, description if description else None)
        print(f"\n✓ Task added successfully!")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        if task.description:
            print(f"  Description: {task.description}")
        print(f"  Created: {task.created_at}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def handle_update_interactive():
    """Interactively update a task."""
    cmd_list(None)
    
    try:
        task_id = int(input("Enter task ID to update: ").strip())
    except ValueError:
        print("✗ Error: Invalid task ID (must be a number)")
        return
    
    if not task_manager.get_task(task_id):
        print(f"✗ Error: Task with ID {task_id} not found")
        return
    
    new_title = input("Enter new task title: ").strip()
    if not new_title:
        print("✗ Error: Task title cannot be empty")
        return
    
    new_description = input("Enter new description (optional, press Enter to skip): ").strip()
    
    try:
        task = task_manager.update_task(task_id, new_title, new_description if new_description else None)
        print(f"\n✓ Task updated successfully!")
        print(f"  ID: {task.id}")
        print(f"  Title: {task.title}")
        if task.description:
            print(f"  Description: {task.description}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def handle_delete_interactive():
    """Interactively delete a task."""
    cmd_list(None)
    
    try:
        task_id = int(input("Enter task ID to delete: ").strip())
    except ValueError:
        print("✗ Error: Invalid task ID (must be a number)")
        return
    
    try:
        task_manager.delete_task(task_id)
        print(f"\n✓ Task {task_id} deleted successfully!")
    except ValueError as e:
        print(f"✗ Error: {e}")


def handle_complete_interactive():
    """Interactively mark a task as complete."""
    cmd_list(None)
    
    try:
        task_id = int(input("Enter task ID to complete: ").strip())
    except ValueError:
        print("✗ Error: Invalid task ID (must be a number)")
        return
    
    try:
        task = task_manager.complete_task(task_id)
        print(f"\n✓ Task {task.id} marked as complete!")
        print(f"  Title: {task.title}")
    except ValueError as e:
        print(f"✗ Error: {e}")


def interactive_mode():
    """Run the CLI in interactive mode."""
    print("\n" + "="*70)
    print("  Welcome to ToDo CLI - Interactive Mode")
    print("="*70)
    print("  Type your commands interactively")
    print("  Type '6' or 'exit' at any time to quit\n")
    
    while True:
        try:
            choice = interactive_menu()
            
            if choice == "1":
                handle_add_interactive()
            elif choice == "2":
                cmd_list(None)
            elif choice == "3":
                handle_update_interactive()
            elif choice == "4":
                handle_delete_interactive()
            elif choice == "5":
                handle_complete_interactive()
            elif choice == "6" or choice.lower() == "exit":
                print("\n✓ Goodbye!\n")
                break
            else:
                print("✗ Invalid choice. Please enter a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\n✓ Goodbye!\n")
            break
        except Exception as e:
            print(f"\n✗ Unexpected error: {e}\n")


def main():
    """Main entry point for the CLI application."""
    # Check if arguments were provided
    if len(sys.argv) > 1:
        # If arguments are provided, use command-line mode
        parser = argparse.ArgumentParser(
            description="A simple command-line task management application",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog="""
Examples:
  todo.py add "Buy groceries"
  todo.py add "Study Python" -d "Learn argparse module"
  todo.py list
  todo.py update 1 "Buy milk"
  todo.py delete 1
  todo.py complete 1
            """,
        )
        
        subparsers = parser.add_subparsers(dest="command", help="Available commands")
        subparsers.required = True
        
        # Add command
        add_parser = subparsers.add_parser("add", help="Add a new task")
        add_parser.add_argument("title", help="Title of the task")
        add_parser.add_argument("-d", "--description", help="Optional description of the task")
        add_parser.set_defaults(func=cmd_add)
        
        # List command
        list_parser = subparsers.add_parser("list", help="List all tasks")
        list_parser.set_defaults(func=cmd_list)
        
        # Update command
        update_parser = subparsers.add_parser("update", help="Update an existing task")
        update_parser.add_argument("id", type=int, help="ID of the task to update")
        update_parser.add_argument("title", help="New title for the task")
        update_parser.add_argument("-d", "--description", help="Optional new description")
        update_parser.set_defaults(func=cmd_update)
        
        # Delete command
        delete_parser = subparsers.add_parser("delete", help="Delete a task")
        delete_parser.add_argument("id", type=int, help="ID of the task to delete")
        delete_parser.set_defaults(func=cmd_delete)
        
        # Complete command
        complete_parser = subparsers.add_parser("complete", help="Mark a task as complete")
        complete_parser.add_argument("id", type=int, help="ID of the task to complete")
        complete_parser.set_defaults(func=cmd_complete)
        
        # Parse arguments
        args = parser.parse_args()
        
        # Execute the command
        try:
            args.func(args)
        except Exception as e:
            print(f"✗ Unexpected error: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # If no arguments, use interactive mode
        try:
            interactive_mode()
        except Exception as e:
            print(f"✗ Unexpected error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
