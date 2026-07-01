import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("SURF_API_KEY")

if not API_KEY:
    raise ValueError("SURF_API_KEY not found in .env file")

# Surf API endpoint
url = "https://api.asksurf.ai/gateway/v1/chat/completions"

# Request headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Request payload
payload = {
    "model": "surf-1.5",
    "messages": [
        {
            "role": "user",
            "content": "Hello Surf! Reply only with: API connection successful."
        }
    ],
    "stream": False,
    "reasoning_effort": "low"
}

try:
    print("Sending request to Surf API...\n")

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=60
    )

    print("=" * 50)
    print(f"Status Code : {response.status_code}")
    print("=" * 50)

    try:
        print(response.json())
    except Exception:
        print(response.text)

except requests.exceptions.Timeout:
    print("❌ Request timed out.")

except requests.exceptions.ConnectionError:
    print("❌ Unable to connect to Surf API.")

except Exception as e:
    print(f"❌ Unexpected Error: {e}")