# 20/20 Data Refinery — Improvement Roadmap

This roadmap states what the refinery has, what it does not have yet, and the
order in which the gaps close. It **extends** the documents that already govern
the project; it does not replace or contradict them:

- `synthesis/20-20-sector-research-synthesis.md` — the screening framework:
  §2 (methodology tiers, five-pillar score, normalization rules), §5
  (free-source data plan), §8 (limitations + recommended 90-day program),
  Appendix A (evidence labeling standard).
- `site/FREE-DATA-ROADMAP.md` — the free-source audit, the prioritized source
  list, the data-model additions, and the Phase A/B/C implementation order.
- `site/plan.md` — the phase-one upgrade plan (evidence layer + read-only API)
  that the current site already implements.
- `site/TODO.md` — the delivery checklist and the project's Preview-only
  status.

Voice rule, same as the rest of the corpus: estimates are labeled as
estimates, forecasts are never presented as results, and no claim in this
document should be read as stronger than its evidence.

---

## 1. Where things stand (baseline, 2026-10-16)

An honest inventory, because every later tier is measured against it.

- **Corpus.** 20 sector reports (`reports/`), one synthesis framework
  (`synthesis/`), and a working website export (`site/`): static front end +
  Node server, searchable sector pages, a claim-level evidence graph
  (270 claims, 54 active viewable source records at the last audit recorded in
  `site/FREE-DATA-ROADMAP.md`), a read-only agent API with an OpenAPI
  contract, and the AI Skills Archive.
- **Scores are provisional — by design, and correctly so.** The five-pillar
  composite (synthesis §2.2: 0.35P + 0.25O + 0.20G + 0.10C + 0.10E) is
  currently analyst judgment applied to narrative evidence of 2023–2025
  vintage. No standardized dataset sits underneath it yet. The synthesis
  itself says so (§8: the ordering allocates research time, not capital).
- **Coverage is uneven.** Per the audit in `site/FREE-DATA-ROADMAP.md`, four
  sectors have **zero** active source references (financial services and
  fintech; biotechnology and life sciences; energy and utilities; food,
  beverage and agriculture) and two have one (technology and software;
  industrial manufacturing and robotics). Several dossiers have company lists
  but no structured metrics.
- **Ingestion is a roadmap plus samples, not a system.** 17 official datasets
  are cataloged (`site/public/data-catalog.json`); metric recipes are exposed
  (`/api/v1/metrics`) as recipes, not measured values; bounded live samples
  from keyless APIs exist (`/api/v1/samples`) with provenance recorded. There
  is no time-series store and no scheduled ingestion yet.
- **Source checking has run, but is not scheduled.** The bounded checker, the
  exclusion manifest, and the review queue all exist. The single unchecked
  item in `site/TODO.md` is the recurring weekly ScheduleTask for the
  source-checking engine, to be created once the site is deployed.
- **Skills archive is a starter shelf.** 20 derived entries
  (`site/public/content/skills/`), each compact: level, category, use cases,
  capabilities, workflow, provenance, license notes. No worked examples, no
  executable artifacts, no tests, no quality scores yet.
- **Publication status: Preview-only**, by the owner's choice (`site/TODO.md`).
  Nothing in this roadmap changes that status; publishing is an owner
  decision (see §8).

## 2. Tier A — Make it real

Goal: replace judgment-over-narrative inputs with reproducible, dated, sourced
data underneath the scores, following the priorities already set in
`site/FREE-DATA-ROADMAP.md` and the data plan in synthesis §5.

- **A1. Ingestion, in the roadmap's Phase A order.** SEC EDGAR/XBRL company
  facts → BEA GDP-by-industry and input-output → BLS employment, wages, PPI,
  productivity → EIA energy and emissions → CMS + ClinicalTrials.gov +
  openFDA (healthcare/biotech) → CFPB complaints (finance) → USDA (food and
  agriculture). The remaining cataloged datasets follow by sector-gap
  priority: zero- and one-source sectors first.
- **A2. Time-series storage.** Implement the model proposed in
  `site/FREE-DATA-ROADMAP.md`: `metric_id`, sector / industry / company,
  value, unit, period start/end, geography, `source_id`, `retrieved_at`,
  `vintage`. A revision is a new record; historical vintages are never
  overwritten silently.
- **A3. Recipes before values.** Ingestion populates only metrics defined by
  the existing metric recipes. Every metric carries a definition, unit,
  population, time period, and comparability note before its first value is
  published — an official dataset is not automatically a ranking-grade metric
  (roadmap caveat, carried forward).
- **A4. Key discipline.** Free-but-keyed sources (BEA, EIA) keep their keys
  server-side only, never in source code or public JSON — the existing rule
  in `site/TODO.md`, restated because ingestion makes it load-bearing.
- **A5. Weekly source-check scheduling.** Close the open `site/TODO.md` item:
  once the site is deployed, create the recurring weekly ScheduleTask for the
  source-checking engine. Its output is the auditable update report plus
  review-queue deltas. Existing rule preserved: a recovered source is never
  auto-promoted, and no claim or score changes without a review record.
- **A6. Dataset versioning and a "what changed" feed.** Every ingestion run
  mints a dataset version; `data.json` and `evidence.json` carry version and
  vintage metadata. A changelog feed — machine-readable JSON plus a human
  page — lists added/revised metrics, changed or excluded sources, and claim
  changes for each version. A score may change only with the dataset version
  and the approving review record cited.
- **A7. Graduation criteria for the "provisional" label.** Graduation is per
  sector, per pillar, and is displayed on the sector page. A pillar graduates
  for a sector only when all of its conditions hold:
  - **P — Profitability:** at least three consecutive annual periods of
    *audited issuer actuals* or *official actuals* (Appendix A labels) cover
    the sector's defined sub-industries, and a through-the-cycle note exists
    (synthesis §8, item 4).
  - **O — Opportunity:** the demand inputs are measured series (official or
    industry-body with stated methodology), not forecasts alone. Forecasts
    remain labeled and serve as context only.
  - **G — Growth quality:** the organic vs. acquired / price / subsidy split
    is computable from ingested series for a majority of the sector's scale
    proxy. *Proposed threshold (an estimate of sufficiency, open to revision
    with a recorded rationale): ≥60%.*
  - **C — Customer quality:** at least one independent, methodology-transparent
    customer dataset with a stated denominator is ingested — or the pillar is
    published as "not available" for that sector (synthesis §2.1) rather than
    graduated on vendor-reported substitutes.
  - **E — Evidence quality:** the sector's confidence overlay (synthesis
    §2.3) computes from ingested metadata at **Medium** or better, and the
    sensitivity run (including equal-weight results) is published alongside.
  The sector composite keeps the "provisional" label until all five pillars
  have graduated for that sector. These criteria are themselves proposed
  standards; changing them is versioned with a rationale, like data.

## 3. Tier B — Complete the framework

The synthesis defines three tiers of analysis (§2.1); only Tier 1 (the sector
screen) exists. Tier B builds the other two, in the order of the §8 90-day
program: master data dictionary (§5.2) → data load → peer-group splits →
scorecards → customer evidence → publish score, confidence, and sensitivity
together.

- **B1. Tier-2 sub-industry scores.** Split each sector into homogeneous
  sub-industries before scoring (synthesis §2.1 example: technology and
  software → cloud/IaaS, enterprise SaaS, cybersecurity, semiconductors,
  digital advertising, IT services). Revenue recognition, margin structure,
  and capex are never blended across sub-industries.
- **B2. Tier-3 company scorecards.** Companies come from the synthesis §4
  universe map — a research universe, never a ranking — and are scored only
  against their closest peer group, using the Company Quality Score
  (synthesis §2.4: 0.30P + 0.20O + 0.20G + 0.15C + 0.15E). Multi-segment
  companies get segment-level scoring and a transparent sum-of-parts view.
  Risk and valuation remain **separate gates**, never folded into the score.
- **B3. Normalization rules, carried over from synthesis §2.1 without
  dilution:** reported GAAP/IFRS first; adjusted metrics only alongside their
  reconciliation and the issuer's definition; latest completed annual period
  plus LTM, both labeled; non-calendar fiscal years translated explicitly;
  currency converted at a stated average-period rate for flows and closing
  rate for stocks, with local-currency growth retained; sector-specific
  lenses where the generic ones mislead (utilities: rate base, allowed ROE,
  reliability, regulatory outcomes; banks: capital, credit, NIM, efficiency;
  pre-profit biotech: probability-adjusted pipeline economics); GMV,
  bookings, payment volume, backlog, installed capacity, and subscribers are
  operating indicators, not revenue or profit; independent customer metrics
  compare only within the same study, geography, period, and respondent base,
  and missing customer data reads "not available," never neutral.
- **B4. Publication discipline.** No sector or company conclusion is promoted
  when its confidence is Low or its rank is weight-sensitive (synthesis
  §2.3). Comparability warnings (`/api/v1/comparability`) extend to every new
  scorecard field, and a separate market-scale dimension is shown rather than
  hidden inside profitability (`site/FREE-DATA-ROADMAP.md`, Phase B).

## 4. Tier C — Deepen the Skills Archive

Baseline (§1): 20 compact derived entries. Deepening is per skill, and each
addition is checkable rather than decorative:

- **C1. Worked example.** One realistic end-to-end scenario per skill,
  executed in the skill's own stated workflow, with inputs and outputs shown.
- **C2. Executable artifact.** Where a skill admits one, a usable artifact —
  procedure, template, or checklist in `SKILL.md` form — accompanies the
  summary, versioned with it.
- **C3. Per-skill quality scoring.** A published rubric (proposed dimensions:
  provenance completeness, workflow testability, worked-example coverage,
  source freshness, license clarity). Scores are displayed next to the skill
  and labeled as assessments, not measurements.
- **C4. Per-skill tests.** Each skill carries at least one acceptance test: a
  task plus an observable pass condition, so "the skill works" is falsifiable.
- **C5. Versioning.** Semantic version and a changelog per skill; the catalog
  (`skills.json`) carries version and review date, mirroring the evidence
  layer's freshness discipline.
- **C6. Dedup / taxonomy pass.** One taxonomy across the archive (level ×
  category × capability). Near-duplicate pairs are examined and the outcome
  recorded — stated as an open question, not a conclusion: the two security
  entries (`production-agent-security`, `secure-agent-architecture`) are the
  first candidates for review. A gaps list (capabilities with no skill) is
  published with the taxonomy.
- **C7. Sector↔skill cross-links.** For each of the 20 sectors, the skills
  that operate a modern business in it, each link carrying a one-line
  rationale. Cross-links are editorial claims and carry the Appendix A
  labeling (analyst judgment) like everything else.
- **Guardrails, unchanged:** derived summaries only — no reproduced course
  text; provenance and license notes retained; connector entries carry
  credential *references*, never credential values.

## 5. Tier D — New categories

New categories are views over the same evidence base. None introduces a score
until Tier A data supports it.

- **D1. Cross-sector lenses.** Four cuts across all 20 sectors:
  - **AI adoption** — deployment and usage signals per sector, each labeled
    by evidence type (independent survey vs. issuer disclosure are not
    interchangeable).
  - **Capital flows** — capex, R&D, and investment series per sector
    (EDGAR / BEA, once Tier A lands).
  - **Labor and workforce** — employment, wages, openings, and projections
    per sector (BLS).
  - **Regulation** — a factual event and obligation log per sector. An event
    record, not legal advice.
- **D2. Regional cuts.** U.S. first, where the data depth is; global cuts via
  World Bank indicators where definitions allow. A regional cut publishes
  only where its comparability warnings can be stated honestly; a sector
  whose evidence is U.S.-only stays labeled U.S.-only.
- **D3. Trades & Field Services deep-dive.** A sub-industry deep-dive inside
  Sector 16 (real estate and construction) covering the trade businesses —
  HVAC, plumbing, electrical, and their peers. Its dual purpose is stated
  openly: it is refinery research **and** market research for the sister
  products (the Momo platform and the bookkeeping app), whose customers are
  these businesses. The same rules bind it: cited and labeled claims,
  candidate lists as research universes rather than rankings, demand and
  software-adoption evidence distinguished from vendor marketing.

## 6. Tier E — Distribution & machine access

- **E1. Home.** Per the owner's direction, the refinery becomes the research
  category of the Empire site rather than a standalone storefront. Until the
  owner chooses otherwise, the site remains Preview-only and this repository
  remains its source of truth.
- **E2. MCP server wrapper.** A read-only MCP server over the existing
  `/api/v1/*` surface — sectors, claims, sources, search, comparisons,
  skills, catalog, metrics, vintages, comparability. This is the dogfood
  rule applied deliberately: the archive's own `tool-use-and-mcp` skill is
  the reference pattern, and the wrapper's documentation cites it.
- **E3. Citation and ingestion friendliness, maintained as the data grows.**
  `llms.txt` stays current with every new resource; the OpenAPI contract is
  versioned with the API; stable identifiers for claims, metrics, and skills
  are never reused; every JSON resource carries version and vintage metadata
  so a machine consumer can cite a specific state of the data.
- **E4. Boundary kept.** This tier introduces no authentication, mutation, or
  billing — the phase-one boundary in `site/plan.md` holds. Those belong only
  to the gated work in §7.

## 7. Monetization sequence (later, and gated)

One rule, stated once and binding on every step: **the public evidence layer
stays free.** Claims, sources, evidence trails, freshness states, and
comparability warnings are the trust asset; they are not paywalled. What may
be charged for is scale, history, and depth built on top of that layer.

The sequence, each step gated on the tier work that makes it honest:

1. **Paid API / dataset tier.** *Entry criteria:* Tier A ingestion live for a
   majority of the 17 cataloged datasets; dataset versioning and the
   changelog feed operating; the versioned API contract stable across at
   least two dataset releases. *What it sells:* higher rate limits, bulk
   downloads, historical vintages, Tier-3 scorecard data feeds.
2. **Premium archive.** *Entry criteria:* Tier C complete for a defined core
   set of skills — worked example, executable artifact, acceptance test, and
   quality score each. *What it sells:* the deepened, tested, versioned skill
   library and its updates.
3. **Sponsored sector deep-dives.** *Entry criteria:* a measured (not
   estimated) audience baseline, and a disclosure practice modeled on the
   evidence labels — sponsorship is disclosed on the artifact itself, and
   sponsors do not alter scores, claims, rankings, or exclusions.

No prices are proposed here. The cost and audience inputs are not yet
measured, and a figure written today would be an estimate dressed as a plan.
Pricing at each gate is an owner decision (§8).

## 8. Phasing & ownership

- **Master sequence.** This roadmap is **Phase 5** of the owner's program —
  after the sister products are built, polished, live, and launched. Nothing
  here preempts launch work. Within Phase 5, the synthesis §8 90-day program
  is the execution spine for Tiers A–B; Tier C interleaves; Tier D lenses
  follow Tier A data; the Tier E MCP wrapper depends only on the existing API
  and can be built whenever Phase 5 capacity allows.
- **Runs unattended, once set up:** weekly source-checks, scheduled ingestion
  runs, changelog generation, freshness re-labeling. These produce review
  queues and reports — never silent changes to claims, scores, or sources.
- **Needs an owner decision:** publishing or integrating the site (Tier E1);
  creating accounts or API keys for keyed free sources; changing a
  graduation criterion (§2 A7); each monetization gate and its pricing;
  accepting any sponsored deep-dive.
- **Review cadence.** This roadmap is revisited when any tier completes or a
  graduation criterion is first met. Revisions are committed with their
  rationale recorded — the same discipline the project applies to data
  vintages.
