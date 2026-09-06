# RESCORE — TRN (Trainline plc, LSE:TRN) — mode `--both`

**Task type:** RESCORE (routine follow-up on the still-open CMA drip-pricing investigation; no fresh Rule 9 trigger required to re-check a name already under heightened Quality Watch)
**Date:** 2026-08-31
**10Y US Treasury Yield:** **4.72%** (2026-08-31, tradingeconomics.com, corroborated by Bloomberg reporting "Treasury 10-Year Yield Tops 4.75%, Highest Since January 2025" earlier in the week — FRED's CSV endpoint not attempted this session given the same access issue flagged 2026-08-22)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket — unchanged)
**Last review:** 2026-08-22 (Valuation Score 10.0, Quality Score 67.2 — fails 80.0+ gate, Composite 21.4 reference-only; HOLD, do not top up; heightened Quality Watch opened on the CMA news)
**Position status:** Held, 600 shares, unchanged since 2026-06-24 (per 2026-08-30 `/sync-portfolio`, most recent available — not re-run this session); weight 2.59%⚠️ per [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session was triggered

Scheduled follow-up on the 2026-08-22 heightened Quality Watch — the CMA drip-pricing investigation opened 2026-08-19 remains open with no finding yet, and this session checks for developments plus recomputes both scores against fresh data. No independent Rule 9 price-move trigger fired this week (see §1).

---

## 1. Live price (Rule 0 — fetched first)

- **IBKR `get_price_snapshot` (contract_id 371871705):** last **199.1 GBX**, no halt; prior close 202.6, change −1.73% intraday.
- **Price of record for this session: 199.1 GBX = 1.9910 GBP.** Up +0.81% from the 2026-08-22 session's 197.5 GBX — consistent with holdings.md's 2026-08-30 sync note ("£1.975 → £1.991/share (+0.81%)"). Well inside the ±15% Rule 9 threshold — no new unexplained-move trigger.
- **FX rate:** live GBP→USD from IBKR `get_account_balances` (fetched this session) = **1.35423005**. → 199.1 GBX = **$2.6960 USD**.
- **52-week range (IBKR `misc_statistics`):** low **178.00 GBX**, high **304.00 GBX** — confirms the stop calculated in §8 sits below the 52-week low, same structural note as 08-22.

---

## 2. What's new since 2026-08-22

**No resolution of the CMA investigation.** Per GOV.UK's case page and this week's coverage (Cleary Antitrust Watch, Investing.com), the CMA opened its formal investigation into Trainline (alongside parallel probes into Virgin Atlantic and RED Driving School) on 18 August 2026 and remains at the evidence-gathering stage — **no finding of wrongdoing, no fine, no fee-structure change confirmed yet.** Nothing to re-test in the Moat checklist this session beyond what 08-22 already captured.

**New this session — a sell-side reaction that has now caught up with the news:** JPMorgan's TRN price target, cited 08-22 as "Sell rated, 220p" (still above the 190–197.5p trading range at the time, i.e. a stale pre-CMA figure not yet a genuine confirmation of anything), has since been **cut to 185p** (source: stockanalysis.com consensus page, 2026-08-31). 185p now sits **below** the current 199.1p live price — the first analyst target this framework has seen actually price in the CMA overhang rather than lag it. Consensus 12-month target is still reported as ~352p (Strong Buy, 13 analysts) — a wide analyst dispersion, not resolved this session, noted as context only (this framework's own Blended FV, not consensus, drives the score).

**No other Rule 9 trigger found:** no earnings release (next report confirmed **30 Oct 2026**, per stockanalysis.com — consistent with the "~Oct 2026" estimate from 08-22); no CEO/CFO-level change (Ian Brown's handover — effective 7 Sept, full 28 Sept 2026 — remains scheduled, not yet occurred as of today, 31 Aug); no guidance revision; no M&A.

Sources: [GOV.UK CMA case page](https://www.gov.uk/cma-cases/trainline-consumer-protection-enforcement-case), [Cleary Antitrust Watch](https://www.clearyantitrustwatch.com/2026/08/cma-ramps-up-drip-pricing-enforcement-with-investigations-into-trainline-virgin-atlantic-and-red-driving-school/), [stockanalysis.com](https://stockanalysis.com/quote/lon/TRN/).

---

## 3. Data refresh — **yfinance unreachable this session (flagged, not silently worked around)**

`yfinance` (the framework's standard data source for TRN, used in every prior session) failed on every attempt this session — repeated `CurlError`/SSL connection resets against `query2.finance.yahoo.com`, `guce.yahoo.com`, and `fc.yahoo.com` via the environment's outbound proxy (confirmed via `__agentproxy/status`: repeated `ws_closed_mid_exchange` failures, a network-level block in this session's environment, not a data-availability gap). Per "never invent or estimate financial data," the response is to **substitute a cited alternate source and flag the gap explicitly**, not to fabricate figures.

**FY2026 fundamentals — carried forward, cross-checked where possible:** stockanalysis.com (fetched fresh this session) independently confirms **Total Revenue £452.68M** and **Net Income £79.81M** — both match the 07-05/08-22 yfinance-sourced figures to the rounded million, i.e. no new fiscal year has reported (consistent with the confirmed 30 Oct 2026 next-earnings date). The line items not shown on stockanalysis.com's summary view (EBIT, EBITDA, FCF, OCF, Net Debt, Total Debt, Cash, Invested Capital, Total Equity, Gross Margin) are **carried forward unchanged from the 08-22 session's yfinance pull** — cross-checked as internally consistent (Revenue/Net Income match exactly) rather than blindly assumed:

| Field | Value (FY2026, carried forward — cross-checked on Revenue/NI only) |
|---|---|
| Total Revenue | £452,684,000 *(cross-checked: stockanalysis.com shows £452.68M)* |
| Net Income | £79,813,000 *(cross-checked: stockanalysis.com shows £79.81M)* |
| EBIT | £126,429,000 |
| EBITDA | £167,243,000 |
| Free Cash Flow | £79,547,000 |
| Operating Cash Flow | £133,019,000 |
| Net Debt | £167,426,000 |
| Total Debt | £261,946,000 |
| Cash | £59,703,000 |
| Invested Capital | £431,498,000 |
| Total Equity | £204,369,000 |
| Gross Margin | 82.591% |

**Shares outstanding — data-quality flag, resolved with a documented choice:** stockanalysis.com reports **343.82M** shares outstanding (backed out from its stated market cap 684.54M GBP ÷ price 1.991 GBP) vs. the yfinance-sourced **341,488,172** used 08-22 — an *increase* of ~2.33M shares over 9 days, which runs counter to the ongoing buyback program (share count fell each of the two prior sessions). This is very unlikely to be a real share issuance in 9 days; most plausibly a less-frequently-updated field on the substitute source. **Used anyway, not overridden**, per this session's sourcing discipline (use the number the cited live source actually reports, flag the anomaly, don't silently substitute a framework-preferred figure) — the impact on the final score is immaterial regardless (see §6, both valuation sub-scores are floor-saturated either way). **Shares outstanding used this session: 343,820,000.** Flagged for correction once yfinance access is restored.

**Forward EPS:** backed out from stockanalysis.com's stated Forward P/E (8.15×) at live price: 1.9910 / 8.15 = **0.24429 GBP** (vs. 0.26487 GBP on 08-22 — a further ~7.8% downward revision, continuing the marginal-decline trend already noted 07-05→08-22).

**5-year historical PE range:** still unavailable (unchanged) → `FwdPE_Score` no-history fallback (50.0, neutral, flagged), same as every prior TRN session.

---

## 4. Quality Score — recomputed, same FY2026 base (unchanged from 08-22)

Per [quality-scoring.md](../framework/quality-scoring.md). All FY2026 inputs unchanged (§3 — no new fiscal year; Revenue/NI cross-checked fresh this session). Moat checklist re-examined against this session's news (§2) — no new evidence found that would flip any signal.

**Hard disqualifier check:** unchanged — all three ✅ PASS (FCF/NI 99.667%/164.33%, Net Debt/EBITDA 1.00109×, FCF positive 4/4 years).

**Profitability (25%):**
```
Net Margin = 79,813,000 / 452,684,000 = 17.632%
ROIC = (126,429,000 × 0.70) / 431,498,000 = 20.510%
NetMargin_Component = clamp((17.632/30)×100) = 58.77
ROIC_Component       = clamp((20.510/30)×100) = 68.37
Profitability_Score  = (58.77 + 68.37) / 2 = 63.57
```

**Margins (15%):** Gross Margin 82.591% (unchanged) → `GrossMargin_Score = clamp((82.591/80)×100, 0, 100) = 100.0`

**Growth (20%):** Revenue 3yr CAGR 11.43% (unchanged, same FY base) → base `Growth_Score = clamp((11.43/25)×100) = 45.72`. TAM (+10) and structural-deceleration (−10) modifiers both carried forward unchanged (no new fiscal year to re-test either) → net 0 → `Growth_Score = 45.72`

**Balance Sheet (15%):** `Net Debt/EBITDA = 167,426,000 / 167,243,000 = 1.00109×` → `BalanceSheet_Score = clamp(100×(1 − 1.00109/4), 0, 100) = 74.97`

**Moat Signal (15%)** — re-examined against this session's news (§2), unchanged:

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** (unchanged) | No new evidence found this session. |
| Brand premium (pricing power) | **FALSE** (unchanged) | CMA investigation remains open, unresolved — no new finding to reinforce or clear it further than 08-22 already established. |
| Network effect | **FALSE** (unchanged) | No new evidence. |
| Switching costs | **TRUE** (unchanged) | Unrelated to the fee controversy. |
| Scale cost advantage | **FALSE** (unchanged) | No new cost-per-unit data found. |

```
Moat_Score = (2/5) × 100 = 40.0   (unchanged)
```

**FCF Quality (10%):** `FCF/NI = 79,547,000 / 79,813,000 = 99.667%` → `FCFQuality_Score = clamp(((0.99667 − 0.40)/0.60)×100, 0, 100) = 99.44`

### Quality Score total

```
Quality Score = 63.57×0.25 + 100.0×0.15 + 45.72×0.20 + 74.97×0.15 + 40.0×0.15 + 99.44×0.10
             = 15.8925 + 15.00 + 9.144 + 11.2455 + 6.00 + 9.944
             = 67.23 → 67.2
```

**Quality Score = 67.2 — still FAILS the 80.0+ gate**, numerically identical to 07-05 and 08-22 (no new fiscal year, no new moat evidence this session).

---

## 5. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** Forward PE = 1.9910 / 0.24429 = **8.1504×** (matches stockanalysis.com's stated 8.15, cross-checked). EY = 1/8.1504 = **12.269%**. Spread = 12.269% − 4.72% = **+7.549pp** ≥ +1.5% → no flag (+0).
- **Step 2 — Rate Regime Modifier:** 10Y = 4.72%, in the 3.5–5% bracket → **+5**.
- **Combined Rate Gate modifier: +5** — same bracket as every prior TRN session.

---

## 6. Valuation Score

### Sub-scores (fresh price, flagged shares outstanding — §3)

**FCF Yield (40% weight):**
```
MarketCap = 343,820,000 × 1.9910 GBP = 684,646,220 GBP  (≈ stockanalysis.com's stated 684.54M, rounding)
FCF Yield = 79,547,000 / 684,646,220 = 11.621%
FCF_Score = clamp(100×(1 − 11.621/10), 0, 100) = 0.00   (floor-saturated, same as 08-22)
```

**EV/EBIT (40% weight, PEG-redistributed):**
```
EV = MarketCap 684,646,220 + Total Debt 261,946,000 − Cash 59,703,000 = 886,889,220 GBP
EV/EBIT = 886,889,220 / 126,429,000 = 7.0150×
EV/EBIT_Score = clamp((7.0150−12)/23×100, 0, 100) = 0.00   (floor-saturated)
```

**Forward PE + Historical PE Modifier (20% weight):**
```
Forward PE = 8.1504× (from §5). No 5yr PE history reconstructable → no-history fallback:
FwdPE_Score = 50.0 (neutral, flagged) — unchanged
```

**PEG:** N/A, same reasoning as prior sessions. Redistributed to EV/EBIT (→40%).

### Raw weighted score

| Sub-score | Weight | Score | Weighted |
|---|---|---|---|
| FCF Yield | 40% | 0.00 | 0.00 |
| EV/EBIT | 40% | 0.00 | 0.00 |
| Forward PE | 20% | 50.00 | 10.00 |
| **Raw weighted score** | | | **10.00** |

**+ Rate Gate modifier: +5** → **15.00** (before Upside/Downside).

### Upside/Downside (Expected-Return) Modifier

**Fair Value:**
- **DCF component: 345.6 GBX — carried forward, same caveat as 08-22.** No new FY26/27 information exists this session to re-derive a CMA-specific bear scenario (still no finding, still no fee-structure change) — re-deriving from scratch would require inventing a probability/magnitude assumption this framework's sourcing rule prohibits. Same explicit flag stands: **treat the Blended FV below as likely somewhat optimistic** pending a bear-case revision once the CMA investigation's shape clarifies.
- **Multiples component — partial refresh this session** (yfinance unreachable — see §3 — so peer EV/EBITDA multiples could not be re-pulled; peer Forward PE multiples fetched fresh via stockanalysis.com):
  - **EV/EBITDA — carried forward from 08-22, flagged not refreshed:** BKNG 15.482× / EXPE 13.296× / MMYT 37.179× / TRIP 11.126× → median **14.389×** → implied EV = 14.389 × TRN EBITDA 167,243,000 = 2,406,459,527 GBP → implied equity = 2,406,459,527 − Net Debt 167,426,000 = 2,239,033,527 GBP → implied FV/share = 2,239,033,527 / 343,820,000 = 6.5122 GBP = 651.22 GBX → discounted 20% (Rule 5) → **520.98 GBX**.
  - **Forward PE — fresh pull this session (stockanalysis.com):** BKNG 18.46× / EXPE 14.83× / MMYT 95.30× / TRIP 9.87×. **MMYT excluded as a data-quality outlier** — a jump from 24.355× (08-22) to 95.30× in 9 days is not a plausible re-rating; far more consistent with a near-zero/distorted trailing-quarter earnings base skewing the forward estimate (Rule 5 peer-quality discretion, same kind of judgment already applied to exclude TCOM's negative EV/EBITDA in every prior TRN session). Median of remaining 3 (BKNG/EXPE/TRIP) = **14.83×** × forward EPS 0.24429 GBP = 3.6236 GBP = 362.36 GBX → discounted 20% → **289.89 GBX**.
  - **Multiples-Based FV = average(520.98, 289.89) = 405.44 GBX.**
- **Blended FV = 0.40×345.6 + 0.60×405.44 = 138.24 + 243.264 = 381.50 GBX.**

**Sanity check:** stockanalysis.com's consensus 12-month target (~352p, 13 analysts, "Strong Buy") sits reasonably close to our 381.50 GBX; JPMorgan's newly-cut 185p bear outlier (§2) sits well below both, now for the first time actually pricing something below the live 199.1p — noted, not incorporated (this framework scores off its own scenario-weighted FV, not consensus).

```
Gap Upside % = (381.50 / 199.1) − 1 = +91.56%
Catalyst window = 2.0 years (unchanged — GBR timeline)
Annualized gap = 91.56% / 2.0 = 45.78%/yr
Intrinsic growth = 11.5%/yr (carried forward — no new FY26/27 guidance)
Shareholder yield = 0% dividend + 9.46% net buyback yield (FY26 disclosed figure, carried forward — the shares-outstanding anomaly in §3 means this session can't independently re-confirm the buyback pace, flagged)

E = 45.78 + 11.5 + 9.46 = 66.74%.  H = 10%.  E ≥ H → uncapped M would be −15.0 (floor)
```

**Guardrail 1 (catalyst reliability) — unchanged, still applied:** GBR's full operational launch is still tracked to 2027, not inside an 18–24 month window — no new information this session narrows that timeline. **Guardrail 1 stays applied — capped at −5.0.**

**M = −5.0.**

### Final Valuation Score

```
Final Score = 15.00 (raw + Rate Gate) + (−5.0) (Upside/Downside, guardrail-capped) = 10.00
```

**Final Valuation Score = 10.0 — numerically unchanged from 07-05 and 08-22.** Same structural reason as before: both valuation sub-scores are floor-saturated and the Upside/Downside Modifier is guardrail-capped well before the uncapped `E` value (66.74% this session vs. 70.12% on 08-22) actually matters — the framework absorbs the difference without the final number moving.

---

## 7. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 67.2) + 0.50 × 10.0
                = 16.4 + 5.0
                = 21.4
```

**Composite Score = 21.4 — numerically unchanged from 07-05 and 08-22.** Lands in the "BUY — Full position 6–8%" band by the numbers alone; per this framework's established practice for a held position whose Quality Score fails the 80.0+ gate, this remains a false green light and is not acted on — same standing rule as every prior TRN session.

---

## 8. Action recommendation — HOLD existing 600 shares; do **NOT** add; Quality Watch remains open

**Unchanged from 08-22: HOLD, do not top up.** The Quality Score (67.2 < 80.0) remains the sole, sufficient blocker; the CMA investigation remains open with no finding, so there is no new fact this session that would either escalate to a Phase 06 exit trigger or clear the Quality Watch flag.

**Phase 06 triggers checked, neither fires:**
- Balance sheet crisis: no — leverage and liquidity unaffected; unchanged from 08-22's analysis.
- Management change: no — Ian Brown's handover remains a scheduled transition (7/28 Sept 2026), not yet occurred, not reactive.

**Quality Watch stays open, not escalated.** The one incremental fact this session (JPMorgan's price target cut to 185p, now below the live price) is a sentiment data point, not a new Phase 06 trigger — noted for the record, doesn't change the recommendation.

### Informational-only order setup (shown for transparency — NOT being executed, same as prior sessions)

```
Blended Fair Value = 381.50 GBX  (caveated — see §6, likely optimistic pending bear-case revision)
Buy Price (20% MoS) = 381.50 × 0.80 = 305.20 GBX
Live price (199.1 GBX) vs. Buy Price: 34.76% below → would read "enter now" if gate-eligible
Primary Sell Target = 381.50 GBX
Bull-Case Trim Target = 560.5 × 0.90 = 504.45 GBX  (DCF Bull carried forward, same caveat)
Stop Loss — re-anchored to live entry (same degeneracy as prior sessions):
  20% below live entry → 199.1 × 0.80 = 159.28 GBX
  Flag: this stop sits below the 52-week low (178.00 GBX, IBKR misc_statistics, fetched this session) — a real consequence of trading near/below 52-week lows, not a calculation error.
R/R = (381.50 − 199.1) / (199.1 − 159.28) = 182.40 / 39.82 = 4.58:1 — clears the 2:1 minimum by a wide margin

Portfolio context: combined total ≈ $62,381.53 (per 2026-08-30 /sync-portfolio, most recent available — not re-run this session)
Entry (USD) = 1.9910 GBP × 1.35423005 = $2.6960/share
Stop (USD)  = 1.5928 GBP × 1.35423005 = $2.1570/share
Risk/share  = $0.5390
Max $ risk (1.5%) ≈ $935.72
Risk-based target shares ≈ 935.72 / 0.5390 ≈ 1,736 shares (≈$4,682, ≈7.51% of portfolio)
Allocation cap (Score 0.0–29.9): 6–8% ≈ $3,742.89–$4,990.52
Position Size = min(risk-based ≈$4,682, cap) ≈ $4,682 — within the 6-8% band and well inside the 15% hard cap
Incremental top-up implied: ≈1,736 − 600 ≈ 1,136 shares (≈$3,063 at live price)
```
**Not executed.** The Quality Gate governs, independent of how attractive these mechanics look — same standing conclusion as every prior TRN session.

---

## 9. Portfolio Rebalancing Summary

N/A — single-ticker rescore, no other position touched this session.

---

## 10. Next Review Trigger

- **Mandatory, unchanged:** any update on the CMA drip-pricing investigation — a finding of wrongdoing (or clearance), a fine/remedy amount, or a fee-structure change Trainline makes in response. Still the binding near-term catalyst.
- **Mandatory:** Trainline's FY2027 interim/H1 results (confirmed **30 Oct 2026**) — will let the DCF Bear case be properly re-derived with post-CMA information.
- Ian Brown's full CEO/Board handover (28 Sept 2026) — a check-in once in seat, not a re-score trigger alone.
- Any GBR-related announcement — still the binding constraint on Guardrail 1's −5 cap.
- **New this session:** restore `yfinance` access and re-verify the shares-outstanding anomaly flagged in §3 (343.82M vs. the 08-22 figure of 341,488,172) and the peer EV/EBITDA multiples not refreshed this session.
- Standard Rule 9 triggers: guidance revision, M&A, >15% unexplained price move, management change.

---

## 11. Glossary

- **CAGR** — Compound Annual Growth Rate.
- **CMA (Competition and Markets Authority)** — the UK's competition/consumer-protection regulator; its drip-pricing investigation into Trainline remains open, unresolved this session.
- **Composite Score** — this framework's 0.0–100.0 blended ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; computed only for reference here since Quality fails the gate.
- **DCF** — Discounted Cash Flow.
- **Drip pricing** — presenting mandatory charges later in a purchase flow rather than in the advertised headline price; the specific practice the CMA is investigating.
- **EBIT / EBITDA** — operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS** — Earnings Per Share.
- **EV / EV/EBIT, EV/EBITDA** — Enterprise Value / Enterprise Value divided by operating-profit measures.
- **EY (Earnings Yield)** — 1 ÷ Forward PE.
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks earnings quality).
- **Forward PE** — Price ÷ next-12-months expected EPS.
- **FV / PW Fair Value** — Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear).
- **GBR (Great British Railways)** — UK rail-nationalization program; relevant to TRN as a regulatory/political risk to its retailer role.
- **GBX / pence (GBp)** — 1/100th of a British pound; LSE quoting convention.
- **Hurdle rate** — the minimum acceptable annual return (10% in this framework).
- **Moat** — a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety)** — the discount below fair value demanded before buying.
- **Net Debt/EBITDA** — leverage ratio; this framework's balance-sheet-risk gate.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − tax rate)).
- **PE (Price-to-Earnings) ratio**, **PEG ratio** — standard valuation multiples; PEG = PE ÷ growth rate.
- **Phase 04 Quality Watch** — this framework's escalation flag for a held position whose Quality Score sits below the 80.0+ gate or is deteriorating.
- **Phase 06** — this framework's exit-review phase (balance-sheet crisis, management change, and other full-exit triggers).
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear blended estimate.
- **Quality Score** — this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 valuation scoring.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-score interest-rate check.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss on a trade; 2:1 minimum required.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — always fetch a live price before any valuation work.
- **Rule 5** — comparables-set quality requirement (discount applied for thin/mismatched peer sets; also used here to exclude a data-quality-outlier peer multiple).
- **Rule 9** — fundamental events that force an immediate re-score (>15% unexplained price move, guidance revision, M&A, management change); did not fire this session — this was a scheduled Quality Watch follow-up instead.
- **Upside/Downside Modifier (Expected-Return Modifier)** — the ±15 additive score adjustment based on expected annual return.
