---
name: error-analysis-for-agents
description: Find what is actually broken by reading real agent traces, coding failures into a taxonomy, counting them, and letting the counts — not intuition — choose the fixes and the evals. Use when the task matches the listed use cases.
---

# Error Analysis for AI Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Quality and governance

## Purpose

Find what is actually broken by reading real agent traces, coding failures into a taxonomy, counting them, and letting the counts — not intuition — choose the fixes and the evals.

## Use when

- Use when agent quality has plateaued and nobody can say why.
- Use when deciding which evaluation to build next.
- Use after launch, when real traffic replaces test scenarios.

## Capabilities

- Trace sampling
- Open and axial coding
- Failure taxonomies
- Judge validation
- Failure prioritization

## Workflow

1. Sample around a hundred real traces, including successes, from production or realistic use.
2. Read each trace and write a one-sentence note naming the first upstream failure (open coding).
3. Group the notes into a failure taxonomy (axial coding) and count how often each mode occurs.
4. Build binary pass/fail judges only for the most frequent failure modes — one judge per failure, never a generic quality score.
5. Validate each judge against human labels using true-positive and true-negative rates, not raw agreement, and iterate until it tracks the humans.
6. Fix the most frequent upstream failure first, then repeat the loop; for agents, decompose failures by step (transition analysis) to find where runs leave the rails.

## Connector references

- `audit-log`

## Provenance and licensing

Derived method summary from the linked talks; no transcript text is reproduced. Error analysis is product work — a domain expert should own the labels.

- [Evals, Error Analysis, and Better Prompts — Hamel Husain on How I AI (video)](https://www.youtube.com/watch?v=PgzOBNse2EA) — YouTube standard license — concepts summarized, no content reproduced.
- [How to Build AI Evals — Hamel Husain and Shreya Shankar (video walkthrough)](https://www.youtube.com/watch?v=J7N9FMouSKg) — YouTube standard license — concepts summarized, no content reproduced.
