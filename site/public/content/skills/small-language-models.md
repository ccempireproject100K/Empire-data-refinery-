---
name: small-language-models
description: Choose and run small language models for cost, latency, privacy, or offline needs, and verify they are good enough for the assigned task. Use when the task matches the listed use cases.
---

# Small Language Models

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Runtime choices

## Purpose

Choose and run small language models for cost, latency, privacy, or offline needs, and verify they are good enough for the assigned task.

## Use when

- Use when a frontier model is overkill for classification, extraction, or drafting.
- Use when inference must run on-device or inside a private network.
- Use when per-request cost or latency dominates the design.

## Capabilities

- Task-fit assessment
- Model comparison
- Local runtime setup
- Quality spot-checking
- Escalation routing

## Workflow

1. Define the narrow task and the minimum acceptable quality.
2. Benchmark two or three candidate small models on real examples, not vendor demos.
3. Set up the local or hosted runtime with pinned versions and resource limits.
4. Add a router that escalates hard or low-confidence cases to a larger model.
5. Monitor quality drift as inputs change and re-benchmark on a schedule.
6. Document which tasks the small model owns and which it must never take.

## Connector references

- None required.

## Provenance and licensing

Derived summary; benchmark figures from any single course should be re-measured on your own workload.

- [Microsoft Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) — MIT-licensed Microsoft course repository; verify the LICENSE file for copied code or text.
