---
name: runtime-guardrails
description: Enforce policy at runtime with programmable rails — input, dialog, retrieval, execution, and output — that check, steer, or block LLM behavior independently of the model’s own alignment. Use when the task matches the listed use cases.
---

# Runtime Guardrails

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Security and governance

## Purpose

Enforce policy at runtime with programmable rails — input, dialog, retrieval, execution, and output — that check, steer, or block LLM behavior independently of the model’s own alignment.

## Use when

- Use when a chatbot or agent must stay on-topic and in-policy under adversarial users.
- Use when tool calls need argument validation before anything executes.
- Use when RAG answers must be grounded in retrieved evidence before reaching users.

## Capabilities

- Rail design
- Dialog flows (Colang)
- Self-check classifiers
- Grounding checks
- Latency-aware enforcement

## Workflow

1. Write the policy as explicit rails separated by stage: input, dialog, retrieval, execution, and output.
2. Implement cheap deterministic checks first (patterns, allowlists, schema validation) and reserve model-based self-checks for ambiguous cases.
3. Validate tool-call arguments in execution rails before any side effect runs.
4. Buffer streamed output when output rails must inspect a complete response before release.
5. Log every rail trigger with its reason, and tune false positives on real traffic — a guardrail users route around is not a control.
6. Measure the latency and cost the rails add, and attack-test them with the same adversarial sets used for red teaming.

## Connector references

- `audit-log`

## Provenance and licensing

Derived implementation summary; guardrails are one layer of defense, not a guarantee of safe behavior.

- [NVIDIA NeMo Guardrails repository](https://github.com/NVIDIA-NeMo/Guardrails) — Apache-2.0 open source; this summary is derived, not copied.
- [NeMo Guardrails documentation (in the same repository)](https://github.com/nvidia/nemo-guardrails/blob/HEAD/docs/reference/cli/index.mdx) — Documentation shipped with the Apache-2.0 repository; concepts summarized, no text reproduced.
