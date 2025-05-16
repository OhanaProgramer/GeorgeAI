from pathlib import Path
# core/task_manager.py

import os
import json
from datetime import datetime

# Path to store task files, each named by date
TASK_DIR = "tasks"

def init_task_folder():
    """
    Creates the tasks/ folder if it doesn't exist.
    Keeps task files organized by date.
    """
    if not os.path.exists(TASK_DIR):
        os.makedirs(TASK_DIR)

def get_today_filename():
    """
    Builds the full path for today's task file.
    Format: tasks/YYYY-MM-DD.json
    """
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(TASK_DIR, f"{today}.json")

def prompt_for_tasks():
    """
    Prompts the user to input up to 3 tasks for the day.
    Returns a list of task dicts, each with a 'task' and 'completed' flag.
    """
    print("🗒️ Let's plan your top 3 tasks for today.\n")
    tasks = []
    for i in range(1, 4):
        task = input(f"Task {i}: ").strip()
        if task:
            tasks.append({"task": task, "completed": False})
    return tasks

def load_today_tasks():
    """
    Loads today's task list from file, if it exists.
    Returns a list of task dictionaries.
    """
    try:
        filename = get_today_filename()
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_or_create_task_file(date_str=None):
    if not date_str:
        date_str = datetime.today().strftime("%Y_%m_%d")
    task_path = Path(__file__).resolve().parent.parent / "tasks" / f"{date_str}_task.json"
    if task_path.exists():
        with open(task_path, "r") as f:
            return json.load(f)
    else:
        return []

def save_tasks(tasks, date_str=None):
    if date_str is None:
        # Save to today's file using original format
        filename = get_today_filename()
        with open(filename, "w") as f:
            json.dump(tasks, f, indent=2)
        print(f"\n✅ Tasks saved to {filename}")
    else:
        # Save to specified date file using alternative format
        task_path = Path(__file__).resolve().parent.parent / "tasks" / f"{date_str}_task.json"
        with open(task_path, "w") as f:
            json.dump(tasks, f, indent=2)

__all__ = [
    "init_task_folder",
    "get_today_filename",
    "prompt_for_tasks",
    "save_tasks",
    "load_today_tasks",
    "load_or_create_task_file"
]
