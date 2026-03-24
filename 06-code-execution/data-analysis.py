#!/usr/bin/env python3
"""Run data analysis code in a secure sandbox. Cost: $0.005 per run."""
import os, requests

API_KEY = os.environ.get("ITERA_KEY") or exit("Set ITERA_KEY")
BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

analysis_code = """
import statistics

# Sample sales data
sales = [1200, 1450, 980, 2100, 1750, 890, 2300, 1600, 1100, 1900]

stats = {
    "count": len(sales),
    "total": sum(sales),
    "mean": round(statistics.mean(sales), 2),
    "median": statistics.median(sales),
    "stdev": round(statistics.stdev(sales), 2),
    "min": min(sales),
    "max": max(sales),
    "above_mean": sum(1 for s in sales if s > statistics.mean(sales))
}

for k, v in stats.items():
    print(f"{k}: {v}")
"""

print("💻 Running data analysis in sandbox... ($0.005)")
r = requests.post(f"{BASE}/code_execute", headers=HEADERS, json={
    "language": "python",
    "code": analysis_code
})
print("\n📊 Results:")
print(r.json().get("output", ""))
