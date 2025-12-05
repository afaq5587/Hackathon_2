import sys
from typing import Optional
from ..services.task_service import TaskService
from ..models.task import TaskStatus
from . import commands
from . import display

def get_input(prompt: str, required: bool = True) -> Optional[str]:
    """Helper to get input with optional validation."""
    while True:
        value = input(prompt).strip()
        if not value and required:
            display.print_error("Input cannot be empty.")
            continue
        return value if value else None

def get_int_input(prompt: str) -> Optional[int]:
    """Helper to get integer input."""
    while True:
        value = input(prompt).strip()
        if not value: return None
        try:
            return int(value)
        except ValueError:
            display.print_error("Please enter a valid number.")

def handle_add(service: TaskService):
    display.print_welcome()
    print("--- Add New Task ---")
    title = get_input("Title: ")
    description = get_input("Description (optional): ", required=False)
    commands.cmd_add(service, title, description)
    input("\nPress Enter to continue...")

def handle_update(service: TaskService):
    commands.cmd_list(service)
    print("\n--- Update Task ---")
    task_id = get_int_input("Enter Task ID to update: ")
    if not task_id: return
    
    title = get_input("New Title (press Enter to keep current): ", required=False)
    description = get_input("New Description (press Enter to keep current): ", required=False)
    
    if not title and not description:
        display.print_error("No changes provided.")
    else:
        commands.cmd_update(service, task_id, title, description)
    input("\nPress Enter to continue...")

def handle_delete(service: TaskService):
    commands.cmd_list(service)
    print("\n--- Delete Task ---")
    task_id = get_int_input("Enter Task ID to delete: ")
    if task_id:
        commands.cmd_delete(service, task_id)
        input("\nPress Enter to continue...")

def handle_complete(service: TaskService):
    commands.cmd_list(service)
    print("\n--- Complete Task ---")
    task_id = get_int_input("Enter Task ID to mark complete: ")
    if task_id:
        commands.cmd_complete(service, task_id)
        input("\nPress Enter to continue...")

def handle_search(service: TaskService):
    keyword = get_input("\nEnter keyword search: ")
    commands.cmd_search(service, keyword)
    input("\nPress Enter to continue...")

def handle_filter(service: TaskService):
    print("\n1. Pending")
    print("2. Completed")
    choice = get_input("Select status (1/2): ")
    
    status = "pending" if choice == "1" else "completed" if choice == "2" else None
    if status:
        commands.cmd_filter(service, status)
    else:
        display.print_error("Invalid selection")
    input("\nPress Enter to continue...")

def interactive_loop(service: TaskService):
    while True:
        display.print_welcome()
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Update Task")
        print("4. Complete Task")
        print("5. Delete Task")
        print("6. Search")
        print("7. Filter by Status")
        print("8. Clear Completed")
        print("9. Exit")
        
        choice = input("\nSelect an option (1-9): ").strip()
        
        if choice == "1":
            handle_add(service)
        elif choice == "2":
            commands.cmd_list(service)
            input("\nPress Enter to continue...")
        elif choice == "3":
            handle_update(service)
        elif choice == "4":
            handle_complete(service)
        elif choice == "5":
            handle_delete(service)
        elif choice == "6":
            handle_search(service)
        elif choice == "7":
            handle_filter(service)
        elif choice == "8":
            commands.cmd_clear(service)
            input("\nPress Enter to continue...")
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            display.print_error("Invalid option")
