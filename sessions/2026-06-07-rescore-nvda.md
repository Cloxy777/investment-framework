# RESCORE — NVDA — 2026-06-07

**Task type:** RESCORE
**Date:** 07 Jun 2026
**10Y US Treasury Yield:** 4.55% (close, 05 Jun 2026 — TradingEconomics/CNBC aggregation)
**Rate Regime Modifier in effect:** +0.5 (10Y in the 3.5–5% bracket)
**Last review on record:** none — `holdings.md` shows blank Score/Review-Date for NVDA. This is the framework's first live re-score of this name; it establishes the baseline.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$205.10** | Last completed close, Fri 05 Jun 2026 |
| 52-week range | $140.83 – $236.54 | IBKR `get_price_snapshot` (broker-reported `misc-statistics`) |
| Analyst consensus PT | $298.42 (62 analysts, "Strong Buy") | stockanalysis.com via web search |

**How the price was pinned down (worth recording — a near-miss):** IBKR's `get_price_snapshot` returned `last = $218.66` flagged `is_close: true`. Taken at face value, that would have been the live price. But a parallel web search returned $205.10 / $204.04 / "~$216 Wednesday" — three different numbers, the exact ambiguity Rule 0 exists to prevent. I pulled `get_price_history` (1-day bars, last 7 sessions) and that resolved it cleanly:

| Date | Close |
|---|---|
| 2026-06-04 | $218.66 |
| 2026-06-05 | **$205.10** ← most recent completed session |

So the snapshot tool had handed back **the prior session's close**, not the latest one — a one-day-stale "live" price that would have been wrong by ~6.6% had I trusted it directly (the same shape of error as the SPGI lesson, just from a different source). $205.10 is corroborated two independent ways:
1. stockanalysis.com explicitly states "$205.10 as of market close June 5, 2026"
2. Market-cap cross-check: 24.2B shares × $205.10 = $4,963.4B ≈ the independently-reported ~$4.97T market cap for "June 2026" (whereas 24.2B × $218.66 = $5.29B ≈ the *separately reported* "$5.3T as of June 4" — confirming each price belongs to its own date, and that June 5's close is the right "live" figure for today, a Sunday, with markets closed since Friday).

Today (Sun 07 Jun) markets are closed — $205.10 is the most current price available, and it represents a **-6.2% single-day move** from the prior close. Contributing context found via search: NVDA's China AI-chip market share has reportedly collapsed from ~95% to ~8% as Chinese buyers shift to domestic chips (H200 export/adoption issues), plus broad "priced-for-perfection" rotation concerns following the May Q4 FY26 earnings beat. Neither is a >15% move, so Rule 9's automatic re-score trigger isn't tripped by this alone — but it's relevant context for the qualitative read below.

---

## 2. Data Gaps / Variance Flagged

No metric was missing outright, but several had **source disagreement** wide enough to flag explicitly rather than silently pick one:

| Metric | Range found | What I used & why |
|---|---|---|
| 10-yr average PE | 53.3× – 66.6× (macrotrends/fullratio/ycharts disagree) | Midpoint ≈ **60×** — flagged as a range, not a precise figure |
| ROIC | 94% – 152% (gurufocus/financecharts/finbox — different measurement windows) | All land far above the 15% threshold; precise figure doesn't change the qualitative read, so I didn't force a single number |
| EV/EBIT | Not directly published anywhere I could find (everyone quotes EV/EBITDA, ~27.6×–30.2×) | **Derived** from sourced inputs — see §3 — and shown in full rather than substituted with EV/EBITDA |
| PEG | 0.30 (trailing: PE 32.75 ÷ TTM EPS growth 108.9%) vs ≈0.43 (forward: fwd PE ~22.5 ÷ consensus next-FY EPS growth ~52%) | Both fall in the same "<0.8 → −1" bucket, so the modifier is unambiguous even though the headline ratio isn't |
| Fair Value (DCF outputs) | $123.28 (GuruFocus) / $166.09 (AlphaSpread) / $281.94 (cited 8.3% WACC model) — a >2× spread | Used directly (see §6) rather than built from scratch — see note there |

---

## 3. Inputs Collected

**Sector:** Technology / Semiconductors — AI compute & data-center GPUs
**Current portfolio weight:** 5.30% (IBKR-only, 14 sh — per `holdings.md`/`snapshots/ibkr.md`)

| Item | Value | Source |
|---|---|---|
| Revenue (FY2026, ended ~Jan 2026) | $215.9B (+65% YoY) | NVIDIA FY2026 Q4 press release |
| Operating income (EBIT) | $130.4B | NVIDIA FY2026 Q4 press release |
| Net income | $120.1B | NVIDIA FY2026 Q4 press release |
| Free cash flow (FY2026) | $96.6B | NVIDIA CFO commentary / aggregator cross-check |
| Gross margin (GAAP, FY2026) | 71.1% | NVIDIA FY2026 Q4 press release |
| Net margin | 55.6% (= $120.1B ÷ $215.9B — ties to reported) | Calculated from above |
| Net cash / (net debt) | **net cash** of $54.1B (i.e., negative net debt) | Aggregator (financecharts/macrotrends), consistent across sources |
| Shares outstanding | ~24.2B | Google Finance via search |
| Forward PE | ~22.0×–23.0× (used 22.5× midpoint) | gurufocus / stockanalysis |
| 10-yr avg PE | ~53–67× (used 60× midpoint — flagged) | macrotrends / fullratio / ycharts |
| Sector (semiconductor) median forward PE | ~36.06× | gurufocus |
| Revenue CAGR 3yr | ~100% (FY2023 ~$27B → FY2026 $215.9B) | Cross-checked: independently reported "~100.43%" matches my own (215.9/27)^(1/3)−1 ≈ 100% |
| ROIC | ~94%–152% (range — see §2) | gurufocus / financecharts / finbox |
| Net debt/EBITDA | n/a — net **cash** position | derived from net-cash figure above |
| FCF/NI conversion | 80.4% (= $96.6B ÷ $120.1B) | Calculated from above — passes the >70% quality check comfortably |
| 10Y Treasury | 4.55% | TradingEconomics/CNBC |

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 22.5 = 4.44%
Spread = EY − 10Y Treasury = 4.44% − 4.55% = −0.11%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−0.11%, ~1.6 points short).
→ Per the gate's rule, this means *do not open a new position* at current pricing/valuation. NVDA is an existing holding, so this doesn't force an exit — but it confirms that **adding** here would not clear the framework's own bar, which dovetails with the trim signal that follows.

**Step 2 — Rate Regime Modifier**
10Y = 4.55% → falls in the "3.5–5%" bracket → **Modifier = +0.5**

---

## 5. Full Score Calculation

**FCF Yield — 40% weight**
```
FCF Yield = FCF ÷ Market Cap = $96.6B ÷ ($205.10 × 24.2B shares = $4,963.4B) = 1.95%
```
1.95% sits in the "<2%" bucket (sub-score 8–10). It's right at the boundary rather than deep in single-digit-yield territory, so I picked the **low end of that band: sub-score = 8** (the most defensible point — it would take only a hair more FCF or a few % lower price to push this into the "2–4% → 6–7" bucket).
→ Contribution: 8 × 0.40 = **3.20**

**EV/EBIT — 25% weight**
No tracker publishes EV/EBIT for NVDA directly (they all quote EV/EBITDA), so I derived it from sourced inputs and show the full chain:
```
Market Cap = 24.2B sh × $205.10  = $4,963.4B
EV         = Market Cap − Net Cash = $4,963.4B − $54.1B = $4,909.3B
EV/EBIT    = EV ÷ EBIT = $4,909.3B ÷ $130.4B ≈ 37.7×
```
(Sanity check: implies EBITDA ≈ EV ÷ ~28.9x [reported EV/EBITDA] ≈ $169.9B, i.e. D&A ≈ $39.5B — a believable figure for a company capex-investing at NVDA's scale.)
37.7× is in the ">35× → sub-score 10" bucket.
→ Contribution: 10 × 0.25 = **2.50**

**Forward PE + Historical PE Modifier — 20% weight**
- Base score vs. sector: Forward PE ~22.5× sits ~38% *below* the semiconductor sector median (~36.06×) — rated **low** on the 1–10 scale → base sub-score = **2**
- Historical PE Modifier (Upgrade 2): Forward PE 22.5× vs. 10-yr avg ≈ 60× → (22.5 − 60) ÷ 60 = **−62.5%**, comfortably past the ">20% below average → −1" trigger → modifier = **−1**
- Adjusted sub-score = 2 + (−1) = **1** (floor)
→ Contribution: 1 × 0.20 = **0.20**

**PEG Modifier — 15% weight (Fast Grower)**
Fast-Grower test: EPS growth has run ~+145% (FY24→FY25) then ~+65% (FY25→FY26) — comfortably clears ">15% for 3+ years," so the PEG slot applies (no redistribution to EV/EBIT).
PEG ≈ 0.30 (trailing) to 0.43 (forward) → both land in **"<0.8 → −1"**.

> ⚠️ **Methodology note worth a closer look (flagging rather than silently picking):** the formula lists this slot as `PEG_or_fallback × 0.15`, which reads as if it expects a 1–10 sub-score like the other three components — but Upgrade 3's table only defines small *modifier*-style values (−1 / 0 / +0.5 / +1), the same shape as the additive Rate Regime Modifier. I went with the literal modifier value as the weighted input (treating it the same way the Rate Regime Modifier is applied — a small additive nudge), which is the more conservative of the two readings here. I show both below; **they don't change the action band**, but it's worth clarifying which the framework intends so future re-scores are consistent:
> - **Modifier-value reading (used as primary):** contribution = (−1) × 0.15 = **−0.15**
> - **Sub-score reading (alternate):** PEG <0.8 ≈ "very cheap relative to growth" → sub-score ≈ 1 → contribution = 1 × 0.15 = +0.15

**Raw weighted score (primary reading):**
```
= (8 × 0.40) + (10 × 0.25) + (1 × 0.20) + (−1 × 0.15)
= 3.20 + 2.50 + 0.20 − 0.15
= 5.75
```
**+ Rate Regime Modifier (+0.5) = 6.25**

Boundary rule only forces a round-up at exactly X.5 — 6.25 isn't, so standard rounding applies → **Final Score = 6**

*(Cross-check with the alternate PEG reading: 6.05 + 0.5 = 6.55 → rounds to 7. Either way the result lands in the 6–7 band — same action.)*

---

## 6. Final Valuation Score & Action

# Final Score: 6  →  Action: TRIM 25–30% of position

This is a **valuation-multiple-driven** trim signal — EV/EBIT (37.7×) and FCF yield (1.95%) both register at the most "expensive" end of their tables, and the forward-PE-vs-history read says the market is pricing in continued hyper-growth that the historical PE band would call rich. The position is well inside the 8% cap (5.30%), so this is **not** a cap-driven trim — it's the framework's own valuation signal, exactly the kind of documented trigger Rule 11 (act only on documented triggers) requires.

---

## 7. Order Setup — TRIM

**Fair Value (triangulated, Rule 3 — 40% DCF / 60% multiples):**

Building a from-scratch 3-stage DCF here would mean *me* assuming NVDA's multi-year growth fade, margin trajectory and terminal rate — exactly the kind of invented inputs the framework prohibits. Instead I triangulated from **sourced, named third-party model outputs**, which is consistent with "show your sources, don't invent the underlying assumptions":

| Method | Estimates found | Used |
|---|---|---|
| DCF-style (Method A) | $123.28 (GuruFocus FCF-DCF) / $166.09 (AlphaSpread DCF) / $281.94 (cited 8.3%-WACC model) | median ≈ **$166** |
| Multiples-based (Method B) | Analyst consensus PT $298.42 (62 analysts) / GuruFocus GF Value ≈ $297.54–$315.31 (avg ≈ $306) | avg ≈ **$302** |

```
Blended FV = 0.40 × $166 + 0.60 × $302 ≈ $66.40 + $181.20 ≈ $248
```

**Fair value range: ~$166 – $315, base case ≈ $248** (per Rule 10 — a range, not a point estimate).

> **Rule 10 callout — document the gap:** note that the *current* price ($205.10) sits *below* this blended base case, not above it. The trim signal here isn't "price > fair value" — it's "the multiples that define cheap/expensive in this framework (EV/EBIT, FCF yield, fwd-PE-vs-history) are all flashing rich on today's *earnings base*, even though several analyst/model fair-value estimates still see room to the upside." The >2× spread between the DCF-style estimates ($123–$282) is itself informative: it means the bear case (deceleration as the AI-capex cycle matures, China share collapse) and the bull case (continued AI infrastructure dominance) are still wide open, and the market hasn't resolved which one it believes. **Catalyst/timeline for the gap to close:** likely the next 2–4 quarters of data-center revenue trajectory and margin trend will show whether growth is decelerating toward the ~52% forward-EPS-growth consensus or holding near the ~65–100% trailing pace — that's the thing to watch, and a natural re-score trigger in its own right.

- **Sell / Trim Target (= Fair Value baseline):** ≈ **$248**
- **Bull-Case Trim Target** = Bull-case FV ($315, GF Value high end) × 0.90 = **$283.50**
- **Buy Price / Stop Loss / R-R / Position Size:** *not computed* — these are entry-risk concepts (sizing a *new* position's risk against its stop). NVDA is an existing holding being trimmed, not entered; recomputing a "buy price" for it would be both meaningless and exactly the kind of black-box number the framework warns against producing just to fill a template slot.

**Trim execution plan:**

| Item | Value |
|---|---|
| Current position | 14 sh @ $205.10 = $2,871.40 (≈5.30% of portfolio — nowhere near the 8% cap; this is purely valuation-driven) |
| Trim band (Score 6) | 25–30% of position |
| 25% of 14 sh = 3.5 sh · 30% = 4.2 sh | → trim **4 whole shares** (= 28.6% of the position — squarely inside the band) |
| Estimated proceeds | 4 × $205.10 ≈ **$820.40** |
| Resulting position | 10 sh ≈ $2,051.00 (≈3.8% of portfolio) |

**Capital recycling (Phase 05): "Proceeds always reinvested into current Score 1–3 names only."**
🚩 **Cannot identify a destination yet** — every other row in `holdings.md` has a blank Last-Score cell; this is the framework's first live re-score, so there is no Score 1–3 name on record to recycle into. Until further re-scores establish one, proceeds should sit in cash (the existing `CASH (IBKR)` balance) rather than be redeployed on a guess — consistent with "never act without a documented trigger."

---

## 8. Next Review Trigger

Re-score NVDA on **whichever comes first**:
- **Next earnings release** — Q2 FY2027 (NVDA's fiscal year runs Feb–Jan; Q1 FY2027 was already reported in late May 2026 per the 8-K filings found, so Q2 FY2027 should land ~August 2026 — confirm exact date via the weekly earnings-calendar check)
- **Quarterly Rate Environment Gate refresh** — due July 2026 (10Y yield / regime modifier update)
- **Event triggers (Rule 9):** any further >15% move without a fundamental cause (today's −6.2% doesn't qualify, but two or three more sessions like it would), a guidance revision, management change, material M&A, or a credible short-thesis publication — most relevant given the China-share-loss narrative actively in the news cycle right now
