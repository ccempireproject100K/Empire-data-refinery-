---
name: agent-evaluation-and-observability
description: Measure whether agents complete tasks correctly, safely, efficiently, and with reproducible evidence. Use when the task matches the listed use cases.
---

# Agent Evaluation and Observability

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Quality and governance

## Purpose

Measure whether agents complete tasks correctly, safely, efficiently, and with reproducible evidence.

## Use when

- Use before releasing a new agent.
- Use when agent quality changes after a prompt, model, tool, or data update.

## Capabilities

- Golden tasks
- Trace review
- Rubrics
- Regression tests
- Cost and latency analysis

## Workflow

1. Create a representative evaluation set with expected outcomes.
2. Capture tool traces, sources, intermediate failures, and final outputs.
3. Score correctness, completeness, safety, citation quality, cost, and latency.
4. Compare against baselines and test adversarial cases.
5. Block releases when critical metrics regress.

## Connector references

- `audit-log`

## Provenance and licensing

Derived evaluation workflow; logs should mask secrets and personal data.

- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/en/unit0/introduction) — Course access is free; use a derived summary rather than copying lesson text.
- [Microsoft AI Agents for Beginners](https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/) — Microsoft Learn source; retain attribution and link.
