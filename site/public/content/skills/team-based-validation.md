---
name: team-based-validation
description: Pair the agent that plans and builds with independent validator agents — and with plan files that carry their own validation hooks — so work is checked against the spec by something other than the agent that produced it. Use when the task matches the listed use cases.
---

# Team-Based Validation with Self-Checking Plans

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Quality and governance

## Purpose

Pair the agent that plans and builds with independent validator agents — and with plan files that carry their own validation hooks — so work is checked against the spec by something other than the agent that produced it.

## Use when

- Use when a single agent grades its own homework and defects ship with confident summaries.
- Use when plans must contain required sections (tasks, orchestration, verification) before building starts.
- Use when a growing library of specialist sub-agents needs consistent structure and tool discipline.

## Capabilities

- Spec-driven building
- Self-validating plan files
- Independent validator agents
- Task-system orchestration
- Meta-agent generation

## Workflow

1. Require a written spec before building: goal, step-by-step tasks, team roles, and how completion will be verified.
2. Attach validators to the plan itself — hooks that fire when planning stops and check the spec file exists and contains every required section; planning is not done until its own checks pass.
3. Form the team from specialized sub-agents: builders that implement tasks from the spec and validators that check results against it, coordinated through a shared task list.
4. Keep validators independent — they read the spec and the output, never the builder’s reasoning — and loop failures back as new tasks.
5. When the team lacks a role, generate the new sub-agent from a description with a meta-agent that applies the house structure and minimal tool set, instead of hand-writing each one.
6. Treat a passed validation as the definition of done, and archive the spec with the result for audit.

## Connector references

- `audit-log`

## Provenance and licensing

Derived pattern summary from the linked repository’s documented validation system; no repository code or text is reproduced.

- [IndyDevDan (disler) — claude-code-hooks-mastery repository (team-based validation system and meta-agent)](https://github.com/disler/claude-code-hooks-mastery) — No LICENSE file in the repository — concepts summarized only, no code or text reproduced.
