---
name: agent-skills-authoring
description: Package reusable agent know-how as a skill folder with a concise SKILL.md, supporting references, and scripts that load only when relevant. Use when the task matches the listed use cases.
---

# Agent Skills Authoring

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent infrastructure

## Purpose

Package reusable agent know-how as a skill folder with a concise SKILL.md, supporting references, and scripts that load only when relevant.

## Use when

- Use when the same procedure is re-explained to agents repeatedly.
- Use when distributing a capability to a team or agent runtime.
- Use when a long prompt should become a maintained, versioned asset.

## Capabilities

- Skill scoping
- Trigger descriptions
- Progressive disclosure
- Reference and script layout
- Skill testing

## Workflow

1. Define one job the skill does and the phrases that should trigger it.
2. Write the smallest useful SKILL.md: purpose, steps, constraints, and output expectations.
3. Move long references and examples into linked files that load on demand.
4. Add scripts only for deterministic steps and document their inputs and side effects.
5. Test the skill on realistic tasks, including cases where it should not trigger.
6. Version the skill and record provenance for every bundled source.

## Connector references

- None required.

## Provenance and licensing

Derived authoring checklist. Audit bundled scripts before trusting any third-party skill.

- [Claude Agent Skills overview](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — Official documentation; use source links rather than copying proprietary text.
- [Agent Skills open format](https://agentskills.io/home) — Open skills format; retain source attribution and verify current specification terms.
