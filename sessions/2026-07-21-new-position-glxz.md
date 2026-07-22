# New Position Evaluation — GLXZ (Galaxy Gaming, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-07-21
**10Y US Treasury yield:** ~4.56% (most recent widely-reported level on record in this repo, 2026-07-17 — context only, **not used**: this session stops at the Quality Gate below, before the Rate Environment Gate would apply)
**Trigger:** Telegram post t.me/bolshegold/9805 (~2026-07-21 07:56 UTC) reporting that Galaxy Gaming's merger with Evolution AB missed its July 17, 2026 Outside Date without satisfying/waiving the remaining Nevada/Louisiana regulatory closing conditions, leaving the company "vulnerable." **Per Rule 0, no claim from the Telegram post is used as a financial input anywhere below.** The post's substance is independently confirmed by a real GlobeNewswire press release dated 2026-07-20 (filed as Exhibit 99.1 to an SEC Form 8-K), cited directly in §2 below — the post is only the reason this ticker was looked at.
**Sector:** Consumer Discretionary — Casino/Gaming equipment & technology (proprietary table games, side bets, and iGaming/RMG platform licensing)
**Current GLXZ portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md)); no prior watchlist entry anywhere under `watchlist/` (confirmed via Glob before this session — first-ever evaluation).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched via Interactive Brokers MCP tools before any valuation work.

| Field | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 68293415, exchange **PINK** — "GALAXY GAMING INC") | **$1.57** | Last trade, flagged `is_close: true` — no trade has printed intraday at the time of this check. |
| Prior close | $1.57 | Same snapshot. |
| Bid/ask | Empty (`{}`) — no live two-sided quote available | Confirms thin/no-quote conditions. |
| Volume (today) | 0 | Confirms no trade has occurred yet today. |

**Live price used throughout this session: $1.57.**

**Liquidity flag:** GLXZ trades on **OTC Pink Sheets** (PINK), not a major exchange. The zero-volume, empty-bid/ask snapshot is not a data-fetch failure — it is a genuine characteristic of this thinly-traded Pink Sheet stock. Any future order-setup work on this name (moot here — see §3) would need to account for wide effective spreads and execution-price uncertainty well beyond what a NYSE/Nasdaq-listed name would carry. This is independent of, and does not affect, the Quality Score gate result below (which fails decisively regardless of price/liquidity).

---

## 2. M&A Event Confirmation (Rule 9) — Independent of the Telegram Trigger

Per this framework's Rule 9 ("Material M&A announcement → Re-score + recalculate debt ratios + moat impact"), the underlying event is confirmed directly from the company's own SEC filing, not from the Telegram post:

- **Source:** Galaxy Gaming, Inc. Form 8-K, Exhibit 99.1, filed with the SEC 2026-07-20 (CIK 0000013156) — press release titled *"Galaxy Gaming Is Evaluating Its Options in Light of the Passing of the July 17, 2026 Merger Outside Date Without Satisfaction or Waiver of the Remaining Regulatory Closing Conditions."*
- **What it says:** The merger agreement between Galaxy Gaming and Evolution Malta Holding Limited (a subsidiary of Evolution AB) passed its **July 17, 2026 Outside Date** without two remaining gaming-regulatory approvals (previously reported as Nevada and Louisiana) having been obtained, and Evolution has not waived those conditions. **Neither party has terminated the agreement.** Galaxy states it is evaluating its options, including seeking a further extension of the Outside Date, or terminating the Merger Agreement.
- **Management quote (Matt Reback, President & CEO):** "For two years, we have been working with Evolution towards a closing of the Merger Agreement... We are excited about the trajectory of the company, and we look forward to a continued relationship with Evolution."
- **No termination fee, breakup fee, or specific next-step timeline was disclosed** in the press release itself.
- **Background:** The Outside Date had already been extended once before (from an earlier date to November 24, 2025's amendment setting July 17, 2026), per the company's Q1 2026 10-Q. This is now the second time the deal has run past a deadline without closing.

**Framework implication:** This is exactly the kind of live, unresolved situation Rule 9 exists to flag — but it does not change *how* this session proceeds. A pending, uncertain M&A outcome is a valuation/scenario question for Phase 02 (relevant only if the Quality Gate is cleared). It has no bearing on the trailing financial-statement inputs the Phase 01 Quality Score is built from. Accordingly, this session runs the standard Quality Score first, as instructed.

---

## 3. Data Sourcing & TTM Roll-Forward

**Sources used (all SEC EDGAR primary filings, CIK 0000013156) — no yfinance/aggregator data used (yfinance blocked via this session's proxy, consistent with prior sessions' documented TLS-fingerprint failures):**

- FY2025 10-K (period end 2025-12-31, filed ~2026-03-27/30): https://www.sec.gov/Archives/edgar/data/13156/000119312526129503/glxz-20251231.htm
- Q1 2026 10-Q (period end 2026-03-31, filed 2026-05-01): https://www.sec.gov/Archives/edgar/data/0000013156/000119312526215114/glxz-20260331.htm
- Q1 2025 10-Q (period end 2025-03-31): https://www.sec.gov/Archives/edgar/data/13156/000095017025068307/glxz-20250331.htm
- FY2023 10-K (period end 2023-12-31): https://www.sec.gov/Archives/edgar/data/13156/000095017024035514/glxz-20231231.htm

**TTM = FY2025 + Q1 2026 − Q1 2025** (standard roll-forward convention used throughout this repo, e.g. the 2026-06-12 HIMS session):

| Line item | FY2025 (10-K) | Q1 2026 (10-Q) | Q1 2025 (10-Q) | **TTM (FY25+Q1'26−Q1'25)** |
|---|---|---|---|---|
| Total Revenue | $30,873,552 | $7,662,561 | $7,784,933 | **$30,751,180** |
| Cost of ancillary products | $780,377 | $67,188 | $188,002 | $659,563 |
| Operating Income | $8,179,610 | $2,173,665 | $1,975,296 | **$8,377,979** |
| Net Income (Loss) | $1,483,619 | $1,367,556 | $(2,021,282) | **$4,872,457** |
| Income tax provision | $144,349 | $30,632 | $36,421 | $138,560 |
| Interest expense | $3,587,921 | $776,489 | $1,003,350 | $3,361,060 |
| D&A | $3,209,679 | $869,951 | $779,817 | $3,299,813 |
| Operating cash flow | $7,697,622 | $2,544,086 | $1,168,692 | **$9,073,016** |
| Investing activities (cash used; capex proxy) | $2,825,540 | $1,030,320 | $283,330 | $3,572,530 |

**Derived TTM figures:**
- Gross Profit TTM = $30,751,180 − $659,563 = **$30,091,617** → Gross Margin TTM = **97.86%**
- Net Margin TTM = $4,872,457 / $30,751,180 = **15.85%**
- Free Cash Flow TTM = OCF − investing-activities proxy = $9,073,016 − $3,572,530 = **$5,500,486**
- FCF/NI conversion TTM = $5,500,486 / $4,872,457 = **112.9%**
- EBITDA TTM (GAAP-derived: Operating Income + D&A, not the company's own non-GAAP "Adjusted EBITDA" which layers in stock-comp/severance/FX add-backs not independently re-derivable on a TTM basis from the quarters available) = $8,377,979 + $3,299,813 = **$11,677,792**

**Balance sheet (most recent quarter-end, 2026-03-31 10-Q):**
- Long-term debt (gross, incl. current portion): $38,908,240 + $2,626,990 = **$41,535,230**
- Cash and cash equivalents: **$4,853,794**
- **Net Debt** = $41,535,230 − $4,853,794 = **$36,681,436**
- **Total Stockholders' Deficit:** **$(16,178,622)** (negative equity)
- Shares outstanding: 25,354,623

**Data gap flagged:** The company's own "Adjusted EBITDA" (FY2025: $13,257,035 per the 10-K) is not used for the Net Debt/EBITDA hard-disqualifier check below, because it can't be precisely re-derived on a TTM basis from the quarterly figures available this session (the specific stock-comp/severance/FX add-back components for Q1 2025 and Q1 2026 individually were not broken out in the filings reviewed). Using the company's non-GAAP figure would understate leverage relative to the GAAP-derived EBITDA used here — a conservative choice consistent with "never invent or estimate," since the GAAP figure is directly computable from filed statements without judgment calls about which add-backs to trust.

---

## 4. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 4.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | GLXZ data | Verdict |
|---|---|---|
| **Net Debt/EBITDA over threshold** (2.5× standard — Galaxy Gaming is a gaming-equipment licensor, not a payment network/exchange, so the Upgrade 5 asset-light 4×/6× override does **not** apply) | Net Debt/EBITDA (TTM) = $36,681,436 / $11,677,792 = **3.14×** | ❌ **FIRES — 3.14× > 2.5× standard threshold** |
| Not FCF-positive for 3+ consecutive years | OCF alone: FY2022 +$6,391,040 / FY2023 +$2,729,477 / FY2024 +$4,098,634 / FY2025 +$7,697,622 — **all positive**. But under the OCF-minus-investing-activities proxy used elsewhere in this session: FY2022 +$2,973,703 / **FY2023 −$226,204** (investing activities used $2,955,681 slightly exceeded OCF) / FY2024 +$2,476,030 / FY2025 +$4,872,082 — **marginally negative in FY2023 only**. | ⚠️ **Ambiguous/borderline** — OCF itself was positive every year 2022–2025; the FY2023 dip under the investing-activities-as-capex proxy is small (~$226K) and "investing activities" isn't a literal disclosed maintenance-capex line, so this is flagged as a data-quality caveat, **not** independently confirmed as a second hard-disqualifier trigger. Immaterial to the outcome regardless (see §4.3). |
| FCF/Net Income conversion <70% for 2+ consecutive years without documented growth-capex explanation | FCF/NI TTM = 112.9% (see §3) — comfortably above 70% | ✅ **PASS — does not fire** |

**One hard disqualifier fires cleanly and unambiguously: Net Debt/EBITDA (3.14×) exceeds the standard 2.5× threshold.** Per quality-scoring.md, this fails the company **regardless of the weighted Quality Score** computed below. The FCF-positivity item is flagged as an open question but is not needed to reach the gate-fail conclusion and does not change it either way.

### 4.2 Sub-scores (all six, computed for completeness per this framework's "show every calculation" rule, despite the hard disqualifier above)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = 15.85% → NetMargin_Component = clamp((15.85/30)×100) = **52.82**. ROIC (TTM): NOPAT = Operating Income TTM × (1 − effective tax rate) = $8,377,979 × (1 − 2.77%) ≈ **$8,146,328** (effective tax rate = TTM tax $138,560 / TTM pretax income $5,011,017 = 2.77% — unusually low, likely reflecting NOL carryforwards; used as computed, not adjusted, per "never invent/estimate"). Invested Capital = Net Debt + Total Equity = $36,681,436 + $(16,178,622) = **$20,502,814**. ROIC = $8,146,328 / $20,502,814 = **39.73%** → ROIC_Component = clamp((39.73/30)×100) = clamp(132.4) = **100.0** (capped). **Caveat: this ROIC reading is distorted by negative stockholders' equity** — the deficit shrinks the Invested Capital denominator well below what a normally-capitalized company of this earnings size would show, inflating the ratio. Not treated as a reliable standalone quality signal; shown for completeness only. Profitability_Score = (52.82 + 100.0)/2 = **76.41** (no FCF-positivity cap applied — see §4.1 ambiguity note; OCF itself was positive all 4 years shown). | **76.41** |
| **Margins (15%)** | Gross Margin (TTM) = 97.86% (license-revenue-heavy model; minimal cost of ancillary products) → GrossMargin_Score = clamp((97.86/80)×100) = clamp(122.3) = **100.0** (capped). 2-year trend: FY2024 95.2% → FY2025 97.5%/TTM 97.86% — mildly expanding, but score is already at the 100.0 cap so no bonus is needed. | **100.0** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $23,442,306 → FY2025 $30,873,552) = (30,873,552/23,442,306)^(1/3) − 1 = **9.62%** → base = clamp((9.62/25)×100) = **38.47**. **Documented structural-deceleration evidence** (FY2025 10-K MD&A, cited directly, independent of the Telegram post): total FY2025 revenue **declined** 2.7% YoY ($30.87M vs $31.74M), driven by **core (land-based) revenue falling 10.4% YoY, which the company attributes to casino closures in North America** — a permanent-footprint-reduction cause, not a cyclical one. Digital/iGaming revenue grew (+13.2% YoY) partially offsetting this, but total company revenue still declined YoY on a GAAP basis. Given the company's own filing attributes the larger, higher-margin segment's decline to a structural (not cyclical) cause, the **−10 modifier is applied** rather than a TAM-expansion +10 (no quantified market-share or TAM-expansion figure was found to support the alternative). Growth_Score = clamp(38.47 − 10) = **28.47**. | **28.47** |
| **Balance Sheet (15%)** | Net Debt/EBITDA (TTM) = 3.14× (see §4.1) → BalanceSheet_Score = clamp(100×(1 − 3.14/4)) = clamp(21.5) = **21.46** | **21.46** |
| **Moat Signal (15%)** | See evidence table below — **0 of 5 signals** cleared the cited-evidence bar. (0/5)×100 | **0.0** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 112.9% → clamp(((1.129−0.40)/0.60)×100) = clamp(121.5) = **100.0** (capped) | **100.0** |

**Moat signal evidence (cited directly from the FY2025 10-K "Business"/"Risk Factors" sections):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | 10-K discloses **no numeric market share figure** at all — only that Galaxy competes with several larger companies (Light & Wonder, IGT, Play AGS, TCS/John Huxley, Aces Up Gaming, Genesis Gaming Solutions, Masque Publishing) | **FALSE** — no cited share data |
| Brand premium | No pricing-power/price-increase-without-volume-loss evidence found in the filing | **FALSE** |
| Network effect | Table-game/side-bet licensing to casinos is not a two-sided marketplace/user-growth-driven model | **FALSE** |
| Switching costs | 10-K **explicitly undercuts** this signal: "a majority of our clients contract with us... on a month-to-month or annual basis with typically a 30–45 day termination notice requirement" — short, low-friction termination windows are evidence *against* durable lock-in, not for it | **FALSE** |
| Scale cost advantage | No cost-per-unit data vs. smaller competitors disclosed; company instead states most competitors "are larger than we are, have more financial resources than we do" — i.e. Galaxy is the *smaller* party in its competitive set | **FALSE** |

**Result: 0/5 — Moat_Score = 0.0.** This is not a case of missing data; the filing itself contains language that actively contradicts several of the signals (weak switching costs, smaller-than-competitors scale).

### 4.3 Final weighted Quality Score

```
Quality Score = (76.41 × 0.25) + (100.0 × 0.15) + (28.47 × 0.20) + (21.46 × 0.15) + (0.0 × 0.15) + (100.0 × 0.10)
              = 19.10 + 15.00 + 5.69 + 3.22 + 0.00 + 10.00
              = 53.01 → 53.0 (rounded to nearest 0.1)
```

**53.0 < 80.0 — fails the gate**, and it is independently confirmed to fail by the hard disqualifier in §4.1 (Net Debt/EBITDA 3.14× > 2.5×). Both routes to failure are decisive and would not be reversed by any single judgment call in this session (the distorted-ROIC caveat, the Growth modifier direction, or the FCF-positivity ambiguity) — none of those, resolved the other way, would move the weighted score anywhere near 80.0, nor would they cure the balance-sheet hard disqualifier.

### Result: **Phase 01 FAIL** (weighted score **and** hard disqualifier)

Galaxy Gaming has some genuinely strong quality characteristics for its size — a 97.9% TTM gross margin (a high-margin IP-licensing revenue model), FCF comfortably exceeding net income (112.9% conversion), and a currently-profitable P&L (TTM net margin 15.85%). But it carries **negative stockholders' equity** ($(16.2)M as of 2026-03-31) built on a debt load ($41.5M total debt) that is **large relative to its TTM cash-operating-profit** (3.14× Net Debt/EBITDA, above this framework's 2.5× standard threshold), a modest and recently-declining top line (9.6% 3yr CAGR, with the FY2025 core segment specifically citing a structural North American casino-closure headwind), and **no independently-citable moat signal** — the 10-K's own language on client termination notice periods and relative competitive scale works against, not for, a moat case. This is exactly the profile (small, thinly-traded, debt-heavy, no clear durable advantage) the strict 80.0+ Quality Gate and its hard disqualifiers exist to screen out, independent of any near-term M&A catalyst.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0, or a hard disqualifier fires, stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 5. Recommendation

**PASS.** Do not open a position, and do not place a limit order. Galaxy Gaming fails Phase 01 both by weighted Quality Score (53.0, well short of the 80.0 gate) and by an independently-confirmed hard disqualifier (Net Debt/EBITDA 3.14× > 2.5×).

This is not a verdict on how the pending Evolution AB merger situation will resolve (extension, termination, or eventual close) — that is a live, genuinely uncertain corporate-action question this session deliberately does not speculate on, consistent with "never invent or estimate financial data" and with not acting on an unresolved event alone. It is a verdict that, independent of the merger outcome, Galaxy Gaming's standalone trailing financials (leverage, negative equity, thin growth, no cited moat) do not clear this framework's bar for a "high quality" business eligible for valuation scoring at all.

**Add GLXZ to the watchlist** (`not-in-portfolio/GLXZ/`) as "Phase 01 FAIL / not scored," with re-evaluation triggered by:
- **Resolution of the merger situation** (extension announced, termination announced, or deal closes) — a Rule 9 M&A event regardless of outcome.
- **Q2 2026 earnings** (next scheduled quarterly filing) — refresh the TTM roll-forward and re-check the Net Debt/EBITDA hard disqualifier in particular, since a debt paydown or refinancing could plausibly move it.
- Any **management change** or **guidance revision**.

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 7. Next Review Trigger

- **Primary trigger:** Any news resolving the Evolution AB merger's status (extension, termination, or closing) — Rule 9 material M&A event, re-score regardless of outcome.
- **Routine trigger:** Galaxy Gaming's next quarterly SEC filing (Q2 2026 10-Q, expected ~August 2026) — refresh TTM figures and re-check the Net Debt/EBITDA hard disqualifier.
- Per [watchlist/README.md](../watchlist/README.md), a "Phase 01 FAIL / not scored" entry carries no numeric Phase 02 score and so does not go stale on a future valuation-scoring methodology-version bump.
- Absent the above, future Telegram mentions of GLXZ should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets.
- **D&A** — Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation & Amortization — a rough proxy for cash operating profit, used in the Net Debt/EBITDA leverage ratio.
- **Effective tax rate** — The actual percentage of a company's pretax income paid as income tax in a given period (tax provision ÷ pretax income) — distinct from the statutory rate, and can read unusually low (as here, ~2.8% TTM) when NOL carryforwards or other tax attributes are in play.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; a ratio below 70% for 2+ consecutive years is this framework's FCF Quality hard disqualifier (does not fire here — GLXZ's TTM ratio is 112.9%).
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. One of this framework's Quality Score Margins sub-score inputs.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score — see [quality-scoring.md](../framework/quality-scoring.md). GLXZ fails on the Net Debt/EBITDA condition.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. GLXZ's TTM figure (3.14×) exceeds the standard 2.5× threshold.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **NI (Net Income)** — Accounting profit after all expenses, interest, and taxes ("the bottom line").
- **Outside Date** — The contractual deadline in a merger/acquisition agreement by which the deal must close, or either party gains the right to walk away — see [glossary.md](../framework/glossary.md) for the full entry and this session's specific facts.
- **OTC Pink Sheets (OTC Markets, Pink tier)** — The lowest, most lightly-regulated quotation tier of the over-the-counter market — see [glossary.md](../framework/glossary.md) for the full entry. GLXZ trades on this tier.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. GLXZ scores 53.0.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (GLXZ does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework, though flagged here as distorted by GLXZ's negative equity.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work — never infer or invent it.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Stockholders' Deficit** — When a company's Total Liabilities exceed its Total Assets, its Total Stockholders' Equity line goes negative and is relabeled a "Deficit" — see [glossary.md](../framework/glossary.md) for the full entry and this session's specific facts (GLXZ: $(16,178,622) at Q1 2026).
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
