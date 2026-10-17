from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
DATA = json.loads((PUBLIC / 'data.json').read_text())
ARCHIVE_DATE = DATA.get('version', '2026-10-15')


def source_type(title: str) -> str:
    t = title.lower()
    if any(k in t for k in ['sec filing', 'annual report', '10-k', '10k', 'regulatory']):
        return 'company or regulatory filing'
    if any(k in t for k in ['survey', 'customer', 'satisfaction', 'review']):
        return 'customer or survey evidence'
    if any(k in t for k in ['census', 'fred', 'bea', 'bls', 'iea', 'world bank', 'government']):
        return 'official statistics'
    if any(k in t for k in ['forecast', 'mckinsey', 'gartner', 'report']):
        return 'research or forecast'
    return 'public source'


def source_id(sector_id: str, index: int) -> str:
    return f'src-{sector_id}-{index + 1:02d}'


def claim_id(slug: str, index: int) -> str:
    return f'{slug}-claim-{index + 1:02d}'

sources = []
claims = []
sector_index = []

for sector in DATA['sectors']:
    refs = sector.get('references', [])
    by_url = {ref.get('url'): source_id(sector['id'], i) for i, ref in enumerate(refs) if ref.get('url')}
    local_sources = []
    for i, ref in enumerate(refs):
        sid = source_id(sector['id'], i)
        item = {
            'id': sid,
            'title': ref.get('title', 'Untitled public source'),
            'url': ref.get('url', ''),
            'sectorIds': [sector['id']],
            'sourceType': source_type(ref.get('title', '')),
            'reviewState': 'source-linked',
            'archiveReviewDate': ARCHIVE_DATE,
            'freshnessStatus': 'review recommended',
            'claimCount': 0,
            'host': urlparse(ref.get('url', '')).netloc,
        }
        sources.append(item)
        local_sources.append(item)

    local_claims = []
    def add_claim(kind, text, evidence_level, source_ids=None, note=''):
        item = {
            'id': claim_id(sector['slug'], len(local_claims)),
            'sectorId': sector['id'],
            'sectorSlug': sector['slug'],
            'sectorName': sector['name'],
            'claimType': kind,
            'text': text,
            'evidenceLevel': evidence_level,
            'sourceIds': source_ids or [],
            'archiveReviewDate': ARCHIVE_DATE,
            'freshnessStatus': 'review recommended',
            'note': note,
        }
        local_claims.append(item)
        for src in local_sources:
            if src['id'] in item['sourceIds']:
                src['claimCount'] += 1
        return item

    add_claim('sector interpretation', sector.get('interpretation', ''), 'analyst synthesis', [], 'A concise interpretation of the sector dossier; not a measured fact.')
    for paragraph in [p.strip() for p in sector.get('bottomLine', '').split('\n\n') if p.strip()]:
        urls = re.findall(r'\((https?://[^)]+)\)', paragraph)
        linked = [by_url[url] for url in urls if url in by_url]
        clean = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1', paragraph)
        add_claim('research narrative', clean, 'source-linked narrative' if linked else 'analyst synthesis', linked, 'Source links are shown when the paragraph includes a matching public URL.')
    score_text = 'Provisional score profile: ' + ', '.join(f'{key} {value}/5' for key, value in sector.get('scores', {}).items()) + f'; composite {sector.get("composite", 0)}/5.'
    add_claim('priority model', score_text, 'provisional model', [], 'The score is a research-priority estimate, not a forecast or investment recommendation.')
    add_claim('measurement plan', 'Next measures: ' + ' '.join(sector.get('metrics', [])[:4]), 'measurement plan', [], 'Metrics are suggested diligence fields and are not themselves measured results.')
    for caveat in sector.get('caveats', [])[:3]:
        add_claim('caveat', caveat, 'interpretive caveat', [], 'Caveats bound how the dossier should be interpreted.')
    sector_index.append({
        'sectorId': sector['id'],
        'sectorSlug': sector['slug'],
        'sectorName': sector['name'],
        'rank': sector['rank'],
        'claimIds': [c['id'] for c in local_claims],
        'sourceIds': [s['id'] for s in local_sources],
        'claimCount': len(local_claims),
        'sourceCount': len(local_sources),
        'archiveReviewDate': ARCHIVE_DATE,
        'freshnessStatus': 'review recommended',
    })
    claims.extend(local_claims)

catalog = {
    'name': '20/20 Evidence Graph',
    'version': ARCHIVE_DATE,
    'description': 'Claim-level links between the 20/20 sector dossiers and their public source references. Archive review metadata is not a claim that every source was automatically rechecked on that date.',
    'freshnessPolicy': 'Only sources from hosts that returned a viewable 2xx response in the latest audit remain active. Excluded sources are retained in the audit and exclusion manifests for review.',
    'sectors': sector_index,
    'claims': claims,
    'sources': sources,
}
(PUBLIC / 'evidence.json').write_text(json.dumps(catalog, indent=2, ensure_ascii=False))
print(f'Generated {len(claims)} claims and {len(sources)} source records')
