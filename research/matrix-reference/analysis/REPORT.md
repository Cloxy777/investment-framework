# REPORT — engine reconstruction (final, paid tier, 2026-10-03)

Sample: **488 cards** (487 company cards of the 547-company universe + ABNB; 20 of them also in detailed mode), 98 with Taras's paid tiles. All values are what the UI prints (the cards show every raw input next to each score and the config keys, so most rules were recovered exactly). Reproduce: `python analysis/parse_cards.py && python analysis/run_all_cards.py` (saved output: `analysis/run_all_cards.out.txt`). Earlier free-tier report (20 cards) is superseded by this one; its numbers are a subset.

## Fit statistics (exact = identical displayed value)
| Quantity | Result | Status |
|---|---|---|
| Quality components: profitability, growth, margin, balance, capital & SBC, discipline | **488 / 488 each** | Exact (capital & SBC is a fitted formula: 13 constants; high-buy-back cut-off 2 % guessed) |
| Quality components: predictability, moat (456 classified cards) | 456 / 456 each | Exact (registry tag lookup; moat modifiers AI -3, share-down -4) |
| Unclassified companies (32): score renormalised on known weights | exact | Exact |
| Flag penalty (given the flag-table rows) | 488 / 488 | Exact |
| Score | 488 / 488 | Exact (float-format rounding, floor 0) |
| Level | 477 / 488 | 10 level-E cards from the registry tag "not understood" + 1 level-hysteresis card (LHX) |
| Lenses (PEG, S&P, FCF yield, own history, growth vs market) | 2 390 / 2 435 | **Exact**; 43 of the 45 misses carry a printed hysteresis note and lie within 5 % of a threshold; 2 unexplained (CRWD, PANW history lens) |
| Price word (on displayed lens sum, growth, level, CAGR) | 454 / 467 | Fitted; value-trap word has 5 outliers (AIG, CLX, OXY, GPN, MET) and others (APO, DAL, DTE ...) |
| Verdict (matrix + STRONG BUY + critical/thesis rules + gate-0 shadow) | 464 / 467 | Exact except VICI (shadow) and 2 parse gaps |
| x2 growth path / CAGR, FY table >= 4 years | 248 / 288 within 0.3 pp (86 %) | Fitted |
| x2 CAGR, FY table 3 years or fewer | 44 / 152 | **Unknown** (engine uses FY+3 estimates with 1-2 analysts that the card does not print) |
| x2 scenario multiples (pessimistic 16 / base min(NTM, avg3 scaled) / optimistic 1.2 base or 20.1) | within rounding on every card with a computable value | Fitted |
| "До наступного вердикту" score route | 60 / 60 | Exact |
| "До наступного вердикту" price route | about 2 exact, 3 within 1 %, rest off (first 11 cards) | Hypothesis (discrete candidate multiples) |
| Ten-signs thresholds | revenue 8 %, EPS 10 %, margin 15 %, FCF growth 5 %, net debt 2x, capex 15 %, dilution 1 %, concentration 20 % | Fitted (boundaries from 488 cards) |
| Data-completeness gap weights | guidance 3, history/current multiple 10, moat 6, type 6, SBC share 6, EPS forecast 6.5, margin/growth/FCF-yield 6-7 (max residual 0.7 pp) | Fitted |
| Doubling year "х2 у році N" | not reproduced | Unknown |
| Hysteresis (lenses, level, price word) | mechanism observed and quantified (5 % band for lenses, 2 points for level) | needs previous-day state to replicate |

## Exact formulas (where)
`formulas/quality.md` (incl. paid update), `price-lenses.md`, `x2.md`, `verdict-rules.md`, `flags-catalogue.md` + `flags-corpus.md` (all 59 sentence templates, 33 flag-table kinds), `ten-signs.md`, `data-completeness.md`, `next-verdict-generator.md`, `misc.md`; machine-readable constants `formulas/methodology-rules.json`. Code: `analysis/engine_replica.py` (850 lines), `run_all_cards.py` (test harness), `parse_cards.py`, helpers listed in README.

## Still unknown / not derivable
1. Raw-data inputs (ROIC, SBC/FCF, net cash, debt/EBITDA, normalised EPS, NTM EPS from quarterly consensus, FX conversion, ADR detection) are taken as displayed; rebuilding them from SEC/FMP is not validated here (the cards print source tags and fields: `years_profitable`, `operating_margin_after_tax`, `net_margin`, `net_cash`, `debt_to_ebitda`, `sbc_to_fcf`, `buyback_yield`, `share_count_change`, `roic`, `ocf_ttm`, `capex_ttm`).
2. Hysteresis state machine and the price-word / value-trap outliers.
3. FY+3 consensus used by x2 step 1 for companies with short printed tables; doubling-year formula; next-verdict price/EPS-growth routes.
4. Registry inputs (basket, business type, moat, AI risk, market-share trend, growth source, capex funding, "not understood" tag, Taras's review/rating/theses/kill-lines): manual, partly AI-drafted; exported as `data/derived/registry-tags.csv` and `data/derived/taras-all.json` so they can be bootstrapped, not derived.
5. Numeric triggers of about 15 flags and of AI-draft flags (guidance cuts, one-offs) — sentence corpus recorded.
6. Anything behind the Pro tier: the "AI аналітика" tile is a teaser even on this plan.

## What to capture next (if access continues)
A second and third daily snapshot of all 487 cards (about 55 minutes each with `analysis/js/harvest_cards.js`) — turns hysteresis, price-word outliers, level history and the valuation-change quadrant into fit data and gives the first real time series; then the detailed-mode text for all cards if the 8-step narrative is wanted verbatim.
