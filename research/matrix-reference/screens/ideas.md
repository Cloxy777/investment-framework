# Screen: Ideas ("Ідеї") — `/ideas/`

Nav: Що нового -> Ідеї. Captured 2026-09-29. Screenshot: `ideas__top.jpg`.

## Purpose
Ready-made screener presets ("добірки"). "The number in each preset is computed by the same filters that open in the screener via the link, so list and number can't diverge."

## Content — 4 preset cards (title link -> screener with filter hash; count "N компаній · first three tickers і далі")
| Preset | Description (paraphrased) | Screener link hash | Count seen |
|---|---|---|---|
| Рівень A за справедливою або дешевою ціною | best companies the market is not overpricing; excludes "not my sector" (Taras's decision 26.09.2026); "speculation only" remains (gate 0: cyclical/exchange-price revenue, position only in speculative basket with profit-taking plan) | `/screener/#level=A&ціна=FAIR,CHEAP&verdict=STRONG_BUY,BUY,BUY_WAIT,AVOID,SPEC_ONLY,NEED_DATA&sort=score&dir=-1` | 7 (005930.KS, ASML, MA …) |
| Дешевшає, а бізнес росте | multiple falling while forecasts rising — worth daily attention | `/screener/#quadrant=cheaper_on_business&sort=score&dir=-1` | 0 |
| Просадка понад 30 % при рівні A або B | good company far from its high: check whether business or just price broke | `/screener/#level=A,B&dd_min=30&sort=score&dir=-1` | 10 (ADBE, ADSK, APP …) |
| Нові BUY за тиждень | companies whose verdict became BUY/STRONG_BUY in the last week | `/screener/#newbuy=1&sort=score&dir=-1` | 0 (count differs from 7 on start page — see open-questions) |
Screener URL hash keys learned: `level`, `ціна` (Cyrillic key; values CHEAP/FAIR/…), `verdict` (comma list), `quadrant`, `dd_min`, `newbuy`, `sort`, `dir` (`-1`/`1`).
Inputs: none (links). Footer with data date + universe count.
