import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'

SOURCES = [
    {
        'id': 'sec-edgar', 'name': 'SEC EDGAR APIs', 'publisher': 'U.S. Securities and Exchange Commission',
        'url': 'https://www.sec.gov/edgar/sec-api-documentation', 'access': 'keyless-public', 'cadence': 'real-time / nightly bulk',
        'coverage': 'Public-company submissions, XBRL company facts, filing history, and comparable financial statement concepts.',
        'sectors': ['technology-and-software','artificial-intelligence-and-data-infrastructure','healthcare-and-pharmaceuticals','biotechnology-and-life-sciences','financial-services-and-fintech','e-commerce-and-marketplaces','industrial-manufacturing-and-robotics','media-entertainment-and-gaming','automotive-and-electric-vehicles','chemicals-and-advanced-materials'],
        'metrics': ['revenue','gross profit','operating income','net income','cash flow from operations','capital expenditure','research and development','assets','liabilities'],
        'endpoint': 'https://data.sec.gov/submissions/CIK##########.json', 'status': 'ready',
        'caveats': 'Requires CIK normalization, SEC request etiquette, fiscal-period discipline, and careful handling of company-specific custom tags.'
    },
    {
        'id': 'census-developer', 'name': 'U.S. Census developer datasets', 'publisher': 'U.S. Census Bureau',
        'url': 'https://www.census.gov/data/developers/data-sets.html', 'access': 'keyless-public', 'cadence': 'varies by dataset',
        'coverage': 'ACS, QWI, PSEO, Economic Census, business dynamics, housing, migration, demographics, and public finance.',
        'sectors': ['all'], 'metrics': ['employment','wages','population','migration','housing units','business formations','graduate outcomes'],
        'endpoint': 'https://api.census.gov/data/', 'status': 'ready',
        'caveats': 'Geographic coverage and release years differ by program; preserve geography and survey vintage.'
    },
    {
        'id': 'bls-data', 'name': 'BLS public data', 'publisher': 'U.S. Bureau of Labor Statistics',
        'url': 'https://www.bls.gov/data/', 'access': 'keyless-public', 'cadence': 'monthly / quarterly / annual',
        'coverage': 'CPI, PPI, employment, wages, productivity, JOLTS, QCEW, occupational employment, and projections.',
        'sectors': ['all'], 'metrics': ['employment','average hourly earnings','producer prices','job openings','turnover','productivity','occupation demand'],
        'endpoint': 'https://api.bls.gov/publicAPI/v2/timeseries/data/', 'status': 'ready',
        'caveats': 'Industry and occupation series require crosswalks; avoid mixing seasonally adjusted and unadjusted series.'
    },
    {
        'id': 'bea-api', 'name': 'BEA Data API', 'publisher': 'U.S. Bureau of Economic Analysis',
        'url': 'https://www.bea.gov/API/signup/', 'access': 'free-registration-api-key', 'cadence': 'monthly / quarterly / annual',
        'coverage': 'GDP by industry, input-output tables, regional GDP/employment, international transactions, and multinational activity.',
        'sectors': ['all'], 'metrics': ['value added','gross output','intermediate inputs','regional GDP','industry employment','international services trade'],
        'endpoint': 'https://apps.bea.gov/api/data/', 'status': 'documented-not-called',
        'caveats': 'Free registration is required; store the key server-side and preserve release vintage.'
    },
    {
        'id': 'eia-open-data', 'name': 'EIA Open Data', 'publisher': 'U.S. Energy Information Administration',
        'url': 'https://www.eia.gov/opendata/', 'access': 'free-registration-api-key', 'cadence': 'hourly / monthly / annual',
        'coverage': 'Electricity, fuels, generation, capacity, prices, production, reserves, trade, consumption, and emissions.',
        'sectors': ['energy-and-utilities','renewable-energy-and-climate-technology','transportation-and-logistics','chemicals-and-advanced-materials','industrial-manufacturing-and-robotics'],
        'metrics': ['generation','capacity','retail sales','fuel price','production','reserves','consumption','CO2 emissions'],
        'endpoint': 'https://api.eia.gov/v2/', 'status': 'documented-not-called',
        'caveats': 'Free API key registration is required; units and revisions vary by series.'
    },
    {
        'id': 'cms-data', 'name': 'CMS Data', 'publisher': 'Centers for Medicare & Medicaid Services',
        'url': 'https://data.cms.gov/', 'access': 'open-public', 'cadence': 'varies by dataset',
        'coverage': 'Provider enrollment, utilization, payments, beneficiaries, quality of care, prescriptions, and facility data.',
        'sectors': ['healthcare-and-pharmaceuticals','biotechnology-and-life-sciences','financial-services-and-fintech'],
        'metrics': ['provider count','beneficiary count','payments','utilization','quality measures','prescriber activity'],
        'endpoint': 'https://data.cms.gov/api-docs', 'status': 'ready',
        'caveats': 'Dataset definitions and reporting periods differ; provider identifiers and measure specifications must be preserved.'
    },
    {
        'id': 'clinicaltrials', 'name': 'ClinicalTrials.gov API', 'publisher': 'National Library of Medicine / NIH',
        'url': 'https://clinicaltrials.gov/data-api/api', 'access': 'keyless-public', 'cadence': 'daily on weekdays',
        'coverage': 'Study status, phase, enrollment, sponsor, intervention, condition, geography, outcomes, and results posting.',
        'sectors': ['biotechnology-and-life-sciences','healthcare-and-pharmaceuticals'],
        'metrics': ['trial count','phase mix','enrollment','sponsor concentration','recruitment status','time to completion'],
        'endpoint': 'https://clinicaltrials.gov/api/v2/studies', 'status': 'ready',
        'caveats': 'Registered studies are not equivalent to successful products; separate trials, arms, and posted results.'
    },
    {
        'id': 'openfda', 'name': 'openFDA API', 'publisher': 'U.S. Food and Drug Administration',
        'url': 'https://open.fda.gov/apis/', 'access': 'keyless-public', 'cadence': 'varies by endpoint',
        'coverage': 'Drug, device, food and adverse-event, label, recall, and enforcement records.',
        'sectors': ['biotechnology-and-life-sciences','healthcare-and-pharmaceuticals','food-beverage-and-agriculture'],
        'metrics': ['recall count','adverse-event count','label events','device events','enforcement activity'],
        'endpoint': 'https://api.fda.gov/', 'status': 'ready',
        'caveats': 'FDA warns that not all openFDA data are validated for clinical or production use; use as a signal layer.'
    },
    {
        'id': 'cfpb-complaints', 'name': 'CFPB Consumer Complaint Database', 'publisher': 'Consumer Financial Protection Bureau',
        'url': 'https://www.consumerfinance.gov/data-research/consumer-complaints/', 'access': 'open-public', 'cadence': 'generally daily',
        'coverage': 'Consumer complaints by financial product, issue, company, geography, and company response.',
        'sectors': ['financial-services-and-fintech','e-commerce-and-marketplaces','consumer-goods-and-retail'],
        'metrics': ['complaints','response timeliness','issue mix','product mix','complaints per customer or market share'],
        'endpoint': 'https://cfpb.github.io/api/ccdb/api.html', 'status': 'ready',
        'caveats': 'Not a representative statistical sample; normalize by company scale and do not equate complaint volume with harm rate.'
    },
    {
        'id': 'world-bank', 'name': 'World Bank Open Data', 'publisher': 'World Bank',
        'url': 'https://data.worldbank.org/', 'access': 'open-public', 'cadence': 'varies by indicator',
        'coverage': 'Global development indicators for people, prosperity, planet, infrastructure, and digital transformation.',
        'sectors': ['all'], 'metrics': ['GDP','population','inflation','trade','health','education','energy access','internet use','emissions'],
        'endpoint': 'https://api.worldbank.org/v2/', 'status': 'ready',
        'caveats': 'Country, year, indicator definition, and revision metadata are essential for comparisons.'
    },
    {
        'id': 'fred', 'name': 'FRED Economic Data', 'publisher': 'Federal Reserve Bank of St. Louis',
        'url': 'https://fred.stlouisfed.org/', 'access': 'free-registration-api-key', 'cadence': 'varies by series',
        'coverage': 'Macroeconomic, financial, labor, housing, price, and market series from many publishers.',
        'sectors': ['all'], 'metrics': ['interest rates','inflation','housing','credit','labor','exchange rates','economic activity'],
        'endpoint': 'https://api.stlouisfed.org/fred/', 'status': 'documented-not-called',
        'caveats': 'Record the underlying source, release, observation vintage, units, and revision history.'
    },
    {
        'id': 'bts', 'name': 'Bureau of Transportation Statistics', 'publisher': 'U.S. Department of Transportation',
        'url': 'https://www.bts.gov/', 'access': 'open-public', 'cadence': 'monthly / quarterly / annual',
        'coverage': 'Freight, aviation, transit, vehicles, border crossings, employment, safety, reliability, and transportation economics.',
        'sectors': ['transportation-and-logistics','automotive-and-electric-vehicles','aerospace-and-defense','travel-hospitality-and-experiences'],
        'metrics': ['freight index','air traffic','ridership','vehicle sales','border freight','safety','on-time performance'],
        'endpoint': 'https://data.bts.gov/', 'status': 'ready',
        'caveats': 'Mode, geography, and reporting lag differ; distinguish traffic, revenue, volume, and reliability measures.'
    },
    {
        'id': 'usda', 'name': 'USDA Economic Research Service and NASS', 'publisher': 'U.S. Department of Agriculture',
        'url': 'https://www.ers.usda.gov/data-products/', 'access': 'open-public', 'cadence': 'monthly / annual / seasonal',
        'coverage': 'Agricultural production, commodity prices, farm income, food prices, land use, trade, and rural economics.',
        'sectors': ['food-beverage-and-agriculture','renewable-energy-and-climate-technology','consumer-goods-and-retail'],
        'metrics': ['yield','commodity price','farm income','food-at-home inflation','trade','land use','rural employment'],
        'endpoint': 'https://www.ers.usda.gov/data-products/', 'status': 'candidate',
        'caveats': 'NASS Quick Stats API access may require a free key; bulk tables and ERS products remain publicly available.'
    },
    {
        'id': 'noaa-climate', 'name': 'NOAA Climate Data Online', 'publisher': 'National Oceanic and Atmospheric Administration',
        'url': 'https://www.ncei.noaa.gov/cdo-web/', 'access': 'open-public', 'cadence': 'daily / monthly / annual',
        'coverage': 'Weather, climate normals, extremes, hazards, stations, and environmental observations.',
        'sectors': ['renewable-energy-and-climate-technology','energy-and-utilities','insurance','food-beverage-and-agriculture','real-estate-and-construction','travel-hospitality-and-experiences'],
        'metrics': ['temperature','precipitation','extreme events','heating/cooling degree days','hazard exposure'],
        'endpoint': 'https://www.ncei.noaa.gov/cdo-web/webservices/v2', 'status': 'candidate',
        'caveats': 'Station coverage and API token rules vary; use geography and measurement definitions explicitly.'
    },
    {
        'id': 'usaspending', 'name': 'USAspending.gov', 'publisher': 'U.S. Government',
        'url': 'https://www.usaspending.gov/', 'access': 'keyless-public', 'cadence': 'daily / fiscal-year reporting',
        'coverage': 'Federal contracts, grants, loans, obligations, agencies, recipients, and award geography.',
        'sectors': ['aerospace-and-defense','professional-services-and-education','healthcare-and-pharmaceuticals','industrial-manufacturing-and-robotics'],
        'metrics': ['award obligations','agency concentration','recipient concentration','contract category','geographic exposure'],
        'endpoint': 'https://api.usaspending.gov/api/v2/', 'status': 'candidate',
        'caveats': 'Obligations are not revenue or profit; distinguish award type, fiscal year, agency, and recipient entity.'
    },
    {
        'id': 'epa-envirofacts', 'name': 'EPA Envirofacts', 'publisher': 'U.S. Environmental Protection Agency',
        'url': 'https://enviro.epa.gov/', 'access': 'open-public', 'cadence': 'varies by program',
        'coverage': 'Environmental permits, emissions, facility compliance, toxic releases, and regulated-site records.',
        'sectors': ['energy-and-utilities','chemicals-and-advanced-materials','industrial-manufacturing-and-robotics','renewable-energy-and-climate-technology','real-estate-and-construction'],
        'metrics': ['facility count','emissions','toxic releases','compliance events','permit activity'],
        'endpoint': 'https://enviro.epa.gov/', 'status': 'candidate',
        'caveats': 'Facility reporting and enforcement records are not a complete measure of environmental impact or liability.'
    },
    {
        'id': 'patentsview', 'name': 'USPTO PatentsView', 'publisher': 'U.S. Patent and Trademark Office',
        'url': 'https://patentsview.org/', 'access': 'open-public', 'cadence': 'weekly / varies',
        'coverage': 'Patent documents, inventors, assignees, technology classifications, citations, and innovation networks.',
        'sectors': ['artificial-intelligence-and-data-infrastructure','biotechnology-and-life-sciences','industrial-manufacturing-and-robotics','renewable-energy-and-climate-technology','chemicals-and-advanced-materials'],
        'metrics': ['patent count','forward citations','assignee concentration','technology mix','inventor network'],
        'endpoint': 'https://search.patentsview.org/api/v1/', 'status': 'candidate',
        'caveats': 'Patent quantity is an innovation activity proxy, not proof of commercial value or defensibility.'
    }
]

RECIPES = [
    {'id':'company-profitability','name':'Company profitability profile','sources':['sec-edgar'],'grain':'company-fiscal-period','fields':['revenue','operating income','net income','cash flow from operations','capital expenditure'],'normalization':['currency','fiscal period','consolidated vs segment','GAAP vs IFRS'],'sectors':['all']},
    {'id':'industry-labor-demand','name':'Industry labor demand','sources':['bls-data','census-developer'],'grain':'industry-geography-period','fields':['employment','wages','job openings','employment growth','business births'],'normalization':['NAICS version','geography','seasonal adjustment','nominal vs real'],'sectors':['all']},
    {'id':'energy-system-scale','name':'Energy system scale and transition','sources':['eia-open-data','world-bank','epa-envirofacts'],'grain':'energy-source-geography-period','fields':['generation','capacity','price','consumption','emissions'],'normalization':['unit conversion','energy source','geography','CO2 scope'],'sectors':['energy-and-utilities','renewable-energy-and-climate-technology']},
    {'id':'healthcare-demand-quality','name':'Healthcare demand and quality','sources':['cms-data','clinicaltrials','openfda'],'grain':'provider-product-study-period','fields':['beneficiaries','payments','quality measure','trial enrollment','recalls','adverse events'],'normalization':['provider type','product identity','study phase','population','reporting period'],'sectors':['healthcare-and-pharmaceuticals','biotechnology-and-life-sciences']},
    {'id':'customer-friction','name':'Customer friction and service quality','sources':['cfpb-complaints','bts','cms-data'],'grain':'company-product-geography-period','fields':['complaints','response timeliness','reliability','quality measure'],'normalization':['customer/base denominator','product category','geography','period'],'sectors':['financial-services-and-fintech','transportation-and-logistics','healthcare-and-pharmaceuticals']},
    {'id':'public-demand','name':'Public-sector demand and procurement','sources':['usaspending','census-developer','bts'],'grain':'recipient-category-geography-fiscal-period','fields':['obligations','award count','agency concentration','employment','freight activity'],'normalization':['award type','fiscal year','recipient identity','NAICS/PSC'],'sectors':['aerospace-and-defense','professional-services-and-education','industrial-manufacturing-and-robotics']}
]

catalog = {'version':'2026-10-15-phase-two','title':'20/20 Free Public Data Catalog','description':'High-value official datasets and metric recipes for future normalized ingestion. Catalog entries do not automatically change rankings.','sourceCount':len(SOURCES),'sources':SOURCES}
(PUBLIC/'data-catalog.json').write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + '\n')
(PUBLIC/'metric-recipes.json').write_text(json.dumps({'version':catalog['version'],'recipes':RECIPES}, indent=2, ensure_ascii=False) + '\n')

lines = ['# 20/20 Free Public Data Catalog', '', catalog['description'], '', '| Dataset | Publisher | Access | Status | Sectors | |', '|---|---|---|---|---|---|']
for source in SOURCES:
    sectors = ', '.join(source['sectors'][:4]) + ('…' if len(source['sectors']) > 4 else '')
    lines.append(f"| [{source['name']}]({source['url']}) | {source['publisher']} | `{source['access']}` | `{source['status']}` | {sectors} | [Endpoint]({source['endpoint']}) |")
lines += ['', '## Metric recipes', '']
for recipe in RECIPES:
    lines.append(f"### {recipe['name']}")
    lines.append(f"- Sources: {', '.join(recipe['sources'])}")
    lines.append(f"- Grain: `{recipe['grain']}`")
    lines.append(f"- Fields: {', '.join(recipe['fields'])}")
    lines.append(f"- Normalize: {', '.join(recipe['normalization'])}")
    lines.append('')
lines += ['## Safety and provenance', '', '- Keyless/open sources can be sampled by the bounded ingestion script.', '- Free-registration and API-key sources remain documented but are not called until credentials are intentionally configured.', '- No catalog entry automatically changes sector scores or rankings.', '- Every promoted metric must retain source ID, endpoint, retrieval time, unit, geography, period, vintage, and comparability notes.']
(PUBLIC/'data-catalog.md').write_text('\n'.join(lines) + '\n')
print(f'Generated {len(SOURCES)} catalog sources and {len(RECIPES)} metric recipes')
