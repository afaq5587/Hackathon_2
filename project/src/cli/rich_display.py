from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from rich import box
import datetime

console = Console()

def print_banner():
    """Prints a beautiful banner for the application."""
    banner_text = Text("ToDo CLI", style="bold magenta", justify="center")
    subtitle = Text("PRO Edition", style="italic cyan", justify="center")
    
    panel = Panel(
        Text.assemble(banner_text, "\n", subtitle),
        box=box.DOUBLE,
        style="magenta",
        expand=False
    )
    console.print(panel, justify="center")
    console.print()

def print_tasks(tasks):
    """Prints a list of tasks in a rich table."""
    if not tasks:
        console.print("[italic yellow]No tasks found.[/italic yellow]")
        return

    table = Table(title="Your Tasks", box=box.ROUNDED, show_header=True, header_style="bold cyan")

    table.add_column("ID", style="dim", width=4, justify="right")
    table.add_column("Title", style="bold white")
    table.add_column("Description", style="white")
    table.add_column("Status", justify="center")
    table.add_column("Created", style="dim", justify="right")

    for task in tasks:
        status_style = "green" if task.status.value == "completed" else "red"
        status_text = f"[{status_style}]{task.status.value}[/{status_style}]"
        
        # Format date if available
        created_at = task.created_at
        if isinstance(created_at, str):
             # Try to parse simple string if needed, or just display
             pass
        elif isinstance(created_at, datetime.datetime):
             created_at = created_at.strftime("%Y-%m-%d %H:%M")

        table.add_row(
            str(task.id),
            task.title,
            task.description or "",
            status_text,
            str(created_at)
        )

    console.print(table)
    console.print()

def print_success(message):
    """Prints a success message."""
    console.print(f"[bold green]✔ {message}[/bold green]")

def print_welcome():
    """Prints the welcome banner."""
    print_banner()

def print_error(message):
    """Prints an error message."""
    console.print(f"[bold red]✘ {message}[/bold red]")

def print_info(message):
    """Prints an info message."""
    console.print(f"[blue]ℹ {message}[/blue]")

def print_menu(options):
    """Prints a menu of options."""
    menu_text = Text()
    for key, value in options.items():
        menu_text.append(f"{key}. ", style="bold cyan")
        menu_text.append(f"{value}\n", style="white")
    
    panel = Panel(
        menu_text,
        title="Menu",
        box=box.ROUNDED,
        border_style="blue",
        expand=False
    )
    console.print(panel)

