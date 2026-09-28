# RESCORE — MSFT — 2026-09-28

**Task type:** RESCORE (mode `--both`)
**Date:** 28 Sep 2026
**10Y US Treasury Yield:** 5.24% (TradingEconomics live quote, cross-checked against Yahoo Finance/CNBC/247WallSt coverage of the same session, all converging on 5.21–5.25%; used the TradingEconomics live figure) — up sharply from 4.70% at the 07-30 session, crossing out of the "3.5–5%" bracket into the ">5%" bracket for the first time in this framework's tracked history of MSFT sessions.
**Rate Regime Modifier (Step 2):** **+10** (was +5) — a genuine bracket change, not a rounding artifact.
**Last review on record:** MSFT Valuation Score **38.9** (2026-07-30, nominal BUY-Standard band on the raw score) — [sessions/2026-07-30-rescore-msft.md](2026-07-30-rescore-msft.md); Quality Score **79.9** (primary)/82.9 (sensitivity), **failed the 80.0+ gate**; no Composite Score adopted (reference-only figures computed and clearly labeled, per the same convention followed below).
**Current MSFT portfolio weight:** 14.24% per [holdings.md](../portfolio/holdings.md) (last full sync 22 Aug 2026, pre-dating today's price move — see §11).

> *Jargon decoded on first use: FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EBITDA = operating profit before depreciation/amortization; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; NOPAT = net operating profit after tax; ROIC = return on invested capital; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; TTM = trailing twelve months; NTM = next twelve months; RPO = remaining performance obligations.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$509.99** | IBKR `get_price_snapshot` (contract_id 272093, NASDAQ), intraday `last` field, 28 Sep 2026 (`is_close: false`, not a stale/frozen quote). |
| Cross-check | Market Cap ÷ Shares Outstanding = $3,781,236,359,168 ÷ 7,425,545,491 = **$509.16** (`yfinance`) | Within 0.16% of the IBKR live tick — consistent, no Rule 0 concern. |
| 52-week range | $349.20 – $550.29 | IBKR `misc_statistics` |
| Price change vs. prior session close | −1.20% ($6.18) | IBKR `change` field (intraday move, not a Rule 9 signal on its own) |
| Analyst consensus PT | $577.26 mean (range $440–$870) | Web search (Investing.com aggregation), not a scored input — bull-case sanity check only |
| Price vs. 07-30 review ($449.40) | **+13.48%** | ($509.99/$449.40) − 1. Meaningful but below the 15% "unexplained move" Rule 9 threshold; moot regardless since the rate-regime shift below already independently fires Rule 9. |

---

## 2. Rule 9 Trigger Check (2026-07-30 → 2026-09-28)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | **No** | FY2027 Q1 not yet reported — confirmed still expected late Oct 2026 (no date more specific than "late October" found; flagged, not invented). |
| Guidance revision | No | No standalone revision found since the 07-30 guidance. |
| M&A (of an external company) | No | None found. |
| Management change | No | None found. |
| **Macro shift** | **YES** | US 10Y Treasury yield climbed from 4.70% (30 Jul) to **~5.24%** (28 Sep) — a >0.5pp move that crosses the Rate Environment Gate's "3.5–5%" → ">5%" bracket boundary, now the highest 10Y level since 2007 per multiple financial-press sources (rising on hawkish Fed commentary, elevated inflation expectations, and renewed geopolitical (Iran) risk premium in oil). This is an explicit "macro shift (central bank policy...)" Rule 9 trigger in its own right, independent of any MSFT-specific news. |
| >15% unexplained price move | No | +13.48% since 07-30, below the 15% threshold; moot given the macro trigger already firing. |

**Other items checked, none independently material:**
1. MSFT's FY26 workforce reduction, OpenAI partnership restructuring (Azure-exclusivity removed, IP licensing extended through 2032, April 2026), and the securities class action (case No. 26-cv-02071) are all unchanged since 07-30 — no new escalation found.
2. FY2027 capex guidance continues to be discussed in the financial press (calendar-2026 capex now tracking toward ~$175B, a "~$190B plan" cited by one source) but this is **elaboration on already-known FY26 capex trends** (capex +79.5% YoY was already captured in the 07-30 session), not a fresh company guidance revision — not treated as an independent Rule 9 trigger.

**Conclusion: Rule 9 macro-shift trigger fired (Rate Environment Gate bracket change) — full re-score performed below.** No new fiscal quarter has been reported since 07-30 (FY2027 Q1 is not due until late Oct 2026), so **all fundamental (non-price, non-rate) inputs below are the same FY2026 fiscal-year figures used in the 07-30 session** — re-verified fresh from `yfinance` this session (which has now fully ingested the FY2026 annual statements, unlike 07-30's data-lag workaround) — only live price, share count (small net buyback effect), forward EPS estimate, and the 10Y Treasury input have moved.

---

## 3. Data-Quality Flag — `fetch_fundamentals` EBIT Field (Confirmed, Not Silently Worked Around)

`python -m scripts.fetch_fundamentals MSFT` output (pasted verbatim below) reports **EV/EBIT = 22.989** and **ROIC = 28.219%**, built on `yfinance`'s `"EBIT"` field = **$168.985B** (FY2026 annual). This is a real, verified discrepancy against MSFT's own reported **Operating Income = $155.237B** (matches the officially disclosed $155.2B in the FY2026 earnings release and 10-K, confirmed via web search) — the script's own module docstring already documents this exact drift ("as of yfinance 0.2.66, `t.info['ebit']` returns None... this script uses `t.financials.loc['EBIT']` instead"), but does not flag that this substitute `EBIT` row is **not** the same as `Operating Income` (it appears to include non-operating items reconciled back in, likely embedding the FY2026 OpenAI-stake mark-to-market gain and other below-the-line items).

**Per Rule 6 ("normalize before you value") and consistency with every prior MSFT session (06-07 through 07-30), this session uses the officially-reported $155.237B Operating Income figure, not the script's raw `EBIT` output, for EV/EBIT and ROIC/NOPAT.** This is flagged transparently rather than silently substituted — see the recomputed figures in §5 and the **known, pre-existing tooling limitation**, not a fresh data gap.

```
## Fundamentals — MSFT

Market Cap            = 3,781,236,359,168
Enterprise Value      = 3,884,813,910,016
Shares Outstanding    = 7,425,545,491
Forward PE            = 21.508
FCF Yield %           = 1.772
EV/EBIT               = 22.989   [!] Uses yfinance "EBIT" ($168.985B), not Operating Income ($155.237B) — see flag above
Net Margin %          = 40.305  [!] GAAP, not normalized for the FY2026 OpenAI one-off — see §5
Gross Margin %        = 67.944
ROIC % (NOPAT/InvCap) = 28.219  [!] Same EBIT-field issue as above
Revenue 3yr CAGR %    = 16.124
Net Debt/EBITDA       = 0.100   [!] Uses the same inflated EBIT-based EBITDA; recomputed in §5
FCF/NI TTM %          = 50.084  [!] GAAP-based; normalized figure used below is 52.01%
FCF/NI annual (oldest first) = [82.2%, 84.0%, 70.3%, 50.1%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 31.492 / 24.123 / 38.730  (n=20 quarters)
```

The market cap, EV, shares outstanding, forward PE, FCF yield, gross margin, revenue CAGR, FCF-positivity, and 5yr PE history fields above are unaffected by the EBIT issue and used as-is. Full recomputation of the affected fields is in §5.

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved (10th consecutive session).** MSFT still discloses no maintenance-vs-growth capex split. Raw FY2026 Free Cash Flow used as the FCF_Score input, as in every session back to 06-07.
2. **`fetch_fundamentals`'s `EBIT`/EV-EBIT/ROIC output is not usable as-is** — see §3. Recomputed from official Operating Income throughout.
3. **One-time OpenAI investment gain (+$4.963B FY2026 net income) again stripped per Rule 6** — same figure, same basis as 07-30 (no fresher one-off items found this session; no new quarter reported).
4. **Total debt convention unchanged:** $40.294B (notes only: current $9.227B + LT $31.067B) used throughout, vs. `yfinance`'s broader $56.826B `Total Debt` convention (includes lease liabilities) — consistent with every prior session.
5. **5yr avg/range PE unchanged from 07-30** (avg 31.492× vs. 31.546×, essentially flat — no new quarter has rolled into or out of the 20-quarter window since the last earnings print).
6. **Precise FY2027 Q1 earnings date not found** (only "late October 2026" cited) — flagged rather than invented; used as the qualitative next-review trigger, not as an input to any calculation.
7. **Quality Score gate result again NOT robust to the same single judgment call (Moat Signal, "scale cost advantage")** — third consecutive session with an unresolved 0.1-point margin. Searched again this session (Sep 2026 Azure/AI capex coverage); found industry-wide hyperscaler capex/PUE commentary but no fresh MSFT-specific unit-cost-vs-named-competitor citation. No new evidence either way.
8. **Portfolio weight (14.24%) is from the 22 Aug 2026 sync**, pre-dating today's +13.48% cumulative price move since 07-30 — not recomputed here (that is `/sync-portfolio`'s job); flagged in §11.

---

## 5. MSFT — Inputs Collected (FY2026 = same fiscal year as 07-30, re-verified fresh; only price/shares/rate inputs are new)

**Sector:** Technology — Software, Cloud Infrastructure (Azure) & Productivity

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 7,425,545,491 (down slightly from 7,428,434,704 on 07-30 — net buybacks) | `yfinance` |
| **Market Cap** | 7,425,545,491 × $509.99 = **$3,786,953.94M** | Computed |
| Total notes debt (current + LT) | $9.227B + $31.067B = **$40.294B** | `yfinance` balance sheet (FY2026, 6/30/2026) |
| Cash + ST investments | **$76.651B** | `yfinance` balance sheet |
| **Net Debt** | $40.294B − $76.651B = **−$36.357B (net cash)** | Computed |
| **EV** | $3,786,953.94M − $36,357M = **$3,750,596.94M** | Computed |
| FY2026 Operating Income (official) | **$155.237B** | `yfinance` annual `Operating Income` row, matches officially reported $155.2B (FY2026 earnings release / 10-K) |
| **EV/EBIT** | $3,750,596.94M ÷ $155,237M = **24.160×** | Computed (uses official Operating Income — see §3 flag) |
| FY2026 Operating Cash Flow | **$182.935B** | `yfinance` |
| FY2026 CapEx | **$115.948B** | `yfinance` |
| **FY2026 FCF** | $182.935B − $115.948B = **$66.987B** | Computed (matches 07-30 exactly — same fiscal year) |
| **FCF Yield** | $66.987B ÷ $3,786,953.94M = **1.7689%** | Computed |
| FY2026 Net Income (GAAP) | **$133.749B** | `yfinance` |
| One-time OpenAI investment gain (FY26) | **+$4.963B** net income | Carried forward unchanged from 07-30 (same fiscal year, no fresher figure found) |
| **FY2026 Net Income (normalized, Rule 6)** | $133.749B − $4.963B = **$128.786B** | Computed |
| FY2026 Revenue | **$331.839B** | `yfinance` |
| **Net Margin (normalized)** | $128.786B ÷ $331.839B = **38.81%** | Computed |
| FY2026 D&A | **$38.534B** | `yfinance` |
| **EBITDA (official-Operating-Income basis)** | $155.237B + $38.534B = **$193.771B** | Computed |
| **Net Debt/EBITDA** | −$36.357B ÷ $193.771B = **−0.1876×** (net cash) | Computed |
| **Effective tax rate (FY2026)** | Tax $32.185B ÷ Pretax $165.934B = **19.396%** | `yfinance` |
| **NOPAT** | $155.237B × (1 − 0.19396) = **$125.127B** | Computed |
| Total Stockholders' Equity | **$442.387B** | `yfinance` (unchanged from 07-30) |
| **Invested Capital** | $40.294B + $442.387B = **$482.681B** | Computed (matches `fetch_fundamentals`'s own $482.681B figure — the invested-capital input itself is unaffected by the EBIT issue) |
| **ROIC** | $125.127B ÷ $482.681B = **25.92%** | Computed |
| FCF/NI conversion (normalized) | $66.987B ÷ $128.786B = **52.01%** | Computed |
| Gross Margin (FY2026) | $225.465B ÷ $331.839B = **67.94%** | Computed |
| Revenue 3yr CAGR (FY2023 $211.915B → FY2026 $331.839B) | **16.12%** | Computed |
| Forward EPS (NTM) | **$23.67588** | `yfinance` `forwardEps` (up from $22.72328 on 07-30 — analysts have raised estimates post-beat) |
| **Forward PE** | $509.99 ÷ $23.67588 = **21.540×** | Computed |
| 5yr avg PE (anchor) | 31.492× (range 24.123×–38.730×, n=20 quarters) | Re-verified live |
| TTM EPS growth | $17.28 vs. $13.64 a year ago = **+26.69%** | `yfinance` `get_earnings_dates` reconstruction — same trailing-4-quarter window as 07-30 (no new quarter reported), confirms **Fast Grower** unchanged |
| PEG | 21.540 ÷ 26.69 = **0.8071** | Computed |
| FY2026 dividends paid | **$26.445B** | `yfinance` (full-year FY2026 figure now available — no more statement-lag workaround needed) |
| FY2026 buybacks | **$22.271B** | `yfinance` |
| **Shareholder yield** | ($26.445B + $22.271B) ÷ $3,786,953.94M = **1.2864%** | Computed |

---

## 6. MSFT — Quality Score (2026-06-29 methodology)

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | FY2026 52.01% (normalized) is the only year below 70% in the trailing 4 (FY2023–FY2025 all ≥70%) | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS |
| Net Debt/EBITDA over threshold? | **−0.1876× (net cash)** | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | Yes | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Full script output below (verbatim):

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((38.81/30)x100) = 100.00
ROIC_Component = clamp((25.92/30)x100) = 86.40
Profitability_Score = (100.00 + 86.40) / 2 = 93.20

**Margins (15%)**
GrossMargin_Score = clamp((67.94/80)x100) = 84.92

**Growth (20%)**
Growth_Score = clamp((16.12/25)x100) = 64.48
+10 TAM/pricing-power evidence: Azure crossed $100B annualized revenue, grew 43% YoY in FY2026 Q4
(vs 39-40% guided); commercial RPO +84% YoY to $678B; FY2027 Q1 guidance further accelerates Azure
to 45% constant-currency growth (Microsoft FY2026 Q4 earnings release, 29 Jul 2026 -- no fresher
quarter available, FY2027 Q1 not yet reported as of 28 Sep 2026).
Growth_Score (final, clamped) = 74.48

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - -0.1876/4)) = 100.00

**Moat Signal (15%)**
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Azure crossed $100B annualized revenue, grew 43% YoY (accelerating), FY27 Q1 guided to 45% cc growth -- unchanged basis from 07-30 session, no fresher quarter reported since. |
| brand_premium | True | Microsoft 365 Copilot passed 30 million paid seats (FY2026 Q4) at sustained premium pricing (Frontier Suite E7, $99/user/month) -- unchanged basis from 07-30 session, no fresher quarter reported since. |
| network_effect | True | LinkedIn two-sided network -- unchanged mechanism from every prior session. |
| switching_costs | True | Enterprise identity/security/productivity-stack integration (Entra ID, M365 tiers) -- unchanged mechanism. |
| scale_cost_advantage | False | Same gap as every prior session: no MSFT-specific cost-per-unit citation found against a named smaller competitor; only industry-wide hyperscaler PUE data. Searched again this session (Sep 2026 Azure/AI capex coverage) -- no new evidence found either way. |
Moat_Score = (4/5) x 100 = 80.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((0.5201 - 0.40)/0.60)x100) = 20.02

**Quality Score — Final**
Quality Score = (93.20x0.25) + (84.92x0.15) + (74.48x0.20) + (100.00x0.15) + (80.00x0.15) + (20.02x0.10)
= 79.936 -> rounds to 79.9

# Quality Score = 79.9 — FAILS the 80.0+ gate
```

**Sensitivity (same flagged judgment call as every prior session):** if "scale cost advantage" were credited TRUE, Moat_Score = 100.0 and Quality Score = 79.936 + (20.0×0.15) = **82.9** (passes). No new evidence resolved this ambiguity either way this session — **third consecutive session failing the gate on the primary determination by the same razor-thin ~0.1-point margin** (07-05: 78.3; 07-30: 79.9; today: 79.9).

**# Quality Score = 79.9 (primary) — FAILS the 80.0+ gate.**

---

## 7. MSFT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 21.540 = 4.6425%
Spread = EY − 10Y Treasury = 4.6425% − 5.24% = −0.5975%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 5.24% → **">5%"** bracket (crossed up from "3.5–5%" since 07-30) → **+10**

**Total Rate Modifier for MSFT = +15** (up from +10 on 07-30 — a genuine bracket change, the first since this framework began tracking MSFT)

---

## 8. MSFT — Phase 02 Valuation Score (script output, verbatim)

```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 1.7689/10)) = 82.311

**EV/EBIT**
EV/EBIT_Score = clamp((24.16 - 12)/23 x 100) = 52.870

**Forward PE**
Deviation% = (21.54 - 31.492)/31.492 x 100 = -31.602%
FwdPE_Score = clamp(50 + -31.602x2.5) = 0.000 (fallback formula; Historical PE Modifier already folded in)

**PEG**
PEG_Score = clamp((0.8071 - 0.5)/2.0 x 100) = 15.355

**Rate Environment Gate**
EY = 1/21.54 x 100 = 4.6425%
Spread = EY - 10Y (5.24%) = -0.5975pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.24% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x733.95 + 0.50x639.25 + 0.25x497.19 = 627.4100
Gap Upside % = (627.4100/509.99) - 1 = 23.0240%
Annualized gap = 23.0240% / 2yr = 11.5120%/yr
E = 11.5120 (annualized gap) + 14 (intrinsic growth) + 1.2864 (shareholder yield: 0.6984 div + 0.588 buyback) = 26.7984%/yr
E (26.7984%) >= H (10.0%) -> M = -15 x clamp((26.7984-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.25 + FwdPE_Score x 0.2 + PEG_Score x 0.15
= 48.445

**Final Valuation Score**
Final Score = Raw (48.445) + Rate Modifier (+15) + Upside/Downside Modifier (-15.000)
= 48.445 -> rounds to 48.4

# Valuation Score = 48.4
```

**Fair value scenario architecture (bull/base/bear exit multiples 31.0×/27.0×/21.0×, carried forward unchanged from 07-30):**

| Scenario | Weight | PE applied | Fair Value |
|---|---|---|---|
| Bull | 25% | 31.0× | $23.67588 × 31.0 = **$733.95** |
| Base | 50% | 27.0× | $23.67588 × 27.0 = **$639.25** |
| Bear | 25% | 21.0× | $23.67588 × 21.0 = **$497.19** |

**⚠️ Flag: no fundamental reason found this session to revise the scenario multiples themselves** — the underlying inputs that moved are forward EPS (up on raised analyst estimates) and the live price, not the multiple assumptions.

**Guardrail checks:** (1) catalyst documented — FY27 Q1 earnings ~late Oct 2026 — upside credit allowed. ✓ (2) PW FV ($627.41) sits below the $870 analyst high and below the $577.26 mean consensus PT — scenario-weighted, not the rosy point. ✓ (3) full calc shown above. ✓ (4) bounded ±15, at the −15 floor (10th consecutive session at this floor). ✓

---

## 9. MSFT — Final Valuation Score, Quality Score, and Composite Score

| | Value |
|---|---|
| Raw weighted | 48.445 |
| Rate Gate (Step 1 fail +5, Step 2 bracket +10) | **+15** (up from +10 on 07-30) |
| Upside/Downside Modifier | −15.0 (E = +26.80%) |
| **FINAL VALUATION SCORE** | **48.4** |
| Prior valuation score | 38.9 (07-30) |
| **Quality Score** | **79.9 (FAILS 80.0+ gate — primary determination, by 0.1pt; 82.9 sensitivity, see §6)** |

**Composite Score: NOT computed by script** — `python -m scripts.scoring.composite_score --set quality_score=79.9 --set valuation_score=48.4` correctly refused:
```
# Composite Score REFUSED — Quality Score fails the 80.0+ gate
Quality Score 79.9 < 80.0 — fails the gate, Composite Score is not computed for a company that hasn't cleared Phase 01
```

*Reference only (not the operative Composite Score, computed by hand per the exact 07-30 convention — not via the script, which refuses this by design):*
```
If Quality = 79.9 (primary):  Composite = 0.50×(100−79.9) + 0.50×48.4 = 10.05 + 24.2 = 34.25 → 34.3
If Quality = 82.9 (alt/pass): Composite = 0.50×(100−82.9) + 0.50×48.4 =  8.55 + 24.2 = 32.75 → 32.8
```
Both reference numbers land in the 30.0–49.9 "Standard BUY" band. **Not used to drive the action recommendation below** — same treatment as 07-05 and 07-30.

**Action recommendation basis:** falls back to the **raw Valuation Score (48.4)** against the Action Table, exactly as in the two prior sessions.

---

## 10. MSFT — Action Recommendation & Position Cap Check

**Raw Valuation Score 48.4 → nominally BUY — Standard position 3–5% (30.0–49.9 band)** — same band as 07-30's 38.9, now near the top of the band (the score has risen ~24% since 07-30 mainly on the Rate Regime bracket jump, partially offset by the stock getting somewhat more expensive on FCF Yield/EV-EBIT as price rose).

**THREE independent gates still block adding capital — same structure as 07-30:**

1. **⚠️ Position cap (Upgrade 7) — status uncertain, flagged rather than assumed.** Last documented weight is **14.24%** (22 Aug 2026 sync), which predates the full +13.48% price move since 07-30. This session does not recompute portfolio weights (`/sync-portfolio`'s job) but flags that the actual current weight is likely close to, and could be at or over, the 15% hard cap.
2. **🚫 Risk/Reward ratio.** See §12 — the order setup R/R is **1.33:1**, below the 2:1 minimum. This remains the clearest, unambiguous block.
3. **🚫 Quality Score gate (primary determination), unchanged at a razor-thin margin.** Quality Score 79.9 fails the 80.0+ bar by only 0.1 point — the third consecutive session failing on the primary determination at essentially the same margin as 07-30. Does not force an exit (quality-gate failure alone is not a valid Phase 06 exit trigger) and this is a large, pre-existing holding, not a new candidate — continuing Phase 04 Quality Watch treatment.

**Net: no fresh capital added.** Conclusion unchanged from 07-05 and 07-30: do not add. The standing compliance trim from the 2026-06-15 rebalance remains overdue. The open question of logging MSFT as a **Human Override** (per the ZS precedent) remains flagged, not resolved, by this session.

---

## 11. Portfolio / Compliance Note (independent of valuation score)

MSFT's last documented weight (14.24%, 22 Aug 2026 sync) predates the full price move since that sync — the actual current weight is unknown without a fresh sync but is plausibly close to or over the 15% hard cap given the stock's continued run. This is the **10th consecutive session** flagging a position-cap concern for MSFT. Recommend prioritizing a fresh `/sync-portfolio` run and the standing [2026-06-15 rebalance](2026-06-15-rebalance.md) compliance trim.

---

## 12. Order Setup (shown for completeness — nominal BUY band — both gates above still block it)

Run via `python -m scripts.scoring.order_setup --input inputs.json` (verbatim):

```
## Order Setup

Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (627.41) x (1 - 25%) = 470.5575
Live price 509.99 vs buy price ceiling 470.5575 -> limit order at buy price (live price above ceiling); entry price used = 470.5575
Primary Sell Target = Fair Value = 627.4100
Bull-Case Trim Target = Bull FV (733.95) x 0.90 = 660.5550
Stop Loss = Entry Price (470.5575) x (1 - 25%) = 352.9181
R/R Ratio = (Sell Target 627.4100 - Entry 470.5575) / (Entry 470.5575 - Stop 352.9181) = 156.8525/117.6394 = 1.3333:1
*** FLAG: R/R 1.3333:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (61622.32) x 1.5% = 924.3348
Risk Per Share = Entry (470.5575) - Stop (352.9181) = 117.6394
Shares by risk-based sizing = 924.3348 / 117.6394 = 7.8574
Allocation cap = Portfolio Value (61622.32) x 5% = 3081.1160 -> 6.5478 shares
Position Size (shares) = min(risk-based, cap) = 6.5478  [binding: allocation cap]
Position Size ($) = 6.5478 x 470.5575 = 3081.1160
Current shares held = 17; gap vs. target = -10.4522
```

**⚠️ R/R (1.33:1) still fails the 2:1 minimum (Rule 6).** Per Rule 6, R/R below 2:1 = do not enter, independent of the score band, the position cap, or the Quality Score question. Note the model target size (6.55 shares, ~$3,081) is well **below** the 17 shares actually held — the position is already model-oversized, consistent with the standing compliance-trim flag in §11.

---

## 13. Next Review Trigger

- **Routine:** MSFT FY2027 Q1 earnings, expected late Oct 2026 (exact date not yet published — flagged, §4 item 6). Will bring a genuinely fresh quarter of fundamentals for the first time since 07-30.
- **🚨 Open item (elevated priority, 10 sessions running): confirm current portfolio weight via `/sync-portfolio`.** The last-documented 14.24% figure predates the full price move since 07-30.
- **🚨 Open item (unresolved, 3 sessions running): resolve the Quality Score gate question (§6).** The gap has held at ~0.1 point across two consecutive sessions — either (a) obtain a harder, MSFT-specific cost-per-unit citation for "scale cost advantage," or (b) accept the primary 79.9 determination and decide how to treat a large held position sitting this close to the framework's own 80.0+ quality gate — log as a Human Override or continue as a Phase 04 monitoring item.
- **Open compliance item (10th flag): dedicated `/rebalance` execution of the position-cap trim** — still not executed.
- **Open methodology item:** Owner Earnings (Upgrade 1) decision for non-disclosing mega-caps — 10th consecutive session.
- **New monitoring item (this session): the Rate Environment Gate bracket change (3.5–5% → >5%)** — this is the first time in this framework's tracked MSFT history that the 10Y has crossed into the >5% bracket; watch whether this is sustained or reverses at the next session, since it is currently adding a full +5pp to MSFT's valuation score versus the prior bracket.
- **Monitoring items (unchanged, not Rule 9 triggers):** (1) the securities class action, case No. 26-cv-02071; (2) the confirmed workforce reduction; (3) the gross-margin compression trend; (4) FY2027 capex guidance (calendar-2026 capex tracking toward ~$175B) — watch for the next quarter's confirmed figure.

---

## Glossary

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year — a quick gauge of where the current price sits within its recent trading history. |
| **bps (basis points)** | 1 bps = 0.01 percentage points. 50 bps = 0.5%. |
| **Buyback yield (net buyback yield)** | The rate at which a company's share count shrinks per year from repurchasing its own stock (net of any new shares issued), a component of shareholder yield. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; not adopted for MSFT this session (reference-only figures shown, clearly labeled). |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **Effective tax rate** | Tax provision ÷ pretax income for a given period — used to compute NOPAT for the ROIC calculation. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT, EV/EBITDA** | Enterprise Value (market cap + net debt) / multiples comparing EV to operating profit, independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **Gross Margin** | Gross Profit ÷ Revenue. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; flagged (not adopted) for MSFT this session pending user decision. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set — a 25% MoS means buying at 75% of estimated fair value. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means a net-cash position. |
| **NI (Net Income)** | Accounting profit after all expenses, interest, and taxes. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NTM (Next Twelve Months)** | A forward-looking estimate covering the next twelve months from today. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — adjusts PE for growth. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value — 25% bull + 50% base + 25% bear. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. MSFT: 79.9 (fails the gate by 0.1pt), sensitivity 82.9. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **RPO (Remaining Performance Obligations) / cRPO** | Contracted future revenue not yet recognized — a forward-looking backlog metric; MSFT's commercial RPO grew 84% YoY to $678B (last reported quarter). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work. |
| **Rule 1–8, Rule 10 (10-Rule Fair Value Framework)** | The numbered rules governing valuation methodology, including Rule 6 (normalize one-off items before valuing) and Rule 10 (separate intrinsic value from market price with a documented catalyst). |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, guidance revision, management change, material M&A, macro shift, or a >15% unexplained price move. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent four reported quarters combined, used to reflect a company's current run-rate. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
