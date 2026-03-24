# 10 — AI Chat with Tools

Multi-tool research agent: search the web, scrape pages, and synthesize answers with AI.

## What it does
1. **Web search** — finds top 3 relevant URLs for your query
2. **Scrape** — extracts clean text from each page
3. **AI synthesis** — GPT-4o-mini reads the sources and answers your question

## Cost per run
| Step | Endpoint | Cost |
|------|----------|------|
| Web Search | POST /search | $0.001 |
| Web Scrape (×3) | POST /scrape | $0.006 |
| AI Chat | POST /ai/chat | $0.005 |
| **Total** | | **~$0.012** |

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

python3 multi-tool-agent.py "What are the best practices for building AI agents in 2025?"
python3 multi-tool-agent.py "How does RAG work?"
```
