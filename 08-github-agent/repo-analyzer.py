#!/usr/bin/env python3
"""Search GitHub repos and analyze them. Cost: ~$0.003 per run."""
import os, requests

API_KEY = os.environ.get("ITERA_KEY") or exit("Set ITERA_KEY")
BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

query = "mcp server tools ai agents"
print(f"🔍 Searching GitHub for: '{query}'... ($0.001)")
r = requests.get(f"{BASE}/github/search", headers=HEADERS, params={"q": query, "type": "repositories", "per_page": 5})
repos = r.json().get("items", [])

print(f"\n📋 Top {len(repos)} repos:")
for repo in repos[:5]:
    print(f"  ⭐ {repo.get('stargazers_count'):,} | {repo.get('full_name')} — {repo.get('description','')[:60]}")
