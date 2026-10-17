---
name: llm-threat-controls
description: Defend an LLM application against the OWASP Top 10 risks — prompt injection, sensitive disclosure, excessive agency, unsafe outputs, and unbounded consumption — with layered controls. Use when the task matches the listed use cases.
---

# LLM Threat Controls

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Security and governance

## Purpose

Defend an LLM application against the OWASP Top 10 risks — prompt injection, sensitive disclosure, excessive agency, unsafe outputs, and unbounded consumption — with layered controls.

## Use when

- Use when threat-modeling a chatbot, RAG system, or agent before launch.
- Use when a security review needs a shared vocabulary for LLM-specific risks.
- Use when an incident suggests model behavior, not code, was the attack path.

## Capabilities

- Threat enumeration
- Injection defenses
- Output handling controls
- Agency limits
- Consumption budgets

## Workflow

1. Walk the current OWASP LLM Top 10 and mark which risks the system actually exposes.
2. Treat all retrieved and tool-returned text as untrusted data, never as instructions.
3. Validate and encode model output before it reaches browsers, shells, databases, or APIs.
4. Bound agency: least-privilege tools, human approval for irreversible actions, and per-task scopes.
5. Set token, cost, and rate budgets with alerts so consumption attacks surface early.
6. Re-run the review after model, prompt, tool, or data changes and record residual risks.

## Connector references

- `audit-log`
- `secrets-vault`

## Provenance and licensing

Derived control checklist. Rankings change between editions; cite the edition you assessed against.

- [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) — OWASP GenAI Security Project guidance (CC BY-SA 4.0, share-alike); retain attribution and verify the current edition.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — OWASP guidance; retain attribution and verify current terms.
