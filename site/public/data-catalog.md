# 20/20 Free Public Data Catalog

High-value official datasets and metric recipes for future normalized ingestion. Catalog entries do not automatically change rankings.

| Dataset | Publisher | Access | Status | Sectors | |
|---|---|---|---|---|---|
| [SEC EDGAR APIs](https://www.sec.gov/edgar/sec-api-documentation) | U.S. Securities and Exchange Commission | `keyless-public` | `ready` | technology-and-software, artificial-intelligence-and-data-infrastructure, healthcare-and-pharmaceuticals, biotechnology-and-life-sciences… | [Endpoint](https://data.sec.gov/submissions/CIK##########.json) |
| [U.S. Census developer datasets](https://www.census.gov/data/developers/data-sets.html) | U.S. Census Bureau | `keyless-public` | `ready` | all | [Endpoint](https://api.census.gov/data/) |
| [BLS public data](https://www.bls.gov/data/) | U.S. Bureau of Labor Statistics | `keyless-public` | `ready` | all | [Endpoint](https://api.bls.gov/publicAPI/v2/timeseries/data/) |
| [BEA Data API](https://www.bea.gov/API/signup/) | U.S. Bureau of Economic Analysis | `free-registration-api-key` | `documented-not-called` | all | [Endpoint](https://apps.bea.gov/api/data/) |
| [EIA Open Data](https://www.eia.gov/opendata/) | U.S. Energy Information Administration | `free-registration-api-key` | `documented-not-called` | energy-and-utilities, renewable-energy-and-climate-technology, transportation-and-logistics, chemicals-and-advanced-materials… | [Endpoint](https://api.eia.gov/v2/) |
| [CMS Data](https://data.cms.gov/) | Centers for Medicare & Medicaid Services | `open-public` | `ready` | healthcare-and-pharmaceuticals, biotechnology-and-life-sciences, financial-services-and-fintech | [Endpoint](https://data.cms.gov/api-docs) |
| [ClinicalTrials.gov API](https://clinicaltrials.gov/data-api/api) | National Library of Medicine / NIH | `keyless-public` | `ready` | biotechnology-and-life-sciences, healthcare-and-pharmaceuticals | [Endpoint](https://clinicaltrials.gov/api/v2/studies) |
| [openFDA API](https://open.fda.gov/apis/) | U.S. Food and Drug Administration | `keyless-public` | `ready` | biotechnology-and-life-sciences, healthcare-and-pharmaceuticals, food-beverage-and-agriculture | [Endpoint](https://api.fda.gov/) |
| [CFPB Consumer Complaint Database](https://www.consumerfinance.gov/data-research/consumer-complaints/) | Consumer Financial Protection Bureau | `open-public` | `ready` | financial-services-and-fintech, e-commerce-and-marketplaces, consumer-goods-and-retail | [Endpoint](https://cfpb.github.io/api/ccdb/api.html) |
| [World Bank Open Data](https://data.worldbank.org/) | World Bank | `open-public` | `ready` | all | [Endpoint](https://api.worldbank.org/v2/) |
| [FRED Economic Data](https://fred.stlouisfed.org/) | Federal Reserve Bank of St. Louis | `free-registration-api-key` | `documented-not-called` | all | [Endpoint](https://api.stlouisfed.org/fred/) |
| [Bureau of Transportation Statistics](https://www.bts.gov/) | U.S. Department of Transportation | `open-public` | `ready` | transportation-and-logistics, automotive-and-electric-vehicles, aerospace-and-defense, travel-hospitality-and-experiences | [Endpoint](https://data.bts.gov/) |
| [USDA Economic Research Service and NASS](https://www.ers.usda.gov/data-products/) | U.S. Department of Agriculture | `open-public` | `candidate` | food-beverage-and-agriculture, renewable-energy-and-climate-technology, consumer-goods-and-retail | [Endpoint](https://www.ers.usda.gov/data-products/) |
| [NOAA Climate Data Online](https://www.ncei.noaa.gov/cdo-web/) | National Oceanic and Atmospheric Administration | `open-public` | `candidate` | renewable-energy-and-climate-technology, energy-and-utilities, insurance, food-beverage-and-agriculture… | [Endpoint](https://www.ncei.noaa.gov/cdo-web/webservices/v2) |
| [USAspending.gov](https://www.usaspending.gov/) | U.S. Government | `keyless-public` | `candidate` | aerospace-and-defense, professional-services-and-education, healthcare-and-pharmaceuticals, industrial-manufacturing-and-robotics | [Endpoint](https://api.usaspending.gov/api/v2/) |
| [EPA Envirofacts](https://enviro.epa.gov/) | U.S. Environmental Protection Agency | `open-public` | `candidate` | energy-and-utilities, chemicals-and-advanced-materials, industrial-manufacturing-and-robotics, renewable-energy-and-climate-technology… | [Endpoint](https://enviro.epa.gov/) |
| [USPTO PatentsView](https://patentsview.org/) | U.S. Patent and Trademark Office | `open-public` | `candidate` | artificial-intelligence-and-data-infrastructure, biotechnology-and-life-sciences, industrial-manufacturing-and-robotics, renewable-energy-and-climate-technology… | [Endpoint](https://search.patentsview.org/api/v1/) |

## Metric recipes

### Company profitability profile
- Sources: sec-edgar
- Grain: `company-fiscal-period`
- Fields: revenue, operating income, net income, cash flow from operations, capital expenditure
- Normalize: currency, fiscal period, consolidated vs segment, GAAP vs IFRS

### Industry labor demand
- Sources: bls-data, census-developer
- Grain: `industry-geography-period`
- Fields: employment, wages, job openings, employment growth, business births
- Normalize: NAICS version, geography, seasonal adjustment, nominal vs real

### Energy system scale and transition
- Sources: eia-open-data, world-bank, epa-envirofacts
- Grain: `energy-source-geography-period`
- Fields: generation, capacity, price, consumption, emissions
- Normalize: unit conversion, energy source, geography, CO2 scope

### Healthcare demand and quality
- Sources: cms-data, clinicaltrials, openfda
- Grain: `provider-product-study-period`
- Fields: beneficiaries, payments, quality measure, trial enrollment, recalls, adverse events
- Normalize: provider type, product identity, study phase, population, reporting period

### Customer friction and service quality
- Sources: cfpb-complaints, bts, cms-data
- Grain: `company-product-geography-period`
- Fields: complaints, response timeliness, reliability, quality measure
- Normalize: customer/base denominator, product category, geography, period

### Public-sector demand and procurement
- Sources: usaspending, census-developer, bts
- Grain: `recipient-category-geography-fiscal-period`
- Fields: obligations, award count, agency concentration, employment, freight activity
- Normalize: award type, fiscal year, recipient identity, NAICS/PSC

## Safety and provenance

- Keyless/open sources can be sampled by the bounded ingestion script.
- Free-registration and API-key sources remain documented but are not called until credentials are intentionally configured.
- No catalog entry automatically changes sector scores or rankings.
- Every promoted metric must retain source ID, endpoint, retrieval time, unit, geography, period, vintage, and comparability notes.
