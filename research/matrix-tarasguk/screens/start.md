# Screen: Start page ("З чого почати" / First steps)

- URL: `https://matrix.tarasguk.com/start/` (also `/`; nav item "Перші кроки" -> `/`)
- Captured: 2026-09-29, logged-in session, light theme, desktop width (~1568px viewport, content column ~800px centered)
- Screenshots: `start__top.jpg`, `start__banner-expanded.jpg`, `start__matrix-cell-selected.jpg`, `start__buy-zone-scatter-top.jpg`, `start__buy-zone-list.jpg`, `start__week-and-portfolio-summary.jpg`, `nav__menu-*.jpg`
- Note: on load the page briefly shows "Відкриваємо дані для цієї сторінки…" (loading state: "Opening data for this page…") before sections fill in.

## Purpose
Landing dashboard. Shows where all analysed companies currently sit on the **Quality level (A–E) × Price word (5 columns) matrix**, which companies are in the BUY zone, what changed this week, a summary of the site author's ("Taras") own portfolio and his recent trades, and a pointer to the "how to read a card" and methodology pages.

## Page sections (top to bottom)
1. **Top banner** — see sitemap "Global chrome". Collapsed text + expander "Подробиці про дані і доступ". Expanded content (paraphrased): closed testing; prices, multiples and analyst consensus come from Financial Modeling Prep (Builders plan, display permitted by licence); company filings from SEC EDGAR; index row from FactSet Earnings Insight; a card is computed from one dataset, no source switcher; errors in numbers can be reported via a button on the page (button lives on cards, TBD); **access valid until 06.10.2026** (per-user access end date — plan/trial info); site is in closed testing, data and calculations still being verified.
2. **Header + global search** (see sitemap).
3. **H1 "З чого почати"**.
4. **"Матриця: де зараз компанії"** (Matrix: where companies are now)
   - Intro line: a cell = quality level + price word; click a cell to show companies in it.
   - **Matrix grid 5 rows × 5 columns** ("Матриця рівень x ціна: скільки компаній у клітинці").
     - Rows = quality level **A, B, C, D, E** (top = best).
     - Columns (price words, left->right): **дешево** (cheap) · **справедлива** (fair) · **дорого, але росте** (expensive but growing) · **дорого без росту** (expensive without growth) · **пастка дешевизни** (value trap).
     - Each cell is a `button`. Cell content: verdict label (e.g. `BUY`, `BUY WAIT`, `AVOID`, `STRONG BUY / BUY`, `ЛИШЕ СПЕКУЛЯЦІЯ` = speculation only) + a count line: `"N · переглянуто M"` (N companies in cell, M of them "reviewed"/viewed by Taras) or `"порожньо"` (empty) when N=0.
     - Cell shading: blue, saturation scales with number of companies (denser = more). Empty cells pale.
     - The **verdict label per cell is a fixed mapping of (level, price word)** (see rules-and-metrics.md, "Matrix verdict map"). Observed 2026-09-29:
       | | дешево | справедлива | дорого, але росте | дорого без росту | пастка дешевизни |
       |---|---|---|---|---|---|
       | A | STRONG BUY / BUY | BUY | BUY WAIT | BUY WAIT | AVOID |
       | B | BUY | BUY | BUY WAIT | BUY WAIT | AVOID |
       | C | BUY | BUY WAIT | BUY WAIT | AVOID | AVOID |
       | D | ЛИШЕ СПЕКУЛЯЦІЯ | AVOID | AVOID | AVOID | AVOID |
       | E | AVOID | AVOID | AVOID | AVOID | AVOID |
     - Counts observed (N / reviewed): A-cheap 2/2, A-fair 0, A-exp-grow 4/4, A-exp-nogrow 0, A-trap 0; B-cheap 4/0, B-fair 6/3, B-exp-grow 5/1, B-exp-nogrow 2/1, B-trap 0; C-cheap 0, C-fair 6/2, C-exp-grow 4/2, C-exp-nogrow 3/0, C-trap 1/0; D-cheap 1/0, D-fair 0, D-exp-grow 2/0, D-exp-nogrow 1/0, D-trap 1/0; E all 0.
   - **Two banner rows under the grid** (info, not buttons):
     - "Поза матрицею, ворота 0: 57" — companies outside the matrix: speculation-only, not the author's sector, or outside his circle of competence: sector, cycle or exchange-traded-product-price stopped analysis before the matrix ("gate 0").
     - "Вердикт змінили наступні кроки: 5" — companies whose final verdict differs from what the matrix cell says, because later steps (x2 arithmetic, flags, or data issues) changed the verdict.
   - Footnote: "Лише спекуляція" in cell D·cheap means weak quality at a cheap price, not a sector/gate-0 exclusion.
   - Caption: blue cells = density; the matrix comes from "the engine's matrix" (verdict + number of cards now in it, + how many Taras reviewed; on mobile the two numbers are shown separated by a slash).
   - Collapsible `<details>`: "Подробиці: Матриця рівень x ціна: скільки компаній… розгорнути" — body says "updated with recalculation".
   - **Action: click a cell** -> below the matrix (page scrolls) an in-page result block appears: heading `Рівень B · справедлива ціна: 8 компаній` (level · price word: N companies) and a grid of **company tiles** (4 per row): logo, TICKER (bold), company name, `"B · 81,5 бала"` (level letter · quality score with 1 decimal + Ukrainian plural word "бала/балів") and a verdict chip (BUY green). Then a primary button **"Відкрити в скринері з цими фільтрами"** (opens screener pre-filtered by that level + price word -> `/screener/` with query filters; TBD verify).
     - Observed inconsistency: cell B·fair showed "6 · переглянуто 3" but the list showed 8 companies (ADSK, GOOG, TSM, AVGO, SPGI, TRI, INTU, ABNB) — see open-questions.
     - Tile click -> company card (TBD).
     - Empty-cell click: not yet tested (see PROGRESS).
5. **"Зараз у зоні BUY за рушієм: 16"** (Now in BUY zone per the engine: 16)
   - Explanation: all companies with verdict BUY or STRONG BUY, whether or not in Taras's portfolio. Verdict is computed from numbers; Taras's own opinion is shown separately and does NOT enter the calculation.
   - **Scatter chart "Зона BUY на карті матриці"**: X = sum of price lenses (right = cheaper), ticks -6…+8; Y = quality score 0–100 (ticks 0, 50, 100). Vertical dashed lines: "справедлива ціна від +1" (fair price from +1, orange) and "дешева ціна від +4" (cheap price from +4, green). Horizontal dashed lines: "рівень A від 80", "рівень B від 70", "рівень C від 55". Points = BUY / STRONG BUY companies (green dots) labelled with ticker; click a point -> company card. Caption: "companies on the map: 12" (of 16; 4 not plotted, presumably missing coordinates). Companies plotted: ADBE, ADSK, APP, AVGO, BKNG, GOOG, INTU, NFLX, NVDA, SPGI, TOI.V, TSM.
   - **List rows** (first 5 shown, "top 5"): logo/initials, TICKER (link), name, verdict chip (STRONG BUY / BUY) at right; second line `"A 91,0 · дешева ціна"` and, for BUY, the note "BUY стане STRONG BUY після перегляду Тарасом (STRONG BUY вимагає тегів, підтверджених Тарасом)" (BUY becomes STRONG BUY once Taras reviews; STRONG BUY requires tags confirmed by Taras).
   - Button **"Усі 16 компаній зони BUY у скринері"** -> screener filtered to verdict BUY/STRONG BUY.
6. **"Що змінилось за тиждень"** (What changed this week)
   - Sentence: "Since 22.09.2026, 64 cards changed, 12 today. Entered the BUY zone: ABNB, ADBE, ADSK, INTU, SPGI, TMUS, TOI.V." Tickers are links to cards.
   - Links: "Підсумок тижня" (`/week/`) · "Що змінилось сьогодні" (`/changes/`).
7. **"Портфель Тараса"** (Taras's portfolio) summary
   - 3 KPI tiles: **ріст прибутку компаній за 12 місяців** `+34,7 %` (subtitle: reported EPS growth, weighted by position share) · **ціна за рік** `+17,2 %` (weighted by position share) · **покрито портфеля** `97,4 %` (positions with both numbers: 21 of 28).
   - Caption: "Portfolio statement as of 16.09.2026; card numbers as of the date in the page footer." (footer date = TBD, scroll to bottom).
   - `<details>` "Що стоїть за числами" — lists tickers lacking a number and why (e.g. SKHY no 1-yr price change; RBRK/CRWD/NET no 12-mo EPS growth; DISK, RVI, WISE.L no card).
   - **Holdings list** (28 positions), sorted by share descending. Row: ticker link, name, verdict chip, `"A 91,0 · дешева ціна · частка 10,3 %"` (level score · price word · portfolio weight). Verdict chips seen: STRONG BUY, BUY, BUY WAIT, AVOID, ЛИШЕ СПЕКУЛЯЦІЯ, НЕ МІЙ СЕКТОР (not my sector).
8. **"Останні угоди Тараса"** (Taras's latest trades)
   - Chart "Угоди Тараса на осі часу": timeline, one row per company (14 companies), X = date range 28.10.2025–16.09.2026, green dots = buy/add ("купівля", "докупівля"), red dots = trim/sell ("фіксація частини" = partial profit-taking, "продаж" = sell). Tooltip on point shows date + action.
   - Toggle **"таблиця"** (table view) of the same data: columns `Дата | Тікер | Дія` (60 trades over 14 companies, sorted date desc).
   - Then a list of the 10 latest trades with details: `date TICKER action N шт. по $price` (e.g. "16.09.2026 AVGO докупівля 1 шт. по $336,29") — units "шт." = shares.
9. **"Як читати картку"** (How to read a card) — text block explaining the company card: verdict row at top (what to do, price word, quality level); tiles below each expandable: quality level with scores, ten signs and red flags, price assessment, "x2 arithmetic", and a chart for every number that has a time series. "Детально" (detailed) mode shows the same verdict in eight steps. Links: "Докладно" -> methodology page ("Як рахує рушій: методологія") and screener ("Усі компанії з фільтрами: скринер").
10. **Disclaimer**: "Not financial advice, do your own analysis, especially risk analysis."

## Inputs on this screen
| Control | Type | Values / behavior | Notes |
|---|---|---|---|
| Global search | combobox `type=search` | free text ticker or company name; placeholder "NVDA, Apple, ASML"; `/` hotkey; "Знайти" submit | results/suggestions TBD (screens/search.md) |
| Matrix cell (25) | button | click selects cell, shows company list below + screener CTA | selected-state styling not captured; empty-cell behavior TBD |
| Details expanders (3) | `<details>` | open/close | |
| "таблиця" toggle | button on trades chart | chart <-> table | not yet clicked |
| Theme toggle | button | light <-> dark | |
| Links | ticker links, screener CTAs, week/changes links | navigation | |

## Outputs / states
- Loading: text "Відкриваємо дані для цієї сторінки…".
- Empty cell label: "порожньо".
- Verdict chips colors: STRONG BUY / BUY green; BUY WAIT amber/beige; AVOID (color TBD, capture on screener).
- Numbers: decimal comma, `%` separated by space ("34,7 %"), dates DD.MM.YYYY, prices with `$` and comma decimals.

## Navigation
- In: any page via logo/`Перші кроки`.
- Out: company cards, screener (with filters), `/week/`, `/changes/`, methodology, `/how-to-read/`, portfolio.

## Business rules visible here
See [../rules-and-metrics.md](../rules-and-metrics.md).

## Addendum: theme toggle (dark mode) and load states
- Screenshot `start__dark-theme.jpg`. The header button cycles **three states: system (auto) -> light -> dark -> system**; aria-label shows current state: "Тема: світла. Перемкнути на темну", "Тема: темна. Перемкнути на як у системі". Choice stored in `localStorage.theme` (`light`/`dark`; key absent = follow system); applied as `data-theme` attribute on `<html>`. Dark theme: near-black background, white text, matrix cells in blue tints (denser = brighter blue). I restored the original state (key removed).
- Load state: matrix area shows "Завантажуємо перелік компаній…" before the cells render.
