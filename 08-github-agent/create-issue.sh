#!/bin/bash
# Create a GitHub issue from text description
# Cost: $0.002 per issue
API_KEY="${ITERA_KEY:?Set ITERA_KEY}"
REPO="${1:?Usage: $0 <owner/repo> <title> [body]}"
TITLE="${2:?Provide issue title}"
BODY="${3:-Created by IteraTools GitHub agent}"

echo "🐙 Creating GitHub issue in $REPO... (\$0.002)"
curl -s -X POST https://api.iteratools.com/github/issue \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"repo\": \"$REPO\", \"title\": \"$TITLE\", \"body\": \"$BODY\"}" \
  | python3 -c "import sys,json; d=json.load(sys.stdin); print('Issue #' + str(d.get('number')) + ':', d.get('html_url',''))"
