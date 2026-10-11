#!/usr/bin/env python3
"""Run the replica over EVERY parsed card (tolerant). Prints mismatch rates per quantity and lists. Usage: python run_all_cards.py [-v]"""
import glob, json, os, sys, collections, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine_replica as E
E_cyc = E.cyc_cap

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
verbose = '-v' in sys.argv
stats = collections.defaultdict(lambda: [0, 0, []])   # name -> [ok, n, mismatches]
errs = collections.defaultdict(list)


def rec(name, ok, tag):
    s = stats[name]
    s[1] += 1
    s[0] += bool(ok)
    if not ok:
        s[2].append(tag)


for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'cards', '*.json'))):
    card = json.load(open(f, encoding='utf-8'))
    t = card['ticker_file']
    q = card.get('quality')
    if not q or len(q.get('components', {})) < 8:
        errs['noquality'].append(t)
        continue
    card['_revenue_ltm'] = E.revenue_ltm(t)
    try:
        got = E.quality_from_card(card)
        excl = [n for n, k in q['components'].items() if k.get('excluded')]
        for n, v in got.items():
            exp = q['components'][n]['points']
            if exp is None:
                continue
            rec('comp:' + n, abs(v - exp) < 0.051, (t, v, exp))
        comps = {n: v for n, v in got.items() if n not in excl}
        comps['Дисципліна'] = E.discipline(card)
        wsum = sum(E.WEIGHTS[n] for n in comps)
        rec('comp:Дисципліна', abs(comps['Дисципліна'] - q['components']['Дисципліна']['points']) < 0.051, (t, comps['Дисципліна'], q['components']['Дисципліна']['points']))
        pen = E.flag_penalty_from_table(card)
        rec('penalty', q.get('flag_penalty') is not None and abs(pen - q['flag_penalty']) < 0.051, (t, pen, q.get('flag_penalty')))
        score = max(0.0, (sum(comps.values()) * 100.0 / wsum if excl else sum(comps.values())) - pen)
        rec('score', abs(float('%.1f' % score) - q['score_final']) < 0.051, (t, float('%.1f' % score), q['score_final']))
        reviewed = (card['header'].get('taras_review_line') or '').startswith('Тарас переглянув')
        crit = any(r['severity'] == 'критичний' and r['flag'] not in E.PRICE_FLAGS for r in card['flags']['table'])
        lvl = E.level_from(score, reviewed, crit)
        sbc_r = E.getv(q['components']['Капітал і SBC'], 'оплата акціями до FCF')
        loss = q['components']['Прибутковість']['points'] == 0
        e_rule = loss or (sbc_r is not None and sbc_r >= 1.0)
        if e_rule:
            lvl = 'E'
        rec('level', lvl == q['level_final'], (t, lvl, q['level_final'], q.get('level_cut_tail')))
        if q['level_final'] == 'E' and not e_rule:
            stats['level E by registry tag (not loss, not SBC>=100%)'][1] += 1
            stats['level E by registry tag (not loss, not SBC>=100%)'][2].append(t)
    except Exception as e:
        errs['quality:' + str(type(e).__name__)].append((t, str(e)[:80]))
    try:
        sc = E.lens_scores(card, t)
        cyc = E_cyc(card)
        if cyc and sc['PEG'] > 1:
            sc['PEG'] = 1
        for k in ['PEG', 'Проти S&P 500', 'FCF yield після SBC', 'Ріст проти EPS індексу', 'Проти власної історії']:
            exp = card['valuation']['lenses'][k]['score']
            rec('lens:' + k, sc[k] == exp, (t, sc[k], exp, ' | '.join(card['valuation']['hysteresis'])[:60]))
    except Exception as e:
        errs['lens:' + str(type(e).__name__)].append((t, str(e)[:80]))
    try:
        r = E.x2_full(card, t)
        x = card['x2']
        shown = [E.nz(c) for c in x['cagr']]
        for k, s_ in zip(('pess', 'base', 'opt'), shown):
            rec('x2cagr:' + k, abs(r[k]['cagr'] - s_) <= 0.3, (t, round(r[k]['cagr'], 1), s_))
    except Exception as e:
        errs['x2:' + str(type(e).__name__)].append((t, str(e)[:80]))

print('cards parsed', len(glob.glob(os.path.join(ROOT, 'data', 'cards', '*.json'))))
for k, (ok, n, bad) in sorted(stats.items()):
    print('%-36s %4d / %-4d %s' % (k, ok, n, (bad[:8] if verbose or len(bad) <= 4 else str(bad[:4]) + ' ...')))
for k, v in errs.items():
    print('ERR', k, len(v), v[:5])


# ---------------- verdict / price word on all cards (uses displayed lens sum and displayed x2 CAGRs to isolate the rule layer) ----------------
vstats = collections.defaultdict(lambda: [0, 0, []])
for f in sorted(glob.glob(os.path.join(ROOT, 'data', 'cards', '*.json'))):
    card = json.load(open(f, encoding='utf-8'))
    t = card['ticker_file']
    q = card.get('quality')
    if not q or q.get('level_final') is None or not card.get('valuation') or card['valuation'].get('lens_sum') is None or not card.get('x2') or not card['x2'].get('cagr'):
        continue
    try:
        h = card['header']
        level, score = q['level_final'], q['score_final']
        v = card['valuation']
        g = v.get('eps_growth_peg_pct')
        shown_c = [E.nz(c) for c in card['x2']['cagr']]
        base_c, bear_c = shown_c[1], shown_c[0]
        trap = any(rr['flag'] == 'вартісна пастка' for rr in card['flags']['table'])
        word = E.price_word(v['lens_sum'], h.get('ntm_pe'), score, g, level, base_c, False)
        shown_word = E.WORD_UA.get(h.get('price_word_chip', ''), None)
        if shown_word:
            rec2 = vstats['price_word']; rec2[1] += 1; rec2[0] += (word == shown_word)
            if word != shown_word:
                rec2[2].append((t, word, shown_word, v['lens_sum'], g, level, base_c))
        cell = E.MATRIX[level][word]
        peg = h['ntm_pe'] / g if (g and g > 0 and h.get('ntm_pe')) else None
        if level == 'A' and peg is not None and peg < 0.5:
            cell = 'BUY'
        qual_crit = any(rr['severity'] == 'критичний' and rr['flag'] not in E.PRICE_FLAGS for rr in card['flags']['table'])
        verdict = cell
        bar = 14.0 if level == 'A' else 15.0
        if qual_crit and verdict == 'BUY':
            verdict = 'BUY WAIT' if level in 'ABC' else 'AVOID'
        qc_rows = [rr for rr in card['flags']['table'] if rr['severity'] == 'критичний' and rr['flag'] not in E.PRICE_FLAGS and not (rr['points_removed'] == 0.0 and 'сусідньому' in rr['note'])]
        gwp = any(rr['flag'] == 'виручка росте, а прибутки і маржа ні' and rr['severity'] == 'критичний' for rr in card['flags']['table'])
        rev_ntm = E.getp(q['components']['Ріст'], 'ріст виручки')
        if len(qc_rows) >= 2:
            verdict = 'AVOID'                                   # several critical flags: 'бізнес не фінансує себе сам'
        elif gwp and rev_ntm is not None and rev_ntm < 0.10:
            verdict = 'AVOID'                                   # broken thesis: growth without profit and revenue growth < 10 %
        elif gwp and verdict in ('BUY', 'STRONG BUY'):
            verdict = 'BUY WAIT' if level in 'ABC' else 'AVOID'  # thesis in question
        reviewed = (h.get('taras_review_line') or '').startswith('Тарас переглянув')
        gi = q['components']['Ріст']['inputs']
        revg = E.getp(q['components']['Ріст'], 'ріст виручки')
        epsg = E.getp(q['components']['Ріст'], 'ріст EPS')
        if verdict == 'BUY' and word == 'CHEAP' and level in 'AB' and reviewed and revg is not None and epsg is not None and revg >= 0.10 and epsg >= 0.14 and base_c >= bar and bear_c >= 0 and not qual_crit:
            verdict = 'STRONG BUY'
        if verdict in ('BUY', 'STRONG BUY') and base_c < 10.0:
            verdict = 'BUY WAIT'
        shown = h['verdict_line']
        target = h.get('shadow_verdict') if shown in ('НЕ МІЙ СЕКТОР', 'ЛИШЕ СПЕКУЛЯЦІЯ') else shown
        r3 = vstats['verdict(shadow if gate0)']; r3[1] += 1; r3[0] += (verdict == target)
        if verdict != target:
            r3[2].append((t, verdict, target, shown, level, word))
    except Exception as e:
        errs['verdict:' + type(e).__name__].append((t, str(e)[:60]))
print('--- rule layer on displayed inputs ---')
for k, (ok, n, bad) in vstats.items():
    print('%-30s %4d / %-4d %s' % (k, ok, n, bad[:10]))
for k, v in errs.items():
    if k.startswith('verdict'):
        print('ERR', k, len(v), v[:3])
