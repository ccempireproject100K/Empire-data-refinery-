---
name: agent-memory
description: Decide what an agent should remember, where it should live, how long it should persist, and how it can be corrected. Use when the task matches the listed use cases.
---

# Agent Memory

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent architecture

## Purpose

Decide what an agent should remember, where it should live, how long it should persist, and how it can be corrected.

## Use when

- Use when an agent needs continuity across tasks.
- Use when memory could contain personal, confidential, or stale information.

## Capabilities

- Working memory
- Long-term memory
- Retrieval policy
- Consent and deletion
- Memory validation

## Workflow

1. Classify information as ephemeral, session, user, or organizational memory.
2. Store only information with a clear future-use justification.
3. Attach source, date, confidence, and owner metadata.
4. Let users inspect, correct, export, and delete memory where applicable.
5. Expire stale or unverified memory and test retrieval quality.

## Connector references

- `document-store`

## Provenance and licensing

Derived memory-governance workflow; storage implementation remains application-specific.

- [Microsoft AI Agents for Beginners — Agent Memory](https://github.com/microsoft/ai-agents-for-beginners/tree/main/13-agent-memory) — MIT repository; verify the LICENSE file before copying code or text.
