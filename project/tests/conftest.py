"""Conftest for pytest - shared fixtures and configuration."""

import pytest
from src.todo.task_manager import TaskManager


@pytest.fixture
def task_manager():
    """Provide a fresh TaskManager instance for each test."""
    return TaskManager()
