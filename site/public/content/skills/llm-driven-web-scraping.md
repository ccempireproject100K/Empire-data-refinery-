---
name: llm-driven-web-scraping
description: Extract structured data from websites with an LLM in the loop — define the schema first, fetch and clean pages, let the model extract against the schema, and escalate to a browsing agent only for pages that fight back. Use when the task matches the listed use cases.
---

# LLM-Driven Web Scraping

> Derived archive skill. This file summarizes public sources and does not reproduce source-course text.

**Level:** Intermediate  
**Category:** Knowledge retrieval

## Purpose

Extract structured data from websites with an LLM in the loop — define the schema first, fetch and clean pages, let the model extract against the schema, and escalate to a browsing agent only for pages that fight back.

## Use when

- Use when a site has no API and its layout changes too often for hand-written selectors.
- Use when the target data is semantic (prices with conditions, specs, reviews) rather than tidy tables.
- Use when a research agent needs web facts in a strict, citable shape.

## Capabilities

- Schema-first extraction
- Page cleaning for models
- Structured output validation
- Auth and CAPTCHA escalation
- Browser-agent fallback

## Workflow

1. Write the output schema before touching the site: fields, types, and what counts as missing.
2. Pick the cheapest method that can work per site — plain fetch and parse first, LLM extraction second, a full browsing agent last.
3. Convert pages to clean text or markdown and trim navigation and boilerplate before anything reaches the model; tokens spent on menus buy nothing.
4. Extract against the schema with structured output, then validate programmatically and retry or flag failures instead of accepting near-misses.
5. Handle login walls and CAPTCHAs by escalating deliberately — an authenticated session or a browsing agent — and record which sites required it.
6. Cache the raw pages so extraction can be re-run when the schema improves, without re-crawling.

## Connector references

- `web-search`

## Provenance and licensing

Derived practice summary from the linked video (page opened and checked, including its method overview and chapter structure); no transcript text is reproduced.

- [This is how I scrape 99% websites via LLM — AI Jason (Jason Zhou) (video)](https://www.youtube.com/watch?v=7kbQnLN2y_I) — YouTube standard license — concepts summarized, no content reproduced.
