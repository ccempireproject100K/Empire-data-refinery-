---
name: computer-use-agents
description: Build agents that operate real desktop software through screenshots and accessibility trees, with coordinate grounding, sandboxed virtual machines, and execution-based evaluation. Use when the task matches the listed use cases.
---

# Computer Use Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Tool use

## Purpose

Build agents that operate real desktop software through screenshots and accessibility trees, with coordinate grounding, sandboxed virtual machines, and execution-based evaluation.

## Use when

- Use when a task exists only in GUI applications with no usable API.
- Use when automating legacy desktop or cross-application workflows.
- Use when measuring a model’s desktop competence before trusting it near real machines.

## Capabilities

- Observation design
- Visual grounding
- Action spaces
- VM sandboxing
- Execution-based evaluation

## Workflow

1. Choose the observation mode — screenshot, accessibility tree, set-of-marks overlay, or a combination — and measure the accuracy trade-off on your tasks.
2. Define a small, reliable action space (click, type, scroll, keypress, wait) and ground every action to a visible element.
3. Run the agent inside a disposable virtual machine with snapshots, synthetic data, and no real credentials.
4. Re-observe after every action; treat text trajectory history as the memory, not a growing stack of screenshots.
5. Include feasible tasks and deliberately infeasible ones so refusal and clarification behavior are tested, and gate real-account actions behind human confirmation.
6. Evaluate from final machine state with execution-based checks, and budget steps, time, and cost per task.

## Connector references

- None required.

## Provenance and licensing

Derived summary from the OSWorld benchmark and its published analysis; never point a computer-use agent at real accounts without human confirmation gates.

- [OSWorld repository (XLANG Lab)](https://github.com/xlang-ai/OSWorld) — Apache-2.0 open source; this summary is derived, not copied.
- [OSWorld project page and paper (NeurIPS 2024)](http://osworld-v1.xlang.ai/) — Project page of the Apache-2.0 OSWorld project; findings summarized, no text reproduced.
