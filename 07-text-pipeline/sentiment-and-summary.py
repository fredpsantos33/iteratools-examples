#!/usr/bin/env python3
"""Analyze sentiment and summarize text. Cost: ~$0.003 per run."""
import os, requests

API_KEY = os.environ.get("ITERA_KEY") or exit("Set ITERA_KEY")
BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

text = """
The new IteraTools API is incredibly powerful. I was able to build a complete
image processing pipeline in under an hour. The documentation is clear and the
pay-per-use pricing means I only pay for what I actually use. Highly recommended
for anyone building AI agents or automation workflows.
"""

print("😊 Analyzing sentiment... ($0.001)")
r = requests.post(f"{BASE}/sentiment", headers=HEADERS, json={"text": text})
s = r.json()
print(f"   Score: {s.get('score')} | Label: {s.get('label')} | Comparative: {s.get('comparative')}")

print("\n📝 Summarizing... ($0.002)")
r = requests.post(f"{BASE}/summarize", headers=HEADERS, json={"text": text, "max_sentences": 2})
print("   " + r.json().get("summary", ""))
