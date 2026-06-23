# RESCORE — MSFT — 2026-06-23

**Task type:** RESCORE (single ticker)
**Date:** 23 Jun 2026 (Tuesday — markets open)
**10Y US Treasury Yield:** 4.50% (TradingEconomics/CNBC, 23 Jun 2026 — up from the 4.46% used in the 06-20 session; still in the "3.5–5%" bracket)
**Rate Regime Modifier (Step 2):** +5 (unchanged — 10Y still in the 3.5–5% bracket)
**Rate Environment Gate Step 1:** MSFT **FAILS** the Earnings Yield Spread Test → a **separate** +5 additive. **Total Rate Modifier = +10** (unchanged from 06-20).
**Purpose of this run:** routine 3-day interim check per Rule 9 (no scheduled trigger expected, but confirming nothing fired) and a full price-dependent refresh of the 06-20 score, which was the first MSFT score to carry the new Upside/Downside Modifier.
**Last review on record:** MSFT 35.0 ([sessions/2026-06-20-rescore-msft.md](2026-06-20-rescore-msft.md)).

---

## 1. Live Price (Rule 0)

| Ticker | Latest price used | Source | Note |
|---|---|---|---|
| **MSFT** | **$370.00** | IBKR `get_price_snapshot` (contract 272093), 23 Jun 2026, intraday | +0.72% vs prior close. Markets open today (Tuesday), unlike the 06-20 Saturday close. |

- **52-week range:** **$356.28 – $552.28** (IBKR `misc_statistics`). Current price sits **~3.9% above the 52-week low** and **~33.0% below the 52-week high**.
- **Year-to-date:** **−23.32%** (IBKR).
- **Analyst consensus price target (bull-case sanity check):** mean **$561.39**, median **$555**, high **$870**, low **$400** (55 analysts, `yfinance` — unchanged from 06-20; a separate web search today independently corroborates a "Buy" consensus with a $565.62 mean target across 32 analysts, consistent within normal cross-source variance).
- **Price drift since last review:** $378.91 (20 Jun close) → $370.00 (23 Jun intraday) = **−2.35%**. Well under the 15% Rule 9 threshold — no price-driven fundamental trigger.

---

## 2. Rule 9 Trigger Check (mandatory — 3-day window since 06-20)

Web search run for MSFT news between 2026-06-20 and 2026-06-23. Findings:

1. **Chevron data-center power deal (announced 22 Jun 2026).** Microsoft and Chevron agreed a 20-year deal for Chevron to supply a 2.67-gigawatt natural-gas power plant in West Texas serving Microsoft's AI/cloud data centers. This is an *operational/infrastructure* announcement (power supply for existing AI capex plans), not a guidance revision, M&A of a business, or a balance-sheet event. **Does not meet a Rule 9 trigger** — it is consistent with, not a change to, the AI/Azure capex thesis already embedded in this framework's scenario model.
2. **Rosen Law Firm securities class action (active, deadline 11 Aug 2026 to seek lead plaintiff).** The underlying class period is **1 May 2025 – 28 Jan 2026** — i.e., this is litigation about *already-disclosed, already-priced* historical conduct (Copilot positioning/benchmark claims, capex reallocation away from Azure), first surfaced in filings in mid-June 2026, not a new event in the 06-20→06-23 window. No new disclosure, guidance change, or financial restatement accompanies it. **Not a fresh Rule 9 trigger** — flagged for awareness and continued monitoring (Phase 04 narrative/short-thesis-style engagement), but it predates this review window and does not itself change any input to the score.
3. **Board departure — Reid Hoffman not standing for re-election** (disclosed 2 Jun 2026, before the 06-20 session). No new management/board news in the 06-20→06-23 window specifically. Not a fresh trigger.
4. **No earnings, guidance revision, M&A, or new management change occurred in the 06-20 → 06-23 window.** Next scheduled earnings remains **FY26 Q4, expected late July 2026**.

**Conclusion: no Rule 9 trigger fired in this window.** This is a routine price-refresh re-score, not an event-driven one. Stated plainly per the task instructions: nothing material happened.

---

## 3. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved (5th consecutive session).** MSFT still discloses no maintenance-vs-growth capex split, so Owner Earnings cannot be computed without inventing a figure (prohibited). **Raw TTM Free Cash Flow used** as the FCF_Score input, as in every prior session back to 06-07.
2. **Fundamentals reused from the 2026-06-12 session (no earnings since 06-12, confirmed again today — see §2).** Reused: TTM EBIT $148.929B, TTM FCF $72.916B, TTM Net Income $125.22B, net debt $24.922B, shares outstanding 7,428,434,704, EPS-growth Fast-Grower status (TTM +23.3%, corroborated today by `yfinance` `earningsGrowth` 23.4% / `earningsQuarterlyGrowth` 23.1% — consistent, no change). Only **price-dependent figures refreshed** (market cap, EV, EV/EBIT, FCF yield, forward PE, PEG) — same lineage convention as 06-20 vs 06-12.
3. **5-year average PE re-computed fresh this session** via the `yfinance` reconstructed-TTM-EPS method (same 20-quarter window, 2021-07-27 to 2026-04-29 — unchanged from 06-20 since no new earnings print has occurred): **avg 31.97×, range 24.17×–38.80×** (n=20 quarters), **identical to 06-20** to 2 decimal places. No movement — confirmed, not just reused.
4. **Forward PE — used 19.26× (refreshed, midpoint of two methods).** `yfinance` live `forwardEps` $19.3459 ÷ $370.00 price → 19.13×. Carrying forward the 06-20 session's implied NTM EPS ($19.08) at the new price → 19.39×. Used the **midpoint 19.26×**, with a robustness check across 19.13–19.39× (Rate Gate Step 1 result and FwdPE_Score both unaffected — see §5/§6).
5. **FCF/Net Income conversion ratio** — `yfinance` FY-annual series re-pulled today: 89.6% / 82.2% / 84.0% / 70.3% (FY2022–FY2025), **identical to 06-20**. No new TTM figure available (no earnings since FY26 Q3) — the 58.2% TTM-through-Q3-FY26 figure from 06-20 stands, still explained by AI/datacenter growth capex per the Phase 04 carve-out.
6. **Gross margin / ROIC / Revenue CAGR** — Phase 01 quality-gate inputs, not Phase 02 score inputs. No new data since 06-20 (no earnings). Not re-collected; flagged, not guessed.
7. **Scenario fair value carried forward from 06-20, recalculated at the new price.** No fundamental change occurred (§2) to justify revising the bull/base/bear PE multiples (31.0×/27.0×/21.0×), intrinsic growth (13%/yr), or shareholder yield (1.96%) assumptions built on 06-20 — see §6 for why each is still defensible. Only the live price and the resulting NTM EPS, Gap Upside %, and E were recalculated.

---

## 4. MSFT — Inputs (price-refreshed)

**Sector:** Technology — Software, Cloud Infrastructure (Azure) & Productivity
**Current portfolio weight:** ~15.01% (marginally over the 15% cap — see §9; orchestrator owns holdings.md).

| Item | Value | Basis |
|---|---|---|
| Live price | $370.00 | Rule 0, §1 |
| Shares outstanding | 7,428,434,704 | Reused (10-Q FY26 Q3 cover) |
| **Market Cap** | 7,428,434,704 × $370.00 = **$2,748.52B** | Computed |
| Net debt | $24.922B | Reused (10-Q) |
| **Enterprise Value (EV)** | $2,748.52B + $24.922B = **$2,773.44B** | Computed |
| TTM EBIT | $148.929B | Reused |
| **EV/EBIT** | 2,773.44 ÷ 148.929 = **18.6226×** | Computed (was 19.067× at $378.91) |
| TTM FCF | $72.916B | Reused |
| **FCF Yield** | 72.916 ÷ 2,748.52 = **2.6529%** | Computed (was 2.5905%) |
| TTM Net Income | $125.22B | Reused |
| Forward PE (NTM) | **19.2592×** | §3 flag 4 |
| 5yr avg PE (trailing anchor) | **31.9693×** (range 24.1686–38.8030×) | `yfinance`, recomputed fresh — unchanged from 06-20 |
| EPS growth (Fast Grower test) | FY24 +22%, FY25 +15.5%, TTM +23.3% — **all >15% → Fast Grower confirmed, still holds** | Reused + corroborated today (`yfinance` earningsGrowth 23.4%) |
| PEG | **0.8266** (19.2592 ÷ 23.3) | Computed |
| FCF/NI conversion | 58.2% (TTM) | §3 flag 5 — unchanged |
| Net Debt/EBITDA | 0.131× | Reused — well within limits |

---

## 5. MSFT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 19.2592 = 5.1923%
Spread = EY − 10Y Treasury = 5.1923% − 4.50% = +0.6923%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.6923%, ~0.81pp short) → **+5 additive**.
*Robustness across Forward PE 19.13–19.39×:* spread ranges +0.66% to +0.73% — FAIL in all cases. The +5 is robust. (Spread improved slightly vs. 06-20's +0.58% — a lower price helps more than the higher 10Y hurts — but still well short of passing.)

**Step 2 — Rate Regime Modifier**
10Y = 4.50% → "3.5–5%" bracket → **+5** (unchanged)

**Total Rate Modifier for MSFT = +10** (unchanged from 06-20)

---

## 6. MSFT — Full Score Calculation (raw weighted + Rate Modifier)

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.6529 / 10), 0, 100) = 73.471
```
→ Contribution: 73.471 × 0.40 = **29.388**

**EV/EBIT — 25% weight**
```
EV/EBIT_Score = clamp((18.6226 − 12) / 23 × 100, 0, 100) = 28.794
```
→ Contribution: 28.794 × 0.25 = **7.198**

**Forward PE (fallback formula — 5yr avg only) — 20% weight**
```
Deviation% = (19.2592 − 31.9693) / 31.9693 × 100 = −39.757%
FwdPE_Score = clamp(50 + (−39.757) × 2.5, 0, 100) = clamp(−49.39, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0** (fallback formula folds in the Historical PE Modifier — no separate ±10 applied)

**PEG — 15% weight (Fast Grower confirmed, §4)**
```
PEG       = Forward PE ÷ TTM EPS growth% = 19.2592 ÷ 23.3 = 0.8266
PEG_Score = clamp((0.8266 − 0.5) / 2.0 × 100, 0, 100) = 16.329
```
→ Contribution: 16.329 × 0.15 = **2.449**

**Raw weighted score:**
```
= 29.388 + 7.198 + 0.0 + 2.449
= 39.036
```
**+ Rate Modifier (+10) = 49.036** (before the Upside/Downside Modifier)

---

## 7. MSFT — Upside/Downside Modifier (refreshed at new price)

**Step 0 — Scenario fair value.** No fundamental change occurred since 06-20 (§2), so the 06-20 scenario framework's bull/base/bear PE multiples, intrinsic growth, and shareholder yield assumptions remain defensible and are **carried forward** — only the live price and resulting NTM EPS/Gap/E are recalculated, exactly as instructed.

NTM EPS = Live Price ÷ Forward PE = $370.00 ÷ 19.2592 = **$19.2116** (vs $19.08 on 06-20 — moved slightly because both price and forward PE shifted, partially offsetting).

| Scenario | Weight | PE applied | Rationale (unchanged from 06-20 — still defensible, no new information) | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 31.0× | Azure/AI monetization re-accelerates; multiple re-rates to ~5yr average (31.97× — unchanged this session). Still below the $561 analyst-mean PT and far below the $870 high. | $19.2116 × 31.0 = **$595.56** |
| **Base** | 50% | 27.0× | Consensus mid-teens EPS growth (FY26 +20.7%, FY27 +16% — no revision since 06-20) but a haircut multiple vs. the 31.97× 5yr average to reflect the higher-rate regime (10Y now 4.50%, up from 4.46%). | $19.2116 × 27.0 = **$518.71** |
| **Bear** | 25% | 21.0× | Growth decelerates / AI-capex returns disappoint; multiple de-rates near the low end of the 5yr band (24.17×). Bear FV $403.44 remains close to the analyst $400 low PT — downside still underwritten to the Street's worst case. | $19.2116 × 21.0 = **$403.44** |

```
PW Fair Value = 0.25×595.56 + 0.50×518.71 + 0.25×403.44 = $509.11
```
(Probability-Weighted. Sits below the $561 analyst mean and $555 median PT — still conservative, sanity-check passes. Up modestly from 06-20's $505.59, driven by the slightly higher NTM EPS base.)

**Step 1 — Expected annual return E.**
```
Gap Upside %    = (509.11 ÷ 370.00) − 1              = +37.60%
Catalyst window = 2 years  (unchanged — FY26 Q4 late-Jul-2026 print + FY27 Azure/AI re-acceleration
                            cycle; still within Rule 10's 18–24mo horizon → upside credit allowed)
Annualized gap  = 37.60% ÷ 2                          = +18.80%
Intrinsic growth = +13%/yr   (unchanged — deliberately below consensus EPS CAGR of +16–20.7%)
Shareholder yield = dividend ~0.96% + net buyback ~1.0% = +1.96% (unchanged; `yfinance` trailing
                    dividend yield re-checked today at 0.94–0.99% depending on field — immaterial drift)

E = 18.80% + 13% + 1.96% = +33.76%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 33.76% ≥ H → M = −15 × clamp((33.76 − 10)/15, 0, 1) = −15 × clamp(1.58, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (the maximum attractive bound, same as 06-20 — E moved further above the +25%/yr full-credit threshold, so the floor is even more robust this session).

**Guardrail checks:**
1. **Catalyst:** documented (FY26 Q4 earnings + FY27 Azure/AI cycle), within 18–24 months → upside credit allowed. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($509.11) is below the analyst mean ($561) and median ($555); bear case underwritten near the $400 low PT. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** at the −15 floor. ✓

---

## 8. MSFT — Final Score & Action

```
Final Score = raw weighted 39.036 + Rate Modifier (+10) + Upside/Downside Modifier (−15)
            = 34.036
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 34.0**

# Final Score: 34.0 → Action band: BUY — Standard position 3–5% (30.0–49.9)

**Did the score change vs. 06-20?** **Yes, marginally** — 35.0 → 34.0 (−1.0 point), driven almost entirely by the lower live price ($378.91 → $370.00) pulling FCF_Score, EV/EBIT_Score, and the Upside/Downside Modifier's expected return all slightly more favorable, partially offset by the higher 10Y yield (4.46% → 4.50%, no bracket change) and a marginally higher forward PE estimate. **The action band did NOT change** — still BUY — Standard (30.0–49.9).

---

## 9. Portfolio / Compliance Note (independent of valuation score)

MSFT sits at **~15.01% — marginally over the 15% hard cap (Upgrade 7)**, per `portfolio/holdings.md` (20 Jun 2026 snapshot; not edited here). This is the same structural concentration issue flagged across the last 5 consecutive sessions (06-07, 06-11 backfill, 06-12, 06-20, and now 06-23), though the magnitude of the breach has narrowed considerably from the original ~16% to ~15.01% (~0.01pp over) as price has fallen. The open compliance trim from the 2026-06-15 rebalance remains the operative housekeeping action on MSFT, independent of the valuation score. *(holdings.md is owned by the orchestrator — not edited here.)*

---

## 10. Order Setup (BUY band requires it — shown, with the gating flags)

Computed for completeness because the score lands in a BUY band, but **note both gates below** — the trade is not actionable, same conclusion as 06-20.

```
Blended Fair Value (= PW FV):        $509.11
Margin of Safety (Score 30–49.9):    25%   (lower end; wide-moat proven compounder — unchanged rationale)
BUY PRICE (limit):                   $509.11 × (1 − 0.25) = $381.83
  → Live price $370.00 is BELOW the formal buy price (−3.10%) — nominally an actionable entry level.
PRIMARY SELL TARGET (blended FV):    $509.11
BULL-CASE TRIM TARGET (bull × 0.90): $595.56 × 0.90 = $536.00
STOP LOSS (Buy × (1 − 25%)):         $381.83 × 0.75 = $286.37   (below the 52-week low context $356.28 — a wide structural stop)
R/R at formal entry = (509.11 − 381.83) ÷ (381.83 − 286.37) = 127.28 ÷ 95.46 = 1.33:1
```

**⚠️ R/R = 1.33:1 is BELOW the 2:1 minimum (Rule 6) — unchanged from 06-20.** Despite ~37.6% upside to fair value (even wider than 06-20's 33.4%), the wide 25% stop makes the reward/risk ratio insufficient using the formal Buy Price as entry. (Using the current live price of $370.00 directly as entry instead — a slightly more aggressive read — improves R/R to ~1.66:1, still below 2:1.) Per Rule 6, **R/R below 2:1 = do not enter** even when the score-band says BUY.

**Net:** the same two independent gates each still block adding capital here — (a) the ~15.01% position cap (marginally over), and (b) sub-2:1 R/R. The BUY-band **score** (34.0) stands and is the headline of this rescore; the **trade** does not execute — identical conclusion to 06-20.

---

## 11. Next Review Trigger

- **Routine:** MSFT FY2026 Q4 earnings (fiscal year ending June 2026), expected **late July 2026** — standard post-earnings re-score (will also refresh the TTM fundamentals reused here for the 6th consecutive session).
- **Open compliance item (5th flag):** dedicated `/rebalance` execution of the position-cap trim (now a much smaller ~0.01pp overage than the original ~1–2pp).
- **Open methodology item:** Upgrade 1 (Owner Earnings) decision for non-disclosing mega-caps (§3 flag 1).
- **Monitoring item (new, not a Rule 9 trigger):** Rosen Law Firm securities class action (class period 1 May 2025–28 Jan 2026, lead-plaintiff deadline 11 Aug 2026) — track for any escalation (settlement terms, scope expansion, or a fresh disclosure) that could constitute a future Rule 9 trigger; today's filing itself does not qualify.
- **Watch:** if price re-rates toward fair value, the Upside/Downside Modifier shrinks and the score will rise back toward the HOLD band — re-derive at the next earnings print regardless.

---

## Glossary

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year — a quick gauge of where the current price sits within its recent trading history. |
| **bps (basis points)** | 1 bps = 0.01 percentage points. |
| **Buyback yield (net buyback yield)** | The rate at which a company's share count shrinks per year from repurchasing its own stock (net of new issuance) — a component of shareholder yield. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers). |
| **Catalyst window** | The timeframe (per Rule 10, typically 18–24 months) within which a documented, specific event is expected to close the gap between price and fair value — required before the Upside/Downside Modifier can credit large expected upside. |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **Fast Grower** | Peter Lynch's term for a company growing earnings per share (EPS) faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap — how much free cash a company throws off relative to its price; higher is cheaper. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **FV (Fair Value)** | The analyst's estimate of what a company is intrinsically worth, independent of its current market price. |
| **Hurdle rate** | The minimum acceptable annual return for an investment to be worth making — this framework uses 10% as the hurdle the Upside/Downside Modifier measures expected return against. |
| **IRR** | Internal Rate of Return — the annualized percentage return an investment is expected to generate. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Net Debt/EBITDA** | Net debt divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **NI (Net Income)** | Net Income — accounting profit after all expenses, interest, and taxes ("the bottom line"). |
| **NTM (Next Twelve Months)** | The forward-looking 12-month period used for forward earnings estimates. |
| **Owner Earnings** | Warren Buffett's adjusted cash-flow measure: Net Income + D&A − Maintenance CapEx only — used instead of raw FCF for moat-building reinvestors like MSFT (Hybrid Upgrade 1). |
| **PE (Price-to-Earnings) ratio** | Share price ÷ earnings per share. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **PT (Price Target)** | An analyst's forecast of where a stock's price will be at a future date. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case (Rule 7). |
| **R/R (Risk/Reward ratio)** | (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **Shareholder yield** | Cash returned to shareholders as a percentage of share price — dividend yield plus net buyback yield combined. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | An additive ±15 adjustment to the valuation score based on expected annual return (the gap to PW Fair Value, annualized over the catalyst window, plus intrinsic growth and shareholder yield). |
