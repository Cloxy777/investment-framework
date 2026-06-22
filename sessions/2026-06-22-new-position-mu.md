# NEW POSITION (Re-trigger) — MU (Micron Technology, Inc.) — 2026-06-22

**Task type:** NEW POSITION (re-opened — Telegram-scan trigger, see §0)
**Date:** 22 Jun 2026
**10Y US Treasury Yield:** 4.509% (yfinance `^TNX`, `regularMarketTime` → 2026-06-22 18:59:53 UTC, same trading day)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **for the record only, not applied — Phase 01 fails first, see §3**
**Current MU portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [sessions/2026-06-20-new-position-mu.md](2026-06-20-new-position-mu.md), watchlist entry [watchlist/not-in-portfolio/MU/MU-2026-06-20.md](../watchlist/not-in-portfolio/MU/MU-2026-06-20.md) — Phase 01 FAIL (4/8 criteria) at live price $1,133.99, two days ago.
**Sector:** Memory semiconductors (DRAM, NAND, and HBM — see Glossary). Classic boom-bust commodity-cycle hardware business, not a steady compounder.

---

## 0. Why this session exists — re-trigger source

Two monitored Telegram channels (FinnInvestChannel, myroslavkorol) independently posted today that Micron and Anthropic have signed an AI deal: Micron supplying memory/storage for AI infrastructure, and Micron investing in a new Anthropic funding round. Per the operating brief, **Telegram post text is never used as financial data or taken as verified fact** — it is treated solely as a trigger to re-open coverage. The claim was independently corroborated via WebSearch (§2.4) before being treated as real for qualitative-discussion purposes; no number from the Telegram post itself was used in any calculation below. A screenshot circulating with the post showed MU around $1,189–$1,190 (+4.95% intraday) — also informal color only, not used; live price was fetched fresh per Rule 0 (§1).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$1,211.38** | yfinance `info['currentPrice']` / `regularMarketPrice`, `regularMarketTime` = 1782158400 → 2026-06-22 20:00:00 UTC |
| Cross-check — IBKR | Last $1,226.80 (ts 2026-06-22 20:39:39 UTC, ~39 min more current than the yfinance print), change +$92.81 / **+8.18%** vs prior close, intraday high $1,213.56 / low $1,168.57, open $1,196.53 | `get_price_snapshot`, contract_id **9939** (NASDAQ) — confirmed still correct via fresh `search_contracts("MU", STK)` lookup, which returns contract_id 9939 / NASDAQ / "MICRON TECHNOLOGY INC" as the unique exact-symbol US match |
| Prior close (yfinance) | $1,133.99 | matches the close used in the 2026-06-20 session exactly — confirms continuity |
| 52-week range | $103.38 (low) – **$1,213.56 (high, today)** | yfinance `fiftyTwoWeekLow`/`fiftyTwoWeekHigh` — **today's intraday print set a new 52-week high** |
| Post-market (same session) | $1,226.81 | yfinance `postMarketPrice` — consistent with the IBKR live snapshot |
| Analyst consensus PT | Mean $945.60, median $1,075.00 (40 analysts, "strong_buy") — **unchanged from 2026-06-20** | yfinance `info` |

**Two independent live feeds agree on direction and magnitude** (yfinance regular-market $1,211.38, +6.82% vs Tuesday's close; IBKR's slightly later snapshot $1,226.80, +8.18%) — both reflect a real, large, same-day intraday rally, not a stale quote (contrast with the 2026-06-20 session's correctly-flagged stale IBKR print). **$1,211.38** (yfinance regular-market price) is used as the live price for all valuation arithmetic below, being the more conservative (lower) of the two and the one with a clean `regularMarketTime` audit trail; the IBKR snapshot is shown for cross-check only, consistent with Rule 0 practice in the prior session.

**Context:** $1,211.38 is **~11.7x** above the 52-week low (~$103.4) and sits **within 0.18% of today's new 52-week/all-time high** ($1,213.56) — i.e. literally at the cycle peak as of this session, a more extreme position than the "near the high" framing of 2026-06-20 ($1,133.99 was 1.3% off the then-high). It is **28.1% above** the analyst mean PT ($945.60) and **12.7% above** the median PT ($1,075.00) — both gaps have widened versus 2026-06-20 (was 20% and 5.4% respectively), since the price moved and the (unchanged) consensus targets did not.

---

## 2. Data Gathered — Refresh Status

### 2.1 Trailing financials — confirmed unchanged (no new earnings reported)

`t.financials`, `t.cashflow`, `t.quarterly_financials`, `t.quarterly_cashflow`, and `t.quarterly_balance_sheet` were re-pulled fresh today and are **byte-for-byte identical** to the 2026-06-20 session:
- Most recent quarterly column is still **2026-02-28** (Q2 FY2026) — no Q3 FY2026 column has appeared.
- Annual FY columns still run FY2021–FY2025 (fiscal year end Aug 31); FY2023 is still the trough/loss year (Revenue $15.540B, Gross Profit −$1.416B, EBIT −$5.270B, Net Income −$5.833B, FCF −$6.117B).
- `eps_trend` `0y` row still reads **61.00952** (FY2026E EPS, the correct "0y" forward basis per the same `lastFiscalYearEnd`/`nextFiscalYearEnd` resolution as 2026-06-20).

### 2.2 Earnings calendar check — Q3 FY2026 has NOT yet been reported

WebSearch confirms: **Micron reports fiscal Q3 2026 results on Wednesday, June 24, 2026** (earnings call 2:30pm Mountain Time) — two days after this session, not yet released. This matches the prior session's "expected late June 2026" forecast and explains why every trailing financial figure above is unchanged. **Per the task's own logic: nothing in the trailing financials can have changed, so any movement in the computed ratios below is driven entirely by the live-price change (denominator effect), not by new fundamentals.**

Sources: [Micron Technology to Report Fiscal Third Quarter Results on June 24 (StockTitan)](https://www.stocktitan.net/news/MU/micron-technology-to-report-fiscal-third-quarter-results-on-june-24-22gcrbths4gp.html), [SEC 8-K, FY2026 Q2 press release](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000004/a2026q2ex991-pressrelease.htm), [SEC 10-Q for the quarter ended 2026-02-26](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000006/mu-20260226.htm).

### 2.3 TTM reconstruction and balance sheet — unchanged

| Metric | TTM Value (unchanged from 2026-06-20) |
|---|---|
| Total Revenue | $58.119B |
| Gross Profit | $33.963B |
| EBIT | $28.318B |
| EBITDA | $37.059B |
| Net Income | $24.111B |
| Free Cash Flow | $10.281B |

| Balance sheet (2026-02-28, unchanged) | Value |
|---|---|
| Total Debt | $10.798B |
| Cash & Cash Equivalents | $13.908B |
| Stockholders' Equity | $72.459B |
| Net Debt | **−$3.110B** (net cash) |

### 2.4 Independent corroboration of the Telegram-claimed Micron–Anthropic deal — CONFIRMED REAL

WebSearch independently confirms a real, same-day announcement (not invented, not Telegram-sourced data): **Micron and Anthropic announced a strategic agreement on 2026-06-22**, corroborated across multiple independent outlets including **Micron's own investor-relations press release**.

**What the deal actually says, per Micron's own announcement and independent reporting:**
- **Supply agreement:** Micron will supply Anthropic with **HBM (High-Bandwidth Memory), DRAM, and SSDs (solid-state drives)** for AI data-center infrastructure — multi-year.
- **Technical collaboration:** Micron and Anthropic will co-design memory/storage architecture optimized for AI workloads — a deeper engineering relationship than a pure supply contract.
- **Enterprise AI adoption:** Micron will deploy Claude (Anthropic's model family) internally across its own operations — a customer relationship in the *other* direction.
- **Investment:** Anthropic's **Series H round closed 2026-05-28**, raising **$65B at a $965B post-money valuation**. Micron is reported as a participant in that round, but **Micron's specific investment amount is undisclosed** in every source found — this is a real data gap, not filled in here per "never invent or estimate financial data."
- **Market reaction:** Reporting attributes an approximate **+5.5%** same-day stock move to the announcement (compatible with, though not identical to, the larger ~7–8% move measured directly off both live feeds above — the gap is most likely other contemporaneous market activity / index effects not isolated by either source, and is not reconciled further here since it does not change any conclusion).

Sources: [Micron and Anthropic Announce Strategic Agreement to Scale Next-Generation AI Infrastructure — Micron Technology Investor Relations](https://investors.micron.com/news-releases/news-release-details/micron-and-anthropic-announce-strategic-agreement-scale-next), [Barchart](https://www.barchart.com/story/news/2581941/micron-and-anthropic-announce-strategic-agreement-to-scale-next-generation-ai-infrastructure), [StockTitan](https://www.stocktitan.net/news/MU/micron-and-anthropic-announce-strategic-agreement-to-scale-next-zduaiobz9mvv.html), [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/micron-anthropic-announce-strategic-agreement-130000301.html), [U.S. News](https://money.usnews.com/investing/news/articles/2026-06-22/micron-anthropic-sign-ai-infrastructure-supply-agreement), [InvestingNews](https://investingnews.com/micron-and-anthropic-announce-strategic-agreement-to-scale-next-generation-ai-infrastructure/), [CryptoBriefing](https://cryptobriefing.com/micron-anthropic-supply-agreement-series-h/).

**Note on Anthropic as a security:** Anthropic is privately held with no public ticker. It is not a tradable security and is not evaluated as one anywhere in this framework; it is discussed here only as context for MU's qualitative thesis (§6).

### 2.5 Recomputed ratios (TTM financials — unchanged — + live price $1,211.38)

```
Market Cap        = $1,211.38 × 1,127,734,051 shares = $1,366.114B
Net Debt           = $10.798B − $13.908B = −$3.110B (net cash, unchanged)
EV                 = $1,366.114B + (−$3.110B) = $1,363.004B

Net Debt/EBITDA    = −$3.110B / $37.059B = −0.084×   (net cash — passes trivially, unchanged)
FCF Yield          = $10.281B / $1,366.114B = 0.753%   (was 0.804% on 6/20 — WORSE, price-driven)
EV/EBIT            = $1,363.004B / $28.318B = 48.13×   (was 45.05× on 6/20 — WORSE, price-driven)
EV/EBITDA          = $1,363.004B / $37.059B = 36.78×   (was 34.42× on 6/20)
ROE (TTM NI/Equity)= $24.111B / $72.459B = 33.28%   (unchanged — denominator is equity, not price)
Gross Margin (TTM) = $33.963B / $58.119B = 58.44%   (unchanged)
Net Margin (TTM)   = $24.111B / $58.119B = 41.49%   (unchanged)
```

### 2.6 Revenue 3yr CAGR — unchanged (no new fiscal year has closed)

```
FY-basis: (FY2025 $37.378B / FY2022 $30.758B)^(1/3) − 1 = 6.71%   (identical to 2026-06-20 — same FY endpoints)
```

### 2.7 Forward PE — recomputed off the new price, same `0y` eps_trend basis

```
0y eps_trend (FY2026E EPS) = $61.00952   (unchanged from 2026-06-20)
Forward PE = $1,211.38 / $61.00952 = 19.86×   (was 18.59× on 6/20 — higher, price-driven)
```

(Raw yfinance `info['forwardPE']` again reads the wrong `+1y` row — today it shows 10.14× off `forwardEps` $119.43, which is the `+1y`/FY2027E figure, not the `0y`/FY2026E figure that should anchor "forward" PE. Same correction applied as 2026-06-20, re-verified against `lastFiscalYearEnd`/`nextFiscalYearEnd`.)

### 2.8 Rate Environment Gate inputs (for the record — see §4 on why not applied)

```
Earnings Yield = 1 / Forward PE = 1 / 19.86 = 5.04%
Spread = 5.04% − 4.509% (10Y) = +0.53%   (< +1.5% threshold → would trigger Step 1's +5 yellow flag)
Step 2 Rate Regime Modifier = +5 (10Y 4.509% is in the 3.5–5% bracket)
```

10Y Treasury moved from 4.451% (6/18 close, used 6/20) to 4.509% today — still squarely in the 3.5–5% bracket, no regime change.

---

## 3. Phase 01 — Quality Gate (Re-run)

Using valuation-scoring.md's Quantitative Pre-Screen Filters — identical threshold set as 2026-06-20:

| Check | MU Value (2026-06-22) | MU Value (2026-06-20) | Threshold | Result |
|---|---|---|---|---|
| Gross margin | 58.44% (TTM) | 58.44% | >40% | ✅ PASS (unchanged) |
| Net margin | 41.49% (TTM) | 41.49% | >12% | ✅ PASS (unchanged) |
| ROIC/ROE proxy | 33.28% (TTM NI / latest equity) | 33.28% | >15% | ✅ PASS (unchanged) |
| Revenue growth (3yr CAGR) | 6.71% (FY2022→FY2025) | 6.71% | >8% | ❌ **FAIL (unchanged)** |
| FCF positive 3 consecutive years | FY2023 = **−$6.117B** | same | required | ❌ **FAIL (unchanged)** |
| Net debt/EBITDA | −0.084× (net cash) | −0.084× | <2.5× | ✅ PASS (unchanged) |
| FCF yield | **0.753%** (TTM FCF $10.281B / mkt cap $1,366.114B) | 0.804% | >4% | ❌ **FAIL — worse** |
| EV/EBIT | **48.13×** (TTM) | 45.05× | <20× | ❌ **FAIL — worse** |

**4 of 8 criteria still fail — decisively, and two of them (FCF yield, EV/EBIT) deteriorated further** since the live price rose ~6.8% (yfinance basis) while every trailing-financials input is unchanged. This is exactly the mechanical outcome flagged as "likely" in this task's framing: an announcement that is real and may matter to MU's *forward* trajectory pushed the price up, which by definition makes a price-denominated cheapness ratio (FCF yield, EV/EBIT) **worse**, not better — it cannot retroactively repair trailing revenue CAGR or the FY2023 FCF loss year either, since neither of those depends on price at all.

### Why this is a clean FAIL, reinforced not weakened by today's news

- **FCF yield (0.753% vs >4%)** and **EV/EBIT (48.13× vs <20×)** both fail by more than 2x the threshold (EV/EBIT now fails by nearly 2.5x). The mechanism is unchanged from 2026-06-20 — and amplified: the stock is now **~11.7x** off its 52-week low and **at a new all-time high** as of today, on top of an already-extended AI/HBM-driven re-rating. Today's news (a real supply deal plus an unquantified investment stake) added fresh fuel to a valuation that was already priced for an extraordinary continuation of Q2 FY2026's results before the announcement.
- **FCF positive 3 consecutive years** still fails outright — FY2023's −$6.117B loss is a closed historical fact that no announcement, however large, can revise. Unchanged from 2026-06-20.
- **Revenue 3yr CAGR (6.71% vs >8%)** is unchanged — still computed off the same FY2022→FY2025 endpoints, still flagged as distorted by the FY2023 trough sitting inside the window, still reported as-computed per "never invent or estimate financial data" rather than substituted.
- **Gross margin (58.44%), net margin (41.49%), ROE (33.28%)** still pass, and are still flagged — exactly as on 2026-06-20 — as cycle-inflated rather than structural. Today's news does not change this: a large customer/supply commitment from Anthropic does not itself alter MU's trailing margin history, which still shows a 3-year round trip from negative to currently elevated.

**Gate result: FAIL — same 4 criteria, two of them worse.** Per operating-brief.md: "If it fails, STOP — report exactly why, do not proceed to scoring." **The Rate Environment Gate and full Phase 02 valuation score are not run.**

---

## 4. Rate Environment Gate — NOT RUN

Per the operating brief, Phase 01 failure stops the process before this step. For the record only (§2.8): Forward PE 19.86× → Earnings Yield 5.04%; spread vs. 10Y (4.509%) = +0.53%, below the +1.5% threshold (would trigger Step 1's +5 yellow-flag modifier — narrower margin of failure than 6/20's +0.93% spread, since forward PE rose with price while forward EPS didn't move). Step 2's Rate Regime Modifier would be +5 (10Y still in the 3.5–5% bracket). Neither is applied to any score — there is no score.

---

## 5. Phase 02 — Full Valuation Score — NOT RUN

Not applicable — Phase 01 failed, same as 2026-06-20. No FCF Yield, EV/EBIT, Forward PE, or PEG sub-scores are computed.

**Upgrade 3 (PEG ratio) — re-affirmed, regardless of gate outcome:** MU remains a classic cyclical (unchanged FY2023 loss year, unchanged recovery pattern). Per Upgrade 3, PEG-based scoring continues to be **"never applied to cyclicals."** Nothing in today's news changes this classification — a supply/investment deal with a single large AI customer does not convert a commodity-memory cyclical into a structural compounder on its own; it would need to show up as a multi-year change in the *trailing* earnings/FCF pattern before that judgment is revisited.

---

## 6. Qualitative Notes — Updated for Today's Findings

1. **Why are margins high?** Unchanged assessment from 2026-06-20 — cyclical AI/HBM demand spike, not structural. Today's Anthropic deal is a **demand-side confirmation of the same story already priced in**: a large compute/AI buyer locking in supply is exactly the kind of catalyst that would explain why the current up-cycle might extend, but it is incremental evidence *for* the cyclical-upswing thesis, not evidence that the business model itself has become structurally different. A multi-year supply agreement is a real positive but is still a contract within the same boom-bust commodity-memory business described on 2026-06-20.
2. **Moat assessment:** Unchanged — oligopoly structure (MU, Samsung, SK Hynix) with real capital-intensity barriers, no durable pricing power independent of the supply/demand cycle. **One nuance worth flagging:** a co-design relationship with a frontier AI lab (per the announcement, joint work on memory/storage architecture optimized for AI workloads, not just an off-the-shelf supply contract) is closer to the kind of qualification-cycle stickiness already credited to HBM specifically in the 2026-06-20 session — a modest positive nuance, not enough on its own to upgrade the moat assessment, and explicitly **not** something that overrides any of the four mechanical Phase 01 failures.
3. **Capital allocation track record:** Unchanged — heavy capacity capex (~35% of TTM revenue), largely required just to remain a relevant supplier. An equity investment in Anthropic's Series H, if and when Micron's specific dollar amount becomes public, would be a new capital-allocation data point worth tracking at the next mandatory review — it cannot be evaluated today because the amount is undisclosed (data gap, not filled in per "never invent or estimate financial data").
4. **Growth sources next 3–5 years:** Unchanged demand-side drivers (AI/HBM, data-center DRAM/NAND, PC/mobile normalization) — today's news is a concrete, named, large-customer data point *within* that existing thesis (Anthropic joins the roster of AI-infrastructure buyers driving HBM demand), not a new growth vector.
5. **Best bear case:** Unchanged and, if anything, reinforced by today's price action — buying within 0.18% of a new all-time high, on the day of the news, at an EV/EBIT of 48.13× (worse than 6/20's already-stretched 45.05×) is the textbook definition of paying up further into a "priced for perfection" cyclical peak. A real deal announcement that pushes the stock to a new high while trailing fundamentals stand still is not a contradiction of the bear case — it is a restatement of it with a bigger gap between price and trailing fundamentals.
6. **Disruption vector check:** Unchanged from 2026-06-20 — the relevant risk remains cyclical supply-response risk (new fab capacity from MU/Samsung/SK Hynix/Chinese entrants), not technological displacement of memory itself.

**Explicit instruction-mandated note:** even a real, large supply/investment deal of the kind confirmed today does **not** retroactively repair trailing revenue CAGR, the FY2023 FCF loss year, FCF yield, or EV/EBIT — all four are either backward-looking historical facts (CAGR, FCF history) or mechanically worsened by the price increase the news itself caused (FCF yield, EV/EBIT). It is, however, directly relevant to MU's **forward** trajectory (a named, large, credible AI customer with a multi-year supply commitment plus a technical co-design relationship) and is flagged explicitly here as something the next mandatory review (Q3 FY2026 earnings, 2 days away) should weigh once Micron's own guidance/commentary on the deal's scale and timing becomes available on the earnings call.

---

## 7. Recommendation

# **PASS — Phase 01 FAIL (unchanged). Do not enter. Existing watchlist entry updated, not re-scored.**

MU still fails the Phase 01 quality gate on the same **4 of 8 criteria** as the 2026-06-20 session, and two of them (FCF yield, EV/EBIT) deteriorated further as the live price rallied ~6.8–8.2% intraday today. The Micron–Anthropic deal reported by Telegram was **independently corroborated as real** via WebSearch — a genuine multi-year HBM/DRAM/SSD supply agreement plus an undisclosed-size Micron investment in Anthropic's just-closed Series H ($65B raise, $965B post-money valuation) — but a real deal of this kind cannot, by the mechanics of this framework's own gate, fix a closed historical FCF-loss year, an already-computed 3-year revenue CAGR, or a price-denominated cheapness ratio that the announcement's own market reaction made *more* expensive, not less. The qualitative case for MU's forward trajectory is, if anything, marginally strengthened by today's news; the case for entering a new position **today, at this price, against this trailing financial record** is not.

**No Phase 02 score was computed. No fair value, order setup, or position sizing was produced.** **No position should be opened.**

---

## 8. Next Review Trigger

**Date/event:** MU's Q3 FY2026 earnings release, confirmed for **Wednesday, 24 June 2026** (2 days from this session) — a mandatory Rule 9 re-score regardless of outcome, and the first opportunity to see whether the trailing financials (revenue CAGR, FCF-positive-years count, TTM EV/EBIT/FCF-yield denominators) actually shift, and whether management quantifies the Anthropic deal's scale/timing on the earnings call. Also still applicable, carried forward from 2026-06-20:
- A meaningful **pullback from cycle-peak pricing** (e.g. back toward the $700–800 range or lower) that would mechanically improve FCF yield and EV/EBIT even before fundamentals change.
- **Confirmation that TTM EBIT/FCF have caught up** to the current run-rate over 2+ more quarters.
- Any **>15% unexplained price move** from $1,211.38 (today's reference price) — note today's own move (~6.8–8.2%) does not by itself meet this Rule 9 bar, but is the second large single-day move in this name within a week and is itself a reason for tighter monitoring cadence until Q3 earnings land.
- Any **guidance revision, capacity-expansion announcement, or management change** (Rule 9) — Q3 earnings (2 days away) is the next scheduled occasion for guidance.
- **Micron disclosing the actual size of its Anthropic investment** — currently undisclosed; once public, re-evaluate as a capital-allocation data point (§6.3).
- If revisited: resolve the unresolved comparables groundwork and 5yr historical-PE window ambiguity flagged in the 2026-06-20 session (§2 there) before computing a full Phase 02 score.

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

- **52-week range** — The lowest and highest price a stock has traded at over the past year.
- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **CapEx** — Capital Expenditure, money spent on physical assets like factories and equipment.
- **DRAM / NAND** — The two main memory-chip families: DRAM is working memory (servers/PCs/phones), NAND is flash storage (SSDs/USB drives). Both are commoditized, cyclical businesses.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — measures of operating profit before financing/accounting effects.
- **EPS** — Earnings Per Share, net income divided by shares outstanding.
- **EV** — Enterprise Value, a company's total value to all capital providers (market cap + debt − cash).
- **EV/EBIT, EV/EBITDA** — Enterprise Value divided by operating profit measures; how expensive a company is relative to its earnings, independent of capital structure.
- **EY (Earnings Yield)** — 1 ÷ Forward PE, expressed as a yield comparable to bond yields.
- **FCF** — Free Cash Flow, cash left after running and maintaining the business.
- **FCF Yield** — Free Cash Flow ÷ Market Cap; higher means cheaper.
- **Forward PE** — Price ÷ expected next-twelve-months earnings per share.
- **FV (Fair Value)** — An analyst's estimate of intrinsic worth, independent of market price.
- **GAAP** — Generally Accepted Accounting Principles, the standard US accounting rulebook.
- **HBM (High-Bandwidth Memory)** — A premium, stacked-DRAM format used in AI accelerator GPUs; higher-margin than commodity DRAM/NAND but still cyclical.
- **Moat** — A durable competitive advantage protecting a business's profits from competitors.
- **Net Debt/EBITDA** — A leverage ratio measuring years of cash profit needed to pay off all debt.
- **PEG ratio** — PE ratio ÷ earnings growth rate; judges whether a fast grower's multiple is justified by its growth.
- **PE (Price-to-Earnings) ratio** — Share price ÷ earnings per share.
- **PT (Price Target)** — An analyst's forecast of a future stock price.
- **pp (percentage points)** — A direct difference between two percentages, as opposed to a percentage change.
- **Rate Environment Gate** — The mandatory pre-check before Phase 02 scoring, comparing Earnings Yield to the 10-Year Treasury yield.
- **Rate Regime Modifier** — An additive score adjustment (−10 to +10) based on the current 10-Year Treasury yield bracket.
- **ROE** — Return on Equity, Net Income ÷ shareholder equity.
- **ROIC** — Return on Invested Capital, how efficiently a company turns invested capital into profit.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — Fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move.
- **SSD (Solid-State Drive)** — A flash-memory-based storage device, the end product much of NAND chip output goes into.
- **TAM** — Total Addressable Market, the full revenue opportunity available to a company.
- **Treasury yield (10Y)** — The interest rate on 10-year US government bonds, this framework's risk-free-rate benchmark.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results.
