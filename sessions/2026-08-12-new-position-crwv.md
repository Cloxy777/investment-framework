# New Position Evaluation — CRWV (CoreWeave, Inc., NASDAQ)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 2026-08-12
**10Y US Treasury Yield:** 4.72% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-08-10 — normal FRED reporting lag; fetched directly via `fredgraph.csv?id=DGS10`)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4.4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current CRWV portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md)).
**Prior coverage:** None — first-ever evaluation of this ticker. No entry existed in either [watchlist/in-portfolio/](../watchlist/in-portfolio/) or [watchlist/not-in-portfolio/](../watchlist/not-in-portfolio/) before this session.
**Sector:** Technology, classified by data vendor (stockanalysis.com) as "Software - Infrastructure," but operationally a GPU-specialized cloud/AI-infrastructure-as-a-service provider (a "**Neocloud**" — see closing Glossary) renting Nvidia GPU compute capacity, not a diversified software vendor. IPO'd on Nasdaq 2025-03-28.
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

Telegram channel **FinnInvestChannel**, post **3084** (2026-08-12T07:59:54 UTC), claiming CoreWeave "Q3 earnings-style" figures: revenue $2.575B (+112% YoY), adjusted EBITDA $1.51B (+101% YoY), adjusted EBITDA margin 59%, revenue backlog $104B, active power capacity 1.5GW, contracted power capacity 3.7GW, plus a claim that CoreWeave added >$25B in new client contracts early in Q3.

**Per Rule 0, this post's claim is never used as financial data** — it is only the reason this ticker was looked at. No watchlist entry existed for CRWV in either `in-portfolio/` or `not-in-portfolio/`, and CRWV is not a current holding — per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's decision tree, "No watchlist entry exists at all → `/new-position <TICKER>`" fires unconditionally, independent of whatever the post claims. Every figure used for scoring below is independently sourced from CoreWeave's own Q2 2026 earnings press release, stockanalysis.com's financial statements (cross-checked where flagged), and Interactive Brokers live pricing — never from the Telegram post text itself.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work. **NASDAQ:CRWV, contract_id 771759702** (confirmed via `search_contracts` — the primary US-listed common stock, "COREWEAVE INC-CL A," distinct from the Mexico BDR and Toronto listing of the same root, the leveraged/inverse single-stock ETF products (`CRWG`, `CWVX`, `CRWU`, `CORD`, `CRWX`, `CWII`, `CWY`), the London/Amsterdam leveraged ETPs (`3CRW`, `CRW3`), the options-income ETPs (`CRWY`, `YCRW`), and CoreWeave's own corporate/subsidiary bonds).

| Field | Value | Detail |
|---|---|---|
| **Last trade** | **$105.04** | Live intraday print (not a stale/inferred price), as of 2026-08-12 08:13:14 UTC. |
| Bid / Ask | $105.00 / $105.10 | |
| Change (intraday) | +$14.72 / **+16.3%** | Driven by CoreWeave's Q2 2026 earnings release (after Tuesday 2026-08-11's close) — a documented Rule 9 fundamental trigger (quarterly earnings), not an unexplained move. Not itself scored as evidence — price action alone is never a Rule 9 trigger per CLAUDE.md. |
| 52-week high | $153.20 | |
| 52-week low | $60.55 | |
| 13-week / 26-week high | $132.15 / $138.25 | |

**Live price used throughout this session: $105.04.**

---

## 2. Independent Fact-Check of the Telegram Post's Claims

The post's figures were checked against CoreWeave's own Q2 2026 earnings press release (2026-08-11, via [investors.coreweave.com](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx)) and corroborating secondary coverage (CNBC, Seeking Alpha). **Unlike the 2026-08-11 HIMS session (where one Telegram-claimed figure was materially wrong), every figure in this post checks out against the primary source:**

| Claim | Post said | Independently verified | Verdict |
|---|---|---|---|
| Q2 2026 revenue | $2.575B, +112% YoY | $2,575M, +112.4% YoY (vs. $1,212M Q2 2025) | **Accurate** |
| Adjusted EBITDA | $1.51B, +101% YoY | $1,510M, +100.5% YoY (vs. $753M Q2 2025) | **Accurate** (rounds to +101%) |
| Adjusted EBITDA margin | 59% | 59% (down from 62% YoY) | **Accurate** |
| Revenue backlog | $104B | "approximately $104 billion as of June 30, 2026" | **Accurate** |
| Active power capacity | 1.5GW | 1.5 GW (expanded by "nearly 500 MWs") | **Accurate** |
| Contracted power capacity | 3.7GW | "approximately 3.7 GW" | **Accurate** |
| New client contracts added early Q3 | >$25B | "more than $25 billion of net new customer commitments added in early Q3" | **Accurate** |

**Not mentioned in the post, but material and independently found:** Q2 2026 **GAAP net loss was $626M** (up from $290M a year earlier), driven substantially by net interest expense of $640M (more than double the $267M in Q2 2025) on the debt funding CoreWeave's data-center buildout. "Adjusted EBITDA" is CoreWeave's own non-GAAP metric (see Glossary) — it excludes stock-based compensation and other items, and is not the same as the GAAP-derived, TTM-basis figures used in the Quality Score below (§4). The post cherry-picked the flattering non-GAAP growth metrics without the GAAP net-loss/leverage picture, but did not misstate any of the numbers it chose to include.

Sources: [CoreWeave Q2 2026 press release](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx), [CNBC](https://www.cnbc.com/2026/08/11/coreweave-crwv-q2-earnings-report-2026.html), [Seeking Alpha](https://seekingalpha.com/news/4631186-coreweave-expects-12_4b-13_2b-of-2026-revenue-while-raising-year-end-active-power-target-to).

---

## 3. Data Source Note

Same environment constraint documented in prior sessions (e.g. 2026-08-07 NBIS, 2026-07-19/07-23 TSLA): `yfinance`'s `curl_cffi` backend fails through this session's proxy (`SSLError: Recv failure: Connection reset by peer`), confirmed again this session. Worked around via `WebFetch` against **stockanalysis.com**'s financials/balance-sheet/cash-flow/ratios pages and CoreWeave's own investor-relations press release. A raw-HTML cross-check via direct `curl` against stockanalysis.com returned only the client-side JS shell (the financial data loads via a client-side API call not present in the static HTML fetched this way) — this is a genuine tooling limitation of this session's environment, not a data-quality gap; the `WebFetch`-sourced figures were instead cross-checked internally (e.g. computing Net Margin directly from cited Net Income ÷ Revenue and comparing to the vendor's own displayed "Profit Margin" figure, §4.1) and against the primary-source CoreWeave earnings release for every Q2 2026 figure (§2). The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint. No required input was invented or estimated; every figure below is cited to its source, and every discrepancy found is flagged rather than silently resolved.

---

## 4. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 4.1 Raw financial inputs (all sourced, cited)

**TTM (trailing twelve months, period ended ~2026-06-30):**

| Metric | Value | Source |
|---|---|---|
| Revenue | $7,590M | [stockanalysis.com/stocks/CRWV/financials](https://stockanalysis.com/stocks/crwv/financials/) |
| Gross Profit | $5,117M | same |
| Gross Margin (computed) | **67.42%** | 5,117/7,590, reconciles with vendor's displayed 67.42% |
| Operating Income | -$144M | same |
| Operating Margin | -1.90% | same |
| Net Income | -$1,928M | same |
| Net Margin (computed) | **-25.40%** | Computed directly as Net Income ÷ Revenue = -1,928/7,590. **Flagged discrepancy:** the page's own displayed "Profit Margin" TTM figure is -18.00%, which does not reconcile to these same two cited numbers from the same table. Used the directly-reconcilable -25.40% figure — immaterial to the outcome either way, since NetMargin_Component clamps to 0.0 at both values (§4.3). |
| ROIC (TTM) | **-0.33%** | [.../financials/ratios](https://stockanalysis.com/stocks/crwv/financials/ratios/) "Return on Invested Capital" row, Aug'26 column. Independently sanity-checked: NOPAT ≈ Operating Income (-$144M) ÷ Invested Capital (Debt + Equity - Cash ≈ $51.1B) ≈ -0.28%, consistent in sign and rough magnitude. |
| Operating Cash Flow (TTM) | $6,911M | [.../cash-flow-statement](https://stockanalysis.com/stocks/crwv/financials/cash-flow-statement/) |
| CapEx (TTM) | -$20,566M | same |
| Free Cash Flow (TTM) | **-$13,655M** (= 6,911 - 20,566) | same |

**Annual figures (fiscal years, for the 3+/2+ consecutive-year hard-disqualifier tests and 3yr CAGR):**

| FY | Revenue | Net Income | Operating CF | CapEx | FCF |
|---|---|---|---|---|---|
| FY2025 | $5,131M | -$1,196M | $3,058M | -$10,309M | **-$7,251M** |
| FY2024 | $1,915M | -$937M | $2,749M | -$8,702M | **-$5,953M** |
| FY2023 | $229M | -$594M | $1,833M | -$2,943M | **-$1,110M** |
| FY2022 | $15.83M | -$31.06M | $0.91M | -$72.4M | **-$71.49M** |

**Free cash flow has never been positive in any fiscal year on record (FY2022–FY2025) or on a TTM basis** — CoreWeave has been in continuous, deepening cash burn throughout its GPU/data-center buildout, funded by debt.

**Balance sheet (TTM, most recent quarter ~2026-06-30):** Total Debt $51,608M, Cash & Equivalents $5,524M, Short-Term Investments $15M, Total Shareholders' Equity $5,024M → **Net Debt = 51,608 - 5,524 - 15 = +$46,069M** (a large net-debt position, not net cash — flagging that one `WebFetch` summary sentence this session mischaracterized this as "negative $46.1B" net debt, i.e. net cash; that phrasing does not reconcile with the same page's own Total Debt/Cash figures and was discarded as a summarizer error). **Net Debt/EBITDA (TTM, as reported) = 11.98×**, per [.../financials/ratios](https://stockanalysis.com/stocks/crwv/financials/ratios/) Aug'26 column — internally consistent with the balance-sheet figures (implies TTM EBITDA ≈ $46,069M / 11.98 ≈ $3.8B, plausible given deeply negative Operating Income and correspondingly very large D&A on ~$77B of total assets, most of it GPUs/data-center infrastructure). Source: [.../balance-sheet](https://stockanalysis.com/stocks/crwv/financials/balance-sheet/) and [.../ratios](https://stockanalysis.com/stocks/crwv/financials/ratios/).

### 4.2 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | CRWV data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | Every fiscal year on record (FY2022 -$71.49M, FY2023 -$1,110M, FY2024 -$5,953M, FY2025 -$7,251M) and the TTM (-$13,655M) are negative — CoreWeave has never once posted a positive FCF year, let alone 3 consecutive. | **FIRES — decisively.** |
| **Net Debt/EBITDA over threshold (2.5× standard, or 4× under the Upgrade 5 asset-light override)** | 11.98× (TTM, as reported) — nearly 5× the 2.5× standard threshold, and still 3× over even the 4× asset-light override. CoreWeave is a highly capital-intensive GPU/data-center infrastructure operator (100% of Total Assets is effectively hard infrastructure — servers, GPUs, leased/owned data-center facilities), the opposite of the "payment network / exchange / asset-light financial" profile Upgrade 5 is scoped to, so only the standard 2.5× threshold applies anyway; even the looser override wouldn't save it. | **FIRES — decisively.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | TTM FCF/NI = -13,655/-1,928 = 708% (a formula edge case, see §4.3 flag below — both figures are negative, and FCF is *more* negative than Net Income, meaning cash burn is deeper than the accounting loss, not a genuine "708% conversion"). A documented growth-capex explanation is directly available and citable: TTM CapEx (-$20,566M) is roughly double FY2025's already-large -$10,309M, consistent with continued AI data-center/GPU buildout (§2's $104B backlog, 3.7GW contracted power). **Moot regardless** — the two disqualifiers above already independently fail the company. | **Moot — not resolved either way, doesn't change the outcome.** |

**Two independent hard disqualifiers fire, each decisively** (not by a narrow margin — FCF has never been positive even once, and leverage is ~5× the standard ceiling). Per [quality-scoring.md](../framework/quality-scoring.md): "a weighted average can't average away an outright balance-sheet or cash-flow-quality failure." Proceeding to the full weighted score below anyway, for transparency (no black-box outputs) — it is not needed to reach the conclusion.

### 4.3 Sub-score calculation

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((-25.40/30)×100, 0, 100) = **0.0** (negative margin clamps to floor). ROIC_Component = clamp((-0.33/30)×100, 0, 100) = **0.0**. Profitability_Score = (0.0+0.0)/2 = **0.0**. (The "cap at 40.0 if not FCF-positive 3yr" rule is moot — already at the 0.0 floor.) | **0.0** |
| **Margins (15%)** | GrossMargin_Score = clamp((67.42/80)×100, 0, 100) = **84.27**. Gross margin has actually been **declining**, not structurally expanding, over the recent trend (FY2023 69.87% → FY2024 74.26% → FY2025 71.68% → TTM 67.42%) — no +10 trend bonus applies (also moot: that bonus is only defined for sub-40% gross margins). | **84.27** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $15.83M → FY2025 $5,131M) = (5,131/15.83)^(1/3) - 1 = **+586.9%/yr**. **Flagged as distorted, not a clean organic-growth read** (Rule 6) — FY2022 was a near-startup-scale base (CoreWeave's GPU-cloud business was tiny before the 2023–2025 AI buildout), so this is base-effect arithmetic more than a comparable trend. A shorter, still-extreme FY2023→FY2025 2yr CAGR (+373.4%/yr) confirms genuine hypergrowth even excluding the smallest year, consistent with the $104B backlog and raised 2026 guidance ($12.4–13.2B revenue) documented in §2 — real TAM-expansion evidence, though mechanically moot here since Growth_Score = clamp((586.9/25)×100, 0, 100) is already clamped at the ceiling regardless of which base year is used. | **100.0** (flagged) |
| **Balance Sheet (15%)** | Net Debt/EBITDA = 11.98× (TTM, as reported) → clamp(100×(1 - 11.98/4), 0, 100) = clamp(100×(1-2.995), 0, 100) = clamp(-199.5, 0, 100) = **0.0**. | **0.0** |
| **Moat Signal (15%)** | See §4.5 for the full 5-signal check with citations. Only **1 of 5** signals (Switching Costs) meets this framework's "never mark a signal true without a cited source" bar. Moat_Score = (1/5)×100 = **20.0**. | **20.0** |
| **FCF Quality (10%)** | FCF/NI (TTM) = -13,655/-1,928 = **708.2%** → literal formula: clamp(((7.082-0.40)/0.60)×100, 0, 100) = clamp(1113.8, 0, 100) = **100.0**. **Flagged as a formula edge case, not a genuine finding:** this ratio formula assumes a positive Net Income denominator (or at least FCF less negative than NI); here *both* figures are negative and FCF is *more* negative than Net Income — meaning CoreWeave's cash burn (-$13.7B) is actually deeper than its reported accounting loss (-$1.9B), the substantive **opposite** of "strong FCF conversion." Applying the literal formula here would let a black-box arithmetic quirk overstate quality, contrary to this framework's core "no black-box outputs" and "more conservative" tie-breaking principles. **This session uses 0.0 for the weighted total** (the substantively correct read: cash conversion is not just weak but actively worse than the accounting loss suggests), showing the literal 100.0 alongside it for transparency. Flagged in §7 as a candidate quality-scoring.md clarification (like the 2026-08-05 rolling-window clarification) for the negative/negative edge case generally — not resolved unilaterally in this session, since it's moot to the outcome either way. | **0.0** (conservative; literal formula would show 100.0 — flagged) |

### 4.4 Final weighted Quality Score

```
Quality Score = (0.0 × 0.25) + (84.27 × 0.15) + (100.0 × 0.20) + (0.0 × 0.15) + (20.0 × 0.15) + (0.0 × 0.10)
              = 0.0 + 12.641 + 20.0 + 0.0 + 3.0 + 0.0
              = 35.641 → 35.6 (rounded to nearest 0.1)
```

*(For transparency: if the FCF Quality sub-score's literal 100.0 formula output were used instead of the conservative 0.0 treatment flagged in §4.3, the total would be 45.6 — still 34.4 points below the gate.)*

**35.6 < 80.0 — fails the gate by 44.4 points** (or 34.4 points under the alternate literal-formula treatment), and independently, **two hard disqualifiers fire, each decisively** (§4.2: FCF has never been positive in any year on record; Net Debt/EBITDA 11.98× vs. a 2.5× threshold). Any one of these three findings alone is sufficient to fail Phase 01.

### 4.5 Moat Signal detail (5-signal checklist, cited evidence only)

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **FALSE** (not cited) | Multiple secondary sources describe CoreWeave as a large/leading GPU-cloud provider, but no primary-source, dated market-share percentage or ranking was directly verified this session — flagged as a genuine data gap (§7), not treated as "no moat," per "never mark a signal true without a cited source." |
| Brand premium | **FALSE** | No pricing-power evidence found (price increases without volume loss, premium vs. competitors); GPU-cloud capacity is generally competed on price/availability, not brand premium. |
| Network effect | **FALSE** | CoreWeave sells dedicated compute capacity to individual enterprise customers under bilateral contracts — no documented two-sided marketplace/network-effect mechanism. |
| Switching costs | **TRUE** | Customers commit to large, multi-year committed-capacity contracts — $104B revenue backlog as of 2026-06-30, including a $21B Meta agreement (through 2032, layered on a prior $14B commitment) and a multi-year Anthropic compute agreement (§2). Once a customer's AI training/inference workloads are provisioned onto CoreWeave's specific infrastructure/orchestration stack under a multi-year committed-capacity contract, mid-contract migration carries both contractual exit cost and real technical/operational re-provisioning cost. Source: [CoreWeave Q2 2026 press release](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Reports-Strong-Second-Quarter-2026-Results/default.aspx). |
| Scale cost advantage | **FALSE** (not cited) | Qualitative "large-scale GPU provider" claims exist in secondary coverage, but no cost-per-unit data showing a gap vs. smaller competitors was directly verified this session — flagged as a data gap (§7), same treatment as the market-share signal above. |

**Moat_Score = (1/5) × 100 = 20.0.**

### Result: **Phase 01 FAIL — weighted Quality Score 35.6, misses the 80.0+ gate by 44.4 points. Two hard disqualifiers also fire independently and decisively.**

Per [new-position.md](../.claude/commands/new-position.md) step 2: stop here rather than proceeding to scoring. **No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 5. Recommendation

**PASS.** Do not open a position, do not place a limit order, and do not add CRWV to a watchlist-only "monitor" status beyond the standard re-evaluation triggers below. CoreWeave's Q2 2026 results were genuinely strong on the growth/demand axis the Telegram post highlighted — revenue +112% YoY, a $104B backlog, and >$25B of new commitments in early Q3 are all independently verified as accurate (§2) — but the framework's Quality Score is built to look past a hot growth narrative at the balance-sheet and cash-flow substance underneath it, and there the picture is unambiguous: CoreWeave has never generated positive free cash flow in any year since its 2022 figures begin, carries $51.6B of debt against $5.5B of cash (Net Debt/EBITDA 11.98×, roughly 5× this framework's standard ceiling), and posted a widening GAAP net loss ($626M in Q2 2026 alone, driven substantially by $640M of quarterly net interest expense) even as adjusted, non-GAAP metrics improved. This is a company still deep in a debt-funded infrastructure buildout, structurally the profile this framework's FCF-positivity and leverage hard disqualifiers exist to catch — not a comment on whether the AI-infrastructure buildout ultimately succeeds, which is outside this framework's quantitative quality bar.

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 7. Next Review Trigger

No routine re-check scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of the following Rule 9-style fundamental triggers: (a) a sustained shift to positive free cash flow over 2+ consecutive quarters; (b) a credible deleveraging path bringing Net Debt/EBITDA back under 2.5× (e.g. GAAP operating income turning durably positive, or a material equity raise reducing net debt); (c) the next quarterly earnings release (Q3 2026, expected ~November 2026) or a guidance revision; (d) a management change or material M&A/strategic-financing event; (e) a >15% stock-price move with no identified cause (today's +16.3% move does not qualify — it is fully explained by the Q2 2026 earnings release, §1/§2). If a future session reaches this gate again, the **Market share** and **Scale cost advantage** Moat Signal sub-signals (§4.5) still need properly-cited primary-source evidence gathered — flagged as genuine data gaps this session, not resolved as "no moat." Absent any of the above, future Telegram mentions of CRWV should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 8. Data gaps flagged (Rule 0)

- **`yfinance` unusable this session** — same `curl_cffi`/proxy `SSLError` as prior sessions (2026-08-07 NBIS, 2026-07-19/07-23 TSLA), confirmed again this session. Worked around via `WebFetch` against stockanalysis.com and CoreWeave's own investor-relations press release; a direct `curl` fetch of stockanalysis.com pages returned only the client-side JS shell (data loads via a client-side API call), so the usual raw-HTML cross-check wasn't possible this session — every `WebFetch`-sourced figure was instead internally cross-checked (ratio reconciliation, balance-sheet-vs-ratios-page consistency) and, for every Q2 2026 figure specifically, against the primary-source CoreWeave earnings release (§2).
- **Net Margin discrepancy (material to catch, immaterial to the outcome):** `WebFetch`'s summary of the stockanalysis.com financials page displayed TTM "Profit Margin" as -18.00%, which does not reconcile with the same table's own cited Net Income (-$1,928M) ÷ Revenue ($7,590M) = -25.40%. Used the directly-reconcilable -25.40% figure. Immaterial to the outcome either way, since NetMargin_Component clamps to 0.0 at both values (§4.3).
- **"Net debt −$46.1B" mischaracterization:** one `WebFetch` summary sentence described CoreWeave's balance sheet as having a "negative $46.1 billion" net debt position (i.e., implying net cash) — this doesn't reconcile with the same page's own Total Debt ($51,608M) vs. Cash+ST Investments ($5,539M) figures, which imply a **positive** ~$46.1B net-debt (not net-cash) position, consistent with the separately-reported 11.98× Net Debt/EBITDA ratio. Treated as a summarizer error and discarded; the reconcilable, internally-consistent reading (large net debt) was used.
- **FCF Quality sub-score formula edge case (§4.3):** the FCF/NI conversion-ratio formula produces a literal 100.0 when both figures are negative and FCF is more negative than NI — the opposite of its intended meaning. This session used a conservative 0.0 for the weighted total rather than the literal formula output, and flags this as worth a future quality-scoring.md clarification for the general negative/negative case (not resolved unilaterally here, and moot to this session's outcome regardless).
- **Moat Signal — Market share and Scale cost advantage (§4.5) not adequately cited this session** — secondary coverage repeatedly describes CoreWeave as a large/leading GPU-cloud provider, but no primary-source market-share percentage/ranking or cost-per-unit comparison was directly verified. Marked FALSE per "never mark a signal true without a cited source," flagged as a genuine data gap rather than a substantive "no moat" finding — should be filled in on any future re-evaluation that reaches this gate again.
- **Customer concentration** — found via secondary sources (not independently primary-source-verified this session) that Microsoft has historically represented a majority of CoreWeave's revenue (~62-67% in FY2024/FY2025 per third-party aggregation of CoreWeave's own 10-K disclosures). Not used as a scored input (no Quality Score sub-score covers customer concentration directly), but worth flagging as thesis-relevant context for any future re-evaluation, alongside the Meta/Anthropic/OpenAI backlog diversification cited in §2/§4.5.

---

## 9. Glossary

- **Active power capacity / Contracted power capacity** — Active power capacity is the electrical power already energized and in live production use across a data-center operator's footprint; contracted power capacity is the larger forward total secured but not yet fully online. CRWV: 1.5 GW active, ~3.7 GW contracted as of Q2 2026.
- **Adjusted EBITDA** — A company's own non-GAAP variant of EBITDA that strips out items management deems non-recurring (e.g. stock-based compensation). CoreWeave's Q2 2026 Adjusted EBITDA ($1,510M, 59% margin) is not directly comparable to the GAAP-derived TTM figures used in this session's Quality Score (§4), which show a deeply negative GAAP Operating Margin.
- **Backlog** — The dollar value of signed customer orders not yet recognized as revenue. CoreWeave's revenue backlog was ~$104B as of 2026-06-30, plus >$25B of new commitments added in early Q3 2026.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. CRWV's headline 3yr CAGR (+586.9%/yr) is flagged as distorted by a near-startup-scale FY2022 base, not treated as a clean organic-growth signal.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets. CRWV's TTM CapEx (-$20,566M) reflects continued large-scale GPU/data-center buildout.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for CRWV since it never clears the 80.0+ Quality Score gate.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Negative for CRWV in every fiscal year on record (FY2022–FY2025) and on a TTM basis.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. For CRWV both figures are negative and the literal formula output (708%) is a flagged edge case, not genuine cash-conversion strength (§4.3).
- **GPU (Graphics Processing Unit)** — A processor originally built for graphics rendering, now the dominant chip type for AI training/inference — the core product CoreWeave rents out as a cloud service.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. CRWV's TTM figure is 67.42%, though declining from a FY2024 peak of 74.26%.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score. Two fire for CRWV: not FCF-positive for 3+ consecutive years, and Net Debt/EBITDA over its 2.5× threshold.
- **Hyperscaler** — An operator of very-large-scale, globally-distributed cloud/data-center infrastructure (Microsoft Azure, AWS, Google Cloud) — the diversified-cloud counterpart to a specialized "Neocloud" like CoreWeave.
- **Neocloud** — A GPU-specialized cloud-infrastructure provider (CoreWeave, Nebius, Lambda) renting AI compute capacity, distinct from a diversified hyperscaler.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; CRWV carries a large net-debt position at a reported 11.98× ratio, nearly 5× this framework's standard 2.5× threshold.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit. CRWV's computed TTM figure is -25.40%.
- **Owner Earnings** — Warren Buffett's adjusted cash-flow measure (Net Income + D&A − Maintenance CapEx only); not applied here since Hybrid Upgrade 1 is scoped only to MSFT/GOOGL/META/AMZN.
- **Quality Score** — A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. CRWV scores 35.6.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it into profit. CRWV's TTM ROIC is -0.33% (negative).
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 6** — This framework's fair-value-methodology instruction to normalize financial statements before valuing a business — strip out one-time/base-effect distortions rather than take them at face value.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. Today's +16.3% move is fully explained by (c), the Q2 2026 earnings release — not an unexplained move.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of financial data, rolling forward each quarter, as distinct from a fixed fiscal year.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
