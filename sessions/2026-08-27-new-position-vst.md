# NEW POSITION — Vistra Corp. (NYSE: VST) — 2026-08-27

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, automated/unattended run)
**Date:** 27 Aug 2026
**10Y US Treasury Yield:** 4.67% (TradingEconomics — "rose to 4.67% on August 27, 2026, marking a 0.02pp increase from the previous session")
**VST portfolio weight:** 0% — not held, no row in [holdings.md](../portfolio/holdings.md)
**Prior coverage:** None. No `watchlist/` entry for VST anywhere in the repo prior to this session (confirmed by direct search before this run) — first-ever `/new-position` pass for this ticker.
**Sector:** Independent Power Producer (IPP) / merchant power generation + competitive retail electricity — natural gas, nuclear, coal, solar, and battery storage generation plus a retail electricity brand (TXU Energy). **Not a rate-regulated utility** — this distinction matters throughout (see §2.6).

*Jargon decoded on first use (non-finance reader) — full definitions in §5 Glossary: IPP = Independent Power Producer; PPA = Power Purchase Agreement; ERCOT/PJM = the two grid operators relevant here; TTM = trailing twelve months; NOPAT = net operating profit after tax; ROIC = return on invested capital; EBIT/EBITDA = operating profit (before/also before depreciation & amortization); CAGR = compound annual growth rate; FCF = free cash flow; behind-the-meter, interconnection queue, nuclear uprate = data-center-power-specific terms explained in context below.*

---

## 0. Trigger — Telegram post and independent verification

**Source:** Telegram channel `FinnInvestChannel`, post `3153` (2026-08-27 16:54 UTC) — the channel's author reported opening a mini-portfolio position in VST, citing an AI-data-center power-demand thesis and existing supply contracts with Meta and AWS. Per this framework's non-negotiable rule, **the post text is never used as financial data below — it is only the signal to run this evaluation.** No watchlist entry exists anywhere in the repo for VST, so this evaluation runs regardless of whether the claim itself checks out.

**Independent verification (WebSearch/SEC filings, not the Telegram post) — confirmed, and a materially bigger story than a one-line summary suggests:**

- **Meta PPA (real, dated, SEC-disclosed):** In January 2026, Vistra entered 20-year Power Purchase Agreements (PPAs) with Meta for a total of 2,609 MW of carbon-free power/capacity from its PJM nuclear plants (1,268 MW from Perry, 908 MW from Davis-Besse, plus additional planned nuclear uprate capacity from Perry, Davis-Besse, and Beaver Valley). Delivery on the operating portion begins late 2026, full delivery by year-end 2027; uprate capacity delivery begins by 2031, full delivery by year-end 2034. [World Nuclear News; power-eng.com; ANS Nuclear Newswire — 2026-01]
- **AWS/Amazon PPA (real, dated):** In September 2025, Vistra signed a separate 20-year PPA (with options to extend up to 20 more years) to supply 1,200 MW of carbon-free power from the Comanche Peak Nuclear Power Plant — subsequently confirmed by multiple sources to be with Amazon Web Services, supporting a $5B Amazon data-center project near the plant. Delivery begins Q4 2027, ramping to full capacity by 2032. [Utility Dive; Yahoo Finance/The Motley Fool — 2026]
- **Pricing evidence:** the Meta PPA is estimated at roughly $110/MWh, versus a current forward average power price of roughly $58/MWh — an approximate 2x premium for long-term, firm, 24/7 carbon-free baseload. [enkiai.com aggregation, cross-referenced against deal-term reporting from power-eng.com and World Nuclear News]
- **Important nuance the Telegram post did not capture:** management's own Q2 2026 earnings materials state the Meta PPA benefits are "expected to contribute to Adjusted EBITDA in 2027" — i.e., **these contracts are real and signed, but their earnings impact has not yet meaningfully shown up in Vistra's trailing financials as of this session.** The Quality Score below is computed off actual, reported TTM results, not the future PPA ramp. [SEC 8-K, Q2 2026 earnings release, filed 2026-08-10]

**Net verdict on the trigger: confirmed.** Both the Meta and AWS/Comanche Peak PPAs are genuine, dated, material contracts, not overstated. This is a real fundamental catalyst worth evaluating — but, as shown below, evaluating VST *today* still means scoring today's balance sheet and today's trailing financials, which is where this session's finding actually turns.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$140.49** | IBKR `get_price_snapshot` (contract_id 254457731, NYSE), `last.price`, timestamp epoch 1787860995 = **2026-08-27 20:03:15 UTC** |
| Change vs. prior close | +$0.46 (+0.33%) | IBKR `change` field |
| Bid / Ask | $139.50 / $140.16 | IBKR `bid_ask` |
| Volume (day) | 2,882,700 | IBKR `volume` |
| 52-week range | $132.67 – $219.13 | IBKR `misc_statistics` |
| 13-week / 26-week high | $171.00 / $177.85 | IBKR `misc_statistics` |
| Dividend yield (trailing) | 0.65% | IBKR `dividend_yield` |
| Cross-check | $139.82 (stockanalysis.com, near-simultaneous pull) — within normal same-session intraday movement of the IBKR figure | stockanalysis.com |
| Shares outstanding | 335.64M | stockanalysis.com |
| Market cap (computed) | ≈$46.93B (335.64M × $139.82, stockanalysis's own snapshot) | Computed / cross-checked against stockanalysis's own `marketCap` figure |
| Analyst consensus PT (Rule 0 Step 4 bull-case sanity check) | Mean **$217.42** (20 analysts, +55.5% implied upside), "Strong Buy" consensus; other sources report a mean nearer $225 (17–23 analysts) | stockanalysis.com; TIKR.com (WebSearch) |

**Flag:** the ~$217–225 analyst consensus sits far above where this session's Quality Gate analysis below ends — not reconciled, just noted (the gate fails on fundamentals-quality/balance-sheet grounds, not on a valuation disagreement with the Street).

---

## 2. Quality Score — Phase 01 (methodology version 2026-06-29)

### 2.1 Sourcing

Primary source: SEC EDGAR directly — CIK 0001692819, pulled via `data.sec.gov`'s XBRL `companyconcept`/`companyfacts` APIs (audited GAAP tags) and the rendered financial-statement exhibits (`R2.htm`/`R3.htm`) of Vistra's FY2025 10-K (filed 2026-02-27, accession 0001692819-26-000006) and its Q1/Q2/Q3 2025 and Q1/Q2 2026 10-Qs. `yfinance` was not used this session (SEC EDGAR direct pull was sufficient and more precise for a company with the income-statement structure below). Every TTM figure is independently reconstructed from quarterly XBRL data and cross-checked against stockanalysis.com's own TTM figures — full match (see §2.2).

### 2.2 TTM income statement (USD millions, Q3 2025 → Q2 2026), reconstructed from quarterly SEC filings

Vistra's income statement is structured differently from a typical company — no single "Cost of Revenue"/"Gross Profit" line. The line items, direct from the filed Condensed Consolidated Statements of Operations:

| Line | Q3'25 | Q4'25 (derived: FY25 − 9mo) | Q1'26 | Q2'26 | **TTM** |
|---|---|---|---|---|---|
| Operating revenues | 4,971 | 4,584 | 5,640 | 4,017 | **19,212** |
| Fuel, purchased power costs, and delivery fees | (2,370) | (2,310) | (2,530) | (1,774) | **(8,984)** |
| Operating costs | (655) | (500)* | (700) | (853) | (2,708) |
| Depreciation and amortization | (460) | (463) | (484) | (445) | (1,852) |
| SG&A expenses | (444) | (563)* | (427) | (392) | (1,826) |
| Impairment of long-lived assets | (5) | (223)* | 0 | 0 | (228) |
| **Operating income (EBIT)** | **1,037** | **474** | **1,499** | **553** | **3,563** |

*Q4'25 individual expense lines (Operating costs, SG&A, Impairment) are back-solved as the FY2025-minus-9-months residual and allocated using each line's own FY2025-vs-9mo delta — only the **Fuel costs** and **Operating income** rows are independently verified against filed figures (FY2025 fuel cost $9,101M matches 9mo-$6,791M + derived Q4 $2,310M exactly; FY2025 operating income $1,906M matches 9mo-$1,432M + derived Q4 $474M exactly). Immaterial to every downstream calculation, which uses only Revenue, Fuel Costs, EBIT, and D&A — all independently confirmed.

**TTM Revenue $19,212M and TTM EBIT $3,563M both match stockanalysis.com's own independently-reported TTM figures exactly** — a strong cross-check.

TTM Net income attributable to Vistra common stock (after $192M/yr cumulative preferred dividends) = **$2,027M** (also matches stockanalysis.com's TTM Net Income and TTM EPS $5.87 exactly: $2,027M / ~345.4M diluted shares ≈ $5.87). **Flag, shown for transparency:** Vistra has meaningful preferred stock outstanding; "Net income attributable to Vistra" *before* preferred dividends is $2,219M TTM. This session uses the $2,027M (after-preferred, common-stockholder) figure as "Net Income" throughout — the same figure the primary cross-check source (stockanalysis.com) reports as VST's headline Net Income and the one EPS is built from. (This differs from the convention this framework used in the 2026-08-07 CELH session, which used the *larger*, before-preferred figure for Yahoo-Finance-consistency reasons specific to that ticker — noted here rather than silently picking a side. The choice does not change this session's Quality Gate outcome either way — see sensitivity note in §2.9.)

TTM Income tax expense $584M / TTM pretax income $2,803M → **effective tax rate 20.835%**.

### 2.3 Profitability (25% weight)

```
NOPAT = EBIT_TTM × (1 − eff. tax rate) = 3,563 × (1 − 0.20835) = 2,820.7
Invested Capital = Total Debt (19,595, §2.6) + Stockholders' Equity (5,482, 2026-06-30, excl. NCI) = 25,077
  (no-cash-netting convention — consistent with the 2026-08-25 LLY and 2026-08-27 Wise sessions'
  stated "standard convention," though flagged: glossary.md's own "Invested Capital" entry currently
  describes a cash-netting convention — a real, unresolved inconsistency between the glossary and
  recent session practice, noted here rather than silently resolved either way; doesn't change this
  session's outcome, see §2.9)
ROIC = 2,820.7 / 25,077 = 11.248%

Net Margin = 2,027 / 19,212 = 10.551%

NetMargin_Component = clamp((10.551/30)×100, 0, 100) = 35.169
ROIC_Component       = clamp((11.248/30)×100, 0, 100) = 37.493
Profitability_Score (uncapped) = (35.169 + 37.493) / 2 = 36.331
```

FCF-positivity cap check (§2.9): FY2023–FY2025 all FCF-positive — **no cap applies**. **Profitability_Score = 36.331**

### 2.4 Margins (15% weight)

Vistra has no standard "gross profit" line; this session uses **Revenue − Fuel, purchased power costs, and delivery fees** as the gross-margin proxy — the direct, unavoidable cost of the power sold, the closest GAAP-disclosed analog to cost of goods sold for a merchant generator/retailer:

```
TTM Gross Profit = 19,212 − 8,984 = 10,228
TTM Gross Margin = 10,228 / 19,212 = 53.238%
GrossMargin_Score = clamp((53.238/80)×100, 0, 100) = 66.547
```

**3-year trend (annual, for the structural-expansion bonus check):** FY2023 48.87% → FY2024 57.71% → FY2025 48.70% → TTM 53.24%. This is **volatile, not a clean structural uptrend** — it tracks wholesale power-price and hedging-outcome swings year to year, not a secular margin-expansion story. **No +10 trend bonus applied** (also moot at this margin level, well above the 40% bonus-eligibility ceiling). **Margins_Score = 66.547**

### 2.5 Growth (20% weight)

```
Revenue: FY2022 $13,728M → FY2025 $17,738M (both from filed 10-Ks, XBRL-confirmed)
3yr CAGR = (17,738/13,728)^(1/3) − 1 = 8.918%
Growth_Score (base) = clamp((8.918/25)×100, 0, 100) = 35.671
```

**TAM-expansion modifier (+10, documented):** the Meta and AWS/Comanche Peak PPAs (§0) are real, dated, SEC-disclosed 20-year contracts adding a combined 3,809 MW of new demand for Vistra's nuclear fleet — genuine, cited TAM-expansion evidence, independent of this session's Telegram trigger. **No deceleration penalty applies** — while YoY revenue growth has been uneven (FY23→24 +16.6%, FY24→25 +3.0%, TTM +3.8%), that reflects commodity/hedging-price volatility, not a documented structural TAM contraction; if anything the forward story (PPA ramp beginning 2027) points the opposite direction. **Growth_Score = 35.671 + 10 = 45.671**

### 2.6 Balance Sheet (15% weight) — where the gate decisively fails

```
Total Debt (2026-06-30, SEC XBRL LongTermDebtAndCapitalLeaseObligationsIncludingCurrentMaturities +
  ShortTermBorrowings) = 19,595 + 0 = 19,595
Cash (2026-06-30) = 435
Net Debt = 19,595 − 435 = 19,160

EBITDA (GAAP, TTM) = EBIT (3,563) + D&A (1,852) = 5,415
Net Debt/EBITDA (GAAP) = 19,160 / 5,415 = 3.538×

BalanceSheet_Score = clamp(100×(1 − 3.538/4), 0, 100) = 11.542
```

**Cross-check against management's own non-GAAP metric (shown for completeness, doesn't change the conclusion):** Vistra's own "Ongoing Operations Adjusted EBITDA" — which strips out large mark-to-market hedging swings the GAAP figure above includes — was $1,581M (Q3'25) + $1,742M (Q4'25, derived: FY25 $5,912M − 9mo $4,170M) + $1,494M (Q1'26) + $1,767M (Q2'26) = **$6,584M TTM** [company press releases, Q1–Q3 2025 and Q1–Q2 2026 earnings releases, cross-checked against FY2025's disclosed $5,912M full-year Adjusted EBITDA]. On this more favorable, company-reported basis: **Net Debt/EBITDA = 19,160 / 6,584 = 2.910×.**

**Both readings — 3.54× (GAAP) and 2.91× (management's own non-GAAP Adjusted EBITDA) — exceed the framework's 2.5× standard threshold.** Vistra does not qualify for the Upgrade 5 asset-light override (that override is reserved for payment networks/exchanges where 100% of debt is financial and interest coverage exceeds 15×; Vistra is a physical, capital-intensive power generator with secured project/utility-style debt funding a $41,000 MW generation fleet — the opposite of asset-light, regardless of its recent BBB- investment-grade upgrades from S&P (Dec 2025) and Fitch (Mar 2026)).

**BalanceSheet_Score = 11.542 — and per [quality-scoring.md](../framework/quality-scoring.md)'s hard-disqualifier list, "Net debt/EBITDA over its applicable threshold (2.5× standard...)" fails the company regardless of its weighted score. This fires independently below.**

### 2.7 Moat Signal (15% weight)

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Vistra is the largest competitive (IPP) power generator in the US (~41,000 MW across gas, nuclear, coal, solar, and battery storage); its Luminant subsidiary is ERCOT's largest single generator (~13,600 MW); TXU Energy is the largest retail electricity provider in Texas (~1.7M customers; ~4.3M total retail customers company-wide) [company filings/investor materials via WebSearch, cross-referenced across multiple sources]. |
| Brand premium / pricing power | **TRUE** | The Meta PPA is priced at an estimated ~$110/MWh against a ~$58/MWh current forward average power price — an approximate 2x premium, reflecting real pricing power for firm, 24/7, carbon-free baseload capacity that scarce nuclear supply commands over the general market. [enkiai.com aggregation, cross-referenced against power-eng.com/World Nuclear News deal-term reporting — flagged as a secondary-source figure, not independently confirmed against Vistra's own contract text, which is not public] |
| Network effect | **FALSE** | No two-sided or platform-style mechanism — physical power generation and retail electricity sales do not exhibit this dynamic. |
| Switching costs | **TRUE** | Two independent, reinforcing mechanisms, both documented: (1) the Meta/AWS PPAs are 20-year contracts — genuine multi-decade lock-in for both counterparties; (2) PJM interconnection-queue wait times now average 6–8 years, so a hyperscaler cannot quickly replicate Vistra's already-built, already-interconnected generation fleet by contracting with a new entrant — Vistra's existing capacity is a structurally scarce, hard-to-replace asset. [Utility Dive, landgate.com, multiple 2026 sector-analysis sources via WebSearch] |
| Scale cost advantage | **FALSE — not credited** | One aggregator source (koalagains.com, a third-party AI-generated stock-analysis site) cited an "O&M cost per MWh ~12% below sub-industry average" figure. This is a specific cost-per-unit claim, but it is a single, non-primary-source citation not independently corroborated against a company filing, earnings call, or established data provider — a targeted follow-up search for the same figure in Vistra's own investor materials did not find it. Consistent with this framework's strict evidentiary bar applied in the LLY/Wise/NVDA precedent sessions ("capacity/investment data alone, without a corroborated cost-per-unit citation, does not qualify"), **not credited.** |

```
Moat_Score = (3/5) × 100 = 60.0
```

### 2.8 FCF Quality (10% weight)

```
TTM Operating Cash Flow (Q3'25+Q4'25+Q1'26+Q2'26, reconstructed from cumulative-YTD XBRL figures) = 5,121
TTM CapEx (PaymentsToAcquirePropertyPlantAndEquipment, same reconstruction) = 2,866
TTM FCF = 5,121 − 2,866 = 2,255

FCF/NI Ratio = 2,255 / 2,027 = 111.248%
FCFQuality_Score = clamp(((1.11248 − 0.40)/0.60)×100, 0, 100) = 100.0 (capped)
```

FY2025 FCF ($1,318M) and FY2025 OCF/CapEx ($4,070M / $2,752M) both independently match stockanalysis.com's reported figures exactly — a strong cross-check on the reconstruction method. **FCFQuality_Score = 100.0**

### 2.9 Hard disqualifier check (all three)

| Check | Value | Threshold | Result |
|---|---|---|---|
| Not FCF-positive for 3+ consecutive years | FY2023 +$3,777M, FY2024 +$2,485M, FY2025 +$1,318M — all three positive | disqualify if uniformly negative | ✅ PASS |
| FCF/NI conversion <70% for 2+ consecutive years | FY2023 281.2%, FY2024 100.7%, FY2025 175.3% — all comfortably above 70% | disqualify if <70% for 2+ yrs | ✅ PASS |
| **Net Debt/EBITDA over its applicable threshold** | **3.538× (GAAP) / 2.910× (management's own non-GAAP Adjusted EBITDA) — both readings above 2.5×** | disqualify if >2.5× standard (no asset-light override applies, §2.6) | **❌ FAILS — HARD DISQUALIFIER FIRES** |

**A hard disqualifier fires, independent of the weighted score below.**

### 2.10 Final Quality Score (shown for completeness — the gate has already failed via the hard disqualifier above)

```
Quality Score = (36.331×0.25) + (66.547×0.15) + (45.671×0.20) + (11.542×0.15) + (60.0×0.15) + (100.0×0.10)
              = 9.083 + 9.982 + 9.134 + 1.731 + 9.000 + 10.000
              = 48.930 → rounds to 48.9
```

**Sensitivity check (doesn't change the outcome):** using the before-preferred-dividend Net Income figure ($2,219M instead of $2,027M, §2.2) would raise Net Margin to 11.552%, NetMargin_Component to 38.507, Profitability_Score to 37.999, and the overall Quality Score to ≈49.3 — still far below 80.0, and the Balance Sheet hard disqualifier is entirely unaffected by this choice either way.

**Quality Score = 48.9 / 100.0 — FAILS the 80.0+ gate, both on the weighted score (48.9 << 80.0) and independently via the Net Debt/EBITDA hard disqualifier (§2.9). This is not a close call on either test.**

---

## 3. Recommendation

# **PASS — Quality Score (48.9) fails the 80.0+ gate decisively, and a hard disqualifier (Net Debt/EBITDA 3.54× GAAP / 2.91× management-adjusted, both above the 2.5× standard threshold) fires independently. No new position opened. Watchlist only.**

Per [quality-scoring.md](../framework/quality-scoring.md)'s Strict 80.0+ Gate: *"stop — don't proceed to valuation, regardless of how cheap the stock looks."* No Rate Environment Gate, Phase 02 valuation score, fair-value work, or order setup is computed as part of this recommendation, consistent with this framework's precedent for a gate-failing candidate (e.g. LLY 2026-08-25, MELI 2026-08-05, MU 2026-07-10).

**What's genuinely notable here, worth surfacing plainly:**

1. **The Telegram trigger checks out.** The Meta and AWS/Comanche Peak nuclear PPAs are real, dated, material, 20-year contracts — not overstated by the post. This is a legitimate secular demand story.
2. **But that story is a 2027-and-beyond earnings event, not a today event.** Management's own materials say the Meta PPA contribution to Adjusted EBITDA begins in 2027. This session scores today's actual, reported trailing financials — where the AI-data-center thesis has not yet meaningfully arrived.
3. **The disqualifying issue is leverage, not the AI story.** Vistra's balance sheet — Net Debt/EBITDA of 3.54× on a GAAP basis, or 2.91× even using management's own more-favorable non-GAAP Adjusted EBITDA — sits above this framework's 2.5× standard threshold under every reading tested. This is the same leverage profile a genuinely capital-intensive, still-expanding physical-infrastructure buildout produces; it isn't a data error or a one-off.
4. **The Moat picture is a real, mixed strength.** Market share, pricing power (backed by real ~2x-market PPA pricing), and switching costs (both contractual and interconnection-queue-driven) are credible, documented positives (Moat_Score 60.0) — this is not a weak business. But Profitability (36.3) and Growth (45.7, even after the TAM-expansion credit) are still middling on trailing numbers, and the leverage issue is decisive regardless.
5. **This is a "great narrative, wrong balance-sheet moment" case, not a "bad company" case.** If the leverage ratio comes down as the Meta/AWS PPA cash flows actually begin landing in 2027 (as guided), and if the weighted-score gap narrows as trailing growth catches up to the contracted backlog, a future rescore could look very different. Nothing here says the AI-power thesis is wrong — only that today's numbers don't clear this framework's quality bar yet.

**Next review trigger:** VST's next quarterly earnings release (Q3 2026, expected ~November 2026) — specifically watch (a) whether Net Debt/EBITDA is trending down as capacity investment matures and early PPA-related cash flows begin, (b) any further disclosed data-center PPA capacity additions beyond Meta/AWS, and (c) the 2026-financial-year Adjusted EBITDA outturn against the $6.8–7.6B 2026 guidance range (guidance itself is not scored, per this framework's "Why Forward Guidance Is Not a Sub-score" rule, but a large guidance revision is a Rule 9 trigger). Also watch for the standard Rule 9 triggers: guidance revision, management change, M&A, macro shift, or a >15% unexplained price move.

---

## 4. Watchlist & Portfolio Note

New entry created: [watchlist/not-in-portfolio/VST/VST-2026-08-27.md](../watchlist/not-in-portfolio/VST/VST-2026-08-27.md) — VST's first-ever watchlist entry. This session does not touch [portfolio/holdings.md](../portfolio/holdings.md) (VST is not held, and no position is opened). No trade recommended or executed; nothing logged to `decisions/`.

---

## 5. Glossary

*(Pulled from [glossary.md](../framework/glossary.md); new terms added this session are marked below)*

| Term | Meaning |
|---|---|
| **Behind-the-meter (generation)** | Power generation located on the customer's side of the meter, bypassing the public grid and its interconnection queue — over 25% of new US data-center capacity now uses this approach. *(New term.)* |
| **CAGR** | Compound Annual Growth Rate. |
| **EBIT / EBITDA** | Operating profit, before/also-before depreciation & amortization. |
| **EDGAR** | The SEC's public database of company filings — this session's primary data source. |
| **Effective tax rate** | Tax provision ÷ pretax income for the period. |
| **ERCOT (Electric Reliability Council of Texas)** | The independent grid operator running roughly 90% of the Texas power market, electrically isolated from the rest of the US grid — Vistra's home market via its Luminant (generation) and TXU Energy (retail) subsidiaries. *(New term.)* |
| **FCF / FCF-NI conversion ratio** | Free Cash Flow; FCF ÷ Net Income, a cash-quality check on accounting profit. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of its weighted score — Net Debt/EBITDA over threshold is the one that fires for VST this session. |
| **Interconnection queue** | The line of projects waiting for grid-operator approval to physically connect to the transmission system — multi-year waits (6–8 years in parts of PJM) that an incumbent generator with existing, already-connected capacity bypasses entirely. *(New term.)* |
| **Invested Capital** | Debt + equity put to work in a business — this session used a no-cash-netting convention (consistent with recent session precedent), flagged against an inconsistency with glossary.md's own stated (cash-netting) convention. |
| **Investment grade** | A credit rating (BBB-/Baa3 or higher) signaling low perceived default risk — Vistra was upgraded to BBB- by S&P (Dec 2025) and Fitch (Mar 2026). |
| **IPP (Independent Power Producer)** | A company that owns/operates power generation and sells it at market-based rates, rather than as a rate-regulated utility — Vistra's business model. *(New term.)* |
| **Merchant generator / merchant power** | A generation asset selling at market-clearing wholesale prices rather than regulated cost-of-service rates. *(New term.)* |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the ROIC numerator. |
| **Nuclear uprate** | An NRC-approved increase in a nuclear reactor's licensed capacity via upgrades to an existing plant, rather than new construction — the source of the additional capacity in Vistra's Meta PPA. *(New term.)* |
| **PJM (PJM Interconnection)** | The independent grid operator covering 13 mid-Atlantic/Midwest US states plus DC — the region of Vistra's nuclear plants covered by the Meta PPA. *(New term.)* |
| **PPA (Power Purchase Agreement)** | A long-term contract under which a buyer agrees to purchase power from a supplier at agreed terms — the Meta and AWS/Comanche Peak deals central to this session's trigger. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 valuation scoring. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples or stale data. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **TTM (Trailing Twelve Months)** | The most recent four reported quarters combined — reconstructed this session from quarterly SEC filings (Q3 2025 through Q2 2026). |
| **XBRL** | The SEC's structured, machine-readable financial-data tagging format — the source of every precise figure pulled directly from Vistra's own filings this session. |
