---
name: agent-ux-patterns
description: Design interfaces that keep people oriented and in control while an agent works: visible process, honest confidence, permission slips for consequential actions, and graceful failure. Use when the task matches the listed use cases.
---

# Agent UX Patterns

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent UX

## Purpose

Design interfaces that keep people oriented and in control while an agent works: visible process, honest confidence, permission slips for consequential actions, and graceful failure.

## Use when

- Use when shipping a user-facing agent, copilot, or support automation.
- Use when an agent UI feels like a black box and users do not trust its output.
- Use when deciding what an agent may do autonomously versus what needs approval.

## Capabilities

- Capability communication
- Process visibility
- Confidence display
- Approval design
- Failure recovery UX

## Workflow

1. Communicate capabilities and limits up front — intro, suggested actions, progressive disclosure — so users ask for what the agent can actually do.
2. Show the agent’s process (current step, sources, working indicator) instead of a bare spinner; silence reads as failure.
3. Present outcomes as diffs or summaries a person can verify quickly, not as raw logs or walls of text.
4. Gate irreversible or external actions behind a clear permission step, keep a prominent stop control, and design checkpoints because most agent actions have no undo.
5. Communicate uncertainty honestly, look up what can be looked up, and ask at most one clarifying question before acting.
6. On failure, preserve completed work, say plainly what happened and why, and offer a retry that skips finished steps.

## Connector references

- None required.

## Provenance and licensing

Derived pattern summary from the linked talks; no transcript text is reproduced. Design as if there is no undo — for most agent actions, there is not.

- [AgentUI — 5 UI Patterns Every AI Agent App Reuses (video)](https://www.youtube.com/watch?v=NHqGTNLuHK8) — YouTube standard license — concepts summarized, no content reproduced.
- [Designing Agent UX — lecture on agent design patterns and trust (video)](https://www.youtube.com/watch?v=9OdJofTenbc) — YouTube standard license — concepts summarized, no content reproduced.
- [Google A2UI explainer — generative UI for agents (video)](https://www.youtube.com/watch?v=AWtIxcPGhkk) — YouTube standard license — concepts summarized, no content reproduced.
