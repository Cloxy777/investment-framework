# Part 5 — Validation: paired comparison, backtest design, acceptance criteria

Nothing in this document recomputes a score. All repo figures are **read from existing dated watchlist entries** (`watchlist/**`) and `portfolio/holdings.md`; Matrix figures are from `research/matrix-reference/rules-supplement.md` section D (`RS`), captured **2026-09-29**. The two sides are therefore **not contemporaneous** (dates differ by 2 days to 3.5 months, and prices moved). Where a disagreement could be a pure time effect, that is said. If any valuation is ever recomputed from this table, Rule 0 applies first (live price, `framework/fair-value-methodology.md:13-30`). Labels: **[F]** fact, **[I]** inference, **[O]** opinion.

## 1. Paired comparison on overlapping tickers

### 1.1 Table

`Q` = Quality Score, `V` = Valuation Score, `C` = Composite Score (repo, 0 = most attractive). Matrix level letter, price word, verdict and score from `RS:168-181`. Repo action = the action recorded in the entry (nominal action from the Composite band, then the "practical" action). Repo price is the price on the entry date; Matrix price is on 2026-09-29.

| Ticker | Repo entry date · price | Repo Q / V / C | Repo action | Matrix level · score | Matrix price word | Matrix verdict | Matrix base / opt. CAGR | Direction agrees? |
|---|---|---|---|---|---|---|---|---|
| NVDA | 2026-09-17 · $218.70 | 90.3 / 36.2 / 23.0 | nominal BUY full (Composite 0–29.9), practical HOLD/no add (sizing binds by 0.345 shares; R/R 2.11:1 passes) | A · 91.0 | cheap (+6) | STRONG BUY | 20.4 / 21.7 % | **Yes** (both at the top of the book) |
| MSFT | 2026-07-30 · $449.40 | 79.9 (FAILS gate by 0.1) / 38.9 / 29.5 (ref only) | BUY band on raw V, **not actionable** (R/R 1.33:1) | A · 87.0 | expensive but growing | BUY WAIT | 17.5 / 21.8 % | **Yes** (no purchase now) — but quality verdicts differ (gate FAIL vs level A) |
| GOOG | 2026-07-22 · $342.61 | 71.4 (FAIL) / 64.2 / 46.4 (false green) | HOLD | B · 78.0 | fair | BUY | 13.2 % (base) | **No** (HOLD vs BUY) |
| META | 2026-08-26 (PM) · $578.83 | 87.5 / 39.4 / 26.0 | nominal BUY full, practical HOLD/no new capital (price 12.6% above the $514.08 buy limit) | B · 75.2 | expensive but growing | BUY WAIT (BUY at price < $477, NTM P/E 14.3) | 17.4 % (base) | **Yes** on action (both wait for a lower price; the two limits differ: $514 vs $477) — quality differs (+12.3) |
| AVGO | 2026-09-28 · $352.39 | 86.3 / 71.3 / 42.5 | HOLD, no add (R/R best case 1.71:1) | *not captured in RS section D* | — | — | — | n/a (Matrix lists AVGO only as a stop-list exception, `RS:38`) |
| ASML | 2026-09-11 · $1,717.30 | 82.4 / 94.6 / 56.1 | WATCHLIST ONLY | A · 88.0 | expensive but growing | BUY WAIT | 13.5 / 17.7 % | **Yes** |
| V | 2026-07-29 · $365.94 | 85.6 / 54.5 / 34.5 | nominal BUY standard, trade gated | A · 85.0 | expensive but growing | BUY WAIT | 12.3 / 16.5 % | **Partly** (repo nominal BUY vs Matrix BUY WAIT; quality agrees to 0.6) |
| NFLX | 2026-07-17 · $67.80 | 69.8 (FAIL) / 49.3 / 39.8 (false green) | HOLD | A · 85.8 | cheap | STRONG BUY | 18.0 / 20.1 % | **No** (HOLD vs STRONG BUY) |
| ABNB | 2026-08-24 · $187.30 | 80.5 / 87.1 / 53.3 | HOLD, no entry | B · 71.5 | fair | BUY | 14.4 / 18.7 % | **No** (HOLD vs BUY) — repo price is 20% higher than the Matrix's $156.08 |
| ADSK | 2026-08-23 · $253.82 | 84.9 / 39.0 / 27.1 | SET LIMIT ≤ $244.01 | B · 81.5 (capped B: growth) | fair | BUY | 12.2 / 17.5 % | **Yes** |
| MA | 2026-09-11 · $566.15 | 84.2 / 44.3 / 30.1 | nominal BUY standard, trade gated | A · 88.8 | expensive but growing | BUY WAIT | 14.7 / 18.9 % | **Partly** (same pattern as V) |
| ORCL | 2026-06-12 · $182.77 | Phase 01 FAIL (4 criteria) | PASS / do not buy | D · 51.5 | expensive but growing | AVOID | — | **Yes** |
| MU *(extra)* | 2026-07-29 · $808.27 | 49.0 (gate FAIL via FCF hard disqualifier) | PASS | B · 76.8 (gate 0: speculation only) | cheap | ЛИШЕ СПЕКУЛЯЦІЯ (shadow BUY WAIT) | 9.0 % (base) | **Yes** (do not own) — for opposite reasons (see 1.3) |
| SOFI *(extra)* | 2026-06-21 · $17.42 | Phase 01 FAIL (5 of 8), V 96.5 | PASS | D · 42.9 (stop-list) | fair | НЕ МІЙ СЕКТОР | — | **Yes** |

Not compared: MSFT/GOOG/NVDA overlap with `holdings.md` weights (MSFT 14.24%, NVDA 6.92%, META 6.07%, AVGO 3.43%, GOOG 0.55%, V 0.59%, NFLX 1.38%, `portfolio/holdings.md:51-78`).

### 1.2 Summary statistics (ten names with both a repo Q and a Matrix score)

- **Gate agreement (≥ 80.0 vs Matrix level A or score ≥ 80):** agree on 6 of 10. Both pass: NVDA, MA, ASML, V, ADSK. Both fail: GOOG. Repo pass / Matrix below: META, ABNB. Repo fail / Matrix passes: MSFT, NFLX.
- **Quality score difference (repo − Matrix):** NVDA −0.7, META +12.3, ADSK +3.4, V +0.6, MA −4.6, ASML −5.6, ABNB +9.0, MSFT −7.1, GOOG −6.6, NFLX −16.0. Mean absolute difference **6.6 points**; mean signed −1.5.
- **Rank agreement** of the ten quality scores: Spearman ρ = **0.18** (n = 10). [I] This is weak, but with unmatched dates, cap effects (ADSK), and n = 10 it is a prompt for the component-level pilot below, not a finding.
- **Action agreement (direction — buy now vs wait/hold):** 8 of 13 comparable names agree outright (NVDA, MSFT, META, ASML, ADSK, ORCL, MU, SOFI); 2 partly (V, MA); 3 disagree (GOOG, NFLX, ABNB — all cases where the Matrix says buy and the repo holds). **No case where the repo says buy and the Matrix says avoid.** [F] read from the table.

### 1.3 Every disagreement — which factor drives it, who is likelier right

| # | Ticker | What differs | Driving factor | Who is likelier right, and why |
|---|---|---|---|---|
| D1 | NFLX | Q 69.8 (gate FAIL) vs 85.8 (A); HOLD vs STRONG BUY | **Quality inputs.** The Matrix awards up to 15 points for predictability of a subscription business, uses forward (consensus) growth, and counts years of profitability (`RM:31-44`); the repo scores trailing gross margin/80, net margin and ROIC/30, 3-year revenue CAGR/25 and a 5-signal moat checklist needing cited evidence (`quality-scoring.md:41-113`). The repo's Margins term (gross margin ÷ 80) is a moat proxy that tends to score a content-cost business lower than a software business [I — NFLX's gross margin is not in the files I read, so this is unverified]. | **Undetermined — best test in the set.** [O] I lean towards "neither"; the repo's Margins term is a moat proxy poorly suited to a content-cost business, whereas the Matrix's predictability table is an author tag. A component-level recomputation with fresh data (Rule 0) resolves it; see pilot A. |
| D2 | MSFT | Q 79.9 (FAIL by 0.1) vs 87.0 (A) | Same as D1 plus the gate's knife edge: 0.1 point decides eligibility of a 14.24% holding. | Neither is wrong on action (no purchase now). The 0.1 difference is exactly the case for **P-009** (three-state gate). |
| D3 | GOOG | Q 71.4 vs 78.0; V 64.2 (fair band, HOLD) vs price word fair, verdict BUY; base CAGR 13.2% | **Different hurdle for "buy".** The repo needs Composite ≤ 49.9 *and* R/R ≥ 2:1 *and* the Quality gate; the Matrix needs level ≥ B, price word fair or cheap and base CAGR ≥ 10% (bar 15% only for STRONG BUY, `RM:76`). A 13.2% base CAGR is above the repo's own 10% hurdle `H` (`valuation-scoring.md:130`). Also **time**: repo entry is 69 days older. | [O] The Matrix's BUY is a lower bar by construction (no margin of safety, no R/R). Repo's HOLD is consistent with its rules. Not a contradiction of facts; a difference in what "BUY" means. P-001 makes the repo's implied return visible next to a consensus-path CAGR. |
| D4 | META | Q 87.5 vs 75.2 (**+12.3**, repo higher) | **Matrix's predictability (advertising 9/15) and capital-&-SBC terms** (compare page: predictability 9.0 with the largest headroom, `RS:107`) — the repo has neither; it rewards ROIC/margins. | [O] The repo is likelier to be *too generous* on SBC-heavy, capex-heavy names (see P-007); the Matrix's Capital & SBC table failed my verification (V32), so its side of the gap is not fully trustworthy either. |
| D5 | META | Buy limit $514.08 (repo) vs BUY below $477 (Matrix) | Repo limit = FV × (1 − MoS) (Owner-Earnings-adjusted); Matrix = price at which the price-word lenses reach "fair" (NTM P/E 14.3 ⇒ EPS ≈ $33.4). | Not comparable methods. Useful check: P-001's buy-price curve would state the price at which base consensus CAGR = 10% for META; compare all three prices. |
| D6 | ABNB | Q 80.5 vs 71.5 (**+9.0**); V 87.1 vs "fair"; HOLD vs BUY | **Time and price**: repo price $187.30 vs Matrix $156.08 (−16.7%): every price-based sub-score in the repo (FCF yield, EV/EBIT, forward PE, Upside modifier) has moved. Quality: repo gives a 4-year-profit company 80.5 by margin/ROIC/CAGR; Matrix's profitability term is 9.8/15 (only 4 profitable years, `01-verification.md` V26) and level B (71.5). The repo already flags its own 80.5 as "sensitive to two judgment calls" (`watchlist/not-in-portfolio/ABNB/ABNB-2026-08-24.md`). | Repo valuation is **stale for this comparison** (do not conclude). Quality: [O] the Matrix's persistence lens is a fair criticism of a knife-edge pass; **P-009** addresses the knife edge without adopting the Matrix's weight. |
| D7 | V, MA | Nominal BUY on Composite (34.5 / 30.1) vs BUY WAIT | **Quality's 50% weight in the Composite**: V's raw Valuation Score is 54.5 (Fair Value band, watchlist only) but the Composite (34.5) lands in the 30–49.9 "Cheap" band because Q ≈ 85; MA's raw 44.3 (Cheap) becomes 30.1, on the Very Cheap boundary (`valuation-scoring.md:169`). The Matrix says "expensive but growing" with base CAGR 12.3% / 14.7% below the 15% bar. Both repo entries are "trade gated". | [O] Both are defensible; the repo's own gates (R/R, sizing) blocked the trade, which is the safety net working. Interesting: the repo's Composite makes a fair-priced high-quality name look "Cheap" — the same effect the repo calls a "false green light" for NFLX and GOOG (`…/NFLX-2026-07-17.md`, `…/GOOG-2026-07-22.md`). Worth a separate review of the Composite weighting (open question). |
| D8 | ASML | V 94.6 (very expensive) vs "expensive but growing" (BUY WAIT) | **Growth lens.** The Matrix rewards +52.1% NTM EPS growth (PEG 0.6, growth vs market lens +1); repo valuation sub-scores are anchored on multiples and FCF, and forward PE vs its own 5-year range. | [I] Both stop the purchase. The Matrix's +52% may itself be a cycle-boosted number (semicap upcycle) — P-002 would print the flag if trailing EPS growth > 100%; if not, the forward-growth divergence flag P-004 would be the tool. |
| D9 | MU | Repo Q 49.0 (FCF-history disqualifier) vs Matrix B 76.8, "cheap" | Opposite reasons for the same conclusion: the repo blocks via a trough year (FY2023) in the 3-year window; the Matrix blocks via a stop-list/speculation-only basket. | **Demonstrated blind spot in the repo** — once FY2023 leaves the window the repo has no cycle awareness (P-002). |
| D10 | AVGO | no Matrix vector | Matrix treats AVGO as a author-approved stop-list exception (`RS:38`), no card data captured | Cannot compare. Add AVGO to the "re-capture" list (`open-questions-for-user.md`). |

**Pattern.** [I] The repo is *stricter than the Matrix at the buy decision* (extra gates: Quality 80.0, Composite band, R/R, sizing) and *looser than the Matrix on SBC-heavy, ad-funded, capex-heavy quality* (META). The Matrix is looser at the buy decision (no R/R, no margin of safety) but has a wider set of red flags. None of the disagreements is a case where the repo would buy something the Matrix considers AVOID.

## 2. Backtest design (feasible with free data)

### 2.1 What can be reconstructed point-in-time (PIT) — and what cannot

| Input | Free source | PIT-feasible? | Notes |
|---|---|---|---|
| Prices (split-adjusted close) | yfinance | Yes (adjusted for splits/dividends; use consistently) | Delisted tickers usually missing → survivorship |
| Fundamentals ≥ 3 fiscal years back | yfinance `financials` | **Limited**: about 4 annual and 4–5 quarterly periods (`fetch_fundamentals.py:1-40`; `valuation-scoring.md:271-297`) | Enough for the last ~1 year of quality scores, not for history |
| Fundamentals 10+ years | **SEC EDGAR XBRL `companyfacts`** (free, keyless) | **Yes, with the `filed` date** ⇒ true as-of-filing series for US filers, XBRL era (2009+) | Restated values appear under later filings — use only facts with `filed ≤ as-of date` |
| 10-year Treasury | FRED | Yes | |
| Forward PE, consensus growth, analyst fair values | none free & PIT | **No** | Exclude PEG, forward PE, Upside/Downside Modifier (set M = 0) and P-001 from the backtest; use trailing PE percentile instead of forward-PE range |
| Non-US filers (Wirecard, Nokia pre-2009, GE 2003) | none free & structured | **No** | Graveyard cases before the XBRL era are **not reproducible** for free; document as a limit |

### 2.2 Look-ahead pitfalls (and mitigations)

1. **Filing lag**: a fiscal-year-end value is not known until the filing date (typically 30–60 days later) — key every fact on `filed`, never on `end`.
2. **Restatements**: `companyfacts` returns later restatements for old periods — take the first-filed value.
3. **Ticker/CIK reuse and mergers**: map on CIK, not ticker.
4. **Survivorship**: yfinance drops delisted names; **use the graveyard names as forced inclusions** and add the list of index deletions where free (e.g. Wikipedia "changes" tables — partial). State the residual bias.
5. **Split/dividend adjustment**: mix of adjusted price and unadjusted per-share numbers creates false yields; use market cap = price × shares from the same filing date.
6. **Threshold peeking**: the 80.0 gate and all placeholders in `03-proposals.md` must be fixed **before** looking at forward returns; calibration of placeholders uses a training window, evaluation a later window.
7. **Regime overfitting**: the Matrix's constants are from one regime; this repo's own thresholds too. Evaluate across ≥ 2 rate regimes if data allows.

### 2.3 Metrics

- **Gate (80.0)**: hit rate = share of gate-PASS names outperforming a benchmark (MSCI Quality proxy ETF and S&P 500, per `benchmark-comparison.md:13-35`) over 12 and 36 months; **false negatives** = gate-FAIL names that beat the benchmark by > 10 pp; **false positives** = gate-PASS names losing > 30% vs benchmark; **drawdown avoided** = mean max-drawdown of FAIL names minus PASS names.
- **Composite ranking**: rank-IC (Spearman) between Composite at t and 12-month forward return; decile spread.
- **Turnover**: band changes per name-year and add/trim events with vs without P-009 hysteresis; with vs without P-003.
- **Flags/kill-lines**: precision (fired → drawdown ≥ 30% within 12 months), recall on the graveyard replays, lead time in quarters.
- **Guard metric**: portfolio-level turnover must **not** increase versus baseline (anti-turnover principle).

### 2.4 Minimal pilot — one session (≈ 3–4 hours)

Scope: the quality-side of the framework and two proposals (P-009, P-003), on a small, reproducible set.

1. **Universe (12 names)**: graveyard names reachable in the XBRL era — **IBM (2012–2018)**, **Valeant/Bausch Health (2014–2017)**, **Peloton (2020–2022)**, **GE (2015–2019)** — plus **8 current names**: NVDA, MSFT, META, NFLX, ABNB, ADSK, MU, ORCL. State plainly that Wirecard, Nokia and Cisco-2000 are out of reach for free structured data.
2. **Script** (`scripts/pilot/pit_quality.py`, throw-away): for each name and each 10-Q/10-K filing date `d` in the window, build the inputs for `quality_score.compute` from `companyfacts` (facts with `filed ≤ d`): net margin, ROIC (needs invested capital — take `StockholdersEquity + Debt − Cash` and document), gross margin, 3-yr revenue CAGR, ND/EBITDA, FCF/NI (annual and TTM), FCF positivity. Moat signals and TAM modifiers **cannot** be automated ⇒ hold them at a fixed conservative value (e.g. moat 3 of 5) for the entire run and label the pilot "quantitative quality only".
3. **Outputs per filing date**: `quality_score`, `gate_state` (P-009 with prior state), hard-disqualifier hits, P-003 kill-line firings computed from consecutive quarters, and the price drawdown from the running peak (yfinance).
4. **Questions answered**: (a) On IBM, Valeant, Peloton, GE: on which filing date did the score drop below 80.0 / did a hard disqualifier fire / did a kill-line fire — and how far was that from the peak? (b) On the 8 current names: how many gate flips between consecutive filings with and without a 2.0-point band? (c) For NFLX/META/ABNB: print the six repo sub-scores next to the Matrix's components to attribute D1, D4, D6.
5. **Deliverable**: one markdown table per name; no trading conclusions; decision log entry if any placeholder is calibrated.

Pre-declared tolerance: the pilot is a **plumbing and sanity test**, not evidence for adopting any threshold. Any claim of predictive power needs the full-universe backtest below.

### 2.5 Full backtest (only if the pilot passes)

Universe: S&P 500 constituents at each rebalance date (history from free sources is partial — record the missing share), quarterly rebalance, PIT fundamentals from XBRL, trailing valuation only, equal-weight PASS names vs benchmark, 2011–2025, walk-forward calibration of the placeholders (train 2011–2017, test 2018–2025). Report all metrics in 2.3 with confidence intervals; explicitly separate the **quality-gate effect** from the **valuation effect**.

## 3. Acceptance criteria and rollback per proposal

| ID | Acceptance criterion (measurable) | Rollback / kill condition |
|---|---|---|
| P-001 | On the 8 overlap names: |ours − Matrix base CAGR| ≤ 2 pp for ≥ 6; unit tests reproduce ABNB base 14.43 ± 0.05, pessimistic −0.82 ± 0.05; no session where the tool printed a number for a non-positive EPS | Remove the step from `/new-position` if consensus data is missing on > 30% of runs for 3 months or if analysts stop using the output (no citations in session logs) |
| P-002 | Every memory/semicap/commodity name in `watchlist/` flagged; ≤ 10% of non-cyclicals flagged | Raise the threshold if > 25% of names flag; drop if flag is ignored in 10 consecutive sessions |
| P-003 | Retro-fit on 5 names × 2 events: zero contradictions with recorded decisions; time from earnings to a documented decision ≤ 3 business days in ≥ 80% of events over the next quarter | Stop generating if overdue re-scores do not fall (RBRK/ZS-type latency persists) after 2 quarters |
| P-004 | ≥ 70% of names with documented "growth decelerating" evidence were flagged in advance; flag rate ≤ 20% of holdings | Remove flag if false-positive rate > 40% |
| P-005 | 100% of new sessions carry a category; zero Fast-Grower/PEG inconsistencies | Make optional |
| P-006 | User-approved registry exists; replay of `sessions/` shows number of `/new-position` runs avoided and **zero** stops the user later disagrees with | Retire any basket with a stop the user overrides twice |
| P-007 A | Table for ZS, RBRK, DUOL, NOW, ADBE, VEEV, DOCS, UBER produced with real SBC data | — |
| P-007 B | Adopt only if ≥ 3 names move ≥ 5 score points **and** the action band changes for ≥ 1 held name in a direction that a documented review agrees with | Keep `--sbc-adjust` off (single flag) |
| P-008 | Every FAIL maps to a documented note or new issue within 1 week; all flags reproduce by hand on 3 names | Drop flags with > 40% UNKNOWN rate |
| P-009 | ≥ 50% fewer PASS↔FAIL flips on replay of held-name history; **zero** adds allowed in AMBER | Set band to 0.0 (one constant) |
| P-010 | Seed matches `holdings.md` for ≥ 90% of fields; weekly record runs 8 consecutive weeks without manual repair | Revert to prose-only history |
| P-011 | Reproduces the worked example (79.44 / 33.69 / 67.0% coverage) from the same inputs | — |
| P-012 | Cluster table exists; acknowledgement written whenever ≥ 30% | Remove if never triggered in 2 quarters |
| P-013 | (b) fill is continuous at ±10 and ±20; tests pass; documents agree on Phase 01 numbers | Revert to the "refuse" behaviour if the interpolation moves any held name's band unexpectedly |
| P-015 | Rescore triggered ≤ 1 per name per quarter on average; no order ever placed on a trigger alone | Drop the −30% line if it fires > 3× more than Rule 9 without a fundamental event found |
| P-016 | Known-inverse tests pass; monotonicity guard never trips in 20 real inputs | — |
| P-017–P-019 | Formatter outputs equal stored numbers; precheck lists 100% of missing fields on the test set | — |
| P-020 | Template used for every framework change after adoption | — |

## Glossary

From [framework/glossary.md](../../framework/glossary.md): **Composite Score**, **Quality Score**, **Valuation Score**, **Hard disqualifier**, **FCF/NI conversion ratio**, **Owner Earnings**, **MoS (Margin of Safety)**, **Hurdle rate**, **CAGR**, **PEG ratio**, **Forward PE**, **TTM (Trailing Twelve Months)**, **SBC (Stock-Based Compensation)**, **8-K**, **10-K (Annual Report)**, **EDGAR**, **Fiscal Year (FY)**, **Turnover (portfolio turnover)**, **Expectancy** (average win × win rate − average loss × loss rate), **Historical (realized) volatility**.

New terms (not yet in glossary.md — proposed definitions):
- **Backtest** — re-running a rule on past data to see how it would have performed.
- **Point-in-time (PIT)** — using only the information that was publicly available on the date in question.
- **Look-ahead bias** — accidentally using information that was not yet known on the date being tested, which makes results look better than reality.
- **Survivorship bias** — testing only companies that still exist today, which hides the failures.
- **Hit rate / false positive / false negative** — hit rate = share of picks that worked; a false positive is a pick that failed; a false negative is a rejected name that would have worked.
- **Rank-IC (Spearman)** — a −1…+1 number showing how well ranking companies by a score predicts their ranking by later return.
- **Drawdown** — the fall from a peak price to a later low, in percent.
- **Walk-forward calibration** — choosing parameters on an earlier period and testing them on a later one.
- **XBRL `companyfacts`** — the SEC's free data feed of every number in company filings, each tagged with the date it was filed.
- **Knife edge** — a decision that flips on a tiny change (e.g. a score of 79.9 vs 80.0).
