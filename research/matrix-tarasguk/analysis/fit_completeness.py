#!/usr/bin/env python3
"""Recover data-completeness gap weights: completeness % = 100 - sum(weight of each missing field)."""
import glob, os, re, json
import numpy as np
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
rows = []
names = {}
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'cards', '*.simple.txt'))):
    t = os.path.basename(f)[:-len('.simple.txt')]
    s = open(f, encoding='utf-8').read().replace(chr(160), ' ')
    m = re.search(r'Заповненість полів\nщо саме\tстан\tхто закриває\n(.*?)\nзаповнені поля', s, re.S)
    if not m:
        continue
    lines = [l for l in m.group(1).split('\n') if l.strip()]
    tot = next((l for l in lines if l.startswith('усього полів')), None)
    if not tot:
        continue
    pct = float(re.search(r'(\d+) %', tot.split('\t')[1]).group(1))
    gaps = []
    for l in lines:
        if l.startswith('усього полів'):
            continue
        g = l.split('\t')[0].strip()
        g = re.sub(r'\s+', ' ', g)
        gaps.append(g)
        names[g] = names.get(g, 0) + 1
    rows.append((t, pct, gaps))
keys = sorted(names, key=lambda k: -names[k])
X = np.zeros((len(rows), len(keys))); y = np.zeros(len(rows))
for i, (t, pct, gaps) in enumerate(rows):
    for g in gaps:
        X[i, keys.index(g)] = 1
    y[i] = 100 - pct
sol = np.linalg.lstsq(X, y, rcond=None)[0]
res = X @ sol - y
out = {'n_cards': len(rows), 'max_abs_residual': float(abs(res).max()), 'weights': {k: round(float(v), 2) for k, v in zip(keys, sol)}, 'counts': names}
json.dump(out, open(os.path.join(ROOT, 'formulas', 'data-completeness-fit.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(rows), 'cards; residual max', round(float(abs(res).max()), 2), 'rank', np.linalg.matrix_rank(X), 'of', len(keys))
for k, v in zip(keys, sol):
    print('%6.2f  n=%3d  %s' % (v, names[k], k[:110]))
