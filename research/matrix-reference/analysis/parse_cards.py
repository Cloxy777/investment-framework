#!/usr/bin/env python3
"""Parse data/cards/<T>.simple.txt + .detailed.txt into data/cards/<T>.json (structured) .
Raw text stays next to the JSON so the parse can be redone. Numbers: Ukrainian decimal comma -> float.
Usage: python parse_cards.py [TICKER ...]"""
import glob, json, os, re, sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
CARDS = os.path.join(ROOT, 'data', 'cards')


def num(s):
    """'1 053,98' / '+56,6 %' / '-$1,2 млрд' -> float (units multiplied: тис/млн/млрд/трлн)."""
    if s is None:
        return None
    s = s.replace(' ', ' ').replace(' ', ' ').strip()
    m = re.search(r'([+\-−]?)\s*[$₩€£]?\s*([+\-−]?\d[\d ]*(?:[.,]\d+)?)\s*(трлн|млрд|млн|тис)?', s)
    if not m:
        return None
    sign = -1 if (m.group(1) in '-−' and m.group(1)) or m.group(2).startswith(('-', '−')) else 1
    v = float(m.group(2).lstrip('+-−').replace(' ', '').replace(',', '.'))
    mult = {'трлн': 1e12, 'млрд': 1e9, 'млн': 1e6, 'тис': 1e3}.get(m.group(3), 1)
    return sign * v * mult


def sections(text):
    """split simple.txt into dict: BASE, tiles{id}, FULL"""
    out = {'tiles': {}}
    cur = None
    buf = []
    def flush():
        if cur is None:
            return
        out['tiles' if cur.startswith('TILE:') else cur] = out.get('tiles') if False else None
    parts = re.split(r'^(### [A-Z ()]+.*|=== TILE \w+ ===)\s*$', text, flags=re.M)
    # parts: [pre, hdr1, body1, hdr2, body2 ...]
    for i in range(1, len(parts), 2):
        h, b = parts[i], parts[i + 1]
        m = re.match(r'=== TILE (\w+) ===', h)
        if m:
            out['tiles'][m.group(1)] = b.strip('\n')
        elif h.startswith('### BASE'):
            out['base'] = b.strip('\n')
        elif h.startswith('### FULL'):
            out['full'] = b.strip('\n')
        elif h.startswith('### PRICE PERIOD'):
            out.setdefault('periods', {})[re.search(r'pp-\w+-(\w+)', h).group(1)] = b.strip()
        elif h.startswith('### PRICE CHARTS'):
            out['price_charts'] = b.strip('\n')
    return out


def parse_header(base, detailed_base=''):
    h = {}
    lines = [l for l in base.split('\n')]
    h['name'] = lines[0].strip()
    m = re.search(r'^(\S+) · біржа (.+)$', base, re.M)
    if m:
        h['ticker'], h['exchange'] = m.group(1), m.group(2).strip()
    m = re.search(r'^за день ([+\-−]?[\d,]+) %', base, re.M)
    h['day_change_pct'] = num(m.group(1)) if m else None
    m = re.search(r'^капіталізація (.+)$', base, re.M)
    h['market_cap_short'] = m.group(1) if m else None
    # verdict block: lines after 'капіталізація' up to 'що означає'
    m = re.search(r'капіталізація .+\n(.+?)\n(.+?)\n(.+?)\n(?:.*\n)?що означає', base)
    vb = re.search(r'капіталізація [^\n]*\n(.*?)що означає', base, re.S)
    if vb:
        bl = [x.strip() for x in vb.group(1).split('\n') if x.strip()]
        h['verdict_block'] = bl
        for x in bl:
            if x.startswith('Рівень '):
                h['level'] = x.split()[-1]
        VW = ('STRONG BUY', 'BUY', 'BUY WAIT', 'AVOID', 'ЛИШЕ СПЕКУЛЯЦІЯ', 'НЕ МІЙ СЕКТОР', 'БРАКУЄ ДАНИХ', '·')
        h['shadow_verdict'] = None
        if len(bl) > 2 and bl[1] == '·':
            h['shadow_verdict'] = bl[2]
        mid = [x for x in bl[1:] if x not in VW and not x.startswith('Рівень ') and not x.startswith('сектор') and x != h['shadow_verdict']]
        if mid:
            h['price_word_chip'] = mid[0]
        h['gate0_note'] = next((x for x in bl if x.startswith('сектор')), None)
        if bl:
            h['verdict_line'] = bl[0]
    m = re.search(r'^(Можливий пік циклу[^\n]*)$', base, re.M)
    h['cycle_peak_note'] = m.group(1) if m else None
    h['taras_holds'] = bool(re.search(r'^Тарас тримає цю акцію', base, re.M))
    m = re.search(r'частка в його портфелі ([\d,]+) %', base)
    m = re.search(r'^(Тарас [^\n]*переглян[^\n]*)$', base, re.M)
    h['taras_review_line'] = m.group(1) if m else None
    m = re.search(r'^за рік ([+\-−]?[\d,]+) % · від максимуму 52 тижнів ([+\-−]?[\d,]+) %', base, re.M)
    if m:
        h['year_change_pct'], h['off_52w_high_pct'] = num(m.group(1)), num(m.group(2))
    m = re.search(r'^\$([\d  ,]+)\n[+\-−][\d,]+ % · [+\-−]\$[\d,]+\nза рік\nзакриття (\d\d\.\d\d\.\d{4})', base, re.M)
    if m:
        h['price_usd'], h['price_date'] = num(m.group(1)), m.group(2)
    m = re.search(r'^ціна ₩?([\d  ]+)\s*·\s*у рушії \$([\d,]+)', base, re.M)
    for lab, key in [('Капіталізація', 'market_cap'), ('NTM P/E', 'ntm_pe'), ('Дивіденди', 'dividend_yield_pct'), ('Макс. 52 тиж.', 'high_52w'), ('Мін. 52 тиж.', 'low_52w')]:
        mm = re.search(r'^' + re.escape(lab) + r'\n([^\n]+)$', base, re.M)
        if mm:
            h[key] = num(mm.group(1)) if mm.group(1).strip() not in ('немає', 'н/д') else None
            h[key + '_raw'] = mm.group(1).strip()
    for m in re.finditer(r'^(Ворота 0, коло компетенції|Рівень якості|Десять ознак хорошої компанії|Ред флаги|Оцінка|Зміна оцінки|Арифметика х2|TTM мультиплікатори|Наступний звіт)\n([^\n]+)$', base, re.M):
        h.setdefault('tile_summaries', {})[m.group(1)] = m.group(2).strip()
    m = re.search(r'^Розбір текстом\n(.+)$', base, re.M)
    h['text_analysis'] = m.group(1).strip() if m else None
    m = re.search(r'Поруч у субсекторі: ([^\n]+)', base)
    h['subsector_line'] = m.group(1) if m else None
    m = re.search(r'Повнота даних: ([^\n]+)', base)
    h['completeness_line'] = m.group(1) if m else None
    m = re.search(r'дані станом на (\d\d\.\d\d\.\d{4})', base)
    h['data_as_of'] = m.group(1) if m else None
    m = re.search(r'Повнота даних: [^\n]*?(\d+) % даних', base)
    h['completeness_pct'] = float(m.group(1)) if m else None
    return h


COMP_NAMES = ['Прибутковість', 'Ріст', 'Прогнозованість', 'Моат', 'Маржа', 'Баланс', 'Капітал і SBC', 'Дисципліна']


def parse_level(tile):
    out = {}
    out['headline'] = tile.split('\n')[0]
    m = re.match(r'Рівень якості: (\w) · ([\d,]+) бала', out['headline'])
    if m:
        out['level'], out['score'] = m.group(1), num(m.group(2))
    lines = tile.split('\n')
    # find component blocks
    idx = {}
    for i, l in enumerate(lines):
        if l.strip() in COMP_NAMES and i + 1 < len(lines) and (re.match(r'^[\d,]+ з \d+', lines[i + 1].strip()) or lines[i + 1].strip() == 'виключено') and l.strip() not in idx:
            idx[l.strip()] = i
    order = sorted(idx.items(), key=lambda kv: kv[1])
    comps = {}
    for k, (name, i) in enumerate(order):
        end = order[k + 1][1] if k + 1 < len(order) else next((j for j, l in enumerate(lines) if l.startswith('складові разом')), len(lines))
        blk = lines[i:end]
        m = re.match(r'^([\d,]+) з (\d+)', blk[1].strip())
        if m:
            c = {'points': num(m.group(1)), 'max': float(m.group(2)), 'explain': blk[2].strip() if len(blk) > 2 else ''}
        else:
            c = {'points': None, 'max': None, 'excluded': True, 'explain': ' '.join(x.strip() for x in blk[1:3])}
        inputs = {}
        for l in blk[3:]:
            l = l.strip()
            mm = re.match(r'^(.+?) = (.+?)(?: · (.+))?$', l)
            if mm and not l.startswith(('Пороги', 'ключі', 'теги', 'поле в', 'звідки')):
                raw = mm.group(2).strip()
                try:
                    val = float(raw)
                except ValueError:
                    val = None
                inputs[mm.group(1).strip()] = {'raw': raw, 'value': val, 'source': (mm.group(3) or '').strip()}
            elif l.startswith('Пороги:'):
                c['thresholds_line'] = l[len('Пороги:'):].strip()
            elif l.startswith('ключі порогів у налаштуваннях:'):
                c['threshold_keys'] = [x.strip() for x in l.split(':', 1)[1].split(';')]
            elif l.startswith('поле в наших даних:'):
                c.setdefault('fields', []).append(l.split(':', 1)[1].strip())
            elif l.startswith('теги подання SEC:'):
                c['sec_tags'] = l.split(':', 1)[1].strip()
        c['inputs'] = inputs
        comps[name] = c
    out['components'] = comps
    m = re.search(r'^складові разом ([\d,]+)(?: \(([^)]*)\))?, штраф прапорців ([\d,]+), бал ([\d,]+): рівень (\w) \(межі A (\d+), B (\d+), C (\d+)\)(.*)$', tile, re.M)
    if m:
        out['sum_components'], out['flag_penalty'], out['score_final'], out['level_final'] = num(m.group(1)), num(m.group(3)), num(m.group(4)), m.group(5)
        out['sum_note'] = m.group(2)
        out['level_cut_tail'] = m.group(9).strip()
    m = re.search(r'^Пояснення рівня\n(.+)$', tile, re.M)
    out['explanation'] = m.group(1).strip() if m else None
    m = re.search(r'^Тег і цифри\n(.+?)\nмоат: (.+?)\nпрогнозованість: (.+)$', tile, re.M)
    if m:
        out['tag_numbers'] = {'moat': m.group(2), 'predictability': m.group(3)}
    # level history by year
    yrs = []
    for m in re.finditer(r'^(20\d\d)\t([\d,]+)\t(\w)\t(.*)$', tile, re.M):
        yrs.append({'year': int(m.group(1)), 'score': num(m.group(2)), 'level': m.group(3), 'flags': m.group(4)})
    out['level_by_year'] = yrs
    m = re.search(r'ряд з (\d\d\.\d\d\.\d{4}), накопичується \(днів (\d+)\)', tile)
    out['level_history_days'] = int(m.group(2)) if m else None
    return out


def parse_checklist(tile):
    lines = tile.splitlines()
    head = lines[0]
    items = []
    i = 1
    if i < len(lines) and lines[i].strip() == '✕':  # first X is the close button of the panel
        i += 1
    while i + 1 < len(lines):
        mk = lines[i].strip()
        if mk in ('✓', '✕', '?'):
            items.append({'mark': {'✓': 'pass', '✕': 'fail', '?': 'unknown'}[mk], 'text': lines[i + 1].strip()})
            i += 2
        else:
            i += 1
    m = re.search(r'^Позитивні сигнали: (.+)$', tile, re.M)
    return {'headline': head, 'items': items, 'positive_signals': m.group(1) if m else None}


def parse_flags(tile):
    out = {'headline': tile.split('\n')[0]}
    m = re.search(r'^критичних: (\d+) · серйозних: (\d+) · мінорних: (\d+) · виміряно нижче порога: (\d+)', tile, re.M)
    if m:
        out['counts'] = dict(zip(['critical', 'serious', 'minor', 'below_threshold'], map(int, m.groups())))
    out['sentences'] = [l.strip() for l in tile.split('\n') if re.match(r'^(критичний|серйозний|мінорний): ', l.strip())]
    rows = []
    for m in re.finditer(r'^(.+?)\t(критичний|серйозний|мінорний|)\t(\d*)\t(.*)$', tile, re.M):
        rows.append({'flag': m.group(1).strip(), 'severity': m.group(2), 'points_removed': num(m.group(3)) if m.group(3) else None, 'note': m.group(4).strip()})
    out['table'] = rows
    k = tile.find('Відомі ризики')
    out['known_risks'] = [l.strip() for l in tile[k:].split('\n')[1:] if l.strip()] if k >= 0 else []
    return out


def parse_valuation(tile):
    out = {'headline': tile.split('\n')[0]}
    m = re.match(r'Оцінка: (.+?) · (.+?) ([\d,]+|—) · PEG (.+)$', out['headline'])
    m2 = re.search(r'ріст EPS ([+\-−][\d,]+) % \(для PEG, 24 міс\.\) за консенсусом аналітиків \((\d+) аналітик', tile)
    if m2:
        out['eps_growth_peg_pct'], out['eps_growth_peg_analysts'] = num(m2.group(1)), int(m2.group(2))
    lenses = {}
    for m in re.finditer(r'^(PEG|FCF yield після SBC|Проти S&P 500|Проти власної історії|Ріст проти EPS індексу)\t(.*?)\t(.*?)\t([+\-−]?\d+)$', tile, re.M):
        lenses[m.group(1)] = {'value': m.group(2), 'compare': m.group(3), 'score': int(m.group(4).replace('−', '-'))}
    out['lenses'] = lenses
    m = re.search(r'^Сума лінз\t\t(.+?)\t([+\-−]?\d+)$', tile, re.M)
    if m:
        out['lens_sum_word'], out['lens_sum'] = m.group(1), int(m.group(2).replace('−', '-'))
    out['hysteresis'] = [l.strip() for l in tile.split('\n') if l.startswith('гістерезис')]
    # 5y EPS table
    rows = []
    for m in re.finditer(r'^(.+?)\t\$([\d,]+)\t([+\-−][\d,]+ %)?\t(.*?)\t(\d*)\t(.*?)\t(.*)$', tile, re.M):
        rows.append({'period': m.group(1), 'eps': num(m.group(2)), 'growth': m.group(3), 'source': m.group(4), 'analysts': m.group(5), 'spread': m.group(6), 'consensus_note': m.group(7)})
    out['eps_5y_table'] = rows
    m = re.search(r'^Одне джерело на графіку: (.+)$', tile, re.M)
    out['eps_path_rule'] = m.group(1) if m else None
    m = re.search(r'Щоб з нинішньої ціни заробляти 15 % на рік, EPS має рости на ([\d,]+) % на рік 5 років \(для 10 % на рік, як ринок, на ([\d,]+) %\); аналітики чекають ([\d,]+) %; рушій закладає ([\d,]+) %\. Мультиплікатор через 5 років той самий, що в базовому сценарії \(([\d,]+)\)', tile)
    if m:
        out['implied_growth'] = dict(zip(['need_15', 'need_10', 'consensus', 'engine', 'exit_multiple'], [num(x) for x in m.groups()]))
    # trailing P/E history stats
    m = re.search(r'середнє ([\d,]+)\nмаксимум ([\d,]+)\nмінімум ([\d,]+)\nостаннє ([\d,]+)', tile)
    if m:
        out['trailing_pe_history'] = dict(zip(['mean_all', 'max', 'min', 'last'], [num(x) for x in m.groups()]))
    return out


def parse_returns(tile):
    out = {'headline': tile.split('\n')[0]}
    m = re.search(r'^оптимістично ([+\-−]?[\d,]+) % \(у вердикт не входить\) · песимістично ([+\-−]?[\d,]+) % · показник ([\d,]+) → ([\d,]+)', tile, re.M)
    if m:
        out['optimistic_cagr'], out['pessimistic_cagr'] = num(m.group(1)), num(m.group(2))
    m = re.search(r'^ріст EPS на рік: ([+\-−]?[\d,]+) %', tile, re.M)
    out['engine_growth_per_year'] = num(m.group(1)) if m else None
    # scenario rows
    def row(label_re):
        m = re.search(r'^' + label_re + r'\t([^\t]*)\t([^\t]*)\t([^\t]*)', tile, re.M)
        return [x.strip() for x in m.groups()] if m else None
    out['eps_today'] = row(r'EPS сьогодні \(NTM, рік 1\)')
    out['eps_5y'] = row(r'EPS через 5 р\.')
    out['multiple_today'] = row(r'Мультиплікатор сьогодні')
    out['multiple_scenario'] = row(r'Мультиплікатор у сценарії')
    out['price_5y'] = row(r'Ціна через 5 р\.')
    out['cagr'] = row(r'CAGR')
    out['x2_year'] = row(r'х2 досягається')
    m = re.search(r'^ціна сьогодні \$([\d  ,]+)', tile, re.M)
    out['price_today'] = num(m.group(1)) if m else None
    # growth paths: lines "N. x %" in order within the 'Ріст по роках' cell
    gp = re.search(r'^Ріст по роках\t?\n(.*?)\nкроки рахуються', tile, re.S | re.M)
    paths = []
    if gp:
        cur = []
        for l in gp.group(1).split('\n'):
            l = l.strip()
            if re.match(r'^1\. ', l) and cur:
                paths.append(cur)
                cur = []
            if l and re.match(r'^\d\. ', l):
                cur.append(l)
        if cur:
            paths.append(cur)
    out['growth_paths'] = paths
    m = re.search(r'^нижні межі: BUY від ([\d,]+) %, нижня межа ([\d,]+) %', tile, re.M)
    if m:
        out['bars'] = {'buy_pct': num(m.group(1)), 'hold_pct': num(m.group(2))}
    m = re.search(r'^Що вирішило вердикт: (.+)$', tile, re.M)
    out['what_decided'] = m.group(1) if m else None
    rows = []
    for m in re.finditer(r'^(зараз|ціль [\d,]+ %|нижня межа HOLD [\d,]+ %)\t\$([\d  ,]+)\t([+\-−]?[\d,]+) %\t([+\-−]?[\d,]+) %$', tile, re.M):
        rows.append({'row': m.group(1), 'price': num(m.group(2)), 'base_cagr': num(m.group(3)), 'to_current_pct': num(m.group(4))})
    out['buy_price_table'] = rows
    m = re.search(r'^Щоб мати 15 % на рік у базовому сценарії, ціна має бути не вище \$([\d  ,]+) \(зараз \$([\d  ,]+)\)', tile, re.M)
    if m:
        out['price_for_15'] = num(m.group(1))
    an = []
    for m in re.finditer(r'^(фінансовий рік до (\d\d\.\d\d\.\d{4}))(?: \([^)]*\))?\t\$([\d  ,]+)\t([^\t]*)\t(\d+)$', tile, re.M):
        an.append({'fiscal_year_end': m.group(2), 'eps': num(m.group(3)), 'growth': m.group(4).strip(), 'analysts': int(m.group(5))})
    out['analyst_table'] = an
    m = re.search(r'^Перераховуємо їх у 12-місячні відрізки.*$', tile, re.M)
    out['method_text'] = m.group(0) if m else None
    return out


def parse_ttm(tile):
    out = {'headline': tile.split('\n')[0]}
    for lab, key in [('TTM P/E', 'ttm_pe'), ('TTM P/FCF', 'ttm_pfcf'), ('TTM P/OCF', 'ttm_pocf'), ('FCF за 12 місяців', 'fcf_ttm'), ('OCF за 12 місяців', 'ocf_ttm')]:
        m = re.search(r'^' + re.escape(lab) + r'\t([^\t\n]+)', tile, re.M)
        if m:
            first = m.group(1).split(' · ')[0].strip()
            out[key] = num(first) if not first.startswith('не порах') else None
            out[key + '_raw'] = m.group(1).strip()
    # history stats blocks
    for nm in ['P/E', 'P/FCF', 'P/OCF']:
        m = re.search(r'Історія trailing ' + re.escape(nm) + r', помісячно\nза 5 років, (\d+) точок помісячно, ряд у наших даних лише з (\d\d\.\d\d\.\d{4}):\nсереднє ([\d,]+)\nмаксимум ([\d,]+)\nмінімум ([\d,]+)\nостаннє ([\d,]+)', tile)
        if m:
            out.setdefault('history', {})[nm] = {'points': int(m.group(1)), 'since': m.group(2), 'mean': num(m.group(3)), 'max': num(m.group(4)), 'min': num(m.group(5)), 'last': num(m.group(6))}
        m = re.search(r'Історія trailing ' + re.escape(nm) + r', помісячно\nРік\tСереднє.*?середнє за період\t([\d,]+)\t([\d,]+)\t([\d,]+)\t(\d+)\nмедіана за період\t([\d,]+)\t([\d,]+)\t([\d,]+)', tile, re.S)
        if m:
            out.setdefault('history_table_tail', {})[nm] = {'mean_period_row': [num(x) for x in m.groups()[:3]], 'points': int(m.group(4)), 'median_row': [num(x) for x in m.groups()[4:7]]}
    return out


def parse_change(tile):
    return {'headline': tile.split('\n')[0], 'text': '\n'.join(l for l in tile.split('\n')[1:] if l.strip() and l.strip() != '✕')[:3000]}


def parse_detailed(text):
    out = {}
    for key, pat in [('gate0', r'^Ворота 0, коло компетенції: (.+)$'), ('gate1', r'^Ворота 1, рівень якості: (.+)$'), ('gate2', r'^Ворота 2, ціна: (.+)$'),
                     ('matrix', r'^Матриця рівень x ціна: (.+)$'), ('x2', r'^Арифметика х2: базовий CAGR (.+)$'), ('verdict_why', r'^Вердикт: (.+)$'), ('needed', r'^Що потрібно для кращого вердикту: (.+)$'),
                     ('headline', r'^((?:STRONG BUY|BUY WAIT|BUY|AVOID|ЛИШЕ СПЕКУЛЯЦІЯ|НЕ МІЙ СЕКТОР|БРАКУЄ ДАНИХ)[^\n]*(?:сума лінз|рівень)[^\n]*)$'),
                     ('flags_step', r'^Прапорці: (.+)$'), ('data_step', r'^Повні дані: (.+)$|^Дані: (.+)$')]:
        m = re.search(pat, text, re.M)
        if m:
            out[key] = next(g for g in m.groups() if g)
    m = re.search(r'^позиція: (.+)$', text, re.M)
    out['position_line'] = m.group(0) if m else None
    for lab in ['кіл-лайни', 'При -30', 'структура виручки']:
        m = re.search(r'^(' + re.escape(lab) + r'.*)$', text, re.M)
        out[lab] = m.group(1) if m else None
    sub = re.findall(r'^(?:позиція|[^\n]{2,40}): разом з іншими такими позиціями не більше (\d+) % портфеля$', text, re.M)
    out['subsector_cap'] = sub[0] if sub else None
    return out


def parse_card(t):
    sp = os.path.join(CARDS, t + '.simple.txt')
    dp = os.path.join(CARDS, t + '.detailed.txt')
    norm = lambda x: x.replace(' ', ' ').replace(' ', ' ')
    s = norm(open(sp, encoding='utf-8').read())
    d = norm(open(dp, encoding='utf-8').read()) if os.path.exists(dp) else ''
    sec = sections(s)
    card = {'ticker_file': t, 'captured': re.search(r'captured (\S+)', s).group(1)}
    card['header'] = parse_header(sec.get('base', ''))
    T = sec['tiles']
    if 'gate0' in T:
        card['gate0'] = {'headline': T['gate0'].split('\n')[0], 'text': '\n'.join(T['gate0'].split('\n')[1:6])}
    if 'level' in T:
        card['quality'] = parse_level(T['level'])
    if 'checklist' in T:
        card['ten_signs'] = parse_checklist(T['checklist'])
    if 'flags' in T:
        card['flags'] = parse_flags(T['flags'])
    if 'valuation' in T:
        card['valuation'] = parse_valuation(T['valuation'])
        if card['header'].get('ntm_pe') is None:
            mm = re.search(r'NTM P/E ([\d,]+)', card['valuation']['headline'])
            if mm:
                card['header']['ntm_pe'] = num(mm.group(1))
    if 'change' in T:
        card['valuation_change'] = parse_change(T['change'])
    if 'returns' in T:
        card['x2'] = parse_returns(T['returns'])
    if 'ttm' in T:
        card['ttm'] = parse_ttm(T['ttm'])
    for k in ['next_report', 'fin_revenue', 'fin_segments', 'fin_revenue_forecast', 'fin_eps', 'fin_eps_forecast', 'fin_cashflow', 'ai']:
        if k in T:
            card.setdefault('other_tiles', {})[k] = T[k][:6000]
    for k in ['taras', 'taras_paid']:
        if k in T:
            card['other_tiles'][k] = T[k]
    if 'taras_paid' in T:
        tp = T['taras_paid']
        rows = []
        for m in re.finditer(r'^(\d\d\.\d\d\.\d{4})	(оцінка|відео|теза|ризик|коментар|угода|угоди|[а-яі]+)	([^	]*)	([^	]*)	(.*)$', tp, re.M):
            rows.append({'date': m.group(1), 'kind': m.group(2), 'taras_word': m.group(3), 'engine_then': m.group(4), 'text': m.group(5)})
        trades = [m.group(0) for m in re.finditer(r'^\d\d\.\d\d\.\d{4} (?:add|trim|buy|sell|new|exit) .*$', tp, re.M)]
        card['taras'] = {'trades': trades, 'headline': T['taras'].splitlines()[0] if 'taras' in T else None, 'paid_headline': tp.splitlines()[0], 'timeline': rows}
    card['detailed'] = parse_detailed(d)
    card['periods'] = sec.get('periods', {})
    return card


def main():
    ticks = sys.argv[1:] or sorted({os.path.basename(f)[:-len('.simple.txt')] for f in glob.glob(os.path.join(CARDS, '*.simple.txt'))})
    for t in ticks:
        try:
            c = parse_card(t)
        except Exception as e:
            print('PARSEFAIL', t, e)
            continue
        with open(os.path.join(CARDS, t + '.json'), 'w', encoding='utf-8') as f:
            json.dump(c, f, ensure_ascii=False, indent=1)
        q = c.get('quality', {})
        print(t, q.get('level'), q.get('score'), 'comps', len(q.get('components', {})), 'lenses', len(c.get('valuation', {}).get('lenses', {})), 'x2rows', len(c.get('x2', {}).get('buy_price_table', [])), 'signs', len(c.get('ten_signs', {}).get('items', [])))


if __name__ == '__main__':
    main()
