---
name: multi-agent-orchestration
description: Coordinate specialized agents with explicit roles, handoffs, shared artifacts, and a final synthesis step. Use when the task matches the listed use cases.
---

# Multi-Agent Orchestration

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Agent architecture

## Purpose

Coordinate specialized agents with explicit roles, handoffs, shared artifacts, and a final synthesis step.

## Use when

- Use when independent research or judgment can run in parallel.
- Use when one agent should not hold the entire task context.

## Capabilities

- Role design
- Parallel fan-out
- Map-reduce synthesis
- Failure collection
- Handoff contracts

## Workflow

1. Define one bounded responsibility per agent.
2. Give every agent the same structured output contract.
3. Run independent work in parallel only when state does not conflict.
4. Collect successful and failed results explicitly.
5. Use one reducer to synthesize without silently discarding gaps.

## Connector references

- None required.

## Provenance and licensing

Derived orchestration pattern; it does not include a hidden agent network or credentials.

- [Microsoft AI Agents for Beginners — Multi-AI Agent Systems](https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/how-to-use-a-multi-ai-agent-system/) — Microsoft Learn source; retain attribution and link.
