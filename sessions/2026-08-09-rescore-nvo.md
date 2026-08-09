# RESCORE — NVO (Novo Nordisk A/S, US-listed ADR) — 2026-08-09

**Task type:** RESCORE (single ticker, mode `--both`)
**Trigger:** [GitHub issue #467](https://github.com/cloxy777/investment-framework/issues/467) — "RESCORE: NVO - earnings released 2026-08-04" (Novo Nordisk's Q2/H1 2026 results, filed via SEC Form 6-K the same day). A genuine, on-schedule Rule 9 event (quarterly earnings release + a guidance revision in the same release) — not a Telegram or price-move trigger.
**Date:** 09 Aug 2026 (Sunday — markets closed since Friday 07 Aug close; per Rule 0 and this repo's established convention (see the 2026-07-05 NVO and 2026-07-04 AVGO sessions), the most recent completed trading session's close is used as the live price).
**10Y US Treasury Yield:** 4.64% (CNBC `US10Y`, 4.639% close, 07 Aug 2026 — the most recent trading day; cross-checked against TradingEconomics' 4.65% for the same date. Both fall from 4.656% on 06-Aug per a jobs-report-driven yield decline reported the same day.)
**Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% bracket)
**Current NVO portfolio weight:** 0.39% per [holdings.md](../portfolio/holdings.md) — nowhere near the 15% single-position cap (Upgrade 7, [strategy.md](../framework/strategy.md)); confirmed not binding.
**Prior score (2026-07-05):** Valuation 61.4 / Quality 66.2 (fails 80.0+ gate) / Composite 47.6 (reference only). Action: HOLD, no new capital, no trim.
**ADR / currency note (re-checked fresh this session, per task instructions):** NVO is a Danish ADR — one NVO ADR = one Novo Nordisk B-share, Copenhagen-listed underlying. Novo reports audited financials in **DKK under IFRS** and files a **Form 20-F** annually with the SEC as a foreign private issuer (not a 10-K); quarterly/event disclosures come via **Form 6-K** (not 8-K or 10-Q). This session's fundamentals are sourced directly from Novo's own Q2/H1 2026 Form 6-K (filed 2026-08-04, SEC EDGAR) and converted to USD only where a USD-denominated figure is required (Market Cap, EV, FCF Yield, EV/EBIT) using a **live, dated USD/DKK spot rate** — never assumed. Quality Score sub-scores (margins, ROIC, growth rates, leverage ratios) are DKK-to-DKK ratios and require no FX conversion at all.
**First-use jargon decoded in the closing Glossary (step 9).**

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$47.26** | IBKR `get_price_history` (contract_id 10611, NYSE), most recent daily bar close = **2026-08-07** (Friday — last trading session before the weekend). |
| Snapshot cross-check | $47.23 (`last`), $47.26 (`plprice`/mark) | IBKR `get_price_snapshot`, timestamped 2026-08-07 23:58 UTC (after the 4pm ET close) — `plprice` matches `get_price_history`'s close exactly; the `$0.03` gap to `last` is immaterial and not the multi-dollar staleness pattern flagged in earlier sessions. |
| Independent cross-check | **$47.26**, "as of August 7, 2026, 4:00 PM EDT" | stockanalysis.com statistics page — exact match. |
| Day's move | +$1.29 (+2.81%) | Recovering slightly on 07 Aug after the ~6% post-earnings drop on 04 Aug (Wegovy pill sales narrowly missed consensus despite the headline beat/guidance raise — see §3). |
| 52-week range | **$34.65 – $62.04** | IBKR `misc_statistics` |
| 13-week range | $41.01 – $52.12 | IBKR `misc_statistics` |
| Analyst consensus PT | **$47.32** (stockanalysis.com, dated 07 Aug 2026, 14 analysts, "Buy") — essentially at the live price; a much higher **$51.19** average (37 analysts, undated source) was also found | Wide dispersion flagged, consistent with prior sessions — the dated figure is preferred and used for the Rule 4 sanity check in §7. |
| Dividend yield | 2.72% | stockanalysis.com, dated 07 Aug 2026 |
| USD/DKK FX | **6.4824** | Multiple sources cross-checked: 6.48239 (07 Aug 2026, 11:56 UTC — date-matched to the live price), 6.4796 ("current," Investing.com), 6.4701/6.4606 (recent prior closes, both within ~0.3% of the rate used). 6.4824 used throughout for USD conversions below. |

---

## 2. Data Gathered — Sources & Gaps

**`yfinance` not attempted this session** — per the documented `curl_cffi` TLS-failure pattern (see sessions/2026-08-07-rescore-uber.md), fundamentals were sourced directly from Novo Nordisk's own **Q2/H1 2026 Form 6-K** (SEC EDGAR, filed 2026-08-04, accession 0000353278-26-000023, document `caq22026.htm`) — the primary, audited-basis source — plus stockanalysis.com/Yahoo Finance for live-market statistics (forward PE, PEG, dividend yield), each cross-checked and individually dated below.

| Metric | Value | Source / note |
|---|---|---|
| H1 2026 Net Sales (reported) | DKK 175,311M (+13% DKK / +18% CER vs H1 2025's 154,944M) | Novo's Form 6-K, Appendix 1 (Condensed Income Statement) |
| H1 2026 Net Sales (**adjusted**, ex-340B) | DKK 148,551M (−2% DKK / +2% CER vs H1 2025) | Same filing, "Performance highlights" — the 340B provision reversal (below) inflates reported sales, so adjusted is the cleaner read |
| H1 2026 Gross Profit (reported / adjusted) | 144,613M / 117,853M → Gross Margin 82.5% reported / **79.3% adjusted** | Same filing |
| H1 2026 Operating Profit / EBIT (reported / adjusted) | 86,679M / **66,247M** | Same filing |
| H1 2026 Net Profit (reported / adjusted) | 69,546M / **56,900M** | Same filing |
| H1 2026 Diluted EPS (reported / adjusted) | 15.66 DKK / **12.81 DKK** | Same filing |
| H1 2026 Effective tax rate | 19,501 / 89,047 = 21.90% | Same filing (income statement) |
| H1 2026 Free Cash Flow (company-defined) | **DKK 55,297M** | Same filing, Appendix 2 (Condensed Cash Flow Statement) — OCF DKK 79,283M − CapEx (PP&E 23,986M + intangibles 854M = 24,840M) ≈ 54,443M, close to the company's own reported 55,297M line (small gap plausibly other cash-flow items) |
| H1 2026 D&A (incl. Q2 impairment) | DKK 13,840M | Same filing. **Q2 2026 non-cash impairment: DKK 6,328M** (intangible pipeline write-offs, incl. monlunabant DKK 4,000M — development terminated, portfolio optimization) — normalized D&A ex-impairment = 7,512M |
| **Balance sheet — 30 Jun 2026, most current available** | Total debt DKK 140,127M (121,794M non-current + 18,333M current); Cash DKK 44,482M; **Net debt DKK 95,645M**; Total equity DKK 221,277M | Same filing, Appendix — a genuine, material *deleveraging* since the last review: net debt is **down** from Q1 2026's DKK 125,255M and even below FY2025 year-end's DKK 104,494M, despite continued heavy CapEx and buybacks — driven by H1 2026's strong operating cash flow |
| H1 2025 comparatives (for TTM reconstruction) | Net Sales 154,944M; Gross Profit 129,208M (83.4% margin); EBIT 72,240M; Net Profit 55,537M; FCF 38,381M; CapEx 30,861M (28,083 PP&E + 2,778 intangibles); D&A 8,663M | Same filing (comparative columns) |
| FY2025 annual (carried forward, unchanged — most recently completed fiscal year) | Net Sales 309,064M; Gross Profit 250,276M (80.98% margin); EBIT 127,658M; Net Profit 102,434M (33.14% margin); FCF 28,295M; CapEx ≈90,140M; D&A ≈21,982M; effective tax rate 21.53% | [2026-07-05 session](2026-07-05-rescore-nvo.md), sourced from Novo's FY2025 6-K, unchanged since no new full fiscal year has completed |
| Shares outstanding | ~4,440M (H1 2026 diluted weighted-average, per Novo's own EPS reconciliation) | Same 6-K. Cross-checked against stockanalysis.com's "4.43 billion" (07 Aug 2026) — within 0.3%, immaterial. **4,440M used throughout.** |
| Forward PE | **15.37×** | stockanalysis.com, explicitly dated "as of August 7, 2026, 4:00 PM EDT" — ties out exactly to the live price used ($47.26). ⚠️ Wide vendor dispersion flagged again this session: GuruFocus/wisesheets both showed 13.32–13.37× (undated, likely stale vs. today's price). The dated, price-matched figure is used, consistent with this repo's standing practice. |
| 5yr PE range | Avg 30.52×, Low 14.10× (2025), High 38.25× (2022) | wisesheets.io year-by-year 2021–2025 series — **identical to the 2026-07-05 session's figures** (annual data, unchanged mid-year) |
| PEG (forward, live) | **3.08** ("5yr expected," Yahoo Finance, dated 04 Aug 2026) | Cross-checked against other undated figures found this session (0.68, 3.37) which conflict internally and lack an as-of date/price tie-out — not used. All figures ≥2.5 in the dated/plausible range, so PEG_Score saturates at 100.0 regardless — same conclusion as every prior NVO session. |
| Buybacks (2026 YTD) | DKK 7,533M as of 03 Aug 2026 (H1 2026 alone: DKK 5,899M), against a DKK 15,000M full-year program | Same 6-K |
| Dividends | H1 2026 dividend paid DKK 35,312M; interim dividend declared DKK 3.75/share, payable Aug 2026 | Same 6-K |
| US GLP-1 market share | **Eli Lilly 60.1% vs. Novo 39.4%**, combined obesity+diabetes GLP-1 market | Multiple financial-media reports on Q2 2026 earnings (CNBC, others), Aug 2026 — a further deterioration from the 57%/43% split cited at Q3 2025 (2026-07-05 session) |
| Ex-US GLP-1 market share | Lilly ahead of Novo (unchanged, no fresher data found this session) | GxP News, May 2026 — carried forward, not re-verified this session |
| Oral Wegovy (US) | >265,000 weekly prescriptions as of 17 Jul 2026; >5 million cumulative since launch | Novo's Q2 2026 6-K |
| CagriSema | NDA filed Dec 2025 (REDEFINE 1/2 basis) — FDA decision still expected **Q4 2026** (standard ~10–12mo review timeline from filing). A separate, smaller REDEFINE 9 trial (lower-dose) has completed with results pending conference presentation; a new high-dose Phase 3 trial was just initiated, expected readout **H1 2028** (not itself a near-term catalyst). | SEC 6-K + WebSearch cross-check |

No metric was invented or estimated; every figure above traces to Novo's own Form 6-K or a vendor figure carrying an explicit as-of date/price tie-out. No data gaps required stopping this session — all Standard Re-Score template fields (operating-calendar.md) were obtained.

---

## 3. Fundamental Changes Since Last Review (2026-07-05 → 2026-08-09)

**A genuine Rule 9 double-trigger: Q2 2026 earnings (04 Aug 2026) plus a guidance revision in the same release.**

- **Guidance raised again** — FY2026 adjusted sales and adjusted operating profit growth guidance (CER) improved from **−4%/−12%** (at the 06 May Q1 print) to **0%/−6%** (04 Aug). Still guides to a decline at the low end, break-even at best — but a real, second consecutive improvement. Company attributes it to "increased expectations for GLP-1 product sales."
- **H1 2026 underlying (adjusted) growth actually turned modestly positive**: +2% CER on both sales and operating profit — a genuine improvement vs. the outright adjusted *declines* (−4% to −6% CER) reported at Q1 2026 alone (2026-07-05 session, §3). Guidance still implies H2 2026 will be weaker than H1 was, since the full-year range (0% to −6%) sits below H1's own +2% pace.
- **US GLP-1 market share loss to Eli Lilly has worsened, not stabilized**: 57%/43% (Q3 2025) → **60.1%/39.4%** (Q2 2026) — a further ~3pp share loss over roughly nine months. Lilly's oral pill (Foundayo) also beat Q2 2026 sales estimates, intensifying the head-to-head against Novo's own oral Wegovy pill. Novo's US shares fell ~6% on the earnings day itself specifically on a Wegovy-pill-sales miss, despite the headline beat and guidance raise.
- **Two new non-cash one-off items this quarter, both normalized out per Rule 6**: (a) the DKK 26.8B Q1 2026 340B provision reversal (already known, still flowing through H1's reported-vs-adjusted gap); (b) a **new** DKK 6.3B Q2 2026 non-cash impairment on intangible pipeline assets (incl. DKK 4.0B for monlunabant, whose development was terminated) — a pipeline-narrowing event, not a going-concern signal, but worth tracking as a second consecutive quarter of "clean up" charges.
- **Balance sheet materially improved**: net debt fell from Q1 2026's DKK 125,255M to **DKK 95,645M** at 30 Jun 2026 — a genuine deleveraging (not merely a reporting-basis artifact), despite continued heavy CapEx (DKK 24,840M in H1 2026 alone) and accelerated buybacks (DKK 5,899M in H1 2026). Driven by H1 2026's strong DKK 79,283M operating cash flow.
- **Oral Wegovy's commercial ramp continued**: >265,000 weekly US prescriptions (17 Jul 2026), >5 million cumulative — a genuine positive data point, though (per the market-share numbers above) not enough to reverse the broader competitive trend.
- **CagriSema**: no new negative trial readout this session; the near-term FDA decision (Q4 2026) remains the nearest dated catalyst, unchanged from 2026-07-05.
- No management change, no material M&A, no macro/rate-policy shift beyond the routine Treasury drift already reflected in §1's yield figure.
- **Price move since 07-05: −6.3%** ($50.43 → $47.26) — explained by the earnings-day reaction (Wegovy pill miss), not an unexplained Rule 9 trigger on its own, but it interacts materially with this session's Upside/Downside Modifier (§7).

---

## 4. Rate Environment Gate — Re-verified With Fresh Data

```
Step 1 — Earnings Yield Spread Test
EY = 1 ÷ Forward PE = 1 ÷ 15.37 = 6.506%
Spread = EY − 10Y Treasury = 6.506% − 4.64% = +1.866pp
Threshold: Spread ≥ +1.5% → PASS (no +5 addition)
```

**Result: PASS, comfortably — and by a much wider margin than the 2026-07-05 session's razor-thin +0.078pp.** The improvement is driven by Forward PE *falling* from 16.48× to 15.37× even as the live price also fell (−6.3%) — meaning the market's forward EPS estimate for NVO rose since 07-05, consistent with the guidance raise in §3. Robustness check: using the alternate lower vendor Forward PE figures found (13.32–13.37×, flagged as likely stale/undated) would widen the passing margin further (EY ≈7.5%, spread ≈+2.9pp) — the PASS conclusion is not sensitive to which plausible Forward PE figure is used.

```
Step 2 — Rate Regime Modifier
10Y = 4.64% → 3.5–5% bracket → +5
```

**Combined Rate Gate additions this session: +5** (Step 1 contributes +0, unchanged bracket from every session since 06-20).

---

## 5. Quality Score (2026-06-29 methodology) — Basis: TTM (trailing twelve months through 30 Jun 2026), adjusted/normalized per Rule 6, with FY2025-annual shown as a sensitivity cross-check throughout (same dual-basis discipline as this cycle's UBER session)

### Hard disqualifier check (fiscal-year rolling window, per the [2026-08-05 rolling-window clarification](../framework/quality-scoring.md))

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive yrs w/o growth-capex explanation? | FY2024: 69,700/100,988 = **69.0%**; FY2025: 28,295/102,434 = **27.6%** — both below 70%, unchanged from 07-05 (no new full fiscal year completed since) | disqualify unless documented growth-capex explanation exists | ⚠️ **Carve-out applies — PASS**, unchanged from every prior session. The GLP-1 manufacturing capacity build-out (Catalent fill-finish acquisition, Clayton NC facility, Kalundborg/Hillerød expansions) remains the documented cause — H1 2026 CapEx of DKK 24,840M confirms the program is still active, just at a lower run-rate than 2025's peak. |
| Net Debt/EBITDA over threshold? | TTM (30 Jun 2026 balance sheet ÷ TTM adjusted EBITDA): 95,645/142,496 = **0.671×** | disqualify if >2.5× (standard) | ✅ PASS, comfortably — improved from 07-05's 0.837× (Q1 2026 basis), reflecting the deleveraging in §3 |
| FCF-positive 3+ consecutive years? | FY2023, FY2024, FY2025 all positive; H1 2026 alone (55,297M) already exceeds all of FY2025 | disqualify if not | ✅ PASS |

No hard disqualifier fires. Proceeding to the weighted score.

### Profitability (25% weight)

```
TTM Adjusted Net Sales  = FY2025 (309,064) − H1 2025 (154,944) + H1 2026 adjusted (148,551) = DKK 302,671M
TTM Adjusted Net Profit = FY2025 (102,434) − H1 2025 (55,537)  + H1 2026 adjusted (56,900)  = DKK 103,797M

Net Margin (TTM, adjusted) = 103,797 / 302,671 = 34.30%
NetMargin_Component = clamp((34.30/30)×100, 0, 100) = clamp(114.3, 0, 100) = 100.0

TTM Adjusted EBIT = FY2025 (127,658) − H1 2025 (72,240) + H1 2026 adjusted (66,247) = DKK 121,665M
TTM effective tax rate = [FY2025 tax 28,106 − H1'25 tax 15,301 + H1'26 tax 19,501] / [FY2025 pretax 130,540 − H1'25 pretax 70,838 + H1'26 pretax 89,047]
                        = 32,306 / 148,749 = 21.72%
NOPAT = 121,665 × (1 − 0.2172) = DKK 95,239M
Invested Capital (30 Jun 2026) = Total Debt 140,127 + Equity 221,277 − Cash 44,482 = DKK 316,922M
ROIC = 95,239 / 316,922 = 30.05%
ROIC_Component = clamp((30.05/30)×100, 0, 100) = clamp(100.2, 0, 100) = 100.0

Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF-positive cap — 3yr positive confirmed above)
```
*Sensitivity (FY2025-annual basis, unchanged from 07-05): Net Margin 33.14%, ROIC 33.55% — both still saturate to 100.0. Robust to basis choice.*

### Margins (15% weight)

```
TTM Adjusted Gross Profit = FY2025 (250,276) − H1 2025 (129,208) + H1 2026 adjusted (117,853) = DKK 238,921M
Gross Margin (TTM, adjusted) = 238,921 / 302,671 = 78.94%
GrossMargin_Score = clamp((78.94/80)×100, 0, 100) = 98.68
```
No structural-trend bonus applies (bonus is only for sub-40% margins showing expansion — not the case here). **Watch item, not a trigger:** TTM gross margin (78.94%) sits ~2.0pp below FY2025's 80.98% — a real but modest compression, well short of the 3pp "structural margin compression" fair-value-methodology.md sell trigger. Flagged for the next review, not actioned.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 → FY2025, unchanged) = (309,064/176,954)^(1/3) − 1 = 20.43%
Growth_Score = clamp((20.43/25)×100, 0, 100) = 81.74
```

**Modifier — documented structural deceleration, −10 applied again this session, evidence refreshed and, if anything, strengthened:**
- FY2026 guidance still projects an adjusted CER decline at the low end (0% to −6%) even after two consecutive upward revisions — the framework's own guided outlook remains net-negative for the full year.
- US GLP-1 share loss to Lilly has **worsened**, not stabilized, since 07-05 (57%/43% → 60.1%/39.4%) — the clearest, freshest evidence this modifier is capturing a real structural (not cyclical) dynamic.
- Lilly's oral pill outperforming Novo's own oral Wegovy pill in the same quarter reinforces the competitive-share thesis rather than undermining it.
- The category-wide GLP-1 TAM is still expanding (oral Wegovy's own 5M-cumulative-script ramp is a genuine positive) — but as in every prior session, that expansion is not translating into share gains or pricing power *for Novo specifically*, so no offsetting +10 bonus is applied.

```
Growth_Score = clamp(81.74 − 10, 0, 100) = 71.74
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA (TTM, 30 Jun 2026 balance sheet ÷ TTM adjusted EBITDA)
  TTM Adjusted EBITDA = TTM Adjusted EBIT (121,665) + TTM normalized D&A (ex-impairment)
    TTM normalized D&A = FY2025 (21,982) − H1 2025 (8,663) + H1 2026 ex-impairment (13,840 − 6,328 = 7,512) = DKK 20,831M
    TTM Adjusted EBITDA = 121,665 + 20,831 = DKK 142,496M
  Net Debt/EBITDA = 95,645 / 142,496 = 0.671×
BalanceSheet_Score = clamp(100×(1 − 0.671/4), 0, 100) = 83.22
```
*Sensitivity (reported, unadjusted TTM EBITDA — includes the one-off items): 95,645/169,256 = 0.565× → score 85.87. Either basis is far inside the 2.5× standard gate; the adjusted/normalized figure (83.22) is used as primary, consistent with Rule 6.* This is a real improvement vs. 07-05's 79.1 (Q1 2026 basis), reflecting the deleveraging in §3.

### Moat Signal (15% weight) — checklist, cited evidence only, refreshed this session

| Signal | Marked | Evidence |
|---|---|---|
| Market share stable/growing | **FALSE** | US combined obesity+diabetes GLP-1 share: Eli Lilly 60.1% vs. Novo 39.4% (Q2 2026 earnings-period reporting, Aug 2026) — a further ~3pp deterioration from the 57%/43% split cited at 2026-07-05 (Q3 2025 data). Lilly also remains ahead ex-US (carried forward, May 2026 GxP News, not re-verified this session). Oral Wegovy's own strong prescription ramp is a genuine positive counter-data-point in one sub-segment but does not reverse the documented aggregate trend, which has gotten *worse* since the last review, not better. |
| Brand premium | **FALSE** | No cited evidence of price increases without volume loss; net US price erosion remains part of the company's own guidance narrative, unchanged. |
| Network effect | **FALSE** | No two-sided-marketplace or user-growth-driven mechanism applies to a prescription pharmaceutical business. |
| Switching costs | **FALSE** | The continuing pace and magnitude of the share shift to Lilly (worsening quarter over quarter) remains itself evidence against durable switching costs in this category. |
| Scale cost advantage | **FALSE** | No cited cost-per-unit data vs. smaller competitors on file, unchanged from 07-05. |

```
Moat_Score = (0/5) × 100 = 0.0
```
Unchanged at the most severe reading of any holding scored in this repo — reinforced, not resolved, by this session's fresher (and more adverse) market-share data.

### FCF Quality (10% weight)

```
TTM FCF = FY2025 (28,295) − H1 2025 (38,381) + H1 2026 (55,297) = DKK 45,211M
TTM Adjusted Net Profit (from Profitability, above) = DKK 103,797M
FCF/NI (TTM, adjusted-NI basis) = 45,211 / 103,797 = 43.56%
FCFQuality_Score = clamp(((0.4356 − 0.40)/0.60)×100, 0, 100) = 5.93
```
*Sensitivity (reported, unadjusted TTM Net Profit — includes the 340B one-off): 45,211/116,443 = 38.82% → score floors at 0.0 (below the 40% floor of the formula's range).* Primary (adjusted-NI) figure used per Rule 6, consistent with every other sub-score in this session's Quality calc. Either way this remains the weakest sub-score in the book (10% weight makes the primary-vs-sensitivity choice immaterial to the final Quality Score — 0.59 points either way).

### Quality Score — Final

```
Quality Score = (100.0×0.25) + (98.68×0.15) + (71.74×0.20) + (83.22×0.15) + (0.0×0.15) + (5.93×0.10)
              = 25.0 + 14.802 + 14.348 + 12.483 + 0.0 + 0.593
              = 67.226 → 67.2
```

**Quality Score = 67.2 — FAILS the 80.0+ gate, though a modest improvement on 07-05's 66.2** (+1.0), driven mainly by the Balance Sheet sub-score (deleveraging) and marginal Profitability/FCF-Quality refinements, essentially offset by nothing improving on the Growth or Moat side — those two remain the binding constraints, and the fresh Moat evidence this session is, if anything, worse than before. Sensitivity range across all disclosed alternate bases: **66.6–67.9** — a robust FAIL regardless of which basis combination is used, not a knife-edge case.

Per RESCORE process, an existing holding failing the Quality Gate is not retroactively force-exited — surfaced again as a **Phase 04 Quality Watch escalation** (see §9).

---

## 6. Valuation Score (Phase 02) — Basis: TTM (primary), FY2025-annual (sensitivity)

### FCF Yield (40% weight)

```
Market Cap = $47.26 × 4,440M shares = $209,834.4M

TTM (primary):
  FCF (TTM) = DKK 45,211M ÷ 6.4824 = $6,974.4M
  FCF Yield = 6,974.4 / 209,834.4 = 3.324%
  FCF_Score = clamp(100×(1 − 3.324/10), 0, 100) = 66.76

FY2025-annual (sensitivity):
  FCF (FY2025) = DKK 28,295M ÷ 6.4824 = $4,364.6M
  FCF Yield = 4,364.6 / 209,834.4 = 2.080%
  FCF_Score = clamp(100×(1 − 2.080/10), 0, 100) = 79.20
```
No Owner Earnings adjustment (Upgrade 1) applied — NVO is not on the framework's named Upgrade-1 list, unchanged rationale from every prior NVO session.

### EV/EBIT (25% weight)

```
Net Debt (30 Jun 2026, most current) = DKK 95,645M ÷ 6.4824 = $14,754.6M
EV = Market Cap $209,834.4M + Net Debt $14,754.6M = $224,589.0M

TTM (primary):
  EBIT (TTM, adjusted) = DKK 121,665M ÷ 6.4824 = $18,768.4M
  EV/EBIT = 224,589.0 / 18,768.4 = 11.97×
  EV/EBIT_Score = clamp((11.97 − 12)/23 × 100, 0, 100) = clamp(−0.14, 0, 100) = 0.0

FY2025-annual (sensitivity):
  EBIT (FY2025) = DKK 127,658M ÷ 6.4824 = $19,693.3M
  EV/EBIT = 224,589.0 / 19,693.3 = 11.41×
  EV/EBIT_Score = clamp((11.41 − 12)/23 × 100, 0, 100) = 0.0
```
Both bases now sit **below** the 12× floor (was 12.44× — score 1.9 — on 07-05) — a modest further cheapening on this metric, floors to 0.0 either way.

### Forward PE + Historical PE Modifier (20% weight)

A genuine 5yr low/high range exists (§2) → primary formula:
```
Forward PE = 15.37×, 5yr Low = 14.10×, 5yr High = 38.25×
FwdPE_Score = clamp((15.37 − 14.10)/(38.25 − 14.10) × 100, 0, 100) = clamp(5.26, 0, 100) = 5.26
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs. 5yr avg (30.52×): (15.37 − 30.52)/30.52 × 100 = **−49.6%** (>20% below) → **−10**.
```
FwdPE_Score = clamp(5.26 − 10, 0, 100) = 0.0
```

### PEG (15% weight) — Fast-Grower eligibility maintained

**Ruling carried forward, unchanged:** NVO's trailing 3yr EPS CAGR (23.5%, clean audited base, established at 2026-06-20) still comfortably clears the >15%-for-3+-years Fast Grower bar — this is a backward-looking eligibility test, unaffected by this quarter's guidance swings. PEG stays live.

```
PEG = 3.08 (Yahoo, "5yr expected," dated 04 Aug 2026)
PEG_Score = clamp((3.08 − 0.5)/2.0 × 100, 0, 100) = clamp(129.0, 0, 100) = 100.0
```

### Raw Weighted Score

```
TTM (primary):
Raw = (66.76×0.40) + (0.0×0.25) + (0.0×0.20) + (100.0×0.15)
    = 26.704 + 0 + 0 + 15.0 = 41.704

FY2025-annual (sensitivity):
Raw = (79.20×0.40) + (0.0×0.25) + (0.0×0.20) + (100.0×0.15)
    = 31.68 + 0 + 0 + 15.0 = 46.68
```

**+ Rate Environment Gate (§4): +0 (Step 1 PASS) + 5 (Step 2) = +5**

```
TTM:          41.704 + 5 = 46.704
FY2025-basis: 46.68  + 5 = 51.68
```

---

## 7. Upside/Downside Modifier (Expected-Return Modifier)

**Step 1 — scenario fair values (Rule 7).** Forward ADR EPS base ≈ $3.075 (live price ÷ Forward PE: $47.26/15.37):

| Scenario | Wt | Assumption | EPS | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | Oral-Wegovy international ramp (H2 2026) + CagriSema FDA approval (Q4 2026) + Medicare $50/mo GLP-1 coverage meaningfully slow the share loss to Lilly; partial re-rate | $3.20 | 18× | **$57.60** |
| Base | 50% | Consensus forward EPS holds near current estimate; multiple holds near the current de-rated level (unchanged assumption from 07-05 — no evidence yet of a re-rating) | $3.08 | 14× | **$43.12** |
| Bear | 25% | Lilly's oral pill (Foundayo) continues to outpace Novo's oral Wegovy; further US net-price erosion per the low end of guidance; de-rate | $2.70 | 9× | **$24.30** |

```
PW Fair Value = 0.25×57.60 + 0.50×43.12 + 0.25×24.30 = $42.04
```
**Sanity check (Rule 4):** PW FV $42.04 sits **~11%** below the dated analyst consensus PT ($47.32) and further below the wider, undated 37-analyst average ($51.19) — a conservative, not rosy, scenario blend, appropriately reflecting the moat-erosion evidence in §5 rather than assuming a rosy recovery (Guardrail 2).

**Step 2 — catalyst window & annualization (Rule 10).** Documented catalysts within the window: oral-Wegovy international launch ramp (H2 2026) and the CagriSema FDA decision (**Q4 2026**, ~4–5 months out) — both inside 18–24 months, so the standard 2yr window applies (no −5 upside cap needed; Guardrail 1 satisfied).

```
Gap Upside % = (42.04 ÷ 47.26) − 1 = −11.05%
Annualized gap = −11.05% ÷ 2 = −5.53%/yr
```

**Step 3 — expected annual return E.**
```
Intrinsic growth = +2.56%/yr   (H1 2026 adjusted diluted EPS growth: 12.81 DKK vs. H1 2025's 12.49 DKK
   [55,537M ÷ 4,448M shares] — a directly sourced, disclosed figure this session, replacing 07-05's
   assumed +1.0%/yr placeholder with the freshest real growth print available)

Shareholder yield = dividend yield 2.72% + buyback yield
   Buyback yield: DKK 7,533M repurchased Jan 1 – 3 Aug 2026 (≈7.1 months) → annualized ≈ DKK 12,731M/yr
     ÷ FX 6.4824 ÷ Market Cap $209,834.4M = 0.94%
   Shareholder yield = 2.72% + 0.94% = 3.66%

E = −5.53 + 2.56 + 3.66 = +0.69%/yr
```

**Step 4 — map E to M** (hurdle H = 10%, 0 ≤ E < H branch, since E flipped from negative to modestly positive this session):
```
M = +5 × (H − E)/H = +5 × (10 − 0.69)/10 = +5 × 0.931 = +4.66
```
**Sensitivity:** the intrinsic-growth input is the most discretionary piece here — even swinging it from 0% to +3%/yr moves E only between roughly −1.85% and +1.15%, both still comfortably inside the 0≤E<H branch (M between +4.4 and +5.0). **The modifier's sign and rough magnitude are not sensitive to this judgment call** — a genuine improvement in robustness vs. 07-05, where the modifier sat close to a branch boundary.

**This session's headline finding:** the expected-return picture has **flipped from modestly negative (E=−3.71%, M=+8.71 on 07-05) to modestly positive (E=+0.69%, M=+4.66 now)** — driven by the ADR price *falling* 6.3% since 07-05 while the probability-weighted fair value estimate held roughly flat ($42.35 → $42.04), and by a real, sourced improvement in the intrinsic-growth input (guidance-raise-driven). NVO now trades only modestly above, rather than meaningfully above, its own probability-weighted fair value.

---

## 8. Final Valuation Score & Composite Score

```
TTM (primary):
FINAL VALUATION SCORE = Raw + Rate Gate (46.704) + Upside/Downside Modifier (+4.66) = 51.364 → 51.4

FY2025-annual (sensitivity):
FINAL VALUATION SCORE = Raw + Rate Gate (51.68) + Upside/Downside Modifier (+4.66) = 56.34 → 56.3
```

**Both bases land in the same 50.0–69.9 "Fair Value" band — the action conclusion (§9) is not sensitive to which FCF/EBIT basis is used**, unlike this cycle's UBER session where the two bases crossed a band boundary.

| | TTM (primary) | FY2025-annual (sensitivity) |
|---|---|---|
| Raw weighted | 41.704 | 46.68 |
| Rate Gate | +5 | +5 |
| Upside/Downside Modifier | +4.66 | +4.66 |
| **FINAL VALUATION SCORE** | **51.4** | **56.3** |
| Prior valuation score (07-05) | 61.4 | 61.4 |
| **Quality Score** | **67.2** (FAILS 80.0+ gate) | — |

```
Composite Score (reference only, per established practice for a Quality-Score-gate failure on an existing holding)
                = 0.50 × (100 − 67.2) + 0.50 × 51.4
                = 0.50 × 32.8 + 0.50 × 51.4
                = 16.4 + 25.7
                = 42.1
```

**Composite Score = 42.1** (vs. 47.6 on 07-05) — nominally in the **"Cheap → BUY, Standard position 3–5%"** band (30.0–49.9). **Not adopted to drive the action recommendation**, consistent with this repo's standing practice for any holding whose Quality Score fails the gate (AVGO/NKE/NOW/UBER precedent) — shown for the record only, per "no black box."

---

## 9. Action Recommendation

**(a) The raw Valuation Score (51.4 primary / 56.3 sensitivity) sits in the 50.0–69.9 "Fair Value" band under both bases** → per the current Phase 03/05 action tables: **Hold — watch only, no new entry, no trim.**

**(b) Order-setup discipline, for completeness (reference only, since action is driven independently by (a) and (c)):**

| Field | Value |
|---|---|
| Blended (PW) Fair Value | $42.04 |
| Margin of Safety (Composite 30–49.9 band) | 25–30%, midpoint 27.5% |
| **Buy price (limit), midpoint** | $42.04 × 0.725 = **$30.48** |
| Primary sell target | $42.04 |
| Bull-case trim target | $57.60 × 0.90 = $51.84 |
| Stop loss (buy × 0.725) | $22.10 |
| **R/R at midpoint buy price** | (42.04 − 30.48) / (30.48 − 22.10) = 11.56 / 8.38 = **1.38:1 — fails the 2:1 minimum** |
| Live price vs. buy price | $47.26 is **~55% above** the disciplined buy price |

The sell target ($42.04) still sits below the live price ($47.26) — NVO is trading above, not below, its own probability-weighted fair value, though the gap has narrowed from ~19% (07-05) to ~12.4% now. **No order is placed.**

**(c) Phase 04 Quality Watch escalation, carried forward and reinforced by fresher evidence** — Quality Score (67.2) fails the 80.0+ gate, driven chiefly by **Moat_Score 0.0 (0/5 signals)** — unchanged at the most severe reading in this repo, and this session's freshest evidence (US GLP-1 share now 60.1%/39.4%, worse than 07-05's 57%/43%) points the wrong direction, not toward resolution. Two things still keep this from crossing into a Phase 06 "growth thesis broken" **Full Exit** recommendation: (i) guidance was raised for a second consecutive quarter (less-negative, not cut), so the specific "guidance cut 2+ consecutive quarters" trigger does not fire — if anything the opposite pattern is now underway; and (ii) profitability, margins, and the balance sheet remain excellent-to-improving (Profitability 100.0, Margins 98.7, Balance Sheet 83.2 — the last of these a real improvement this session) — this is a moat/growth problem, not a "fundamental deterioration: margins structurally broken, ROIC below cost of capital" situation.

**Turnaround Sub-Gate (Upgrade 4)** — checked again for completeness: still doesn't qualify. Condition 3 (an independent FV estimate showing ≥40% margin of safety) still fails outright — live price ($47.26) sits above, not below, this session's PW Fair Value ($42.04).

### Net Action: **HOLD** — maintain the existing ~0.39%-weight position as-is

- **No new capital** — independently blocked by the raw Valuation Score band, the R/R gate, and the Quality Watch/Moat_Score=0.0 finding — all three unchanged in direction from 07-05, though the magnitude of the "overvalued" signal has genuinely eased this session (Valuation Score 61.4→51.4, E flipped from −3.7% to +0.7%).
- **No trim** — the Valuation Score is well below the 70.0+ trim threshold under either basis, and the (false-green-light) Composite (42.1) is nowhere near a trim band either.
- **This name remains an open, unactioned candidate for a formal `override-log.md` entry / dedicated EXIT REVIEW** — flagged continuously since 2026-06-07 and still not logged (confirmed no NVO row exists in [override-log.md](../portfolio/override-log.md) as of this session). This session's evidence (worsening Moat, but improving guidance/balance-sheet/valuation) is genuinely mixed rather than a clean escalation — calling the override question is left to the user/orchestrator, consistent with this repo's scope conventions.

**Position cap check (Upgrade 7):** 0.39% is nowhere near the 15% hard cap — not binding, confirmed per task instructions.

---

## 10. Next Review Trigger

- **Q3 2026 earnings** (expected early-to-mid November 2026, based on Novo's typical quarterly cadence) — the next scheduled Rule 9 trigger; specifically watch (a) whether US/ex-US GLP-1 share loss to Lilly continues to worsen or finally stabilizes, (b) whether the third consecutive guidance revision continues improving or reverses, (c) oral-Wegovy's international launch ramp, and (d) whether the gross-margin compression flagged in §5 (80.98%→78.94% TTM) continues or was a one-quarter blip.
- **CagriSema FDA decision, Q4 2026** — the nearest named catalyst feeding the Upside/Downside Modifier (§7); an approval (or a further underwhelming signal) would materially move the Bull-scenario assumption.
- **Rate Gate Step 1** — now passing comfortably (+1.87pp margin, much healthier than 07-05's +0.08pp) — a lower-priority watch item this cycle.
- **Standing Rule 9 triggers**: a management change, material M&A, or a >15% unexplained price move.
- **The standing, unactioned override-log/EXIT REVIEW recommendation** (§9) — carried forward again this session, now with a more genuinely mixed (not purely deteriorating) evidence picture than in prior cycles.

---

## 11. Glossary

- **340B Drug Pricing Program**: a US federal program requiring drug manufacturers to discount outpatient drugs for certain low-income-serving providers; a **reversal** of a related liability provision is a one-off, non-cash accounting gain — Novo's Q1 2026 results included a DKK 26.8B reversal, still flowing through this session's H1 2026 reported-vs-adjusted comparisons.
- **ADR (American Depositary Receipt)**: a US-exchange-listed security representing shares of a non-US company; NVO ADR = 1 Novo Nordisk B-share.
- **CAGR**: Compound Annual Growth Rate.
- **CapEx**: Capital Expenditure.
- **CER (Constant Exchange Rate)**: a growth-rate presentation stripping out currency-movement effects — used throughout Novo's own guidance and results commentary.
- **Composite Score**: this framework's blended 0.0–100.0 ranking — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — shown here as a disclosed reference figure only, since NVO's Quality Score fails the 80.0+ gate.
- **D&A**: Depreciation & Amortization.
- **DCF**: Discounted Cash Flow.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **EPS**: Earnings Per Share.
- **EV / EV/EBIT**: Enterprise Value (market cap + net debt) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against the 10-Year Treasury in the Rate Environment Gate.
- **Fast Grower**: a company growing EPS >15%/yr for 3+ years on a clean earnings base — this framework's PEG sub-score trigger.
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check).
- **Form 6-K**: a furnished report foreign private issuers file with the SEC between annual filings — this session's primary source for NVO's Q2/H1 2026 results.
- **Form 20-F**: the annual report foreign private issuers file with the SEC — NVO's equivalent of a US 10-K.
- **Forward PE**: price ÷ next-twelve-months expected EPS.
- **FV / PW Fair Value**: Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear, Rule 7).
- **GLP-1**: the hormone-mimicking drug class (Novo's Ozempic/Wegovy, Lilly's Mounjaro/Zepbound) at the center of NVO's business and this session's Moat Signal findings.
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of weighted score.
- **Hurdle rate**: the minimum acceptable annual return (10%) the Upside/Downside Modifier measures expected return against.
- **IFRS**: International Financial Reporting Standards — the accounting framework Novo Nordisk reports under (vs. US GAAP).
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Moat**: a durable competitive advantage protecting a business's profits — quantified at 0.0 (0 of 5 signals) for NVO again this session.
- **MoS (Margin of Safety)**: the discount below fair value demanded before buying.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate.
- **NI**: Net Income.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PEG ratio**: PE ÷ earnings growth rate.
- **pp (percentage points)**: a direct difference between two percentages.
- **PT (Price Target)**: an analyst's price forecast.
- **Quality Score**: this framework's 0.0–100.0 score (higher = better); 80.0+ required to reach Phase 02/Composite Score.
- **Rate Environment Gate / Rate Regime Modifier**: the pre-score check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-bracket adjustment.
- **R/R (Risk/Reward ratio)**: expected gain ÷ expected loss; this framework requires ≥2:1 to enter.
- **ROIC**: Return on Invested Capital.
- **Rule 0 / Rule 4 / Rule 6 / Rule 7 / Rule 9 / Rule 10**: this framework's standing instructions to always fetch a live price first; sanity-check implied returns; normalize one-off items before valuing; use a scenario-weighted (not rosy) fair value; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst/timeline.
- **Shareholder yield**: dividend yield plus net buyback yield.
- **TAM**: Total Addressable Market.
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported results.
- **Treasury yield (10Y)**: this framework's risk-free-rate benchmark.
- **Turnaround Sub-Gate**: the conditional path (Upgrade 4) letting a company failing some quality criteria still enter as a small position if 5 specific tests all pass — checked (and found not to qualify) for NVO again in §9.
- **Upside/Downside Modifier (Expected-Return Modifier)**: the additive ±15 valuation-score adjustment based on expected annual return vs. the 10% hurdle.
