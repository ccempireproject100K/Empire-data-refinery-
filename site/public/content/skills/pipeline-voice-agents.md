---
name: pipeline-voice-agents
description: Build voice agents as a streaming cascade — voice activity detection, speech-to-text, an agent core, and text-to-speech — with explicit latency budgets and interruption handling. Use when the task matches the listed use cases.
---

# Pipeline Voice Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Realtime systems

## Purpose

Build voice agents as a streaming cascade — voice activity detection, speech-to-text, an agent core, and text-to-speech — with explicit latency budgets and interruption handling.

## Use when

- Use when each voice stage must be chosen, measured, or swapped independently.
- Use when adding voice to an existing text agent without rewriting its logic.
- Use when telephony (SIP/WebSocket) or local and open models are requirements.

## Capabilities

- Pipeline composition
- Endpointing and barge-in
- Latency budgeting
- Telephony integration
- Voice tracing

## Workflow

1. Choose the cascaded pipeline over speech-to-speech deliberately: control and observability per stage versus raw latency.
2. Assemble stages as stream processors (transport, VAD, STT, agent, TTS) with frames flowing between them.
3. Tune voice activity detection and endpointing so turns end naturally and callers can interrupt (barge-in) without losing the thread.
4. Adapt the agent core to voice: make it session-scoped or stateless per turn and keep responses speakable and short.
5. Instrument per-stage latency and word-error rates, set a total response budget, and trace full calls.
6. Test with real noise, accents, crosstalk, and interruptions before trusting lab results.

## Connector references

- `provider-api`
- `audit-log`

## Provenance and licensing

Derived design summary for cascaded voice pipelines; it complements, and does not replace, the speech-to-speech entry in this archive.

- [Pipecat repository (Daily)](https://github.com/pipecat-ai/pipecat) — BSD 2-Clause open source; this summary is derived, not copied.
- [LiveKit Agents repository](https://github.com/livekit/agents) — Apache-2.0 open source; this summary is derived, not copied.
- [Turn Any LangGraph Agent Into a Voice Agent — LangChain (video)](https://www.youtube.com/watch?v=i_Tf956Yh0U) — YouTube standard license — concepts summarized, no content reproduced.
- [Build Advanced AI Agents with LiveKit — freeCodeCamp (video course)](https://www.youtube.com/watch?v=B0TJC4lmzEM) — YouTube standard license — concepts summarized, no content reproduced.
