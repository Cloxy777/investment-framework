# NEW POSITION (Re-evaluation) — ASML (ASML Holding N.V.) — 2026-09-11

**Task type:** NEW POSITION (routine full fresh re-run, requested directly — not itself a Rule 9 trigger)
**Date:** 11 Sep 2026
**10Y US Treasury Yield:** 4.94% (TradingEconomics intraday reading, 2026-09-11 — "eased to 4.94% on September 11, 2026" amid a global bond selloff pushing yields toward the 2026 highs; FRED's official `DGS10` series still shows a lagged 4.83% for 2026-09-09, the most recent officially posted value as of this session. Given the unusually fast multi-day move this week [Bloomberg: "Global Bond Selloff Sends 10-Year Treasury Yields to Cusp of 5%," 2026-09-11], the fresher intraday reading is used here rather than the ~2-day-lagged FRED post — a reversal of the usual sourcing preference, disclosed because it matters for a same-day live-price session. Note: this choice is immaterial to every downstream conclusion in this session — both readings fall in the same 3.5–5% Rate Regime bracket, and the Earnings Yield Spread Test fails by a wide margin either way.)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket, under either reading)
**Current ASML portfolio weight:** 0% — not held (confirmed against `portfolio/holdings.md` and `portfolio/override-log.md` before this session began; unchanged, not touching `holdings.md`)
**Prior coverage:** [watchlist/not-in-portfolio/ASML/ASML-2026-07-15.md](../watchlist/not-in-portfolio/ASML/ASML-2026-07-15.md) — Quality Score 82.4, Valuation Score 100.0, Composite Score 58.8, WATCHLIST ONLY, live price then $1,869.22. This session is a full fresh re-run per explicit task instruction — every input refetched live, nothing carried over from that session's conclusions.
**Sector:** Technology / Semiconductor capital equipment — sole global manufacturer of EUV lithography systems (unchanged; see the 2026-07-12 and 2026-07-15 sessions and glossary for background).

---

## 0. Why this session exists

A direct task request for a full fresh NEW POSITION re-run on ASML, not a Telegram or Rule 9 trigger. Confirmed before proceeding: ASML is not a current holding (`portfolio/holdings.md`, `portfolio/override-log.md` — no mention), and no ASML session more recent than 2026-07-15 exists in `sessions/`. ASML's own Q3 2026 results are not yet out (confirmed below, §1.1) — the last reported quarter remains Q2 2026 (reported 2026-07-15), so this session's TTM financial window is unchanged from 2026-07-15, but live price, live FX, the Rate Environment Gate, forward consensus estimates, and everything price-dependent are refetched fresh, as required.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$1,717.30** | IBKR `get_price_snapshot`, contract_id 117902840 (NASDAQ NY Registry Share), fetched 2026-09-11 (epoch ts 1789118206) |
| Change on day | +$29.87 (+1.77%) | Same snapshot |
| Bid / Ask | $1,717.24 / $1,718.27 | Same snapshot |
| 52-week range | $802.01 – $1,999.96 | Same snapshot (`misc_statistics`) — price sits well off the 52wk high, ~46% above the 52wk low |
| Live EUR/USD FX rate | **1.159775** (1 EUR = $1.159775, mid of bid 1.15975 / ask 1.15980) | IBKR `get_price_snapshot`, EUR/USD contract_id 12087792, fetched this session — used throughout for EUR→USD conversions below |

Price is down **8.13%** from the 2026-07-15 session's $1,869.22 reference (a decline, not a >15% move — doesn't independently trip Rule 9's ">15% unexplained move" trigger). No specific negative catalyst identified for the decline in this session's research (§1.1); it reads as part of the broader 2026-09-11 bond-market selloff (10Y approaching 5%, §above) compressing richly-valued growth/AI-capex-adjacent multiples generally, consistent with Rule 9's "not valid: price dropped on... macro fear" carve-out — i.e. this alone would not be a valid sell/entry trigger on its own, but it is exactly the kind of price movement this framework's routine re-scoring exists to capture objectively.

### 1.1 Confirmed: no new quarterly report since 2026-07-15

Checked directly via `yfinance` quarterly financials — the most recent reported quarter remains **2026-06-30 (Q2 2026)**, matching the 2026-07-15 session exactly (no newer column present). ASML's next earnings release is confirmed for **14 Oct 2026** (Q3 2026), guided at €11.0–12.0B net sales / 55–57% gross margin (unchanged guidance from the 07-15 press release). **This session's TTM financial window is therefore identical to the 2026-07-15 session's (Q3 2025 – Q2 2026)** — no new fiscal data exists to refresh it, so the Phase 01 Quality Score inputs below are carried forward from that session's primary-source figures rather than re-derived, while every price-dependent Phase 02 input (market cap, EV, multiples, forward PE, fair value, Upside/Downside Modifier) is fully recomputed against today's live price/FX/10Y.

Checked for other Rule 9 triggers since 07-15: no guidance revision, no management change, no M&A. Two September 2026 announcements found — Samsung Electronics/ASML extending their High-NA EUV collaboration (2026-09-08) and a TSMC/ASML industry initiative on 12-inch photomasks for High-NA EUV (2026-09-07) — both reinforce already-credited Moat signals (brand premium, switching costs) rather than introducing new ones or new financial data; noted qualitatively, not separately scored.

---

## 2. Data Gathered

### 2.1 TTM financials (unchanged from 2026-07-15 session — Q3 2025–Q2 2026, EUR millions)

Source: ASML's own Q2 2026 Excel workbook (`ourbrand.asml.com`), as verified in the 2026-07-15 session; re-verified this session against `yfinance` quarterly financials/cashflow (exact match on Total Revenue and Net Income for all four quarters).

```
                          Q3 2025    Q4 2025    Q1 2026    Q2 2026    TTM (Q3'25–Q2'26)
Total net sales            7,516.0    9,718.1    8,766.9    9,326.5     35,327.5
Gross profit                3,880.3    5,068.6    4,645.0    5,035.4     18,629.3
Income from operations      2,468.4    3,431.1    3,157.8    3,456.1     12,513.4
Net income                  2,124.5    2,839.6    2,756.7    2,917.6     10,638.4
D&A                           274.6      255.2      259.4      246.9      1,036.1
Operating cash flow           559.1   11,410.3   (2,185.6)    1,703.0     11,486.8
CapEx (PP&E purchases)         295.9      447.9      402.4      299.4      1,445.6
```

```
Gross Margin TTM  = 18,629.3 / 35,327.5 = 52.73%
Net Margin TTM    = 10,638.4 / 35,327.5 = 30.11%
EBITDA TTM        = 12,513.4 + 1,036.1  = 13,549.5
FCF TTM           = 11,486.8 − 1,445.6  = 10,041.2
FCF/NI TTM        = 10,041.2 / 10,638.4 = 94.39%
Effective tax rate TTM = 2,217.1 / (10,638.4 + 2,217.1) = 17.25%
```

### 2.2 Balance sheet (as of 28 Jun 2026, still the freshest — unchanged)

```
Cash + ST investments         7,581.5
Long-term debt                1,984.4
Total shareholders' equity   21,825.4

Net Debt = 1,984.4 − 7,581.5 = −5,597.1 (net cash)
Net Debt/EBITDA = −5,597.1 / 13,549.5 = −0.413×
```

Weighted-average basic shares outstanding, Q2 2026: **384.5 million** — same flagged approximation as 07-15 (no exact period-end count disclosed in ASML's abbreviated release); `yfinance`'s `sharesOutstanding` (384.1M) is consistent within 0.1%.

### 2.3 Invested Capital / ROIC / NOPAT (unchanged)

```
NOPAT = EBIT_TTM × (1 − 17.25%) = 12,513.4 × 0.8275 = 10,355.3M EUR
Invested Capital = Total Debt + Equity − Cash = 1,984.4 + 21,825.4 − 7,581.5 = 16,228.3M EUR
ROIC = 10,355.3 / 16,228.3 = 63.81%
```

### 2.4 Market Cap / EV / multiples — refreshed with today's live price and FX

```
Market Cap (USD) = $1,717.30 × 384.5M shares = $660,301.9M

Total Debt (USD)  = €1,984.4M × 1.159775 = $2,301.5M
Cash (USD)        = €7,581.5M × 1.159775 = $8,792.8M
EV = 660,301.9 + 2,301.5 − 8,792.8 = $653,810.6M

EBIT_TTM (USD)  = €12,513.4M × 1.159775 = $14,512.7M
FCF_TTM (USD)   = €10,041.2M × 1.159775 = $11,645.5M

EV/EBIT (TTM)   = 653,810.6 / 14,512.7 = 45.05×
FCF Yield (TTM) = 11,645.5 / 660,301.9 = 1.764%
```

Both multiples read slightly **cheaper** than 2026-07-15's EV/EBIT 49.84× / FCF yield 1.596% — the ~8% price decline outweighs the (unchanged) TTM EBIT/FCF base.

### 2.5 Forward consensus — no longer stale, used per the framework's normal "0y row" convention

The 2026-07-15 session had to build a bottom-up FY2026E EPS estimate because Yahoo's annual consensus row was stale (1 analyst) hours after the earnings release. Two months on, this data-quality problem has resolved — pulled fresh this session via `yfinance`'s `earnings_estimate`:

```
FY2026E EPS consensus (0y row, n=32 analysts) = €38.19  (growth +54.55% YoY — consistent with the confirmed guidance raise)
FY2027E EPS consensus (+1y row, n=33 analysts) = €51.72
Q3 2026E EPS consensus (0q row, n=14 analysts) = €10.58  (for context — up sharply from the €8.52 estimate the 07-15 session cited, consensus has caught up to the raised guidance)

FY2026E EPS (USD) = 38.19 × 1.159775 = $44.29
Forward PE = $1,717.30 / $44.29 = 38.77×
```

This is the standard "0y row" convention resuming after a temporary data-quality gap — not a new methodology deviation.

Sell-side context (`yfinance` `analyst_price_targets`, qualitative only, never scored): mean target $2,158.12, median $2,216.30, "strong_buy" (16 analysts) — both targets rose materially from 07-15's ($1,902.31 mean) despite the lower live price, i.e. the gap between sell-side targets and this framework's bottom-up fair value work (§4) has widened, not narrowed.

### 2.6 5-year historical PE range — unchanged

Same as the two prior ASML sessions (FY2026 not yet complete, so no new annual data point exists): **5yr Low 34.25× (FY2023), High 49.28× (FY2021), Avg 38.33×.**

### 2.7 TTM basic EPS — unchanged

```
TTM basic EPS = Q3'25 €5.49 + Q4'25 €7.35 + Q1'26 €7.15 + Q2'26 €7.59 = €27.58
```

### 2.8 Growth / TAM evidence — reinforced with fresh September 2026 evidence, magnitude unchanged

No new financial guidance since 07-15 (next update due with Q3 2026 earnings, 14 Oct 2026). Two September 2026 announcements, from ASML's own press releases, reinforce (don't newly establish) already-credited Moat/Growth qualitative evidence:
- **2026-09-08:** Samsung Electronics and ASML announced an expanded strategic collaboration on High-NA EUV and next-generation semiconductor manufacturing.
- **2026-09-07:** ASML and TSMC announced an industry initiative to transition to 12-inch photomasks for High-NA EUV, targeting a pilot line by 2031 and High-NA production readiness by 2033.
- **2026-09-08 (SPIE conference):** Intel Foundry and ASML jointly presented on High-NA EUV reticle-stitching techniques.

These reinforce the already-credited Brand premium/pricing-power and Switching-costs Moat signals (multi-year strategic co-development lock-in with the industry's three leading-edge foundries) but don't newly qualify a signal that wasn't already TRUE, and carry no new quantitative data — the Growth sub-score's +10 TAM modifier (already at its cap) is unchanged in magnitude, re-substantiated with this fresher evidence.

### 2.9 Data gaps flagged this session

1. No new quarterly filing since 2026-07-15 — TTM financial window and every Phase 01 input carried forward unchanged from that session (§1.1). This is a data-availability fact (Q3 2026 not yet reported), not an invented substitute.
2. Exact period-end share count still not disclosed; Q2 2026 weighted-average basic shares (384.5M) used as proxy, same as 07-15 (§2.2).
3. Owner Earnings maintenance-vs-growth CapEx split still unavailable — ASML is not one of the four Hybrid Upgrade 1 mandated names (MSFT/GOOGL/META/AMZN); standard FCF used throughout.
4. 5yr historical PE range still built from 5 annual snapshots (unchanged limitation).
5. 10Y Treasury sourcing note (see header) — intraday TradingEconomics reading (4.94%) used in place of FRED's ~2-day-lagged official post (4.83%) given this week's unusually fast rate move; immaterial to every downstream conclusion (§ above).

None of these blocked scoring.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, unchanged version; TTM inputs unchanged from 2026-07-15)

### 3.1 Legacy 8-criterion table (context only, unchanged from 07-15)

| Check | TTM Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 52.73% | >40% | PASS |
| Net margin | 30.11% | >12% | PASS |
| ROIC | 63.81% | >15% | PASS |
| Revenue growth (3yr CAGR, FY-anchored) | 15.55% | >8% | PASS |
| FCF positive 3 consecutive years | FY2023–2025 all positive | required | PASS |
| Net debt/EBITDA | −0.413× (net cash) | <2.5× | PASS |
| FCF yield | 1.764% | >4% | **FAIL** |
| EV/EBIT | 45.05× | <20× | **FAIL** |

Same 6-of-8 pattern as both prior sessions — the two failures remain purely valuation metrics (both improved slightly this session on the lower price, same as the 07-15→07-12 trend).

### 3.2 Hard disqualifier check (unchanged reasoning, unchanged data)

- **FCF/NI conversion <70% for 2+ consecutive years:** only FY2023 (41.9%) falls below 70%, a single isolated year; TTM FCF/NI is 94.39%. **Does not fire.**
- **Net Debt/EBITDA over threshold:** −0.413× (net cash), far under 2.5×. **Does not fire.**
- **Not FCF-positive 3+ consecutive years:** FY2021–FY2025 and TTM all positive. **Does not fire.**

**No hard disqualifier fires.**

### 3.3 Quality Score — full computation (identical inputs and result to 2026-07-15, since no new fiscal year/quarter has reported)

```
Profitability (25%):
  NetMargin_Component = clamp(30.11/30 × 100) = 100.00 (capped)
  ROIC_Component       = clamp(63.81/30 × 100) = 100.00 (capped)
  Profitability_Score  = (100.00 + 100.00) / 2 = 100.00

Margins (15%):
  GrossMargin_Score = clamp(52.73/80 × 100) = 65.92  (no trend bonus, already far above the 40% eligibility ceiling)

Growth (20%):
  Growth_Score raw = clamp(15.55/25 × 100) = 62.20
  TAM/pricing-power modifier: +10 RE-SUBSTANTIATED (fresh September 2026 evidence, §2.8: expanded Samsung
    High-NA collaboration, TSMC 12-inch-photomask industry initiative, Intel Foundry High-NA reticle-
    stitching work — all reinforcing, not newly establishing, already-credited evidence)
  Growth_Score = 62.20 + 10 = 72.20

Balance Sheet (15%):
  BalanceSheet_Score = clamp(100 × (1 − (−0.413)/4)) = clamp(110.33) = 100.00 (capped, net cash)

Moat Signal (15%) — unchanged 3-of-5 checklist:
  Market share stable/growing: TRUE (unchanged — ~100% EUV share, sole manufacturer)
  Brand premium / pricing power: TRUE (unchanged; further reinforced by the September 2026 Samsung/TSMC/
    Intel High-NA collaboration announcements)
  Network effect: NOT marked true (unchanged — not applicable to this business model)
  Switching costs: TRUE (unchanged — no alternative EUV supplier, multi-year qualification lock-in;
    reinforced by the same September 2026 announcements)
  Scale cost advantage: NOT marked true (unchanged — no citable cost-per-unit comp exists)
  Moat_Score = (3/5) × 100 = 60.00

FCF Quality (10%):
  FCFQuality_Score = clamp(((0.9439 − 0.40)/0.60) × 100) = 90.64

Quality Score = 100.00×0.25 + 65.92×0.15 + 72.20×0.20 + 100.00×0.15 + 60.00×0.15 + 90.64×0.10
              = 25.000 + 9.888 + 14.440 + 15.000 + 9.000 + 9.064
              = 82.392  →  rounds to 82.4
```

**Quality Score = 82.4 / 100.0 — clears the 80.0 gate, unchanged from 2026-07-15** (no new fiscal data exists to move it; the September 2026 qualitative evidence reinforces an already-capped Growth modifier without changing its magnitude).

⚠️ Same open flag as prior sessions: Hybrid Upgrade 1 (Owner Earnings) not applied — ASML doesn't disclose a maintenance-vs-growth CapEx split and isn't one of the four mandated names. Standard FCF used throughout.

---

## 4. Rate Environment Gate

```
Step 1 — Earnings Yield Spread Test:
  Forward PE (§2.5) = $1,717.30 / $44.29 = 38.77×
  EY = 1 / 38.77 = 2.579%
  Spread = EY − 10Y (4.94%) = 2.579% − 4.94% = −2.361pp
  Spread < +1.5% → Step 1 FAILS → additive +5

Step 2 — Rate Regime Modifier:
  10Y = 4.94% → within the 3.5–5% bracket → +5

Combined Rate Environment Gate contribution = +5 + 5 = +10   (unchanged in magnitude from both prior sessions,
  even though 10Y itself rose materially — 4.62% → 4.83–4.94% — the 3.5–5% bracket is wide enough that the
  regime step doesn't move; Step 1 still fails by a wide margin regardless of the exact reading used)
```

---

## 5. Phase 02 — Valuation Score

### 5.1 PEG applicability — unchanged

Same lumpy/cyclical diluted-EPS history as both prior sessions (two of the last four fiscal years were EPS *declines*) — ASML still does not qualify as a Fast Grower. **PEG not applicable; its 15% weight stays redistributed to EV/EBIT (40%).**

### 5.2 Sub-scores

```
FCF Yield (40%):
  FCF_Score = clamp(100 × (1 − 1.764/10)) = 82.36

EV/EBIT (40%, redistributed):
  EV/EBIT_Score = clamp((45.05 − 12)/23 × 100) = clamp(143.7) = 100.00 (capped)

Forward PE (20%):
  Primary formula (5yr range available — 34.25× low, 49.28× high):
  FwdPE_Score = clamp((38.77 − 34.25)/(49.28 − 34.25) × 100) = clamp(30.09) = 30.09
  Historical PE Modifier vs. 5yr avg 38.33×: Forward PE 38.77× is +1.15% above avg → within ±10% → 0
    (no modifier — this is a materially different outcome from both prior sessions, where Forward PE was
    pinned above the 5yr high and the FwdPE sub-score capped at 100.0)

Raw weighted score = 82.36×0.40 + 100.00×0.40 + 30.09×0.20
                   = 32.944 + 40.00 + 6.018
                   = 78.96
```

**This is the key structural change this session.** In both prior sessions, Forward PE sat above the entire trailing 5-year PE range (pinning FwdPE_Score at its 100.0 ceiling). This session, the combination of (a) the ~8% price decline and (b) forward consensus EPS finally catching up to the confirmed guidance raise (FY2026E EPS consensus rising from the 07-15 session's bottom-up €33.00 to a now-current €38.19, §2.5) pulled Forward PE from 49.59× down to 38.77× — now sitting almost exactly at the 5-year average (38.33×) rather than above the 5-year high. FCF Yield and EV/EBIT (still capped) both remain expensive-side, but the raw weighted score (78.96) is meaningfully below both prior sessions' (93.62 on 07-15, 94.08 on 07-12).

### 5.3 Fair Value work (feeds the Upside/Downside Modifier)

**Method A — 3-scenario DCF.** Same structure as the two prior sessions (CAPM-derived WACC, base-year FCF = FY2025 actual €11,084.9M — still the latest full clean fiscal year, Stage 1 = 2026–2030, Gordon-growth terminal). **Growth assumptions unchanged from 2026-07-15** (22%/12%/4% bull/base/bear Stage-1 FCF growth) since no new fundamental data has emerged to justify revising them (no Q3 2026 report yet) — only the discount rate is refreshed for today's higher 10Y:

```
Cost of equity (CAPM) = 4.94% + 1.394 × 5.5% = 12.607% (base WACC; negligible net debt)
```

| Scenario | WACC | Terminal g | Stage-1 FCF growth/yr | DCF EV (EUR) | + Net cash | Equity value/share (EUR) | (USD @1.159775) |
|---|---|---|---|---|---|---|---|
| Bull | 11.607% | 3.0% | 22% (unchanged — no new data to revise) | €280.0B | +€5.60B | €742.81 | **$861.49** |
| Base | 12.607% | 2.5% | 12% (unchanged) | €164.0B | +€5.60B | €440.97 | **$511.42** |
| Bear | 13.607% | 2.0% | 4% (unchanged) | €105.5B | +€5.60B | €288.88 | **$335.04** |

Every scenario's per-share value falls modestly vs. 2026-07-15 (Bull $881.97→$861.49, Base $519.81→$511.42, Bear $338.61→$335.04) — purely a discount-rate effect (higher 10Y → higher WACC across all three scenarios), since the underlying cash-flow growth assumptions are unchanged.

**Method B — Comparable multiples** (TTM basic EPS €27.58 unchanged; FY2026E EPS now the current consensus €38.19 rather than 07-15's bottom-up €33.00 estimate; updated EV/EBIT USD base from §2.4):

```
Historical PE (trailing) = 38.33 × €27.58 → USD                         = $1,226.05
Historical PE (forward)  = 38.33 × €38.19 (current consensus) → USD    = $1,697.70
EV/EBIT @ 25× = (EBIT_USD×25 + net cash_USD)/shares                    = $960.49
EV/EBIT @ 30× = (EBIT_USD×30 + net cash_USD)/shares                    = $1,149.22
Base multiples value (avg of above 4)                                  = $1,258.36

Bull multiples: EV/EBIT @ 35× ($1,337.94) + Historical-PE-at-5yr-high 49.28×TTM-EPS ($1,576.53), avg = $1,457.12
Bear multiples: EV/EBIT @ 17.75× ($686.85) + Historical-PE-at-5yr-low 34.25×TTM-EPS ($1,095.60), avg = $891.19
```

The Historical-PE-forward leg rose materially ($1,444.90 → $1,697.70) purely because the FY2026E consensus EPS input is no longer stale — a data-quality improvement, not a change in the underlying business.

**Triangulation (40% DCF / 60% Multiples):**

```
Bull blended FV = 0.40×861.49 + 0.60×1,457.12 = $1,218.87
Base blended FV = 0.40×511.42 + 0.60×1,258.36 = $959.59
Bear blended FV = 0.40×335.04 + 0.60×891.19   = $668.73

PW Fair Value = 0.25×1,218.87 + 0.50×959.59 + 0.25×668.73 = $951.70
```

**PW Fair Value rose modestly to $951.70** (from $927.71 on 07-15) — the fresher, higher consensus EPS in the multiples leg outweighs the higher-WACC drag on the DCF leg. Still well below both the live price ($1,717.30) and the sell-side mean target ($2,158.12, §2.5) — the gap to sell-side consensus has widened even as the gap to the live price narrowed, since sell-side targets rose while the live price fell.

### 5.4 Upside/Downside Modifier

```
Gap Upside% = (951.70 / 1,717.30) − 1 = −44.58%
Catalyst window: no specific 18–24mo re-rating catalyst identified (unchanged) — downside gap, so the
  upside-side guardrail cap doesn't apply here.
Annualized gap = −44.58% / 2 = −22.29%/yr

Intrinsic growth rate = diluted EPS 3yr CAGR (FY2022→FY2025, unchanged — FY2026 not yet complete) = +20.48%/yr

Shareholder yield (recomputed against this session's new market cap denominator; TTM cash-flow numerators
  unchanged since the TTM window itself is unchanged, §1.1):
  TTM dividends paid    = €2,894.3M (unchanged)
  TTM net buyback       = €3,810.0M (unchanged: €3,949.7M buybacks − €139.7M issuance proceeds)
  Dividend yield  = (€2,894.3M × 1.159775) / $660,301.9M = 0.508%
  Net buyback yield = (€3,810.0M × 1.159775) / $660,301.9M = 0.669%
  Shareholder yield = 0.508% + 0.669% = 1.178%/yr  (up slightly from 1.065% on 07-15 — same cash-return
    numerators against a smaller market-cap denominator)

E = −22.29% + 20.48% + 1.178% = −0.63%/yr

E < 0 → M = 5 + 10 × clamp((−E)/10pp, 0, 1) = 5 + 10 × clamp(0.63/10, 0, 1) = 5 + 0.63 = +5.63
```

### 5.5 Final Valuation Score

```
Final Score = Raw weighted (78.96) + Rate Environment Gate (+10) + Upside/Downside Modifier (+5.63)
            = 94.59  →  rounds to 94.6
```

**Valuation Score = 94.6 / 100.0 — down materially from 100.0 (the ceiling) on both prior sessions.** This is the first ASML session where the Valuation Score isn't pinned at its maximum, driven almost entirely by Forward PE finally sitting inside (rather than above) its own trailing 5-year range, itself the product of the ~8% price pullback plus consensus EPS estimates catching up to the confirmed guidance raise. Still deep in expensive territory (94.6 is within the top decile of the 0–100 scale), just no longer literally maxed out.

---

## 6. Composite Score (Quality + Valuation)

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 82.4) + 0.50 × 94.6
                = 0.50 × 17.6 + 47.3
                = 8.8 + 47.3
                = 56.1
```

**Composite Score = 56.1 — falls in the 50.0–69.9 band: HOLD — watch only, no new entry, no trim.** More attractive than both prior sessions (58.8 on 07-15, 59.3 on 07-12), driven entirely by the Valuation Score's move off its 100.0 ceiling (Quality Score is unchanged at 82.4, no new fiscal data). Still comfortably inside the same Hold band, not close to either the 70.0 Trim boundary or the 49.9 Buy-eligible boundary.

---

## 7. Order Setup

**Not applicable.** Composite Score 56.1 sits in the 50.0–69.9 "Watchlist only — no new entry, no trim" band, unchanged in category from both prior sessions. No buy price, sell target, stop loss, or position size is computed this session. The PW Fair Value ($951.70) and its scenario range ($668.73 bear – $1,218.87 bull, §5.3) are recorded for reference and for the Upside/Downside Modifier, not as an actionable entry price. Per `fair-value-methodology.md`'s Score-band integration table, a Composite Score of 50.0–69.9 ("No MoS") maps directly to Watchlist only.

---

## 8. Qualitative Notes

1. **The score moved for a genuinely new reason this session — not fundamentals, but a valuation-mechanics unlock.** Quality Score is byte-for-byte unchanged (82.4) because no new fiscal data exists (Q3 2026 not yet reported). The entire Composite Score improvement (58.8 → 56.1) traces to the Forward PE sub-score dropping out of its 100.0 ceiling as the price fell ~8% and consensus EPS caught up to July's guidance raise — exactly the kind of the-market-does-the-work-for-you movement this framework is built to capture without needing a new earnings print.
2. **No adverse fundamental news identified for the price decline.** Two September 2026 announcements found (Samsung High-NA collaboration expansion, TSMC/ASML 12-inch photomask initiative) are both positive/reinforcing, not negative catalysts. The decline reads as part of a broader bond-market-driven multiple compression (10Y approaching 5%) rather than an ASML-specific event — consistent with, not a violation of, Rule 9's "price dropped on... macro fear" non-trigger carve-out.
3. **Sell-side consensus and this framework's bottom-up fair value continue to diverge in opposite directions.** Sell-side mean target rose to $2,158 (from $1,902) even as the live price fell — sell-side is pricing in the guidance raise more aggressively than this framework's scenario-weighted DCF+multiples build ($951.70 PW FV), a divergence reported, not reconciled, per standing practice.
4. **Data-quality note resolved:** the "0y" consensus row that read as stale immediately after the 07-15 earnings release (1 analyst) has normalized to a full 32-analyst count two months later — the bottom-up substitute methodology used in July is no longer needed this session, and the framework's normal "read the 0y row" convention resumes.
5. **10Y sourcing judgment call, disclosed:** used a same-day intraday reading (4.94%, TradingEconomics) over FRED's officially posted but ~2-day-lagged value (4.83%) given this week's unusually fast bond selloff — flagged as a deliberate, immaterial-to-outcome deviation from the framework's usual FRED-primary convention (§ header).

---

## 9. Recommendation

# **WATCHLIST ONLY — Composite Score 56.1 (Hold / no new entry, no trim band). Do not enter now.**

ASML's Quality Score remains unchanged and comfortably above the 80.0 gate (82.4 — no new fiscal data since the 2026-07-15 session's Q2 2026 report; Q3 2026 reports 14 Oct 2026). Its Valuation Score, however, moved materially — from a pinned 100.0 ceiling down to **94.6** — because Forward PE finally fell inside its own trailing 5-year range (rather than above it) as the price declined ~8% since 07-15 and forward consensus EPS caught up to the confirmed guidance raise. The 50/50 Composite Score blend improves from 58.8 to **56.1**, but remains squarely inside the **50.0–69.9 "Hold — watch only, no new entry, no trim"** band — meaningfully cheaper than before, but still not close to the 49.9 Buy-eligible boundary. **This is a WATCHLIST/PASS outcome, not a BUY/TRIM/EXIT action** — no order setup, no entry, no position opened, `holdings.md` untouched.

---

## 10. Next Review Trigger

- **Q3 2026 earnings, confirmed for 14 Oct 2026** (Rule 9 mandatory trigger) — will refresh the TTM window for the first time since Q2 2026 and re-test every Quality Score input, not just the price-dependent Valuation Score inputs refreshed this session.
- **Any further pullback toward this session's PW Fair Value (~$952) or bull-case DCF+multiples blend (~$1,219)** — the Valuation Score still has real headroom to fall further even with an unchanged Quality Score; it is no longer pinned at its ceiling, so further price moves will now show up directly in the score rather than being absorbed by the cap.
- Any guidance revision, management change, or M&A (Rule 9 standard triggers).
- Any >15% unexplained move from today's $1,717.30 reference.

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

| Term | Meaning |
|---|---|
| **CAPM (Capital Asset Pricing Model)** | A formula estimating a stock's required return (cost of equity) as the risk-free rate plus Beta times the Equity Risk Premium; used here to set the DCF discount rate. *(New term, added to glossary.md this session.)* |
| **Composite Score** | This framework's blended Quality + Valuation ranking number (0.50 × (100 − Quality Score) + 0.50 × Valuation Score); ASML's is 56.1 this session, down from 58.8 on 2026-07-15. |
| **DCF (Discounted Cash Flow)** | A valuation method estimating a company's worth today by projecting future cash flow and discounting it back to present value. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization; ASML's TTM EBITDA is €13,549.5M (unchanged). |
| **EPS (Earnings Per Share)** | Net income divided by shares outstanding. |
| **EUV (Extreme Ultraviolet Lithography)** | The most advanced chip-manufacturing lithography technology; ASML is the sole global manufacturer of EUV systems. |
| **EV/EBIT** | Enterprise Value divided by EBIT; ASML's TTM figure is 45.05× this session (down from 49.84× on 07-15, on the lower price). |
| **FCF Yield** | Free Cash Flow ÷ Market Cap; higher means cheaper; ASML's TTM figure is 1.764% this session. |
| **Forward PE** | Price ÷ next-twelve-months expected earnings per share; ASML's is 38.77× this session — the key driver of this session's score change, now sitting near its own 5yr average rather than above its 5yr high. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score; none fired for ASML this session. |
| **Moat** | A durable competitive advantage protecting a business's profits from competitors; ASML's checklist reading is unchanged at 3-of-5 signals this session. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate); the numerator used to compute ROIC. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value estimate (25% bull + 50% base + 25% bear); ASML's is $951.70/share this session, up from $927.71 on 07-15. |
| **Quality Score** | This framework's 0.0–100.0 continuous quality grade; 80.0+ required to proceed to valuation scoring. ASML scores 82.4 this session, unchanged from 07-15 (no new fiscal data). |
| **Rate Environment Gate** | The mandatory pre-check before Phase 02 scoring, comparing Earnings Yield to the 10-Year Treasury yield; contributed +10 this session (unchanged in magnitude from prior sessions). |
| **ROIC** | Return on Invested Capital; ASML's TTM figure is 63.81% (unchanged). |
| **Rule 9** | Fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. This session was a direct request, not itself a Rule 9 trigger; no Rule 9 event was found to have occurred since 07-15. |
| **Shareholder yield** | Cash returned to shareholders as a % of share price (dividends + net buybacks); ASML's is 1.178% this session, up slightly from 1.065% on 07-15 (unchanged cash-return numerators against a smaller market cap denominator). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results; this session's window (Q3 2025–Q2 2026) is unchanged from 07-15, since no new quarter has reported. |
| **Upside/Downside Modifier** | An additive ±15 adjustment to the valuation score based on expected annual return; ASML's computed at +5.63 this session, down from +8.64 on 07-15 (expected loss narrowed as fair value rose modestly while the price fell). |
| **Valuation score** | This framework's 0.0–100.0 continuous score (0 = cheapest, 100.0 = most expensive); ASML scores 94.6 this session — the first ASML session where this score is not pinned at the 100.0 ceiling. |
| **WACC (Weighted Average Cost of Capital)** | The discount rate used in a DCF, blending the cost of equity and cost of debt weighted by their share of capital; ASML's base-case WACC is 12.607% this session (≈ cost of equity alone, given negligible net debt), up from 12.3% on 07-15 on the higher 10Y Treasury yield. |
