---
name: structured-data-extraction
description: Turn unstructured text and documents into validated records using explicit schemas, constrained outputs, and repair loops. Use when the task matches the listed use cases.
---

# Structured Data Extraction

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Data workflows

## Purpose

Turn unstructured text and documents into validated records using explicit schemas, constrained outputs, and repair loops.

## Use when

- Use when converting emails, invoices, forms, or articles into database records.
- Use when downstream software needs dependable fields, not prose.
- Use when manual data entry from documents is the bottleneck.

## Capabilities

- Schema design
- Constrained generation
- Field validation
- Repair and retry
- Extraction evaluation

## Workflow

1. Define the record schema with types, required fields, and allowed values.
2. Split long documents so each extraction call sees one coherent unit.
3. Request schema-conformant output and validate it programmatically.
4. On validation failure, return the specific errors to the model for one bounded repair attempt.
5. Measure field-level accuracy on a labeled sample before scaling.
6. Route low-confidence records to human review with the source text attached.

## Connector references

- `document-store`
- `provider-api`

## Provenance and licensing

Derived workflow; example schemas from sources are not reproduced.

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) — MIT License; verify the LICENSE file for copied code or text.
