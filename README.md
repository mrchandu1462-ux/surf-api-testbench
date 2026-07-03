# 🚀 SurfBench

> A Python toolkit for testing, benchmarking, and evaluating the Surf API.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-v1.0-success)
![GitHub](https://img.shields.io/badge/Git-Version%20Controlled-orange)

---

# 📖 Overview

SurfBench is an open-source toolkit built while exploring the Surf API.

Instead of being a simple API client, SurfBench provides a set of developer tools for interacting with, benchmarking, and evaluating the Surf API.

The project was built incrementally through small engineering milestones, with each feature tested, committed, and documented.

---

# ✨ Features

## 🗨️ Interactive Prompt Runner

- Multi-turn conversations
- Context retention
- Session logging
- Token tracking
- Latency measurement

---

## 📊 Benchmark Runner

Automatically benchmark the Surf API using a prompt dataset.

Features:

- Runs multiple prompts automatically
- Measures latency
- Records token usage
- Stores responses
- Generates structured benchmark reports

---

## 📄 Report Generator

Generate human-readable benchmark summaries.

Displays:

- Total requests
- Success rate
- Average latency
- Prompt tokens
- Completion tokens
- Total tokens

---

## 💾 Automatic JSON Logging

Every benchmark and conversation is saved as structured JSON for future analysis.

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

```bash
git clone https://github.com/mrchandu1462-ux/surf-api-testbench.git

cd surf-api-testbench

python -m venv venv

venv\Scripts\activate

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
python prompt_runner.py
```

---

## Benchmark Runner

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
- Records token usage
- Saves benchmark report

---

## Report Generator

```bash
python report_generator.py
```

Generates a readable benchmark summary from the latest benchmark report.

---

# 📊 Example Benchmark Output

```text
============================================================
✅ BENCHMARK COMPLETE
============================================================

Total Requests      : 10
Successful          : 10
Failed              : 0

Average Latency     : 86.85 sec

Avg Prompt Tokens   : 2400
Avg Completion Tok. : 236
Avg Total Tokens    : 4018

Report saved to:
benchmarks/surfbench_2026-07-03_22-27-43.json
```

---

# 📦 Generated Files

## Benchmark Reports

```text
benchmarks/

surfbench_2026-07-03_22-27-43.json
```

Contains:

- Prompt
- Response
- Status Code
- Latency
- Token Usage
- Benchmark Statistics

---

## Session Logs

```text
results/

2026-07-03_15-30-18.json
```

Contains:

- Conversation
- Session statistics
- Token usage
- Latency

---

## Text Reports

```text
reports/

report_2026-07-03_22-42-03.txt
```

Provides a readable benchmark summary.

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
- Conversation Sessions
- Session Logging
- Benchmark Runner
- Benchmark Reports
- Report Generator
- Shared Surf API Client

---

## 🚀 Future Improvements

- Benchmark Comparison
- CSV Export
- HTML Reports
- Stress Testing
- Performance Dashboard
- Response Quality Evaluation

---

# 📈 Development Workflow

Every feature follows the same engineering workflow:

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

The goal is to build practical developer tools through small, well-tested iterations.

---

# 👨‍💻 Author

**Chandu Saikam**

GitHub:

https://github.com/mrchandu1462-ux

---

# ⭐ Current Status

**SurfBench v1.0**

A lightweight developer toolkit for testing, benchmarking, and evaluating the Surf API.

Current capabilities include:

- Interactive conversations
- Automated benchmarking
- Structured JSON logging
- Benchmark report generation

Future releases will expand benchmarking, reporting, and evaluation capabilities.