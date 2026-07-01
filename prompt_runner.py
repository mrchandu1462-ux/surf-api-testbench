import os
import time
import requests
from dotenv import load_dotenv

# Load API key
load_dotenv()

API_KEY = os.getenv("SURF_API_KEY")

if not API_KEY:
    raise ValueError("SURF_API_KEY not found in .env")

URL = "https://api.asksurf.ai/gateway/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("=" * 40)
print("🚀 Surf Prompt Runner v1")
print("=" * 40)

prompt = input("\nEnter your prompt:\n> ")

payload = {
    "model": "surf-1.5",
    "messages": [
        {
            "role": "user",
            "content": prompt
        }
    ],
    "stream": False,
    "reasoning_effort": "low"
}

print("\nSending request...")

start = time.time()

try:
    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload,
        timeout=60
    )

    end = time.time()

    latency = round(end - start, 2)

    print("\n" + "=" * 40)
    print(f"Status Code : {response.status_code}")
    print(f"Latency    : {latency} sec")
    print("=" * 40)

    data = response.json()

    answer = data["choices"][0]["message"]["content"]

    print("\nResponse:\n")
    print(answer)

    usage = data.get("usage", {})

    print("\n" + "=" * 40)
    print("Token Usage")
    print("=" * 40)
    print(f"Prompt Tokens    : {usage.get('prompt_tokens')}")
    print(f"Completion Tokens: {usage.get('completion_tokens')}")
    print(f"Total Tokens     : {usage.get('total_tokens')}")

except Exception as e:
    print("\nError:")
    print(e)