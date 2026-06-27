# RESCORE — MSFT — 2026-06-26

**Task type:** RESCORE (single ticker)
**Date:** 26 Jun 2026 (Friday — markets open)
**10Y US Treasury Yield:** 4.38% (TradingEconomics, 26 Jun 2026 — down from 4.50% used in the 06-23 session; still in the "3.5–5%" bracket)
**Rate Regime Modifier (Step 2):** +5 (unchanged — 10Y still in the 3.5–5% bracket)
**Rate Environment Gate Step 1:** MSFT **FAILS** the Earnings Yield Spread Test → a **separate** +5 additive. **Total Rate Modifier = +10** (unchanged from 06-23).
**Purpose of this run:** continuing the short-interval Rule 9 check cadence (06-20 → 06-23 → 06-26) through this week's volatility, and a full price-dependent refresh of the 06-23 score.
**Last review on record:** MSFT 34.0 ([sessions/2026-06-23-rescore-msft.md](2026-06-23-rescore-msft.md)).

---

## 1. Live Price (Rule 0)

| Ticker | Latest price used | Source | Note |
|---|---|---|---|
| **MSFT** | **$368.65** | IBKR `get_price_snapshot` (contract 272093), 26 Jun 2026, 12:07pm ET intraday | +4.48% vs prior close ($352.83, 25 Jun close — corroborated by independent web search). |

- **52-week range:** **$349.20 – $552.28** (IBKR `misc_statistics`). **A new 52-week low was set this week** ($349.20, vs. $356.28 cited on 06-23) before today's bounce. Current price sits **~5.6% above the new 52-week low** and **~33.2% below the 52-week high**.
- **Year-to-date:** **−23.6%** (IBKR), down from −23.32% on 06-23.
- **Analyst consensus price target (bull-case sanity check):** cross-checked today across S&P Global (56 analysts, mean $561.11), MarketBeat-style aggregators ($562.10, $569.87, $565.16) — consensus clusters **$561–$570**, "Strong Buy"/"Buy" — consistent with the $561.39 mean used on 06-23.
- **Price drift since last review:** $370.00 (23 Jun intraday) → $368.65 (26 Jun intraday) = **−0.36%** net. Intraweek path was more volatile: $370.00 → $365.46 (24 Jun close) → $352.83 (25 Jun close, −4.65% from review) → $368.65 (26 Jun intraday, +4.48% bounce). Both the net move and the largest single-day move (−3.45/−3.8% on 25 Jun) are well under the 15% Rule 9 threshold.

---

## 2. Rule 9 Trigger Check (mandatory — 3-day window since 06-23)

Web search run for MSFT news between 2026-06-23 and 2026-06-26. Findings:

1. **Securities class action — case number now confirmed: No. 26-cv-02071** (W.D. Washington), *City of St. Clair Shores Police and Fire Retirement System v. Microsoft*. Cross-checked the underlying facts against the 06-23 entry: same disclosure (28 Jan 2026 — Azure growth slowdown + Microsoft 365 Copilot premium customers disclosed at only 15M, causing a 10% one-day stock drop), same lead-plaintiff deadline (**11 Aug 2026**). **This is the same litigation already flagged on 06-23, not a new event** — multiple law firms (BFA Law, Rosen, Robbins Geller, etc.) are independently soliciting lead-plaintiff applicants for the identical case, which is why it resurfaces in searches under different firm names. **Not a fresh Rule 9 trigger.**
2. **Xbox/gaming division restructuring.** Reporting (Bloomberg 10 Jun, GeekWire, Kotaku) describes new Xbox CEO Asha Sharma (≈100 days into tenure, i.e. appointed before this review window) planning "significant" layoffs after a 33% YoY plunge in hardware revenue and a 7% decline in quarterly gaming revenue; ~1,000 job cuts reported across Xbox Game Studios, marketing, and hardware engineering, with budget cuts to follow. **No specific headcount, severance cost, or segment-margin figure has been formally disclosed by Microsoft** — this is press reporting on a planned reorganization, not a guidance revision, M&A event, or management change at the Microsoft Corp level (Sharma is a divisional CEO, and her appointment predates this window). **Does not meet a Rule 9 trigger** under the framework's defined list, but flagged below as a Phase 04 monitoring item — likely to be quantified at the FY26 Q4 earnings call.
3. **Quantum computing credibility questions.** A 24 Jun 2026 Nature commentary cast doubt on the methodology behind Microsoft's Majorana-based quantum computing claims. This is a reputational/scientific-credibility issue with no balance-sheet or earnings impact disclosed. **Not a Rule 9 trigger.**
4. **Analyst price-target cuts (Stifel and others), still "Hold"/"Neutral" ratings.** Price target revisions are not a Rule 9 trigger under this framework (sanity-check input only, not an action trigger).
5. **FY2026 capex (~$190B) cited as a growing analyst concern** alongside the Chevron power deal (already flagged 06-23) — this is consistent with, not a revision to, the AI/Azure capex thesis already embedded in the scenario model. No new guidance figure was issued in this window. **Not a Rule 9 trigger.**
6. **No earnings, formal guidance revision, M&A, or Microsoft Corp-level management change occurred in the 06-23 → 06-26 window.** Next scheduled earnings remains **FY26 Q4, expected late July 2026**.

**Conclusion: no Rule 9 trigger fired in this window.** The price decline to a fresh 52-week low and back is explained by sentiment/macro factors above (litigation overhang, quantum-credibility doubts, capex concerns, gaming-segment weakness, analyst caution) rather than a confirmed fundamental break — consistent with "price dropped on intact thesis" being explicitly excluded as a valid exit trigger. This remains a routine price-refresh re-score.

---

## 3. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved (6th consecutive session).** MSFT still discloses no maintenance-vs-growth capex split. **Raw TTM Free Cash Flow used** as the FCF_Score input, as in every prior session back to 06-07.
2. **Fundamentals reused from the 2026-06-12 session (no earnings since 06-12, confirmed again today — see §2).** Reused: TTM EBIT $148.929B, TTM FCF $72.916B, TTM Net Income $125.22B, net debt $24.922B, shares outstanding 7,428,434,704, TTM EPS growth +23.3% (Fast-Grower status). Only **price-dependent figures refreshed** (market cap, EV, EV/EBIT, FCF yield, forward PE, PEG, scenario fair value).
3. **`yfinance` was unreachable this session — flagged, not silently worked around.** `pip install yfinance` succeeded, but every live data call failed with a `curl_cffi`/TLS library error (`OPENSSL_internal:invalid library`) going through the environment's egress proxy — a known unsupported case (proxy README: certificate-pinned/non-standard-TLS clients), not a code or credentials issue. **Consequence:** the forward-PE inputs below could not be freshly re-pulled from `yfinance` today. Instead, the **last verified `yfinance` figures (pulled 06-23)** were carried forward — defensible because no earnings print has occurred to revise consensus estimates — and the resulting forward PE was **cross-checked against five independent public sources** (GuruFocus 18.83×, two Yahoo-derived reads 19.53–19.74×, fullratio/financecharts 18.18–19.74×) queried live today, all of which bracket the carried-forward estimate. This is flagged explicitly per "never invent or estimate financial data" — the 5yr avg/range PE and FCF/NI conversion ratio (also normally `yfinance`-sourced) are unaffected since they are reused, unchanged fundamentals-based figures (see point 2 and 4 below), not figures requiring a fresh pull this session.
4. **5-year average PE — unchanged, not recomputed.** Carried forward from 06-20/06-23: **avg 31.9693×, range 24.1686×–38.8030×** (n=20 quarters). No new earnings print has occurred since that figure was last computed, so the underlying TTM-EPS series this average is built on has not moved — recomputing would reproduce the same number, not a fresh one.
5. **Forward PE — used 19.1223× (carried-forward EPS inputs ÷ new live price, midpoint of two methods, see flag 3).** Method 1: 06-23's `yfinance` `forwardEps` ($19.3459) ÷ $368.65 = 19.0557×. Method 2: 06-23's implied NTM EPS ($19.2116) ÷ $368.65 = 19.1889×. Midpoint = **19.1223×**. Robustness: both methods land within the 18.18–19.74× cross-source range pulled live today (flag 3).
6. **FCF/Net Income conversion ratio** — unchanged, reused: 89.6% / 82.2% / 84.0% / 70.3% (FY2022–FY2025 annual); 58.2% TTM-through-Q3-FY26 (carried, no new quarter).
7. **Gross margin / ROIC / Revenue CAGR** — Phase 01 quality-gate inputs, not Phase 02 score inputs. No new data since 06-23 (no earnings). Not re-collected; flagged, not guessed.
8. **Scenario fair value bull/base/bear PE multiples (31.0×/27.0×/21.0×), intrinsic growth (13%/yr), and shareholder yield (1.96%) carried forward from 06-20/06-23 — unchanged.** No fundamental change occurred (§2) to justify revising them. Only the live price and the carried-forward NTM EPS estimate (→ resulting Gap Upside % and E) were recalculated.

---

## 4. MSFT — Inputs (price-refreshed)

**Sector:** Technology — Software, Cloud Infrastructure (Azure) & Productivity
**Current portfolio weight:** ~15.01% per [holdings.md](../portfolio/holdings.md) (last synced 22 Jun 2026 — not recomputed here; weight refresh is `/sync-portfolio`'s job, not `/rescore`'s. See §9.)

| Item | Value | Basis |
|---|---|---|
| Live price | $368.65 | Rule 0, §1 |
| Shares outstanding | 7,428,434,704 | Reused (10-Q FY26 Q3 cover) |
| **Market Cap** | 7,428,434,704 × $368.65 = **$2,738.49B** | Computed |
| Net debt | $24.922B | Reused (10-Q) |
| **Enterprise Value (EV)** | $2,738.49B + $24.922B = **$2,763.41B** | Computed |
| TTM EBIT | $148.929B | Reused |
| **EV/EBIT** | 2,763.41 ÷ 148.929 = **18.5552×** | Computed (was 18.6226× at $370.00) |
| TTM FCF | $72.916B | Reused |
| **FCF Yield** | 72.916 ÷ 2,738.49 = **2.6626%** | Computed (was 2.6529%) |
| TTM Net Income | $125.22B | Reused |
| Forward PE (NTM) | **19.1223×** | §3 flags 3, 5 |
| 5yr avg PE (trailing anchor) | **31.9693×** (range 24.1686–38.8030×) | Reused/confirmed unchanged — §3 flag 4 |
| EPS growth (Fast Grower test) | TTM +23.3% — **Fast Grower confirmed, still holds** | Reused |
| PEG | **0.8207** (19.1223 ÷ 23.3) | Computed |
| FCF/NI conversion | 58.2% (TTM) | §3 flag 6 — unchanged |
| Net Debt/EBITDA | 0.131× | Reused — well within limits |

---

## 5. MSFT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 19.1223 = 5.2295%
Spread = EY − 10Y Treasury = 5.2295% − 4.38% = +0.8495%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.8495%, ~0.65pp short) → **+5 additive**.
*(Spread improved slightly vs. 06-23's +0.69% — a lower 10Y yield outweighs the marginally higher implied forward PE — but still well short of passing.)*

**Step 2 — Rate Regime Modifier**
10Y = 4.38% → "3.5–5%" bracket → **+5** (unchanged)

**Total Rate Modifier for MSFT = +10** (unchanged from 06-23)

---

## 6. MSFT — Full Score Calculation (raw weighted + Rate Modifier)

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.6626 / 10), 0, 100) = 73.374
```
→ Contribution: 73.374 × 0.40 = **29.350**

**EV/EBIT — 25% weight**
```
EV/EBIT_Score = clamp((18.5552 − 12) / 23 × 100, 0, 100) = 28.501
```
→ Contribution: 28.501 × 0.25 = **7.125**

**Forward PE (fallback formula — 5yr avg only) — 20% weight**
```
Deviation% = (19.1223 − 31.9693) / 31.9693 × 100 = −40.185%
FwdPE_Score = clamp(50 + (−40.185) × 2.5, 0, 100) = clamp(−50.46, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight (Fast Grower confirmed, §4)**
```
PEG       = Forward PE ÷ TTM EPS growth% = 19.1223 ÷ 23.3 = 0.8207
PEG_Score = clamp((0.8207 − 0.5) / 2.0 × 100, 0, 100) = 16.035
```
→ Contribution: 16.035 × 0.15 = **2.405**

**Raw weighted score:**
```
= 29.350 + 7.125 + 0.0 + 2.405
= 38.880
```
**+ Rate Modifier (+10) = 48.880** (before the Upside/Downside Modifier)

---

## 7. MSFT — Upside/Downside Modifier (refreshed at new price)

**Step 0 — Scenario fair value.** No fundamental change occurred since 06-23 (§2), so the bull/base/bear PE multiples, intrinsic growth, and shareholder yield assumptions remain defensible and are **carried forward** — only the live price and the resulting NTM EPS/Gap/E are recalculated.

NTM EPS = Live Price ÷ Forward PE = $368.65 ÷ 19.1223 = **$19.2785** (vs $19.2116 on 06-23 — a small upward drift from blending the two carried-forward EPS-estimate methods at the new price).

| Scenario | Weight | PE applied | Rationale (unchanged from 06-20/06-23 — still defensible, no new information) | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 31.0× | Azure/AI monetization re-accelerates; multiple re-rates to ~5yr average (31.97×). Still below the ~$561–570 analyst consensus PT and far below the $870 high. | $19.2785 × 31.0 = **$597.63** |
| **Base** | 50% | 27.0× | Consensus mid-teens EPS growth (no revision since 06-23) but a haircut multiple vs. the 31.97× 5yr average to reflect litigation overhang, gaming-segment weakness, and capex-margin concerns flagged in §2. | $19.2785 × 27.0 = **$520.52** |
| **Bear** | 25% | 21.0× | Growth decelerates / AI-capex returns disappoint / gaming restructuring costs bite; multiple de-rates near the low end of the 5yr band (24.17×). Bear FV $404.85 remains close to the analyst $400 low PT — downside still underwritten to the Street's worst case. | $19.2785 × 21.0 = **$404.85** |

```
PW Fair Value = 0.25×597.63 + 0.50×520.52 + 0.25×404.85 = $510.88
```
(Probability-Weighted. Sits below the ~$561–570 analyst consensus — still conservative, sanity-check passes. Up modestly from 06-23's $509.11, driven by the slightly higher carried-forward NTM EPS base.)

**Step 1 — Expected annual return E.**
```
Gap Upside %    = (510.88 ÷ 368.65) − 1                = +38.58%
Catalyst window = 2 years  (unchanged — FY26 Q4 late-Jul-2026 print + FY27 Azure/AI re-acceleration
                            cycle; still within Rule 10's 18–24mo horizon → upside credit allowed)
Annualized gap  = 38.58% ÷ 2                            = +19.29%
Intrinsic growth = +13%/yr   (unchanged — deliberately below consensus EPS CAGR of +16–20.7%)
Shareholder yield = +1.96%   (unchanged — dividend ~0.96% + net buyback ~1.0%)

E = 19.29% + 13% + 1.96% = +34.25%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 34.25% ≥ H → M = −15 × clamp((34.25 − 10)/15, 0, 1) = −15 × clamp(1.617, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (the maximum attractive bound, same as 06-20/06-23 — E moved further above the +25%/yr full-credit threshold, so the floor remains robust).

**Guardrail checks:**
1. **Catalyst:** documented (FY26 Q4 earnings + FY27 Azure/AI cycle), within 18–24 months → upside credit allowed. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($510.88) is below the ~$561–570 analyst consensus; bear case underwritten near the $400 low PT. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** at the −15 floor. ✓

---

## 8. MSFT — Final Score & Action

```
Final Score = raw weighted 38.880 + Rate Modifier (+10) + Upside/Downside Modifier (−15)
            = 33.880
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 33.9**

# Final Score: 33.9 → Action band: BUY — Standard position 3–5% (30.0–49.9)

**Did the score change vs. 06-23?** **Yes, marginally** — 34.0 → 33.9 (−0.1 point), driven by the lower live price ($370.00 → $368.65) pulling FCF_Score and EV/EBIT_Score slightly more favorable and the carried-forward NTM EPS edging the Upside/Downside Modifier's expected return calc up, partially offset by the lower 10Y yield (4.50% → 4.38%, no bracket change, slightly *worse* for the Rate Gate spread test direction but still within the same +5 outcome) and a marginally higher PEG. **The action band did NOT change** — still BUY — Standard (30.0–49.9), 4th consecutive session in this band.

---

## 9. Portfolio / Compliance Note (independent of valuation score)

MSFT sits at **~15.01%** per `portfolio/holdings.md` (22 Jun 2026 sync; not recomputed here — weight refresh is `/sync-portfolio`'s responsibility, not `/rescore`'s). This is the same structural concentration issue flagged across the last **6 consecutive sessions** (06-07, 06-11 backfill, 06-12, 06-20, 06-23, and now 06-26). Given broad portfolio price movement since the 06-22 sync, this figure may no longer be precisely current — a fresh `/sync-portfolio` run would be needed to confirm the exact live weight; the open compliance trim from the 2026-06-15 rebalance remains the operative housekeeping action regardless of the exact current percentage.

---

## 10. Order Setup (BUY band requires it — shown, with the gating flags)

Computed for completeness because the score lands in a BUY band, but **note both gates below** — the trade is not actionable, same conclusion as 06-20/06-23.

```
Blended Fair Value (= PW FV):        $510.88
Margin of Safety (Score 30–49.9):    25%   (lower end; wide-moat proven compounder — unchanged rationale)
BUY PRICE (limit):                   $510.88 × (1 − 0.25) = $383.16
  → Live price $368.65 is BELOW the formal buy price (−3.79%) — nominally an actionable entry level.
PRIMARY SELL TARGET (blended FV):    $510.88
BULL-CASE TRIM TARGET (bull × 0.90): $597.63 × 0.90 = $537.87
STOP LOSS (Buy × (1 − 25%)):         $383.16 × 0.75 = $287.37   (below the new 52-week low context $349.20 — a wide structural stop)
R/R at formal entry = (510.88 − 383.16) ÷ (383.16 − 287.37) = 127.72 ÷ 95.79 = 1.33:1
```

**⚠️ R/R = 1.33:1 is BELOW the 2:1 minimum (Rule 6) — unchanged from 06-20/06-23.** Despite ~38.6% upside to fair value (the widest of the three sessions so far), the wide 25% stop makes the reward/risk ratio insufficient using the formal Buy Price as entry. Using the live price ($368.65) directly as entry (stop unchanged at $287.37) improves R/R to **1.75:1** — still below 2:1. Per Rule 6, **R/R below 2:1 = do not enter** even when the score-band says BUY.

**Net:** the same two independent gates each still block adding capital here — (a) the ~15.01% position cap (marginally over, per §9), and (b) sub-2:1 R/R. The BUY-band **score** (33.9) stands and is the headline of this rescore; the **trade** does not execute — identical conclusion to 06-20 and 06-23.

---

## 11. Next Review Trigger

- **Routine:** MSFT FY2026 Q4 earnings (fiscal year ending June 2026), expected **late July 2026** — standard post-earnings re-score (will also refresh the TTM fundamentals reused here for the 7th consecutive session).
- **Open compliance item (6th flag):** dedicated `/rebalance` execution of the position-cap trim; also recommend a fresh `/sync-portfolio` to confirm MSFT's exact current weight given broad price movement since the 06-22 sync (§9).
- **Open methodology item:** Upgrade 1 (Owner Earnings) decision for non-disclosing mega-caps (§3 flag 1).
- **Open tooling item (new):** `yfinance` access failed this session with a `curl_cffi` TLS error through the egress proxy (§3 flag 3) — worth a one-time check whether this is transient or needs a proxy-side fix, since the framework's automated 5yr-PE/FCF-NI-ratio pipeline depends on it.
- **Monitoring items (not Rule 9 triggers):** (1) the BFA Law/Rosen/Robbins Geller securities class action, case No. 26-cv-02071 (lead-plaintiff deadline 11 Aug 2026) — unchanged this session, watch for any escalation; (2) Xbox/gaming division restructuring (~1,000 reported planned layoffs, no formal figures disclosed yet) — watch for management to quantify costs/segment-margin impact at the FY26 Q4 call.
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
