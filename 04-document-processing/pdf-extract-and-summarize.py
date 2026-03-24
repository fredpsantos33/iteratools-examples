#!/usr/bin/env python3
"""Extract PDF text and summarize with AI. Cost: ~$0.004 per run."""
import os, sys, requests

API_KEY = os.environ.get("ITERA_KEY") or sys.exit("Set ITERA_KEY env var")
PDF_URL = sys.argv[1] if len(sys.argv) > 1 else sys.exit("Usage: python3 script.py <pdf_url>")
BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

print("📄 Extracting PDF text... ($0.002)")
r = requests.post(f"{BASE}/pdf/extract", headers=HEADERS, json={"url": PDF_URL})
text = r.json().get("text", "")[:3000]
print(f"   Extracted {len(text)} chars")

print("🤖 Summarizing with AI... ($0.002)")
r = requests.post(f"{BASE}/ai/chat", headers=HEADERS, json={
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": f"Summarize this document in 3 bullet points:\n\n{text}"}]
})
print("\n" + r.json().get("reply", ""))
