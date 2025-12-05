import sys
from typing import Optional
from ..services.task_service import TaskService
from ..models.task import TaskStatus
from . import display

def cmd_add(service: TaskService, title: str, description: Optional[str]):
    """Handle add command."""
    try:
        task = service.add_task(title, description)
        display.print_success(f"Task added successfully! (ID: {task.id})")
        display.print_tasks([task])
    except ValueError as e:
        display.print_error(str(e))
        sys.exit(1)

def cmd_list(service: TaskService):
    """Handle list command."""
    tasks = service.list_tasks()
    display.print_tasks(tasks)

def cmd_update(service: TaskService, task_id: int, title: Optional[str], description: Optional[str]):
    """Handle update command."""
    try:
        task = service.update_task(task_id, title, description)
        display.print_success(f"Task {task.id} updated successfully!")
        display.print_tasks([task])
    except ValueError as e:
        display.print_error(str(e))
        sys.exit(1)

def cmd_delete(service: TaskService, task_id: int):
    """Handle delete command."""
    try:
        service.delete_task(task_id)
        display.print_success(f"Task {task_id} deleted successfully!")
    except ValueError as e:
        display.print_error(str(e))
        sys.exit(1)

def cmd_complete(service: TaskService, task_id: int):
    """Handle complete command."""
    try:
        task = service.complete_task(task_id)
        display.print_success(f"Task {task.id} marked as complete!")
        display.print_tasks([task])
    except ValueError as e:
        display.print_error(str(e))
        sys.exit(1)

def cmd_search(service: TaskService, keyword: str):
    """Handle search command."""
    tasks = service.search_tasks(keyword)
    if tasks:
        display.print_success(f"Found {len(tasks)} tasks matching '{keyword}':")
        display.print_tasks(tasks)
    else:
        print(f"No tasks found matching '{keyword}'.")

def cmd_filter(service: TaskService, status: str):
    """Handle filter command."""
    try:
        task_status = TaskStatus(status.lower())
        tasks = service.list_tasks(status=task_status)
        display.print_success(f"Tasks with status '{status}':")
        display.print_tasks(tasks)
    except ValueError:
        display.print_error(f"Invalid status: {status}. Must be 'pending' or 'completed'")
        sys.exit(1)

def cmd_clear(service: TaskService):
    """Handle clear command."""
    count = service.clear_completed()
    if count > 0:
        display.print_success(f"Cleared {count} completed tasks.")
    else:
        print("No completed tasks to clear.")
