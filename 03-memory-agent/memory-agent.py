#!/usr/bin/env python3
"""
memory-agent.py
AI agent with persistent vector memory.
Stores facts, retrieves relevant context, and chats with memory injection.
Cost per query: ~$0.007 (upsert: $0.001 + search: $0.001 + AI chat: $0.005)

Usage:
    export ITERA_KEY="it-XXXX-XXXX-XXXX"
    python3 memory-agent.py
"""

import os
import sys
import requests

API_KEY = os.environ.get("ITERA_KEY")
if not API_KEY:
    sys.exit("Error: Set ITERA_KEY environment variable")

BASE = "https://api.iteratools.com"
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Use a fixed namespace (user ID) for this demo
NAMESPACE = "demo_user_001"


def api(endpoint: str, payload: dict) -> dict:
    resp = requests.post(f"{BASE}{endpoint}", headers=HEADERS, json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()


def store_memory(text: str) -> str:
    """Store a fact in vector memory ($0.001/call)"""
    result = api("/memory/upsert", {
        "namespace": NAMESPACE,
        "text": text,
        "metadata": {"user": NAMESPACE}
    })
    return result.get("id", "stored")


def search_memories(query: str, top_k: int = 3) -> list:
    """Semantic search over stored memories ($0.001/call)"""
    result = api("/memory/search", {
        "namespace": NAMESPACE,
        "query": query,
        "top_k": top_k
    })
    return result.get("results", [])


def chat_with_memory(question: str) -> str:
    """Chat using retrieved memories as context ($0.005/call)"""
    # First, find relevant memories
    memories = search_memories(question)
    memory_text = "\n".join(r.get("text", "") for r in memories)

    # Build messages with memory context
    messages = []
    if memory_text:
        messages.append({
            "role": "system",
            "content": f"You are a helpful assistant. Use this context about the user:\n{memory_text}"
        })
    messages.append({"role": "user", "content": question})

    result = api("/ai/chat", {"messages": messages})
    return result.get("content", result.get("message", str(result)))


# Demo: store some facts, then query
print("=== Memory Agent Demo ===\n")

# Store some facts
facts = [
    "The users