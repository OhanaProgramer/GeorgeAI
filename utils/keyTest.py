import openai

# Replace with your actual key or use os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key="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")

try:
    models = client.models.list()
    print("✅ API key is valid. You have access to:")
    for model in models.data[:5]:  # show just a few
        print("-", model.id)
except openai.AuthenticationError as e:
    print("❌ Invalid API key.")
except Exception as e:
    print("⚠️ Something else went wrong:", e)
