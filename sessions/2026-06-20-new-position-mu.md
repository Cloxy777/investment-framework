# NEW POSITION — MU (Micron Technology, Inc.) — 2026-06-20

**Task type:** NEW POSITION
**Date:** 20 Jun 2026
**10Y US Treasury Yield:** 4.451% (yfinance `^TNX`, regularMarketTime → Thu 18 Jun 2026 close; Fri 19 Jun 2026 was a US bond-market holiday [Juneteenth observed], confirmed independently via WebSearch)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **for the record only, not applied — see §4**
**Current MU portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md)), no prior watchlist entry
**Sector:** Memory semiconductors (DRAM — Dynamic Random-Access Memory, the working-memory chips in servers/PCs/phones; and NAND — flash storage chips in SSDs/USB drives), including High-Bandwidth Memory (HBM, a stacked-DRAM format used in AI accelerator GPUs). A classic boom-bust commodity-cycle hardware business, not a steady compounder.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$1,133.99** | yfinance `info['currentPrice']`/`regularMarketPrice`, cross-checked via `t.history(period="5d")` Close column (6/17 = $1,043.19 → 6/18 = $1,133.99) and `regularMarketTime` (1781812800 → 2026-06-18 20:00 UTC) |
| 52-week range | $103.27–$103.38 (low) – $1,149.43 (high) | yfinance (low) / IBKR + yfinance agree (high) |
| Post-market (same session) | $1,151.95 | yfinance `postMarketPrice` |
| Analyst consensus PT | Mean $945.60, median $1,075.00 (range $249.00–$1,750.00, 40 analysts), recommendation "strong_buy" | yfinance `info` |

⚠️ **Stale-feed flag:** IBKR's `get_price_snapshot` (contract ID 9939) returned **$1,043.19** with volume/high/low/open all = 0 — a textbook stale/non-refreshing quote signature. This matches yfinance's **prior-session** close (6/17), not the current one. Friday 6/19/2026 was Juneteenth (observed) — a US market holiday — confirmed independently via WebSearch, which explains why neither feed had a fresher print at the time of the call. Used yfinance's $1,133.99 as the live price: it is internally consistent across three independent checks (snapshot field, intraday history, `regularMarketTime` timestamp) and is the more recent of the two prints. Per Rule 0, price was fetched before any valuation arithmetic was performed.

**Context:** $1,133.99 is **~10x above** the 52-week low (~$103.3) and within ~1.3% of the 52-week high ($1,149.43) — i.e. trading at or near its cycle peak. It sits **~20% above** the analyst mean PT ($945.60) and **~5.4% above** the median PT ($1,075.00), despite a "strong buy" consensus rating and a wide target dispersion ($249–$1,750) that itself signals high analyst disagreement about where in the cycle MU currently sits.

---

## 2. Data Gathered (Phase 01 & 02 Inputs)

### Annual financials (fiscal year ends ~Aug 31) — the boom-bust cycle in raw numbers

| FY | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| FY2022 | $30.758B | $13.898B | $9.760B | $16.876B | $8.687B | $7.75 |
| FY2023 | $15.540B | **−$1.416B** | **−$5.270B** | $2.486B | **−$5.833B** | **−$5.34** |
| FY2024 | $25.111B | $5.613B | $1.802B | $9.582B | $0.778B | $0.70 |
| FY2025 | $37.378B | $14.873B | $10.131B | $18.483B | $8.539B | $7.59 |

Source: `t.financials` (yfinance annual income statement). **FY2023 is an outright trough/loss year** — negative gross profit, negative EBIT, negative net income, negative EPS. This is the DRAM/NAND down-cycle bottom, not a one-off charge.

### Annual cash flow

| FY | FCF | OCF | CapEx |
|---|---|---|---|
| FY2022 | $3.114B | $15.181B | −$12.067B |
| FY2023 | **−$6.117B** | $1.559B | −$7.676B |
| FY2024 | $0.121B | $8.507B | −$8.386B |
| FY2025 | $1.668B | $17.525B | −$15.857B |

Source: `t.cashflow`. FY2023 FCF is sharply negative — breaks "FCF positive 3 consecutive years" on a clean fiscal-year basis (see gate discussion below).

### Quarterly financials (5 most recent) — the current AI/HBM upcycle surge

| Quarter end | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| 2025-02-28 | $8.053B | $2.963B | $1.870B | $3.949B | $1.583B | $1.41 |
| 2025-05-31 | $9.301B | $3.508B | $2.236B | $4.330B | $1.885B | $1.68 |
| 2025-08-31 | $11.315B | $5.054B | $3.755B | $5.904B | $3.201B | $2.83 |
| 2025-11-30 | $13.643B | $7.646B | $6.135B | $8.347B | $5.240B | $4.60 |
| 2026-02-28 | **$23.860B** | **$17.755B** | **$16.192B** | **$18.478B** | **$13.785B** | **$12.07** |

Source: `t.quarterly_financials`. The most recent quarter (Q2 FY2026, ended Feb 2026) shows revenue and EBIT **more than doubling quarter-over-quarter** — an extraordinary, AI/HBM-demand-driven spike, not a stable run-rate.

### Quarterly cash flow (5 most recent)

| Quarter end | FCF | OCF | CapEx |
|---|---|---|---|
| 2025-02-28 | **−$0.113B** | $3.942B | −$4.055B |
| 2025-05-31 | $1.671B | $4.609B | −$2.938B |
| 2025-08-31 | $0.072B | $5.730B | −$5.658B |
| 2025-11-30 | $3.022B | $8.411B | −$5.389B |
| 2026-02-28 | $5.516B | $11.903B | −$6.387B |

Source: `t.quarterly_cashflow`. Note the 2025-02-28 quarter was still slightly **FCF-negative** — the recovery from the FY2023/early-FY2025 trough was not yet complete a year ago.

### TTM (trailing twelve months) reconstruction — sum of last 4 reported quarters (2026-02-28, 2025-11-30, 2025-08-31, 2025-05-31)

| Metric | TTM Value |
|---|---|
| Total Revenue | $58.119B |
| Gross Profit | $33.963B |
| EBIT | $28.318B |
| EBITDA | $37.059B |
| Net Income | $24.111B |
| Free Cash Flow | $10.281B |
| Operating Cash Flow | $30.653B |
| CapEx | −$20.372B |

### Balance sheet (most recent quarter, 2026-02-28)

| Metric | Value |
|---|---|
| Total Debt | $10.798B |
| Cash & Cash Equivalents | $13.908B |
| Cash + Short-Term Investments | $14.589B |
| Stockholders' Equity | $72.459B |
| **Net Debt** (Total Debt − Cash) | **−$3.11B (net cash position)** |

### Computed ratios (TTM financials + most recent balance sheet + live price $1,133.99)

```
Market Cap        = $1,133.99 × 1,127,734,051 shares = $1,278.839B
Net Debt           = $10.798B − $13.908B = −$3.11B (net cash)
EV                 = $1,278.839B + (−$3.11B) = $1,275.729B

Net Debt/EBITDA    = −$3.11B / $37.059B = −0.084×   (net cash — passes trivially)
FCF Yield          = $10.281B / $1,278.839B = 0.804%
EV/EBIT            = $1,275.729B / $28.318B = 45.05×
EV/EBITDA          = $1,275.729B / $37.059B = 34.42×
ROE (TTM NI/Equity)= $24.111B / $72.459B = 33.28%
Gross Margin (TTM) = $33.963B / $58.119B = 58.44%
Net Margin (TTM)   = $24.111B / $58.119B = 41.49%
```

### Revenue 3yr CAGR

```
FY-basis: (FY2025 $37.378B / FY2022 $30.758B)^(1/3) − 1 = 6.71%
```
⚠️ This window has the FY2023 trough year ($15.540B) sitting inside the start-to-end comparison, which mechanically suppresses the computed CAGR relative to what a "normal-to-normal" comparison would show — but per "never invent or estimate financial data," the FY-based figure using actual reported endpoints is what's reported below, flagged rather than substituted.

### Forward PE — the "0y vs +1y" trap (resolved, same issue as the DB1 precedent session)

yfinance's raw `info['forwardPE']` (9.61×) and `info['forwardEps']` ($117.95) use the **`+1y` (FY2027E)** row of `t.eps_trend`, not the correct **`0y` (FY2026E)** row ($61.00952). Confirmed via `info['lastFiscalYearEnd']` = 2025-08-28 and `info['nextFiscalYearEnd']` = 2026-08-28 that `0y` is the fiscal year that should anchor "forward" PE.

```
Correct Forward PE = $1,133.99 / $61.00952 = 18.59×
```

### 5-year historical PE reconstruction (`get_earnings_dates(limit=40)` + rolling TTM EPS)

49 quarters of reported EPS available back to 2014; 41 have valid (TTM EPS > 0) PE, 6 quarters in 2023–2024 excluded as TTM EPS ≤ 0 (the FY2023 loss period flows through here too). Because the exclusion forces the window to reach further back to fill a 20-quarter count, three candidate readings were computed and none is a clean "20 valid quarters within a true 5-calendar-year span":

| Reading | n | Avg PE | Low PE | High PE |
|---|---|---|---|---|
| True trailing 5-calendar-year window | 15 | 20.37× | 5.64× | 85.99× |
| Same, excluding 85.99× outlier (near-zero-TTM-EPS artifact, 2024-09-25) | 14 | 15.68× | 5.64× | 29.95× |
| Mechanical "last 20 valid quarters" (spans >5 calendar years) | 20 | 20.47× | 5.64× | 85.99× |

⚠️ This is flagged but **not resolved into a single number** because Phase 01 fails first (§3) — it becomes moot. Per valuation-scoring.md's own caveat ("if fewer than 5 years of TTM EPS are reconstructable, treat as the no-history fallback"), MU's earnings-cycle volatility means even the act of choosing a window is itself a judgment call the framework's stated rule doesn't cleanly resolve — worth flagging for whoever revisits this name.

### Rate Environment Gate inputs (for the record — see §4 on why not applied)

```
Earnings Yield = 1 / Forward PE = 1 / 18.59 = 5.38%
Spread = 5.38% − 4.451% (10Y) = +0.93%   (< +1.5% threshold → would trigger Step 1's +5 flag)
Step 2 Rate Regime Modifier = +5 (10Y in 3.5–5% bracket)
```

### Comparables groundwork (for the record — not used, Phase 01 failed first)

Peers investigated: Western Digital (WDC), SanDisk (SNDK), Seagate (STX), Samsung Electronics (005930.KS), SK Hynix (000660.KS), Kioxia Holdings (285A.T). Against MU's TTM revenue of $58.119B and Rule 5's ±50% band ($29.06B–$87.18B):

| Peer | TTM Revenue (USD) | In Band? |
|---|---|---|
| WDC | $11.78B | No — too small (20.3% of MU) |
| SanDisk | $13.18B | No — too small (22.7%) |
| Seagate | $11.01B | No — too small (18.9%) |
| Samsung Electronics (total company) | $253.83B | No — too large (436.7%); segment-only memory revenue not sourced |
| SK Hynix | $86.34B | **Yes** (148.5%) — only confirmed in-band peer |
| Kioxia | Data gap — quarterly statements carry only EPS/share-count rows, no revenue/EBIT; only stale FY2025 (ended Mar 2025) annual data available | Unresolved |

This comparables exercise is **incomplete and was not finished** — it became moot once Phase 01 failed (§3), per the operating brief's "stop, don't proceed to scoring" instruction. Captured here only so a future re-look doesn't have to redo this groundwork from scratch.

---

## 3. Phase 01 — Quality Gate

Using valuation-scoring.md's Quantitative Pre-Screen Filters (the threshold set specified for this task):

| Check | MU Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 58.44% (TTM) | >40% | ✅ PASS |
| Net margin | 41.49% (TTM) | >12% | ✅ PASS |
| ROIC/ROE proxy | 33.28% (TTM NI / latest equity) | >15% | ✅ PASS |
| Revenue growth (3yr CAGR) | 6.71% (FY2022→FY2025) | >8% | ❌ **FAIL** |
| FCF positive 3 consecutive years | FY2023 = **−$6.117B** (also: most recent comparable quarter a year ago, 2025-02-28, was −$0.113B) | required | ❌ **FAIL** |
| Net debt/EBITDA | −0.084× (net cash) | <2.5× | ✅ PASS |
| FCF yield | 0.804% (TTM FCF $10.281B / mkt cap $1,278.839B) | >4% | ❌ **FAIL** |
| EV/EBIT | 45.05× (TTM) | <20× | ❌ **FAIL** |

**4 of 8 criteria fail — decisively, not on a hairline.**

### Why this is a clean FAIL, not a judgment call to smooth over

- **FCF yield (0.804% vs >4%)** and **EV/EBIT (45.05× vs <20×)** both fail by more than 2x the threshold. These are driven by the same mechanism: MU's stock price has risen roughly **10x** from its 52-week low (~$103) to the current $1,133.99, on the back of an AI/HBM demand spike that shows up dramatically in the *most recent single quarter* (Q2 FY2026 EBIT of $16.19B vs ~$1.87B a year earlier — an >8x swing). The market is pricing in a continuation or expansion of that quarter's results; TTM fundamentals, even after a strong recovery, have not remotely caught up to that price move. This is the textbook signature of **"priced for perfection at the top of a cycle"** for a cyclical hardware name.
- **FCF positive 3 consecutive years** fails on every basis tested. FY2023 (the fiscal year ending Aug 2023) was an outright FCF loss of −$6.117B — not a rounding miss. Even shifting to a trailing-quarters lens to be charitable, the quarter from almost exactly one year ago (2025-02-28) was still FCF-negative (−$0.113B). There is no honest reading of the data that produces a clean pass here; the most recent four quarters happen to all be positive only because they capture the tail end of the recovery and then the AI/HBM spike — not because the business reliably generates FCF through a full cycle.
- **Revenue 3yr CAGR (6.71% vs >8%)** is the one metric where the distortion argument has real force — the FY2023 trough year sits inside the comparison window and mechanically drags the computed CAGR down. Flagged explicitly. But per "never invent or estimate financial data," the answer is not to substitute a different window or a TTM-based figure that isn't a true 3-year comparison — it's to report the FY-based number as computed and flag the distortion, which is what's done here. Even granting the distortion, this metric alone would not change the gate outcome given the other two unambiguous failures.
- **Gross margin (58.44%), net margin (41.49%), and ROE (33.28%)** all pass comfortably — but per the task's explicit instruction, these are **flagged, not smoothed over, as cyclical risk**: a memory-chip maker's margins/ROE swinging from negative (FY2023) to >40%/>30% (today) within three years is not evidence of a durable structural moat-driven margin profile. It is evidence of being mid-upcycle. The same metric set computed at a different point in the DRAM/NAND cycle (e.g., 12 months ago, or 12 months from now if pricing reverts) could look entirely different. This is explicitly the kind of qualitative caveat Lynch/Graham apply to cyclicals: judge them on normalized, not peak, earnings.

**Gate result: FAIL.** Per operating-brief.md: "If it fails, STOP — report exactly why, do not proceed to scoring." **The Rate Environment Gate and full Phase 02 valuation score are not run** (inputs captured "for the record" in §2/§4 only).

---

## 4. Rate Environment Gate — NOT RUN

Per the operating brief, Phase 01 failure stops the process before this step. For the record only (see §2 for the underlying numbers): Forward PE 18.59× → Earnings Yield 5.38%; spread vs. 10Y (4.451%) = +0.93%, which is below the +1.5% threshold and would trigger Step 1's +5 yellow-flag modifier. Step 2's Rate Regime Modifier would be +5 (10Y in the 3.5–5% bracket). Neither is applied to any score — there is no score.

---

## 5. Phase 02 — Full Valuation Score — NOT RUN

Not applicable — Phase 01 failed. No FCF Yield, EV/EBIT, Forward PE, or PEG sub-scores are computed.

**Upgrade 3 (PEG ratio) — explicitly addressed and ruled out, regardless of gate outcome:** MU is a **classic cyclical** (DRAM/NAND boom-bust; FY2023 was an outright loss year with negative EPS of −$5.34, followed by a recovery to +$7.59 in FY2025, and a current run-rate of $12.07 in a single quarter). Per Upgrade 3's explicit instruction, PEG-based scoring is **"never applied to cyclicals"** — this overrides any trailing EPS-growth percentage that might technically clear the 15%-for-3-years Fast Grower bar, because that growth is mathematically an artifact of recovering from a negative/near-zero earnings base, not a durable compounding rate. Had Phase 02 been reached, PEG's 15% weight would have been redistributed to EV/EBIT (making it 40%), exactly as it was for DB1.DE in the 2026-06-19 session for a different (non-cyclical) reason. This judgment is recorded here explicitly per the task instruction not to silently skip it — it simply never became operative because Phase 01 already failed.

Raw inputs gathered in case of a future re-look (not scored): TTM FCF $10.281B, TTM EBIT $28.318B, EV $1,275.729B, Forward PE 18.59× (0y-basis), 5yr historical PE candidates 15.68×–20.47× avg depending on window choice (see §2), comparables groundwork (SK Hynix only confirmed in-band peer; Samsung/WDC/SanDisk/Seagate/Kioxia all excluded or data-gapped — see §2).

---

## 6. Qualitative Notes (for the record, despite Phase 01 FAIL)

1. **Why are margins high?** ⚠️ **Cyclical, not structural — flagged explicitly per task instruction.** MU's current 58.44% gross margin / 41.49% net margin / 33.28% ROE reflect a severe, demand-driven up-cycle in DRAM and especially HBM (High-Bandwidth Memory) pricing, fueled by AI-accelerator demand (HBM ships alongside GPUs in AI training/inference servers) colliding with constrained supply (memory fabs take years to add capacity). This is the same company that posted **negative gross margin** in FY2023. Memory is a commodity semiconductor business with little pricing power in a glut and extraordinary pricing power in a shortage — margins here are a cycle signal, not a moat signal.
2. **Moat assessment:** Weak to moderate. MU is one of only three scaled global DRAM makers (alongside Samsung and SK Hynix) and a leading NAND producer — real oligopoly structure and high capital-intensity barriers to new entrants — but **no pricing power independent of the supply/demand cycle**, no meaningful switching costs for memory buyers (DRAM/NAND are largely commoditized, interchangeable parts qualified across multiple suppliers), and historically a price-taker in down-cycles. HBM is a partial exception (higher technical differentiation, qualification cycles with GPU makers like Nvidia create some stickiness) but is still a small share of total output today.
3. **Capital allocation track record:** Heavy, necessary capex to stay competitive in process-node and HBM capacity (TTM CapEx −$20.372B against TTM revenue of $58.119B, ~35% of revenue) — this is largely **maintenance-plus-capacity capex required just to remain a relevant supplier**, not obviously the kind of moat-widening growth capex Upgrade 1 (Owner Earnings) is designed to credit; that adjustment was not invoked here since Phase 01 failed before any FCF-yield refinement would matter.
4. **Growth sources next 3–5 years:** AI-driven HBM demand (the current upcycle driver), continued data-center DRAM/NAND demand growth, eventual normalization of PC/mobile end-markets. All of these are demand-side, cycle-dependent drivers rather than structural TAM expansion the company controls.
5. **Best bear case:** ⚠️ **Cyclicality is the bear case, not a side risk — flagged explicitly per task instruction.** Memory pricing is notoriously prone to oversupply once the current capacity additions (from MU and both Korean competitors) come online — the same dynamic that produced FY2023's outright losses could recur once AI/HBM capex growth decelerates or supply catches up to demand. Buying at ~10x off the 52-week low, within 1.3% of the all-time-range high, priced at an EV/EBIT of 45x against TTM earnings that are themselves inflated by a single extraordinary quarter, is buying at what looks like peak-cycle pricing — the opposite of the "quality at a fair price" entry point this framework is built around.
6. **Disruption vector check:** Lower near-term risk than most tech disruption vectors — DRAM/NAND/HBM are foundational hardware with no credible alternative architecture displacing them in the 5-year horizon. The more relevant "disruption" is **cyclical**, not technological: a supply response (new fab capacity from MU, Samsung, SK Hynix, or a Chinese entrant like CXMT/YMTC scaling faster than expected) could compress the current pricing environment well within 5 years, which is functionally a disruption to the current earnings level even without any new technology displacing memory itself.

---

## 7. Recommendation

# **PASS — Phase 01 FAIL. Do not enter. Watchlist entry created (not scored).**

MU fails the Phase 01 quality gate on **4 of 8 criteria**, two of them (FCF yield 0.804% vs >4%; EV/EBIT 45.05× vs <20×) by more than 2x the threshold. The pattern here is the classic "priced for perfection at the top of a cycle" signature: margins and ROE that look excellent in isolation (58.44% gross margin, 41.49% net margin, 33.28% ROE) are themselves an artifact of being mid-upcycle in a company that posted **negative** gross margin, EBIT, and net income just three fiscal years ago (FY2023). The stock trades ~10x above its 52-week low and within 1.3% of its 52-week high, and the most recent quarter's results (Q2 FY2026) more than doubled quarter-over-quarter — evidence of a violent up-cycle, not a steady compounding business.

Per Upgrade 3, PEG-based scoring was explicitly **not** applied despite MU's recent EPS growth technically clearing a "15% for 3 years" threshold on paper — that growth is an artifact of recovering from a negative earnings base in a cyclical, not a durable compounding rate, and Upgrade 3 explicitly bars PEG application to cyclicals. This judgment is recorded regardless of the gate outcome.

**No Phase 02 score was computed. No fair value, order setup, or position sizing was produced** (gate failed before Phase 02). **No position should be opened.**

---

## 8. Next Review Trigger

**Date/event:** MU's next earnings release (Q3 FY2026, expected late June 2026) for a mandatory Rule 9 re-score, and/or any of the following:
- A meaningful **pullback from cycle-peak pricing** (e.g., back toward the $700–800 range or lower) that would mechanically improve FCF yield and EV/EBIT even before fundamentals change — re-run Phase 01 at that point.
- **Confirmation that TTM EBIT/FCF have caught up** to the current run-rate over 2+ more quarters (i.e., the current quarter's extraordinary results prove durable rather than a one-quarter spike) — would materially change the revenue-CAGR and FCF-positive-3-years gate items on a forward basis.
- Any **>15% unexplained price move** from $1,133.99 (Rule 9).
- Any **guidance revision, capacity-expansion announcement (supply-side cycle risk), or management change** (Rule 9).
- If revisited: resolve the unresolved comparables groundwork (Samsung memory-segment-only revenue, Kioxia's revenue/EBIT data gap) and the 5yr historical-PE window ambiguity flagged in §2 before computing a full Phase 02 score.

**No position opened — nothing to log in `decisions/`.**
