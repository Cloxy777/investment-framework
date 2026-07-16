# New Position Evaluation — SMR (NuScale Power Corporation, NYSE)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 2026-07-16
**10Y US Treasury Yield:** 4.58% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-07-14 — normal 1-day FRED reporting lag)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force is **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current SMR portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md), `grep -i "SMR\|NuScale"` returns no match).
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is SMR's first-ever evaluation under this framework.
**Sector:** Nuclear power equipment — small modular reactor (SMR) design and licensing, pre-commercial (no completed commercial power-plant sale as of this session).
**Filer type:** SEC domestic filer, CIK **0001822966**. Formerly "Spring Valley Acquisition Corp." — went public via SPAC merger (name changed 2022-04-29). Fiscal year ends 31 December.
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

FinnInvestChannel Telegram post #2945 (2026-07-16, ~15:01 UTC) listed "52-week lows: Oklo, NuScale, Oracle" with no further detail. NuScale Power Corporation trades as **SMR** on NYSE. Per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 4 ("No watchlist entry exists at all → `/new-position <TICKER>`"), this session was triggered regardless of the mention being a bare 52-week-low listing with no other claimed catalyst. **Per Rule 0, no claim from the triggering post is used as financial data anywhere below** — the post is only the reason this ticker was looked at; every figure in this session is independently fetched/sourced and cited. (The post's "52-week low" framing is independently corroborated in §1 below, from IBKR's own live market-data snapshot — not from the post.)

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

**Contract disambiguation:** `search_contracts("SMR")` returned 45+ matches, including several decoys that are *not* the underlying stock — notably leveraged/derivative ETF products tracking SMR (`SMU` "TRADR 2X LONG SMR DAILY ETF", `SMUP` "T-REX 2XL SMR DT ETF"), a same-ticker unrelated Australian coal miner (ASX:SMR "Stanmore Resources"), and various unrelated tickers sharing the "SMR" substring. The correct instrument is **NYSE:SMR, contract_id 559289446, "NUSCALE POWER CORP", country_code US** — confirmed as the primary US equity listing, not a leveraged derivative or an unrelated company.

| Field | Value | Detail |
|---|---|---|
| **Last trade** | **$7.60** | `is_close: false` — live intraday trade, not a prior close |
| Bid / Ask | $7.59 / $7.60 | Tight spread, liquid quote |
| Change | −$0.76 / **−9.09%** | Large single-day move — see §1.1 |
| Today's volume | 11,669,150 shares | Elevated |
| 52-week high | $57.33 | |
| 52-week low (prior, pre-today) | $8.08 | |
| Price 52 weeks ago (`open_52w`) | $42.56 | Implies roughly an 82% decline over the trailing year at today's $7.60 |

**Today's $7.60 print is below the previously-recorded 52-week low of $8.08 — i.e. SMR made a fresh 52-week low today**, independently confirming (via IBKR's own live data, not the Telegram post) that the post's "52-week lows: ... NuScale ..." framing was accurate as a trigger, even though it was never used as a scored input.

**Live price used throughout this session: $7.60.**

### 1.1 Note on the −9.09% single-day move

Rule 9 in [fair-value-methodology.md](../framework/fair-value-methodology.md) flags a **>15% unexplained move** as a mandatory re-valuation trigger; today's −9.09% move doesn't independently cross that threshold, but is large enough to be worth noting. A web search (2026-07-16) found this is consistent with an established, sustained multi-month decline, not a single new catalyst today: recent coverage cites project delays, weak operating results, no binding/closed commercial customer contracts, a securities-fraud class-action lawsuit over alleged misrepresentation of commercialization partner **ENTRA1 Energy**'s milestone-payment exposure (a "$495M payment in Q3 2025, with potential future payments exceeding $3B" per the lawsuit's allegations), and long-standing backer **Fluor Corp** reducing/exiting its stake by mid-2026. These are cited here as independently-sourced qualitative context, not as scored financial inputs (Rule 0) — the actual scoring in §3 below uses only SEC XBRL structured data.

Sources: [ENTRA1 Lawsuits And Commercialization Concerns (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/entra1-lawsuits-commercialization-concerns-might-151510889.html), [NuScale faces ENTRA1 lawsuits (Nuclear Engineering International)](https://www.neimagazine.com/news/nuscale-faces-entra1-lawsuits/), [SMR Court Notice: Securities Fraud Class Action (PR Newswire)](https://www.prnewswire.com/news-releases/smr-court-notice-nuscale-power-hit-with-securities-fraud-class-action-over-entra1-issues-after-12-stock-drop-302734887.html), [Why NuScale Power (SMR) Is Down... Mounting Delays, Weak Results And No Firm Contracts (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/why-nuscale-power-smr-down-150821532.html).

---

## 2. Data Source Note

`yfinance`'s `curl_cffi` backend failed with a TLS-level `Recv failure: Connection reset by peer` through this session's proxy (a recurring, previously-documented environment issue in this repo — same failure class as prior sessions). A plain `requests`-based fetch to the same Yahoo hosts succeeded (got a normal HTTP 401/429 rather than a connection reset), confirming the proxy itself is not the blocker — the issue is specific to `curl_cffi`'s TLS fingerprint-impersonation layer. Rather than fight that further, **fundamentals were sourced directly from SEC EDGAR's XBRL `companyfacts` API** (`https://data.sec.gov/api/xbrl/companyfacts/CIK0001822966.json`) — a primary, Rule-0-compliant source requiring no cookie/crumb workaround, pulling NuScale's own filed 10-K figures (FY2020–FY2025) directly. The 10Y Treasury yield was sourced from FRED's public CSV endpoint (`fredgraph.csv?id=DGS10`), which also doesn't require the blocked backend. No required input was invented or estimated; every figure below is cited to this SEC XBRL pull or explicitly flagged where a tag was unavailable (e.g. no structured Depreciation & Amortization tag was found — flagged in §3.2).

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | SMR data (SEC XBRL, `us-gaap` tags, FY2020–FY2025 10-K annual figures) | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | Free Cash Flow (Operating Cash Flow − CapEx) by fiscal year: FY2020 **−$3.87M** (−0.346M OCF − 3.526M CapEx) / FY2021 **−$101.1M** / FY2022 **−$150.9M** / FY2023 **−$185.0M** / FY2024 **−$108.7M** / FY2025 **−$460.1M** (−459.610M OCF − 0.508M CapEx). **FCF has been negative in every one of the 6 fiscal years on record since the company began filing under this CIK — never once FCF-positive, let alone for 3 consecutive years.** Burn is *accelerating*, not stabilizing: FY2025's outflow (−$460.1M) is more than 4× FY2024's (−$108.7M). | **FAILS — fires decisively.** |
| **Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light)** | No `LongTermDebt`, `LongTermDebtNoncurrent`, or `DebtCurrent` tags found anywhere in the XBRL filing history — cross-checked: the company appears to carry **no funded financial debt**. Cash and cash equivalents (FY2025): **$836.4M**. Net Debt ≈ **−$836.4M (net cash)**. | **Does not fire** (best case — zero debt). |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FY2025: FCF −$460.1M ÷ Net Income −$355.8M = **129.3%** (a positive ratio only because *both* figures are negative — see §3.2 FCF Quality note; this is **not** a case of healthy cash conversion of real profit). Read literally against the ">70%" text, this specific disqualifier condition does not mechanically fire — but per [quality-scoring.md](../framework/quality-scoring.md)'s own glossary note, **the FCF-positivity disqualifier above (which does fire) carries no carve-out**, unlike this one. | Not the operative disqualifier here — moot given the row above. |

**Result: hard disqualifier fires — "Not FCF-positive for 3+ consecutive years."** Per [quality-scoring.md](../framework/quality-scoring.md): *"These mirror the existing Phase 01 non-negotiables — a weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* And per the glossary's **Hard disqualifier** entry: *"Not every hard disqualifier carries a carve-out: the FCF-positivity check has none."* NuScale is a pre-commercial company that has never generated positive free cash flow in its public reporting history — this is not a borderline or judgment-call case.

### 3.2 Sub-scores computed anyway, for full transparency (per operating-brief.md's "no black-box outputs" — shown even though §3.1 already determines the outcome)

| Sub-score (weight) | Formula & inputs (all FY2025, SEC XBRL, 10-K filed 2026-02-26) | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin = Net Income −$355,794,000 ÷ Revenue $31,479,000 = **−1,130.5%**. NetMargin_Component = clamp((−1130.5/30)×100, 0, 100) = **0.0**. ROIC: NOPAT ≈ EBIT (Operating Income Loss) = **−$689,571,000** (effective tax rate immaterial — FY2025 `IncomeTaxExpenseBenefit` was only $322,000 against a $664.1M pretax loss, consistent with a full valuation allowance on a company with no taxable income). Invested Capital = Total Debt $0 + Stockholders' Equity $1,168,841,000 − Cash $836,417,000 = **$332,424,000**. ROIC = −689,571,000 / 332,424,000 = **−207.4%**. ROIC_Component = clamp((−207.4/30)×100, 0, 100) = **0.0**. Profitability_Score = (0.0+0.0)/2 = **0.0** (the "cap at 40 if not FCF-positive 3yr" rule is moot — already 0). | **0.0** |
| **Margins (15%)** | Gross Margin (FY2025) = $11,431,000 / $31,479,000 = **36.32%**. GrossMargin_Score = clamp((36.32/80)×100, 0, 100) = **45.4**. 5-year trend (all FY, GrossProfit/Revenue): FY2020 40.8% → FY2021 38.2% → FY2022 38.0% → FY2023 16.9% → FY2024 **86.7%** → FY2025 36.3%. **No structural trend** — wildly volatile (16.9%→86.7%→36.3% in 3 successive years), consistent with lumpy, non-recurring engineering/license-fee contract revenue recognition rather than a stable per-unit product margin. No +10 trend bonus applies (trend is not consistently improving; the most recent year is in fact a sharp *decline* from FY2024's spike). **Data-quality flag:** this gross-margin figure is not comparable to a steady-state commercial manufacturer's margin — shown per formula, per Rule 0 ("show every calculation, don't invent"), but flagged as low-confidence given the company has never had a full year of steady commercial-scale revenue. | **45.4** (flagged low-confidence) |
| **Growth (20%)** | Revenue 3yr CAGR: FY2022 $11,804,000 → FY2025 $31,479,000 = (31,479/11,804)^(1/3) − 1 = **+38.66%**. Base = clamp((38.66/25)×100, 0, 100) = **100.0** (clamped). **Modifier — judgment call, flagged explicitly:** two documented, cited facts pull in opposite directions. (a) *TAM-expansion narrative*: AI-data-center power demand is a well-documented, sector-wide nuclear/SMR tailwind, and NuScale holds the only US NRC Standard Design Approval for an SMR (see §3.2 Moat below) — a real industry-level catalyst. (b) *Documented structural deceleration, company-specific*: FY2025 revenue **fell 15.0% year-over-year** ($37.045M FY2024 → $31.479M FY2025, both SEC-filed 10-K figures) even as the sector narrative strengthened; independently-sourced press (§1.1) reports "no firm/binding customer contracts," "project delays," and (per one Yahoo Finance article) a quarter with revenue down 96% YoY. Applying the modifier to the *company's own* cited revenue trajectory (rather than a macro/sector narrative not yet reflected in NuScale's own numbers) is the more Rule-0-consistent read — **−10 applied** (documented structural deceleration), not +10. Growth_Score = clamp(100.0 − 10, 0, 100) = **90.0**. *(Flagged: this 3yr CAGR is itself heavily base-effect-distorted — growing off a near-zero, lumpy contract-revenue base is not evidence of a stable, repeatable commercial growth trajectory; shown per formula, not asserted as a meaningful growth signal.)* | **90.0** (flagged low-confidence / distorted base effect) |
| **Balance Sheet (15%)** | Total Debt = **$0** (no debt tags found in XBRL — confirmed debt-free). Net Debt = −$836,417,000 (net cash). **Formula inapplicability flagged**: `BalanceSheet_Score = clamp(100×(1−NetDebt/EBITDA/4))` assumes positive EBITDA (the ratio's economic meaning is "years of cash profit needed to retire debt"); FY2025 EBITDA is deeply negative (Operating Income Loss −$689.6M, before an unavailable D&A add-back — no `DepreciationDepletionAndAmortization` tag found in the filing, flagged as a data gap), so dividing a negative Net Debt by a negative EBITDA produces a mathematically defined but economically meaningless positive ratio. Per Rule 0, this formula's output is not force-fit into the weighted sum; instead, the substantive fact — **zero funded debt** — is scored at its best-defined reference point, **100.0** (the formula's 0× row). **Separately flagged, not captured by this sub-score**: cash-runway risk is real and severe — $836.4M cash against a FY2025 operating cash outflow of −$459.6M implies under ~2 years of runway at the current (and accelerating) burn rate absent further capital raises/dilution. | **100.0** (flagged — masks real runway risk not captured by a leverage-only metric) |
| **Moat Signal (15%)** | See evidence table below — **0 of 5** signals cleared the cited-evidence bar. | **0.0** |
| **FCF Quality (10%)** | FCF/NI = −$460,118,000 / −$355,794,000 = **129.3%** → mechanically, clamp(((1.293−0.40)/0.60)×100, 0, 100) = **100.0**. **Flagged as not meaningful**: this formula is designed to catch *paper profit that isn't real cash* (a ratio well below 100% when net income is positive but FCF lags it); here both figures are negative, so the ratio's >100% reading does not mean "healthy cash conversion of profit" — there is no profit to convert. Shown per formula for transparency, exactly as flagged, not asserted as a genuine quality signal. | **100.0** (flagged — mechanically computed, not substantively meaningful) |

**Moat signal evidence (cited, per signal — all five checked against the framework's required "cited evidence" bar):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable or growing | NuScale holds the **only US NRC Standard Design Approval** for a small modular reactor (VOYGR-4/6/12 designs, up to 924MWe) — a real, citable regulatory-leadership fact. But **no completed/closed commercial power-plant sale exists yet** (multiple 2026 press sources, §1.1) — there is no commercial market with a share to hold. Regulatory first-mover status ≠ cited market-share data (company filings or third-party market-share reports), which the framework's evidence bar specifically requires. | **FALSE** (real fact, wrong category — not force-fit) |
| Brand premium | No evidence of pricing power — no closed commercial contracts exist to demonstrate premium pricing without volume loss. | **FALSE** |
| Network effect | Not a platform/marketplace business model. | **FALSE** |
| Switching costs | No installed customer base yet to be locked in — nothing to switch away from. | **FALSE** |
| Scale cost advantage | No commercial-scale production and no cost-per-unit data (pre-commercial company). | **FALSE** |

### 3.3 Final weighted Quality Score (computed for completeness, despite §3.1's disqualifier already determining the outcome)

```
Quality Score = (0.0 × 0.25) + (45.4 × 0.15) + (90.0 × 0.20) + (100.0 × 0.15) + (0.0 × 0.15) + (100.0 × 0.10)
              = 0.0 + 6.81 + 18.0 + 15.0 + 0.0 + 10.0
              = 49.81 → 49.8 (rounded to nearest 0.1)
```

**49.8 < 80.0 — fails the gate on the weighted score alone**, even *before* invoking the hard disqualifier, and even though two of the six sub-scores here (Balance Sheet 100.0, FCF Quality 100.0) are inflated by formula edge-cases flagged above as not substantively meaningful for a debt-free-but-deeply-cash-burning, pre-profit company. Discounting those two sub-scores toward something more representative of actual balance-sheet/cash-flow risk would only push the weighted score further below 80.0, not toward it. The conclusion is not sensitive to any of this session's judgment calls (the Growth modifier direction, the Margins trend read, or how strictly the Balance Sheet/FCF Quality edge cases are treated).

### Result: **Phase 01 FAIL — hard disqualifier fired ("Not FCF-positive for 3+ consecutive years," no carve-out available) AND weighted score (49.8) is 30.2 points short of the 80.0 gate.**

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... or a hard disqualifier fires, stop there and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring, per the Phase 03 table in [strategy.md](../framework/strategy.md) (Composite Score is a precondition for that table applying at all).

This is not a verdict that small modular reactor technology or the AI-driven nuclear-power-demand narrative is unsound — NuScale's NRC design approval is a genuine, citable regulatory achievement, and the sector tailwind is real. It is a verdict that a pre-commercial company with **zero years of positive free cash flow across its entire public reporting history**, an accelerating cash burn (−$460M in FY2025 alone), no closed commercial contracts, an active securities-fraud class action, and a major backer reducing its stake does not clear this framework's specific, strict definition of "high quality" — regardless of how attractive the stock's 82%-off-highs price might look on its own. This is exactly the "value trap" scenario the 80.0+ Quality Score gate exists to catch (see Glossary).

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) the company's first closed/binding commercial power-plant sale (the single biggest de-risking event for this name); (b) a sustained multi-quarter positive FCF trajectory (not just one favorable quarter); (c) resolution of the ENTRA1 securities-fraud class action; (d) a quarterly earnings release or guidance revision; (e) a management change or material M&A/strategic-investment event (e.g. a new anchor investor replacing Fluor's reduced stake); (f) a >15% stock-price move with no identified cause.
- Absent any of the above, future Telegram mentions of SMR/NuScale should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Data gaps flagged (Rule 0)

- **`yfinance` unusable this session** (documented `curl_cffi` TLS-reset failure through the proxy) — worked around via direct SEC EDGAR XBRL API pull instead; no financial figure below was estimated or inferred to compensate.
- **No structured `DepreciationDepletionAndAmortization` XBRL tag found** for SMR — EBITDA could not be independently derived with a clean D&A add-back; flagged in §3.2's Balance Sheet row rather than estimating a D&A figure.
- **No `LongTermDebt`/`DebtCurrent` XBRL tags found** — read as "no funded debt exists" (corroborated by the company's SPAC-derived, equity/PIPE-funded capital structure) rather than as a missing-data gap, but flagged for transparency since it rests on tag *absence* rather than an explicit "$0" disclosure line.
- **Shares outstanding / market cap** not independently pulled this session (not needed — no Phase 02/position-sizing work was reached).

---

## 8. Total FY2025 loss context (not scored, shown for completeness)

FY2025 consolidated `ProfitLoss` (including noncontrolling interests) was **−$664.5M**, of which **−$308.7M** is allocated to noncontrolling interests under NuScale's Up-C-style post-SPAC capital structure, leaving **−$355.8M** attributable to NuScale Power Corporation's own common shareholders (the figure used as "Net Income" throughout §3.2, consistent with standard EPS/net-margin convention). The larger consolidated figure is cited here only as context — using it instead would not change any conclusion above (all relevant ratios are already unambiguously disqualifying).

---

## 9. Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every company that files with EDGAR — used here to pull NuScale's structured XBRL financial data directly from the SEC.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for SMR since it never clears the 80.0+ Quality Score gate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation & Amortization — a rough proxy for cash operating profit, used in the Net Debt/EBITDA leverage ratio. Not cleanly computable for SMR this session (D&A tag unavailable) and deeply negative regardless.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Negative for NuScale in every fiscal year on record.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; not a meaningful signal when both figures are negative, as flagged in §3.2 for SMR.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. One of this framework's Quality Score Margins sub-score inputs.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score — see [quality-scoring.md](../framework/quality-scoring.md). Unlike the FCF/NI conversion disqualifier (which carries a growth-capex carve-out), the **FCF-positivity disqualifier has no carve-out** — the one that fires for SMR here.
- **IPO (Initial Public Offering)** — The traditional process by which a private company first sells shares to the public on a stock exchange. NuScale instead went public via a **SPAC** merger (see below).
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **NCI (Noncontrolling Interest)** — The portion of a consolidated subsidiary's equity/earnings that belongs to outside shareholders rather than the parent filing the statements — relevant to NuScale's FY2025 loss bridge (§8) under its Up-C-style structure.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative Net Debt means net cash. SMR carries zero funded debt.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. SMR scores 49.8 on the weighted formula, and independently fails via a hard disqualifier.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. SMR does not make this list.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; deeply negative (−207.4%) for SMR.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work — never infer or invent it.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SPAC (Special Purpose Acquisition Company)** — A shell company that raises money via its own IPO to merge with a private company and take it public, as an alternative to a traditional IPO. NuScale went public this way in 2022 (as "Spring Valley Acquisition Corp." pre-merger); often leaves a distorted early public-financial history and a residual Up-C-style capital structure, as seen in SMR's noncontrolling-interest loss allocation (§8).
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **Up-C structure** — An "umbrella partnership corporation" structure, common among companies with a controlling pre-IPO/private-equity sponsor, where the public company holds an economic interest in an operating partnership alongside other unit-holders rather than owning 100% directly — the reason NuScale's FY2025 consolidated loss (−$664.5M) is larger than the loss attributable to its own common shareholders (−$355.8M), the noncontrolling-interest allocation making up the difference (§8).
- **Value trap** — A stock that looks statistically cheap but stays cheap or keeps falling because the underlying business quality is actually deteriorating or was never strong enough to support a re-rating — the risk this framework's 80.0+ Quality Score gate is specifically designed to surface, rather than acting on an attractively-cheap price alone. Directly applicable to SMR's 82%-off-highs price action.
- **XBRL (eXtensible Business Reporting Language)** — A structured, machine-readable data format the SEC requires public companies to tag their financial-statement figures in — used to pull SMR's precise figures directly from SEC filings this session.
