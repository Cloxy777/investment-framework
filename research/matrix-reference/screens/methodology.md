# Screen: Methodology ("Методологія")

- URL: `/methodology/` — reached from links "як рахується вердикт" / "Як рахує рушій: методологія". Captured 2026-09-29. Screenshot: `methodology__top.jpg`.
- Static long-form page with in-page table of contents ("Зміст") and "вгору" (back to top) links. No inputs besides header/search.
- **This page is the authoritative rule book. Full numeric rules are in [../rules-and-metrics.md](../rules-and-metrics.md)** (thresholds tables copied there as facts; prose paraphrased).

## Purpose
Explains in four steps (same for every company) how a verdict is produced: competence circle -> business quality in points -> price via lenses -> 5-year doubling arithmetic. Says "good company at a fair price".

## Sections (TOC order)
1. Ворота 0: коло компетенції (Gate 0: circle of competence)
2. Ворота 1: рівень якості від A до E (Gate 1: quality level)
3. Ворота 2: ціна (Gate 2: price, 5 lenses)
4. Матриця: рівень і ціна дають вердикт (matrix)
5. Після матриці: прапорці, арифметика х2, дані і позиція (post-matrix)
6. Усі вердикти (all verdicts glossary)
7. Ред флаги (red flags table)
8. Правила, які поки не працюють на живих даних (rules not yet working on live data)
9. Індекси (indices; source + composition date + count)
10. Субсектори (sub-sectors; counts of companies per subsector)

## UI elements
- Tables: baskets (basket | why), stop-list (basket | why | when exception possible), speculation-only baskets, component scoring tables (condition | points), matrix (level × price word incl. a 6th column "Немає мультиплікатора" -> "БРАКУЄ ДАНИХ"), verdict glossary, position size by level, flags table (flag | severity | category | live-data status), not-working-rules table, index table, subsector table.
- Ukrainian typography: decimal comma, "x" as multiplication sign in "1,5x".

## Data on page seen 2026-09-29
- Indices: S&P 500 (source FMP composition, dated 23.09.2026, 500 companies); Nasdaq 100 (source api.nasdaq.com list, 19.09.2026, 100).
- Subsector list: ~80 subsectors, largest: chips 12, cybersecurity 7, pharma ("ліки") 7, memory 7, electricity 6.
- Stop-list exceptions decided by Taras: ASML, AVGO, BJ, COST, HY9H, MA, NVDA, SSU, TSM, V.

See rules-and-metrics.md for all formulas.
