# IteraTools Examples

Real-world examples for the [IteraTools API](https://iteratools.com) — 80+ pay-per-use AI tools for agents and automation.

## Get an API Key
1. Visit [iteratools.com/keys](https://iteratools.com/keys)
2. Add credits (start with $1)
3. Set the env var: `export ITERA_KEY="it-XXXX-XXXX-XXXX"`

## Examples

| # | Folder | What it does | Cost |
|---|--------|--------------|------|
| 01 | [image-pipeline](./01-image-pipeline/) | Generate image + remove background | ~$0.008 |
| 02 | [web-research-agent](./02-web-research-agent/) | Search + scrape + summarize | ~$0.005 |
| 03 | [memory-agent](./03-memory-agent/) | AI agent with persistent memory | ~$0.010 |
| 04 | [document-processing](./04-document-processing/) | Extract PDF + AI summary | ~$0.004 |
| 05 | [browser-automation](./05-browser-automation/) | Screenshot + describe + interact | ~$0.011 |
| 06 | [code-execution](./06-code-execution/) | Run Python in secure sandbox | $0.005 |
| 07 | [text-pipeline](./07-text-pipeline/) | Translate + TTS + sentiment | ~$0.003 |
| 08 | [github-agent](./08-github-agent/) | Search repos + create issues | ~$0.003 |
| 09 | [calendar-scheduling](./09-calendar-scheduling/) | Check availability + schedule | ~$0.003 |
| 10 | [ai-chat-with-tools](./10-ai-chat-with-tools/) | Multi-tool research agent | ~$0.010 |

## Pricing

All tools are pay-per-use. Typical costs:

| Tool | Endpoint | Price |
|------|----------|-------|
| Image Generate (Flux 1.1 Pro) | POST /image/generate | $0.005 |
| Image Fast (Flux Schnell) | POST /image/fast | $0.002 |
| Remove Background | POST /image/rembg | $0.003 |
| Web Search | POST /search | $0.001 |
| Web Scrape | POST /scrape | $0.002 |
| Web Crawl | POST /crawl | $0.010 |
| Screenshot | POST /screenshot | $0.003 |
| PDF Extract | POST /pdf/extract | $0.002 |
| AI Chat (GPT-4o-mini) | POST /ai/chat | $0.005 |
| Text to Speech | POST /tts | $0.001 |
| Translate | POST /translate | $0.002 |
| Summarize | POST /summarize | $0.002 |
| Sentiment Analysis | POST /sentiment | $0.001 |
| Code Execute (sandbox) | POST /code_execute | $0.005 |
| Browser Automation | POST /browser/act | $0.005 |
| Memory Store | POST /memory/upsert | $0.003 |
| Memory Search | POST /memory/search | $0.002 |
| GitHub Issue | POST /github/issue | $0.002 |

## More

- [Full API docs](https://docs.iteratools.com)
- [All 80+ tools](https://iteratools.com/tools/)
- [MCP server](https://www.npmjs.com/package/mcp-iteratools) — use with Claude, Cursor, Cline
- [OpenAPI spec](https://api.iteratools.com/openapi.json)
