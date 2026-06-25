# RESCORE — META — 2026-06-25

**Task type:** RESCORE (single ticker)
**Date:** 25 Jun 2026
**10Y US Treasury Yield:** 4.40% (TradingEconomics, 25 Jun 2026 — down from 4.50% used in the 06-23 session; still in the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **18.0** (2026-06-23, BUY — Full position 6–8% — [sessions/2026-06-23-rescore-meta.md](2026-06-23-rescore-meta.md))
**Gap since last review:** 2 days (Tuesday→Thursday). No earnings due in that window (next is META Q2 2026, expected late July 2026).

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow (operating cash flow minus capital spending); EV = enterprise value (market value of equity plus net debt — what it would cost to buy the whole business); EBIT = earnings before interest and tax (operating profit); EV/EBIT = enterprise value divided by operating profit; PE = price-to-earnings ratio; forward PE = price divided by *next-12-months* expected earnings; PEG = PE divided by earnings growth rate; D&A = depreciation and amortization (the non-cash charge for using up long-lived assets); capex = capital expenditure (spending on property, plant, equipment, servers); Owner Earnings = Buffett's cash-profit measure = net income + D&A − maintenance capex; MoS = margin of safety (discount to fair value demanded before buying); R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); IRR = internal rate of return.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$546.22** | IBKR `get_price_snapshot` (contract_id 107113386, META Class A / NASDAQ), pulled this session 25 Jun 2026 |
| Change vs prior close | **−2.05%** (−$11.45) | IBKR `change` field |
| 52-week range | **$520.26 – $794.42** | IBKR `misc_statistics` — identical to 06-23, no new 52-week extreme hit |
| Year-to-date change | **−17.18%** | IBKR `year_to_date_change` |
| Dividend yield (trailing) | 0.38% | IBKR `dividend_yield` — cross-checked, matches Yahoo's 0.38% exactly |
| Analyst consensus PT | mean **$827.32**, median **$825.00**, high **$1,015.00**, low **$664.46** (59 analysts) | Yahoo `quoteSummary` direct pull (cookie+crumb flow, §4) — used only as a bull-case sanity check (Rule 0 Step 4); modestly above the ~$825–840 range cited on 06-23 |

Price vs 06-23 session: $560.52 → $546.22 = **−2.55%**. Well inside the 15% Rule 9 threshold — no price-driven fundamental trigger.

---

## 2. Rule 9 Trigger Check (2026-06-23 → 2026-06-25)

Web search run for META news in the 2-day window. Findings:

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report is META Q2 2026, expected late July 2026 — unchanged |
| Guidance revision | No | The $79B in new data-center lease commitments (bringing cumulative commitments to $182.9B) being reported by Bloomberg/DCD this week is **analysis of Meta's Q1 2026 10-Q filing** (quarter ended 31 Mar 2026, filed late April/early May 2026) — already reflected in the 06-12/06-20/06-23 baseline, not a new disclosure this window |
| M&A | No | No announcements found |
| Management change | No | No CEO/CFO-level change; the org-restructuring/morale commentary (CTO Andrew Bosworth) traces to the May 2026 layoffs and Applied AI division creation — predates this window |
| Macro shift | No | 10Y ticked down from 4.50% → 4.40%, still inside the same "3.5–5%" Rate Regime bracket — not a regime shift |
| >15% unexplained price move | No | −2.55% over 2 days, far under threshold |
| Other | No | Piper Sandler reiterated a Buy rating (single-analyst opinion, not a trigger); product news (a standalone "Arena" prediction-market app in development, $299 smart glasses) is not a financial/fundamental event |

**Conclusion: no Rule 9 trigger fired in this window.** This is a routine, schedule-free re-score driven only by price drift and the small Treasury move.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** 7.22% (per [holdings.md](../portfolio/holdings.md) — not re-derived this session, orchestrator-owned)

### Carried unchanged from the 06-23 session (no new quarter has been reported)

| Item | Value | Why carried |
|---|---|---|
| TTM EBIT | $88.621B | No new filing since Q1 2026 (next is Q2 2026, late July) |
| TTM FCF (raw — scored input) | $45.65B | Same — Owner Earnings (Upgrade 1) still unresolved, see Data Gap below |
| TTM Net Income | $70.629B | Same |
| Net cash | $22.43B (cash+securities $81.180B − senior-note debt $58.748B) | Same |
| Shares outstanding | ≈2.196B | Same — cross-validated exactly this session against Yahoo's `sharesOutstanding` (2,196,045,588) |
| FCF/NI conversion | 64.6% | Unchanged |
| Net Debt/EBITDA | −0.20× (net cash position) | Unchanged |
| 5yr avg PE (trailing anchor) | 23.589× (range 9.255×–36.014×, n=20 quarters) | Unchanged — most recent earnings date in the rolling window is still 2026-04-29 (Q1 2026); window hasn't shifted |
| Fast-Grower (PEG eligibility) | **FAILS** (FY2024 NI +59.5% one-off rebound, FY2025 −3.0%) | Unchanged — multi-year filed-earnings check, cannot move inside a 2-day window. PEG's 15% weight stays redistributed to EV/EBIT (40% total) |
| Forward EPS (NTM consensus) | $36.25 | **Re-verified this session via direct Yahoo `quoteSummary` pull** (manual cookie+crumb flow, same technique used for MSFT's 06-25 rescore after `yfinance`'s `curl_cffi` transport failed the proxy's TLS handshake) — returned `forwardEps` $36.24596, identical to the carried $36.25 to the cent. Confirms no analyst-consensus drift since 06-23. |

### Refreshed this session (price-dependent)

| Item | 06-23 value | 06-25 value (fresh) | Computation |
|---|---|---|---|
| Live price | $560.52 | **$546.22** | IBKR snapshot (§1) |
| Market Cap | $1,230.90B | **2.196B × $546.22 = $1,199.499B** | Computed |
| EV | $1,208.47B | **$1,199.499B − $22.43B = $1,177.069B** | Computed |
| **EV/EBIT** | 13.6364× | **$1,177.069B ÷ $88.621B = 13.2820×** | Computed |
| **FCF Yield** | 3.7087% | **$45.65B ÷ $1,199.499B = 3.8058%** | Computed |
| Forward PE | 15.4626× | **$546.22 ÷ $36.25 = 15.0681×** | Computed at fresh live price |

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (6th consecutive session).** META does not disclose a maintenance-vs-growth capex split. No change this session — same open `decisions/` item as every prior META rescore.
2. **Forward EPS data-source note.** `yfinance` itself failed this session via the same `curl_cffi`/proxy TLS incompatibility documented in today's MSFT rescore (`OPENSSL_internal: invalid library` — a browser-TLS-impersonation transport the proxy's CA setup doesn't support). Used the manual Yahoo `quoteSummary` cookie+crumb `requests` flow instead (no TLS bypass) — confirmed `forwardEps` $36.24596, matching the carried $36.25 figure essentially exactly, so no methodology concern here (unlike MSFT, where secondary sources had genuinely conflicted — META's figure simply reconfirmed cleanly).
3. **5yr PE reconstruction not re-run this session** — no new quarter has rolled into the trailing 20-quarter window since 06-23 (last earnings date still 2026-04-29), so the figures carried from the 06-23 fresh reconstruction remain current; re-deriving would reproduce the identical window.
4. Gross margin/ROE/revenue-growth quality spot-checks not re-collected (Phase 01 inputs, not Phase 02 score inputs) — no new data since last earnings.

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 15.0681 = 6.6365%
Spread = EY − 10Y Treasury = 6.6365% − 4.40% = +2.2365%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+2.2365%, **~0.74pp of cushion** — wider than 06-23's ~0.47pp) → **no additive.**

> The cushion widened again: the price drop (−2.55%) pulled forward PE down further (15.46× → 15.07×), raising the earnings yield more than the 10Y's small *decline* (4.50%→4.40%) ate into the spread (a falling 10Y actually widens the spread further, all else equal). Gate remains comfortably PASS.

**Step 2 — Rate Regime Modifier**
10Y = 4.40% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +5** (unchanged from 06-23).

---

## 6. META — Full Score Calculation

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.8058 / 10), 0, 100) = 61.942
```
→ Contribution: 61.942 × 0.40 = **24.7770**

**EV/EBIT — 40% weight** (PEG not applicable → its 15% redistributed here, 25%+15%)
```
EV/EBIT_Score = clamp((13.2820 − 12) / 23 × 100, 0, 100) = 5.5740
```
→ Contribution: 5.5740 × 0.40 = **2.2296**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (15.0681 − 23.589) / 23.589 × 100 = −36.1294%
FwdPE_Score = clamp(50 + (−36.1294) × 2.5, 0, 100) = clamp(−40.3235, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — Fast-Grower test: FAIL** (unchanged §3). PEG's 15% weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 24.7770 + 2.2296 + 0.0
= 27.0066
```
**+ Rate Modifier (+5) = 32.0066** *(before the Upside/Downside Modifier)*

---

## 7. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: carry forward the 06-23 scenario framework's EPS/exit-PE assumptions.** No fundamental change occurred in this window (§2). Recomputed below at the new live price.

**Step 1 — Scenario fair values (Rule 7, carried EPS/exit-PE assumptions, unchanged)**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 | 24× | **$960.00** |
| **Base** | 50% | $36.25 (consensus NTM) | 20× | **$725.00** |
| **Bear** | 25% | $28.0 | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×725.00 + 0.25×364.00 = $693.50   (unchanged — same EPS/PE inputs)
```
Sanity check: PW FV $693.50 remains below the $827.32 analyst mean / $825.00 median PT; bull case ($960) below the $1,015 street high. Still a conservative, not rosy, blend.

**Step 2 — Gap, annualization, components (recomputed at new live price)**
```
Gap Upside %    = ($693.50 ÷ $546.22) − 1                  = +26.9635%
Catalyst window = 2 years (unchanged)
Annualized gap  = 26.9635% ÷ 2                              = +13.4818%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = buyback yield + dividend yield (recomputed at fresh market cap $1,199.499B,
                    carried dollar amounts: $26.25B buyback, $5.32B dividend)
                  = $26.25B/$1,199.499B + $5.32B/$1,199.499B  = 2.1887% + 0.4435% = +2.6322%/yr
```
```
E (expected annual return) = 13.4818 + 12.0 + 2.6322 = +28.1140%/yr
```

**Step 3 — Catalyst / timeline (Rule 10 + Guardrail 1).** Same two catalysts as 06-23, both still inside the 18–24-month window: (a) AI ad-monetization proof points, first visible at Q2 2026 earnings (late July 2026); (b) capex-ROI demonstration. **Upside credit fully allowed.**

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 28.1140% ≥ H → M = −15 × clamp((28.1140 − 10) / 15, 0, 1)
                      = −15 × clamp(1.2076, 0, 1)
                      = −15.0000
```
**Upside/Downside Modifier M = −15.0** — unchanged at the maximum allowed credit (E rose further above the +25%/yr ceiling, from 26.43% on 06-23 to 28.11% now, but the modifier is bounded and was already saturated).

---

## 8. META — Final Score & Action

```
Final Score = Raw weighted (27.0066) + Rate Modifier (+5) + Upside/Downside Modifier (−15.0)
            = 17.0066
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 17.0**

# Final Score: 17.0 → Action band: BUY — Full position 6–8% (Score 0.0–29.9)

**Action category vs prior session: UNCHANGED.** 18.0 (06-23) → 17.0 (06-25) — both land in the **0.0–29.9 "BUY — Full position 6–8%"** band. The **entire −1.0 point move** is attributable to the lower raw weighted score (28.0111 → 27.0066, a drop of ~1.0045) — driven by the price decline making FCF Yield and EV/EBIT cheaper. **The Rate Modifier (+5) and Upside/Downside Modifier (−15.0) were both unchanged** — Step 1 of the Rate Gate still passes (just with a wider cushion) and the expected-return modifier was already pinned at its −15 floor in both sessions. No Rule 9 trigger fired (§2) — this is the score mechanically responding to a 2-day price move.

**Practical recommendation (unchanged in substance): HOLD — no automatic fresh capital.** META is an existing holding at 7.22%, inside the 6–8% full-position band, well under the 15% hard cap. No new fundamental trigger this session.

---

## 9. META — Order Setup (Score in BUY band → required)

Confidence: same as 06-23 — 20% MoS (high end of the 15–20% range for Score 0.0–29.9, given capex uncertainty).

```
[x] Valuation Score (incl. Upside/Downside Mod): 17.0   (≤49.9 ✓ — entry permitted)
[x] Expected annual return E / catalyst window:  +28.1% / 2yr
[x] Upside/Downside Modifier applied:            −15.0
[x] Blended Fair Value (PW, Rule 7):             $693.50  (unchanged from 06-23 — same scenario inputs)
[x] Margin of Safety %:                          20%
[x] BUY PRICE (limit):     $693.50 × (1 − 0.20)        = $554.80   (unchanged — FV unchanged)
[x] PRIMARY SELL TARGET:   = Blended FV                = $693.50
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $554.80 × (1 − 0.25)        = $416.10   (25% max loss, Score 0–29.9 high-conviction)
[x] Risk/Reward Ratio (base-case target):  ($693.50 − $554.80) ÷ ($554.80 − $416.10) = $138.70 ÷ $138.70 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $554.80) ÷ $138.70 = $309.20 ÷ $138.70 = 2.23:1
```

**⚠️ Notable change this session — live price has crossed BELOW the formal buy-price limit for the first time.** Across 06-12, 06-20, and 06-23, the live price stayed above the $554.80 buy limit (most recently by just $5.72 / 1.0% on 06-23). Today's live price ($546.22) sits **$8.58 (1.55%) below** that limit — meaning a standing GTC limit order at $554.80 would now be filled. **This does not, by itself, clear the trade for entry**: the R/R gate is independent and still fails. Recomputing R/R using the live price as a hypothetical entry (holding the Stop Loss and Sell Target fixed at their formula-anchored values, same convention used in today's MSFT rescore): ($693.50 − $546.22) ÷ ($546.22 − $416.10) = $147.28 ÷ $130.12 = **1.13:1 — still below the 2:1 minimum**, only modestly improved from the formal entry's 1.00:1. **Net: still no entry** — both the base-case formal R/R and the live-price R/R fail 2:1; only the bull-case trim target clears it (2.23:1, an aggressive underwrite this framework does not use as the actionability bar).

**Position sizing:** META is already at 7.22%, inside the 6–8% allocation band; room to the band's 8% ceiling: 0.78pp. No fresh-capital action is forced by this score.

---

## 10. Portfolio Note

META at 7.22% is comfortably under the 15% hard cap (Upgrade 7) and sits within the 6–8% full-position band its score points to. No portfolio-level action triggered. This session does not change the holdings.md weight — that update is handled by the orchestrator.

---

## 11. Next Review Triggers

- **Next earnings — META Q2 2026 (quarter ending June 2026), expected late July 2026** → routine post-earnings re-score (first real data point on the AI-monetization/capex-ROI catalyst).
- **Rule 9 fundamental triggers:** any guidance revision, management change, material M&A, or a >15% unexplained price move.
- **Rate Gate watch:** Step 1 passes with ~0.74pp of cushion (wider than 06-23's ~0.47pp) — still bears watching if forward PE rises or the 10Y climbs.
- **Buy-price watch — escalated.** Live price has now crossed *below* the $554.80 limit (first time across four sessions) — track closely; if it holds or falls further, the binding constraint on entry becomes purely the R/R gate (still failing at 1.00–1.13:1), not price availability.
- **Owner Earnings (Upgrade 1) methodology decision** — open for a 6th consecutive session.

---

## Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **bps / pp (percentage points)** | A direct difference between two percentages — distinct from a "%" change. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchasing its own stock, net of new issuance — a component of shareholder yield. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense for using up long-lived assets. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit. |
| **EPS** | Earnings Per Share. |
| **EV** | Enterprise Value — market cap + net debt. |
| **EV/EBIT** | Enterprise Value ÷ EBIT — a cheapness multiple independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF** | Free Cash Flow. |
| **FCF Yield** | FCF ÷ Market Cap — higher is cheaper. |
| **FCF/NI conversion ratio** | FCF ÷ Net Income — checks whether accounting profit is becoming real cash. |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV (Fair Value)** | The analyst's estimate of intrinsic worth, independent of market price. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NTM (Next Twelve Months)** | The forward-looking 12-month period used for forward earnings estimates. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; unresolved for META). |
| **PE (Price-to-Earnings) ratio** | Share price ÷ EPS. |
| **PEG ratio** | PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **PW (Probability-Weighted) Fair Value** | 25% bull + 50% base + 25% bear blended fair value (Rule 7). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate** | The pre-check run before every score, comparing earnings yield to the 10Y Treasury and applying a regime modifier. |
| **Rate Regime Modifier** | Additive −10 to +10 score adjustment based on the 10Y Treasury bracket. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
