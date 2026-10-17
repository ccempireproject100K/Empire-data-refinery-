---
name: single-file-agents
description: Package each agent as one self-contained, single-purpose Python file with inline dependencies — runnable, shareable, and versionable like a script instead of a project. Use when the task matches the listed use cases.
---

# Single-File Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent architecture

## Purpose

Package each agent as one self-contained, single-purpose Python file with inline dependencies — runnable, shareable, and versionable like a script instead of a project.

## Use when

- Use when an agent does exactly one job (query a database, reshape JSON, summarize a codebase) and must be easy to hand to someone.
- Use when spinning up many small specialist agents beats maintaining one monolith.
- Use when an agent must run in a fresh environment with zero setup ceremony.

## Capabilities

- Single-purpose agent design
- Inline dependency declaration
- CLI-as-interface design
- Provider portability
- Copy-and-version iteration

## Workflow

1. Give the agent one job and one prompt tuned to it; refuse scope creep into a second job — write a second file instead.
2. Declare every dependency in the file header so a single command (uv run) provisions and executes it anywhere.
3. Expose the interface as command-line arguments and environment variables for provider keys; never hardcode secrets.
4. Keep the prompt, tools, and loop in the one file so the agent’s whole behavior can be read in minutes.
5. Iterate by copying the file to a new version rather than mutating the original, so working agents never regress silently.
6. Compose agents by chaining their command-line input and output instead of merging them into a framework.

## Connector references

- None required.

## Provenance and licensing

Derived pattern summary from the linked public repositories; no repository code or text is reproduced.

- [IndyDevDan (disler) — single-file-agents repository](https://github.com/disler/single-file-agents) — No LICENSE file in the repository — concepts summarized only, no code or text reproduced.
- [Dave Ebbelaar — single-file-ai-agent-tutorial repository](https://github.com/daveebbelaar/single-file-ai-agent-tutorial) — MIT License; verify the LICENSE file for copied code or text.
