---
name: agentic-rag
description: Retrieve, rank, cite, and synthesize external information before an agent answers. Use when the task matches the listed use cases.
---

# Agentic RAG

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Knowledge retrieval

## Purpose

Retrieve, rank, cite, and synthesize external information before an agent answers.

## Use when

- Use for research assistants and evidence-aware answers.
- Use when source freshness, provenance, and citation quality matter.
- Use when a knowledge base or document archive must be searched before action.

## Capabilities

- Query decomposition
- Retrieval and reranking
- Citation tracking
- Source quality checks
- Uncertainty reporting

## Workflow

1. Translate the request into searchable sub-questions.
2. Choose an approved source set and record retrieval timestamps.
3. Retrieve primary or authoritative material before secondary commentary.
4. Attach source URLs to claims and distinguish facts from interpretation.
5. Check for contradictions, stale documents, and missing evidence before responding.

## Connector references

- `web-search`
- `document-store`

## Provenance and licensing

Derived from public course concepts and adapted as a compact 20/20 research workflow.

- [Microsoft AI Agents for Beginners — Agentic RAG](https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/what-is-agentic-rag/) — Microsoft Learn source; retain attribution and link.
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) — Course access is free; use a derived summary rather than copying lesson text.
