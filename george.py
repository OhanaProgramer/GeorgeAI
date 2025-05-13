# george.py

import openai
import os
import datetime
from dotenv import load_dotenv
from utils.helper import get_today_theme, load_daily_prompt
from core.task_manager import init_task_folder, prompt_for_tasks, save_tasks

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
    today = datetime.date.today().strftime("%A")
    theme, module = get_today_theme()
    print(f"📅 Today is {today} – Theme: {theme}\n")

    # === Morning Planning Phase ===
    init_task_folder()
    start_today = input("🌅 Good morning. Would you like to plan your day? (y/n): ").lower()
    if start_today == "y":
        tasks = prompt_for_tasks()
        save_tasks(tasks)
        print("\n🧠 George is ready when you are.\n")

    # === Chat Loop ===
    starter_prompt = load_daily_prompt(module)
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
