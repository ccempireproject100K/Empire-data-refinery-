---
name: agent-planning
description: Break complex goals into observable steps, dependencies, checkpoints, and recovery paths. Use when the task matches the listed use cases.
---

# Agent Planning Patterns

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Reasoning workflows

## Purpose

Break complex goals into observable steps, dependencies, checkpoints, and recovery paths.

## Use when

- Use when a task has multiple dependent actions.
- Use when the agent must pause, resume, or explain progress.

## Capabilities

- Task decomposition
- Dependency mapping
- Checkpoints
- Replanning
- Progress reporting

## Workflow

1. Define the final deliverable and acceptance conditions.
2. Break the goal into minimal verifiable steps.
3. Identify dependencies, permissions, and irreversible actions.
4. Execute one bounded step at a time and inspect results.
5. Replan only when evidence changes the path.

## Connector references

- None required.

## Provenance and licensing

Derived planning checklist for agent workflows.

- [Microsoft AI Agents for Beginners — Planning Design](https://learn.microsoft.com/en-us/shows/ai-agents-for-beginners/what-is-the-ai-agent-planning-design-pattern/) — Microsoft Learn source; retain attribution and link.
