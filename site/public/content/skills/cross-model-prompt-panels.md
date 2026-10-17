---
name: cross-model-prompt-panels
description: Send the same prompt to several models from different providers through one interface, save the answers side by side, and — for hard calls — let a panel of models advise while one decider model commits. Use when the task matches the listed use cases.
---

# Cross-Model Prompt Panels

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent architecture

## Purpose

Send the same prompt to several models from different providers through one interface, save the answers side by side, and — for hard calls — let a panel of models advise while one decider model commits.

## Use when

- Use when choosing which provider or model deserves a workload, with evidence instead of loyalty.
- Use when a high-stakes answer deserves more than one model’s opinion.
- Use when prompts live as files that should run identically against any model.

## Capabilities

- Provider-prefixed model addressing
- Parallel fan-out
- Side-by-side answer capture
- Panel-and-decider deliberation
- Prompt files as assets

## Workflow

1. Keep prompts as standalone files so the identical text can be sent to any model without copy drift.
2. Address models with explicit provider prefixes so one command can mix providers (and local models) in a single run.
3. Fan the prompt out to the panel in parallel and save every response as its own file for diffing.
4. For decisions, use the board pattern: several models answer as advisors, then one designated decider model reads all answers and commits to a decision with reasons.
5. Record cost, latency, and your verdict per model; repeat on a schedule because provider quality moves.
6. Promote the winning model to the default for that prompt class, and re-run the panel when a new model lands.

## Connector references

- `provider-api`

## Provenance and licensing

Derived pattern summary from the linked public repository; it complements the prompt-evaluation entry in this archive — panels compare live answers, evaluation pipelines score against datasets. No repository text is reproduced.

- [IndyDevDan (disler) — just-prompt repository (MCP server for multi-provider prompting)](https://github.com/disler/just-prompt) — No LICENSE file in the repository — concepts summarized only, no code or text reproduced.
