---
name: agent-red-teaming
description: Probe an AI system the way an adversary would — scripted single- and multi-turn attacks with converters, scorers, and repeatable campaigns — before someone less friendly does. Use when the task matches the listed use cases.
---

# Agent Red Teaming

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Security and governance

## Purpose

Probe an AI system the way an adversary would — scripted single- and multi-turn attacks with converters, scorers, and repeatable campaigns — before someone less friendly does.

## Use when

- Use for a pre-launch security assessment of a chatbot, RAG system, or agent.
- Use when testing whether guardrails survive adaptive, multi-turn attacks rather than single prompts.
- Use to regression-test safety after a model, prompt, or tool change.

## Capabilities

- Objective definition
- Attack orchestration
- Prompt converters
- Scoring and attack success rate
- Campaign regression

## Workflow

1. Define objectives, harm categories, and scope in writing, with authorization for the target system — red teaming is sanctioned testing, not improvisation.
2. Map the surface with single-turn probe datasets across categories (leakage, manipulation, policy bypass, agent tool abuse).
3. Escalate to multi-turn strategies — gradual escalation, branching attacks — against the weakest categories, because agents fail across turns, not just within one.
4. Apply converters (encodings, translations, obfuscation, persona shifts) to test how deep the defenses go.
5. Score every response with human or model judges and track attack success rate per category, not a single global number.
6. Store campaigns as reusable datasets and re-run them after every fix or model change, diffing results before shipping.

## Connector references

- `audit-log`

## Provenance and licensing

Derived practice summary for authorized testing only; attack prompts and datasets from the sources are not reproduced.

- [Microsoft PyRIT repository](https://github.com/microsoft/PyRIT) — MIT License; verify the LICENSE file for copied code or text.
- [AI Red Teaming 101 — Microsoft AI Red Team course (video series)](https://www.youtube.com/watch?v=DwFVhFdD2fs) — YouTube standard license — concepts summarized, no content reproduced.
- [NVIDIA garak repository](https://github.com/NVIDIA/garak) — Apache-2.0 open source; this summary is derived, not copied.
