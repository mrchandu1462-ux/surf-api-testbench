# 🚀 Surf API Testbench

> A Python-based QA toolkit for testing, benchmarking, and understanding the Surf API.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Status](https://img.shields.io/badge/Status-Active%20Development-success)
![GitHub](https://img.shields.io/badge/Git-Version%20Controlled-orange)

---

## 📖 Overview

This project began with a simple goal:

**"Can I communicate with the Surf API from Python?"**

Rather than stopping after the first successful API call, I decided to build something more useful—a toolkit that can be expanded into a complete QA and benchmarking framework.

Instead of treating this as a one-time experiment, the project is being developed incrementally, with each feature tested, documented, and tracked through Git.

---

## ✨ Current Features

- Interactive Prompt Runner
- Secure API authentication using `.env`
- Live Surf API integration
- Response latency measurement
- Token usage tracking
- Automatic JSON result logging
- Git version control
- GitHub workflow

---

## 📁 Project Structure

```text
surf-api-testbench/
│
├── results/
├── venv/
├── .env
├── .gitignore
├── prompt_runner.py
├── test.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

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

## ▶️ Usage

Run:

```bash
python prompt_runner.py
```

Example:

```text
Enter your prompt:

> Explain Bitcoin in simple words.
```

The application will:

- Send a live request to the Surf API
- Measure response latency
- Display token usage
- Save the complete result as a JSON file

---

## 📊 Sample Output

```text
Status Code : 200

Latency : 2.14 sec

Prompt Tokens : 398

Completion Tokens : 87

Total Tokens : 485

Result saved:

results/2026-07-01_13-09-54.json
```

---

## 💾 Automatic Result Logging

Every request is stored as structured JSON.

Example:

```text
results/

2026-07-01_13-09-54.json
```

Each record contains:

- Timestamp
- Prompt
- Response
- Model
- Status Code
- Latency
- Token Usage

This creates a growing dataset that can later be used for benchmarking, reporting, and QA analysis.

---

# 🗺️ Roadmap

## ✅ Milestone 1 — Foundation

- [x] Python Environment
- [x] Surf API Integration
- [x] Prompt Runner
- [x] JSON Result Logging
- [x] GitHub Repository

---

## 🚧 Milestone 2 — Interactive Testing

- [ ] Conversation Mode
- [ ] Session History
- [ ] Exit Commands

---

## 🚧 Milestone 3 — Benchmarking

- [ ] Batch Prompt Testing
- [ ] Latency Analytics
- [ ] Token Analytics
- [ ] Response Comparison

---

## 🚧 Milestone 4 — QA Toolkit

- [ ] HTML Reports
- [ ] CSV Export
- [ ] Stress Testing
- [ ] Error Analytics
- [ ] Benchmark Dashboard

---

## 🛠️ Tech Stack

- Python
- Requests
- python-dotenv
- Git
- GitHub
- Surf API

---

## 📈 Development Philosophy

This repository is intentionally being built through small, meaningful iterations.

Each feature follows the same workflow:

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

The goal is not just to create a working application, but to document the engineering process behind it.

---

## 👨‍💻 Author

**Chandu Saikam**

GitHub:
https://github.com/mrchandu1462-ux

---

## ⭐ Project Status

**Active Development**

This repository is evolving into a practical QA toolkit for testing and benchmarking the Surf API. New capabilities will be added through incremental, well-tested releases.