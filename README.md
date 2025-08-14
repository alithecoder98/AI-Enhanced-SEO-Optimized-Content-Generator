# 🤖✨ AI-Enhanced SEO-Optimized Content Generator

A sleek **Flask** web app that wraps a **CrewAI** multi-agent workflow powered by **Google Gemini 2.0 Flash**.
Enter a **Topic**, pick a **Tone** & **Audience**, and get a \~**1200-word**, SEO-structured article with clean headings and publish-ready copy — all in a modern, techy UI.

---

## 🧭 Table of Contents

* [Features](#-features)
* [Demo Flow](#-demo-flow)
* [Tech Stack](#-tech-stack)
* [Project Structure](#-project-structure)
* [Quick Start](#-quick-start)
* [Environment Variables](#-environment-variables)
* [Run Locally](#-run-locally)
* [API](#-api)
* [Screenshots](#-screenshots)
* [Security Notes](#-security-notes)
* [Troubleshooting](#-troubleshooting)
* [Roadmap](#-roadmap)
* [Contributing](#-contributing)
* [License](#-license)

---

## ✨ Features

* 🧠 **Multi-agent pipeline** (CrewAI): research → SEO outline → intro → body → conclusion → tone unify → finalize.
* ⚡ **Gemini 2.0 Flash only**: fast, cost-effective, stable completions.
* 🧩 **SEO-aware output**: H1/H2 structure, keyword-friendly prose, cohesive intro/body/conclusion.
* 🖥️ **Modern UI** (Tailwind): techy, minimal, responsive.
* 📋 **One-click copy** of the final summary.
* 🔒 **No secrets in git**: uses `.env` locally and a public `.env.example`.
* 🧱 **Stability guards**: normalizes model outputs and disables tool calls to avoid odd return shapes.

> ℹ️ UI shows **only the Summary** (final content). Target word count is **fixed at 1200** server-side.

---

## 🎬 Demo Flow

1. Fill **Topic**, **Tone**, **Audience**.
2. Click **Run Crew**.
3. Receive a **final, SEO-ready article** (≈1200 words) you can copy with one click.

---

## 🛠 Tech Stack

* **Backend**: Flask
* **Agents**: CrewAI
* **LLM**: Google Gemini 2.0 Flash (via LiteLLM under the hood)
* **Frontend**: TailwindCSS
* **Runtime**: Python 3.10+

---

## 🗂 Project Structure

```
.
├─ app.py                    # Flask server + output normalization patch
├─ crew_runner.py            # Builds agents & tasks and runs the Crew
├─ agents/                   # Agent factory functions
├─ prompts/                  # Prompt templates (optional)
├─ tools/                    # (If any custom tools; currently disabled)
├─ templates/
│  └─ index.html             # Techy UI (Tailwind)
├─ config/                   # App/config helpers
├─ llm_config.py             # Gemini model config for CrewAI
├─ requirements.txt          # Python dependencies
├─ .gitignore                # Keeps secrets & junk out of git
├─ .env.example              # Safe template for environment variables
└─ README.md
```

---

## 🚀 Quick Start

```bash
# Clone your repo
git clone https://github.com/alithecoder98/AI-Enhanced-SEO-Optimized-Content-Generator.git
cd AI-Enhanced-SEO-Optimized-Content-Generator

# Create env from template
copy .env.example .env   # Windows PowerShell
# cp .env.example .env   # macOS/Linux

# Edit .env and add your real GEMINI_API_KEY

# Create & activate venv (Windows)
python -m venv .venv
. .\.venv\Scripts\activate

# Install deps
pip install -r requirements.txt

# Run
python app.py
# open http://localhost:5000
```

---

## 🔧 Environment Variables

Create a local `.env` (never commit real secrets!) based on `.env.example`.

```dotenv
# Google Gemini (required)
GEMINI_API_KEY=YOUR_GEMINI_API_KEY

# LiteLLM / CrewAI
LITELLM_PROVIDER=gemini
LITELLM_MODEL=gemini/gemini-2.0-flash

# Optional tools
TAVILY_API_KEY=
LANGUAGETOOL_API_URL=https://api.languagetool.org/v2/check

# App params (optional)
PORT=5000
LLM_TEMPERATURE=0.3
LLM_MAX_TOKENS=2000
```

> **.gitignore** already excludes `.env`. Only **`.env.example`** lives in the repo.

---

## 🧪 API

### `POST /api/run`

Run the crew and receive the final article (summary).

**Request (JSON)**

```json
{
  "topic": "AI",
  "tone": "Formal",
  "audience": "Students"
}
```

> `word_count` is not needed; the backend uses **1200** automatically.

**Response (JSON)**

```json
{
  "ok": true,
  "final": "<markdown-like final content>"
}
```

**Example (PowerShell)**:

```powershell
Invoke-RestMethod -Uri http://localhost:5000/api/run -Method Post -ContentType 'application/json' -Body (@{
  topic="AI"; tone="Formal"; audience="Students"
} | ConvertTo-Json)
```

---

## 🖼 Screenshots

(Add your screenshots to the repo and reference them here.)

* **UI Home**
  `![Home](docs/screens/home.png)`

---

## 🔐 Security Notes

* **Never commit `.env`** (API keys). `.gitignore` blocks it by default.
* If secrets were pushed accidentally:

  1. Rotate keys immediately.
  2. Remove from history (e.g., `git filter-repo`) and force-push.

---

## 🧰 Troubleshooting

* **No output / odd tool calls**
  We **disable tool calling** and **normalize outputs** so CrewAI always receives plain text. Ensure you’re on the provided `app.py`, `crew_runner.py`, and `llm_config.py`.
* **“Nothing added to commit” / “src refspec main”**
  Run in order: `git add .` → `git commit -m "msg"` → `git branch -M main` → `git push -u origin main`.
* **Module not found / version mismatch**
  Re-install deps: `pip install -r requirements.txt`. Confirm Python ≥ 3.10.

---

## 🗺 Roadmap

* ⏳ Streaming tokens (SSE/WebSockets)
* 🎯 Keyword suggestions & density meter
* 📦 Export to Markdown/HTML/PDF
* 🧪 Built-in plagiarism & grammar checks
* 🌐 One-click deploy (Render/Fly/Heroku)

---

## 🤝 Contributing

PRs welcome!

1. Fork the repo
2. Create a feature branch: `git checkout -b feat/awesome`
3. Commit: `git commit -m "Add awesome feature"`
4. Push: `git push -u origin feat/awesome`
5. Open a Pull Request

---

## 📄 License

MIT (or your preferred license). Add a `LICENSE` file if you haven’t already.

---

**Made with 🧡, Flask, CrewAI, and Gemini 2.0 Flash.**
