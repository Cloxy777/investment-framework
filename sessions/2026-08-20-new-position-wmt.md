# NEW POSITION — WMT (Walmart Inc., NYSE) — 2026-08-20

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — re-evaluation on a confirmed Rule 9 earnings event)
**Date:** 2026-08-20 (Thursday)
**Current WMT portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [WMT-2026-08-16.md](../watchlist/not-in-portfolio/WMT/WMT-2026-08-16.md) — Quality Score 40.6/100.0, Quality Gate FAIL, PASS/watchlist-only. That entry's stated "Next review trigger" was **"WMT's Q2 FY2027 earnings (quarter ended 2026-07-31), expected 2026-08-20"** — which is exactly the event that fired today.
**Sector:** Consumer Staples / Discount & Department Store Retail
**First-use jargon decode:** see closing Glossary (§8)

---

## 0. Why this session exists — trigger source

A post on **FinnInvestChannel** (Telegram, post FinnInvestChannel/3123, 2026-08-20T15:34:14 UTC) reported Walmart's Q2 FY2027 results, framing them as evidence the US consumer is weakening: *"Walmart каже, що американський споживач слабшає… Продажі у США виросли лише на 2.6% проти очікуваних 3.7%, це найповільніший ріст за 6 років… Q2 при цьому був нормальний: revenue +5.9%, EPS +19%, але прогноз EPS на Q3 $0.64 проти очікуваних $0.68"* ("Walmart says the American consumer is weakening… US sales grew only 2.6% vs. an expected 3.7%, the slowest growth in 6 years… Q2 itself was fine: revenue +5.9%, EPS +19%, but Q3 EPS guidance of $0.64 vs. an expected $0.68").

**The post's text is not used as a financial input anywhere below** — it is only the reason this session exists (CLAUDE.md Rule 0). Every figure in §2 onward is independently primary-sourced from Walmart's own SEC filings and IBKR live market data.

**Independent verification that a real Rule 9 event occurred:** Walmart filed an **8-K** with the SEC on **2026-08-20** (accession 0000104169-26-000145, Items 2.02 and 9.01) furnishing its Q2 FY2027 earnings presentation. This is a genuine, dated quarterly earnings release — a Rule 9 fundamental-event trigger — and it is the specific event the prior watchlist entry named as its next review trigger. Step 4's third branch of `/telegram-scan` therefore applies: not held, prior `not-in-portfolio` entry exists, materially new information beyond what that entry reflects → `/new-position WMT`.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("Walmart")`: contract_id **13824**, exchange **NASDAQ**, description "WALMART INC", country_code US — the correct primary US listing (the DE/MX/CA/CH cross-listings, the WALMEX Mexican subsidiary, and the WMMVY ADR were all returned but not used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$103.64** | IBKR `get_price_snapshot`, `last` field, ts 2026-08-20 16:10:29 UTC, `top_status` = REALTIME |
| Bid / Ask | $103.62 / $103.65 | IBKR `bid_ask` (spread $0.03 — tight, deep book: 180 × 116) |
| Change vs. prior close | **−$10.66 (−9.33%)** | IBKR `change` |
| 52-week high / low | $135.155 / $95.031 | IBKR `misc_statistics` |
| 13-week high / low | $125.80 / $106.79 | IBKR `misc_statistics` |
| Day volume | ~46.40M shares (vs. ~14.52M on 2026-08-16) | IBKR `volume` |
| Dividend yield | 0.64% | IBKR `dividend_yield` |

**Price-move check.** Down 9.33% on the day, and −10.15% versus the $115.34 recorded in the 2026-08-16 entry. This is **under** the framework's 15% "unexplained move" threshold, **and** it is not unexplained — it is a same-day reaction to the earnings release verified in §0. Note the print is currently below the prior 13-week low of $106.79, i.e. a fresh multi-month low.

---

## 2. Primary-sourced fundamentals

**Sourcing note (see §7 Data Gaps):** `yfinance` returned empty statements and Yahoo's `fundamentals-timeseries` endpoint returned HTTP 429 on four attempts this session. All fundamentals below are taken directly from **SEC EDGAR** — the company's own filings — which is the authoritative primary source, not a workaround estimate. Nothing is inferred or invented.

### 2.1 TTM revenue build (twelve months ended 2026-07-31)

Quarterly total revenues, all from Walmart's own disclosure (the Q2 FY2027 8-K constant-currency table restates the trailing five quarters):

| Quarter | Total revenues | Net sales | Gross profit rate |
|---|---|---|---|
| Q3 FY26 (ended 2025-10-31) | $179,496M | $177,769M | 24.2% |
| Q4 FY26 (ended 2026-01-31) | $190,656M | $188,913M | 24.0% |
| Q1 FY27 (ended 2026-04-30) | $177,751M | $175,684M | 24.3% |
| **Q2 FY27 (ended 2026-07-31)** | **$187,937M** | **$186,100M** | **25.4%** |
| **TTM** | **$735,840M** | **$728,466M** | — |

Q3 FY26 and Q1 FY27 total revenues independently cross-check against SEC XBRL `Revenues` facts ($179,496M and $177,751M respectively) — they match exactly.

### 2.2 TTM profit, cash flow and returns — Walmart's own disclosed TTM tables

Walmart's Q2 FY2027 8-K includes explicit trailing-twelve-month tables (its ROA/ROI non-GAAP reconciliation), so these are **disclosed TTM figures, not reconstructed ones**:

| Item (TTM ended 2026-07-31) | Value | Source |
|---|---|---|
| Consolidated net income | **$22,499M** | 8-K ROA table |
| Operating income (EBIT) | **$32,280M** | 8-K ROI table |
| Depreciation & amortization | **$15,094M** | 8-K ROI table |
| **EBITDA** (EBIT + D&A) | **$47,374M** | derived |
| Return on assets (company's own) | 8.0% (vs. 8.3% a year ago) | 8-K |
| Return on investment (company's own non-GAAP) | 15.4% (vs. 15.1% a year ago) | 8-K |

Cash flow, built from the 8-K's year-to-date reconciliation table (FY2026 full year minus H1 FY2026 plus H1 FY2027):

```
TTM OCF   = 41,565 − 18,352 + 19,710 = $42,923M
TTM CapEx = 26,642 − 11,409 + 14,181 = $29,414M
TTM FCF   = 42,923 − 29,414          = $13,509M
TTM FCF/NI = 13,509 / 22,499         = 60.04%
```

**Annual FCF/NI history** (unchanged from the 2026-08-16 session, all completed fiscal years):

| Fiscal Year | OCF | CapEx | FCF | Net Income | FCF/NI |
|---|---|---|---|---|---|
| FY2024 | 35,726 | 20,606 | 15,120 | 15,511 | 97.48% |
| FY2025 | 36,443 | 23,783 | 12,660 | 19,436 | 65.15% |
| FY2026 | 41,565 | 26,642 | 14,923 | 21,893 | 68.16% |

FCF is positive in every year shown and in every fiscal year on Walmart's multi-decade record — the "FCF-positive 3+ consecutive years" disqualifier is nowhere near firing.

### 2.3 Margins

```
TTM cost of sales = Σ(net sales × (1 − gross profit rate))  = $550,146M
TTM gross profit  = TTM total revenues − TTM cost of sales  = $185,694M
TTM gross margin (total-revenue basis)                      = 25.24%
```

The total-revenue-basis convention is carried over unchanged from the 2026-08-16 session so the two scores stay comparable. On Walmart's own net-sales basis the figure is **24.48%** — both are far below the framework's 40% threshold, so the choice of convention does not move the outcome (see §7).

```
TTM Net Margin = 22,499 / 735,840 = 3.06%
```

### 2.4 Balance sheet (most recent filed, quarter ended 2026-04-30)

The Q2 FY2027 **10-Q** has not been filed yet — today's disclosure is the 8-K earnings presentation only, which does not include a balance sheet. Balance-sheet inputs therefore come from the most recent **filed** primary source, the Q1 FY2027 10-Q (SEC XBRL):

| Item | 2026-04-30 |
|---|---|
| Long-term debt, noncurrent | $36,887M |
| Long-term debt, current | $3,896M |
| Short-term borrowings | $10,673M |
| **Total debt** | **$51,456M** |
| Cash and cash equivalents | $10,729M |
| Total equity incl. NCI | $100,682M |

```
Net Debt = 51,456 − 10,729 = $40,727M
Net Debt/EBITDA = 40,727 / 47,374 (TTM EBITDA) = 0.860×
Invested Capital = 51,456 + 100,682 − 10,729 = $141,409M
```

This pairs an April-dated balance sheet with a July-dated TTM income figure — a disclosed three-month timing mismatch, flagged in §7 and shown there to be immaterial to the outcome.

### 2.5 Growth, margin-trend and moat evidence — all from the Q2 FY2027 8-K (2026-08-20)

- **Gross margin still structurally expanding:** FY2024 24.37% → FY2025 24.85% → FY2026 24.93% → TTM 25.24%. The company attributes Q2's **+96 bps gross profit rate improvement to 25.4%** to *"tariff refunds, partially offset by price investments and higher fuel costs"* and *"favorable business mix led by global advertising."* The tariff-refund portion is explicitly a benefit that *"may not recur at the same level"* — noted, and it is why the trend bonus is credited on the multi-year trajectory rather than on this quarter alone.
- **TAM-expansion evidence, re-confirmed and stronger than in August:** *"total advertising +38%, including Walmart Connect +43%"*; *"Marketplace sales +52%"*; *"Global eCommerce net sales grew 23%; representing 24% of total net sales"*; *"Membership & other income grew 11.2%; reflecting 17% global growth in membership fee revenue"*; *"Walmart+ fee revenue up double-digits with record Q2 net adds."* Every one of these lines is growing several times faster than the ~5% core revenue rate.
- **Market-share evidence (Moat Signal 1):** *"Sales reflected continued strong momentum in eCommerce and broad-based share gains"*; *"Share gains continued across categories and income tiers led by upper-income households."*
- **Scale cost advantage (Moat Signal 5):** carried from the 2026-08-16 session; unchanged.
- **Documented growth-capex explanation, re-confirmed today:** *"The decrease in free cash flow was due to an increase of $2.8 billion in capital expenditures to support our omnichannel growth strategy."* FY2027 capex guidance was raised from *"approximately 3.5% of net sales"* to *"approximately 4.0% of net sales."*
- **Full-year guidance was raised, not cut:** FY2027 net sales (cc) growth guidance went from 3.5–4.5% to **4.0–5.0%**; adjusted operating income (cc) growth from 6.0–8.0% to **7.0–8.5%**; adjusted EPS from $2.75–2.85 to **$2.80–2.87**.

---

## 3. Phase 01 — Quality Score

### 3.1 Hard disqualifiers

| Disqualifier | This company | Verdict |
|---|---|---|
| Not FCF-positive 3+ consecutive years | FCF positive every year on record (§2.2) | ✅ PASS, clean |
| Net Debt/EBITDA over threshold | **0.860×** vs. 2.5× standard threshold (§2.4) | ✅ PASS, clean — and *improved* from 0.908× in August, since TTM EBITDA rose |
| FCF/NI <70% for 2+ consecutive years **without** a documented growth-capex explanation | FY2025 65.15% / FY2026 68.16% — both sub-70% — **but** a documented growth-capex explanation exists and was **re-confirmed in today's release** ("$2.8 billion in capital expenditures to support our omnichannel growth strategy", §2.5) | ✅ PASS — does not fire; the continuous FCF Quality sub-score in §3.7 still reflects the low ratio |

**No hard disqualifier fires.**

### 3.2 Profitability (25% weight)

```
NetMargin_Component = clamp((3.06 / 30) × 100, 0, 100) = 10.19

Tax rate: FY2026 actual blended effective rate = 7,199 / 29,469 = 24.43%  (FY2026 10-K)
  — bracketed by the company's own FY2027 guidance, reaffirmed today at 23.5%–24.5%
NOPAT = TTM EBIT $32,280M × (1 − 0.2443) = $24,394M
ROIC (TTM) = 24,394 / 141,409 = 17.25%
ROIC_Component = clamp((17.25 / 30) × 100, 0, 100) = 57.50

Profitability_Score = (10.19 + 57.50) / 2 = 33.85   (no FCF-positivity cap — §3.1)
```

Net margin is the binding constraint and always will be for a discount retailer: 3.06% of a 30% scale is 10.2 points. ROIC is genuinely respectable (17.25%, and Walmart's own ROI metric *rose* to 15.4% from 15.1%) — it simply cannot carry a blended sub-score on its own.

### 3.3 Margins (15% weight)

```
GrossMargin_Score = clamp((25.24 / 80) × 100, 0, 100) = 31.54
```

**+10 structural-trend bonus applies** — gross margin sits below the 40% static threshold but has expanded every period for 3+ years running (24.37% → 24.85% → 24.93% → 25.24%), with a cited, disclosed driver (mix shift toward advertising/membership/marketplace, §2.5).

```
Margins_Score = clamp(31.54 + 10, 0, 100) = 41.54
```

### 3.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2023 $611,289M → FY2026 $713,163M) = (713,163/611,289)^(1/3) − 1 = 5.27%
Growth_Score (raw) = clamp((5.27 / 25) × 100, 0, 100) = 21.09
```

No new fiscal year has completed since the August session, so the CAGR input is unchanged by construction.

**+10 TAM-expansion modifier applies** — documented, *actual* (not guidance) evidence from today's release: advertising +38%, Walmart Connect +43%, Marketplace +52%, e-commerce +23%, membership fee revenue +17% (§2.5).

**Explicitly considered and rejected: the −10 structural-deceleration modifier.** The trigger post's whole thesis is deceleration, and Walmart U.S. comp sales did slow from +4.1% (Q1 FY27) to **+2.6%** (Q2 FY27). But the framework requires evidence growth is decelerating **structurally, not cyclically**, and the filing itself documents the opposite reading: ~125 bps of that 2.6% is a **pharmacy-deflation headwind from Maximum Fair Price regulation** — a policy/regulatory price effect, not lost demand — and ex-Health-&-Wellness comp was **+3.4%**. Meanwhile the company **raised** full-year net sales, operating income, and EPS guidance (§2.5), and every faster-growing monetization line accelerated. Applying −10 on this evidence would be reading the Telegram post's framing into the score rather than the filing. **Flagged for human audit/override:** a reasonable analyst could argue the Q3 EPS guide ($0.62–0.64 vs. the $0.62 Q3 FY26 base) is soft enough to warrant the penalty. It would not change the outcome — see §5.

```
Growth_Score = clamp(21.09 + 10, 0, 100) = 31.09
```

### 3.5 Balance Sheet (15% weight)

```
Net Debt/EBITDA = 0.860×   (§2.4)
BalanceSheet_Score = clamp(100 × (1 − 0.860/4), 0, 100) = 78.51
```

Asset-light override (Upgrade 5) not applicable — Walmart is a capital-intensive physical retailer, not an asset-light network. This is the company's strongest sub-score, and it improved from 77.30 in August.

### 3.6 Moat Signal (15% weight)

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | ✅ TRUE | *"broad-based share gains"*; *"Share gains continued across categories and income tiers"* (Q2 FY27 8-K) |
| Brand premium | ❌ FALSE | Walmart competes on **price**, not brand premium — the release repeatedly cites *"price investments"* as a margin headwind, i.e. the opposite of pricing power |
| Network effect | ❌ FALSE | Marketplace +52% is real growth but no documented two-sided network mechanism is disclosed; not credited without a cited mechanism |
| Switching costs | ❌ FALSE | Grocery/general-merchandise retail has near-zero switching cost; Walmart+ membership is a retention program, not contractual lock-in |
| Scale cost advantage | ✅ TRUE | Carried from the 2026-08-16 session — largest global retailer by revenue, structural per-unit distribution cost advantage |

```
Moat_Score = (2 / 5) × 100 = 40.00
```

### 3.7 FCF Quality (10% weight)

```
FCF/NI Ratio (TTM) = 60.04%   (§2.2)
FCFQuality_Score = clamp(((0.6004 − 0.40) / 0.60) × 100, 0, 100) = 33.40
```

**Improved** since August, which recorded a TTM ratio of 55.21% (sub-score 25.35); today's 60.04% scores 33.40. The improvement comes from H1 FY2027 operating cash flow rising $1.4B YoY, partly offset by the $2.8B capex increase.

### 3.8 Quality Score

```
Quality Score = 33.85×0.25 + 41.54×0.15 + 31.09×0.20 + 78.51×0.15 + 40.00×0.15 + 33.40×0.10
              = 8.46 + 6.23 + 6.22 + 11.78 + 6.00 + 3.34
              = 42.0
```

## **Quality Score = 42.0 / 100.0 — FAILS the strict 80.0+ Quality Gate by 38.0 points.**

Marginally *better* than the 40.6 recorded on 2026-08-16 (driven by improved FCF conversion, a higher gross profit rate, and lower leverage against a larger EBITDA base) — but nowhere near the gate.

---

## 4. Rate Environment Gate / Phase 02 valuation / Composite Score — NOT COMPUTED

Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all. Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."*

This rule is doing real work today. WMT just fell 9.33% to a fresh multi-month low, which is precisely the setup where a valuation-first process would start building a case. The framework deliberately refuses to compute one. **No Rate Environment Gate, no valuation sub-scores, no Composite Score, no fair value, no buy/sell/stop levels, and no position size are produced in this session.**

---

## 5. Robustness of the gate failure

The failure does not depend on any judgment call or any data gap in §7:

| Sensitivity | Quality Score | Still fails? |
|---|---|---|
| **As computed** | **42.0** | ✅ fails by 38.0 |
| ROIC forced to 30% (maximum possible component) | 47.3 | ✅ fails by 32.7 |
| Net Debt forced to zero (BalanceSheet = 100) | 45.3 | ✅ fails by 34.7 |
| Both of the above together | 50.6 | ✅ fails by 29.4 |
| Moat forced to 5/5 (all signals credited) | 51.0 | ✅ fails by 29.0 |
| −10 deceleration modifier applied (§3.4, the bearish reading) | 38.0 | ✅ fails by 42.0 |

Even stacking the most generous defensible assumption on every contested input simultaneously leaves the score in the low 50s. **The gap is structural, not marginal:** a 3% net margin and a 5% revenue CAGR cannot produce an 80+ score under this framework's weights, and no single quarter changes that.

---

## 6. Recommendation

## **PASS — watchlist only. No position, no order, no levels.**

- **Quality Score 42.0/100.0** against a strict 80.0+ gate (§3.8). Phase 03's action table is never reached, because Phase 02 is never entered.
- Walmart is a genuinely well-run, financially sound business — 17.25% ROIC, 0.86× net leverage, decades of positive FCF, real share gains, and a fast-growing high-margin advertising/membership/marketplace layer. It is simply **not the kind of business this framework is built to own**: thin-margin, high-volume retail scores structurally poorly on Profitability, Margins and Growth, which together carry 60% of the weight.
- **The 9.33% drawdown changes nothing.** Acting on it would violate the framework's core discipline — act on documented triggers and scores, never on price movement alone. A cheaper price on a 42.0-quality company is still a 42.0-quality company.
- **No broker order was placed, modified, or proposed.** This routine stops at a score and a recommendation; only the human places trades.

---

## 7. Data gaps and integrity notes

**Data gaps (all disclosed, none blocking, none filled by invention):**

1. **`yfinance` and Yahoo `fundamentals-timeseries` were both unavailable** — `yfinance` returned empty income/cash-flow statements; the timeseries endpoint returned HTTP 429 on four attempts across both `query1` and `query2` hosts. **Worked around by going to SEC EDGAR directly** (companyfacts XBRL API + the 2026-08-20 8-K exhibit), which is the authoritative primary source and strictly better than the vendor feed. No figure is estimated. This is the third session in a week to hit Yahoo unavailability (see the 2026-08-19 MRK session) — worth a `/healthcheck` follow-up if it persists.
2. **Q2 FY2027 10-Q not yet filed**, so no balance sheet dated 2026-07-31 exists yet. Net Debt, Net Debt/EBITDA and Invested Capital use the **2026-04-30 10-Q** balance sheet (a filed, primary-sourced, dated figure) paired with TTM income data through 2026-07-31 — a disclosed three-month mismatch. §5 shows that even forcing net debt to zero leaves the score at 45.3, so this cannot affect the outcome.
3. **TTM effective tax rate not directly disclosed** for the twelve months ended 2026-07-31 (would require Q2 FY2027 pretax/tax detail from the unfiled 10-Q). Used the **FY2026 actual blended rate of 24.43%** from the 10-K, which the company's own reaffirmed FY2027 guidance range (23.5%–24.5%) brackets. Affects only ROIC; §5 shows a maximum-ROIC sensitivity still fails.
4. **Gross margin derived from disclosed gross profit *rates*** (1-decimal precision) rather than a cost-of-sales line item, since the 10-Q is unfiled. Both plausible conventions were computed (25.24% total-revenue basis / 24.48% net-sales basis) and both are so far below the 40% threshold that the sub-score moves by under 1 point either way.

Because every figure is sourced and no gap can move the pass/fail outcome, **the auto-commit for this ticker is not skipped.**

**Data-integrity note on the trigger post** (recorded for the mention log, not used in scoring). Comparing the post against the filing:

- ✅ *"revenue +5.9%"* — confirmed exactly (total revenues +5.9% to $187,937M).
- ✅ *"US sales grew only 2.6%"* — confirmed as **Walmart U.S. comp sales +2.6% ex-fuel**. The post presents this as a headline "US sales" growth rate; it is a comparable-sales metric, and the filing discloses ~125 bps of it as a pharmacy-deflation regulatory effect, with ex-H&W comp at +3.4%.
- ✅ *"EPS +19%"* — matches **adjusted** EPS ($0.81 vs. $0.68, +19.1%). The post does not mention that **reported** diluted EPS *fell* 9.1% ($0.80 vs. $0.88).
- ⚠️ *"vs expected 3.7%"* and *"vs expected $0.68"* — consensus estimates, not company disclosures; **not verified and not used**.
- ⚠️ *"slowest growth in 6 years"* — not in the filing; **not verified and not used**.
- ⚠️ **Material omission:** the post does not mention that Walmart **raised** its full-year FY2027 guidance across net sales, operating income and EPS on the same day (§2.5). The post's selection of figures is directionally bearish relative to the filing taken as a whole.

None of the above affected the score, which was built exclusively from the filings.

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **8-K** | The "current report" a US public company files with the SEC within days of a material event — commonly used to furnish a quarterly earnings release ahead of the fuller 10-Q that follows weeks later. Walmart's Q2 FY2027 results were sourced from its 2026-08-20 8-K, since the corresponding 10-Q had not yet been filed. |
| **10-K (Annual Report)** | The annual audited financial-disclosure report a US public company files with the SEC. |
| **10-Q (Quarterly Report)** | The quarterly financial-disclosure report filed between annual 10-Ks — used here to reconstruct TTM figures. |
| **CC (Constant Currency)** | A growth-rate presentation that strips out currency movements, so reported growth reflects underlying business activity rather than FX swings. |
| **Comparable sales (comps / same-store sales)** | Sales growth at stores open at least a year, stripping out the effect of opening new stores — the like-for-like organic-growth metric for retail. |
| **Composite Score** | This framework's 50/50 blend of Quality Score and Valuation Score — not computed here, because the Quality Gate stops the evaluation first. |
| **EBITDA** | Earnings before interest, taxes, depreciation and amortization — a rough measure of operating cash profit, used here as the denominator of the leverage ratio. |
| **FCF (Free Cash Flow)** | Operating cash flow minus capital expenditures — the cash a business actually generates after paying to maintain and grow its asset base. |
| **FCF/NI conversion ratio** | Free cash flow divided by net income — how much of reported accounting profit turns into real cash. Persistently below 70% is a red flag unless explained by growth capex. |
| **Gross margin / gross profit rate** | Revenue minus the direct cost of the goods sold, as a percentage of revenue. Walmart reports its "gross profit rate" on a net-sales basis; this session also computes a total-revenue-basis figure for comparability with the prior WMT session. |
| **Maximum Fair Price (MFP)** | The negotiated ceiling price the US Medicare drug-price-negotiation program sets for selected prescription drugs. Where it applies, pharmacy revenue per prescription falls even if unit volumes hold — Walmart disclosed roughly a 125 bps drag on Q2 FY2027 US comparable sales from MFP-related pharmacy deflation and brand-to-generic transfers, which is why this session treats the comp slowdown as regulatory rather than structural demand weakness. *(New term.)* |
| **Moat** | A durable structural advantage protecting a company's profits from competition — scored here as a 5-signal checklist. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — how many years of operating cash profit it would take to repay all debt; this framework's primary balance-sheet-risk gate. |
| **NOPAT** | Net Operating Profit After Tax — operating income with taxes deducted but before financing costs; the numerator of ROIC. |
| **Quality Gate (80.0+)** | This framework's strict rule that a company must score 80.0 or higher on the Quality Score to be eligible for valuation scoring at all. Below it, the evaluation stops regardless of how cheap the stock looks. |
| **ROA (Return on Assets)** | Net income divided by total assets — how efficiently a company generates profit from its full asset base. |
| **ROIC (Return on Invested Capital)** | How efficiently a company turns the capital invested in it (debt + equity) into profit — a core quality signal in this framework. |
| **Rule 0** | This framework's rule that live prices must always be fetched from a real market data source, and that financial data is never invented or estimated. Applied here both to the price and to the refusal to treat the Telegram post's numbers as data. |
| **Rule 9 (Model Refresh Triggers)** | The framework's enumerated list of fundamental events that justify re-scoring a company — earnings, guidance revision, M&A, management change, macro/rate shift, or a >15% unexplained price move. Walmart's Q2 FY2027 earnings release is the trigger for this session. |
| **Tariff refund** | A repayment of previously-paid import duties (e.g. following a tariff rollback, exclusion, or successful reclassification). Walmart cited tariff refunds as a significant driver of its Q2 FY2027 gross profit rate improvement and warned the benefit "may not recur at the same level" — i.e. a partly non-repeating margin tailwind, which is why this session credits the margin-trend bonus on the multi-year trajectory rather than on this quarter alone. *(New term.)* |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results, as opposed to a fiscal-year or forward-looking figure. |
| **Walmart Connect** | Walmart's retail-media/advertising business, sold to brands and marketplace sellers. Grew 43% in Q2 FY2027 — cited as documented Growth Score TAM-expansion evidence. |
| **XBRL** | The structured, machine-readable data format US public companies must tag their SEC filings in — accessed here via the SEC's companyfacts API to pull Walmart's reported figures directly from its own filings. |
