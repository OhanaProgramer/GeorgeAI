from dotenv import load_dotenv
import openai
import os

# ----- LOAD ENVIRONMENT VARIABLES -----
# Load environment variables from .env file
load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
try:
    models = client.models.list()
    print("✅ API key is valid. You have access to:")
    for model in models.data[:5]:  # show just a few
        print("-", model.id)
except openai.AuthenticationError as e:
    print("❌ Invalid API key.")
except Exception as e:
    print("⚠️ Something else went wrong:", e)

# ----- TESTING THE API -----
def ask_gpt(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content.strip()

def main():
    print("🤖 Personal AI Companion. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        try:
            reply = ask_gpt(user_input)
            print(f"AI: {reply}\n")
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    main()
