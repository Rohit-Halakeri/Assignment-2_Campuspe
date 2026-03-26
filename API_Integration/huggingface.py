import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

def main():
    print("=== Hugging Face Chat ===")
    user_input = input("Enter your prompt: ")
    print("Querying API.....")

    try:
        client = OpenAI(
            base_url="https://router.huggingface.co/v1",
            api_key=os.environ.get("HUGGINGFACE_API_KEY").strip()
        )
        response = client.chat.completions.create(
            model="meta-llama/Llama-3.1-8B-Instruct:cerebras",
            messages=[{"role": "user", "content": user_input}]
        )
        print("\nResponse:", response.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}")

main()