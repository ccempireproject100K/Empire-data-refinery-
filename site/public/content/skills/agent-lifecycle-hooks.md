---
name: agent-lifecycle-hooks
description: Attach deterministic scripts to the lifecycle events of a coding agent — before and after tool calls, on notifications, at stop — to block dangerous actions, format output, log everything, and get the agent’s attention (or yours) at the right moment. Use when the task matches the listed use cases.
---

# Agent Lifecycle Hooks

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent infrastructure

## Purpose

Attach deterministic scripts to the lifecycle events of a coding agent — before and after tool calls, on notifications, at stop — to block dangerous actions, format output, log everything, and get the agent’s attention (or yours) at the right moment.

## Use when

- Use when an autonomous coding agent must never run destructive commands (rm -rf, secret-file reads) even in unattended mode.
- Use when every tool call needs an audit trail for debugging or compliance.
- Use when long-running agents should notify you — by sound, speech, or message — only when they finish or need input.

## Capabilities

- Lifecycle event mapping
- Pre-tool guardrails
- Post-tool automation
- Notification and text-to-speech alerts
- Hook payload logging

## Workflow

1. Map the lifecycle events your harness exposes (session start, prompt submit, pre/post tool use, notification, sub-agent stop, session stop) and what each payload contains.
2. Write hooks as small single-file scripts that read the event payload as JSON on stdin and stay fast and deterministic.
3. Put safety in pre-tool hooks: inspect the pending command or file path and block destructive patterns with a non-zero exit before anything executes.
4. Put hygiene in post-tool hooks: auto-format, lint, or test what the agent just changed, and feed failures back.
5. Route notifications to a channel you will actually notice (desktop alert, text-to-speech summary) so unattended runs stay supervised.
6. Log every event with its payload from day one; when an agent surprises you, the hook log is how you reconstruct why.

## Connector references

- `audit-log`

## Provenance and licensing

Derived practice summary from the linked video (page opened and checked) and its companion repository; no transcript or repository text is reproduced.

- [I’m HOOKED on Claude Code Hooks: Advanced Agentic Coding — IndyDevDan (video)](https://www.youtube.com/watch?v=J5B9UGTuNoM) — YouTube standard license — concepts summarized, no content reproduced.
- [IndyDevDan (disler) — claude-code-hooks-mastery repository](https://github.com/disler/claude-code-hooks-mastery) — No LICENSE file in the repository — concepts summarized only, no code or text reproduced.
