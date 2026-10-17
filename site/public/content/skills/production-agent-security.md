---
name: production-agent-security
description: Deploy agents with least privilege, auditability, safe tool boundaries, secret hygiene, and incident response. Use when the task matches the listed use cases.
---

# Production Agent Security

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Security and operations

## Purpose

Deploy agents with least privilege, auditability, safe tool boundaries, secret hygiene, and incident response.

## Use when

- Use before connecting an agent to production data or mutating tools.
- Use when reviewing a skill or connector from an unknown source.
- Use when setting up logging, key rotation, or emergency revocation.

## Capabilities

- Threat modeling
- Least privilege
- Secret lifecycle
- Audit logging
- Revocation and recovery

## Workflow

1. Inventory data, tools, credentials, and possible side effects.
2. Grant the minimum permissions required for each task.
3. Keep secrets out of skill files, source code, logs, prompts, and client bundles.
4. Record tool access and security events without logging secret values.
5. Rotate, expire, revoke, and test recovery procedures for credentials.
6. Audit every bundled script and external dependency before activation.

## Connector references

- `secrets-vault`
- `audit-log`

## Provenance and licensing

Security guidance is intentionally conservative. External skills should be audited like software, not trusted because they are labeled educational.

- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — OWASP guidance; retain attribution and verify current terms.
- [Claude Agent Skills security considerations](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — Official documentation; use source links rather than copying proprietary text.
- [Microsoft AI Agents for Beginners repository](https://github.com/microsoft/ai-agents-for-beginners) — MIT repository; verify the LICENSE file for copied code or text.
