import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()


class SurfClient:

    def __init__(
        self,
        model="surf-1.5",
        timeout=120,
        max_retries=3
    ):

        self.api_key = os.getenv("SURF_API_KEY")

        if not self.api_key:
            raise ValueError("SURF_API_KEY not found in .env")

        self.url = "https://api.asksurf.ai/gateway/v1/chat/completions"

        self.model = model
        self.timeout = timeout
        self.max_retries = max_retries

        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def chat(self, messages):

        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "reasoning_effort": "low"
        }

        last_error = None

        for attempt in range(1, self.max_retries + 1):

            try:

                start = time.perf_counter()

                response = requests.post(
                    self.url,
                    headers=self.headers,
                    json=payload,
                    timeout=self.timeout
                )

                latency = round(time.perf_counter() - start, 2)

                if response.status_code in (429, 500, 502, 503, 504):

                    print(
                        f"Retry {attempt}/{self.max_retries} "
                        f"(HTTP {response.status_code})"
                    )

                    time.sleep(attempt)

                    continue

                response.raise_for_status()

                data = response.json()

                if (
                    "choices" not in data
                    or not data["choices"]
                    or "message" not in data["choices"][0]
                ):
                    raise ValueError(
                        f"Unexpected API response:\n{data}"
                    )

                answer = data["choices"][0]["message"]["content"]

                usage = data.get("usage", {})

                return {
                    "status_code": response.status_code,
                    "latency": latency,
                    "answer": answer,
                    "usage": usage,
                    "raw": data
                }

            except (
                requests.exceptions.Timeout,
                requests.exceptions.ConnectionError,
                requests.exceptions.HTTPError,
                ValueError
            ) as e:

                last_error = e

                print(
                    f"Attempt {attempt}/{self.max_retries} failed:"
                )
                print(e)

                if attempt < self.max_retries:
                    time.sleep(attempt)

        raise RuntimeError(
            f"Request failed after {self.max_retries} attempts.\n{last_error}"
        )