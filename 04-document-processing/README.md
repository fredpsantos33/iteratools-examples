# 04 — Document Processing

Extract text from a PDF and summarize it with AI.

## What it does
1. Sends a PDF URL to `/pdf/extract` → get full text
2. Sends text to `/ai/chat` (GPT-4o-mini) → get a 3-bullet summary

## Cost per run
| Step | Endpoint | Cost |
|------|----------|------|
| PDF Extract | POST /pdf/extract | $0.002 |
| AI Chat | POST /ai/chat | $0.002 |
| **Total** | | **~$0.004** |

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# Bash
./pdf-extract-and-summarize.sh https://example.com/document.pdf

# Python
python3 pdf-extract-and-summarize.py https://example.com/document.pdf
```
