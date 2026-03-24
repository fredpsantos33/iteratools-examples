#!/usr/bin/env python3
"""Browser automation: navigate and interact with web pages. Cost: ~$0.005 per session."""
import os, requests

API_KEY = os.environ.get("ITERA_KEY") or exit("Set ITERA_KEY")
BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

print("🌐 Running browser automation... ($0.005)")
result = requests.post(f"{BASE}/browser/act", headers=HEADERS, json={
    "actions": [
        {"type": "navigate", "url": "https://httpbin.org/forms/post"},
        {"type": "type", "selector": "input[name=custname]", "text": "Test Agent"},
        {"type": "type", "selector": "input[name=custtel]", "text": "555-1234"},
        {"type": "select", "selector": "select[name=size]", "value": "medium"},
        {"type": "extract", "selector": "form"}
    ]
}).json()

print("Actions completed:")
for action in result.get("results", []):
    print(f"  ✅ {action.get('type')}: {str(action.get('result',''))[:80]}")
