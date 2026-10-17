---
name: agent-deployment
description: Package, deploy, health-check, scale, and update agent services with clear runtime boundaries. Use when the task matches the listed use cases.
---

# Agent Deployment

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Advanced  
**Category:** Operations

## Purpose

Package, deploy, health-check, scale, and update agent services with clear runtime boundaries.

## Use when

- Use when moving an agent from local development to a hosted service.
- Use when deploying multiple versions or environments.

## Capabilities

- Runtime configuration
- Health checks
- Environment separation
- Scaling
- Release rollback

## Workflow

1. Separate development, staging, and production resources.
2. Declare runtime configuration without embedding secrets.
3. Add unauthenticated health checks and authenticated application routes.
4. Deploy immutable versions and retain rollback targets.
5. Monitor resource use, errors, latency, and external dependency failures.

## Connector references

- `secrets-vault`
- `audit-log`

## Provenance and licensing

Derived deployment checklist; actual hosting and credentials remain environment-specific.

- [Microsoft AI Agents for Beginners — Deploying Scalable Agents](https://github.com/microsoft/ai-agents-for-beginners/tree/main/16-deploying-scalable-agents) — MIT repository; verify the LICENSE file before copying code or text.
