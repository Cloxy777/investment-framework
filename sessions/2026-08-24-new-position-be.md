# New Position Evaluation: BE (Bloom Energy Corp) — 2026-08-24

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Ticker:** BE — NYSE (Class A), IBKR contract_id 326398514
**Company:** Bloom Energy Corporation — designs, manufactures, and sells solid-oxide fuel cell ("Bloom Energy Server") on-site power generation systems; increasingly positioned as an on-site/behind-the-meter power source for AI data centers alongside its legacy industrial/commercial customer base
**Fiscal year end:** December 31
**10Y US Treasury yield:** 4.69% (FRED `DGS10`, 2026-08-20 close — most recent available) — recorded for completeness only; this session stops before the Rate Environment Gate would apply (see §3)
**First-use jargon decode:** see closing Glossary (§7)

---

## 0. Why this session exists — trigger source, and watchlist check

A Telegram post on `t.me/FinnInvestChannel` (post FinnInvestChannel/3137, ~2026-08-24 15:42 UTC) reported that Paul Pelosi purchased 15,000 shares of BE plus 200 long-term call options (\$100 strike, expiring June 2027) — a **congressional-trading disclosure, not financial data**. Per this repo's standing Rule 0 convention, the Telegram post's text is used **only** as the reason this session was triggered — none of its claims (share count, option strike, expiry, or the transaction itself) are treated as a financial input anywhere below.

**Watchlist check performed before assuming no entry exists:** `find -iname "*BE*"` under `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`, plus a direct `grep` for "BE"/"Bloom Energy" against `portfolio/holdings.md`, returned **no matches anywhere** in the repo. Confirmed genuine first-ever evaluation. `watchlist/STALE.md` was also checked — BE carries no entry there (expected, since no prior score exists for a methodology version to invalidate).

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

Contract confirmed via `search_contracts("BE")`: contract_id **326398514**, NYSE, "BLOOM ENERGY CORP-A" — the correct primary US listing (other results returned were unrelated tickers sharing the "BE" string — Beleave Inc, Belgium/Saudi bonds, BE Semiconductor, Franklin/Beacon funds, etc. — none used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **\$204.68** | IBKR `get_price_snapshot`, `last` field, contract_id 326398514. `is_close: false`, `halted: false`, timestamp resolves to 2026-08-24 16:12:52 UTC — a live, current-session print. |
| Change vs. prior close | +\$3.23 (+1.6%) | IBKR `change` |
| 52-week high / low | \$351.25 / \$47.84 | IBKR `misc_statistics` |
| 13-week / 26-week high / low | \$351.25 / \$157.35 · \$351.25 / \$116.54 | IBKR `misc_statistics` |
| Open 52 weeks ago | \$44.80 | IBKR `misc_statistics` |
| Dividend yield | 0.0% (no dividend) | IBKR `dividend_yield` |

\$204.68 sits well off the 52-week high (\$351.25, roughly −42%) and far above the 52-week low (\$47.84, roughly +328%) — an extremely wide range, context only, not scored. No order-setup arithmetic is performed this session (see §3 for why).

---

## 2. Data Sourcing

`yfinance` was attempted first and confirmed broken — `curl_cffi.requests.exceptions.SSLError: Recv failure: Connection reset by peer` on a basic `Ticker.info` call, consistent with this repo's documented SSL breakage since 2026-07-07. **Primary sources used instead:**

- **SEC XBRL `companyconcept` / `companyfacts` API** (`data.sec.gov`, CIK **0001664703**) for `NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`, `ProfitLoss`, `OperatingIncomeLoss`, `CashAndCashEquivalentsAtCarryingValue`, and `LongTermDebt` — audited, tagged, company-filed figures, fiscal-year-labeled by the SEC's own structured data (not a vendor's re-derivation). CIK confirmed via SEC EDGAR full-text/company search (WebSearch).
- **stockanalysis.com** (WebFetch) for supplementary/derived figures (gross margin, forward PE, EV/EBITDA, Net Debt/EBITDA) — every figure that mattered to the hard-disqualifier conclusion was independently cross-verified against the SEC XBRL primary source before being relied upon (see §3.3 — the two sources match to the dollar).
- **StockTitan** (WebFetch) for the Q2 2026 earnings summary and recent partnership announcements (§4) — qualitative color only, not used as a scored input.
- **FRED** `DGS10` CSV for the 10Y Treasury yield (§ header) — fetched successfully this session (unlike some recent sessions where FRED/CNBC returned 403), but not decision-relevant since this evaluation stops before the Rate Environment Gate.

**Data-quality note:** stockanalysis.com's own reported FY2025 Operating Income (\$88.47M) and Net Income (−\$88.43M) differ modestly from the SEC XBRL primary figures used below (GAAP Operating Income \$72.802M; `ProfitLoss` including noncontrolling interests −\$87.140M) — likely reflecting a different noncontrolling-interest or adjustment convention. This session uses its own SEC-XBRL-sourced figures wherever a figure is decision-relevant (§3.3's FCF numbers match stockanalysis.com to the dollar, so this discrepancy doesn't affect the disqualifier conclusion either way).

---

## 3. Phase 01 — Quality Score: Hard Disqualifier Check

Per [quality-scoring.md](../framework/quality-scoring.md), three hard disqualifiers fail a company **regardless of weighted score**. Checking the FCF-positive-streak test carefully for BE, per this session's explicit instruction (the same disqualifier fired for SOUN earlier today).

### 3.1 — FCF/Net Income conversion ratio <70% for 2+ consecutive years

| Fiscal Year | Operating Cash Flow | CapEx | FCF | Net Income (`ProfitLoss`, incl. NCI) | FCF/NI |
|---|---|---|---|---|---|
| FY2024 | \$91.998M | \$58.852M | \$33.146M | **−\$27.203M** | not meaningful — NI negative |
| FY2025 | \$113.949M | \$56.759M | \$57.190M | **−\$87.140M** | not meaningful — NI negative |

(All figures: SEC XBRL `companyconcept`, primary-sourced — see §2.)

Net Income (GAAP, including noncontrolling interests) is negative in every fiscal year 2021–2025 despite FCF turning positive in FY2024–FY2025 — the ratio is not meaningful in the sense this check intends (catching cash-flow-quality problems in an already-profitable company) in either computable year. **This disqualifier does NOT fire** — there is no 2-consecutive-year run *below* 70% among the computable ones, because none are computable in the intended sense.

### 3.2 — Net Debt/EBITDA over threshold (2.5× standard)

Not a payment network, exchange, or asset-light financial — the standard 2.5× threshold and /4 denominator apply, no Upgrade 5 override.

| Item | FY2025 value | Source |
|---|---|---|
| Total debt (`LongTermDebt`, current + noncurrent) | \$2,617.879M | SEC XBRL, primary |
| Cash and cash equivalents | \$2,454.108M | SEC XBRL, primary |
| **Net debt** | **\$163.771M** | Calculated |
| Net Debt/EBITDA (reported) | **0.24×** | stockanalysis.com ratios |

Net debt is small relative to BE's ~\$2.45B cash balance (a large FY2025 convertible-notes raise, evidently not yet deployed) — comfortably clears the 2.5× threshold under any reasonable EBITDA denominator. **This disqualifier does NOT fire.**

### 3.3 — Not FCF-positive for 3+ consecutive years

Per the 2026-08-05 rolling-window clarification, this test uses **the most recently completed fiscal years available at the time of scoring**. BE's FY2025 10-K has been filed (2026-02-09), so the current window is **FY2023–FY2025**:

| Fiscal Year | Operating Cash Flow | CapEx | **FCF** | Source |
|---|---|---|---|---|
| FY2021 | −\$60.681M | \$49.810M | **−\$110.491M** | SEC XBRL, primary |
| FY2022 | −\$191.723M | \$116.823M | **−\$308.546M** | SEC XBRL, primary |
| FY2023 | −\$372.531M | \$83.739M | **−\$456.270M** | SEC XBRL, primary |
| FY2024 | \$91.998M | \$58.852M | **+\$33.146M** | SEC XBRL, primary |
| FY2025 | \$113.949M | \$56.759M | **+\$57.190M** | SEC XBRL, primary |

(Cross-checked against stockanalysis.com's independently-reported FCF figures for all five years — matches to the dollar/cent in every year, e.g. FY2023 −\$456.27M, FY2025 \$57.19M.)

**FY2023 was FCF-negative** (a deep −\$456.27M, BE's worst year on record). The current streak of consecutive FCF-positive fiscal years is **2 (FY2024–FY2025), not yet 3**. This bright-line test carries no growth-capex or other carve-out in quality-scoring.md — unlike §3.1's FCF/NI check, there is no documented exception clause attached to this disqualifier.

### **HARD DISQUALIFIER FIRES: not FCF-positive for 3+ consecutive years.**

This is a clean, decisively-supported result — verified against Bloom Energy's own SEC-filed, XBRL-tagged figures, cross-checked against a second independent source (stockanalysis.com) to the dollar. Per [quality-scoring.md](../framework/quality-scoring.md) ("a weighted average can't average away an outright balance-sheet or cash-flow-quality failure") and [.claude/commands/new-position.md](../.claude/commands/new-position.md) step 2, **this session stops here**. No weighted Phase 01 Quality Score (Profitability/Margins/Growth/Moat/FCF-Quality sub-scores), Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.

---

## 4. Why this reads as "not yet," not "no" — context for the recommendation and next review

Nothing below is scored — it's qualitative color relevant to judging how close BE is to clearing §3.3, and separately, on the Telegram post's actual substance (a congressional trade disclosure, not financial data).

**4.1 — The FCF-positive streak is actively extending, not stalling.** Q1 FY2026 (Jan–Mar 2026) alone already shows OCF \$73.610M against CapEx \$26.182M — an implied **+\$47.428M** of FCF in a single quarter, comparable to over 80% of all of FY2024. Revenue growth has also sharply accelerated: Q2 2026 revenue hit a record \$1.065B, **+165.5% YoY**, with full-year 2026 guidance raised to **\$3.9–4.2B** (vs. FY2025's \$2.024B — roughly 93–108% YoY guided growth) and non-GAAP operating income guided at **\$800–900M**. If FY2026 closes FCF-positive (as the Q1 print and the guided operating-income trajectory strongly suggest, though **not yet confirmed — nothing here is treated as reported**), the rolling window at the next evaluation (FY2024–FY2025–FY2026) would show **3 consecutive positive years for the first time**, clearing §3.3.

**4.2 — The AI/data-center power narrative, not scored but genuinely substantial:** per StockTitan's Q2 2026 summary, Bloom's AI-infrastructure customer base has grown to "nearly two dozen customers with approximately 250 MW of capacity, up from nearly zero" roughly two years ago, through partnerships including American Electric Power, Brookfield, Equinix, Nebius, and Oracle. Notable 2026 announcements: an Oracle agreement covering up to **2.8 GW** (1.2 GW initially contracted, announced April 13); a Brookfield financing-partnership framework expanded from \$5B to **\$25B** (announced June 30); and a **\$1.7B** Nebius fuel-cell deployment project (announced July 16). This is the demand story behind the FY2026 guidance raise in §4.1 — cited here as color, not as a scored Moat Signal (no weighted Quality Score was computed this session to attach it to).

**4.3 — Forward PE / PEG were not going to be usable inputs even had the gate cleared.** BE's GAAP net income has been negative every year 2021–2025 (§3.1) — well short of the "3+ years EPS growth >15% on a clean, non-distorted earnings base" Fast-Grower eligibility bar (Upgrade 3). A future Phase 02 pass would need to redistribute PEG's 15% weight to EV/EBIT and very likely apply the no-history fallback (FwdPE_Score = 50.0, flagged) given the shallow, still-loss-making earnings history — similar to the AFRM/SOFI precedent in this repo.

**4.4 — Best bear case (informational only, no scored conclusion drawn):** BE's FCF turn is only 2 fiscal years old and followed a −\$456M FY2023, so a single disappointing quarter could plausibly interrupt the streak again; the AI-data-center growth narrative is heavily forward-looking and dependent on continued hyperscaler capex cycles (a reversal in AI infrastructure spending would hit the Oracle/Brookfield/Nebius pipeline directly); and the stock's 52-week range (\$47.84–\$351.25, a >7x band) reflects a name still being actively re-rated on a still-young, not-yet-fully-proven profitability inflection — precisely the kind of situation this framework's bright-line 3-consecutive-year FCF test exists to sit out rather than chase.

**4.5 — On the Telegram post's actual substance:** the post reported a congressional-trading disclosure (a Paul Pelosi purchase of BE shares and long-dated calls). This framework does not, and did not here, treat any third party's trading activity — congressional or otherwise — as a financial input; it triggered this evaluation and nothing more. Whatever informational edge such disclosures might or might not carry is outside this framework's scope to assess.

---

## 5. Recommendation: **PASS (no entry) — Quality Gate FAILS on a clean hard disqualifier**

**Do not enter BE this session.** A hard disqualifier fires cleanly on Bloom Energy's own SEC-filed, XBRL-tagged cash flow figures (cross-verified against a second independent source to the dollar): the current 3-fiscal-year window (FY2023–FY2025) contains one deeply negative year (FY2023, −\$456.27M) before the FY2024–FY2025 turn to positive FCF, so the company has not yet sustained the 3+ consecutive FCF-positive years quality-scoring.md requires. **No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work was performed**, consistent with the command specification's instruction to stop at a hard-disqualifier failure.

Unlike SOUN's clean fail earlier today (5 of 5 years FCF-negative, no positive trend at all), BE's is a **near-miss**: 2 consecutive positive years, an accelerating revenue/FCF trajectory, and a Q1 FY2026 print that already implies FY2026 will likely extend the streak to 3. This reads as "not yet eligible" rather than "structurally disqualified" — see §6 for the specific trigger that would clear it.

**The triggering Telegram post** (a congressional-trading disclosure naming a Paul Pelosi purchase of BE shares and calls) was used only as the reason to run this first-ever evaluation; it is not, and was never treated as, a financial input.

---

## 6. Next Review Trigger

No routine re-check is scheduled on a numeric-score basis (no Phase 02 score exists to go stale — the Quality Gate never cleared). Re-evaluate on any of the following, whichever comes first:

- **Bloom Energy's FY2026 10-K** (expected ~February 2027) — if FY2026 closes FCF-positive, the rolling window (FY2024–FY2026) would show 3 consecutive positive years for the first time, clearing §3.3. Given the Q1 FY2026 print (+\$47.4M) and the FY2026 guidance raise (§4.1), this is the most likely near-term path to a cleared gate — but is **not** treated as reported until it actually is.
- A material, documented reversal in the FCF trend (not merely a single soft quarter) — a genuine Rule 9-style fundamental change.
- The standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move (BE's realized volatility this year, per §1's 52-week range, means this trigger is a real possibility, not a formality).

Absent a qualifying trigger, a future Telegram mention of BE should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Glossary

| Term | Meaning |
|---|---|
| **10-K (Annual Report)** | The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements — the primary source for Bloom Energy's FY2021–FY2025 cash flow figures above. |
| **10-Q (Quarterly Report)** | The quarterly financial-disclosure report filed between annual 10-Ks — the source for BE's Q1 FY2026 (Jan–Mar 2026) cash flow figures in §4.1. |
| **Active power capacity / Contracted power capacity (data center)** | Two related metrics an AI-infrastructure/data-center operator (or its power supplier) discloses to show scale and forward demand: active capacity is power already energized and in live use; contracted capacity is the larger forward-looking total secured but not yet fully online. Used as context for the MW/GW figures in §4.2. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets; the deduction from operating cash flow that turns OCF into FCF throughout §3.3 and §4.1. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every EDGAR filer — Bloom Energy's is 0001664703, used to construct the SEC XBRL API paths this session pulled from. |
| **Convertible senior notes** | A bond that can be converted into a fixed number of the issuer's shares instead of being repaid in cash — the likely source of BE's large FY2025 cash build (§3.2), a debt raise still mostly undeployed as of this session. |
| **EDGAR** | The SEC's free public database of every US-registered company's filings — the source for BE's CIK and filing history. |
| **EV/EBIT, EV/EBITDA** | Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to operating profit; referenced only as unscored context (§2 data-quality note) since no Phase 02 score was computed this session. |
| **FCF (Free Cash Flow)** | Operating cash flow minus capital expenditure — cash a business generates after running and maintaining itself. Negative in FY2021–FY2023, positive in FY2024–FY2025 for Bloom Energy (§3.3), the basis for this session's hard-disqualifier fail (2 consecutive positive years, not yet 3). |
| **Fiscal Year (FY)** | A company's 12-month accounting year. Bloom Energy's fiscal year matches the calendar year (ends December 31). |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook; all figures above are GAAP, company-filed, not a non-GAAP or adjusted metric (§2 flags where stockanalysis.com's figures diverge slightly, likely on an adjustment/NCI convention). |
| **Hard disqualifier** | One of three Quality Score conditions ([quality-scoring.md](../framework/quality-scoring.md)) that fails a company regardless of its weighted sub-score total. Bloom Energy fails on "not FCF-positive for 3+ consecutive years" (§3.3). |
| **MW / GW (Megawatt / Gigawatt)** | Units of electrical power capacity; 1 GW = 1,000 MW. Used in §4.2 to describe the scale of Bloom Energy's AI-data-center power deployments and contracted pipeline (e.g. Oracle's up-to-2.8 GW agreement) — unscored qualitative context, not a financial input. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — this framework's primary balance-sheet-risk gate. Computed at 0.24× for BE (§3.2) — comfortably clears the 2.5× threshold; not the disqualifier that fired. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. Not computed for BE this session — a hard disqualifier fired first (§3.3). |
| **Rolling-window (disqualifier test)** | This framework's convention that the FCF-positive-streak hard-disqualifier test uses the most recently completed fiscal years available at the time of scoring, rolling forward as each new fiscal year reports. Used here to set the FY2023–FY2025 window (§3.3), and to explain why an FY2026 close could clear the gate at the next review (§6). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work, and to never treat a Telegram post's claims — including a third-party trading disclosure — as a financial input. The live price (§1) was fetched via IBKR before any other work in this session. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — not used in this session since the evaluation stopped at the annual-fiscal-year hard-disqualifier check before any TTM-based sub-score would have been computed. |
| **XBRL** | The SEC's structured, machine-readable data format for financial-statement figures — the format this session's `companyconcept`/`companyfacts` API pulls (`NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`, `ProfitLoss`, `OperatingIncomeLoss`, `CashAndCashEquivalentsAtCarryingValue`, `LongTermDebt`) came in. |
