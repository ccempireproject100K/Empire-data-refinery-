---
name: agent-cost-optimization
description: Cut agent inference cost with measurement first, then the levers that actually move it: cache-stable prompts, model routing and cascades, semantic caching, context pruning, and hard budgets. Use when the task matches the listed use cases.
---

# Agent Cost Optimization

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Operations

## Purpose

Cut agent inference cost with measurement first, then the levers that actually move it: cache-stable prompts, model routing and cascades, semantic caching, context pruning, and hard budgets.

## Use when

- Use when an agent’s per-task cost is unknown, or climbing faster than usage.
- Use when long multi-turn sessions get quadratically more expensive.
- Use when choosing between hosted models, smaller models, and self-hosting.

## Capabilities

- Cost accounting
- Prompt-cache hygiene
- Model routing
- Semantic caching
- Budget enforcement

## Workflow

1. Instrument cost per run, per step, and per successful task before optimizing anything — and keep quality metrics next to cost in the same dashboard.
2. Keep system prompts, tool definitions, and few-shot blocks byte-stable so provider prefix caches hit, and push dynamic content as late in the prompt as possible.
3. Route by difficulty: small models for easy steps, cascades that escalate only on low confidence, and measure quality per tier so routing never silently degrades output.
4. Add semantic caching for repeated or near-duplicate questions, and batch APIs for work that is not interactive.
5. Cap output tokens, prune accumulated context, and summarize history on long tasks — history is usually the largest line item.
6. Set per-agent budgets and alerts with a kill switch, and re-run the eval suite after every cost change so savings are never bought with silent quality loss.

## Connector references

- `provider-api`
- `audit-log`

## Provenance and licensing

Derived optimization playbook; savings figures quoted by any single source are workload-specific — re-measure on your own traffic.

- [RouteLLM repository (LMSYS)](https://github.com/lm-sys/RouteLLM) — Apache-2.0 open source; this summary is derived, not copied.
- [LiteLLM repository (BerriAI)](https://github.com/BerriAI/litellm) — MIT License for the open-source core (the enterprise/ directory carries separate terms); verify the LICENSE file for copied code or text.
- [AI Engineer Masterclass — Cut Your AI Bill (video)](https://www.youtube.com/watch?v=RoD2JE9LN_w) — YouTube standard license — concepts summarized, no content reproduced.
- [Prefix Caching for LLM cost reduction — practitioner walkthrough (video)](https://www.youtube.com/watch?v=9u83yR1YxwE) — YouTube standard license — concepts summarized, no content reproduced.
