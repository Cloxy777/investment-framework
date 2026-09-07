# RESCORE — ZS (Zscaler, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-09-07 (Monday — most recent trading session 2026-09-04, ahead of the weekend; note fiscal Q4 FY2026 earnings released 2026-09-03 after this window's last daily bar)
**10Y US Treasury Yield:** 4.784% (`yfinance` `^TNX`, 2026-09-04 close — most recent available)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** ZS Valuation 43.1 / Quality 59.4 / Composite 41.9 (reference only) — 2026-07-05, [sessions/2026-07-05-rescore-zs.md](2026-07-05-rescore-zs.md)
**Current ZS portfolio weight:** 0.27% per [holdings.md](../portfolio/holdings.md) — not recomputed this session (weight refresh is `/sync-portfolio`'s job).
**Special case (unchanged):** ZS is held as a **Human Override** — fails the Phase 01 quality gate. `portfolio/override-log.md` **still has no ZS entry** despite this being cited repeatedly as the basis for the position — re-flagging, not resolved here (out of scope for `/rescore`).

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$169.80** | IBKR `get_price_history` (contract_id 310621426, NASDAQ), most recent daily bar close = **2026-09-04**. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$169.03** (`is_close: false`) — same recurring stale/partial-tick pattern flagged in prior sessions. Cross-checked against `yfinance` — `marketCap` (163,054,698 shares × price) backs out to **$169.80**, confirming the daily-bar close is the correct live price. |
| 52-week range | $114.625 – $336.99 | IBKR `misc_statistics` |
| Analyst consensus PT | mean **$206.34**, median $210.00, range $155–$250, n=43 | `yfinance` `targetMeanPrice`/`targetMedianPrice`/`targetLowPrice`/`targetHighPrice` — bull-case sanity check only, not scored. |
| Price vs. 07-05 review ($147.33) | **+15.25%** | Right at the Rule 9 ±15% threshold — see §2; explained by the Q4 earnings beat + volatile post-earnings trading, not investigated as an independent trigger. |
| Within-week volatility | $188.38 (08-31 close) → peak $190.47 (08-31 intraday high) → $169.80 (09-04 close), a **-9.9%** slide off the week's high | Likely "sell the news": Q4 beat (non-GAAP EPS $1.19 vs $1.09 est) but FY2027 guidance implies further growth deceleration (~17% vs TTM 25%) — see §3. |

---

## 2. Rule 9 Trigger Check (2026-07-05 → 2026-09-07)

| Trigger | Found? | Detail |
|---|---|---|
| **Quarterly earnings** | **YES — mandatory trigger** | Fiscal Q4 FY2026 (quarter ended 2026-07-31) reported **2026-09-03**. Revenue $898.2M (+24.9% YoY), GAAP net loss $(3.4)M (vs. $(17.6)M Q4 FY2025), non-GAAP EPS $1.19 vs. $1.09 consensus (+9.2% surprise). Full FY2026 revenue $3,352.5M (+25.4% YoY). This session is the scheduled response to that trigger. |
| Guidance revision | **YES, informational** | FY2027 guidance: revenue $3.908B–$3.938B (midpoint growth ~17.0% YoY), ARR $4.396B–$4.426B (~17% growth) — a continuation of the already-documented deceleration trend (07-05 session flagged 34.8%→25.4%→24.6%(then-est)→17.0%(then-est); now-actual FY2026 growth landed at 25.4%, next FY guided to ~17%). Feeds the Growth sub-score modifier below (§5), not scored as its own line item per [valuation-scoring.md](../framework/valuation-scoring.md) "Why Forward Guidance Is Not a Sub-score." |
| M&A | No | None found. |
| Management change | No | None found. |
| Macro shift | No | 10Y at 4.784% (07-02: 4.485%) — still inside "3.5–5%" bracket, no Rate Regime bracket change. |
| **>15% unexplained price move** | **Move found (+15.25%), explained** | Price rose $147.33 → $169.80 (+15.25%) over the window, entirely attributable to the documented Q4 earnings beat and subsequent volatile post-earnings trading (up to $190.47 intraday, back down to $169.80) — a known, fundamentally-grounded event, not an independent unexplained-move trigger. |

**Conclusion: the scheduled quarterly-earnings trigger fired as expected.** Full re-score below uses the new FY2026 fiscal-year-end (2026-07-31) financials, which — for ZS's July fiscal year-end — constitute the fresh TTM window in full.

---

## 3. Data Gaps / Flags

1. **yfinance quarterly financials/balance sheet/cashflow had not yet ingested the FY2026 Q4 filing** at the time of this session (still showing 2026-04-30 as the latest quarter, 4 days after the 2026-09-03 earnings release). **Sourced the Q4/FY2026 GAAP figures directly from Zscaler's SEC 8-K exhibit 99.1** ([zs-07312026_991.htm](https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-07312026_991.htm)) instead of inventing or estimating — consistent with "never invent or estimate financial data." `yfinance`'s `info` dict (market cap, shares outstanding, forward EPS, analyst estimates/PTs) was current and used normally.
2. **ZS's fiscal year ends July 31** — the just-closed FY2026 (Aug 2025–Jul 2026) *is* the fresh TTM window; no separate quarterly roll-forward was needed for revenue/EBIT/NI/OCF/CapEx/FCF (used the FY2026 annual GAAP totals directly, cross-checked against `yfinance`'s existing TTM-equivalent fields where already populated — matched within rounding on revenue, net income, operating cash flow).
3. **Debt definition — continuity choice.** Zscaler's balance sheet as of 2026-07-31 shows only one interest-bearing item, convertible senior notes ($1,696.355M), with **no finance lease liabilities**. Prior sessions used `yfinance`'s `totalDebt` field, which historically bundled operating lease liabilities ($1,868.16M vs. converts-only ~$1,696M at the time). For continuity with that established treatment, this session again includes operating lease liabilities (current $64.894M + noncurrent $94.575M = $159.469M) alongside the converts, giving **Total Debt = $1,855.824M**. This doesn't change any qualitative conclusion — ZS is net cash either way, comfortably clearing the Balance Sheet hard disqualifier and scoring 100.0 on that sub-score under either definition.
4. **EBITDA reconstructed from GAAP operating loss + D&A**, consistent with the prior session's quarterly-summation method: Q4 FY2026 D&A ($42.933M) + amortization of acquired intangibles ($12.280M) = $55.213M add-back to Q4's $(15.5)M operating loss → Q4 EBITDA $39.713M; summed with the three already-reported FY2026 quarters (Q1–Q3: $35.037M + $26.941M + $49.786M) → **TTM EBITDA = $151.477M**. `yfinance`'s own `info["ebitda"]` field (only $43.85M) again disagrees, likely a different/stale definition — the directly-summed method is used for consistency with prior sessions, same divergence flagged in 07-05.
5. **EV/EBIT placeholder re-verified, unchanged.** FY2026 GAAP operating income is still negative ($(133.3)M) → EV/EBIT remains genuinely undefined → neutral 50.0 placeholder, PEG's 15% weight still redistributed to EV/EBIT (ZS has never had a GAAP-profitable fiscal year — FY2022 through FY2026 all show GAAP net losses, so the Fast-Grower/PEG "clean earnings base" test still fails, per the 07-05 session's reasoning, unchanged).
6. **FCF/Net Income hard-disqualifier — same unresolved interpretive flag as 07-05, doesn't change the outcome.** FY2026 NI is again negative ($(63.2)M) against strongly positive FCF ($779.1M) — the literal "ratio <70% for 2+ years" reading is met on a negative-NI base, but as flagged before, the rule's evident intent (catching *positive* NI failing to convert to cash) doesn't fit this reverse pattern. Not resolved here; doesn't change the conclusion (Quality Score already fails the gate by a wide margin independent of this question).
7. **`override-log.md` still has no ZS entry** — re-flagging the gap first identified 2026-07-05. Recommend the user/orchestrator add the retroactive Human Override entry; not resolved by `/rescore` (out of scope).
8. **Moat Signal evidence carried forward from 07-05** (Gartner MQ SSE leadership, 35%+ price increases with DBNR holding at 114%, documented data-network-effect at 500B+ daily transactions, contractual/integration switching costs) — no new moat-relevant evidence surfaced this session; re-verified the underlying facts haven't reversed (still a SSE Leader per latest available Gartner cycle, no reported customer-base contraction). Scale cost advantage still declined (vendor-marketing-only source, same as before).

---

## 4. ZS — Inputs Collected (fresh this session, `yfinance` + IBKR + Zscaler 8-K/SEC filing for FY2026 Q4)

**Sector:** Technology — Cybersecurity (Zero Trust / SaaS)

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 163,054,698 | `yfinance` `sharesOutstanding` |
| **Market Cap** | 163,054,698 × $169.80 = **$27,686.69M** | Computed — matches `yfinance` `marketCap` ($27,686,688,768) essentially exactly |
| Total debt (2026-07-31, converts + operating leases) | $1,855.824M | SEC 8-K balance sheet (converts $1,696.355M + operating lease liabilities $64.894M + $94.575M) — see §3 flag 3 |
| Cash + ST investments (2026-07-31) | $3,474.15M | SEC 8-K balance sheet ($928.4M cash + $2,545.8M ST investments) — matches `yfinance` `totalCash` |
| **Net Cash** | $3,474.15M − $1,855.824M = **$1,618.33M** | Computed |
| **EV** | $27,686.69M − $1,618.33M = **$26,068.36M** | Computed |
| FY2026 GAAP Operating Income (EBIT) | **−$133.3M** | SEC 8-K income statement — full fiscal year = TTM for ZS's July fiscal year-end |
| TTM EBITDA (Op Income + D&A, quarterly-summed) | **$151.477M** | SEC 8-K cash-flow D&A/intangible-amortization lines (§3 flag 4) |
| FY2026 Operating Cash Flow | **$1,129.7M** | SEC 8-K cash flow statement — matches `yfinance` `operatingCashflow` |
| FY2026 CapEx | **$350.5M** | SEC 8-K cash flow statement |
| **FY2026 FCF** | $1,129.7M − $350.5M = **$779.1M** | SEC 8-K — used over `yfinance`'s `freeCashflow` field ($1,074.9M), which disagrees materially and appears to use a narrower capex definition; official filing figure used per "never invent" |
| **FCF Yield** | $779.1M ÷ $27,686.69M = **2.814%** | Computed |
| FY2026 GAAP Net Income | **−$63.2M** | SEC 8-K — matches `yfinance` `netIncomeToCommon` ($−63.179M) |
| FY2026 Revenue | **$3,352.5M** | SEC 8-K — matches `yfinance` `totalRevenue` |
| Net Margin (TTM) | −$63.2M ÷ $3,352.5M = **−1.885%** | Computed — matches `yfinance` `profitMargins` (−0.01885) |
| Effective tax used for NOPAT | **21%** statutory rate — FY2026 pretax loss $(17.1)M against a *positive* tax provision $46.0M, the same near-zero/negative-pretax distortion flagged in 07-05 (and CSGP 07-04) | SEC 8-K |
| **NOPAT** | −$133.3M × (1 − 0.21) = **−$105.307M** | Computed |
| Stockholders' Equity (2026-07-31) | $2,598.3M | SEC 8-K balance sheet |
| **Invested Capital** (Debt + Equity − Cash) | $1,855.824M + $2,598.3M − $3,474.15M = **$979.97M** | Computed |
| **ROIC (TTM)** | −$105.307M ÷ $979.97M = **−10.75%** | Computed |
| Gross Margin (FY2026) | $2,574.9M ÷ $3,352.5M = **76.81%** | SEC 8-K — brackets `yfinance` `grossMargins` (76.87%) |
| Revenue 3yr CAGR (FY2023 $1,616.95M → FY2026 $3,352.52M) | (3,352.52/1,616.95)^(1/3) − 1 = **27.51%** | `yfinance` annual financials + SEC 8-K FY2026 total |
| Revenue growth trend (deceleration evidence) | Trailing 3yr CAGR 27.5% → FY2026 actual YoY 25.4% → most recent quarter (Q4 FY26) YoY 24.9% → **FY2027 guidance ~17.0%** (management's own guided midpoint, $3.908–3.938B vs. FY2026's $3,352.5M... consistent with ARR guide of ~17%) | SEC 8-K + Zscaler FY2027 guidance (press release) — a consistent, multi-point, now partly-actualized deceleration |
| Forward EPS (NTM, non-GAAP consensus, "+1y") | $5.589 | `yfinance` `earnings_estimate` |
| **Forward PE** | $169.80 ÷ $5.589 = **30.39×** | Computed |
| 3yr post-bubble avg/range PE (12 quarters, non-GAAP EPS reconstruction) | avg **62.94×**, range 32.08×–89.75× | `get_earnings_dates` + price-history reconstruction — refreshed window (rolled forward one quarter from the 07-05 session's 67.02× avg) |
| FCF/NI conversion (TTM) | $779.1M / −$63.2M = **−1232.8%** | Computed — negative because NI is negative, not poor cash conversion (§3 flag 6) |
| Diluted avg shares (FY2023 → FY2026) | 144.942M → 160.2M | `yfinance` annual financials (FY2023) + SEC 8-K (FY2026 diluted) — CAGR = (160.2/144.942)^(1/3)−1 = **+3.39%/yr** dilution |
| Dividend yield | None (no dividend) | `yfinance` |

---

## 5. ZS — Quality Score (2026-06-29 methodology, rolling TTM window)

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | Ratio negative every year FY2022–2026 and TTM (NI never positive) | disqualify if <70% for 2+ yrs *without* a growth-capex explanation | ⚠️ **Same ambiguous flag as 07-05 — literally met, but the rule's evident intent doesn't fit this reverse (negative-NI, strongly-positive-FCF) pattern.** Not resolved; doesn't change the outcome below. |
| Net Debt/EBITDA over threshold? | **Net cash** ($1,618.33M net cash vs. $151.477M TTM EBITDA) | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive every year FY2022–2026 ($231.3M / $333.6M / $585.0M / $726.7M / $779.1M) | disqualify if not | ✅ PASS |

### Profitability (25% weight)
```
Net Margin (TTM)     = −1.885%
NetMargin_Component  = clamp((−1.885/30)×100, 0, 100) = 0.0   (negative, floored)

ROIC (TTM)            = −10.75%
ROIC_Component        = clamp((−10.75/30)×100, 0, 100) = 0.0   (negative, floored)

Profitability_Score   = (0.0 + 0.0) / 2 = 0.0
```
FCF-positive-3yr cap doesn't bind — already 0.0.

### Margins (15% weight)
```
Gross Margin (TTM) = 76.81%
GrossMargin_Score = clamp((76.81/80)×100, 0, 100) = 96.01
```

### Growth (20% weight)
```
Revenue 3yr CAGR (FY2023 $1,616.95M → FY2026 $3,352.52M) = 27.51%
Growth_Score (raw) = clamp((27.51/25)×100, 0, 100) = clamp(110.04, 0, 100) = 100.0
```
**−10 (documented structural deceleration, cited):** trailing 3yr CAGR 27.5% → FY2026 actual YoY 25.4% → Q4 FY26 YoY 24.9% → **management's own FY2027 guidance ≈17.0%** — a consistent, now partly-actualized multi-point deceleration (extends the same trend flagged in 07-05, one data point more confirmed).
```
Growth_Score (with modifier) = clamp(100.0 − 10, 0, 100) = 90.0
```

### Balance Sheet (15% weight)
```
Net Debt/EBITDA = −$1,618.33M / $151.477M = −10.68× (net cash)
BalanceSheet_Score = clamp(100×(1 − (−10.68)/4), 0, 100) = clamp(367.0, 0, 100) = 100.0
```

### Moat Signal (15% weight) — evidence carried forward, re-verified not reversed (§3 flag 8)

| Signal | Marked | Basis |
|---|---|---|
| Market share stable/growing | **TRUE** | SSE Leader (Gartner MQ), large enterprise customer base — re-verified not reversed this session. |
| Brand premium | **TRUE** | 35%+ list-price increase absorbed with DBNR holding at 114% TTM (07-05 evidence, no contrary signal found this session). |
| Network effect | **TRUE** | Documented shared-telemetry threat-intelligence flywheel (500B+ daily transactions), unchanged mechanism. |
| Switching costs | **TRUE** | Deep architecture integration + 12–36-month contracts, unchanged mechanism. |
| Scale cost advantage | **FALSE** | Still only vendor-marketing-sourced, not independent cost-per-unit data — declined to credit, same as 07-05. |

```
Moat_Score = (4/5) × 100 = 80.0
```

### FCF Quality (10% weight)
```
FCF/NI (TTM) = $779.1M / −$63.2M = −1232.8%
FCFQuality_Score = clamp(((−12.328 − 0.40)/0.60)×100, 0, 100) = clamp(−2121.3, 0, 100) = 0.0
```
Same mechanical-artifact caveat as 07-05 — a negative-NI denominator, not evidence of poor cash conversion (FY2026 FCF $779.1M against a small GAAP loss).

### Quality Score — Final
```
Quality Score = (0.0×0.25) + (96.01×0.15) + (90.0×0.20) + (100.0×0.15) + (80.0×0.15) + (0.0×0.10)
              = 0.000 + 14.4015 + 18.000 + 15.000 + 12.000 + 0.000
              = 59.4015 → rounds to 59.4
```

# Quality Score = 59.4 — FAILS the 80.0+ gate (by 20.6 points — unchanged from 07-05, decisively).

Directionally and numerically unchanged from the 07-05 computation (59.388→59.4 then, 59.4015→59.4 now) — the underlying drivers (negative GAAP profitability, SBC-driven zero FCF-Quality score, one point of confirmed growth deceleration) haven't shifted materially in one quarter.

---

## 6. ZS — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 30.39 = 3.2905%
Spread = EY − 10Y Treasury = 3.2905% − 4.784% = −1.4935%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−1.49%, ~2.99pp short) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.784% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for ZS = +10**

---

## 7. ZS — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.814/10), 0, 100) = 71.86
```
→ Contribution: 71.86 × 0.40 = **28.745**

**EV/EBIT — 25% + 15% (PEG redistributed, §3 flag 5) = 40% weight**
```
EV/EBIT_Score = 50.0  (neutral placeholder — TTM GAAP EBIT still negative, −$133.3M)
```
→ Contribution: 50.0 × 0.40 = **20.000**

**Forward PE (fallback formula — 3yr post-bubble avg) — 20% weight**
```
Deviation% = (30.39 − 62.94)/62.94 × 100 = −51.72%
FwdPE_Score = clamp(50 + (−51.72)×2.5, 0, 100) = clamp(−79.31, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight: N/A this session** (ZS has never had a GAAP-profitable fiscal year — FY2022–2026, unchanged) — weight redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 28.745 + 20.000 + 0.0 = 48.745
```
**+ Rate Modifier (+10) = 58.745** (before the Upside/Downside Modifier)

---

## 8. ZS — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture (Rule 7 bull/base/bear), built from live consensus data (§4):**

| Scenario | Weight | EPS (non-GAAP consensus, FY+1) | Exit multiple | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $6.78 (FY+1 high estimate) | ~36.9× | Growth re-accelerates, AI-security narrative sustains a partial re-rate toward (not to) the 62.9× 3yr average; anchored to, not exceeding, the $250 analyst high PT (Rule 7 guardrail). | **$250** |
| **Base** | 50% | $5.589 (FY+1 avg estimate) | ~37.6× | Consensus path; multiple sits between the current 30.4× trough and the 62.9× 3yr average, matches the $210 analyst median PT. | **$210** |
| **Bear** | 25% | $4.68 (FY+1 low estimate) | ~32.1× (no re-rating credit — current trough multiple held) | Growth decelerates per management's own FY2027 guidance (~17%); multiple compresses to today's cycle low, no recovery. Sits at/below the $155 analyst low PT — an honestly underwritten downside (Rule 7 guardrail). | **$150** |

```
PW Fair Value = 0.25×250 + 0.50×210 + 0.25×150 = 62.5 + 105.0 + 37.5 = $205.00
```
Sanity check (Rule 4): base ($210) matches the analyst median exactly; bull ($250) matches the analyst high PT exactly, not exceeding it; bear ($150) sits just below the analyst low PT ($155) — appropriately conservative downside underwriting.

**Step 1 — Expected annual return E.**
```
Gap Upside %      = (205.00 ÷ 169.80) − 1                = +20.73%
Catalyst window   = 2 years (Rule 10 default — ongoing Zero Trust/SASE
                    adoption cycle, routine Nov 2026 earnings checkpoint)
Annualized gap    = 20.73% ÷ 2                            = +10.37%/yr
Intrinsic growth  = +13.83%/yr  (FY+1 consensus EPS growth, `yfinance` growth_estimates —
                    directly-sourced, not inferred)
Shareholder yield = −3.39%/yr  (no dividend; diluted share count CAGR FY2023→FY2026 = +3.39%/yr
                    from SBC-driven dilution → negative buyback yield, honestly counted)

E = 10.37% + 13.83% + (−3.39%) = +20.81%/yr
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 20.81% ≥ H  →  M = −15 × clamp((20.81 − 10)/15, 0, 1) = −15 × clamp(0.7207, 0, 1) = −15 × 0.7207 = −10.81
```
**Modifier M = −10.81** — smaller (less attractive) than 07-05's −12.0: the price rally (+15.25% since 07-05) narrowed the gap to the updated (also higher) fair value.

**Guardrail checks:**
1. **Catalyst:** documented (Zero Trust/SASE adoption cycle, quarterly earnings checkpoints) → upside credit allowed. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($205.00) matches, not exceeds, the analyst median; bull matches (not exceeds) the analyst high PT; bear sits below the analyst low PT. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** −10.81 sits within bounds. ✓

---

## 9. ZS — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (48.745) + Rate Modifier (+10) + Upside/Downside (−10.81)
                       = 47.935
```
Boundary rule: 47.935 rounds to **47.9** (below the .X5 threshold of 47.95).

| | Value |
|---|---|
| Raw weighted | 48.745 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −10.81 (E = +20.81%) |
| **FINAL VALUATION SCORE** | **47.9** |
| Prior valuation score | 43.1 (07-05) |
| **Quality Score** | **59.4 (FAILS 80.0+ gate by 20.6 points — unchanged, see §5)** |

**Valuation Score band: 47.9 → 30.0–49.9 "Cheap" → nominally BUY, Standard 3–5%** — but see §10: independently gated by the Quality Score fail, R/R discipline, and override status, unchanged from 07-05.

**Composite Score — reference only, per established practice for a Quality-Score-gate failure on an existing holding:**
```
Composite Score = 0.50×(100 − 59.4) + 0.50×47.9 = 0.50×40.6 + 0.50×47.9 = 20.3 + 23.95 = 44.25 → rounds up to 44.3
```
**Composite Score = 44.3 — lands in the "BUY — Standard position 3–5%" band, the same false-green-light pattern flagged in 07-05.** Not adopted to drive the action recommendation.

---

## 10. ZS — Action Recommendation

**Three independent facts, any one of which alone is enough to conclude HOLD/no-add — unchanged from 07-05:**

1. **Quality Score (59.4) fails the 80.0+ gate decisively** (20.6 points below the bar, unchanged this quarter).
2. **ZS is a pre-existing Human Override** for exactly this quality-gate fail — any *addition* would need fresh override documentation and explicit human sign-off.
3. **Order-setup R/R independently fails the 2:1 minimum anyway** (shown below).

**Order setup — shown for completeness, testing the nominal Buy-Standard (30.0–49.9) band:**
```
Blended Fair Value (= PW FV):              $205.00
Margin of Safety (30.0–49.9 band, top of range given persistent GAAP losses): 30%
BUY PRICE (limit):                         $205.00 × (1 − 0.30) = $143.50
PRIMARY SELL TARGET:                       $205.00
BULL-CASE TRIM TARGET (bull × 0.90):       $250 × 0.90 = $225.00
STOP LOSS (Buy × (1 − 28%)):               $143.50 × 0.72 = $103.32
R/R at formal entry = (205.00 − 143.50) ÷ (143.50 − 103.32) = 61.50 ÷ 40.18 = 1.531:1  ❌ below 2:1
R/R at live price   = (205.00 − 169.80) ÷ (169.80 − 103.32) = 35.20 ÷ 66.48 = 0.530:1  ❌ far below 2:1
```
To clear 2:1 at a 28% stop, entry would need to be ≈**$131.41** (≈36% MoS) — well below current price, near the 52-week low ($114.625) but not at it. **Both R/R checks fail (Rule 6) — do not enter, independent of the Quality Score question.**

**Net: HOLD the existing 0.27% override position. No fresh capital added** — blocked by three independent gates (Quality Score, override status, R/R), the same conclusion as 07-05.

**No trim recommended either** — Valuation Score 47.9 sits in "Cheap," not an expensive band; none of Phase 06's four valid exit triggers apply.

**Recommend the user/orchestrator remediate the `override-log.md` gap** (§3 flag 7, carried forward from 07-05) — this session does not do so (out of scope).

---

## 11. Next Review Trigger

- **Routine:** ZS fiscal Q1 2027 earnings, next report expected late Nov/early Dec 2026 (per `yfinance` `get_earnings_dates`, next estimate window ~2026-11-24).
- **Open item (carried forward, highest priority): the missing `override-log.md` entry** (§3 flag 7) — recommend the orchestrator add a retroactive Human Override entry for ZS.
- **Open interpretive item (unresolved, flagged not fixed):** whether the FCF/Net Income hard disqualifier should mechanically apply to a negative-NI/positive-FCF profile like ZS's (§3 flag 6) — doesn't change this session's conclusion.
- **Watch:** the FY2027 growth-guidance deceleration (~17% vs. FY2026's 25.4%) is the primary forward risk to the Growth sub-score if it undershoots even that; if price pulls back toward ≈$131 (restoring ≥2:1 R/R against the updated PW Fair Value) the entry math would clear — but the Quality Score gate and override status would still independently block a fresh add regardless.
- **Rule 9 triggers (standing):** guidance revision, M&A, management change, a >15% *unexplained* price move, or the next earnings print.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K** | An SEC filing disclosing a material corporate event, such as quarterly earnings — the source document used this session for FY2026 Q4 financials ahead of `yfinance`'s data update. |
| **ARR (Annual Recurring Revenue)** | The annualized value of a subscription business's active contracts. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — reference-only for ZS this session (59.4 Quality Score fails the gate). |
| **D&A** | Depreciation & Amortization. |
| **DBNR (Dollar-Based Net Retention)** | The percentage of a subscription cohort's revenue retained/expanded a year later. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income. |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules, tracked in `override-log.md`; ZS is treated as one but no entry has ever been logged. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | Debt + Equity − Cash — the denominator of ROIC. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio; negative means net cash. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate). |
| **NTM** | Next Twelve Months. |
| **PE / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. ZS: 59.4, unchanged from 07-05. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; require a minimum 2:1 risk/reward before entering; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **SaaS (Software-as-a-Service)** | A software delivery model where customers pay a recurring subscription. |
| **SASE (Secure Access Service Edge)** | A network-security architecture combining networking and security functions into a single cloud-delivered service. |
| **SBC (Stock-Based Compensation)** | Employee pay in company shares/options — a non-cash expense that lowers GAAP net income and dilutes shareholders. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — for ZS this quarter, equal to the just-closed FY2026. |
| **Zero Trust** | A security model assuming no user or device is inherently trustworthy — Zscaler's core product category. |
| **ZTNA (Zero Trust Network Access)** | The product category implementing Zero Trust principles for network access. |
