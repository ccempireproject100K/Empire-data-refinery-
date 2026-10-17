---
name: embeddings-and-semantic-search
description: Represent text as vectors and retrieve semantically related material while measuring relevance and failure cases. Use when the task matches the listed use cases.
---

# Embeddings and Semantic Search

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Knowledge retrieval

## Purpose

Represent text as vectors and retrieve semantically related material while measuring relevance and failure cases.

## Use when

- Use when keyword search misses relevant concepts.
- Use when building a retrieval layer for documents or skills.

## Capabilities

- Chunking
- Vector representations
- Similarity search
- Metadata filters
- Retrieval evaluation

## Workflow

1. Define the retrieval unit and metadata fields.
2. Chunk documents without destroying meaning or citation boundaries.
3. Generate embeddings with a versioned model.
4. Combine semantic similarity with filters and keyword signals.
5. Evaluate recall, precision, citation coverage, and stale-content behavior.

## Connector references

- `document-store`

## Provenance and licensing

Derived retrieval workflow; vector stores and embedding keys are connector-specific.

- [Google ML Crash Course — Embeddings](https://developers.google.com/machine-learning/crash-course/embeddings) — Public Google developer course; retain the source link and applicable terms.
