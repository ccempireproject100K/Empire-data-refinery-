---
name: framework-free-agent-loop
description: Build a complete working agent in a single short Python file with no framework — a message list, typed tool definitions, and a loop — so every mechanic of agency is visible and understood. Use when the task matches the listed use cases.
---

# Framework-Free Agent Construction

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Beginner  
**Category:** Foundations

## Purpose

Build a complete working agent in a single short Python file with no framework — a message list, typed tool definitions, and a loop — so every mechanic of agency is visible and understood.

## Use when

- Use when learning how agents actually work beneath framework abstractions.
- Use when a prototype must be debuggable line by line.
- Use when auditing what a framework does on your behalf before adopting it.

## Capabilities

- Agent loop mechanics
- Tool definition and dispatch
- Conversation state handling
- Error feedback to the model
- Single-file execution with inline dependencies

## Workflow

1. Declare dependencies inline in the script header (uv-style) so the file runs anywhere with one command and no environment setup.
2. Define a small set of tools (read a file, list a directory, edit a file) as schemas the model can call.
3. Keep the whole conversation as one growing message list; that list is the agent’s entire memory.
4. Loop: send messages plus tool definitions to the model, execute any tool calls it returns, append the results, and repeat until it answers without calling a tool.
5. Return tool errors to the model as messages so it can correct itself instead of crashing the run.
6. Log every tool call and result; when the loop misbehaves, the log is the explanation.

## Connector references

- None required.

## Provenance and licensing

Derived summary of the tutorial repository (which credits Thorsten Ball’s "How to Build an Agent" as its basis); no tutorial code or text is reproduced.

- [Dave Ebbelaar — single-file-ai-agent-tutorial repository](https://github.com/daveebbelaar/single-file-ai-agent-tutorial) — MIT License; verify the LICENSE file for copied code or text.
