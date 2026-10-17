---
name: llamaindex-data-agents
description: Build agents over private data with LlamaIndex indexing, query tools, and workflow events that keep retrieval auditable. Use when the task matches the listed use cases.
---

# LlamaIndex Data Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Frameworks

## Purpose

Build agents over private data with LlamaIndex indexing, query tools, and workflow events that keep retrieval auditable.

## Use when

- Use when an agent must answer and act over a document collection.
- Use when retrieval quality, not the chat loop, is the hard part.
- Use when a RAG prototype needs tool use and multi-step workflows.

## Capabilities

- Index design
- Query engines as tools
- Workflow events
- Retrieval evaluation
- Source attribution

## Workflow

1. Inventory the corpus and decide chunking, metadata, and refresh cadence.
2. Build indexes per collection so permissions and provenance stay separable.
3. Expose query engines as named tools with narrow descriptions.
4. Compose multi-step behavior as explicit workflow events rather than hidden chains.
5. Evaluate retrieval separately from answer quality so failures are attributable.
6. Attach source references to every answer the agent produces.

## Connector references

- `document-store`
- `web-search`

## Provenance and licensing

Derived orientation summary; verify current LlamaIndex APIs against the project documentation before building.

- [Hugging Face AI Agents Course — frameworks unit (LlamaIndex)](https://huggingface.co/learn/agents-course/unit0/introduction) — Apache-2.0 course repository; use a derived summary rather than copying lesson text.
