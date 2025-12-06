# ToDo CLI Application (PRO Edition)

A robust command-line task management application built with Python, featuring persistent storage, rich output, and advanced management commands.

## Features

- **Persistence**: Tasks are saved to `tasks.json` and persist between runs.
- **Rich Display**: Colored output and table formatting (via `colorama` and `tabulate`).
- **Advanced Commands**:
  - `search`: Find tasks by keyword.
  - `filter`: View tasks by status (pending/completed).
  - `clear`: Remove all completed tasks at once.
- **Robust Model**: Clean separation of concerns with `models`, `storage`, and `services`.

## Project Structure

```
src/
├── models/          # Data classes (Task, TaskStatus)
├── storage/         # Persistence layer (JsonStorage)
├── services/        # Business logic (TaskService)
└── cli/             # Interface layer (Commands, Display, Main)
tests/               # Unit tests
```

## Installation

1. **Install Dependencies**:
   ```bash
   pip install .
   ```
   *Or for development/testing:*
   ```bash
   pip install -e .[test]
   ```

2. **Run the Application**:
   If installed:
   ```bash
   todo --help
   ```
   
   Or directly via Python:
   ```bash
   python -m src.cli.main --help
   ```

## Usage Examples

### Basic Operations

```bash
# Add tasks
todo add "Buy groceries" -d "Milk, Eggs, Bread"
todo add "Walk the dog"

# List all tasks
todo list

# Complete a task
todo complete 1

# Delete a task
todo delete 2
```

### Advanced Operations

```bash
# Search for tasks
todo search "groceries"

# Filter by status
todo filter pending
todo filter completed

# Update a task
todo update 1 --title "Buy healthy groceries" -d "Fruits, Veggies"

# Clear all completed tasks
todo clear
```

## Running Tests

Run the full test suite with:

```bash
pytest
```
