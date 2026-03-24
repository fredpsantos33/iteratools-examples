# IteraTools API — Examples

> **80+ AI tools. One API key. Pay-per-use.**

[![API Docs](https://img.shields.io/badge/docs-api.iteratools.com-blue)](https://api.iteratools.com/docs)
[![Get API Key](https://img.shields.io/badge/get_key-iteratools.com%2Fkeys-green)](https://iteratools.com/keys)

Real-world, copy-paste ready examples for the [IteraTools API](https://api.iteratools.com).  
Each folder is self-contained with shell (`curl`) and Python examples.

---

## What is IteraTools?

IteraTools is a multi-tool API for AI agents and developers:
- **80+ tools** — image generation, browser automation, web scraping, TTS, OCR, code execution, translation, and more
- **Pay-per-use** — no monthly subscription, pay only for what you call
- **One key** — unified API for dozens of capabilities
- **AI-native** — designed for agents, automations, and pipelines

---

## Quick Start

```bash
# 1. Get your API key at https://iteratools.com/keys
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# 2. Test it
curl -X POST https://api.iteratools.com/translate \
  -H "Authorization: Bearer $ITERA_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello, world!", "target": "pt"}'
```

---

## Examples

| # | Folder | What it does |
|---|--------|-------------|
| 01 | [image-pipeline](./01-image-pipeline/) | Generate image with Flux + remove background |
| 02 | [web-research-agent](./02-web-research-agent/) | Search → scrape → summarize with AI |
| 03 | [memory-agent](./03-memory-agent/) | Agent with persistent vector memory |
| 04 | [document-processing](./04-document-processing/) | Extract PDF text + AI summary |
| 05 | [browser-automation](./05-browser-automation/) | Screenshot pages + describe with vision |
| 06 | [code-execution](./06-code-execution/) | Run Python in secure sandbox + data analysis |
| 07 | [text-pipeline](./07-text-pipeline/) | Translate + TTS + sentiment analysis |
| 08 | [github-agent](./08-github-agent/) | Search repos + analyze + create issues |
| 09 | [calendar-scheduling](./09-calendar-scheduling/) | Check availability + schedule meetings |
| 10 | [ai-chat-with-tools](./10-ai-chat-with-tools/) | Multi-tool AI agent with search + crawl |

---

## Pricing Summary

| Category | Tools | Price/call |
|----------|-------|-----------|
| Utilities | Weather, Translation, QR, DNS, WHOIS | $0.001 |
| Web | Scrape, Search, RSS | $0.002 |
| Media | TTS, OCR, Charts, PDF | $0.003 |
| AI/Generation | Image (Flux), Vision, AI Chat | $0.005 |
| Browser | Playwright (up to 20 actions) | $0.005 |
| Code Execution | E2B sandbox (Python/Node) | $0.005 |

---

## Setup

All examples use the `ITERA_KEY` environment variable:

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"
```

Python examples require only `requests`:

```bash
pip install requests
```

Shell examples require `curl` and `python3` (for JSON parsing).

---

## Links

- 📚 [Full API Docs](https://api.iteratools.com/docs)
- 🔑 [Get API Key](https://iteratools.com/keys)
- 🌐 [IteraTools Website](https://iteratools.com)
