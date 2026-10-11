# Methodology page: capture status and diff vs baseline (2026-10-03)

Page: `https://matrix.tarasguk.com/free/methodology/` (free tier). Verbatim copy: `data/raw/methodology.free.2026-10-03.txt` (27 222 chars, 484 lines). Structured copy: `formulas/methodology-rules.json` (machine-readable; cross-checked by script: 36 flag labels, 81 sub-sector counts, 7+1 basket labels all found in the raw text; weights sum to 100).

## 1. What "fully extracted and processed" means here
| Layer | State |
|---|---|
| Raw text of every section (Gate 0, Gate 1 + 11 sub-score tables, Gate 2 lenses + price words, matrix, after-matrix, verdict list, 36-row flag table, not-live table, indices, 81 sub-sectors) | DONE, verbatim, no truncation (page has 0 `<details>`, 26 tables, nothing collapsed) |
| Numbers/tables as data | DONE in `methodology-rules.json` |
| DOM anchor ids (internal keys: `flag-<key>`, `price-<WORD>`, `verdict-<KEY>`, `part-*`, `lens-*`) | DONE (36 flag keys recorded; read from element ids on the page, no page source/JS read) |
| Diff vs 29.09 baseline | DONE below (baseline was a paraphrase, not verbatim, so the diff is semantic) |
| Executable implementation (`analysis/engine_replica.py`) | NOT started: needs card data (Phase 1/3) |
| Edge cases the page does not state | listed in section 3 (cannot be extracted from this page at all) |

## 2. Diff vs baseline (`rules-and-metrics.md`, 2026-09-29)
All thresholds, weights, sub-score tables, caps, lens bands, matrix cells and verdict definitions are **unchanged**. Changes/additions found:
1. **Cycle-peak paragraph (Gate 2) gained a sentence:** a manufacturer/cyclical/commodity company that goes from **loss to profit within 12 months is marked the same way** as a cycle peak, and neither enters the verdict nor the lenses. (New rule; not in baseline.)
2. **Indices section: new paragraph** - price comparison vs S&P 500 / Nasdaq-100 on the card price chart and in "My portfolio" uses **ETF prices SPY and QQQ**, not index values (fee gap ~0.1 %/yr).
3. **Index composition source changed:** S&P 500 = "FMP: composition of fund SPY", as of 03.10.2026, **501** companies (was FMP, 23.09.2026, 500). Nasdaq 100 = "FMP: composition of fund QQQ", as of 02.10.2026, **100** (was api.nasdaq.com list, 19.09.2026, 101 cards).
4. **"Rules not working on live data" table now has three columns** (field, why not filled, where the rule is used). New detail: *where margin is heading* is "filled manually; not yet computed from 12M operating margin" and feeds flag `growth_without_profit` and component `margin`; *guidance change* also feeds the ten-signs item "Revenue growth"; AI-risk tag feeds flag `ai_negative` and component `moat`.
5. **Position caps sentence gained "mega-cap also not higher"** (read: a mega-cap STRONG BUY level A is also capped at 15 %). Baseline only said STRONG BUY level A up to 15 %.
6. **Revenue sub-score table heading now says** "(contribution of revenue; the rest of growth in the probe is negative)" - clarifies that the 8 pts max is revenue's share of the 20-pt growth component.
7. **Gate 0 exception text for TSM extended** with a political rationale ("better than investing in the communists themselves"); basket and exception lists unchanged (ASML, AVGO, BJ, COST, HY9H, MA, NVDA, SSU, TSM, V).
8. **Flag table rows are 36** (anchors confirm); each row carries category + "penalty in score / not in score" + "not live" marker. Baseline listed the same set in prose.
9. **Sub-sector counts identical** to baseline (81 values, script-compared) although they are labelled "companies in our cards"; they cannot be counts of the 20 free-tier cards (sum = 175), so they describe the registry/engine set (see open-questions item "what is the counted set").
10. Navigation anchor structure changed: page is now served under `/free/methodology/` (the baseline URL was `/methodology/` and `/methodology.html#verdict-BUY`). Verdict anchors exist as `#verdict-STRONG_BUY`, `#verdict-BUY`, `#verdict-BUY_WAIT`, `#verdict-AVOID` (others presumably `-SPEC_ONLY`, `-NEED_DATA`, `-NOT_MINE`).

## 3. Internal inconsistencies on the page itself (new, add to rules-supplement section E)
- `capex_external_financing`: flag table says category "quality: penalty in score", but the prose says it is a **serious flag without penalty** (points only inside the discipline sub-score). Which one the engine uses must be fitted on a card that carries this flag.
- `sbc_revenue_minor` (minor): table says "penalty in score" while the severity scale gives minor = 0 points. Likely "penalty" here means "counted among quality flags", with 0 points.
- Page states "Бали нижче порахував сам рушій на одній компанії з повними даними, змінюючи по одному полю": the sub-score tables are **measured steps**, not literal config values (e.g. 9.8, 5.2, 4.8, 1.8 look like products of weights x fractions). Treat them as the contract to reproduce, but expect the true config to be fractions of the weight.
- Rounded values hint at the underlying formula: profitability 15 x {0.5, 0.65333..., 0.34667...}; revenue 8 pts with 3.2 = 40 % of 8; EPS 7 pts with 2.8 = 40 % of 7; FCF has no unknown row; margin unknown 5 = 50 % of 10 (not 40 %); balance unknown 5 = 50 %; capital sub-scores unknown 3.5/6/6 (not uniform 40 %). So "unknown = 40 %" is NOT uniform across sub-scores.

- **Capital & SBC does not add up as printed:** sub-score maxima are 6 (SBC/FCF) + 8 (ROIC) + 7 (shares) = 21, but the component max is 10 (NVDA scores 10.0, ABNB 5.0, GOOG 4.0). The combination rule (cap at 10, rescale by 10/21, average, or weakest-link) is not stated. Same check for growth passes (8 + 7 + 5 = 20). First fit target in Phase 3.

## 4. What this page does NOT say (needs card data or cannot be recovered)
Open items the methodology text leaves undefined; all are on the Phase 3 target list:
- Edge inclusivity (>= vs >) of every bucket.
- How the business type, moat class and basket are assigned per company (registry fields set by Taras; not derivable).
- Numeric thresholds of ~30 flags (only concentration 25/33/40 %, debt 1.5x/3x/5x, dividend 60 % of FCF, SBC 20 % of revenue / 100 % of FCF, external financing 25 % of capex / 50 % of OCF, OCF lag 5 % are stated).
- Growth-path decay for years 3-5 (only "max 25 % per step"), definition of "our model" in consensus blending, pessimistic parameters (16 multiple, 0.50 factor are on cards, not here).
- Own-history windows (5y min, 3y max, average: trailing or forward P/E; "history < 3 years clamps to +-1").
- Source/date of the S&P 500 forward P/E and index EPS growth.
- Data-completeness field list and weights; ten-signs thresholds; "до наступного вердикту" generator; quadrant thresholds for "Зміна оцінки"; basis-selection logic; "Gate 3".
- Hysteresis exact behaviour (entry/exit mechanics with the 2 pt and 5 % margins).

## 5. Next for this page
Fit the unknowns above on card data (Phase 1/3). Re-capture `/free/methodology/` again before access ends to detect further changes (the page changed between 29.09 and 03.10).
