#!/bin/bash
# research.sh
# Research agent: search → scrape → AI summarize
# Cost: ~$0.013 per session (search: $0.002 + 3x scrape: $0.006 + AI: $0.005)
#
# Usage: bash research.sh "your research topic"

set -e

ITERA_KEY="${ITERA_KEY:?Set ITERA_KEY environment variable}"
TOPIC="${1:-benefits of intermittent fasting}"
BASE="https://api.iteratools.com"

echo "Searching for: $TOPIC"

# Step 1: Search the web ($0.002)
SEARCH_RESP=$(curl -s -X POST "$BASE/search" \
  -H "Authorization: Bearer $ITERA_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"query\": \"$TOPIC\", \"count\": 3}")

# Extract top 3 URLs
URLS=$(echo "$SEARCH_RESP" | python3 -c "
import sys, json
d = json.load(sys.stdin)
results = d.get('results', [])[:3]
for r in results:
    print(r['url'])
")

echo "Found results. Scraping content..."

# Step 2: Scrape each URL ($0.002 each)
ALL_CONTENT=""
while IFS= read -r url; do
  echo "  Scraping: $url"
  SCRAPED=$(curl -s -X POST "$BASE/scrape" \
    -H "Authorization: Bearer $ITERA_KEY" \
    -H "Content-Type: application/json" \
    -d "{\"url\": \"$url\"}")
  
  CONTENT=$(echo "$SCRAPED" | python3 -c "
import sys, json
d = json.load(sys.stdin)
text = d.get('content', '')[:1500]
print(text)
  ")
  ALL_CONTENT="$ALL_CONTENT\n\nSource: $url\n$CONTENT"
done <<< "$URLS"

# Step 3: Summarize with AI ($0.005)
echo ""
echo "Generating AI summary..."

SUMMARY=$(curl -s -X POST "$BASE/ai/chat" \
  -H "Authorization: Bearer $ITERA_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"messages\": [
      {\"role\": \"user\", \"content\": \"Research topic: $TOPIC\n\nContent from web sources:\n$ALL_CONTENT\n\nPlease provide a comprehensive, well-structured summary of the findings.\"}
    ]
  }")

echo ""
echo "=== RESEARCH SUMMARY ==="
echo "$SUMMARY" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('content', d.get('message', d)))"
