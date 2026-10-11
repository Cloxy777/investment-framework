# RESCORE — ZS (Zscaler, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`) — Rule 9 trigger: **+16.5% single-day move on 2026-09-14** with no earnings catalyst ([issue #802](https://github.com/Cloxy777/investment-framework/issues/802), due 2026-09-17, 24 days overdue at this session)
**Date:** 2026-10-11 (Sunday — prices are the 2026-10-09 Friday close)
**10Y US Treasury Yield:** 5.244% (`yfinance` `^TNX`, 2026-10-09 close)
**Last review on record:** Valuation 47.9 / Quality 59.4 / Composite 44.3 (reference only) — 2026-09-07, [sessions/2026-09-07-rescore-zs.md](2026-09-07-rescore-zs.md)
**Held as a Human Override** (fails the Phase 01 Quality Score gate). Weight 0.34% per the 2026-10-11 sync ([holdings.md](../portfolio/holdings.md)).

> *Jargon decoded in the closing Glossary.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$233.73** | IBKR `get_price_history` (contract 310621426), daily bar close 2026-10-09; cross-checked equal to `yfinance` `currentPrice` |
| Market Cap | 163,054,698 × $233.73 = **$38,110.77M** | Computed; matches `yfinance` `marketCap` ($38,110,773,248) |
| 52-week range | $114.625 – $336.99 | `yfinance` |
| Analyst PTs | mean $233.38 · median **$242.50** · low $164.75 · high **$298.00** · n=44 | `yfinance`; sanity bounds for scenarios only, not scored |
| Move vs. 2026-09-07 review ($169.80) | **+37.65%** | |

## 2. Rule 9 Trigger Check (2026-09-07 → 2026-10-11)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report 2026-11-24 (`get_earnings_dates`). FY2026 Q4 (2026-09-03) was already scored on 09-07. |
| Guidance revision | No new revision found | A third-party market blurb (Wealth Awesome, CAD-quoted, low reliability) says guidance was *reaffirmed* at an Investor Day around 2026-10-06; not independently verified, not relied on. |
| M&A / management change | No | None found. |
| Macro shift | **Yes, informational** | 10Y rose 4.784% → **5.244%**, crossing the 5% line: Rate Regime Modifier moves **+5 → +10**. |
| **>15% price move** | **Yes — the issue #802 trigger** | 2026-09-14: $164.54 → $191.73 (**+16.5%**) on no ZS-specific news. Cause (cited, secondary): a sector-wide cybersecurity rally the same day (RBRK +15.6%, CRWD ~+14%) after a weekend AI-risk article from Anthropic's CEO raised demand sentiment for security vendors ([Motley Fool via Nasdaq, 2026-09-14](https://www.fool.com/investing/2026/09/14/why-rubrik-stock-soared-15-today/)). A sentiment/sector move, not a ZS fundamental. Continued drift to $233.73 (incl. +7.8% on 2026-10-09, **cause not found**) is flagged, not explained. |

**Conclusion:** trigger resolved as sector-sentiment-driven; no fundamental change identified. Re-score run on fresh price, estimates and rate data.

## 3. Data Gaps / Flags

1. **No new ZS filing since the 2026-09-03 FY2026 Q4 8-K.** All trailing financials (TTM = FY2026) are carried unchanged from the [09-07 session §4](2026-09-07-rescore-zs.md); only price, estimates, analyst PTs and the 10Y are refreshed. Not re-derived, so not re-sourced.
2. **Forward EPS convention kept for continuity:** `earnings_estimate` "+1y" = **$5.62336** (09-07 used $5.589). That row is the *next* fiscal year (FY2028, ending Jul 2028), not true NTM (current-year FY2027 is $4.908). It flatters Forward PE (41.6× vs. 47.6× on FY2027 EPS); kept so scores stay comparable to prior sessions.
3. **3yr avg PE (62.94×) not refreshed** — no new quarter reported, so the 12-quarter window is unchanged.
4. **EV/EBIT still undefined** (TTM GAAP EBIT −$133.3M) → 50.0 neutral placeholder; PEG still N/A (no GAAP-profitable fiscal year) → 15% weight redistributed to EV/EBIT. Unchanged.
5. **FCF/NI hard-disqualifier interpretive question** (negative-NI / positive-FCF pattern) and the **missing `override-log.md` entry for ZS** both remain unresolved; neither changes the outcome.
6. `yfinance` `freeCashflow` ($1,074.9M) again disagrees with the SEC-filed FCF ($779.1M); filing figure used.

## 4. Quality Score — unchanged (59.4), re-verified

No new financial data, so sub-scores carry over exactly from [09-07 §5](2026-09-07-rescore-zs.md):

| Sub-score | Value | Weight | Contribution |
|---|---|---|---|
| Profitability (net margin −1.885%, ROIC −10.75% → both floored) | 0.0 | 25% | 0.000 |
| Margins (GM 76.81%) | 96.01 | 15% | 14.402 |
| Growth (CAGR 27.51% → 100, −10 documented deceleration; FY27 guide ~17%) | 90.0 | 20% | 18.000 |
| Balance Sheet (net cash) | 100.0 | 15% | 15.000 |
| Moat (4/5, scale-cost declined) | 80.0 | 15% | 12.000 |
| FCF Quality (FCF/NI negative-NI artifact) | 0.0 | 10% | 0.000 |

**Quality Score = 59.4 — FAILS the 80.0+ gate by 20.6 points.** Hard disqualifiers: Net Debt/EBITDA ✅ (net cash); FCF-positive 3+ yrs ✅; FCF/NI ⚠️ same unresolved flag. Analyst growth estimates for FY2027 are slightly higher now (revenue +17.3%), supporting but not changing the −10 deceleration modifier.

## 5. Rate Environment Gate

```
Step 1: Forward PE = 233.73 ÷ 5.62336 = 41.56×;  EY = 2.406%;  Spread = 2.406% − 5.244% = −2.838%  → below +1.5% → +5
Step 2: 10Y = 5.244% → ">5%" bracket → +10
Total Rate Modifier = +15   (was +10 on 09-07)
```

## 6. Valuation Score

```
FCF Yield   = 779.1 ÷ 38,110.77 = 2.0443%
FCF_Score   = 100 × (1 − 2.0443/10) = 79.557     → × 0.40 = 31.823
EV/EBIT     = undefined (EBIT < 0) → 50.0 placeholder; weight 25% + 15% (PEG) = 40% → 20.000
Fwd PE      = 41.56×; 3yr avg 62.94×; Deviation = −33.96%
FwdPE_Score = clamp(50 + (−33.96)×2.5) = clamp(−34.9) = 0.0   → × 0.20 = 0.000
PEG         = N/A (weight redistributed above)
Raw weighted = 31.823 + 20.000 + 0.000 = 51.823
```

### Upside/Downside Modifier

| Scenario | Weight | Basis | Fair Value |
|---|---|---|---|
| Bull | 25% | FY+1 high EPS $6.78; anchored to (not above) the $298 analyst high PT | **$298.00** |
| Base | 50% | Consensus path; analyst median PT | **$242.50** |
| Bear | 25% | FY+1 low EPS $4.68 × 3yr-range-low PE 32.08× — no re-rating credit (same construction as 09-07) | **$150.00** |

```
PW Fair Value = 0.25×298.00 + 0.50×242.50 + 0.25×150.00 = 74.50 + 121.25 + 37.50 = $233.25
Gap Upside    = 233.25 ÷ 233.73 − 1 = −0.21%;  catalyst window 2 yrs → annualized −0.10%/yr
Intrinsic growth = +14.57%/yr  (`growth_estimates` +1y EPS growth, sourced)
Shareholder yield = −3.39%/yr  (SBC dilution, unchanged from 09-07)
E = −0.10 + 14.57 − 3.39 = +11.08%/yr
M = −15 × clamp((11.08 − 10)/15, 0, 1) = −15 × 0.072 = −1.08
```
The rally has erased the price-to-fair-value gap (+20.7% on 09-07 → ~0%): upside credit shrank from −10.81 to −1.08. Guardrails: catalyst documented (Zero Trust/SASE cycle, 2026-11-24 print); scenario-weighted with bear below the analyst low PT ($164.75); within ±15. ✓

### Final

```
Valuation Score = 51.823 + 15.000 − 1.077 = 65.745 → 65.7
Composite (reference only) = 0.50×(100 − 59.4) + 0.50×65.7 = 20.30 + 32.85 = 53.15 → 53.2 (rounded up)
```

| | 09-07 | 10-11 |
|---|---|---|
| Valuation | 47.9 | **65.7** (+17.8: FCF yield thinner at the higher price, Rate Modifier +5, upside credit mostly gone) |
| Quality | 59.4 | **59.4** (fails gate) |
| Composite (ref only) | 44.3 | **53.2** |

## 7. Action

**HOLD the existing 0.34% override position — no add, no trim.** Valuation 65.7 sits in the 50.0–69.9 "Fair Value — hold, no new entry" band (the earlier "Cheap/BUY" false green light is gone). Phase 05 trims start at 70.0, and a Quality-gate-failing override isn't governed by the Composite anyway. No Phase 06 exit trigger applies. Order setup not applicable (no BUY/TRIM): the live price ($233.73) is already at the PW fair value ($233.25), so expected upside to target is ~0 and R/R is nowhere near 2:1.

Watch: a Valuation Score drifting to 70.0+ (a further price rise with unchanged estimates, or 10Y staying >5%) would put the position in the trim band; the unrealized gain is +48.9% on $157.16 avg cost.

## 8. Next Review Trigger

- Fiscal Q1 FY2027 earnings, ~2026-11-24.
- Rule 9 standing triggers: guidance revision, M&A, management change, an unexplained >15% move.
- **Open governance items (unchanged, not resolved by `/rescore`):** no ZS entry in `override-log.md`; FCF/NI disqualifier interpretation for negative-NI profiles.
- Issue #802 can be closed (rescore done).

---

## Glossary

| Term | Meaning |
|---|---|
| **Rule 9** | Framework rule forcing a re-score after earnings, guidance change, M&A, management change, macro shift, or a >15% price move with no identified cause. |
| **Rate Regime Modifier** | Points added to the valuation score depending on the 10-year Treasury yield; +10 when it is above 5%. |
| **Earnings Yield (EY)** | 1 ÷ forward PE; compared with the 10-year Treasury yield in the Rate Environment Gate. |
| **FCF Yield** | Free cash flow ÷ market cap. |
| **Forward PE** | Price ÷ expected next-period earnings per share. |
| **Human Override** | A position held outside the framework's rules, tracked in `override-log.md`. |
| **Quality Score / 80.0+ gate** | 0–100 business-quality score; must reach 80.0 to be scored for valuation. |
| **Composite Score** | 50/50 blend of inverted Quality and Valuation; lower is more attractive. Reference-only here. |
| **PW Fair Value** | Probability-weighted fair value: 25% bull + 50% base + 25% bear. |
| **R/R** | Risk/reward ratio; minimum 2:1 to enter. |
| **SBC** | Stock-based compensation; non-cash pay in shares that dilutes owners. |
| **Hard disqualifier** | A Quality condition that fails a company regardless of the weighted score. |
