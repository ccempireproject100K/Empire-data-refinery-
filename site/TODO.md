# 20/20 Data Refinery — Delivery Checklist

## Searchable research experience
- [x] Provide a public homepage showing the provisional ranked top 20 sectors with concise summaries, rank context, and links to stable detail pages.
- [x] Provide stable, semantic sector detail routes covering each sector’s research, top industries, candidate companies, scores, sources, and caveats.
- [x] Provide client-side full-dataset search across sectors, industries, companies, metrics, source references, and research text.
- [x] Provide interactive filters and sorting for sector rank, industries, companies, score dimensions, evidence strength, and source attributes.

## Evidence and AI-agent access
- [x] Define and visibly explain profitability, lucrativeness, growth, customer quality, and evidence strength.
- [x] Visually and semantically distinguish measured facts from analyst estimates throughout the research.
- [x] Present citation and source links with source metadata, contextual references, and associated caveats.
- [x] Provide stable machine-readable JSON endpoints or downloadable JSON documents containing the full structured dataset.
- [x] Provide downloadable Markdown documents for the full dataset and research content, organized for AI-agent use.

## AI Skills Archive
- [x] Provide a searchable public archive of derived AI-agent skills from free public courses and open documentation.
- [x] Provide stable skill detail pages with level, category, use cases, capabilities, workflows, provenance, license notes, and downloadable `SKILL.md` files.
- [x] Provide machine-readable `/skills.json` and `/connectors.json` resources.
- [x] Keep credential values out of the archive; store only connector names, credential references, required access, and security notes.

## Accessibility and delivery
- [x] Use responsive, accessible, public presentation with semantic HTML, legible typography, keyboard-friendly controls, and no login or paid-data dependency.
- [x] Keep the route manifest synchronized with all public page routes.
- [x] Verify the app listens on the configured preview port and the machine-readable endpoints return valid content.
- [x] Save the completed project as a checkpoint and publish only when explicitly requested or already authorized by project settings.

## Phase-one intelligence upgrade
- [x] Generate stable claim-level evidence records with source relationships, evidence levels, archive review dates, freshness status, and caveat notes.
- [x] Add a public read-only agent API for sectors, claims, sources, search, comparisons, and skills with a discoverable OpenAPI contract.
- [x] Add an Evidence Map route that lets users search claims and inspect their related sources and freshness state.
- [x] Add a sector comparison route supporting up to four sectors with score pillars, rank, evidence counts, and caveat counts.
- [x] Show evidence trails, freshness labels, and comparison actions on sector detail pages without implying automated source verification.
- [x] Run the bounded source-checking update engine and publish an auditable report that flags changed or unreachable sources without silently changing claims or rankings.
- [ ] Once the site is deployed, create the recurring weekly ScheduleTask for the source-checking engine; keep the project Preview-only until the owner explicitly chooses to publish.
- [x] Add a GitHub import guide and refreshed editable export path while preserving the Preview-only deployment choice.
- [x] Exclude every source that failed the latest viewability audit from active sector references, evidence records, public dossier links, and generated dataset exports; preserve the exclusion manifest and audit history for traceability.
- [x] Audit current coverage against major free official databases and publish a prioritized free-data roadmap covering source candidates, sector gaps, schema additions, normalization, freshness, and comparability safeguards.

## Phase-two public data layer
- [x] Publish a machine-readable catalog of high-value official datasets, including publisher, coverage, access level, update cadence, sector relevance, endpoint/download route, recommended metrics, and caveats.
- [x] Add explicit metric recipes and comparability fields for future normalized ingestion; do not alter provisional sector rankings automatically.
- [x] Fetch bounded live samples from keyless official APIs, recording endpoint, retrieval time, status, provenance, and raw sample shape without using simulated values.
- [x] Add a public `/catalog` page and `/api/v1/catalog` endpoint discoverable by AI agents.
- [x] Keep sources requiring free registration or API keys documented but uncalled until credentials are intentionally configured; never commit secret values.

## Free data-lab add-ons
- [x] Expose normalized metric recipes through `/api/v1/metrics` without presenting recipes as measured values.
- [x] Expose candidate companies with sector context through `/api/v1/companies`, with optional sector filtering.
- [x] Expose source freshness and review metadata through `/api/v1/vintages`.
- [x] Expose currency, period, denominator, industry-crosswalk, and evidence-type warnings through `/api/v1/comparability`.
- [x] Add a client-side ranking-sensitivity workspace to Compare so users can adjust pillar weights without overwriting published ranks or composites.
