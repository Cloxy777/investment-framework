# Screen: Taras's portfolio ("Портфель Тараса") — `/portfolio/`

Nav: top-level link. Captured 2026-09-29. Screenshots: `portfolio__top.jpg`, `portfolio__quality-tile-open.jpg`. The author's real portfolio (public within the site) analysed with the same engine. Snapshot of positions dated 16.09.2026 (28 positions).

## Content (top -> bottom)
1. **KPI row 1** (same as start page): earnings growth 12M `+34,7 %` (reported EPS growth weighted by position share) · price 1Y `+17,2 %` · portfolio coverage `97,4 %` (positions with both numbers: 21 of 28). Caption "Statement as of 16.09.2026; card numbers as of the date in the page footer". `<details>` "Що стоїть за числами" lists tickers missing a number and why.
2. **KPI tiles row 2 (5 buttons, each expands an explanation + chart + `таблиця` toggle; hash `#tile=pf-quality` etc.)**:
   - **Якість портфеля** `B 77,1` (coverage 25 of 28): score of each company × its share, sum ÷ share of positions that have a score; positions without card/score are NOT counted as zero — their weight is redistributed and they are named below; portfolio level uses same scale (A ≥80, B ≥70, C ≥55, else D); company-level caps (critical flags, Taras review) are not carried to the portfolio, so the level is by score. Coverage line "25 of 28 positions, 99,1 % of portfolio". Expanded chart "Внесок позицій у бал портфеля" (contribution of each position to portfolio score: GOOG 16,9, AMZN 11,6, NVDA 9,5, MSFT 6,3, ASML 5,4, META 4,5, UBER 3,0, TSM 2,9, V 2,8, AVGO 2,6 …) as horizontal bars with table toggle.
   - **NTM P/E і PEG портфеля** `20,1 · PEG 0,94`.
   - **CAGR на 5 років** `+16,9 % / +21,6 %` (base / optimistic).
   - **Ріст EPS на 5 років** `+17,4 %`.
   - **Ріст виручки на 12 місяців** `+42,6 %`.
   Each with "покрито 25 з 28".
3. **Holdings list** (28 rows sorted by weight): ticker link, name, verdict chip, `level score · price word · частка N %` (same as start page).
4. **Recent trades** timeline + table (`Дата | Тікер | Дія`; actions купівля/докупівля/фіксація частини/продаж) + list of trades with `N шт. по $price` (same as start page section 8).
Inputs: tile buttons, `таблиця` toggles, ticker links. No forms.
Rules: portfolio metrics are position-weighted averages that skip missing values and renormalise weights; coverage reported explicitly.
