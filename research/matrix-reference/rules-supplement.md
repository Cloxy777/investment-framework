# Rules supplement — formulas, worked examples, constants, test vectors

Companion to [rules-and-metrics.md](rules-and-metrics.md) (which holds the methodology-page rules). This file adds: (A) details that the first pass compressed, (B) formulas **reverse-checked against real card numbers**, (C) constants scattered over cards/pages, (D) test vectors for replicating the engine, (E) known inconsistencies. Source: site pages captured 2026-09-29 (UI only). Items marked *(inferred)* are my deductions, not site statements.

---
## A. Gate-0 registry detail (full)

### A1. Good baskets (pass gate 0; keys in screener "усі кошики")
| Basket (UA) | Key | Why (site's reasoning, paraphrased) |
|---|---|---|
| Власники інтернету | `internet_cloud` | search, ads, marketplaces, cloud: cloud providers keep dominating |
| Платіжні мережі | `payments_network` | among the best businesses that exist |
| Підписочні сервіси з операційним важелем | `subscription` | streaming, education, music |
| Платформи-агрегатори з мережевим ефектом | `platform` | marketplaces, delivery, travel, mobility |
| Дата, рейтинги, індекси | `data_monopoly` | service monopolies selling "air" (financial data, scoring) |
| AI-інфраструктура з монополією на своєму вузлі | `ai_infrastructure` | chips, chip equipment, optics |
| Софт за підпискою з високою маржею | `software` | enterprise, vertical, cybersecurity, databases |
Neutral basket: `consumer_brand` ("споживчий бренд": not loved, not on stop-list; scored by numbers only). Catch-all `other` ("Інше").

### A2. Stop-list baskets -> verdict НЕ МІЙ СЕКТОР (full analysis still computed; "shadow verdict" shown)
| Basket | Key | Why not | Exception possible when |
|---|---|---|---|
| автовиробники | `auto` | huge capex, margin rarely >10 %, competition prevents holding margin for years | monopoly at its node with margin >25 % |
| авіакомпанії | (part of cyclical/other) | same as above | nothing: capex+competition eat everything |
| банки | `bank` | can't independently judge balance sheet/real risks (insider-only) | none (loan-book quality visible only to insiders) |
| бізнес, повʼязаний з Росією | — | state/political decision can multiply value by zero | none |
| виробництво | `manufacturer` | huge capex, margin rarely >10 %, competition | monopolist with Visa-like margin: Nvidia, Broadcom, ASML, TSMC |
| енергетика і комунальні послуги | `energy_utility` | revenue depends on cycle/spot prices/budgets; huge capex, thin margin | none: "I don't understand price formation in this market" |
| крипто | `crypto` | asset produces no cash flow -> fair price incalculable | none |
| люкс | `luxury` | business model itself limits growth (doubling in 5y unlikely); political risk | if China's revenue share became insignificant and growth stopped hitting the exclusivity philosophy |
| неоклауди | `neocloud` | unit economics not proven profitable; huge capex | stable profit appears and debt stops exceeding revenue |
| нерухомість (REIT) | `reit` | model limits growth | temporary dividend position, never core for 10 years |
| оборонка | `defense` | revenue depends on budgets/political decisions | none while revenue depends on budgets |
| ресторани | `restaurant` | margin can't be held; growth-limited model | none: "after Starbucks I admitted I don't understand this model" |
| ритейл | `retail` | same as restaurants | club/subscription model: Costco, BJ's |
| ставки | `betting` | competition; political risk | none |
| страхування | `insurance` | same as banks | none |
Taras-decided exceptions (analysed as normal despite stop-list): ASML (only EUV company), AVGO (monopoly maker with Visa-like margin), BJ (club subscription, cheaper Costco alternative), COST (club subscription, benchmark of good-but-expensive), HY9H & SSU (memory: speculation only with profit-taking), MA & V (payment network without credit risk), NVDA (monopoly maker, Visa-like margin), TSM (monopoly in leading-edge chips).

### A3. Speculation-only baskets -> ЛИШЕ СПЕКУЛЯЦІЯ (position ≤1 % of portfolio)
| Basket | Key | Why | Exception/plan |
|---|---|---|---|
| cyclical | (cyclical) | — | speculation only |
| Китай | `china` | political decision can zero value | none |
| біотех | `biotech` | one event decides: patent, trials, regulator, court | "a bet, not an investment" |
| збиткова історія | `unprofitable_story` | unit economics unproven | speculative basket 1–3 % until stable profit |
| пам'ять, лише спекуляція | `memory` | revenue driven by cycle/exchange product prices | exchange-priced product: profit-taking per plan required |
| свіже IPO | — | not enough public reporting history | after several quarters of public reports |
| сировина | `commodity` | cycle/spot-driven; no cash flow -> fair price incalculable | speculative with mandatory profit-taking |
| фармацевтика | `pharma` | one event decides + budget/cycle dependence | short position while patent lives and 2–3-year horizon visible |
Extra tag "бізнес незрозумілий" -> AVOID regardless of basket.

### A4. Sub-sector vocabulary (controlled list; count of company cards in our set at capture date)
автомобілі 2 · авіабудування 2 · авіадвигуни 1 · аеротаксі 3 · аналітика даних 1 · аукціони 1 · бази даних 3 · банки 1 · біткоїн-казначейство 1 · важка техніка 1 · вантажні перевезення 1 · вантажівки 1 · вертикальний софт 4 · ветеринарна діагностика 1 · виробництво чіпів 1 · відеозвʼязок 1 · готелі 1 · громадська безпека 1 · доставка 1 · екомерс 4 · електроенергія 6 · залізниця 1 · клауд 4 · клубна підписка 1 · конгломерат 2 · корпоративний софт 4 · космос 2 · креативний софт 2 · кібербезпека 7 · ліки 7 · ліцензування чіпів 2 · медичне страхування 1 · медичні пристрої 3 · мережеве обладнання 1 · мобільність 2 · напої 5 · нафта і газ 5 · нафтосервіс 1 · обладнання для енергетики 1 · обладнання для чіпів 5 · оборона 1 · одяг 2 · оптика 1 · оренда 1 · оренда GPU потужностей 2 · оренда казино 1 · освіта 1 · памʼять 7 · платежі 5 · послуги для бізнесу 1 · пошук 0 · промислова дистрибуція 1 · промислові гази 1 · професійні дані 1 · реклама 5 · ресторани 2 · роботизація складів 1 · розкіш 2 · розрахунок зарплат 2 · роялті на землю 1 · рітейл 2 · рітейл автозапчастин 1 · рітейл краси 1 · скоринг 1 · снеки 2 · софт для проєктування чіпів 2 · споживча електроніка 2 · спостереження за системами 1 · ставки 1 · стримінг 3 · стримінг музики 1 · супутники і спектр 1 · телеком 4 · телемедицина 1 · тревел 2 · фінансовий софт 1 · фінансові дані 2 · фінтех 1 · чіпи 12 · ігри 1 · інфраструктурне будівництво 1.
Use: peer group for comparison ("Поруч у субсекторі: X (n)" on card) and 30 % portfolio cap per sub-sector; no effect on verdict.

---
## B. Formulas verified against live card numbers

### B1. Five-year "x2" arithmetic (card tile `returns`) — VERIFIED on ABNB
Definitions (base scenario, no multiple expansion):
1. `EPS1` = NTM EPS (year 1 already inside NTM). ABNB: $6,02.
2. Growth path `g1..g5` per year: years 1–2 from analyst consensus (`g1` = 12-month growth, `g2` = next-year growth; counts of analysts shown, e.g. (22) and (13)); years 3–5 **decay** from the last consensus step (ABNB base: 18,9 % → 19,8 % → 18,8 % → 17,9 % → 17,0 %; each later step ≈ ×(0,95…) with "no more than 25 % per step" cap; source table marks steps 3–5 as our extrapolation).
3. `EPS5 = EPS1 × Π(1+g_i), i = 1..5`. Check: 6,02 × 1,189 × 1,198 × 1,188 × 1,179 × 1,170 ≈ 14,05 (card $14,03) ✓.
4. Multiple in scenario `M`: pessimistic = fixed settings value **16** ("песимістичний мультиплікатор з наших налаштувань"); base = `min(current multiple, 3-year average)` (ABNB: min(25,9; 21,8) = 21,8); optimistic = return to 3-year average or the settings ceiling (26,2).
5. `Price5 = EPS5 × M`. Check: 14,03 × 21,8 = 305,87 ✓ (card $305,87). Pessimistic 9,36 × 16 = 149,68 ✓. Optimistic 14,01 × 26,2 = 367,04 ✓.
6. `CAGR = (Price5 / Price0)^(1/5) − 1`. Check: (305,87/156,08)^(0,2) − 1 = 14,4 % ✓ ; pessimistic (149,68/156,08) → −0,8 % ✓ ; optimistic 18,7 % ✓.
7. Pessimistic growth = consensus steps for years 1–2 multiplied by **0,50** ("коефіцієнт 0,50 з наших налаштувань"), years 3–5 still decay path (ABNB: 9,5 %, 9,9 %, 9,4 %, 8,9 %, 8,5 %).
8. "х2 досягається" row: year when Price0 doubles (ABNB: not in pessimistic/base within 5y; optimistic "year 3,9").
9. Bars: **BUY CAGR bar 15,0 %** shown on ABNB (methodology says 14 % for level A, 15 % others); lower bound **10,0 %** ("нижня межа HOLD 10 %"); base CAGR <10 % -> BUY WAIT.
10. Chart "За якою ціною буде 15 % на рік" (buy-price curve) — *(inferred)* `BuyPrice(target) = Price5_base / (1+target)^5`; table columns `Ціна купівлі | Ціна | Базовий CAGR | До поточної` (price levels vs resulting CAGR and % distance from current). Exact table rows not captured.

### B2. Five price lenses — worked example (ABNB, sum +1 = "справедлива")
| Lens | Inputs shown | Score | Check |
|---|---|---|---|
| PEG | NTM P/E 25,9 / EPS growth +27,5 % (24 months, 31 analysts) = 0,94 | +1 | <1 ✓ |
| FCF yield after SBC | +3,4 % vs "good yield" threshold 4 % | +1 | ≥3 % ✓ |
| vs S&P 500 | 25,9 vs index forward P/E 20,1 (ratio 1,29) | **−1** | methodology table would give 0 (ratio ≤1,3) — see E1 |
| vs own history | trailing P/E 34,6 vs own 3-year trailing average 29,1 (+19 %) | −1 | above average >10 % ✓; forward history: "6 days of snapshots of 365 needed" so trailing used |
| Growth vs market | EPS +27,5 % vs S&P 500 EPS +13,6 % (2027) = 2,02× | +1 | ≥1,5× ✓ |
NVDA (lens sum **+6**): vs S&P +1 (19,1 vs 20,1) · vs history +2 (trailing 28,8 vs 3y avg 52,3) · PEG 0,34 shown but cycle-peak note caps PEG lens at **+1** · FCF yield 2,2 % -> 0 · growth +1 => 5, plus **+1 mega-cap regime bonus** (cap ≥$200B, multiple ≤20, level A) = 6 *(inferred)*.
ORCL: lens sum 0, "дорого, але росте", level D -> AVOID. MU: "Дешево", NTM P/E 6,7, PEG 0,07 (cycle peak: EPS growth +646 %, PEG capped).
Constants: **good FCF-yield threshold 4 %** (fixed number from Taras's decision; no 10-year-treasury link yet); **index EPS growth fallback 13 %** when no forecast; S&P 500 forward P/E used = 20,1 (capture date); S&P 500 EPS growth used = +13,6 % (2027).

### B3. Quality-score example (ABNB = 71,5 = B; NVDA = 91,0 = A; ORCL D; SOFI D 42,9)
| Component (max) | ABNB | NVDA | GOOG | META |
|---|---|---|---|---|
| Profitability (15) | 9,8 | 15,0 | 15,0 | 15,0 |
| Growth (20) | 13,8 | 17,0 | 17,0 | 14,2 |
| Predictability (15) | 12,0 | 9,0 | n/c | 9,0 (biggest headroom per compare page) |
| Moat (15) | 12,0 | 15,0 | n/c | n/c |
| Margin (10) | 4,0 | 10,0 | n/c | n/c |
| Balance (10) | 10,0 | 10,0 | n/c | n/c |
| Capital & SBC (10) | 5,0 | 10,0 | 4,0 (biggest headroom) | n/c |
| Discipline (5) | 5,0 | 5,0 | n/c | n/c |
| Flag penalty | 0 | 0 | n/c | n/c |
| **Score / Level** | **71,5 / B** | **91,0 / A** | 78,0 / B | 75,2 / B |
(n/c = not captured reliably. The compare page's per-row values for GOOG/META were only partly read; only the values above are trustworthy.) ABNB component sum of rounded parts = 71,6 vs shown 71,5 (sub-scores rounded for display).
Colour rule on component bars: ≥75 % of max green; 40–75 % brown; flag penalty red.

### B4. Verdict path examples
- **ABNB**: level B (71,5) × "справедлива" (sum +1) -> matrix BUY; 0 critical flags (1 serious, 0 penalty); base CAGR 14,4 % (>10 %, <15 % BUY bar) ; not reviewed by Taras -> cap BUY (STRONG BUY impossible anyway: price not cheap). Verdict history: BUY WAIT (19–26.09) -> BUY (29.09) because 5-year growth is now computed from annual consensus in 12-month segments (methodology change -> price word changed from "дорого, але росте" to "справедлива").
- **NVDA**: A × cheap -> BUY cell, upgraded to **STRONG BUY** (A/B, cheap, growth ≥10 %/14 %, Taras reviewed 18.09.2026, base CAGR 20,4 % ≥ bar, no critical flag).
- **ORCL**: level D (lens sum 0 = "дорого, але росте") -> AVOID; "needed for better verdict": score >55 (missing 3,5; biggest headroom: balance 4,0 of 10) and disappearance of critical flags (capex > operating cash, customer concentration 2–3 clients, FCF negative several quarters).
- **SOFI**: stop-list -> НЕ МІЙ СЕКТОР (shadow AVOID), level D 42,9.
- **MU / Samsung**: gate 0 "лише спекуляція" (memory) -> ЛИШЕ СПЕКУЛЯЦІЯ with shadow BUY WAIT; cycle-peak note; Samsung base CAGR −8,2 %.
- **GOOG vs META (compare page)**: GOOG BUY -> STRONG BUY needs score >80 (missing 2,0; capital & SBC 4,0/10) **or** base CAGR >15 % (13,2 %, missing 1,8 %). META BUY WAIT -> BUY when price < $477 (NTM P/E 14,3) **or** EPS growth 12M >80 % **or** score >80 (missing 4,8; predictability 9,0/15).

### B5. "До наступного вердикту" (what must change) — generator logic *(inferred)*
For each verdict the engine lists the *cheapest satisfied alternatives* (OR): (a) price threshold: `price ≤ multiple_needed × EPS` where multiple_needed is the level at which lens sum reaches the next price word (e.g. META $477 ⇔ NTM P/E 14,3); (b) growth threshold (e.g. EPS growth >80 % for "дорого, але росте" -> fair — shows PEG route); (c) quality threshold (score 80 for A / 55 for C) with points missing and the component with most headroom; (d) removal of critical flags; (e) base CAGR bar (15 %). Displayed on Compare, Screener column "До наступного вердикту" and report calendar.

### B6. Valuation-change quadrants ("Зміна оцінки" tile; screener filter)
Two daily-tracked movements — multiple (price/EPS) and consensus EPS — form 4 quadrants: **cheaper while business grows** (multiple ↓, forecasts ↑ — "buying opportunity"), **pricier with the business** (multiple ↑, forecasts ↑), **cheaper because forecasts worsen** (multiple ↓, forecasts ↓), **pricier without reason** (multiple ↑, forecasts flat/↓). Tile value `↑ 5,3 %` = change of multiple over the tracked window. Needs history: consensus revision series requires **63 snapshots** (~1 quarter); if missing: "quadrant not defined" and no substitute series is imported. Trail shown as dated segments (`відрізок | квадрант | з дати | до дати`).

### B7. Drawdown chart guide lines
"−30 %: дія з методології" (action) and "−50 %: готовність з методології" (readiness) lines from the max close within the series (series since 30.09.2021, not all-time). Screener filter "просадка від, %" and Ideas preset "Просадка понад 30 % при рівні A або B". *(Action semantics — e.g. add-buy rules — are referenced but not spelled out on the site pages I read.)*

### B8. Report-date "what to watch" (auto-generated per company)
Kill-lines example (ABNB): revenue growth <10 %; guidance cut on revenue or margins; SBC again >30 % of FCF; second consecutive decline of key KPI (GBV, nights & seats booked). Also lists serious flags the report could make critical (e.g. management options 13 % of revenue but share count didn't grow -> serious not critical) and missing fields (guidance). Dates from FMP earnings calendar; "date confirmed" flag not provided, so may shift.

### B9. Portfolio aggregation (Taras's portfolio and "My portfolio")
- **Weighted metric** = Σ(metric_i × share_i) / Σ(share_i over positions that HAVE the metric). Missing positions are never zero: weight is redistributed and the missing tickers are named ("coverage: 25 of 28 positions, 99,1 % of portfolio"; earnings/price coverage 21 of 28 = 97,4 %).
- Portfolio quality level uses the same scale (A ≥80, B ≥70, C ≥55, else D) **on score only** (caps/flags of single companies aren't carried over). Taras's portfolio: quality B 77,1; NTM P/E 20,1 · PEG 0,94; base/optimistic CAGR +16,9 % / +21,6 %; EPS growth 5y +17,4 %; revenue growth 12M +42,6 %; reported EPS growth 12M +34,7 %; price 1Y +17,2 % (snapshot 16.09.2026, 28 positions).
- Contribution of a position to portfolio score = score_i × share_i (chart "Внесок позицій", e.g. GOOG 16,9 = 78,0 × 21,5 %).
- **Reader limits (advice, not Taras's rules)** shown on "My portfolio": per-position limit **10 %** for A/B (STRONG BUY level A up to 15 %), level C 1–5 %, D 0–1 %, E 0 %; **sub-sector cap 30 %**, baskets have no cap; message "for your position: reduce to the limit" when above. Test: 12 % NVDA -> flagged "above limit 10,0 %".

### B10. Ten signs of a good company (card tile; 10 green/red/unknown dots)
1 revenue growth (ABNB +17 %) · 2 EPS growth (+27,5 % over 24 months) · 3 high margin (net 20 %) · 4 recurring revenue (business type = platform/subscription etc.) · 5 FCF growth (+13 %) · 6 balance without debt (net cash) · 7 capex-light (capex % of revenue; ABNB 0 %) · 8 buybacks without dilution (share count −5 %, buyback 4 %) · 9 no customer concentration (no customer ≥10 % of revenue in 10-K) · 10 capex from own cash (operating cash covers capex). Thresholds per sign are from settings (not printed except concentration 10 %). "Positive signals" sentences are generated for extra facts (growth accelerating by N pts, cheaper than index AND growing faster than index, revenue and margin growing together, beats consensus in 100 % of quarters over 3 years).

### B11. Data completeness / freshness
"Повнота даних: 97 %" = share of **critical fields** present (ABNB 97 %, ORCL 90 %); label "достатні" ≥80 %; <60 % downgrades STRONG BUY to BUY (methodology). Data as-of dates: cards recomputed nightly (footer "next recalculation overnight"); fundamentals as of last SEC report (LTM 30.06.2026); consensus FMP dated per card; index composition dated (S&P 23.09.2026, Nasdaq 19.09.2026); histories accumulate since 14.09.2026 (daily closes) / 19.09.2026 (verdict history).

### B12. Blind spots the engine admits (card section "Чого рушій не бачить")
No news between reports; no lawsuits/antitrust in numbers; management change detection only as 8-K item-5.02 draft (CEO-change field is manual); guidance cuts unreadable on free data; **no cycle phase** (cyclical at peak earnings looks cheapest — hence "possible cycle peak" note when trailing EPS growth >100 %); corporate actions (spin-offs, big issuance, fiscal-year change) only as date + 8-K code; revenue geography only largest-country share from XBRL axis, **country-risk flag from ≥35 % of revenue outside home country** (not applied when largest axis member is a region).

---
## C. Constants and thresholds index (all numbers printed anywhere on the site)
| Constant | Value | Where |
|---|---|---|
| Level cut-offs | A ≥80, B ≥70, C ≥55, D <55 | methodology, charts |
| Flag penalties | critical 8, serious 4, minor 0 | methodology |
| Unknown component value | 40 % of component weight | methodology |
| Hysteresis | level 2 pts; lenses 5 % of threshold | methodology |
| Price lens ranges | each −2…+2; fair ≥ +1; cheap ≥ +4 | methodology/charts |
| Mega-cap regime | market cap ≥ $200B, multiple ≤20, levels A/B: +1; multiple ≥30 without ≥30 % growth = expensive | methodology |
| Multiple ceiling / beyond reason | 30 (lifted if PEG <1) / 60 | methodology |
| Value-trap rule | multiple ≤15 & score <60 & growth <10 % | methodology |
| "Expensive but growing" | EPS growth ≥15 % (level A 14 %) | methodology |
| STRONG BUY growth bar | revenue ≥10 %, EPS ≥14 % (consensus, next 12M); level A same | methodology |
| x2 bars | base CAGR ≥15 % BUY (A: 14 % in methodology text; card showed 15,0 %), <10 % BUY WAIT; pessimistic multiple 16; pessimistic growth factor 0,50; growth decay cap 25 % per step | methodology + card |
| Completeness | STRONG BUY→BUY below 60 %; high-completeness bound 80 % | methodology |
| Debt limits | serious >1,5x EBITDA; critical >3x EBITDA; cap D at >5x with negative FCF | methodology |
| Concentration | serious ≥25 % one customer or ≥33 % top-2; critical ≥40 % | methodology |
| Dividend | serious if >60 % of FCF | flags table |
| SBC | serious/critical SBC eats revenue; level E if ≥100 % of FCF; kill-line 30 % of FCF | methodology + card |
| Position sizing (reader) | A/B 5–10 %, C 1–5 %, D 0–1 %, E 0; STRONG BUY A ≤15 %; sub-sector ≤30 %; spec sleeve ≤1 % (loss-making 1–3 %) | methodology + My portfolio |
| Tax one-off | effective tax differs >10 pts vs prior 12M -> normalise (8-quarter median rate) | methodology |
| OCF vs revenue | OCF may lag revenue growth ≤5 % (non-contract capex exception) | methodology |
| Drawdown lines | −30 % action, −50 % readiness | card chart |
| Watchlist size | 20 tickers | watchlist |
| Consensus revision history | needs 63 snapshots; own-history lens forward needs 365 days | card |
| Code limits | ≤5 login codes/hour/address; code valid 10 min; device remembered 30 days | how-to-enter |

---
## D. Test vectors (for validating a re-implementation; values as of 2026-09-29)
| Ticker | Verdict | Price word | Level·score | NTM P/E | PEG | EPS g NTM | x2 base/opt CAGR | Notes |
|---|---|---|---|---|---|---|---|---|
| NVDA | STRONG BUY | cheap (sum +6) | A · 91,0 | 19,1 | 0,34 | +56,6 % | 20,4 % / 21,7 % | trailing P/E 28,8; 3y avg 52,3; price $228,86; cycle-peak note (EPS +109 %) |
| ABNB | BUY | fair (+1) | B · 71,5 | 25,9 | 0,94 | +36,7 % NTM / +27,5 % (24m) | 14,4 % / 18,7 % (pess −0,8 %) | price $156,08; trailing P/E 34,6; P/OCF 19,2; FCF $4,86B; rev $13,16B; EPS $4,03; 1 serious flag (SBC 13 % of revenue, share count flat) |
| ORCL | AVOID | expensive but growing (0) | D · 51,5 | 15 | — | — | — | price $132,63; −53 % 1y; trailing P/E 21,0 vs 3y 37,6 |
| SOFI | НЕ МІЙ СЕКТОР (AVOID shadow) | fair | D · 42,9 | 20 | — | — | — | price $15,93; stop-list |
| MU | ЛИШЕ СПЕКУЛЯЦІЯ (BUY WAIT shadow) | cheap | B · 76,8 | 6,7 | 0,07 | — | 9,0 % base | EPS growth 12M +646 %, price $1 053,98 |
| 005930.KS | ЛИШЕ СПЕКУЛЯЦІЯ (BUY WAIT shadow) | cheap | A · 81,0 | 4,2 | 0,05 | +80,5 % | −8,2 % / 25,9 % | price ₩272 250 (= $199,75 in engine); memory basket |
| GOOG | BUY | fair | B · 78,0 | n/c | n/c | n/c | 13,2 % base | compare page also showed NTM P/E 20,5, PEG 0,49, EPS +42,3 % (11 analysts) for one of GOOG/META — column ambiguous |
| META | BUY WAIT | expensive but growing | B · 75,2 | n/c | n/c | n/c | 17,4 % base | BUY at price < $477 (NTM P/E 14,3) |
| MA | BUY WAIT | expensive but growing | A · 88,8 | 25,5 | 1,46 | +17,5 % | 14,7 % / 18,9 % | screener |
| ASML | BUY WAIT | expensive but growing | A · 88,0 | 31,4 | 0,6 | +52,1 % | 13,5 % / 17,7 % | screener |
| MSFT | BUY WAIT | expensive but growing | A · 87,0 | 24,6 | 1,25 | +19,7 % | 17,5 % / 21,8 % | |
| NFLX | STRONG BUY | cheap | A · 85,8 | 18,5 | 0,71 | +25,9 % | 18,0 % / 20,1 % | |
| V | BUY WAIT | expensive but growing | A · 85,0 | 24,5 | 1,65 | +14,9 % | 12,3 % / 16,5 % | |
| ADSK | BUY | fair | B · 81,5 | 15,9 | 1,93 | +8,3 % | 12,2 % / 17,5 % | 4,9 % yield; would be STRONG BUY after Taras review |
Universe: 546 cards computed in total; 164 in the tester's set; verdict counts in screener default set: STRONG BUY 2, BUY 10, BUY WAIT 25, AVOID 20, ЛИШЕ СПЕКУЛЯЦІЯ 20, НЕ МІЙ СЕКТОР 27 (=104 shown); BUY zone 16 (12 plotted); outside matrix gate 0: 57; verdict overridden after matrix: 5; index sets: Nasdaq 100 = 101 cards (40 in registry), S&P 500 = 500 (65 in registry; 117 with cards in this build).
Matrix counts on start page (N / reviewed): A: cheap 2/2 · fair 0 · exp+grow 4/4 · exp-no-growth 0 · trap 0; B: 4/0 · 6/3 · 5/1 · 2/1 · 0; C: 0 · 6/2 · 4/2 · 3/0 · 1/0; D: 1/0 · 0 · 2/0 · 1/0 · 1/0; E: all 0.

---
## E. Known inconsistencies / unexplained points (do not assume the site is internally consistent)
1. **S&P lens for ABNB**: ratio 25,9/20,1 = 1,29 (≤1,3 should score 0 per methodology) but card shows −1. Possible causes *(inferred)*: uses the dearer of two multiples (NTM P/E with options vs plain), or a stricter threshold, or rounding of the index P/E. Replication should verify with more cards.
2. **Growth sub-score**: ABNB growth 13,8 does not equal revenue 4,8 + EPS (≥25 % → 7) + FCF 3 (=14,8); consistent with EPS bucket 15–25 % (=6): the single "EPS growth per card" (geometric mean rule) may be <25 % although PEG page shows +27,5 %.
3. **BUY bar for level A**: methodology says 14 %, ABNB (B) shows 15,0 % — consistent; A card bar not directly seen.
4. **Counts**: matrix cell B·fair "6 · переглянуто 3" vs list of 8; screener 104/164; start page 57 outside matrix; footer 546.
5. **Level E vs scores**: E shown for scores 55–59 (RBRK, CRWD, NET) => E triggers (loss-making, SBC ≥100 % FCF, not understood) are wider than the score scale suggests.
6. **Gate 3** referenced but not described; basis switcher recomputes "gates 2 and 3".
7. "х2 досягається у році 3,9" — exact formula (interpolated doubling time) not confirmed; simple ln2/ln(1+CAGR) gives ~4,0 for 18,7 %.
8. Scatter x-axis reaches +8 although lens caps imply ±10 max only with regime bonus; only 12 of 16 BUY-zone names plotted.
