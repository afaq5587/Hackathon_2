import argparse
import sys
from ..storage.json_storage import JsonStorage
from ..services.task_service import TaskService
from . import commands
from . import display

def main():
    """Main entry point for the CLI application."""
    storage = JsonStorage()
    service = TaskService(storage)

    parser = argparse.ArgumentParser(
        description="ToDo CLI - Intermediate Edition",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  todo add "Buy groceries" -d "Milk, Eggs"
  todo list
  todo complete 1
  todo search "groceries"
  todo filter completed
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("title", help="Task title")
    parser_add.add_argument("-d", "--description", help="Task description")
    
    # List
    parser_list = subparsers.add_parser("list", help="List all tasks")
    
    # Update
    parser_update = subparsers.add_parser("update", help="Update a task")
    parser_update.add_argument("id", type=int, help="Task ID")
    parser_update.add_argument("--title", help="New title")
    parser_update.add_argument("-d", "--description", help="New description")
    
    # Delete
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID")
    
    # Complete
    parser_complete = subparsers.add_parser("complete", help="Complete a task")
    parser_complete.add_argument("id", type=int, help="Task ID")
    
    # Search
    parser_search = subparsers.add_parser("search", help="Search tasks")
    parser_search.add_argument("keyword", help="Keyword to search for")
    
    # Filter
    parser_filter = subparsers.add_parser("filter", help="Filter tasks by status")
    parser_filter.add_argument("status", choices=["pending", "completed"], help="Status to filter by")
    
    # Clear
    parser_clear = subparsers.add_parser("clear", help="Clear all completed tasks")
    
    args = parser.parse_args()
    
    if not args.command:
        # If no arguments, start interactive mode
        from . import interactive
        interactive.interactive_loop(service)
        sys.exit(0)
        
    try:
        if args.command == "add":
            commands.cmd_add(service, args.title, args.description)
        elif args.command == "list":
            commands.cmd_list(service)
        elif args.command == "update":
            # Validation for update: needs at least one field
            if not args.title and not args.description:
                display.print_error("Please provide --title or --description to update")
                sys.exit(1)
            commands.cmd_update(service, args.id, args.title, args.description)
        elif args.command == "delete":
            commands.cmd_delete(service, args.id)
        elif args.command == "complete":
            commands.cmd_complete(service, args.id)
        elif args.command == "search":
            commands.cmd_search(service, args.keyword)
        elif args.command == "filter":
            commands.cmd_filter(service, args.status)
        elif args.command == "clear":
            commands.cmd_clear(service)
            
    except Exception as e:
        display.print_error(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
