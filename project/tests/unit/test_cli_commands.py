import pytest
from src.services.task_service import TaskService
from src.storage.json_storage import JsonStorage
from src.models.task import TaskStatus

class MockStorage(JsonStorage):
    def __init__(self):
        self.data = []
    def load_tasks(self):
        return self.data
    def save_tasks(self, tasks):
        self.data = tasks

@pytest.fixture
def service():
    return TaskService(MockStorage())

def test_search_tasks(service):
    service.add_task("Buy Milk")
    service.add_task("Buy Eggs")
    service.add_task("Walk Dog")
    
    results = service.search_tasks("Buy")
    assert len(results) == 2
    
    results = service.search_tasks("Dog")
    assert len(results) == 1
    assert results[0].title == "Walk Dog"

def test_filter_tasks(service):
    t1 = service.add_task("Task 1")
    t2 = service.add_task("Task 2")
    service.complete_task(t1.id)
    
    completed = service.list_tasks(status=TaskStatus.COMPLETED)
    assert len(completed) == 1
    assert completed[0].id == t1.id
    
    pending = service.list_tasks(status=TaskStatus.PENDING)
    assert len(pending) == 1
    assert pending[0].id == t2.id

def test_clear_completed(service):
    t1 = service.add_task("Task 1")
    service.add_task("Task 2")
    service.complete_task(t1.id)
    
    count = service.clear_completed()
    assert count == 1
    assert len(service.list_tasks()) == 1
