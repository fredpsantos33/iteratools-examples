#!/bin/bash
# Translate text to another language and generate audio
# Cost: ~$0.003 per run
API_KEY="${ITERA_KEY:?Set ITERA_KEY}"
TEXT="${1:-Hello, I am an AI agent built with IteraTools.}"
LANG="${2:-pt}"

echo "🌍 Translating to $LANG... (\$0.002)"
TRANSLATED=$(curl -s -X POST https://api.iteratools.com/translate \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"$TEXT\", \"target_language\": \"$LANG\"}" \
  | python3 -c "import sys,json; print(json.load(sys.stdin).get('translated_text',''))")

echo "Translated: $TRANSLATED"

echo "🔊 Generating audio... (\$0.001)"
curl -s -X POST https://api.iteratools.com/tts \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"$TRANSLATED\", \"voice\": \"pt-BR-FranciscaNeural\"}" \
  | python3 -c "import sys,json,base64; d=json.load(sys.stdin); open('output.mp3','wb').write(base64.b64decode(d.get('audio_base64','')))" \
  && echo "✅ Audio saved to output.mp3"
