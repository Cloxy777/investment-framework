# New Position Evaluation: HY9H (SK hynix Inc., GDS) — 2026-06-20

**Task type:** NEW POSITION
**Ticker (tradable instrument):** HY9H — Frankfurt Stock Exchange (FWB), IBKR contract_id 517397504, "SK HYNIX INC-GDS," country_code DE, currency EUR
**Underlying company:** SK hynix Inc. — primary listing Korea Exchange (KRX), ticker 000660 (yfinance: `000660.KS`), reporting currency KRW (South Korean won)
**Instrument type:** Global Depositary Share (GDS) — a certificate issued by a depositary bank representing a fixed number of shares of a foreign company, traded on a different exchange (here, Frankfurt) in a different currency (EUR) than the underlying shares (KRW)
**Analyst:** Claude (automated session)
**Account:** U19421206 (IBKR)

---

## 0. Why this session carries the same multi-currency-GDS complexity as the SSU session, but a simpler business mix

This is the third related GDR/GDS evaluation this session (after MU and SSU). Like SSU (Samsung Electronics GDR), it layers two things on top of a standard new-position workflow:
1. **Company fundamentals must come from the primary KRX listing** (000660.KS, KRW) — the GDS itself has no separate financials, it's a wrapper.
2. **The GDS-to-ordinary-share ratio must be confirmed from a reliable source**, not assumed, before any per-GDS fair value, buy price, sell target, stop loss, or position size can be computed.

Unlike SSU, **SK hynix is a pure-play memory semiconductor company** (DRAM, NAND, and — critically — HBM, the high-bandwidth memory used in AI accelerators like Nvidia's GPUs), not a diversified conglomerate. There is no segment-mix/sum-of-the-parts complexity here: SK hynix's consolidated multiples *are* its memory-business multiples. This makes the comparable-peer-set work cleaner than SSU's, but the underlying cyclicality risk — already seen in MU (Micron) and flagged as the central risk in SSU — applies with equal or greater force, since SK hynix has zero diversification away from the memory cycle.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

Per the task's price-fetch strategy (yfinance primary, IBKR secondary/best-effort), given a prior session's experience of a hung IBKR snapshot call on this exact contract:

| Instrument | Price | Source | Timestamp |
|---|---|---|---|
| **HY9H (GDS, EUR, Frankfurt)** | **€1,580.00** | yfinance `HY9H.F` (`.DE` suffix returns no data — confirmed not the right Yahoo suffix for this listing) | 2026-06-19 18:46 UTC (regularMarketTime) |
| Prior close | €1,590.00 | yfinance | — |
| SK hynix ordinary (KRX, KRW) | ₩2,764,000 | yfinance `000660.KS` | 2026-06-19 06:30 UTC |
| Prior close (KRX) | ₩2,685,000 | yfinance | — |
| **IBKR cross-check (secondary)** | **€1,575.00** (last trade), prior close €1,590.00 | `get_price_snapshot`, contract_id 517397504 | 2026-06-19 20:50 UTC |

⚠️ **IBKR note (per task instructions):** unlike the prior session's hung call on this same contract_id, this call **returned successfully** (last trade €1,575.00, prior close €1,590.00 exactly matching yfinance's prior close). It is used here only as a secondary cross-check, consistent with the task's price-fetch strategy — yfinance (€1,580.00) is treated as primary since it was fetched first and is internally consistent with its own historical series (see Section 2's price-math cross-check). The two sources agree to within 0.3%, well inside normal bid/ask spread.

Both yfinance prices carry a "last trading session" timestamp from 2026-06-19 (evening Europe/Asia time) rather than an intraday 2026-06-20 print — consistent with the MU session's finding that non-US markets' most recent close can lag a same-day US session depending on time zones and `regularMarketTime`. This is the most current available price from either source at the time of this evaluation and is used as the live price per Rule 0 (never inferred from a valuation multiple).

**52-week range (KRX ordinary):** ₩245,000 (low) – ₩2,891,000 (high). At ₩2,764,000, SK hynix is trading **~11.3× above its 52-week low** and within **4.4% of its 52-week high** — i.e., near the top of its 52-week range, the same "priced near cycle-peak" signature flagged in the MU session for Micron.

**Analyst consensus (KRX, for context only, not a valuation input):** Mean target price ₩2,712,489, median ₩2,857,500 (38 analysts), "strong buy" consensus. The live price (₩2,764,000) sits almost exactly at the analyst mean target — i.e., analysts see the stock as roughly fairly priced today, not materially mispriced in either direction. Noted per Rule 0 Step 4 as a bull-case sanity check; not used in any score or fair-value calculation.

---

## 2. GDS Ratio Confirmation (blocking-data-gap check)

**Confirmed: 1 GDS = 1 ordinary common share.**

This is the single most load-bearing number in this session — every per-GDS price, fair value, and order-setup figure downstream depends on it — so it was triangulated multiple independent ways rather than assumed, exactly as the SSU session did for its 1:25 ratio:

1. **A historical press release initially suggested a different ratio — flagged and resolved, not silently used.** SK hynix's own 1994 newsroom press release ("hynix Semiconductor Raises US$1,249,980,000 in Global Depositary Shares") states "one GDS represents 5 common shares." Taking this at face value without further checking would have been a serious error — see point 3 below for why it doesn't apply to the present-day HY9H/ISIN US78392B1070 instrument.
2. **Multi-source textual confirmation on the exact ISIN traded today (US78392B1070, WKN A1JWRE):**
   - Google Finance's own security title for this exact ISIN: **"Hynix Semiconductor Rep[resenting] 1 Ord[inary] Shs[hare] 144A Reg S GDR"**
   - wallstreet-online's security description for the same ISIN: **"Shs Sp Glb Depositary Receipt Repr[esenting] 1 Sh[are] Unitary 144A/Reg S"**
   
   Both independently describe the security as representing exactly **1** ordinary share — not 5. Both reference the identical ISIN (US78392B1070) and WKN (A1JWRE) as IBKR's contract_id 517397504.
3. **Why the 1994 press release's "5 shares" figure does not apply today:** No SK hynix stock split was found in WebSearch results covering 2018–2026 (the only split on record is a 1:21 split on 2003-04-14, decades before this GDS program's current structure) — so a split cannot explain the discrepancy. The most likely explanation is that the 1994 GDS offering was a different, older program with its own ratio that has since been restructured or superseded by the present 144A/Reg S GDR program (ISIN US78392B1070) — but per "never invent or estimate," no further attempt is made to reconcile the two historical figures beyond noting that **today's instrument, identified unambiguously by ISIN, is independently described by two unrelated sources as a 1:1 ratio**, and the price-math cross-check below confirms this decisively.
4. **Independent price-math cross-check, on two dates ~2 months apart:**

   | Date | KRX price (₩) | EUR/KRW FX | Implied GDS price (₩÷FX, 1:1 ratio) | Actual GDS price (€) | Diff % |
   |---|---|---|---|---|---|
   | 2026-04-21 | 1,223,795 | 1,731.72 | €706.69 | €696.00 (yfinance `HY9H.F` close) | **−1.51%** |
   | 2026-06-19/20 | 2,764,000 | 1,754.0 | €1,575.83 | €1,580.00 (yfinance) | **+0.26%** |
   | 2026-06-19/20 | 2,764,000 | 1,754.0 | €1,575.83 | €1,575.00 (IBKR live) | **−0.05%** |

   All three independent checks land within ±1.5%, well inside normal bid/ask spread and cross-listing arbitrage tolerance — decisively confirming the 1:1 ratio and **decisively ruling out** the 1994 press release's 5:1 figure (which would imply a GDS price roughly 5× higher than observed — off by ~80%, not a rounding/spread-level discrepancy).

**Conclusion: the ratio is confirmed (1 GDS = 1 ordinary share). The order-setup mechanics below are NOT blocked on this data gap** — though, as in the SSU session, the gate/score outcome means no order setup is actually produced (Section 7).

---

## 3. Phase 01 Quality Gate (thresholds per [valuation-scoring.md](../framework/valuation-scoring.md))

All inputs sourced from the **primary KRX listing** (000660.KS) via `yfinance`. TTM (trailing twelve months) = sum of the last 4 reported quarters (2026-03-31, 2025-12-31, 2025-09-30, 2025-06-30).

| Metric | Threshold | SK hynix (TTM unless noted) | Basis | Result |
|---|---|---|---|---|
| Gross margin | >40% | **68.34%** | TTM (Gross Profit ₩90.27T / Revenue ₩132.08T) | ✅ PASS |
| Net margin | >12% | **56.89%** | TTM (Net Income ₩75.14T / Revenue ₩132.08T) | ✅ PASS |
| ROIC (Return on Invested Capital — net operating profit after tax ÷ [debt + equity − cash]) | >15% | **48.3–60.5%** (range depends on whether cash-only or cash+short-term-investments is used in the invested-capital denominator) | TTM NOPAT (EBIT × [1 − 14.9% FY2025 effective tax rate]) ÷ latest-quarter invested capital | ✅ PASS (comfortably, either basis) |
| Revenue growth (3yr CAGR) | >8% | **29.61%** | FY2022 (₩44.62T) → FY2025 (₩97.15T), annual basis | ✅ PASS |
| FCF positive 3 consecutive years | Required | **FY2022 FCF = −₩4.97T (NEGATIVE), FY2023 FCF = −₩4.50T (NEGATIVE)**; FY2024 +₩13.13T, FY2025 +₩24.79T | Annual, `yfinance` cashflow statement | ❌ **FAIL** (two consecutive negative years, not one) |
| Net debt/EBITDA | <2.5× | **−0.34×** (net cash position) | (yfinance EV − yfinance MktCap) ÷ TTM EBITDA | ✅ PASS |
| FCF yield | >4% | **2.07%** | TTM FCF (₩40.69T) ÷ market cap (yfinance basis) | ❌ **FAIL** |
| EV/EBIT (Enterprise Value ÷ Earnings Before Interest and Tax) | <20× | **20.57×** | TTM EBIT (₩93.62T), yfinance EV basis | ❌ **FAIL** (marginal — 0.57× over threshold) |

### Why TTM (not FY2025 annual) EBIT was used

Same reasoning as the SSU/MU sessions: SK hynix's **Q1 2026 alone (quarter ended March 2026) posted ₩51.78T of EBIT — more than the company's entire FY2025 fiscal year (₩51.39T)**. This is already-reported, actual quarterly data, not an estimate, and reflects the AI/HBM (High Bandwidth Memory — premium DRAM used in AI accelerators like Nvidia's GPUs) pricing upcycle that intensified sharply through late 2025/early 2026. Using FY2025-only EBIT would give an EV/EBIT of roughly 37.5× (₩1,925.3T EV ÷ ₩51.39T) — a much worse, less-representative gate result. TTM is used as the more current, still entirely actual (not estimated) basis, consistent with the precedent sessions.

### FCF-negative stretch is worse than either MU or SSU showed

SK hynix's FCF was negative for **two consecutive fiscal years** (FY2022: −₩4.97T; FY2023: −₩4.50T) before recovering in FY2024 (+₩13.13T) and FY2025 (+₩24.79T). This is a longer down-stretch than SSU (Samsung: one negative year, FY2023 only) and similar in kind to MU (Micron: one negative fiscal year, FY2023, on a different fiscal calendar). The FCF/Net Income conversion ratio over the same period:

| Year | FCF | Net Income | FCF/NI |
|---|---|---|---|
| FY2022 | −₩4.97T | +₩2.23T | −223% (FCF negative, NI still positive) |
| FY2023 | −₩4.50T | −₩9.11T | 49.4% (both negative) |
| FY2024 | +₩13.13T | +₩19.79T | 66.4% |
| FY2025 | +₩24.79T | +₩42.92T | 57.8% |

The pattern (deeply negative-to-volatile conversion in the downturn, recovering but still below a clean 70%+ in the upcycle years) is consistent with the framework's general skepticism toward capital-intensive cyclicals' cash-generation quality, even when accounting-earnings recovery looks dramatic.

### Gate Result: **❌ FAIL — 3 of 8 criteria fail** (FCF positive 3 consecutive years, FCF yield >4%, EV/EBIT <20×)

This is the same three criteria that failed for SSU (Samsung), and overlaps heavily with MU's four failures (MU additionally failed on revenue CAGR, where SK hynix passes comfortably at 29.61% thanks to the sharper TTM-period revenue inflection). Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), a gate failure should stop the evaluation before scoring. Per this session's specific brief (to document the multi-currency GDS pattern fully, matching the SSU precedent), Phase 02 scoring, the fair-value analysis, and the qualitative review are carried through below for completeness — **but the gate failure stands as the controlling fact for the final recommendation (Section 9).**

---

## 4. Rate Environment Gate (run against US 10Y Treasury, per framework convention)

**Step 1 — Earnings Yield Spread Test**

- Forward PE (correctly derived — see "0y vs +1y" note in Section 5): **9.05×**
- Earnings Yield (EY = 1 ÷ Forward PE) = **11.05%**
- US 10Y Treasury yield = **4.451%** (`^TNX`, 2026-06-18 close — same figure used in the same-day MU session; Friday 2026-06-19 was Juneteenth, a US bond-market holiday, so no fresher print exists)
- Spread = 11.05% − 4.451% = **+6.60 percentage points** → well above the +1.5% threshold → **no extra +5 flag**

**Step 2 — Rate Regime Modifier**

US 10Y at 4.451% falls in the **3.5%–5% band → Modifier = +5** (applied below in the Phase 02 score).

**Note on currency consistency (Rule 6):** the Rate Environment Gate itself stays US-Treasury-based per framework convention regardless of the underlying company's currency. The **DCF discount rate**, by contrast, uses the *Korean* 10Y government bond yield, since the DCF is run in KRW (see Section 6).

**Korean 10Y government bond yield used in the DCF: 4.19%, dated 2026-06-19** — sourced via a direct page fetch of tradingeconomics.com ("The yield on South Korea 10Y Bond Yield rose to 4.19% on June 19, 2026"). This is **only 1 day stale**, a meaningful improvement over the SSU session's figure (3.69%, ~2.5 months stale at the time). ⚠️ However, this figure could not be independently cross-corroborated by a second live source in this session — a WebSearch for the same figure returned only older snippets (3.69% as of 2026-04-01) without surfacing the June figure via search-result text, even though the direct page fetch did return it. Flagged per "never invent, flag what's missing" discipline: the 4.19% figure is used as the best directly-sourced figure available, with this single-source caveat carried forward.

---

## 5. Phase 02 Valuation Score

### 5a. The "0y vs +1y" Forward PE trap (resolved, same issue as MU/SSU)

yfinance's raw `info["forwardPE"]` field returns **6.68×** for SK hynix — but this is computed off the **'+1y' (FY2027E)** consensus EPS estimate (₩413,579.4), not the correct "next fiscal year" forward estimate. Confirmed via `info['lastFiscalYearEnd']` = 2025-12-31 and `info['nextFiscalYearEnd']` = 2026-12-31 that the **'0y' row (FY2026E, ₩305,490.4)** is the fiscal year that should anchor "forward" PE, since FY2026 is the company's current, not-yet-completed fiscal year.

**Correct Forward PE = ₩2,764,000 ÷ ₩305,490.4 = 9.05×** (vs. the misleading 6.68× yfinance reports by default)

### 5b. FCF Yield Sub-score (40% weight)

```
FCF_Score = clamp(100 × (1 − FCF_Yield% / 10), 0, 100)
FCF Yield (TTM) = 2.07%
FCF_Score = 100 × (1 − 2.07/10) = 79.3
```

**FCF_Score = 79.3** — TTM FCF Yield of 2.07% is well below the 4% Phase 01 threshold, so this sub-score is unsurprisingly poor (high score = expensive on this metric).

*Owner Earnings (Upgrade 1) check*: SK hynix's TTM capex is 42.4% of operating cash flow — high, but this is overwhelmingly capacity expansion for DRAM/HBM/NAND fabrication (the $20.5B 2026 capex plan is explicitly earmarked for HBM4 capacity and EUV lithography expansion, plus the $12.85B P&T7 advanced-packaging investment), not the kind of discretionary cloud/AI-infrastructure growth capex Upgrade 1 targets (Azure-style buildout for MSFT/META/GOOGL/AMZN). SK hynix is not on Upgrade 1's affected-business list, and no management breakdown of "maintenance vs. growth" capex was found that would support an Owner Earnings substitution without estimating it. Per "never invent or estimate financial data," reported FCF is used as-is.

### 5c. EV/EBIT Sub-score (40% weight — PEG's 15% redistributed here; see 5e)

```
EV/EBIT_Score = clamp((EV/EBIT − 12) / 23 × 100, 0, 100)
EV/EBIT (TTM) = 20.57×
EV/EBIT_Score = (20.57 − 12) / 23 × 100 = 37.26
```

**EV/EBIT_Score = 37.26**

Unlike Samsung's consolidated multiple in the SSU session, **no segment-mix adjustment is needed here** — SK hynix is a pure-play memory company (DRAM, NAND, HBM), so its consolidated EV/EBIT directly reflects its actual memory business economics, with no diluting non-memory segment to correct for. This is the "simpler business mix" referenced in the task brief.

### 5d. Forward PE Sub-score (20% weight)

5-year historical PE range reconstructed via the documented `yfinance` automation (`get_earnings_dates(limit=40)` + rolling TTM EPS + price pairing). **50 quarters of real Reported EPS history** were returned, back to 2013-10-28 — ample depth. Of these, 41 quarters had positive TTM EPS (9 quarters during the FY2023 trough period were excluded as TTM EPS ≤ 0, per the documented exclusion rule for undefined/negative PE).

Three candidate 5-year readings were computed, mirroring the MU session's transparency approach (the loss-period exclusion forces the lookback window to stretch past a clean trailing 5 calendar years to reach 20 valid quarters):

| Reading | n | Avg PE | Low PE | High PE | Resulting FwdPE_Score |
|---|---|---|---|---|---|
| **Mechanical "last 20 valid quarters" (primary, used below)** | 20 | 15.31× | 4.81× | 52.33× | 0.0 (after modifier) |
| True trailing 5-calendar-year window (2021-06-20 to today) | 15 | 13.15× | 4.81× | 52.33× | 0.0 (after modifier) |
| Same, excluding the 52.33× outlier (2024-07-25 — itself a trough-recovery artifact, see below) | 14 | 10.35× | 4.81× | 27.81× | 18.4 (no modifier triggered) |

The **primary reading** (mechanical last-20-valid-quarters, per [valuation-scoring.md](../framework/valuation-scoring.md)'s documented method) is used for the score below; the sensitivity range (final total score 51.6–55.3 across all three readings, computed in Section 5f) does not change the action band, so this ambiguity is flagged but not load-bearing for the recommendation.

```
FwdPE_Score (primary, range-based) = clamp((9.05 − 4.81) / (52.33 − 4.81) × 100, 0, 100) = 8.92
```

**Historical PE Modifier (Upgrade 2):** Forward PE (9.05×) sits **40.9% below** the 5-year average (15.31×) — well past the ">20% below average" threshold → **−10 modifier** applied.

```
FwdPE_Score (final) = clamp(8.92 − 10, 0, 100) = 0.0
```

⚠️ **Cyclical-earnings-trough distortion flagged — same pattern as SSU's Samsung session.** The 5yr-high data point (52.33×, 2024-07-25) is a classic cyclical artifact: this print sits right after the FY2023 trough (EBIT had collapsed from +₩4.54T in FY2022 to **−₩10.19T** in FY2023 — a ₩14.7T swing into outright loss), so the TTM-EPS denominator was still severely depressed at that point even as the share price had begun pricing in recovery — a transient PE spike from a near-zero/recovering-earnings base, not genuine valuation excess. This means the 5-year average (15.31×) may itself be modestly inflated by this single distorted quarter, meaning today's −40.9% deviation could overstate how "cheap" SK hynix's forward PE looks relative to a less-distorted average — directionally the same caveat the SSU session raised about Samsung's own 32.62× high-water mark. No adjusted average is fabricated here; the sensitivity table above shows the alternative reading (excluding the outlier) explicitly instead.

### 5e. PEG Sub-score — N/A, excluded (Upgrade 3)

SK hynix's trailing EPS growth (FY2023's outright loss recovering to FY2025's record profit, with Q1 2026 EPS alone of ₩56,670 vs. ₩11,411 a year earlier) would technically clear a Lynch "Fast Grower" >15%-for-3-years bar by the raw numbers — but Upgrade 3 explicitly states PEG must **"Never apply to cyclicals or stalwarts,"** regardless of trailing growth math. Memory semiconductors (DRAM, NAND, HBM) are a textbook cyclical industry with a well-documented multi-year boom-bust history (SK hynix's own FY2022→FY2023 EBIT swing from +₩4.54T to −₩10.19T is direct, recent evidence), and the current growth spurt is unambiguously the cyclical AI/HBM-driven 2025–2026 upswing, not durable secular compounding. **PEG is excluded per the task's explicit instruction; its 15% weight is redistributed to EV/EBIT** (already reflected as the 40% weight used in Section 5c).

### 5f. Final Score Calculation

```
Weighted score = (FCF_Score × 0.40) + (EV/EBIT_Score × 0.40) + (FwdPE_Score × 0.20)
                = (79.3 × 0.40) + (37.26 × 0.40) + (0.0 × 0.20)
                = 31.72 + 14.90 + 0.0
                = 46.62

Final Score = Weighted score + Rate Regime Modifier
            = 46.62 + 5
            = 51.62 → rounds to 51.6
```

**Sensitivity (alternative 5yr-PE readings, see Section 5d):** using the "true trailing 5yr, excluding outlier" reading instead of the primary mechanical reading would give a FwdPE_Score of 18.4 (no modifier triggered) instead of 0.0, producing a final score of **55.3** — still in the same action band (see below). The primary 51.6 figure is used as the reported result, with this range flagged.

### **Phase 02 Final Score: 51.6 / 100.0 → "HOLD — watch only, no new entry" band (50.0–69.9)**

Per [operating-brief.md](../framework/operating-brief.md)'s Action Table: Score 50.0–69.9 = **HOLD — watch only, no new entry, no trim** (the "Fair Value" band). This is the same action band SSU's 52.7 landed in.

---

## 6. Fair Value Analysis (shown for completeness, despite the Phase 01 gate failure already pointing toward no new entry)

All fundamentals in KRW (Rule 6 — currency consistency).

### 6a. Discounted Cash Flow (DCF), 3-stage, in KRW

**WACC (Weighted Average Cost of Capital) build:**
- Risk-free rate: Korean 10Y govt bond, **4.19%** (2026-06-19, see Section 4 sourcing/staleness note)
- Equity risk premium: 5.0% (standard mature-market assumption)
- Beta: 1.2 (memory-sector cyclicality premium over 1.0 — set slightly higher than Samsung's 1.1 in the SSU session, since SK hynix is a pure-play memory company with no conglomerate diversification dampening its earnings/share-price volatility)
- Cost of equity = 4.19% + 1.2×5.0% = **10.19%**
- Cost of debt (pre-tax): **4.25%** — not an assumed figure; this is the actual coupon on an outstanding SK hynix bond (11-Sep-2028 maturity, found via WebSearch), used as a market-observed proxy rather than an invented spread-over-risk-free-rate assumption. S&P upgraded SK hynix to BBB+ (positive outlook) in February 2026, citing strong HBM-driven profitability — consistent with this being an investment-grade, not distressed, cost of debt.
- After-tax cost of debt = 4.25% × (1 − 14.9% effective tax rate) = **3.62%**
- Capital structure weights: debt is only ~1.1% of total capital (market-cap-weighted) — SK hynix carries modest leverage (unlike Samsung's outright net-cash position, SK hynix has ₩21.8T total debt against ₩54.4T cash+short-term-investments, i.e. still net-cash but with more gross debt on the balance sheet)
- **WACC ≈ 10.12%**

**Cash flow base:** TTM FCF = ₩40.69 trillion

**Stage 1 (Years 1–5):** Decelerating growth off the current AI/HBM upcycle peak — 25%, 18%, 12%, 8%, 5% (explicitly modeling cyclical fade, not flat extrapolation of the current upswing; the first-year rate is set higher than Samsung's 18% in the SSU session because SK hynix's HBM exposure and TTM growth trajectory are both stronger — see Section 8)
**Stage 2 (Years 6–10):** Further fade — 4.5%, 4.0%, 3.5%, 3.0%, 2.5%
**Terminal growth:** 2.0% (long-run KRW nominal-economy proxy, same as the SSU precedent)

| | Enterprise Value | + Net Cash (₩32.53T) | = Equity Value | ÷ Shares (708.3M) | FV/share |
|---|---|---|---|---|---|
| DCF | ₩874.23T | +₩32.53T | ₩906.76T | | **₩1,280,199** |

Terminal value = 49.6% of EV — within a normal range, not a red flag on its own (below the framework's 75% extend-Stage-2 trigger).

**DCF says fair value (₩1,280,199) is 53.7% *below* the current price (₩2,764,000)** — i.e., the DCF sees SK hynix as significantly overvalued at the current price. As with Samsung in the SSU session, the reason is a **cash-vs-earnings divergence**: the DCF is anchored to TTM FCF (₩40.69T), which still reflects heavy ongoing capex (42.4% of operating cash flow) for HBM4/EUV capacity expansion, while TTM EBIT (₩93.62T) has already fully captured the AI/HBM earnings spike. The multiples-based signals in Section 5 (Forward PE, EV/EBIT) look only moderately expensive because they're earnings-anchored; the DCF looks much more expensive because it's cash-anchored and cash conversion lags the earnings recovery. **This divergence is a genuine finding, not a modeling error**, flagged per Rule 6.

### 6b. Comparable Multiples

**Rule 5 scale-band check (peer revenue must be within ±50% of SK hynix's TTM revenue, $86.34B at the live USD/KRW rate of 1,529.89):**

| Peer | TTM Revenue (USD) | % of SK hynix | Within ±50% band ($43.17B–$129.50B)? |
|---|---|---|---|
| Micron (MU) | $58.12B | 67.3% | ✅ **Yes** — only in-band, directly-EBIT-computable peer |
| Western Digital (WDC) | $11.78B | 13.6% | ❌ No — too small |
| Kioxia (285A.T) | $14.49B | 16.8% (revenue convertible, but no usable EBIT line — quarterly statements carry only EPS/share-count rows, same data gap the MU session flagged) | ❌ No (also a data gap, like MU's session found) |
| Samsung Electronics DS segment (memory+foundry) | ~$85.0B (from SSU session, FY2025 official segment data) | 98.4% | ✅ In-band on revenue, but **no standalone EV exists for a segment of a consolidated company** — cannot compute a segment-level EV/EBIT without a sum-of-the-parts allocation, which the SSU session did not attempt for DS specifically (it solved the opposite direction: allocating Samsung's own EV across segments, not deriving a DS-only multiple to apply elsewhere) |

**This leaves only Micron (MU) as a usable, in-band, directly-computable EV/EBIT peer — a single-peer comparison, which is a real limitation flagged explicitly (Rule 5 calls for "minimum 5 peers, maximum 10," not achievable here given the small global pool of scale-matched, EBIT-disclosing pure-play memory companies).**

- MU TTM EV/EBIT (recomputed this session, matches the same-day MU session's own figure exactly): **45.03×**
- WDC TTM EV/EBIT (out-of-band, shown for context only): **35.37×**

```
Peer multiple applied (MU only, n=1, in-band): 45.03×
Implied EV = SK hynix TTM EBIT (₩93.62T) × 45.03 = ₩4,215.5T
− Net Debt (−₩32.53T, i.e. + net cash) = Implied Equity Value ₩4,248.1T
÷ Shares (708.3M) = Implied FV per share ≈ ₩5,997,585
```

**This implies SK hynix is +117.0% *undervalued* vs. its only available scale-matched EV/EBIT peer** — the opposite signal from the DCF.

⚠️ **This result must be read with real caution, not taken at face value — flagged prominently, same discipline as the SSU session's segment-mix flag.** MU's own 45.03× EV/EBIT was independently flagged, in the same-day MU evaluation, as priced "at what looks like peak-cycle pricing" — Micron trades at roughly 10× its own 52-week low and within 1.3% of its 52-week high, on TTM earnings the MU session itself called "inflated by a single extraordinary quarter." Applying an already-flagged-as-extreme peer's multiple to SK hynix's own already-elevated TTM EBIT does not produce a trustworthy independent valuation signal — it largely just transmits one cyclical's peak-pricing distortion onto another. A sensitivity check including WDC despite its band failure (simple 2-peer average, 40.20×) gives a somewhat more moderate but still strongly positive implied FV of ₩5,359,199 (+93.9% vs. current price).

**No clean, undistorted peer multiple is available this cycle** — this is itself a finding: when an entire peer group (SK hynix, Micron, Samsung's DS segment, by extension) is mid-upcycle simultaneously, comparable-multiples valuation loses much of its power to triangulate, because there is no genuinely "normal-cycle" comparable trading anywhere in the peer set right now. This is flagged as a structural limitation of the comps approach for this name at this point in the cycle, not a data-quality problem with any single input.

### 6c. Blended Fair Value

Per the established 40% DCF / 60% multiples blend (precedent-session convention), using the MU-only (Rule-5-compliant) multiples figure as primary:

```
Blended FV (primary) = (₩1,280,199 × 0.40) + (₩5,997,585 × 0.60) = ₩4,110,631 per ordinary share
```

**Sensitivity** (using the 2-peer MU+WDC average instead, despite WDC's band failure): ₩3,727,599 per ordinary share.

```
Blended FV vs. current price (₩2,764,000):
  Primary:     +48.7% (price is BELOW blended FV)
  Sensitivity: +34.9% (price is BELOW blended FV)
```

**Unlike SSU and MU, this session's blended fair value sits *above* the current price under both readings** — driven almost entirely by the comparable-multiples leg, since the DCF leg independently still says the stock is ~54% *overvalued*. This is a genuinely different and more ambiguous signal than either precedent session produced, and is explained, not glossed over, in Section 6b: the multiples-based "undervaluation" signal rests on a single available peer (MU) that is itself independently flagged as trading at peak-cycle pricing. **This blended FV should not be read as "the stock is cheap" — it should be read as "the comps-based leg of this triangulation is currently unreliable, because there is no undistorted peer to anchor it to."** The DCF, which is built from SK hynix's own cash flows rather than a peer's potentially-distorted multiple, is arguably the more trustworthy of the two methods this cycle, and it says the opposite: the stock is overvalued by about 54% against an FCF-anchored intrinsic value.

### 6d. Conversion to EUR per GDS

```
Blended FV per ordinary share (primary): ₩4,110,631
× GDS ratio (1 ordinary share per GDS, confirmed Section 2): ₩4,110,631 per GDS
÷ EUR/KRW FX rate (1,754.0): €2,343.58 per GDS (blended fair value)
```

| | Value |
|---|---|
| **Blended Fair Value per GDS (primary)** | **€2,343.58** |
| **Live GDS price** | **€1,580.00** (yfinance) / €1,575.00 (IBKR) |
| **Live price vs. blended FV** | **−32.6%** (price is *below* blended FV, not above) |

This is the inverse of the SSU finding (where the live price sat ~86% *above* blended FV). Given the caveat in Section 6c about the comps leg's reliability this cycle, this −32.6% reading is **not treated as a buy signal** — see Section 9 for why the gate failure and Phase 02 score band control the recommendation regardless of this number.

---

## 7. Order Setup — NOT computed

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [operating-brief.md](../framework/operating-brief.md), buy price / sell target / stop loss / R/R (risk/reward ratio) / position sizing are only constructed for an actual entry recommendation. Given:
- The Phase 01 quality gate **fails** on 3 criteria, and
- The Phase 02 score (51.6) sits in the **"HOLD — watch only, no new entry"** band (50.0–69.9), and
- The independent DCF (Section 6a) — arguably the more trustworthy leg of the fair-value triangulation this cycle, per the comps-reliability caveat in 6b/6c — shows the live price at roughly **+116% above** DCF-only intrinsic value (₩2,764,000 vs. ₩1,280,199),

there is no scenario under this framework's rules that supports a buy order here. Order setup mechanics are not applicable.

---

## 8. Five Qualitative Questions

**1. Why are margins high?**
SK hynix's TTM gross margin (68.34%) and net margin (56.89%) are dramatically higher than what the same company posted just two-to-three years ago (FY2023: outright negative gross profit and net loss). This is **overwhelmingly cyclical, not structural** — a severe, AI-demand-driven up-cycle in DRAM and especially HBM pricing, colliding with supply that takes years to add (memory fabs have multi-year lead times). There is a real structural component too — SK hynix has the clear technology lead in HBM (estimated 54–80% share of Nvidia's 2026 HBM4 demand depending on source, vs. Samsung's ~25–30% and Micron's ~18%, per multiple WebSearch sources this session) — but the *magnitude* of today's margins is a cycle signal layered on top of a real but more modest structural edge.

**2. What would it take to compete with them?**
Enormous capital intensity (SK hynix's 2026 capex alone is ~$20.5B, plus a separate $12.85B HBM packaging investment), multi-year process-node learning curves, and — critically for HBM specifically — deep, sticky customer-qualification relationships with Nvidia and TSMC (described in WebSearch results as a "triadic" alliance). SK hynix is not uniquely protected from competition in the way a software moat would be — Samsung and Micron clear largely the same technical bar in DRAM/NAND — but in HBM specifically, SK hynix's first-to-market TSV (Through-Silicon Via) packaging experience and accumulated mass-production trust appear to be a genuine, if not unassailable, lead over both peers as of mid-2026.

**3. How has management allocated capital over 5–10 years?**
Heavy, sustained reinvestment into DRAM/NAND/HBM capacity — capex has consistently run in the 30–45% of operating cash flow range, and management has explicitly stated a policy of capping capex near "mid-30% of sales on a three-year moving average." The company is doubling memory wafer capacity over the next five years per its chairman's public statements, betting that AI-driven shortages persist through at least 2030. This is a capital allocation pattern of aggressive, concentrated reinvestment into the company's single core business (no major diversification attempts, unlike Samsung) — high-conviction, high-cyclical-risk capital allocation, not a diversified-hedge approach.

**4. Where is growth coming from next 3–5 years?**
Almost entirely **HBM** (high-bandwidth memory for AI accelerators) and the broader AI-driven DRAM/NAND demand wave. SK hynix is the clear current leader in HBM (multiple sources put its 2026 HBM4/Nvidia-demand share between 54% and 80%, vs. Samsung's ~25–30% and Micron's ~18%) — a meaningfully stronger competitive position in this specific growth driver than either of the other two pure-play/DS-segment peers evaluated this session. Secondary growth could come from conventional DRAM (SK hynix expects >20% year-on-year DRAM demand growth in 2026) and NAND, though management is reportedly taking a more conservative approach to NAND capex specifically to avoid oversupply risk.

**5. Best bear case against owning it?**
(a) **Cyclicality risk, the dominant risk**: SK hynix's own FY2022→FY2023 history is the clearest possible evidence — EBIT swung from +₩4.54T to **−₩10.19T** in a single year, an apples-to-apples demonstration that this business can and does post outright losses when the memory cycle turns. Today's TTM-based "reasonable" multiples (EV/EBIT 20.57×, forward PE 9.05×) could look very different in 12–24 months if the AI/HBM cycle peaks and rolls over — exactly the dynamic Upgrade 3's "never apply PEG to cyclicals" rule and the cyclical-PE-trough flag in Section 5d both exist to guard against. (b) **Capacity-addition oversupply risk**: WebSearch results explicitly flag that SK hynix's own aggressive five-year capacity-doubling commitment, if AI infrastructure spending decelerates before the additional supply is absorbed, could itself create the next down-cycle — the same supply-side mechanism that caused FY2023's collapse. (c) **The DCF/multiples divergence (Section 6) cuts the other way from SSU here, but is still a bear signal once properly read**: the only available scale-matched peer multiple (Micron) is itself flagged as priced for perfection, meaning the "SK hynix looks cheap vs. peers" signal is largely an artifact of comparing one cycle-peak valuation to another, not a genuine mispricing finding — the FCF-anchored DCF, less contaminated by this effect, says the stock is roughly 54% overvalued. (d) **Geographic/geopolitical concentration**: SK hynix's fabs and corporate base are concentrated in South Korea, carrying korean-peninsula geopolitical tail risk that a more globally diversified peer would not (not separately modeled here, but worth flagging qualitatively).

**Disruption vector check:** No imminent technology shift threatens to make DRAM/NAND/HBM irrelevant within 5 years — if anything, AI compute demand is reinforcing the value of advanced memory, exactly as in the MU and SSU sessions. The more relevant risk is the cyclical supply/demand mismatch described above, not paradigm disruption.

---

## 9. Recommendation: **PASS / WATCHLIST ONLY**

**The Phase 01 quality gate fails on 3 of 8 criteria** (FCF positive 3 consecutive years — both FY2022 and FY2023 were negative; FCF yield >4% — actual 2.07%; EV/EBIT <20× — actual 20.57×, a marginal 0.57× over threshold). Per the framework's own process discipline, a gate failure should stop the evaluation before scoring — this session carried the analysis through to completion regardless (per this evaluation's specific brief, to fully document the multi-currency/GDS pattern and its variant findings), but **the gate failure is the controlling fact**.

Even setting the gate aside, the **Phase 02 score of 51.6 lands in the "HOLD — watch only, no new entry" band (50.0–69.9)** — not "Buy" at any conviction level.

**The fair-value picture here is genuinely more ambiguous than either the MU or SSU sessions produced**, and that ambiguity is itself worth carrying forward explicitly rather than averaging away: the DCF (anchored to SK hynix's own actual cash flows) says the stock is roughly 54% *overvalued*; the only available scale-matched comparable multiple (Micron, itself independently flagged elsewhere this session as priced at cycle-peak) implies the stock is roughly 117% *undervalued*. The blended 40/60 figure that results (+48.7% upside to blended FV) should not be read as a buy signal — it is largely an artifact of blending one genuinely cash-based estimate against one comps-based estimate that has no clean, undistorted peer to anchor to this cycle. The DCF, built from the company's own numbers rather than a possibly-distorted peer's multiple, is treated here as the more trustworthy of the two legs.

**No order setup is applicable.** This is added to the not-in-portfolio watchlist for future monitoring (next quarterly earnings, expected late July 2026, plus any signs of the AI/HBM cycle decelerating or oversupply emerging, would be natural re-evaluation triggers), but does not support an entry today under this framework's rules.

---

## 10. Data quality flags carried forward (summary)

- **Korean 10Y government bond yield**: sourced as 4.19% (2026-06-19) via a single direct page fetch of tradingeconomics.com; could not be independently cross-corroborated by a second live source within this session (WebSearch snippets only surfaced an older 3.69%/2026-04-01 figure). Used in the DCF discount rate; flagged for a second-source check at next review.
- **GDS ratio**: confirmed 1:1 via two independent textual sources plus a price-math cross-check on two dates ~2 months apart (−1.51%, +0.26%, and −0.05% deviations, all well within tolerance) — high confidence, but flagged that a 1994 SK hynix press release stated a conflicting 5:1 ratio for what is very likely a different, since-superseded GDS program; this discrepancy was investigated (no stock split found that would explain it) but not fully reconciled to a documented root cause beyond "an older program, not today's ISIN."
- **Cost of debt in the DCF WACC build**: used the actual coupon (4.25%) on a real, named SK hynix bond (11-Sep-2028 maturity) found via WebSearch, rather than an assumed credit spread — a market-observed proxy, not an invented figure, but flagged since it is one specific bond's coupon, not a yield-to-maturity or a full corporate curve.
- **Single-peer (n=1) comparable-multiples set**: only Micron (MU) passed the Rule 5 ±50% scale-band test with a directly computable EV/EBIT; Western Digital (too small) and Kioxia (data gap, no usable EBIT in its quarterly statements) were excluded. Samsung's DS segment is scale-matched on revenue but has no standalone EV to compute a segment multiple from. This single-peer limitation, combined with MU's own multiple being independently flagged as cycle-peak-distorted, materially weakens the comps leg of the fair-value triangulation this cycle — flagged prominently in Sections 6b/6c/9 rather than glossed over.
- **5yr historical PE window ambiguity**: the documented mechanical "last 20 valid quarters" method spans nearly 6 calendar years (not a clean trailing 5) because 9 quarters during the FY2023 loss period were excluded as undefined-PE. Three candidate readings produce a final-score sensitivity range of 51.6–55.3 — same action band throughout, so not load-bearing for the recommendation, but flagged per the MU session's precedent for transparency.
- **ROIC denominator choice** (cash-only vs. cash+short-term-investments basis for invested capital) produces a 48.3%–60.5% range — both comfortably clear the >15% threshold, so the ambiguity doesn't affect the gate result, but is flagged for consistency with future re-scores.

---

## 11. Token usage note

This session involved two live price sources (yfinance primary + a since-resolved IBKR snapshot used as secondary cross-check, unlike the prior session's hang on this same contract), ~12 rounds of yfinance/Python data pulls (SK hynix TTM/annual/quarterly reconstruction, a 50-quarter historical-PE series build, 2 peer companies' TTM figures, 2 FX pairs), 8 WebSearch/WebFetch calls (GDS ratio corroboration ×5, Korean bond yield ×2, credit rating/bond-coupon sourcing ×1, qualitative/competitive research ×2), and a full DCF + single-peer-multiples build with an explicit reliability caveat on the comps leg — consistent with the ~120–160K token/ticker range cited in [.claude/commands/new-position.md](../.claude/commands/new-position.md)'s batch-processing guidance, similar in scope to the SSU session given the shared GDS-ratio-confirmation overhead, despite SK hynix's simpler (non-conglomerate) business mix removing the segment-mix/SOTP work that SSU required.
