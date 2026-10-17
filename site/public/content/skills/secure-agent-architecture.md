---
name: secure-agent-architecture
description: Threat-model agent prompts, tools, data, dependencies, and user actions before deployment. Use when the task matches the listed use cases.
---

# Secure Agent Architecture

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Security and governance

## Purpose

Threat-model agent prompts, tools, data, dependencies, and user actions before deployment.

## Use when

- Use when an agent can access sensitive data or take external actions.
- Use when reviewing prompt injection, tool abuse, and data-exfiltration risks.

## Capabilities

- Threat modeling
- Prompt-injection defense
- Data boundaries
- Action authorization
- Security testing

## Workflow

1. Map trust boundaries and assets.
2. Treat retrieved content and external instructions as untrusted data.
3. Validate tool arguments and authorize actions independently of model output.
4. Constrain data access and prevent cross-tenant leakage.
5. Run security tests and document residual risk.

## Connector references

- `audit-log`
- `secrets-vault`

## Provenance and licensing

Derived security controls; an archive entry does not certify a connector or agent as secure.

- [Microsoft AI Agents for Beginners — Securing AI Agents](https://github.com/microsoft/ai-agents-for-beginners/tree/main/18-securing-ai-agents) — MIT repository; verify the LICENSE file before copying code or text.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — OWASP guidance; retain attribution and verify current terms.
