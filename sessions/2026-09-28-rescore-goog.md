# RESCORE — GOOG (Alphabet Inc., Class C) — 2026-09-28

**Task type:** RESCORE (mode `--both`)
**Date:** 28 Sep 2026
**Trigger:** Routine quarterly-cadence check-in (last review 22 Jul 2026, next review trigger flagged as Alphabet's Q3 FY2026 earnings, "expected late October 2026" — **not yet released as of this session**, confirmed via WebSearch: no Q3 2026 8-K/earnings release found). This is therefore **not** a fresh-earnings Rule 9 trigger — it is a scheduled quarterly re-score run ahead of that release, refreshing live price and the macro (10Y Treasury) inputs. One genuine Rule 9 item **was** found and incorporated: Alphabet's **FY2026 CapEx guidance was raised to $195–205B** (from $180–190B) on the 22 Jul 2026 earnings call — that call's forward commentary happened *after* the 07-22 session's data pull (which explicitly flagged "not available in time for this pull"), so this is new, previously-uncaptured guidance information, incorporated qualitatively below (Rule 9 guidance-revision trigger).
**10Y US Treasury Yield:** **5.21%** (TradingEconomics/aggregated news reads for 28 Sep 2026, describing a "near 20-year high" amid a bond-market selloff; FRED's own official `DGS10` series lags to 2026-09-24's 5.18% print, consistent with the reported short uptrend). Used 5.21% as the working figure, consistent with this framework's established practice of using the freshest available read when the official series lags (same treatment as the 07-22 GOOG session).
**Rate Regime Modifier (Step 2):** **+10** (10Y now in the **>5% bracket** — a new, higher bracket than every prior GOOG session, which sat in the 3.5–5% (+5) bracket. This is the single largest driver of this session's score change — see §4/§5.)
**Current GOOG position:** 1 share, IBKR, 0.57% of portfolio (per `holdings.md`), avg cost $295.70
**Sector:** Communication Services — Internet, Search & Digital Advertising / Cloud
**Last review:** 22 Jul 2026 (Valuation Score 64.2, Quality Score 71.4 — fails 80.0+ gate, Composite 46.4 shown for transparency only, action HOLD).

*Plain-English note: GOOG = Alphabet's Class C share (no voting rights); GOOGL = Class A (voting). The economics are identical share-for-share and this framework treats them interchangeably for scoring.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$339.25** | WebFetch of stockanalysis.com's live GOOG quote page, timestamped "September 28, 2026, 4:00 PM EDT" (regular-session close) — down $1.83 (−0.54%) on the day. Cross-checked against an independent WebSearch aggregation (Investing.com/CNN/Yahoo-sourced), which separately reported $337.76 as an intraday read earlier the same session — the two are consistent with normal intraday drift (both within the day's $336.60–$340.11 range cited across sources) and the closing print is used per Rule 0 discipline (freshest, most complete read). ⚠️ IBKR was not reachable in this session (no broker MCP tool available in this run) — WebFetch/WebSearch-sourced live quotes are used instead, same fallback basis as sessions run without broker access. |
| Previous close | $341.08 | stockanalysis.com |
| Day's range | $336.70 – $340.03 | stockanalysis.com |
| 52-week range | $236.69 – $404.47 | stockanalysis.com (widened vs. 07-22's $188.27–$404.47 low end — the 52-week window has rolled forward past last year's lower prices) |
| Analyst consensus PT | Mean $422.34 (range $340–$475, "Strong Buy") | stockanalysis.com — modestly lower than 07-22's pre-earnings-vintage $430.07 mean, now fully post-Q2-earnings vintage |
| Forward PE (vendor, live) | 24.57× | stockanalysis.com — used directly in §5 (post-earnings-vintage, not the pre-earnings-vintage figure flagged as a caveat in 07-22) |
| Shares outstanding | 12.23B (total, Class A+B+C) | stockanalysis.com — consistent with the 07-22 session's balance-sheet-derived 12,230M; no new quarterly filing has changed this figure (Q3 2026 not yet reported) |

---

## 2. What's Changed Since the Last Session (22 Jul 2026) — Data-Gap Discipline

**No new quarterly filing exists.** Alphabet's Q3 FY2026 earnings, expected "late October 2026" per the 07-22 session's own flag, have **not** been released as of 28 Sep 2026 (confirmed via WebSearch — no Q3 2026 8-K/press release found; all sources reference the 22 Jul 2026 Q2 release as the latest). Per quality-scoring.md's rolling-window clarification, the "most recently completed fiscal years/quarters available at the time of scoring" for the TTM window is therefore still **Q3 2025–Q2 2026**, unchanged from the 07-22 session. **Accordingly, every TTM financial-statement figure feeding the Quality Score (Profitability, Margins, Balance Sheet, FCF Quality sub-scores; Net Debt/EBITDA; the fcf_ni_annual_pct hard-disqualifier series) is carried forward unchanged from the 07-22 session** — recomputing them from scratch against the same underlying filings would not change any figure, and this framework does not invent a new quarter's data that doesn't exist. This is disclosed explicitly here rather than silently reused.

**What genuinely is fresh this session:**
1. **Live price** ($339.25 vs. $342.61) — Rule 0, fetched fresh.
2. **10Y Treasury yield** (5.21% vs. 4.65%) — a large, real move (bond-market selloff to a near-20-year high), fetched fresh.
3. **Forward PE / forward EPS consensus** (24.57× / implied $13.807 EPS vs. 23.35× / $14.674 EPS) — this is a genuine, material finding: **sell-side forward EPS estimates have fallen ~5.9%** since 07-22, despite the live price being only modestly lower. This is consistent with, and plausibly explained by, item 4 below (higher disclosed CapEx eating into near-term forward-earnings models) — flagged as a real, sourced data point, not invented.
4. **CapEx guidance raised to $195–205B for FY2026** (from $180–190B), disclosed on the 22 Jul 2026 earnings call itself (after the 07-22 session's data cutoff) — per CNBC/company-sourced reporting. This is the "not available in time for this pull" item the 07-22 session explicitly flagged as a follow-up; it is now incorporated qualitatively (informing the bear-case caution on near-term margin/FCF pressure) though it does not change any TTM figure already on file (CapEx guidance is forward-looking, not a completed-quarter actual).
5. **Gemini 3.5 Pro remains unreleased and has now missed a third target date** (June, mid-July, early August all missed, per WebSearch as of 23 Aug 2026) — the competitive/execution-risk thread flagged in the 07-16 session has **not** resolved; if anything it has worsened. No credible evidence found this session that this delay has translated into actual consumer search/ad-share loss (Search revenue still grew, per Q2's own report), consistent with the 07-22 session's read.
6. **Search market share**: StatCounter reads 91.02% (Aug 2026), essentially flat vs. 07-22's 91.25% (June 2026) figure and still within the stable 89.3–91.6% band held since Jan 2024 — reaffirms, doesn't change, the Moat Signal finding.
7. **Buybacks**: multiple secondary sources (Yahoo Finance, Benzinga) describe Q3 2026 buybacks as continuing at $0, extending the pause. **This is flagged as unconfirmed by primary filing** — Alphabet's Q3 2026 10-Q/8-K has not yet been published, so this cannot be treated as a disclosed fact the way the Q1/Q2 $0 buyback figures were (those came directly from filed cash-flow statements). Per "never invent or estimate," the TTM buyback-yield figure used in §6 is **carried forward unchanged from the last confirmed complete TTM window (Q3'25–Q2'26)** rather than assuming the secondary-source claim is correct.

No metric below was invented or estimated; anything not independently re-verifiable this session (dividend continuation, buyback pattern beyond the last filed quarter) is explicitly flagged as carried-forward, not silently assumed unchanged.

---

## 3. Quality Score (Phase 01 gate) — TTM basis unchanged, evidence citations refreshed

**Hard disqualifier check** (per quality_score.py's actual implementation — evaluated on the annual `fcf_ni_annual_pct` series, oldest-first, not the TTM figure):

```
fcf_ni_annual_pct (oldest first, from yfinance annual filings, unchanged since no new FY has closed) = [100.1%, 94.2%, 72.7%, 55.4%]
Two most recent consecutive years: FY(n-1)=72.7% (>=70, passes), FY(n)=55.4% (<70)
No 2 CONSECUTIVE years both <70% -> hard disqualifier does NOT fire (cleanly, no carve-out needed)
```
```
Net Debt/EBITDA = -0.76x (net cash) -> well under the 2.5x threshold -> PASS
FCF positive 3+ consecutive years = True (FY2023-2025 all positive, TTM $53,273M still positive) -> PASS
```
No hard disqualifier triggers. Proceeding to the weighted score.

**Script run** (`python -m scripts.scoring.quality_score --input goog_quality.json`), full output pasted verbatim:

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((31.04/30)x100) = 100.00
ROIC_Component = clamp((27.51/30)x100) = 91.70
Profitability_Score = (100.00 + 91.70) / 2 = 95.85

**Margins (15%)**
GrossMargin_Score = clamp((60.9/80)x100) = 76.12

**Growth (20%)**
Growth_Score = clamp((12.51/25)x100) = 50.04
+10 TAM/pricing-power evidence: Google Cloud revenue +82% YoY in Q2 2026 (Alphabet 8-K Exhibit 99.1, 22 Jul 2026),
  reaffirmed by Sept 2026 aggregator reporting (Cloud still expanding fastest of the three hyperscalers, no
  contrary evidence found); StatCounter global search-referral share 91.02% (Aug 2026), stable within the
  89.3-91.6% band held since Jan 2024; ~90% of Fortune 100 using Gemini Enterprise per Alphabet's Q2 2026 release
Growth_Score (final, clamped) = 60.04

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - -0.76/4)) = 100.00

**Moat Signal (15%)**
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | StatCounter: 91.02% (Aug 2026), stable 89.3-91.6% band since Jan 2024, flat vs June 2026's 91.25% |
| brand_premium | False | (no pricing-power-without-volume-loss evidence located, unchanged gap) |
| network_effect | True | YouTube + Search two-sided network-effect mechanism, unchanged |
| switching_costs | True | ~90% of Fortune 100 using Gemini Enterprise per Alphabet's Q2 2026 8-K Exhibit 99.1 |
| scale_cost_advantage | False | (no cost-per-unit comparison vs. smaller competitors located, unchanged gap) |
Moat_Score = (3/5) x 100 = 60.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((0.3849 - 0.40)/0.60)x100) = 0.00

**Quality Score — Final**
Quality Score = (95.85x0.25) + (76.12x0.15) + (60.04x0.20) + (100.00x0.15) + (60.00x0.15) + (0.00x0.10)
= 71.389 -> rounds to 71.4

# Quality Score = 71.4 — FAILS the 80.0+ gate
```

**Quality Score = 71.4 — unchanged from 22 Jul 2026**, exactly as expected given the identical underlying TTM inputs (no new quarter reported). **Phase 04 Quality Watch escalation continues** (now the third consecutive full-detail session, and fourth overall, at or below the gate; unchanged this round rather than worsening). The still-dominant drag remains the FCF Quality sub-score's 0.0 floor (record Q2 CapEx) and the Growth sub-score (50.04 base, capped by the framework's CAGR formula despite a 24% YoY headline growth rate that the formula doesn't directly credit).

**Robustness check (carried forward, unchanged basis):** even a hypothetical all-5-TRUE Moat_Score (100.0) would only lift the total to ~77.4 — still below the 80.0 gate. The gate failure remains driven by Profitability/FCF-Quality, not a knife-edge Moat judgment call.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 24.57x
EY = 1/24.57 x 100 = 4.0700%
Spread = EY - 10Y (5.21%) = -1.1400pp -> fails (<1.5pp) -> +5
```

**Step 2 — Rate Regime Modifier**
```
10Y = 5.21% -> >5% bracket -> +10   (up from +5 in every prior GOOG session, which sat in the 3.5-5% bracket)
```

**Combined Rate Modifier: +15** — the single largest driver of this session's score change vs. 07-22's +10. This reflects a real, independently-verified macro move (10Y Treasury spiking to a near-20-year high amid a bond-market selloff, per multiple news sources), not a GOOG-specific fundamental event — consistent with how the Rate Environment Gate is designed to work (a market-wide input, applied uniformly).

---

## 5. Valuation Score (Phase 02)

### Market Cap / EV (computed independently from live price + last-confirmed balance sheet — Rule 0/Rule 6 discipline, same as every prior GOOG session)

```
Market Cap = $339.25 x 12,230M shares = $4,149,027.5M
EV = Market Cap $4,149,027.5M + Preferred stock $19,000M (unchanged carrying value, no new quarter)
     + Total Debt $98,165M (unchanged) - Cash+STI $242,474M (unchanged)
   = $4,023,718.5M
```
Preferred stock, Total Debt, and Cash+STI are all carried forward from the last confirmed balance sheet (30 Jun 2026, per the 07-22 session) since no newer balance sheet exists (Q3 2026 not yet filed) — flagged explicitly, not silently assumed.

### FCF Yield (40% weight) — Owner Earnings adjustment (Upgrade 1, unchanged applicability: growth CapEx still ~81% of total, comfortably over the 30% threshold)
```
Owner Earnings (TTM, normalized, unchanged) = $138,405M
FCF_Yield_pct = 138,405 / 4,149,027.5 x 100 = 3.3357%
```

### EV/EBIT (25% weight, redistributed to 40% — PEG note below)
```
EBIT TTM (unchanged, normalized) = $164,011M
EV/EBIT = 4,023,718.5 / 164,011 = 24.5333x
```

### Forward PE + Historical PE Modifier (20% weight)

**5yr PE range**: carried forward unchanged from the 07-22 session (17.42x low / 23.92x avg / 31.27x high, n=20 quarters). This range is a function of historical quarterly (price, TTM-EPS) pairs; since no new quarter's EPS has been reported since Q2 2026, the same rolling 20-quarter window applies unchanged — flagged explicitly as reused, not re-derived. (`fetch_fundamentals`'s own auto-reconstructed range — 24.738/18.181/35.452 — was **not** used: per every prior GOOG session's disclosed finding, that tool pairs raw, un-normalized quarterly `Reported EPS` into its rolling TTM-EPS series, and Q1/Q2 2026's raw EPS are massively inflated by the $36.9B/$98.0B one-off equity-security gains — the same distortion that forces the manual Rule-6-normalized reconstruction in every session since 07-04. Using the auto-fetched range uncorrected would materially understate GOOG's true historical PE band for those two quarters.)

Forward PE (post-earnings-vintage consensus, fresh) = 24.57x, implied forward EPS = $339.25/24.57 = $13.807 (vs. 07-22's $14.674 — consensus forward EPS has fallen ~5.9% since last session, see §2 item 3).

```
FwdPE_Score (raw) = clamp((24.57 - 17.42)/(31.27 - 17.42) x 100) = 51.625
Deviation vs 5yr avg (23.92) = (24.57 - 23.92)/23.92 x 100 = +2.717% -> within +-10% -> Historical PE Modifier = 0
FwdPE_Score = clamp(51.625 + 0) = 51.625
```

### PEG (15% weight) — still not scored, redistributed to EV/EBIT

Same methodology call as every session since 07-22: the specific growth-rate inputs feeding a PEG ratio (Yahoo `pegRatio`, `earningsGrowth`, `earningsTrend`) remain distorted by Q1/Q2 2026's one-off equity-security gains, which have not yet rolled off the trailing/consensus windows (Q1 2026's gain rolls off at the Q1 2027 mark). No new evidence found this session that sell-side models have re-based. PEG's 15% weight continues to redistribute to EV/EBIT (25%→40%), per valuation-scoring.md's documented escape hatch.

### Script run (`python -m scripts.scoring.valuation_score --input goog_valuation.json`), full output pasted verbatim:

```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 3.3357/10)) = 66.643

**EV/EBIT**
EV/EBIT_Score = clamp((24.5333 - 12)/23 x 100) = 54.493

**Forward PE**
FwdPE_Score (raw) = clamp((24.57 - 17.42)/(31.27 - 17.42) x 100) = 51.625
Deviation vs 5yr avg (23.92) = (24.57 - 23.92)/23.92 x 100 = 2.717%
Historical PE Modifier: within +-10% of 5yr avg -> 0
FwdPE_Score = clamp(51.625 + 0) = 51.625

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/24.57 x 100 = 4.0700%
Spread = EY - 10Y (5.21%) = -1.1400pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.21% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x413.658 + 0.50x330.263 + 0.25x247.0 = 330.2960
Gap Upside % = (330.2960/339.25) - 1 = -2.6394%
Annualized gap = -2.6394% / 2.0yr = -1.3197%/yr
E = -1.3197 (annualized gap) + 12.0 (intrinsic growth) + 0.6744 (shareholder yield: 0.2594 div + 0.415 buyback) = 11.3547%/yr
E (11.3547%) >= H (10.0%) -> M = -15 x clamp((11.3547-10.0)/15, 0, 1) = -1.3547
Upside/Downside Modifier (bounded [-15, +15]) = -1.3547

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 58.779

**Final Valuation Score**
Final Score = Raw (58.779) + Rate Modifier (+15) + Upside/Downside Modifier (-1.355)
= 72.424 -> rounds to 72.4

# Valuation Score = 72.4
```

### Upside/Downside Modifier scenario detail (Rule 7/Rule 10 discipline)

| Scenario | Wt | Assumption | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | AI monetization continues to prove out (Cloud +82% YoY, ~90% Fortune-100 Gemini Enterprise adoption remain the concrete supporting evidence; held at the same conservative assumption level as 07-22 per Rule 7 discipline against over-reacting to one quarter) | $13.807 x 1.07 = $14.774 | 28.0x | **$413.66** |
| Base | 50% | Fresh, post-earnings-vintage consensus forward EPS x own 5yr avg PE (23.92x) | $13.807 | 23.92x | **$330.26** |
| Bear | 25% | AI-search/Gemini competitive-disruption risk (now a third missed Gemini 3.5 Pro launch target, per §2 item 5) — held at the same level as prior sessions, no new consumer-search-share-loss evidence found | $13.00 | 19.0x | **$247.00** |

**Material finding, flagged:** the Base-case fair value ($330.26) now sits **below** the live price ($339.25) — a reversal from every prior session, where Base FV sat above or essentially at price. This is driven entirely by the ~5.9% decline in consensus forward EPS (§2 item 3), not by any multiple change (5yr avg PE is unchanged). Plausibly connected to the raised CapEx guidance (§2 item 4) weighing on near-term forward-earnings models, though this framework does not assert that causal link as fact — only the EPS decline itself is a sourced data point.

Catalyst window held at 2 years (same catalysts as every prior session: AI monetization proof-points, sustained Cloud profitability, demonstrated defense of core search/ad share — still within the 18-24mo guardrail).

---

## 6. Final Valuation Score

**Valuation Score = 72.4** — a material move from 64.2 (22 Jul 2026), **crossing from the 50.0-69.9 "Fair Value/Hold" band into the 70.0-79.9 "TRIM 25-30%" band** for the first time since 20 Jun 2026. Decomposition of the move:

```
Rate Modifier:              +10 -> +15   (contributes +5.0 to the score, on its own more than the entire move)
Raw weighted score:         57.58 -> 58.78  (contributes +1.2 -- essentially flat; EV/EBIT and FwdPE sub-scores
                                              moved in offsetting directions as price fell modestly and the
                                              PE range/consensus EPS both shifted)
Upside/Downside Modifier:   -3.33 -> -1.35  (contributes +2.0 -- a smaller rescue, driven by the Base FV
                                              dropping below live price per the EPS-estimate decline above)
Net change: +64.2 -> +72.4 (+8.2), of which the Rate Regime Modifier bracket shift alone accounts for ~+5.0
of the +8.2 -- the dominant driver this session, not a GOOG-specific fundamental deterioration.
```

**This is a documented, quantified trigger** (a valuation-score band change, per this framework's "act only on documented triggers" rule) — not an action taken on price movement alone. The proximate cause (a market-wide 10Y Treasury spike) is itself the kind of Rule 9 "macro shift (central bank policy... shock)" event this framework is built to react to via the Rate Environment Gate, exactly as designed.

---

## 7. Composite Score — NOT COMPUTED (Quality Score fails the 80.0+ gate)

Per quality-scoring.md/valuation-scoring.md: **"A company only reaches this step after clearing the 80.0+ Quality Score gate... Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate."** GOOG's Quality Score (71.4) fails that gate (§3). **No Composite Score is computed or reported this session** — `scripts.scoring.composite_score` was deliberately **not run**, consistent with the script's own refusal behavior and this framework's explicit non-negotiable (this repo has recently found two prior sessions, AMZN and CSGP, that incorrectly computed a Composite Score despite a failed gate; this session does not repeat that error).

The **action recommendation below is therefore based on the raw Valuation Score (72.4) directly**, exactly as every prior GOOG session (07-04 through 07-22) has done, since no Composite Score has ever existed for GOOG.

---

## 8. Action Recommendation

**Net Action: TRIM 25–30% — but flagged DE MINIMIS / NOT PRACTICALLY EXECUTABLE at current position size.**

**Why TRIM:** Valuation Score (72.4) falls in the **70.0–79.9 band → "TRIM 25–30%"** per the current Action Table (fair-value-methodology.md / operating-brief.md) — a genuine band change from the 50.0–69.9 "Hold" band occupied in the three prior sessions (07-04, 07-16, 07-22). This is a documented score-change trigger, not a price-movement-alone call (§6).

**Why the position is not actually adjusted this session:** GOOG is currently a **1-share position (0.57% of portfolio)**. A 25–30% trim of 1 share is not a practically executable fractional-share order in this framework's IBKR-based execution model (consistent with the 06-20 session's "tiny position — trim de-minimis" treatment the last time GOOG was in a nominal trim band). No sell order is placed or recommended this session; this is flagged for the orchestrator/human investor's manual judgment (e.g. whether to round down to a full exit, given the position's minimal weight, or to simply note the trim signal and hold given the de-minimis dollar amount involved either way).

**No order-setup script output**: `scripts.scoring.order_setup` was run and **confirmed its own refusal** for this score: `# No order setup: Score 72.4 is in the 70.0-100.0 'Trim or exit' band — no order setup, see trim/exit protocol` — consistent with fair-value-methodology.md's Buy Price/Sell Target/Stop Loss framework, which is specifically a **buy-side** setup (0.0–49.9 score bands with a defined Margin of Safety); it has no defined sell-order mechanics for a TRIM band, by design.

**Did a Full Exit trigger fire?** No. None of the four Full Exit triggers are close to tripping:
- **Fundamental deterioration**: not evidenced — no new quarter reported since Q2 2026's clean, undistorted operating results (30% YoY EBIT growth, margin expansion); ROIC remains high in absolute terms.
- **Growth thesis broken**: not evidenced — Search share stable (91.02%), Cloud growth still strong per last confirmed quarter, no credible evidence of AI-driven consumer-search-share loss despite the ongoing Gemini 3.5 Pro delay.
- **Balance sheet crisis**: not evidenced — deep net cash position, unchanged since Q2.
- **Score 90.0–100.0 sustained 2+ quarters**: not applicable — score is 72.4, well below that band.

**Phase 04 Quality Watch escalation: continues, unchanged this session** (Quality Score flat at 71.4, still failing the gate, for the fourth consecutive/third full-detail session).

**Caveat on the trigger's nature:** this TRIM signal is driven overwhelmingly by a market-wide 10Y Treasury spike (Rate Regime Modifier +10→+15 alone accounts for more than half the score's +8.2pp move), not by a GOOG-specific deterioration. The framework's Rate Environment Gate is explicitly designed to react this way to macro-rate shocks (higher rates compress the fair multiple of every long-duration cash-flow stream, GOOG included) — this is the mechanism working as intended, not a false signal, but it is worth the human investor's attention that this is a **rates story, not a company story**, when deciding how (or whether) to act on a 1-share position.

---

## 9. Next Review Trigger

**Date/event:** Alphabet's Q3 FY2026 earnings release — still expected "late October 2026" per the 07-22 session's estimate, not yet confirmed with a specific date; standard re-score within 3 business days of release per the operating calendar.

**Earlier trigger on:** a >15% unexplained price move (Rule 9); the 10Y Treasury materially reversing (bracket change back below 5%, which alone would remove +5 of this session's Rate Modifier); official confirmation (via Q3 filing) of whether buybacks actually stayed at $0 through Q3 (§2 item 7, currently unconfirmed); or credible evidence the Gemini 3.5 Pro delay (§2 item 5, now three missed targets) is translating into actual consumer search/ad-share loss.

**Specifically flag for the next session:**
1. **Confirm Q3 2026 buyback activity** via the actual 10-Q/8-K once filed — the $0 figure used in this session's shareholder-yield calc is carried forward from the last *confirmed* (Q2 2026) quarter, not independently verified for Q3.
2. **Re-verify the PEG redistribution call** once Q1 2026's one-off gain rolls out of the trailing window (Q1 2027) or sell-side consensus re-bases.
3. **Watch whether the ~5.9% forward-EPS-estimate decline (§2 item 3) is a durable re-rating of AI-capex-related margin pressure or a transient estimate-revision artifact** — worth a direct check once analysts have more data points post the raised CapEx guidance.
4. **Watch the 10Y Treasury regime** specifically — given how much of this session's score move traces to the Rate Regime Modifier bracket change, a reversal below 5% would meaningfully pull the score back toward the Hold band even with no GOOG-specific change.
5. **Revisit the de-minimis 1-share position** — given the recurring pattern of this position generating nominal TRIM signals that aren't practically actionable, worth a standalone decision (outside this rescore) on whether to round the position to zero or top up to a size where the framework's trim/hold signals are actionable.

---

## Glossary

- **8-K**: The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish (via an attached exhibit, typically "Exhibit 99.1") a quarterly earnings press release ahead of the fuller, audited 10-Q/10-K that follows weeks later.
- **ATM Program (At-the-Market Offering Program)**: A facility letting a company sell newly issued shares directly into the open market over time through a sales agent, rather than in one bulk-priced offering.
- **bps (basis points) / pp (percentage points)**: bps: 1 bps = 0.01 percentage points, 50 bps = 0.5%. pp: the plain unit a percentage or rate moved by (e.g. a spread moving from 4.0% to 5.5% moved "1.5pp"), distinct from a percent change of the underlying number.
- **Buyback yield (net buyback yield)**: The rate at which a company's share count shrinks per year from repurchasing its own stock, net of new issuance — a component of shareholder yield.
- **CAGR**: Compound Annual Growth Rate.
- **CapEx**: Capital Expenditure.
- **Catalyst window**: The timeframe within which a documented event is expected to close the price/fair-value gap.
- **Composite Score**: This framework's blended 0.0–100.0 ranking number — 0.50 × (100 − Quality Score) + 0.50 × Valuation Score — computed only after a company clears the 80.0+ Quality Score gate. Not computed this session (GOOG fails the gate).
- **D&A**: Depreciation & Amortization.
- **EBIT**: Earnings Before Interest and Taxes — operating profit.
- **EBITDA**: Earnings Before Interest, Taxes, Depreciation, and Amortization.
- **EPS**: Earnings Per Share.
- **EV**: Enterprise Value — market cap + debt − cash.
- **EV/EBIT**: Enterprise Value divided by EBIT — a valuation multiple independent of capital structure.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against bond yields in the Rate Environment Gate.
- **Fast Grower**: EPS growth >15%/yr for 3+ years — this framework's PEG-sub-score trigger.
- **FCF (Free Cash Flow)**: Cash generated after running and maintaining the business.
- **FCF Yield**: FCF ÷ Market Cap (or EV) — higher is cheaper.
- **FCF/NI conversion ratio**: FCF ÷ Net Income — a cash-quality check.
- **Forward PE**: Price ÷ next-twelve-months expected EPS.
- **FV (Fair Value)**: The analyst's estimate of intrinsic worth, independent of market price.
- **GAAP**: Generally Accepted Accounting Principles.
- **Gross Margin**: Gross Profit ÷ Revenue.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score, subject to specific documented carve-outs.
- **Hurdle rate**: The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Moat**: A durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Net Debt/EBITDA**: A leverage ratio — this framework's primary balance-sheet-risk gate.
- **Net Margin**: Net Income ÷ Revenue.
- **NI**: Shorthand for Net Income.
- **NOPAT (Net Operating Profit After Tax)**: EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **NTM (Next Twelve Months)**: A forward-looking estimate covering the next twelve months from today.
- **Owner Earnings**: Net Income + D&A − maintenance-only CapEx — used instead of raw FCF for moat-building reinvestors including Alphabet (Hybrid Upgrade 1).
- **PEG ratio**: PE ÷ earnings growth rate.
- **Phase 01–06**: The six sequential stages of this framework.
- **PT (Price Target)**: An analyst's price forecast.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0–100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score.
- **Rate Environment Gate**: The mandatory pre-score check comparing Earnings Yield against the 10-Year Treasury.
- **Rate Regime Modifier**: The additive score adjustment (−10 to +10) resulting from that check's Step 2, based on the current Treasury-yield bracket.
- **ROIC**: Return on Invested Capital.
- **Rule 0**: This framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 6**: This framework's "normalize before you value" standing instruction — strip out one-time items and cycle-normalize before valuing a business.
- **Rule 9**: This framework's list of fundamental events (earnings, guidance revision, management change, M&A, macro shift, >15% unexplained price move) that force an immediate re-valuation.
- **Rule 10**: This framework's "separate intrinsic value from market price" instruction — document the gap's cause, assign a catalyst/timeline, and track accuracy over time.
- **TAC (Traffic Acquisition Costs)**: Payments Alphabet makes to distribution partners and network members to be the default search provider or host ads.
- **TAM**: Total Addressable Market.
- **TTM (Trailing Twelve Months)**: The most recent four reported quarters combined.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive ±15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0–100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
