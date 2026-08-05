# New Position Evaluation — CRCL (Circle Internet Group, Inc.) — Re-evaluation

**Task type:** NEW POSITION (re-run, Rule 9 trigger)
**Date:** 2026-08-05
**10Y US Treasury yield:** 4.61% (per today's earlier [2026-08-05 BKNG session](2026-08-05-new-position-bkng.md), WebSearch cross-check of multiple sources) — recorded for header completeness only; **not used this session**, since the Quality Score gate fails before Phase 02/the Rate Environment Gate would ever be invoked (see below).
**Trigger:** Telegram mention ([bolshegold](https://t.me/bolshegold), post 9907, ~10:31 UTC 2026-08-05): Circle reported Q2 FY2026 earnings — GAAP EPS beat, revenue miss vs. estimate, USDC circulation/transaction-volume growth headlines, raised non-interest-income/margin guidance. **None of this post text is used as a financial input below** — it only identified that CRCL had reported earnings; every figure below was independently fetched from Circle's own SEC filing. CRCL has a prior watchlist entry ([watchlist/not-in-portfolio/CRCL/CRCL-2026-06-30.md](../watchlist/not-in-portfolio/CRCL/CRCL-2026-06-30.md)): **2026-06-30 Quality Score 69.0 — failed the 80.0+ gate.** That entry's "Next review trigger" section lists "(c) a quarterly earnings report or guidance revision" as a condition warranting a fresh full re-evaluation — today's Q2 2026 earnings release is exactly that trigger (Rule 9), so this is a full Phase 01 re-run, not a "last checked" note. CRCL is **not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)).

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 789044667, NYSE — "CIRCLE INTERNET GROUP INC", confirmed via `search_contracts` against the same contract_id used in the 2026-06-30 session) | **$62.37** | last trade |
| Day change | **−1.39% (−$0.88)** on the day, prior-close basis | ordinary intraday move, not a Rule 9 unexplained-move trigger on its own (the earnings release itself is the trigger) |
| 52-week range (IBKR `misc_statistics`) | low **$49.90** / high **$189.92** | live price sits well off the 52-week high; the earlier 13-/26-week high readings ($140.00) confirm the $189.92 high occurred more than 26 weeks ago |

**Live price used throughout this session: $62.37.**

---

## 2. Data Source — Circle's own 8-K / Q2 2026 earnings release (SEC EDGAR primary source)

`yfinance` remains structurally blocked in this environment (`curl: (35) Recv failure: Connection reset by peer` on every call — same failure mode as every prior session). All fundamental data below is sourced directly from Circle's own SEC filings (CIK 0001876042):

- **Form 8-K filed 2026-08-05** (accession 0001876042-26-000246), Item 2.02, Exhibit 99.1 — "Circle Reports Second Quarter 2026 Results" press release, containing the unaudited condensed consolidated balance sheet (June 30, 2026 vs. December 31, 2025), unaudited condensed consolidated statements of operations (three and six months ended June 30, 2026 and 2025), a 5-quarter "Quarterly Results of Operations" table, and the Adjusted EBITDA / Adjusted Operating Expenses non-GAAP reconciliation tables (also 5 quarters).
- **Form 10-K, FY ended December 31, 2025** (filed 2026-03-09) — the same audited annual filing used in the 2026-06-30 session, still the most recent **audited** annual financials (a Q2 2026 10-Q has not yet been filed — checked via SEC EDGAR's 10-Q filing history; the most recent 10-Q on file is still Q1 FY2026, filed 2026-05-11).
- **SEC EDGAR XBRL companyconcept API** (`data.sec.gov/api/xbrl/companyconcept/CIK0001876042/us-gaap/...`) — used to pull exact, audited FY2025 `OperatingIncomeLoss`, `IncomeTaxExpenseBenefit`, and `IncomeLossFromContinuingOperationsBeforeIncomeTaxes...` values for the trailing-twelve-month (TTM) reconstruction below.

**Data-gap note (not a blocking gap):** the Q2 2026 8-K press release does **not** include a cash-flow statement (no Operating Cash Flow, Capex, or Free Cash Flow line anywhere in the filing — confirmed by full-text search of the release), and no Q2 2026 10-Q has been filed yet. This means **no TTM/quarterly FCF figure is available this session.** However, per [quality-scoring.md](../framework/quality-scoring.md)'s own "Quantitative Inputs Needed" list, the FCF-related inputs are explicitly **annual-cadence** checks ("FCF/Net Income ratio, **2+ years**"; "FCF positive/negative, **3+ years**") — both are already fully satisfied by the audited FY2023/FY2024/FY2025 data already on file from the 2026-06-30 session (unchanged, since no new complete fiscal year has closed). **This is not a genuinely missing required input** — it's simply that finer (quarterly/TTM) FCF granularity isn't yet available, which the framework's own formulas don't call for. Proceeding on this basis, consistent with CLAUDE.md step 8 ("genuinely missing/unavailable," not "hard to find").

---

## 3. What's new vs. the 2026-06-30 session — TTM reconstruction now avoids the IPO-charge quarter entirely

The 2026-06-30 session had to **normalize** FY2025 Net Income/Operating Income by adding back a company-disclosed **$424M** one-time stock-compensation charge (RSU vesting conditions satisfied by Circle's June 2025 IPO), because that charge sat inside the FY2025 annual figures being scored.

With Q2 2026 now reported, a trailing-twelve-month (TTM) window of **Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026** is now reconstructable — and this window **entirely excludes Q2 2025** (the IPO quarter carrying the $424M charge). This TTM figure needs **no normalization at all** — it is a genuinely clean, as-reported figure. This session uses it as the primary Profitability/Margins basis instead of the FY2025 normalized estimate.

**TTM reconstruction (all inputs are disclosed, real figures combined by simple arithmetic — not invented):**

```
TTM Revenue = Q3'25 $740M + Q4'25 $770M + Q1'26 $694M + Q2'26 $701M = $2,905M
  (from the 8-K's own "Quarterly Results of Operations" table)

TTM RLDC (Revenue Less Distribution Costs, Circle's own gross-profit proxy)
  = Q3'25 $292M + Q4'25 $309M + Q1'26 $287M + Q2'26 $289M = $1,177M
  RLDC Margin = 1,177 / 2,905 = 40.52%

TTM Operating Income (EBIT):
  FY2025 GAAP Operating Income (loss) = −$96,435K (10-K, audited, XBRL-confirmed)
  H1 2025 Operating Income (loss)     = −$232,642K (8-K's H1 comparative column)
  → H2 2025 (Q3+Q4 2025) Operating Income = −96,435 − (−232,642) = +$136,207K
  H1 2026 Operating Income = $79,361K (8-K, six months ended June 30, 2026)
  → TTM EBIT = 136,207 + 79,361 = $215,568K ≈ $215.57M

TTM Net Income (continuing ops, from the 8-K's Adjusted-EBITDA-reconciliation table, which
  discloses "Net income (loss) from continuing operations" per quarter):
  Q3'25 $214,385K + Q4'25 $133,406K + Q1'26 $55,246K + Q2'26 $48,214K = $451,251K ≈ $451.25M
  TTM Net Margin (GAAP) = 451.25 / 2,905 = 15.53%

FY2025 effective tax rate (10-K, audited, XBRL):
  Income tax benefit −$33,375K ÷ Pretax loss −$102,893K = 32.44%
  (used to tax-effect TTM EBIT into NOPAT, since no Q2 2026 tax-footnote detail exists yet)

TTM NOPAT = 215.568 × (1 − 0.3244) = $145.65M

Invested Capital (June 30, 2026 balance sheet):
  Total debt $0 (convertible debt fully repaid — confirmed $0 again, was already $0 at Q1 2026)
  + Total stockholders' equity $3,509,975K
  − Cash and cash equivalents $1,730,126K (same balance-sheet line used in the 06-30 session;
    excludes cash segregated for corporate-held stablecoins and for stablecoin holders)
  = $1,779,849K ≈ $1,779.85M

TTM ROIC = NOPAT / Invested Capital = 145.65 / 1,779.85 = 8.18%
```

**Finding worth flagging:** this clean TTM reconstruction shows **lower** underlying profitability (ROIC 8.18%, ~$215.6M TTM EBIT) than the 06-30 session's FY2025-normalized estimate implied (ROIC 12.62%, $327.6M "normalized" operating income). The prior session's full $424M addback effectively credited the business with *zero* ongoing stock-based compensation expense; the real run-rate still carries real (much smaller, ~$54M/quarter) recurring SBC expense that a clean TTM window correctly reflects. **This is a more accurate, not a worse, read of the business** — but it does mean CRCL's true profitability is weaker than the prior session's normalization implied.

---

## 4. Phase 01 — Quality Score (Gate)

### Hard disqualifier check (fails regardless of weighted score) — re-verified

| Hard disqualifier | Applies to CRCL? | Basis |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years, no growth-capex carve-out | No | Unchanged from 06-30 session (annual data, no new complete FY): GAAP FCF/NI **51.9% (FY2023) / 209.7% (FY2024, clears 70% by a wide margin, breaking any 2-year streak) / undefined (FY2025, GAAP NI negative due to the one-off IPO SBC charge)**. |
| Net debt/EBITDA over threshold (2.5×/4× asset-light) | No | **Net cash, larger than before.** Convertible debt $0 (confirmed again at June 30, 2026 — was already $0 at Q1 2026). Cash and cash equivalents $1,730.1M (up from $1,526.0M at FY2025 YE). Net debt = **−$1,730.1M** (net cash). |
| Not FCF-positive for 3+ consecutive years | No | Unchanged (annual data): FCF positive all 3 audited fiscal years — $138.9M (FY2023) / $326.4M (FY2024) / $529.7M (FY2025). |

**No hard disqualifier fires.**

### Weighted Quality Score

| Sub-score (weight) | Inputs | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net Margin (TTM, GAAP) 15.53%; ROIC (TTM, NOPAT basis) 8.18% — full derivation in §3 above | NetMargin_Component = clamp((15.53/30)×100) = 51.78. ROIC_Component = clamp((8.18/30)×100) = 27.28. Avg = 39.53. No FCF-cap (FCF-positive all 3 years) | **39.53** |
| **Margins** (15%) | RLDC Margin (Circle's own gross-profit proxy, per §3) — TTM 40.52%; 5-quarter trend from the 8-K's own table: 38% (Q2'25) → 39% (Q3'25) → 40% (Q4'25) → 41% (Q1'26) → 41% (Q2'26) | clamp((40.52/80)×100) = 50.65. **No expansion bonus** — the bonus is explicitly conditioned on margin being *below 40%* while expanding; TTM margin (40.52%) and the last two quarters (41%) are now *above* 40%, so the condition doesn't apply (base score only) | **50.65** |
| **Growth** (20%) | Revenue 3yr(2yr) CAGR — unchanged base, no new complete FY: FY2023 $1,450.5M → FY2025 $2,746.6M = **37.61%**. TAM-expansion evidence *re-verified and strengthened* this quarter: USDC circulation $73.3B (+19% YoY, still growing); GENIUS Act tailwind unchanged; Circle received **OCC approval for a national trust bank charter** (Circle National Trust) and NYDFS approval for Circle New York Trust, expanding its regulated-custody addressable scope; Arc (its L1 blockchain) has 100+ ecosystem/institutional builders ahead of its Sept 16, 2026 mainnet launch, with a validator cohort including BlackRock, DTCC, Mastercard, Visa, Standard Chartered. **Growth-deceleration modifier considered but not applied**: total revenue growth has clearly slowed (TTM YoY run-rate ~+6.5% Q2'26 / +12.8% H1'26, well below the 37.61% multi-year CAGR), but per the framework's rule this modifier requires the deceleration to be **"structural, not cyclical."** Management's own attribution is explicitly cyclical/macro: *"Our quarterly financial results reflect the current rate environment and a crypto market that has slowed — both are conditions outside our network."* Stablecoin market share held roughly flat (27%, −66bps YoY) and USDC circulation/transaction volume both kept growing — not consistent with a structural moat/TAM impairment. | Base = clamp((37.61/25)×100) = clamp(150.4) = 100.0. +10 (cited TAM evidence, re-verified) — already capped | **100.00** |
| **Balance Sheet** (15%) | Net Debt −$1,730.1M (net cash, larger than before); TTM Adjusted EBITDA (company-disclosed, "New Definition," sum of Q3'25 $171.476M + Q4'25 $175.910M + Q1'26 $151.401M + Q2'26 $143.478M) = $642.27M; standard /4 denominator | Net Debt/EBITDA = −1,730.1/642.27 = **−2.69×**. clamp(100×(1−(−2.69)/4)) = clamp(167.3) | **100.00** |
| **Moat** (15%) | Re-verified against Q2 2026 disclosures — see evidence table below; still 2 of 5 signals cleared the cited-evidence bar | (2/5)×100 | **40.00** |
| **FCF Quality** (10%) | No Q2 2026 cash-flow statement available (see §2 data-gap note) — this sub-score's required inputs are explicitly annual-cadence per quality-scoring.md, so unchanged from the 06-30 session's normalized FY2025 basis: FCF/NI = 529.7/354.5 = 149.4% (normalization: same $424M SBC addback to FY2025 Net Income, justified because it's a real, non-cash, one-time distortion of the *denominator* only — FCF itself is unaffected by non-cash SBC) | clamp(((1.494−0.40)/0.60)×100) = clamp(182.4) | **100.00** |

**Moat signal evidence (re-verified against Q2 2026 disclosures — no signal changed status):**

| Signal | Evidence this session | Verdict |
|---|---|---|
| Market share stable/growing | 8-K explicitly discloses "Stablecoin Market Share, end of period: 27%" (−66bps YoY) — essentially stable, now a directly-quantified (not just circulation-inferred) figure | **TRUE** (unchanged, fresher citation) |
| Brand premium | No pricing-power evidence found in the Q2 2026 release (Circle doesn't charge USDC holders a fee; nothing in the release describes a price increase without volume loss) | **FALSE** (unchanged) |
| Network effect | Strengthened citation: Circle Payments Network (CPN) reached $14.7B in annualized transaction volume (trailing 30 days, +76% QoQ) with 175 financial institutions enrolled (+29% QoQ); Arc's founding validator cohort includes BlackRock, DTCC, Galaxy, Global Payments, ICE, Mastercard, MoneyGram, SBI Group, Standard Chartered, Sumitomo, and Visa — a multi-sided network effect mechanism, now with fresher quarterly growth data | **TRUE** (unchanged, stronger evidence) |
| Switching costs | No new 10-Q filed yet — still governed by the unchanged FY2025 10-K risk-factor language: switching costs "may not be significant enough to prevent" customer churn (company's own words, still on file) | **FALSE** (unchanged) |
| Scale cost advantage | The new OCC national trust bank charter and NYDFS trust approvals are a regulatory *barrier to entry*, but that's not the same as **cost-per-unit data showing a gap vs. smaller competitors**, which the evidence bar requires — none found this session | **FALSE** (unchanged) |

```
Quality Score = 39.53×0.25 + 50.65×0.15 + 100.00×0.20 + 100.00×0.15 + 40.00×0.15 + 100.00×0.10
              = 9.8825 + 7.5975 + 20.00 + 15.00 + 6.00 + 10.00
              = 68.48  →  68.5 (rounded to nearest 0.1)
```

### Result: **Quality Score 68.5 — fails the 80.0+ gate** (vs. 69.0 on 2026-06-30 — essentially flat, marginally lower)

Per [quality-scoring.md](../framework/quality-scoring.md) and [new-position.md](../.claude/commands/new-position.md) step 2: below 80.0 → stop, don't proceed to valuation. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed** this session either.

**Why the score didn't meaningfully move despite a strong-looking headline earnings report:** the metrics the source Telegram post highlighted (USDC circulation +19% YoY, transaction volume +151% YoY, an EPS beat) don't address the specific weaknesses that failed the gate on 06-30 — moat evidence gaps (still 2/5 signals) and thin core profitability. In fact, once this session's cleaner TTM reconstruction removes the prior session's generous one-off addback, **true recurring profitability reads weaker, not stronger** (ROIC 8.18% TTM vs. 12.62% FY2025-normalized), which roughly offsets a modest, genuine margin improvement (RLDC margin has climbed for five straight quarters, now above the 40% threshold). The revenue miss vs. estimate the trigger post flagged isn't itself scored (this framework doesn't score vs.-estimate misses/beats — only YoY trend and TAM/moat evidence), but the underlying growth deceleration it reflects (7% YoY total revenue growth this quarter vs. the 37.6% multi-year CAGR) is real and was explicitly considered for the Growth sub-score's structural-deceleration modifier — ultimately not applied because management's own explanation is cyclical (rate environment, crypto-market cycle), not structural (moat/TAM impairment), per the framework's explicit "structural, not cyclical" carve-out.

---

## 5. Recommendation

**PASS — do not open a position.** Same conclusion as 2026-06-30, re-derived fresh under Rule 9. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, no order setup — none of that work is meaningful for a name that fails the quality gate, and forcing it through would violate this framework's explicit non-negotiable ("if it's below 80.0... stop and report why").

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance. `portfolio/holdings.md` not touched.

---

## 7. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries carry no numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant the next full re-look:** (a) the Q2 2026 10-Q, once filed, discloses a full cash-flow statement — worth a light-touch check of whether TTM FCF/NI conversion still clears comfortably, though this is unlikely to move the gate outcome on its own; (b) cited evidence clearing the switching-costs or scale-cost-advantage moat signals (e.g. a contractual lock-in mechanism, or per-unit cost data vs. smaller stablecoin issuers — the trust-bank-charter angle is a plausible future candidate for the latter if Circle discloses compliance-cost-per-dollar-of-reserve data at scale); (c) Q3 2026 earnings (next quarterly report) or any guidance revision; (d) a management change or material M&A; (e) confirmation that the growth deceleration flagged this session has become structural rather than cyclical (e.g. a sustained further drop in USDC circulation growth, or evidence of market-share loss to a competing stablecoin).
- Absent any of the above, future Telegram mentions of CRCL should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time.

---

## Glossary

- **8-K** — The "current report" a US public company must file with the SEC within days of a material event — most commonly used to furnish (via an attached exhibit, typically "Exhibit 99.1") a quarterly earnings press release ahead of the fuller, audited 10-Q/10-K that follows weeks later.
- **10-K (Annual Report)** — The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements, MD&A, and risk factors.
- **10-Q (Quarterly Report)** — The quarterly financial-disclosure report a US public company files with the SEC between annual 10-Ks, containing unaudited (reviewed) financial statements.
- **Adjusted EBITDA** — A company's own non-GAAP variant of EBITDA that further strips out items management deems non-recurring or non-operational; not directly comparable to a GAAP-derived EBITDA.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CPN (Circle Payments Network)** — Circle's own multi-sided payments network connecting banks and financial institutions for cross-border USDC-settled transfers — cited as Network Effect Moat Signal evidence.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **GENIUS Act** — US federal legislation establishing a regulatory framework specifically for USD-denominated payment stablecoins, cited in Circle's 10-K as a named industry tailwind.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score. None fire for CRCL.
- **Invested Capital** — The total capital (debt + equity, netted for cash) deployed in a business — the denominator of ROIC.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative means net cash. CRCL is at −2.69× (net cash).
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC.
- **Quality Score** — A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. CRCL scores 68.5.
- **Reserve income** — Interest income Circle earns on the short-term US Treasuries/cash reserves backing USDC in circulation — ~95%+ of Circle's total revenue.
- **RLDC (Revenue Less Distribution Costs)** — Circle's own non-GAAP "gross profit" proxy, used as this framework's Gross Margin basis for CRCL.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **RSU (Restricted Stock Unit)** — A grant of company shares to an employee that vests over time and/or upon a triggering event (here, Circle's June 2025 IPO).
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Stablecoin** — A cryptocurrency token designed to hold a stable value, typically pegged 1:1 to a fiat currency like the US dollar.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked this session, since Phase 01 failed first).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure — the primary basis this session uses (Q3 2025 through Q2 2026), since it entirely avoids the IPO-quarter one-off distortion that required normalization in the prior session.
- **USDC** — Circle's flagship US-dollar-pegged stablecoin, the company's primary product and reserve-income driver.
