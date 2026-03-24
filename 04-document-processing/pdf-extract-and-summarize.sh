#!/bin/bash
# Extract text from PDF + summarize with AI
# Cost: ~$0.004 per run
set -e
API_KEY="${ITERA_KEY:?Set ITERA_KEY env var}"
PDF_URL="${1:?Usage: $0 <pdf_url>}"

echo "📄 Extracting text from PDF..."
TEXT=$(curl -s -X POST https://api.iteratools.com/pdf/extract \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$PDF_URL\"}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('text','')[:3000])")

echo "🤖 Summarizing..."
curl -s -X POST https://api.iteratools.com/ai/chat \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"model\": \"gpt-4o-mini\", \"messages\": [{\"role\": \"user\", \"content\": \"Summarize this document in 3 bullet points:\\n\\n$TEXT\"}]}" \
  | python3 -c "import sys,json; print(json.load(sys.stdin).get('reply',''))"
