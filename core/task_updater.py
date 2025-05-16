from pathlib import Path
from datetime import datetime
import json

def update_task_completion(indices_to_check):
    today_str = datetime.today().strftime("%Y_%m_%d")
    task_file = Path(__file__).resolve().parent.parent / "tasks" / f"{today_str}_task.json"

    if not task_file.exists():
        print(f"❌ Task file not found: {task_file}")
        return []

    with open(task_file, "r") as f:
        tasks = json.load(f)

    updated_indices = []
    for idx in indices_to_check:
        adjusted_index = idx - 1
        if 0 <= adjusted_index < len(tasks):
            if tasks[adjusted_index].get("completed", False):
                print(f"✅ Task {idx} is already marked complete.")
            else:
                tasks[adjusted_index]["completed"] = True
                print(f"✅ Task {idx} now marked complete.")
                updated_indices.append(idx)

    with open(task_file, "w") as f:
        json.dump(tasks, f, indent=4)

    return updated_indices
