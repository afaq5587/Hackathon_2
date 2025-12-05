# ToDo CLI Application

A simple command-line task management application built with Python.

## Features

- ✓ Add new tasks with optional descriptions
- ✓ List all tasks with completion status
- ✓ Update existing tasks
- ✓ Delete tasks
- ✓ Mark tasks as complete
- ✓ View task statistics
- ✓ Error handling with clear messages

## Project Structure

```
src/
├── todo/
│   ├── __init__.py          # Package initialization
│   ├── task.py              # Task model
│   └── task_manager.py      # TaskManager class
└── todo.py                  # Main CLI entry point

tests/
├── test_task.py             # Unit tests for Task class
└── test_task_manager.py     # Unit tests for TaskManager class

README.md                     # This file
pyproject.toml              # Project configuration
```

## Installation

1. Ensure you have Python 3.7+ installed:

   ```bash
   python --version
   ```

2. Install test dependencies (optional):
   ```bash
   pip install pytest
   ```

## Usage

### Add a Task

```bash
python src/todo.py add "Buy groceries"
python src/todo.py add "Study Python" -d "Learn argparse and unittest"
```

### List All Tasks

```bash
python src/todo.py list
```

Output example:

```
Tasks (3 total):
----------------------------------------------------------------------
○ TODO   [  1] Buy groceries
✓ DONE   [  2] Study Python
         └─ Learn argparse and unittest
○ TODO   [  3] Clean room
----------------------------------------------------------------------
Total: 3 | Completed: 1 | Pending: 2
```

### Update a Task

```bash
python src/todo.py update 1 "Buy groceries and cook dinner"
python src/todo.py update 1 "Buy groceries" -d "Milk, bread, eggs"
```

### Delete a Task

```bash
python src/todo.py delete 1
```

### Mark a Task as Complete

```bash
python src/todo.py complete 1
```

### View Help

```bash
python src/todo.py --help
python src/todo.py add --help
python src/todo.py list --help
```

## Running Tests

Run all tests with pytest:

```bash
pytest tests/
```

Run specific test file:

```bash
pytest tests/test_task.py
pytest tests/test_task_manager.py
```

Run with verbose output:

```bash
pytest tests/ -v
```

Run with coverage:

```bash
pytest tests/ --cov=src
```

## Data Model

### Task

A Task represents a single to-do item with the following attributes:

- **id** (int): Unique identifier for the task
- **title** (str): The task title (required)
- **description** (str): Optional description of the task
- **completed** (bool): Whether the task is marked as complete
- **created_at** (str): ISO timestamp of when the task was created

## Implementation Details

### Storage

Tasks are stored in-memory using a Python dictionary for O(1) lookups by ID.

### Command-Line Interface

The CLI uses Python's built-in `argparse` module for command-line argument parsing, providing:

- Clear help messages
- Automatic usage documentation
- Type validation for arguments

### Error Handling

All operations include proper error handling with:

- Meaningful error messages to stderr
- Non-zero exit codes on errors
- Validation of inputs (e.g., non-empty titles, valid IDs)

## Examples

### Basic Workflow

```bash
# Create some tasks
python src/todo.py add "Morning exercise"
python src/todo.py add "Finish project" -d "Complete by Friday"
python src/todo.py add "Buy groceries"

# View all tasks
python src/todo.py list

# Complete a task
python src/todo.py complete 1

# Update a task
python src/todo.py update 2 "Finish project" -d "Complete by Saturday"

# View updated list
python src/todo.py list

# Delete a task
python src/todo.py delete 3

# Final view
python src/todo.py list
```

## Performance

All operations run in under 2 seconds, meeting the performance requirement for this simple CLI application.

## Testing Strategy

The project includes comprehensive unit tests covering:

- Task creation and validation
- Task management operations (add, list, update, delete, complete)
- Error handling and edge cases
- Task statistics

Tests use pytest framework for clarity and features like fixtures and parametrization.

## Future Enhancements

- Persistent storage (JSON, SQLite)
- Task priority levels
- Due dates and reminders
- Task filtering by status/date
- Bulk operations
- Configuration file support
- Database backend

## License

This project is part of the ToDo CLI training exercise.
