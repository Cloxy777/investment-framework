# RESCORE — BKNG (Booking Holdings Inc.)

**Task type:** RESCORE (single ticker, mode `--both` — full Quality + Valuation + Composite)
**Date:** 2026-10-11
**10Y US Treasury Yield:** 5.244% (same figure independently sourced and used in this repo's same-day [ZS rescore](2026-10-11-rescore-zs.md), `yfinance` `^TNX` 2026-10-09 close — WebSearch cross-check found secondary reporting of the 10Y spiking to ~5.2% in late September 2026, directionally consistent but not an exact-date confirmation; no contradicting figure was found)
**Rate Regime Modifier (active):** +10 (>5% bracket) — up from +5 (3.5–5% bracket) at the 2026-08-05 session
**Last review on record:** Quality 89.6 / Valuation 32.8 / Composite 21.6 — 2026-08-05, [sessions/2026-08-05-new-position-bkng.md](2026-08-05-new-position-bkng.md) ("WATCHLIST ONLY — do not enter")
**Held position:** ~10 shares, ~2.36% weight per the 2026-10-11 sync ([holdings.md](../portfolio/holdings.md))

> *Jargon decoded in the closing Glossary.*

---

## 0. Trigger and scope note

BKNG's only prior evaluation ([2026-08-05](2026-08-05-new-position-bkng.md)) concluded **"WATCHLIST ONLY — do not enter"** because Risk/Reward failed the 2:1 minimum at every authorized Margin-of-Safety/stop-loss combination (best case 1.25:1), despite a Composite Score (21.6) that nominally qualified for a Full Position.

Despite that conclusion, GTC order 483688084 (BUY 10 @ $159.00) filled around 2026-09-27 with no `sessions/`/`decisions/`/`override-log.md` entry documenting why — flagged as an undocumented/urgent trade in [holdings.md](../portfolio/holdings.md) and [override-log.md](../portfolio/override-log.md). **Resolving that documentation gap is out of scope for this session** (it belongs in `override-log.md`/`decisions/`, not a `/rescore` run). This session's only job is to run a fresh, current RESCORE now that BKNG is an actual holding, exactly as `/rescore` would for any other holding.

**One factual note on the undocumented position, per Rule 9/next-steps relevance:** as of this rescore, the position remains undocumented in `override-log.md`/`decisions/` — this is unresolved and not cleared by this session.

---

## 1. Live price (Rule 0)

**$160.73** — IBKR `get_price_snapshot`, contract_id 308728373 (NASDAQ, "BOOKING HOLDINGS INC"), intraday (`is_close: false`), prior close $159.97. 52-week range (IBKR `misc_statistics`): low $149.76 / high $219.77 (13-week high $217.32, 26-week high $217.32) — the stock has fallen sharply from the 2026-08-05 session's $204.35 (−21.3%) and now sits only modestly above the ~$159.00 undocumented fill price.

---

## 2. Data sourcing and a key finding: no new quarterly filing since 2026-08-05

**No new 10-Q or 10-K has been filed since the 2026-08-04 10-Q** (confirmed via SEC EDGAR `submissions/CIK0001075531.json` — the only filings since 2026-07-01 are the 2026-08-04 10-Q and its companion 8-K). BKNG's Q3 2026 earnings have **not yet been reported** (historically early-to-mid November). This means:

- **All TTM GAAP fundamentals (net margin, gross margin, revenue 3yr CAGR, net debt/EBITDA, FCF/NI ratios, balance sheet) are structurally unchanged from 2026-08-05** — same four trailing quarters (Q3'25–Q2'26), same 10-Q, same SEC XBRL `companyfacts` data (`https://data.sec.gov/api/xbrl/companyfacts/CIK0001075531.json`, re-pulled fresh this session and cross-checked against the figures published in the 2026-08-05 session — they reconcile exactly).
- **Only price-dependent inputs (market cap, EV, FCF yield, EV/EBIT, forward PE), the 10Y Treasury/Rate Environment Gate, the ROIC third-party cross-check, and qualitative moat/TAM evidence needed a fresh pull.**

Sources used this session:
1. **SEC EDGAR XBRL `companyfacts` API** — re-pulled fresh, used for annual FCF/NI series (FY2022–FY2025, oldest-first) feeding the hard-disqualifier check, and to confirm no new filing exists.
2. **stockanalysis.com** (WebFetch) — gross margin proxy (unchanged, BKNG still has no GAAP Gross Profit line), forward PE components (FY2026 consensus EPS $10.45, 35–37 analysts), peer forward PEs (EXPE, TCOM, ABNB), current price/market-cap/EV cross-checks.
3. **WebSearch** — 10Y Treasury cross-check, ROIC third-party cross-check (3 independent sources), peer multiples cross-check, fresh Q2 2026/Q3 2026-guidance Connected Trip and Genius evidence, Q3 2026 earnings-date status.
4. **IBKR `get_price_snapshot` / `search_contracts`** — live price (Rule 0).

No required metric was unavailable; every figure is cited.

---

## 3. Phase 01 — Quality Score (methodology version 2026-06-29)

Full inputs JSON and script output below, pasted verbatim.

### Key re-sourced inputs

- **Net Margin (TTM) = 25.53%** — unchanged (same TTM window: Q3'25 $9,008M+Q4'25 $6,349M… revenue $28,241M; NI $7,209M — no new quarter).
- **ROIC (TTM) — re-sourced, flagged judgment call, materially different from 2026-08-05.** Three independently-disclosed-methodology third-party sources this session: **GuruFocus 41.47%** (quarterly, as of Jun 2026 — up from the 24.49% quoted in the 2026-08-05 session's GuruFocus pull, itself "as of Mar 2026"), **FFF Institutional ~53.0%** (TTM), **StockAlarm 51.95%** (FY2025 annual). Sorted: 41.47 / 51.95 / 53.0 → **median = 51.95%**. A fourth source, stockanalysis.com, now shows "Current" ROIC of 92.45% — excluded from the median as a clear methodology outlier (consistent with the 2026-08-05 precedent of excluding a definitionally-divergent outlier), same as that session excluded stock-analysis-on.net's 42.20% figure.
  - **This is flagged, not treated as a genuine quality improvement.** BKNG's Invested Capital (Debt + Equity − Cash) is still negative (same unchanged balance sheet: $20,694M debt + (−$10,783M) equity − $17,214M cash = −$7,303M) — NOPAT ÷ a near-zero/negative denominator is structurally unstable, and a swing from 24.49% to 51.95% quarter-to-quarter (with no new filed quarter in between on BKNG's side — these are third-party vendors' own recomputations/revisions) illustrates exactly how unreliable this input is for BKNG, same structural issue as the FICO/MTCH precedents. Carried into the score as the best-available median per the "never invent, use disclosed third-party data" rule, but flagged for Phase 04 monitoring — this input should not be read as 2+x cleaner capital efficiency in two months.
- **Gross Margin (TTM) = 87.23%** — unchanged (stockanalysis.com; still a third-party proxy, BKNG's GAAP statements still carry no Gross Profit/Cost-of-Revenue line).
- **Revenue 3yr CAGR = 16.36%** — unchanged (FY2022→FY2025, no new FY).
- **Net Debt/EBITDA = 0.353×** — unchanged (same debt/cash/EBITDA, same 10-Q).
- **TAM-expansion evidence — re-verified with fresh Q2 2026 data, not just carried over.** Connected Trip transactions grew at a low-double-digit rate in Q2 2026, "more than twice the pace of Booking.com's total transaction growth" (Customer Experience Dive, reporting on the Q2 2026 earnings call); Genius Level 2/3 members (>30% of the active base) now generate a "high-50s%" share of room nights, **up YoY** from the "more than half" figure cited in the 2026-08-05 session — the TAM-expansion and switching-cost evidence is strengthening, not weakening.
- **Growth-deceleration evidence — still not applied (cyclical, not structural).** Q3 2026 guidance (room nights +3–5%, revenue +4–6%, both below analyst consensus) continues to attribute the slowdown explicitly to the Middle East conflict's effect on international travel demand/flight capacity/pricing — the same cyclical, named, non-structural cause as 2026-08-05, so the −10 structural-deceleration modifier still does not apply. Flagged for continued Phase 04 monitoring.
- **FCF Quality — TTM FCF/NI = 132.3%** unchanged. **Annual FCF/NI series (oldest-first, independently recomputed this session from fresh SEC XBRL annual `NetIncomeLossAvailableToCommonStockholdersBasic` / `NetCashProvidedByUsedInOperatingActivities` / `PaymentsToAcquirePropertyPlantAndEquipment` pulls):**
  - FY2022: FCF $6,186M ÷ NI $3,058M = **202.3%**
  - FY2023: FCF $6,999M ÷ NI $4,289M = **163.2%**
  - FY2024: FCF $7,894M ÷ NI $5,882M = **134.2%**
  - FY2025: FCF $9,087M ÷ NI $5,404M = **168.1%**
  - All far above the 70% hard-disqualifier threshold — no issue, consistent with 2026-08-05.
- **Moat Signal — all 5 signals re-verified true, with fresh evidence** (see inputs JSON below) — no erosion found; the switching-cost signal (Genius L2/L3 room-night share) has strengthened YoY.

### Quality Score — script output (verbatim)

Input JSON: `net_margin_pct=25.53, roic_pct=51.95, fcf_positive_3yr_or_more=true, gross_margin_pct=87.23, gross_margin_structural_trend=false, revenue_cagr_3yr_pct=16.36, tam_expansion_evidence=true, growth_decelerating_evidence=false, net_debt_to_ebitda=0.353, asset_light_override=false, moat_signals=[5/5 true], fcf_ni_ttm_pct=132.3, fcf_ni_annual_pct=[202.3, 163.2, 134.2, 168.1]`

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((25.53/30)x100) = 85.10
ROIC_Component = clamp((51.95/30)x100) = 100.00
Profitability_Score = (85.10 + 100.00) / 2 = 92.55

**Margins (15%)**
GrossMargin_Score = clamp((87.23/80)x100) = 100.00

**Growth (20%)**
Growth_Score = clamp((16.36/25)x100) = 65.44
+10 TAM/pricing-power evidence: Connected Trip cross-vertical strategy continues to outpace core growth: Q2 2026 earnings call (Customer Experience Dive, 2026-08) reported Connected Trip transactions growing at a low-double-digit rate, more than 2x total transaction growth, and Genius Level 2/3 members (>30% of active base) now generate a 'high-50s%' share of room nights, up YoY from the already-cited 50%+ level in the 2026-08-05 session -- continued penetration of the ~$1.5T total travel market beyond core accommodation booking, not yet fully monetized ('low double-digit percentage of transactions' per the prior session, still the frontier of the opportunity).
Growth_Score (final, clamped) = 75.44

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - 0.353/4)) = 91.18

**Moat Signal (15%)**
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Booking.com continues to hold the leading OTA-competitor-set share (69.3% vs Expedia 11.5%, globalgrowthinsights.com, re-verified 2026-10, no contrary evidence found of share loss within the OTA set since 2026-08-05). |
| brand_premium | True | Effective host commissions remain elevated (15-30%+ range, cloudbeds.com) with no reversal; Genius relevance-based visibility algorithm (replacing guaranteed-discount visibility) still in effect, unchanged since 2026-08-05. |
| network_effect | True | Genius two-sided marketplace (~2.5M total / ~850K actively participating properties) unchanged structurally; Q2 2026 earnings call confirms continued member growth (hospitality.today baseline, re-verified no contrary evidence). |
| switching_costs | True | Genius Level 2/3 tiered members now generate a 'high-50s%' share of room nights (up YoY), a strengthening, not weakening, lock-in signal vs the 2026-08-05 'more than half' baseline (Customer Experience Dive, Q2 2026 call commentary). |
| scale_cost_advantage | True | No evidence of smaller OTA competitors closing the paid-marketing-efficiency gap; BKNG's >50% direct/owned-channel room-night mix and $7B+ annual ad spend scale remain unchanged since 2026-08-05 (no new quarter reported). |
Moat_Score = (5/5) x 100 = 100.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((1.3230 - 0.40)/0.60)x100) = 100.00

**Quality Score — Final**
Quality Score = (92.55x0.25) + (100.00x0.15) + (75.44x0.20) + (91.18x0.15) + (100.00x0.15) + (100.00x0.10)
= 91.902 -> rounds to 91.9

# Quality Score = 91.9 — PASSES the 80.0+ gate
```

**Quality Score = 91.9 / 100.0 — up from 89.6 on 2026-08-05.** The improvement is driven almost entirely by the ROIC input (now capped at 100.0 vs 81.63 previously) — flagged above as a data-source/judgment-call swing, not a genuine two-month quality improvement. Excluding that single input, the underlying business (margins, growth, balance sheet, moat, FCF quality) is essentially unchanged, consistent with no new quarter having reported.

---

## 4. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ Forward PE = 1 ÷ 15.38 = **6.50%**. Spread = 6.50% − 5.244% (10Y) = **+1.26pp** — below the +1.5pp threshold → **+5 additive modifier**.
- **Step 2 — Rate Regime Modifier:** 10Y yield 5.244% sits in the **>5% bracket** → **+10** (up from +5 at 4.61% in the 2026-08-05 session).

**Total Rate Environment Gate modifier: +15** (up from +10 on 2026-08-05 — a materially less favorable rate backdrop than two months ago).

---

## 5. Phase 02 — Valuation Score

### PEG / Fast Grower eligibility — still not applicable

Unchanged from 2026-08-05: FY2025 diluted EPS fell −4.1% YoY (one-off non-cash FX remeasurement loss on Euro debt), breaking the "3+ consecutive years >15% EPS growth" test regardless of cause (no new FY reported since). PEG's 15% weight redistributes to EV/EBIT (→ 40%).

### Fresh price-dependent inputs

- **Shares outstanding = 751,380,500** (SEC 10-Q cover page, as of 2026-07-27 — still the most current count available; no newer SEC filing or third-party figure found, flagged as stale pending the Q3 2026 10-Q).
- **Market Cap** = 751,380,500 × $160.73 = **$120,769.4M**
- **Enterprise Value** = $120,769.4M + Debt $20,694M − Cash $17,214M = **$124,249.4M**
- **FCF Yield** = TTM FCF $9,539M ÷ Market Cap $120,769.4M = **7.8985%**
- **EV/EBIT** = $124,249.4M ÷ TTM EBIT $9,284M = **13.3832×**
- **Forward PE** = $160.73 ÷ FY2026 consensus EPS $10.45 (37 analysts polled, stockanalysis.com forecast page, range $10.15–$10.80) = **15.3809×**
- **5yr PE history — still a no-history fallback, re-checked.** No usable 5yr average/range was reconstructable this session either — the same COVID-earnings-trough-era distortion flagged in 2026-08-05 remains inside any 5-year lookback window as of October 2026 (the trough quarters run through 2020–2021). **FwdPE_Score = 50.0 (neutral, flagged)**, unchanged treatment.

### Fresh fair value — redone DCF + comparable multiples (not reused from 2026-08-05)

**WACC recomputed with the new 10Y (5.244% vs 4.61%) and current capital-structure weights:**
```
Cost of Equity = Rf (5.244%) + Beta (1.10, WebSearch cross-check: 1.05-1.2 range across sources, kept at 1.10
  for continuity with the 2026-08-05 session's cross-checked figure) x ERP (5.0% standard assumption) = 10.744%
Weights (market value): Equity 85.37% ($120,769.4M), Debt 14.63% ($20,694M)
After-tax cost of debt: 4.46% (unchanged assumption)
WACC (base) = 0.8537x10.744 + 0.1463x4.46 = 9.825% (bull -1pp = 8.825%, bear +1pp = 10.825%, per Rule 2)
```

**10-year, 3-stage DCF (Stage 1 yrs 1–5 explicit, Stage 2 yrs 6–10 fade, Stage 3 terminal — kept at 10 years, same as 2026-08-05, since a 5yr-only model again breaches Rule 4's 75% terminal-value cap). Growth/margin paths kept identical to 2026-08-05 (no new guidance/data to justify revising them — only WACC and starting TTM FCF, unchanged at $9,539M, feed into the model) — only WACC changed:**

| Scenario | WACC | Growth path (Y1→Y10) | FCF margin path | PV(explicit FCF) | PV(Terminal Value) | TV % of EV | DCF FV/share |
|---|---|---|---|---|---|---|---|
| Bull | 8.825% | 9.0% → 3.75% | 35.0% → 38.0% | $95,183M | $144,377M | 60.3% | **$318.83** |
| Base | 9.825% | 8.0% → 2.75% | 34.0% → 37.0% | $83,929M | $100,225M | 54.4% | **$245.09** |
| Bear | 10.825% | 7.0% → 2.75% | 34.0% flat | $74,536M | $70,307M | 48.5% | **$192.77** |

(Terminal growth capped at 2.75% in all scenarios, per Rule 2/GDP cap. All TV% comfortably under Rule 4's 75% sanity ceiling.)

**Comparable multiples — fresh peer forward PEs (stockanalysis.com, checked 2026-10-10/11):** Expedia (EXPE) **12.13×**, Trip.com (TCOM) **9.99×**, Airbnb (ABNB) **29.37×** — all materially compressed from the 2026-08-05 session's figures (EXPE 13.19×, TCOM 17.01×, ABNB 32.36×), consistent with a broader travel-tech sector de-rating alongside the higher-rate backdrop. Peer median = 12.13×, peer average = 17.163×.

| Scenario | Multiple basis | Applied to | Multiples FV/share |
|---|---|---|---|
| Bull | Peer average + quality premium (×1.075, same ratio as 2026-08-05's 25×/23.26× premium) = 18.45× | FY2026 consensus EPS $10.45 | **$192.80** |
| Base | Blend of peer median/average = 14.65× | FY2026 consensus EPS $10.45 | **$153.06** |
| Bear | Peer low end (TCOM 9.99×) | FY2026 consensus EPS $10.45 | **$104.40** |

**Triangulation (40% DCF + 60% Multiples, per fair-value-methodology.md Step 1):**
```
Bull FV = 0.40x318.83 + 0.60x192.80 = $243.21
Base FV = 0.40x245.09 + 0.60x153.06 = $189.87
Bear FV = 0.40x192.77 + 0.60x104.40 = $139.75

PW Fair Value = 0.25x243.21 + 0.50x189.87 + 0.25x139.75 = $190.68
```

**This fresh PW Fair Value ($190.68) is well below the 2026-08-05 session's $223.91** — driven almost entirely by the peer-multiples leg (sector-wide travel-tech de-rating), partially offset by the DCF leg landing in a similar range once the higher WACC is applied.

### Expected annual return E

```
Gap Upside % = (190.68 / 160.73) - 1 = +18.63%
Catalyst window = 2 years (Transformation Program ~$650M run-rate savings target by end-2027, ~14 months out --
  still within the 18-24mo guardrail window; no evidence the catalyst has lapsed or been pulled forward)
Annualized gap = 18.63% / 2 = 9.315%/yr
Intrinsic growth = ~7.80% (base-case FCF CAGR, Y0->Y5: ($13,885M/$9,539M)^(1/5)-1 = 7.797%)
Shareholder yield = dividend yield (1.045%: $1.68 annualized / $160.73) + net buyback yield (7.26%: carried
  over from 2026-08-05 -- flagged stale, no newer SEC share-count data point exists since the 2026-07-27
  cover-page count; no new 10-Q has filed to refresh it)
E = 9.315% + 7.797% + 7.26% + 1.045% = 25.42%/yr
```

**Step 2 — Map E to modifier (H = 10%):**
```
E (25.42%) >= H (10%) -> M = -15 x clamp((25.42-10)/15, 0, 1) = -15 x 1.0 (clamped) = -15.00
```

### Valuation Score — script output (verbatim)

```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 7.8985/10)) = 21.015

**EV/EBIT**
EV/EBIT_Score = clamp((13.3832 - 12)/23 x 100) = 6.014

**Forward PE**
No 5yr PE history available (no-history fallback) -> FwdPE_Score = 50.0 (neutral, flagged)

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/15.3809 x 100 = 6.5016%
Spread = EY - 10Y (5.244%) = 1.2576pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.244% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x243.21 + 0.50x189.87 + 0.25x139.75 = 190.6750
Gap Upside % = (190.6750/160.73) - 1 = 18.6306%
Annualized gap = 18.6306% / 2yr = 9.3153%/yr
E = 9.3153 (annualized gap) + 7.797 (intrinsic growth) + 8.3050 (shareholder yield: 1.045 div + 7.26 buyback) = 25.4173%/yr
E (25.4173%) >= H (10.0%) -> M = -15 x clamp((25.4173-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 20.812

**Final Valuation Score**
Final Score = Raw (20.812) + Rate Modifier (+15) + Upside/Downside Modifier (-15.000)
= 20.812 -> rounds to 20.8

# Valuation Score = 20.8
```

**Valuation Score = 20.8 / 100.0** — down from 32.8 on 2026-08-05 (cheaper on a raw basis — the raw score itself fell from 33.70 to 20.81 on a much lower EV/EBIT, partially offset by the higher +15 Rate Modifier vs +10, and the Upside/Downside modifier floored at -15.0 in both sessions).

---

## 6. Composite Score — script output (verbatim)

```
## Composite Score

Composite Score = 0.50x(100 - 91.9) + 0.50x20.8 = 14.450 -> rounds to 14.4

# Composite Score = 14.4
(Quality Score 91.9, Valuation Score 20.8)
```

**Composite Score = 14.4 / 100.0 — "Very Cheap" band (0.0–29.9), down from 21.6 on 2026-08-05.** Per the Action Table, this nominally maps to a **Full Position (6–8%)** — but see the Order Setup section below: the mandatory R/R gate still blocks any add, same structural conclusion as 2026-08-05.

---

## 7. Order setup

Per fair-value-methodology.md's 0.0–29.9-band tables: MoS range 15–20%, Max Acceptable Loss range 20–25%. Used **MoS = 20%, Max Loss = 20%** — the single most R/R-favorable combination this band authorizes (same logic as the 2026-08-05 "best case" test).

### Order setup — script output (verbatim)

```
## Order Setup

Band: 0.0-29.9 (Enter now)
Buy Price = Fair Value (190.675) x (1 - 20%) = 152.5400
Live price 160.73 vs buy price ceiling 152.5400 -> limit order at buy price (live price above ceiling); entry price used = 152.5400
Primary Sell Target = Fair Value = 190.6750
Bull-Case Trim Target = Bull FV (243.21) x 0.90 = 218.8890
Stop Loss = Entry Price (152.5400) x (1 - 20%) = 122.0320
R/R Ratio = (Sell Target 190.6750 - Entry 152.5400) / (Entry 152.5400 - Stop 122.0320) = 38.1350/30.5080 = 1.2500:1
*** FLAG: R/R 1.2500:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (68101.12) x 1.5% = 1021.5168
Risk Per Share = Entry (152.5400) - Stop (122.0320) = 30.5080
Shares by risk-based sizing = 1021.5168 / 30.5080 = 33.4836
Allocation cap = Portfolio Value (68101.12) x 8% = 5448.0896 -> 35.7158 shares
Position Size (shares) = min(risk-based, cap) = 33.4836  [binding: risk-based sizing]
Position Size ($) = 33.4836 x 152.5400 = 5107.5840
Current shares held = 10; gap vs. target = 23.4836
```

**R/R fails at 1.25:1 — the same best-case ceiling found in the 2026-08-05 session (the math is structurally determined by the band's MoS/stop ranges, not by the specific price/FV levels, so an unchanged band produces the same ceiling).** The limit-order buy-price ceiling this computes to ($152.54) sits **below both the live price ($160.73) and the ~$159.00 undocumented entry cost** — i.e. even the undocumented fill itself was executed above the price level this framework's R/R-gate math would authorize for a *new* buy.

### Context: live price / fair value vs. the $159.00 undocumented entry

- **Undocumented entry cost:** ~$159.00/share (GTC order 483688084, filled ~2026-09-27)
- **Live price today:** $160.73 (+1.1% vs. entry — essentially flat)
- **PW Fair Value:** $190.68 (+18.9% above the $159.00 entry cost, +18.6% above today's live price)
- **R/R-gate-clearing limit price:** $152.54 (i.e. ~4% *below* the undocumented entry — the entry was not even cheap enough by this framework's own gate math)

So the undocumented position was bought close to, not meaningfully below, the current live price, and below fair value — a directionally reasonable entry price in hindsight (the stock is up slightly since, and sits well under the fresh fair-value estimate), but one that still would not have cleared this framework's mandatory 2:1 R/R gate had it been run through `/new-position` first. This is a factual observation for context, not a retroactive override finding — that remains `override-log.md`/`decisions/` territory.

---

## 8. Recommendation

**HOLD — keep the existing ~10 shares; do not add more at the current price.**

- Composite Score 14.4 (Very Cheap band) nominally maps to a Full Position (6–8%) buy signal, but the mandatory 2:1 Risk/Reward gate still fails at the single most favorable authorized combination (1.25:1) — structurally identical to the 2026-08-05 conclusion, now re-confirmed with fresh price/rate/fair-value inputs rather than carried over.
- **No exit trigger fires.** None of the Full-Exit conditions (fundamental deterioration, broken growth thesis, balance-sheet crisis, or a sustained 90.0–100.0 score) apply — Quality Score improved (91.9), the moat signals are intact or strengthening, and the balance sheet remains very low-leverage (0.353× Net Debt/EBITDA).
- **The undocumented-entry documentation gap remains open** — this session does not resolve it; see `override-log.md`/`decisions/` for that separate track.
- Set a price alert at **≤$152.54** (the level at which 2:1 R/R would mechanically clear for an *add*, using this band's tightest authorized stop) — below this, adding to the position would clear the framework's gate; above it, hold as-is.

---

## 9. Data gaps / flags summary

1. **ROIC** — flagged judgment call; used median of 3 third-party sources (41.47% / 51.95% / 53.0% → 51.95%), excluding stockanalysis.com's 92.45% outlier. The ~2x jump from the 24.49% used in August reflects source/quarter volatility in a negative-invested-capital situation, not a genuine quality improvement — flagged for Phase 04 monitoring.
2. **Gross margin** — still a third-party-computed proxy (BKNG's GAAP statements carry no Gross Profit/Cost-of-Revenue line); unchanged at 87.23%, same limitation as 2026-08-05.
3. **5yr PE history** — still a no-history fallback (50.0 neutral); COVID-trough-era distortion remains inside any 5-year lookback window.
4. **Shares outstanding / net buyback yield** — still the 2026-07-27 SEC cover-page count (751,380,500); no newer filing exists to refresh this, flagged stale pending the Q3 2026 10-Q.
5. **The undocumented BKNG entry remains unresolved** in `override-log.md`/`decisions/` — not this session's call to clear.

---

## 10. Next review trigger

- BKNG's Q3 2026 earnings release (Rule 9 standard trigger — not yet reported as of this session; historically early-to-mid November)
- Any guidance revision (up or down) — mandatory re-valuation trigger regardless of schedule
- Price reaching **≤$152.54** — the level at which an add would clear the 2:1 R/R gate
- Resolution of the undocumented-entry documentation gap (separate track, `override-log.md`/`decisions/`)
- Any Middle East conflict resolution/de-escalation materially changing the international-travel-demand outlook management has flagged as the key swing factor

---

## Files touched this session

- `sessions/2026-10-11-rescore-bkng.md` — this file
- `watchlist/in-portfolio/BKNG/BKNG-2026-10-11.md` — new dated entry (old 2026-08-05 file left in place per repo convention, e.g. `watchlist/in-portfolio/AVGO/`)
- `portfolio/holdings.md` — BKNG row: Last Score, Quality Score, Composite Score, Last Review updated; urgent-flag framing updated to reflect the fresh HOLD conclusion (undocumented-trade flag itself left in place, not cleared)

`framework/glossary.md`, `watchlist/STALE.md`, and `decisions/` **not touched** — every glossary term used this session already existed (verified via `scripts.glossary_lookup`), BKNG was never marked stale under the current (2026-06-29) methodology version (its 2026-08-05 score already postdates that version), and no new trade/override is being logged by this rescore.

---

## Glossary

**Composite Score**: This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score. See [valuation-scoring.md](../framework/valuation-scoring.md).

**Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](../framework/quality-scoring.md).

**Valuation Score**: This framework's 0.0–100.0 continuous score (0.0 = cheapest, 100.0 = most expensive) combining the Phase 02 valuation sub-scores, the Rate Environment Gate, and the Upside/Downside Modifier into a single number that maps to an action band (Very Cheap/Cheap/Fair Value/Expensive) — see [valuation-scoring.md](../framework/valuation-scoring.md).

**ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.

**Moat**: Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.

**Genius (Booking.com loyalty program)**: Booking.com's tiered loyalty program: travelers get automatic discounts/perks (and escalating benefits at higher tiers) in exchange for booking history, while participating properties (~850,000 of Booking's ~2.5 million total listed properties) get better search placement and marketing support. Cited as Network Effect and Switching Costs Moat Signal evidence in this framework's 2026-08-05 BKNG session — Genius members book roughly 50% more nights annually than non-members, a documented lock-in mechanism.

**Connected Trip**: Booking Holdings' strategy of integrating flights, ground transport, attractions, insurance, and payments alongside its core accommodation bookings into a single cross-vertical itinerary, aimed at capturing more of each traveler's total spend (a ~$1.5T addressable travel market) rather than just the hotel-booking transaction — cited as documented TAM-expansion evidence in this framework's 2026-08-05 BKNG session.

**FCF/NI conversion ratio**: Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games (see the Valeant/Wirecard cases in [graveyard-audit.md](../framework/graveyard-audit.md)).

**Fast Grower**: Peter Lynch's term for a company growing earnings per share (EPS) faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score.

**Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.

**OTA (Online Travel Agency)**: An online marketplace/broker for travel bookings (accommodation, flights, car rental, packages) that sits between travelers and travel suppliers (hotels, airlines) — Booking Holdings, Expedia Group, and Trip.com Group are the largest global OTAs, distinct from a "meta-search" site (which compares prices across OTAs/suppliers but doesn't itself process the booking) or a supplier's own direct-booking channel.

**PW (Probability-Weighted) Fair Value**: This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case (Rule 7) — used as the single fair-value input to both the order setup and the Upside/Downside Modifier.

**Rate Environment Gate**: The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier.

**Rate Regime Modifier**: An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in.

**Rule 0**: This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.

**Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.

**Shareholder yield**: Cash returned to shareholders as a percentage of share price — dividend yield plus net buyback yield combined.

**Stock split**: A corporate action that increases a company's share count by a fixed ratio (e.g. 25-for-1) while proportionally reducing the price per share, so the total market value and each shareholder's proportional ownership are unchanged. Booking Holdings effected a 25-for-1 stock split on 2 April 2026; all figures in this session are post-split.

**WACC**: Weighted Average Cost of Capital — the blended cost a company pays for its debt and equity financing; used as the discount rate in a DCF.

**DCF**: Discounted Cash Flow — a valuation method that estimates a company's worth today by projecting its future cash and discounting it back to present-day value.

**Terminal Value**: In a multi-stage DCF, the lump-sum value assigned to all cash flows beyond the explicit forecast period, estimated via a perpetuity-growth formula and discounted back to today — often the single largest component of a DCF's total value, which is why Rule 4's sanity check flags a model where it exceeds 75% of total value.

**EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.

**Forward PE**: Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings).

**Historical PE Modifier**: Hybrid Upgrade 2: an additive adjustment to the Forward PE sub-score based on where the current multiple sits versus the company's own trailing 5-year PE. When no statistically usable 5-year PE history exists, this framework uses a flagged neutral 50.0 "no-history fallback" instead of forcing an estimate.

**MoS (Margin of Safety)**: How far below fair value the buy price is set, as a cushion against being wrong — e.g. a 25% MoS means buying at 75% of estimated fair value.

**R/R (Risk/Reward ratio)**: (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering.

**Hard disqualifier**: One of three Quality Score conditions that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation.

**Negative stockholders' equity (shareholders' deficit)**: When a company's total liabilities exceed its total assets, producing a negative "Total shareholders' equity" balance-sheet line — commonly from funding large buybacks with debt faster than earnings retention. Shrinks the Invested Capital denominator in a ROIC calculation, which can inflate the computed ROIC via a smaller denominator rather than genuinely improved capital efficiency.

**Invested Capital**: The total capital (debt + equity, netted for cash) put to work in a business — the denominator in a Return on Invested Capital (ROIC) calculation.

**NOPAT (Net Operating Profit After Tax)**: EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC.

**EY (Earnings Yield)**: 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury).

**TTM (Trailing Twelve Months)**: The most recent 12 months of reported financial results (the last four quarters added together), as opposed to a single fiscal year or a forward-looking estimate.

**EV**: Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.

**Market Cap (Market Capitalization)**: Share price × total shares outstanding — the total value the market currently assigns to all of a company's equity.

**FCF Yield**: Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.

**EPS**: Earnings Per Share — net income divided by number of shares outstanding.

**CAGR**: Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.

**8-K**: The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish a quarterly earnings press release ahead of the fuller 10-Q/10-K.

**Beta**: A stock's sensitivity to overall market moves — a beta of 1.0 means the stock tends to move in line with the market. Used as an input (alongside the risk-free rate and Equity Risk Premium) to estimate cost of equity in a DCF's WACC.

**Equity Risk Premium (ERP)**: The extra return equity investors demand, on average, for holding stocks instead of risk-free government bonds — an assumed modeling input, used with the risk-free rate and Beta to estimate cost of equity in a DCF's WACC.
