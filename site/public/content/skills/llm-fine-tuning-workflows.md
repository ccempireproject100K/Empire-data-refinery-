---
name: llm-fine-tuning-workflows
description: Adapt a model to a narrow task with curated examples, a held-out evaluation, and a rollback plan, instead of tuning on intuition. Use when the task matches the listed use cases.
---

# LLM Fine-Tuning Workflows

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Machine learning

## Purpose

Adapt a model to a narrow task with curated examples, a held-out evaluation, and a rollback plan, instead of tuning on intuition.

## Use when

- Use when prompting plateaus on a stable, well-defined task.
- Use when a smaller tuned model could replace a larger prompted one.
- Use when consistent formatting or classification behavior matters more than generality.

## Capabilities

- Dataset curation
- Train/validation splits
- Run configuration
- Comparative evaluation
- Deployment gating

## Workflow

1. Confirm the task is stable and that prompt and retrieval fixes are exhausted.
2. Curate examples from real failures and successes; remove duplicates and label noise.
3. Hold out an evaluation set the tuning data never touches.
4. Run the smallest training configuration that can show signal.
5. Compare tuned and base models on the held-out set and on cost and latency.
6. Ship behind a gate with monitoring and a one-step rollback to the base model.

## Connector references

- `provider-api`

## Provenance and licensing

Derived workflow; it includes no training data or hyperparameters from any source course.

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) — MIT License; verify the LICENSE file for copied code or text.
- [Hugging Face AI Agents Course — fine-tuning for function calling](https://huggingface.co/learn/agents-course/unit0/introduction) — Course access is free; use a derived summary rather than copying lesson text.
