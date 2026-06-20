# RESCORE — MSFT — 2026-06-20

**Task type:** RESCORE (single ticker)
**Date:** 20 Jun 2026
**10Y US Treasury Yield:** 4.46% (Federal Reserve H.15 daily, 18 Jun 2026 — latest published; markets closed since, no fresher print available)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Rate Environment Gate Step 1:** MSFT **FAILS** the Earnings Yield Spread Test (Earnings Yield, the inverse of the price/earnings ratio, minus the 10-Year Treasury yield) → a **separate** +5 additive. **Total Rate Modifier = +10.**
**Purpose of this run:** apply the brand-new **Upside/Downside Modifier (Expected-Return Modifier)** added to the valuation score today, 2026-06-20 (see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md)). This is the first MSFT score to carry it.
**Last review on record:** MSFT 51.2 ([sessions/2026-06-12-rescore-msft-meta.md](2026-06-12-rescore-msft-meta.md)).

---

## 1. Live Price (Rule 0)

| Ticker | Latest price used | Source | Note |
|---|---|---|---|
| **MSFT** | **$378.91** | IBKR `get_price_snapshot` (contract 272093), 20 Jun 2026, `is_close: true`; cross-checked vs `yfinance` `regularMarketPreviousClose` $378.91 (live `currentPrice` $379.40) | **Market closed (Saturday 20 Jun 2026)** — this is the most recent official close, not a stale prior-date note. No intraday quote exists today. |

- **52-week range:** **$356.28 – $555.45** (`yfinance`; IBKR `misc_statistics` reports 52w high $552.28 — used the higher $555.45). The current price sits just **~6.3% above the 52-week low** and **~32% below the 52-week high**.
- **Year-to-date:** **−21.47%** (IBKR `year_to_date_change`).
- **Analyst consensus price target (bull-case sanity check):** mean **$561.39**, median **$555**, high **$870**, low **$400** (55 analysts, `yfinance`). Rating skew strongly positive ("Strong Buy" consensus).
- **Price drift since last review:** $390.97 (12 Jun) → $378.91 = **−3.08%**. Below the 15% Rule 9 threshold — no price-driven fundamental trigger; folded into the re-score via the lower market cap. The full move from the 52-week high is the relevant value-creation event for the new modifier (see §6).

---

## 2. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved (4th consecutive session).** Upgrade 1 requires Owner Earnings = Net Income + Depreciation & Amortization − *Maintenance* Capital Expenditure whenever growth capex exceeds 30% of total capex (mandatory for MSFT). MSFT still discloses **no maintenance-vs-growth capex split**. Computing Owner Earnings would require inventing a maintenance-capex figure (CLAUDE.md prohibits). **Raw TTM Free Cash Flow used** as the FCF_Score input, as in 06-07 / 06-11 / 06-12. Recommend the `decisions/` entry contemplated on 06-12 to formally suspend Upgrade 1 for non-disclosing companies or define an approved proxy.

2. **Fundamentals reused from the 2026-06-12 session (no earnings since).** MSFT's last report was FY26 Q3 (quarter ended 31 Mar 2026); next is FY26 Q4, expected **late July 2026**. No earnings, guidance revision, M&A, or management change has occurred in the 8 days since 06-12, so the SEC-sourced trailing-twelve-month (TTM) fundamentals derived there remain valid and are **reused**, with **only the price (and therefore market cap / enterprise value / yields / multiples) refreshed**. Reused figures: TTM EBIT (operating income) $148.929B, TTM FCF $72.916B, TTM Net Income $125.22B, net debt $24.922B, shares outstanding 7,428,434,704, EPS-growth Fast-Grower status.

3. **5-year average price/earnings (PE) re-computed fresh this session** via the `yfinance` reconstructed-TTM-EPS method: **avg 31.97×, range 24.17×–38.80×** (n=20 quarters) — consistent with the 32.01× used on 06-12. Used **31.97×**.

4. **Forward PE — used 19.86× (refreshed).** `yfinance` live `forwardPE` = 19.61×; backing the prior session's implied next-twelve-months (NTM) earnings estimate out at the new lower price gives 20.11×. Used the midpoint **19.86×** and ran a robustness check across 19.61–20.11 (Step 1 gate and FwdPE_Score unaffected; see §4–§5).

5. **FCF/Net Income conversion ratio** — `yfinance` FY-annual series: 89.6% / 82.2% / 84.0% / 70.3% (FY2022–FY2025). On the TTM-through-Q3-FY26 basis used here it is **58.2%** ($72.916B ÷ $125.22B), below the 70% quality threshold — explained (as in prior sessions) by elevated AI/datacenter growth capex, the Phase 04 monitor's stated carve-out. Not a quality-deterioration signal.

6. **Gross margin / ROIC / Revenue CAGR (compound annual growth rate)** — Phase 01 quality-gate inputs, not Phase 02 score inputs. `yfinance` current snapshot (gross margin 68.3%, return on equity 34.0%, revenue growth 18.3%) shows no deterioration; not separately re-collected. Flagged, not guessed.

7. **Scenario fair value built fresh this session.** No prior MSFT bull/base/bear fair-value model existed (prior rescores stopped at the HOLD-band score with no order setup). The new Upside/Downside Modifier *requires* a probability-weighted fair value, so one is constructed here from first principles (§6) and fully shown.

---

## 3. MSFT — Inputs (price-refreshed)

**Sector:** Technology — Software, Cloud Infrastructure (Azure) & Productivity
**Current portfolio weight:** ~16% (over the 15% cap — see §8; orchestrator owns holdings.md).

| Item | Value | Basis |
|---|---|---|
| Live price | $378.91 | Rule 0, §1 |
| Shares outstanding | 7,428,434,704 | Reused (10-Q FY26 Q3 cover) |
| **Market Cap** | 7,428,434,704 × $378.91 = **$2,814.71B** | Computed |
| Net debt | $24.922B | Reused (10-Q) |
| **Enterprise Value (EV)** | $2,814.71B + $24.922B = **$2,839.63B** | Computed |
| TTM EBIT | $148.929B | Reused |
| **EV/EBIT** | 2,839.63 ÷ 148.929 = **19.07×** | Computed (was 19.67× at $390.97) |
| TTM FCF | $72.916B | Reused |
| **FCF Yield** | 72.916 ÷ 2,814.71 = **2.5905%** | Computed (was 2.51%) |
| TTM Net Income | $125.22B | Reused |
| Forward PE (NTM) | **19.86×** | §2 flag 4 |
| 5yr avg PE (trailing anchor) | **31.97×** (range 24.17–38.80×) | `yfinance`, fresh |
| EPS growth (Fast Grower test) | FY24 +22%, FY25 +15.5%, TTM +23.3% — **all >15% → Fast Grower** | Reused; consensus fwd FY26 +20.7% / FY27 +16% corroborates |
| PEG | **0.85** (19.86 ÷ 23.3) | Computed |
| FCF/NI conversion | 58.2% | §2 flag 5 |
| Net Debt/EBITDA | 0.131× | Reused — well within limits |

---

## 4. MSFT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 19.86 = 5.0352%
Spread = EY − 10Y Treasury = 5.0352% − 4.46% = +0.5752%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.5752%, ~0.92pp short) → **+5 additive**.
*Robustness across Forward PE 19.61–20.11×:* spread ranges +0.51% to +0.64% — FAIL in all cases. The +5 is robust. (The spread improved vs. 06-12's +0.27% — both a slightly lower 10Y, 4.46 vs 4.55, and a lower price help — but still well short of passing.)

**Step 2 — Rate Regime Modifier**
10Y = 4.46% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for MSFT = +10**

---

## 5. MSFT — Full Score Calculation (raw weighted + Rate Modifier)

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.5905 / 10), 0, 100) = 74.095
```
→ Contribution: 74.095 × 0.40 = **29.638**

**EV/EBIT — 25% weight**
```
EV/EBIT_Score = clamp((19.067 − 12) / 23 × 100, 0, 100) = 30.726
```
→ Contribution: 30.726 × 0.25 = **7.6815**

**Forward PE (fallback formula — 5yr avg only) — 20% weight**
```
Deviation% = (19.86 − 31.97) / 31.97 × 100 = −37.88%
FwdPE_Score = clamp(50 + (−37.88) × 2.5, 0, 100) = clamp(−44.70, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0** (the fallback formula folds in the Historical PE Modifier — no separate ±10 applied, per valuation-scoring.md)

**PEG — 15% weight (Fast Grower confirmed, §3)**
```
PEG       = Forward PE ÷ TTM EPS growth% = 19.86 ÷ 23.3 = 0.8524
PEG_Score = clamp((0.8524 − 0.5) / 2.0 × 100, 0, 100) = 17.618
```
→ Contribution: 17.618 × 0.15 = **2.6427**

**Raw weighted score:**
```
= 29.638 + 7.6815 + 0.0 + 2.6427
= 39.9622
```
**+ Rate Modifier (+10) = 49.9622** (before the Upside/Downside Modifier)

---

## 6. MSFT — Upside/Downside Modifier (NEW — required this run)

**Step 0 — Scenario fair value (Rule 7; two-method triangulation, Rule 1/3).**
Anchored on NTM EPS and MSFT's own trailing 5-year PE band (24.17–31.97–38.80×), which is itself the DCF-cross-checking multiples method for a predictable mega-cap compounder. NTM EPS = Live Price ÷ Forward PE = $378.91 ÷ 19.86 = **$19.08**.

| Scenario | Weight | PE applied | Rationale | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 31.0× | Azure/AI monetization re-accelerates; multiple re-rates to ~5yr average. Still **below** the $561 analyst-mean PT and far below the $870 high — deliberately not the rosy point. | $19.08 × 31.0 = **$591.45** |
| **Base** | 50% | 27.0× | Consensus mid-teens EPS growth (FY26 +20.7%, FY27 +16%) but a **haircut multiple vs. the 31.97× 5yr average** to reflect the higher-rate regime. | $19.08 × 27.0 = **$515.13** |
| **Bear** | 25% | 21.0× | Growth decelerates / AI-capex returns disappoint; multiple de-rates near the **low end of the 5yr band** (24.17×) — bear FV $400.66 lands right at the analyst $400 low PT, i.e. downside is underwritten to the Street's worst case. | $19.08 × 21.0 = **$400.66** |

```
PW Fair Value = 0.25×591.45 + 0.50×515.13 + 0.25×400.66 = $505.59
```
(Probability-Weighted. Sits below the $561 analyst mean and $555 median PT — conservative, sanity-check passes.)

**Step 1 — Expected annual return E.**
```
Gap Upside %   = (505.59 ÷ 378.91) − 1            = +33.43%
Catalyst window = 2 years  (FY26 Q4 late-Jul-2026 print + the FY27 Azure/AI re-acceleration cycle;
                            well within Rule 10's 18–24mo horizon → upside credit allowed, no −5 cap)
Annualized gap = 33.43% ÷ 2                        = +16.72%
Intrinsic growth = +13%/yr   (deliberately BELOW consensus EPS CAGR of +16% to +20.7% — conservative)
Shareholder yield = dividend 0.96% + net buyback ~1.0% = +1.96%

E = 16.72% + 13% + 1.96% = +31.68%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 31.68% ≥ H → M = −15 × clamp((31.68 − 10)/15, 0, 1) = −15 × clamp(1.45, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (the maximum attractive bound — E far exceeds the +25%/yr full-credit level).

**Guardrail checks:**
1. **Catalyst:** documented (FY26 Q4 earnings + FY27 Azure/AI cycle), within 18–24 months → upside credit allowed, the −5 upside cap does **not** apply. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($505.59) is below the analyst mean ($561) and median ($555); bear case underwritten to the $400 low PT. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** at the −15 floor. ✓

**Robustness / conservatism sensitivity:** Using a deliberately harsher scenario set (bull 28× / base 25× / bear 20×, growth 11%, same yield) gives PW FV $467.44 and **E = +24.6%**, which still maps to M ≈ −14.5. The modifier is **robust at/near the −15 floor** across a wide range of conservative assumptions — driven by the stock trading ~32% off its 52-week high while consensus EPS growth stays mid-to-high-teens. For M to come *off* the floor (E < 25%), PW FV would have to fall below ~$455 (a multiple band centred well under MSFT's own trough 5yr PE) — not supportable.

---

## 7. MSFT — Final Score & Action

```
Final Score = raw weighted 39.9622 + Rate Modifier (+10) + Upside/Downside Modifier (−15)
            = 34.9622
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 35.0**

# Final Score: 35.0 → Action band: BUY — Standard position 3–5% (30.0–49.9)

**This is the exact behaviour the new modifier was designed to produce.** Under the prior (pre-modifier) engine MSFT scored 51.2 — stuck in the 50.0–69.9 "Fair Value / HOLD" band purely because the four backward-looking sub-scores are ~65–80% anchored on current multiples. The Upside/Downside Modifier folds in the **forward** dimension: a wide-moat compounder trading ~32% below its 52-week high with mid-to-high-teens expected EPS growth carries a large expected annual return (+31.7%), which pulls the score a full band lower into the entry zone. Without the modifier the framework would have refused to recognise the opportunity.

**Did the action CHANGE vs. prior?** **YES** — band moved from **HOLD (51.2)** to **BUY-Standard (35.0)**.

**BUT — the BUY signal collides with the position cap, and with the R/R gate (see §9).** MSFT is already an existing holding at **~16% of the portfolio, over the 15% hard cap (Upgrade 7)**. The framework's hard cap means **no fresh capital may be added regardless of the BUY-band score** — the concentration constraint dominates. Net practical action: **do not add; the open compliance trim still stands** (§8). The BUY-band score is nonetheless the correct, documented signal and is recorded as such.

---

## 8. Portfolio / Compliance Note (independent of valuation score)

MSFT remains **over the 15% hard cap (Upgrade 7)** — ~16% as of the last sync. This is a **structural concentration issue**, not valuation-driven, and is the **4th consecutive session** flagging it (06-07, 06-11 backfill, 06-12, 06-20). The [2026-06-15 rebalance](2026-06-15-rebalance.md) proposed trimming 3 IBKR shares (~$1,185) to land ~14.05%; that compliance trim is the operative action on MSFT, **not** the BUY-band score. A BUY signal that cannot be acted on (cap-blocked) plus an open compliance trim is internally consistent: the framework will not add to an already-over-cap name no matter how attractive the score. *(holdings.md is owned by the orchestrator — not edited here.)*

---

## 9. Order Setup (BUY band requires it — shown, with the gating flags)

Computed for completeness because the score lands in a BUY band, but **note both gates below** — the trade is not actionable.

```
Blended Fair Value (= PW FV):        $505.59
Margin of Safety (Score 30–49.9):    25%   (lower end; wide-moat proven compounder)
BUY PRICE (limit):                   $505.59 × (1 − 0.25) = $379.19
  → Live price $378.91 is ESSENTIALLY AT the buy price (−0.07%) — nominally an actionable entry level.
PRIMARY SELL TARGET (blended FV):    $505.59
BULL-CASE TRIM TARGET (bull × 0.90): $591.45 × 0.90 = $532.31
STOP LOSS (Buy × (1 − 25%)):         $379.19 × 0.75 = $284.39   (just below the 52-week low context $356.28 — a wide structural stop)
R/R at entry = (505.59 − 379.19) ÷ (379.19 − 284.39) = 126.40 ÷ 94.80 = 1.33:1
```

**⚠️ R/R = 1.33:1 is BELOW the 2:1 minimum (Rule 6).** Despite ~33% upside to fair value, the wide 25% stop ($284) makes the reward/risk insufficient. Per Rule 6, **R/R below 2:1 = do not enter** even when the score-band says BUY. To reach 2:1 the entry would need to be lower or the stop tighter than the score-band table permits.

**Net:** two independent gates each block adding capital here — (a) the 15% position cap (already over), and (b) sub-2:1 R/R. The BUY-band **score** (35.0) stands and is the headline of this rescore; the **trade** does not execute.

---

## 10. Next Review Trigger

- **Routine:** MSFT FY2026 Q4 earnings (fiscal year ending June 2026), expected **late July 2026** — standard post-earnings re-score (will also refresh the TTM fundamentals reused here).
- **Open compliance item (4th flag):** dedicated `/rebalance` execution of the ~3-share cap trim (§8).
- **Open methodology item:** Upgrade 1 (Owner Earnings) decision for non-disclosing mega-caps (§2 flag 1).
- **Watch:** if price re-rates toward fair value, the Upside/Downside Modifier shrinks and the score will rise back toward the HOLD band — re-derive at the next earnings print regardless.
```
