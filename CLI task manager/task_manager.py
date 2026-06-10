import json
from pathlib import Path

Path("tasks.json").touch(exist_ok=True)

def list():
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
    print(json.dumps)