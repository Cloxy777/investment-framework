# RESCORE — NKE (NIKE, Inc.)

## 1. Session header
- **Task type:** RESCORE (single ticker, full `--both` mode) — post-Q1 FY2027 earnings (reported 2026-10-01)
- **Date:** 2026-10-11
- **10Y US Treasury yield:** 5.22% (FRED `DGS10`, 2026-10-08, latest posted; prior days 5.31 / 5.27 / 5.28)
- **Rate Regime Modifier in effect:** **+10** (10Y now >5%; was +5 at the 2026-09-11 rescore — regime band crossed)
- **Prior score:** Valuation 34.4, Quality 39.5, Composite 47.5 (2026-09-11) — HOLD existing / do NOT add
- **Jargon decode:** see closing Glossary.

## 2. Data gaps flagged
- **5yr historical PE range (18.2× low / 29.5× avg / 40.3× high) carried forward unchanged** — `yfinance` reconstruction still unavailable here; slow-moving statistic, flagged for recompute.
- **Consensus FY2027 EPS $1.32** (stockanalysis.com, 39–42 analysts, high $1.69 / low $1.01) — some analysts likely have not yet updated for the 2026-10-01 guide (adjusted EPS $1.15–$1.35), so $1.32 may still be stale-high; flagged. Company guide midpoint is $1.25. The $1.32 consensus basis is **adjusted** EPS (excludes ~$0.15/sh Pace restructuring); GAAP EPS would be lower.
- **FY2028 consensus not available** (paywalled) — not needed by this method.
- Greater China EBIT not disclosed in the company release (one secondary source cites ~$250M; **not used**, unverified).
- No buyback or share-count commentary beyond the 10-Q: Q1 repurchases = $0 (vs $126M a year ago).

## 3. Live data (Rule 0 — fetched first)

| Item | Value | Source |
|---|---|---|
| Live price | **$34.92** | IBKR `get_price_snapshot` (contract 10291, NYSE) — matches the 20-share position mark in the latest IBKR sync |
| Diluted weighted-avg shares (Q1 FY27) | 1,484.2M | 10-Q (acc. 0000320187-26-000193, filed 2026-10-02), income statement |
| Market cap (computed) | $51,828.3M | 1,484.2M × $34.92 |
| Total debt (31 Aug 2026) | $7,893M | 10-Q: current portion $2,000M + long-term $5,893M (no notes-payable line) |
| Cash + short-term investments | $8,368M | 10-Q: $6,903M + $1,465M |
| Enterprise value (computed) | $51,353.3M | Market cap + debt − cash&STI |
| Shareholders' equity | $15,220M | 10-Q balance sheet |
| 10Y Treasury | 5.22% | FRED `DGS10`, 2026-10-08 |

**TTM construction** (FY2026 audited − Q1 FY26 + Q1 FY27), consistent with quality-scoring.md's "TTM" inputs:

| Metric | FY2026 | − Q1 FY26 | + Q1 FY27 | **TTM** |
|---|---|---|---|---|
| Revenue | 46,398 | 11,720 | 11,213 | **45,891** |
| Gross profit | 19,911 | 4,943 | 4,798 | **19,766** (43.07%) |
| Net income | 3,108 | 727 | 712 | **3,093** (6.74%) |
| EBIT (pretax + net interest exp.) | 3,850 | 904 | 907 | **3,853** |
| D&A | 747 | 190 | 193 | **750** |
| OCF | 2,868 | 222 | 135 | **2,781** |
| CapEx | 684 | 207 | 199 | **676** |
| FCF | 2,184 | 15 | −64 | **2,105** |

Q1 FY27 EBIT = pretax $921M + net interest *income* subtracted ($14M) = $907M; Q1 FY26 = $922M − $18M = $904M. Q1 FY26 tax rate 21.1%, Q1 FY27 22.7%.

## 4. Fundamental changes since last review (2026-09-11)
- **Q1 FY2027 (qtr ended 31 Aug 2026), reported 2026-10-01:** revenue $11,213M (−4% reported, −5% currency-neutral) vs $11,720M; gross margin 42.8% (+60bp, logistics/warehousing); SG&A −3%; net income $712M (−2%); diluted EPS $0.48 vs $0.49 — beat on EPS (~$0.43–0.44 expected), slight revenue miss. Sources: [Nike release](https://about.nike.com/newsroom/releases/nike-inc-reports-fiscal-2027-first-quarter-results), [10-Q](https://www.sec.gov/Archives/edgar/data/320187/000032018726000193/R2.htm), [call transcript](https://www.webull.com/news/15677874570593280).
- **Full-year FY2027 guidance (Rule 9 trigger — guidance revision):** revenue to decline **high-single digits**; **adjusted EPS $1.15–$1.35** (excl. ~$0.15 Pace restructuring) vs FY2026 EPS $2.10 → midpoint −40%; EBIT to decline by a greater % than revenue; tax rate mid-20s%. Street had expected ~$1.65–1.69.
- **Greater China:** Q1 revenue $1.18B, **−26%** currency-neutral; guidance assumes China "gets worse" for the rest of FY27; marketplace/digital cleanup "will take multiple seasons"; pressure likely into FY28. Confirms the JPMorgan-flagged headwind (2026-09-11 session) is real and arriving.
- **Converse** $263M, −28%. **NIKE Direct** −8%. **Wholesale** −1%. Performance growing high-single digits.
- **Q2 FY27 headwind:** ~400bp to revenue from lapping EMEA Cyber Week promos and North America sell-in timing.
- **Q1 FCF negative (−$64M); dividends $610M paid vs $135M OCF; buybacks $0.** Dividend run-rate ($1.64/sh ≈ $2.4B) now exceeds TTM FCF ($2.1B) and FY27 EPS guide ($1.15–1.35 adj.) — payout not covered by earnings. Not scored, flagged.
- **Price:** $36.61 → $34.92 (−4.6% since 2026-09-11).

## 5. Rate Environment Gate
- **Step 1 — Earnings Yield Spread:** Forward PE = 34.92 ÷ 1.32 = 26.45×; EY = 3.78%; spread = 3.78% − 5.22% = **−1.44%** < +1.5% → FAIL → **+5**.
- **Step 2 — Rate Regime Modifier:** 10Y 5.22% is **>5%** → **+10** (was +5).
- Combined Rate-Gate additions: **+15** (was +10).

## 6. Quality Score (2026-06-29 methodology)

```
Profitability (25%):
  Net Margin TTM = 3,093/45,891 = 6.74%  → component = (6.74/30)×100 = 22.47
  NOPAT = TTM EBIT 3,853 × (1 − 0.2067) = 3,056.6   (TTM tax rate 20.67%: FY26 pretax ≈ 3,900 [= NI/(1−20.3%)], tax ≈ 792; TTM tax 806 / pretax 3,899)
  Invested Capital = Debt 7,893 + Equity 15,220 = 23,113
  ROIC = 3,056.6 / 23,113 = 13.22%  → component = 44.08
  Profitability_Score = (22.47 + 44.08)/2 = 33.27   (FCF-positive 3 FYs: FY24 6,617 / FY25 3,268 / FY26 2,184 → no cap)

Margins (15%): Gross margin TTM 43.07% → (43.07/80)×100 = 53.84. Trend flat/down (FY24 44.56 → FY25 42.74 → TTM 43.07); bonus applies only <40% anyway → none.

Growth (20%): Revenue 3yr CAGR (FY23→FY26 completed years, unchanged) = −3.24% → 0.0. (−10 structural penalty moot at the floor. Q1 −4%, FY27 guide high-single-digit decline: growth has now turned decidedly negative.)

Balance Sheet (15%): Net debt = 7,893 − 8,368 = −475 (net cash). EBITDA TTM = 3,853 + 750 = 4,603. ND/EBITDA = −0.10× → 100.0 (clamped).
  (Management cites leverage "roughly 2×" — appears lease-adjusted; framework basis excludes leases, consistent with prior sessions. Flag.)

Moat (15%): unchanged checklist — only Scale cost advantage TRUE → 20.0. Reinforcing, unscored: China −26% c-n, Converse −28%, Direct −8%, "multiple seasons" to fix China.

FCF Quality (10%): TTM FCF/NI = 2,105/3,093 = 68.06% → ((0.6806 − 0.40)/0.60)×100 = 46.76
  Hard disqualifier (FCF/NI <70% for 2+ consecutive FYs): FY2025 101.5%, FY2026 70.27% → does NOT fire. TTM is 68.1% (<70%), so a second sub-70% fiscal year (FY2027) would make it two *consecutive* only if FY2026 were also <70%; FY2026 was 70.27% → earliest firing is FY2027+FY2028. Proximity flagged.

Quality Score = 33.27×0.25 + 53.84×0.15 + 0.0×0.20 + 100.0×0.15 + 20.0×0.15 + 46.76×0.10
              = 8.318 + 8.076 + 0 + 15.0 + 3.0 + 4.676 = 39.07 → 39.1
```

**Quality 39.5 → 39.1 — still FAILS the 80.0+ gate** (third consecutive sub-gate score; no hard disqualifier). Marginal decline from TTM FCF/NI slipping 70.3%→68.1% (Q1 FCF −$64M) and ROIC 13.45%→13.22%.

## 7. Phase 02 Valuation Score

```
FCF Yield (40%): TTM FCF 2,105 ÷ Mkt cap 51,828.3 = 4.061% → clamp(100×(1−4.061/10)) = 59.39 ; ×0.40 = 23.754

EV/EBIT (25% + PEG-redistributed 15% = 40%): 51,353.3 ÷ 3,853 = 13.33× → ((13.33−12)/23)×100 = 5.77 ; ×0.40 = 2.310

Forward PE (20%): 34.92 ÷ 1.32 = 26.45×; 5yr range 18.2–40.3 (avg 29.5, carried forward)
  Score = ((26.45−18.2)/(40.3−18.2))×100 = 37.35
  Historical PE Modifier: dev vs avg = (26.45−29.5)/29.5 = −10.3% → not >20% below, so no −10 (the rule defines only >20% / within ±10% / >20% above; the 10–20% gap is unspecified — no interpolation invented, 0 applied; flagged)
  contribution = 37.35 × 0.20 = 7.470

PEG: n/a (not a Fast Grower) → redistributed above.

Raw weighted = 23.754 + 2.310 + 7.470 = 33.534
+ Rate Gate Step 1 (EY spread FAIL)  +5
+ Rate Gate Step 2 (10Y >5%)         +10
= 48.534 (before Upside/Downside Modifier)
```

## 8. Upside/Downside Modifier — full calc

Scenario values re-derived from new information (guidance cut), same method as 2026-09-11:

| Scenario | FV | Assumption |
|---|---|---|
| Bull (25%) | $40 | Prior normalized-EPS assumption ($1.91, 2yr out) scaled by the consensus cut $1.32/$1.71 = 0.772 → ~$1.47 × 27× (unchanged multiple) = $39.8 → $40. *Note: the 2026-09-11 log's $57 bull does not reproduce from its stated inputs ($1.91 × 27 = $51.6); corrected here, not carried forward.* |
| Base (50%) | $29 | FY2027 consensus $1.32 × ~22× (unchanged multiple) = $29.04 |
| Bear (25%) | $24 | Low end of company guidance $1.15 × ~21× (JPMorgan's stated multiple) = $24.15 |

```
PW Fair Value = 0.25×40 + 0.50×29 + 0.25×24 = 10.0 + 14.5 + 6.0 = $30.50   (was $41.50)
Gap Upside % = 30.50/34.92 − 1 = −12.66%
Catalyst window = 2.0 yr (default; none better documented — management says China fix takes "multiple seasons", pressure into FY28)
Annualized gap = −12.66/2 = −6.33%
Intrinsic growth = 0.0%/yr (lowered from +2.0%: FY27 EPS guide is ~−40% vs FY26; no basis for positive underlying growth; disclosed judgment)
Shareholder yield = dividend $1.64 ($0.41×4) ÷ 34.92 = 4.70% + net buyback 0.0% (Q1 repurchases $0; buybacks paused) = 4.70%
E = −6.33 + 0.0 + 4.70 = −1.63%

E < 0 branch: M = +5 + 10 × clamp(1.63/10, 0, 1) = 5 + 1.63 = +6.63
Catalyst guardrail: caps only the upside (negative) side — not binding.
```

## 9. Final valuation score + Composite Score

| | Value |
|---|---|
| Raw weighted | 33.534 |
| Rate Gate (Step 1 + Step 2) | +15 |
| Upside/Downside Modifier | **+6.63** (E = −1.63%, was +13.57%) |
| **FINAL VALUATION SCORE** | **55.2** (was 34.4) — "Fair Value" band |
| **Quality Score** | **39.1** (was 39.5) — FAILS 80.0+ gate |

```
Composite = 0.50×(100 − 39.1) + 0.50×55.2 = 30.45 + 27.60 = 58.05 → exactly .X5 → round UP → 58.1
```

**Composite 58.1** (was 47.5) — reference only; Quality Gate fails. Moved from "Cheap" band into "Fair Value" band (50.0–69.9).

Decomposition of the +20.8 valuation-score jump: Rate regime +5 (10Y crossed 5%), Upside/Downside +10.2 (E fell from +13.57% to −1.63% as PW FV fell $41.50→$30.50, now below the live price), raw weighted score +5.6 (27.9→33.5, mainly Forward PE 14.5→37.4 as the price fell less than EPS estimates).

## 10. Action recommendation — HOLD existing, DO NOT ADD (no trim trigger)

**(a) Quality gate fails** (39.1 vs 80.0), no hard disqualifier.
**(b) Action table:** Composite 58.1 → "Fair Value — Hold, no new entry, no trim." Price is not a trigger; the trigger here is a score change driven by a documented fundamental event (guidance cut) and a rate-regime band change.
**(c) Order setup (turnaround, Rule 8 / Upgrade 4):**

| Field | Value |
|---|---|
| Blended FV (PW) | $30.50 |
| Margin of Safety (turnaround) | 35% |
| Buy price (limit) | **$19.83** |
| Primary sell target | $30.50 |
| Bull-case trim target | $40 |
| Stop (buy × 0.70) | $13.88 |
| R/R at buy | (30.50−19.83)/(19.83−13.88) = **1.79:1 — below 2:1 minimum** |
| R/R at live $34.92 | (30.50−34.92)/(34.92−13.88) = **−0.21:1** (live is *above* PW FV) |

No buy. Live price is above probability-weighted fair value (−12.7%).

**(d) Position / holding facts:** 20 sh, cost $43.31, mark $34.92, −19.4% (−$167.80); ~1.03% of portfolio. IBKR sync shows **no live NKE sell order** (order 1907120519, SELL 20 @ $54.44, is `REPLACED` with no successor) — the old $54.44 target is now far above even the bull FV ($40); if a sell order is restored it should be reset to the new targets ($30.50 primary / $40 bull), not the stale $54.44. Manual TWS check recommended; nothing placed.

**(e) Escalation flags (for user decision, not executed):**
1. **Quality Watch (Phase 04):** third consecutive rescore below gate; guidance now cut ~40% at the EPS midpoint vs FY2026 — Phase 04 guidance-discipline check records a large cut. Not yet the Phase 06 "sustained deterioration" exit bar by the letter, but the case is stronger than at any prior review.
2. **Upgrade 4 Turnaround Sub-Gate formal review + `override-log.md` entry** — recommended since 2026-06-07 and now overdue across **five** rescores. Position is ~1% and is not recorded in the override log.
3. **Dividend coverage:** $1.64/sh dividend vs FY27 adj. EPS guide $1.15–1.35 and TTM FCF/sh ≈ $1.42 — payout exceeds earnings and FCF. A dividend cut would cut shareholder yield (4.70% of the E calc).

**Net: HOLD ~1% position, do NOT add.** Valuation moved from "Cheap" to "Fair Value" because earnings estimates fell faster than price and the stock now trades above PW FV — the earlier "Composite 34.8–47.5 = Cheap" reading was a false green light that has now closed.

## 11. Next review trigger
- **Q2 FY2027 earnings (~late Dec 2026)** — first read on the ~400bp revenue headwind and whether China worsens as guided.
- **China marketplace reset start (Jan 2027)** — Rule 9 trigger; confirm timing.
- Rule 9 standing triggers: further guidance revision, dividend change, management change, >15% unexplained price move.
- 10Y yield: a retreat below 5% restores Rate Regime to +5 (−5 on valuation score) — track.
- Formal Upgrade 4 review + override-log entry (overdue).

## 12. Glossary
- **Adjusted EPS (non-GAAP):** company-defined earnings per share excluding items it labels one-off (here ~$0.15/sh restructuring); GAAP EPS is lower.
- **bp (basis point):** 0.01 percentage point; 60bp = 0.6%.
- **CapEx:** capital expenditure.
- **Composite Score:** framework's blended 0.0–100.0 rank (0.0 = most attractive) of Quality and Valuation, 50/50.
- **Currency-neutral growth:** growth excluding exchange-rate effects.
- **D&A, EBIT, EBITDA, EV, EV/EBIT:** depreciation & amortization; operating profit before interest and taxes (and before D&A for EBITDA); enterprise value (market cap + debt − cash); EV ÷ EBIT.
- **EPS, Forward PE, EY (Earnings Yield):** earnings per share; price ÷ next-year EPS; 1 ÷ Forward PE, compared with the 10Y Treasury.
- **FCF, FCF Yield, FCF/NI conversion:** free cash flow; FCF ÷ market cap; FCF ÷ net income.
- **FV / PW Fair Value:** fair value / probability-weighted (25% bull, 50% base, 25% bear).
- **Hard disqualifier:** one of three Quality conditions that fails a company regardless of score.
- **Hurdle rate:** minimum acceptable annual return (10%).
- **Moat:** durable competitive advantage.
- **MoS (Margin of Safety):** discount to fair value demanded before buying.
- **Net Debt/EBITDA:** leverage ratio; negative = net cash.
- **NOPAT, ROIC:** after-tax operating profit; NOPAT ÷ (debt + equity).
- **Pace (Nike restructuring program):** Nike's multi-year cost-cutting plan (~$1.0B charges, ~$2.5B savings through FY2031).
- **Quality Score / 80.0+ gate:** framework's 0–100 quality grade; 80+ required to reach valuation scoring.
- **Rate Environment Gate / Rate Regime Modifier:** earnings-yield-vs-Treasury check (+5 if spread <1.5%) plus a band-based add-on (+10 when 10Y >5%).
- **R/R:** reward-to-risk ratio; framework requires ≥2:1.
- **Shareholder yield:** dividend yield + net buyback yield.
- **TTM:** trailing twelve months.
- **Turnaround Sub-Gate (Upgrade 4):** path for a company failing some quality tests to enter as a small position if it passes 5 specific tests.
- **Upside/Downside Modifier:** ±15 valuation-score adjustment based on expected annual return E.
