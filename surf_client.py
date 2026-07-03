import os
import time
import requests
from dotenv import load_dotenv

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

API_KEY = os.getenv("SURF_API_KEY")

if not API_KEY:
    raise ValueError("SURF_API_KEY not found in .env file")

# ==========================================
# API Configuration
# ==========================================

URL = "https://api.asksurf.ai/gateway/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

MODEL = "surf-1.5"


# ==========================================
# Surf API Client
# ==========================================

class SurfClient:

    def __init__(self):
        self.url = URL
        self.headers = HEADERS
        self.model = MODEL

    def chat(self, messages, reasoning="low"):

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "reasoning_effort": reasoning
        }

        start = time.time()

        response = requests.post(
            self.url,
            headers=self.headers,
            json=payload
        )

        latency = round(time.time() - start, 2)

        response.raise_for_status()

        data = response.json()

        usage = data.get("usage", {})

        return {
            "status_code": response.status_code,
            "latency": latency,
            "answer": data["choices"][0]["message"]["content"],
            "usage": usage,
            "raw": data
        }