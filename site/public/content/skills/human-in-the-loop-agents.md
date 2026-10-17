---
name: human-in-the-loop-agents
description: Pause agent execution at consequential moments so a person can approve, edit, or reject the next action, then resume from saved state. Use when the task matches the listed use cases.
---

# Human-in-the-Loop Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Agent architecture

## Purpose

Pause agent execution at consequential moments so a person can approve, edit, or reject the next action, then resume from saved state.

## Use when

- Use before an agent sends, pays, deletes, publishes, or changes records.
- Use when full automation is possible but not yet trusted.
- Use when regulations or policy require a human decision in the loop.

## Capabilities

- Interrupt design
- Approval payloads
- Edit-and-resume flows
- Timeout and expiry policy
- Decision audit trails

## Workflow

1. Classify actions by reversibility and blast radius; only consequential ones interrupt.
2. Persist full state at the interrupt so the run can wait indefinitely.
3. Present the reviewer a compact payload: intent, inputs, expected effect, and alternatives.
4. Support approve, edit, and reject as distinct resume values, not a single yes/no.
5. Expire stale approvals and re-validate state before executing an approved action.
6. Log who decided, what changed, and how long review took.

## Connector references

- `audit-log`

## Provenance and licensing

Derived pattern summary. Human review only helps if reviewers get real context and enough time.

- [LangGraph concepts — human-in-the-loop](https://langchain-ai.github.io/langgraph/concepts/human_in_the_loop/) — LangChain documentation; retain source links and verify current terms.
- [LangChain Academy — Introduction to LangGraph](https://github.com/langchain-ai/langchain-academy) — MIT License; verify the LICENSE file for copied code or text.
