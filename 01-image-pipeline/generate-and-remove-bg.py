#!/usr/bin/env python3
"""
generate-and-remove-bg.py
Generate image with Flux 1.1 Pro + remove background with rembg.
Cost: ~$0.008 total (image: $0.005 + rembg: $0.003)

Usage:
    export ITERA_KEY="it-XXXX-XXXX-XXXX"
    python3 generate-and-remove-bg.py "a red sports car in a showroom"
"""

import os
import sys
import requests

API_KEY = os.environ.get("ITERA_KEY")
if not API_KEY:
    sys.exit("Error: Set ITERA_KEY environment variable")

BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

PROMPT = sys.argv[1] if len(sys.argv) > 1 else "a golden retriever puppy on a white surface"


def api(endpoint: str, payload: dict) -> dict:
    resp = requests.post(f"{BASE}{endpoint}", headers=HEADERS, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


# Step 1: Generate image with Flux 1.1 Pro ($0.005/call)
print(f"Generating image...")
print(f"Prompt: {PROMPT}")

image_result = api("/image/generate", {
    "prompt": PROMPT,
    "width": 1024,
    "height": 1024
})

image_url = image_result["url"]
print(f"Image URL: {image_url}")

# Step 2: Remove background with rembg ($0.003/call)
print("\nRemoving background...")

rembg_result = api("/image/remove-bg", {"url": image_url})

result_url = rembg_result["url"]
print(f"Transparent PNG: {result_url}")

print("\nDone!")
print(f"Original:    {image_url}")
print(f"No-BG PNG:   {result_url}")
