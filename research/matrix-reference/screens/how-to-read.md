# Screen: How to read a card ("Як читати картку")

- URL: `/how-to-read/` — nav: З чого почати -> Як читати картку. Captured 2026-09-29. Screenshot: `how-to-read__top.jpg` (top only; rest captured as text).
- Type: static explanatory page (no inputs besides global search/header). Footnote links open the live **ABNB** card (`/t/ABNB/`) at a specific tile via URL hash, e.g. `/t/ABNB/#tile=level` (deep-link pattern `#tile=<name>`).

## Purpose
Explains the company card (`/t/<TICKER>/`) in 8 numbered places. Also states the philosophy: a card is not advice to buy; it is an analysis with the same rules for everyone: competence circle -> business quality in points -> price -> doubling arithmetic.

## Content (paraphrased)
**Whole card in one paragraph.** Top: verdict row (what to do) + price word + quality level, e.g. "BUY · Fair price · Level A"; below it the position and kill-lines. Two modes:
- **"Просто" (Simple)**: expandable tiles — competence circle; quality level with total score and eight components; ten signs of a good company + red flags; valuation (price word, multiple, EPS growth, PEG, FCF yield, comparison vs market and vs own history, charts); valuation change (getting cheaper while business grows vs. getting cheaper because forecasts worsen); x2 arithmetic; data completeness; Taras's assessment. Every number with a time series has a chart: click the price in the header -> 5-year price; tiles open charts for quality, cash flow (OCF and FCF), debt, shares, scenarios.
- **"Детально" (Detailed)**: same verdict as 8 steps with numbers and charts.

**The 8 places**
1. **Verdict row** — boldest word is the verdict; next to it price word + level. Verdict always computed as "I don't hold it" (existing ownership doesn't influence it). Stock price is in the header by the ticker, not in the verdict.
2. **Quality level and score** — level A–E derives from a 0–100 score across eight components, minus a penalty for flags. If the score is high but the level lower, a note explains what caps it: not reviewed by Taras, critical flag, debt, short profitability history.
3. **Valuation ("Оцінка")** — 1st line price word; 2nd the basis multiple; then 12-month EPS growth per consensus, PEG, yield after options (?"доходність після опціонів"), comparison with index and with own history. Like-for-like: forward vs forward, trailing vs trailing.
4. **Red flags** — a **critical flag caps level at C and forbids BUY**; a **serious flag subtracts points**. Each flag is one factual statement with a number and a threshold from settings, not an opinion.
5. **x2 arithmetic** — base scenario never assumes multiple expansion, only earnings growth. Expanded view shows: EPS today, growth by year with source, multiple in the scenario, price in five years, and CAGR.
6. **Known risks** — measured risks that don't reach flag level, with number and threshold, plus typical risks of the basket. Not part of the verdict; reference only.
7. **Basis switcher** — buttons above the tiles recompute **gates 2 and 3** on another basis (**P/E, P/OCF, P/FCF**). Default basis chosen by the engine, with a caption why.
8. **"Детально" mode** — toggle "просто/детально" in card header. Detailed shows the whole path: gate 0, level components, price lenses, matrix cell, flags, arithmetic, data, and a "why exactly this verdict" sentence.

**Deliberately absent from the card**: return promises, analyst target prices, other people's ratings. If a number is missing, the card says there is a gap in words — never substitutes zero or average.

Footer: link "Як рахує рушій: методологія" -> `/methodology/`; disclaimer; note that company logos are used only to identify the company and imply no endorsement; sources/licences of logos stored internally.

## Links on the page
`/t/ABNB/` (ticker + 8 "подивитись на картці ABNB" links with `#tile=` hashes), `/methodology/`, `/screener/`.

## Business rules extracted
Copied to rules-and-metrics.md (gates, flags, basis switch).
