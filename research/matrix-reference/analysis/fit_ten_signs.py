#!/usr/bin/env python3
"""Bracket the pass/fail threshold of each of the ten signs over all parsed cards."""
import glob, json, os, re, collections
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
def pnum(s):
    m = re.search(r'([+\-−]?)(\d+(?:[.,]\d+)?)', s)
    return None if not m else (-1 if m.group(1) in '-−' and m.group(1) else 1) * float(m.group(2).replace(',', '.'))
KINDS = [('rev', r'^Ріст виручки'), ('eps', r'^Ріст прибутків EPS'), ('margin', r'^Висока маржа'), ('recur', r'^Повторювана виручка'), ('fcfg', r'^Ріст FCF'), ('bal', r'^Баланс без боргу'),
         ('capexlight', r'^Capex-лайт'), ('buyback', r'^Buybacks без розмиття'), ('conc', r'^Без концентрації'), ('capexown', r'^Capex з власного')]
obs = collections.defaultdict(list)
for f in glob.glob(os.path.join(ROOT, 'data', 'cards', '*.json')):
    c = json.load(open(f, encoding='utf-8'))
    for it in c.get('ten_signs', {}).get('items', []):
        for k, pat in KINDS:
            if re.search(pat, it['text']):
                v = None
                tx = it['text']
                if k == 'bal' and 'чистий кеш' in tx:
                    v = -99
                elif k == 'fcfg' and "від'ємний" in tx:
                    v = -100
                elif k == 'conc' and 'немає клієнта від' in tx:
                    v = 0
                elif k == 'conc':
                    v = pnum(tx.split('клієнт')[-1]) if 'найбільший клієнт' in tx or 'виручки' in tx else None
                elif k in ('rev', 'eps', 'margin', 'fcfg', 'capexlight', 'buyback', 'bal'):
                    v = pnum(re.sub(r'^[^\d+\-−]*', '', tx.split(' ', 2)[-1]) if False else re.search(r'([+\-−]?\d+(?:[.,]\d+)?)\s*(?:%|x)', tx).group(0)) if re.search(r'([+\-−]?\d+(?:[.,]\d+)?)\s*(?:%|x)', tx) else None
                elif k == 'recur':
                    v = tx.split('виручка', 1)[-1].strip()
                obs[k].append((c['ticker_file'], it['mark'], v, tx))
out = {}
for k, rows in obs.items():
    if k == 'recur':
        t = collections.defaultdict(lambda: collections.Counter())
        for tk, m, v, tx in rows:
            t[v][m] += 1
        out[k] = {kk: dict(vv) for kk, vv in t.items()}
        continue
    pas = [v for tk, m, v, tx in rows if m == 'pass' and v is not None]
    fail = [v for tk, m, v, tx in rows if m == 'fail' and v is not None]
    unk = [tk for tk, m, v, tx in rows if m == 'unknown']
    out[k] = {'n': len(rows), 'pass_min': min(pas) if pas else None, 'pass_max': max(pas) if pas else None, 'fail_min': min(fail) if fail else None, 'fail_max': max(fail) if fail else None, 'unknown': len(unk)}
json.dump(out, open(os.path.join(ROOT, 'formulas', 'ten-signs-fit.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in out.items():
    print(k, json.dumps(v, ensure_ascii=False)[:400])
