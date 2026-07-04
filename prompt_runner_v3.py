import os
import json
import time
from datetime import datetime

from surf_client import SurfClient
# ==================================================
# Load Environment Variables
# ==================================================


# ==================================================
# Send Request to Surf API
# ==================================================



    
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
    client = SurfClient()

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

            response = client.chat(messages)

            status_code = response["status_code"]
            latency = response["latency"]
            answer = response["answer"]
            usage = response["usage"]

            request_count += 1
            total_latency += latency

            total_prompt_tokens += usage.get("prompt_tokens", 0)
            total_completion_tokens += usage.get("completion_tokens", 0)

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