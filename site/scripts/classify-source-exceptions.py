from __future__ import annotations

import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
report = json.loads((ROOT / 'public/update-report.json').read_text())
items = []
for result in report.get('results', []):
    if result.get('status') == 'ok':
        continue
    status = result.get('status')
    code = result.get('httpStatus')
    host = urlparse(result['url']).netloc.lower()
    if code == 404:
        category = 'broken-or-moved-link'
        priority = 'high'
        action = 'Locate the current official page or replace the reference with a stable official publication URL.'
    elif code == 403:
        category = 'access-restricted'
        priority = 'medium'
        action = 'Try the official index, PDF, API, or alternate publication URL; keep the claim marked for human verification.'
    else:
        category = 'transient-or-network-failure'
        priority = 'medium'
        action = 'Retry on the next scheduled run; if repeated, test DNS/TLS and locate an alternate official URL.'
    items.append({
        'sourceId': result['id'],
        'title': result['title'],
        'url': result['url'],
        'host': host,
        'status': status,
        'httpStatus': code,
        'category': category,
        'priority': priority,
        'recommendedAction': action,
        'automatedInterpretation': 'This is a review signal, not proof that the source is invalid and not permission to rewrite the related claim automatically.',
    })
items.sort(key=lambda item: ({'high': 0, 'medium': 1, 'low': 2}[item['priority']], item['host'], item['title']))
summary = {
    'generatedAt': datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z'),
    'sourceAuditGeneratedAt': report.get('generatedAt'),
    'total': len(items),
    'byCategory': dict(Counter(item['category'] for item in items)),
    'byHost': dict(Counter(item['host'] for item in items)),
    'policy': 'Review queue only. It does not modify source links, claims, scores, rankings, or the evidence graph.',
    'items': items,
}
(ROOT / 'public/source-review-queue.json').write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(json.dumps({key: summary[key] for key in ('generatedAt', 'total', 'byCategory')}, indent=2))
