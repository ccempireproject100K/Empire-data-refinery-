---
name: multimodal-prompting
description: Give models images and documents as evidence, structure what they should look for, and verify visual claims before acting on them. Use when the task matches the listed use cases.
---

# Multimodal Prompting

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Beginner  
**Category:** Model literacy

## Purpose

Give models images and documents as evidence, structure what they should look for, and verify visual claims before acting on them.

## Use when

- Use when a task involves screenshots, scans, photos, charts, or PDFs.
- Use when extracting structured facts from visual material.
- Use when a text-only prompt keeps missing information that is visible.

## Capabilities

- Image grounding
- Document triage
- Visual question design
- Cross-checking claims
- Uncertainty reporting

## Workflow

1. State what the model must find, decide, or extract from the visual input.
2. Order and label multiple images or pages so references stay unambiguous.
3. Ask for observations first and conclusions second.
4. Require the model to point to the visual evidence behind each claim.
5. Verify critical values against the source document or a second pass.
6. Record low-confidence readings for human review instead of guessing.

## Connector references

- `document-store`

## Provenance and licensing

Derived summary of public course concepts; no course exercises are reproduced.

- [Anthropic courses repository — API fundamentals](https://github.com/anthropics/courses) — Public Anthropic course repository; review the repository terms before reusing code or text.
- [Microsoft Generative AI for Beginners](https://github.com/microsoft/generative-ai-for-beginners) — MIT-licensed Microsoft course repository; verify the LICENSE file for copied code or text.
