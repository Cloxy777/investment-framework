# New Position Evaluation — EFX (Equifax Inc.)

**Task type:** NEW POSITION
**Date:** 2026-07-21
**10Y US Treasury yield:** ~4.56–4.57% (most recent widely-reported level on record in this repo, 2026-07-17/20 — context only, **not used**: this session stops at the Quality Gate below, before the Rate Environment Gate would apply)
**Trigger:** Telegram post t.me/bolshegold/9807 (~2026-07-21 13:12 UTC) describing Equifax Q2 2026 earnings — a GAAP EPS "miss" vs. a claimed $1.84 consensus, in-line revenue, and mixed guidance revisions. **Per Rule 0, no claim from the Telegram post is used as a financial input anywhere below** — every figure in this session is independently re-pulled from Equifax's own primary sources (SEC/press release) and third-party data (stockanalysis.com), and several of the post's specific claims turn out not to match those primary sources (see §2). No watchlist entry existed anywhere for EFX (checked `watchlist/in-portfolio/EFX/` and `watchlist/not-in-portfolio/EFX/` — neither exists) and EFX is not a current holding (checked [holdings.md](../portfolio/holdings.md)) — so this is a first-ever evaluation triggered by telegram-scan step 4's first bullet ("no watchlist entry exists at all"), independent of the post's substance.
**Sector:** Industrials / Business Services — Consumer & commercial credit reporting, data & analytics, workforce/income verification ("The Work Number")
**Current EFX portfolio weight:** 0% — not currently held; no prior watchlist entry anywhere under `watchlist/` (confirmed via directory listing before this session — first-ever evaluation).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched via Interactive Brokers MCP tools before any valuation work.

| Field | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 6735, exchange **NYSE** — "EQUIFAX INC", confirmed via `search_contracts` against the Enerflex Ltd. "EFX" (TSE) and "EFXT" (NYSE) ticker collisions) | **$166.98** | Last trade, not a close flag — live intraday print. |
| Change (today) | **−$13.10 (−7.27%)** | Same snapshot — a genuine, large intraday decline, independent of the Telegram post's framing. |
| Bid/ask | $166.80 / $167.00 | Tight, liquid two-sided quote — NYSE large-cap, no liquidity flag. |
| 52-week range | $151.20 – $269.68 | From `misc_statistics` — today's price sits near the bottom of the 52-week range. |

**Live price used throughout this session: $166.98.**

---

## 2. Rule 9 Earnings Event — Independently Verified, Corrects Several Telegram-Post Claims

Per this framework's Rule 9 (quarterly earnings → re-score), the underlying event is confirmed directly from Equifax's own Q2 2026 press release (PR Newswire, 2026-07-21), **not** from the Telegram post:

| Metric | Telegram post claimed | **Independently verified (PR Newswire / company release)** |
|---|---|---|
| GAAP EPS | $1.54 vs. "expected $1.84" (a miss) | **$1.54**, up **+1% YoY** from $1.53 in Q2 2025 — the post's own $1.54 figure checks out, but the "$1.84 expected" comparator does not appear in the primary source; the only comparable consensus figure found (WebSearch, Yahoo/StockStory coverage) is **adjusted (non-GAAP) EPS of $2.25 vs. a $2.22 consensus — a beat**, not a miss. |
| Revenue | $1.7B, "matched forecasts," +10.4% YoY | **$1.700B**, **+11% YoY reported / +10% local-currency** — figure itself checks out; growth rate is slightly different (+11%, not +10.4%) but directionally the same. |
| FY2026 revenue guidance | "Slightly reduced to $6.76B from $6.685–$6.805B" | **Raised** to **$6.710B–$6.780B** (10.5–11.6% reported growth) — this is a **narrower, higher-anchored range than the post's claimed prior guidance**, and is a guidance **increase**, not a cut. The post's characterization is inverted relative to the primary source. |
| FY2026 adjusted EPS guidance | "Raised to $8.60 from $8.34–$8.74" | **$8.39–$8.69** per share — close to, but not exactly matching, the post's figures. |

**This is precisely why Rule 0/Rule 9 forbid using a Telegram post's text as financial data**: two of the post's four specific claims (the "$1.84 miss" framing and the "guidance cut") do not hold up against the primary source, which shows an adjusted-EPS beat and a guidance **increase**. All figures used in the scoring below come from the verified primary sources, not the post.

**Other Rule-9-relevant items confirmed from the same release (context only, not scored inputs):**
- Equifax signed a definitive agreement to acquire **Círculo de Crédito** (Mexico's fastest-growing credit bureau), enterprise value **$750M**, expected to close Q4 2026 — a geographic-TAM-expansion M&A event, cited as Growth-modifier evidence below (§3.2).
- Equifax is **doubling** its 2026–2028 AI-driven cost-reduction target to **$150M** (from $75M).
- $366M returned to shareholders in the quarter ($300M buybacks + $66M dividends).
- The **−7.27% same-day price decline** (§1) is a real market reaction despite the adjusted-EPS beat and raised guidance — plausibly driven by margin/multiple concerns or leverage optics around the debt-funded Círculo de Crédito deal, but this session does not need to fully explain the move; it is captured correctly via Rule 0's live price rather than any invented causal narrative.

---

## 3. Data Sourcing & Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

**Sources used:** stockanalysis.com (TTM + FY2021–FY2025 income statement, balance sheet, cash-flow statement, ratios pages) and Equifax's own Q2 2026 press release (PR Newswire, 2026-07-21) and WebSearch-aggregated coverage (StockStory, GuruFocus, Yahoo Finance) for the Q2 print, guidance, and moat-evidence items. yfinance was attempted first and failed with a TLS/connection error through this session's network path (consistent with prior sessions' documented yfinance-blocked note) — stockanalysis.com used as the fallback aggregator, per the same convention as recent sessions.

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | EFX data | Verdict |
|---|---|---|
| **Net Debt/EBITDA over threshold** (2.5× standard) | Net Debt (TTM, Jun '26) = Total Debt $5,467M − Cash $170.1M = **$5,297M**. EBITDA (TTM) = **$1,898M**. Net Debt/EBITDA = 5297/1898 = **2.79×**. **Asset-light override (Upgrade 5) checked and does not apply**: Equifax is a data/analytics business, not a payment network or exchange, and fails the override's own eligibility test on interest coverage alone — EBIT (TTM) $1,150M ÷ Interest Expense (TTM) $221.8M = **5.19× interest coverage**, far short of the >15× the override requires — so the standard 2.5× threshold is the correct one to apply, not the 4×/6× asset-light variant. | ❌ **FIRES — 2.79× > 2.5× standard threshold** |
| Not FCF-positive for 3+ consecutive years | FCF: FY2022 +$132.6M / FY2023 +$515.5M / FY2024 +$813M / FY2025 +$1,134M / TTM +$1,105M — **positive every year shown, 5 for 5** | ✅ **PASS — does not fire** |
| FCF/Net Income conversion <70% for 2+ consecutive years without documented growth-capex explanation | FY2022: $132.6M/$700.2M = 18.9% (fires alone) / FY2023: $515.5M/$551.7M = 93.5% / FY2024: $813M/$607.3M = 133.8% / FY2025: $1,134M/$664.3M = 170.7% / TTM: $1,105M/$696.3M = 158.7% — only **one** year (FY2022) fell below 70%, not 2+ consecutive | ✅ **PASS — does not fire** (single-year dip, not consecutive) |

**One hard disqualifier fires cleanly: Net Debt/EBITDA (2.79×) exceeds the standard 2.5× threshold**, and the asset-light override was explicitly checked and ruled out on its own interest-coverage criterion (5.19× vs. the required >15×) — not just assumed inapplicable. Per quality-scoring.md, this fails the company **regardless of the weighted Quality Score** computed below.

### 3.2 Sub-scores (all six, computed for completeness per this framework's "show every calculation" rule, despite the hard disqualifier above)

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | Net Margin (TTM) = $691.4M/$6,445M = **10.80%** → NetMargin_Component = clamp((10.80/30)×100) = **36.0**. ROIC (TTM, per stockanalysis.com ratios page) = **8.68%** → ROIC_Component = clamp((8.68/30)×100) = **28.93**. Profitability_Score = (36.0 + 28.93)/2 = **32.47** (no FCF-positivity cap — 5/5 years positive, §3.1). | **32.47** |
| **Margins (15%)** | Gross Margin (TTM) = **55.54%** → GrossMargin_Score = clamp((55.54/80)×100) = **69.43**. 3yr trend: FY2023 55.65% → FY2024 55.67% → FY2025 56.45% → TTM 55.54% — essentially flat (TTM dip is a Q2-specific wobble, not a structural trend either direction) — **no +10 bonus applied.** | **69.43** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $5,122M → FY2025 $6,075M) = (6075/5122)^(1/3) − 1 = **5.85%** → base = clamp((5.85/25)×100) = **23.42**. **Documented TAM-expansion evidence** (cited directly from the Q2 2026 PR Newswire release, independent of the Telegram post): the signed, definitive agreement to acquire Círculo de Crédito (Mexico's fastest-growing credit bureau, $750M enterprise value, closing Q4 2026) is company-disclosed geographic market expansion. Separately, CFPB commentary (cited via WebSearch, credit-bureau-industry coverage) that credit-report prices have risen roughly fourfold industry-wide since 2022 is independent third-party evidence of pricing power. No documented structural deceleration was found — YoY revenue growth has if anything **accelerated** (FY22→23 +2.8%, FY23→24 +7.9%, FY24→25 +6.9%, Q2 2026 +11%). **+10 modifier applied** or TAM expansion/pricing power. Growth_Score = clamp(23.42 + 10) = **33.42**. | **33.42** |
| **Balance Sheet (15%)** | Net Debt/EBITDA (TTM) = 2.79× (see §3.1) → BalanceSheet_Score = clamp(100×(1 − 2.79/4)) = **30.23** | **30.23** |
| **Moat Signal (15%)** | See evidence table below — **3 of 5 signals** cleared the cited-evidence bar. (3/5)×100 | **60.0** |
| **FCF Quality (10%)** | FCF/NI (TTM) = 158.7% → clamp(((1.587−0.40)/0.60)×100) = clamp(197.8) = **100.0** (capped) | **100.0** |

**Moat signal evidence (cited from the Q2 2026 PR Newswire release, WebSearch-aggregated third-party industry coverage, and Mordor Intelligence's US Credit Agency Market report):**

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable/growing | Equifax's own reported Q2 2026 revenue growth (+11% reported / +10% local currency) clearly outpaces the broader US Credit Agency Market's cited 5.82% CAGR (Mordor Intelligence) — i.e. Equifax is growing faster than its addressable market, consistent with stable-or-growing share within the "big 3" (Experian/Equifax/TransUnion, ~50–60% combined concentration per third-party market research) | **TRUE** — cited third-party market-size data + company's own reported growth rate |
| Brand premium (pricing power) | CFPB Director publicly characterized the credit-bureau sector as a "credit bureau cartel," citing that credit-report prices have risen **roughly fourfold since 2022** — a regulator-cited pricing-power finding, independent of any framing in the triggering post | **TRUE** — cited third-party (regulatory) source |
| Network effect | No documented two-sided-marketplace/user-growth-driven mechanism found this session (data-aggregation scale is captured separately under Switching Costs / Scale below, not treated as a network effect absent a specific cited mechanism) | **FALSE** — not independently cited |
| Switching costs | Q2 2026 release attributes Workforce Solutions segment growth specifically to "expanded data integrations with HR software companies" and rising active records/verification hit rates — deep embedding into employer payroll/HR workflows is a documented integration-depth lock-in mechanism | **TRUE** — cited from company's own release |
| Scale cost advantage | No cost-per-unit data disclosed vs. smaller competitors this session; "scale proprietary data is the foundation of its AI data moat" (analyst commentary, WebSearch) is directionally supportive but not the specific cost-per-unit comparison the criterion calls for | **FALSE** — evidence found does not meet the specific cited-cost-per-unit bar |

**Result: 3/5 — Moat_Score = 60.0.**

### 3.3 Final weighted Quality Score

```
Quality Score = (32.47 × 0.25) + (69.43 × 0.15) + (33.42 × 0.20) + (30.23 × 0.15) + (60.0 × 0.15) + (100.0 × 0.10)
              = 8.12 + 10.41 + 6.68 + 4.53 + 9.00 + 10.00
              = 48.74 → 48.7 (rounded to nearest 0.1)
```

**48.7 < 80.0 — fails the gate**, and it is independently confirmed to fail by the hard disqualifier in §3.1 (Net Debt/EBITDA 2.79× > 2.5×, with the asset-light override explicitly checked and ruled out). Both routes to failure are decisive — no single judgment call in this session (the Growth modifier direction, the Moat signal count, or the flat-vs-slightly-declining Margins trend) would move the weighted score anywhere near 80.0, nor cure the balance-sheet hard disqualifier.

### Result: **Phase 01 FAIL** (weighted score **and** hard disqualifier)

Equifax is a genuinely profitable, cash-generative business (TTM FCF/NI conversion 158.7%, FCF-positive every year shown, modest but real moat evidence via a documented HR-integration lock-in and CFPB-cited pricing power) growing faster than its addressable market. But it carries **leverage above this framework's standard threshold** (2.79× Net Debt/EBITDA, and about to add more debt-funded M&A via the Círculo de Crédito deal), **thin profitability relative to the 30% scoring ceiling** (10.80% net margin, 8.68% ROIC), and **modest top-line growth** (5.85% 3yr CAGR before the TAM modifier) — a profile this framework's strict 80.0+ Quality Gate is designed to screen out regardless of how the stock's price reacts to any single quarter.

Per [new-position.md](../.claude/commands/new-position.md) step 2: *"If it's below 80.0, or a hard disqualifier fires, stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. Equifax fails Phase 01 both by weighted Quality Score (48.7, well short of the 80.0 gate) and by an independently-confirmed hard disqualifier (Net Debt/EBITDA 2.79× > 2.5×, asset-light override explicitly checked and ruled out on interest coverage).

This is not a verdict on today's outsized (-7.27%) price move, nor on whether the Círculo de Crédito acquisition will prove value-accretive — those are live, unresolved questions this session does not speculate on. It is a verdict that, independent of today's earnings reaction, Equifax's standalone trailing financials (leverage above threshold, thin margins/ROIC relative to this framework's scoring ceiling, modest organic growth) do not clear this framework's bar for a "high quality" business eligible for valuation scoring at all.

**Add EFX to the watchlist** (`not-in-portfolio/EFX/`) as "Phase 01 FAIL / not scored," with re-evaluation triggered by:
- **Q3 2026 earnings** (next scheduled quarterly filing) — refresh TTM figures, re-check the Net Debt/EBITDA hard disqualifier in particular (worth watching given the pending debt-funded Círculo de Crédito close).
- **Close of the Círculo de Crédito acquisition** (expected Q4 2026) — a Rule 9 M&A event; re-score leverage and moat/TAM evidence at that point.
- Any **guidance revision**, **management change**, or **>15% unexplained price move** from $166.98.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Primary trigger:** Close of the Círculo de Crédito acquisition (expected Q4 2026) — Rule 9 material M&A event, re-score regardless of outcome.
- **Routine trigger:** Equifax's Q3 2026 earnings (next scheduled quarterly filing) — refresh TTM figures and re-check the Net Debt/EBITDA hard disqualifier, given the pending debt-funded acquisition.
- Per [watchlist/README.md](../watchlist/README.md), a "Phase 01 FAIL / not scored" entry carries no numeric Phase 02 score and so does not go stale on a future valuation-scoring methodology-version bump.
- Absent the above, future Telegram mentions of EFX should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CFPB (Consumer Financial Protection Bureau)** — The US federal agency that regulates consumer financial products and services, including credit reporting; cited here for its public characterization of credit-bureau pricing behavior.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation & Amortization — a rough proxy for cash operating profit, used in the Net Debt/EBITDA leverage ratio.
- **EPS** — Earnings Per Share — net income divided by number of shares outstanding. This session distinguishes GAAP EPS ($1.54) from Adjusted (non-GAAP) EPS ($2.25) — the latter strips out items management doesn't consider part of core operating performance.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; a ratio below 70% for 2+ consecutive years is this framework's FCF Quality hard disqualifier (does not fire here — only one non-consecutive year, FY2022, fell below 70%).
- **GAAP** — Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements.
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. One of this framework's Quality Score Margins sub-score inputs.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score — see [quality-scoring.md](../framework/quality-scoring.md). EFX fails on the Net Debt/EBITDA condition.
- **Interest coverage (ratio)** — EBIT ÷ interest expense — how many times over a company could pay its interest bill from operating profit; EFX's 5.19× TTM figure is far short of the >15× this framework's asset-light override requires.
- **Investment grade** — A credit rating (BBB-/Baa3 or higher) signaling a low perceived risk of default; not independently confirmed this session, moot since the interest-coverage test alone already rules out the asset-light override.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. EFX's TTM figure (2.79×) exceeds the standard 2.5× threshold.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **Phase 01–06** — The six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. EFX scores 48.7.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (EFX does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price (and primary financial data) before any valuation work — never infer or invent it.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
