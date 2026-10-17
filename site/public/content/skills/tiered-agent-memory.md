---
name: tiered-agent-memory
description: Build long-running agent memory as tiers — in-context core blocks, recall history, and archival storage — that the agent pages, edits, and consolidates itself. Use when the task matches the listed use cases.
---

# Tiered Agent Memory

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Agent architecture

## Purpose

Build long-running agent memory as tiers — in-context core blocks, recall history, and archival storage — that the agent pages, edits, and consolidates itself.

## Use when

- Use when an agent must remember users, facts, and prior work across sessions.
- Use when conversations or task histories outgrow the context window.
- Use when personalization needs memory that a human can inspect and correct.

## Capabilities

- Memory tiers
- Self-editing memory blocks
- Paging and eviction
- Archival search
- Memory consolidation

## Workflow

1. Define the tiers (core in-context blocks, recall history, archival store) and what belongs in each.
2. Expose memory to the agent as explicit read/write tools so every change is an auditable action.
3. Set a context-pressure policy: when the window fills, summarize and page material out to archival storage instead of truncating blindly.
4. Give the agent archival and recall search so paged-out material stays reachable.
5. Consolidate offline: merge duplicates, resolve contradictions, and expire stale entries on a schedule.
6. Evaluate with long-horizon probes for recall accuracy and stale-fact errors, and audit what the agent has stored.

## Connector references

- `document-store`

## Provenance and licensing

Derived architecture summary; memory contents are user data and never part of this archive.

- [Letta (formerly MemGPT) repository](https://github.com/letta-ai/letta) — Apache-2.0 open source; this summary is derived, not copied.
- [Stateful Agents — Charles Packer, Letta (AI Engineer talk, video)](https://www.youtube.com/watch?v=E0k9Ppq6yXY) — YouTube standard license — concepts summarized, no content reproduced.
- [MemGPT: Towards LLMs as Operating Systems (paper)](https://arxiv.org/abs/2310.08560) — Research paper on arXiv; concepts summarized, no text reproduced.
