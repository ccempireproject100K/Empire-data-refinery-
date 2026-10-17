---
name: agent-workflow-patterns
description: Choose and compose predefined workflow patterns — chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer — before reaching for a fully autonomous agent. Use when the task matches the listed use cases.
---

# Agent Workflow Patterns

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent architecture

## Purpose

Choose and compose predefined workflow patterns — chaining, routing, parallelization, orchestrator-workers, and evaluator-optimizer — before reaching for a fully autonomous agent.

## Use when

- Use when a task decomposes into predictable steps that code can orchestrate.
- Use when deciding between a workflow and an autonomous agent.
- Use when a prototype agent is unreliable and needs more deterministic structure.

## Capabilities

- Pattern selection
- Prompt chaining with gates
- Input routing
- Parallel sectioning and voting
- Evaluator-optimizer loops

## Workflow

1. Start with a single augmented model call and add structure only when it measurably helps.
2. Map the task to a pattern: fixed sequence, category routing, independent sections, dynamic decomposition, or a critique loop.
3. Put programmatic checks between chained steps so errors stop early.
4. Give the orchestrator a bounded task list and require a synthesis step.
5. Cap evaluator loops and record the best artifact and its rationale.
6. Promote a workflow to an autonomous agent only when the path cannot be specified in advance.

## Connector references

- None required.

## Provenance and licensing

Derived pattern summary. Pattern names follow the source taxonomy; all workflow steps are rewritten for this archive.

- [Anthropic — Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) — Official Anthropic engineering guidance; use the source link rather than copying text.
- [Anthropic courses repository](https://github.com/anthropics/courses) — Public Anthropic course repository; review the repository terms before reusing code or text.
