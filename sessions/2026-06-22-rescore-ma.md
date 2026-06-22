# RESCORE — MA (Mastercard Incorporated) — 2026-06-22

**Task type:** RESCORE (single ticker)
**Date:** 22 Jun 2026 (Monday — pre-market, US cash session not yet open; figures are the most recent official prints)
**10Y US Treasury Yield:** 4.451% (`^TNX` close 18 Jun 2026 via `yfinance`; no fresher print — markets closed 19 Jun for Juneteenth and the weekend since)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Rate Environment Gate Step 1:** MA **FAILS** the Earnings Yield Spread Test → a **separate** +5 additive. **Total Rate Modifier = +10.**
**Purpose of this run:** quarterly watchlist refresh, and the **first MA score to carry the Upside/Downside Modifier** (added 2026-06-20 — see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md)). Methodology mirrors the [2026-06-20 V rescore](2026-06-20-rescore-v.md), MA's direct duopoly peer and the first session to apply this modifier.
**Last review on record:** MA **53.3** (Fair Value / Watchlist), [watchlist/not-in-portfolio/MA/MA-2026-06-14.md](../watchlist/not-in-portfolio/MA/MA-2026-06-14.md) — computed under the *pre-modifier* engine, using a 10yr-average-only Forward PE fallback (the 5yr-lookback automation only landed 2026-06-20).
**Holding status:** MA is **not held** — absent from [portfolio/holdings.md](../portfolio/holdings.md). This is the watchlist-maintenance use of `/rescore` (per the slash-command's scope); `holdings.md` is not touched this session, and the watchlist update goes to `watchlist/not-in-portfolio/MA/`, not `in-portfolio/`.

---

## 1. Live Price (Rule 0)

| Ticker | Latest price used | Source | Note |
|---|---|---|---|
| **MA** | **$489.79** | `yfinance` `currentPrice`/`regularMarketPrice`. IBKR `get_price_snapshot` (contract ID 38685693, resolved via `search_contracts`) was attempted first per Rule 0 but returned **"OAuth Service Unavailable" (HTTP 503)** → fell back to `yfinance` as the documented Rule-0 fallback (same pattern as the 2026-06-20 V/MSFT sessions). | Last official close, Thu 18 Jun 2026 — market is in pre-market (`marketState: PREPRE`) and has not opened for today's Monday session; Fri 19 Jun was the Juneteenth holiday. |

- **52-week range:** **$464.52 – $601.77** (`yfinance`). Current price sits **~5.4% above the 52-week low** and **~18.6% below the 52-week high**.
- **Analyst consensus price target (bull-case sanity check):** mean **$644.89**, median **$657.50**, high **$735.00**, low **$550.00** (36 analysts, `yfinance`); rating skew **"Strong Buy."** Live price is **~31.6% below the consensus mean PT.**
- **Price drift since last review:** $489.98 (2026-06-14) → $489.79 = **−0.04%**. Far below the 15% Rule 9 threshold — no price-driven trigger; this is a routine watchlist refresh, not an event-driven re-score.

---

## 2. Data Gaps / Flags

1. **IBKR live snapshot unavailable** (OAuth 503 on `get_price_snapshot`) → fell back to `yfinance` per Rule 0's documented fallback path. Cross-checked: `yfinance` `previousClose` ($492.99, Wed 17 Jun close) is internally consistent with the `currentPrice` ($489.79, Thu 18 Jun close) — no data-quality concern, just a stale-by-one-business-day-plus-holiday-weekend quote.

2. **GAAP vs. non-GAAP Operating Income field resolved (carried forward from the 2026-06-14 session's own methodology, re-verified fresh this run).** `yfinance`'s plain "Operating Income" annual field overstates GAAP EBIT (FY2025: $19,514M, implying a 59.5% margin). The correct GAAP-as-filed field is **"Total Operating Income As Reported"** ($18,897M FY2025 → 57.62% margin), which matches Mastercard's publicly reported FY2025 operating margin. **Used "Total Operating Income As Reported" consistently** for all EBIT/EV-EBIT/EBITDA inputs below.

3. **Correction to the prior 2026-06-14 session's CapEx figure.** That session recorded FY2025 CapEx as "$489M" — implausible on its face (below even a single quarter's spend). This session's `yfinance` pull shows FY2025 annual CapEx = **$1,215M**, internally consistent with the sum of the four FY2025 quarterly figures ($357M+$209M+$359M+$290M = $1,215M). **Corrected TTM FCF (period ended 31 Mar 2026) = $17,074M**, cross-checked two independent ways (annual-rollforward method and direct quarterly-sum method — both agree exactly) — vs. the prior session's erroneous $17,801M. Flagging this transparently per CLAUDE.md's "never invent or estimate financial data" — this was a transcription error in the prior session's sourcing, not a re-estimate.

4. **5-year trailing PE band freshly reconstructed** via the documented `yfinance` earnings-dates + price-history method: **avg 36.225×, range 27.695×–54.159×** (n=20 quarters, Jul 2021–Apr 2026). This **supersedes** the 2026-06-14 session's old 10yr-average-only fallback (~37.8×) — the lookback shortened 10yr→5yr framework-wide on 2026-06-20 (see [decisions/2026-06-20-framework-change-5yr-historical-pe-automation.md](../decisions/2026-06-20-framework-change-5yr-historical-pe-automation.md)). Because forward PE (21.501×) sits **below** the 5yr low, the **primary range-based FwdPE formula** is used (not the average-only fallback) — see §5.

5. **Net debt** uses `yfinance`'s reported "Net Debt" balance-sheet line directly: **$11,054M** (Total Debt $18,960M − Cash & equivalents, most recent quarter ended 31 Mar 2026).

6. **First MA session to apply the Upside/Downside Modifier** — no prior MA bull/base/bear scenario model existed (the 2026-06-14 session stopped at the pre-modifier raw+Rate score). Constructed fresh in §6, mirroring the V 2026-06-20 template.

7. **Net buyback yield** (shareholder-yield component) derived from the **3-year** as-reported share-count decline — 956.0M (FY2022) → 894.04M (FY2025) → **~2.21%/yr** — a longer-term average rather than the faster recent-quarter pace (~2.5%/yr over the trailing 12 months), kept conservative and consistent with the multi-year window V used.

8. **Intrinsic growth rate (13%/yr) anchored on Mastercard's own disclosed guidance**, not invented: the company's FY2026 earnings releases (8-K) maintain full-year guidance for adjusted net revenue growth at **"the high end of the low-double-digit to low-teens range"** on a currency-neutral basis. Deliberately used **revenue** guidance (not EPS) as the intrinsic-growth input — this avoids double-counting the buyback-driven EPS uplift already captured separately in shareholder yield (§6), and sits well below the trailing 3yr **EPS** CAGR of 17.36%.
   *Sources: [Mastercard 8-K, FY2026 Q1 earnings release](https://www.sec.gov/Archives/edgar/data/0001141391/000114139126000029/ma03312026-exx991xearnings.htm); [Mastercard 8-K, FY2025 Q4 earnings release](https://www.sec.gov/Archives/edgar/data/0001141391/000114139126000003/ma12312025-exx991xearnings.htm).*

9. **Debt Gate (Hybrid Upgrade 5) passes cleanly.** Mastercard is an asset-light payment network → the relaxed <4× Net Debt/EBITDA threshold applies. Net Debt/EBITDA = **0.531×** ($11,054M ÷ $20,822M TTM EBITDA) — clears even the strict <2.5× standard threshold by ~4.7×. Interest coverage = **26.17×** (FY2025 EBIT $18,897M ÷ interest expense $722M), comfortably above the >15× requirement. Credit ratings: **Aa3 (Moody's) / A+ (S&P), both stable** (per a June 2026 SEC FWP filing) — investment grade. No balance-sheet concern.
   *Source: [Mastercard FWP filing, 4 Jun 2026](https://www.sec.gov/Archives/edgar/data/0001141391/000119312526257761/d148721dfwp.htm).*

10. **FCF/NI conversion quality check passes comfortably.** TTM = 109.66%; annual series FY2022–FY2025 = 101.7% / 97.3% / 105.5% / 109.8% — all above the 70% threshold for all 4 years on record. No earnings-quality concern (Phase 01/04 check).

---

## 3. MA — Inputs (current TTM, period ended 31 Mar 2026)

**Sector:** Payment network (duopoly with Visa) — asset-light financial
**Current portfolio weight:** 0% — not held (watchlist only).

| Item | Value | Basis |
|---|---|---|
| Live price | $489.79 | Rule 0, §1 |
| Shares outstanding | 877.04M | `yfinance` |
| **Market Cap** | **$429,564M** | Computed |
| Net debt | $11,054M | `yfinance` reported Net Debt, §2 flag 5 |
| **Enterprise Value (EV)** | $429,564M + $11,054M = **$440,618M** | Computed |
| TTM EBIT (GAAP, "Total Operating Income As Reported") | $19,655M | Sum of 4 quarters to Mar-2026, §2 flag 2 |
| **EV/EBIT** | 440,618 ÷ 19,655 = **22.418×** | Computed |
| TTM Free Cash Flow (corrected) | $17,074M | §2 flag 3 — cross-checked 2 ways |
| **FCF Yield** | 17,074 ÷ 429,564 = **3.9747%** | Computed |
| TTM Net Income | $15,570M | Sum of 4 quarters to Mar-2026 |
| TTM Revenue | $33,939M | Sum of 4 quarters to Mar-2026 |
| Net margin (TTM) | 45.88% | Computed |
| Operating margin (TTM) | 57.91% | Computed (gross-margin proxy, Phase 01) |
| Forward PE (NTM) | **21.501×** | `yfinance` `forwardPE` (forward EPS $22.7794) |
| 5yr avg PE (trailing anchor) | **36.225×** (range 27.695×–54.159×, n=20 qtrs) | `yfinance`, fresh, §2 flag 4 |
| Revenue 3yr CAGR (FY2022→FY2025) | 13.82% | `yfinance` financials |
| Diluted EPS FY22/23/24/25 | $10.22 / $11.83 / $13.89 / $16.52 | `yfinance` financials |
| EPS growth FY23/24/25 | +15.75% / +17.41% / +18.93% (accelerating) | Computed |
| EPS 3yr CAGR | 17.36% | Computed |
| Fast Grower test | **Pass** — GAAP EPS growth >15% for 3 consecutive years, accelerating, no flagged one-off distortion (carried forward from 2026-06-14 classification, re-verified on fresh data) | Phase 02 / Upgrade 3 |
| PEG | **1.51** (`yfinance` `pegRatio`) | Cross-checks: fwd PE 21.5 ÷ 21.2% fwd earnings growth ≈ 1.01; trailing PE 28.33 ÷ 17.36% 3yr CAGR ≈ 1.63 — reported 1.51 used (mid-range) |
| FCF/NI conversion | 109.66% TTM (97.3–109.8% all of FY22–25) | §2 flag 10 |
| Net Debt/EBITDA | 0.531× | §2 flag 9 (Debt Gate passes) |
| Interest coverage | 26.17× | §2 flag 9 |
| Credit rating | Aa3 (Moody's) / A+ (S&P), stable | §2 flag 9 |

---

## 4. MA — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 21.501 = 4.6509%
Spread = EY − 10Y Treasury = 4.6509% − 4.451% = +0.1999%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.20%, ~1.30 percentage points short) → **+5 additive** (yellow flag, not a veto — 2026-06-07 revision).

**Step 2 — Rate Regime Modifier**
10Y = 4.451% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for MA = +10**

---

## 5. MA — Full Score Calculation (raw weighted + Rate Modifier)

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.9747 / 10), 0, 100) = 60.253
```
→ Contribution: 60.253 × 0.40 = **24.101**
No Owner Earnings (Upgrade 1) adjustment — MA is asset-light; TTM CapEx (~$1.19B) is a small fraction of operating cash flow, nowhere near the 30%-of-total-CapEx growth-capex trigger.

**EV/EBIT — 25% weight (Fast Grower path; PEG carries the other 15%)**
```
EV/EBIT_Score = clamp((22.418 − 12) / 23 × 100, 0, 100) = 45.294
```
→ Contribution: 45.294 × 0.25 = **11.323**

**Forward PE (primary range formula — 5yr low/high) — 20% weight**
```
FwdPE_Score = clamp((21.501 − 27.695) / (54.159 − 27.695) × 100, 0, 100)
            = clamp(−23.403, 0, 100) = 0.000
```
→ Contribution: 0.0 × 0.20 = **0.0**. MA's forward PE sits **below its own 5-year low** (deviation vs. 5yr average = **−40.65%**) — by far the single biggest "cheap" signal in the score, and well past the Upgrade 2 −10% threshold (no Structural Quality Override needed since this is the "cheap," not "expensive," side — that override only gates the +10 penalty).

**PEG — 15% weight (Fast Grower, Upgrade 3)**
```
PEG       = 1.51 (reported)
PEG_Score = clamp((1.51 − 0.5) / 2.0 × 100, 0, 100) = 50.500
```
→ Contribution: 50.500 × 0.15 = **7.575**

**Raw weighted score (Fast Grower path):**
```
= 24.101 + 11.323 + 0.0 + 7.575 = 43.000
```
**+ Rate Modifier (+10) = 53.000** (before the Upside/Downside Modifier)

**Stalwart cross-check (PEG's 15% redistributed to EV/EBIT at 40%):**
```
Raw = 60.253×0.40 + 45.294×0.40 + 0.0×0.20 = 24.101 + 18.118 + 0.0 = 42.219  →  +10 = 52.219
```
Both paths land within ~0.8pt of each other — the classification call does not change the action band (confirmed below).

---

## 6. MA — Upside/Downside Modifier (second MA score to carry it — first dated 2026-06-22)

**Step 0 — Scenario fair value (Rule 7; multiples method).**
Anchored on next-twelve-months (NTM) EPS and Mastercard's own trailing 5-year PE band (27.695×–36.225×–54.159×). NTM EPS = Forward EPS = **$22.7794** (cross-check: Live Price ÷ Forward PE = $489.79 ÷ 21.501 = $22.78 ✓).

| Scenario | Weight | PE applied | Rationale | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 32.5× | Cross-border + Value-Added-Services (cyber/fraud, data analytics) growth reaccelerates; BVNK stablecoin integration becomes a genuine new growth vector rather than a defensive hedge. Multiple re-rates toward the lower-middle of the 5yr band (avg 36.225×) but doesn't fully recover it. FV $740.33 sits just **above** the $735 analyst high PT. | $22.7794 × 32.5 = **$740.33** |
| **Base** | 50% | 28.0× | Consensus low-to-mid-teens EPS growth continues; multiple stays compressed well below the 36.225× 5yr average, reflecting the higher-rate regime and persistent interchange-fee/regulatory overhang. FV $637.82 lands almost exactly at the $644.89 analyst mean / $657.50 median PT — sanity-consistent. | $22.7794 × 28.0 = **$637.82** |
| **Bear** | 25% | 24.0× | Interchange-fee regulatory action or real-time-rail/stablecoin disintermediation pressure compresses the multiple further, below the 5yr low. FV $546.71 lands just under the $550 analyst low PT — downside underwritten. | $22.7794 × 24.0 = **$546.71** |

```
PW Fair Value = 0.25×740.33 + 0.50×637.82 + 0.25×546.71 = $640.67
```
(Probability-Weighted. Sits ~0.6% below the $644.89 analyst mean PT — conservative; sanity check passes.)

**Step 1 — Expected annual return E.**
```
Gap Upside %     = (640.67 ÷ 489.79) − 1                 = +30.805%
Catalyst window  = 2 years (MA Q2 2026 earnings, late Jul/early Aug 2026, + the FY2027
                   cross-border/VAS growth cycle and continued BVNK integration;
                   within Rule 10's 18–24mo horizon → upside credit allowed, no −5 cap)
Annualized gap   = 30.805% ÷ 2                            = +15.403%
Intrinsic growth = +13.0%/yr  (Mastercard's own disclosed currency-neutral net revenue
                   growth guidance — "high end of low-double-digit to low-teens" — §2 flag 8;
                   deliberately BELOW the +17.36% 3yr GAAP EPS CAGR to avoid double-counting
                   the buyback contribution already in shareholder yield below)
Shareholder yield = dividend 0.71% + net buyback ~2.21%/yr = +2.92%

E = 15.403% + 13.0% + 2.92% = +31.323%
```
(Net buyback ~2.21%/yr derived from the 3yr as-reported share-count decline 956.0M → 894.04M, FY2022→FY2025 — §2 flag 7.)

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 31.323% ≥ H → M = −15 × clamp((31.323 − 10)/15, 0, 1) = −15 × clamp(1.4215, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (the maximum attractive bound — E exceeds the +25%/yr full-credit level).

**Guardrail checks:**
1. **Catalyst:** documented (Q2 2026 earnings + FY2027 cross-border/VAS growth cycle + BVNK integration milestones), within 18–24 months → upside credit allowed; the −5 upside cap does **not** apply. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($640.67) sits just below the analyst mean/median ($644.89/$657.50), not the bull case; bear underwritten just under the $550 low PT. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** at the −15 floor. ✓

**Robustness sensitivity:** A harsher scenario set (bull 30×/base 26×/bear 22×, intrinsic 11%) gives PW FV $592.26, gap +20.92%, **E ≈ +24.38% → M ≈ −14.38**. A very-harsh set (28/24/20×, intrinsic 9%) gives PW FV $546.71, gap +11.62%, **E ≈ +17.73% → M ≈ −7.73**. The modifier stays meaningfully negative across a wide range of conservative assumptions — driven by the forward PE sitting ~41% below the 5yr average while EPS growth runs mid-to-high-teens with a ~2.9% shareholder yield.

---

## 7. MA — Final Score & Action

```
Final Score = raw weighted 43.000 + Rate Modifier (+10) + Upside/Downside Modifier (−15)
            = 38.000
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 38.0** (Fast Grower path).
*Stalwart cross-check:* 42.219 + 10 − 15 = 37.219 → **37.2**. Same action band.

# Final Score: 38.0 → Action band: BUY — Standard position 3–5% (30.0–49.9)

**Did the action CHANGE vs. prior?** **YES** — band moved from **WATCHLIST / Fair Value (53.3)** to **BUY-Standard (38.0)**. Under the prior (pre-modifier, pre-5yr-PE) engine, MA was stuck in the 50.0–69.9 "Fair Value / Watchlist" band purely because the four backward-looking sub-scores are mostly anchored on current/trailing multiples. The Upside/Downside Modifier folds in the **forward** dimension: a wide-moat duopoly compounder trading ~18.6% below its 52-week high and ~31.6% below the consensus mean PT, with mid-to-high-teens EPS growth plus a ~2.9% shareholder yield, carries a large expected annual return (+31.3%), pulling the score a full band lower into the entry zone. This is the same effect the modifier produced for V on 2026-06-20 — expected given the two are direct duopoly peers with similar trailing-multiple compression and similar forward growth profiles.

**BUT — the BUY signal does not fully execute, on the R/R gate (see §8):** the new-entry **R/R is below the 2:1 minimum** at the band-required stop. The BUY-band *score* is the correct, documented signal and is recorded as such; the *trade* requires a limit order at a tighter entry than the live price (see below).

---

## 8. Order Setup (BUY band requires it — shown, with the gating flag)

```
Blended Fair Value (= PW FV):        $640.67
Margin of Safety (Score 30–49.9):    25%   (lower end of the 25–30% band; wide-moat proven duopoly compounder, Rule 8)
BUY PRICE (limit):                   $640.67 × (1 − 0.25) = $480.50
  → Live price $489.79 is ~1.9% ABOVE the buy price → a LIMIT order at $480.50, not a market entry.
PRIMARY SELL TARGET (blended FV):    $640.67
BULL-CASE TRIM TARGET (bull × 0.90): $740.33 × 0.90 = $666.30
STOP LOSS (Buy × (1 − 25%)):         $480.50 × 0.75 = $360.38
R/R at buy entry = (640.67 − 480.50) ÷ (480.50 − 360.38) = 160.17 ÷ 120.12 = 1.33:1
```

**⚠️ R/R = 1.33:1 is BELOW the 2:1 minimum (Step 6 — Verify Risk/Reward, [fair-value-methodology.md](../framework/fair-value-methodology.md)).** Despite ~30.8% upside to fair value, the band-mandated 25% MoS combined with a 25% stop is structurally limited to ~1.33:1 R/R regardless of the absolute price level (the two percentages cancel out: MoS% ÷ ((1−MoS%) × Stop%) = 0.25 ÷ (0.75 × 0.25) = 1.33, identical to the same structural outcome the V rescore hit on 2026-06-20). Per the order-setup checklist, **R/R below 2:1 = do not enter** even when the score-band says BUY. To reach 2:1 the entry would need to be lower, or the stop tighter, than the Step 2/Step 4 band tables permit at these MoS levels.

**Net:** the BUY-band **score (38.0)** stands and is the headline of this rescore; the **trade does not fully execute as a market order** — live price ($489.79) sits ~1.9% above the $480.50 limit buy price, and even at that limit the R/R is sub-2:1. MA remains watchlist-only in practice; a **limit order at $480.50** is the documented actionable level, with the explicit caveat that R/R discipline argues against sizing up to the full 3–5% even if filled, pending a tighter stop or lower entry.

---

## 9. Next Review Trigger

- **Routine:** MA's Q2 2026 earnings release, expected **late July/early August 2026** — standard post-earnings re-score (refreshes TTM fundamentals, adds a 4th consecutive accelerating-EPS data point).
- **Limit-order watch:** the modifier turns the score into a genuine BUY signal; the binding constraint is R/R, not conviction. If MA trades toward or through the **$480.50 buy price**, re-run the order setup — a lower entry tightens R/R toward 2:1 and could make a starter add actionable.
- **Watch:** if price re-rates toward fair value, the Upside/Downside Modifier shrinks and the score rises back toward the Hold/Watchlist band — re-derive at the next earnings print regardless.
- **Rule 9 triggers:** any guidance revision, interchange-fee/regulatory ruling, M&A (continued BVNK integration), or management change; a 10Y Treasury decline below 3.5% (Step 2 modifier would drop +5 → 0); or a >15% unexplained price move from $489.79.

---

## Glossary

- **bps (basis points)**, **CAGR**, **CapEx**, **D&A**, **EBIT**, **EBITDA**, **EPS**, **EV**, **EV/EBIT**, **EY (Earnings Yield)**, **Fast Grower**, **FCF**, **FCF Yield**, **FCF/NI conversion ratio**, **Forward PE**, **FV (Fair Value)**, **GAAP**, **Hurdle rate**, **Interest coverage (ratio)**, **Investment grade**, **IRR**, **M&A**, **Moat**, **MoS (Margin of Safety)**, **Net Debt/EBITDA**, **NI (Net Income)**, **PE ratio**, **PEG ratio**, **pp (percentage points)**, **PT (Price Target)**, **R/R (Risk/Reward ratio)**, **ROIC**, **Shareholder yield**, **TAM**, **Treasury yield (10Y)**, **TTM (Trailing Twelve Months)**, **WACC** — see [glossary.md § General financial & valuation terms](../framework/glossary.md#general-financial--valuation-terms).
- **Catalyst window**, **Debt Gate**, **Hybrid Upgrade**, **Phase 01–06**, **PW (Probability-Weighted) Fair Value**, **Qualified Quality List**, **Rate Environment Gate**, **Rate Regime Modifier**, **Structural Quality Override**, **Upside/Downside Modifier (Expected-Return Modifier)** — see [glossary.md § Framework-specific terms](../framework/glossary.md#framework-specific-terms).
