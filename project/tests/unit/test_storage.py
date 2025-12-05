import pytest
import os
import json
from src.storage.json_storage import JsonStorage
from src.models.task import Task

@pytest.fixture
def temp_storage_file(tmp_path):
    file = tmp_path / "test_tasks.json"
    return str(file)

def test_load_empty_storage(temp_storage_file):
    storage = JsonStorage(temp_storage_file)
    tasks = storage.load_tasks()
    assert tasks == []

def test_save_and_load_tasks(temp_storage_file):
    storage = JsonStorage(temp_storage_file)
    task = Task(id=1, title="Test Task")
    storage.save_tasks([task])
    
    loaded_tasks = storage.load_tasks()
    assert len(loaded_tasks) == 1
    assert loaded_tasks[0].id == 1
    assert loaded_tasks[0].title == "Test Task"

def test_load_invalid_json(temp_storage_file):
    with open(temp_storage_file, 'w') as f:
        f.write("invalid json")
    
    storage = JsonStorage(temp_storage_file)
    tasks = storage.load_tasks()
    # Should handle error gracefully and return empty list
    assert tasks == []
