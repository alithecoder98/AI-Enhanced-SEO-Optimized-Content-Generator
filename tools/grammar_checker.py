# tools/grammar_checker.py

import requests
import os

LANGUAGETOOL_API_URL = os.getenv("LANGUAGETOOL_API_URL", "https://api.languagetool.org/v2/check")

def grammar_check(text, language="en-US"):
    payload = {
        "text": text,
        "language": language
    }
    response = requests.post(LANGUAGETOOL_API_URL, data=payload)
    if response.status_code == 200:
        matches = response.json().get("matches", [])
        return {
            "errors": len(matches),
            "suggestions": [match.get("message") for match in matches]
        }
    else:
        raise Exception(f"LanguageTool check failed: {response.status_code}")
