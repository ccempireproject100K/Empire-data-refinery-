# Empire Data Refinery

The **20/20 Data Refinery** corpus: evidence-disciplined research reports on the
20 sectors that make up the modern economy, built as the raw material for a
data refinery — raw sector information in, refined, trustworthy knowledge out.

Each report answers the same core questions about its sector: Why is it
financially lucrative in the 2020s? What drives profitability? Which industries
and subsectors matter most? Which companies lead (as a research universe,
never presented as a ranking)? What are the risks and caveats? And which
metrics are worth capturing about it going forward?

## The corpus — 20 sector reports

| # | Sector | Report |
|---|--------|--------|
| 01 | Technology and software | [reports/01-technology-and-software.md](reports/01-technology-and-software.md) |
| 02 | Artificial intelligence and data infrastructure | [reports/02-artificial-intelligence-and-data-infrastructure.md](reports/02-artificial-intelligence-and-data-infrastructure.md) |
| 03 | Financial services and fintech | [reports/03-financial-services-and-fintech.md](reports/03-financial-services-and-fintech.md) |
| 04 | Healthcare and pharmaceuticals | [reports/04-healthcare-and-pharmaceuticals.md](reports/04-healthcare-and-pharmaceuticals.md) |
| 05 | Biotechnology and life sciences | [reports/05-biotechnology-and-life-sciences.md](reports/05-biotechnology-and-life-sciences.md) |
| 06 | Energy and utilities | [reports/06-energy-and-utilities.md](reports/06-energy-and-utilities.md) |
| 07 | Renewable energy and climate technology | [reports/07-renewable-energy-and-climate-technology.md](reports/07-renewable-energy-and-climate-technology.md) |
| 08 | Transportation and logistics | [reports/08-transportation-and-logistics.md](reports/08-transportation-and-logistics.md) |
| 09 | Automotive and electric vehicles | [reports/09-automotive-and-electric-vehicles.md](reports/09-automotive-and-electric-vehicles.md) |
| 10 | Aerospace and defense | [reports/10-aerospace-and-defense.md](reports/10-aerospace-and-defense.md) |
| 11 | Telecommunications | [reports/11-telecommunications.md](reports/11-telecommunications.md) |
| 12 | Consumer goods and retail | [reports/12-consumer-goods-and-retail.md](reports/12-consumer-goods-and-retail.md) |
| 13 | E-commerce and marketplaces | [reports/13-ecommerce-and-marketplaces.md](reports/13-ecommerce-and-marketplaces.md) |
| 14 | Media, entertainment and gaming | [reports/14-media-entertainment-and-gaming.md](reports/14-media-entertainment-and-gaming.md) |
| 15 | Food, beverage and agriculture | [reports/15-food-beverage-and-agriculture.md](reports/15-food-beverage-and-agriculture.md) |
| 16 | Real estate and construction | [reports/16-real-estate-and-construction.md](reports/16-real-estate-and-construction.md) |
| 17 | Industrial manufacturing and robotics | [reports/17-industrial-manufacturing-and-robotics.md](reports/17-industrial-manufacturing-and-robotics.md) |
| 18 | Chemicals and advanced materials | [reports/18-chemicals-and-advanced-materials.md](reports/18-chemicals-and-advanced-materials.md) |
| 19 | Professional services and education | [reports/19-professional-services-and-education.md](reports/19-professional-services-and-education.md) |
| 20 | Travel, hospitality and experiences | [reports/20-travel-hospitality-and-experiences.md](reports/20-travel-hospitality-and-experiences.md) |

## Synthesis layer

On top of the 20 briefs sits one synthesis report:
**[synthesis/20-20-sector-research-synthesis.md](synthesis/20-20-sector-research-synthesis.md)**.

It turns the sector briefs into a repeatable, evidence-aware **screening
framework** rather than treating them as standalone reads:

- **Five-pillar score** — a proposed scoring methodology (with comparability
  rules: sectors are split into economic sub-industries first, and companies
  are scored only against close operating peers).
- **Provisional ranked top-20** — a research-priority ranking of the 20
  sectors indicating where a normalized diligence process should begin;
  explicitly provisional and **not** an audited league table or investment
  advice.
- **Universe map** — the top industries and candidate companies per sector,
  kept separate from the sector-priority ranking.
- **Free-source data plan** — a collection architecture, minimum data
  dictionary, metric formulas and guardrails, data-quality controls, update
  cadence, and a directory of free primary sources.
- **Evidence labeling standard** (Appendix A) — measured facts, forecasts,
  estimates, and issuer-defined metrics carry different evidentiary weight and
  are labeled accordingly throughout.
- **A recommended 90-day program** for turning the framework into a
  standardized, reproducible data set.

## The site

Under **[site/](site/)** lives the refinery's working website export — the
research as a product, not just documents:

- **Static front end + Node server** (`site/public/`, `site/server.js`;
  `npm start`, port 3000): a searchable research experience over the 20
  sectors with stable sector pages, full-dataset client-side search, and
  filters for rank, score dimensions, evidence strength, and source
  attributes.
- **Claim-level evidence engine** — `site/public/evidence.json` holds stable
  claim-level evidence records with source relationships, evidence levels,
  freshness status, and caveat notes; an Evidence Map and sector comparison
  views sit on top of it.
- **Source-checking pipeline** (`site/scripts/`) — build scripts for the
  dataset, catalog, evidence, and skills, plus a bounded source-checking
  engine that flags changed or unreachable sources (with an exclusion
  manifest and audit history) without silently changing claims or rankings.
- **Read-only agent API** for sectors, claims, sources, search, comparisons,
  and skills, with a discoverable OpenAPI contract
  (`site/public/api/openapi.json`), a data catalog, and downloadable
  Markdown/JSON datasets for AI-agent use.
- **AI Skills Archive** — 51 derived AI-agent skills under
  `site/public/content/skills/` (searchable, each with a downloadable
  `SKILL.md`; connector entries carry credential *references* only, never
  credential values).
- **Roadmap** — `site/FREE-DATA-ROADMAP.md` prioritizes free official data
  sources, sector gaps, and freshness/comparability safeguards.

**Status (per `site/TODO.md`):** the project is **Preview-only by the owner's
choice**. Its delivery checklist is complete except one item: once the site
is deployed, create the recurring weekly ScheduleTask for the source-checking
engine.

**Note on sector copies:** the site carries its own sector texts under
`site/public/content/sectors/`, which differ slightly from the standalone
reports in `reports/`. Both are preserved intentionally — `reports/` is the
report corpus as received; the site copies are the site's own rendering
inputs.

## Corpus conventions

These conventions are observed consistently across the reports and should be
preserved by any future addition or revision:

- **Every report opens with a bottom line** — why the sector is financially
  lucrative in the 2020s — followed by the profitability drivers, the most
  relevant industries/subsectors, candidate leading companies, risks and
  caveats, and the metrics worth capturing in the refinery.
- **All load-bearing claims are cited inline**, with a References section in
  each report (industry research such as Gartner, official statistics such as
  U.S. Census/FRED series, and company disclosures).
- **Forecasts are labeled as forecasts** — e.g. third-party spending
  projections are explicitly noted as "a forecast, not realized revenue."
- **Estimates are flagged as estimates**, and the scope of a figure is stated
  (for example, a U.S.-only statistical series is not presented as a global
  sector total).
- **Company results are distinguished from sector claims**: company-reported
  metrics are attributed to the company and noted as subject to management
  definitions; candidate-company lists are research universes, **not rankings**.
- **Each report carries its own caveats section** covering interpretation
  risks, comparability limits, and where the evidence is thin.

## Roadmap

The improvement roadmap — baseline, Tier A–E work, graduation criteria for the provisional scores, the gated monetization sequence, and phasing — lives in **[ROADMAP.md](ROADMAP.md)**.

## Status

- **Sector reports received 2026-10-16** — all 20 reports staged into this
  repository as received (contents unchanged; files renamed descriptively by
  sector).
- **Website export received 2026-10-16** — the full site project staged
  under `site/` with its structure preserved (see "The site" above).
- **Skill-archive deepening is a later phase**: the AI skill archives that
  belong with this technology-focused refinery (taxonomy, per-skill material,
  quality scoring, deduplication, documentation) will be built on top of this
  corpus in a subsequent phase.
