# 20/20 Phase One Upgrade Plan

## Goal

Turn the public 20/20 archive into an evidence-backed intelligence layer for people and AI agents, beginning with claim tracing, source metadata, freshness visibility, comparison, and stable read-only API endpoints.

## Implementation approach

- Preserve the existing static JSON research dataset and skills archive.
- Generate `public/evidence.json` from the normalized sector dataset. Each claim receives a stable identifier, claim type, evidence level, related source identifiers, and archive review metadata.
- Add `public/api/openapi.json` as the public contract for read-only API routes.
- Extend `server.js` with read-only `/api/v1/*` endpoints for sectors, claims, sources, search, comparisons, and skills. No authentication, mutation, billing, or secret handling is introduced in this phase.
- Add an Evidence Map route and a Compare route to the client-side application. Sector detail pages show claim-level evidence trails, freshness status, and a compare action.
- Keep public-source URLs and derived research summaries separate from credentials. API responses never return secrets.

## Product behavior

- Every sector exposes a visible archive review date and freshness status; the label will not imply that a source was automatically verified on that date.
- Claim pages distinguish analyst synthesis, provisional model output, measurement plans, and source-linked narrative.
- Source records preserve title, URL, sector relationship, source type, claim count, and review state.
- Search can return sectors, claims, sources, and skills through one stable endpoint.
- Comparison supports up to four sectors and shows their five score pillars, composite score, rank, evidence count, and caveat count.
- Machine consumers can discover the API contract and retrieve JSON without an account.

## Design

### Style options

- Editorial evidence ledger — probability 0.07: a typographic research desk with visible source trails and restrained signal colors.
- Analyst terminal — probability 0.06: dense data panels, monospace labels, and instrument-like status states.
- Civic atlas — probability 0.05: map-like navigation, public-interest annotations, and geographic metaphors.

### Chosen style: Editorial evidence ledger

**Design Movement:** Independent magazine research desk meets public-company annual report.

**Core Principles:** Evidence before flourish; provisional judgment is visibly labeled; every data object has a trail; dense information should remain calm and scannable.

**Color Philosophy:** Navy provides authority and reading contrast, warm paper keeps long-form research human, teal marks verified structure and machine access, and orange marks uncertainty, estimates, and review needs.

**Layout Paradigm:** Long editorial rails with asymmetric source panels; comparison and evidence views use wide tables and side annotations instead of card-only dashboards.

**Signature Elements:** Orange evidence rails, teal status pills, and oversized serif section titles that make a data-heavy product feel like a considered publication.

**Interaction Philosophy:** Search, compare, and trace should expose the reasoning path rather than hide it behind modal interactions.

**Animation:** Use only short hover elevation and smooth route transitions; avoid decorative motion that competes with evidence labels.

**Typography System:** Editorial serif for conclusions and section titles; neutral sans-serif for controls, metadata, and data tables; monospace only for API names and stable identifiers.

**Brand Essence:** A public evidence refinery for strategy teams and AI agents; exacting, useful, transparent.

**Brand Voice:** Headlines are concise and declarative. Microcopy names uncertainty without apology. Example lines: “Trace the claim.” “A score is a map, not a verdict.”

**Wordmark & Logo:** Preserve the existing 20/20 mark: two compact signal bars imply paired vision and a data pipeline.

**Signature Brand Color:** Teal `#4ec9b0`, reserved for machine-readable structure and trustworthy navigation.

## Project structure

- `public/data.json`: normalized sector research dataset.
- `public/evidence.json`: generated claims, sources, and freshness metadata.
- `public/api/openapi.json`: read-only API contract.
- `scripts/build-evidence.py`: deterministic evidence graph generator.
- `server.js`: static server plus read-only API routes.
- `public/app.js`: client-side routes, evidence map, comparison view, and sector trace panels.
- `public/styles.css` and `public/evidence-extra.css`: existing and phase-one visual system.
- `public/manus-routes.json`: page route manifest.

## Constraints

This phase does not add user accounts, private workspaces, automated web crawling, payment, or external API credentials. Freshness is transparent archive metadata until a scheduled source-review pipeline is added.

## Phase two: free-data catalog and ingestion foundation

### Goal

Make the roadmap operational without introducing paid data, secret values, or silent ranking changes. Publish a machine-readable catalog of high-value official datasets, explicit access requirements, metric recipes, and small live samples from keyless public APIs.

### Implementation approach

- Generate `public/data-catalog.json`, `public/data-catalog.md`, and `public/metric-recipes.json` from `scripts/build-catalog.py`.
- Add `scripts/fetch-free-samples.py` for bounded, reproducible sample pulls from keyless official endpoints such as SEC metadata, World Bank indicators, BLS series, Census ACS, openFDA, and ClinicalTrials.gov.
- Store samples in `public/free-data-samples.json` with endpoint, retrieval timestamp, status, and provenance; samples remain separate from the provisional sector rankings until normalized and reviewed.
- Add a `/catalog` page for people and a `/api/v1/catalog` endpoint for agents. The page distinguishes keyless/open sources from sources requiring free registration or an API key.
- Add `free-data-roadmap.md` and the catalog to AI discovery resources. Keep all API keys server-side and out of the repository.

### Phase-two product behavior

- Every catalog entry states publisher, coverage, recommended metrics, sector relevance, access level, update cadence, endpoint or download route, and caveats.
- The live sample layer reports failures rather than substituting simulated values.
- Adding a catalog source does not automatically change sector rank, claims, or score weights.
- Future ingestion can promote reviewed metric records into the evidence graph with units, time period, geography, vintage, and source identifiers.

### Phase-two project structure

- `scripts/build-catalog.py`: deterministic public dataset catalog and metric recipe generator.
- `scripts/fetch-free-samples.py`: bounded official-API sample fetcher with no secret inputs.
- `public/data-catalog.json` and `public/data-catalog.md`: machine-readable and human-readable source catalog.
- `public/metric-recipes.json`: proposed normalized metric definitions and endpoint recipes.
- `public/free-data-samples.json`: latest small live sample pull and provenance.
- `public/app.js`: catalog route and access-state presentation.
- `server.js` and `public/api/openapi.json`: catalog API discovery and read-only endpoint.

### Constraints

No paid data, paywall bypass, temporary trial abuse, or credential harvesting. Sources requiring free registration or an API key remain documented but are not called until the credential is intentionally configured. Live samples are evidence of access and schema, not yet investment-grade normalized metrics.

## Phase three: free data-lab and decision-support layer

The site remains free-only. This layer makes the public catalog more useful without importing paid data or inventing normalized values.

- `/api/v1/metrics` exposes the current metric recipes and keeps them separate from measured values.
- `/api/v1/companies` exposes dossier candidate companies with sector context and optional sector filtering.
- `/api/v1/vintages` exposes source review and freshness metadata.
- `/api/v1/comparability` exposes normalization warnings for currency, periods, denominators, industry codes, and evidence types.
- The Compare workspace includes client-side pillar-weight sensitivity. It calculates a derived sensitivity score while preserving the published rank and composite.
- Future ingestion should add reviewed time-series records only after unit, period, geography, vintage, denominator, and stable-identifier checks pass.

This phase deliberately does not add paid feeds, credential harvesting, automated ranking changes, accounts, billing, or private workspaces.
