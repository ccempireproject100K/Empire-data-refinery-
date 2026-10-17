---
name: crawl-to-rag-knowledge-servers
description: Turn websites and documentation into a queryable knowledge base for agents: crawl and chunk the source, embed it into a vector store with source tags, and serve retrieval to any agent through an MCP server. Use when the task matches the listed use cases.
---

# Crawl-to-RAG Knowledge Servers

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Knowledge retrieval

## Purpose

Turn websites and documentation into a queryable knowledge base for agents: crawl and chunk the source, embed it into a vector store with source tags, and serve retrieval to any agent through an MCP server.

## Use when

- Use when a coding assistant must answer from current product or library documentation instead of its training data.
- Use when the same knowledge base should serve many agents and tools through one interface.
- Use when retrieval quality needs upgrading (hybrid search, reranking) in one place, for every consumer.

## Capabilities

- Recursive web crawling
- Structure-aware chunking
- Vector storage with source filtering
- MCP knowledge tools
- Layered retrieval strategies

## Workflow

1. Point the crawler at the source and let it detect the shape — single pages, sitemaps, or plain-text files — then crawl internal links recursively and in parallel.
2. Chunk by document structure (headers first, size second) so each chunk is a meaningful unit, and tag every chunk with its source.
3. Embed chunks into a vector store that supports filtering by source, so queries can be scoped to one site or library.
4. Expose two tools over MCP — crawl/ingest and retrieve — so any connected agent can refresh and query the same knowledge base.
5. Layer retrieval strategies behind the same interface: contextual embeddings, hybrid vector-plus-keyword search, reranking, and specialized extraction for code examples.
6. Re-crawl on a schedule or on demand; a knowledge server whose sources silently age becomes a confident liar.

## Connector references

- `document-store`
- `web-search`

## Provenance and licensing

Derived architecture summary from the linked repository; it complements the agentic RAG entry in this archive with the crawl-and-serve pipeline. No repository code or text is reproduced.

- [Cole Medin — mcp-crawl4ai-rag repository (Crawl4AI RAG MCP Server)](https://github.com/coleam00/mcp-crawl4ai-rag) — MIT License; verify the LICENSE file for copied code or text.
