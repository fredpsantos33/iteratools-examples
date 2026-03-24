# Web Research Agent

Chain search → scrape → summarize to research any topic automatically.

## What this does

1. **`/search`** — Search the web for a topic
2. **`/scrape`** — Extract full content from top URLs
3. **`/ai/chat`** — Summarize findings with AI

## Cost
- Search: $0.002/call
- Scrape (×3): $0.006 total
- AI summary: $0.005/call
- **Total: ~$0.013 per research session**

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# Shell version
bash research.sh "latest advances in solar panel efficiency"

# Python version
python3 research.py "latest advances in solar panel efficiency"
```

## Expected Output

```
Searching for: latest advances in solar panel efficiency
Found 5 results

Scraping: https://example.com/solar-news...
Scraping: https://anothersite.com/energy...
Scraping: https://techblog.com/panels...

Generating AI summary...

=== RESEARCH SUMMARY ===
Based on 3 sources, here are the latest advances in solar panel efficiency:
...
```
