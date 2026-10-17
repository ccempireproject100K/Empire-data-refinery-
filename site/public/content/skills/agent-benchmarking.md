---
name: agent-benchmarking
description: Design and read agent benchmarks honestly — executable task suites with deterministic resets, state-based graders, and consistency metrics — instead of trusting headline scores. Use when the task matches the listed use cases.
---

# Agent Benchmarking

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Quality and governance

## Purpose

Design and read agent benchmarks honestly — executable task suites with deterministic resets, state-based graders, and consistency metrics — instead of trusting headline scores.

## Use when

- Use when comparing agents or models for a real workload.
- Use when building an internal task suite that mirrors your product.
- Use when a public leaderboard claim needs scrutiny before it drives a decision.

## Capabilities

- Task suite design
- Executable grading
- Environment fidelity
- Consistency metrics
- Contamination control

## Workflow

1. Define tasks from real work, each with an unambiguous, checkable end state.
2. Make environments resettable and reproducible, and grade from final state (files, database, UI) rather than from the transcript.
3. For conversational agents, add a simulated user with a policy to follow, and verify both the dialogue constraints and the end state.
4. Run multiple trials and report pass@k (any success) alongside pass^k (success on every trial) so consistency is visible, not hidden.
5. Hold out refreshed and private tasks, and rotate them, to detect contamination and overfitting to the suite.
6. Publish cost, latency, step counts, and failure breakdowns next to every score.

## Connector references

- None required.

## Provenance and licensing

Derived summary of benchmark design practice from the linked open benchmark repositories; benchmark tasks and data are not reproduced.

- [SWE-bench repository](https://github.com/princeton-nlp/SWE-bench) — MIT License; verify the LICENSE file for copied code or text.
- [tau-bench repository (Sierra)](https://github.com/sierra-research/tau-bench) — MIT License; verify the LICENSE file for copied code or text.
- [OSWorld repository (XLANG Lab)](https://github.com/xlang-ai/OSWorld) — Apache-2.0 open source; this summary is derived, not copied.
