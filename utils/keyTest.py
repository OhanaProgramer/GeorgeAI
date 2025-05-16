from dotenv import load_dotenv
import os
import openai

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

def ask_gpt(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content
    except openai.AuthenticationError:
        print("❌ API Authentication failed. Please check your API key.")
        raise
    except Exception as e:
        print("⚠️ Unexpected error while calling GPT:", e)
        raise
