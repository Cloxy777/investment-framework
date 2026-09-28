# RESCORE — AVGO (Broadcom Inc.) — 2026-09-28

**Task type:** RESCORE (mode `--both`)
**Trigger:** Scheduled/user-requested rescore, 13 days after the 2026-09-15 session — no new 8-K on file (confirmed directly via SEC EDGAR's 8-K filing index for CIK 0001730168: most recent filing remains 2026-09-02, no filing since). Treated as a full re-run: live-price-dependent figures refreshed throughout, TTM/fundamental figures carried forward with the same "flagged, carried forward" discipline as every prior AVGO session.
**Date:** 28 Sep 2026
**10Y US Treasury Yield:** **5.24%** (WebFetch: TradingEconomics, 28 Sep 2026 reading — "rose to 5.24% on September 28, 2026, marking a 0.08pp increase from the previous session," a near-20-year high) — cross-checked via WebSearch (multiple outlets, incl. Babypips/CNBC coverage) reporting **5.21%** intraday the same day; the ~3bps gap is ordinary same-day quote-timing noise, both readings sit in the same >5% bracket. **Regime unchanged from 2026-09-15's 5.018%** — the 10Y has stayed above 5% continuously since first crossing it on 14–15 Sep 2026, and has now risen further.
**Rate Regime Modifier (Step 2):** **+10** (10Y still in the >5% bracket — unchanged bracket from 2026-09-15, though the yield itself rose further within that bracket)
**Current AVGO portfolio weight:** 3.50% per [holdings.md](../portfolio/holdings.md) (as of the 2026-09-20 sync; not re-synced this session — refreshing live weight is `/sync-portfolio`'s job, out of `/rescore`'s scope) — still held as an **open, unresolved Human Override**
**Sector:** Semiconductors (fabless — AI accelerators/networking) + Infrastructure Software (VMware)
**Last review:** 15 Sep 2026 (Valuation 70.9 / Quality 86.3 / Composite 42.3) — see [session](../sessions/2026-09-15-rescore-avgo.md)

---

## 0. Override status (reported, not resolved this session)

Per [override-log.md](../portfolio/override-log.md): AVGO's **2026-06-16 override remains open** — still "Open — under review," no rationale supplied. Not this command's scope to resolve.

**Separately, and more urgently flagged since the 2026-09-15 session:** [holdings.md](../portfolio/holdings.md) now carries a top-of-file banner for a **new, undocumented AVGO BUY order — 5 sh @ $310.60 GTC limit, order 87937891, placed 2026-09-19** — 4 days after the 2026-09-15 session explicitly concluded "No order is placed" (R/R fails the minimum threshold across the full MoS/stop range). That session's computed buy range was $248.67–$266.43; this order's $310.60 limit sits **~16.6% above** the top of that range and, as of this session, still **below the live price** ($349.64), meaning it remains a live, working, unfilled GTC order that could fill on a further pullback without any documented rationale in `sessions/`, `decisions/`, or `override-log.md`. **This is not this command's scope to resolve** (no MCP order-management tool exists in this repo, and `/rescore` never places/cancels orders) — carried forward as an unresolved flag for the user's attention, consistent with this session's own newly-computed buy range below (§9).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$349.64** | IBKR `get_price_snapshot` (contract_id 313130367, NASDAQ), **REALTIME** status, `last` trade $349.64. Cross-validated against `yfinance`'s `currentPrice`/`regularMarketPrice` fields, reading **$349.665** — within 0.01%, immaterial. |
| Change vs. prior close | −$3.17 (−0.90%) per IBKR `change` field | IBKR `get_price_snapshot` |
| 52-week range | $289.48 – $494.23 (IBKR `misc_statistics`, 52w) | Essentially unchanged from the 2026-09-15 session's $289.96–$495.00 (normal daily drift in the rolling window). |
| Analyst consensus PT | $531.85 (`yfinance`, 47 analysts) | Unchanged from the 2026-09-15 session — no new analyst-target data surfaced this session. |
| Move since last rescore | $345.55 (15 Sep) → $349.64 (28 Sep) = **+1.18%** | Well under the 15% Rule 9 unexplained-move threshold; this session's rescore is scheduled/routine, not price-triggered. |
| Broader context (WebSearch) | The stock has traded in a wide band this month, touching ~$364 mid-week (24 Sep, per Motley Fool coverage) before easing back toward $350 — consistent with an ongoing rates-driven selloff across growth/tech names as the 10Y presses to fresh multi-decade highs, not an AVGO-specific move. | [Seeking Alpha](https://seekingalpha.com/news/4639799-broadcom-forecasts-58b-fiscal-2026-ai-revenue-and-outlines-115b-in-2027-230b-in-2028), [Motley Fool](https://www.fool.com/investing/2026/09/24/broadcoms-latest-prediction-makes-the-stock-a-no-b/) |

---

## 2. Data Gathered — Sources & Gaps

**No new 8-K since the 2026-09-02 Q3 FY2026 earnings release** — re-confirmed via SEC EDGAR's 8-K filing index for CIK 0001730168 (most recent 10 filings checked; latest remains 2026-09-02). Per the "no invent/estimate" discipline, the TTM window is **not** rolled forward this session — every TTM/fundamental figure below is carried forward unchanged from the 2026-09-15 session (independently re-verified against fresh `yfinance` pulls this session, see the flag below), and only live-price-dependent figures are refreshed.

| Metric | Value | Status |
|---|---|---|
| TTM Revenue | $89,104M | Carried forward — re-verified via fresh `python -m scripts.fetch_fundamentals AVGO` this session (net margin 42.944%, gross margin 68.770%, revenue 3yr CAGR 24.378%, FCF/NI TTM 102.974% all matched the prior session's figures exactly — confirms no new fiscal data has landed) |
| TTM Net Income (GAAP) | $38,265M | Carried forward, re-verified |
| TTM GAAP Operating Income (EBIT) | $42,814M | Carried forward, re-verified |
| TTM FCF | $39,403M | Carried forward |
| TTM Gross Profit / Margin | $61,277M / 68.77% | Carried forward, re-verified |
| TTM Interest Expense | $3,116M | Carried forward |
| TTM D&A | $8,764M | Carried forward |
| TTM EBITDA | $51,578M | Carried forward |
| Net Debt (Q3FY26 end, 2 Aug 2026) | $35,444M | Carried forward — **re-derived this session directly from `yfinance`'s quarterly balance sheet (`quarterly_balance_sheet`, 2026-07-31 column: Total Debt $59,419M, Cash $23,975M, Net Debt $35,444M) — an exact match to every prior AVGO session's figure.** ⚠️ **Data-quality flag, new this session:** `scripts/fetch_fundamentals.py`'s own `net_debt_to_ebitda` output this run read **0.937×** (vs. the correct 0.687× used above) — traced to the script pulling from `yfinance`'s **annual** `balance_sheet` (still stamped FY2025-10-31, the last full fiscal year, not yet rolled forward to Q3 FY2026) rather than the fresher `quarterly_balance_sheet`. The annual sheet shows Total Debt $65,136M / Cash $16,178M / Net Debt $48,958M — genuinely stale data, not a new fundamental development. **Overridden manually this session** using the quarterly balance sheet, consistent with every prior AVGO session's methodology; flagged here as a script bug worth fixing (the script's own docstring already documents a related, different `yfinance` drift issue) rather than silently trusted. The same staleness affects the script's `roic_pct` (28.144%) and `market_cap`/`enterprise_value`/`ev_ebit` outputs (mixing a fresh TTM income-statement window with a stale FY2025 balance-sheet denominator) — none of the script's balance-sheet-dependent outputs were used directly this session; all were manually reconstructed from the quarterly balance sheet instead. |
| Total Equity | $99,690M | Carried forward, re-verified via `quarterly_balance_sheet` |
| Diluted shares (Q3FY26, GAAP basis) | 4,887M | Carried forward — used consistently for Market Cap/EV across every AVGO session to date, for methodological continuity. `yfinance`'s `sharesOutstanding` field reads 4,773.6M (basic, more current) — same ~2.3% gap flagged in every prior session, not re-litigated here. |
| Forward EPS | **$19.38391** (fresh, `yfinance` `forwardEps`) | Refreshed — essentially unchanged from $19.384 on 2026-09-15 (normal rounding-level drift) |
| Forward PE | **18.038×** ($349.64 ÷ $19.38391) | Refreshed |
| 5yr PE range (reconstructed) | Avg 29.892×, Low 13.365×, High 52.758× (n=20 quarters) — **fresh, successfully computed this session** (`pe_mode: "range"`, no fallback needed) | The 2026-09-02 earnings-date row's `Reported EPS` still shows `NaN` in `yfinance`'s `get_earnings_dates` (unbackfilled, same flag as the last 2 sessions), but the rolling 20-quarter reconstruction window doesn't require that specific print — it still resolves cleanly from older, already-reconstructible quarters. Small drift vs. the 2026-09-15 session's Avg 29.9465×/Low 13.3897×/High 52.8544× is normal window-edge rounding, not a data change. |
| Beta | 1.457 | Unchanged (`yfinance` `info.beta`) — identical to 2026-09-15 |
| Effective tax rate (normalized) | 21% carried forward, flagged | Unchanged — no new "clean" quarter since 2026-09-15. (Note: `fetch_fundamentals`'s own TTM effective-tax-rate calc reads 5.45% this run, computed off actual TTM tax-provision/pretax-income — genuinely volatile quarter-to-quarter per the glossary's own "Effective tax rate" entry; kept the normalized 21% for continuity with every prior AVGO session's NOPAT/ROIC calc rather than importing a swing that reflects one-off tax items, not sustainable economics.) |
| VMware/intangible amortization add-back | $9.3B/yr carried forward, flagged | Unchanged — see the 2026-07-04/09-03 sessions for full reasoning |
| Dividend | $0.65/quarter ($2.60/yr annualized) | Unchanged — no new dividend announcement found this session |

**No metric was invented or estimated.** Every fresh figure traces to IBKR's live snapshot, `yfinance`'s live/quarterly fields (cross-checked directly via Python where the wrapper script's own annual-balance-sheet basis was stale — see the flag above), or WebSearch/WebFetch cross-checks against TradingEconomics/SEC EDGAR/Seeking Alpha/Motley Fool; every carried-forward figure is explicitly flagged with the reason it wasn't independently re-derived this session.

---

## 3. Quality Score (Phase 01 gate) — recomputed, inputs unchanged

**Hard disqualifier check (re-verified, unchanged):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs? | TTM 102.97% | disqualify if <70% for 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | 0.687× | disqualify if >2.5× | ✅ PASS |
| FCF-positive 3+ consecutive years? | FY2023–FY2025 all positive, FY2026 trending strongly positive | disqualify if not | ✅ PASS |

Full script output (`python -m scripts.scoring.quality_score --input <inputs.json>`), pasted verbatim:

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((42.944/30)x100) = 100.00
ROIC_Component = clamp((30.47/30)x100) = 100.00
Profitability_Score = (100.00 + 100.00) / 2 = 100.00

**Margins (15%)**
GrossMargin_Score = clamp((68.77/80)x100) = 85.96

**Growth (20%)**
Growth_Score = clamp((24.38/25)x100) = 97.52
+10 TAM/pricing-power evidence (refreshed, see below)
Growth_Score (final, clamped) = 100.00

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - 0.687/4)) = 82.82

**Moat Signal (15%)**
Moat_Score = (2/5) x 100 = 40.00  (unchanged evidentiary basis: market share, switching costs)

**FCF Quality (10%)**
FCFQuality_Score = clamp(((1.0297 - 0.40)/0.60)x100) = 100.00

**Quality Score — Final**
Quality Score = (100.00x0.25) + (85.96x0.15) + (100.00x0.20) + (82.82x0.15) + (40.00x0.15) + (100.00x0.10)
= 86.318 -> rounds to 86.3

# Quality Score = 86.3 — PASSES the 80.0+ gate
```

ROIC = NOPAT ÷ Invested Capital = (Normalized EBIT $52,114M [$42,814M GAAP + $9,300M carried-forward amortization add-back] × (1 − 0.21)) ÷ ($59,419M debt + $99,690M equity − $23,975M cash = $135,134M) = $41,170.1M ÷ $135,134M = **30.47%** — identical methodology and result to every AVGO session since 2026-07-04.

**Growth TAM/pricing-power evidence, refreshed this session:** Broadcom's Q3 FY2026 earnings call (2026-09-02) and subsequent coverage (Seeking Alpha, 24 Sep 2026; Motley Fool, 24 Sep 2026) confirm management raised its AI-semiconductor revenue outlook to **$58B for FY2026**, with **$115B guided for FY2027** and **$230B for FY2028**, underpinned by named multi-year hyperscaler supply commitments: Anthropic targeting 5GW of TPU 8i deployment in 2027 with a further 10GW line of sight, OpenAI's custom "Jalapeno" chip, and accelerated Google Ironwood/TPU 8i shipment volumes. This is a genuine refresh (more specific, longer-dated forward guidance than the 2026-09-15 session had), not a re-citation of stale Q2/Q3 data — same +10 basis as every prior AVGO session.

**Moat Signal — unchanged, still flagged:** the "market share stable/growing" signal remains backed only by company-reported growth data and named hyperscaler relationships, not a third-party market-share-tracker citation — the same evidentiary gap flagged in every prior AVGO session, no new third-party data surfaced this session. Moat_Score stays 40.0 (2/5: market share, switching costs).

**Quality Score = 86.3 — unchanged from 2026-09-15**, exactly as expected: every input is a fundamental/TTM figure, none of which moved (no new 8-K). Sensitivity check (carried forward, unchanged basis): even excluding the borderline "market share" moat signal entirely (Moat_Score → 0), Quality Score would still read **80.3** — still clears the gate.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $349.64 / $19.38391 = 18.038x
EY = 1 / 18.038 x 100 = 5.5439%
Spread = EY − 10Y Treasury = 5.5439% − 5.24% = +0.3039pp
```
Spread (+0.30pp) < +1.5% → **fails** → **+5 additive** (yellow flag, not a veto). The margin narrowed further vs. 2026-09-15's +0.59pp — the 10Y rose faster (+0.22pp) than the earnings yield improved on the modestly higher price.

**Step 2 — Rate Regime Modifier**
10Y = 5.24% → **>5% bracket** (unchanged bracket from 2026-09-15) → **+10**

**Combined Rate Modifier: +15** (unchanged from 2026-09-15's +15 — same bracket, Step 1's marginal narrowing has no effect on the discrete +5/+0 step)

---

## 5. Valuation Score (Phase 02)

Full script output (`python -m scripts.scoring.valuation_score --input <inputs.json>`), pasted verbatim:

```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 2.3057/10)) = 76.943

**EV/EBIT**
EV/EBIT_Score = clamp((40.745 - 12)/23 x 100) = 100.000

**Forward PE**
FwdPE_Score (raw) = clamp((18.038 - 13.365)/(52.758 - 13.365) x 100) = 11.863
Deviation vs 5yr avg (29.892) = (18.038 - 29.892)/29.892 x 100 = -39.656%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(11.863 + -10) = 1.863

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/18.038 x 100 = 5.5439%
Spread = EY - 10Y (5.24%) = 0.3039pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.24% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x724.96 + 0.50x484.6 + 0.25x247.14 = 485.3250
Gap Upside % = (485.3250/349.64) - 1 = 38.8071%
Annualized gap = 38.8071% / 1.2yr = 32.3392%/yr
E = 32.3392 (annualized gap) + 12.0 (intrinsic growth) + 0.7437 (shareholder yield: 0.7437 div + 0.0 buyback) = 45.0829%/yr
E (45.0829%) >= H (10.0%) -> M = -15 x clamp((45.0829-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 71.150

**Final Valuation Score**
Final Score = Raw (71.150) + Rate Modifier (+15) + Upside/Downside Modifier (-15.000)
= 71.150 -> rounds to 71.1

# Valuation Score = 71.1
```

**Inputs behind the script run, shown for transparency:**

```
Market Cap = $349.64 x 4,887M shares = $1,708,940.28M   (diluted-share basis, carried forward for continuity)
FCF Yield = $39,403M / $1,708,940.28M = 2.3057%

EV = Market Cap $1,708,940.28M + Net Debt $35,444M = $1,744,384.28M
EV/EBIT (GAAP TTM) = $1,744,384.28M / $42,814M = 40.745x
```
**Normalization flag (carried forward):** Normalized EBIT ($52,114M) → normalized EV/EBIT = **33.48×**, still below the 35× ceiling, continuing the widening GAAP-vs-normalized gap flagged since 2026-09-03. **Kept GAAP basis as primary** (EV/EBIT_Score = 100.0, saturated) for continuity with every prior AVGO session; using the normalized figure instead would pull the raw weighted score down modestly but not change the action band. Flagged again for future attention (3rd consecutive session).

**Catalyst window (Rule 10):** same documented catalyst as every session since 2026-07-04 — management's FY2027 AI-semiconductor revenue confirmation point (now freshly reinforced by the specific $115B FY2027 / $230B FY2028 guidance cited in §3), expected to be confirmed around AVGO's FY2027 year-end results (~December 2027). From 28 Sep 2026, that's **~439 days ≈ 14.4 months ≈ 1.20 years** — shorter than 2026-09-15's 1.24yr, purely the passage of 13 days against a fixed target date; no new information changes the target date itself.

**Bull/base/bear fair values, unchanged assumption set (34×/25×/15× multiples on forward EPS, carried forward — no new information to justify revising them):**

| Scenario | Wt | EPS basis | Multiple | Fair Value |
|---|---|---|---|---|
| Bull | 25% | $19.38391 × 1.10 = $21.322 | 34× | **$724.96** |
| Base | 50% | $19.38391 | 25× | **$484.60** |
| Bear | 25% | $19.38391 × 0.85 = $16.476 | 15× | **$247.14** |

---

## 6. Final Valuation Score

**Valuation Score = 71.1 — "TRIM 25–30%" band (70.0–79.9)** per the raw Action Table — essentially flat vs. 2026-09-15's 70.9 (a 0.2-point move).

**⚠️ Same finding as 2026-09-15: this move is a rates story, not an AVGO story.** Decomposing vs. 2026-09-15:
- Raw weighted sub-scores: 70.93 → 71.15 (**+0.22**, marginally more expensive — a slightly higher price with unchanged TTM fundamentals)
- Rate Modifier: unchanged at +15 (10Y stayed in the same >5% bracket, just moved further within it)
- Upside/Downside Modifier: unchanged at the −15.0 cap (still fully saturated)

The raw Valuation Score has now sat in the 70.0–79.9 "TRIM" band for two consecutive sessions — still driven by the Rate Environment Gate's regime shift, not by any deterioration in AVGO's own numbers. See §7 for why the Composite Score, which governs the action table, does not follow the raw score into a trim recommendation.

---

## 7. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 86.3) + 0.50 × 71.1
                = 0.50 × 13.7 + 35.55
                = 6.85 + 35.55
                = 42.40 → 42.4
```

**Composite Score = 42.4 — stays in the "Cheap" (30.0–49.9) band**, up marginally (less attractive) from 42.3 on 2026-09-15 — a 0.1-point move, essentially flat. Per [valuation-scoring.md](../framework/valuation-scoring.md)'s explicit instruction, the Composite Score — not the raw Valuation Score — governs the Phase 03/05 action table once a Quality Score is on file. AVGO's unchanged, still-strong 86.3 Quality Score continues to absorb the rate-driven valuation-score pressure, keeping the Composite well short of the 50.0+ "Hold" band, let alone the 70.0+ trim band the raw Valuation Score alone would suggest.

---

## 8. Action Recommendation

Composite Score 42.4 stays in the **30.0–49.9 "Cheap" → Standard position 3–5%** band — nominally BUY-eligible. Full order setup run below, per the operating brief.

### Fair Value — two methods, triangulated (Rule 1: Tech/Growth → DCF primary, Multiples secondary)

**Method A — 3-Stage DCF (Rule 2).** Same 10-year growth-fade schedule as every prior session, rebased on the unchanged $39,403M TTM FCF and a WACC refreshed for the current price-based capital-structure weights and treasury yield:

```
WACC build:
  Cost of equity = Rf (5.24%) + Beta (1.457) x ERP (5.0%, assumed) = 12.525%
  Cost of debt (pretax) = TTM interest expense $3,116M / Total Debt $59,419M = 5.244%; after-tax (21%) = 4.143%
  Weights: E/(D+E) = 96.64% (Market Cap $1,708,940.28M), D/(D+E) = 3.36% (Debt $59,419M)
  WACC = 96.64%x12.525% + 3.36%x4.143% = 12.240%

Stage 1 (yrs 1-5), FCF base $39,403M, same growth path as every prior session:
  y1 +25% -> $49,253.8M | y2 +20% -> $59,104.5M | y3 +15% -> $67,970.2M | y4 +12% -> $76,126.6M | y5 +10% -> $83,739.3M

Stage 2 (yrs 6-10), linear fade from 10% to the 2.5% terminal rate:
  y6 $90,857.1M | y7 $97,217.1M | y8 $102,564.0M | y9 $106,666.6M | y10 $109,333.3M

Terminal Value (at y10) = $109,333.3M x 1.025 / (0.12240 - 0.025) = $1,150,581.4M
Terminal Value as % of total DCF EV = 45.4% (well under the 75% Rule 4 sanity cap)

Sum of discounted FCFs (yrs 1-10) = $435,520.8M
PV of Terminal Value = $362,610.8M
Enterprise Value (DCF) = $798,131.7M
Equity Value = $798,131.7M - Net Debt $35,444M = $762,687.7M
DCF Fair Value / share = $762,687.7M / 4,887M = $156.06
```
(Down modestly from $160.10 on 2026-09-15 — purely the higher WACC, on the higher risk-free rate, with beta and the growth path unchanged.)

**Method B — Scenario-weighted multiples (§5 PW Fair Value):** **$485.33**

**⚠️ Same material finding as every prior session — wide divergence between the two methods**, same underlying tension: a disciplined GDP-terminal-growth DCF vs. AVGO's own trailing 5-year PE range.

```
Triangulation (Rule 3, Tech/Growth weights): Blended FV = 40% x DCF + 60% x Multiples
                                            = 0.40 x $156.06 + 0.60 x $485.33
                                            = $62.42 + $291.20
                                            = $353.62
```

### Order Setup Checklist

Full R/R sweep across the applicable 30.0–49.9-band MoS × stop matrix (script output, `python -m scripts.scoring.order_setup --input <inputs.json>`, run once per MoS/stop combination):

| MoS | Stop | Buy Price | Stop Loss | R/R |
|---|---|---|---|---|
| 25% | 25% | $265.22 | $198.91 | 1.33:1 |
| 25% | 30% | $265.22 | $185.65 | 1.11:1 |
| 30% | 25% | $247.53 | $185.65 | **1.71:1 (best case)** |
| 30% | 30% | $247.53 | $173.27 | 1.43:1 |

```
[✓] Composite Score (incl. Quality blend):    42.4 — "Cheap" (30.0-49.9 band)
[✓] Expected annual return E / catalyst:      +45.08% / 1.20yr (feeds the Upside/Downside Modifier, §5)
[✓] Upside/Downside Modifier applied:         -15.0
[✓] DCF Fair Value:                           $156.06
[✓] Multiples-Based Fair Value:               $485.33
[✓] Blended Fair Value:                       $353.62
[ ] Margin of Safety %:                       25-30% (Composite 30.0-49.9 band)
[✓] PRIMARY SELL TARGET:                      $353.62 (Blended FV, baseline)
[✓] BULL-CASE TRIM TARGET:                    $724.96 x 0.90 = $652.46
[ ] STOP LOSS: 25-30% max loss from Buy Price  (range $173.27-$198.91 depending on MoS/stop combination)
[✗] Risk/Reward Ratio — checked across the full matrix above: best case 1.71:1 — FAILS the 2:1 minimum throughout.
```

**Per fair-value-methodology.md Step 6: R/R fails the minimum threshold across the entire applicable MoS/stop range. No order is placed.**

**Position sizing is also moot for a different reason:** AVGO's current 3.50% weight already sits **within** the Composite Score's implied 3–5% "Standard position" target band — no sizing gap to fill even before the R/R gate is considered.

### Net Action: **HOLD** — maintain the current 6-share position as-is

- No trim: Composite Score (42.4) is far below any trim threshold (70.0+) — the Composite (not the raw Valuation Score's 71.1) is the number the action table runs against.
- No add: R/R on the computed order setup fails the 2:1 minimum (best case 1.71:1), and the position is already within its Composite-Score-implied target size.
- **The open 2026-06-16 override remains unresolved** (§0) — unchanged by this rescore.
- **The undocumented 2026-09-19 BUY order (5 @ $310.60, order 87937891) remains open and unresolved** (§0) — sitting ~16.6% above this session's own freshly-computed buy range ($247.53–$265.22), same gap flagged at the time the order was discovered.

**Same action band as the 2026-09-15 session (HOLD)** — the underlying picture is essentially unchanged: Quality Score identical at 86.3, Composite Score essentially flat (42.3 → 42.4), and the raw Valuation Score's continued residence in the "TRIM" band remains fully explained by the Rate Environment Gate rather than any AVGO-specific development. This is the Composite Score construct working exactly as designed for a second consecutive session.

---

## 9. Next Review Trigger

**Date/event:** AVGO's Q4 FY2026 earnings release (expected ~December 2026, per the typical AVGO reporting cadence — `yfinance`'s `get_earnings_dates` confirms a scheduled print on 2026-12-09) — re-run Phase 01/02 with refreshed TTM figures. **Follow-ups carried forward, worth checking first at that rescore:**
1. **Fix or work around the `fetch_fundamentals.py` staleness bug** flagged in §2 — its `net_debt_to_ebitda`/`roic_pct`/`market_cap`/`enterprise_value` outputs currently mix a fresh quarterly income-statement TTM with a stale annual (FY2025) balance sheet. Worth a PR to switch the script's balance-sheet source to `quarterly_balance_sheet`, since the Q4 FY2026 print due 2026-12-09 will make the annual sheet even more stale relative to the quarterly one.
2. **Watch the EV/EBIT GAAP-vs-normalized divergence** (§5) — normalized EV/EBIT (33.48×) remains below the 35× ceiling but continues to track close to it; worth a `decisions/` entry if it ever crosses and starts moving the actual score.
3. **Monitor the Rate Environment regime** — the 10Y has now spent two consecutive sessions above 5% and rose further this session (5.018% → 5.24%). If it falls back under 5% before the next scheduled rescore, the Rate Regime Modifier reverts to +5 and the raw Valuation Score would fall back toward the mid-60s, all else equal (not itself a trigger to rescore early).
4. **The two open, undocumented order/override items flagged in §0** — the 2026-06-16 Human Override and the 2026-09-19 BUY order (87937891) — both need the user's direct attention; neither is resolved by a rescore.

Earlier trigger on a >15% unexplained move from $349.64 (Rule 9), a further guidance revision/M&A/management change, or new third-party market-share data that would firm up the Moat_Score's remaining evidentiary gap.

---

## Glossary

- **8-K**: The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish a quarterly earnings press release ahead of the fuller 10-Q/10-K.
- **Beta**: A stock's sensitivity to overall market moves — used as an input to estimate cost of equity in a DCF's WACC.
- **bps (basis points)**: 1 bps = 0.01 percentage points. 50 bps = 0.5%.
- **CAGR**: Compound Annual Growth Rate.
- **CapEx**: Capital Expenditure.
- **Catalyst window**: The timeframe (per Rule 10, typically 18-24 months) within which a documented event is expected to close the price/fair-value gap.
- **Composite Score**: This framework's blended 0.0-100.0 ranking number — `0.50 x (100 - Quality Score) + 0.50 x Valuation Score` — computed only after a company clears the 80.0+ Quality Score gate.
- **D&A**: Depreciation & Amortization.
- **DCF (Discounted Cash Flow)**: A valuation method estimating a company's worth today by projecting future cash flows and discounting them back to the present.
- **EBIT**: Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA**: Earnings Before Interest, Taxes, Depreciation, and Amortization.
- **Equity Risk Premium (ERP)**: The extra return equity investors demand over the risk-free rate — an assumed DCF input, not a fetched fact.
- **EPS**: Earnings Per Share.
- **EV**: Enterprise Value — market cap + debt - cash.
- **EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **EY (Earnings Yield)**: 1 / Forward PE, compared against bond yields in the Rate Environment Gate.
- **FCF (Free Cash Flow)**: Cash generated after running and maintaining the business.
- **FCF Yield**: FCF / Market Cap (or EV) — higher is cheaper.
- **FCF/NI conversion ratio**: FCF / Net Income — a cash-quality check.
- **Forward PE**: Price / next-twelve-months expected EPS.
- **FV (Fair Value)**: The analyst's estimate of intrinsic worth, independent of market price.
- **GAAP**: Generally Accepted Accounting Principles.
- **Gross Margin**: Gross Profit / Revenue.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score.
- **Human Override**: A position opened or held outside the framework's own rules — tracked for life in `override-log.md`. AVGO's 2026-06-16 entry is one, and remains open.
- **Hurdle rate**: The minimum acceptable annual return (10% in this framework) the Upside/Downside Modifier measures expected return against.
- **Invested Capital**: The total capital (debt + equity, net of cash here) put to work in a business — the denominator of ROIC.
- **IRR**: Internal Rate of Return.
- **Moat**: A durable competitive advantage protecting a business's profits from competitors.
- **MoS (Margin of Safety)**: How far below fair value the buy price is set.
- **Net Debt/EBITDA**: A leverage ratio — this framework's primary balance-sheet-risk gate.
- **Net Margin**: Net Income / Revenue.
- **NI (Net Income)**: Accounting profit after all expenses, interest, and taxes.
- **NOPAT (Net Operating Profit After Tax)**: EBIT x (1 - effective tax rate) — the numerator of ROIC here.
- **PEG ratio**: PE / earnings growth rate.
- **pp (percentage points)**: A direct difference between two percentages — distinct from a "%" change.
- **PT (Price Target)**: An analyst's price forecast.
- **PW (Probability-Weighted) Fair Value**: This framework's blended fair value — 25% bull + 50% base + 25% bear.
- **Quality Score**: This framework's 0.0-100.0 score (higher = better) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score.
- **Rate Environment Gate**: The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier.
- **Rate Regime Modifier**: An additive adjustment (-10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in.
- **Rule 0**: This framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 1-8, Rule 10 (10-Rule Fair Value Framework)**: The numbered rules governing sector-appropriate valuation method choice (Rule 1), the 3-stage DCF standard (Rule 2), the weighted "football field" blend of valuation methods (Rule 3), sanity-check protocols including the 75% terminal-value cap (Rule 4), comparable-company standards (Rule 5), normalizing one-off items before valuing (Rule 6), mandatory bull/base/bear scenario weighting (Rule 7), margin-of-safety discipline by confidence level (Rule 8), and separating intrinsic value from market price with a documented catalyst (Rule 10).
- **Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **R/R (Risk/Reward ratio)**: Expected gain / expected loss on a trade; this framework requires >=2:1 to enter.
- **ROIC**: Return on Invested Capital.
- **TAM**: Total Addressable Market.
- **Terminal Value**: The lump-sum value assigned to all DCF cash flows beyond the explicit forecast period.
- **TTM (Trailing Twelve Months)**: The most recent 12 months of reported financial results.
- **Upside/Downside Modifier (Expected-Return Modifier)**: The additive +/-15 adjustment based on expected annual return vs. the 10% hurdle.
- **Valuation Score**: This framework's 0.0-100.0 score (lower = cheaper) combining the Phase 02 sub-scores, Rate Gate, and Upside/Downside Modifier.
- **WACC**: Weighted Average Cost of Capital — the DCF discount rate.
