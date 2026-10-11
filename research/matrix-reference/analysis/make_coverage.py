#!/usr/bin/env python3
"""coverage-matrix.csv + taxonomy tables from parsed cards."""
import csv, glob, json, os, re, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
rows = []
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'cards', '*.json'))):
    c = json.load(open(f, encoding='utf-8'))
    t = c['ticker_file']
    h, q = c['header'], c.get('quality') or {}
    if len(q.get('components', {})) < 8:
        continue
    txt = open(os.path.join(ROOT, 'data', 'cards', t + '.simple.txt'), encoding='utf-8').read().replace(chr(160), ' ')
    sub = re.search(r'Поруч у субсекторі: ([^\n]+)', txt)
    basket = re.search(r'Кошик: ([^·\n]+)', txt)
    themes = re.search(r'Кошик: [^\n]*· теми: ([^\n]+)', txt)
    gate = c['detailed'].get('gate0', '')
    comps = q['components']
    flags = c['flags'].get('counts', {})
    rows.append({
        'ticker': t, 'name': h['name'], 'exchange': h.get('exchange'), 'currency': 'USD', 'basket': (basket.group(1).strip() if basket else gate.split(' · ')[-1].split(':')[0]), 'themes': themes.group(1) if themes else '',
        'subsector_peers': sub.group(1) if sub else '', 'business_type': comps['Прогнозованість']['inputs']['тип бізнесу']['raw'], 'moat': comps['Моат']['inputs']['конкурентна перевага']['raw'],
        'growth_source': comps['Дисципліна']['inputs']['джерело росту']['raw'], 'level': q['level_final'], 'score': q['score_final'], 'level_cap_tail': q.get('level_cut_tail', '').strip('; '), 'price_word': h.get('price_word_chip'),
        'lens_sum': (c.get('valuation') or {}).get('lens_sum'), 'verdict': h.get('verdict_line'), 'shadow': h.get('shadow_verdict') or '', 'reviewed': int((h.get('taras_review_line') or '').startswith('Тарас переглянув')),
        'taras_holds': int(h.get('taras_holds', False)), 'crit': flags.get('critical', 0), 'serious': flags.get('serious', 0), 'minor': flags.get('minor', 0),
        'cycle_peak': int(bool(h.get('cycle_peak_note'))), 'market_cap_usd_b': round((h.get('market_cap') or 0) / 1e9, 1), 'ntm_pe': h.get('ntm_pe'), 'completeness_pct': h.get('completeness_pct'),
        'basis': 'NTM P/E',
    })
with open(os.path.join(ROOT, 'coverage-matrix.csv'), 'w', encoding='utf-8', newline='') as fo:
    w = csv.DictWriter(fo, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
def cnt(k):
    return collections.Counter(r[k] for r in rows)
print({k: dict(cnt(k)) for k in ['exchange', 'basket', 'business_type', 'moat', 'growth_source', 'level', 'price_word', 'verdict', 'reviewed', 'cycle_peak']})
