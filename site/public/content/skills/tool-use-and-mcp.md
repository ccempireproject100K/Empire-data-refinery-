---
name: tool-use-and-mcp
description: Connect an AI application to tools, resources, data sources, and workflows through explicit interfaces. Use when the task matches the listed use cases.
---

# Tool Use and MCP

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Agent infrastructure

## Purpose

Connect an AI application to tools, resources, data sources, and workflows through explicit interfaces.

## Use when

- Use when an agent must call APIs or local tools.
- Use when designing a reusable tool server for multiple AI clients.
- Use when documenting tool inputs, outputs, permissions, and failure modes.

## Capabilities

- Tool schemas
- Resource access
- Prompt templates
- MCP server planning
- Permission boundaries

## Workflow

1. Define each tool with a narrow name, purpose, input schema, output schema, and error contract.
2. Separate read-only resources from mutating actions.
3. Require explicit confirmation for consequential actions.
4. Log tool calls without recording secret values.
5. Test malformed inputs, timeouts, partial results, and revoked credentials.

## Connector references

- `mcp-server`

## Provenance and licensing

This skill describes interfaces and safeguards; it does not contain access credentials or runnable third-party integrations.

- [Model Context Protocol introduction](https://modelcontextprotocol.io/introduction) — Open protocol documentation; check the source repository terms before copying text or code.
- [Agent Skills open format](https://agentskills.io/home) — Open skills format; retain source attribution and verify current specification terms.
