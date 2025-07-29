import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), '../data/todo_list.json')

def read_task():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE) as file:
        return json.load(file)

def write_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file, indent=2)

