#!/usr/bin/env python3
"""Build ../test-vectors.json: for every captured card the inputs (as displayed) and expected outputs. Also test-vectors.ndjson (one card per line)."""
import glob, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..')


def vector(c):
    q = c['quality']
    h = c['header']
    v = c.get('valuation') or {}
    x = c.get('x2') or {}
    comps = q['components']
    inputs = {
        'quality': {n: {k: i['raw'] for k, i in comp['inputs'].items()} for n, comp in comps.items()},
        'explain': {n: comp['explain'] for n, comp in comps.items()},
        'flags_table': c['flags']['table'], 'flag_sentences': c['flags']['sentences'],
        'review_line': h.get('taras_review_line'), 'cycle_peak_note': h.get('cycle_peak_note'),
        'price_usd': x.get('price_today'), 'ntm_pe': h.get('ntm_pe'), 'market_cap': h.get('market_cap'), 'eps_growth_peg_pct': v.get('eps_growth_peg_pct'),
        'lens_inputs': {k: {'value': l['value'], 'compare': l['compare']} for k, l in (v.get('lenses') or {}).items()},
        'hysteresis_notes': v.get('hysteresis'), 'x2_eps_today_ntm': (x.get('eps_today') or [None, None])[1], 'analyst_fy_table': x.get('analyst_table'),
        'ttm': {k: c['ttm'].get(k) for k in ('ttm_pe', 'ttm_pfcf', 'ttm_pocf', 'fcf_ttm', 'ocf_ttm')} if c.get('ttm') else None,
        'data_as_of': h.get('data_as_of'), 'completeness_pct': h.get('completeness_pct'),
    }
    expected = {
        'components': {n: comp['points'] for n, comp in comps.items()}, 'excluded_components': [n for n, comp in comps.items() if comp.get('excluded')],
        'flag_penalty': q.get('flag_penalty'), 'score': q.get('score_final'), 'level': q.get('level_final'), 'level_cut_tail': q.get('level_cut_tail'),
        'lens_scores': {k: l['score'] for k, l in (v.get('lenses') or {}).items()}, 'lens_sum': v.get('lens_sum'), 'price_word': h.get('price_word_chip'),
        'verdict': h.get('verdict_line'), 'shadow_verdict': h.get('shadow_verdict'),
        'x2': {k: x.get(k) for k in ('growth_paths', 'multiple_scenario', 'eps_5y', 'price_5y', 'cagr', 'x2_year', 'buy_price_table', 'bars')},
        'ten_signs': [(i['mark'], i['text']) for i in (c.get('ten_signs') or {}).get('items', [])],
        'needed_for_better_verdict': (c.get('detailed') or {}).get('needed'), 'what_decided': x.get('what_decided'),
    }
    return {'inputs': inputs, 'expected': expected}


out = {'_meta': {'captured': '2026-10-03', 'tier': 'paid (full access), 487 cards + ABNB', 'note': 'inputs are the raw values printed next to each component; expected are the displayed outputs. Reference implementation: analysis/engine_replica.py + analysis/run_all_cards.py'}, 'cards': {}, '_errors': []}
with open(os.path.join(ROOT, 'test-vectors.ndjson'), 'w', encoding='utf-8') as nd:
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'cards', '*.json'))):
        try:
            c = json.load(open(f, encoding='utf-8'))
            if not c.get('quality') or c['quality'].get('score_final') is None:
                out['_errors'].append((os.path.basename(f), 'no quality'))
                continue
            vec = vector(c)
            out['cards'][c['ticker_file']] = vec
            nd.write(json.dumps({'ticker': c['ticker_file'], **vec}, ensure_ascii=False) + '\n')
        except Exception as e:  # noqa
            out['_errors'].append((os.path.basename(f), str(e)[:80]))
json.dump(out, open(os.path.join(ROOT, 'test-vectors.json'), 'w', encoding='utf-8'), ensure_ascii=False)
print('cards', len(out['cards']), 'errors', out['_errors'][:5])
