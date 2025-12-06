import shutil
import sys
from typing import List
from ..models.task import Task

# Try to import colorama and tabulate, fallback if not present
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class Fore:
        GREEN = ""
        YELLOW = ""
        RED = ""
        BLUE = ""
        CYAN = ""
        RESET = ""
    class Style:
        BRIGHT = ""
        RESET_ALL = ""

try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False

def print_success(message: str):
    prefix = "✓"
    try:
        prefix.encode(sys.stdout.encoding)
    except (UnicodeEncodeError, AttributeError):
        prefix = "[OK]"

    if HAS_COLOR:
        print(f"{Fore.GREEN}{prefix} {message}{Style.RESET_ALL}")
    else:
        print(f"{prefix} {message}")

def print_error(message: str):
    prefix = "✗"
    try:
        prefix.encode(sys.stdout.encoding)
    except (UnicodeEncodeError, AttributeError):
        prefix = "[ERR]"

    if HAS_COLOR:
        print(f"{Fore.RED}{prefix} {message}{Style.RESET_ALL}")
    else:
        print(f"{prefix} {message}")

def print_tasks(tasks: List[Task]):
    if not tasks:
        print("No tasks found.")
        return

    if HAS_TABULATE:
        headers = ["ID", "Status", "Title", "Created At"]
        table_data = []
        for task in tasks:
            status_color = Fore.GREEN if task.status == "completed" else Fore.YELLOW
            status_symbol = "✓" if task.status == "completed" else "○"
            
            # Format title with description if exists
            title = task.title
            if task.description:
                title += f"\n  └─ {task.description}"
            
            row = [
                task.id,
                f"{status_color}{status_symbol} {task.status.value}{Fore.RESET}",
                title,
                task.created_at.strftime("%Y-%m-%d %H:%M")
            ]
            table_data.append(row)
        
        print(tabulate(table_data, headers, tablefmt="simple"))
    else:
        # Fallback simple print
        print(f"{'ID':<5} {'Status':<12} {'Title'}")
        print("-" * 50)
        for task in tasks:
            status = "✓ DONE" if task.status == "completed" else "○ TODO"
            print(f"{task.id:<5} {status:<12} {task.title}")
            if task.description:
                print(f"       └─ {task.description}")

def print_welcome():
    title = "ToDo CLI - PRO Edition"
    width = shutil.get_terminal_size().columns
    print("=" * width)
    print(title.center(width))
    print("=" * width)
