# NEW POSITION — CrowdStrike Holdings, Inc. (CRWD) — 2026-07-22

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, automated/unattended run)
**Date:** 22 Jul 2026
**10Y US Treasury Yield:** 4.63% (most recent posted level on record in this repo, 2026-07-21 close — context only, **not used**: this session stops at the Quality Gate below, before the Rate Environment Gate would apply)
**CRWD portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)
**Prior coverage:** none. No watchlist entry exists anywhere for CRWD (checked both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` — confirmed absent), and no prior `sessions/` file evaluates it. Per the `/telegram-scan` decision rule, the *absence* of any watchlist entry is sufficient on its own to trigger a full `/new-position` evaluation, independent of how material the specific triggering news item is.
**Sector:** Technology — Cybersecurity (cloud-native endpoint/identity/cloud security platform)

---

## 0. Why this session exists — trigger source

Telegram channel `FinnInvestChannel`, post `FinnInvestChannel/2973` (2026-07-22): mentioned a CrowdStrike + Cerebras partnership announcement (deploying Falcon AI Detection and Response models on Cerebras infrastructure). Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. The claimed partnership was independently verified (not taken at face value):

CrowdStrike (NASDAQ: CRWD) and Cerebras Systems (NASDAQ: CBRS) announced a strategic partnership on **22 July 2026**: CrowdStrike will leverage Cerebras's inference speed to help power **Falcon AI Detection and Response (AIDR)**, while Cerebras itself standardizes on the Falcon platform to secure its own business. This extends CrowdStrike's leadership in the AIDR category it says it pioneered to secure AI models/agents/identities. Real-time, machine-speed inference is positioned as critical because AI-driven attacks unfold in seconds. Confirmed via multiple independent outlets: [The Manila Times / GlobeNewswire](https://www.manilatimes.net/2026/07/22/tmt-newswire/globenewswire/crowdstrike-and-cerebras-partner-to-power-ai-detection-and-response-on-the-worlds-fastest-inference/2389483), [StockTitan](https://www.stocktitan.net/news/CBRS/crowd-strike-and-cerebras-partner-to-power-ai-detection-and-response-c0z2mpeoumzb.html), [Benzinga](https://www.benzinga.com/markets/large-cap/26/07/60616587/crowdstrike-partners-with-cerebras-to-boost-ai-cybersecurity).

**Verdict on the trigger:** accurate — a real, same-day product/partnership announcement, not a material fundamental event on its own (a go-to-market/product integration announcement, not an earnings or guidance event), but the watchlist-absence trigger fires regardless of the news item's materiality, so a full evaluation proceeds below.

---

## 1. Live Price (Rule 0) and contract lookup

| Field | Value | Source |
|---|---|---|
| Contract lookup | contract_id **370757467**, NASDAQ, symbol CRWD, "CROWDSTRIKE HOLDINGS INC - A" | IBKR `search_contracts` query "CRWD" |
| **Live price used** | **$188.50** (last trade) | IBKR `get_price_snapshot`, contract_id 370757467, ts 1784750396 → **2026-07-22 19:59:56 UTC**, `is_close: false`, `halted: false`, bid/ask $188.00/$188.46 |
| Today's intraday change | −$2.65 / −1.39% vs. yesterday's close ($191.15) | IBKR `change` field |
| 52-week range | **$85.68 (low) – $217.50 (high)** | IBKR `misc_statistics` |
| Price 52 weeks ago (`open_52w`) | $120.375 | IBKR `misc_statistics` |
| YTD change | +60.85% (+$71.31) | IBKR `year_to_date_change` |
| Dividend yield | 0.0% (no dividend) | IBKR snapshot |

No inference from multiples — price fetched live and first, per Rule 0.

---

## 2. Phase 01 — Quality Score (2026-06-29 methodology)

### 2.1 Data sourcing

`yfinance` (`pip install --quiet yfinance lxml`; `YF_DISABLE_CURL_CFFI=1` env var set — the curl_cffi TLS-impersonation backend was unavailable in this sandbox, so `yfinance` fell back to a plain `requests` session, which still returned live, complete data on this run) — quarterly financials/cashflow/balance-sheet, summed into TTM. **Cross-verified against stockanalysis.com** (revenue, net income, gross margin, FCF, OCF, CapEx, SBC — all independently pulled via `WebFetch`) for every figure used below; both sources agree to within normal reporting/rounding tolerance (see notes per line item). CrowdStrike's fiscal year ends **31 January**; the TTM window used is Q1 FY2027 + Q4 FY2026 + Q3 FY2026 + Q2 FY2026 (quarters ending 2026-04-30, 2026-01-31, 2025-10-31, 2025-07-31).

### 2.2 TTM figures (as of quarter ended 2026-04-30)

| Metric | yfinance (self-summed TTM) | stockanalysis.com (TTM) | Used |
|---|---|---|---|
| Revenue | $5,094.200M | $5,094M | **$5,094.2M** |
| Gross Profit | $3,822.137M | $3,818M | **$3,822.137M** (75.03% margin) |
| GAAP Operating Income | −$199.236M | −$219.92M | **−$199.236M** (self-summed from quarterly filings; both sources solidly negative, same sign/magnitude — used as the EBIT basis, see §2.4 note) |
| Net Income | −$24.521M | −$24.89M | **−$24.521M** |
| EBITDA | $106.085M (self-derived: Operating Income + TTM D&A of $305.321M) | $85.4M | **$106.085M**, self-derived and shown in full — see reconciliation note below |
| Free Cash Flow | $1,431.313M | $1,505M | **$1,431.313M** (self-summed from quarterly OCF−CapEx, internally consistent: OCF $1,819.179M − CapEx $387.866M = FCF $1,431.313M) |
| Operating Cash Flow | $1,819.179M | $1,819M | **$1,819.179M** |
| CapEx | −$387.866M | −$313.98M | **−$387.866M** (self-summed from quarterly filings; stockanalysis's TTM CapEx figure diverges more than other lines — flagged, doesn't change any conclusion since CapEx/Revenue is ~6–8% either way, not "elevated growth capex" territory) |
| Stock-Based Compensation (SBC) | $1,146.721M | $1,147M | **$1,146.721M** |

**EBITDA reconciliation note:** vendor EBITDA figures for CRWD vary widely by definition (some strip stock-based comp or other items as "adjusted EBITDA," which this framework does not use per its "guidance/self-reported non-GAAP metrics aren't scored" convention). The $106.085M figure above is self-derived directly from GAAP Operating Income + D&A (both pulled from raw quarterly statement line items), and is reasonably close to stockanalysis.com's $85.4M independent figure (same sign, same order of magnitude — the ~$21M gap is immaterial to every downstream calculation below, since Net Debt is deeply negative regardless of which EBITDA figure is used — see §2.6).

### 2.3 Balance sheet (as of 2026-04-30)

| Metric | Value | Source |
|---|---|---|
| Total Debt | $821.343M | yfinance quarterly balance sheet |
| Cash & Equivalents | $4,552.801M | yfinance quarterly balance sheet |
| **Net Debt** | **−$3,731.458M** (net cash position) | Computed |
| Invested Capital | $5,379.720M | yfinance quarterly balance sheet |
| Stockholders' Equity | $4,633.877M | yfinance quarterly balance sheet |

### 2.4 Profitability (25% weight)

```
NetMargin_Component = clamp((Net Margin% / 30) × 100, 0, 100)
  TTM Net Margin = −24.521 / 5,094.2 = −0.4815%
  NetMargin_Component = clamp((−0.4815/30)×100, 0, 100) = 0.0

ROIC_Component = clamp((ROIC% / 30) × 100, 0, 100)
  NOPAT = EBIT × (1 − tax rate)
```

**Tax-rate note:** TTM Tax Provision ($6.167M) exceeds TTM Pretax Income ($1.961M), producing a nonsensical 314% "effective tax rate" off a near-zero denominator — not usable. Per Rule 6 ("normalize before you value"), a statutory 21% US federal rate is used instead as a defensible standard substitute, flagged explicitly rather than silently plugging in the distorted figure.

```
  EBIT basis = GAAP Operating Income (TTM) = −$199.236M  (standard, unambiguous definition;
    yfinance's separate "EBIT" info-field line returned a materially different, positive figure
    or the same period, likely reflecting a different non-operating-item treatment in that
    specific pre-aggregated field — the raw, self-summed GAAP Operating Income from the
    quarterly statements is used instead as the more standard and defensible basis)
  NOPAT = −199.236 × (1 − 0.21) = −$157.4M
  ROIC = −157.4 / 5,379.720 (Invested Capital) = −2.93%
  ROIC_Component = clamp((−2.93/30)×100, 0, 100) = 0.0

Profitability_Score = (0.0 + 0.0) / 2 = 0.0
```

No FCF-positivity cap applies (CrowdStrike **is** FCF-positive 3+ consecutive years — see §2.7) — the 0.0 above is the raw margin/ROIC result, not a cap.

### 2.5 Margins (15% weight)

```
GrossMargin_Score = clamp((Gross Margin% / 80) × 100, 0, 100)
  TTM Gross Margin = 3,822.137 / 5,094.2 = 75.03%
  GrossMargin_Score = clamp((75.03/80)×100, 0, 100) = 93.79
```

No structural-trend bonus applicable — margin is already well above the 40% threshold where the bonus would apply (it's reserved for sub-40%-margin businesses trending up). Annual gross margin has been essentially flat/high for 4 years: FY2023 73.18%, FY2024 75.16%, FY2025 74.96%, FY2026 74.68%, TTM 75.03% (all self-computed from `t.financials`).

**Margins_Score = 93.79**

### 2.6 Balance Sheet (15% weight)

```
BalanceSheet_Score = clamp(100 × (1 − NetDebt/EBITDA / 4), 0, 100)
  Net Debt/EBITDA = −3,731.458 / 106.085 = −35.17× (net cash — deeply negative ratio)
  BalanceSheet_Score = clamp(100 × (1 − (−35.17/4)), 0, 100) = clamp(979.3, 0, 100) = 100.0
```

Robust regardless of which EBITDA figure (self-derived $106.085M vs. stockanalysis's $85.4M) is used — CrowdStrike carries essentially no net leverage (net cash of ~$3.7B against only $821M gross debt).

**BalanceSheet_Score = 100.0**

### 2.7 Growth (20% weight)

```
Growth_Score = clamp((Revenue 3yr CAGR% / 25) × 100, 0, 100)
  Revenue: FY2023 $2,241.236M → FY2026 $4,812.005M (fiscal years ended Jan 2023 / Jan 2026)
  3yr CAGR = (4,812.005 / 2,241.236)^(1/3) − 1 = 28.99% ≈ 29.0%
  Growth_Score (base) = clamp((29.0/25)×100, 0, 100) = clamp(116.0, 0, 100) = 100.0  (capped)
```

Cross-check: stockanalysis.com's own reported figures for the same 4 fiscal years (Revenue $2,241M → $4,812M) yield the same conclusion (well above the 25% cap either way computed).

**TAM-expansion / pricing-power modifier (+10, documented):** CrowdStrike's own reporting shows ARR of $5.25B with 50% of customers on 6+ Falcon platform modules, 34% on 7+, 24% on 8+ (module cross-sell into adjacent categories — cloud security, identity security, exposure management, and now agentic-AI security), 115% dollar-based net retention, and 97% gross retention (source: CrowdStrike Q3/Q4 FY2026 investor materials, cross-cited via [FourWeekMBA](https://fourweekmba.com/crowdstrike-revenue-breakdown/)). The triggering Cerebras partnership itself is incremental evidence of TAM expansion into a new category (securing third-party AI infrastructure/models), consistent with the company's stated AIDR (AI Detection and Response) push. This modifier is capped at 100.0 (already at the ceiling from the base CAGR) — shown for completeness, no numeric effect.

**Growth deceleration check:** annual YoY revenue growth has clearly decelerated — FY2024 +36.35%, FY2025 +29.39%, FY2026 +21.72% (self-computed from the same annual figures). This is a documented *trend*, but no specific cited evidence was found in this session (TAM saturation disclosure, competitive share loss, pricing compression) that the deceleration is *structural* rather than the ordinary base-effect slowdown expected as a company scales from ~$2B to ~$5B of revenue. Per the rule's requirement to cite specific evidence before applying the −10 structural-deceleration modifier, it is **not applied** here — flagged as an open question for future re-scores rather than guessed at.

**Growth_Score = 100.0**

### 2.8 Moat Signal (15% weight)

| Signal | Verdict | Cited evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Named a Leader in the 2026 Gartner Magic Quadrant for Endpoint Protection for the **7th consecutive time**; positioned furthest right for Completeness of Vision and highest for Ability to Execute among all vendors for the 4th year running; 97% "Willingness to Recommend" in Gartner Peer Insights, most 5-star ratings of any Customers' Choice vendor (source: [CrowdStrike IR press release](https://ir.crowdstrike.com/news-releases/news-release-details/crowdstrike-named-leader-2026-gartnerr-magic-quadranttm-endpoint), [Barchart](https://www.barchart.com/story/news/2202728/crowdstrike-named-a-leader-in-the-2026-gartner-magic-quadrant-for-endpoint-protection-for-seventh-consecutive-time)) |
| Brand premium (pricing power) | **TRUE** | Documented annual price increases of 5–8% at renewal; 115% dollar-based net retention (customers pay more over time within existing accounts) alongside 97% gross retention (near-zero churn) — expansion without customer loss is the standard evidence this framework requires for pricing power (source: [CostBench](https://costbench.com/software/cybersecurity/crowdstrike/), [FourWeekMBA](https://fourweekmba.com/crowdstrike-revenue-breakdown/)) |
| Network effect | **TRUE** | Documented mechanism: CrowdStrike's Threat Graph correlates telemetry events across its **entire customer base** in real time — when a new attack pattern hits one organization, every other Falcon customer gets protection within seconds. More endpoints feeding the graph → better/faster detection for all customers, the standard two-sided-value network-effect mechanism (source: [CrowdStrike Threat Graph product page](https://www.crowdstrike.com/en-us/platform/threat-graph/)) |
| Switching costs | **TRUE** | Documented mechanism: deep multi-module platform lock-in — 50% of customers now run 6+ Falcon modules, 34% run 7+, 24% run 8+ (up from 64%/27% on a 5+/7+ basis in early 2024), each additional module deepens workflow/data integration and raises the operational cost of migrating away (source: [FourWeekMBA](https://fourweekmba.com/crowdstrike-revenue-breakdown/)) |
| Scale cost advantage | **FALSE — not credited** | Searched specifically for cost-per-unit data showing CrowdStrike's own production/delivery cost advantage vs. smaller competitors (e.g. SentinelOne). What was found instead was evidence of *lower total cost of ownership for CrowdStrike's customers* vs. legacy multi-agent vendors (a switching-cost/value-proposition point, already credited above) — not the specific "our unit economics beat smaller rivals due to scale" evidence this signal requires. Not marked true without a cited number, consistent with "never invent or estimate financial data." |

```
Moat_Score = (4 of 5 TRUE / 5) × 100 = 80.0
```

**Moat_Score = 80.0**

### 2.9 FCF Quality (10% weight) — and the hard disqualifier

```
FCFQuality_Score = clamp(((FCF/NI Ratio − 0.40) / 0.60) × 100, 0, 100)
```

**This is where CrowdStrike runs into a genuine structural problem, not just a low continuous score.** TTM Net Income is **negative** (−$24.521M) while TTM FCF is strongly positive (+$1,431.313M) — the ratio itself (1,431.313 / −24.521 ≈ **−58.4×**) is not a meaningful "conversion percentage"; it is deeply negative, i.e., far below the 70% threshold under any interpretation.

```
FCFQuality_Score = clamp(((−58.4 − 0.40)/0.60)×100, 0, 100) = clamp(very negative, 0, 100) = 0.0
```

**Multi-year check (for the hard-disqualifier test, "2+ consecutive years"):**

| Fiscal year (ended Jan) | Net Income | FCF | Ratio |
|---|---|---|---|
| FY2023 | −$183.245M | $674.570M | negative (NI negative) |
| FY2024 | +$72.181M | $929.095M | 1,287% (NI positive but thin — driven by heavy SBC add-back, not a conversion-quality problem in the disqualifier sense) |
| FY2025 | −$15.241M | $1,067.906M | negative (NI negative) |
| FY2026 | −$162.502M | $1,241.490M | negative (NI negative) |
| TTM (thru 2026-04-30) | −$24.521M | $1,431.313M | negative (NI negative) |

**FY2025 and FY2026 are two consecutive fiscal years with negative Net Income (ratio undefined/deeply negative), and the TTM period continues that pattern into a third.** This fires the **FCF/NI conversion hard disqualifier** in [quality-scoring.md](../framework/quality-scoring.md): *"FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation."*

**Checked for the stated carve-out (growth-capex explanation) — does not apply:** CapEx/Revenue is only ~6–8% (TTM CapEx $387.866M / Revenue $5,094.2M = 7.6%), not an unusually elevated growth-capex ratio for a SaaS business at this scale. The gap between negative GAAP Net Income and strongly positive FCF is driven almost entirely by **Stock-Based Compensation** — TTM SBC of $1,146.721M is more than 45× TTM GAAP Operating Income's magnitude and roughly equal to the entire GAAP operating loss plus a healthy margin on top. SBC is a real, dilutive economic cost to existing shareholders (see glossary entry) that the cash-flow statement's add-back convention masks — it is not the "elevated growth CapEx" scenario the framework's carve-out is written for. **Sensitivity check (not a scored input, shown for transparency):** an SBC-adjusted FCF (TTM FCF $1,431.313M − TTM SBC $1,146.721M = **$284.6M**) would still be positive but roughly 1/5th the headline figure — illustrating how much of the reported cash-generation strength is a function of non-cash compensation accounting rather than the underlying GAAP-profitability picture.

**FCFQuality_Score = 0.0, and the hard disqualifier independently fails the Quality Gate regardless of the weighted score below.**

### 2.10 Other hard disqualifiers checked

| Disqualifier | Result |
|---|---|
| FCF/NI conversion <70% for 2+ consecutive years, no growth-capex carve-out | **FIRES** — see §2.9 |
| Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light override) | Does not fire — net cash position, ratio deeply negative (§2.6) |
| Not FCF-positive for 3+ consecutive years | Does not fire — FCF positive every fiscal year FY2023–FY2026 and TTM (§2.9 table) |

### 2.11 Final Quality Score

```
Quality Score = (Profitability×0.25) + (Margins×0.15) + (Growth×0.20) + (BalanceSheet×0.15) + (Moat×0.15) + (FCFQuality×0.10)
              = (0.0×0.25) + (93.79×0.15) + (100.0×0.20) + (100.0×0.15) + (80.0×0.15) + (0.0×0.10)
              = 0.0 + 14.0685 + 20.0 + 15.0 + 12.0 + 0.0
              = 61.0685 → rounds to 61.1
```

**Quality Score = 61.1 / 100.0 — fails the 80.0+ gate on the weighted score alone, and independently fails via the FCF/NI conversion hard disqualifier (§2.9).** Per [quality-scoring.md](../framework/quality-scoring.md): *"a weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* Per this task's instructions and the operating brief, **stop here — do not proceed to Phase 02 valuation scoring or the Composite Score.**

---

## 3. Recommendation

# **PASS — Quality Score 61.1/100.0, fails the 80.0+ gate. Also independently failed by the FCF/Net Income conversion hard disqualifier (2 consecutive fiscal years — FY2025, FY2026 — plus the current TTM — of negative GAAP Net Income against strongly positive FCF, driven overwhelmingly by Stock-Based Compensation rather than a documented growth-capex explanation). Do not enter.**

CrowdStrike is a genuinely strong *business* on several individual axes — a real network-effect/switching-cost moat backed by cited third-party evidence (7-time Gartner Magic Quadrant Leader, Threat Graph's real-time cross-customer detection, deep multi-module platform lock-in), ~29% 3-year revenue CAGR, a 75% gross margin, and a net-cash balance sheet with essentially no leverage risk. But this framework's Quality Score is explicitly a *quality* gate, not a growth-story gate: on trailing GAAP profitability, CrowdStrike is currently **unprofitable** (TTM Net Income −$24.5M, TTM GAAP Operating Income −$199.2M) and its cash generation, while strong in headline terms, is structurally propped up by very large Stock-Based Compensation (TTM $1,146.7M) rather than by genuine operating profitability converting cleanly into cash. The framework's FCF/NI conversion hard disqualifier exists precisely to catch this pattern — a company whose cash-flow statement looks excellent while its income statement (the harder-to-manage, audited profitability record) does not — and it fires here on its own literal terms, independent of and in addition to the 61.1 weighted score already falling well short of 80.0.

The triggering Cerebras/Falcon AIDR partnership announcement (§0) is real and independently verified, but is a product/go-to-market announcement, not a fundamental change to CrowdStrike's trailing profitability or cash-conversion profile — it does not alter this verdict.

**No position opened — nothing to log in `decisions/`.**

---

## 4. Next review trigger

CrowdStrike's next scheduled quarterly earnings report (fiscal Q2 FY2027, expected ~late August/early September 2026 based on its historical reporting cadence) — a full quarter of new financial-statement data that would let this Quality Score be recomputed on a fresh TTM basis. Watch specifically for: (1) a return to sustained GAAP profitability (Net Income positive for 2+ consecutive quarters would meaningfully change the Profitability and FCF Quality sub-scores), (2) any deceleration in SBC as a % of revenue (currently ~22.5% of TTM revenue), which would improve the FCF/NI conversion picture directly, and (3) confirmation of whether the FY2024→FY2026 revenue growth deceleration (36% → 29% → 22%) continues, stabilizes, or reverses — relevant to the Growth sub-score's TAM/pricing-power modifier in a future session. Also, per standard Rule 9 triggers: any >15% unexplained price move from today's $188.50 reference, guidance revision, management change, or material M&A.

---

## 5. Files touched this session

- `sessions/2026-07-22-new-position-crwd.md` — this file
- `watchlist/not-in-portfolio/CRWD/CRWD-2026-07-22.md` — **new file** (first-ever CRWD watchlist entry)

`watchlist/STALE.md` not touched (Phase 01 FAIL / not-scored-under-Composite entries are exempt from the stale-score mechanism — CRWD never reached Phase 02, so there is no valuation score for a methodology version to invalidate).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **ARR (Annual Recurring Revenue)** — the annualized run-rate value of a subscription business's contracted recurring revenue at a point in time; CrowdStrike disclosed $5.25B ARR.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **FCF (Free Cash Flow)** — cash generated by the business after capital expenditure.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check; a low ratio without a CapEx explanation is a red flag for earnings-quality games. CrowdStrike's ratio is undefined/deeply negative due to negative Net Income.
- **Gartner Magic Quadrant** — a widely-cited analyst-firm ranking of vendors along "completeness of vision" and "ability to execute," with the top-right quadrant labeled "Leaders." CrowdStrike is a 7-time consecutive Leader in the Endpoint Protection Magic Quadrant.
- **Gross Margin** — Gross Profit ÷ Revenue, the share of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score. CrowdStrike's FCF/NI conversion ratio fires this one independently of the 61.1 weighted score.
- **Invested Capital** — total capital (debt + equity, netted for cash) put to work in a business — the denominator in ROIC.
- **Moat** — a durable competitive advantage.
- **Net Debt/EBITDA** — a leverage ratio; net debt divided by EBITDA. Deeply negative for CrowdStrike (net cash position).
- **Net Margin** — Net Income ÷ Revenue.
- **Net Retention Rate (NRR / Dollar-Based Net Retention)** — the percentage of recurring revenue retained and expanded from an existing customer cohort over 12 months; CrowdStrike's is 115%.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate), the numerator of ROIC.
- **Quality Score** — this framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. CrowdStrike scores 61.1.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **SBC (Stock-Based Compensation)** — employee pay in company shares/options; a non-cash expense that inflates FCF relative to GAAP net income but remains a real economic (dilutive) cost. CrowdStrike's TTM SBC of $1.147B is the central driver of its Quality Score problems this session.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.
