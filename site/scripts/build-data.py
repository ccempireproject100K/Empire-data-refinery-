from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = Path('/home/ubuntu')
REPORT = SOURCE_ROOT / '20-20-research-report.md'
SECTOR_ROOT = SOURCE_ROOT / '20-20-sector-reports'
PUBLIC = ROOT / 'public'
CONTENT = PUBLIC / 'content'
EXCLUSIONS_PATH = PUBLIC / 'source-exclusions.json'
CONTENT.mkdir(parents=True, exist_ok=True)

TABLE_RE = re.compile(r'^\|\s*(\d+)\s*\|\s*(.*?)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*([\d.]+)\s*\|\s*\*\*([\d.]+)\*\*\s*\|\s*(.*?)\s*\|$')
URL_RE = re.compile(r'\[([^\]]+)\]\((https?://[^)]+)\)')
DEF_RE = re.compile(r'^\[\d+\]:\s+(https?://\S+)\s+"([^"]+)"', re.M)


def slugify(value: str) -> str:
    value = value.lower().replace('&', 'and')
    return re.sub(r'[^a-z0-9]+', '-', value).strip('-')


def clean_markdown(value: str) -> str:
    value = re.sub(r'\*\*([^*]+)\*\*', r'\1', value)
    value = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', value)
    return re.sub(r'\s+', ' ', value).strip()


def heading_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r'^##\s+(.+?)\s*$', text, re.M))
    blocks = []
    for i, match in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        blocks.append((match.group(1).strip(), text[match.end():end].strip()))
    return blocks


def block_for(blocks: list[tuple[str, str]], keywords: tuple[str, ...]) -> str:
    for heading, content in blocks:
        lower = heading.lower()
        if any(keyword in lower for keyword in keywords):
            return content
    return ''


def named_items(block: str) -> list[dict[str, str]]:
    items = []
    for line in block.splitlines():
        line = line.strip()
        match = re.match(r'^(?:\d+\.\s+|-\s+)?\*\*(.*?)\*\*\s*(?::|—|-)?\s*(.*)$', line)
        if match and match.group(2).strip():
            items.append({'name': clean_markdown(match.group(1)), 'description': clean_markdown(match.group(2))})
    return items


def bullet_items(block: str) -> list[str]:
    items = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith('- '):
            items.append(clean_markdown(line[2:]))
    return items


def sanitize_public_document(text: str, excluded_urls: set[str], excluded_hosts: set[str]) -> str:
    def remove_blocked_link(match: re.Match[str]) -> str:
        return '' if urlparse(match.group(2)).netloc.lower() in excluded_hosts else match.group(0)
    text = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', remove_blocked_link, text)
    for url in excluded_urls:
        text = text.replace(url, '')
    lines = []
    for line in text.splitlines():
        urls = re.findall(r'https?://\S+', line)
        if urls and any(urlparse(url.rstrip(').,')).netloc.lower() in excluded_hosts for url in urls):
            if line.lstrip().startswith(('-', '*', '[')):
                continue
            line = re.sub(r'https?://\S+', '', line)
        lines.append(line)
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(lines))


def intro_for(text: str, blocks: list[tuple[str, str]]) -> str:
    # Keep the introductory evidence-rich paragraphs before the industry map.
    chunks = []
    for heading, content in blocks:
        low = heading.lower()
        if any(k in low for k in ('industr', 'subsector', 'profit pool', 'candidate', 'company')):
            break
        if content:
            chunks.append(content)
        if len(chunks) >= 2:
            break
    value = '\n\n'.join(chunks)
    return value[:5000].strip()


synthesis = REPORT.read_text()
excluded_urls = set()
excluded_hosts = set()
if EXCLUSIONS_PATH.exists():
    exclusions = json.loads(EXCLUSIONS_PATH.read_text())
    excluded_urls = {item.get('url') for item in exclusions.get('items', []) if item.get('url')}
    excluded_hosts = set(exclusions.get('excludedHosts', []))
rankings: dict[str, dict] = {}
for line in synthesis.splitlines():
    match = TABLE_RE.match(line)
    if match:
        rank, sector, p, o, g, c, e, composite, interpretation = match.groups()
        rankings[sector.strip()] = {
            'rank': int(rank),
            'scores': {'profitability': float(p), 'opportunity': float(o), 'growth': float(g), 'customer': float(c), 'evidence': float(e)},
            'composite': float(composite),
            'interpretation': interpretation.strip(),
        }
ranked_names = {record['rank']: name for name, record in rankings.items()}

sectors = []
for path in sorted(SECTOR_ROOT.glob('*.md')):
    text = path.read_text()
    blocks = heading_blocks(text)
    file_number = int(path.stem)
    title_match = re.search(r'^#\s+(.+)$', text, re.M)
    title = title_match.group(1).strip() if title_match else ranked_names.get(file_number, f'Sector {file_number}')
    # The reports are numbered in the same order as the synthesis; this avoids title suffix drift.
    name = ranked_names.get(file_number, re.sub(r'\s+—.*$', '', title))
    industries_block = block_for(blocks, ('most relevant industries', 'industries and subsectors', 'industries / subsectors', 'profit pools'))
    companies_block = block_for(blocks, ('candidate leading companies', 'candidate companies', 'example companies'))
    metrics_block = block_for(blocks, ('what to measure', 'suggested 20/20 data fields', 'free public data sources and metrics', 'available metrics'))
    caveats_block = block_for(blocks, ('caveat', 'limitation', 'risk and interpretation'))
    refs_block = block_for(blocks, ('references', 'sources'))
    references = [{'title': label.strip(), 'url': url.strip()} for label, url in URL_RE.findall(refs_block)]
    references += [{'title': title.strip(), 'url': url.strip()} for url, title in DEF_RE.findall(refs_block)]
    seen = set()
    references = [ref for ref in references if not (ref['url'] in seen or seen.add(ref['url']))]
    references = [ref for ref in references if ref['url'] not in excluded_urls and urlparse(ref['url']).netloc.lower() not in excluded_hosts]
    ranking = rankings.get(name, {})
    sectors.append({
        'id': path.stem,
        'slug': slugify(name),
        'name': name,
        'rank': ranking.get('rank', file_number),
        'scores': ranking.get('scores', {'profitability': 0, 'opportunity': 0, 'growth': 0, 'customer': 0, 'evidence': 0}),
        'composite': ranking.get('composite', 0),
        'interpretation': ranking.get('interpretation', ''),
        'bottomLine': sanitize_public_document(intro_for(text, blocks), excluded_urls, excluded_hosts),
        'industries': named_items(industries_block) or [{'name': line, 'description': ''} for line in bullet_items(industries_block)],
        'companies': named_items(companies_block),
        'metrics': bullet_items(metrics_block),
        'caveats': bullet_items(caveats_block),
        'references': references,
        'sourceDocument': f'/content/sectors/{path.name}',
    })

sectors.sort(key=lambda item: item['rank'])
sector_public = CONTENT / 'sectors'
sector_public.mkdir(parents=True, exist_ok=True)
for path in sorted(SECTOR_ROOT.glob('*.md')):
    (sector_public / path.name).write_text(sanitize_public_document(path.read_text(), excluded_urls, excluded_hosts))
(CONTENT / 'full-research-report.md').write_text(sanitize_public_document(REPORT.read_text(), excluded_urls, excluded_hosts))

export = {
    'name': '20/20 Data Refinery',
    'version': '2026-10-15',
    'description': 'An evidence-aware research universe covering 20 sectors, their industries, candidate companies, metrics, sources, caveats, and provisional priority scores.',
    'methodology': {
        'sectorPriorityFormula': '0.35P + 0.25O + 0.20G + 0.10C + 0.10E',
        'companyQualityFormula': '0.30P + 0.20O + 0.20G + 0.15C + 0.15E',
        'pillars': [
            {'key': 'profitability', 'label': 'Profitability and cash economics', 'weight': 0.35},
            {'key': 'opportunity', 'label': 'Lucrativeness / opportunity', 'weight': 0.25},
            {'key': 'growth', 'label': 'Growth quality', 'weight': 0.20},
            {'key': 'customer', 'label': 'Customer quality', 'weight': 0.10},
            {'key': 'evidence', 'label': 'Evidence quality and comparability', 'weight': 0.10},
        ],
        'importantNote': 'Scores are provisional research-priority estimates, not investment advice or definitive league-table rankings.',
    },
    'sectors': sectors,
}
(PUBLIC / 'data.json').write_text(json.dumps(export, indent=2, ensure_ascii=False))

lines = [
    '# 20/20 Data Refinery — Structured Research Dataset', '',
    '> This export is intended for both people and AI agents. Scores are provisional research-priority estimates, not investment advice.', '',
    '## Methodology', '',
    f"Sector priority formula: `{export['methodology']['sectorPriorityFormula']}`. Company quality formula: `{export['methodology']['companyQualityFormula']}`.", '',
]
for pillar in export['methodology']['pillars']:
    lines.append(f"- **{pillar['label']}** (`{pillar['key']}`): weight {pillar['weight']:.0%}.")
lines.extend(['', '## Ranked sectors', ''])
for sector in sectors:
    lines.extend([
        f"### {sector['rank']}. {sector['name']}", '',
        f"- Slug: `{sector['slug']}`",
        f"- Composite: **{sector['composite']:.2f}**",
        f"- Scores: P {sector['scores']['profitability']:.1f}; O {sector['scores']['opportunity']:.1f}; G {sector['scores']['growth']:.1f}; C {sector['scores']['customer']:.1f}; E {sector['scores']['evidence']:.1f}",
        f"- Interpretation: {sector['interpretation']}",
        f"- Detail document: `/content/sectors/{sector['id']}.md`", '',
        '**Why it matters**', sector['bottomLine'], '', '**Industries**',
    ])
    for item in sector['industries']:
        lines.append(f"- **{item['name']}** — {item['description']}")
    lines.extend(['', '**Candidate companies (not a ranking)**'])
    for company in sector['companies']:
        lines.append(f"- **{company['name']}** — {company['description']}")
    lines.extend(['', '**What to measure**'])
    for metric in sector['metrics']:
        lines.append(f'- {metric}')
    lines.extend(['', '**Caveats**'])
    for caveat in sector['caveats']:
        lines.append(f'- {caveat}')
    lines.extend(['', '**References**'])
    for ref in sector['references']:
        lines.append(f"- [{ref['title']}]({ref['url']})")
    lines.extend(['', '---', ''])
(PUBLIC / 'content/full-dataset.md').write_text('\n'.join(lines))
print(f'Generated {len(sectors)} sectors and {sum(len(s["references"]) for s in sectors)} references')
