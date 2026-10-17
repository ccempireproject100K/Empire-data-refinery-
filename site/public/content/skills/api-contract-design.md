---
name: api-contract-design
description: Define stable API inputs, outputs, errors, limits, authentication references, and versioning for agents. Use when the task matches the listed use cases.
---

# API Contract Design

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Connectors

## Purpose

Define stable API inputs, outputs, errors, limits, authentication references, and versioning for agents.

## Use when

- Use when exposing a business capability as an agent tool.
- Use when an API must remain safe and understandable to multiple clients.

## Capabilities

- Schema design
- Error contracts
- Idempotency
- Rate limits
- Versioning

## Workflow

1. Define the smallest useful operation.
2. Specify required and optional fields with examples.
3. Return structured success and failure responses.
4. Document idempotency, pagination, rate limits, and retries.
5. Reference credentials by name and scope, never by value.

## Connector references

- `provider-api`

## Provenance and licensing

Derived API contract checklist; it does not create or store a provider key.

- [Model Context Protocol introduction](https://modelcontextprotocol.io/introduction) — Open protocol documentation; check current source terms.
- [Stripe secret API key best practices](https://docs.stripe.com/keys-best-practices) — Official Stripe documentation; retain source link and do not copy real credentials.
