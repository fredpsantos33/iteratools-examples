#!/usr/bin/env python3
"""Find free slots and create calendar event. Cost: ~$0.003."""
import os, requests
from datetime import datetime, timedelta

API_KEY = os.environ.get("ITERA_KEY") or exit("Set ITERA_KEY")
GOOGLE_TOKEN = os.environ.get("GOOGLE_OAUTH_TOKEN") or exit("Set GOOGLE_OAUTH_TOKEN")
BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

print("📅 Checking availability... ($0.001)")
r = requests.get(f"{BASE}/calendar/availability", headers=HEADERS, json={
    "google_oauth_token": GOOGLE_TOKEN,
    "days": 7,
    "slot_minutes": 60
})
free_slots = r.json().get("free_slots", [])

if not free_slots:
    print("No free slots found!")
    exit(1)

first_slot = free_slots[0]
print(f"   First available: {first_slot}")

print(f"\n📌 Creating event at {first_slot}... ($0.002)")
r = requests.post(f"{BASE}/calendar/event", headers=HEADERS, json={
    "google_oauth_token": GOOGLE_TOKEN,
    "title": "AI Agent Meeting",
    "start": first_slot,
    "duration_minutes": 60,
    "description": "Scheduled automatically by IteraTools agent"
})
event = r.json()
print(f"   ✅ Event created: {event.get('html_link', event.get('id', ''))}")
