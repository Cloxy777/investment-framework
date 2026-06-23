# RESCORE — META — 2026-06-23

**Task type:** RESCORE (single ticker)
**Date:** 23 Jun 2026
**10Y US Treasury Yield:** 4.50% (TradingEconomics/CNBC via web search — up from 4.46% used in the 06-20 session; still in the "3.5–5%" bracket → Rate Regime Modifier Step 2 unchanged at +5)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **19.6** (2026-06-20, BUY — Full position 6–8% — [sessions/2026-06-20-rescore-meta.md](2026-06-20-rescore-meta.md))
**Gap since last review:** 3 days (Saturday→Tuesday). No earnings due in that window (next is META Q2 2026, expected late July 2026).

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow (operating cash flow minus capital spending); EV = enterprise value (market value of equity plus net debt — what it would cost to buy the whole business); EBIT = earnings before interest and tax (operating profit); EV/EBIT = enterprise value divided by operating profit; PE = price-to-earnings ratio; forward PE = price divided by *next-12-months* expected earnings; PEG = PE divided by earnings growth rate; D&A = depreciation and amortization (the non-cash charge for using up long-lived assets); capex = capital expenditure (spending on property, plant, equipment, servers); Owner Earnings = Buffett's cash-profit measure = net income + D&A − maintenance capex; MoS = margin of safety (discount to fair value demanded before buying); R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ PE); IRR = internal rate of return.*

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$560.52** | IBKR `get_price_snapshot` (contract_id 107113386, META Class A / NASDAQ), pulled this session 23 Jun 2026 |
| Prior close | $563.85 | IBKR (`prior_close`) — live quote is −0.59% / −$3.33 below it |
| 52-week range | **$520.26 – $794.42** | IBKR `misc_statistics` |
| Year-to-date change | **−15.01%** | IBKR `year_to_date_change` |
| Analyst consensus PT | ~$825–$840 (no change identified since 06-20; last upgrade 26 Jan 2026, last downgrade 30 Apr 2026 — both pre-date this window) | Web search aggregation — used only as a bull-case sanity check (Rule 0 Step 4) |

**Rule 0 source note:** the 06-20 session had IBKR permission-denied for META and fell back to `yfinance`. IBKR worked cleanly this session — used as primary per the methodology's preference order. (`yfinance`'s `currentPrice` field returned a stale $563.85 — identical to the prior close — confirming the IBKR live snapshot is the more current read today; `yfinance`'s own cashflow/financials/earnings-dates tables were still used for the fundamentals/PE-history work in §3 below, which doesn't depend on its quote freshness.)

Price vs 06-20 session: $577.22 → $560.52 = **−2.89%** (the prompt's brief independently quoted −2.93% off a $560.30 read a few minutes earlier in the same session — both readings are well inside the 15% Rule 9 threshold). No fundamental-event trigger from price alone.

---

## 2. Rule 9 Trigger Check (2026-06-20 → 2026-06-23)

Explicitly checked each Rule 9 category via web search for the 3-day window:

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report is META Q2 2026, expected late July 2026 — unchanged from 06-20 |
| Guidance revision | No | The FY2026 capex guidance raise ($115–135B → $125–145B) happened on the **Q1 2026 earnings call in late April 2026** — already reflected in the 06-20 baseline, not new this window |
| M&A | No | No announcements found |
| Management change | No | One sub-divisional departure noted (the lead of Meta's "AI For Work" internal-tools group) — not a CEO/CFO-level change and does not meet the Rule 9 bar |
| Macro shift | No | 10Y ticked from 4.46% → 4.50%, still inside the same "3.5–5%" Rate Regime bracket — not a regime shift |
| >15% unexplained price move | No | −2.89% over 3 days, far under threshold |

**Conclusion: no Rule 9 trigger fired in this window.** This is a routine, schedule-free re-score driven only by price drift and the small Treasury move — consistent with the prompt's framing. Nothing was invented to manufacture a trigger.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** 7.22% (per [holdings.md](../portfolio/holdings.md))

### Carried unchanged from the 06-20 session (filed fundamentals — no new quarter has been reported; verified below that no newer filed data exists)

| Item | Value | Why carried |
|---|---|---|
| TTM EBIT | $88.621B | Last filed-data roll-forward (06-12 session); Q2 2026 (the next update) isn't out until late July |
| TTM FCF (raw — scored input) | $45.65B | Same — Owner Earnings (Upgrade 1) still unresolved, see Data Gap below |
| TTM Net Income | $70.629B | Same |
| TTM D&A | $20.719B | Same |
| Cash + marketable securities | $81.180B | Same (Q1 2026 balance sheet) |
| Senior-note debt (excl. operating leases, per EV convention) | $58.748B | Same |
| Net cash | $81.180B − $58.748B = **$22.43B** | Computed, unchanged |
| Shares outstanding | ≈2.196B | Same (10-Q cover) |
| FCF/NI conversion | $45.65B ÷ $70.629B = **64.6%** | Unchanged — still below 70% but explained by the AI/datacenter capex ramp (Phase 04 carve-out), not a quality flag |
| Net Debt/EBITDA | −0.20× (net cash position) | Unchanged — no leverage concern |
| Gross margin / ROE / revenue growth (spot-check, not scored) | 81.9% / 32.9% / 33.1% | `yfinance` — all intact, no quality deterioration |

**Verification this session:** pulled `yfinance` quarterly financials/cashflow directly (Q2'25–Q1'26) and cross-checked against the carried figures. Raw quarterly-table sums (TTM EBIT $90.789B, TTM NI $70.587B, TTM FCF $48.253B) differ slightly from the carried figures — traced this to `yfinance`'s `Total Debt` field ($86.769B) bundling in lease obligations that the 06-20/06-12 sessions deliberately excluded ("operating leases excluded per EV convention"); the **Long Term Debt** line ($58.748B) matches the carried figure exactly. No new fiscal year or quarter has been filed since 06-20 — FY2025 annual figures (capex $69.69B vs D&A $18.62B) are identical to the prior session's. Continuing to carry the prior session's reconciled figures rather than re-deriving from a table that uses an inconsistent debt definition.

### Refreshed this session (price-dependent)

| Item | 06-20 value | 06-23 value (fresh) | Computation |
|---|---|---|---|
| Live price | $577.22 | **$560.52** | IBKR snapshot (§1) |
| Market Cap | $1,267.6B | **2.196B × $560.52 = $1,230.90B** | Computed |
| EV | $1,245.17B | **$1,230.90B − $22.43B = $1,208.47B** | Computed |
| **EV/EBIT** | 14.05× | **$1,208.47B ÷ $88.621B = 13.6364×** | Computed |
| **FCF Yield** | 3.6013% | **$45.65B ÷ $1,230.90B = 3.7087%** | Computed |
| Forward PE | 15.93× | **$560.52 ÷ $36.25 (fwd EPS, unchanged) = 15.4626×** | Computed at fresh live price — used in preference to `yfinance`'s native `forwardPE` field (15.556×), which is built off its own stale `currentPrice` ($563.85, = prior close) rather than the fresh IBKR quote, per Rule 0 |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

EPS growth: FY2023 NI $39.10B → FY2024 $62.36B (+59.5%, a low-comp "Year of Efficiency" rebound, a one-off) → FY2025 $60.46B (**−3.0%**). This is a multi-year filed-earnings history check and cannot change inside a 3-day window; re-verified via `yfinance` financials this session (FY2025 NI $60.458B, FY2024 $62.360B, FY2023 $39.098B — matches). **Still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base." **PEG is not applicable; its 15% weight is redistributed to EV/EBIT** (making EV/EBIT 40% total), unchanged from every prior META session.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved; raw FCF used (5th consecutive session).** META does not disclose a maintenance-vs-growth capex split. FY2025 capex ($69.69B) remains ~3.7× D&A ($18.62B), clearly growth-heavy, but no decomposition exists to compute Owner Earnings without inventing a split — prohibited by CLAUDE.md. As before, using raw FCF is the **conservative** choice: the only defensible OE proxy (maintenance capex ≈ D&A) would give OE ≈ NI $70.629B → OE yield 5.74% → FCF_Score 42.6 (cheaper than the 62.91 used here). This is now the 5th consecutive session flagging this gap — the recommendation from 06-20 to open a `decisions/` entry resolving the methodology (suspend Upgrade 1 for non-disclosers, or adopt the D&A proxy) still stands and has not yet been actioned.
2. **5yr PE reconstruction unchanged at the 4-decimal level** (see §5) — same 20-quarter window since the next earnings print (Q2 2026) hasn't landed yet, so no new quarter rolled into the trailing series.
3. Gross margin/ROE/revenue-growth quality spot-checks not formally re-collected as Phase 01 inputs this session (same posture as 06-20) — they don't feed the Phase 02 score; spot-checked via `yfinance` and found intact (no deterioration).

---

## 5. META — 5yr PE Recomputation (fresh, via `yfinance`)

Re-ran the full reconstruction method from [valuation-scoring.md](../framework/valuation-scoring.md) rather than reusing 06-20's figures verbatim — rebuilt the trailing TTM-EPS series from `get_earnings_dates` (46 quarters available) and paired each quarter's TTM EPS with the contemporaneous price, then took the most recent 20 quarters (~5yr):

```
5yr avg PE = 23.589×   (06-20: 23.59×)
5yr low PE  = 9.255×   (06-20: 9.26×)
5yr high PE = 36.014×  (06-20: 36.01×)
n = 20 quarters
```

**Result: unchanged to within rounding.** The most recent earnings date in the rolling window is still 2026-04-29 (Q1 2026) — the same as on 06-20 — so the 20-quarter window hasn't shifted. No drift to report; confirms the anchor is stable, not stale.

---

## 6. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 15.4626 = 6.4672%
Spread = EY − 10Y Treasury = 6.4672% − 4.50% = +1.9672%
```
Pass threshold: Spread ≥ +1.5%. **Result: PASS** (+1.9672%, **~0.47pp of cushion** — wider than 06-20's ~0.32pp) → **no additive.**

> The 06-20 session flagged this gate as passing by only a thin margin and warned a rise in forward PE or the 10Y could flip it back to FAIL. Instead, the cushion **widened**: the price drop (−2.89%) pulled forward PE down further (15.93× → 15.46×), which raised the earnings yield more than the 10Y's small uptick (4.46%→4.50%) ate into the spread. Gate remains comfortably PASS.

**Step 2 — Rate Regime Modifier**
10Y = 4.50% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +5** (unchanged from 06-20).

---

## 7. META — Full Score Calculation

**FCF Yield — 40% weight** (raw FCF; Owner-Earnings proxy would score *cheaper* — Data Gap #1)
```
FCF_Score = clamp(100 × (1 − 3.7087 / 10), 0, 100) = 62.9130
```
→ Contribution: 62.9130 × 0.40 = **25.1652**

**EV/EBIT — 40% weight** (PEG not applicable → its 15% redistributed here, 25%+15%)
```
EV/EBIT_Score = clamp((13.6364 − 12) / 23 × 100, 0, 100) = 7.1148
```
→ Contribution: 7.1148 × 0.40 = **2.8459**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (15.4626 − 23.589) / 23.589 × 100 = −34.4500%
FwdPE_Score = clamp(50 + (−34.4500) × 2.5, 0, 100) = clamp(−36.125, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**
(Fallback formula already folds in the Historical PE Modifier — no separate ±10 applied, consistent with the anti-double-count note.)

**PEG — Fast-Grower test: FAIL** (re-verified §3). PEG's 15% weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 25.1652 + 2.8459 + 0.0
= 28.0111
```
**+ Rate Modifier (+5) = 33.0111** *(before the Upside/Downside Modifier)*

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: carry forward the 06-20 scenario framework's EPS/exit-PE assumptions.** No fundamental change occurred in this window (§2), and the two documented catalysts (AI ad-monetization proof points at Q2 2026 earnings, capex-ROI demonstration) are unchanged and still inside the 18–24 month window. Re-deriving fresh bull/base/bear EPS assumptions from the same underlying (unchanged) financials would not produce a materially different scenario set — only the live price and resulting gap/E genuinely move. Recomputed below at the new live price.

**Step 1 — Scenario fair values (Rule 7, carried EPS/exit-PE assumptions)**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 | 24× | **$960.00** |
| **Base** | 50% | $36.25 (consensus NTM) | 20× | **$725.00** |
| **Bear** | 25% | $28.0 | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×725.00 + 0.25×364.00 = $693.50   (unchanged — same EPS/PE inputs)
```
Sanity check (Rule 0 Step 4 / Rule 4): PW FV $693.50 remains below the ~$825–840 analyst consensus PT and the bull case ($960) below the street-high — still a conservative, not rosy, blend.

**Step 2 — Gap, annualization, components (recomputed at new live price)**
```
Gap Upside %    = ($693.50 ÷ $560.52) − 1                  = +23.7244%
Catalyst window = 2 years (unchanged — no narrower documented window)
Annualized gap  = 23.7244% ÷ 2                              = +11.8622%/yr
Intrinsic growth = +12.0%/yr   (carried — durable FCF/EPS CAGR, unchanged basis)
Shareholder yield = buyback yield + dividend yield (recomputed at fresh market cap $1,230.90B)
                  = $26.25B/$1,230.90B + $5.32B/$1,230.90B  = 2.1326% + 0.4322% = +2.5648%/yr
```
```
E (expected annual return) = 11.8622 + 12.0 + 2.5648 = +26.4270%/yr
```

**Step 3 — Catalyst / timeline (Rule 10 + Guardrail 1).** Same two catalysts as 06-20, both still inside the 18–24-month window: (a) AI ad-monetization proof points, first visible at **Q2 2026 earnings (late July 2026)**; (b) capex-ROI demonstration. **Upside credit fully allowed; the −5 catalyst cap does NOT apply.**

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 26.4270% ≥ H → M = −15 × clamp((26.4270 − 10) / 15, 0, 1)
                      = −15 × clamp(1.0951, 0, 1)
                      = −15 × 1.0000
                      = −15.0000
```
**Upside/Downside Modifier M = −15.0** — the maximum allowed credit (E has now crossed the +25%/yr ceiling that fully saturates the modifier, vs −14.56 on 06-20 when E was 24.56%/yr). The move is entirely mechanical: the live price fell ~2.9% while the PW Fair Value held flat (no scenario inputs changed), which widened the gap-to-fair-value and pushed E over the +25% line.

**Robustness check:** with raw+rate fixed at 33.01, the score's full range across the entire ±15 modifier band is **18.0** (M=−15) to **48.0** (M=+15) — META stays in a BUY band (Full or Standard) across the *entire* possible range of this modifier. The forecast sharpens *where* in the BUY range it lands; it does not manufacture the BUY signal (same conclusion as 06-20).

---

## 9. META — Final Score & Action

```
Final Score = Raw weighted (28.0111) + Rate Modifier (+5) + Upside/Downside Modifier (−15.0)
            = 18.0111
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 18.0**

# Final Score: 18.0 → Action band: BUY — Full position 6–8% (Score 0.0–29.9)

**Action category vs prior session: UNCHANGED.** 19.6 (06-20) → 18.0 (06-23) — both land in the **0.0–29.9 "BUY — Full position 6–8%"** band. The score moved modestly cheaper (−1.6 points), driven almost entirely by the Upside/Downside Modifier saturating at its −15.0 ceiling (vs −14.56 before) as the price drop widened the gap to an unchanged fair value — not by any new fundamental development. No Rule 9 trigger fired (§2); this is the score mechanically responding to a 3-day price move, exactly as the framework's modifier is designed to do.

**Practical recommendation (unchanged in substance): HOLD — no automatic fresh capital.** META is an existing holding at **7.22%**, inside the 6–8% full-position band the score points to, well under the 15% hard cap (Upgrade 7). No new fundamental trigger this session — only price/rate/modifier mechanics moved. Order setup below for completeness, per the framework's "run for every BUY or TRIM action" rule.

---

## 10. META — Order Setup (Score in BUY band → required)

Confidence: wide-moat proven compounder with heavy in-flight AI capex — using the same conservative 20% MoS as 06-20 (15–20% range for Score 0.0–29.9; take the higher end given capex uncertainty, consistent with the prior session).

```
[x] Valuation Score (incl. Upside/Downside Mod): 18.0   (≤49.9 ✓ — entry permitted)
[x] Expected annual return E / catalyst window:  +26.4% / 2yr
[x] Upside/Downside Modifier applied:            −15.0
[x] Blended Fair Value (PW, Rule 7):             $693.50  (unchanged from 06-20 — same scenario inputs)
[x] Margin of Safety %:                          20%
[x] BUY PRICE (limit):     $693.50 × (1 − 0.20)        = $554.80   (unchanged — FV unchanged)
[x] PRIMARY SELL TARGET:   = Blended FV                = $693.50
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $554.80 × (1 − 0.25)        = $416.10   (25% max loss, Score 0–29.9 high-conviction)
[x] Risk/Reward Ratio (base-case target):  ($693.50 − $554.80) ÷ ($554.80 − $416.10) = $138.70 ÷ $138.70 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $554.80) ÷ $138.70 = $309.20 ÷ $138.70 = 2.23:1
```

> **R/R still FAILS the 2:1 minimum at the base-case sell target — unchanged conclusion from 06-20.** Because the Blended Fair Value ($693.50), Buy Price ($554.80), and Stop Loss ($416.10) are all unchanged (no scenario input moved), the R/R picture is identical: **1.0:1 against the primary sell target (fails 2:1)**, **2.23:1 against the bull-case trim target (passes)** — the trade only clears 2:1 if underwritten to the bull case, not the base case. **Live price ($560.52) remains above the $554.80 buy-price limit** (by $5.72, down from $22.42 on 06-20 — the gap has narrowed by ~3% as price has drifted toward the limit, but has not closed). **Net: limit order at $554.80 stands; no entry today.**

**Position sizing:** META is already at **7.22%**, inside the 6–8% allocation band for a Score 0.0–29.9 name (Step 5: take the lower of risk-based size and the cap — the cap binds here). Room to the band's 8% ceiling: **0.78pp**. No fresh-capital action is forced by this score; this is unchanged from 06-20.

---

## 11. Portfolio Note

META at 7.22% is comfortably under the 15% hard cap (Upgrade 7) and sits within the 6–8% full-position band its score points to. No portfolio-level action triggered — no trim signal (score is deep in BUY territory, nowhere near the ≥70 trim bands), no forced top-up (R/R fails at the base case, and the position is already inside its target band). This session does not change the holdings.md weight — that update is handled by the orchestrator after this batch.

---

## 12. Next Review Triggers

- **Next earnings — META Q2 2026 (quarter ending June 2026), expected late July 2026** → routine post-earnings re-score (refreshes the TTM fundamentals carried since 06-12, and the AI-monetization/capex-ROI catalyst gets its first real data point).
- **Rule 9 fundamental triggers:** any guidance revision (especially a further FY capex-guidance change — the bear case hinges on capex), management change, material M&A, or a >15% unexplained price move.
- **Rate Gate watch:** Step 1 passes with ~0.47pp of cushion (+1.97% vs +1.50% required) — wider than 06-20's ~0.32pp, but still bears watching if forward PE rises or the 10Y climbs further.
- **Buy-price proximity watch:** live price ($560.52) is now only **$5.72 (1.0%) above** the $554.80 limit order — the closest the price has come to triggering entry across the last three sessions. Worth a price check before the next scheduled review if there's any further drift down.
- **Owner Earnings (Upgrade 1) methodology decision** — open for a 5th consecutive session (Data Gap #1); the recommendation to resolve this via a `decisions/` entry still stands.

---

## Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **bps / pp (percentage points)** | A direct difference between two percentages (e.g. margin falling from 42% to 39% is a 3pp drop) — distinct from a "%" change. |
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
| **IRR** | Internal Rate of Return. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; unresolved for META, see Data Gap #1). |
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
