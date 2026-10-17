---
name: openai-agents-sdk
description: Build agents from a small set of primitives — agents, tools, handoffs, guardrails, sessions, and built-in tracing. Use when the task matches the listed use cases.
---

# OpenAI Agents SDK Orientation

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Frameworks

## Purpose

Build agents from a small set of primitives — agents, tools, handoffs, guardrails, sessions, and built-in tracing.

## Use when

- Use when standardizing on the OpenAI Agents SDK for a Python or TypeScript service.
- Use when a prototype built on raw API calls needs structure without a heavy framework.
- Use when handoffs between specialist agents are the main design problem.

## Capabilities

- Agent configuration
- Function tools
- Handoffs and agents-as-tools
- Input and output guardrails
- Trace review

## Workflow

1. Define each agent with one responsibility, its instructions, and its tools.
2. Model delegation explicitly: handoffs for full transfer, agents-as-tools for bounded subtasks.
3. Add input and output guardrails that run alongside the agent loop.
4. Attach a session store when conversations must persist across runs.
5. Run representative tasks and inspect traces before tuning prompts.
6. Keep a raw-API fallback path for steps the SDK abstracts awkwardly.

## Connector references

- `provider-api`
- `audit-log`

## Provenance and licensing

Derived orientation summary; SDK APIs change quickly, so verify against the linked documentation.

- [OpenAI Agents SDK documentation](https://openai.github.io/openai-agents-python/) — Official OpenAI documentation for an MIT-licensed SDK; retain source links.
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) — MIT License; verify the LICENSE file for copied code or text.
