# New Position Evaluation — AAPL (Apple Inc.)

**Task type:** NEW POSITION
**Date:** 2026-07-06
**10Y US Treasury yield:** 4.38% (most recent value on record in this repo, per the 2026-07-06 HNHPF session — cited for header consistency with the standard session template only; **not actually invoked**, since Phase 01 fails before the Rate Environment Gate is reached — see Section 3)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `t.me/tarasguk` post (#11300, ~13:57:22 UTC 2026-07-06) reading "$AVGO продовжили контракт із $AAPL до 2031 року" ("Broadcom extended its contract with Apple through 2031"), reporting that Broadcom's chip-technology licensing agreement with Apple (said to be ~20% of Broadcom's revenue) was extended through 2031, with Apple reportedly unable to bring an in-house replacement chip to market by then. Broadcom (AVGO) is a current holding (3.73% weight, last rescored 2026-07-04 — Quality Score 82.1, Composite Score 43.1). AAPL has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). Per [.claude/commands/telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's first bullet ("No watchlist entry exists at all → `/new-position <TICKER>`"), this proceeds as a standard `/new-position` run — same "first mention of an untracked name gets a full evaluation regardless of how thin the trigger is" precedent as HNHPF/OUST/AMD/CRCL. Per Rule 0, **no claim from the triggering post is used as a financial input anywhere below** — neither the contract-extension claim nor the "~20% of Broadcom's revenue" figure is independently verified or used in this session; the post is only the reason AAPL was looked at today.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any valuation work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 265598, NASDAQ — "APPLE INC") | **$312.84** | Last trade at 2026-07-06T16:09:53Z, `is_close: false`, `halted: false` — a genuine live intraday print (well within the 13:30–20:00 UTC regular US trading session), not a stale/prior-close figure. |
| Day change (same snapshot) | **+$4.21 (+1.36%)** on the day | not used as a financial input — directional context only |
| Bid/ask | $312.82 / $312.87 | live NBBO at fetch time |
| 52-week range (IBKR `misc_statistics`) | low **$200.879** / high **$317.40** | 13-week and 26-week highs are identical to the 52-week high ($317.40), meaning the 52-week high was set within the trailing 13 weeks — current price is ~1.4% below that recent high and +55.7% above the 52-week low. |
| Dividend yield (IBKR) | 0.34% | not used as a scoring input in this session (gate fails before the Upside/Downside Modifier's shareholder-yield component would be needed) — shown for completeness. |

**Live price used throughout this session: $312.84.**

---

## 2. Data Source Note — AAPL is a US SEC filer; `yfinance` not attempted (documented environment failure), SEC XBRL used directly

Apple Inc. is a US-domestic SEC registrant (**CIK 0000320193**), filing Form 10-K/10-Q. Per this session's own instructions and the repeated, documented `curl_cffi` TLS-impersonation failure precedent already established across AAPL/CHTR/WSE/AMD/CDR/CRCL/OUST/NKE sessions in this repo, `yfinance` was not separately re-attempted (expected to fail identically and add no new information). Fundamentals were instead sourced directly from:

- **SEC XBRL `companyfacts` and `companyconcept` APIs** (`data.sec.gov/api/xbrl/...`) — for the full FY2021–FY2025 annual time series and the underlying FY2025/FY2026 quarterly (10-Q) figures used to reconstruct trailing-twelve-month (TTM) numbers through the most recent filed quarter (fiscal Q2 2026, period ended 2026-03-28, Form 10-Q filed 2026-05-01 — Apple's fiscal Q3 2026 10-Q is not yet filed as of this session's date).
- **Apple's own FY2025 Form 10-K** (accession 0000320193-25-000079, filed 2025-10-31, period ended 2025-09-27) — primary filing text, used for the Products/Services gross-margin disaggregation table (Item 7 MD&A) and the revenue-by-product-category note (Note — Revenue, "Disaggregated Net Sales," R38.htm).
- **Third-party market-share and industry sources**, cited individually in Section 3.2's Moat Signal table, for qualitative evidence the SEC filings don't carry (global smartphone unit/premium-segment share, ecosystem-switching-cost statistics, a peer gross-margin comparison).

Every quantitative figure in Section 3 is either a direct SEC XBRL/10-K figure or an explicitly-shown derivation from two or more such figures (e.g. TTM = sum of four disclosed quarters). No required Phase 01 input was invented, estimated, or inferred from the triggering post.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | AAPL data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FCF (Operating Cash Flow − CapEx, both from SEC XBRL annual 10-K figures): FY2021 **$92.953B**, FY2022 **$111.443B**, FY2023 **$99.584B**, FY2024 **$108.807B**, FY2025 **$98.767B** — **FCF-positive every year on record (5 of 5 shown, and every fiscal year for over two decades).** | **PASS — does not fire.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | As of the most recent balance sheet (2026-03-28, Q2 FY2026 10-Q): Total debt = Long-term debt (noncurrent $74.404B + current $8.310B) + Commercial paper $1.997B = **$84.711B**. Liquid assets = Cash $45.572B + Marketable securities (current $22.935B + noncurrent $78.088B) = **$146.595B**. **Net debt = −$61.884B (net cash)**. TTM EBITDA (Section 3.2) = $159.976B. Net Debt/EBITDA = **−0.39×**. | **PASS — does not fire (net cash position).** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | FCF/NI: FY2021 **98.18%**, FY2022 **111.66%**, FY2023 **102.67%**, FY2024 **116.08%**, FY2025 **88.17%**, TTM (Q3 FY2025–Q2 FY2026) **105.39%**. **Every year comfortably above 70% — no carve-out needed.** | **PASS — does not fire.** |

No hard disqualifier fires. AAPL's outcome (see 3.3) is decided entirely by the weighted score, not by a disqualifier.

### 3.2 Sub-scores (all six, per the weighted formula)

All figures below use **trailing-twelve-months (TTM)** ending 2026-03-28 (the most recent quarter with a filed 10-Q), reconstructed as the sum of the four most recent disclosed quarters (Q3 FY2025 $28,202M... shown per line item below), cross-checked against each FY2025 annual 10-K figure. All dollar figures in millions unless noted.

**TTM reconciliation (shown once, reused across sub-scores):**

| Line item | Q3 FY2025 (2025-06-28) | Q4 FY2025 (derived: FY2025 annual − 9mo FY2025) | Q1 FY2026 (2025-12-27) | Q2 FY2026 (2026-03-28) | **TTM total** |
|---|---|---|---|---|---|
| Revenue | 94,036 | 102,466 | 143,756 | 111,184 | **451,442** |
| Net Income | 23,434 | 27,466 | 42,097 | 29,578 | **122,575** |
| Gross Profit | 43,718 | 48,341 | 69,231 | 54,781 | **216,071** |
| Operating Income (EBIT) | 28,202 | 32,427 | 50,852 | 35,885 | **147,366** |
| D&A | 2,830 | 3,127 | 3,214 | 3,439 | **12,610** |
| Pretax income | 28,031 | 32,804 | 51,002 | 35,833 | **147,670** |
| Income tax expense | 4,597 | 5,338 | 8,905 | 6,255 | **25,095** |
| Operating cash flow | 27,867 | 29,728 | 53,925 | 28,702 | **140,222** |
| CapEx | 3,462 | 3,242 | 2,373 | 1,971 | **11,048** |

(Derived quarters = the disclosed FY2025 annual total minus the disclosed 9-month-YTD figure through Q3 FY2025, per each line item — standard TTM reconstruction; every input number itself is a directly-filed SEC XBRL figure, none estimated.)

TTM Free Cash Flow = $140,222M − $11,048M = **$129,174M**. TTM effective tax rate = $25,095M / $147,670M = **17.00%**. TTM EBITDA = $147,366M + $12,610M = **$159,976M**.

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = 122,575/451,442 = **27.15%** → NetMargin_Component = clamp((27.15/30)×100) = **90.51**. ROIC = NOPAT/Invested Capital. NOPAT = TTM EBIT × (1 − effective tax rate) = 147,366 × (1−0.1700) = **$122,314M**. Invested Capital = Total Debt ($84,711M) + Equity ($106,491M, as of 2026-03-28) − liquid assets ($146,595M, same cash+securities figure netted in the Balance Sheet row above, for consistency) = **$44,607M**. ROIC = 122,314/44,607 = **274.2%** → ROIC_Component = clamp((274.2/30)×100) = clamp(913.9) = **100.0** (clamped — flagged: this extreme figure is a real, disclosed feature of Apple's capital structure, not a data error — decades of aggressive buybacks have shrunk book equity to $106.5B against $122B+ of TTM NOPAT, not an inflated numerator). Profitability_Score = (90.51+100.0)/2 = **95.25** (no FCF-positivity cap — every year on record is FCF-positive). | **95.25** |
| **Margins (15%)** | Gross Margin (TTM) = 216,071/451,442 = **47.86%** (cross-checks against Apple's own FY2025-annual-basis disclosed "Total gross margin percentage" of 46.9% in the FY2025 10-K — the small gap is the TTM window including a strong Q1 FY2026 holiday quarter at 48.2% and Q2 FY2026 at 49.3%, both above the FY2025 average). GrossMargin_Score = clamp((47.86/80)×100) = **59.83**. **No +10 structural-trend bonus** — that bonus only applies when gross margin is expanding *while still below the 40% static threshold*; AAPL's margin has been above 40% throughout the lookback window (FY2021 41.78% → FY2025 46.9%, TTM 47.86% — genuinely expanding, but already past the threshold the bonus is designed for). | **59.83** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $394.328B → FY2025 $416.161B, both directly filed annual figures) = (416.161/394.328)^(1/3) − 1 = **+1.81%** → base = clamp((1.81/25)×100) = **7.25**. **Documented TAM-expansion evidence** (independently sourced, not from the trigger post): Apple's own FY2025 10-K discloses **Services net sales growing from $85.200B (FY2023) to $109.158B (FY2025)** — a 2-year CAGR of **+13.2%/yr**, taking Services from 22.2% to 26.2% of total revenue, at a much higher (75.4% FY2025) gross margin than the Products business (36.8% FY2025) — a genuine, company-disclosed structural mix-shift toward a durably higher-margin, faster-growing segment. This is corroborated by the *direction* of consolidated growth itself: FY2023 revenue was **down** 2.8% YoY, FY2024 **up** 2.0%, FY2025 **up** 6.4% — an accelerating, not decelerating, multi-year trend, which is the opposite of what the Growth sub-score's −10 "structural deceleration" modifier requires. **+10 applied** (not −10; not 0 — see flagged judgment call below). Growth_Score = 7.25 + 10 = **17.25**. *Flagged judgment call: this is a mixed picture (hardware — iPhone, Wearables — growing near-zero-to-negative; Services genuinely accelerating) and a reasonable reader could argue for 0 (no modifier) instead of +10. Sensitivity check: even at 0, Growth_Score would be 7.25 and the final Quality Score would be 74.2 — still decisively below the 80.0 gate. The gate outcome does not depend on this call either way.* | **17.25** |
| **Balance Sheet (15%)** | Net Debt/EBITDA (TTM, as of 2026-03-28) = −$61,884M / $159,976M = **−0.39×** (net cash — see 3.1). BalanceSheet_Score = clamp(100×(1−(−0.39)/4)) = clamp(109.7) = **100.0**. | **100.0** |
| **Moat Signal (15%)** | See evidence table below — **5 of 5 signals** cleared the cited-evidence bar. (5/5)×100 | **100.0** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 129,174/122,575 = **105.39%** → clamp(((1.0539−0.40)/0.60)×100) = clamp(108.98) = **100.0**. | **100.0** |

**Moat signal evidence (cited, per signal):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | Apple was the **#1 global smartphone vendor by unit share in calendar 2025** (20% share, +10% YoY shipment growth — the highest among the top 5 brands) per Counterpoint Research/MacRumors (Jan 2026), and **grew again in Q1 2026** (21% share per Counterpoint, 22% per Omdia, +9% YoY) even as the overall market *contracted* 3% (Forbes/PhoneArena, Apr 2026) — genuinely growing share, not merely stable, and gaining against a shrinking market. | **TRUE** |
| Brand premium | Apple held **~71% of the global premium smartphone segment ($600+ price tier)** per Counterpoint Research (2024 data, cited via multiple 2026 secondary sources) — direct evidence of sustained premium-pricing power and premium-tier dominance, though flagged as a segment-share proxy rather than a literal same-SKU "price increase without volume loss" data point. | **TRUE** (flagged as proxy evidence) |
| Network effect | Apple disclosed an **installed base of over 2.5 billion active devices, an all-time high across every major product category**, on its fiscal Q2 2026 earnings call (30 Apr 2026) — a genuine two-sided marketplace dynamic (the App Store ecosystem: developers build for the platform because of its installed-base size; users benefit from the platform because of the resulting app breadth), sourced directly from the company's own investor communication. | **TRUE** |
| Switching costs | Documented integration-depth/migration-cost mechanism: iMessage (~1 billion monthly active users), iCloud data/photo/backup migration friction, and cross-device Continuity/Find My/purchased-content lock-in. A secondary aggregator (TechLila, "The Apple Ecosystem Lock-In Statistics 2026") reports **92% customer retention** and **only ~4% of iPhone users switching to Android annually vs. ~15% the other direction** — flagged as blog/aggregator-level sourcing (not a primary research-firm report), but directionally consistent with the widely-documented ecosystem-lock-in literature and sufficient to support a genuinely documented mechanism (integration depth + migration cost), which is the framework's actual evidentiary bar for this signal. | **TRUE** (flagged: secondary-aggregator statistic, not a top-tier research-firm source) |
| Scale cost advantage | Apple's own FY2025 10-K discloses **Products gross margin of 36.8%** (Item 7 MD&A, "Products and Services Performance" table) — compared against **Xiaomi's smartphone-segment gross margin of ~10.9% in 2025** (down from 12.6% in 2024, per Chinese business press/36kr reporting on Xiaomi's own disclosures) — a real, cited, apples-to-apples *hardware-segment* margin gap of more than 3× in Apple's favor, consistent with (though not solely attributable to) component-purchasing scale advantage; comparable Samsung mobile-division hardware-margin data was not found this session and is not used. | **TRUE** |

### 3.3 Final weighted Quality Score

```
Quality Score = (95.25 × 0.25) + (59.83 × 0.15) + (17.25 × 0.20) + (100.0 × 0.15) + (100.0 × 0.15) + (100.0 × 0.10)
              = 23.8125 + 8.9745 + 3.45 + 15.0 + 15.0 + 10.0
              = 76.237 → 76.2 (rounded to nearest 0.1)
```

**76.2 < 80.0 — fails the gate**, by 3.8 points. This is a **narrower miss** than the HNHPF (35.7) or OUST (44.2) sessions, and is worth stating plainly: this is not a low-quality company by any conventional reading. Four of the six sub-scores are at or near the maximum (Balance Sheet 100.0, Moat 100.0, FCF Quality 100.0, Profitability 95.25). The miss is driven entirely by **Growth (17.25)** and, to a lesser extent, **Margins (59.83)** — both a direct, structural consequence of Apple's scale: a company already generating ~$451B of TTM revenue mechanically cannot post the 25%+ revenue CAGR this framework's Growth sub-score is calibrated to reward (that ceiling suits an early/mid-stage compounder, not a multi-trillion-dollar incumbent), and its Products-heavy revenue mix (73.8% of TTM revenue) caps blended gross margin below the 80% ceiling calibrated for software-like businesses, even though the Products segment margin (36.8%) and Services margin (75.4%) are each strong *for their respective business models*.

**Sensitivity check (per the flagged judgment call in 3.2):** even under the least generous defensible reading of the Growth modifier (0 instead of +10), the Quality Score is 74.2 — still decisively below 80.0. Under the most generous alternate reading of the Moat evidence (all 5 signals held to a stricter bar and only 3 of 5 credited), Quality Score would be 70.2 — still fails. **The Phase 01 FAIL outcome is robust to every discretionary call made in this session.**

### Result: **Phase 01 FAIL**

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0... stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring.

This is not a verdict that Apple is a weak or deteriorating business — the opposite is closer to true on four of the six axes this framework measures (profitability, balance-sheet strength, moat durability, and cash-conversion quality are all at or near the framework's ceiling). It is a verdict that **this framework's specific 80.0+ Quality Score bar, and in particular its Growth sub-score's 25%-CAGR-to-100.0 calibration, is not built to admit an already-hyperscale, ~$451B-revenue incumbent whose consolidated top-line growth is structurally single-digit** — regardless of how dominant its market position or how durable its moat. That is an explicit, known feature of this strict gate (see quality-scoring.md's own worked example, which reaches a structurally similar conclusion for a different reason), not a bug specific to this session. The trigger event itself (a reported AVGO–AAPL chip-supply contract extension through 2031) is a supply-chain data point about a *different* held company (AVGO) and, even if independently confirmed later, would not itself change AAPL's own Quality Score inputs.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance. (Note: AVGO, the company actually named alongside AAPL in the triggering post, remains a held position — last rescored 2026-07-04, Quality Score 82.1 / Composite Score 43.1 — and is unaffected by this AAPL evaluation; no action taken on AVGO in this session.)

---

## 6. Next Review Trigger

- **Mandatory Rule 9 re-check:** Apple's next scheduled disclosure — fiscal Q3 2026 Form 10-Q (period ending ~2026-06-27), expected to be filed early August 2026 (consistent with Apple's historical ~5-week filing lag).
- **Mechanical trigger:** the Growth sub-score is the primary gap to the 80.0 gate (17.25 vs. the ~35+ needed, holding all else constant, to clear it on Growth alone) — a sustained re-acceleration in consolidated revenue growth (e.g. from a genuine AI-driven device upgrade cycle, if one materializes and is company-confirmed rather than inferred) or continued Services mix-shift would be the most direct path to a materially different result next time. A margin re-rating (e.g. from a favorable product mix shift or the tariff-related headwinds referenced in the FY2025 10-K's MD&A resolving) would also help but is a smaller lever than Growth.
- **Other Rule 9 events:** a guidance revision, management change, material M&A, or a >15% stock-price move with no identified cause. Also worth independently verifying (not scored, informational only): whether the AVGO–AAPL contract-extension claim from the triggering post is confirmed by either company's own disclosures — if so, it would be a Rule 9 trigger for AVGO's own next review, not for AAPL's Quality Score inputs.
- Absent any of the above, future Telegram mentions of AAPL should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **10-K (Annual Report)** — The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements, MD&A, and risk factors — the primary source used for AAPL in this session.
- **10-Q (Quarterly Report)** — The quarterly financial-disclosure report filed between annual 10-Ks — used here to reconstruct trailing-twelve-month (TTM) figures through the most recently filed quarter.
- **ASP (Average Selling Price)** — The average price a company sells a unit of its product for — a pricing-power signal used as part of this session's Brand Premium moat-signal evidence.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **CIK (Central Index Key)** — The unique numeric identifier the SEC assigns to every EDGAR filer (Apple's is 0000320193) — used to construct this session's SEC XBRL/filing data-pull paths.
- **D&A** — Depreciation & Amortization — a non-cash expense spreading the cost of long-lived assets over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and profitability ratios.
- **Effective tax rate** — The actual percentage of pretax income paid as tax in a period — used here to convert TTM EBIT into NOPAT for the ROIC calculation.
- **EPS** — Earnings Per Share — net income divided by number of shares outstanding.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score — none fired for AAPL this session.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; a negative figure means net cash, as found for AAPL here.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. AAPL scores 76.2.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies eligible for valuation scoring. (AAPL does not make this list, this session.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the basis used throughout this session's sub-scores.
- **XBRL (eXtensible Business Reporting Language)** — The SEC's structured, machine-readable data-tagging format for filed financial statements — the source of every quantitative figure in this session, pulled via the SEC's `companyfacts`/`companyconcept` APIs.
