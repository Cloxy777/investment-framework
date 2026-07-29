# NEW POSITION (Re-trigger) — MU (Micron Technology, Inc.) — 2026-07-29

**Task type:** NEW POSITION (re-opened — Telegram-scan trigger, Routine 6)
**Date:** 29 Jul 2026
**10Y US Treasury Yield:** ~4.62% (WebSearch, TradingEconomics/Investing.com, 2026-07-28 close — FRED `DGS10` direct pull timed out through this session's proxy, see §2.0 data-source note)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **for the record only, not applied — Quality Gate fails first, see §3**
**Current MU portfolio weight:** 0% — not currently held (confirmed against [holdings.md](../portfolio/holdings.md) and a live IBKR `get_account_positions` pull, which lists no MU position)
**Prior coverage:** [2026-06-20](2026-06-20-new-position-mu.md), [2026-06-22](2026-06-22-new-position-mu.md), [2026-06-24](2026-06-24-new-position-mu.md), [2026-07-08](2026-07-08-new-position-mu.md); watchlist [MU-2026-07-08.md](../watchlist/not-in-portfolio/MU/MU-2026-07-08.md) — Quality Gate FAIL (49.0/100), live price $902.74.
**Sector:** Memory semiconductors (DRAM, NAND, HBM). Classic boom-bust commodity-cycle hardware business.

---

## 0. Why this session exists — re-trigger source, and what it turned out to be

A Telegram post on **FinnInvestChannel** (post #3006, ~06:40 UTC 2026-07-29) claimed: *"Revenue: $54.6B vs. forecast $57.7B, below expectations by 5.4%. Operating profit: $41.6B vs. forecast $44.2B. DRAM rose ~30% per quarter, NAND rose 50%+."* Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only, and every number in it must be independently verified or discarded.

**Independent verification finds this claim is false as stated.** Micron has not reported any earnings since Q3 FY2026 (period end 2026-05-31, already reflected in the 2026-07-08 session). WebSearch of Micron's own investor-relations calendar and third-party earnings trackers (TipRanks, MarketBeat, SEC EDGAR) confirms Micron's **next earnings report is scheduled for 29 September 2026, after market close** — a full two months from today. There is no "actual vs. forecast" quarterly comparison to make yet, so the Telegram post's specific figures ($54.6B/$57.7B revenue, $41.6B/$44.2B operating profit) do not correspond to any real reported or previewed data point for MU. This is directly analogous to the 2026-07-08 session's finding (Telegram's claimed $888.00 price was inaccurate) and the 2026-06-24 session's finding (a prior Telegram figure was likewise unconfirmed) — a third consecutive instance of an inaccurate FinnInvestChannel post about this ticker.

**What actually happened, independently confirmed via WebSearch (StocksToTrade, Yahoo Finance, FXLeaders, TradingKey, Forbes, Motley Fool, Invezz, SemiAnalysis):** MU fell **−8.85%** in the regular session on 2026-07-28 (from $900.20 to $820.53) and is down further in pre-market trading this morning, as part of a broad memory-sector selloff. The proximate cause is **CXMT (ChangXin Memory Technologies)**, a Chinese DRAM manufacturer, whose Nasdaq/public debut surged ~465% and reignited "memory oversupply" fears — CXMT is ramping toward ~350,000 DRAM wafers/month by end-2026 (near Micron's own ~375,000/month), with a Nomura estimate putting its global DRAM share at ~18% by 2028 (from ~10% now), while Micron currently holds ~24% (behind Samsung 36% and SK Hynix 29%). Western Digital/SanDisk, Micron, and SK Hynix all fell together on the news, alongside broader AI-capex-sentiment caution following Samsung's preliminary results. **This is a real, well-documented, material industry event — a competitor capacity-expansion/competitive-threat development squarely within Rule 9's re-valuation triggers** (a peer's capacity ramp bearing directly on Micron's own pricing/oversupply risk) — even though it is not the specific "earnings miss" the Telegram post described. It independently justifies this session under the prior watchlist entry's documented "Next review trigger" language ("any guidance revision, capacity-expansion announcement, or management change").

**Note on Micron's own guidance (context only, not new information this session):** a WebSearch cross-check also surfaced that Micron's own Q3 FY2026 earnings call (late June 2026) **raised**, not cut, its Q4 FY2026 guidance — $50B revenue guided (vs. $42.5B analyst consensus at the time) and $30.73 EPS, on sold-out HBM capacity through 2027. This predates the 2026-07-08 session and is the opposite of a "miss" — it further undermines the Telegram post's specific narrative, though it is not itself new information driving today's price move (the CXMT-driven selloff is).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$808.27** | IBKR `get_price_snapshot`, contract_id **9939** (NASDAQ), last trade ts 2026-07-29 08:10:03 UTC, bid/ask $807.16/$807.60 |
| Cross-check — Yahoo Finance | Pre-market price $807.01, ts 2026-07-29 08:12:20 UTC (~2 min apart, $1.26 / 0.16% apart) | Yahoo `price` module, `preMarketPrice` |
| Session context | Pre-market (regular session opens 13:30 UTC today) | IBKR snapshot timing + Yahoo `currentTradingPeriod` |
| Yesterday's regular-session close (2026-07-28) | $820.53 (down −8.85% / −$79.67 from 2026-07-27's $900.20) | Yahoo `regularMarketPrice` / `regularMarketChangePercent`; cross-checked against IBKR's implied prior close ($808.27 + $12.26 change = $820.53 — exact match) |
| Today's change so far (pre-market vs. yesterday's close) | **−$12.26 / −1.49%** | IBKR `change`/`change_pct` |
| 52-week range | $103.22–$103.38 (low) – $1,255.00 (high, set ~2026-06-25) | IBKR `misc_statistics` ($103.224) cross-checked against Yahoo `fiftyTwoWeekLow` ($103.38) — both agree to within $0.16 |
| Change vs. 2026-07-08 reference ($902.74) | **−10.46%** | Computed |
| Change vs. 52-week high ($1,255.00, ~2026-06-25) | **−35.60%** | Computed |

**Two independent, near-simultaneous live feeds agree to within $1.26 (0.16%)** — a genuine, real-time pre-market quote. **$808.27 is used as the live price for all arithmetic below.**

---

## 2. Data Gathered

### 2.0 Data source note

Same `yfinance`-via-proxy TLS incompatibility flagged in the 2026-07-08 session (`curl_cffi` browser-TLS impersonation fails with `SSLError`/`curl: (35) Recv failure`). Worked around identically: plain `requests` (which the proxy handles natively) against Yahoo Finance's public JSON endpoints (`v8/finance/chart`, `v10/finance/quoteSummary`, `ws/fundamentals-timeseries`), using a session cookie + crumb obtained by visiting `finance.yahoo.com` first, then `query2.finance.yahoo.com/v1/test/getcrumb` — same underlying Yahoo Finance data `yfinance` itself wraps, same Rule-0 compliance (live, unaltered vendor data). A direct `FRED` (`fredgraph.csv`) pull for the 10Y Treasury yield timed out through the proxy (>120s, no response) — worked around via WebSearch for the same, publicly reported figure (TradingEconomics/Investing.com), flagged explicitly since the Rate Environment Gate is captured for the record only this session (gate fails at the Quality Score step first).

### 2.1 Critical finding: no new quarterly data since 2026-07-08 — independently confirmed

Pulled fresh quarterly fundamentals (`ws/fundamentals-timeseries`, types `quarterlyTotalRevenue`, `quarterlyEBIT`, `quarterlyEBITDA`, `quarterlyNetIncome`, `quarterlyFreeCashFlow`, `quarterlyOperatingCashFlow`, `quarterlyCapitalExpenditure`, `quarterlyGrossProfit`, `quarterlyTotalDebt`, `quarterlyCashAndCashEquivalents`, `quarterlyStockholdersEquity`) — the five most recent quarters returned are **byte-for-byte identical** to the 2026-07-08 session's figures (Q4FY25 through Q3FY26, most recent quarter end 2026-05-31). This independently corroborates §0's finding: Micron has not reported since Q3 FY2026, consistent with the confirmed 29 Sep 2026 next-earnings date.

| Quarter (end date) | Revenue | Gross Profit | EBIT | EBITDA | Net Income | OCF | CapEx | FCF |
|---|---|---|---|---|---|---|---|---|
| 2025-08-31 (Q4 FY25) | $11.315B | $5.054B | $3.755B | $5.904B | $3.201B | $5.730B | −$5.658B | $0.072B |
| 2025-11-30 (Q1 FY26) | $13.643B | $7.646B | $6.135B | $8.347B | $5.240B | $8.411B | −$5.389B | $3.022B |
| 2026-02-28 (Q2 FY26) | $23.860B | $17.755B | $16.192B | $18.478B | $13.785B | $11.903B | −$6.387B | $5.516B |
| 2026-05-31 (Q3 FY26) | $41.456B | $35.056B | $33.212B | $35.576B | $28.243B | $25.388B | −$7.826B | $17.562B |

Balance sheet (most recent quarter, 2026-05-31): Total Debt $6.376B, Cash & Equivalents $24.995B, Stockholders' Equity $100.724B — all unchanged from 2026-07-08.

### 2.2 Recomputed TTM (Q4FY25–Q3FY26) and ratios — live price re-applied

```
TTM Revenue      = 11.315+13.643+23.860+41.456 = 90.274B          (unchanged)
TTM Gross Profit = 5.054+7.646+17.755+35.056    = 65.511B          (unchanged)
TTM EBIT         = 3.755+6.135+16.192+33.212    = 59.294B          (unchanged)
TTM EBITDA       = 5.904+8.347+18.478+35.576    = 68.305B          (unchanged)
TTM Net Income   = 3.201+5.240+13.785+28.243    = 50.469B          (unchanged)
TTM OCF          = 5.730+8.411+11.903+25.388    = 51.432B          (unchanged)
TTM CapEx        = -5.658-5.389-6.387-7.826     = -25.260B         (unchanged)
TTM FCF          = 51.432 - 25.260 = 26.172B     (= sum of quarterly FCF: 0.072+3.022+5.516+17.562 = 26.172B ✓, unchanged)

Shares outstanding = 26.022B totalCash / $23.041 totalCashPerShare = 1,129,394,201
  (cross-checks to 2026-07-08 session's 1,129,393,151 — effectively unchanged)

Market Cap = $808.27 × 1,129,394,201 = $912.855B
Net Debt   = $6.376B - $24.995B = -$18.619B (net cash, unchanged balance sheet)
EV         = $912.855B + (-$18.619B) = $894.236B

Gross Margin (TTM)  = 65.511/90.274 = 72.57%    (unchanged)
Net Margin (TTM)    = 50.469/90.274 = 55.91%    (unchanged)
ROE proxy (TTM NI / latest equity) = 50.469/100.724 = 50.11%   (unchanged)
Net Debt/EBITDA     = -18.619/68.305 = -0.2726×  (net cash, unchanged)
FCF Yield            = 26.172/912.855 = 2.867%   (up from 2.567% on 2026-07-08 — price fell more than FCF)
EV/EBIT               = 894.236/59.294 = 15.08×  (down from 16.88× — cheaper)
EV/EBITDA             = 894.236/68.305 = 13.09×
FCF/NI ratio          = 26.172/50.469 = 51.86%   (unchanged)
```

**Every fundamental input to the Quality Score is unchanged from 2026-07-08** — only price-dependent figures (market cap, EV, FCF yield, EV/EBIT — Phase 02 inputs only, never reached this session) moved, and moved favorably (cheaper) given the price decline.

### 2.3 Revenue 3yr CAGR and FCF-positive-3-years — independently re-verified, unchanged (FY-anchored, structural)

Pulled fresh annual fundamentals (`annualTotalRevenue`, `annualFreeCashFlow`, `annualNetIncome`) — again byte-for-byte identical to all four prior MU sessions:

```
FY2022 Revenue $30.758B -> FY2025 Revenue $37.378B (FY2026 not yet closed — closes 2026-08-28, ~1 month away)
CAGR = (37.378/30.758)^(1/3) - 1 = 6.71%   (unchanged from all 4 prior sessions)

FY2022 FCF =  $3.114B (positive)
FY2023 FCF = -$6.117B (loss year, still inside the most recent 3 closed fiscal years FY2023-FY2025)
FY2024 FCF =  $0.121B (positive)
FY2025 FCF =  $1.668B (positive)
```

FY2023's loss year has **not yet** rolled out of the FCF-positive-3-years window — that only happens once FY2026 closes (2026-08-28, confirmed via Yahoo `defaultKeyStatistics.nextFiscalYearEnd`) and files (~Oct 2026, consistent with the confirmed 29 Sep 2026 earnings date). **Today (29 Jul 2026) is about one month before that window closes** — this session is genuinely too early for the hard disqualifier to clear, a fact independently confirmed rather than assumed.

### 2.4 Rate Environment Gate inputs — for the record only (not applied, gate fails first)

```
0y (FY2026E) EPS estimate = $73.44403 (Yahoo earningsTrend, "0y" row, endDate 2026-08-31 — NOT the raw
  `forwardPE`/`forwardEps` fields, which read the wrong "+1y"/FY2027E row: forwardEps $153.73953, endDate
  2027-08-31 — same data-quality correction applied in all 4 prior MU sessions, re-verified this session)
Forward PE = $808.27 / $73.44403 = 11.01×
Earnings Yield = 1/11.01 = 9.09%
10Y Treasury ≈ 4.62% (2026-07-28 close, WebSearch — TradingEconomics/Investing.com; direct FRED pull timed out, see §2.0)
Spread vs. 10Y = 9.09% - 4.62% = +4.47%  (>= +1.5% threshold — would PASS Step 1 cleanly, no yellow flag)
Rate Regime Modifier (Step 2) = +5 (10Y still in the 3.5-5% bracket)
```

Neither is applied — the Quality Gate stops the process first (§3).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology, unchanged version)

### 3.1 Legacy 8-criterion comparison table (continuity with prior sessions)

| Check | 2026-07-29 Value | 2026-07-08 Value | Threshold | Result |
|---|---|---|---|---|
| Gross margin | 72.57% (TTM) | 72.57% | >40% | ✅ PASS (unchanged) |
| Net margin | 55.91% (TTM) | 55.91% | >12% | ✅ PASS (unchanged) |
| ROIC/ROE proxy | 50.11% | 50.11% | >15% | ✅ PASS (unchanged) |
| Revenue growth (3yr CAGR) | 6.71% | 6.71% | >8% | ❌ **FAIL (unchanged, structural)** |
| FCF positive 3 consecutive years | FY2023 = **−$6.117B** | same | required | ❌ **FAIL (unchanged, structural — clears ~Aug/Oct 2026)** |
| Net debt/EBITDA | −0.2726× (net cash) | −0.273× | <2.5× | ✅ PASS (unchanged) |
| FCF yield | **2.867%** | 2.567% | >4% | ❌ **FAIL — improved (price decline), still fails** |
| EV/EBIT | **15.08×** | 16.88× | <20× | ✅ **PASS — improved (price decline)** |

**3 of 8 legacy criteria fail — identical count and identical failing criteria to 2026-07-08.** The only movement is in the two price-dependent metrics (FCF yield, EV/EBIT), both of which improved (cheaper) as the stock fell, but neither crosses a pass/fail line that wasn't already on the correct side.

### 3.2 Quality Score — full computation

**Hard disqualifier check (fails regardless of weighted score):**
- FCF/NI conversion <70% for 2+ years without growth-capex explanation: still well below 70% every FY2022–FY2025 (unchanged trailing figures) — but Micron's documented, publicly disclosed *growth* capex (fab construction / HBM capacity expansion, further corroborated this session by the "sold out through 2027" guidance context in §0) — exception applies, this disqualifier does **not** independently fire. Unchanged from 2026-07-08.
- Net Debt/EBITDA over threshold: −0.2726×, far under 2.5× — does not fire. Unchanged.
- **Not FCF-positive for 3+ consecutive years: FIRES.** FY2023 (−$6.117B) sits inside the current FY2023–FY2025 window — independently re-verified in §2.3, unchanged. **This alone fails the gate regardless of the weighted score below.**

**Weighted sub-scores (identical inputs to 2026-07-08 — every underlying fundamental is unchanged, see §2.2–2.3):**

```
Profitability (25%):
  NetMargin_Component = clamp(55.91/30×100) = 100.0
  ROIC_Component (ROE proxy) = clamp(50.11/30×100) = 100.0
  Raw = (100.0+100.0)/2 = 100.0
  --> capped at 40.0 (not FCF-positive 3 consecutive years)
  Profitability_Score = 40.0

Margins (15%):
  GrossMargin_Score = clamp(72.57/80×100) = 90.7   (no trend-bonus needed, already well above 40%)
  Margins_Score = 90.7

Growth (20%):
  Growth_Score = clamp(6.71/25×100) = 26.9
  TAM/pricing-power modifier: NOT applied this session, consistent with all 4 prior MU sessions —
  the AI/HBM demand surge (further evidenced this session by Micron's sold-out-through-2027 capacity
  and raised Q4 guide, §0) remains treated as a cyclical upswing in a commodity-hardware business, not
  an independently-cited durable TAM-expansion thesis distinct from the cycle itself. Flagged explicitly
  again: this is a judgment call under repeated tension (4 consecutive sessions of unusually strong
  demand signals) but held consistent for comparability across sessions rather than silently drifted.
  Growth_Score = 26.9

Balance Sheet (15%):
  BalanceSheet_Score = clamp(100×(1-(-0.2726)/4)) = 106.8 -> capped 100.0
  BalanceSheet_Score = 100.0

Moat Signal (15%) — checklist, only signals with cited evidence marked true (unchanged from 2026-07-08):
  Market share stable/growing: NOT marked true — and if anything, this session's CXMT finding (§0)
    weakens rather than strengthens this signal: a new competitor is documented ramping toward ~18%
    global DRAM share by 2028 (from ~10% now) against Micron's own ~24%, i.e. active share-erosion
    risk, not stability. Still not confidently citable as "stable or growing" either way — no change
    to the score, but the qualitative evidence base shifted slightly negative.
  Brand premium: NOT marked true — no cited pricing-power evidence beyond cyclical ASP swings.
  Network effect: NOT marked true — not applicable to a hardware/component manufacturer.
  Switching costs: MARKED TRUE — documented multi-year HBM/DRAM/SSD supply + technical co-design
    relationship with Anthropic (independently verified in the 2026-06-22 MU session, re-cited since).
  Scale cost advantage: NOT marked true — Micron remains the #3 DRAM player by share (~24% vs.
    Samsung ~36% / SK Hynix ~29%), with CXMT now a 4th entrant (~8% share) — no Micron-specific
    cost-per-unit scale edge is documented.
  Moat_Score = (1/5)×100 = 20.0

FCF Quality (10%):
  FCF/NI ratio = 26.172/50.469 = 51.86%
  FCFQuality_Score = clamp(((0.5186-0.40)/0.60)×100) = 19.8

Quality Score = 40.0×0.25 + 90.7×0.15 + 26.9×0.20 + 100.0×0.15 + 20.0×0.15 + 19.8×0.10
              = 10.00 + 13.605 + 5.38 + 15.00 + 3.00 + 1.98
              = 48.965  →  rounds to 49.0
```

**Quality Score = 49.0 / 100.0 — identical to 2026-07-08, below the 80.0 gate, and the hard disqualifier (not FCF-positive 3+ years) fails it independently regardless.**

**Gate result: FAIL — on both the hard disqualifier and the weighted score, unchanged from 2026-07-08.** Per operating-brief.md / quality-scoring.md: stop here, do not proceed to the Rate Environment Gate or Phase 02 valuation scoring.

---

## 4. Rate Environment Gate — NOT RUN (captured for the record only, §2.4)

Not applied — the Quality Gate stops the process first.

---

## 5. Phase 02 — Valuation Score / Composite Score — NOT RUN

Not applicable — Quality Gate failed (§3.2). No FCF Yield, EV/EBIT, Forward PE, or PEG sub-scores are computed into a valuation score; no Composite Score exists.

---

## 6. Qualitative Notes

1. **The Telegram trigger's specific claim was false, independently confirmed** — no MU earnings report has occurred since Q3 FY2026 (2026-05-31 period end); the next is confirmed for 29 Sep 2026. The $54.6B/$57.7B revenue and $41.6B/$44.2B operating-profit figures in the post do not correspond to any real reported or previewed data.
2. **The real driver was a genuine, well-documented industry event** — CXMT's blockbuster public debut reigniting memory-oversupply concerns, part of a broader sector selloff (SanDisk, SK Hynix also fell) — legitimately within Rule 9's scope (competitor capacity expansion bearing on MU's own pricing/oversupply risk) even though it is not literally an MU earnings or guidance event.
3. **Every fundamental input to the Quality Score is unchanged from 2026-07-08** — independently re-verified via fresh API pulls of both quarterly and annual data, not assumed. The Quality Score is not price-dependent, so an unchanged fundamental picture necessarily produces an unchanged Quality Score (49.0 both sessions).
4. **The two price-dependent legacy metrics (FCF yield, EV/EBIT) both improved** as the stock fell further — MU is mechanically cheaper today than on 2026-07-08 by every valuation multiple — but this has no bearing on the Quality Gate, which is fundamentals-only and must clear before any valuation work is even attempted.
5. **The FCF-positive-3-years hard disqualifier is on a known, near-term clock** — FY2026 closes 2026-08-28 (~1 month from today) and files ~late Sept/early Oct 2026, at which point FY2023's loss year rolls out of the 3-year window. This session is genuinely too early for that to have happened yet; the next natural re-check point is that filing window, not before, absent a new Rule 9 trigger.
6. **Moat evidence remains thin, and the new CXMT information is mildly negative, not positive, for the one plausible future upgrade path** (a "market share stable/growing" credit) — a fourth credible DRAM competitor actively ramping capacity argues against, not for, that signal ever clearing this framework's citation bar for MU specifically, even as HBM-specific demand remains extremely strong.

---

## 7. Recommendation

# **PASS — Quality Gate FAIL (hard disqualifier + Quality Score 49.0 < 80.0, unchanged from 2026-07-08). Do not enter.**

MU still does not clear this framework's 80.0+ Quality Score gate, and independently fails on the "not FCF-positive for 3+ consecutive years" hard disqualifier (FY2023's loss year, which does not roll out of the window until FY2026 closes ~2026-08-28). No Phase 02 valuation score or Composite Score was computed. No fair value, order setup, or position sizing was produced. **No position should be opened.**

This session is nonetheless a **materially new pointer**, not a routine re-check: it independently debunks the specific Telegram claim that triggered it (no earnings report has occurred), identifies and documents the real cause of the price move (CXMT-driven sector selloff, a legitimate Rule 9 capacity-expansion-adjacent trigger), and confirms — rather than assumes — that every underlying fundamental is unchanged since 2026-07-08. Per [watchlist/README.md](../watchlist/README.md), a Rule 9 trigger firing warrants a fresh dated watchlist entry even where the score and action end up unchanged, since the reasoning has genuinely changed.

---

## 8. Next Review Trigger

- **FY2026 fiscal year-end close and filing** (closes 2026-08-28, files with earnings ~29 Sep 2026 after close, now a confirmed date) — the point at which FY2023's loss year finally drops out of the FCF-positive-3-years window, removing that hard disqualifier (revenue CAGR would also need FY2026's actual print to recompute, likely materially higher given the year's demonstrated demand strength).
- **Confirmation (or reversal) of the CXMT oversupply thesis** — watch whether DRAM pricing power actually erodes as CXMT ramps, or whether Micron's HBM-specific mix insulates it, over the next 1–2 quarters.
- **Any further >15% unexplained move** from today's $808.27 reference.
- Any guidance revision, capacity-expansion announcement (Micron's own), or management change (Rule 9).
- If revisited for a full Phase 02/Composite Score: resolve the still-open comparables groundwork (Samsung memory-segment revenue, Kioxia data gap) flagged since 2026-06-20.

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

- **52-week range** — The lowest and highest price a stock has traded at over the past year.
- **ATH (All-Time High)** — The highest price a stock has ever traded at.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **CXMT (ChangXin Memory Technologies)** — See new glossary entry added this session (framework/glossary.md).
- **Composite Score** — This framework's blended Quality + Valuation ranking number; not computed here since the Quality Gate failed first.
- **DRAM / NAND** — The two main memory-chip families: DRAM is working memory, NAND is flash storage. Both are commoditized, cyclical businesses.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating profit before financing/accounting effects.
- **EPS** — Earnings Per Share, net income divided by shares outstanding.
- **EV** — Enterprise Value, a company's total value to all capital providers (market cap + debt − cash).
- **EV/EBIT, EV/EBITDA** — Enterprise Value divided by operating profit measures; how expensive a company is relative to its earnings.
- **EY (Earnings Yield)** — 1 ÷ Forward PE, expressed as a yield comparable to bond yields.
- **FCF** — Free Cash Flow, cash left after running and maintaining the business.
- **FCF Yield** — Free Cash Flow ÷ Market Cap; higher means cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether accounting profit is turning into real cash.
- **Forward PE** — Price ÷ expected next-twelve-months earnings per share.
- **GAAP** — Generally Accepted Accounting Principles, the standard US accounting rulebook.
- **Hard disqualifier** — A Quality Score condition that fails a company regardless of its weighted score.
- **HBM (High-Bandwidth Memory)** — A premium, stacked-DRAM format used in AI accelerator GPUs.
- **IPO (Initial Public Offering)** — The process by which a private company first sells shares to the public on an exchange.
- **Moat** — A durable competitive advantage protecting a business's profits from competitors.
- **Net Debt/EBITDA** — A leverage ratio measuring years of cash profit needed to pay off all debt.
- **Net Margin** — Net Income ÷ Revenue.
- **PE (Price-to-Earnings) ratio** — Share price ÷ earnings per share.
- **Quality Score** — This framework's 0.0-100.0 continuous score grading Phase 01 criteria; 80.0+ required to proceed to valuation scoring.
- **Rate Environment Gate** — The mandatory pre-check before Phase 02 scoring, comparing Earnings Yield to the 10-Year Treasury yield.
- **Rate Regime Modifier** — An additive score adjustment based on the current 10-Year Treasury yield bracket.
- **ROE** — Return on Equity, Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — Fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move.
- **TAM (Total Addressable Market)** — The total revenue opportunity available to a company if it captured 100% of demand for its product/service category.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results.
- **Wafer** — The thin silicon disc on which semiconductor chips are manufactured — the physical unit a foundry sells its manufacturing capacity by.
