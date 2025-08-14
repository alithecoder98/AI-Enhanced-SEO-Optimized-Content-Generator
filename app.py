# app.py
import os
from io import StringIO
from contextlib import redirect_stdout
from typing import Any

from flask import Flask, render_template, request, jsonify

# --- Patch: normalize CrewAI message formatting for models that return list/parts ---
from crewai.utilities import agent_utils as _au
from crewai.agents import crew_agent_executor as _exec

def _to_text(x: Any) -> str:
    if isinstance(x, str):
        return x
    if isinstance(x, list):
        parts = []
        for p in x:
            if isinstance(p, dict) and "text" in p:
                parts.append(str(p["text"]))
            else:
                parts.append(str(p))
        return "\n".join(parts)
    if x is None:
        return ""
    return str(x)

def _format_message_for_llm_patched(prompt, role="user"):
    prompt = _to_text(prompt).rstrip()
    return {"role": role, "content": prompt}

# Apply the patch in BOTH places (source + imported symbol)
_au.format_message_for_llm = _format_message_for_llm_patched
_exec.format_message_for_llm = _format_message_for_llm_patched
# --- End patch ---

from crew_runner import run_crew

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/api/run", methods=["POST"])
def api_run():
    try:
        data = request.get_json(force=True) or {}
        topic = (data.get("topic") or "AI").strip()
        tone = (data.get("tone") or "Professional").strip()
        audience = (data.get("audience") or "General readers").strip()
        word_count = 1200  # <— fixed as requested

        # capture verbose output (not shown in UI, but handy for debugging)
        buf = StringIO()
        with redirect_stdout(buf):
            final_result = run_crew(topic=topic, tone=tone, audience=audience, word_count=word_count)

        # ensure string
        if not isinstance(final_result, str):
            final_result = str(final_result)

        return jsonify({"ok": True, "final": final_result})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"ok": True})

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
