import os
import json
from glob import glob
from datetime import datetime


BENCHMARK_DIR = "benchmarks"
REPORT_DIR = "reports"


def get_latest_benchmark():

    files = glob(os.path.join(BENCHMARK_DIR, "*.json"))

    if not files:
        print("No benchmark reports found.")
        return None

    latest = max(files, key=os.path.getctime)

    with open(latest, "r", encoding="utf-8") as f:
        data = json.load(f)

    return latest, data


def save_report(report):

    os.makedirs(REPORT_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = os.path.join(
        REPORT_DIR,
        f"report_{timestamp}.txt"
    )

    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)

    return filename


def main():

    result = get_latest_benchmark()

    if result is None:
        return

    path, data = result

    success_rate = 0

    if data["total_requests"] > 0:
        success_rate = round(
            (data["successful_requests"] / data["total_requests"]) * 100,
            2
        )

    report = f"""
============================================================
                SURFBENCH REPORT
============================================================

Benchmark File      : {os.path.basename(path)}

Benchmark ID        : {data["benchmark_id"]}

Model               : {data["model"]}

Timestamp           : {data["timestamp"]}

------------------------------------------------------------

Total Requests      : {data["total_requests"]}

Successful          : {data["successful_requests"]}

Failed              : {data["failed_requests"]}

Success Rate        : {success_rate}%

------------------------------------------------------------

Average Latency     : {data["average_latency_seconds"]} sec

Prompt Tokens       : {data["average_prompt_tokens"]}

Completion Tokens   : {data["average_completion_tokens"]}

Total Tokens        : {data["average_total_tokens"]}

============================================================
"""

    print(report)

    filename = save_report(report)

    print(f"Report saved to: {filename}")


if __name__ == "__main__":
    main()