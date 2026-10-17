---
name: programmable-coding-agents
description: Drive a coding agent as a programmable Unix-style utility — headless prompts, tool allowlists, pipes and scripts — so agents slot into shell pipelines, CI, and other programs instead of only interactive chat. Use when the task matches the listed use cases.
---

# Programmable Coding Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Tool use

## Purpose

Drive a coding agent as a programmable Unix-style utility — headless prompts, tool allowlists, pipes and scripts — so agents slot into shell pipelines, CI, and other programs instead of only interactive chat.

## Use when

- Use when an agent step belongs inside a script, cron job, or CI pipeline.
- Use when another program (a bot, a dashboard, a voice interface) must invoke the agent and consume its output.
- Use when the same agent task must run identically across many repositories.

## Capabilities

- Headless agent invocation
- Tool allowlisting
- Pipeline composition
- Cross-language drivers
- Automation triggers

## Workflow

1. Invoke the agent non-interactively with the task as an argument and capture its output as data, not as a transcript to eyeball.
2. Scope every invocation with an explicit tool allowlist (for example write/edit only) so a scripted agent can never exceed its brief.
3. Compose with pipes and files: agent output becomes the next command’s input, in the Unix tradition.
4. Wrap invocations in the host language of the system (shell, JavaScript, Python) and treat failures as exit codes to handle, not surprises.
5. Add triggers deliberately — a schedule, a webhook, a message, a voice command — each with the same allowlist discipline.
6. Keep a human gate in front of destructive or publishing steps no matter how reliable the pipeline feels.

## Connector references

- `provider-api`

## Provenance and licensing

Derived practice summary from the linked video (page opened and checked) and its companion repository; no transcript or repository text is reproduced.

- [AI Coding is NOT ENOUGH: Claude Code’s NEXT LEVEL Agentic Coding FEATURE — IndyDevDan (video)](https://www.youtube.com/watch?v=2TIXl2rlA6Q) — YouTube standard license — concepts summarized, no content reproduced.
- [IndyDevDan (disler) — claude-code-is-programmable repository](https://github.com/disler/claude-code-is-programmable) — No LICENSE file in the repository — concepts summarized only, no code or text reproduced.
