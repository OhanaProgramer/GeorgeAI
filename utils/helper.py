# utils/helper.py

from datetime import date
from datetime import datetime
import importlib
from pathlib import Path


 # -------- Data structures --------
# This is a mapping of the days of the week to their respective themes and module names.
theme_map = {
    "Sunday": ("Morality Sunday", "morality"),
    "Monday": ("Science Monday", "science"),
    "Tuesday": ("Mental Focus Tuesday", "mental_focus"),
    "Wednesday": ("Unity Dev Wednesday", "unity"),
    "Thursday": ("Financial Thursday", "financial"),
    "Friday": ("Relationship Friday", "relationship"),
    "Saturday": ("Deep Dive Saturday", "deep_dive"),
}

def get_sod_file_path():
    today_str = datetime.today().strftime("%Y_%m_%d")
    base_path = Path(__file__).resolve().parent.parent
    sod_file = base_path / "reflections" / f"{today_str}_SOD.md"
    return sod_file

def get_today_theme():
    weekday = date.today().strftime("%A")
    return theme_map.get(weekday, ("General Inquiry", "general"))

def load_daily_prompt(module_name):
    try:
        mod = importlib.import_module(f"prompts.{module_name}")
        return mod.get_prompt()
    except Exception:
        return "What would you like to reflect on today?"

def get_active_modules():
    path = get_sod_file_path()
    if not path.exists():
        print(f"SOD file not found: {path}")
        return []

    active = []
    in_module_section = False

    with open(path, "r") as file:
        for line in file:
            line = line.strip()

            # Step 1: Locate the module section
            if line.startswith("## 🧩 Focus Modules"):
                in_module_section = True
                continue

            # Step 2: Exit section if we hit a new header or empty
            if in_module_section and (line.startswith("## ") or line == ""):
                break

            # Step 3: Parse active modules
            if in_module_section and line.startswith("- [x]"):
                module = line.replace("- [x]", "").strip()
                active.append(module)

    return active

if __name__ == "__main__":
    modules = get_active_modules()
    print("Active modules today:", modules)
