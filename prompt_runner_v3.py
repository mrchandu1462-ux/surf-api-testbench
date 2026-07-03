import os
import json
import time
from datetime import datetime

import requests
from dotenv import load_dotenv
# ==================================================
# Load Environment Variables
# ==================================================

load_dotenv()

API_KEY = os.getenv("SURF_API_KEY")

if not API_KEY:
    raise ValueError("SURF_API_KEY not found in .env file")


# ==================================================
# API Configuration
# ==================================================

URL = "https://api.asksurf.ai/gateway/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
# ==================================================
# Send Request to Surf API
# ==================================================

def send_request(messages):

    payload = {
        "model": "surf-1.5",
        "messages": messages,
        "stream": False,
        "reasoning_effort": "low"
    }

    print("\nSending request...")

    start_time = time.time()

    response = requests.post(
        URL,
        headers=HEADERS,
        json=payload
    )

    latency = round(time.time() - start_time, 2)

    data = response.json()

    answer = data["choices"][0]["message"]["content"]

    usage = data.get("usage", {})

    return (
        response.status_code,
        latency,
        answer,
        usage,
        data
    )
# ==================================================
# Save Conversation Session
# ==================================================

def save_session(
    messages,
    request_count,
    total_latency,
    total_prompt_tokens,
    total_completion_tokens,
    total_tokens
):

    os.makedirs("results", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"results/{timestamp}.json"

    session = {
    "session_id": f"SESSION_{timestamp}",

    "timestamp": timestamp,

    "total_messages": len(messages),

    "total_requests": request_count,

    "average_latency_seconds": round(
        total_latency / request_count, 2
    ) if request_count else 0,

    "total_prompt_tokens": total_prompt_tokens,

    "total_completion_tokens": total_completion_tokens,

    "total_tokens": total_tokens,

    "conversation": messages
}

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(session, f, indent=4, ensure_ascii=False)

    return filename
# ==================================================
# Main Application
# ==================================================

def main():

    print("=" * 50)
    print("🚀 Surf Prompt Runner v3")
    print("=" * 50)
    print("Type 'exit' to quit.\n")

    messages = []

    request_count = 0
    total_latency = 0

    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_tokens = 0

    while True:

        prompt = input("You > ").strip()

        # Exit
        if prompt.lower() == "exit":

            if request_count > 0:

                filename = save_session(
                    messages,
                    request_count,
                    total_latency,
                    total_prompt_tokens,
                    total_completion_tokens,
                    total_tokens
                )

                print(f"\n💾 Conversation saved: {filename}")

            print("👋 Goodbye!")
            break

        # Ignore empty input
        if not prompt:
            print("Please enter a prompt.\n")
            continue

        messages.append({
            "role": "user",
            "content": prompt
        })

        try:

            status_code, latency, answer, usage, data = send_request(messages)

            request_count += 1
            total_latency += latency

            total_prompt_tokens += usage.get("prompt_tokens", 0)
            total_completion_tokens += usage.get("completion_tokens", 0)

            # Calculate ourselves
            total_tokens = (
                total_prompt_tokens +
                total_completion_tokens
            )

            messages.append({
                "role": "assistant",
                "content": answer
            })

            print("\n" + "=" * 50)
            print(f"Status Code : {status_code}")
            print(f"Latency     : {latency} sec")
            print("=" * 50)

            print("\nSurf >")
            print(answer)

            print("\n" + "=" * 50)
            print("Token Usage")
            print("=" * 50)
            print(f"Prompt Tokens     : {usage.get('prompt_tokens')}")
            print(f"Completion Tokens : {usage.get('completion_tokens')}")
            print(f"Total Tokens      : {usage.get('total_tokens')}")

            print("\n" + "-" * 50 + "\n")

        except Exception as e:
            print("\nError:")
            print(e)


if __name__ == "__main__":
    main()