#!/bin/bash
# generate-and-remove-bg.sh
# Generate image with Flux 1.1 Pro + remove background
# Cost: ~$0.008 total (image: $0.005 + rembg: $0.003)
#
# Usage: bash generate-and-remove-bg.sh "your prompt here"

set -e

ITERA_KEY="${ITERA_KEY:?Set ITERA_KEY environment variable}"
PROMPT="${1:-a golden retriever puppy on a white surface}"
BASE="https://api.iteratools.com"

echo "Generating image..."
echo "Prompt: $PROMPT"

# Step 1: Generate image with Flux 1.1 Pro ($0.005)
IMAGE_RESP=$(curl -s -X POST "$BASE/image/generate" \
  -H "Authorization: Bearer $ITERA_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"$PROMPT\", \"width\": 1024, \"height\": 1024}")

IMAGE_URL=$(echo "$IMAGE_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['url'])")
echo "Image URL: $IMAGE_URL"

# Step 2: Remove background with rembg ($0.003)
echo ""
echo "Removing background..."

REMBG_RESP=$(curl -s -X POST "$BASE/image/remove-bg" \
  -H "Authorization: Bearer $ITERA_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"url\": \"$IMAGE_URL\"}")

RESULT_URL=$(echo "$REMBG_RESP" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['url'])")
echo "Transparent PNG: $RESULT_URL"

echo ""
echo "Done!"
