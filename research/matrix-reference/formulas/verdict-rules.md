# Verdict pipeline — recovered rules

Reference code: `engine_replica.py::verdict_check` (20/20 verdicts and price words reproduced from displayed levels, lens sums, EPS growth, x2 CAGRs). Methodology text: `methodology-rules.json`.

## Order of evaluation — Exact on 20 cards
1. **Gate 0** (registry basket, not derivable): stop-list basket -> verdict `НЕ МІЙ СЕКТОР` with grey **shadow verdict** printed (`НЕ МІЙ СЕКТОР · AVOID` for TSLA, basket `auto`; `Taras exceptions` list lets ASML/AVGO/COST/MA/NVDA/TSM/V through). Speculation baskets -> `ЛИШЕ СПЕКУЛЯЦІЯ` (none in free set). Tag "business not understood" -> AVOID.
2. Level (quality.md) and price word (price-lenses.md).
3. Matrix cell `MATRIX[level][word]`:
   | | CHEAP | FAIR | EXP. GROWING | EXP. NO GROWTH | VALUE TRAP | NO MULTIPLE |
   |---|---|---|---|---|---|---|
   | A | BUY | BUY | BUY WAIT | BUY WAIT | AVOID | БРАКУЄ ДАНИХ |
   | B | BUY | BUY | BUY WAIT | BUY WAIT | AVOID | БРАКУЄ ДАНИХ |
   | C | BUY | BUY WAIT | BUY WAIT | AVOID | AVOID | БРАКУЄ ДАНИХ |
   | D | ЛИШЕ СПЕКУЛЯЦІЯ | AVOID | AVOID | AVOID | AVOID | БРАКУЄ ДАНИХ |
   | E | AVOID | AVOID | AVOID | AVOID | AVOID | БРАКУЄ ДАНИХ |
   Special cell: level A and PEG < 0.5 -> BUY regardless of word/sum (never STRONG BUY).
4. Post-matrix adjustments (order as implemented, all consistent with data):
   - quality-critical flag (not price flags) and verdict BUY -> BUY WAIT for A/B/C else AVOID.
   - **STRONG BUY** only if cell == BUY **and** word == CHEAP **and** level in {A,B} **and** reviewed by Taras **and** revenue growth NTM >= 10 % **and** EPS growth NTM >= 14 % **and** base CAGR >= bar (14 % level A / 15 % others) **and** bear (pessimistic) CAGR >= 0 **and** no quality-critical flag. (NFLX, NVDA pass; ADBE would need Taras's review -> stays BUY; MA/AVGO/TSM/GOOG are FAIR -> BUY.)
   - base CAGR < 10 % and verdict in {BUY, STRONG BUY} -> BUY WAIT. (Completeness < 60 % downgrades STRONG BUY to BUY: not observable; min completeness in sample 81 %.)
   - Stop-list basket: final verdict replaced by НЕ МІЙ СЕКТОР, computed verdict kept as shadow.
5. Display: chip line "Вердикт · Слово ціни · Рівень X"; headline sentence in detailed mode: `"<VERDICT>: <word> (сума лінз <s>), рівень <L>"`; reasons sentence "причини рушія: …"; "вердикт рушія за методологією, Тарас цю компанію не переглядав".
- Level shown on the verdict is the capped level (ADBE score 81.0 -> level B because unreviewed).

## Verified per-card paths (all 20 match)
NVDA A·CHEAP(+6) -> BUY -> STRONG BUY | NFLX A·CHEAP(+6) -> STRONG BUY | MA A·FAIR BUY | MSFT A·EXP.GROWING(-1) BUY WAIT | V A·EXP.GROWING(-1) BUY WAIT | ADBE B(cap)·CHEAP(+5) BUY | GOOG/ABNB/AVGO/TSM B·FAIR BUY | META/PLTR B·EXP.GROWING BUY WAIT | AAPL B·EXP.NO GROWTH(-5) BUY WAIT | AMD/AMZN/UBER C·… BUY WAIT | COST/CRM C·EXP.NO GROWTH AVOID | ORCL D·EXP.GROWING AVOID | TSLA D -> НЕ МІЙ СЕКТОР (shadow AVOID).

## Position sizing / reviewed-state lines (display only)
Detailed card prints `позиція: від a % до b % портфеля` by level (A 5-15 for STRONG BUY A, 5-10 B ...), `<sub-sector>: разом з іншими такими позиціями не більше 30 % портфеля`, kill-lines (Taras field), "При -30 % без зміни бізнесу: додаю до ліміту позиції…" (Taras's rule text). These are registry texts, not computed.

## Not observable on free tier
БРАКУЄ ДАНИХ, ЛИШЕ СПЕКУЛЯЦІЯ (spec baskets), level E, broken-thesis rule, hysteresis on level, completeness downgrade.

---
# UPDATE 2026-10-03 (paid tier, 487 cards): extra post-matrix rules, final status
Rule layer evaluated on displayed inputs (lens sum, EPS growth, level, CAGRs): **verdict 464/467 headline-or-shadow words reproduced** (`run_all_cards.py`; the 3 misses: VICI shadow, DVA and FOUR have no parsed shadow), **price word 454/467**. Additions to the order of evaluation:
1. **Several quality-critical flags** (>= 2 distinct events; "same event" rows do not count): verdict **AVOID** whatever the matrix says; card text "спрацювало кілька критичних прапорців (...): бізнес не фінансує себе сам" (NOW C, GPN D, PANW D).
2. **Thesis flags** (flag `виручка росте, а прибутки і маржа ні` = revenue up while margin and EPS fall; guidance cut is a second source but not live): single flag + **NTM revenue growth >= 10 %** -> "теза під питанням: не купую до звіту, який спростує ризики": BUY -> BUY WAIT for levels A/B/C (AVOID for D/E) (AJG, CMG, MELI, PKG, TSLA); single flag + **NTM revenue growth < 10 %** -> "теза зламана: guidance або прогнози знижено, а росту немає" -> **AVOID** even for level C (CL 4.2 %, MET 5.7 %, MO -5.4 %, MRSH 6.1 % revenue growth). The methodology page says broken thesis -> BUY WAIT for A/B/C; the data say AVOID (threshold 10 % on NTM revenue growth).
3. **What decided** texts (x2 tile "Що вирішило вердикт"): `ворота 0; <reason>` for stop-list/speculation baskets; `thesis; теза під питанням ...`; `thesis; теза зламана ...`; `thesis; спрацювало кілька критичних прапорців (...)`; `клітинка матриці; справедлива ціна за хорошу компанію; ...`; "вердикт рушія за методологією, Тарас цю компанію не переглядав" (or the AI-classification variant "класифікація ШІ").
4. **Gate 0 outcomes in the full set** (shadow shown for both): НЕ МІЙ СЕКТОР (stop-list baskets: auto, airline, bank, energy_utility, insurance, reit, retail, restaurant, defense, betting, luxury, crypto, neocloud, manufacturer except Taras exceptions), ЛИШЕ СПЕКУЛЯЦІЯ (memory, biotech, pharma, unprofitable_story, commodity, cyclical, china; fresh IPO), БРАКУЄ ДАНИХ (3 cards). Price word NO_MULTIPLE -> БРАКУЄ ДАНИХ.
5. STRONG BUY conditions unchanged (verified on the 2 STRONG BUY cards NVDA, NFLX of the 29.09/03.10 data; the paid screener shows STRONG BUY 2, BUY 20, BUY WAIT 46, AVOID 66, ЛИШЕ СПЕКУЛЯЦІЯ 117, БРАКУЄ ДАНИХ 3, НЕ МІЙ СЕКТОР 233 = 487).
