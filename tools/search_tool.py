# tools/search_tool.py

import requests
import os

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def search_topic_with_tavily(query, num_results=5):
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "advanced",
        "max_results": num_results
    }

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [r["content"] for r in data.get("results", [])]
    else:
        raise Exception(f"Search failed: {response.status_code} {response.text}")

