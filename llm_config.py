# llm_config.py
import os
from crewai import LLM  # if this import fails on your version: from crewai.llm import LLM

MODEL = os.getenv("LITELLM_MODEL", "gemini/gemini-2.0-flash")
GEMINI_KEY = os.getenv("GEMINI_API_KEY")

llm_config = LLM(
    model=MODEL,
    api_key=GEMINI_KEY,               # Gemini key only
    temperature=float(os.getenv("LLM_TEMPERATURE", "0.3")),
    max_tokens=int(os.getenv("LLM_MAX_TOKENS", "2000")),
    top_p=float(os.getenv("LLM_TOP_P", "1.0")),
    timeout=int(os.getenv("LLM_TIMEOUT", "120")),
    # No base_url here; LiteLLM routes Gemini automatically
    # No tool/function params — we'll block tools at the agent level below
)
