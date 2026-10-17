---
name: mcp-security-practices
description: Deploy MCP clients and servers without confused-deputy, token-passthrough, and consent failures that turn a tool protocol into a privilege-escalation path. Use when the task matches the listed use cases.
---

# MCP Security Practices

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Security and governance

## Purpose

Deploy MCP clients and servers without confused-deputy, token-passthrough, and consent failures that turn a tool protocol into a privilege-escalation path.

## Use when

- Use when an MCP server can act with a user or service authority.
- Use when adding OAuth or remote servers to an agent product.
- Use when reviewing a third-party MCP server before connecting it.

## Capabilities

- Consent design
- Token audience validation
- Session security
- Tool description review
- Server allowlisting

## Workflow

1. Require explicit, per-server user consent before an agent gains new tools.
2. Bind tokens to the server audience; never pass a token through to downstream APIs.
3. Treat tool descriptions and server metadata as untrusted input that can change between sessions.
4. Pin session identifiers to the authenticated user and protect them like credentials.
5. Allowlist servers for sensitive environments and re-review them on update.
6. Log authorization decisions and provide a one-action disconnect for every server.

## Connector references

- `mcp-server`
- `secrets-vault`
- `audit-log`

## Provenance and licensing

Derived from public protocol security guidance; re-check the current MCP specification before each deployment.

- [Model Context Protocol introduction and security guidance](https://modelcontextprotocol.io/introduction) — MCP documentation published under CC BY 4.0 (specification repository transitioning from MIT to Apache-2.0); retain attribution.
- [OWASP Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — OWASP guidance; retain attribution and verify current terms.
