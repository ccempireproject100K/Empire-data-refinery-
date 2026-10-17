---
name: mcp-server-development
description: Implement a Model Context Protocol server that exposes tools, resources, and prompts with validated inputs and a deliberately chosen transport. Use when the task matches the listed use cases.
---

# MCP Server Development

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent infrastructure

## Purpose

Implement a Model Context Protocol server that exposes tools, resources, and prompts with validated inputs and a deliberately chosen transport.

## Use when

- Use when wrapping an internal system for use by multiple AI clients.
- Use when a tool integration should outlive any single agent framework.
- Use when exposing read-only data separately from mutating actions.

## Capabilities

- Server scaffolding
- Tool and resource handlers
- Transport selection
- Input validation
- Inspector testing

## Workflow

1. Inventory the capabilities and split them into tools (actions), resources (data), and prompts (templates).
2. Define schemas for every input and output before writing handlers.
3. Implement handlers with least-privilege credentials held server-side.
4. Choose stdio for local clients or streamable HTTP for shared deployment, and configure authentication accordingly.
5. Test with the MCP Inspector and at least one real client before release.
6. Version the server and log calls without recording secret values.

## Connector references

- `mcp-server`
- `secrets-vault`

## Provenance and licensing

Derived build checklist. The protocol evolves through dated revisions; pin the revision you implement.

- [Model Context Protocol introduction](https://modelcontextprotocol.io/introduction) — MCP documentation published under CC BY 4.0 (specification repository transitioning from MIT to Apache-2.0); retain attribution.
