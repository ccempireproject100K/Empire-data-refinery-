from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import ssl
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
EVIDENCE_PATH = PUBLIC / 'evidence.json'
REPORT_PATH = PUBLIC / 'update-report.json'
CHECKS_PATH = PUBLIC / 'source-checks.json'


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def check(source: dict, timeout: float, previous: dict) -> dict:
    started = time.monotonic()
    url = source['url']
    item = {
        'id': source['id'], 'title': source['title'], 'url': url,
        'checkedAt': now_iso(), 'status': 'error', 'httpStatus': None,
        'etag': None, 'lastModified': None, 'contentHash': None,
        'changedSinceLastCheck': None, 'responseTimeMs': None, 'note': None,
    }
    try:
        request = Request(url, headers={'User-Agent': '20-20-source-checker/1.0 (+public research archive)'}, method='GET')
        context = ssl.create_default_context()
        with urlopen(request, timeout=timeout, context=context) as response:
            body = response.read(1_000_000)
            item['httpStatus'] = response.status
            item['etag'] = response.headers.get('ETag')
            item['lastModified'] = response.headers.get('Last-Modified')
            item['contentHash'] = hashlib.sha256(body).hexdigest()
            item['status'] = 'ok' if 200 <= response.status < 400 else 'http-error'
            old = previous.get(source['id'], {})
            if old.get('contentHash'):
                item['changedSinceLastCheck'] = old.get('contentHash') != item['contentHash']
            item['note'] = 'Fetched the first 1 MB for a bounded content fingerprint; not a full document archive.'
    except HTTPError as error:
        item['httpStatus'] = error.code
        item['status'] = 'http-error'
        item['note'] = f'HTTP error: {error.reason}'
    except (URLError, TimeoutError, OSError) as error:
        item['status'] = 'unreachable'
        item['note'] = str(error.reason if hasattr(error, 'reason') else error)
    finally:
        item['responseTimeMs'] = round((time.monotonic() - started) * 1000)
    return item


def main() -> None:
    parser = argparse.ArgumentParser(description='Check public 20/20 evidence sources and write an auditable report.')
    parser.add_argument('--timeout', type=float, default=12)
    parser.add_argument('--max-workers', type=int, default=8)
    parser.add_argument('--max-sources', type=int, default=0)
    args = parser.parse_args()
    evidence = json.loads(EVIDENCE_PATH.read_text())
    excluded_items = []
    exclusions_path = PUBLIC / 'source-exclusions.json'
    if exclusions_path.exists():
        excluded_items = json.loads(exclusions_path.read_text()).get('items', [])
    previous_items = {}
    if CHECKS_PATH.exists():
        try:
            previous_items = {item['id']: item for item in json.loads(CHECKS_PATH.read_text()).get('results', [])}
        except (json.JSONDecodeError, KeyError):
            previous_items = {}
    sources_by_url = {source['url']: source for source in evidence['sources'] if source.get('url')}
    for item in excluded_items:
        if item.get('url') and item['url'] not in sources_by_url:
            sources_by_url[item['url']] = {'id': item.get('sourceId', 'excluded-source'), 'title': item.get('title', 'Excluded source'), 'url': item['url']}
    sources = list(sources_by_url.values())[:args.max_sources or None]
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.max_workers)) as pool:
        futures = [pool.submit(check, source, args.timeout, previous_items) for source in sources]
        results = [future.result() for future in futures]
    results.sort(key=lambda item: item['id'])
    ok = sum(item['status'] == 'ok' for item in results)
    changed = sum(item['changedSinceLastCheck'] is True for item in results)
    report = {
        'name': '20/20 Source Update Report',
        'version': '2026-10-15',
        'generatedAt': now_iso(),
        'populationPolicy': 'Checks active sources plus previously excluded exact URLs so viewability can recover without automatic restoration.',
        'policy': 'This engine detects availability and bounded content fingerprints. It proposes review; it never silently changes claims, scores, or rankings.',
        'sourceCount': len(results), 'okCount': ok, 'errorCount': len(results) - ok, 'changedSinceLastCheck': changed,
        'results': results,
    }
    CHECKS_PATH.write_text(json.dumps({'generatedAt': report['generatedAt'], 'results': results}, indent=2, ensure_ascii=False))
    REPORT_PATH.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    print(json.dumps({'sourceCount': len(results), 'okCount': ok, 'errorCount': len(results) - ok, 'changedSinceLastCheck': changed, 'report': str(REPORT_PATH)}, indent=2))


if __name__ == '__main__':
    main()
