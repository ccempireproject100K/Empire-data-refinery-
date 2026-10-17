---
name: smolagents-code-agents
description: Build lightweight agents whose actions are Python code, with sandboxed execution, composable tools, and managed sub-agents. Use when the task matches the listed use cases.
---

# smolagents Code Agents

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Frameworks

## Purpose

Build lightweight agents whose actions are Python code, with sandboxed execution, composable tools, and managed sub-agents.

## Use when

- Use when an agent benefits from loops, variables, and combined tool calls in one step.
- Use when a minimal, readable framework is preferable to a large platform.
- Use when experimenting with code-writing agents before committing to a stack.

## Capabilities

- CodeAgent configuration
- Tool authoring
- Sandbox selection
- Managed agents
- Run inspection

## Workflow

1. Pick CodeAgent for code actions or ToolCallingAgent for native JSON tool calls.
2. Register tools with precise docstrings; the model reads them as its manual.
3. Choose a real sandbox for generated code; the built-in local executor is not a security boundary.
4. Limit authorized imports and steps, and enable planning intervals for long tasks.
5. Add managed agents for specialized subtasks instead of growing one prompt.
6. Inspect runs with traces to find wasted steps and failing tools.

## Connector references

- `provider-api`

## Provenance and licensing

Derived orientation summary. Never run generated code outside a sandbox you control.

- [smolagents documentation — inspecting runs](https://huggingface.co/docs/smolagents/en/tutorials/inspect_runs) — smolagents is Apache-2.0 open source; this summary is derived, not copied.
- [Hugging Face AI Agents Course — smolagents unit](https://github.com/huggingface/agents-course/blob/HEAD/units/en/unit2/smolagents/tool_calling_agents.mdx) — Apache-2.0 course repository; use a derived summary rather than copying lesson text.
