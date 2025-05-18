def display_sod_entry():
    from utils.george_voice import speak
    try:
        display_sod()
        speak("Here’s your start of day reflection.")
    except FileNotFoundError:
        speak("Start of day file not found. Would you like to create one?")

def display_eod_entry():
    from utils.george_voice import speak
    try:
        display_eod()
        speak("Here’s your end of day summary.")
    except FileNotFoundError:
        speak("End of day file not found. You can write a reflection later if you'd like.")
# george.py
# George AI - Your Daily Companion
# This is a simple AI companion that helps you plan your day, reflect on your tasks,
# and engage in meaningful conversations. It uses OpenAI's GPT-4o model to generate 
# responses based on user input and daily themes. It also manages tasks and reflections
# using a structured approach.  It is designed to be a daily companion that helps
# you stay organized and focused on your goals.


import openai
import os
from datetime import date
from dotenv import load_dotenv
from core.module_log_generator import generate_module_logs
from core.sod_viewer import display_sod
from core.eod_viewer import display_eod
from utils.george_voice import speak_if_summary
from utils.george_voice import speak

# ----- Imports Local ----
from utils.helper import get_today_theme, load_daily_prompt
from core.task_manager import (
    init_task_folder,
    prompt_for_tasks,
    load_or_create_task_file,
    save_tasks
)
from core.display import display_tasks_for_today
from utils.helper import get_active_modules
from core.task_updater import update_task_completion
from core.startup_checks import run_startup_integrity_check
# ----- Constants ----

# Load OpenAI API key
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def display_start_of_day():
    from datetime import date
    from utils.helper import get_today_theme
    from utils.george_voice import speak

    weekday = date.today().strftime("%A")
    theme, _ = get_today_theme()
    speak(f"Good morning, Jacques. It's {weekday}, and today's theme is {theme}. Let's make it count.")
    
    print("\n🌅 Start of Day Summary\n")
    print(f"📅 Today is {weekday}")
    print(f"🎯 Theme: {theme}")
    print("\n📝 Tasks for Today:\n")
    display_tasks_for_today()

def display_intraday_view():
    from utils.george_voice import speak
    speak("Here’s your current progress update.")
    print("\n📍 IntraDay Check-In\n")
    display_tasks_for_today()

def display_end_of_day():
    from utils.george_voice import speak
    speak("Let’s wrap up your day with a final reflection and review.")
    print("\n🌙 End of Day Summary\n")
    display_eod()

def display_task_menu():
    from utils.george_voice import speak
    speak("Here's your task management menu.")
    print("""\
🧩 Task Menu:
1. add – Add a new task
2. edit – Edit an existing task
3. delete – Remove a task
4. check – Mark task(s) complete by number

(Type 'check #' directly, e.g., 'check 1 2')
""")

def main():
    print("🤖 George AI v1 – Your Daily Companion\n")
    speak_if_summary("greeting")
    run_startup_integrity_check()

    # === Morning Setup ===
    weekday = date.today().strftime("%A")
    theme, _ = get_today_theme()
    modules = get_active_modules()

    # Generate module logs
    generated_logs = generate_module_logs()
    if generated_logs:
        print("📄 Created module logs:")
        for log in generated_logs:
            print(" -", log)
    else:
        print("✅ All module logs already exist.")


    print(f"📅 Today is {weekday} – Theme: {theme}")
    print(f"📋 Your active modules: {', '.join(modules)}")

    # Clear screen before launching interactive menu
    os.system("cls" if os.name == "nt" else "clear")


    # === Task Display ===
    print("\n🧠 Loading today's task view...\n")
    display_tasks_for_today()

    # === Menu-first Entry ===
    print("\n🧠 What would you like to do?\n(Type 'menu' to see available options.)\n")

    # === Chat Loop ===
    starter_prompt = load_daily_prompt(modules)
    print(f"🧠 {starter_prompt}\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "ds":
            display_sod_entry()
            continue
        if user_input.strip().lower() == "de":
            display_eod_entry()
            continue
        if user_input.strip().lower() == "s":
            display_start_of_day()
            continue
        if user_input.lower().startswith("check"):
            try:
                indices = list(map(int, user_input.strip().split()[1:]))
                updated = update_task_completion(indices)
                if updated:
                    print(f"✅ Tasks marked complete: {updated}")
                else:
                    print("⚠️ No tasks updated.")
                print("\n🔁 Updated task list:\n")
                display_tasks_for_today()
                continue  # Skip GPT fallback
            except ValueError:
                print("❌ Invalid format. Use: check 1 2 3")
                continue
        if user_input.lower().strip() == "menu":
            print("""\
George Menu:
1. S  - Start of Day (✅ complete)
2. I  - IntraDay     (✅ complete)
3. E  - End of Day   (✅ complete)
4. T  - Task Menu    (✅ complete)
5. DS - Display SOD  (✅ complete)
6. DE - Display EOD  (✅ complete)
7. AI - Ask George   (✅ working)
8. SU - Summarizer   (🟡 planned)
""")
            continue
        if user_input.strip().lower() == "i":
            display_intraday_view()
            continue
        if user_input.strip().lower() == "e":
            display_end_of_day()
            continue
        if user_input.strip().lower() == "t":
            display_task_menu()
            continue

        print("\n📋 Current Tasks:")
        display_tasks_for_today()

        if user_input.strip().lower() == "add":
            new_task = input("Enter the task description: ").strip()
            
            # Show category options
            categories = ["GeorgeAI", "ExoPlanet", "Health", "Email", "Other"]
            print("Choose a category:")
            for idx, cat in enumerate(categories, 1):
                print(f"{idx}. {cat}")
            try:
                cat_choice = int(input("Enter number: ").strip())
                new_category = categories[cat_choice - 1]
            except:
                print("❌ Invalid input. Defaulting to 'Other'")
                new_category = "Other"

            # Priority options
            priority_options = ["low", "medium", "high"]
            print("Choose priority:")
            for idx, p in enumerate(priority_options, 1):
                print(f"{idx}. {p}")
            try:
                p_choice = int(input("Enter number: ").strip())
                priority = priority_options[p_choice - 1]
            except:
                print("❌ Invalid input. Defaulting to 'medium'")
                priority = "medium"

            # Time block options
            time_block_options = ["Morning", "Afternoon", "Evening", "Any"]
            print("Choose time block:")
            for idx, tb in enumerate(time_block_options, 1):
                print(f"{idx}. {tb}")
            try:
                tb_choice = int(input("Enter number: ").strip())
                time_block = time_block_options[tb_choice - 1]
            except:
                print("❌ Invalid input. Defaulting to 'Any'")
                time_block = "Any"

            # Notes
            notes = input("Any notes? ").strip()

            today_str = date.today().strftime("%Y_%m_%d")
            task_file = load_or_create_task_file(today_str)
            task_file.append({
                "task": new_task,
                "category": new_category,
                "completed": False,
                "priority": priority,
                "time_block": time_block,
                "notes": notes,
                "module": new_category
            })
            save_tasks(task_file)
            print(f"✅ Task added: [{new_category}] {new_task} ({priority}, {time_block})")

            print("\n🔁 Updated Tasks:")
            display_tasks_for_today()
            continue
        elif user_input.strip().lower() == "edit":
            today_str = date.today().strftime("%Y_%m_%d")
            task_list = load_or_create_task_file(today_str)
            if not task_list:
                print("⚠️ No tasks found to edit.")
                continue

            print("Which task number would you like to edit?")
            for i, t in enumerate(task_list, 1):
                print(f"[{i}] {t['task']} ({t.get('category', 'Uncategorized')})")

            try:
                choice = int(input("Enter number: ").strip())
                if 1 <= choice <= len(task_list):
                    task = task_list[choice - 1]
                    new_text = input(f"New description (or press Enter to keep: \"{task['task']}\"): ").strip()
                    if new_text:
                        task["task"] = new_text
                    new_notes = input(f"New notes (or press Enter to keep: \"{task.get('notes', '')}\"): ").strip()
                    if new_notes:
                        task["notes"] = new_notes
                    save_tasks(task_list)
                    print("✅ Task updated.")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Invalid input.")
            continue
        elif user_input.strip().lower() == "delete":
            today_str = date.today().strftime("%Y_%m_%d")
            task_list = load_or_create_task_file(today_str)
            if not task_list:
                print("⚠️ No tasks found to delete.")
                continue

            print("Which task number would you like to delete?")
            for i, t in enumerate(task_list, 1):
                print(f"[{i}] {t['task']} ({t.get('category', 'Uncategorized')})")

            try:
                choice = int(input("Enter number: ").strip())
                if 1 <= choice <= len(task_list):
                    deleted_task = task_list.pop(choice - 1)
                    save_tasks(task_list)
                    print(f"🗑 Task deleted: {deleted_task['task']}")
                else:
                    print("❌ Invalid task number.")
            except ValueError:
                print("❌ Invalid input.")

            print("\n🔁 Updated Tasks:")
            display_tasks_for_today()
            continue
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye from George.")
            break
        try:
            full_prompt = f"{starter_prompt}\nUser: {user_input}"
            reply = ask_gpt(full_prompt)
            print(f"George: {reply}\n")
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    main()
