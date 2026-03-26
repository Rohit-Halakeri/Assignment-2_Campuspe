import os
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

def main():
    print("=== OpenAI GPT Chat ===")
    user_input = input("Enter your prompt: ")

    try:
        client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY").strip())
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print("\nResponse:", response.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}")

main()

