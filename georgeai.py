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

# ----- Imports Local ----
from utils.helper import get_today_theme, load_daily_prompt
from core.task_manager import init_task_folder, prompt_for_tasks, save_tasks
from core.display import display_tasks_for_today
from utils.helper import get_active_modules
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

def main():
    print("🤖 George AI v1 – Your Daily Companion\n")

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

    response = input("Would you like to add or change anything? (y/n): ").strip().lower()
    if response == "y":
        print("(This feature will allow SOD edits or additions – coming soon.)")

    # === Task Display ===
    print("\n🧠 Loading today's task view...\n")
    display_tasks_for_today()

    # === Task Planning Option ===
    start_today = input("\nWould you like to plan your day from scratch? (y/n): ").strip().lower()
    if start_today == "y":
        init_task_folder()
        tasks = prompt_for_tasks()
        save_tasks(tasks)
        print("\n🧠 George is ready when you are.\n")

    # === Chat Loop ===
    starter_prompt = load_daily_prompt(modules)
    print(f"🧠 {starter_prompt}\n")

    while True:
        user_input = input("You: ")
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
