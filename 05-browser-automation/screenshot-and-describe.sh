#!/bin/bash
# Take screenshot of URL and describe it with GPT-4o Vision
# Cost: ~$0.011 per run
set -e
API_KEY="${ITERA_KEY:?Set ITERA_KEY}"
URL="${1:?Usage: $0 <url>}"

echo "📸 Taking screenshot of $URL... (\$0.003)"
IMG=$(curl -s -X POST https://api.iteratools.com/screenshot \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$URL\", \"full_page\": false}" \
  | python3 -c "import sys,json; print(json.load(sys.stdin).get('image',''))")

echo "👁️ Describing with GPT-4o Vision... (\$0.008)"
curl -s -X POST https://api.iteratools.com/image/describe \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"image\": \"$IMG\", \"prompt\": \"Describe this webpage screenshot in detail.\"}" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('data',{}).get('description',''))"
