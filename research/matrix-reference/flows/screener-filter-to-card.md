# Flow: screener filtering -> results -> card / compare

1. `/screener/` default: all verdicts/levels/prices, sorted by score desc, "показано 104 з 164" (100 rows per page + `показати ще N`).
2. Choose e.g. verdict=BUY, level=B -> hash `#verdict=BUY&level=B&sort=score&dir=1`, counter "показано 10 з 164".
3. Optionally expand "Ще 16 фільтрів": quadrant, basket, sub-sector, review, basis, known risks, min CAGR, max PEG, min yield, min drawdown, ticker-like text, level ceiling, new-BUY-this-week, index, critical flag, matrix position.
4. Sort by clicking a column header (best→worst first click).
5. Row: ☆ (watchlist), ticker link -> card. For side-by-side: open `/compare/` and add 2–4 tickers (no multi-select in screener seen).
6. Reset with `скинути`.
