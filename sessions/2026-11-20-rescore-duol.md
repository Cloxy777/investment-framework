# RESCORE — DUOL (Duolingo, Inc.) — 2026-11-20

**Task type:** RESCORE (mode `--both`), user-invoked (`/rescore DUOL`), post-earnings (Q3 FY2026 print, 2026-11-03)
**Date:** 20 Nov 2026
**10Y US Treasury Yield:** 5.07% — FRED DGS10 print for 2026-11-18, as recorded in today's [NVDA rescore](2026-11-20-rescore-nvda.md) (not re-fetched here: direct curl to Treasury/SEC returned nothing in this environment). Cross-check: a web search shows the 10Y closed 5.10% on 2026-11-17 (secondary source).
**Rate Regime Modifier (Step 2):** +10 (10Y above 5%)
**Last review:** 01 Sep 2026 (Valuation 85.1, Quality 83.2, Composite 51.0 — price-only Rule 9 rescore, [log](2026-09-01-rescore-duol.md)). Last *fundamentals* rescore: 06 Aug 2026 (Q2 FY2026).
**Position:** 10.83% of the framework account per [holdings.md](../portfolio/holdings.md) (IBKR sync 2026-11-15, DUOL then $131.59). Price is now higher, so true weight is above 10.83% (exact figure needs the next `/sync-portfolio`). Not re-synced this run.
**Sector:** Technology — Education Software (EdTech / Language Learning)

**Why this session fired:** Q3 FY2026 earnings (Rule 9 quarterly re-score). Price move since 09-01 ($158.50 → $146.26, −7.7%) is below the 15% line; the trigger is the earnings filing, not price. This is also the first DUOL score under the 2026-10-12 SBC-as-a-cost methodology (the 09-01 watchlist entry carried a STALE SCORE banner).

---

## 1. Live Price (Rule 0)

IBKR `get_price_snapshot` (contract 505002183): last **$146.26**, bid/ask $145.73 / $146.85, prior close $149.38, day −$3.12 (−2.09%). 52-week range $87.89 – $213.37; 13-week high $175.56, 26-week low $103.68. Fetched first, before any valuation math.

## 2. What changed since 2026-09-01 (primary source: SEC 8-K, accession 0001628280-26-069474, filed 2026-11-03)

Read via a fetch subagent from the EX-99.1 press release and EX-99.2 shareholder letter. Figures in $ thousands unless noted.

| Item | Q3 FY2025 | Q3 FY2026 |
|---|---|---|
| Revenue | 271,713 | **309,007** (+14%) |
| Gross profit | 196,911 | 225,132 (72.9% margin vs 72.5%) |
| Income from operations | 35,159 | **24,196** (−31%) |
| Net income | 292,195 (includes $222.7M one-time tax valuation-allowance release) | **27,165** |
| Diluted EPS | $5.95 | **$0.54** (consensus $0.55, a penny miss) |
| Bookings | $281.9M | $316.1M (+12%) |
| DAUs | 50.5M | **64.9M (+29%)**, up from +23% in Q2 |
| Paid subscribers | 11.5M | 13.1M (+14%) |
| Free cash flow | 77,356 | 75,340 |

- Q3 GAAP opex includes an **$11.4M accrual** for a company-wide bonus tied to Q4 DAU growth of 25%+, plus a timing shift of some expenses from Q3 into Q4 (company-stated).
- **Guidance:** Q4 revenue $322M (+14%), Q4 bookings $382M (+13%), Q4 adjusted EBITDA $84M (26.1%); Q4 gross margin 72.0%, down 90bp sequentially from expanded AI-feature rollout. FY2026 revenue $1,221M (+18%), bookings $1,296M (+12%), adjusted EBITDA $323M (26.5%). Q4 DAU growth guided "similar to Q3". No 2027 guidance.
- **Buyback:** $400M program (announced February). $6.4M in Q3 (48,419 shares); **$82.0M cumulative through 2026-10-30** (781,439 shares). Company says this offset all dilution from 2024–2025.
- **Dilution table (shareholder letter):** 47.1M shares outstanding at 2026-09-30; **50.8M total estimated diluted shares** (includes 2.6M RSUs, 0.4M option dilution, 0.6M unearned performance RSUs).
- **Checkpoints set on 09-01 / 08-06:** DAU growth above 20% — beat (29%). Gross margin ~71% — beat (72.9%). Revenue growth vs the 11.1% guide — beat (14.0%). Buyback offsetting dilution — company says yes for 2024–2025, but diluted count still rose (50.03M diluted weighted average in Q2 vs 50.8M estimated diluted now).
- Net result: user growth strong, monetisation growth and operating margin soft. GAAP operating income fell 31% YoY.

## 3. Data sourcing and gaps

1. **`python -m scripts.fetch_fundamentals DUOL` ran successfully** (yfinance worked again). Its TTM statement fields match the SEC data, so I used them: TTM FCF $395,488K = 397,504 − 77,356 + 75,340 (matches the 08-06 TTM roll-forward exactly); TTM net income $145,737K = 41,954 + 43,460 + 33,158 + 27,165; TTM gross margin 72.81% and net margin 12.327% reconcile to my roll-forward. Verbatim output:

```
Market Cap            = 6,894,159,360
Enterprise Value      = 5,757,803,520
Shares Outstanding    = 40,779,003
Forward PE            = 18.955
FCF Yield %           = 5.737
EV/EBIT               = 39.404
Net Margin %          = 12.327
Gross Margin %        = 72.811
ROIC % (NOPAT/InvCap) = 8.278  [tax_rate=0.2369, NOPAT=111,502,319, InvestedCapital=1,347,006,000]
Revenue 3yr CAGR %    = 41.082
Net Debt/EBITDA       = -5.661  [EBITDA_ttm=166,504,000]
FCF/NI TTM % (plain)  = 271.371
(FCF - SBC)/NI TTM %  = 163.920  [reported NI]
SBC yield %           = 2.271
Gross buyback yield % = UNKNOWN - supply manually; scorers will stop and ask  (enter 0 only if the filings show no repurchases)
FCF/NI annual (oldest first) = [-73.1%, 870.9%, 298.5%, 87.0%]
FCF positive 3yr+     = True
5yr PE history        = NO-HISTORY FALLBACK (n=17 usable quarters) — only 17 quarters of reconstructable TTM-EPS PE history available, need 20 (5yr) — no-history fallback per valuation-scoring.md, never averaging over an undisclosed shorter window

SBC block (TTM, advisory — no score effect)
  SBC 156,596,000.0   FCF 395,488,000.0   Market cap 6,894,159,360.0
  SBC/FCF = 39.6%  -> at/above the 30% — watch line
  FCF yield (reported)  = 5.74%
  FCF yield after SBC   = 3.47%
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```

2. **yfinance fields I did not use, and why:**
   - *Shares (40.78M), market cap, EV, ROIC (8.3%), net debt/EBITDA (−5.66×):* Class A only / a different invested-capital definition. Same dual-class trap documented in the 07-04 and 08-06 sessions. I rebuilt these from the filing, using **50.8M company-stated total diluted shares** (new this quarter; the 10-Q cover count and weighted-average diluted count were not in the 8-K exhibits — weighted-average diluted shares implied by NI ÷ EPS is ≈50.3M, derived, not reported).
   - *Forward PE 18.955:* Yahoo's forward EPS implies ≈$7.71, far above any GAAP estimate (FY2026 GAAP EPS consensus $2.80, Chartmill, 2026-11-14, 25 analysts; FY2027 $3.28, WallStreetZen, undated). This is the same GAAP-vs-non-GAAP vendor mismatch flagged in the 08-06 session. I used **$146.26 ÷ $3.28 = 44.6×** as the forward PE; the Rate Gate Step 1 fails under *both* readings (18.96× → earnings yield 5.27%, spread +0.20pp vs the 10Y, below the +1.5pp threshold), so the choice does not change the score. The forward-PE sub-score itself is the no-history fallback (50.0) regardless.
3. **TTM EBIT rolled forward:** Q4 FY25 43,454 + Q1 FY26 44,527 + Q2 FY26 33,945 + Q3 FY26 24,196 = **$146,122K** (Q4/Q1/Q2 from the 08-06 log, SEC XBRL-sourced; Q3 from the 8-K). Matches yfinance's EV/EBIT-implied EBIT.
4. **TTM D&A:** 15,799 (08-06) − 3,553 + 4,280 = **$16,526K**; TTM EBITDA = 146,122 + 16,526 = **$162,648K** (yfinance shows 166,504K — different D&A basis; I kept the filing-based figure).
5. **Net debt (same convention as 08-06):** operating lease liability (noncurrent) $84,216K − cash and equivalents $1,239,607K = **−$1,155,391K**. This excludes $134,294K of short-term and $110,120K of long-term investments, as before. Including them would make net cash $1,399,805K and EV/EBIT 41.3× instead of 42.9× — both above the 35× cap, so **no score effect**. Total debt is zero (no debt line on the balance sheet). The current portion of lease liabilities is not broken out in the 8-K.
6. **Gross buyback yield:** $82.0M cumulative program-to-date through 2026-10-30 (company-stated) ÷ market cap = 1.104%. The strict TTM-to-9/30 figure is a few $M lower (October purchases are included); effect under 0.05pp of yield, and the buyback term only moves the modifier by that amount. No pre-2026 TTM repurchases are known; none assumed.
7. **SBC TTM $156,596K** is from yfinance's cash-flow statement (9M FY26 SBC expense $120,334K per the 8-K cash-flow statement; the Adj. EBITDA reconciliation's larger SBC line includes payroll taxes on equity). Not independently re-derived for Q4 FY25.
8. **Not normalised:** the Q3 FY2025 $222.7M tax-valuation-allowance release has now rolled out of the TTM window, so TTM net income ($145,737K) needs no Rule 6 normalisation (08-06 used a normalised $153.9M). No other one-time item identified (a $1.6M software impairment in Q3 and a $0.3M acquisition cost are immaterial).
9. **Data gaps (not blocking):** 9M income-statement lines, 9M capex and 9M cash repurchases are not in the 8-K exhibits (the 10-Q was not fetched); TTM EPS 1 year ago is unavailable from vendors (Q4 FY24 EPS not sourced) so `cycle_peak` stays UNKNOWN — see §6. A MarketBeat/FactSet-grade dated FY2027 consensus was not obtainable.

## 4. Inputs

| Item | Value | Source / derivation |
|---|---|---|
| Live price | $146.26 | IBKR |
| Diluted shares | 50.8M | Shareholder letter dilution table |
| Market cap | $7,430,008,000 | 146.26 × 50.8M |
| Net debt / EV | −$1,155,391,000 / $6,274,617,000 | §3.5 |
| TTM revenue / GP / EBIT / NI | $1,182,296K / $860,837K / $146,122K / $145,737K | roll-forward of 08-06 TTM: −Q3 FY25 + Q3 FY26 |
| TTM FCF / SBC | $395,488K / $156,596K | §3 |
| FCF yield / SBC yield / after-SBC | 5.3228% / 2.1076% / 3.2152% | ÷ market cap |
| EV/EBIT | 42.94× | |
| Net margin / gross margin | 12.327% / 72.811% | |
| ROIC | 34.18% | NOPAT = 146,122 × (1 − 23.69%) = 111,502; invested capital = lease 84,216 + equity 1,481,597 − cash 1,239,607 = 326,206 (08-06 convention) |
| Net debt/EBITDA | −7.10× | −1,155,391 ÷ 162,648 |
| Revenue 3yr CAGR | 41.08% | FY2022→FY2025, unchanged (no new completed fiscal year) |
| (FCF − SBC)/NI | 163.92% | (395,488 − 156,596) ÷ 145,737 |
| Gross buyback yield | 1.1036% | §3.6 |
| 10Y | 5.07% | §header |

Hard disqualifiers: FCF/NI plain annual FY2023 870.9%, FY2024 298.5%, FY2025 87.0% (all ≥70%) — pass. Net debt/EBITDA −7.10× — pass. FCF positive 4+ years — pass. SBC/FCF = 39.6%, below the 100% disqualifier — pass.

## 5. Quality Score (script output, verbatim)

Command: `python -m scripts.scoring.quality_score --input duol_q.json` (inputs as in §4; moat evidence below is embedded in the output).

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((12.327/30)x100) = 41.09
ROIC_Component = clamp((34.18/30)x100) = 100.00
Profitability_Score = (41.09 + 100.00) / 2 = 70.55

**Margins (15%)**
GrossMargin_Score = clamp((72.811/80)x100) = 91.01

**Growth (20%)**
Growth_Score = clamp((41.082/25)x100) = 100.00
-10 structural growth deceleration evidence: Q3 FY2026 revenue +14% YoY (Q2 +18.3%, FY2025 +38.7%); FY2026 revenue guide +18%, Q4 guide +14% - DUOL Q3 FY2026 shareholder letter, SEC 8-K accession 0001628280-26-069474 (2026-11-03). Carried -10 modifier consistent with 07-04/08-06/09-01 sessions.
Growth_Score (final, clamped) = 90.00

**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - -7.104/4)) = 100.00

**Moat Signal (15%)**
| Signal | True | Evidence |
| market_share_stable_or_growing | True | Q3 FY2026: DAU 64.9M (+29% YoY, up from +23% in Q2), MAU 153.1M (+13%), paid subscribers 13.1M (+14%) - shareholder letter, SEC 8-K 2026-11-03 (company-reported, not third-party share data). |
| brand_premium | False | No cited pricing-power evidence found (unchanged). |
| network_effect | False | No documented two-sided-network mechanism (unchanged). |
| switching_costs | True | Streak/XP/League gamification lock-in (unchanged mechanism); paid subscribers +14% YoY to 13.1M in Q3 FY2026 shareholder letter. |
| scale_cost_advantage | True | Q3 FY2026 gross margin 72.9% vs 72.5% YoY (+40bp) while DAU +29% - shareholder letter. CAUTION: Q4 gross margin guided 72.0%, -90bp sequentially, from expanded AI-feature rollout. |
Moat_Score = (3/5) x 100 = 60.00

**FCF Quality (10%)**
FCFQuality_Score = clamp(((1.6392 - 0.40)/0.60)x100) = 100.00  [ratio = (FCF - SBC)/NI]

**Quality Score - Final**
Quality Score = (70.55x0.25) + (91.01x0.15) + (90.00x0.20) + (100.00x0.15) + (60.00x0.15) + (100.00x0.10)
= 83.288 -> rounds to 83.3

# Quality Score = 83.3 - PASSES the 80.0+ gate
```

**Quality Score = 83.3, clears the 80.0+ gate** (08-06: 83.2). No Quality Watch escalation. Moves under the new SBC-as-a-cost method: FCF Quality sub-score uses (FCF − SBC)/NI = 163.9% (saturated at 100). The tam-expansion flag stays False (no cited source). **Sensitivity:** if the scale-cost-advantage signal is judged False (Q4 gross margin guide is down 90bp on AI-feature costs), Moat drops to 40.0 and Quality to **80.3** — still passes the gate, but with only 0.3 points of headroom. Worth watching next quarter.

## 6. Valuation Score (script output, verbatim)

Command: `python -m scripts.scoring.valuation_score --input duol_v.json`. Judgment inputs: Bull 40× / Bear 18× EV/EBIT ladder on TTM EBIT and net debt (same multiples as 08-06/09-01; Base = today's actual multiple, which equals the live price by construction); catalyst window 2 years (Rule 10 default); intrinsic growth 8% (unchanged judgment; FCF has been flat YoY this quarter, FY2026 revenue guide +18%, bookings +12%); no dividend; gross buyback yield 1.1036%. Bull FV = (40 × 146,122 + 1,155,391) ÷ 50.8M = $137.80; Bear FV = (18 × 146,122 + 1,155,391) ÷ 50.8M = $74.52.

```
## Valuation Score

**FCF Yield (40%)**
FCF yield after SBC = 5.3228% - 2.1076% (SBC yield) = 3.2152%
FCF_Score = clamp(100x(1 - 3.2152/10)) = 67.848

**EV/EBIT**
EV/EBIT_Score = clamp((42.941 - 12)/23 x 100) = 100.000

**Forward PE**
No 5yr PE history available (no-history fallback) -> FwdPE_Score = 50.0 (neutral, flagged)

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/44.6 x 100 = 2.2422%
Spread = EY - 10Y (5.07%) = -2.8278pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.07% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x137.8 + 0.50x146.26 + 0.25x74.52 = 126.2100
Gap Upside % = (126.2100/146.26) - 1 = -13.7085%
Annualized gap = -13.7085% / 2.0yr = -6.8542%/yr
E = -6.8542 (annualized gap) + 8.0 (intrinsic growth) + 1.1036 (shareholder yield: 0.0 div + 1.1036 buyback) = 2.2494%/yr
0 <= E (2.2494%) < H -> M = 5 x (10.0-2.2494)/10.0 = 3.8753
Upside/Downside Modifier (bounded [-15, +15]) = 3.8753

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 77.139

**Final Valuation Score**
Final Score = Raw (77.139) + Rate Modifier (+15) + Upside/Downside Modifier (+3.875)
= 96.015 -> rounds to 96.0

# Valuation Score = 96.0
```

**Valuation Score = 96.0** (standalone: "Trim or exit" band; 09-01: 85.1). Drivers: FCF yield after SBC is only 3.2% (new methodology; the 09-01 score used the pre-SBC yield 5.0% → sub-score 49.9, now 67.8), EV/EBIT stays capped at 100.0, and the Rate Gate rose from +10 to +15 as the 10Y moved from 4.75% to 5.07%.

**Advisory flags (no score effect):** SBC/FCF 39.6% (above the 30% watch line); FCF yield after SBC 3.47% per script (3.22% on my market cap).

```
python -m scripts.scoring.flags_common --forward-pe 44.6 --eps-growth 17.1
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  multiple_ceiling       MULTIPLE_CEILING       forward PE 44.6 >= 30† with EPS growth 17.1% < 30%† — price needs growth the estimates don't show
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```

How each was handled:
- **MULTIPLE_CEILING (raised):** consistent with the score — the stock needs growth beyond the 17% consensus EPS step (2.80 → 3.28). It is already reflected in the Hold/valuation read; informs the no-add decision. EPS growth input is my own derivation from two vendor figures (FY2026 $2.80, FY2027 $3.28, the latter undated).
- **cycle_peak (UNKNOWN, data gap):** TTM GAAP EPS now is $2.97 (0.88+0.89+0.66+0.54), and the year-ago TTM contained the one-off $5.95 quarter, so TTM EPS is *falling*, not at a cycle peak; the formal flag cannot be computed because Q4 FY2024 EPS was not sourced.
- **value_trap_candidate (UNKNOWN):** requires forward PE ≤15; ours is 44.6× (18.96× on Yahoo's field) — cannot be raised either way.

**Sensitivity of the Upside/Downside Modifier's judgment inputs** (all other inputs fixed):

| Variation | E | M | Valuation | Composite | Band |
|---|---|---|---|---|---|
| Primary (8% growth, 2yr, 1.10% buyback) | +2.25% | +3.875 | 96.0 | **56.4** | Hold |
| Growth 6% | +0.25% | +4.875 | 97.0 | 56.9 | Hold |
| Growth 10% | +4.25% | +2.875 | 95.0 | 55.9 | Hold |
| Catalyst window 1.5yr | −0.04% | +5.035 | 97.2 | 57.0 | Hold |
| Buyback yield 0 | +1.15% | +4.427 | 96.6 | 56.7 | Hold |
| Moat scale-advantage False (Quality 80.3) | n/a | n/a | 96.0 | ≈57.9 | Hold |

Every variation stays in the 50.0–69.9 Hold band; none approaches 70.0 (Trim) or 49.9 (Cheap).

## 7. Composite Score (script output, verbatim)

```
python -m scripts.scoring.composite_score --set quality_score=83.3 --set valuation_score=96.0
Composite Score = 0.50x(100 - 83.3) + 0.50x96.0 = 56.350 -> rounds to 56.4
# Composite Score = 56.4  (Quality Score 83.3, Valuation Score 96.0)
```

**Composite 56.4 = Hold band (50.0–69.9)**, up from 51.0 on 09-01, same band. Quality is flat; the worsening is entirely valuation (SBC-adjusted FCF yield, higher rate gate).

## 8. Action Recommendation

**HOLD — no add, no trim.**

- *No add:* Composite is in the Hold band — no margin of safety, watchlist only. Position (≥10.83% of the framework account) is also well above the 3–5% target for any Cheap read.
- *No trim:* the Composite governs once a Quality Score exists, and it sits 13.6 points below the 70.0 Trim threshold, robust across the sensitivity table. The standalone Valuation Score (96.0) is in the Trim/Exit band, but it is superseded by Composite per the framework; the user should note the sizeable gap between the two reads.
- *No exit trigger:* no fundamental deterioration under Rule 9 — no guidance cut (FY revenue guide *raised* $1.21B → $1.22B), no management change, no M&A, no dilutive raise, net-cash balance sheet, buyback running. Soft spots to monitor: GAAP operating income −31% YoY (partly the $11.4M bonus accrual and Q3→Q4 expense timing), Q4 gross margin guide −90bp sequentially, and the 0.3-point Quality headroom in the moat sensitivity.
- *No order setup:* `scripts.scoring.order_setup` only runs for governing scores below 50.0 (the bands with a defined margin of safety); Composite 56.4 gets none by design, so no buy price, stop or R/R was computed.
- *Fair value reference:* PW Fair Value (EV/EBIT ladder) $126.21 vs live $146.26 (−13.7%). DCF Method A was not recomputed this run (no order is contemplated; the 09-01 log's DCF used a 9.09% WACC that is now stale given the higher 10Y).

## 9. Next Review Trigger

Q4 FY2026 earnings (expected ~2026-02-24 per Chartmill; check the company's date announcement). Specific checks: Q4 revenue vs the $322M guide (+14%) and bookings vs $382M (+13%); Q4 DAU growth "similar to Q3" (~29%) and whether it clears the 25% bonus threshold; Q4 gross margin vs the 72.0% guide (moat-signal check); GAAP operating margin recovery; diluted share count vs the 50.8M estimate and buyback pace. Standard triggers: guidance cut, management change, M&A, or a >15% unexplained price move from $146.26.

---

## Glossary

- **Adjusted EBITDA**: EBITDA with stock compensation and some other items added back — a company-defined, non-GAAP profit measure.
- **Bookings**: Value of subscriptions sold in a period; revenue recognises it over time, so bookings lead revenue.
- **Composite Score**: This framework's blend, `0.50 × (100 − Quality) + 0.50 × Valuation`; governs the action once both exist.
- **DAU / MAU**: Daily / monthly active users.
- **DCF (Discounted Cash Flow)**: Valuation by discounting projected cash flows to today.
- **Dilution**: New shares issued (e.g. employee stock awards) shrink existing holders' ownership share.
- **EBIT / EBITDA**: Earnings before interest and taxes / also before depreciation and amortisation.
- **EV/EBIT**: Enterprise value divided by EBIT — a debt-neutral price multiple; lower is cheaper.
- **FCF (Free Cash Flow)**: Operating cash flow minus capital spending.
- **FCF Yield**: FCF ÷ market cap; this framework deducts stock compensation (SBC) from it.
- **Forward PE**: Price ÷ next fiscal year's expected earnings per share.
- **GAAP**: Standard US accounting rules; "non-GAAP" figures exclude items like stock pay.
- **Hold band**: Composite 50.0–69.9 — no add, no trim.
- **MULTIPLE_CEILING**: Advisory flag: forward PE ≥30 with EPS growth <30% — an expensive stock without growth to justify it.
- **PW (Probability-Weighted) Fair Value**: 25% bull + 50% base + 25% bear case values.
- **Quality Score**: This framework's 0–100 quality grade; 80.0+ needed to pass the gate.
- **Rate Environment Gate**: Adds points to the valuation score when bond yields make stocks relatively less attractive.
- **Rule 0 / Rule 9**: Always fetch a live price first / the list of events (earnings, big price moves, management change) that force a re-score.
- **SBC (Stock-Based Compensation)**: Employee pay in shares; treated as a real cost in this framework since 2026-10-12.
- **TTM**: Trailing twelve months.
- **Valuation Score**: This framework's 0–100 cheapness score; lower = cheaper.
