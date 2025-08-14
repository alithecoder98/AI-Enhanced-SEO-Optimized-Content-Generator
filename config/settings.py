# config/settings.py

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# === API KEYS === #
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
LANGUAGETOOL_API_URL = os.getenv("LANGUAGETOOL_API_URL", "https://api.languagetool.org/v2/check")

# === DEFAULT CONFIGURATION === #
DEFAULT_NUM_SEARCH_RESULTS = 5
DEFAULT_TONE = "Professional"
DEFAULT_MODEL = "gemini/gemini-2.0-flash"  # Or override via agent
DEFAULT_WORD_COUNT = 1200
DEFAULT_LANGUAGE = "en-US"
