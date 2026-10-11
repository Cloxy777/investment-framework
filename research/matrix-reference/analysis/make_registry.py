#!/usr/bin/env python3
"""data/derived/registry-tags.csv: the non-derivable per-company inputs (registry tags) + membership lists + Taras fields, one row per card."""
import csv, glob, json, os, re, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
mem = json.load(open(os.path.join(ROOT, 'data', 'lists', 'screener-filter-membership.json'), encoding='utf-8'))
inv = collections.defaultdict(lambda: collections.defaultdict(list))
for k, v in mem.items():
    key, val = k.split('=', 1)
    for t in v:
        inv[t][key].append(val)
scr = json.load(open(os.path.join(ROOT, 'data', 'lists', 'screener-all.json'), encoding='utf-8'))
taras = {}
for r in scr['rows']:
    t = (r['ticker'] or '').replace('/t/', '').strip('/')
    cells = r['cells']
    taras[t] = {'review': cells[14] if len(cells) > 14 else '', 'taras_rating': cells[15] if len(cells) > 15 else ''}
os.makedirs(os.path.join(ROOT, 'data', 'derived'), exist_ok=True)
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'cards', '*.json'))):
    c = json.load(open(f, encoding='utf-8'))
    t = c['ticker_file']
    q = c.get('quality') or {}
    comps = q.get('components', {})
    def raw(n, lab):
        d = comps.get(n, {}).get('inputs', {}).get(lab)
        return d['raw'] if d else ''
    h = c['header']
    rows.append({
        'ticker': t, 'name': h.get('name'), 'exchange': h.get('exchange'), 'basket': ';'.join(inv[t].get('sector', [])), 'subsectors': ';'.join(inv[t].get('subsector', [])),
        'sp500': int('sp500' in inv[t].get('index', [])), 'nasdaq100': int('nasdaq100' in inv[t].get('index', [])),
        'business_type': raw('Прогнозованість', 'тип бізнесу'), 'moat': raw('Моат', 'конкурентна перевага'), 'ai_risk': raw('Моат', 'ризик від ШІ'), 'market_share_trend': raw('Моат', 'куди йде частка ринку'),
        'growth_source': raw('Дисципліна', 'джерело росту'), 'capex_funding': raw('Дисципліна', 'чим фінансується capex'), 'margin_trend': raw('Маржа', 'куди йде маржа'),
        'tag_source': (comps.get('Прогнозованість', {}).get('inputs', {}).get('тип бізнесу', {}) or {}).get('source', ''),
        'verdict': h.get('verdict_line'), 'shadow': h.get('shadow_verdict') or '', 'level': q.get('level_final'), 'score': q.get('score_final'), 'price_word': h.get('price_word_chip'),
        'review_state': taras.get(t, {}).get('review', ''), 'taras_rating': taras.get(t, {}).get('taras_rating', ''), 'taras_review_line': h.get('taras_review_line') or '', 'taras_holds': int(h.get('taras_holds', False)),
        'taras_videos': len([r for r in (c.get('taras') or {}).get('timeline', []) if r['kind'] == 'відео']), 'taras_trades': len((c.get('taras') or {}).get('trades', [])),
    })
with open(os.path.join(ROOT, 'data', 'derived', 'registry-tags.csv'), 'w', encoding='utf-8', newline='') as fo:
    w = csv.DictWriter(fo, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print(len(rows), 'rows;', collections.Counter(r['basket'] for r in rows).most_common(8))
