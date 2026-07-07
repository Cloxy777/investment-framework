# NEW POSITION — Deutsche Börse AG (DB1.DE) — 2026-07-07 (full re-evaluation)

**Task type:** NEW POSITION — full re-evaluation (methodology version 2026-06-29)
**Date:** 7 Jul 2026
**10Y US Treasury yield:** 4.49% (TradingEconomics, 7 Jul 2026 — same-day figure used across other 2026-07-07 sessions this cycle)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Current DB1 portfolio weight:** 0% — not held (confirmed against [holdings.md](../portfolio/holdings.md))
**Prior session:** [2026-06-19-new-position-db1.md](2026-06-19-new-position-db1.md) — score 47.8, computed **before** both the 2026-06-20 Upside/Downside Modifier change and the 2026-06-29 Quality Score/Composite Score addition. Flagged stale on both counts in [watchlist/STALE.md](../watchlist/STALE.md). Phase 01 was a clean 8/8 PASS.
**Sector:** Germany/EU Market Infrastructure — cash-equities exchange (Xetra), derivatives exchange and clearing (Eurex), post-trade settlement/custody (Clearstream), fund distribution/processing (Fund Services), investment-management software and indices (SimCorp, STOXX, ISS — "Investment Management Solutions" segment)
**Currency:** All calculations in EUR unless stated. Rate Environment Gate benchmarks the **US** 10Y Treasury (framework convention); DCF WACC uses the **German 10Y Bund** as risk-free rate for currency-consistent valuation of EUR cash flows.

**Why this is a full re-evaluation, not an addendum:** DB1 already cleared Phase 01 with a real Phase 02 score, so per this task's scope this session re-verifies Phase 01 with fresh data, computes the full Quality Score (first-ever for this ticker), recomputes the full Valuation Score under the current methodology (5yr PE lookback + Upside/Downside Modifier), and computes the Composite Score.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **EUR 259.70** | Google Finance direct quote, timestamped "July 7, 8:33:53 PM GMT+2" (today), cross-checked against an independent stockanalysis.com fetch taken minutes earlier in the same session — both returned **EUR 259.70** exactly |
| Previous close | EUR 254.20 | Google Finance |
| Intraday range | EUR 255.30 – 259.90 | Google Finance |
| 52-week range | EUR 200.10 – 276.00 | stockanalysis.com |
| Shares outstanding | 182.11M | stockanalysis.com — consistent with the 06-19 session's yfinance-sourced 182,105,935 |
| Market cap (computed) | **EUR 47,294.0M** | 182.11M × €259.70 (self-computed; stockanalysis.com's own displayed figure, €46.29B, does not reconcile exactly against its own displayed price/share count — flagged as a vendor internal-consistency gap, self-computed figure used as primary) |
| Beta (raw, DB1 own) | 0.30 | stockanalysis.com — structurally low, same pattern as 06-19 (0.28), not used directly for WACC (see §7) |
| Analyst consensus PT (12-month) | ~EUR 280–291 range; **EUR 285.67** (12 analysts) used as primary | stockanalysis.com (285.67, 12 analysts — same analyst count as 06-19); cross-checked against TipRanks (286.00 avg / 291.40 "consensus" / 240–310 range, 8 buy + 3 hold) and eToro (280.25) — all in a tight band, "Buy"/"Moderate Buy" rating across sources |
| EUR/USD | 1.1425 | WebSearch (multiple sources converged 1.1424–1.1440, 7 Jul 2026) |
| GBP/USD | 1.3388 | WebSearch, 7 Jul 2026 (for LSEG peer-comp currency conversion) |
| German 10Y Bund | 2.94% | WebSearch (7 Jul 2026), used as DCF risk-free rate |

**yfinance was attempted first and failed** with a `curl_cffi` TLS `Connection reset by peer` on every call — a hard network-level failure, not a transient rate-limit (same failure mode independently seen in this cycle's CVX session). Per the task's explicit fallback instruction, this entire session is sourced from WebSearch/WebFetch instead: Deutsche Börse's own primary-source company releases (FY2025 preliminary results, Q1/2026 quarterly statement, "Company Figures" IR page, outstanding-bonds IR page) wherever possible, with third-party data vendors (stockanalysis.com, marketscreener.com, wisesheets.io) cross-validated against each other and, where possible, against the company's own disclosures.

---

## 2. Data Gathered & Data Gaps Flagged

### Income statement — primary source (Deutsche Börse's own FY2025 preliminary-results release and Q1/2026 quarterly statement)

| € million | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 | Q1/2025 | Q1/2026 | **TTM (Q2'25–Q1'26)** |
|---|---|---|---|---|---|---|---|---|
| Sales revenue (gross) | — | — | — | 5,972 | 6,543 | 1,636 | 1,821 | **6,728** |
| Net revenue (mgmt's key metric) | 3,510 | 4,338 | 5,077 | 5,829 | 6,026 | 1,507 | 1,638 | **6,157** |
| EBITDA | 2,044 | 2,526 | 2,944 | 3,396 | 3,512 | 912 | 1,007 | **3,607** |
| EBIT | 1,750 | 2,170 | 2,525 | 2,900 | 3,010 | 787 | 877 | **3,100** |
| Net profit (attributable to DB1 shareholders) | 1,210 | 1,494 | 1,724 | 1,948/1,949* | 1,995 | 525 | 585 | **2,055** |
| Income tax expense | — | — | — | — | 753 | 196 | 224 | **781** |
| Earnings before tax (EBT) | — | — | — | — | 2,857 | 748 | 838 | **2,947** |
| Basic EPS (€) | — | — | 9.35 | 10.60 | 10.90 | 2.86 | 3.21 | — |

*Sources: [Company Figures](https://www.deutsche-boerse.com/dbg-en/media/group-at-a-glance/media-company-figures) (5yr Net Revenue/EBITDA/EBIT/Net Profit series); [FY2025 preliminary results release](https://www.deutsche-boerse.com/resource/blob/4887536/a68752b1b7c85f9cf530531c0c221dc4/data/company-release-q4-2025-en.pdf), 11 Feb 2026; [Q1/2026 quarterly statement](https://www.deutsche-boerse.com/resource/blob/5053028/5524b27e0d1ea96ed562d1b6dedd7465/data/gdb-quarterly-statement-q1-2026_en.pdf), 27 Apr 2026. TTM = FY2025 − Q1/2025 + Q1/2026, the same reconstruction method verified in valuation-scoring.md's `yfinance` section, applied here to primary-source figures since yfinance itself is unreachable. *Company Figures page's FY2024 net profit (1,948) differs by €1M from the FY2025 release's own FY2024 comparative (1,949) — immaterial rounding, FY2025 release's figure used where both are available.*

**TTM effective tax rate** = 781/2,947 = **26.50%** (computed, not invented — both inputs primary-sourced).

### Balance sheet — primary source, with a genuine, disclosed data-basis judgment call

Deutsche Börse's balance sheet is dominated by CCP-matched-book and client-settlement items (e.g. "financial instruments held by central counterparties," "cash deposits by market participants," "restricted bank balances") that mirror on both the asset and liability side and are **not** the company's own financial leverage — the same CCP-bucket artifact flagged in the 06-19 session. This session sources DB1's **actual gross financial debt directly from its own bonds-outstanding IR page** rather than a balance-sheet "financial liabilities measured at amortized cost" line (€24.3bn at FY2025 year-end per the primary balance-sheet extract) that plainly co-mingles CCP/settlement-related payables with true bond debt — using that gross balance-sheet line would overstate leverage by roughly 4×, an obvious sanity-check failure the framework's Rule 4 exists to catch.

| Field | Value | Source |
|---|---|---|
| **Total gross debt (outstanding bonds)** | **EUR 6,450M** | [DB1 bonds IR page](https://www.deutsche-boerse.com/dbg-en/investor-relations/share-and-bonds/bonds) — 9 listed bonds, €500m–€1.25bn each, maturities 2026–2048, coupons 0.125–3.875%; none have matured as of today (earliest maturity Sept 2026) |
| Weighted-average coupon (computed from the bond list) | **2.640%** | Self-computed, notional-weighted across all 9 bonds |
| After-tax cost of debt | 1.943% | 2.640% × (1 − 26.50%) |
| Cash and cash equivalents | EUR 1,782M | FY2025 year-end (31 Dec 2025) primary balance-sheet extract — "Other cash and bank balances." **No more-current breakout available**: the Q1/2026 balance-sheet extract aggregates "Other current assets" (29,918M) without breaking out cash separately, so FY2025 year-end remains the most current specific cash figure — same limitation as 06-19, flagged as a data gap. |
| **Net Debt (computed)** | **EUR 4,668.0M** | 6,450 − 1,782 |
| Shareholders' equity (excl. non-controlling interests) | EUR 10,494M | Q1/2026 balance sheet (31 Mar 2026), most current available |
| Shareholders' equity (incl. NCI) | EUR 10,882M | Q1/2026 balance sheet |
| Company's own leverage target | Net debt/EBITDA ≤ 2.25× | [DB1 IR "Financial position" page](https://www.deutsche-boerse.com/dbg-en/investor-relations/at-a-glance/aims-and-outlook/financial-position) — corroborates that the company's own binding leverage discipline is measured on a narrow bond-debt basis, not the €24.3bn gross balance-sheet line, supporting this session's methodology choice |
| Credit rating | AA− (S&P), consistent with 06-19 | Not independently re-verified this session (not disputed by any source found) |

### ROIC — computed properly this session (was an ROE proxy in 06-19)

06-19 used ROE (19.21%) as an explicit **proxy** for ROIC because Invested Capital components weren't cleanly available at the time. This session has the components (EBIT, tax rate, debt, equity, cash) and computes actual ROIC per the current `glossary.md`/CVX-session convention (NOPAT ÷ Invested Capital, Invested Capital = Debt + Equity − Cash):

```
NOPAT (TTM) = EBIT × (1 − effective tax rate) = 3,100 × (1 − 0.2650) = EUR 2,278.5M
Invested Capital (excl. NCI) = Debt(6,450) + Equity(10,494) − Cash(1,782) = EUR 15,162.0M
ROIC = 2,278.5 / 15,162.0 = 15.03%
```

**This is a razor-thin pass of the >15% Phase 01 threshold** — a materially different picture than 06-19's comfortable-looking 19.21% ROE proxy. **Sensitivity flagged explicitly:** using Invested Capital *including* NCI equity (15,550.0M, arguably the more internally-consistent basis since EBIT/NOPAT are also fully-consolidated, pre-NCI-split figures) gives ROIC = **14.65% — a marginal FAIL**. This session uses the excl-NCI convention (the more standard ROIC textbook treatment, equity attributable to parent shareholders) as primary, consistent with quality-scoring.md's literal "ROIC (TTM)" input requirement — but this is flagged as a genuine, borderline, methodology-sensitive data point, not a comfortable pass. ROE (19.0–19.2%, cross-validated across two vendors) is shown as a supplementary profitability signal, not used as the primary ROIC input this session (the framework's own quantitative-inputs list asks for ROIC specifically).

### Gross margin, net margin — vendor-sourced (no primary "Gross Profit"/COGS line disclosed)

DB1's own income statement has no "Cost of Revenue"/"Gross Profit" line (same structural fact flagged in 06-19) — an exchange/clearing business doesn't naturally decompose that way. Gross Margin is therefore taken from third-party vendors, cross-validated across three independent sources this session: stockanalysis.com (81.23–81.27%), valueinvesting.io (81.27%, as of 2025-12-31), and a third aggregator (~81.7% TTM) — tightly clustered and consistent with 06-19's yfinance-sourced 81.23%. **Gross Margin used: 81.27%** (still not fully reconciled to a disclosed cost-of-revenue breakdown — same unresolved Data Gap as 06-19, not re-litigated this session since three independent vendors converge closely).

Net Margin (TTM) is computed from primary-source figures this session (Net profit attributable ÷ Net revenue = 2,055/6,157 = **33.38%**) rather than reused from a vendor black-box field. This is **higher** than a cross-checked third-party vendor figure (~28.6% TTM, WebSearch) — the same DB1-specific "which revenue line" ambiguity flagged in 06-19 (Sales revenue vs. Net revenue vs. a vendor's own idiosyncratic "Total Revenue" concept never fully reconciled there either). This session's 33.38% is used as primary since every input is directly traceable to Deutsche Börse's own filed figures; the vendor's lower figure likely nets against a broader revenue base this session could not independently reconstruct. Both comfortably clear the >12% Phase 01 threshold regardless.

### Revenue growth (3yr CAGR) — Net Revenue basis, primary-sourced

```
3yr CAGR = (Net Revenue FY2025 / Net Revenue FY2022)^(1/3) − 1
         = (6,026 / 4,338)^(1/3) − 1 = 11.58%
```
Sourced entirely from the company's own "Company Figures" 5-year table — cleaner provenance than 06-19's yfinance-sourced 12.20% (a different, unreconciled revenue-line basis), though the two figures are close enough (11.58% vs 12.20%) not to be a material discrepancy.

### EPS history (Fast Grower / PEG test) — unchanged from 06-19 (historical facts don't change)

| Year | Basic EPS | YoY growth | >15%? |
|---|---|---|---|
| FY2022 → FY2023 | €8.14 → €9.35 | +14.87% | ❌ No |
| FY2023 → FY2024 | €9.35 → €10.60 | +13.37% | ❌ No |
| FY2024 → FY2025 | €10.60 → €10.90 | +2.83% | ❌ No |

**Not a Fast Grower** — same finding as 06-19. PEG's 15% weight redistributes to EV/EBIT (40% total).

### Forward PE inputs — FY2026E EPS consensus (cross-validated across 3 sources)

| Source | FY2026E EPS |
|---|---|
| stocksguide.com (~20 analysts, high €13.49 / low €11.10) | €12.16 |
| marketscreener.com | **€12.27** (used as primary — independently cross-validated: its FY2026 revenue estimate, €6,460M, and EBITDA estimate, €3,861M, both closely match the company's own FY2026 guidance implied totals — net revenue ~€6.4bn (€5.7bn ex-treasury + ~€0.7bn treasury), EBITDA ~€3.8bn (€3.1bn ex-treasury + ~€0.7bn treasury) — giving confidence this vendor's estimate set is well-grounded in the same guidance this session already relies on) |
| Another aggregator | €12.47 |

**FY2026E EPS used: €12.27.** Forward PE = 259.70 / 12.27 = **21.165×**. Flagged: this is meaningfully sensitive to which consensus figure is used (Forward PE ranges 20.82–21.36× across the three sources) — shown transparently rather than picking silently.

### 5-year historical PE range — **current methodology (5yr lookback, changed 2026-06-20)**, not 06-19's 10yr figure

06-19 predates the 2026-06-20 shortening of the historical-PE lookback from 10yr to 5yr — this is one of the two specific reasons DB1 was flagged stale. Full year-by-year PE table (wisesheets.io, same source as 06-19, refetched):

| Year | PE |
|---|---|
| 2025 | 20.53 |
| 2024 | 20.98 |
| 2023 | 19.77 |
| 2022 | 19.83 |
| 2021 | 22.32 |
| *(2016–2020, no longer used under the 5yr lookback)* | — |

```
5yr Low  = 19.77 (2023)
5yr High = 22.32 (2021)
5yr Avg  = (20.53+20.98+19.77+19.83+22.32)/5 = 20.686
```
Materially narrower than 06-19's 10yr range (11.21–25.60×, avg 20.82×) — the 2016 outlier trough year has rolled out of the window, exactly the kind of methodology-driven change this re-evaluation exists to capture.

### Peer comparables (Rule 5) — refreshed

Same 5 in-band peers as 06-19 (LSEG, ICE, CME, NDAQ, CBOE), each independently fetched (stockanalysis.com quote + ratios pages, 7 Jul 2026):

| Company | EV/EBIT | Forward PE | TTM Revenue | Revenue vs. DB1 (Sales-revenue-gross basis, $7,687M) |
|---|---|---|---|---|
| LSEG (LON:LSEG) | 23.02× | 18.02× | £9.35B → $12.52B (GBP/USD 1.3388) | 162.8% — **borderline/outside ±50% band on this basis** (see flag below) |
| ICE (NYSE:ICE) | 17.76× | 16.91× | $10.44B | 135.8% ✅ |
| CME (NASDAQ:CME) | 19.91× | 19.17× | $6.74B | 87.7% ✅ |
| NDAQ (NASDAQ:NDAQ) | 22.47× | 20.96× | $5.42B | 70.5% ✅ |
| CBOE (BATS:CBOE) | 15.74× | 17.86× | $4.79B | 62.3% ✅ |
| **Median (5 peers)** | **19.91×** | **18.02×** | | |
| Median (4 peers, ex-LSEG) | 18.835× | 18.515× | | |

**Flagged methodology sensitivity:** comparing DB1's own **gross Sales-revenue** figure ($7,687M = €6,728M × 1.1425) against each peer's own vendor-reported "TTM Revenue" puts LSEG at ~163% of DB1's scale — just outside Rule 5's ±50% band, versus 06-19's finding of 146% (in-band), which used a different DB1 revenue basis (yfinance's own €7,381M "Total Revenue" field, never fully reconciled — see 06-19's Data Gap #1). This session cannot cleanly resolve which revenue-line convention the vendor-reported peer figures themselves use, so **both the 5-peer (incl. LSEG) and 4-peer (ex-LSEG) medians are shown**; the 5-peer set is used as primary for continuity with 06-19's established peer set (the underlying businesses haven't materially changed scale relative to each other), but the 4-peer cross-check moves the final multiples-based FV by only ~2.3% — not a material swing either way. HKEX, Euronext, SGX excluded as too small, unchanged from 06-19.

### Data Gaps flagged (summary)

1. **Gross margin** — no primary "Gross Profit"/COGS line disclosed by DB1; vendor-sourced (81.27%), cross-validated across 3 sources but not reconciled to a disclosed cost breakdown.
2. **Net margin basis** — DB1's multiple revenue-line concepts (Sales revenue / Net revenue / vendor "Total Revenue") don't cleanly reconcile; this session's primary-source-derived 33.38% (TTM) is used, differing from a ~28.6% vendor figure using an unreconstructable basis.
3. **Cash** — no more-current balance-sheet cash breakout than FY2025 year-end (31 Dec 2025); ~5 months stale relative to live price, same limitation as 06-19.
4. **ROIC** — razor-thin at 15.03% (excl. NCI) vs. 14.65% (incl. NCI) — genuinely borderline, methodology-sensitive, not a comfortable pass. Flagged prominently since it materially affects the Quality Score's Profitability sub-score.
5. **LSEG revenue-scale classification** — borderline in/out of Rule 5's ±50% band depending on which DB1 revenue-line convention is used against the peer's own reported figure; both medians shown.
6. **FY2026E EPS consensus** — ranges €12.16–12.47 across 3 sources; €12.27 used, cross-validated against guidance-consistent revenue/EBITDA estimates from the same vendor.
7. **Cost of debt** — this session improves on 06-19's estimate (~3.5%, anchored to 2 of 9 bonds' coupons) with a fully computed notional-weighted coupon across all 9 disclosed outstanding bonds (2.640%) — closes that flagged gap.

---

## 3. Phase 01 — Quality Gate (re-verified with fresh data)

| Check | DB1 Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 81.27% (vendor-sourced, cross-validated 3×) | >40% | ✅ PASS |
| Net margin | 33.38% (TTM, primary-source-derived) | >12% | ✅ PASS |
| ROIC | **15.03%** (excl. NCI; 14.65% incl. NCI — borderline) | >15% | ✅ PASS (thin — see Data Gap #4) |
| Revenue CAGR 3yr | 11.58% (Net Revenue basis, primary-sourced) | >8% | ✅ PASS |
| FCF positive 3+ consecutive years | Yes — FY2022–2025 all positive (multiple cross-checked sources) | required | ✅ PASS |
| Net debt/EBITDA | 1.294× (Net Debt €4,668M ÷ TTM EBITDA €3,607M) | <2.5× (standard) or <4× (asset-light) | ✅ PASS (comfortably, either threshold) |
| FCF yield | 5.138% (€2,430M ÷ €47,294.0M market cap) | >4% | ✅ PASS |
| EV/EBIT | 16.76× (EV €51,962.0M ÷ TTM EBIT €3,100M) | <20× | ✅ PASS |

**Gate result: PASS — 8/8**, consistent with 06-19, but the margin of safety on the ROIC check has narrowed materially now that a proper ROIC (not an ROE proxy) is computed — flagged prominently above, and it is the single largest driver of the Quality Score's Profitability sub-score falling short of a comfortable pass (see §4).

---

## 4. Quality Score (Phase 01 engine) — first-ever for this ticker — [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29

### Hard disqualifiers — checked first, none fire

- FCF/NI conversion <70% for 2+ consecutive years: FY2025 FCF/NI ≈ 121.8% (€2,430M/€1,995M), FY2024 ≈ 105–121% depending on CapEx source (both vendor readings clear 70% easily) — **does not fire**.
- Net Debt/EBITDA over threshold: 1.294× vs. 6× (asset-light override, see below) or 2.5× (standard) — **does not fire**.
- Not FCF-positive 3+ consecutive years: FCF positive every year FY2022–2025 — **does not fire**.

### Profitability (25% weight)

```
NetMargin_Component = clamp(33.38/30 × 100, 0, 100) = 100.0  (capped)
ROIC_Component       = clamp(15.03/30 × 100, 0, 100) = 50.09
Profitability_Score  = (100.0 + 50.09) / 2 = 75.05
```
No FCF-positivity cap applied (FCF-positive 5+ consecutive years). **ROIC_Component is the single largest drag on the Quality Score** — flagged: if the incl-NCI ROIC (14.65%) were used instead, this component drops further to 48.83, Profitability to 74.42 — the sensitivity doesn't change the gate outcome either way (already fails), but it underscores how thin this input is.

### Margins (15% weight)

```
GrossMargin_Score = clamp(81.27/80 × 100, 0, 100) = 100.0  (capped)
```
No trend-bonus applicable (bonus only applies below the 40% static threshold).

### Growth (20% weight)

```
Growth_Score (raw) = clamp(11.58/25 × 100, 0, 100) = 46.31
```
**TAM-expansion modifier +10 applied**, cited evidence: the binding **Allfunds Group plc** acquisition agreement (signed 21 Jan 2026, ~€5.3bn, court-approved Scheme of Arrangement approved by Allfunds shareholders 12 Mar 2026, expected close H1 2027) expands DB1's addressable market into fund-distribution/wealth-tech infrastructure — a genuinely new, disclosed, binding growth vector distinct from organic Trading & Clearing/Securities Services growth, plus continued double-digit SaaS growth within the existing Investment Management Solutions segment (SaaS net revenue +30% FY2025, +19% Q1/2026) and the EU policy tailwind toward EU-domiciled derivatives clearing. No structural-deceleration evidence found (Q1/2026 net revenue ex-treasury grew +12% YoY, an acceleration vs. FY2025's +9% — the opposite of deceleration).

```
Growth_Score = clamp(46.31 + 10, 0, 100) = 56.31
```

### Balance Sheet (15% weight) — **Asset-light override (Upgrade 5) applied**

DB1 is an exchange/clearing operator (explicitly named in Upgrade 5's covered category) whose disclosed debt is 100% financial (9 listed bonds, no operating debt), with:
- Interest coverage = TTM EBIT (3,100) ÷ |TTM financial result| (154) = **20.13×** — clears the >15× hurdle
- AA− credit rating — investment grade

Both conditions met → **/6 denominator override applies** (0.0 floor moves to 6× instead of 4×):
```
BalanceSheet_Score = clamp(100 × (1 − 1.294/6), 0, 100) = 78.43
```
(Standard /4 denominator, for reference, would give 67.65 — the override materially matters here.)

### Moat Signal (15% weight) — 3 of 5 TRUE, each with cited evidence

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | ✅ TRUE | Eurex is Europe's largest derivatives exchange (well-documented, longstanding market position); Trading & Clearing segment net revenue ex-treasury +9% FY2025, +14% Q1/2026 — consistent share-holding-or-growing performance, not share loss masked by market growth |
| Brand premium | ❌ FALSE | No cited pricing-power-without-volume-loss evidence found for a B2B market-infrastructure business (not a consumer-brand context) |
| Network effect | ✅ TRUE | Documented mechanism: an already-listed/cleared instrument's liquidity is destroyed by moving it to a competing venue, locking in incumbency — the standard two-sided-market liquidity-network-effect argument for exchanges/CCPs, unchanged from 06-19 |
| Switching costs | ✅ TRUE | Documented mechanism: clearing-member relationships, EU-wide regulatory licensing/authorization, and the integrated SimCorp/ISS/STOXX enterprise-software stack (multi-year enterprise contracts, deep client-workflow integration) — the ISS 19.69% minority-stake buy-in (closed end-March 2026, €1.15bn) further consolidates this platform |
| Scale cost advantage | ❌ FALSE | No cited cost-per-unit data vs. smaller competitors found this session (same strict citation standard applied to NVDA's CoWoS-access and MSFT's PUE arguments in other 2026-07 sessions — plausible but not independently evidenced) |

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI Ratio (FY2025) = €2,430M / €1,995M = 121.8%
FCFQuality_Score = clamp(((1.218 − 0.40)/0.60) × 100, 0, 100) = 100.0  (capped)
```

### Quality Score total

```
Quality Score = 75.05×0.25 + 100.0×0.15 + 56.31×0.20 + 78.43×0.15 + 60.0×0.15 + 100.0×0.10
              = 18.7625 + 15.0 + 11.262 + 11.7645 + 9.0 + 10.0
              = 75.789
```

# Quality Score = 75.8 → **FAILS the 80.0+ gate** (by 4.2 points — a real, non-boundary miss, not a rounding artifact)

No hard disqualifier fires — this is purely a weighted-score shortfall, driven mainly by the thin ROIC-based Profitability component (75.05) and the Moat Signal ceiling (60.0, capped by the framework's strict citation standard on Brand and Scale sub-signals). Per quality-scoring.md: *"Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* Per this task's explicit instruction and this repo's 2026-07 established practice (AMZN/GOOG/MSFT/NKE/NOW/NVO/NFLX precedent for existing holdings), the full Valuation Score and Composite Score are still computed below **as reference-only figures**, flagged as a **false green light** that must not be acted upon.

---

## 5. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = 259.70 / 12.27 = 21.165×
EY = 1 / 21.165 = 4.725%
Spread = 4.725% − 4.49% (10Y UST) = +0.235%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.235% falls well short) → **+5 additive** (Step 1).

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +10** (same combined outcome as 06-19, driven by the same structural fact — DB1's forward earnings yield sits close to the current Treasury yield, not a wide spread).

---

## 6. Valuation Score (Phase 02) — [valuation-scoring.md](../framework/valuation-scoring.md), methodology version 2026-06-29

### FCF Yield (40% weight)

```
FCF Yield = FCF / Market Cap = €2,430.0M / €47,294.0M = 5.138%
FCF_Score = clamp(100 × (1 − 5.138/10), 0, 100) = 48.62
```
FCF = FY2025 OCF (€2,810M, cross-validated exactly across two independent vendors and consistent with the 06-19 session's yfinance figure) minus CapEx. **CapEx flagged as an unreconciled cross-vendor discrepancy this session**: one vendor's cash-flow-statement page shows FY2025 CapEx of only €55M (implying FCF €2,755M, FCF Yield 5.83%, FCF_Score 41.75), while this session retains the more conservative €380M figure carried forward from 06-19's yfinance pull (not independently re-verifiable this session, yfinance unreachable) on the reasoning that DB1 discloses meaningful capitalized-software investment (SimCorp/Investment Management Solutions platform build-out) that a narrow "PP&E-only" capex reading would likely understate. The more conservative (lower-FCF, higher-score) reading is used as primary.

### EV/EBIT (40% weight, redistributed — not a Fast Grower, see §2)

```
EV = Market Cap (47,294.0) + Net Debt (4,668.0) = €51,962.0M
EV/EBIT = 51,962.0 / 3,100 (TTM EBIT) = 16.762×
EV/EBIT_Score = clamp((16.762 − 12)/23 × 100, 0, 100) = 20.70
```

### Forward PE (20% weight) — **PRIMARY formula, current 5yr range** (methodology change from 06-19's 10yr basis)

```
Forward PE   = 21.165×
5yr Low PE   = 19.77×  (2023)
5yr High PE  = 22.32×  (2021)

FwdPE_Score (raw) = clamp((21.165 − 19.77)/(22.32 − 19.77) × 100, 0, 100) = 54.72
```

**Historical PE Modifier (Upgrade 2)**
```
Deviation from 5yr avg (20.686) = (21.165 − 20.686)/20.686 = +2.32%
```
Within ±10% → modifier = **0**.
```
FwdPE_Score (adjusted) = 54.72
```

This sub-score moved materially from 06-19's 58.85 (10yr-basis) to 54.72 (5yr-basis) — a direct, visible effect of the methodology change this re-evaluation exists to capture. Both readings place DB1 in a similar "near the middle of its own historical range" position, but the 5yr window is now materially narrower (19.77–22.32× vs. 11.21–25.60×), so the same forward multiple reads as somewhat less "cheap relative to its own history" than under the old 10yr lookback.

### PEG — not applicable (redistributed to EV/EBIT, see §2)

### Final Score

```
Raw weighted score = (48.62 × 0.40) + (20.70 × 0.40) + (54.72 × 0.20)
                    = 19.448 + 8.280 + 10.944
                    = 38.674 (unrounded intermediate: 38.674)

+ Rate Regime Modifier (5+5) = 38.674 + 10 = 48.674
```

### Upside/Downside Modifier — full calc shown

**Step 1 — Fair Value, bull/base/bear (Rule 1: DCF + Multiples, Rule 7: mandatory scenario weighting)**

*Method A — 3-stage DCF* (Rule 2: yrs 1–5 explicit, yrs 6–10 fade to 2.5% terminal, Gordon-growth terminal value). Base FCF = €2,430M (FY2025). WACC and growth varied per scenario (Rule 2: WACC ±1pp):

**WACC — judgment call, flagged explicitly (carried forward from 06-19's established resolution, beta refreshed).** DB1's own raw beta (0.30) is structurally too low to use directly — same conclusion as 06-19 (0.28), which found even a peer-average beta produced a WACC low enough to fail Rule 4's sanity checks (Bear-case DCF EV materially exceeding actual current EV). This session again anchors WACC to **ICE's beta (0.95, current)**, the most business-model-comparable large peer (up slightly from 06-19's 0.92 reading):

```
Cost of Equity (beta=0.95) = 2.94% (German 10Y Bund) + 0.95×5.0% (ERP) = 7.69%
Capital structure: Equity €47,294.0M (88.0%) / Debt €6,450.0M (12.0%)
After-tax cost of debt = 2.640% × (1−0.2650) = 1.943%  (computed from the full 9-bond notional-weighted coupon — see §2, an improvement on 06-19's ~3.5% estimate)
WACC (Base) = 0.880×7.69% + 0.120×1.943% = 7.00%
```

| Scenario | WACC | Yrs 1–5 growth | EV (3-stage DCF) | TV weight |
|---|---|---|---|---|
| Bear | 8.00% | +6% | €55,475.6M | 61.3% |
| Base | 7.00% | +8% | €76,665.4M | 67.8% |
| Bull | 6.00% | +10% | €111,981.3M | 74.6% |

All three clear Rule 4's <75% terminal-value-weight sanity check (Bull at 74.6% is the closest, but passes — cleaner than 06-19's Bull case, which breached to 75.8%). Growth rates bumped modestly from 06-19's Bear/Base/Bull (5/7/9%) to (6/8/10%), reflecting DB1's own disclosed FY2026 guidance (net revenue ex-treasury guided to ~€5.7bn, +9.85% vs. FY2025's €5,189M organic-only base) and Q1/2026's already-confirmed +12% net-revenue-ex-treasury growth — both running ahead of 06-19's more conservative organic-only 7% Base assumption.

```
Bear-case EV (55,475.6) still sits +6.8% above current EV (51,962.0) — mild undervaluation supported even under the conservative scenario, consistent with 06-19's pattern.
```

*Method B — Peer multiples, scenario-varied (Rule 5 peer set, low/median/high across the 5 in-band peers — see §2):*

| Scenario | EV/EBIT peer mult. | FwdPE peer mult. | Multiples FV/share |
|---|---|---|---|
| Bear | 15.74× (CBOE, low) | 16.91× (ICE, low) | (242.30+207.49)/2 = **224.89** |
| Base | 19.91× (CME, median) | 18.02× (LSEG, median) | (313.29+221.11)/2 = **267.20** |
| Bull | 23.02× (LSEG, high) | 20.96× (NDAQ, high) | (366.23+257.18)/2 = **311.70** |

**Triangulation (40% DCF + 60% Multiples), per scenario:**
```
Bear:  0.40×278.99 + 0.60×224.89 = 246.53   (DCF FV/share: (55,475.6−4,668)/182.11 = 278.99)
Base:  0.40×395.35 + 0.60×267.20 = 318.46   (DCF FV/share: (76,665.4−4,668)/182.11 = 395.35)
Bull:  0.40×589.28 + 0.60×311.70 = 422.73   (DCF FV/share: (111,981.3−4,668)/182.11 = 589.28)
```

**PW Fair Value (Rule 7):**
```
PW Fair Value = 0.25×422.73 + 0.50×318.46 + 0.25×246.53 = 326.55
```
Sanity check (Rule 4): PW FV (€326.55) sits **+14.3%** above the analyst consensus mean PT (€285.67, 12 analysts) — a moderate, not extreme, divergence (wider than 06-19's +11.2%, mainly reflecting the guidance-informed growth bump above), still not an outlier call given the "Buy"/"Moderate Buy" analyst consensus rating.

**Step 2 — Expected annual return `E`**

```
Gap Upside % = (326.55 / 259.70) − 1 = +25.74%
Catalyst window = 2 years (default per Rule 10's fallback — see guardrail discussion below)
Annualized gap = 25.74% / 2 = 12.87%

Intrinsic growth = 8.07%/yr — analyst consensus FY2026E→FY2027E EPS growth (€12.27 → €13.26, marketscreener.com), used in preference to a self-generated DCF growth assumption, per "never invent"

Shareholder yield = Dividend yield (4.20/259.70 = 1.617%) + Buyback yield (€500M announced 2026 program ÷ €47,294.0M market cap = 1.057%, gross — not netted for SBC-driven issuance, data not separately available) = 2.674%

E = 12.87% + 8.07% + 2.674% = 23.61%
```

**Step 3 — Map to modifier, with the catalyst guardrail**

```
E (23.61%) ≥ H (10%) → M (uncapped) = −15 × clamp((23.61−10)/15, 0, 1) = −15 × 0.907 = −13.61
```

**Guardrail check — not capped, decision flagged explicitly.** Rule 10 requires a documented catalyst + timeline within 18–24 months before crediting large upside. This session identifies three concrete, dated events within that window: (1) Q2/2026 earnings (23 Jul 2026, ~2 weeks out) — will confirm whether the accelerating Q1/2026 growth trajectory holds; (2) FY2026 full-year guidance delivery (~Feb 2027, ~7 months out) — a direct test of the ~€5.7bn net-revenue-ex-treasury / ~€3.1bn EBITDA-ex-treasury guidance this session's growth assumptions lean on; (3) the binding Allfunds acquisition closing (expected H1 2027, ~9–12 months out) — a specific, signed, board-approved, shareholder-approved transaction (not a preliminary talks situation), earnings-accretive and TAM-expanding. Unlike the DOCS precedent this cycle (where the cap was applied because the only identifiable catalyst was an unverified management narrative actively disputed by open securities-litigation over disclosure adequacy), DB1 carries no comparable credibility overhang on its own guidance or M&A disclosures — so this session does **not** apply the guardrail cap, using the full computed modifier.

```
Upside/Downside Modifier applied = −13.6   (rounded)
```

### Final Valuation Score

```
Final Score = 48.674 (raw + Rate Modifier) + (−13.615) (Upside/Downside Modifier)
            = 35.059
Rounded: 35.1
```

# Valuation Score = 35.1 → band 30.0–49.9 ("Cheap") — but see §7: **not actionable on its own, since Quality fails the 80.0+ gate (§4)**

---

## 7. Composite Score — reference only ("false green light")

Per quality-scoring.md, Composite Score "isn't computed for, and doesn't rescue, a company failing the quality gate." Per this task's explicit instruction and the established 2026-07 practice for this exact situation (AMZN/GOOG/MSFT/NKE/NOW/NVO/NFLX sessions), it is still computed below **as a reference figure only**:

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 75.8) + 0.50 × 35.1
                = 0.50 × 24.2 + 0.50 × 35.1
                = 12.1 + 17.55
                = 29.65 → exactly on a ".X5" boundary → round UP (conservative) → 29.7
```

# Composite Score = 29.7 — numerically lands in the "Very Cheap → Full position (6–8%)" band (0.0–29.9)

**This is a false green light and must not be acted on at face value.** Read in isolation, 29.7 would nominally recommend the framework's single most aggressive entry action for DB1. It does not reflect the framework's actual conclusion — see §9.

---

## 8. Fair Value & Order Setup — [fair-value-methodology.md](../framework/fair-value-methodology.md)

Shown in full per the operating brief's "show every calculation, no black-box outputs" rule, even though §9 concludes DB1 should not be entered — this is exactly the same posture 06-19 took (showing the full order-setup mechanics of a failing R/R gate for transparency).

### Blended FV (Step 1 convention — PW-DCF blended with base-case multiples, used for Buy Price/Sell Target mechanics, distinct from the Upside/Downside Modifier's own separately-scenario-weighted PW FV in §6)

```
PW-DCF (0.25×Bull + 0.50×Base + 0.25×Bear DCF FV/share) = 0.25×589.28 + 0.50×395.35 + 0.25×278.99 = 414.74
Blended FV = 0.40 × 414.74 (PW-DCF) + 0.60 × 267.20 (Base-case Multiples) = 165.90 + 160.32 = EUR 326.22
```

(Note: this is numerically almost identical to §6's separately-derived, fully-per-scenario-triangulated PW Fair Value of €326.55 — reassuring cross-check, not a coincidence to rely on, but consistent with 06-19's finding that both fair-value framings tend to converge for this name.)

### Buy Price & R/R Gate

Nominal Valuation Score 35.1 falls in the 30.0–49.9 (Cheap) band → MoS 25–30%. DB1's ROIC (15.03%, computed properly this session — see §2) sits at the very bottom edge of Rule 8's "Standard quality business (ROIC 15–20%)" tier (not the "proven compounder >20yr ROIC>15%" tier) → **30% MoS** used, same conservative choice as 06-19:

```
Buy Price ceiling = Blended FV × (1 − 0.30) = 326.22 × 0.70 = EUR 228.35
```

**Current price (EUR 259.70) is ABOVE the Buy Price ceiling** — implied MoS at current price = 1 − (259.70/326.22) = **20.39%**, below the 25–30% required band. Per Step 2: Score 30.0–49.9 → "Set limit order," not enter-now.

**Step 6 (Risk/Reward) — tested at the limit-order entry price (€228.35)**

```
Primary Sell Target = Blended FV = EUR 326.22
```

| Stop band (25–30% max loss) | Stop price | R/R |
|---|---|---|
| 25% (tight end) | €171.27 | 1.71:1 |
| 27.5% (midpoint) | €165.56 | 1.56:1 |
| 30% (loose end) | €159.85 | 1.43:1 |

**None of the three points clear the 2:1 minimum.** Solved algebraically: a 2:1 R/R from this entry requires a stop at €179.42 (21.43% max loss) — tighter than even the aggressive end of the standard 25–30% band, and there is no DB1-specific risk characteristic that would justify tightening below the standard band. **R/R gate FAILS. Do not enter.** — the same conclusion, and an almost identical numeric range (1.43–1.71:1 here vs. 1.43–1.71:1 in 06-19), as the prior session.

**Supplementary checks (all confirm the failure is robust):**
- At the current price (€259.70), tighter 20–25% stop band: R/R ranges **1.02–1.28:1** — still fails, worse than the limit-order entry.
- At the loosest MoS entry (25%, €244.67): R/R ranges **1.11–1.33:1** across the standard stop band — still fails, worse (same pattern 06-19 found).
- Using the **Bull-Case Trim Target** (€380.46 = 90% of the Bull-scenario Blended FV, €422.73) instead of the Primary Sell Target would produce a passing **2.22–2.66:1** — **not used**, since Step 6 explicitly pairs R/R against the Primary (base-case) Sell Target; substituting the bull-case number to manufacture a pass would be exactly the rule-bending the framework's "no black-box outputs" rule prohibits (same explicit refusal as 06-19).

### Order Setup Checklist

```
[x] Quality Score:                           75.8 — FAILS the 80.0+ gate (§4)
[x] Valuation Score (incl. Upside/Downside):  35.1   (Cheap band, 30.0-49.9 — reference only, see below)
[x] Composite Score:                         29.7   (Very Cheap band — FALSE GREEN LIGHT, not actionable, see §7/§9)
[x] DCF Fair Value (PW, scenario-weighted):  EUR 414.74
[x] Multiples-Based Fair Value (base case):  EUR 267.20
[x] Blended Fair Value:                      EUR 326.22
[x] Margin of Safety %:                      30% (Rule 8, Standard quality ROIC 15-20% tier, thin) -> Buy Price ceiling EUR 228.35;
                                              current price (EUR 259.70) is ABOVE the ceiling (20.39% implied MoS, below the
                                              25-30% required band) -> limit order indicated, NOT enter-now
[x] BUY PRICE (limit order, if gates cleared): EUR 228.35
[x] PRIMARY SELL TARGET (at FV):             EUR 326.22
[x] BULL-CASE TRIM TARGET:                   EUR 380.46  (shown for completeness; NOT used for the R/R gate)
[ ] STOP LOSS:                               FAILS GATE -- no stop in the standard 25-30% band clears 2:1
[ ] Risk/Reward Ratio:                       1.43-1.71:1 across the standard stop band -- FAILS the 2:1 minimum
[ ] Max $ Risk / POSITION SIZE:              NOT COMPUTED -- both the Quality Gate (§4) and the R/R gate independently block entry
[x] Thesis invalidation triggers:            see SS10
```

**Per fair-value-methodology.md Step 6, this session does not proceed to position sizing.** Unlike 06-19 (which only had the R/R gate to contend with), DB1 is now **independently blocked by two separate gates** — the Quality Score gate (§4, 75.8 < 80.0) and the R/R gate (this section) — either one alone would be sufficient to block entry.

---

## 9. Recommendation

# **WATCHLIST ONLY — DO NOT ENTER.** The Quality Score (75.8) fails the 80.0+ gate, so the Composite Score (29.7, which would nominally read "Very Cheap → Full position 6–8%") is a false green light that must not be acted on. Independently — and even setting the quality-gate finding aside entirely — the Risk/Reward gate also fails at every tested entry (1.43–1.71:1 vs. the 2:1 minimum), the same conclusion 06-19 reached before either the Quality Score or the Upside/Downside Modifier existed.

**Why this outcome, in order of how decisively each finding blocks entry:**

1. **Quality Score 75.8 fails the 80.0+ gate — a real, 4.2-point miss, not a rounding artifact or a hard-disqualifier trip.** No hard disqualifier fires (FCF/NI conversion, balance sheet, FCF-positivity all clear comfortably) — this is purely the weighted-average of six sub-scores falling short. The single largest drag is the Profitability sub-score's ROIC component: a properly-computed ROIC (15.03%, using NOPAT ÷ Invested Capital per the framework's current convention) is dramatically thinner than 06-19's ROE-proxy reading (19.21%) ever suggested, and is itself borderline-sensitive to whether non-controlling interests are included in the Invested Capital base (14.65% incl. NCI — a marginal *fail* of even the binary Phase 01 >15% ROIC check). The Moat Signal sub-score (60.0) is also capped by the framework's strict citation standard — DB1's business genuinely has strong liquidity-network-effect and switching-cost moats (both credited), but no independently cited evidence supports crediting Brand or Scale-cost-advantage signals, unlike some other large-cap names this cycle.

2. **Even treating the Composite/Valuation Score at face value, the Risk/Reward gate independently fails.** DB1's Forward PE sub-score (54.72, under the *current* 5yr-lookback methodology) sits close to the middle of its own 5-year trading range — the stock isn't trading unusually cheap relative to its own recent history, even though its absolute FCF yield (5.14%) and EV/EBIT (16.76×) look attractive against the framework's universal thresholds. That combination produces a real but modest valuation gap, mathematically incompatible with a 2:1 R/R once a realistic stop-loss distance is applied — structurally the same finding as 06-19, now reconfirmed under the current methodology with fresh data.

3. **This is a name worth continuing to watch, not passing on outright.** Unlike a hard-disqualifier failure (e.g. CHTR's leverage breach, or a structurally-broken business), DB1's Quality Score miss is a genuinely close weighted-average shortfall on an otherwise clean 8/8 Phase 01 business, with credible, dated catalysts (Q2/2026 earnings 23 Jul 2026, FY2026 guidance delivery ~Feb 2027, the binding Allfunds close ~H1 2027) that could plausibly move either the Quality Score (via continued margin/ROIC improvement, or a more clearly-evidenced Moat signal) or the R/R math (via a price pullback, which — per the same mechanism 06-19 identified — would widen R/R and lower the valuation score simultaneously) toward an actionable setup within the next 1–2 review cycles.

**What would change this call:**
- **A lower entry price** — the binding R/R constraint is the numerator (upside), so a price decline with the fundamental thesis intact would mechanically widen R/R while also lowering the valuation score.
- **A Quality Score re-check showing genuine margin/ROIC improvement** — e.g., if FY2026 guidance delivery (~Feb 2027) confirms the ~16% EBITDA-ex-treasury growth trajectory, the resulting ROIC improvement could plausibly close some or all of the 4.2-point gate shortfall.
- **Independently-cited evidence supporting the Brand or Scale-cost-advantage Moat signals** (currently uncredited for lack of citation, not because the underlying business plausibly lacks them).
- FY2026 full-year results (~Feb 2027) — mandatory re-score (Rule 9); check organic vs. total (incl. Allfunds, once closed) growth vs. guidance.
- The Allfunds acquisition closing (expected H1 2027) — a Rule 9 material-M&A trigger requiring a fresh full re-evaluation once it closes (adds meaningful scale and a new business line).
- Margin compression — gross margin (81.27%) falling >3pp structurally, or ROIC falling further below the already-thin 15% level.
- EU regulatory action against Eurex/Clearstream's clearing-monopoly economics (the historical EMIR open-access threat) re-emerging as a live policy risk.
- >15% unexplained price move from €259.70 (Rule 9) — immediate re-score.
- Ongoing litigation to monitor as a risk flag (not a thesis-breaking event on its own): the Peterson II Iran-asset-turnover case at Clearstream Banking S.A. (Luxembourg court ruled against Clearstream 31 Mar 2026 on a ~$1.7bn claim; Clearstream is assessing an appeal) and ISS's 13 Apr 2026 lawsuit challenging an Indiana state law on proxy advisors (ISS as plaintiff, not defendant — a regulatory-environment risk to the proxy-advisory business line, not an allegation against DB1 itself).

**Qualitative notes** (5 Questions, largely carried forward from 06-19 with 2026 updates):
- **Why margins are high:** Xetra (German cash equities), Eurex (Europe's largest derivatives exchange), and Clearstream (post-trade settlement/custody) are regulated, liquidity-network-effect businesses with high operating leverage against near-fixed infrastructure costs.
- **Competitive moat:** decades of accumulated trading/clearing liquidity, EU-wide regulatory licensing, and clearing-member relationships are not organically replicable; EU market-infrastructure competition has historically come via consolidation, not de novo entrants.
- **Capital allocation:** continues as an active consolidator — the Allfunds acquisition (€5.3bn, signed Jan 2026) and the ISS minority-stake buy-in (€1.15bn, closed Mar 2026) both closed/signed since 06-19 — funded by a debt/equity mix alongside a growing dividend (€4.20/share, +5% YoY) and an ongoing €500M/year share buyback program.
- **Growth drivers (3–5yr):** Eurex derivatives volume (EU clearing tailwind), Investment Management Solutions segment (SimCorp/STOXX/ISS/Axioma, now including Allfunds' fund-distribution platform once closed), Clearstream collateral/securities-financing, and a new $200M/1.5% strategic stake in Kraken's parent (Payward, Inc., announced 14 Apr 2026, closing expected Q2 2026) signaling a deepening digital-assets strategy.
- **Bear case:** revenue remains volume/volatility/rate-dependent; EU regulatory/political risk (EMIR open-access) and integration risk across three concurrent M&A processes (SimCorp, ISS, and now Allfunds) are real, ongoing risks; the Peterson II litigation outcome (Clearstream Luxembourg) is an unresolved legal-risk overhang worth tracking, though not yet large enough relative to the balance sheet to be thesis-breaking.
- **Disruption vector:** low near-term risk — post-2008 regulation mandates central clearing for derivatives, a structural tailwind rather than a threat to centralized clearinghouses; the EU's own push toward EU-domiciled clearing (as an alternative to US/UK CCPs) is more plausibly a tailwind than a threat specifically for Deutsche Börse.

**Process note:** this session documents the analytical recommendation only. No broker order has been placed and nothing has been logged in `decisions/` or `portfolio/holdings.md`.

---

## 10. Next Review Trigger

- **Q2/2026 earnings — 23 Jul 2026** (~2 weeks out) — routine Rule 9 trigger; check whether the Q1/2026 growth acceleration (+12% net revenue ex-treasury YoY) held, and whether FY2026 guidance was reaffirmed, raised, or cut.
- **FY2026 full-year results (~Feb 2027)** — mandatory re-score (Rule 9); the single most important check given how much of this session's Upside/Downside Modifier and DCF growth assumptions lean on the company's own FY2026 guidance being delivered.
- **Allfunds acquisition closing (expected H1 2027)** — material M&A, Rule 9 trigger; requires a full fresh Phase 01/Quality Score re-check on the combined entity, not an extrapolation from today's standalone numbers.
- **A price decline toward or below the EUR 228.35 MoS-implied limit price** — would mechanically widen R/R toward the 2:1 minimum; full position-sizing pass would still additionally require the Quality Score gate to also be cleared (§4) before this becomes actionable.
- **Any development materially improving the Quality Score's weakest inputs** — a clearer, independently-cited Moat signal (Brand or Scale-cost-advantage), or a ROIC improvement that resolves the current 14.65–15.03% ambiguity decisively above 15% with room to spare.
- **>15% unexplained price move from €259.70** (Rule 9) — immediate re-score.
- **Peterson II litigation developments** (Clearstream Luxembourg appeal) and **EU regulatory signal** specific to Eurex/Clearstream clearing-monopoly economics (EMIR-style open-access risk).
- **Quarterly Rate Environment Gate update** (next: ~Oct 2026).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session: ADR, AA− (Investment grade), Beta, Buyback yield (net buyback yield), CAGR, Composite Score, Coupon (bond), Debt Gate, DCF, EBIT, EBITDA, Equity Risk Premium (ERP), EV, EV/EBIT, EY (Earnings Yield), Fast Grower, FCF, FCF Yield, FCF/NI conversion ratio, Forward PE, FV (Fair Value), Gross Margin, Hard disqualifier, Hurdle rate, Interest coverage (ratio), Invested Capital, IRR, Moat, MoS (Margin of Safety), Net Debt/EBITDA, Net Margin, NOPAT, PE ratio, PEG ratio, Effective tax rate, PT (Price Target), PW (Probability-Weighted) Fair Value, Quality Score, Rate Environment Gate, Rate Regime Modifier, ROE, ROIC, R/R (Risk/Reward ratio), Rule 0, Rule 9, Scheme of arrangement, Shareholder yield, TAM, Terminal Value, Treasury yield (10Y), TTM, Upside/Downside Modifier, Valuation score, Value trap, WACC.
