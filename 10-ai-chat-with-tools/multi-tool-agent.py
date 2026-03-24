#!/usr/bin/env python3
"""Research agent: search + scrape + AI synthesis. Cost: ~$0.010 per query."""
import os, sys, requests

API_KEY = os.environ.get("ITERA_KEY") or exit("Set ITERA_KEY")
QUERY = " ".join(sys.argv[1:]) or "What are the best practices for building AI agents in 2025?"
BASE = "https://api.iteratools.com"
H = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

print(f"🔍 Researching: {QUERY}\n")

# Step 1: Search the web ($0.001)
print("Step 1: Web search... ($0.001)")
results = requests.post(f"{BASE}/search", headers=H, json={"query": QUERY, "num_results": 3}).json()
urls = [r["url"] for r in results.get("results", [])[:3]]
print(f"   Found {len(urls)} sources")

# Step 2: Scrape each URL ($0.002 each)
snippets = []
for url in urls:
    print(f"Step 2: Scraping {url[:50]}... ($0.002)")
    text = requests.post(f"{BASE}/scrape", headers=H, json={"url": url}).json().get("text", "")
    snippets.append(f"Source: {url}\n{text[:800]}")

# Step 3: Synthesize with AI ($0.005)
print("Step 3: AI synthesis... ($0.005)")
context = "\n\n---\n\n".join(snippets)
response = requests.post(f"{BASE}/ai/chat", headers=H, json={
    "model": "gpt-4o-mini",
    "messages": [
        {"role": "system", "content": f"Answer based on these sources:\n\n{context}"},
        {"role": "user", "content": QUERY}
    ]
}).json()

print(f"\n{'='*60}")
print(f"Answer:\n{response.get('reply', '')}")
print(f"{'='*60}")
print(f"\nTotal cost: ~$0.010")
