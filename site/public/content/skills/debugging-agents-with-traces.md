---
name: debugging-agents-with-traces
description: Debug agents from their traces — span trees that show every prompt, tool call, and handoff — to localize silent failures, loops, and cost blowups that plain logs never reveal. Use when the task matches the listed use cases.
---

# Debugging Agents with Traces

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Quality and governance

## Purpose

Debug agents from their traces — span trees that show every prompt, tool call, and handoff — to localize silent failures, loops, and cost blowups that plain logs never reveal.

## Use when

- Use when an agent finishes “successfully” but produces wrong results.
- Use when multi-agent runs fail somewhere in the middle and nobody knows where.
- Use when runaway loops burn tokens without raising a single error.

## Capabilities

- Trace instrumentation
- Span-tree reading
- Loop detection
- First-divergence analysis
- Replay debugging

## Workflow

1. Instrument the agent once with an open standard (OpenTelemetry semantic conventions for GenAI) so traces survive framework and vendor changes.
2. Capture inputs, outputs, token counts, latency, and cost on every span — with secrets and personal data masked before storage.
3. On a bad run, read the trace top-down and find the first span whose output diverges from intent; everything downstream of it is symptom, not cause.
4. Check four signals on every incident: latency (p99, not the average), cost per run, error rate, and correctness — an agent can be fast, cheap, error-free, and wrong.
5. Detect loop tax by flagging repeated near-identical tool calls and runs whose cost is a multiple of the median run.
6. Fix at the divergent span, then add that trace to the regression set so the same failure stays fixed.

## Connector references

- `audit-log`

## Provenance and licensing

Derived debugging workflow; traces are production data — apply retention and masking policies before storing or sharing them.

- [LLM Observability From Scratch — traces, spans, and silent failures (video)](https://www.youtube.com/watch?v=NH6wxVUlH10) — YouTube standard license — concepts summarized, no content reproduced.
- [Langfuse repository](https://github.com/langfuse/langfuse) — Open-source observability platform (MIT open-source core; see the repository LICENSE for current terms); this summary is derived, not copied.
- [OpenTelemetry GenAI semantic conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/) — OpenTelemetry documentation (Apache-2.0 project); the conventions evolve — pin a version.
