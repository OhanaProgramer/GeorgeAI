# utils/helper.py

import datetime
import importlib

theme_map = {
    "Sunday": ("Morality Sunday", "morality"),
    "Monday": ("Science Monday", "science"),
    "Tuesday": ("Mental Focus Tuesday", "mental_focus"),
    "Wednesday": ("Unity Dev Wednesday", "unity"),
    "Thursday": ("Financial Thursday", "financial"),
    "Friday": ("Relationship Friday", "relationship"),
    "Saturday": ("Deep Dive Saturday", "deep_dive"),
}

def get_today_theme():
    weekday = datetime.date.today().strftime("%A")
    return theme_map.get(weekday, ("General Inquiry", "general"))

def load_daily_prompt(module_name):
    try:
        mod = importlib.import_module(f"prompts.{module_name}")
        return mod.get_prompt()
    except Exception:
        return "What would you like to reflect on today?"
