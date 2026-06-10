import json
import uuid
from pathlib import Path

Path("tasks.json").touch(exist_ok=True)

def list_tasks():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
    print(json.dumps(tasks, indent=4))

def add(task):
    id = uuid.uuid4()
    is_done = False
    new_task = {
        "ID": str(id),
        "Task": task,
        "is_done": is_done
    }
    with open('tasks.json', 'r') as file:
        existing_tasks = json.load(file)
        if not isinstance(existing_tasks, list):
            existing_tasks = [existing_tasks]
    existing_tasks.append(new_task)
    with open("tasks.json", 'w') as file:
        json.dump(existing_tasks, file, indent=4)
    print("New Task has been added! do list() to view all you tasks.")
