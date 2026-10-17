---
name: realtime-voice-agents
description: Build speech-to-speech agents that manage turns, interruptions, tool calls, and guardrails within a live audio session. Use when the task matches the listed use cases.
---

# Realtime Voice Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Realtime systems

## Purpose

Build speech-to-speech agents that manage turns, interruptions, tool calls, and guardrails within a live audio session.

## Use when

- Use when an agent must hold a spoken conversation with low latency.
- Use when phone or in-app voice is the primary interface.
- Use when text chat prototypes need a voice counterpart with the same tools.

## Capabilities

- Session design
- Turn and interruption handling
- Voice tool calling
- Streaming guardrails
- Latency budgeting

## Workflow

1. Define the session contract: voice, turn-taking behavior, and when the agent may interrupt or be interrupted.
2. Reuse the same tool definitions as the text agent so behavior stays consistent.
3. Stream partial transcripts and tool results so the conversation never stalls silently.
4. Apply guardrails to both the user audio transcript and the agent responses.
5. Budget latency per stage and degrade gracefully to shorter replies under load.
6. Log transcripts, tool calls, and interruptions for quality review with secrets and personal data masked.

## Connector references

- `provider-api`
- `audit-log`

## Provenance and licensing

Derived design summary; test with real speakers and noisy audio before relying on lab results.

- [OpenAI Agents SDK documentation — realtime agents](https://openai.github.io/openai-agents-python/) — Official OpenAI documentation for an MIT-licensed SDK; retain source links.
- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) — MIT License; verify the LICENSE file for copied code or text.
