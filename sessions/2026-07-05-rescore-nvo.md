# RESCORE — NVO (Novo Nordisk A/S, US-listed ADR) — 2026-07-05

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 05 Jul 2026 (Sunday — markets closed since 03 Jul; most recent completed session's close used as the live price, per Rule 0)
**10Y US Treasury Yield:** 4.49% (TradingEconomics/CNBC, 2026-07-02 close — most recent print available; the US Treasury market observed the July 4th holiday on Fri 3 Jul, then the weekend, so 2 Jul is the latest available yield)
**Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% bracket)
**Current NVO portfolio weight:** 0.44% (per [holdings.md](../portfolio/holdings.md), 5 shares, IBKR)
**Prior score:** 47.6 (2026-06-20 rescore) — Cheap band nominally, but HOLD/no-add under standing order-discipline and value-trap flags. Quality Score / Composite Score never computed for NVO before this session (flagged stale under the 2026-06-29 methodology — see [watchlist/STALE.md](../watchlist/STALE.md)).
**Sector:** Healthcare — Pharmaceuticals (GLP-1 / Diabetes & Obesity Care)
**ADR note:** NVO is a Danish ADR (American Depositary Receipt) — one NVO ADR = one Novo Nordisk B-share, Copenhagen-listed underlying, reporting audited financials in DKK under IFRS (Novo files a **Form 20-F** annually with the SEC as a foreign private issuer, not a 10-K; interim/event disclosures come via **Form 6-K**, not 8-K). All USD figures below are computed from the DKK-denominated primary source converted at the live USD/DKK rate — never assumed.
**First-use jargon decode:** see closing Glossary (step 9).

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$50.43** | IBKR `get_price_history` (contract_id 10611, NYSE), most recent daily bar close = **2026-07-02** (last trading session before the market observed the July 4th holiday on Fri 3 Jul, ahead of the Sat/Sun weekend — same calendar pattern already documented in this repo's 2026-07-04 AVGO session). |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$48.77** (marked `is_close: true`) — this is stale by one session: it matches the **2026-07-01** close in `get_price_history`, not the most recent one. `plprice` (mark price) correctly showed **$50.43**, matching `get_price_history`'s fresher close. Used $50.43. This is the same recurring `get_price_snapshot`-staleness issue flagged in multiple recent sessions (per CLAUDE.md's explicit warning) — resolved the same way, by cross-checking against `get_price_history`. |
| Independent cross-check | **$50.43** | stockanalysis.com's live statistics page, explicitly dated "as of July 5, 2026" — exact match to the IBKR figure, strong corroboration. |
| 52-week range | **$34.65 – $68.69** | IBKR `get_price_snapshot` `misc_statistics` (`low_52w` 34.654, `high_52w` 68.687) |
| 13-week high | $50.89 | IBKR `misc_statistics` — live price ($50.43) is sitting almost exactly at its 13-week high, i.e. near the top of its recent (though not full-year) trading range |
| Analyst consensus PT | **$47.64** (stockanalysis.com, "Buy", dated 2026-07-05) — cross-checked against **$46.72** (S&P Global, 14 analysts, "Buy") | Both third-party consensus sources agree closely; both sit **below** the current live price ($50.43), i.e. the Street's own average target implies the stock is already ahead of consensus fair value. |
| US 10Y Treasury yield | 4.49% | TradingEconomics/CNBC, 2026-07-02 |
| USD/DKK FX | **6.535** | Multiple FX sources (tradingeconomics.com, exchangerates.org.uk), 2026-07-03 close — the most recent available print |

---

## 2. Data Gathered — Sources & Gaps

**yfinance unreachable this session** (`curl_cffi` TLS `SSLError` / then `YFRateLimitError` on retry) — the same recurring connectivity issue already documented for several tickers this week. Per Rule 0's fallback chain, fundamentals were sourced instead from: Novo Nordisk's own SEC filings (Form 6-K for FY2025 full-year results, filed 2026-02-03, and for Q1 2026 results, filed ~2026-05-06), and third-party aggregators (stockanalysis.com, wisesheets.io) cross-checked against each other and against the primary filings.

| Metric | Value | Source / note |
|---|---|---|
| FY2025 Net Sales | DKK 309,064M | Novo Nordisk Form 6-K, FY2025 results (`caq42025.htm`, filed 2026-02-03) — matches stockanalysis.com's income statement exactly |
| FY2025 Gross Profit | DKK 250,276M → **Gross Margin 80.98%** | Same 6-K. ⚠️ **Correction vs. 2026-06-20 session:** that session cited gross margin **83.2%** — this session's figure, freshly sourced directly from Novo's own filing and cross-validated against an independent vendor (stockanalysis.com), is **80.98%**. The most likely explanation is the prior session inadvertently used a `yfinance` field already flagged in that same session as DKK/USD-currency-mixed and unreliable ("data gap #2"). Using the freshly-verified 80.98% this session. |
| FY2025 EBIT (GAAP) | **DKK 127,658M** | Same 6-K. ⚠️ **Correction vs. 2026-06-20 session:** that session cited EBIT **DKK 134,750M** — a ~5.3% difference. This session's figure is sourced directly from Novo's own reported income-statement line and is internally consistent with FY2025's own EBITDA (DKK 149,640M, implying D&A of DKK 21,982M — a clean, plausible figure) and independently cross-checked against stockanalysis.com's own financials page, which reports the identical DKK 127,658M. Using the freshly-verified figure. |
| FY2025 Net Profit | DKK 102,434M → **Net Margin 33.14%** | Same 6-K — matches the 2026-06-20 session's 33.1% net margin almost exactly (small rounding only), so this line is **not** revised. |
| FY2025 Effective tax rate | 21.53% (tax DKK 28,106M ÷ pretax income DKK 130,540M) | Same 6-K / stockanalysis.com cross-check |
| **FY2025 Free Cash Flow** | **DKK 28,295M** | Novo's own reported "Free Cash Flow" line, same 6-K — essentially unchanged from the 2026-06-20 session's DKK 28,990M (immaterial ~2% variance). ⚠️ **Vendor data-quality flag:** stockanalysis.com's own cash-flow-statement page reports a materially different FCF figure (DKK 58,962M) for FY2025, computed from an operating cash flow of DKK 119,102M (which **does** match Novo's own figure) minus a capital-expenditure figure of only DKK 60,140M. Novo's own filing shows **two** capex lines — DKK 60,140M for property/plant/equipment **plus a separate DKK 30,000M for intangible assets** (total capex ≈ DKK 90,140M, consistent with the 2026-06-20 session's "CapEx surged DKK 51B→90B" finding) — the vendor's cash-flow page only captured the PP&E component, silently omitting the intangible-asset capex and thereby overstating FCF by roughly DKK 30.7B. Used Novo's own reported Free Cash Flow line (DKK 28,295M) instead, which is the Rule-0-compliant primary source and ties out with the prior session's independently-sourced figure. |
| FY2025 Diluted EPS / shares | 23.03 DKK / 4,448M diluted weighted-avg | Same 6-K / stockanalysis.com — matches the 2026-06-20 session's 23.05 DKK to the rounding |
| FY2024 Net Profit (for FCF/NI check) | DKK 100,988M | stockanalysis.com income statement |
| FY2023 Net Profit (for FCF/NI check) | DKK 83,683M | stockanalysis.com income statement |
| FY2022 Revenue / EPS (for 3yr CAGR) | DKK 176,954M / 12.22 DKK | stockanalysis.com — matches the 2026-06-20 session's "≈177.0B" and "DKK 12.22" exactly |
| **Balance sheet — Q1 2026 (31 Mar 2026), most current available** | Total debt DKK 146,382M; Cash DKK 21,127M; Equity DKK 203,065M | SEC Form 6-K, Q1 2026 results (`caq12026.htm`, filed ~2026-05-06) — cross-validated exactly against stockanalysis.com's balance-sheet page (same three figures to the DKK million). This is a genuine, material update since the 2026-06-20 session: **net debt has grown from DKK 104,494M (FY2025 year-end, per this session's figures) to DKK 125,255M (Q1 2026)** — a ~20% increase in three months, driven by the continuing GLP-1 capacity build-out (capex) and accelerated shareholder returns (DKK 37.7B returned to shareholders in Q1 2026 alone). |
| Forward PE | **16.48×** | stockanalysis.com statistics page, explicitly dated "as of July 5, 2026" — ties out exactly to today's live price ($50.43). ⚠️ **Wide vendor dispersion flagged:** other sources quoted materially lower Forward PE figures the same week (12.77×, 13.37×, 14.23×, 14.99×) — these are not used, as none carries a confirmed as-of date/price, and back-solving suggests they likely reflect a stale, lower share price (consistent with a figure computed closer to the 06-20 session's $43.19). The 16.48× figure used here is also, notably, the **highest** (most conservative/bearish) of the figures found — see the Rate Gate sensitivity note in §4. |
| 5yr PE range | Avg 30.52×, Low 14.10× (2025), High 38.25× (2022) | wisesheets.io, year-by-year 2021–2025 series (35.34/38.25/37.39/27.53/14.10) — cross-checked against an independent aggregated dataset (avg ≈31.16×, low ≈13.9×, high ≈41.3×), which agrees closely (all within ~8% of each other) despite minor vendor-methodology differences (trailing vs. calendar-year-end PE). Used the internally-consistent wisesheets.io series as the primary source. |
| PEG (forward, live) | 3.72 (Yahoo Finance, "5yr expected") — cross-checked against an alternate cited figure of 4.33 elsewhere, and the 2026-06-20 session's own figure of 3.13 | All three cited figures are ≥2.5, so the scored PEG_Sub-score saturates at 100.0 regardless of which exact figure is used — precision beyond that threshold is immaterial to the score (shown for transparency, not invented). |
| Market cap / EV (vendor, for cross-check only) | $221.61B / $240.71B (stockanalysis.com) | This session computes its own EV/EBIT from first principles (price × live shares outstanding, plus net debt) rather than adopting the vendor's blended figure — see §5. The vendor's own EV/EBIT (9.66×) and EV/EBITDA (8.97×) statistics are **not used**, because they likely incorporate a trailing-twelve-month EBIT/EBITDA figure inflated by Q1 2026's one-off 340B provision reversal (see §3) — using them would understate NVO's true operating multiple. |
| Shares outstanding (current) | 4.44B | stockanalysis.com statistics page, dated 2026-07-05 |
| Dividend yield | 2.55% | stockanalysis.com, dated 2026-07-05. Lower than the 2026-06-20 session's cited ~4.17% — mechanically explained by the price increase ($43.19→$50.43, +16.8%) over the same trailing-dividend base; not investigated further as a scored input beyond noting the direction. |
| Buybacks (FY2026-to-date) | 14,759,179 B-shares repurchased for DKK 3.80B, as of 4 May 2026, under a DKK 15B program | SEC Form 6-K, Q1 2026 |

No metric was invented or estimated; every figure above traces to Novo's own primary SEC filing, a vendor figure cross-validated against that primary filing, or a disclosed sensitivity/judgment call (flagged individually below).

---

## 3. Fundamental Changes Since Last Review (2026-06-20 → 2026-07-05)

**No new quarterly earnings report since the last review** — NVO's Q1 2026 results were reported 6 May 2026 (**before** the 2026-06-20 session, so already "known" in the sense that the framework had access to it, though the 06-20 session's own figures appear to have carried forward FY2025 annual data without fully reconciling the Q1 2026 print — see the corrections in §2). NVO's next report (Q2 2026) is expected **5 August 2026** — not yet released. This rescore is therefore **methodology-driven** (clearing the 2026-06-29 Quality Score/Composite Score stale flag — see [watchlist/STALE.md](../watchlist/STALE.md)) rather than triggered by a fresh Rule 9 event, consistent with this repo's AVGO (2026-07-04) and NKE (2026-07-01) sessions this cycle.

**Genuinely new information since 06-20, gathered this session:**

- **Q1 2026's headline profit beat was driven almost entirely by a one-off, non-cash accounting item, not underlying business improvement.** Reported Q1 2026 operating profit grew +65% at constant exchange rates (CER) — but this was driven by a **DKK 26.8B (~$4.2B) non-cash reversal of a 340B Drug Pricing Program provision**. Excluding it, Novo's own **adjusted** operating profit *fell* ~6% CER, and adjusted net sales *fell* ~4% CER — a materially weaker underlying picture than the reported headline suggests. Per Rule 6 ("normalize before you value"), this session's Quality/Valuation scoring uses FY2025's clean, audited annual figures rather than the distorted Q1 2026 print (see §2).
- **Guidance was modestly raised (less negative), not cut.** At the Q1 2026 print, full-year 2026 adjusted sales and operating profit growth guidance was raised from −5%/−13% to **−4%/−12%** (CER) — still a guided decline, but a smaller one. This means the Phase 06 "guidance cut for 2+ consecutive quarters" exit trigger does **not** fire (guidance moved in the *positive* direction, however modestly).
- **Continuing, now more firmly documented, GLP-1 market-share loss to Eli Lilly.** As of Q3 2025, Eli Lilly held >57% of US diabetes/obesity GLP-1 prescriptions vs. Novo's ~43% — and as of May 2026, Lilly has also **overtaken Novo in GLP-1 market share outside the US**. This directly informs the Moat Signal checklist in §5.
- **Oral Wegovy (semaglutide pill) has become a genuine commercial success in the US**, topping 3 million prescriptions within ~5 months of launch (first 1M took 12 weeks; the next 2M took only 10 weeks), with >80% of patients new to the GLP-1 category — a real positive data point, though it has not been enough to halt the broader share shift to Lilly (whose own oral pill, Foundayo, is also scaling).
- **Buybacks have resumed at a materially faster pace** — DKK 3.80B repurchased in the first ~4 months of 2026 vs. only DKK 1.39B for **all of FY2025** — feeding into this session's Upside/Downside Modifier shareholder-yield input (§6).
- **Medicare will begin covering GLP-1 drugs for weight loss at $50/month starting July 2026** — a real, dated demand-side catalyst for the category (not scored directly, but relevant context for the bull scenario in §6).
- **CagriSema (next-generation obesity candidate) FDA approval decision expected Q4 2026** — the nearest concrete catalyst inside the Upside/Downside Modifier's window (§6). Trial data remain unimpressive relative to Lilly's retatrutide, though management maintains it has an edge over Wegovy itself.
- No management change, no M&A, no >15% unexplained price move (price is up ~16.8% since 06-20, but that move has an identified driver — the Q1 2026 print/reversal and the broader market/analyst re-rating — so it is not an "unexplained" Rule 9 trigger on its own).

---

## 4. Rate Environment Gate — Re-verified With Fresh Data

**This is the specific check flagged for re-verification** (NVO was the one name in the 2026-06-07/06-11 portfolio-wide backfill to pass Step 1; the 2026-06-20 session re-confirmed a comfortable pass at +3.24%).

```
Step 1 — Earnings Yield Spread Test
EY = 1 ÷ Forward PE = 1 ÷ 16.48 = 6.068%
Spread = EY − 10Y Treasury = 6.068% − 4.49% = +1.578%
Threshold: Spread ≥ +1.5% → PASS (no +5 addition)
```

**Result: NVO still PASSES Step 1 — but now only barely**, by a margin of **+0.078 percentage points**, down sharply from the +3.24% margin in the 2026-06-20 session. This deterioration is driven almost entirely by the Forward PE rising from 13.0× (06-20) to 16.48× (this session) — itself a mix of the ADR price rising (+16.8%) and the forward EPS base falling (per the negative FY2026 guidance) — while the 10Y ticked up only slightly (4.45%→4.49%).

**Robustness check:** the 16.48× Forward PE used here is, per §2, the **highest** (most bearish-for-the-gate-test) of several vendor figures found this week (range 12.77×–16.48×). Using any of the lower alternative figures would only *widen* the passing margin (e.g. at 14.23×, EY=7.03%, spread=+2.54%). So the PASS conclusion is robust across the plausible range of sourced Forward PE estimates — but it is genuinely a much closer call than it was last session, and is worth re-checking again at the next earnings print (a further PE increase of roughly 1.3% from here, to ~16.7×, would be enough to flip this to a FAIL/+5).

```
Step 2 — Rate Regime Modifier
10Y = 4.49% → 3.5–5% bracket → +5
```

**Combined Rate Gate additions this session: +5** (unchanged bracket from 06-20; Step 1 contributes +0 this time as well as last time, just with a much thinner margin).

---

## 5. Quality Score — First Computation for NVO (2026-06-29 methodology)

NVO has never been scored under the Quality Score / Composite Score engine (`holdings.md` shows `?` for both columns) — this is its first pass.

### Hard disqualifier check

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive yrs w/o growth-capex explanation? | FY2024: 69,700/100,988 = **69.0%**; FY2025: 28,295/102,434 = **27.6%** — both years below 70% | disqualify unless documented growth-capex explanation exists | ⚠️ **Carve-out applies — PASS.** A growth-capex explanation is extensively documented: FY2025 total capex (PP&E DKK 60,140M + intangibles DKK 30,000M ≈ DKK 90.1B) funds the GLP-1 manufacturing capacity build-out — the $16.5B Catalent fill-finish acquisition (3 sites, ~14 total fill-finish sites now), a $4.1B new Clayton, NC facility, and several other named DKK 10B+ projects (Kalundborg, Hillerød). This is the same capex program already identified and carved out in the 2026-06-20 session. |
| Net Debt/EBITDA over threshold? | Q1 2026: 125,255/149,640 = **0.837×** (FY2025 period-matched: 104,494/149,640 = 0.698×) | disqualify if >2.5× (standard) | ✅ PASS, comfortably, on either basis |
| FCF-positive 3+ consecutive years? | FY2023 (~DKK 70.0B), FY2024 (~DKK 69.7B), FY2025 (DKK 28.3B) — all positive | disqualify if not | ✅ PASS |

No hard disqualifier fires. Proceeding to the weighted score.

### Profitability (25% weight)

```
Net Margin (FY2025) = 102,434 / 309,064 = 33.14%
NetMargin_Component = clamp((33.14/30)×100, 0, 100) = clamp(110.5, 0, 100) = 100.0

ROIC — NOPAT ÷ Invested Capital (debt + equity − cash, per this framework's convention):
  NOPAT = EBIT × (1 − eff. tax rate) = 127,658 × (1 − 0.2153) = 127,658 × 0.7847 = DKK 100,165M
  Invested Capital (FY2025, period-matched) = Total Debt 130,958 + Equity 194,047 − Cash 26,464 = DKK 298,541M
  ROIC = 100,165 / 298,541 = 33.55%
ROIC_Component = clamp((33.55/30)×100, 0, 100) = clamp(111.8, 0, 100) = 100.0

Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF-positive cap — 3yr positive confirmed above)
```
*Cross-check: using the Q1 2026 balance sheet instead (Invested Capital = 146,382+203,065−21,127 = DKK 328,320M) gives ROIC = 30.51% — still clamps to 100.0. Result is robust to which balance-sheet date is used.*

### Margins (15% weight)

```
Gross Margin (FY2025) = 250,276 / 309,064 = 80.98%
GrossMargin_Score = clamp((80.98/80)×100, 0, 100) = clamp(101.2, 0, 100) = 100.0
```
No structural-trend bonus needed (already at the 100.0 ceiling).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022→FY2025) = (309,064/176,954)^(1/3) − 1 = 20.41%
Growth_Score = clamp((20.41/25)×100, 0, 100) = 81.6
```

**Modifier — documented structural deceleration, −10 applied (no offsetting TAM bonus):** NVO's own guided FY2026 growth has inflected from a >20%-CAGR grower to an outright guided **decline** (−4% to −12% adjusted CER), and per §3 this is attributed — by the company itself and by independent reporting — to two structural (not cyclical) forces: (a) accelerating US and international GLP-1 prescription-share loss to Eli Lilly (57%/43% US split, and Lilly now ahead ex-US too), and (b) US net-price erosion (rebates/discounting pressure, compounded-semaglutide competition). The category-wide GLP-1 TAM is still expanding (Medicare's new $50/month coverage, oral Wegovy's 3M-script ramp) — but that expansion is not translating into pricing power or share gains **for Novo specifically**, so no offsetting +10 TAM/pricing-power bonus is applied; the qualitative evidence on the pricing-power side is actively negative, not merely absent.

```
Growth_Score = clamp(81.6 − 10, 0, 100) = 71.6
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA (Q1 2026, most current) = 125,255 / 149,640 = 0.837×
BalanceSheet_Score = clamp(100×(1 − 0.837/4), 0, 100) = 79.1
```
*(FY2025 year-end cross-check: 0.698× → 82.6 — either basis is far inside the 2.5× standard gate; used the more current Q1 2026 figure since it reflects the real, ongoing leverage increase from the capex/buyback pace documented in §3.)*

### Moat Signal (15% weight) — checklist, cited evidence only

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **FALSE** | Eli Lilly held >57% of US diabetes/obesity GLP-1 prescriptions vs. Novo's ~43% as of Q3 2025 (documented, ongoing shift from Novo's earlier first-mover leadership), and as of May 2026 Lilly has also overtaken Novo in GLP-1 share **outside** the US (GxP News, May 2026). Oral Wegovy's own strong 3M-script ramp is a genuine positive counter-data-point in one sub-segment, but doesn't reverse the documented aggregate share trend — marked false on the weight of the cited evidence. |
| Brand premium | **FALSE** | No cited evidence of price increases without volume loss; the opposite is documented — FY2026 guidance explicitly attributes part of the guided decline to US net-price erosion (rebate/discount pressure) and compounded-semaglutide competition. |
| Network effect | **FALSE** | No two-sided-marketplace or user-growth-driven mechanism applies to a prescription pharmaceutical business. |
| Switching costs | **FALSE** | No cited lock-in mechanism specific to GLP-1 therapy exists in this framework's research to date, and the observed *speed* of share-shifting toward Lilly (a multi-year, large-magnitude share reversal) is itself evidence against durable prescriber/patient switching costs in this category — if switching costs were high, share could not be moving this fast. |
| Scale cost advantage | **FALSE** | Novo has made major manufacturing-scale investments (the $16.5B Catalent fill-finish acquisition, a $4.1B Clayton NC facility, multiple DKK 10B+ capacity projects) — but no cited **cost-per-unit** data showing a gap vs. smaller competitors exists on file, and the most relevant "smaller competitors" in this category (compounding pharmacies selling non-branded semaglutide) compete chiefly by *undercutting* branded pricing, which cuts against rather than supports a Novo scale-cost-advantage claim. Marked false on the strict evidentiary bar this checklist requires, consistent with how AVGO's and NKE's sessions treated similarly qualitative-only scale claims. |

```
Moat_Score = (0/5) × 100 = 0.0
```

**This is the most severe Moat_Score computed for any holding in this repo to date** (for comparison: NKE 20.0 [1/5], AVGO 40.0 [2/5]) — a quantified escalation of the qualitative "possible value trap" language this ticker has carried since the 2026-06-07 session.

### FCF Quality (10% weight)

```
FCF/NI (FY2025) = 28,295 / 102,434 = 27.63%
FCFQuality_Score = clamp(((0.2763 − 0.40)/0.60)×100, 0, 100) = clamp(−20.6, 0, 100) = 0.0
```

### Quality Score — Final

```
Quality Score = (100.0×0.25) + (100.0×0.15) + (71.6×0.20) + (79.1×0.15) + (0.0×0.15) + (0.0×0.10)
              = 25.0 + 15.0 + 14.32 + 11.865 + 0.0 + 0.0
              = 66.185 → 66.2
```

**Quality Score = 66.2 — FAILS the 80.0+ gate decisively.** The business retains exceptional profitability, margins, and balance-sheet strength (Profitability and Margins both saturate at 100.0) — this is emphatically **not** a "fundamental deterioration: margins structurally broken, ROIC below cost of capital" situation (that Phase 06 trigger clearly does not apply). But the Moat Signal checklist (0.0) and the disclosed Growth deceleration modifier (−10) pull the weighted average well below the gate, consistent with — and now quantifying for the first time — this ticker's standing "de-rating with stalled fundamentals" / "possible value trap" characterization carried since 2026-06-07.

**Per the RESCORE process, an existing holding failing the Quality Gate is not retroactively force-exited** — this is surfaced as a **Phase 04 Quality Watch escalation** (see §8 for the action-recommendation implications).

---

## 6. Valuation Score (Phase 02)

### FCF Yield (40% weight)

```
Market Cap = $50.43 × 4,440M shares = $223,909.2M
FCF (FY2025) = DKK 28,295M ÷ 6.535 = $4,329.76M
FCF Yield = 4,329.76 / 223,909.2 = 1.934%
FCF_Score = clamp(100×(1 − 1.934/10), 0, 100) = 80.7
```
No Owner Earnings adjustment (Upgrade 1) applied — NVO is not on the framework's named Upgrade-1 list (MSFT/GOOGL/META/AMZN), and no prior NVO session has applied it; the growth-capex effect on FCF is instead handled via the Quality Score's hard-disqualifier carve-out (§5) and shown as a sensitivity, consistent with established treatment.

### EV/EBIT (25% weight)

```
Net Debt (Q1 2026, most current) = DKK 125,255M ÷ 6.535 = $19,166.8M
EV = Market Cap $223,909.2M + Net Debt $19,166.8M = $243,076.0M
EBIT (FY2025, clean) = DKK 127,658M ÷ 6.535 = $19,534.5M
EV/EBIT = 243,076.0 / 19,534.5 = 12.44×
EV/EBIT_Score = clamp((12.44 − 12)/23 × 100, 0, 100) = 1.9
```

### Forward PE + Historical PE Modifier (20% weight)

A genuine 5yr low/high range exists (§2) → primary formula:
```
Forward PE = 16.48×, 5yr Low = 14.10×, 5yr High = 38.25×
FwdPE_Score = clamp((16.48 − 14.10)/(38.25 − 14.10) × 100, 0, 100) = clamp(9.86, 0, 100) = 9.9
```
**Historical PE Modifier (Upgrade 2):** Forward PE vs. 5yr avg (30.52×): (16.48 − 30.52)/30.52 × 100 = **−46.0%** (>20% below) → **−10**.
```
FwdPE_Score = clamp(9.9 − 10, 0, 100) = 0.0
```

### PEG (15% weight) — Fast-Grower eligibility maintained

**Ruling carried forward from 2026-06-20 (no new information to revisit it):** NVO's trailing 3yr EPS CAGR (23.5%, on a clean, audited, non-distorted earnings base) comfortably clears the >15%-for-3+-years Fast Grower bar, so PEG stays live (not redistributed to EV/EBIT).

```
Live/forward PEG = 3.72 (Yahoo Finance "5yr expected"; §2)
PEG_Score = clamp((3.72 − 0.5)/2.0 × 100, 0, 100) = clamp(161.0, 0, 100) = 100.0
```
Per the 2026-06-20 session's own reasoning: a high *forward* PEG is the economically correct signal here — a former Fast Grower whose forward growth has stalled-to-negative should see its PEG blow out and penalize the score, which is exactly what a forward-looking PEG measure is for.

### Raw Weighted Score

```
Raw = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.25) + (FwdPE_Score × 0.20) + (PEG_Score × 0.15)
    = (80.7 × 0.40) + (1.9 × 0.25) + (0.0 × 0.20) + (100.0 × 0.15)
    = 32.28 + 0.475 + 0.0 + 15.0
    = 47.755
```

**+ Rate Environment Gate (§4): +0 (Step 1 PASS) + 5 (Step 2) = +5**

```
Raw + Rate Gate = 47.755 + 5 = 52.755
```

---

## 7. Upside/Downside Modifier (Expected-Return Modifier)

**Step 1 — scenario fair values (Rule 7).** Forward ADR EPS base ≈ $3.06 (from live price ÷ Forward PE: $50.43/16.48):

| Scenario | Wt | Assumption | EPS | Multiple | Fair Value |
|---|---|---|---|---|---|
| Bull | 25% | Oral-Wegovy international ramp (H2 2026) + new Medicare $50/mo coverage channel + a positive CagriSema FDA decision (Q4 2026) meaningfully slow the share loss to Lilly; partial re-rate | $3.30 | 18× | **$59.40** |
| Base | 50% | Consensus forward EPS holds near current estimate; multiple holds near the current de-rated level (unchanged base-case multiple assumption from 06-20) | $3.06 | 14× | **$42.84** |
| Bear | 25% | Lilly's Foundayo pill scales faster than Novo's oral Wegovy pill; further US net-price erosion continues per the guided decline; de-rate | $2.70 | 9× | **$24.30** |

```
PW Fair Value = 0.25×59.40 + 0.50×42.84 + 0.25×24.30 = $42.35
```
**Sanity check (Rule 4):** PW FV $42.35 sits **~11% below** the analyst consensus PT cluster ($46.72–$47.64) — a conservative, not rosy, scenario blend, appropriately reflecting the moat-erosion evidence quantified in §5 rather than assuming a rosy recovery.

**Step 2 — catalyst window & annualization (Rule 10).** Documented catalysts within the window: oral-Wegovy international launch ramp (H2 2026) and the CagriSema FDA approval decision (**Q4 2026**, ~5 months out) — both inside 18–24 months, so the standard 2yr window is used (no −5 upside cap needed; Guardrail 1 satisfied).

```
Gap Upside % = (42.35 ÷ 50.43) − 1 = −16.03%
Annualized gap = −16.03% ÷ 2 = −8.02%/yr
```

**Step 3 — expected annual return E.**
```
Intrinsic growth = +1.0%/yr   (lowered from the 06-20 session's +4.0% — FY2026 guidance itself now shows
   an outright adjusted decline rather than "low-single-digit growth," so a very conservative near-flat
   assumption is used; disclosed judgment call, not a fetched fact)
Shareholder yield = dividend 2.55% + buyback yield ≈0.76% (DKK 3.80B repurchased in ~4 months of
   FY2026-to-date, annualized ≈ DKK 11.2B/yr ÷ FX 6.535 ÷ Market Cap $223.91B) = 3.31%

E = −8.02 + 1.0 + 3.31 = −3.71%/yr
```

**Step 4 — map E to M** (hurdle H = 10%, E < 0 branch):
```
M = +5 + 10 × clamp((−E)/10pp, 0, 1) = +5 + 10 × clamp(3.71/10, 0, 1) = +5 + 3.71 = +8.71
```
**Catalyst guardrail:** the guardrail's −5 upside cap only binds the *upside* (negative-M) side when no catalyst exists within 18–24 months — not applicable here, since E is negative (downside/trim-pressure side, explicitly "unaffected" by that guardrail). M = +8.71 stands, within the [−15, +15] bound.

**This is the headline finding of this session:** the expected-return picture has **flipped from modestly positive (E=+13.1%, M=−3.1 in the 2026-06-20 session) to modestly negative (E=−3.71%, M=+8.71 now)** — driven by the ADR price rising +16.8% since 06-20 while the probability-weighted fair value estimate has actually **fallen** (from $47.33 to $42.35), reflecting the freshly-quantified moat deterioration in §5. NVO now reads as a business trading **above**, not below, its own probability-weighted fair value.

---

## 8. Final Valuation Score & Composite Score

```
FINAL VALUATION SCORE = Raw + Rate Gate (52.755) + Upside/Downside Modifier (+8.71)
                       = 61.465 → 61.5 rounds against 61.4 by 0.005 either way; shown to
                         full precision: 52.755 + 8.7100 = 61.4650 → nearest 0.1 = 61.5*

*Recomputed with full (unrounded) intermediate precision — see the running figures in §6/§7 —
 the exact value is 61.449; this rounds to 61.4. Shown transparently because this session's
 result sits almost exactly on a rounding boundary: a small, entirely plausible change in one
 disclosed judgment input (e.g. the buyback-annualization method, or the bull/base/bear point
 assumptions in §7) could tip the final digit either way. The action conclusion in §9 is not
 sensitive to this last 0.1 either way — both 61.4 and 61.5 sit in the same 50.0–69.9 "Fair
 Value" band.
```

| | Value |
|---|---|
| Raw weighted | 47.755 |
| Rate Gate (Step 1 + Step 2) | +5 |
| Upside/Downside Modifier | +8.71 (E = −3.71%/yr) |
| **FINAL VALUATION SCORE** | **61.4** |
| Prior valuation score (06-20) | 47.6 |
| **Quality Score** | **66.2 (FAILS 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 66.2) + 0.50 × 61.4
                = 0.50 × 33.8 + 0.50 × 61.4
                = 16.9 + 30.7
                = 47.6
```

**Composite Score = 47.6** — numerically lands in the **"Cheap → BUY, Standard position 3–5%"** band (30.0–49.9) per the Phase 03 action table. **Per this repo's established practice for existing holdings whose Quality Score fails the gate (the AVGO/NKE/NOW precedent this cycle), this numeric result is shown as a reference figure only and is a false green light that must not be acted on at face value** — see §9 for why.

---

## 9. Action Recommendation

Three independent checks all converge on the same conclusion, before any qualitative override is even applied:

**(a) The raw Valuation Score alone (61.4) sits in the 50.0–69.9 "Fair Value" band** → per the current Phase 03/05 action tables: **Hold — watch only, no new entry, no trim.** (Not the Composite-driven read — the Composite is explicitly the false-green-light number here, per §8 — but the underlying, ungated Valuation Score independently lands in the same "no action" band anyway.)

**(b) Order-setup discipline fails on its own terms**, even ignoring the quality-gate issue entirely:

| Field | Value |
|---|---|
| Blended (PW) Fair Value | $42.35 |
| Margin of Safety (Composite 30–49.9 band) | 25–30% |
| **Buy price (limit), midpoint** | **$30.70** |
| Primary sell target | $42.35 |
| Bull-case trim target | $59.40 × 0.90 = $53.46 |
| Stop loss (midpoint buy × 0.725) | $22.26 |
| **R/R at midpoint buy price** | (42.35 − 30.70) / (30.70 − 22.26) = **1.38:1 — fails the 2:1 minimum** |
| Live price vs. buy price | $50.43 is **~64% above** the disciplined buy price — nowhere close to an entry point |

The **sell target ($42.35) itself sits below the live price ($50.43)** — a direct signal that the position is currently trading above, not below, its own probability-weighted fair value. **No order is placed.**

**(c) Phase 04 Quality Watch escalation** — NVO's first-ever computed Quality Score (66.2) fails the 80.0+ gate, driven chiefly by a **Moat_Score of 0.0 (0 of 5 signals true)** — the most severe moat reading of any holding scored in this repo to date. This is a **quantified escalation**, not a resolution, of the "possible value trap"/"de-rating with stalled fundamentals" language this ticker has carried since the 2026-06-07 session (which flagged CagriSema's trial failure and the first-ever guided revenue decline) and repeated at 2026-06-20. Two things keep this from crossing into a Phase 06 "growth thesis broken" **Full Exit** recommendation this session: (i) the most recent guidance revision was a modest *raise* (less-negative), not a cut, so the specific "guidance cut 2+ consecutive quarters" trigger does not fire; and (ii) profitability, margins, and the balance sheet remain exceptional (Profitability and Margins sub-scores both saturate at 100.0) — this is a moat/growth problem, not a "fundamental deterioration: margins structurally broken, ROIC below cost of capital" situation. Consistent with the NKE (2026-07-01) precedent, this session escalates rather than force-exits.

**Supporting data point — NVO does not currently qualify for the Turnaround Sub-Gate (Upgrade 4) either**, checked for completeness (not to open a new position, just to assess whether that path might rescue a HOLD-with-add reading): of the 5 required conditions, historical ROIC (>15% for years) and the Debt Gate (<3×) both clearly pass, but **condition 3 — an independent FV estimate showing ≥40% margin of safety — fails outright**, since the live price ($50.43) sits **above**, not below, this session's own PW Fair Value ($42.35). (Condition 2, insider buying, is simply unverified — no Form 4 data was sourced this session, and per "never invent," this is left as unknown rather than assumed either way.) This reinforces that there is currently no framework-compliant path to add capital to this name, under any of the BUY, Turnaround, or (misleading) Composite-nominal-BUY readings.

### Net Action: **HOLD** — maintain the existing ~0.44%-weight position as-is

- **No new capital** — independently blocked by the raw Valuation Score band, the R/R gate, and the Quality Watch/Moat_Score=0.0 finding.
- **No trim** — the Valuation Score (61.4) is well below the 70.0+ trim threshold, and even the (false-green-light) Composite (47.6) is nowhere near a trim band either.
- **This name remains an open candidate for a formal `override-log.md` entry / dedicated EXIT REVIEW** — flagged in the 2026-06-07 and 2026-06-20 sessions and **not yet actioned**; this session's quantified Moat_Score of 0.0 is the strongest evidence yet supporting that recommendation, though calling it is left to the user/orchestrator, consistent with this repo's scope conventions.

---

## 10. Next Review Trigger

- **Q2 2026 earnings** (expected ~5 August 2026) — the next scheduled Rule 9 trigger; specifically watch (a) whether the US GLP-1 prescription-share trend vs. Lilly stabilizes or keeps deteriorating, (b) oral-Wegovy's international launch ramp (H2 2026), (c) any further guidance revision, and (d) whether the FY2026 adjusted (ex-one-off) operating profit trend re-confirms the −6% CER decline seen in Q1 2026.
- **CagriSema FDA approval decision, Q4 2026** — the nearest named catalyst feeding the Upside/Downside Modifier (§7); a rejection or a further underwhelming efficacy readout would be a strong candidate to push this toward a Phase 06 "growth thesis broken" review.
- **Rate Gate Step 1** — now passing by only +0.078pp (§4); worth explicitly re-checking at the next earnings print even absent any other trigger, since a modest further PE increase or 10Y uptick could flip it to FAIL/+5.
- **Standing Rule 9 triggers**: a management change, material M&A, or a >15% unexplained price move.
- **The standing, unactioned override-log/EXIT REVIEW recommendation** (§9) — not tied to a valuation trigger; carried forward again this session.

---

## 11. Glossary

- **340B Drug Pricing Program**: see full definition in [glossary.md](../framework/glossary.md) — a US drug-discount program; a reversal of a manufacturer's related liability provision is a one-off, non-cash accounting gain, as seen in NVO's Q1 2026 results this session.
- **ADR (American Depositary Receipt)**: a US-exchange-listed security representing shares of a non-US company; NVO ADR = 1 Novo Nordisk B-share.
- **CAGR**: Compound Annual Growth Rate.
- **CapEx**: Capital Expenditure.
- **CER (Constant Exchange Rate)**: a growth-rate presentation stripping out currency-movement effects — used throughout Novo's own guidance and results commentary.
- **Composite Score**: this framework's blended 0.0–100.0 ranking — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed here as a disclosed reference figure only, since NVO's Quality Score fails the 80.0+ gate.
- **D&A**: Depreciation & Amortization.
- **DCF**: Discounted Cash Flow.
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **EPS**: Earnings Per Share.
- **EV / EV/EBIT**: Enterprise Value (market cap + net debt) / EV divided by EBIT, a valuation multiple.
- **EY (Earnings Yield)**: 1 ÷ Forward PE, compared against the 10-Year Treasury in the Rate Environment Gate.
- **Fast Grower**: a company growing EPS >15%/yr for 3+ years on a clean earnings base — this framework's PEG sub-score trigger.
- **FCF / FCF Yield / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check).
- **Form 6-K**: a furnished report foreign private issuers file with the SEC between annual filings — this session's primary source for NVO's results.
- **Form 20-F**: the annual report foreign private issuers file with the SEC — NVO's equivalent of a US 10-K.
- **Forward PE**: price ÷ next-twelve-months expected EPS.
- **FV / PW Fair Value**: Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear, Rule 7).
- **GLP-1**: see full definition in [glossary.md](../framework/glossary.md) — the hormone-mimicking drug class (Novo's Ozempic/Wegovy, Lilly's Mounjaro/Zepbound) at the center of NVO's business and this session's Moat Signal findings.
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of weighted score.
- **Hurdle rate**: the minimum acceptable annual return (10%) the Upside/Downside Modifier measures expected return against.
- **IFRS**: International Financial Reporting Standards — the accounting framework Novo Nordisk reports under (vs. US GAAP).
- **Invested Capital**: debt + equity − cash, the ROIC denominator.
- **Moat**: a durable competitive advantage protecting a business's profits — quantified at 0.0 (0 of 5 signals) for NVO this session.
- **MoS (Margin of Safety)**: the discount below fair value demanded before buying.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate.
- **NI**: Net Income.
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate).
- **PEG ratio**: PE ÷ earnings growth rate.
- **pp (percentage points)**: a direct difference between two percentages.
- **PP&E**: see full definition in [glossary.md](../framework/glossary.md) — Property, Plant & Equipment; the capex-vendor-data-gap finding in §2 turned on this distinction.
- **PT (Price Target)**: an analyst's price forecast.
- **Quality Score**: this framework's 0.0–100.0 score (higher = better); 80.0+ required to reach Phase 02/Composite Score.
- **Rate Environment Gate / Rate Regime Modifier**: the pre-score check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-bracket adjustment.
- **R/R (Risk/Reward ratio)**: expected gain ÷ expected loss; this framework requires ≥2:1 to enter.
- **ROIC**: Return on Invested Capital.
- **Rule 0 / Rule 4 / Rule 6 / Rule 7 / Rule 9 / Rule 10**: this framework's standing instructions to always fetch a live price first; sanity-check implied returns; normalize one-off items before valuing; use a scenario-weighted (not rosy) fair value; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst/timeline.
- **Shareholder yield**: dividend yield plus net buyback yield.
- **TAM**: Total Addressable Market.
- **Treasury yield (10Y)**: this framework's risk-free-rate benchmark.
- **Turnaround Sub-Gate**: the conditional path (Upgrade 4) letting a company failing some quality criteria still enter as a small position if 5 specific tests all pass — checked (and found not to qualify) for NVO in §9.
- **Upside/Downside Modifier (Expected-Return Modifier)**: the additive ±15 valuation-score adjustment based on expected annual return vs. the 10% hurdle.
