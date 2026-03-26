import requests

p = input("Prompt: ")

r = requests.post(
    "http://localhost:11434/api/generate",
    json={"model": "tinyllama", "prompt": p, "stream": False}
)

print("\nBot:", r.json()["response"])