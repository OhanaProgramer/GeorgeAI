# core/display.py

from pathlib import Path
import json
from datetime import datetime
from collections import defaultdict
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme

# Theme and console setup
custom_theme = Theme({
    "complete": "green",
    "incomplete": "white",
    "category": "bold cyan",
    "title": "bold yellow"
})
console = Console(theme=custom_theme)

def display_tasks_for_today():
    """
    Loads and displays today's task list grouped by category with index numbers.
    Returns a flat indexed list of tasks with metadata for interaction.
    """
    today_str = datetime.today().strftime("%Y_%m_%d")
    base_path = Path(__file__).resolve().parent.parent
    task_file = base_path / "tasks" / f"{today_str}_task.json"
 

    if not task_file.exists():
        console.print(f"No task file found for today: {task_file}", style="bold red")
        return

    # Load task data
    with open(task_file, "r") as f:
        tasks = json.load(f)

    # Group by category
    grouped_tasks = defaultdict(list)
    for task in tasks:
        grouped_tasks[task.get("category", "Uncategorized")].append(task)

    # Display title
    console.print(Panel.fit(f"\U0001F4C5 Tasks for {today_str.replace('_', '-')}", style="title"))

    flat_index = 1
    indexed_task_list = []

    for category, task_list in grouped_tasks.items():
        console.print(f"\n[{category}]", style="category")
        for task in task_list:
            checkbox = "[x]" if task.get("completed") else "[ ]"
            style = "complete" if task.get("completed") else "incomplete"
            console.print(f"[{flat_index}] {checkbox} {task['task']}", style=style)
            indexed_task_list.append({
                "index": flat_index,
                "task": task,
                "category": category
            })
            flat_index += 1

    return indexed_task_list

if __name__ == "__main__":
    display_tasks_for_today()
