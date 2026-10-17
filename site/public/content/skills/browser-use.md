---
name: browser-use
description: Use web browsers safely for navigation, extraction, and reversible interactions while respecting user boundaries. Use when the task matches the listed use cases.
---

# Browser Use

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Tool use

## Purpose

Use web browsers safely for navigation, extraction, and reversible interactions while respecting user boundaries.

## Use when

- Use when information or workflows exist only in a dynamic web app.
- Use when a browser action needs careful confirmation or takeover.

## Capabilities

- Page navigation
- Form interpretation
- State inspection
- User takeover
- Action confirmation

## Workflow

1. Identify the exact page, goal, and consequences of the action.
2. Read visible page state before clicking or submitting.
3. Treat login, payment, legal, medical, government, and destructive steps as protected workflows.
4. Ask for user takeover when secret input or manual interaction is required.
5. Verify the result and report what changed.

## Connector references

- `web-search`

## Provenance and licensing

Derived browser safety workflow; it does not grant access to any user account.

- [Microsoft AI Agents for Beginners — Browser Use](https://github.com/microsoft/ai-agents-for-beginners/tree/main/15-browser-use) — MIT repository; verify the LICENSE file before copying code or text.
