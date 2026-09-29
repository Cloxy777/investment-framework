# Screen: Company card ("картка") — `/t/<TICKER>/`

- Example captured: `/t/ABNB/` (Airbnb) on 2026-09-29. URL patterns: `/t/<TICKER>/`; deep link to a tile via hash `#tile=<id>` (seen ids: `level`, `valuation`, `returns` (= x2 arithmetic), `ttm`, `fin_cashflow`; the hash updates when a tile opens). Non-US tickers carry exchange suffix (e.g. `TOI.V`, `005930.KS`).
- Screenshots: `company-card__top.jpg`, `company-card__tiles-grid.jpg`, `company-card__x2-tile-open.jpg`.
- Load state: text "Відкриваємо картку…" then card appears.

## Purpose
One-page analysis of a company by the engine's rules: verdict + supporting tiles. Not advice. Verdict always computed as "not held".

## Layout (top -> bottom)
1. **Header**: logo, company name (H1), `TICKER · біржа NASDAQ` (exchange).
2. **Verdict row**: big verdict word (BUY green), chip price word ("Справедлива ціна"), chip level ("Рівень B" purple), link **"що означає"** -> `/methodology.html#verdict-BUY` (anchor per verdict).
3. **Action buttons**: `☆ у вочліст` (add to watchlist — writes data; NOT clicked), `порівняти з …` (-> `/compare/#ABNB/`), `зберегти PDF` (export; NOT clicked).
4. **Price strip** (expands charts): `ціна $156,08 · за рік +27 % · від максимуму 52 тижнів -19 %` + "графіки" chip. Expanded shows charts, each with a `таблиця` (table) toggle:
   - **Ціна за 5 років**: period buttons `5 років | рік | YTD | місяць`; line chart (monthly close, USD), 52w high/low markers, current price; table columns `Рік | Початок | Кінець | Мінімум | Максимум`. Source note: FMP close price + as-of date. Period "місяць" has no chart when there are <3 points (daily closes only tracked from snapshots since 14.09.2026).
   - **Історія вердикту рушія**: bar timeline of verdict per day (BUY WAIT brown, BUY green); table `з дати | до дати | вердикт | днів`; series starts 19.09.2026, accumulating (one point per nightly recompute).
   - **Стрічка часу: зміни вердикту і рівня**: dots on change days; table `дата | що змінилось | було | стало` (verdict BUY WAIT -> BUY; price word "дорого, але росте" -> "справедлива").
   - **Ціна проти прибутку**: indexed (100 at 31.05.2022) price vs trailing 12M EPS; table `дата | ціна | EPS за 12 міс. | ціна, індекс | EPS, індекс`; note about one-off tax item (normalised EPS vs reported). Collapsible "Подробиці".
   - **Просадка від максимуму** (drawdown): red area; guide lines "-30 %: action from methodology" and "-50 %: readiness from methodology"; table `Рік | Найглибша просадка | На кінець року`.
5. **"Подробиці вердикту"** (collapsible "+", link "розгорнути"): one-line reason (here: "Taras has not fully reviewed this company"); plus a caption about basis choice ("by default NTM P/E instead of P/NTM FCF: registry basis forbidden or unavailable").
6. **Mode switch**: `Картка: [просто] [детально] методологія(link -> /methodology.html)`. "просто" = tile grid; "детально" = the same verdict as a linear multi-step explanation (line "BUY: справедлива (сума лінз +1), рівень B", then Gate 0 line, Gate 1 components with chart+table, lenses, matrix cell, flags, arithmetic, data, "why this verdict").
7. **Tile grid (3 columns)**: each tile is a button; opening one shows a panel under the grid with ✕ (accordion, one at a time):
   | Tile | Collapsed value (ABNB) | Expanded content |
   |---|---|---|
   | Ворота 0, коло компетенції | проходить | basket + why ("aggregator platforms with network effect: marketplaces, delivery, travel, mobility"), "Compare with: BKNG · comparison page", basket + themes |
   | Рівень якості | B · 71,5 бала | explanation (incl. normalised-EPS tax note), 8 component scores "X з max", sum, flag penalty, thresholds line "A 80, B 70, C 55"; chart bars (green ≥75% of max, brown 40–75%, red = flag penalty) + table `Складова | Балів | Максимум`; cap explained in words |
   | Десять ознак хорошої компанії | 10 зелених, 0 невідомих з 10 (10 dots) | 10 checks with ✓/✗/?: revenue growth (+17 %), EPS growth (+27,5 % over 24m), high margin (net 20 %), recurring revenue (platform), FCF growth (+13 %), balance without debt (net cash), capex-light (capex % revenue), buybacks without dilution (shares −5 %, buyback 4 %), no customer concentration (no customer ≥10 % revenue), capex from own cash; then "positive signals" sentences |
   | Ред флаги | 0 критичних · 1 серйозний | counts (critical/serious/minor/measured-below-threshold), flag sentences with number + threshold, chart "Прапорці: серйозність і вага" + table `прапорець | серйозність | знято балів | що з ним`, "Відомі ризики" block (reference only) |
   | Оцінка | Справедлива · NTM P/E 25,9 · PEG 0,94 | EPS growth used (+27,5 % 24m, 31 analysts); **lens table** `Лінза | Значення | З чим порівнюємо | Бал`: PEG 0,94 (+1) · FCF yield after SBC +3,4 % vs good-yield threshold 4 % (+1) · vs S&P 500: NTM P/E 25,9 vs index 20,1 (−1) · vs own history: trailing P/E 34,6 vs 3y avg 29,1 (−1; "forward history accumulating: 6 days of snapshots of 365 needed") · growth vs index EPS (+1); sum +1 = fair; chart "Лінзи ціни: від −2 до +2" |
   | Зміна оцінки | ↑ 5,3 % | 4-quadrant explanation: cheaper while business grows (buying opportunity) · pricier with the business · cheaper because forecasts worsen · pricier without reason; "Слід у квадранті" table `відрізок | квадрант | з дати | до дати`; consensus-revision series flagged "accumulating (2 of 63 snapshots needed)" |
   | Арифметика х2 | CAGR 14,4 % базовий сценарій, 5 років, з річних прогнозів аналітиків | 3-scenario table Песимістичний/Базовий/Оптимістичний: EPS today (NTM, year 1) · growth per year (analyst consensus for yrs 1–2, pessimistic ×0,50, then decayed) · EPS in 5y · multiple today · multiple in scenario (pessimistic = settings value 16; base = min(current, 3y avg) 21,8; optimistic = return to mean/ceiling 26,2) · price in 5y · CAGR (−0,8 / 14,4 / 18,7 %) · "х2 reached": no / no / in year 3,9; bounds "BUY from 15,0 %, lower bound 10,0 %"; sentence "what decided the verdict"; chart "За якою ціною буде 15 % на рік" (buy price vs 5y CAGR; target 15 %, HOLD floor 10 %) |
   | TTM мультиплікатори | P/E 34,6 · P/OCF 19,2 | TTM P/E, TTM P/FCF ("not computed: non-positive or missing report"), P/OCF, FCF 12M, OCF 12M with source (SEC EDGAR sum of 4 quarters; FMP daily closes); chart "Історія trailing P/E, помісячно" with period buttons and stats (mean, max, min, last, 3y mean) |
   | Наступний звіт | 05.11.2026 | date from FMP earnings calendar (may shift); consensus source/date; **"what to watch in the report (from engine decision)"**: kill-lines (revenue growth <10 %, guidance cut, SBC >30 % FCF again, second consecutive drop of key KPI), serious flags the report could turn critical, missing fields |
   | AI аналітика · платно (🔒) | "stress-test of thesis, moat, why price moves" | **paid feature**, locked on this plan — not opened |
8. **"Розбір текстом"** (collapsible auto-generated paragraph): price, market cap, 1y change, % below 52w high, NTM P/E, trailing P/E vs 3y avg, "forward history accumulating".
9. **"Розбір фінансових показників"** ("history by years and LTM, only from reports and consensus"): tiles Виручка ($13,16 млрд) · Структура виручки (segments % of revenue/operating profit, 10-K year) · Прогноз виручки (NTM +17,0 % (32 analysts)) · EPS ($4,03) · Прогноз EPS (NTM +36,7 %) · FCF і OCF (FCF $4,86 млрд). Opening one shows bar chart by fiscal year + LTM (blue = FY, green = LTM, grey dashed trend), growth % per bar, `таблиця` toggle (`Період | Значення | Ріст`), source note (SEC EDGAR "N items", last report date) and gap notes ("no OCF/FCF forecast in the source: cash-flow consensus will appear with a paid provider").
10. **"Детальні фінанси"** — quarters and years from reports, chart or table (not opened yet).
11. **Footer strip**: "data as of 28.09.2026", "Neighbours in sub-sector: тревел (1)", "Data completeness: sufficient, 97 % of data", disclaimer with "% of critical fields".

## Inputs on this screen
Mode switch (просто/детально), tile buttons (accordion), chart period selectors (`5 років, рік, YTD, місяць`), `таблиця` toggles, expanders (`розгорнути`), ✕ close, links (compare, methodology anchors, sub-sector), and side-effect buttons `у вочліст` and `зберегти PDF` (not exercised). No free-text forms; no validation messages seen.

## Outputs / states
- Verdict chips: STRONG BUY / BUY (green), BUY WAIT (amber/brown), AVOID, ЛИШЕ СПЕКУЛЯЦІЯ, НЕ МІЙ СЕКТОР, БРАКУЄ ДАНИХ.
- Gap handling: "немає", "не порахований: …", "накопичується" (series accumulating from date X, N of M snapshots needed), "(немає даних)".
- As-of dates and source (FMP / SEC EDGAR) beside every number.
- Formats: decimal comma; `$13,16 млрд`; `млн`; `%` with space.

## Replication notes
Card = deterministic function of (a) registry fields set by Taras (basket, tags, reviewed flag), (b) FMP fundamentals + consensus + prices, (c) SEC EDGAR statements. History series (verdict, lens, consensus revisions) accumulate from nightly snapshots (started 14–19.09.2026).

---
# Addendum: card variants and extra sections (captured 2026-09-29 on NVDA, SOFI, ORCL)
Screenshots: `company-card__nvda-strong-buy-detailed.jpg`, `company-card__sofi-not-my-sector.jpg`, `company-card__orcl-avoid.jpg`.

## Mode preference is remembered
The "просто / детально" switch persists across cards (browser storage): after choosing "детально" once, other cards opened in detailed mode. In **detailed mode the 3-column tile grid is replaced by a linear list of steps**.

## Detailed mode (NVDA example; "STRONG BUY: дешево (сума лінз +6), рівень A" headline)
Steps (each is a sentence + expandable chart/table):
1. **Ворота 0** — "passes · AI infrastructure with node monopoly: chips, chip equipment, optics" (basket + subcategory).
2. **Ворота 1, рівень якості** — all 8 components in one line ("profitability 15,0 of 15; growth 17,0 of 20; predictability 9,0 of 15; moat 15,0 of 15; margin 10,0 of 10; balance 10,0 of 10; capital & SBC 10,0 of 10; discipline 5,0 of 5. Components total 91,0, flag penalty 0, score 91,0, level A") + components chart/table.
3. **Ворота 2, ціна** — basis multiple and EPS growth, then each lens with score (vs S&P 500: 19,1 vs index 20,1 (+1); vs own history: trailing 28,8 vs 3y avg 52,3 (+2); PEG 0,34 …); lens sum (+6).
4. **Матриця рівень x ціна** — "cell A × cheap gives BUY. Final engine verdict STRONG BUY: decided by cheap price for a good company".
5. **Прапорці** (critical/serious/minor).
6. **Арифметика х2** — base / optimistic / pessimistic CAGR (20,4 % / 21,7 % / 6,5 %), 3-scenario table with price in 5 years ($313,46 / $578,80 / $611,16) and a **"buy price" table** `Ціна купівлі | Ціна | Базовий CAGR | До поточної` (what price gives what CAGR).
7. Data completeness and 8. "why exactly this verdict" sentence.

## Extra header lines seen on cards (conditional elements)
- **Cycle-peak note** (NVDA): "Possible cycle peak: EPS growth 12M +109 %; not a flag in the verdict, PEG lens capped at +1" (bold line under verdict).
- **"Тарас тримає цю акцію · частка в його портфелі 10,3 % на 16.09.2026"** — shown when the company is in Taras's portfolio.
- **"Тарас переглянув 18.09.2026"** (or "Тарас цю компанію не переглядав повністю") inside "Подробиці вердикту".
- **Basis caption** (why NTM P/E: "forward multiple exists only for it; P/OCF, P/FCF in the free source are trailing only").
- **Stop-list card (SOFI)**: verdict word is **НЕ МІЙ СЕКТОР** with grey "shadow verdict" `· AVOID` next to it, price-word chip and level chip still shown (Справедлива ціна · Рівень D) and note "sector in the stop-list beyond gate 0". Headline: "НЕ МІЙ СЕКТОР: not mine beyond gate 0, level D". Full analysis still available.
- **AVOID card (ORCL)**: red AVOID, "Дорого, але росте" chip, level D; headline "AVOID: expensive but growing (lens sum 0), level D".
- Non-US listing e.g. `ORCL · біржа NYSE`.

## Extra sections at the bottom of a card (below "Детальні фінанси")
- **"Чого рушій не бачить"** (What the engine does not see) — collapsible list of honest blind spots: news between reports not read; lawsuits/antitrust not in numbers; management changes not detected (8-K items listed only as a draft; CEO-change field is filled by Taras manually); guidance cuts not readable on free data; no cycle-phase (cyclical at peak earnings looks cheapest); corporate actions (spin-offs, big issuance, fiscal-year change) shown only as date + 8-K item code; revenue geography seen only as largest-country share from XBRL axis (no currency dependence).
- **"Географія виручки"** (Revenue geography) — e.g. `Americas (region): 66,0 % of revenue`, country-risk flag threshold "≥35,0 % of revenue outside home country", note that the largest axis member is a region so share isn't fed to engine; other members EMEA 22,7 %, Asia Pacific 11,3 %; source = SEC EDGAR XBRL geography axis, 10-K, filing id and period.
- **"Події з подань SEC"** (Events from SEC filings) — 8-K count by item code for 12 months (e.g. "12 8-K filings: 1.01 ×2, 2.02 ×4, …"), "possible management change — draft for Taras's review" list of dated 5.02 filings (each with link "подання"), "Корпоративні дії" list. Explains that an item code says what happened by form, not by content.
- Footer strip: "Поруч у субсекторі: клауд (3)" (peer count by sub-sector), "Повнота даних: достатні, 90 % даних".

## Detailed-mode steps 7–8 and "Детальні фінанси" tile (ORCL; screenshot `company-card__detailed-finance-quarters.jpg`)
- **Step 7 "Повна дані"** — data completeness (e.g. "90 % of critical fields; missing: share of SBC in free cash flow (on OCF basis, in revenue); guidance direction").
- **Step 8 "Вердикт"** — "Why exactly this verdict": e.g. "AVOID: expensive but growing (lens sum 0), level D; engine reasons: expensive but growing: can buy if it dips; verdict by methodology; Taras did not review" + **"What is needed for a better verdict"**: e.g. "at quality score above 55 (missing 3,5 pts; biggest headroom: Balance component, 4,0 of 10); when critical flag disappears (capex above operating cash, customer concentration in 2–3 clients, FCF negative several quarters in a row)". (Same idea as the "До наступного вердикту" row in Compare/Screener.)
- **"Детальні фінанси" tile** (collapsed by default; "quarters and years from reports, chart or table"): sub-section "По кварталах" — combined chart (blue bars revenue, green bars operating profit, olive bars net profit; lines for operating margin and net margin, last-value labels) + `таблиця` toggle; table columns `Квартал | виручка | операційний прибуток | чистий прибуток | операційна маржа | чиста маржа` (quarter end date DD.MM.YYYY; amounts `$19,3 млрд`; margins in %). Probably also an annual sub-section (not scrolled).

---
# Addendum 2 (2026-09-29, second session): financial-breakdown tiles, price-chart periods, more variants
Screenshots: `company-card__mu-spec-only.jpg`, `company-card__samsung-non-us.jpg`.

## "Розбір фінансових показників" tiles (ABNB) — deep links `#tile=fin_revenue`, `fin_revenue_forecast`, `fin_eps_forecast`, `fin_cashflow`, …
| Tile | Panel content |
|---|---|
| **Виручка** ($13,16 млрд) | bar chart "Виручка за роками і LTM": FY2021–FY2025 (blue) + LTM (green, `LTM 30.06.2026`), growth % over each bar (+40 %, +18 %, +12 %, +10 %, +7 %), dashed trend; `таблиця` toggle `Період | Значення | Ріст` (2021 $6,0 млрд / немає; 2022 $8,4 млрд +40,2 %; … LTM $13,2 млрд +7,5 %); wide table `період / значення / ріст до попереднього`; source "SEC EDGAR, company reports (14 items); last report 30.06.2026" |
| **Структура виручки** (segments 100 %/100 % op. profit, 10-K 2025) | one-line comparison with 3 years ago ("Reportable Segment gives 100 % of revenue and 100 % of operating profit; 3 years ago 100 % and 100 %"); chart "Сегменти і географія частками" with `таблиця` (`вісь | рядок розкриття | частка виручки`): axis `сегменти` (Reportable Segment 100,0 %) and `географія` (Non-US 60,7 %, North America 42,4 %, US 39,3 %, EMEA 38,6 %, Latin America 9,5 %, Asia Pacific 9,4 % — overlapping members of different geography axes, not additive) |
| **Прогноз виручки** (NTM +17,0 % (32 аналітики)) | two-bar chart LTM (green) vs NTM (grey, consensus forecast) with values ($13,2 → $15,4 млрд, +17,0 %); table; details expander "Подробиці: Прогноз виручки" ; note that NTM = next 12 months per consensus growth from the source (32 analysts) |
| **EPS** ($4,03) | bars by fiscal year 2021–2025 (−$0,57, $2,78, $7,24, $4,11, $4,03) with growth (+160 %, −43 %, −2 %); table; note: annual EPS is *our calculation* = net income / diluted weighted-average shares, both from SEC XBRL; "LTM EPS as a separate number is not on the card: added in the data layer" (gap stated in words) |
| **Прогноз EPS** (NTM +36,7 %) | table `період | ріст EPS за консенсусом`: NTM +36,7 %; next year +17,5 %; in two years +19,4 %; note "only consensus growth rates from the source; absolute EPS estimates by fiscal year with analyst count and consensus date are not provided by the source, so not shown and not reconstructed" |
| **FCF і OCF** | (see main section) two charts + tables OCF/FCF by years + LTM, with `тренд` |
- **"Розбір текстом"** expands to a numbered auto-written analysis: (1) price, market cap, 1y change, % below 52w high, multiples; (2) ten-signs summary ("passes all criteria of a good company: revenue growth (+17 %); …; SBC eats 35 % of FCF; green signs 10 of 10, level B"); (3) key negative/risk sentence (e.g. management options 13,0 % of revenue but share count didn't grow, so serious not critical); continues with further numbered points (truncated in capture).

## Price chart periods (open by clicking the "ціна … графіки" strip first)
Buttons `5 років | рік | YTD | місяць`. `рік` -> monthly points since 30.09.2025 (table rows 2025, 2026); `YTD` -> since 31.01.2026 (table shows 2026 only) with caption "series from DD.MM.YYYY, shorter than 5 years"; **`місяць` button is present but the period has no chart** — caption "Periods without a chart: month (in our data price is monthly; only 2 points in this period; daily closes are kept from snapshots since 14.09.2026)". Charts/tables of verdict history, timeline, price-vs-EPS and drawdown sit below in the same block.

## More header variants
- **Speculation-only with shadow verdict (MU, 005930.KS)**: big brown `ЛИШЕ СПЕКУЛЯЦІЯ` + `· BUY WAIT` (shadow verdict), chips `Дешева ціна`, `Рівень B/A`, text "сектор поза колом за воротами 0". Tile "Ворота 0" collapsed value: "лише спекуляція". Bold cycle-peak line with cause: "Possible cycle peak: EPS growth 12M +646 %, cause: memory price rise; not a flag in the verdict, PEG lens capped at +1". Ten signs may include red (fail) and grey (unknown) dots (e.g. "6 зелених, 1 невідома з 10"). x2 CAGR can be low/negative (MU 9,0 %; Samsung −8,2 %) even at "cheap".
- **Non-US listing (005930.KS, exchange KRX)**: no logo; price strip shows local currency and engine USD: `ціна ₩272 250 · у рушії $199,75 · за рік +222 % · від максимуму 52 тижнів −28 %` ("у рушії" = the USD-converted price the engine uses). Header line "Тарас тримає цю акцію · частка … на 16.09.2026", "Тарас переглянув 19.09.2026".
- **Screener empty result state** (e.g. `#verdict=NEED_DATA` -> 0 companies today): table headers stay, message "У таблиці 0 з 164 компаній за фільтрами. Вердикт рахується з цифр, оцінка Тараса в розрахунок не входить." (БРАКУЄ ДАНИХ card therefore not currently observable.)

## Addendum 3: "Відомі ризики" (Known risks) block inside the Red-flags tile (ABNB)
Under the flags table, heading **"Відомі ризики · довідка, у вердикт не входить"** (reference only, not in verdict) with three kinds of lines: (a) **measured-below-threshold items with number and threshold**, e.g. "external capex financing over 12 months (no data): capex below threshold 25 % (debt $0,0 млрд, issuance $0,0 млрд)"; (b) **data gaps in words**, e.g. "the 10-K for 31.12.2025 has no disclosure of a customer ≥10 % of revenue"; (c) **"типові ризики сектора за методологією"** — basket-typical risks (e.g. platform fee pressure from regulator or sellers; a competitor with cheap money can dump prices for years). The "Подробиці вердикту → розгорнути" link toggles an inline reason panel (no visible expansion in my capture beyond the one-line reason — see open-questions).
