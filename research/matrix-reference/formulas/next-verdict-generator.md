# "До наступного вердикту" / "Що потрібно для кращого вердикту" generator

Texts captured per card in `data/cards/<T>.json -> detailed.needed` (also screener column and compare row). Format: OR-list of routes separated by `;`. Present only when a better verdict exists (NFLX, NVDA: none; TSLA: "ціною не змінюється: <basket reason>").

## Routes (what each one is) — status per route
| Route text | Rule | Status |
|---|---|---|
| `при балі якості вище C (бракує балів D, найбільший запас: складова X, балів a з b)` | C = next level cut above the current **score**: 55 if D, 70 if C, 80 if B (no route for A or when score already >= 80, e.g. ADBE). `D = C - score` (1 dp). Component X = `argmax(max - points)` over the 8 components, text "a з b" = its points and maximum | **Exact 13/13** (`analysis` check in this session) |
| `при базовому CAGR вище B % (зараз CAGR c %, бракує d %)` | shown iff base CAGR < bar; B = 15 (14 for level A); d = B - c | Exact 7/7 |
| `після перегляду Тарасом (STRONG BUY вимагає тегів, підтверджених Тарасом)` | shown for a BUY with level in {A,B} when not reviewed and STRONG BUY is the next step | Exact (ABNB, ADBE) |
| `коли зникне критичний прапорець a, b, c` | lists the quality-critical flags (ORCL) | Exact |
| `при рості EPS 12 міс. вище X %` | EPS growth at which the verdict would improve (COST 21, CRM 8, META 86, MSFT 23, UBER 4, V 27) — solved on the engine with growth as the variable (affects PEG lens, growth lens, price word `need` bar, base CAGR bar); exact algorithm Unknown | Unknown |
| `коли ціна впаде нижче $P (мультиплікатор NTM P/E M)` | price at which the verdict reaches the next rank, **search over price with all lenses recomputed** (P/E, trailing P/E, PEG, S&P ratio, FCF yield all scale with price; regime bonus switches at P/E <= 20 for mega-caps; base CAGR changes with price) ; displayed M = P / EPS_NTM | Fitted-approx |

## Price route: replica vs shown (`engine_replica.py::next_verdict_check`, grid search from current price down)
| Ticker | shown price (P/E) | replica |
|---|---|---|
| AAPL | $196 (20.5) | $195.88 (20.54) ok |
| META | $387 (12.1) | $386.06 (12.09) ok |
| COST | $440 (19.3) | $441.91 (19.39) ~ |
| V | $300 (20.0) | $302.05 (20.1) ~ (shown is exactly the mega-cap regime multiple 20.0) |
| AVGO | $348 (20.0) | $349.9 (20.1) ~ |
| MA | $442 (20.0) | $455.6 (20.6) off (shown uses 20.0 = regime edge) |
| MSFT | $409 (20.0) | $418.8 (20.5) off |
| AMD | $133 (9.8) | $128.05 (9.43) off |
| CRM | $200 (13.6) | $210.5 (14.35) off |
| PLTR | $80 (38.4) | $112.2 (53.9) off |
| UBER | $6.58 (1.6) | $13.2 (3.2) off |
| TSM | $404 (19.2) | (not run: no yield/hist) |
| GOOG, ABNB, AMZN, ORCL, ADBE | no price route shown | replica gives routes for GOOG (hysteresis-held lens makes the stateless replica start from a different sum) |
Observations: when the shown multiple is exactly 20.0 (MSFT, MA, V, AVGO) the binding step is the **mega-cap regime bonus edge (P/E <= 20)**; the site's search looks at discrete candidate multiples/steps where the lens sum changes, whereas a continuous scan finds nearby values. Hypothesis: the generator evaluates the engine at the thresholds of each lens (S&P ratio 1.0/1.3/2.0 x 20.1, PEG 0.5/1/1.3/2 x growth, yield thresholds, regime 20) and reports the highest price meeting the target. This is not implemented.

## Where else it appears
Screener column "До наступного вердикту" (same text), compare row (full text), start page BUY-zone list ("BUY стане STRONG BUY коли ціна впаде нижче $442 (мультиплікатор NTM P/E 20,0)"), report calendar not.

---
# UPDATE 2026-10-03 (paid tier)
The whole screener column "До наступного вердикту" is captured for 487 cards (`data/lists/screener-all.csv`, column 14) and each card's text is in `data/cards/<T>.simple.txt`/`.json` (`detailed.needed` only exists for the 20 detailed captures; screener text is the same string). Score route re-verified on all 487 screener texts that contain it: **60/60 exact** (cut, missing points, biggest-headroom component over the known components); the CAGR route appears only once more in the screener column (1/1). Most screener texts are price routes or gate-0 explanations. The price route remains approximate (hysteresis-held lens sums and discrete candidate multiples).
Stop-list cards print the gate-0 reason instead: `ціною не змінюється: <basket why>` (233 НЕ МІЙ СЕКТОР cards).
