# NEW POSITION — AVGO (Broadcom Inc.) — 2026-10-03

**Task type:** NEW POSITION (fresh full evaluation of an **already-held** name, position-aware).
**Date:** 3 Oct 2026 (Saturday; US markets closed)
**Held position:** 6 sh @ avg $382.44 (IBKR `get_account_positions`), market value $2,130.60, unrealized P&L -$164.05. **Open Human Override** (2026-06-16, see [override-log.md](../portfolio/override-log.md)) — still unresolved, not this session's scope.
**Prior record:** [2026-09-28 rescore](2026-09-28-rescore-avgo.md): Valuation 71.3 / Quality 86.3 / Composite 42.5 → HOLD.
**Sector:** Semiconductors (fabless AI accelerators/networking) + infrastructure software (VMware)

---

## 1. Live price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Price used** | **$355.10** | IBKR `get_price_snapshot` (contract 313130367). `top_status` = **FROZEN** and the last-trade timestamp is 2026-10-02 23:59:58 UTC, i.e. this is the **Friday 2 Oct regular-session closing price** (market closed for the weekend), not a stale quote. Position snapshot `market_price` $355.1000061 agrees. |
| Prior close / change | $343.64 / +$11.46 (+3.33%) | IBKR |
| yfinance cross-check | `currentPrice` $355.14, `previousClose` $343.64 | within 0.01% |
| 52-week range | $289.48 – $494.23 (13-week low $335.82, 26-week low $309.77) | IBKR `misc_statistics` |
| Analyst consensus PT | $531.31 (yfinance `targetMeanPrice`) | context only |
| Move since 09-28 | $352.39 → $355.10 = **+0.77%** | far below the 15% Rule 9 threshold |

## 2. Rule 9 trigger check since 2026-09-28

| Trigger | Fired? | Detail |
|---|---|---|
| Earnings release | **No** | Q3 FY2026 reported 2026-09-02 (already in the data). Q4 FY2026 (quarter ends 1 Nov 2026) is scheduled **after close Wed 9 Dec 2026**, with guidance of ~$34.8B revenue and ~66% non-GAAP operating margin (web search result summarising Broadcom's [Q3 release](https://investors.broadcom.com/news-releases/news-release-details/broadcom-inc-announces-third-quarter-fiscal-year-2026-financial)). No new 10-Q/8-K financials, so every TTM input is carried forward. |
| Guidance revision | No | None found. |
| Management change | None found | |
| M&A | None found | |
| >15% unexplained move | No | +0.77% since 09-28; the +3.3% Friday move is explained by the news below. |
| **News (not a formal trigger)** | **Yes, flagged** | 2 Oct 2026: Bloomberg reports Broadcom's bank syndicate is starting to gather **~$60B of AI-chip financing** ($42B Class A senior secured loans led by BofA/Citi/Morgan Stanley; $18B Class B subordinated debt led by Blackstone) to help Anthropic and other AI companies fund purchases of Broadcom chips; the debt could convert into Anthropic shares ([Bloomberg](https://bloomberg.com/news/articles/2026-10-02/broadcom-starts-amassing-60-billion-to-fund-chips-for-anthropic), [Seeking Alpha](https://seekingalpha.com/news/4649721-broadcom-gathers-60b-financing-package-to-fund-ai-chips-for-anthropic-report), [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/broadcom-financing-syndicate-reportedly-seeks-102617677.html)). The sources found **do not say** whether credit risk sits on Broadcom's balance sheet, nor mention any Broadcom guarantee; they describe Broadcom as arranger and potential lender and note questions about interdependence with Anthropic (no conflict established). Demand-positive for AI revenue, but a **vendor-financing / counterparty-concentration risk flag** to resolve in the next filing. Secondary-source reporting; no Broadcom filing located. **Not a scoring input** (no balance-sheet data changed; never invent). |

**10Y US Treasury (FRED DGS10, fetched 2026-10-03):** latest posted **5.24% (2026-10-01)**; prior days 5.29% (09-30), 5.26% (09-29), 5.24% (09-28). The 2026-10-02 value had not yet posted. Used **5.24%** (vs 5.21% on 09-28; still above the 5% bracket).

## 3. Data gathered (nothing invented)

`python -m scripts.fetch_fundamentals AVGO` output (verbatim; run with yfinance's live price ~$355.14):
```
## Fundamentals — AVGO

Market Cap            = 1,695,307,005,952
Enterprise Value      = 1,730,750,971,904
Shares Outstanding    = 4,773,629,865
Forward PE            = 18.324
FCF Yield %           = 2.324
EV/EBIT               = 39.710
Net Margin %          = 42.944
Gross Margin %        = 68.770
ROIC % (NOPAT/InvCap) = 28.144  [tax_rate=0.0545, NOPAT=41,211,298,154, InvestedCapital=146,428,000,000]
Revenue 3yr CAGR %    = 24.378
Net Debt/EBITDA       = 0.937  [EBITDA_ttm=52,259,999,744]
FCF/NI TTM %          = 102.974
FCF/NI annual (oldest first) = [141.9%, 125.2%, 329.3%, 116.4%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 30.868 / 13.365 / 52.758  (n=20 quarters)
```
Basis note (unchanged since 2026-09-15): the script's Market Cap/EV/ROIC use yfinance's basic share count (4,773.6M) and its own tax-rate estimate. The framework's established basis is used for scoring: diluted shares 4,887M, TTM FCF $39,403M, TTM GAAP EBIT $42,814M, net debt $35,444M, normalized ROIC 30.47% (normalized EBIT $52,114M × (1 − 21%) ÷ invested capital $135,134M), net debt/EBITDA 0.687× ($35,444M ÷ TTM EBITDA $51,578M). All TTM/balance-sheet figures are carried forward from [2026-09-28](2026-09-28-rescore-avgo.md) (no new filing).

**Refreshed with the live price:**
- Market cap = $355.10 × 4,887M = $1,735,373.7M; EV = + $35,444M = $1,770,817.7M
- FCF yield = $39,403M ÷ $1,735,373.7M = **2.2706%**
- EV/EBIT = $1,770,817.7M ÷ $42,814M = **41.361×** (normalized: ÷ $52,114M = 33.98×, still under the 35× ceiling; the GAAP figure already saturates the sub-score at 100.0)
- Forward EPS $19.381 (yfinance `forwardEps` $19.38135) → Forward PE = 355.10 ÷ 19.381 = **18.322×**
- Dividend yield = $2.60 ÷ $355.10 = 0.7322%
- **5yr PE average moved 29.892 → 30.868** (low/high unchanged at 13.365/52.758): the script's rolling 20-quarter window changed since 09-28. Not a data error; flagged for continuity. Effect on the score is small (the deviation-vs-average modifier stays at -10).

## 4. Quality Score (Phase 01 gate)

Hard disqualifiers: FCF/NI TTM 102.97% (annual [141.9, 125.2, 329.3, 116.4], none <70%) PASS; net debt/EBITDA 0.687× (limit 2.5×) PASS; FCF positive 3+ years PASS.

`python -m scripts.scoring.quality_score` output (condensed from the script's markdown; every line is the script's):
```
Profitability (25%)
NetMargin_Component = clamp((42.944/30)x100) = 100.00
ROIC_Component = clamp((30.47/30)x100) = 100.00
Profitability_Score = (100.00 + 100.00) / 2 = 100.00

Margins (15%)
GrossMargin_Score = clamp((68.77/80)x100) = 85.96

Growth (20%)
Growth_Score = clamp((24.378/25)x100) = 97.51
+10 TAM/pricing-power evidence (carried forward: AI accelerator/networking TAM, VMware private cloud)
Growth_Score (final, clamped) = 100.00

Balance Sheet (15%)
BalanceSheet_Score = clamp(100x(1 - 0.687/4)) = 82.82

Moat Signal (15%)
market_share_stable_or_growing True | brand_premium False | network_effect False | switching_costs True | scale_cost_advantage False
Moat_Score = (2/5) x 100 = 40.00

FCF Quality (10%)
FCFQuality_Score = clamp(((1.0297 - 0.40)/0.60)x100) = 100.00

Quality Score = (100.00x0.25) + (85.96x0.15) + (100.00x0.20) + (82.82x0.15) + (40.00x0.15) + (100.00x0.10)
= 86.318 -> rounds to 86.3

# Quality Score = 86.3 - PASSES the 80.0+ gate
```
Unchanged from 09-28 (no input moved). The financing news does not change any scored input today; if a later filing shows Broadcom retaining the credit risk, net debt and FCF quality will be re-tested then.

## 5. Rate Environment Gate and Valuation Score (Phase 02)

`python -m scripts.scoring.valuation_score` output (verbatim content):
```
FCF Yield (40%)
FCF_Score = clamp(100x(1 - 2.2706/10)) = 77.294

EV/EBIT
EV/EBIT_Score = clamp((41.361 - 12)/23 x 100) = 100.000

Forward PE
FwdPE_Score (raw) = clamp((18.322 - 13.365)/(52.758 - 13.365) x 100) = 12.583
Deviation vs 5yr avg (30.868) = (18.322 - 30.868)/30.868 x 100 = -40.644%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(12.583 + -10) = 2.583

PEG
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

Rate Environment Gate
EY = 1/18.322 x 100 = 5.4579%
Spread = EY - 10Y (5.24%) = 0.2179pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.24% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

Upside/Downside Modifier
PW Fair Value = 0.25x724.85 + 0.50x484.53 + 0.25x247.11 = 485.2550
Gap Upside % = (485.2550/355.1) - 1 = 36.6531%
Annualized gap = 36.6531% / 1.17yr = 31.3274%/yr
E = 31.3274 + 12.0 (intrinsic growth) + 0.7322 (shareholder yield: 0.7322 div + 0 buyback) = 44.0596%/yr
E >= H (10.0%) -> M = -15 x clamp((44.0596-10.0)/15, 0, 1) = -15.0000
Upside/Downside Modifier (bounded [-15, +15]) = -15.0000

Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2 = 71.434
Final Score = Raw (71.434) + Rate Modifier (+15) + Upside/Downside Modifier (-15.000) = 71.434 -> rounds to 71.4

# Valuation Score = 71.4
```
Input notes: scenario fair values use NTM EPS $19.381 with the same architecture as every AVGO session since 2026-07-04 — bull = EPS × 1.10 × 34× = $724.85, base = EPS × 25× = $484.53, bear = EPS × 0.85 × 15× = $247.11. Catalyst: management's FY2027 AI-semiconductor revenue target (>$100B), confirmation ~Dec 2027, window 1.17 yr (Guardrail 1 satisfied). Intrinsic growth 12.0% carried forward. No buyback yield credited.

**Valuation 71.4 sits in the raw 70.0–79.9 band**, but per valuation-scoring.md the **Composite Score governs** once a Quality Score is on file.

`python -m scripts.scoring.composite_score` output:
```
Composite Score = 0.50x(100 - 86.3) + 0.50x71.4 = 42.550 -> rounds to 42.6
# Composite Score = 42.6   (Quality Score 86.3, Valuation Score 71.4)
```
**Composite 42.6 → "Cheap" band 30.0–49.9 → standard position 3–5%, limit order with 25–30% margin of safety.** (Flat vs 42.5 on 09-28.)

## 6. Fair value and order setup

**Method A — 3-stage DCF** (Rule 1: Tech/Growth → DCF primary), same growth path as prior sessions, rebased on TTM FCF $39,403M:
```
Cost of equity = 5.24% + 1.457 x 5.0% (ERP, assumed) = 12.525%
After-tax cost of debt = (3,116/59,419 = 5.244%) x (1 - 21%) = 4.143%
Weights: E 96.69% (mkt cap $1,735,373.7M) / D 3.31% (debt $59,419M) -> WACC = 12.247%
FCF y1-y5 (+25/+20/+15/+12/+10%): 49,253.8 / 59,104.5 / 67,970.2 / 76,126.6 / 83,739.3
FCF y6-y10 (linear fade to 2.5%): 90,857.1 / 97,217.1 / 102,564.0 / 106,666.6 / 109,333.3
TV = 109,333.3 x 1.025 / (0.12247 - 0.025) = $1,149,696M; PV(TV) = $362,090M (45.4% of EV, under the 75% cap)
PV of FCFs y1-10 = $435,367M; EV (DCF) = $797,457M; equity = $797,457M - $35,444M = $762,013M
DCF FV/share = $762,013M / 4,887M = $155.93
```
**Method B — scenario-weighted multiples:** PW FV = $485.26 (the valuation script's $485.2550).
**Divergence flag (same as every prior session):** DCF $155.93 vs multiples $485.26 — a disciplined GDP-terminal-growth DCF versus AVGO's own 5-year PE range. Rule 3 (Tech/Growth) blend 40/60:
```
Blended FV = 0.40 x 155.93 + 0.60 x 485.26 = 62.37 + 291.16 = $353.52
```
The blended FV ($353.52) is essentially the live price ($355.10): the stock trades at the framework's blended fair value, with no margin of safety.

`python -m scripts.scoring.order_setup` (score 42.6, FV $353.52, bull $724.85, live $355.10, MoS 27.5%, stop 27.5%, portfolio value $61,298, risk 1.5%, cap 5%, 6 shares held):
```
Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (353.52) x (1 - 27.5%) = 256.3020
Live price 355.1 vs buy price ceiling 256.3020 -> limit order at buy price (live price above ceiling); entry price used = 256.3020
Primary Sell Target = Fair Value = 353.5200
Bull-Case Trim Target = Bull FV (724.85) x 0.90 = 652.3650
Stop Loss = Entry Price (256.3020) x (1 - 27.5%) = 185.8189
R/R Ratio = (353.5200 - 256.3020) / (256.3020 - 185.8189) = 97.2180/70.4830 = 1.3793:1
*** FLAG: R/R 1.3793:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = 61298 x 1.5% = 919.4700; Risk Per Share = 70.4830; risk-based shares = 13.0453
Allocation cap = 61298 x 5% = 3064.9000 -> 11.9582 shares
Position Size = 11.9582 shares ($3,064.90) [binding: allocation cap]; current 6; gap 5.9582
```
Full MoS/stop matrix (every cell flagged below 2:1):

| MoS \ Stop | 25% | 30% |
|---|---|---|
| 25% (buy $265.14) | 1.33:1 | 1.11:1 |
| 30% (buy $247.46) | **1.71:1** | 1.43:1 |

Best case in the allowed range is 1.71:1 and still fails the 2:1 minimum. Portfolio value $61,298 = IBKR NLV $50,408 (live `get_account_balances` BASE) + Freedom24 $10,890 (last known, unchanged since the 08-22 sync); same combined-total convention as holdings.md, which used $61,622.32 with the older IBKR NLV of $50,732.36.

## 7. Position-aware recommendation

**Existing position:** 6 sh × $355.10 = $2,130.60 = **3.48% of the combined portfolio ($61,298)** (3.46% on holdings.md's $61,622.32; 4.23% of IBKR-only NLV $50,408). The target band for Composite 42.6 is 3–5% and the hard cap is 15% — **well inside both**; no concentration issue. Unrealized P&L -$164.05 (-7.2% vs. avg cost $382.44) is sunk cost and never a trigger.

| Action | Test | Result |
|---|---|---|
| Trim | Composite 42.6 is far below the 70.0+ trim region; no fundamental deterioration; 15% cap not approached | **No** |
| Exit | No exit trigger | **No** |
| **Add** | Needs a valid order setup: R/R is 1.11–1.71:1 across the whole allowed MoS/stop range (fails 2:1); live price $355.10 is above the $247–265 buy ceiling; blended FV ≈ live price; position already inside its 3–5% band | **No — R/R gate fails** |
| **Hold** | Quality 86.3 passes; Composite in Cheap band; position within target size | **HOLD, 6 shares** |

# **Recommendation: HOLD the 6-share position. Do not add. No new order.**

If the user nonetheless wants a standing add order, the framework's computed ceiling is $256.30 (stop $185.82, sell target $353.52), but it is flagged as failing R/R, so none is recommended. Same action category as 09-28 and 09-15.

**Why not act on Friday's +3.3% or the financing news:** act on score changes and documented fundamental triggers, never price alone. The score barely moved (71.3 → 71.4; Composite 42.5 → 42.6), no financials changed, and the financing report raises an unresolved risk-allocation question rather than a data input.

**Open override (reported, unresolved):** the 2026-06-16 override is still "Open — under review" in override-log.md with no user-supplied rationale. Unchanged; needs the user.

## 8. Next review trigger

- **Q4 FY2026 earnings, Wed 9 Dec 2026 (after close)** — rescore with fresh TTM figures; check (1) whether the Anthropic/AI-chip financing creates Broadcom balance-sheet exposure (net debt, guarantees, receivables, investments), (2) the EV/EBIT GAAP-vs-normalized gap (33.98× vs the 35× ceiling), (3) the 10Y regime (above 5% for three consecutive checks; if it falls under 5%, the rate modifier reverts to +5 and the raw valuation score drops ~5 points).
- Earlier trigger on a >15% unexplained move from $355.10, guidance revision, M&A, management change, or a Broadcom filing/credible report that it retains credit risk on the financing.
- Unconditional: the user still needs to supply a rationale for the 2026-06-16 override.

## 9. Watchlist and housekeeping

- `python -m scripts.watchlist_diff --old-score 71.3 --old-category HOLD --new-score 71.4 --new-category HOLD ...` returned **`new_file`** ("score changed 71.3 -> 71.4"), so [watchlist/in-portfolio/AVGO/AVGO-2026-10-03.md](../watchlist/in-portfolio/AVGO/AVGO-2026-10-03.md) was created (prior rows carried forward).
- `python -m scripts.stale_score --apply` → `newly_stale: [], resolved: []` (AVGO carried no stale mark).
- `framework/glossary.md`: added **Syndicated loan / senior secured tranche** and **Vendor / customer financing**.
- `portfolio/holdings.md` not edited (weight refresh is `/sync-portfolio`'s job). No `decisions/` entry (no trade).
- Tooling note: on Windows, `order_setup`'s checklist crashes with a cp1252 UnicodeEncodeError unless `PYTHONIOENCODING=utf-8` is set.

---

## Glossary

Standing definitions in [framework/glossary.md](../framework/glossary.md):

- **Add / Hold / Trim** - increase, keep, or reduce an existing position; only Hold is supported here.
- **Allocation cap** - the maximum share of the portfolio a single position may occupy (5% for the Cheap band; 15% absolute cap).
- **Beta** - sensitivity of a stock to market moves; an input to cost of equity.
- **Composite Score** - 0.50 x (100 - Quality) + 0.50 x Valuation; governs the action table (42.6 here).
- **DCF (Discounted Cash Flow)** - valuing a company by discounting projected future cash flows to today.
- **EBIT / EBITDA** - operating earnings before interest and taxes / also before depreciation and amortization.
- **EPS / Forward PE** - earnings per share / price divided by next-twelve-months expected EPS.
- **EV / EV/EBIT** - enterprise value (market cap + debt - cash) and its ratio to EBIT.
- **FCF / FCF Yield / FCF/NI** - free cash flow; FCF divided by market cap; FCF divided by net income.
- **FROZEN (market-data status)** - the broker's label when the market is closed; the last price shown is the last regular-session trade.
- **Fair Value (FV) / PW Fair Value** - analyst's estimate of intrinsic worth; probability-weighted 25% bull + 50% base + 25% bear.
- **Hard disqualifier** - a Quality condition that fails a company regardless of its score.
- **Human Override** - a position held outside the framework's own rules; AVGO's 2026-06-16 entry is open.
- **Margin of Safety (MoS)** - how far below fair value the buy price is set.
- **Moat** - durable competitive advantage.
- **Net Debt/EBITDA** - leverage ratio; hard disqualifier above 2.5x.
- **Quality Score** - 0-100 grade; 80.0+ needed to proceed (86.3 here).
- **R/R (Risk/Reward)** - expected gain divided by expected loss; the framework needs at least 2:1.
- **Rate Environment Gate** - comparing the earnings yield with the 10-Year Treasury yield and adding a rate-regime penalty (+15 here).
- **Rule 0 / Rule 9** - always fetch a live price first; forced re-valuation on specified triggers.
- **Syndicated loan / senior secured tranche** - a large loan split among many lenders, the safer senior piece repaid first (new term).
- **Terminal Value / WACC** - value of cash flows beyond the forecast window; the DCF discount rate.
- **Valuation Score** - 0-100 score where lower means cheaper (71.4 here).
- **Vendor / customer financing** - a supplier helping its own customers pay for its products; a risk flag (new term).
