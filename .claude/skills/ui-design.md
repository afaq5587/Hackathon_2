# Skills: Creating Beautiful CLI UIs

This document outlines the patterns and libraries used to create professional command-line interfaces, specifically using the `rich` library.

## 1. Core Library: `rich`

The `rich` library is the industry standard for Python terminal UIs. It replaces standard `print()` with a powerful `Console` object.

```python
from rich.console import Console
console = Console()
```

## 2. Key Visual Components

### Banners and Headers
Use `rich.panel.Panel` combined with styled `Text` to create impressive headers.
*   **Technique**: Wrap styled text in a Panel with a double box style.
*   **Example**:
    ```python
    from rich.panel import Panel
    from rich.text import Text
    from rich import box

    text = Text("Application Name", style="bold magenta")
    panel = Panel(text, box=box.DOUBLE, style="magenta", expand=False)
    console.print(panel)
    ```

### Styled Tables
Replace plain text lists with `rich.table.Table`.
*   **Features**: Automatic column sizing, colored borders, headers.
*   **Best Practice**: Use `box.ROUNDED` for a modern look.
*   **Example**:
    ```python
    from rich.table import Table
    
    table = Table(title="Tasks", box=box.ROUNDED)
    table.add_column("ID", style="dim")
    table.add_column("Status", style="green")
    table.add_row("1", "Active")
    console.print(table)
    ```

### Semantic Color Coding
Use colors to convey meaning, not just for decoration.
*   **Success**: `[bold green]✔ Success[/]`
*   **Error**: `[bold red]✘ Error[/]`
*   **Info**: `[blue]ℹ Info[/]`
*   **Pending/Warning**: `[yellow]`

### Interactive Menus
For interactive loops, present options in a styled `Panel` rather than a plain list.
*   **Layout**: `Key`. `Description`
*   **Visuals**: Use a border to group options together.

## 3. User Experience (UX) Principles

*   **Consistency**: Use the same color for the same status across the app (e.g., "completed" is always green).
*   **Feedback**: Always provide immediate visual feedback (success message or updated table) after an action.
*   **Clarity**: Don't clutter the screen. Use spacing (padding) effectively.
*   **Notifications**: For long-running apps or background awareness, integrate desktop notifications (e.g., `plyer`) to re-engage the user.
