---
name: coding-agent-fleet-observability
description: Stream every hook event from every running coding agent into one store and a live dashboard — sessions, tool calls, handoffs, and lifecycle events — so parallel agent teams stay visible and debuggable instead of chaotic. Use when the task matches the listed use cases.
---

# Coding-Agent Fleet Observability

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Quality and governance

## Purpose

Stream every hook event from every running coding agent into one store and a live dashboard — sessions, tool calls, handoffs, and lifecycle events — so parallel agent teams stay visible and debuggable instead of chaotic.

## Use when

- Use when several agents or sub-agents run in parallel and nobody can say what each one did.
- Use when an agent team produced a bad result and the failure must be reconstructed event by event.
- Use when deciding whether orchestration is actually helping, with counts instead of impressions.

## Capabilities

- Hook event streaming
- Session and source tagging
- Event storage and filtering
- Live multi-agent dashboards
- Handoff tracing

## Workflow

1. Emit an event from a hook at every lifecycle point (pre/post tool, prompt submit, sub-agent start/stop, stop) — hooks are the one place nothing escapes notice.
2. Tag each event with its source application, session, and agent identity before sending it anywhere.
3. POST events to a small collector that appends them to a queryable store (SQLite is enough) in arrival order.
4. Push new events to a web dashboard over a socket so a human can watch the fleet work in real time and filter by agent, session, or event type.
5. When something goes wrong, replay the session’s event stream to find the first wrong tool call or handoff instead of re-reading final code.
6. Keep raw payloads, not just summaries — the argument of the tool call you did not expect is the one that matters.

## Connector references

- `audit-log`

## Provenance and licensing

Derived architecture summary from the linked repository and video (both opened and checked); it complements the trace-debugging entry in this archive with the fleet-level event pipeline. No source text is reproduced.

- [IndyDevDan (disler) — claude-code-hooks-multi-agent-observability repository](https://github.com/disler/claude-code-hooks-multi-agent-observability) — No LICENSE file in the repository — concepts summarized only, no code or text reproduced.
- [Claude Code Multi-Agent Orchestration with Opus 4.6, Tmux and Agent Sandboxes — IndyDevDan (video)](https://www.youtube.com/watch?v=RpUTF_U4kiw) — YouTube standard license — concepts summarized, no content reproduced.
