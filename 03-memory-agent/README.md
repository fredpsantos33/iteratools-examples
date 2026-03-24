# Memory Agent

Build an AI agent with persistent vector memory — store facts, search semantically, and chat with context.

## What this does

1. **`/memory/upsert`** — Store facts/documents in vector DB
2. **`/memory/search`** — Semantic search over stored memories
3. **`/ai/chat`** — Chat with retrieved context injected

## Cost
- Memory upsert: $0.001/call
- Memory search: $0.001/call
- AI chat: $0.005/call
- **Total: ~$0.007 per query**

## Usage

```bash
export ITERA_KEY="it-XXXX-XXXX-XXXX"

# Shell: store a memory
bash memory-agent.sh store "user_123" "Alice loves Python and works at Google"

# Shell: query
bash memory-agent.sh query "user_123" "What programming languages does Alice know?"

# Python: interactive agent
python3 memory-agent.py
```

## Expected Output

```
Stored memory: mem_abc123

Searching relevant memories for: What programming languages does Alice know?
Found 1 relevant memory.

AI Response:
Based on what I know about you, Alice loves Python and works at Google,
so Python is definitely her primary programming language.
```
