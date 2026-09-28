# RESCORE — AMZN — 2026-09-28

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 28 Sep 2026
**10Y US Treasury Yield:** 5.21% (TradingEconomics, "US 10 Year Note Bond Yield," dated 28 Sep 2026 — "rose to 5.21% ... reaching levels not seen since 2007"; corroborated by a second independent source, CNBC, reporting the same day that the 10-year yield is "at its highest in nearly two decades," and by dshort/Advisor Perspectives' 25 Sep 2026 snapshot showing 5.17–5.18% the prior trading session — all sources agree the print sits solidly above the 5% bracket boundary) — **crosses out of the "3.5–5%" bracket into the ">5%" bracket** (was 4.75% at the 2026-08-01 session).
**Rate Regime Modifier (Step 2, this session):** +10 (was +5 on 2026-08-01 — a real bracket change, not a rounding artifact)
**Trigger:** Orchestrator-directed periodic re-score. No single Rule 9 event this session, but two things surfaced during data collection that independently justify a fresh look: (a) the 10Y Treasury's move from 4.75% → ~5.2% is a genuine **macro shift** (Rule 9's "central bank policy / commodity shock" category — driven by rising inflation expectations and hawkish Fed repricing per multiple news sources), which mechanically changes the Rate Regime Modifier; (b) AMZN's stock price has drifted from $271.58 (31 Jul close) to $246.21 (this session, -9.3%) on a broad multi-week decline (capex/margin-pressure concerns, AI-pricing-competition worries, and the macro rate move) — **not** a single >15% unexplained move, so it is not itself a standalone Rule 9 trigger, but it is fully consistent with (and explained by) the macro shift already noted.
**Last review on record:** AMZN Valuation Score **82.7**, Quality Score 56.7 (fails 80.0+ gate), "Composite Score" 63.0 (see §6 below — this recorded Composite is flagged this session as having been computed in violation of the framework's own documented rule) — HOLD (2026-08-01, [sessions/2026-08-01-rescore-amzn.md](2026-08-01-rescore-amzn.md)). Per `portfolio/holdings.md`'s current row, current weight 4.99%.

> *Jargon decoded on first use, per CLAUDE.md's non-finance-reader rule: full definitions in the Glossary (§10).*

---

## 1. Data Gaps Flagged (before proceeding)

1. **`scripts.fetch_fundamentals` failed with `NaN found in trailing 4 quarters of 'EBIT'`.** Investigated directly: yfinance's `quarterly_financials` for AMZN returns `NaN` across **every** line item (Revenue, EBIT, Net Income, Pretax Income, Tax Provision, Gross Profit) for the most recent quarter-column (2026-06-30, i.e. Q2 FY2026) — a data-availability gap in yfinance's quarterly table, not a genuine "AMZN's last quarter is unknown" fact (Q2 FY2026 was fully reported via 10-Q on 2026-07-31 and used extensively in the 2026-07-31/08-01 sessions, sourced directly from Amazon's own SEC filings). **Resolution used:** since no new quarter has been reported since Q2 FY2026 (Q3 FY2026 earnings confirmed via web search for 29 Oct 2026 — not yet reported), this session carries forward the same SEC-sourced TTM figures the 2026-08-01 session established (10-Q/8-K Ex-99.1 sourced) — exactly the same carry-forward logic that session itself used relative to 2026-07-31. Not a new estimate; the same previously-verified real data, still current because no fresher quarter exists.
2. **5-year historical PE range is now technically computable (20 usable quarters) but visibly distorted — judgment call to still use the no-history fallback.** Reconstructing the trailing PE series (per valuation-scoring.md's documented method) now returns `pe_mode: "range"`, avg 64.5×, but spanning **21.8× to 251.1×** — the 251.1× outlier comes from an April 2023 TTM EPS of just $0.42 (a post-pandemic earnings trough), and the window still includes the volatile 2022 near-loss quarters. A range this wide (11×+ spread) is a textbook case of "GAAP earnings base too distorted to be meaningful" — the explicit no-history-fallback condition valuation-scoring.md names alongside "recent IPO" and "loss-making history." Consistent with every prior AMZN session (06-20 through 08-01) reaching the same no-history conclusion (for a related but not identical reason — those sessions cited FY2022 loss quarters specifically), this session again uses `FwdPE_Score = 50.0` (neutral, flagged) rather than a range visibly contaminated by a near-zero-earnings quarter. Shown as evidence, not asserted: the 24-quarter PE reconstruction (2020-07-30 → 2026-07-30) is available on request.
3. **Forward PE / FY2026 consensus EPS shows wide dispersion across sources.** yfinance's own `info["forwardPE"]` field returned 23.50 then 23.49 on two calls moments apart (implied forward EPS ≈ $10.48, intraday price movement between calls) — used this session as the single, directly-sourced, cross-checkable figure (same field `fetch_fundamentals.py` itself would pull). Other sources diverge sharply: Simply Wall St ≈ $10.71 (roughly consistent with yfinance), but Seeking Alpha/TickFlow ≈ $7.75–$7.76 (a ~35% lower estimate) and the carried-forward 2026-08-01 figure was $8.71. The dispersion likely reflects GAAP-vs-adjusted EPS or differing forward-window conventions across providers, and could not be resolved to a single authoritative consensus this session — flagged explicitly rather than picking a source silently. Directionally immaterial to the Rate Environment Gate's Step 1 result (Earnings Yield fails the +1.5pp spread test under any of these forward-PE estimates).
4. **FCF/NI annual figures re-sourced from yfinance disagree with prior sessions' company-definition figures for FY2025** (9.91% via yfinance's own "Free Cash Flow" field vs. 14.41% cited in the 07-04/07-31/08-01 sessions, which used Amazon's own OCF-minus-net-capex FCF definition). This session keeps the prior sessions' figures (FY2024 64.51%, FY2025 14.41%) for internal consistency with the same FCF definition used throughout this name's TTM figures, rather than mixing in yfinance's differently-defined FCF mid-session — flagged, does not change the hard-disqualifier outcome (both figures are <70% either way).

---

## 2. Rule 9 Trigger Check (2026-08-01 → 2026-09-28)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Q3 FY2026 not yet reported (confirmed via web search: 29 Oct 2026) |
| Guidance revision | No new revision found | FY2026 capex guidance remains ~$220B (unchanged from 07-31/08-01; a "memory-price-driven" cost breakdown reported in September press is additional color on the same already-known $220B figure, not a new guidance number) |
| Material M&A | No new items | OpenAI $50B investment already fully covered (2026-08-01 session) |
| Management change | None found | — |
| **Macro shift** | **YES** | 10Y Treasury 4.75% → ~5.21%, crossing the "3.5–5%" → ">5%" Rate Regime Modifier bracket boundary — driven by rising inflation expectations (University of Michigan survey) and hawkish Fed repricing (multiple news sources, cross-checked) |
| >15% unexplained price move | No | -9.3% over ~2 months (271.58 → 246.21), explained by a combination of the macro rate move, ongoing capex/margin-pressure concerns, and AI-pricing-competition worries — not unexplained, and not a single >15% move |

**Conclusion:** the macro-shift trigger (10Y Treasury bracket change) is real and independently justifies this rescore's Rate Regime Modifier update; combined with this being the routine periodic check-in, the session proceeds on both grounds.

---

## 3. Live Price (Rule 0)

| Source | Value | Timestamp |
|---|---|---|
| stockanalysis.com (direct fetch) | **$246.21** (down $3.46, -1.39%) | 28 Sep 2026, 3:42pm EDT |
| yfinance `t.info` (direct pull, this session) | $246.20 / $246.21 (two calls, seconds apart) | 28 Sep 2026, live session |
| **Live price used this session** | **$246.21** | Two independent sources agree to the cent — Rule 0 satisfied |

(A third source, investing.com, returned a slightly different "previous close" figure of $249.67 in an initial web-search snippet — not used, since it read as a cached/summary value rather than a live tick, and the two directly-fetched sources above agree with each other independently.)

---

## 4. Carried-Forward TTM Figures (unchanged since 2026-08-01 — no new quarter reported)

All figures below are unchanged from the 2026-08-01 session (all originally SEC 10-Q/8-K Ex-99.1 sourced) — reproduced per "no black-box outputs," not re-derived:

| Item | Value |
|---|---|
| TTM Revenue | $775.674B |
| Normalized TTM EBIT (ex-$4.3B Q3'25 FTC-settlement/severance) | $98.022B |
| Normalized TTM Net Income (ex-Anthropic mark-to-market gains, ex-FTC/severance) | $77.107B |
| TTM Operating cash flow | $161.4B |
| TTM net capex | $169.0B |
| TTM FCF (Amazon's own OCF − net capex definition) | −$7.6B |
| TTM D&A | $75.2B |
| Net debt (30 Jun 2026) | $5.9B |
| Total stockholders' equity | $551.6B |
| Shares outstanding (30 Jun 2026 cover-page count) | 10.783B |
| FY2025 effective tax rate | 19.6% |
| Revenue FY2022 → FY2025 | $513.983B → $716.924B (3yr CAGR 11.731%, cross-checked fresh against yfinance annual financials this session — matches) |
| Gross margin, TTM | 50.775% |
| Growth-capex share of TTM net capex | 55.5% ($93.8B of $169.0B) → exceeds the 30% Upgrade 1 trigger, Owner Earnings applies |

---

## 5. AMZN — Quality Score (2026-06-29 methodology; carried-forward inputs, unchanged since 08-01)

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((9.941/30)x100) = 33.14
ROIC_Component = clamp((11.583/30)x100) = 38.61
Profitability_Score = (33.14 + 38.61) / 2 = 35.87

**Margins (15%)**
GrossMargin_Score = clamp((50.775/80)x100) = 63.47

**Growth (20%)**
Growth_Score = clamp((11.731/25)x100) = 46.92
+10 TAM/pricing-power evidence: AWS revenue +36.7% YoY in Q2 FY2026 (accelerating), $364B+ cloud
services backlog, multi-year AI compute contracts with OpenAI/Anthropic (Amazon Q2 2026 8-K Ex-99.1)
Growth_Score (final, clamped) = 56.92

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - 0.0341/4)) = 99.15

**Moat Signal (15%)**
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | False | AWS market share ~28% per Synergy Research, flat/down from ~32% in 2021 |
| brand_premium | True | Prime membership pricing power |
| network_effect | True | Third-party sellers ~60-62% of units sold |
| switching_costs | True | AWS data-egress fee structure creates migration friction |
| scale_cost_advantage | True | Multi-year cost-per-unit efficiency across 1,000+ fulfillment centers |
Moat_Score = (4/5) x 100 = 80.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((-0.0562 - 0.40)/0.60)x100) = 0.00

**Quality Score — Final**
Quality Score = (35.87x0.25) + (63.47x0.15) + (56.92x0.20) + (99.15x0.15) + (80.00x0.15) + (0.00x0.10)
= 56.746 -> rounds to 56.7

# Quality Score = 56.7 — FAILS the 80.0+ gate
```

**Hard disqualifier check:** none fire. FCF/NI <70% for 2 consecutive fiscal years (FY2024 64.51%, FY2025 14.41%) carries the standing, documented growth-capex explanation (55.5% growth-capex share, well above the 30% trigger); Net Debt/EBITDA (0.034×) is trivial; FCF-positive every *completed* fiscal year on record.

**Quality Score = 56.7 — unchanged from 07-31/08-01, still decisively FAILS the 80.0+ gate.** No new quarterly data exists this session to move any sub-score. The Phase 04 Quality Watch (opened 2026-07-04) remains open and unresolved. Next real test: Q3 FY2026 earnings (29 Oct 2026).

---

## 6. AMZN — Phase 02 Valuation Score

**Owner Earnings (Upgrade 1) — unchanged inputs, new price:**
- Growth capex check (unchanged): 55.5% of TTM net capex → Upgrade 1 applies.
- OE = Normalized Net Income $77.107B = **$77.107B** (D&A terms cancel by construction).
- Market Cap = 10.783B shares × **$246.21** = **$2,654.882B**.
- OE yield = $77.107B ÷ $2,654.882B = **2.9044%**.

```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 2.90435/10)) = 70.957

**EV/EBIT (40% — PEG not applicable, 15% redistributed here)**
EV = Market Cap $2,654.882B + Net Debt $5.9B = $2,660.782B
EV/EBIT_Score = clamp((27.1447 - 12)/23 x 100) = 65.847

**Forward PE (20%)**
No 5yr PE history usable (distorted-earnings-base fallback — see Data Gap #2)
-> FwdPE_Score = 50.0 (neutral, flagged)

**PEG**
PEG not applicable (not a Fast Grower — same reasoning as every prior AMZN session: net income
trajectory dominated by one-off Anthropic/OpenAI marks, not a clean 3+yr >15% EPS growth base)
-> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/23.491074 x 100 = 4.2569%
Spread = EY - 10Y (5.21%) = -0.9531pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.21% -> Step 2 bracket modifier = +10   <-- bracket CHANGED this session (was +5 at 4.75%)
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x306.25 + 0.50x256.89 + 0.25x176.17 = 249.0500
  (Same bull/base/bear scenario assumptions as 07-31/08-01 — unchanged EBIT base, unchanged exit
  multiples 27.0x/24.0x/18.0x — since no new fundamental data exists to revise them this session.)
Gap Upside % = (249.0500/246.21) - 1 = 1.1535%
Annualized gap = 1.1535% / 2.0yr = 0.5767%/yr
E = 0.5767 (annualized gap) + 10.0 (intrinsic growth) + 0.0000 (shareholder yield) = 10.5767%/yr
E (10.5767%) >= H (10.0%) -> M = -15 x clamp((10.5767-10.0)/15, 0, 1) = -0.5767
Upside/Downside Modifier (bounded [-15, +15]) = -0.5767

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 64.721

**Final Valuation Score**
Final Score = Raw (64.721) + Rate Modifier (+15) + Upside/Downside Modifier (-0.577)
= 79.144 -> rounds to 79.1

# Valuation Score = 79.1
```

**Why the score moved (78.1 → 82.7 → 79.1 across the last three sessions):** unlike 08-01 (a pure price-rally effect), this session's move is a **tug-of-war between two offsetting forces**: (1) the **price decline** (-9.3%) mechanically makes the FCF-yield and EV/EBIT sub-scores *look cheaper* (raw weighted score fell from 70.66 to 64.72), but (2) the **Rate Regime Modifier jumped +5pp** (from +10 total to +15 total) as the 10Y Treasury crossed the 5% bracket boundary — more than offsetting the cheaper multiples. Net effect: score falls modestly (82.7 → 79.1) despite the stock being meaningfully cheaper in absolute-price terms, because the macro backdrop (higher risk-free rate) has gotten less favorable by a larger margin. **This is exactly the Rate Environment Gate mechanism working as designed** — it is a documented, rule-based trigger (a real 10Y Treasury regime shift), not an invented adjustment or a reaction to price movement alone.

---

## 7. Composite Score — REFUSED, and a flagged inconsistency in prior sessions

```
$ python -m scripts.scoring.composite_score --set quality_score=56.7 --set valuation_score=79.1
# Composite Score REFUSED — Quality Score fails the 80.0+ gate
Quality Score 56.7 < 80.0 — fails the gate, Composite Score is not computed for a company that
hasn't cleared Phase 01
```

**This is the correct, documented behavior — and it exposes a real problem with how the last three AMZN sessions were scored.** `framework/valuation-scoring.md`'s Composite Score section states explicitly: *"A company only reaches this step after clearing the 80.0+ Quality Score gate... Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate."* The 2026-06-29 decision record ([decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md)) says the same. `watchlist/STALE.md`'s own precedent for a *different* ticker (SGE, 2026-08-24) confirms this is applied correctly elsewhere: *"Per quality-scoring.md's strict gate, no Phase 02 valuation score or Composite Score was computed."*

Yet the **2026-07-04, 2026-07-31, and 2026-08-01 AMZN sessions all hand-computed and used a Composite Score** (62.1, 60.7, 63.0 respectively) despite AMZN's Quality Score failing the gate in every one of those sessions (57.6, 56.7, 56.7) — and used that Composite Score, not the raw Valuation Score, to justify the HOLD action recommendation each time. This appears to be a **repeated, undetected departure from the framework's own documented rule** (likely because `composite_score.py`'s strict gate enforcement either post-dates those sessions or those sessions bypassed the script and computed the formula by hand without checking the gate condition first).

**This session does not perpetuate that error.** No Composite Score is computed or reported for AMZN. **Flagged prominently for the orchestrator/user:** this may warrant a `decisions/` entry documenting the correction, and a look at whether any *other* held ticker's session history has the same issue.

---

## 8. AMZN — Action

**No Composite Score exists this session (§7), so the action recommendation is governed by the raw Valuation Score (79.1) directly against the operating-brief.md Action Table** — the same basis the framework used for AMZN before the Composite Score existed (06-07/06-20 sessions), and the only basis actually available when a held position's Quality Score fails the gate.

**Valuation Score 79.1 → Action band: 70.0–79.9 → TRIM 25–30%.**

**This is a material change from the 2026-08-01 session's recorded "HOLD."** Two things are true simultaneously and both need to be said plainly:
1. Under the framework's own documented rule (no Composite when Quality fails the gate), AMZN's action recommendation should arguably have already been governed by the raw Valuation Score at 07-04/07-31/08-01 too — meaning the HOLD calls at 82.7/78.1/73.4-ish raw scores may also have understated the signal at those points (82.7 and 78.1 both sit in "expensive" territory on the raw Action Table as well: 82.7 → TRIM to 50%, 78.1 → TRIM 25-30%).
2. This session's own inputs (price down 9.3%, but Rate Regime Modifier up 5pp) land at 79.1 — just inside the TRIM 25-30% band, one-tenth of a point from the 80.0 "TRIM to 50%" boundary.

**No order setup applies** — `scripts.scoring.order_setup` is designed only for the 0.0–49.9 (BUY) bands and explicitly refuses for a TRIM/EXIT-band score, confirmed this session:
```
$ python -m scripts.scoring.order_setup --set score=79.1 ...
# No order setup: Score 79.1 is in the 70.0-100.0 'Trim or exit' band — no order setup, see
trim/exit protocol
```
This matches `fair-value-methodology.md`'s own design — the Buy/Sell/Stop checklist is a buy-side mechanism; Phase 05 trims are qualitative (reduce position by the stated %, no MoS/stop-loss math). **Practical trim mechanics** (informational, not an order-setup calculation): reduce the AMZN position by 25–30% of its current size — current weight is 4.99% per `portfolio/holdings.md`; exact share count and post-trim target weight are for the orchestrator/broker sync to execute, not computed here (no exact share count/portfolio-value figures were provided to this session). Primary reference price for any trim: PW Fair Value $249.05 (essentially at the current $246.21 live price — the trim signal here is coming from the raw multiples/rate-modifier calculus, not from the stock trading meaningfully above its own probability-weighted fair value estimate; both facts are shown so nothing is hidden).

**Quality Watch (opened 2026-07-04, still open, unresolved as of this session):** Quality Score remains 56.7, decisively below the 80.0+ gate. Per rescore.md, an existing holding failing the quality gate is **not retroactively force-exited on quality alone** — this TRIM recommendation is driven by the Valuation Score/Rate Environment Gate, not by the Quality Score.

---

## 9. Next Review Triggers

- **Next earnings — AMZN Q3 FY2026, 29 Oct 2026** (confirmed via web search) — the next checkpoint for (a) whether TTM FCF conversion recovers or deteriorates further, (b) the first quarter to reflect the $21.3B post-Q2 OpenAI cash outlay on the balance sheet (Net Debt/EBITDA re-check), and (c) whether the Quality Score gate-fail (56.7) improves, worsens, or persists.
- **Phase 04 Quality Watch (carried, unresolved)** — re-verify at Q3 FY2026.
- **Rate Environment Gate** — currently in the ">5%" bracket (+10 Step 2); the next scheduled quarterly Rate Environment Gate update is January 2027 per operating-calendar.md, but any further material 10Y move before then would itself be a documented macro-shift trigger for an ad hoc re-check.
- **Composite Score correction (new, this session)** — flagged for the orchestrator: consider a `decisions/` entry documenting that Composite Score should not have been computed for AMZN while its Quality Score fails the gate (07-04 through 08-01 sessions), and whether other held tickers have the same issue.
- **Rule 9 standing triggers:** guidance revision outside normal cadence, management change, further material M&A, or a >15% unexplained price move.
- **FY2026 consensus EPS dispersion (new, this session)** — worth resolving to a single authoritative source next session; the 7.75–10.71 range across providers is wide enough to be worth a closer look even though it didn't change this session's qualitative conclusions.

---

## 10. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output)

| Term | Meaning |
|---|---|
| **10-Q** | The quarterly financial-disclosure report a US public company files with the SEC between annual 10-Ks, containing unaudited (reviewed) financial statements for the most recent fiscal quarter. |
| **8-K** | The "current report" a US public company must file with the SEC within days of a material event, most commonly to furnish a quarterly earnings press release. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50 — computed only for companies that have cleared the 80.0+ Quality Score gate. |
| **D&A** | Depreciation & Amortization. |
| **Earnings Yield Spread Test** | Step 1 of the Rate Environment Gate: Earnings Yield (1 ÷ Forward PE) minus the 10-Year Treasury yield; a spread below +1.5% adds a +5 flag. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT / EV/EBITDA** | Enterprise Value (market cap + net debt) / EV divided by EBIT or EBITDA. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | A company growing EPS faster than 15%/year for 3+ years — this framework's trigger for the PEG sub-score. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score, absent a documented carve-out. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for AMZN/MSFT/GOOGL/META (Upgrade 1). |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **R/R (Risk/Reward ratio)** | (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
