# 07 — Text Pipeline

Text processing pipeline: translate to any language, generate audio with TTS, and analyze sentiment.

## What it does
- **translate-and-tts**: Translates text and generates an MP3 audio file
- **sentiment-and-summary**: Analyzes sentiment score and summarizes text

## Cost per run
| Step | Endpoint | Cost |
|------|----------|------|
| Translate | POST /translate | $0.002 |
| Text to Speech | POST /tts | $0.001 |
| Sentiment Analysis | POST /sentiment | $0.001 |
| Summarize | POST /summarize | $0.002 |

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# Translate + TTS
./translate-and-tts.sh "Hello world" pt
# → saves output.mp3

# Sentiment + Summary
python3 sentiment-and-summary.py
```
