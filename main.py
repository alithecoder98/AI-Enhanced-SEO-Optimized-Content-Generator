# main.py

# --- Patch: normalize CrewAI message formatting for models that return list/parts ---
from typing import Any
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

def ask_user_inputs():
    print("📝 AI SEO Content Generator")
    topic = (input("Enter a topic: ") or "").strip()
    if not topic:
        topic = "AI"

    tone = (input("Choose a tone (e.g., Formal, Friendly, Persuasive): ") or "").strip() or "Professional"
    audience = (input("Who is your target audience? ") or "").strip() or "General readers"
    word_count_raw = (input("Target word count (default 1200): ") or "").strip()
    word_count = int(word_count_raw) if word_count_raw.isdigit() else 1200

    return {
        "topic": topic,
        "tone": tone,
        "audience": audience,
        "word_count": word_count,
    }

if __name__ == "__main__":
    user_inputs = ask_user_inputs()
    final_content = run_crew(**user_inputs)

    print("\n✅ Final Generated Content:\n")
    print(final_content if isinstance(final_content, str) else str(final_content))
