import os
import json
from datetime import datetime

from surf_client import SurfClient


def load_prompts():
    with open("prompts.json", "r", encoding="utf-8") as f:
        return json.load(f)


def save_benchmark(report):
    os.makedirs("benchmarks", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"benchmarks/surfbench_{timestamp}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    return filename


def main():

    print("=" * 60)
    print("🚀 SurfBench Benchmark Runner")
    print("=" * 60)

    prompts = load_prompts()

    client = SurfClient()

    results = []

    successful_requests = 0
    failed_requests = 0

    total_latency = 0
    total_prompt_tokens = 0
    total_completion_tokens = 0
    total_tokens = 0

    print(f"\nLoaded {len(prompts)} prompts.\n")

    for index, prompt in enumerate(prompts, start=1):

        print(f"[{index}/{len(prompts)}] {prompt}")

        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]

        try:

            response = client.chat(messages)

            latency = response["latency"]
            usage = response["usage"]

            successful_requests += 1

            total_latency += latency
            total_prompt_tokens += usage.get("prompt_tokens", 0)
            total_completion_tokens += usage.get("completion_tokens", 0)
            total_tokens += usage.get("total_tokens", 0)

            results.append({
                "prompt": prompt,
                "response": response["answer"],
                "status_code": response["status_code"],
                "latency_seconds": latency,
                "usage": usage
            })
            print(f"   ✓ {latency} sec | {usage.get('total_tokens', 0)} tokens")

        except Exception as e:

            failed_requests += 1

            results.append({
                "prompt": prompt,
                "error": str(e)
            })

    average_latency = round(
        total_latency / successful_requests, 2
    ) if successful_requests else 0

    average_prompt_tokens = round(
        total_prompt_tokens / successful_requests
    ) if successful_requests else 0

    average_completion_tokens = round(
        total_completion_tokens / successful_requests
    ) if successful_requests else 0

    average_total_tokens = round(
        total_tokens / successful_requests
    ) if successful_requests else 0

    report = {

        "benchmark_id": f"BENCH_{datetime.now().strftime('%Y%m%d_%H%M%S')}",

        "timestamp": datetime.now().isoformat(),

        "model": client.model,

        "total_requests": len(prompts),

        "successful_requests": successful_requests,

        "failed_requests": failed_requests,

        "average_latency_seconds": average_latency,

        "average_prompt_tokens": average_prompt_tokens,

        "average_completion_tokens": average_completion_tokens,

        "average_total_tokens": average_total_tokens,

        "results": results
    }

    filename = save_benchmark(report)

    print("\n" + "=" * 60)
    print("✅ BENCHMARK COMPLETE")
    print("=" * 60)
    print(f"Total Requests      : {len(prompts)}")
    print(f"Successful          : {successful_requests}")
    print(f"Failed              : {failed_requests}")
    print(f"Average Latency     : {average_latency} sec")
    print(f"Avg Prompt Tokens   : {average_prompt_tokens}")
    print(f"Avg Completion Tok. : {average_completion_tokens}")
    print(f"Avg Total Tokens    : {average_total_tokens}")
    print(f"\n📁 Report saved to: {filename}")


if __name__ == "__main__":
    main()