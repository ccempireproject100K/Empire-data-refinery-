import json
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'

SAMPLES = [
    {'id':'sec-company-tickers','catalogId':'sec-edgar','url':'https://www.sec.gov/files/company_tickers.json','description':'SEC public-company ticker/CIK metadata'},
    {'id':'world-bank-us-gdp','catalogId':'world-bank','url':'https://api.worldbank.org/v2/country/USA/indicator/NY.GDP.MKTP.CD?format=json&per_page=5','description':'World Bank GDP current US dollars for the United States'},
    {'id':'bls-cpi','catalogId':'bls-data','url':'https://api.bls.gov/publicAPI/v2/timeseries/data/CUUR0000SA0?latest=true','description':'BLS latest CPI-U all-items series'},
    {'id':'census-acs-us','catalogId':'census-developer','url':'https://api.census.gov/data/2024/acs/acs1?get=NAME,B01001_001E,B19013_001E&for=us:1','description':'Census ACS population and median household income for the United States'},
    {'id':'openfda-drug-enforcement','catalogId':'openfda','url':'https://api.fda.gov/drug/enforcement.json?limit=2','description':'openFDA drug enforcement sample'},
    {'id':'clinicaltrials-diabetes','catalogId':'clinicaltrials','url':'https://clinicaltrials.gov/api/v2/studies?query.term=diabetes&pageSize=2','description':'ClinicalTrials.gov diabetes study sample'},
]


def shrink(value, depth=0):
    if depth > 3:
        return '[truncated]'
    if isinstance(value, list):
        return [shrink(item, depth + 1) for item in value[:3]]
    if isinstance(value, dict):
        items = list(value.items())
        if len(items) > 40:
            items = items[:40]
        return {str(key): shrink(item, depth + 1) for key, item in items}
    if isinstance(value, str) and len(value) > 500:
        return value[:500] + '…'
    return value


def main():
    results = []
    for item in SAMPLES:
        checked_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
        request = urllib.request.Request(item['url'], headers={'User-Agent': '20-20 Data Refinery public research; contact via project owner'})
        record = {**item, 'checkedAt': checked_at}
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                body = response.read(2_000_000)
                record['status'] = 'ok' if 200 <= response.status < 300 else 'http-error'
                record['httpStatus'] = response.status
                record['contentType'] = response.headers.get('content-type', '')
                record['bytesRead'] = len(body)
                try:
                    record['sample'] = shrink(json.loads(body.decode('utf-8')))
                except (UnicodeDecodeError, json.JSONDecodeError):
                    record['sample'] = {'textPreview': body[:500].decode('utf-8', errors='replace')}
        except urllib.error.HTTPError as error:
            record.update({'status':'http-error','httpStatus':error.code,'error':str(error.reason)})
        except Exception as error:
            record.update({'status':'error','error':f'{type(error).__name__}: {error}'})
        results.append(record)
    report = {
        'version': '2026-10-15-phase-two',
        'generatedAt': datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'),
        'policy': 'Bounded samples from official public endpoints only. Samples demonstrate access and schema; they do not change sector rankings or claims.',
        'sampleCount': len(results),
        'okCount': sum(item.get('status') == 'ok' for item in results),
        'results': results,
    }
    (PUBLIC / 'free-data-samples.json').write_text(json.dumps(report, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'sampleCount': report['sampleCount'], 'okCount': report['okCount'], 'statuses': [item['status'] for item in results]}, indent=2))


if __name__ == '__main__':
    main()
