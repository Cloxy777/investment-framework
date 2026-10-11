# Data completeness % — recovered weights

Card footer: "Повнота даних: достатні, N % даних"; tile "Заповненість полів" (table `що саме | стан | хто закриває`, first row "усього полів для вердикту N %"). Bar chart: filled (green) / closed by paid provider (brown) / nobody (red); "решта поділена за тим, хто здатен її закрити: платний провайдер, ручний запис Тараса або ніхто"; "Частки решти рахуються за кількістю прогалин, а не за їхньою вагою у вердикті" (shares of the remainder are counted per gap, not weighted).

Observed over 20 cards (completeness = 100 - sum of gap weights):
| Missing critical field | Weight (pp) | Evidence |
|---|---|---|
| guidance direction ("напрям guidance", paid provider) | **3** | present on every card (97 % = 100-3) |
| SBC share of free cash flow (when basis OCF / FCF unknown) | **7** | ORCL 90 % = 100-3-7 |
| competitive advantage / moat (not set in registry) | **7** | PLTR 90 % = 100-3-7 |
| multiple history in the NTM P/E basis | **10** | V 87 % = 100-3-10 |
| free-cash-flow yield (currency problem TWD) | **6** | TSM 81 % = 100-3-10-6 |
Labels: "достатні" >= 80 %; <60 % downgrades STRONG BUY to BUY (methodology; high bound 80 %). Min in sample 81 % (TSM); max 97 %. Status: Fitted — five gap weights recovered exactly; other fields' weights and the denominator list are unknown (the sum of all weights is 100; ~31 critical fields would match a 3-point granularity).
TSM extra detail shown: "історія капіталізації не відновлюється: ціна x розбавлені акції EDGAR у 5,0 раза більша за капіталізацію FMP: імовірно одна ADR" and "різні валюти (TWD, USD)... курс ЄЦБ недоступний: ЄЦБ припинив публікувати курс TWD 30.10.2020" => ADR ratio detection (share count x price vs market cap) and ECB-rate-only FX conversion (a rate source dependency).

---
# UPDATE 2026-10-03: weights refitted on 488 cards (`analysis/fit_completeness.py`, `formulas/data-completeness-fit.json`; max residual 0.7 pp = whole-percent rounding)
| Missing field | Weight (pp) | cards |
|---|---|---|
| guidance direction (paid provider) | 3 | 485 |
| multiple history in basis NTM P/E | 10 | 367 |
| multiple history in basis P/FFO | 10 | 26 |
| multiple history in basis P/NTM FCF | 10 | 14 |
| current multiple in basis NTM P/E / P/FFO (no valuation without it) | 10 | 8 + 1 |
| moat (competitive advantage) | 6 | 65 |
| business type | 6 | 45 |
| both classification tags (type and moat) | 13 (about 6 + 6 + 1) | 32 |
| SBC share of FCF (OCF basis: of revenue) | 6 | 54 |
| EPS growth 12M forecast (without it no verdict) / EPS or FCF forecast | 6.5 | 20 + 20 |
| margin / revenue growth / FCF yield | 6-7 | 5 / 4 / 5 |
| balance (cash, debt, shares), price or cap, years profitable, FMP symbol collision | about 5 each | 1 each |
Labels: "достатні" >= 80 %; STRONG BUY -> BUY below 60 %.
