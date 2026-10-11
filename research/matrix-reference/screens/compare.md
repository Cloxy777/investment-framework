# Screen: Compare companies ("Порівняння компаній") — `/compare/`

- Nav: Скринер -> Порівняти компанії; card button "порівняти з …" -> `/compare/#TICKER/`. Captured 2026-09-29. Screenshots: `compare__empty.jpg`, `compare__typeahead.jpg`, `compare__two-companies.jpg`.
- URL state in hash: `/compare/#GOOG/META` (tickers separated by `/`; opens a set directly). Note: changing only the hash in the same tab did not re-render; the state updates via the UI field.

## Purpose
Side-by-side comparison of **2 to 4** companies. Same metrics aligned in rows; better value highlighted (green tint). "Nothing is recomputed: all numbers come from the same cards."

## Inputs
- Field "додати компанію" (search combobox, placeholder "оберіть компанії: тікер або назва"). Type-ahead list under field; suggestions show `TICKER Company (Ukrainian alias)` e.g. "GOOG Alphabet (Гугл)", "META Meta Platforms (Мета)" — so search also matches Ukrainian transliterations. Selecting adds a chip `TICKER · Name ×` (× removes). Hint text: choose 2–4 companies; after first: "the second is added the same way". Max 4; min 2 (with only 1 selected the table already renders one column).
- Footer button **"Повідомити про помилку"** (report an error; form not opened).
- Global search also present.

## Outputs (2 companies: GOOG vs META)
Column headers = ticker link + name -> card. Row groups (uppercase section titles):
1. **ВЕРДИКТ**: Вердикт (BUY / BUY WAIT) · Слово ціни (Справедлива / Дорого, але росте) · **До наступного вердикту** (what must change for verdict to upgrade), e.g. GOOG: "BUY becomes STRONG BUY at quality score above 80 (missing 2,0 pts; biggest headroom: Capital & SBC component, 4,0 of 10) or at base CAGR above 15 % (now 13,2 %, missing 1,8 %)"; META: "BUY WAIT becomes BUY when price falls below $477 (NTM P/E 14,3) or EPS growth 12M above 80 % or quality score above 80 (missing 4,8 pts, biggest headroom: Predictability, 9,0 of 15)".
2. **РІВЕНЬ ЯКОСТІ**: Рівень (B/B) · Бал з 100 (78,0 / 75,2; best highlighted).
3. **СКЛАДОВІ БАЛУ**: 8 components each "X з max": profitability, growth, predictability, moat, margin, balance sheet, capital & SBC, discipline.
4. **Valuation block**: multiple (NTM P/E 20,5), PEG (0,49), EPS growth next 12M by consensus (+42,3 %, 11 analysts), lens scores (+1/−2/0/+1/+1 and sum +1).
5. **ДЕСЯТЬ ОЗНАК**: count of green signs.
6. **РЕД ФЛАГИ**: counts (critical/serious/minor).
7. **АРИФМЕТИКА Х2**: base CAGR (13,2 % / 17,4 %).
8. **ОЦІНКА ТАРАСА**: Taras's own rating with date (e.g. "STRONG BUY, 18.09.2026") — separate from engine verdict.
9. **Chart**: price indexed to 100 at common start (30.09.2021), monthly close, one line per company (META green line); note "changes are compared, not prices of different companies".
- Page footer (all pages seen on this one): "Data as of 29.09.2026, next recalculation overnight, companies 546. Методологія · Як читати картку. Матриця Тараса Гука · matrix.tarasguk.com. [Повідомити про помилку]". => the total universe is **546** cards.
- Empty state: prompt "Оберіть компанії: від двох до чотирьох, полем вище…" + disclaimer.
