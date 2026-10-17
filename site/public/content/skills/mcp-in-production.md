---
name: mcp-in-production
description: Run MCP servers as shared production services — remote streamable-HTTP transport, OAuth authorization, stateless scaling, monitoring, and versioning that real clients can rely on. Use when the task matches the listed use cases.
---

# MCP in Production

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Agent infrastructure

## Purpose

Run MCP servers as shared production services — remote streamable-HTTP transport, OAuth authorization, stateless scaling, monitoring, and versioning that real clients can rely on.

## Use when

- Use when graduating a local stdio MCP server to a team or public service.
- Use when web-based agents (not just desktop clients) need your tools.
- Use when operating MCP alongside existing APIs without duplicating them badly.

## Capabilities

- Remote transport
- OAuth 2.1 authorization
- Stateless scaling
- Server observability
- Version and client compatibility

## Workflow

1. Move from stdio to the streamable HTTP transport, and decide explicitly what session state exists and where it lives.
2. Put authorization in front: OAuth 2.1 with scoped tokens and per-user consent, and never forward client tokens to downstream APIs.
3. Deploy statelessly where possible so any instance can serve any request; use durable execution for long-running tool calls.
4. Instrument tool calls with tracing, error rates, and latency, and alert on client-visible failures, not just server errors.
5. Version tools additively, publish a changelog, and test against the major MCP clients before each release.
6. Design tools like APIs — narrow, deterministic, few in number — with clear input schemas, rather than one tool per internal endpoint.

## Connector references

- `mcp-server`
- `secrets-vault`
- `audit-log`

## Provenance and licensing

Derived operations summary; the MCP authorization specification is still evolving — re-check it before each deployment.

- [Build and Ship Any MCP Server — Cole Medin (video)](https://www.youtube.com/watch?v=Zw3sfAIpeH8) — YouTube standard license — concepts summarized, no content reproduced.
- [MCP transports documentation](https://modelcontextprotocol.io/docs/concepts/transports) — MCP documentation (CC BY 4.0); this archive records concepts, not copied passages.
- [MCP Demo Day — Cloudflare engineering blog](https://blog.cloudflare.com/mcp-demo-day/) — Cloudflare engineering blog; production patterns summarized, no text reproduced.
