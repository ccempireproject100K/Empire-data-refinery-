---
name: api-integration-and-secrets
description: Document API requirements safely while keeping secret values in a protected server-side environment. Use when the task matches the listed use cases.
---

# API Integration and Secrets

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Connectors

## Purpose

Document API requirements safely while keeping secret values in a protected server-side environment.

## Use when

- Use when an agent skill needs an external API.
- Use when publishing a connector catalog for humans or agents.
- Use when replacing a leaked, expired, or over-permissioned key.

## Capabilities

- API contract mapping
- Credential-name references
- Scope planning
- Key rotation
- Failure-safe integration

## Workflow

1. Record the provider, endpoint family, required scopes, rate limits, and data handling rules.
2. Reference a credential by environment-variable or vault name only.
3. Use restricted or read-only credentials when possible.
4. Keep secret values server-side and out of public pages, skills, prompts, logs, and repositories.
5. Define expiration, rotation, revocation, monitoring, and incident-response steps.

## Connector references

- `provider-api`
- `secrets-vault`

## Provenance and licensing

This catalog stores connector metadata, never API key values.

- [Stripe secret API key best practices](https://docs.stripe.com/keys-best-practices) — Official Stripe documentation; retain source link and do not copy real credentials.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — OWASP guidance; retain attribution and verify current terms.
- [Model Context Protocol introduction](https://modelcontextprotocol.io/introduction) — Open protocol documentation; check current source terms.
