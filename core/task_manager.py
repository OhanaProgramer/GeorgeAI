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

def save_tasks(task_list):
    """
    Saves the user's task list to a JSON file for today's date.
    """
    filename = get_today_filename()
    with open(filename, "w") as f:
        json.dump(task_list, f, indent=2)
    print(f"\n✅ Tasks saved to {filename}")

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
