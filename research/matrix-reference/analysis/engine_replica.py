#!/usr/bin/env python3
"""Replica of the matrix.tarasguk.com engine, built only from what the UI displays.
Inputs come from data/cards/<T>.json (raw values the card prints next to every component).
Run:  python engine_replica.py          -> mismatch report per quantity over all cards.

Status of each rule is marked in formulas/*.md (Exact / Fitted / Hypothesis / Unknown)."""
import glob, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CARDS = os.path.join(ROOT, 'data', 'cards')

# ---------------- config (values printed on cards / methodology) ----------------
CFG = {
    'unknown_weight': 0.40,
    'years_profitable': {'full': 5, 'partial': 2, 'pts_full': 15.0, 'pts_partial': 9.75, 'pts_short': 5.25, 'pts_loss': 0.0, 'pts_unknown': 7.5},
    'growth': {'rev': (10.0, 20.0, [0.0, 2.0, 4.8, 8.0], 3.2), 'eps': (10.0, 15.0, 25.0, [0.0, 1.75, 4.2, 5.95, 7.0], 2.8), 'fcf': (10.0, 15.0, [0.0, 1.2, 3.0, 5.0], 2.0)},
    'margin': [(45.0, 10.0), (30.0, 8.0), (20.0, 6.0), (15.0, 4.0), (10.0, 2.0), (-1e9, 0.0)],
    'predictability': {'subscription': 15, 'payments_network': 15, 'data_ratings': 15, 'cloud_contracts': 14, 'cloud_hyperscaler': 14, 'platform': 12, 'software': 12,
                       'club_subscription': 10, 'retail_membership': 10, 'advertising': 9, 'chips': 9, 'semis_monopoly': 9, 'brand_one_off': 8, 'rental': 8,
                       'restaurant': 6, 'manufacturer': 6, 'cyclical': 3, 'commodity': 2, 'bank': 4, 'pharma': 3, 'undefined': 8,
                       'data_monopoly': 15, 'consumer_brand': 8, 'other': 8, 'reit': 8, 'heavy_machinery': 8, 'retail': 8},
    'moat': {'monopoly': 15, 'oligopoly': 12, 'network': 12, 'switching': 10, 'brand': 8, 'none': 2, 'absent': 2, 'unknown': 6},
    'ai_risk': {'strengthens': 2, 'neutral': 0, 'unknown': 0, 'threat': -3},
    'balance': {'net_cash': 10.0, 'ok': (1.5, 7.0), 'tolerable': (3.0, 4.0), 'bad': 1.0, 'unknown': 5.0},
    # capital & SBC: sum of sub-scores (SBC, ROIC, shares) - 10, plus buy-back adjustment, floor 0  [Fitted, 20/20 cards]
    'capital': {'sbc': [(5.0, 8.0), (15.0, 7.0), (30.0, 5.0), (1e9, 3.0)], 'sbc_unknown': 5.5,
                'roic': {'exc': 2.0, 'good': 1.0, 'mid': 0.0, 'minus': -2.0, 'unknown': 0.0},
                'shares': {'ng': 1.0, 'small': 0.0, 'dil': -1.0, 'unknown': 0.0},
                'buyback': {'high': 1.0, 'low': 0.0, 'div_only': -1.0, 'none': -2.0}},
}


WEIGHTS = {'Прибутковість': 15, 'Ріст': 20, 'Прогнозованість': 15, 'Моат': 15, 'Маржа': 10, 'Баланс': 10, 'Капітал і SBC': 10, 'Дисципліна': 5}


def pct(x):
    return None if x is None else x * 100.0


def bucket_desc(x, edges, vals):
    """edges ascending lower-bounds; returns vals[i] where x >= edges[i-1] ... helper not used"""
    raise NotImplementedError


def profitability(years):
    c = CFG['years_profitable']
    if years is None:
        return c['pts_unknown']
    if years <= 0:
        return c['pts_loss']
    if years >= c['full']:
        return c['pts_full']
    if years >= c['partial']:
        return c['pts_partial']
    return c['pts_short']


def growth(rev, eps, fcf):
    """rev/eps/fcf as fractions or None. FCF unknown -> 40% of its 5 pts."""
    out = 0.0
    w, g, p, u = CFG['growth']['rev']
    r = rev if rev is None else rev * 100
    out += u if r is None else (p[0] if r < 0 else p[1] if r < w else p[2] if r < g else p[3])
    w, g, gr, p, u = CFG['growth']['eps']
    e = eps if eps is None else eps * 100
    out += u if e is None else (p[0] if e < 0 else p[1] if e < w else p[2] if e < g else p[3] if e < gr else p[4])
    w, g, p, u = CFG['growth']['fcf']
    f = fcf if fcf is None else fcf * 100
    out += u if f is None else (p[0] if f < 0 else p[1] if f < w else p[2] if f < g else p[3])
    return round(out, 2)


def margin_pts(m):
    if m is None:
        return 5.0
    m *= 100
    for lo, pts in CFG['margin']:
        if m >= lo:
            return pts


def margin_full(m, trend, btype, rev_growth, fcf_margin, basket=None):
    """Margin component. Rules: bucket table; trend 'down' -> -2 (floor 0); software rule of 40 -> full 10;
    platform-type low margin that grows -> at least half of weight (5). [Fitted on 20 cards; type list for the half-weight rule is a Hypothesis]"""
    pts = margin_pts(m)
    if (basket == 'software' or (basket is None and btype == 'software')) and rev_growth is not None and fcf_margin is not None and (rev_growth + fcf_margin) * 100 >= 40.0:
        pts = 10.0
    if trend == 'up' and pts < 5.0 and btype in ('platform', 'subscription', 'software'):   # 'важіль масштабу' / 'не менше половини ваги'
        pts = 5.0
    if trend == 'down':
        pts = max(0.0, pts - 2.0)
    return pts


def balance(net_cash, d2e):
    b = CFG['balance']
    if net_cash is not None and net_cash > 0:
        return b['net_cash']
    if d2e is None:
        return b['unknown']
    return b['ok'][1] if d2e <= b['ok'][0] else b['tolerable'][1] if d2e <= b['tolerable'][0] else b['bad']


def capital(sbc_ratio, roic, share_change, buyback_yield, div_yield, sbc_thresholds=(5.0, 15.0, 30.0)):
    c = CFG['capital']
    if sbc_ratio is None:
        s = c['sbc_unknown']
    else:
        v = sbc_ratio * 100
        a, b, d = sbc_thresholds
        s = 8.0 if v < a else 7.0 if v < b else 5.0 if v < d else 3.0
    if roic is None:
        r = c['roic']['unknown']
    else:
        v = roic * 100
        r = c['roic']['exc'] if v >= 30 else c['roic']['good'] if v >= 20 else c['roic']['mid'] if v >= 10 else c['roic']['minus']
    if share_change is None:
        h = c['shares']['unknown']
    else:
        v = share_change * 100
        h = c['shares']['ng'] if v <= 0 else c['shares']['small'] if v < 2 else c['shares']['dil']
    by = (buyback_yield or 0) * 100
    dv = (div_yield or 0) * 100
    # high buy-back threshold: between 1.7 % (low) and 3.2 % (high) in the data; 2 % is a guess
    b = c['buyback']['high'] if by >= 2.0 else c['buyback']['low'] if by > 0 else (c['buyback']['div_only'] if dv > 0 else c['buyback']['none'])
    return max(0.0, s + r + h + b)


def getp(comp, prefix):
    for k, d in comp['inputs'].items():
        if k.startswith(prefix):
            return d['value']
    return None


def getv(comp, label):
    d = comp['inputs'].get(label)
    return None if d is None else d['value']


def raw(comp, label):
    d = comp['inputs'].get(label)
    return None if d is None else d['raw']


def quality_from_card(card):
    q = card['quality']
    C = q['components']
    res = {}
    res['Прибутковість'] = profitability(getv(C['Прибутковість'], 'роки прибутковості'))
    g = C['Ріст']
    res['Ріст'] = growth(getp(g, 'ріст виручки'), getp(g, 'ріст EPS'), getp(g, 'ріст FCF'))
    res['Прогнозованість'] = float(CFG['predictability'].get(raw(C['Прогнозованість'], 'тип бізнесу'), 8))
    moat = raw(C['Моат'], 'конкурентна перевага')
    ai = raw(C['Моат'], 'ризик від ШІ')
    share = raw(C['Моат'], 'куди йде частка ринку')
    res['Моат'] = max(0.0, float(CFG['moat'].get(moat, 6)) + {'unknown': 0, 'neutral': 0, 'negative': -3, 'positive': 2}.get(ai, 0) + {'down': -4}.get(share, 0))
    m = C['Маржа']
    net, opm = getv(m, 'чиста маржа'), getv(m, 'операційна маржа після податку')
    mm = None if (net is None and opm is None) else min(x for x in (net, opm) if x is not None)
    rev_g = getp(g, 'ріст виручки')
    fcf_m = None
    qr = quarterly_revenue(card['ticker_file'])
    if qr and len(qr) >= 8:
        rev_g = sum(qr[:4]) / sum(qr[4:8]) - 1          # LTM revenue growth (4 quarters vs previous 4): fits rule of 40 on 14/14 software cards
        try:
            fcf_m = card['ttm']['fcf_ttm'] / sum(qr[:4])
        except Exception:
            fcf_m = None
    elif card['ttm'].get('fcf_ttm') and card.get('_revenue_ltm'):
        fcf_m = card['ttm']['fcf_ttm'] / card['_revenue_ltm']
    res['Маржа'] = margin_full(mm, raw(m, 'куди йде маржа'), raw(C['Прогнозованість'], 'тип бізнесу'), rev_g, fcf_m, basket_of(card['ticker_file']))
    b = C['Баланс']
    res['Баланс'] = balance(getv(b, 'чистий кеш'), getv(b, 'борг до EBITDA'))
    k = C['Капітал і SBC']
    sbc = getv(k, 'оплата акціями до FCF')
    thr = (5.0, 15.0, 30.0)
    if sbc is None:
        sbc = getv(k, 'оплата акціями до виручки')
        thr = (5.0, 10.0, 20.0)
    res['Капітал і SBC'] = capital(sbc, getv(k, 'ROIC'), getv(k, 'зміна кількості акцій'), getv(k, 'дохідність викупу акцій'), getv(k, 'дивідендна дохідність'), thr)
    return res


def quarterly_revenue(t):
    txt = open(os.path.join(CARDS, t + '.simple.txt'), encoding='utf-8').read().replace(chr(160), ' ')
    i = txt.find('Виручка по кварталах' + chr(10) + 'Квартал' + chr(9) + 'виручка')
    if i < 0:
        return None
    out = []
    for m in re.finditer(r'^(\d\d\.\d\d\.\d{4})	\$([\d,]+)\s*(млрд|млн)?', txt[i:i + 3000], re.M):
        out.append(float(m.group(2).replace(',', '.')) * {'млрд': 1e9, 'млн': 1e6}.get(m.group(3), 1))
    return out


_BASKET = None


def basket_of(t):
    global _BASKET
    if _BASKET is None:
        _BASKET = {}
        pth = os.path.join(ROOT, 'data', 'lists', 'screener-filter-membership.json')
        if os.path.exists(pth):
            for k, v in json.load(open(pth, encoding='utf-8')).items():
                if k.startswith('sector='):
                    for x in v:
                        _BASKET[x] = k.split('=', 1)[1]
    return _BASKET.get(t)


def revenue_ltm(t):
    txt = open(os.path.join(CARDS, t + '.simple.txt'), encoding='utf-8').read().replace(chr(160), ' ')
    m = re.search(r'^Виручка[\n]\$([\d,]+) (млрд|млн)', txt, re.M)
    if not m:
        return None
    return float(m.group(1).replace(',', '.')) * (1e9 if m.group(2) == 'млрд' else 1e6)


def main():
    mism = {}
    n = 0
    for f in sorted(glob.glob(os.path.join(CARDS, '*.json'))):
        card = json.load(open(f, encoding='utf-8'))
        t = card['ticker_file']
        card['_revenue_ltm'] = revenue_ltm(t)
        got = quality_from_card(card)
        n += 1
        for name, v in got.items():
            exp = card['quality']['components'][name]['points']
            if abs(v - exp) > 0.051:
                mism.setdefault(name, []).append((t, v, exp))
    print('cards', n)
    for name in ['Прибутковість', 'Ріст', 'Прогнозованість', 'Моат', 'Маржа', 'Баланс', 'Капітал і SBC']:
        print('%-18s mismatches %d / %d  %s' % (name, len(mism.get(name, [])), n, mism.get(name, [])))


if __name__ == '__main__':
    main()


# ---------------- discipline, flag penalty, score, level (appended) ----------------
GROWTH_SRC = {'organic': 5.0, 'mixed': 4.0, 'acquisitions': 2.0, 'acquisition': 2.0, 'm&a': 2.0, 'unknown': 4.0}


def discipline(card):
    d = card['quality']['components']['Дисципліна']
    src = raw(d, 'джерело росту') or 'unknown'
    base = GROWTH_SRC.get(src, 4.0)
    ex = d['explain']
    if 'чисел OCF і capex немає' in ex:   # no capex numbers: registry funding tag moves the base 0 / -1 / -2
        tag = raw(d, 'чим фінансується capex')
        return base + {'ocf': 0.0, 'unknown': -1.0, 'debt': -2.0}.get(tag, 0.0)
    if '1 з 2 балів' in ex:
        return base - 1.0
    if '0 балів' in ex:   # external financing lands on balance sheet, or capex > OCF without passed waiver
        return base - 2.0
    return base


# penalty rules per flag (name -> kind). kinds: 'pen' (points by severity), 'graded' (already inside a component: 0), 'same_event' (0), 'price' (0), 'minor' (0)
NO_PENALTY_FLAGS = {
    'опціони зʼїдають виручку', 'розмиття акціонерів', 'зовнішнє фінансування capex', 'борг вище 1,5x EBITDA', 'ріст на обіцянках кількох клієнтів',
    'маржа стискається', 'витрати ростуть швидше за виручку', 'ризик дизрапції від ШІ', 'capex більший за операційний кеш',
}
PRICE_FLAGS = {'вартісна пастка', 'мультиплікатор поза межами розумного', 'дорого без росту', 'мультиплікатор вище стелі'}
SEV_PTS = {'критичний': 8.0, 'серйозний': 4.0, 'мінорний': 0.0}


def flag_penalty_from_table(card):
    tot = 0.0
    for r in card['flags']['table']:
        if not r['severity'] or r['flag'] in NO_PENALTY_FLAGS or r['flag'] in PRICE_FLAGS:
            continue
        if r['flag'] == 'виручка росте, а маржа і FCF ні' and (r['severity'] == 'мінорний' or any(x['flag'] == 'виручка росте, а прибутки і маржа ні' for x in card['flags']['table'])):
            continue
        tot += SEV_PTS[r['severity']]
    return tot


def level_from(score, reviewed, has_critical):
    s = float('%.1f' % score)
    lvl = 'A' if s >= 80 else 'B' if s >= 70 else 'C' if s >= 55 else 'D'
    if lvl == 'A' and not reviewed:
        lvl = 'B'
    if has_critical and lvl in ('A', 'B'):
        lvl = 'C'
    return lvl


def full_check():
    ok = {'discipline': 0, 'penalty': 0, 'score': 0, 'level': 0}
    n = 0
    bad = {k: [] for k in ok}
    for f in sorted(glob.glob(os.path.join(CARDS, '*.json'))):
        card = json.load(open(f, encoding='utf-8'))
        t = card['ticker_file']
        card['_revenue_ltm'] = revenue_ltm(t)
        q = card['quality']
        comps = quality_from_card(card)
        comps['Дисципліна'] = discipline(card)
        pen = flag_penalty_from_table(card)
        score = sum(comps.values()) - pen
        reviewed = (card['header'].get('taras_review_line') or '').startswith('Тарас переглянув')
        crit = any(r['severity'] == 'критичний' and r['flag'] not in PRICE_FLAGS for r in card['flags']['table'])
        lvl = level_from(score, reviewed, crit)
        n += 1
        checks = {'discipline': (comps['Дисципліна'], q['components']['Дисципліна']['points']), 'penalty': (pen, q.get('flag_penalty')), 'score': (float('%.1f' % score), q.get('score_final')), 'level': (lvl, q.get('level_final'))}
        for k, (a, b) in checks.items():
            good = (a == b) if k == 'level' else (b is not None and abs(a - b) < 0.051)
            ok[k] += good
            if not good:
                bad[k].append((t, a, b))
    print('--- full quality check (%d cards) ---' % n)
    for k in ok:
        print('%-10s exact %d / %d  mismatches: %s' % (k, ok[k], n, bad[k]))


if __name__ == '__main__':
    full_check()


# ---------------- price side: lenses, price word, verdict (appended) ----------------
SP_PE = 20.1          # S&P 500 forward P/E printed on every card (2026-10-03)
IDX_G = 13.6          # S&P 500 EPS growth printed on every card
YIELD_GOOD = 4.0      # 'поріг доброго FCF yield 4 %'


def cyc_cap(card):
    """PEG lens is capped at +1 only for 'possible cycle peak' (trailing EPS growth > 100 %), NOT for a loss->profit turnaround note."""
    n = card['header'].get('cycle_peak_note') or ''
    return bool(n) and 'вихід зі збитку' not in n


def nz(x):
    return float(re.sub(r'[^0-9.\-]', '', x.replace(',', '.').replace('\u2212', '-')))


def trailing_pe_stats(t):
    txt = open(os.path.join(CARDS, t + '.simple.txt'), encoding='utf-8').read().replace(chr(160), ' ')
    i = txt.find('Історія trailing P/E, помісячно\nРік\tСереднє')
    if i < 0:
        return None
    blk = txt[i:i + 1500]
    rows = [(int(m.group(1)), nz(m.group(2)), nz(m.group(3)), nz(m.group(4)), int(m.group(5))) for m in re.finditer(r'^(20\d\d)\t([\d,]+)\t([\d,]+)\t([\d,]+)\t(\d+)$', blk, re.M)]
    m = re.search(r'середнє за період\t([\d,]+)\t([\d,]+)\t([\d,]+)\t(\d+)', blk)
    return {'rows': rows, 'mean_all': nz(m.group(1)) if m else None}


def lens_scores(card, t):
    v = card['valuation']
    h = card['header']
    level = card['quality']['level_final']
    out = {}
    L = v['lenses']
    pe = h.get('ntm_pe')
    g = v.get('eps_growth_peg_pct')
    # PEG
    if pe is None or g is None or g <= 0:
        peg = None
        out['PEG'] = -2 if (g is not None and g <= 0) else 0
    else:
        peg = pe / g
        s = 2 if peg < 0.5 else 1 if peg < 1.0 else 0 if peg <= 1.3 else -1 if peg <= 2.0 else -2
        out['PEG'] = s
    out['_peg'] = peg
    # S&P
    ratio = pe / SP_PE if pe else None
    s = 0 if ratio is None else (1 if level in 'AB' else 0) if ratio <= 1.0 else 0 if ratio <= 1.3 else -1 if ratio <= 2.0 else -2
    out['Проти S&P 500'] = s
    # FCF yield
    fy = L['FCF yield після SBC']['value']
    if fy.strip() in ('немає', 'н/д'):
        out['FCF yield після SBC'] = 0
    else:
        y = nz(fy.replace('%', '').replace('+', '').strip())
        try:   # recompute from unrounded inputs: (FCF - SBC) / market cap
            sbc_r = card['quality']['components']['Капітал і SBC']['inputs'].get('оплата акціями до FCF', {}).get('value')
            fcf = card['ttm'].get('fcf_ttm')
            cap = h.get('market_cap')
            if sbc_r is not None and fcf and cap:
                y2 = fcf * (1 - sbc_r) / cap * 100
                if abs(y2 - y) < 0.2:
                    y = y2
        except Exception:
            pass
        out['FCF yield після SBC'] = 2 if y >= 4 else 1 if y >= 3 else 0 if y >= 2 else -1 if y >= 1 else -2
    # growth vs market
    if g is None:
        out['Ріст проти EPS індексу'] = 0
    else:
        out['Ріст проти EPS індексу'] = 1 if g >= 1.5 * IDX_G else -1 if g < 0.9 * IDX_G else 0
    # history
    hl = L['Проти власної історії']
    mt0 = re.search(r'trailing P/E ([\d,]+)', hl['value'])
    mm0 = re.search(r'власне середнє ([\d,]+) за 3 роки', hl['compare'])
    if hl['compare'].startswith('історії немає') or not mt0 or not mm0:
        out['Проти власної історії'] = 0
    else:
        mt = mt0
        mm = mm0
        cur, mean3 = nz(mt.group(1)), nz(mm.group(1))
        st = trailing_pe_stats(t)
        rows = st['rows']
        min5 = min(r[2] for r in rows)
        max3 = max(r[3] for r in rows[-3:])
        if cur <= min5 * 1.05:
            s = 2
        elif cur >= max3 * 0.95:
            s = -2
        elif cur < mean3 * 0.9:
            s = 1
        elif cur > mean3 * 1.1:
            s = -1
        else:
            s = 0
        if sum(r[4] for r in rows) < 36:   # history shorter than 3 years clamps to +-1
            s = max(-1, min(1, s))
        out['Проти власної історії'] = s
        out['_hist'] = (cur, mean3, min5, max3)
    return out


def lens_sum(card, sc):
    base = sum(sc[k] for k in ['PEG', 'Проти S&P 500', 'FCF yield після SBC', 'Ріст проти EPS індексу', 'Проти власної історії'])
    cyc = cyc_cap(card)
    if cyc and sc['PEG'] > 1:
        base -= sc['PEG'] - 1
    return base


def price_check():
    names = ['PEG', 'Проти S&P 500', 'FCF yield після SBC', 'Ріст проти EPS індексу', 'Проти власної історії']
    bad = {k: [] for k in names}
    badsum = []
    n = 0
    for f in sorted(glob.glob(os.path.join(CARDS, '*.json'))):
        card = json.load(open(f, encoding='utf-8'))
        t = card['ticker_file']
        sc = lens_scores(card, t)
        cyc = cyc_cap(card)
        if cyc and sc['PEG'] > 1:
            sc['PEG'] = 1
        hyst = ' | '.join(card['valuation']['hysteresis'])
        n += 1
        for k in names:
            exp = card['valuation']['lenses'][k]['score']
            if sc[k] != exp:
                bad[k].append((t, sc[k], exp, 'HYST' if k.split()[0].lower() in hyst.lower() or {'PEG': 'PEG', 'Проти S&P 500': 'S&P'}.get(k, '#') in hyst else ''))
        s = sum(sc[k] for k in names)
        h = card['header']
        lvl = card['quality']['level_final']
        capv = h.get('market_cap')
        if capv and capv >= 200e9 and h.get('ntm_pe') and h['ntm_pe'] <= 20 and lvl in 'AB':
            s += 1
        exp_s = card['valuation'].get('lens_sum')
        if s != exp_s:
            badsum.append((t, s, exp_s))
    print('--- price lenses (%d cards); mismatches (HYST = card says previous-day state kept) ---' % n)
    for k in names:
        print('%-26s %d  %s' % (k, len(bad[k]), bad[k]))
    print('lens sum (incl. mega-cap +1):', len(badsum), badsum)


if __name__ == '__main__':
    price_check()


# ---------------- x2 arithmetic (appended) ----------------
import datetime as dt

DECAY = {'platform': (0.95, 0.05), 'payments_network': (0.95, 0.05), 'subscription': (0.95, 0.05), 'data_monopoly': (0.95, 0.05),
         'manufacturer': (0.85, 0.04), 'cyclical': (0.85, 0.04), 'commodity': (0.85, 0.04)}
DEFAULT_DECAY = (0.90, 0.04)
DATA_DATE = dt.date(2026, 10, 3)
BUY_BAR = {'A': 14.0, 'other': 15.0}


def _prev_end(e):
    try:
        return dt.date(e.year - 1, e.month, e.day)
    except ValueError:
        return dt.date(e.year - 1, e.month, 28)


def _addyear(D, k):
    try:
        return dt.date(D.year + k, D.month, D.day)
    except ValueError:
        return dt.date(D.year + k, D.month, 28)


def _seg(fy, start, end):
    tot, touched = 0.0, []
    for i, (e, eps, n) in enumerate(fy):
        s = _prev_end(e)
        L = (e - s).days
        ov = (min(end, e) - max(start, s)).days
        if ov <= 0:
            continue
        tot += eps * round(ov / L * 12) / 12
        touched.append(i)
    return tot, touched


def growth_path(card, btype, D=DATA_DATE):
    x = card['x2']
    fy = []
    for r in x['analyst_table']:
        e = r['fiscal_year_end']
        fy.append((dt.date(int(e[6:]), int(e[3:5]), int(e[:2])), r['eps'], r['analysts']))
    decay, lt = DECAY.get(btype, DEFAULT_DECAY)
    if not fy:
        return None
    # extend the FY table by extrapolation when a 12-month segment needs a fiscal year beyond the table (growth of last known FY)
    n_real = len(fy)
    if len(fy) >= 2 and fy[-1][1] > 0 and fy[-2][1] > 0:
        gl = fy[-1][1] / fy[-2][1]
        e = fy[-1][0]
        val = fy[-1][1]
        for _ in range(3):
            try:
                e = dt.date(e.year + 1, e.month, e.day)
            except ValueError:
                e = dt.date(e.year + 1, e.month, 28)
            val *= gl
            fy.append((e, val, 0))
    segs = [_seg(fy, _addyear(D, k - 1), _addyear(D, k)) for k in range(1, 7)]
    last_fy = n_real - 1
    steps, kinds = [], []
    for j in range(1, 6):
        (a, ta), (b, tb) = segs[j - 1], segs[j]
        cons = (b / a - 1) * 100 if a > 0 and b > 0 else None
        idx = set(ta) | set(tb)
        n = min([fy[i][2] for i in idx]) if idx else 0
        touches_far = last_fy in idx
        prev = steps[-1] if steps else None
        if prev is None:
            ours = cons
        else:
            f = 0.75 if prev > 20.0 else decay
            ours = min(25.0, max(lt * 100, prev * f)) if False else min(25.0, prev * f)
        if j == 1 and cons is not None:
            g, kind = cons, 'cons'
        elif cons is not None and not touches_far and n >= 10:
            g, kind = cons, 'cons'
        elif cons is not None and not touches_far and 3 <= n < 10:
            g, kind = min(ours, (ours + cons) / 2), 'avg'
        else:
            g, kind = ours, 'ours'
        steps.append(g)
        kinds.append(kind)
    return steps, kinds


def x2_check():
    mism = []
    n = 0
    for f in sorted(glob.glob(os.path.join(CARDS, '*.json'))):
        card = json.load(open(f, encoding='utf-8'))
        t = card['ticker_file']
        if t == 'TSM':
            continue
        btype = raw(card['quality']['components']['Прогнозованість'], 'тип бізнесу')
        shown = [nz(re.match(r'\d\. ([\d,]+)', g).group(1)) for g in card['x2']['growth_paths'][1]]
        got = growth_path(card, btype)
        n += 1
        errs = [round(a - b, 1) for a, b in zip(got[0], shown)]
        mism.append((t, got[1], errs))
    print('--- x2 growth path: error (calc - shown, pp) per step, kind of each step ---')
    for t, k, e in mism:
        print(t, k, e)


if __name__ == '__main__':
    x2_check()


def x2_full(card, t):
    """Return dict with base/pess/opt multiples, EPS5, price5, CAGR (percent) computed from NTM EPS + growth path + multiple rules."""
    x = card['x2']
    btype = raw(card['quality']['components']['Прогнозованість'], 'тип бізнесу')
    steps, kinds = growth_path(card, btype) if x['analyst_table'] else (None, None)
    if steps is None:  # TSM: no FY table on card -> use displayed base path
        steps = [nz(re.match(r'\d\. ([\d,]+)', g).group(1)) for g in x['growth_paths'][1]]
    e0 = nz(x['eps_today'][1])
    p0 = x['price_today']
    ntm = card['header'].get('ntm_pe')
    st = None
    hl = card['valuation']['lenses']['Проти власної історії']
    if not hl['compare'].startswith('історії немає'):
        mt = re.search(r'trailing P/E ([\d,]+)', hl['value'])
        mm = re.search(r'власне середнє ([\d,]+) за 3 роки', hl['compare'])
        cur, mean3 = nz(mt.group(1)), nz(mm.group(1))
        avg_scaled = mean3 * ntm / cur
    else:
        avg_scaled = None
    base_m = min(ntm, avg_scaled) if avg_scaled else ntm
    pess_m = min(16.0, base_m)
    opt_m = base_m * 1.2 if base_m > SP_PE else SP_PE
    out = {}
    for name, mult, f in (('pess', pess_m, 0.5), ('base', base_m, 1.0), ('opt', opt_m, 1.0)):
        e = e0
        for g in steps:
            e *= 1 + g * f / 100
        price5 = e * mult
        out[name] = {'mult': mult, 'eps5': e, 'price5': price5, 'cagr': ((price5 / p0) ** 0.2 - 1) * 100}
    out['steps'] = steps
    return out


def x2_values_check():
    rows = []
    for f in sorted(glob.glob(os.path.join(CARDS, '*.json'))):
        card = json.load(open(f, encoding='utf-8'))
        t = card['ticker_file']
        r = x2_full(card, t)
        x = card['x2']
        shown_c = [nz(c) for c in x['cagr']]
        shown_m = [nz(m.split(' (')[0]) for m in x['multiple_scenario']]
        rows.append((t, [round(r[k]['cagr'] - s, 1) for k, s in zip(('pess', 'base', 'opt'), shown_c)], [round(r[k]['mult'] - s, 2) for k, s in zip(('pess', 'base', 'opt'), shown_m)]))
    print('--- x2 CAGR error (calc - shown, pp) [pess, base, opt]  and multiple error ---')
    for t, a, b in rows:
        print(t, a, b)
    ok = sum(1 for _, a, _ in rows if all(abs(v) <= 0.3 for v in a))
    print('cards with all three CAGR within 0.3pp:', ok, '/', len(rows))


if __name__ == '__main__':
    x2_values_check()


# ---------------- price word + verdict (appended) ----------------
MATRIX = {
    'A': {'CHEAP': 'BUY', 'FAIR': 'BUY', 'EXPENSIVE_GROWING': 'BUY WAIT', 'EXPENSIVE_NO_GROWTH': 'BUY WAIT', 'VALUE_TRAP': 'AVOID', 'NO_MULTIPLE': 'БРАКУЄ ДАНИХ'},
    'B': {'CHEAP': 'BUY', 'FAIR': 'BUY', 'EXPENSIVE_GROWING': 'BUY WAIT', 'EXPENSIVE_NO_GROWTH': 'BUY WAIT', 'VALUE_TRAP': 'AVOID', 'NO_MULTIPLE': 'БРАКУЄ ДАНИХ'},
    'C': {'CHEAP': 'BUY', 'FAIR': 'BUY WAIT', 'EXPENSIVE_GROWING': 'BUY WAIT', 'EXPENSIVE_NO_GROWTH': 'AVOID', 'VALUE_TRAP': 'AVOID', 'NO_MULTIPLE': 'БРАКУЄ ДАНИХ'},
    'D': {'CHEAP': 'ЛИШЕ СПЕКУЛЯЦІЯ', 'FAIR': 'AVOID', 'EXPENSIVE_GROWING': 'AVOID', 'EXPENSIVE_NO_GROWTH': 'AVOID', 'VALUE_TRAP': 'AVOID', 'NO_MULTIPLE': 'БРАКУЄ ДАНИХ'},
    'E': {'CHEAP': 'AVOID', 'FAIR': 'AVOID', 'EXPENSIVE_GROWING': 'AVOID', 'EXPENSIVE_NO_GROWTH': 'AVOID', 'VALUE_TRAP': 'AVOID', 'NO_MULTIPLE': 'БРАКУЄ ДАНИХ'},
}
WORD_UA = {'Дешева ціна': 'CHEAP', 'Справедлива ціна': 'FAIR', 'Дорого, але росте': 'EXPENSIVE_GROWING', 'Дорого без росту': 'EXPENSIVE_NO_GROWTH', 'Пастка дешевизни': 'VALUE_TRAP'}
STOP_BASKETS_AUTO = {'TSLA'}  # registry basket 'auto' (stop-list) -- basket itself is registry data, not derivable


def price_word(lens_sum_v, ntm_pe, score, eps_g, level, base_cagr, trap=False):
    """trap = card carries the critical price flag 'вартісна пастка' (low multiple but trailing earnings falling; sentence 'Мультиплікатор X низький, але прибутки падають на Y %').
    Multiple >= 30 without >= 30 % EPS growth is always expensive (regime 2026)."""
    if ntm_pe is None:
        return 'NO_MULTIPLE'
    if ntm_pe <= 15 and score < 60 and eps_g is not None and eps_g < 10:
        return 'VALUE_TRAP'
    always_expensive = ntm_pe >= 30 and (eps_g is None or eps_g < 30)
    if not always_expensive:
        if lens_sum_v >= 4:
            return 'CHEAP'
        if lens_sum_v >= 1:
            return 'FAIR'
    need = 14.0 if level == 'A' else 15.0
    if eps_g is not None and eps_g >= need:
        return 'EXPENSIVE_GROWING'
    return 'EXPENSIVE_NO_GROWTH' if base_cagr < need else 'EXPENSIVE_GROWING'


def verdict_check():
    bad, n = [], 0
    for f in sorted(glob.glob(os.path.join(CARDS, '*.json'))):
        card = json.load(open(f, encoding='utf-8'))
        t = card['ticker_file']
        h = card['header']
        level = card['quality']['level_final']
        score = card['quality']['score_final']
        v = card['valuation']
        lensS = v['lens_sum']  # displayed sum (includes hysteresis + regime bonus)
        g = v.get('eps_growth_peg_pct')
        r = x2_full(card, t)
        base_c, bear_c = r['base']['cagr'], r['pess']['cagr']
        word = price_word(lensS, h.get('ntm_pe'), score, g, level, base_c)
        cell = MATRIX[level][word]
        peg = h['ntm_pe'] / g if g and g > 0 else None
        if level == 'A' and peg is not None and peg < 0.5:
            cell = 'BUY'
        qual_crit = any(rr['severity'] == 'критичний' and rr['flag'] not in PRICE_FLAGS for rr in card['flags']['table'])
        verdict = cell
        bar = 14.0 if level == 'A' else 15.0
        if qual_crit and verdict in ('BUY',):
            verdict = 'BUY WAIT' if level in 'ABC' else 'AVOID'
        reviewed = (h.get('taras_review_line') or '').startswith('Тарас переглянув')
        revg = card['quality']['components']['Ріст']['inputs']['ріст виручки на 12 місяців']['value']
        epsg = card['quality']['components']['Ріст']['inputs']['ріст EPS на 12 місяців']['value']
        if verdict == 'BUY' and word == 'CHEAP' and level in 'AB' and reviewed and revg >= 0.10 and epsg >= 0.14 and base_c >= bar and bear_c >= 0 and not qual_crit:
            verdict = 'STRONG BUY'
        if verdict in ('BUY', 'STRONG BUY') and base_c < 10.0:
            verdict = 'BUY WAIT'
        shown = h['verdict_line']
        shadow = None
        if t in STOP_BASKETS_AUTO:
            shadow, verdict = verdict, 'НЕ МІЙ СЕКТОР'
        n += 1
        shown_word = WORD_UA.get(h.get('price_word_chip', ''), '?')
        if verdict != shown or (word != shown_word and shown_word != '?'):
            bad.append((t, 'calc', verdict, word, 'shown', shown, shown_word))
    print('--- verdict + price word (%d cards) mismatches: %d ---' % (n, len(bad)))
    for b in bad:
        print(b)


if __name__ == '__main__':
    verdict_check()


# ---------------- "до наступного вердикту": price route by bisection (appended) ----------------
VERDICT_RANK = {'AVOID': 0, 'BUY WAIT': 1, 'BUY': 2, 'STRONG BUY': 3}


def card_state(card):
    """Collect numeric state needed to re-evaluate the verdict at another price."""
    h = card['header']
    x = card['x2']
    st = {'p0': x['price_today'], 'ntm_pe0': h['ntm_pe'], 'cap0': h.get('market_cap'), 'level': card['quality']['level_final'], 'score': card['quality']['score_final']}
    v = card['valuation']
    st['g'] = v.get('eps_growth_peg_pct')
    L = v['lenses']
    fy = L['FCF yield після SBC']['value']
    st['yield0'] = None if fy.strip() in ('немає', 'н/д') else nz(fy.replace('%', ''))
    hl = L['Проти власної історії']
    if hl['compare'].startswith('історії немає'):
        st['hist'] = None
    else:
        cur = nz(re.search(r'trailing P/E ([\d,]+)', hl['value']).group(1))
        mean3 = nz(re.search(r'власне середнє ([\d,]+) за 3 роки', hl['compare']).group(1))
        rows = trailing_pe_stats(card['ticker_file'])['rows']
        st['hist'] = {'cur0': cur, 'mean3': mean3, 'min5': min(r[2] for r in rows), 'max3': max(r[3] for r in rows[-3:]), 'points': sum(r[4] for r in rows)}
    st['cyc'] = cyc_cap(card)
    st['reviewed'] = (h.get('taras_review_line') or '').startswith('Тарас переглянув')
    st['qual_crit'] = any(rr['severity'] == 'критичний' and rr['flag'] not in PRICE_FLAGS for rr in card['flags']['table'])
    cq = card['quality']['components']['Ріст']['inputs']
    st['revg'] = cq['ріст виручки на 12 місяців']['value']
    st['epsg'] = cq['ріст EPS на 12 місяців']['value']
    return st


def verdict_at(card, st, price, x2cache):
    k = price / st['p0']
    pe = st['ntm_pe0'] * k
    lenses = {}
    g = st['g']
    if g is None or g <= 0:
        peg_s, peg = (-2 if g is not None else 0), None
    else:
        peg = pe / g
        peg_s = 2 if peg < 0.5 else 1 if peg < 1.0 else 0 if peg <= 1.3 else -1 if peg <= 2.0 else -2
    if st['cyc'] and peg_s > 1:
        peg_s = 1
    ratio = pe / SP_PE
    sp_s = (1 if st['level'] in 'AB' else 0) if ratio <= 1.0 else 0 if ratio <= 1.3 else -1 if ratio <= 2.0 else -2
    if st['yield0'] is None:
        y_s = 0
    else:
        y = st['yield0'] / k
        y_s = 2 if y >= 4 else 1 if y >= 3 else 0 if y >= 2 else -1 if y >= 1 else -2
    gm = 0 if g is None else (1 if g >= 1.5 * IDX_G else -1 if g < 0.9 * IDX_G else 0)
    if st['hist'] is None:
        h_s = 0
    else:
        hh = st['hist']
        cur = hh['cur0'] * k
        s = 2 if cur <= hh['min5'] * 1.05 else -2 if cur >= hh['max3'] * 0.95 else 1 if cur < hh['mean3'] * 0.9 else -1 if cur > hh['mean3'] * 1.1 else 0
        if hh['points'] < 36:
            s = max(-1, min(1, s))
        h_s = s
    total = peg_s + sp_s + y_s + gm + h_s
    cap = (st['cap0'] or 0) * k
    if cap >= 200e9 and pe <= 20 and st['level'] in 'AB':
        total += 1
    # base CAGR at this price
    r = x2cache(price, pe)
    word = price_word(total, pe, st['score'], st['epsg'] * 100 if st['epsg'] is not None else None, st['level'], r)
    cell = MATRIX[st['level']][word]
    if st['level'] == 'A' and peg is not None and peg < 0.5:
        cell = 'BUY'
    verdict = cell
    if st['qual_crit'] and verdict == 'BUY':
        verdict = 'BUY WAIT' if st['level'] in 'ABC' else 'AVOID'
    bar = 14.0 if st['level'] == 'A' else 15.0
    if verdict == 'BUY' and word == 'CHEAP' and st['level'] in 'AB' and st['reviewed'] and st['revg'] >= 0.10 and st['epsg'] >= 0.14 and r >= bar and not st['qual_crit']:
        verdict = 'STRONG BUY'
    if verdict in ('BUY', 'STRONG BUY') and r < 10.0:
        verdict = 'BUY WAIT'
    return verdict, word, total, r


def price_route(card):
    t = card['ticker_file']
    st = card_state(card)
    base = x2_full(card, t)
    steps = base['steps']
    e0 = nz(card['x2']['eps_today'][1])
    ntm0 = st['ntm_pe0']
    avg_scaled_factor = None
    hl = card['valuation']['lenses']['Проти власної історії']

    def x2cache(price, pe):
        # base CAGR at a different price: multiple = min(pe, mean3 * pe / cur)
        mult = pe
        if st['hist'] is not None:
            mult = min(pe, st['hist']['mean3'] * pe / (st['hist']['cur0'] * price / st['p0']))
        e = e0
        for g in steps:
            e *= 1 + g / 100
        return ((e * mult / price) ** 0.2 - 1) * 100
    cur_v, _, _, _ = verdict_at(card, st, st['p0'], x2cache)
    out = {'now': cur_v}
    target_rank = VERDICT_RANK.get(cur_v)
    if target_rank is None:
        return out
    # search lower prices for the first verdict with higher rank, bisection on a fine grid
    best = None
    for tgt in sorted({VERDICT_RANK[k] for k in VERDICT_RANK if VERDICT_RANK[k] > target_rank}):
        lo, hi = 0.01 * st['p0'], st['p0']
        ok = None
        # scan downwards for monotone region
        grid = [st['p0'] * (1 - i / 4000) for i in range(0, 3999)]
        for p in grid:
            vv, _, _, _ = verdict_at(card, st, p, x2cache)
            if VERDICT_RANK.get(vv, -1) >= tgt:
                ok = p
                break
        if ok is not None:
            out['price_for_rank_%d' % tgt] = round(ok, 2)
            out['pe_for_rank_%d' % tgt] = round(ok / st['p0'] * ntm0, 2)
    return out


def next_verdict_check():
    print('--- price route (grid search below current price); shown text in brackets ---')
    for f in sorted(glob.glob(os.path.join(CARDS, '*.json'))):
        card = json.load(open(f, encoding='utf-8'))
        t = card['ticker_file']
        if t in ('TSLA', 'TSM', 'NFLX', 'NVDA'):
            continue
        try:
            r = price_route(card)
        except Exception as e:  # noqa
            r = {'ERR': str(e)}
        m = re.search(r'нижче \$([\d  ,]+) \(мультиплікатор NTM P/E ([\d,]+)\)', (card['detailed'].get('needed') or '').replace(chr(160), ' '))
        print(t, r, '[%s]' % (m.group(0) if m else '-'))


if __name__ == '__main__':
    next_verdict_check()
