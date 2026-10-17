---
name: ai-cookbook-complexity-ladder
description: Grow AI systems one rung at a time — augmented LLM call, prompt chain, tool-calling agent, agent harness, multi-agent team — reusing tested cookbook modules at each rung and climbing only when the simpler rung provably fails. Use when the task matches the listed use cases.
---

# AI Cookbook: Climbing the Complexity Ladder

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Foundations

## Purpose

Grow AI systems one rung at a time — augmented LLM call, prompt chain, tool-calling agent, agent harness, multi-agent team — reusing tested cookbook modules at each rung and climbing only when the simpler rung provably fails.

## Use when

- Use when scoping a new AI feature and resisting the urge to start with a multi-agent system.
- Use when teaching a team a shared progression from first LLM call to production agent.
- Use when a stalled agent project needs to be rebuilt from the last rung that worked.

## Capabilities

- Complexity staging
- Workflow pattern reuse
- Knowledge module integration
- MCP server building blocks
- Copy-adapt development

## Workflow

1. Start at rung one: a single LLM call augmented with retrieval or examples. Ship it and measure before climbing.
2. Add prompt chains when one call cannot hold the reasoning; keep each step in the chain inspectable.
3. Introduce tool calling when the system must act on the world, with the chain’s steps becoming the agent’s tools.
4. Wrap the agent in a harness (state, retries, logging, budgets) when it leaves the notebook and meets real users.
5. Split into multiple agents only when a single agent’s context or reliability demonstrably breaks — and keep the cookbook’s knowledge, pattern, and MCP modules as the shared parts bin at every rung.
6. At each rung, copy the closest working recipe and adapt it, instead of designing from a blank file.

## Connector references

- None required.

## Provenance and licensing

Derived summary of the cookbook’s structure and progression (agents, patterns, knowledge, MCP, and tools modules); no cookbook code or text is reproduced.

- [Dave Ebbelaar — ai-cookbook repository](https://github.com/daveebbelaar/ai-cookbook) — MIT License (LICENCE file in the repository, 2025); verify the LICENCE file for copied code or text.
