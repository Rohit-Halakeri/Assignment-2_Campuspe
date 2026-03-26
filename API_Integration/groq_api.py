# import os
# from groq import Groq
# from dotenv import load_dotenv

# load_dotenv()

# def main():
#     print("=== Groq LLaMA Chat ===")
#     user_input = input("Enter your prompt: ")

#     try:
#         client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
#         response = client.chat.completions.create(
#             model="llama-3.1-8b-instant",
#             messages=[{"role": "user", "content": user_input}]
#         )
#         print("\nResponse:", response.choices[0].message.content)

#     except Exception as e:
#         print(f"Error: {e}")

# main()

import os
from groq import Groq
from dotenv import load_dotenv
from pathlib import Path

# Force load from exact location
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)


def main():
    print("=== Groq LLaMA Chat ===")
    user_input = input("Enter your prompt: ")

    try:
        client = Groq(api_key=os.environ.get("GROQ_API_KEY").strip())
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )
        print("\nResponse:", response.choices[0].message.content)

    except Exception as e:
        print(f"Error: {e}")

main()