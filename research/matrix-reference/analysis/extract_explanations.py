#!/usr/bin/env python3
"""Collect every distinct explanatory sentence the cards print (numbers masked), with the tickers it appears on.
Output: data/derived/explanations.tsv (masked_text, n_cards, example_ticker, example_raw)."""
import glob, os, re, collections
root = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
files = sorted(glob.glob(os.path.join(root, 'data', 'cards', '*.simple.txt')) + glob.glob(os.path.join(root, 'data', 'cards', '*.detailed.txt')))
mask = lambda s: re.sub(r'\d+([.,]\d+)?', '#', s)
seen = collections.OrderedDict()
for f in files:
    t = os.path.basename(f).split('.')[0]
    for ln in open(f, encoding='utf-8'):
        ln = ln.rstrip('\n').strip()
        if len(ln) < 70 or ln.startswith('#') or '\t' in ln[:3]:
            continue
        k = mask(ln)
        d = seen.setdefault(k, {'tick': set(), 'ex': (t, ln)})
        d['tick'].add(t)
os.makedirs(os.path.join(root, 'data', 'derived'), exist_ok=True)
with open(os.path.join(root, 'data', 'derived', 'explanations.tsv'), 'w', encoding='utf-8') as o:
    for k, d in sorted(seen.items(), key=lambda kv: -len(kv[1]['tick'])):
        o.write('%d\t%s\t%s\n' % (len(d['tick']), d['ex'][0], d['ex'][1]))
print(len(seen), 'distinct lines')
