---
name: prompt-evaluation-pipelines
description: Build repeatable evaluation sets and graders that score prompt quality before and after changes reach production. Use when the task matches the listed use cases.
---

# Prompt Evaluation Pipelines

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Quality and governance

## Purpose

Build repeatable evaluation sets and graders that score prompt quality before and after changes reach production.

## Use when

- Use when changing a production prompt, model, or template.
- Use when prompt quality is currently judged by anecdote.
- Use when a team needs a shared quality bar across many prompts.

## Capabilities

- Eval set design
- Grader selection
- Human review sampling
- Regression comparison
- Failure clustering

## Workflow

1. Collect representative inputs, including edge cases and known failures.
2. Define what a good output looks like with a rubric or reference answers.
3. Choose graders: exact checks, model-based scoring, human review, or a mix.
4. Run candidate and baseline prompts on the same frozen set.
5. Cluster failures by cause and fix the largest cluster first.
6. Freeze the set and re-run it on every prompt or model change.

## Connector references

- `audit-log`

## Provenance and licensing

Derived from public course concepts; grader prompts and datasets from sources are not reproduced.

- [Anthropic courses repository — Prompt evaluations course](https://github.com/anthropics/courses) — Public Anthropic course repository; review the repository terms before reusing code or text.
- [Hugging Face AI Agents Course](https://huggingface.co/learn/agents-course/unit0/introduction) — Course access is free; use a derived summary rather than copying lesson text.
