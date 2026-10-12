#!/usr/bin/env python3
"""data/derived/taras-all.json + taras-trades.csv: Taras's paid-tier content per company (rating history, theses, videos with word, trades)."""
import csv, glob, json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
out = {}; trades = []
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'cards', '*.json'))):
    c = json.load(open(f, encoding='utf-8'))
    t = c.get('taras')
    if not t:
        continue
    out[c['ticker_file']] = {'headline': t.get('headline'), 'paid_headline': t.get('paid_headline'), 'timeline': t.get('timeline'), 'trades': t.get('trades'),
                             'position_line': (c.get('detailed') or {}).get('position_line'), 'taras_review_line': c['header'].get('taras_review_line'), 'holds': c['header'].get('taras_holds')}
    for tr in t.get('trades', []):
        trades.append([c['ticker_file'], tr])
json.dump(out, open(os.path.join(ROOT, 'data', 'derived', 'taras-all.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open(os.path.join(ROOT, 'data', 'derived', 'taras-trades.csv'), 'w', encoding='utf-8', newline='') as fo:
    w = csv.writer(fo); w.writerow(['ticker', 'trade']); w.writerows(trades)
print(len(out), 'companies with Taras timeline;', len(trades), 'trade lines')
