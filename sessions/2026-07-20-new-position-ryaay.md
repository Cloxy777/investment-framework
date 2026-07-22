# NEW POSITION — RYAAY (Ryanair Holdings plc, Nasdaq ADR) — 2026-07-20

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, documented re-review trigger)
**Date:** 20 Jul 2026 (Monday)
**10Y US Treasury Yield:** ~4.56% (context only — most recent widely-reported level as of 2026-07-17; not used this session, since it stops at the Quality Gate, §3, before the Rate Environment Gate would apply)
**Current RYAAY portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [watchlist/not-in-portfolio/RYAAY/RYAAY-2026-07-19.md](../watchlist/not-in-portfolio/RYAAY/RYAAY-2026-07-19.md) — Phase 01 FAIL, Quality Score 65.1, session [sessions/2026-07-19-new-position-ryaay.md](2026-07-19-new-position-ryaay.md)
**Sector:** Industrials — Airlines (European ultra-low-cost carrier; parent of Ryanair DAC, Buzz, Lauda Europe, Malta Air, Ryanair UK)
**First-use jargon decode:** see closing Glossary (§8)

---

## 0. Why this session exists — trigger source

Channel **bolshegold** (Telegram) posted twice this morning UTC 2026-07-20: post #9797 (07:44 UTC) referenced Ryanair Q1 results figures, and the current top post #9798 (07:47 UTC — the post that moved the watch-file marker) reads (Russian): *"Хм, интересный слайд. Райнайр продолжает доминировать среди лоукостеров ЕС и продолжает снижать издержки на масштабе"* — "Hmm, interesting slide. Ryanair continues to dominate among EU low-cost carriers and continues to reduce costs at scale." Per Rule 0 and this repo's standing convention, **the post text is not used as financial data** — it is a trigger only.

The reason this is a *legitimate* trigger (not just routine "last checked, no change"): the 2026-07-19 watchlist entry's documented "Next review trigger" condition (a) is **"RYAAY's Q1 FY2027 trading update, confirmed scheduled for Monday 20 July 2026"** — i.e. today. Ryanair did in fact report Q1 FY2027 results this morning (20 July 2026, before UK/Irish market open), so this is a genuine Rule 9 fundamental-event trigger, independent of the Telegram post's own content. This session is a fresh, independent re-evaluation — full Phase 01 recompute from primary-sourced data, not a rubber-stamp of the prior 65.1.

---

## 1. Live Price (Rule 0)

Contract re-confirmed via `search_contracts("RYAAY")`: contract_id **210918190**, exchange **NASDAQ**, description "RYANAIR HOLDINGS PLC-SP ADR" (same instrument as the 2026-07-19 session; the two CORPACT dividend-record instruments again excluded as non-tradable).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$60.20** | IBKR `get_price_snapshot`, `last` field, contract_id 210918190 (NASDAQ), `is_close: false` — genuine live intraday trade (Monday, US market open) |
| Change vs. prior close | **−$2.37 (−3.79%)** | IBKR `get_price_snapshot` `change` field |
| Prior close | $62.57 | IBKR `get_price_snapshot` `prior-close` field |
| Bid/Ask | $59.44 / $70.00 | IBKR `get_price_snapshot` `bid_ask` field (wide, thin-book spread — flagged, not smoothed over) |
| 52-week high | $73.76 | IBKR `misc_statistics` `high_52w` |
| 52-week low | $53.14 | IBKR `misc_statistics` `low_52w` |
| 13-week high | $67.59 | IBKR `misc_statistics` `high_13w` |
| 26-week high | $72.56 | IBKR `misc_statistics` `high_26w` |
| Dividend yield | 1.58% | IBKR `get_price_snapshot` `dividend_yield` field |
| US 10Y Treasury yield | ~4.56% | Widely-reported level, 2026-07-17 (context only — not used this session, see header) |

$60.20 is down 3.79% intraday, consistent with market reaction to the weaker Q1 FY2027 profit figures reported this morning (see §2) — a **documented fundamental trigger** (Q1 results), not an unexplained price move, so no Rule 9 "unexplained >15% move" flag applies (and the move is well under 15% regardless). This price is used for reference throughout; no order-setup arithmetic is performed below, since the Quality Gate fails again (§3).

---

## 2. Data Gathered — Q1 FY2027 Primary Source

### 2.1 Source

Ryanair furnished its **Q1 FY2027 (quarter ended June 30, 2026) unaudited condensed consolidated interim financial statements** via its own investor-relations results centre (`investor.ryanair.com/results-centre/q1-fy27/`, PDF "Q1-FY27-Ryanair-Results.pdf"), released this morning, 20 July 2026. This document contains the full income statement, balance sheet, cash-flow statement, and MD&A in the same company-labeled IFRS line items as the FY2026 20-F/6-K used in the 2026-07-19 session — same primary-source discipline. **As of this session, the equivalent Form 6-K had not yet appeared on SEC EDGAR** (checked: most recent 6-K on file is dated 2026-07-13, accession 0001654954-26-006616) — normal SEC-indexing lag behind a same-day international press release, not a Ryanair disclosure gap. The interim financial statements state the Audit Committee approved them on **17 July 2026**, and the release itself is dated **20 July 2026** — both facts corroborate this is genuine, board-approved, primary-sourced data, not a leak or rumor. All figures in € millions unless noted.

### 2.2 Q1 FY2027 income statement (quarter ended June 30, 2026, vs. June 30, 2025)

| Item (€M) | Q1 FY2026 (Jun '25) | Q1 FY2027 (Jun '26) | Change |
|---|---|---|---|
| Scheduled revenues | 2,943.8 | 2,914.5 | −1% |
| Ancillary revenues | 1,393.8 | 1,469.6 | +5% |
| **Total revenue** | **4,337.6** | **4,384.1** | **+1%** |
| Fuel and oil | 1,456.8 | 1,689.3 | +16% |
| Airport and handling charges | 495.1 | 519.9 | +5% |
| Staff costs | 461.7 | 476.3 | +3% |
| Depreciation | 343.3 | 417.1 | +21% |
| Route charges | 356.3 | 386.1 | +8% |
| Marketing, distribution and other | 221.2 | 203.0 | −8% |
| Maintenance, materials and repairs | 89.9 | 117.0 | +30% |
| **Total operating expenses** | **3,424.3** | **3,808.7** | **+11%** |
| **Operating profit (EBIT)** | **913.3** | **575.4** | **−37%** |
| Net finance and other income | 48.7 | 14.9 | |
| Foreign exchange gain/(loss) | (31.8) | 2.6 | |
| Profit before tax | 930.2 | 592.9 | |
| Tax expense | (110.3) | (55.2) | |
| **Profit for the quarter (Net Income)** | **819.9** | **537.7** | **−34%** |
| Basic EPS (€) | 0.7717 | 0.5164 | |
| Weighted avg. basic shares (M) | 1,062.5 | 1,041.3 | |

Q1 FY2027 net income fell 34% YoY — driven by the price of Ryanair's unhedged (20%) jet fuel more than doubling during the quarter (to ~$150/bbl, per the MD&A) amid the Middle East conflict, plus a 6% average-fare decline (traffic still grew 6% to 61.3M passengers — a volume-for-price trade, the opposite direction from FY2026's fare increase). Source: Q1 FY27 Ryanair Results, pp.4–5 ("Condensed Consolidated Interim Income Statement for the Quarter Ended June 30, 2026").

### 2.3 Balance sheet, June 30, 2026 vs. March 31, 2026

| Item (€M) | Jun 30, 2026 | Mar 31, 2026 |
|---|---|---|
| Cash and cash equivalents | 2,483.8 | 2,733.4 |
| Financial assets: cash > 3 months | 319.7 | 812.4 |
| Restricted cash | 31.2 | 31.2 |
| Current maturities of debt | 0.0 | 1,198.8 |
| Non-current maturities of debt | 38.3 | 147.8 |
| **Total debt** | **38.3** | **1,346.6** |
| Total shareholders' equity | 9,480.5 | 10,101.4 |
| Total assets | 18,163.3 | 19,747.7 |

Total debt fell from €1,346.6M to just **€38.3M** — the final €1.2BN Eurobond was repaid in May 2026 (confirmed both sessions), leaving Ryanair with only a residual €38.3M of non-current debt. Shareholders' equity declined €0.6BN quarter-over-quarter, which the company's own MD&A attributes to a €1.0BN IFRS hedge-accounting *reserve* movement (a mark-to-market swing in the fuel/FX hedging book run through other comprehensive income, not operating performance) partially offset by the €0.5BN net profit — flagged for completeness, not itself scored. Source: Q1 FY27 Ryanair Results, p.3 ("Condensed Consolidated Interim Balance Sheet as at June 30, 2026").

### 2.4 Cash flow, quarter ended June 30, 2026 vs. June 30, 2025

| Item (€M) | Q1 FY2026 | Q1 FY2027 |
|---|---|---|
| Net cash from operating activities | 1,458.2 | 1,203.4 |
| CapEx — purchase of PP&E | 622.8 | 474.7 |
| **FCF** | **835.4** | **728.7** |

Source: Q1 FY27 Ryanair Results, p.6 ("Condensed Consolidated Interim Statement of Cash Flows").

### 2.5 TTM reconstruction (quarter ended June 30, 2026)

Ryanair is a foreign private issuer with no `yfinance`-style automated TTM support and no quarterly 10-Q equivalent; the framework's standard TTM-reconstruction convention (add the new quarter, subtract the same quarter a year ago — as used for AAPL in this framework's 10-Q sessions) is applied manually here using the FY2026 annual figures (year ended March 31, 2026, from the 2026-07-19 session, §2.2–§2.4 of that file) and the Q1 FY2026 / Q1 FY2027 figures above:

```
TTM (Jul 2025 – Jun 2026) = FY2026 Annual − Q1 FY2026 + Q1 FY2027
```

| Item (€M) | FY2026 Annual | − Q1 FY2026 | + Q1 FY2027 | = TTM (to Jun 2026) |
|---|---|---|---|---|
| Total revenue | 15,544.3 | 4,337.6 | 4,384.1 | **15,590.8** |
| Fuel and oil | 5,418.6 | 1,456.8 | 1,689.3 | 5,651.1 |
| Airport and handling | 1,762.3 | 495.1 | 519.9 | 1,787.1 |
| Staff costs | 1,856.5 | 461.7 | 476.3 | 1,871.1 |
| Depreciation | 1,373.4 | 343.3 | 417.1 | 1,447.2 |
| Route charges | 1,318.2 | 356.3 | 386.1 | 1,348.0 |
| Marketing/distribution/other | 803.5 | 221.2 | 203.0 | 785.3 |
| Maintenance/materials/repairs | 552.6 | 89.9 | 117.0 | 579.7 |
| Exceptional charge (AGCM, one-off, FY26 only) | 85.0 | 0.0 | 0.0 | 85.0 |
| **Total operating expenses** | 13,170.1 | 3,424.3 | 3,808.7 | **13,554.5** |
| **EBIT** | 2,374.2 | 913.3 | 575.4 | **2,036.3** |
| Net finance and other income | 80.0 | 48.7 | 14.9 | 46.2 |
| FX gain/(loss) | (30.9) | (31.8) | 2.6 | 3.5 |
| Profit before tax | 2,423.3 | 930.2 | 592.9 | 2,086.0 |
| Tax expense | (249.6) | (110.3) | (55.2) | (194.5) |
| **Net income** | 2,173.7 | 819.9 | 537.7 | **1,891.5** |
| Net cash from operating activities | 3,694.9 | 1,458.2 | 1,203.4 | 3,440.1 |
| CapEx | 1,892.4 | 622.8 | 474.7 | 1,744.3 |
| **FCF** | 1,802.5 | 835.4 | 728.7 | **1,695.8** |

Cross-checked: EBIT (13,554.5 opex sum matches the sum of individual TTM cost lines); PBT − Tax = 2,086.0 − 194.5 = 1,891.5 = Net income (matches). TTM revenue (€15,590.8M) is only +0.3% above the FY2026 annual figure (€15,544.3M) — Q1 FY27's +1% revenue growth almost exactly offset Q1 FY26's contribution being removed, consistent with the MD&A's own framing of a "broadly flat" underlying trajectory this quarter. TTM net income (€1,891.5M) is **13% below** the FY2026 annual figure (€2,173.7M) — the weaker Q1 FY27 quarter pulls the trailing-twelve-month profitability picture down from the FY2026 year-end level, as expected given the reported 34% YoY quarterly profit decline.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, recomputed on TTM-to-Jun-2026 data)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without documented growth-capex explanation | FY2024: 39.96% (single year) · FY2025: 115.61% · FY2026: 82.92% · **TTM-Jun2026: 89.65%** — no 2+ consecutive sub-70% run | disqualify if 2+ *consecutive* years sub-70% | ✅ **PASS** |
| Net Debt/EBITDA over threshold (2.5× standard) | **TTM-Jun2026: −0.702×** (net cash — even more net-cash than FY2026's −0.370×, since total debt fell from €1,346.6M to €38.3M) | disqualify if >2.5× | ✅ **PASS**, by a wider margin than the prior session |
| FCF-positive 3+ consecutive years | FY2024 €766.0M · FY2025 €1,863.2M · FY2026 €1,802.5M · **TTM-Jun2026 €1,695.8M** — all positive | disqualify if not | ✅ PASS |

**No hard disqualifier fires** — if anything, the balance sheet and FCF-quality picture is *stronger* this session (nearly debt-free at €38.3M, vs. €1,346.6M three months ago) than 2026-07-19's.

### 3.2 Quality Score — full computation (TTM to June 30, 2026)

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 1,891.5 / 15,590.8 = 12.132%
  NetMargin_Component = clamp((12.132/30)×100, 0, 100) = 40.44

  Effective tax rate (TTM) = 194.5 / 2,086.0 = 9.324%
  NOPAT = EBIT × (1 − eff. tax rate) = 2,036.3 × (1 − 0.09324) = €1,846.44M
  Invested Capital = Total Debt + Equity − Cash = 38.3 + 9,480.5 − 2,483.8 = €7,035.0M
  ROIC = 1,846.44 / 7,035.0 = 26.25%
  ROIC_Component = clamp((26.25/30)×100, 0, 100) = 87.49

  Profitability_Score = (40.44 + 87.49) / 2 = 63.97   (no FCF-positivity cap — TTM + 3 fiscal years all positive)

MARGINS (15% weight):
  Same construction as 2026-07-19 (Fuel and oil + Airport and handling charges + Route charges as the
  "direct flight-operating cost" analog — no GAAP gross-profit line exists for an airline):

  Gross Margin (TTM) = (15,590.8 − (5,651.1 + 1,787.1 + 1,348.0)) / 15,590.8
                      = (15,590.8 − 8,786.2) / 15,590.8 = 43.645%
  GrossMargin_Score = clamp((43.645/80)×100, 0, 100) = 54.56

  3yr trend check (same construction): FY2024 43.08% → FY2025 42.14% → TTM-Jun2026 43.65% — still
  non-monotonic and already above the 40% threshold the +10 "structural expansion while below 40%" bonus
  is gated on — not eligible either way, same conclusion as 2026-07-19.

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2023→FY2026, unchanged from 2026-07-19 — FY2027 has not yet closed as a full fiscal
  year, so no new complete-year endpoint exists to recompute this input against; using a TTM-to-TTM window
  would require Q1 FY2023 data not sourced this session, and is not needed to change the gate conclusion —
  see §3.3 sensitivity note):
  Growth_Score (raw) = clamp((12.99/25)×100, 0, 100) = 51.97
  TAM-expansion modifier: +10 — REAFFIRMED this session. The Q1 FY27 release repeats the identical, still-
  firm 300-aircraft Boeing 737 MAX-10 order (150 firm + 150 options, delivery 2027–2034) and the same
  208.4m→300m+ passengers-by-FY34 target, adding that Boeing "continues to expect MAX-10 certification in
  late summer 2026" and confirms "first 15 MAX-10s on time in Spring 2027" — if anything, incremental
  confirmatory evidence, not a change, so the modifier basis stands unchanged.
  Growth_Score = clamp(51.97 + 10, 0, 100) = 61.97

  No deceleration modifier — TTM revenue (€15,590.8M) is still (marginally) above the FY2026 annual figure
  (€15,544.3M); Q1 FY27's own revenue still grew +1% YoY despite the fare decline (traffic +6% more than
  offsetting the 6% average-fare cut) — not evidence of structural deceleration.

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM) = −0.702× (net cash — improved from FY2026's −0.370×)
  BalanceSheet_Score = clamp(100×(1 − (−0.702)/4), 0, 100) = clamp(117.55, 0, 100) = 100.0

MOAT SIGNAL (15% weight) — re-verified against the Q1 FY27 release, no signal count changed:
  Market share stable/growing — TRUE (unchanged; OAG July 2026 data, same as 2026-07-19, already dated to
    this period).
  Brand premium — FALSE, and the Q1 FY27 data further disconfirms rather than newly supports this signal:
    Q1 FY27 average fares FELL 6% YoY, and the company's own MD&A describes this as fares requiring
    "stimulation" amid Middle East-conflict-driven demand softness — i.e. Ryanair cutting price to defend
    volume, the textbook opposite of durable brand-premium pricing power, and fully consistent with the
    "load-active/yield-passive" strategy already cited as the reason this signal wasn't credited in the
    2026-07-19 session. Not credited.
  Network effect — FALSE (unchanged; no mechanism exists for this business model).
  Switching costs — FALSE (unchanged; no loyalty-lock-in mechanism).
  Scale cost advantage — TRUE, and reaffirmed with fresh evidence: FY27 fuel hedging confirmed 80% at
    ~$67/bbl (unchanged), and the Group "recently extended fuel hedges (on price dips) into FY28," now 15%
    hedged at ~$85/bbl — continued, active extension of the same structural cost-hedging advantage cited
    previously, now with a second forward year locked in. Credited.

  Moat_Score = (2/5) × 100 = 40.0   (unchanged)

FCF QUALITY (10% weight):
  FCF/NI (TTM) = 1,695.8 / 1,891.5 = 89.65%
  FCFQuality_Score = clamp(((0.8965 − 0.40)/0.60)×100, 0, 100) = clamp(82.76, 0, 100) = 82.76

QUALITY SCORE = 63.97×0.25 + 54.56×0.15 + 61.97×0.20 + 100.0×0.15 + 40.0×0.15 + 82.76×0.10
             = 15.9925 + 8.184 + 12.394 + 15.000 + 6.000 + 8.276
             = 65.846 → rounds to 65.8
```

**Result: 65.8 / 100.0 — still fails the 80.0+ gate**, up marginally (+0.7) from the 2026-07-19 session's 65.1. The move is small and net-positive (stronger balance sheet, better FCF conversion) but almost entirely offset by weaker TTM profitability (Q1 FY27's 34% profit decline pulling the trailing-twelve-month Net Margin and ROIC down from the FY2026 year-end level) and a slightly thinner Margins reading.

### 3.3 Robustness check (sensitivity, not a point estimate)

Using the same deliberately generous, largely non-defensible combination as the 2026-07-19 session (Margins using "Fuel and oil" alone as the cost-of-revenue analog; Moat credited a full, unsupported 5/5):

```
Generous Gross Margin (TTM) = (15,590.8 − 5,651.1) / 15,590.8 = 63.76%  → GrossMargin_Score = 79.69

63.97×0.25 + 79.69×0.15 + 61.97×0.20 + 100.0×0.15 + 100.0×0.15 + 82.76×0.10
= 15.9925 + 11.9535 + 12.394 + 15.000 + 15.000 + 8.276 = 78.615 → rounds to 78.6
```

**Still below the 80.0 gate** even under this generous reading (78.6, vs. 77.8 in the 2026-07-19 session) — the higher FCF Quality sub-score (fresh TTM data) nudges the ceiling up slightly, but it remains short of 80.0 by 1.4 points, reached only by crediting Moat signals (Brand premium, Network effect, Switching costs) this session again found **no citable evidence** for — and this quarter's data (fares falling 6%) argues *against* Brand premium more directly than before, not for it.

**Sensitivity note on the Growth input (§3.2):** even a hypothetically much higher/lower Growth_Score swings the total by at most ±4.0 points (20% weight × up to 20-point swing on a 0–100 scale, since Growth_Score is already mid-range) — nowhere near enough to bridge the ~14-point gap to 80.0 on its own. Recomputing the 3yr CAGR on a strict TTM-to-TTM basis (which would require sourcing Q1 FY2023 data not pulled this session) would not change the gate outcome, so was not pursued further, consistent with not inventing data that isn't decision-relevant.

### 3.4 Gate result

**Quality Score = 65.8 / 100.0 — FAILS the 80.0+ gate**, essentially unchanged from the 2026-07-19 session's 65.1 (a genuinely fresh TTM window, incorporating today's Q1 FY2027 results, moves the score by less than 1 point). No hard disqualifier independently fires (§3.1 — Ryanair is in fact in a *stronger* net-cash position this quarter, nearly debt-free at €38.3M total debt). Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md): **stop here — do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or fair-value/order-setup work.**

---

## 4. Qualitative Notes

1. **This was a genuine, substantive re-evaluation, not a rubber-stamp.** Today's Q1 FY2027 release was a real, material data point (a documented 34% YoY quarterly profit decline, driven by unhedged jet-fuel prices spiking amid the Middle East conflict, and a 6% average-fare cut) — the framework's own Rule 9 fundamental-event trigger fired legitimately, independent of the Telegram post's own wording. The recomputation shows the framework's conclusion is robust to this new information, not merely repeated from memory.
2. **The balance sheet keeps getting stronger, not weaker, even as profitability softened this quarter.** Total debt fell from €1,346.6M (Mar 2026) to €38.3M (Jun 2026) after the final bond repayment; Net Debt/EBITDA improved from −0.370× to −0.702×. The Quality Gate failure remains driven by the same structural factors flagged 2026-07-19 — a Moat Signal checklist calibrated more naturally to software/consumer-brand moats than to a low-cost point-to-point airline's cost-based moat, and a Profitability formula whose 30%-cap scale doesn't flatter even industry-leading airline margins — not by any balance-sheet or cash-quality concern.
3. **This quarter's fare decline (−6% YoY) further undercuts, rather than newly supports, a "Brand premium" Moat Signal credit.** The 2026-07-19 session already declined to credit Brand premium despite FY26's +10% fare increase, reasoning that Ryanair's own "load-active/yield-passive" strategy treats fares as a market-clearing residual, not a durable pricing lever. Q1 FY27's swing the *other* direction (fares cut 6% to "stimulate" demand) is exactly the behavior that framing predicts, and reinforces rather than contradicts the prior session's judgment call.
4. **The Middle East conflict's fuel-price impact, flagged as context (not yet realized) in the 2026-07-19 session, has now shown up concretely in reported results** — the 20% unhedged portion of Q1 FY27 jet fuel more than doubled in price (to ~$150/bbl), the single largest driver of the quarter's operating-cost increase (+11% to €3.81BN) and profit decline. Ryanair's response — extending hedges further out (now 15% of FY28 locked at ~$85/bbl, on top of 80% of FY27 at ~$67/bbl) — is exactly the "widening cost advantage" behavior credited under Moat Signal "Scale cost advantage" in both sessions.
5. **No FY27 profit guidance was given** ("zero H2 visibility... too early for FY27 PAT guidance," per the CEO's own commentary) — consistent with Rule 9/the framework's standing view that management guidance is a trigger, not a scored input (see [valuation-scoring.md](../framework/valuation-scoring.md#why-forward-guidance-is-not-a-sub-score)); nothing here is treated as a scored figure.
6. **This session's Growth sub-score input (3yr Revenue CAGR) remains anchored to complete fiscal years** (FY2023→FY2026, 12.99%) rather than being rebuilt on a strict TTM-to-TTM basis, since FY2027 has not yet closed and sourcing a matching Q1 FY2023 data point wasn't needed to change the gate conclusion (§3.3) — flagged explicitly per "never invent or estimate financial data," rather than silently reusing the number without comment.

---

## 5. Recommendation

# **PASS — Quality Gate FAIL again (Quality Score 65.8 < 80.0). Do not enter. Continue watchlist-only.**

Today's Q1 FY2027 trading update — a genuine, documented Rule 9 trigger, not just a Telegram mention — was fully and independently re-evaluated with fresh primary-source data (a TTM reconstruction incorporating the new quarter). The result: **Quality Score 65.8, up only 0.7 points from the 2026-07-19 session's 65.1**, still failing the 80.0+ gate by roughly 14 points, and the generous robustness ceiling (78.6) still falls 1.4 points short. The balance sheet is if anything stronger this quarter (nearly debt-free); the gate failure remains driven by the same structural factors as before — a Moat Signal checklist poorly suited to a low-cost airline's cost-based (rather than brand-based) competitive advantage, and a Profitability formula scale that doesn't flatter even strong airline-level margins. **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed** — this session stops at the Quality Gate per the command specification. **No BUY/TRIM/EXIT action results from this session.**

---

## 6. Next Review Trigger

No routine re-check is scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of the following Rule 9-style fundamental triggers (carried forward from 2026-07-19, condition (a) now resolved by this session):

- **Q2 FY2027 trading update** (typically ~early November 2026) — will show whether the fare/fuel dynamics seen this quarter persist, worsen, or reverse, and gives a second data point on whether FY27's fare trajectory is a one-quarter dip or a trend.
- Any material change in the MAX-10 delivery schedule or the 300m-passengers-by-FY34 growth target (reaffirmed, unchanged, this session).
- Resolution (either direction) of the Italian AGCM antitrust appeal (€256M fine, €85M provisioned) — not addressed in the Q1 FY27 release; still pending as far as this session found.
- A management change (CEO Michael O'Leary's contract extension status was not addressed in the Q1 FY27 release; last reported "almost concluded" in the FY26 release), material M&A, a macro/rate shift, or a >15% unexplained price move (today's −3.79% move is explained by the Q1 results, not unexplained).
- **FY2027 fiscal year-end close** (~May 2027 report) — the point at which a full new fiscal year replaces FY2023 in the 3yr Revenue CAGR window (§3.2, §4 note 6), giving the first genuinely new-endpoint Growth sub-score recomputation.

Absent any of the above, a future Telegram mention of RYAAY should be logged as "last checked, no change" per the watchlist convention.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Data Gaps Flagged

1. **No SEC-filed Form 6-K for Q1 FY2027 existed as of this session** (checked 2026-07-20; most recent 6-K on EDGAR is dated 2026-07-13) — worked around by using the company's own investor-relations-published, board-approved (Audit Committee sign-off 17 July 2026) interim financial statements PDF directly, the same primary-source standard the framework already applies to Ryanair's other filings. Non-blocking; the SEC filing, once it appears, is expected to reproduce these same figures verbatim (as it has for prior quarters).
2. **Q1 FY2023 quarterly data was not sourced**, so the Growth sub-score's 3yr Revenue CAGR remains computed on a complete-fiscal-year (FY2023→FY2026) rather than strict TTM-to-TTM basis — flagged in §3.2/§3.3/§4 note 6 as a deliberate scope decision (the gate outcome doesn't turn on this input), not a silent gap.
3. **No update was found on the Italian AGCM antitrust appeal or CEO O'Leary's contract-extension status** — neither was addressed in the Q1 FY27 release; both remain open per the 2026-07-19 session's framing, carried into §6's next-review triggers.

None of these gaps affect the Quality Gate conclusion (§3.4), which fails by a wide, robustness-checked margin (65.8 vs. 80.0, and 78.6 even under a generous reading).

---

## 8. Glossary

| Term | Meaning |
|---|---|
| **AGCM (Autorità Garante della Concorrenza e del Mercato)** | Italy's national competition/antitrust regulator — levied a €256M fine against Ryanair (under appeal, €85M provisioned); status unchanged/unaddressed this session. |
| **Ancillary revenue** | An airline's non-ticket revenue (baggage fees, priority boarding, reserved seats, etc.). Ryanair's Q1 FY27 ancillary revenue rose 5% to €1.47BN. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating profit, and a rough proxy for cash operating profit, respectively. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). RYAAY's TTM-to-June-2026 FCF/NI conversion is 89.65%. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. None fired for RYAAY this session (§3.1). |
| **IFRS (International Financial Reporting Standards)** | The accounting standard Ryanair uses for its audited/reviewed financial statements. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in this framework's ROIC calculation. |
| **"Load-active/yield-passive" strategy** | Ryanair's own stated capacity-management strategy: actively managing traffic volume/load factor, while treating average fare as a market-clearing residual — the reason this session again declines to credit Moat Signal "Brand premium," reinforced by Q1 FY27's 6% fare cut. |
| **MD&A (Management's Discussion and Analysis)** | The section of a company's results release where management explains, in its own words, what drove the reported numbers — used here as sourced qualitative context, never as a scored input in its own right. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — this framework's primary balance-sheet-risk gate. RYAAY's TTM-to-June-2026 figure is **−0.702×** (net cash), improved from FY2026's −0.370×. |
| **Net Margin** | Net Income ÷ Revenue. RYAAY's TTM-to-June-2026 Net Margin is 12.13%. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. RYAAY scored 65.8 this session (was 65.1 on 2026-07-19). |
| **ROIC** | Return on Invested Capital. RYAAY's TTM-to-June-2026 ROIC is 26.25%. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. Today's Q1 FY2027 trading update is this session's Rule 9 trigger. |
| **TAM (Total Addressable Market)** | The total revenue opportunity available to a business if it captured its entire relevant market. Ryanair's 300m-passengers-by-FY34 target was reaffirmed (unchanged) in the Q1 FY27 release. |
| **TTM (Trailing Twelve Months)** | The most recent 12 consecutive months of financial results, reconstructed here as FY2026 Annual − Q1 FY2026 + Q1 FY2027, since Ryanair (a foreign private issuer) has no standard quarterly 10-Q-equivalent trailing-figure data source. |

---

## 9. Sources

- Ryanair Holdings plc, "Q1 FY27 Ryanair Results" (investor.ryanair.com/wp-content/uploads/2026/07/Q1-FY27-Ryanair-Results.pdf) — unaudited condensed consolidated interim financial statements for the quarter ended June 30, 2026, released and Audit-Committee-approved 17–20 July 2026.
- SEC EDGAR — checked for a corresponding Form 6-K (`sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001038683&type=6-K`); not yet filed as of this session (most recent: 2026-07-13, accession 0001654954-26-006616).
- [sessions/2026-07-19-new-position-ryaay.md](2026-07-19-new-position-ryaay.md) — prior session, source of the FY2024–FY2026 annual figures used in the TTM reconstruction (§2.5) and the unchanged Growth/Moat evidence base.
- IBKR `search_contracts` / `get_price_snapshot` — live price, contract confirmation, 52-week statistics, dividend yield.
- Web search — Q1 FY2027 results confirmation and headline figures (cross-check against the primary PDF); approximate 10Y Treasury yield level (context only).
