---
name: deterministic-agent-workflow-harnesses
description: Encode a development process as a versioned workflow of nodes — deterministic steps (tests, scripts, git) mixed with AI steps (plan, implement, review) — so agent runs follow the same sequence, gates, and artifacts every time instead of improvising. Use when the task matches the listed use cases.
---

# Deterministic Agent Workflow Harnesses

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Agent infrastructure

## Purpose

Encode a development process as a versioned workflow of nodes — deterministic steps (tests, scripts, git) mixed with AI steps (plan, implement, review) — so agent runs follow the same sequence, gates, and artifacts every time instead of improvising.

## Use when

- Use when agent output quality varies run to run because the process lives in a prompt instead of a structure.
- Use when a team wants one shared, reviewable definition of "how we build a feature with agents".
- Use when long agent tasks should run unattended and arrive as a finished, validated pull request.

## Capabilities

- Workflow-as-code (YAML)
- Mixed deterministic/AI nodes
- Loop-until-done steps
- Worktree isolation
- Human approval gates

## Workflow

1. Write the process down as a workflow file: named nodes with explicit dependencies — plan, implement, validate, review, approve, publish.
2. Make every step that can be deterministic a plain command (test suite, linter, build) with no model involved; reserve AI nodes for judgment work.
3. Give implementation nodes a loop with an explicit completion condition and a fresh context per iteration, so long tasks do not rot in one endless conversation.
4. Run each workflow in an isolated git worktree so parallel runs and failed runs never contaminate the main checkout.
5. Insert human approval gates at irreversible points (merge, deploy, publish) and let the workflow wait there indefinitely.
6. Commit the workflow files with the project so the process itself is reviewed, versioned, and identical for every runner — CLI, chat, or scheduler.

## Connector references

- None required.

## Provenance and licensing

Derived summary of the Archon project’s documented workflow model; no repository code or text is reproduced.

- [Cole Medin — Archon repository (open-source harness builder for AI coding)](https://github.com/coleam00/Archon) — MIT License; verify the LICENSE file for copied code or text.
