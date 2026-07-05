# RESCORE — UBER (Uber Technologies, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-07-05 (Sunday — markets closed; most recent trading session 2026-07-02)
**10Y US Treasury Yield:** 4.49% (TradingEconomics/dshort "Treasury Yields Snapshot," 2 Jul 2026 close — same figure used in the same-day [MSFT](2026-07-05-rescore-msft.md) and [NOW](2026-07-05-rescore-now.md) rescores for consistency across same-day sessions; cross-checked against FRED `DGS10`'s most recent posted value, 2026-07-01 = 4.48% — both land in the same 3.5–5% Rate Regime bracket, no sensitivity either way)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** UBER **34.8** (2026-06-20, nominally BUY-Standard band, but blocked at entry by a sub-2:1 R/R — [sessions/2026-06-20-rescore-uber.md](2026-06-20-rescore-uber.md)); Quality Score / Composite Score never computed (predates the 2026-06-29 methodology change — flagged stale, see [watchlist/STALE.md](../watchlist/STALE.md)).
**Current UBER portfolio weight:** 0.42% per [holdings.md](../portfolio/holdings.md) — nowhere near the 15% hard cap (Upgrade 7).
**First-ever Quality Score / Composite Score computation for UBER this session.**

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$74.43** | IBKR `get_price_history` (contract_id 365207014, NYSE), most recent daily bar close = **2026-07-02**. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$72.66** (flagged `is_close: true`) — one session stale: `get_price_history` shows 2026-07-01 close = $72.66 and 2026-07-02 close = $74.43. Same recurring stale-snapshot pattern flagged in the 2026-07-05 NOW/MSFT and 2026-07-04 AVGO sessions — used the fresher $74.43 instead. Cross-checked independently against stockanalysis.com, whose "Current Stock Price" field also read **$74.43** exactly — corroborates the fresher figure. |
| Mark price (`plprice`) | $74.35 | IBKR `get_price_snapshot` — close to $74.43, consistent with the fresher close rather than the stale $72.66 "last." |
| 52-week range | $67.21 – $101.98 | IBKR `misc_statistics` |
| Year-to-date change | −11.08% (−$9.05) | IBKR `year_to_date_change` |
| Analyst consensus PT | mean **$104.48** (+40.4%), range $70–$150, 53 analysts, "Strong Buy" consensus | stockanalysis.com — bull-case sanity check only (Rule 0 Step 4), not a scored input |
| Dividend yield | 0% (no dividend) | IBKR `dividend_yield` + stockanalysis.com, consistent |
| Price vs. 06-20 review ($70.91) | **+5.0%** | Well under the 15% Rule 9 threshold |

---

## 2. Rule 9 Trigger Check (2026-06-20 → 2026-07-05)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Q1 2026 was already reported 6 May 2026 (predates 06-20 review); Q2 2026 not due until early August 2026 per the 06-20 entry's own "next review trigger." |
| Guidance revision | No | Q2 2026 guidance (Gross Bookings $56.25–57.75B, Adj. EBITDA $2.70–2.80B) was issued with the 6 May 2026 Q1 print — predates this window, not a fresh trigger. |
| M&A / material investment | No (predates window) | Uber's $10B+ AV fleet-acquisition commitment (15 Apr 2026) and the Uber–Rivian robotaxi partnership (19 Mar 2026, up to $1.25B invested in Rivian through 2031) both predate the 06-20 review. No new AV/M&A announcement found dated between 2026-06-20 and 2026-07-05 (WebSearch canvass of recent Uber news). |
| Management change | No | None found. |
| Macro shift | No | 10Y ticked from 4.44% (06-20) to 4.49% (07-05) — still inside the 3.5–5% bracket, no Rate Regime bracket change. |
| >15% unexplained price move | No | +5.0% since 06-20 — a modest continuation, not unexplained, well under the 15% threshold. |

**Conclusion: no Rule 9 trigger fired.** This is a routine, scheduled price-refresh rescore — but see §4 for the **first-ever UBER Quality Score computation**, which is new information independent of any Rule 9 event.

---

## 3. Data Gaps / Flags

1. **`yfinance` unreachable this session** — identical `curl_cffi` TLS-impersonation `SSLError` / `YFRateLimitError` pattern already documented for AAPL/CHTR/WSE/AMD/CDR/CRCL/NKE in this repo's session history (tried both a bare `yf.Ticker()` and the `requests.Session()` workaround that worked for MSFT/AVGO on 2026-07-04/05; both failed here). **Fallback per Rule 0's documented contingency:** all quantitative inputs below are sourced directly from **SEC EDGAR** (Uber's XBRL company-facts API, cross-checked against the underlying 10-Q/10-K/8-K filings), with **stockanalysis.com** used only as a cross-check / for analyst-consensus figures not in SEC filings (forward EPS consensus, price target) — consistent with how NKE's 2026-07-01 session used stockanalysis.com as its Rule-0-compliant fallback.

2. **🚩 Major GAAP net-income distortion, company-disclosed — required normalization for the Quality Score (Rule 6).** Uber's TTM GAAP net income ($8,540M — SEC-derived, see §5) is materially distorted by two large, company-flagged one-off/non-cash items:
   - **Q3 2025: a $4.9B tax-valuation-allowance-release benefit** — Uber's own Q3 2025 earnings press release (SEC 8-K, filed 2025-11-04) states verbatim: *"Q3 2025 net income includes a $4.9 billion benefit from a tax valuation release."* The SEC XBRL `IncomeTaxExpenseBenefit` tag shows a $4,046M net tax *benefit* for the quarter (the $4.9B gross release netted against other, smaller tax items) — a textbook **deferred tax valuation allowance release** (see glossary), the same mechanism already documented in this repo for DUOL/NOW/AMD.
   - **Q3 2025: a further ~$1.5B net gain from equity-investment revaluations** (same press release), and, in a mirror-image reversal, **Q1 2026: a $1.494B *loss*** from the same mechanism (SEC XBRL `OtherNonoperatingIncomeExpense` = −$1,494M for the quarter) — Uber's own Q1 2026 earnings release (SEC 8-K, filed 2026-05-06) states GAAP net income "includes $1.5B headwind from equity investment revaluations," confirming the figure. Uber holds several minority equity stakes (e.g. in Aurora Innovation and other AV/mobility partners) that are marked to fair value through earnings each quarter — a recurring, large, **non-cash**, non-operating source of net-income volatility distinct from the business's underlying operating performance.
   - **Handling (not invented, not silently absorbed):** per Rule 6 ("normalize before you value") and this framework's NVO/AMD precedent (normalize using company-disclosed one-off dollar figures or a clean-period effective tax rate, rather than either ignoring the distortion or fabricating an adjustment), §5 below shows **both** the raw GAAP Net Margin and a normalized Net Margin (backing out the three disclosed dollar figures above) side by side, and uses the normalized figure as the scored Profitability input. NOPAT/ROIC uses a normalized effective tax rate derived the same way (GAAP TTM tax figure with the $4.9B one-off backed out), not the nonsensical GAAP TTM effective rate (which is a large net *benefit*, i.e. negative — stockanalysis.com's own TTM figure: **−76.36%**).

3. **5yr historical PE range — no-history fallback used, consistent with UBER's own 06-20 session.** Uber only turned durably GAAP-profitable in FY2023 (FY2019–FY2022 were all GAAP net losses); a trailing 5-year PE series would span mostly negative/undefined-EPS periods and isn't a meaningful "5yr average/range" per [valuation-scoring.md](../framework/valuation-scoring.md)'s no-history fallback rule (*"recent IPO, loss-making history, or GAAP earnings base too distorted to be meaningful"*). This matches the 06-20 UBER session's own treatment (which used this same fallback) — not a new gap, and independent of the `yfinance` outage in flag 1 above (even with `yfinance` working, the underlying 5-year window still wouldn't be meaningful for UBER specifically).

4. **PEG / Fast-Grower eligibility — not qualifying, consistent with 06-20.** Per the same distorted-earnings-base logic in flag 2, Uber's trailing GAAP EPS is not a "clean, non-distorted" 3-year base (FY2023 $1,887M → FY2024 $9,856M, +422%, itself driven by earlier valuation-allowance releases → FY2025 $10,053M, +2% on the surface but containing the Q3 2025 one-off described above). **Not a qualifying Fast Grower this session** — PEG's 15% weight redistributed to EV/EBIT (→ 40%), matching the 06-20 UBER session's own determination.

5. **Moat Signal "Market share stable or growing" — citation is dated.** The most recent third-party US rideshare market-share split found (Bloomberg Second Measure, via secondmeasure.com) is **March 2024** (Uber ~76% of observed US rideshare spend, stable month-over-month at that time) — over two years old as of this session. No fresher independent share-tracker data was reachable. Shown transparently in §5 rather than silently treated as current; corroborated only loosely by Uber's own (not independently verified) Q1 2026 platform-growth metrics (MAPC +17% YoY, Gross Bookings +25% YoY), which measure Uber's own growth, not competitors' — so don't independently confirm *share* movement one way or the other.

---

## 4. UBER — Inputs Collected (SEC EDGAR primary, this session)

**Sector:** Technology — Mobility & Delivery Platforms (ride-hailing, food/grocery delivery, freight brokerage)

| Item | Value | Source |
|---|---|---|
| Shares outstanding (cover page, most recent) | 2,035,599,013 (as of 2026-05-01) | SEC 10-Q cover page (filed 2026-05-06), `dei:EntityCommonStockSharesOutstanding` |
| **Market Cap** | 2,035,599,013 × $74.43 = **$151,509.63M** | Computed |
| Total debt (2026-03-31) | $10,514M (LongTermDebtNoncurrent $10,514M + LongTermDebtCurrent $0) | SEC XBRL, 10-Q filed 2026-05-06 |
| Cash + short-term investments (2026-03-31) | $6,091M ($5,558M cash + $533M current marketable securities) | SEC XBRL, same 10-Q |
| **Net Debt** | $10,514M − $6,091M = **$4,423M** | Computed |
| **EV** | $151,509.63M + $4,423M = **$155,932.63M** | Computed |
| TTM Revenue (Q2'25–Q1'26) | $12,651M + $13,467M + $14,366M + $13,203M = **$53,687M** | SEC XBRL quarterly rollforward (Q4'25 derived: FY2025 $52,017M − 9mo'25 $37,651M) — matches stockanalysis.com's TTM figure exactly |
| TTM Cost of revenue (excl. D&A) | $7,611M + $8,109M + $8,681M + $7,258M = **$31,659M** | SEC XBRL `CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization` |
| **TTM Gross Profit** | $53,687M − $31,659M = **$22,028M** (41.03% margin) | Computed — matches stockanalysis.com exactly |
| **TTM EBIT (Operating Income)** | $1,450M + $1,113M + $1,774M + $1,923M = **$6,260M** | SEC XBRL `OperatingIncomeLoss` — matches stockanalysis.com exactly |
| **EV/EBIT** | $155,932.63M ÷ $6,260M = **24.91×** | Computed |
| TTM Operating Cash Flow | $2,564M + $2,328M + $2,883M + $2,351M = **$10,126M** | SEC XBRL `NetCashProvidedByUsedInOperatingActivities`, quarterly-differenced from cumulative YTD figures |
| TTM CapEx | $89M + $98M + $75M + $65M = **$327M** | SEC XBRL `PaymentsToAcquirePropertyPlantAndEquipment`, same method |
| **TTM FCF** | $10,126M − $327M = **$9,799M** | Computed |
| **FCF Yield** | $9,799M ÷ $151,509.63M = **6.47%** | Computed |
| TTM Net Income (GAAP, attributable to Uber) | $1,355M + $6,626M + $296M + $263M = **$8,540M** | SEC XBRL `NetIncomeLoss`, quarterly-differenced |
| **GAAP Net Margin (TTM)** | $8,540M ÷ $53,687M = **15.91%** | Computed — **distorted, see §3 flag 2** |
| **Normalized Net Income (TTM)** | $8,540M − $4,900M (Q3'25 tax release) − $1,500M (Q3'25 equity gain) + $1,494M (Q1'26 equity loss) = **$3,634M** | Computed from company-disclosed one-off dollar figures (§3 flag 2) |
| **Normalized Net Margin (TTM)** | $3,634M ÷ $53,687M = **6.77%** | Computed — **used as the scored Profitability input** |
| TTM Pretax income (excl. equity-method line) | $1,504M + $2,620M + $291M + $496M = **$4,911M** | SEC XBRL `IncomeLossFromContinuingOperationsBeforeIncomeTaxesMinorityInterestAndIncomeLossFromEquityMethodInvestments` |
| TTM GAAP tax expense/(benefit) | $142M + (−$4,046M) + (−$40M) + $194M = **−$3,750M** (net benefit) | SEC XBRL `IncomeTaxExpenseBenefit` |
| **Normalized tax expense (TTM)** | −$3,750M + $4,900M (one-off backed out) = **$1,150M** | Computed |
| **Normalized effective tax rate** | $1,150M ÷ $4,911M = **23.42%** | Computed — used for NOPAT below |
| **NOPAT (normalized)** | $6,260M × (1 − 0.2342) = **$4,795.9M** | Computed |
| Total Stockholders' Equity (2026-03-31) | $24,751M | SEC XBRL `StockholdersEquity` |
| **Invested Capital** (Debt+Equity convention) | $10,514M + $24,751M = **$35,265M** | Computed |
| **ROIC (TTM, normalized)** | $4,795.9M ÷ $35,265M = **13.60%** | Computed |
| TTM D&A | $175M + $188M + $185M + $184M = **$732M** | SEC XBRL `DepreciationDepletionAndAmortization` |
| **EBITDA (TTM)** | $6,260M + $732M = **$6,992M** | Computed |
| **Net Debt/EBITDA (TTM)** | $4,423M ÷ $6,992M = **0.63×** | Computed |
| Revenue FY2022 → FY2025 | $31,877M → $52,017M | SEC XBRL annual `Revenues` (10-K) |
| **Revenue 3yr CAGR** | (52,017/31,877)^(1/3) − 1 = **17.73%** | Computed |
| FCF/NI conversion (TTM) | $9,799M ÷ $8,540M = **114.7%** (GAAP basis) | Computed |
| Annual FCF/NI: FY2023 / FY2024 / FY2025 | 178.2% / 69.9% / 97.1% | Computed from SEC annual OCF/CapEx/NI (FY2024 dips marginally below the 70% line — see §5) |
| FCF positive, annual (FY2023–2025) | $3,362M / $6,895M / $9,763M — all positive | SEC XBRL, computed |
| Forward EPS consensus (FY2026, non-GAAP) | $3.33 (48 analysts) | stockanalysis.com/stocks/uber/forecast — **non-GAAP/adjusted basis**, flagged by the source itself |
| **Forward PE** | $74.43 ÷ $3.33 = **22.36×** | Computed — matches stockanalysis.com's own displayed 22.35× to within rounding |
| Shareholder yield — net buyback | Shares outstanding 2,091.856M (5/5/2025 cover date) → 2,035.599M (5/1/2026 cover date) = **−2.69%** over ~12.6 months ≈ **+2.5%/yr** net buyback yield (no dividend) | SEC XBRL `dei:EntityCommonStockSharesOutstanding`, computed |

---

## 5. UBER — Quality Score (first-ever computation, 2026-06-29 methodology)

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | FY2023 178.2% / FY2024 **69.9%** / FY2025 97.1% — only **one** year (FY2024) dips (barely) below 70%, not 2+ consecutive | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS (not consecutive; FY2024's dip is itself partly an artifact of that year's own elevated, valuation-allowance-boosted NI in the denominator — noted, not required to resolve the pass/fail here) |
| Net Debt/EBITDA over threshold? | **0.63×** | disqualify if >2.5× (standard) | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FY2023/2024/2025 all positive (see §4) | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)

```
GAAP Net Margin (TTM)       = $8,540M / $53,687M = 15.91%   [distorted — see §3 flag 2]
Normalized Net Margin (TTM) = $3,634M / $53,687M = 6.77%    [used as scored input]

NetMargin_Component (normalized) = clamp((6.77/30)×100, 0, 100) = 22.56
NetMargin_Component (GAAP, shown for reference only)            = clamp((15.91/30)×100, 0, 100) = 53.02

ROIC (TTM, normalized tax rate) = $4,795.9M / $35,265M = 13.60%
ROIC_Component = clamp((13.60/30)×100, 0, 100) = 45.33

Profitability_Score (normalized, scored) = (22.56 + 45.33) / 2 = 33.95
Profitability_Score (GAAP, reference)    = (53.02 + 45.33) / 2 = 49.18
```
No FCF-positive cap applies either way (3+ consecutive years positive, confirmed above). **Using the normalized figure (33.95)** as the scored input, per Rule 6 and this framework's NVO/AMD precedent for company-disclosed one-off items.

### Margins (15% weight)

```
Gross Margin (TTM) = 41.03%
GrossMargin_Score = clamp((41.03/80)×100, 0, 100) = 51.29
```
3yr trend: FY2023 39.75% → FY2024 39.39% → FY2025 39.76% → TTM 41.03% — essentially flat with a modest recent uptick, not a clear multi-year structural expansion (a dip in the middle year). In any case the **+10 structural-expansion bonus only applies to a margin below the 40% threshold that's trending up** — TTM margin (41.03%) already sits above 40%, so the bonus condition doesn't apply regardless of the trend judgment. No bonus.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $31,877M → FY2025 $52,017M) = 17.73%
Growth_Score = clamp((17.73/25)×100, 0, 100) = 70.92
```
**+10 (documented TAM expansion / platform growth, cited, Q1 2026 earnings release, SEC 8-K filed 2026-05-06):**
- Gross Bookings **+25% YoY** (+21% constant currency) to $53.7B.
- Trips **+20% YoY** to 3.6 billion.
- Monthly Active Platform Consumers (MAPC) **+17% YoY** to 199 million.
- **Uber One membership reached 50 million members**, now "driving half of our Gross Bookings across Mobility and Delivery" (company disclosure) — real, cited, current evidence of continued platform/TAM expansion via a growing paid-loyalty program, not merely a qualitative claim.

No decelerating-growth evidence found — Q2 2026 guidance (issued with the same release) calls for continued 18–22% constant-currency Gross Bookings growth, not a slowdown.

```
Growth_Score (with bonus) = clamp(70.92 + 10, 0, 100) = 80.92
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = 0.63×
BalanceSheet_Score = clamp(100×(1 − 0.63/4), 0, 100) = clamp(84.19, 0, 100) = 84.19
```
Standard /4 denominator applies — Uber is a rideshare/delivery marketplace, not a payment network/exchange, so the Upgrade 5 asset-light override (/6 denominator) doesn't apply (and isn't needed regardless, given the comfortably-low ratio).

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** (dated citation, flagged) | Bloomberg Second Measure (via secondmeasure.com): Uber held **~76% of observed US rideshare spend as of March 2024**, "about the same as" the prior month — the most recent independent share-tracker figure found (§3 flag 5 — over 2 years old, no fresher independent split located). No evidence of erosion found since; loosely consistent with, though not independently confirmed by, Uber's own Q1 2026 MAPC (+17% YoY) and Gross Bookings (+25% YoY) growth. |
| Brand premium | **FALSE** | No cited price-increase-without-volume-loss or premium-vs-competitor evidence found. Uber One's 50M-member growth (above) is loyalty-program *adoption*/monetization evidence, not the specific pricing-power evidentiary type the checklist requires (same rigor standard applied to NOW's/MSFT's FALSE signals in the 2026-07-05 sessions). |
| Network effect | **TRUE** | Uber's own FY2025 Form 10-K (filed 2026-02-13): *"Our massive, efficient, and intelligent network consists of hundreds of millions of Drivers, consumers, Merchants, Shippers and Carriers... Our network becomes smarter with every trip."* A documented, company-disclosed multi-sided-marketplace mechanism — the textbook network-effect case, directly comparable to how PDD's group-buying mechanism was credited in a prior session. |
| Switching costs | **FALSE** | Uber's own FY2025 10-K explicitly states drivers "are free to provide services on our competitors' platforms" — **multi-homing** (see glossary) is disclosed and unrestricted for the supply side, with no contractual or integration-depth lock-in mechanism documented for either drivers or riders. Directly undermines a switching-cost claim, so marked false with the company's own language as the citation. |
| Scale cost advantage | **FALSE** | No cost-per-trip or other unit-cost data found showing a gap vs. smaller competitors (Lyft, regional players) — only revenue-scale and platform-growth citations were found, which are inputs, not the cost-per-unit *output* the checklist specifically requires (same rigor standard as NOW's and NKE's FALSE "scale" calls). |

```
Moat_Score = (2/5) × 100 = 40.0
```
**Sensitivity, shown transparently:** if "Market share" were instead marked FALSE (given how dated its citation is) the Moat_Score would drop to 20.0 and the overall Quality Score to ~57.0; if a third signal were credited TRUE the Moat_Score would rise to 60.0 and the overall Quality Score to ~64.0 (see §6 for the full range) — **the 80.0+ gate result is robust to this uncertainty either way (see §6)**, unlike the knife-edge NOW/MSFT/AVGO cases.

### FCF Quality (10% weight)

```
FCF/NI (TTM, GAAP basis) = $9,799M / $8,540M = 114.7%
FCFQuality_Score = clamp(((1.147 − 0.40)/0.60)×100, 0, 100) = clamp(124.6, 0, 100) = 100.0
```
Using the normalized NI ($3,634M) instead would give an even higher ratio (269.7%) — both are already above the 100% ceiling, so the sub-score is 100.0 either way; the GAAP-basis figure is shown as the primary calc since it doesn't change the outcome.

### Quality Score — Final

```
Quality Score = (33.95×0.25) + (51.29×0.15) + (80.92×0.20) + (84.19×0.15) + (40.0×0.15) + (100.0×0.10)
              = 8.4875 + 7.6935 + 16.184 + 12.6285 + 6.000 + 10.000
              = 60.9935 → rounds to 61.0
```

# Quality Score = 61.0 — FAILS the 80.0+ gate, decisively (not a knife-edge case).

**Sensitivity check (shown transparently, "no black box"):** using the un-normalized GAAP Net Margin instead of the normalized figure raises the score to ~64.8; crediting a third Moat signal TRUE raises it further to ~67.8–70.8 depending on combination. **Every reasonable combination of these judgment calls still lands well below the 80.0 gate** — this is a robust FAIL, unlike the ±3.0-point knife-edge results seen for NOW, MSFT, and AVGO this cycle.

**This is UBER's first-ever computed Quality Score.** Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* Per [rescore.md](../.claude/commands/rescore.md) step 3, **this does not force an exit** for an existing holding — quality-gate failure alone is not one of strategy.md's four valid Phase 06 exit reasons — but it is flagged here as a **Phase 04 Quality Watch escalation**, the most significant new finding of this session. Per the established practice for existing holdings whose Quality Score fails the gate (AMZN/GOOG/MSFT/NKE/NOW 2026-07 sessions), the Valuation Score and a **reference-only** Composite Score are still computed below, explicitly flagged as not to be acted on at face value given the gate failure.

---

## 6. UBER — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 22.36 = 4.4723%
Spread = EY − 10Y Treasury = 4.4723% − 4.49% = −0.0177%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (short by ~1.52pp) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for UBER = +10**

---

## 7. UBER — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 6.47/10), 0, 100) = 35.30
```
→ Contribution: 35.30 × 0.40 = **14.12**

**EV/EBIT — 25% + 15% (PEG redistributed, §3 flag 4) = 40% weight**
```
EV/EBIT_Score = clamp((24.91 − 12)/23 × 100, 0, 100) = clamp(56.13, 0, 100) = 56.13
```
→ Contribution: 56.13 × 0.40 = **22.45**

**Forward PE — no-history fallback (§3 flag 3) — 20% weight**
```
FwdPE_Score = 50.0  (neutral midpoint, flagged — no meaningful 5yr PE range/average exists for a
   company that was GAAP-loss-making through FY2022, consistent with the 06-20 UBER session's
   own treatment)
```
→ Contribution: 50.0 × 0.20 = **10.0**

**PEG — 15% weight: N/A this session** (not a qualifying Fast Grower on a clean earnings base, §3 flag 4) — weight redistributed to EV/EBIT above.

**Raw weighted score:**
```
= 14.12 + 22.45 + 10.0 = 46.57
```
**+ Rate Modifier (+10) = 56.57** (before the Upside/Downside Modifier)

---

## 8. UBER — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture (new this session — UBER's GAAP EPS is too distorted by the one-off items in §3 flag 2 to build an EPS×PE scenario set reliably, so this session uses a P/FCF-multiple approach instead, consistent with FCF Yield already being the framework's dominant 40%-weighted input and with Uber's own guided operating metric of choice being Adjusted EBITDA/FCF rather than GAAP EPS):**

| Scenario | Weight | FY2026 FCF | Shares | FCF/share | Exit P/FCF | Rationale | Fair Value |
|---|---|---|---|---|---|---|---|
| **Bull** | 25% | $11.5B | 2.036B | $5.65 | 24× | Uber One scaling (50M members, half of Gross Bookings) and AV-partner monetization (Rivian, WeRide, MOIA) beat consensus FCF; market re-rates modestly toward growth-platform multiples, still below high-growth SaaS levels | $5.65 × 24 = **$135.60** |
| **Base** | 50% | $11.02B (consensus, stockanalysis.com) | 2.036B | $5.41 | 18× | Consensus FCF delivered; modest multiple expansion from today's implied ~15.5× TTM P/FCF (continued execution, no re-rating euphoria) | $5.41 × 18 = **$97.40** |
| **Bear** | 25% | $9.5B | 2.036B | $4.67 | 12× | AV-disruption risk, driver-reclassification/regulatory risk, delivery-competition pressure; multiple compresses below today's level | $4.67 × 12 = **$56.00** |

```
PW Fair Value = 0.25×135.60 + 0.50×97.40 + 0.25×56.00 = 33.90 + 48.70 + 14.00 = $96.60
```
Sits below the $104.48 analyst consensus mean PT (Guardrail 2 — never the rosy point) and comfortably inside the $70–$150 analyst range.

**Step 1 — Expected annual return E.**
```
Gap Upside %     = (96.60 ÷ 74.43) − 1                = +29.79%
Catalyst window  = 2 years (Rule 10 default — Uber One scaling, AV-partner monetization ramp, and
   the guided Adjusted EBITDA margin-expansion path are ongoing/multi-quarter rather than a single
   sharp near-term event, but are documented and within the 18–24mo window per management's own
   guidance cadence)
Annualized gap   = 29.79% ÷ 2                          = +14.90%
Intrinsic growth = +12.0%/yr  (conservative — below the raw trailing 17.73% revenue 3yr CAGR and
   below consensus FY2026 FCF growth of ~+12.5% off the TTM base, since much of the trailing rate
   reflects a smaller base-year effect)
Shareholder yield = +2.5%/yr  (net buyback yield only, no dividend — §4)

E = 14.90% + 12.0% + 2.5% = +29.40%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 29.40% ≥ H → M = −15 × clamp((29.40 − 10)/15, 0, 1) = −15 × clamp(1.293, 0, 1) = −15 × 1.0 = −15.0
```
**Modifier M = −15.0 (floored)** — same floor result as the 06-20 UBER session, though for a materially different underlying reason: 06-20's E (~+31%) was driven mostly by the price gap alone; this session's E (+29.4%) is spread more evenly across the annualized gap, intrinsic growth, and shareholder yield, with the price gap itself (+29.79% total, +14.90% annualized) actually a bit smaller than 06-20's citation.

**Guardrail checks:**
1. **Catalyst:** documented (Uber One scale-up, AV-partner monetization, guided margin path), within 18–24 months → upside credit allowed; not a knife-edge single-event catalyst, but sufficiently specific and company-guided. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($96.60) sits below the $104.48 analyst consensus mean. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** −15.0 sits exactly at the floor, within bounds. ✓

---

## 9. UBER — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (46.57) + Rate Modifier (+10) + Upside/Downside (−15.0)
                       = 41.57
```
Boundary rule: not a ".X5" case → **Final Valuation Score = 41.6**

| | Value |
|---|---|
| Raw weighted | 46.57 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −15.0 (floored; E = +29.40%) |
| **FINAL VALUATION SCORE** | **41.6** |
| Prior valuation score | 34.8 (06-20) |
| **Quality Score** | **61.0 (FAILS 80.0+ gate — decisively, see §5)** |

**Valuation Score band: 41.6 → 30.0–49.9 "Cheap" → nominally BUY, Standard position 3–5%** — this is a *different* situation from the NOW/NKE "false green light" pattern: there, the *raw* Valuation Score itself sat in the unattractive Hold band, and only blending in a failed Quality Score pulled the Composite into an attractive-looking band. Here, **the raw Valuation Score already looks cheap on its own, before any Quality blending** — which is exactly the scenario the 80.0+ Quality gate exists to catch: a statistically cheap multiple sitting on top of a business that doesn't clear this framework's quality bar is the textbook definition of a **value trap** (see glossary), not a case of the Composite Score manufacturing false attractiveness out of nothing.

**Composite Score — reference only, per the established practice for a Quality-Score-gate failure on an existing holding (AMZN/GOOG/MSFT/NKE/NOW 2026-07 sessions):**
```
Composite Score = 0.50×(100 − 61.0) + 0.50×41.6 = 0.50×39.0 + 0.50×41.6 = 19.5 + 20.8 = 40.3
```
**Composite Score = 40.3 — also lands in the "BUY — Standard position 3–5%" band (30.0–49.9), essentially the same band as the raw Valuation Score alone.** Unlike NOW/NKE, blending in the failed Quality Score doesn't materially change the action-table band here (both land in the same Cheap/Buy-Standard range) — but per [valuation-scoring.md](../framework/valuation-scoring.md), *"Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate"* regardless of which component is doing the work. **This Composite Score is NOT being adopted to drive the action recommendation below** — shown only for the record, per "no black box."

---

## 10. UBER — Action Recommendation

**Two independent facts, either one of which alone is enough to conclude HOLD/no-add:**

1. **The Quality Score (61.0) fails the 80.0+ gate decisively** (§5) — and because the *raw* Valuation Score already looked cheap on its own terms (not just the Composite), this is a genuine, first-order **value-trap flag**: a statistically cheap stock sitting on a business that doesn't clear this framework's quality bar, not merely a blending artifact. Per [rescore.md](../.claude/commands/rescore.md), an existing holding failing the gate is **not retroactively force-exited**, but is escalated as a **Phase 04 Quality Watch** item.
2. **The order-setup R/R check independently fails**, shown below for completeness (testing the nominally-attractive 30.0–49.9 "Cheap" band as if it were actionable):

```
Blended Fair Value (= PW FV):              $96.60
Margin of Safety (30.0–49.9 band):         28%  (same convention as the 06-20 UBER session)
BUY PRICE (limit):                         $96.60 × (1 − 0.28) = $69.55
PRIMARY SELL TARGET:                       $96.60
BULL-CASE TRIM TARGET (bull × 0.90):       $135.60 × 0.90 = $122.04
STOP LOSS (Buy × (1 − 28%)):               $69.55 × 0.72 = $50.08
R/R at formal entry = (96.60 − 69.55) ÷ (69.55 − 50.08) = 27.05 ÷ 19.47 = 1.389:1  ❌ below 2:1
R/R at live price   = (96.60 − 74.43) ÷ (74.43 − 50.08) = 22.17 ÷ 24.35 = 0.910:1  ❌ further below 2:1
```
**Both R/R checks fail the 2:1 minimum (Rule 6) — the same practical conclusion as the 06-20 session, which also failed this gate (1.39:1 then vs. 1.39:1 now — essentially unchanged).** Per Rule 6, R/R below 2:1 = do not enter, independent of score band or the Quality Score question.

**Net: HOLD the existing 0.42% position. No fresh capital added — doubly blocked, by an independent R/R failure and by the first-ever Quality Score's decisive gate failure.**

**Position cap check:** 0.42% is nowhere near the 15% hard cap (Upgrade 7) — not a binding constraint here, included only for completeness.

**Quality Watch escalation (Phase 04, new this session):** UBER's first-ever computed Quality Score (61.0) fails the 80.0+ gate by a wide, non-knife-edge margin. This does not meet the Full Exit bar (Phase 06 requires *sustained* fundamental deterioration or one of the other three specific triggers — none apply; the underlying business shows real strengths (17.7% revenue 3yr CAGR, 6.47% FCF yield, 0.63× net debt/EBITDA, FCF-positive every year since FY2023, a genuine two-sided-network moat signal, continued Gross Bookings/MAPC/Uber One growth) — the gate failure is driven specifically by **modest normalized profitability** (a normalized 6.77% net margin and 13.6% ROIC, once the one-off tax/equity items are backed out) and an **incomplete moat checklist** (2 of 5 signals credibly cited), not a sign of active deterioration. Recommend the user consider whether to log a **Human Override** entry in [override-log.md](../portfolio/override-log.md) (mirroring the ZS/NOW precedent for a held, quality-gate-failing position) — flagged here as an open item, not decided or written by this session (`override-log.md` is not edited here, per scope).

**Value-trap flag (new framing this session, distinct from the Quality Watch item above):** because UBER's *raw* Valuation Score already reads "Cheap" independent of any Quality blending, this is a cleaner example of the specific risk the 80.0+ gate is designed to catch than the NOW/NKE cases were — worth surfacing explicitly rather than only as a generic gate-failure note.

---

## 11. Next Review Trigger

- **Routine:** UBER Q2 2026 earnings, expected early August 2026 (unconfirmed exact date — will refresh every TTM fundamental used here, including a cleaner post-Q1'26-loss/post-Q3'25-gain TTM window less distorted by the one-off items in §3).
- **Open item (new, highest priority): the value-trap / Quality Watch flag (§10).** Recommend deciding whether to log a Human Override for this position, consistent with the NOW/ZS precedent, given the Quality Score's decisive (not knife-edge) gate failure.
- **Open data item:** the March 2024 US rideshare market-share citation (§3 flag 5, §5) is stale; a fresher independent share-tracker figure would tighten the Moat Signal's "Market share stable/growing" call, though §5's sensitivity check shows the overall gate result doesn't hinge on it.
- **Watch:** AV-partner monetization progress (Rivian robotaxi deployment target 2028, WeRide, MOIA) and Uber One's continued scale-up — both cited as this session's Growth-bonus and bull-case-scenario evidence; a slip in either would be a fair-value/scenario-architecture revisit, not necessarily a fresh Rule 9 event on its own.
- **Rule 9 triggers (standing):** guidance revision, M&A/material AV investment, management change, a >15% unexplained price move, or the Q2 2026 earnings print itself.

---

## Glossary

| Term | Meaning |
|---|---|
| **AV (Autonomous Vehicle)** | A self-driving vehicle; "robotaxi" refers specifically to an AV operated as an on-demand ride-hailing service. Uber partners with (rather than builds) AV developers — e.g. Rivian, WeRide, MOIA — to deploy AVs on its platform. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; shown as a **reference-only, not-adopted** number for UBER this session (61.0 Quality Score fails the gate). |
| **D&A** | Depreciation & Amortization. |
| **Deferred tax valuation allowance release** | A one-off GAAP accounting event reversing a prior write-down on deferred tax assets once a company judges them likely usable — inflates net income/EPS in the recognition period without cash impact. Identified as the driver of UBER's $4.9B Q3 2025 tax benefit (§3). |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — this framework's PEG-eligibility trigger; UBER does not qualify this session (§3). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Gross Bookings** | The total dollar value of activity transacted through Uber's platform (Mobility + Delivery + Freight) before Uber's own take-rate/revenue is deducted — Uber's primary top-line volume metric, distinct from (and larger than) reported Revenue. |
| **Gross Margin** | Gross Profit (Revenue − Cost of Revenue) ÷ Revenue. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; flagged (not adopted) as an open item for UBER this session. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **MAPC (Monthly Active Platform Consumers)** | The number of unique consumers who used at least one Uber offering (Mobility or Delivery) in a given month — Uber's core platform-reach metric, distinct from Gross Bookings (a dollar-volume metric) or MAU (a generic active-user count used by other companies). |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Multi-homing** | When users on one or both sides of a platform routinely use multiple competing platforms rather than committing to just one — cited here (per Uber's own 10-K) as evidence against a rideshare "switching costs" moat signal, the same caveat previously applied to Trainline (TRN). |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **P/FCF (Price-to-Free-Cash-Flow)** | Market capitalization ÷ Free Cash Flow — an earnings-multiple analog used in this session's Upside/Downside scenario architecture in place of an EPS×PE approach, since UBER's GAAP EPS is too distorted by one-off items (§3) to build a reliable scenario set from. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. UBER's first-ever computation this session: 61.0 (fails the gate, decisively). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **Robotaxi** | An autonomous vehicle operated as an on-demand ride-hailing service — see AV above. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; normalize before valuing / require a minimum 2:1 risk/reward; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **Value trap** | A stock that looks statistically cheap but stays cheap (or keeps falling) because the underlying business quality is deteriorating or was never strong enough to support a re-rating — the specific risk this session's Quality Score gate failure is flagged as an example of, since UBER's *raw* Valuation Score already looked cheap independent of any Quality blending. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |
