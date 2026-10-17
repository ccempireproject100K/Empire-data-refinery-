# 20/20 Free Data Roadmap

**Research date:** 2026-10-15  
**Current active dataset:** 20 sectors, 270 claims, 54 active viewable source records

## What the current coverage audit shows

The active dataset is strongest where there are already several source records, but coverage is uneven:

- **0 active source references:** Financial services and fintech; Biotechnology and life sciences; Energy and utilities; Food, beverage and agriculture.
- **1 active source reference:** Technology and software; Industrial manufacturing and robotics.
- **2 active source references:** Telecommunications; Renewable energy and climate technology; Automotive and electric vehicles; Transportation and logistics.
- Many sector dossiers have useful company lists but no structured metrics yet.

The next pass should prioritize **comparable, reproducible measurements** rather than adding more narrative links.

## Highest-value free sources to add

| Priority | Official source | What it adds | Best 20/20 sectors | Access notes |
|---|---|---|---|---|
| 1 | [SEC EDGAR APIs](https://www.sec.gov/edgar/sec-api-documentation) | Company submissions, XBRL company facts, revenue, operating income, margins, cash flow, capex, R&D, assets and liabilities | Technology, AI, healthcare, biotech, finance, e-commerce, industrials, media, automotive, chemicals | Public APIs do not require authentication or API keys. Must comply with SEC rate/privacy guidance; use CIK-based retrieval and cache results. |
| 2 | [U.S. Census developer datasets](https://www.census.gov/data/developers/data-sets.html) | Industry size, employment, wages, demographics, housing, migration, business dynamics and regional demand | All U.S.-focused sectors; especially real estate, construction, retail, education and professional services | Public APIs and downloads. ACS, QWI, PSEO, Economic Census and public-sector finance are particularly valuable. |
| 3 | [BLS data](https://www.bls.gov/data/) | CPI/PPI, employment, wages, productivity, job openings, labor turnover, occupational demand and employment projections | All sectors; especially labor-intensive services, manufacturing, healthcare, logistics, construction and software | Public tables, text files and API. Use industry and occupation crosswalks to make comparisons consistent. |
| 4 | [BEA API](https://www.bea.gov/API/signup/) | GDP by industry, value added, gross output, input-output tables, regional GDP/employment, international transactions and multinational activity | All sectors; especially finance, energy, manufacturing, travel and professional services | Free registration is required for an API key. This is a legitimate free key, not a paid source. Keep the key server-side. |
| 5 | [EIA Open Data](https://www.eia.gov/opendata/) | Electricity generation, capacity, retail sales, fuel prices, production, reserves, consumption, trade and emissions | Energy/utilities; renewable energy; chemicals; transportation; industrial manufacturing | Free/open data. API registration/key is required. EIA explicitly provides API and bulk/open-data access. |
| 6 | [CMS Data](https://data.cms.gov/) | Provider enrollment, utilization, payments, beneficiaries, quality-of-care, prescription and facility data | Healthcare and pharmaceuticals; biotech; insurance/financial services | Public datasets, tools and API documentation. Strong source for demand, utilization, provider scale and quality signals. |
| 7 | [ClinicalTrials.gov API](https://clinicaltrials.gov/data-api/api) | Trial count, phase, enrollment, sponsor, condition, intervention, status, outcome and geography | Biotechnology and life sciences; healthcare and pharmaceuticals | Public REST API; data refreshes daily Monday–Friday. Use timestamp fields and distinguish registered studies from posted results. |
| 8 | [openFDA API](https://open.fda.gov/apis/) | Drug/device/food labels, recalls, adverse events and enforcement-related public records | Biotech, pharmaceuticals, healthcare, food and agriculture | Public JSON API. FDA warns that not all data are validated for clinical or production use; treat as a signal layer, not a definitive safety score. |
| 9 | [FRED](https://fred.stlouisfed.org/) | Interest rates, inflation, credit, housing, labor, exchange rates, market and macro series from many sources | All sectors; especially finance, real estate, energy and consumer sectors | Free web/download access and API ecosystem. Record the underlying series source and release date to avoid mixing revisions. |
| 10 | [World Bank Open Data](https://data.worldbank.org/) | Cross-country development indicators covering people, prosperity, planet, infrastructure and digital transformation | Global comparisons across all sectors; especially energy, agriculture, healthcare, education and digital infrastructure | Free and open access. Use World Development Indicators/DataBank with country, year and indicator metadata. |
| 11 | [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/) | Complaint volume, product/issue mix, company responses and consumer-friction signals | Financial services and fintech; payments; consumer credit; insurance-adjacent research | Public downloads and API. The CFPB cautions that complaint data are not a representative statistical sample; normalize by company scale where possible. |
| 12 | [Bureau of Transportation Statistics](https://www.bts.gov/) | Freight, airline, transit, vehicle, border-crossing, safety, reliability, employment and transportation-economic indicators | Transportation/logistics; automotive; aerospace; travel; energy | Official public statistics and data portal. Good source for operating conditions and demand proxies. |

## Additional targeted sources

- **Aviation and aerospace:** FAA/National Airspace System data, BTS airline and airport datasets, NASA technical/publication data.
- **Defense:** USAspending.gov and Federal Procurement Data System public contract awards; normalize award value, obligation, agency and fiscal year.
- **Agriculture and food:** USDA ERS, NASS Quick Stats and FDA food recalls; add crop yields, commodity prices, farm income, food-at-home inflation and recall events.
- **Climate and resilience:** NOAA Climate Data Online, FEMA disaster datasets and EPA Envirofacts; add weather exposure, emissions, environmental compliance and resilience demand.
- **Construction and real estate:** Census building permits, housing starts, ACS housing, BEA regional GDP and FRED housing series.
- **Innovation and research:** NIH RePORTER, NSF awards, USPTO patent data, and OpenAlex for publication/citation signals. Treat patents and papers as innovation activity, not guaranteed commercial value.
- **Customer quality:** CFPB complaints, CMS quality measures, BTS reliability, FDA recalls, and any validated public satisfaction dataset. Do not mix complaint volume and satisfaction ratings without a documented normalization method.

## Data model additions that would make 20/20 materially stronger

1. **Time series layer:** `metric_id`, `sector`, `industry`, `company`, `value`, `unit`, `period_start`, `period_end`, `geography`, `source_id`, `retrieved_at`, `vintage`.
2. **Company normalization:** CIK/EIN or another stable identifier, parent/subsidiary relationship, ticker, industry code, fiscal year-end and currency.
3. **Industry crosswalks:** NAICS ↔ SIC ↔ ISIC where possible, with version/date fields.
4. **Scale-normalized customer signals:** complaints per million customers, recalls per product volume, reliability per trip/flight, quality per provider or beneficiary.
5. **Freshness and vintage tracking:** distinguish original release, revision, last checked, and current value; never overwrite historical vintages silently.
6. **Confidence labels:** official measured fact, derived calculation, analyst estimate, proxy, or qualitative claim.
7. **Comparability warnings:** currency, inflation basis, fiscal/calendar period, geography, company scope, and accounting-standard differences.
8. **Agent-ready query layer:** endpoints for `metrics`, `companies`, `timeseries`, `sources`, `vintages`, and `comparability-warnings`, with explicit units and provenance.

## Recommended implementation order

### Phase A — close the biggest gaps

1. SEC EDGAR/XBRL company facts.
2. BEA GDP-by-industry and input-output data.
3. BLS industry employment, wages, PPI and productivity.
4. EIA energy and emissions data.
5. CMS + ClinicalTrials.gov + openFDA for healthcare/biotech.
6. CFPB complaints for finance/fintech.
7. USDA datasets for food/agriculture.

### Phase B — make rankings more defensible

- Add a separate **market scale** score rather than hiding scale inside profitability.
- Add **data confidence** and **freshness** as visible dimensions.
- Normalize company metrics by revenue, employees, customers, beneficiaries, shipments or installed capacity.
- Show sensitivity: how rankings change when profitability, growth, customer quality or evidence weights move.

### Phase C — automate carefully

- Keep the Preview-only site and manual review workflow.
- After deployment, run the documented weekly source audit.
- Never auto-promote a recovered source, change a score, or rewrite a claim without a review record.

## Important caveats

- Free access does not mean unrestricted redistribution; each dataset’s terms and attribution rules still apply.
- API keys for free services are still secrets and must stay out of source code and public JSON.
- Public datasets may be revised, incomplete, geographically narrow or non-representative. 20/20 should preserve the source vintage and clearly label derived metrics.
- A dataset being official does not automatically make it suitable for ranking. Every metric needs a definition, unit, population, time period and comparability note.
