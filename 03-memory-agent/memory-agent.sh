#!/bin/bash
# memory-agent.sh
# Agent with persistent vector memory: upsert + semantic search + AI chat
# Cost per query: ~$0.007 (upsert: $0.001 + search: $0.001 + AI: $0.005)
#
# Usage:
#   bash memory-agent.sh store USER_ID "fact to remember"
#   bash memory-agent.sh query USER_ID "question to ask"

set -e

ITERA_KEY="${ITERA_KEY:?Set ITERA_KEY environment variable}"
BASE="https://api.iteratools.com"
ACTION="${1:-help}"
USER_ID="${2:-user_default}"
TEXT="${3:-}"

if [ "$ACTION" = "store" ]; then
  echo "Storing memory for $USER_ID: $TEXT"
  
  # Store in vector memory ($0.001)
  RESP=$(curl -s -X POST "$BASE/memory/upsert" \
    -H "Authorization: Bearer $ITERA_KEY" \
    -H "Content-Type: application/json" \
    -d "{
      \"namespace\": \"$USER_ID\",
      \"text\": \"$TEXT\",
      \"metadata\": {\"user\": \"$USER_ID\"}
    }")
  
  MEM_ID=$(echo "$RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get(id, stored))")
  echo "Stored memory: $MEM_ID"

elif [ "$ACTION" = "query" ]; then
  QUESTION="$TEXT"
  echo "Query for $USER_ID: $QUESTION"
  
  # Search relevant memories ($0.001)
  SEARCH_RESP=$(curl -s -X POST "$BASE/memory/search" \
    -H "Authorization: Bearer $ITERA_KEY" \
    -H "Content-Type: application/json" \
    -d "{
      \"namespace\": \"$USER_ID\",
      \"query\": \"$QUESTION\",
      \"top_k\": 3
    }")
  
  MEMORIES=$(echo "$SEARCH_RESP" | python3 -c "
import sys, json
d = json.load(sys.stdin)
results = d.get('results', [])
for r in results:
    print(r.get('text', ''))
")
  echo "Found memories."
  
  # Chat with memory context ($0.005)
  echo "Generating response..."
  CHAT_RESP=$(curl -s -X POST "$BASE/ai/chat" \
    -H "Authorization: Bearer $ITERA_KEY" \
    -H "Content-Type: application/json" \
    -d "{
      \"messages\": [
        {\"role\": \"system\", \"content\": \"You are a helpful assistant. Use these memories about the user:\n$MEMORIES\"},
        {\"role\": \"user\", \"content\": \"$QUESTION\"}
      ]
    }")
  
  echo ""
  echo "=== AI RESPONSE ==="
  echo "$CHAT_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get(content, d.get(message, d)))"

else
  echo "Usage:"
  echo "  bash memory-agent.sh store USER_ID \"fact to remember\""
  echo "  bash memory-agent.sh query USER_ID \"question\""
fi
