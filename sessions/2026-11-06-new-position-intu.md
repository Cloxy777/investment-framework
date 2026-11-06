# NEW POSITION — Intuit Inc. (INTU) — 2026-11-06

**Task type:** NEW POSITION (re-evaluation, not held) — prior: 2026-08-23 (BUY, Composite 13.0), 2026-08-24 (rescore deferral), 2026-08-26 (WATCHLIST ONLY, R/R fail, Quality 81.2)
**Date:** 06 Nov 2026 | **10Y Treasury:** 4.90% (FRED `DGS10`, 2026-11-04, latest posted) | **Rate Regime Modifier that would apply:** +5 (3.5–5% bracket) — *not applied: valuation scoring did not run (gate failed)*
**Portfolio weight:** 0% (not held)

**Outcome in one line:** Quality Score **78.1 — FAILS the 80.0+ gate → PASS (Phase 01 FAIL).** No valuation score, Composite Score or order setup computed, per the `/new-position` instruction to stop at a failed gate. The result is a **narrow, input-source-driven fail** (see §5) — not a deterioration in the business.

---

## 1. Why this session ran
User-initiated `/new-position intu`. Context: INTU carried a `⚠️ STALE SCORE` mark (scoring methodology changed 2026-10-12: SBC treated as a cost), so its last score (Composite 10.8) was not comparable to today's methodology. Rule 9 inputs since 08-26: **Investor Day 2026-09-17** reiterated Q1 and FY2027 guidance with no changes (Business Wire release, via Finviz); a Q1 FY2027 report is **not yet out** (Business Wire notice: **Nov 19**, per the release page sidebar; AJ Bell lists 11-20 — unconfirmed). So no new financial statements exist beyond FY2026 (10-K/8-K of 2026-08-25); TTM = FY2026.

Noted from the Investor Day release: starting Q1 FY27, Intuit's non-GAAP measures **no longer exclude SBC** (FY27 non-GAAP EPS guide $22.88–23.12 now includes a $5.81 SBC hit), which is consistent with this framework's SBC-as-a-cost treatment but means FY27 guidance is **not like-for-like** with FY26 non-GAAP EPS $24.27.

## 2. Live price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$351.83** (bid 347.28 / ask 354.14; −$3.01, −0.85% on the day) | IBKR `get_price_snapshot`, contract 270662 |
| 52-week range | $251.68 – $675.92 (13-wk high $372.98, low $262.32) | IBKR `misc_statistics` |
| Dividend yield | 1.4% | IBKR |
| Analyst targets (sanity check only) | mean $407.76 / median $400 / high $732 / low $290; yfinance "current" $354.84 | yfinance |

Price vs 08-26 ($348.40): +1.0%. Not a Rule 9 move.

## 3. Fundamentals — `python -m scripts.fetch_fundamentals INTU` (verbatim)

```
Market Cap            = 94,826,020,864
Enterprise Value      = 96,047,022,080
Shares Outstanding    = 267,236,000
Forward PE            = 13.170
FCF Yield %           = 9.087
EV/EBIT               = 15.311
Net Margin %          = 21.289
Gross Margin %        = 80.171
ROIC % (NOPAT/InvCap) = 17.855  [tax_rate=0.2412, NOPAT=4,760,265,581, InvestedCapital=26,661,000,000]
Revenue 3yr CAGR %    = 14.287
Net Debt/EBITDA       = 0.433  [EBITDA_ttm=6,848,999,936]
FCF/NI TTM % (plain)  = 188.721
(FCF - SBC)/NI TTM %  = 143.693  [reported NI]
SBC yield %           = 2.168
Gross buyback yield % = 5.707
FCF/NI annual (oldest first) = [200.8%, 156.4%, 157.2%, 188.7%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 33.439 / 13.207 / 64.904  (n=20 quarters)
```

```
SBC block (TTM, advisory — no score effect)
  SBC 2,056,000,000.0   FCF 8,617,000,000.0   Market cap 94,826,020,864.0
  SBC/FCF = 23.9%
  FCF yield (reported)  = 9.09%
  FCF yield after SBC   = 6.92%
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```

**Notes on the script output (disclosed, not hidden):**
- **Forward PE 13.17 is not used for anything here**: yfinance's `forwardEps` ($26.94) is the *FY2028* consensus. The relevant forward year is FY2027: consensus non-GAAP EPS **$23.81** (32 analysts, range $21.83–29.21, yfinance `earnings_estimate`) vs. Intuit's own guidance midpoint **$23.00** → forward PE 14.8× (consensus) or **15.3×** (guidance, the conservative, primary-source basis used in the 08-26 session). Moot for scoring since the gate failed.
- **SBC** TTM $2,056M = 507 + 485 + 521 + 543 (the four quarters ending 2026-07-31, yfinance); **FCF** $8,617M = 1,258 + 5,236 + 1,524 + 599. FCF and net income reconcile to the 08-26 session's 8-K-sourced figures ($8,617M; $4,566M).
- **Advisory flags** (script gave `UNKNOWN`; re-run manually with GAAP diluted EPS FY2026 $16.46 vs FY2025 $13.67, forward PE 15.30, FY27 guided EPS growth 23.5%): 
  ```
  cycle_peak             NONE     EPS TTM +20% (<= 100%†)
  multiple_ceiling       NONE     forward PE 15.3, EPS growth 23.5%
  value_trap_candidate   NONE     forward PE 15.3, EPS TTM growth +20.4%
  ```
  No flag raised; no `UNKNOWN` remains. SBC/FCF 23.9% is below the 30% "elevated" line.

## 4. Phase 01 — Quality Score (script output, verbatim)

Inputs: script outputs above plus manual qualitative fields. TAM/deceleration/moat evidence is **carried from the 2026-08-26 session** (its citations: FY2026 8-K, earnings-call coverage, AceCloudHosting) and updated only with the 09-17 Investor Day reiteration; none of it was freshly re-verified this session, and no new evidence has been published since (no filing after 8-K 2026-08-25). Hard disqualifiers: FCF/NI annual [200.8, 156.4, 157.2, 188.7] — none <70%; Net Debt/EBITDA 0.433× < 2.5×; FCF positive 3+ years; SBC/FCF 23.9% < 100% — **none fire**.

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((21.289/30)x100) = 70.96
ROIC_Component = clamp((17.855/30)x100) = 59.52
Profitability_Score = (70.96 + 59.52) / 2 = 65.24
```
**Margins (15%)**
```
GrossMargin_Score = clamp((80.171/80)x100) = 100.00
```
**Growth (20%)**
```
Growth_Score = clamp((14.287/25)x100) = 57.15
+10 TAM/pricing-power evidence: Intuit FY2026 8-K (2026-08-25): Big Bets (QBO Advanced/Intuit Enterprise Suite, assisted tax, money services) grew 34% and are ~30% of revenue; QBO Advanced + IES customers +28% YoY; reaffirmed in FY27 guidance at the 2026-09-17 Investor Day (Business Wire).
-10 structural growth deceleration evidence: FY27 guidance (8-K 2026-08-25, reiterated 2026-09-17 Investor Day): revenue +9-10% vs +13.9% in FY2026; TurboTax +2-3%; online paying customers +3%, TurboTax units -2%.
Growth_Score (final, clamped) = 57.15
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - 0.433/4)) = 89.18
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | QuickBooks ~80% US small-business accounting share (AceCloudHosting 2026), carried from 2026-08-26 session; not re-verified this session |
| brand_premium | True | QBO list prices raised 1 Aug 2026 (Plus 115->140, Advanced 275->340) with GBS +14%/QBO Online Accounting +20% growth in Q4 FY26 (8-K); counter-evidence: TurboTax price is top churn reason (earnings call) - carried, flagged |
| network_effect | True | QBO App Store third-party integrations and Credit Karma two-sided marketplace, carried from 2026-08-26 session |
| switching_costs | True | Business + accountant + integrations multi-party lock-in on QBO, carried from 2026-08-26 session |
| scale_cost_advantage | False | No cost-per-unit citation vs smaller competitors |
Moat_Score = (4/5) x 100 = 80.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((1.4369 - 0.40)/0.60)x100) = 100.00  [ratio = (FCF - SBC)/NI]
```
**Quality Score — Final**
```
Quality Score = (65.24x0.25) + (100.00x0.15) + (57.15x0.20) + (89.18x0.15) + (80.00x0.15) + (100.00x0.10)
= 78.116 -> rounds to 78.1
```

# Quality Score = 78.1 — FAILS the 80.0+ gate

## 5. Why it fails now when it passed on 08-26 (81.2) — the sensitivity that matters

The only scoring inputs that changed are **data-source definitions**, not business fundamentals:

| Input | 08-26 session (stockanalysis.com / hand-built) | This session (`fetch_fundamentals`, yfinance) | Effect |
|---|---|---|---|
| ROIC | 22.93% | **17.855%** (NOPAT $4,760M ÷ invested capital $26,661M) | Profitability 73.70 → 65.24 (−2.1 pts of Quality) |
| Net Debt/EBITDA | 0.169× (net debt $1,136M) | 0.433× (net debt $2,964M — yfinance counts only cash, not short-term investments, and includes $752M leases) | Balance Sheet 95.78 → 89.18 (−1.0 pt) |
| FCF Quality | 100.0 | 100.0 (after-SBC ratio 143.7%) | none — SBC methodology change does not bite here |

**ROIC source check (disclosed):** the script's NOPAT uses yfinance `EBIT` $6,273M, which — like the aggregator operating-income figure flagged in the 08-26 session (§2) — is **above the SEC 8-K GAAP operating income of $5,884M**. Re-running ROIC on 8-K EBIT with the script's tax rate and invested capital gives 5,884 × (1 − 0.2412) ÷ 26,661 = **16.75%**. So correcting the script's EBIT *lowers* ROIC further; it does not rescue the gate.

| Scenario | ROIC | Quality | Gate |
|---|---|---|---|
| **Script as run (primary)** | 17.855% | **78.1** | **FAIL** (−1.9) |
| ROIC on SEC 8-K EBIT | 16.75% | 77.7 | FAIL (−2.3) |
| ROIC as used on 08-26 (stockanalysis.com 22.93%, net-debt term unchanged at 0.433×) | 22.93% | 80.2 | PASS (+0.2) |

Only the third row passes, and only by 0.2, on a ROIC figure whose derivation is not reproducible from this repo's script. **The framework instruction is to use the script's output and stop on a fail; I did not substitute the passing-source ROIC.** Both the 08-23 (82.8) and 08-26 (81.2) passes were already flagged as fragile (Moat brand-premium call; growth-deceleration treatment); this is the same fragility showing up through a different input. Note also that all 08-26 sensitivity rows that dropped the moat or growth modifier would fail anyway.

**Open question for the investor (not for this run to settle):** which ROIC definition the framework should standardise on for asset-light software with heavy share-count management (the framework's own script vs. an external aggregator). If the stockanalysis.com definition were adopted, INTU would sit at ~80.2 — a coin-flip pass — and Phase 02 would then need to be run.

## 6. Recommendation

# **PASS (do not enter) — Phase 01 FAIL, Quality Score 78.1 < 80.0.**

- No Rate Gate, Valuation Score, Composite Score or order setup run (gate policy).
- For context only (informational, no score effect): FCF yield 9.09% (6.92% after SBC), EV/EBIT 15.3×, forward PE ~15.3× (guidance midpoint) — optically cheap. On 08-26 the entry was already blocked by the 2:1 R/R gate (1.46–1.83:1); nothing in the Quality fail changes the "no entry" conclusion, it only reinforces it.
- Nothing is a Full Exit trigger (not held). No decision-log entry (no trade).

## 7. Next review trigger
- **Q1 FY2027 earnings — Nov 19, 2026** (first print under the "deliberate reset"; first with Mailchimp as its own segment and SBC-inclusive non-GAAP). Mandatory Rule 9 re-score then.
- Earlier if the ROIC-definition question in §5 is resolved in favour of the aggregator basis, or the price falls toward the ~$285–300 zone from the 08-26 R/R analysis (then re-run the full chain, incl. the Quality gate).

## Glossary

**Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md).
**ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
**Rule 0**: This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
**Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
**SBC (Stock-Based Compensation)**: Employee pay in the form of company shares or stock options rather than cash. A non-cash expense added back in cash-flow statements (inflating FCF relative to GAAP net income), but a real economic cost to existing shareholders through ongoing dilution — worth tracking alongside FCF/NI conversion and share-count trend, not just the headline FCF figure. Since the 2026-10-12 methodology it is treated as a cost in both the FCF yield (Valuation) and FCF Quality (Quality).
**FCF**: Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
**Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
**Non-GAAP**: A company's own adjusted presentation of a financial measure (e.g. Non-GAAP net income/EPS, Adjusted EBITDA) that strips out items management deems non-recurring or non-operational — severance, litigation provisions, acquired-intangible amortization, one-off tax items, and similar. Useful for management's own view of underlying trend, but self-reported and not independently audited to the same standard as the GAAP figures alongside it. This framework scores off **GAAP** figures throughout (see the many company-specific Non-GAAP variants above — Adjusted EBITDA, AOI, Core, Benchmark EBIT — each with the same caveat), consistent with not scoring self-reported, company-adjusted metrics (see "Why Forward Guidance Is Not a Sub-score" in [valuation-scoring.md](valuation-scoring.md)). Visa's Q3 FY2026 release, for example, reported Non-GAAP net income of $6.3B ($3.32 diluted EPS) vs. GAAP net income of $5.6B ($2.97) — this framework's 2026-07-29 V session scored off the GAAP figures. *(New term.)*
**GAAP**: Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements.
**Moat Signal**: This framework's 5-point Quality Score checklist ([quality-scoring.md](quality-scoring.md)) that turns the general "Moat" concept (above) into a scored input: market share stable/growing, brand premium, network effect, switching costs, and scale cost advantage, each markable TRUE only against a cited source — `Moat_Score = (count of TRUE signals ÷ 5) × 100`.
**TAM**: Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
**EBIT**: Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
**Investor Day**: A company-hosted event (distinct from a routine quarterly earnings call) where management presents a broader, often multi-year strategic and financial outlook to investors and analysts. Like quarterly guidance, an Investor Day's forward-looking targets are self-reported management commentary: this framework treats it as a mandatory Rule 9 re-valuation *trigger*, never as a scored input in its own right (see "Why Forward Guidance Is Not a Sub-score" in [valuation-scoring.md](valuation-scoring.md)). SanDisk (SNDK) held its first as a standalone company on 2026-08-13, cited in this framework's 2026-08-13 SNDK session. *(New term.)*
**Composite Score**: This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Used against the Phase 03/05 action tables instead of the raw valuation score. See [valuation-scoring.md](valuation-scoring.md).
**Forward PE**: Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings).
**FCF/NI conversion ratio**: Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. A low ratio without a CapEx explanation is a red flag for earnings-quality games (see the Valeant/Wirecard cases in [graveyard-audit.md](graveyard-audit.md)).

**Phase 01 FAIL** (framework label): the candidate's Quality Score is below the 80.0 gate, so it is not scored for valuation and not bought.
**PASS (action)**: in this framework's watchlist, "PASS" means "do not enter" — it is not an approval.
