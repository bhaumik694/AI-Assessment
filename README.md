# 🎓 EduPilot-AI

> An agentic AI pipeline that generates, reviews, and refines grade-appropriate educational content — explanations and quizzes — on any topic, in seconds.

---

## 📋 Table of Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the App](#running-the-app)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

**EduPilot-AI** is a full-stack AI-powered learning platform with a multi-agent backend and a Streamlit frontend. Given a grade level (1–10) and a topic, it runs a three-stage agentic pipeline:

1. **Generate** — produces a grade-appropriate explanation and MCQ quiz
2. **Review** — an AI reviewer evaluates the content for accuracy and age-appropriateness
3. **Refine** — if the review fails, the content is automatically improved and returned

The frontend (`app.py`) communicates with the FastAPI backend over HTTP, displaying all three stages of output in a clean, step-by-step UI.

---

## How It Works

```
User Input (grade + topic)
        │
        ▼
┌───────────────────┐
│  Generator Agent  │  →  Explanation + MCQ quiz
└───────────────────┘
        │
        ▼
┌───────────────────┐
│  Reviewer Agent   │  →  Pass / Fail + feedback
└───────────────────┘
        │
   Fail? │ Yes
        ▼
┌───────────────────┐
│  Generator Agent  │  →  Refined explanation + quiz
│  (with feedback)  │
└───────────────────┘
        │
        ▼
   JSON Response to Frontend
```

The pipeline is orchestrated by `pipeline.py`, which coordinates the two agents and applies grade-specific rules from `grade_rules.py` to tailor vocabulary, complexity, and question difficulty.

---

## ✨ Features

- **Multi-agent pipeline** — separate Generator and Reviewer agents with distinct responsibilities
- **Grade-aware content** — `grade_rules.py` enforces age-appropriate language and complexity for grades 1–10
- **Auto-refinement** — content that fails review is automatically re-generated with reviewer feedback injected
- **Structured outputs** — Pydantic schemas (`schemas.py`) ensure consistent, typed JSON responses
- **FastAPI backend** — clean REST API with a single `/generate` endpoint
- **Streamlit frontend** — interactive UI with grade selector, step progress indicator, and formatted MCQ display
- **Any topic** — works across all school subjects: maths, science, history, languages, and more

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Python · Streamlit |
| Backend | Python · FastAPI · Uvicorn |
| LLM Integration | `llm.py` (LLM client wrapper) |
| Data Validation | Pydantic (`schemas.py`) |
| Agent Orchestration | Custom pipeline (`pipeline.py`) |
| Grade Logic | Rule-based (`grade_rules.py`) |

---

## 📁 Project Structure

```
EduPilot-AI/
│
├── requirements.txt               # Python dependencies
│
├── backend/                       # FastAPI backend + agent pipeline
│   ├── main.py                    # FastAPI app — exposes POST /generate
│   ├── pipeline.py                # Orchestrates Generator → Reviewer → (Refine) flow
│   ├── llm.py                     # LLM client wrapper (API calls to the language model)
│   ├── schemas.py                 # Pydantic models for request/response validation
│   ├── grade_rules.py             # Grade-level rules: vocabulary, complexity, MCQ difficulty
│   │
│   └── agents/
│       ├── generator.py           # Generator agent — produces explanation + MCQ quiz
│       └── reviewer.py            # Reviewer agent — evaluates content, returns pass/fail + feedback
│
└── frontend/
    └── app.py                     # Streamlit UI — grade selector, topic input, results display
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- An LLM API key (OpenAI, Groq, or whichever provider `llm.py` is configured for)

---

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/bhaumik694/EduPilot-AI.git
cd EduPilot-AI
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set your LLM API key**

Create a `.env` file in the root:

```env
LLM_API_KEY=your_api_key_here
```

---

### Running the App

**Start the FastAPI backend** (terminal 1):

```bash
cd backend
uvicorn main:app --reload --port 8000
```

The API will be live at `http://127.0.0.1:8000`.

**Start the Streamlit frontend** (terminal 2):

```bash
cd frontend
streamlit run app.py
```

Open `http://localhost:8501` in your browser.

---

## 📡 API Reference

### `POST /generate`

Runs the full generator → reviewer → refine pipeline.

**Request body:**
```json
{
  "grade": 5,
  "topic": "Photosynthesis"
}
```

**Response:**
```json
{
  "initial_output": {
    "explanation": "...",
    "mcqs": [
      {
        "question": "...",
        "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
        "answer": "A. ..."
      }
    ]
  },
  "review": {
    "status": "pass",
    "feedback": []
  },
  "refined_output": null
}
```

If `review.status` is `"fail"`, `refined_output` will contain an improved version of `initial_output`.

Interactive docs available at `http://127.0.0.1:8000/docs` once the backend is running.

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

