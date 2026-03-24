#!/usr/bin/env python3
"""
research.py
Web research agent: search → scrape top 3 URLs → AI summarize
Cost: ~$0.013 per session (search: $0.002 + 3x scrape: $0.006 + AI chat: $0.005)

Usage:
    export ITERA_KEY="it-XXXX-XXXX-XXXX"
    python3 research.py "latest advances in solar panel efficiency"
"""

import os
import sys
import requests

API_KEY = os.environ.get("ITERA_KEY")
if not API_KEY:
    sys.exit("Error: Set ITERA_KEY environment variable")

BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

TOPIC = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "benefits of intermittent fasting"


def api(endpoint: str, payload: dict) -> dict:
    resp = requests.post(f"{BASE}{endpoint}", headers=HEADERS, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


print(f"Researching: {TOPIC}")
print("-" * 50)

# Step 1: Search the web ($0.002/call)
print("Searching...")
search_result = api("/search", {"query": TOPIC, "count": 3})
results = search_result.get("results", [])[:3]
print(f"Found {len(results)} sources")

# Step 2: Scrape each URL ($0.002/call each)
scraped_content = []
for r in results:
    url = r.get("url", "")
    title = r.get("title", url)
    print(f"  Scraping: {url}")
    try:
        scraped = api("/scrape", {"url": url})
        content = scraped.get("content", "")[:2000]  # limit per source
        scraped_content.append(f"### {title}\nURL: {url}\n{content}")
    except Exception as e:
        print(f"  (skipped: {e})")

# Step 3: Summarize with AI ($0.005/call)
print("\nGenerating summary...")
combined = "\n\n".join(scraped_content)
context = f"Research topic: {TOPIC}\n\nContent from {len(scraped_content)} web sources:\n\n{combined}"

summary_result = api("/ai/chat", {
    "messages": [
        {
            "role": "user",
            "content": f"{context}\n\nPlease provide a comprehensive, well-structured summary of the findings about: {TOPIC}"
        }
    ]
})

print("\n" + "=" * 50)
print("RESEARCH SUMMARY")
print("=" * 50)
print(summary_result.get("content", summary_result.get("message", str(summary_result))))
