import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine_replica as E
for t in sys.argv[1:]:
    c = json.load(open(os.path.join(E.CARDS, t + '.json'), encoding='utf-8')); x = c['x2']
    c['_revenue_ltm'] = E.revenue_ltm(t)
    shown = [[E.nz(re.match(r'\d\. ([\-\d,]+)', g).group(1)) for g in p] for p in x['growth_paths']]
    print('##', t, 'basis', c['header'].get('ntm_pe'), 'shown base', shown[1], 'eps0', x['eps_today'][1], 'p0', x['price_today'])
    print('   mult shown', [m.split(' (')[0] for m in x['multiple_scenario']], 'cagr shown', x['cagr'])
    print('   fy', [(r['fiscal_year_end'], r['eps'], r['analysts']) for r in x['analyst_table']])
    try:
        btype = E.raw(c['quality']['components']['Прогнозованість'], 'тип бізнесу')
        st, kd = E.growth_path(c, btype)
        r = E.x2_full(c, t)
        print('   calc steps', [round(v, 1) for v in st], kd, 'mult', {k: round(r[k]['mult'], 1) for k in ('pess', 'base', 'opt')}, 'cagr', {k: round(r[k]['cagr'], 1) for k in ('pess', 'base', 'opt')})
    except Exception as e:
        print('   ERR', e)
