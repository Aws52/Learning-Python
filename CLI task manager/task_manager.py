import json
import uuid
from pathlib import Path
import sys

tasks_file = Path("tasks.json")

if not tasks_file.exists() or tasks_file.stat().st_size == 0:
    with open(tasks_file, "w") as file:
        json.dump([], file)

def list_tasks(status=None):
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
    if status is not None:
        tasks = [task for task in tasks if task.get("is_done") == status]
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
    print("New Task has been added! do list to view all you tasks.")

def delete(id):
    with open("tasks.json", "r") as file:
        existing_tasks = json.load(file)
    for i in range(len(existing_tasks)):
        if(existing_tasks[i]["ID"] == str(id)):
            del existing_tasks[i]
            with open("tasks.json", 'w') as file:
                json.dump(existing_tasks, file, indent=4)
            print("The task has been deleted! do list to view all you tasks.")
            break
    else:
        print(
            "No such task ID. Please insert a correct one, do list to view all you tasks."
        )

def done(id):
    with open("tasks.json", "r") as file:
        existing_tasks = json.load(file)
    for i in range(len(existing_tasks)):
        if existing_tasks[i]["ID"] == str(id):
            existing_tasks[i]["is_done"] = True
            with open("tasks.json", "w") as file:
                json.dump(existing_tasks, file, indent=4)
            print("The task has been marked (Done)")
            break
    else:
        print(
            "No such task ID. Please insert a correct one, do list to view all you tasks."
        )

arguments = sys.argv[1:]

if len(arguments) >= 1:
    match arguments:
        case ["list"]:
            list_tasks()
        case ["list", status_value]:
            if status_value == "true":
                list_tasks(status=True)
            else:
                list_tasks(status=False)
        case ["add", task_text]:
            add(task=task_text)
        case ["delete", task_id]:
            delete(id=task_id)
        case ["done", task_id]:
            done(id=task_id)
        case _:
            print("""Command is not recognised. Use one of the following:
                        list (true or false for "is_done" field, leave empty for the full list)
                        add "task goes here",
                        delete task_id
                        done task_id""")
