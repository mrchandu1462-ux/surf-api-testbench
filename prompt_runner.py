import os
import json
import time
from datetime import datetime

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("SURF_API_KEY")

if not API_KEY:
    raise ValueError("SURF_API_KEY not found in .env file")

URL = "https://api.asksurf.ai/gateway/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

print("=" * 50)
print("🚀 Surf Prompt Runner v2")
print("=" * 50)

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

try:
    print("\nSending request...")

    start_time = time.time()

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload
    )

    end_time = time.time()

    latency = round(end_time - start_time, 2)

    data = response.json()

    print("\n" + "=" * 50)
    print(f"Status Code : {response.status_code}")
    print(f"Latency     : {latency} sec")
    print("=" * 50)

    answer = data["choices"][0]["message"]["content"]

    print("\nResponse:\n")
    print(answer)

    usage = data.get("usage", {})

    print("\n" + "=" * 50)
    print("Token Usage")
    print("=" * 50)
    print(f"Prompt Tokens     : {usage.get('prompt_tokens')}")
    print(f"Completion Tokens : {usage.get('completion_tokens')}")
    print(f"Total Tokens      : {usage.get('total_tokens')}")

    # -----------------------------
    # Save Result
    # -----------------------------
    os.makedirs("results", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    result = {
        "timestamp": timestamp,
        "prompt": prompt,
        "status_code": response.status_code,
        "latency_seconds": latency,
        "model": data.get("model"),
        "response": answer,
        "usage": usage
    }

    filename = f"results/{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)

    print("\n" + "=" * 50)
    print("✅ Result saved successfully!")
    print(f"📁 {filename}")
    print("=" * 50)

except Exception as e:
    print("\nError:")
    print(e)