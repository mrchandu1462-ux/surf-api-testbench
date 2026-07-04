# 🚀 SurfBench – Surf API Benchmarking Toolkit

> An open-source developer toolkit for testing, benchmarking, and evaluating applications built with the Surf API.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Version](https://img.shields.io/badge/Version-v1.0-success)
![Status](https://img.shields.io/badge/Status-Active-success)
![GitHub](https://img.shields.io/badge/Git-Version%20Controlled-orange)

---

# 📖 Overview

SurfBench is an open-source Python toolkit built while exploring the Surf API.

Rather than being a simple API client, SurfBench provides reusable developer tools for interacting with, benchmarking, and evaluating the Surf API.

The project focuses on making API testing repeatable, measurable, and easy to extend through modular components and structured reporting.

---

# 🎯 Motivation

While learning the Surf API, I wanted more than a single script that sends requests.

The goal was to build a reusable toolkit that allows developers to:

- Interactively test prompts
- Benchmark API performance
- Measure latency and token usage
- Save structured benchmark results
- Generate readable benchmark reports

SurfBench is the first step toward a lightweight QA and benchmarking toolkit for the Surf ecosystem.

---

# ✨ Features

## 🗨️ Interactive Prompt Runner

- Multi-turn conversations
- Conversation memory
- Session logging
- Token usage tracking
- Latency measurement

---

## 📊 Automated Benchmark Runner

Benchmark the Surf API using a prompt dataset.

Features include:

- Batch prompt execution
- Automatic latency measurement
- Token usage analytics
- Structured JSON benchmark reports
- Success / failure tracking

---

## 📄 Benchmark Report Generator

Generate readable summaries from benchmark results.

Reports include:

- Total requests
- Success rate
- Average latency
- Prompt tokens
- Completion tokens
- Total tokens

---

## 💾 Automatic Logging

SurfBench automatically stores:

- Conversation sessions
- Benchmark reports
- Structured JSON outputs
- Human-readable summaries

---

# 🏗️ Architecture

```text
                    +----------------------+
                    |   Prompt Runner      |
                    +----------+-----------+
                               |
                               |
                    +----------v-----------+
                    |     SurfClient       |
                    |  Shared API Client   |
                    +----------+-----------+
                               |
                               |
                        Surf API Gateway
                               |
                    +----------+-----------+
                    | Benchmark Runner     |
                    +----------+-----------+
                               |
                    +----------v-----------+
                    | Report Generator     |
                    +----------------------+
```

---

# 📁 Project Structure

```text
surf-api-testbench/

├── benchmarks/
│   └── surfbench_*.json
│
├── reports/
│   └── report_*.txt
│
├── results/
│   └── session_*.json
│
├── prompt_runner.py
├── prompt_runner_v3.py
├── benchmark_runner.py
├── report_generator.py
├── surf_client.py
├── prompts.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/mrchandu1462-ux/surf-api-testbench.git

cd surf-api-testbench
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
SURF_API_KEY=your_api_key_here
```

---

# ▶️ Usage

## Interactive Prompt Runner

```bash
python prompt_runner_v3.py
```

Supports:

- Multi-turn conversations
- Session logging
- Context retention

---

## Automated Benchmark Runner

```bash
python benchmark_runner.py
```

Reads prompts from:

```text
prompts.json
```

Automatically:

- Sends requests
- Measures latency
- Tracks token usage
- Generates benchmark reports

---

## Benchmark Report Generator

```bash
python report_generator.py
```

Creates a readable summary from the latest benchmark.

---

# 📊 Example Benchmark Output

```text
============================================================
✅ BENCHMARK COMPLETE
============================================================

Total Requests      : 10
Successful          : 10
Failed              : 0

Average Latency     : 18.09 sec

Avg Prompt Tokens   : 1638
Avg Completion Tok. : 270
Avg Total Tokens    : 3393

Report saved to:
benchmarks/surfbench_2026-07-04_11-07-43.json
```

---

# 📦 Generated Files

## Conversation Sessions

```text
results/

2026-07-04_10-15-24.json
```

Contains:

- Conversation history
- Session statistics
- Token usage
- Latency

---

## Benchmark Reports

```text
benchmarks/

surfbench_2026-07-04_11-07-43.json
```

Contains:

- Prompt
- Response
- Status Code
- Latency
- Token Usage
- Benchmark statistics

---

## Human Readable Reports

```text
reports/

report_2026-07-04_11-12-08.txt
```

Provides a concise benchmark summary.

---

# 🎯 Design Principles

SurfBench follows a simple engineering philosophy:

- Modular architecture
- Shared API client
- Reusable components
- Structured outputs
- Benchmark-driven testing
- Easy extensibility

---

# 🛠️ Tech Stack

- Python
- Requests
- python-dotenv
- JSON
- Git
- GitHub
- Surf API

---

# 🗺️ Roadmap

## ✅ Version 1.0

- Interactive Prompt Runner
- Conversation Memory
- Session Logging
- Shared API Client
- Benchmark Runner
- Benchmark Reports
- Report Generator

---

## 🚀 Version 1.1

- Configurable timeout
- Retry mechanism
- Better error handling
- CLI arguments
- Config file support

---

## 🚀 Future Releases

- Parallel benchmarking
- Benchmark comparison
- HTML reports
- CSV export
- Performance dashboard
- Response quality evaluation
- Visual analytics

---

# 📈 Development Workflow

Every feature follows the same workflow:

```text
Plan
   ↓
Build
   ↓
Test
   ↓
Commit
   ↓
Push
```

The objective is to build practical developer tools through incremental, well-tested improvements.

---

# 👨‍💻 Author

**Chandu Saikam**

GitHub:

https://github.com/mrchandu1462-ux

---

# 🤝 Contributing

Suggestions, bug reports, and feature requests are always welcome.

If you have ideas that could improve SurfBench or make it more useful for Surf developers, feel free to open an issue or contribute.

---

# 📄 License

This project is released under the MIT License.

---

# ⭐ Project Status

**SurfBench v1.0**

SurfBench is a lightweight developer toolkit for testing, benchmarking, and evaluating the Surf API.

Current capabilities include:

- Interactive conversations
- Automated benchmarking
- Shared API client
- Structured JSON logging
- Benchmark report generation

The long-term vision is to evolve SurfBench into a comprehensive toolkit for API benchmarking, regression testing, and developer-focused QA workflows.