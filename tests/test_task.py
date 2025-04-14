# tests/test_task.py

from src.task import Task
from src.utils import sort_tasks

def test_task_to_dict_and_from_dict():
    task = Task(1, "Test Task", "2025-05-01", "High", False, tag="school")
    task_dict = task.to_dict()
    new_task = Task.from_dict(task_dict)
    
    assert new_task.id == task.id
    assert new_task.title == task.title
    assert new_task.due_date == task.due_date
    assert new_task.priority == task.priority
    assert new_task.completed == task.completed
    assert new_task.tag == task.tag

def test_task_str_output():
    task = Task(1, "Test CLI", "2023-01-01", "Critical")
    out = str(task)
    assert "[ ]" in out
    assert "Test CLI" in out
    assert "Critical" in out

def test_priority_sorting():
    tasks = [
        Task(1, "Low priority", priority="Low"),
        Task(2, "High priority", priority="High"),
        Task(3, "Critical priority", priority="Critical")
    ]
    sorted_tasks = sort_tasks(tasks, by="priority")
    assert sorted_tasks[0].priority == "Critical"
    assert sorted_tasks[1].priority == "High"
    assert sorted_tasks[2].priority == "Low"
