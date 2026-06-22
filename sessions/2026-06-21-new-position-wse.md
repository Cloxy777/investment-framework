# New Position Evaluation: WSE (Wise plc) — 2026-06-21

**Task type:** NEW POSITION
**Ticker:** WSE — NASDAQ (secondary listing, dual-listed since 2026-05-11), IBKR contract_id 881566839. Primary listing remains LSE under WISE / WISE.L, IBKR contract_id 881108665.
**Company:** Wise plc (formerly TransferWise) — cross-border payments fintech: international money transfer, multi-currency account, debit card, and the "Wise Platform" B2B infrastructure product.
**Analyst:** Claude (automated session)
**Trigger:** Routine 6 (Telegram Stock-Mention Scan) — [t.me/bolshegold post #9602](https://t.me/bolshegold), 2026-06-21 ~18:02 UTC, named Wise in a "stocks reporting this week" round-up (gist: AML investigation update and customer-growth trajectory to watch at this week's earnings). Per CLAUDE.md Rule 0, the post is used only as a trigger to look at this ticker — no number from it is used anywhere below; every figure here was pulled fresh.
**Batch context:** Companion session to BULL, CCL, SOFI (same Telegram-scan trigger batch, evaluated independently).

---

## 0. Ticker identity and dual-listing currency handling

WSE = Wise plc, confirmed. It began trading on NASDAQ under "WSE" on 2026-05-11; the original/primary listing remains LSE under "WISE" (WISE.L). **Both listings represent the same underlying company and the same GBP-denominated financial statements** — confirmed directly: `yfinance`'s `financialCurrency` field returns `GBP` for *both* tickers, and the FY2025 income-statement/cash-flow/balance-sheet figures pulled from each ticker object are identical.

**Currency handling used throughout this session:**
- All fundamentals (revenue, EBIT, EBITDA, net income, FCF, debt, cash) are sourced and shown in **GBP** (the reporting currency).
- The live **GBP/USD** rate used for every conversion is **1.319209** (yfinance `GBPUSD=X`, fetched live this session, timestamped 2026-06-21).
- Every multiple/ratio below states which currency basis it was computed on, and cross-checks the other basis where feasible (see §1, §2).
- **5-year historical PE:** WISE.L's price history only goes back to **2021-07-01** (Wise's direct listing on the LSE) — under 5 years — and `get_earnings_dates(limit=40)` returns **no historical reported EPS at all** for either ticker (only the single upcoming 2026-06-25 date, with `Reported EPS` = NaN). The 5yr-avg-PE reconstruction method in valuation-scoring.md cannot be run here; this is a genuine **no-history case**, not a judgment call — flagged explicitly per "never invent or estimate financial data," and the documented **No-history fallback (FwdPE_Score = 50.0)** is used in §4.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Price | Timestamp / notes |
|---|---|---|
| **yfinance NASDAQ:WSE** (`history`, daily) | **$10.84** (close) | Thu 2026-06-18 close — most recent NASDAQ session (today, 2026-06-21, is a Sunday; markets closed) |
| **yfinance LSE:WISE.L** (`history`, daily) | **818.0 GBp = £8.18** | Fri 2026-06-19 close (one session more recent than NASDAQ's, since LSE was open Friday) |
| **IBKR snapshot, NASDAQ contract 881566839** | $11.17, `is_close: true` | This is **Wed 2026-06-17's** close, not Thursday's — **one session more stale** than yfinance's NASDAQ print. Flagged, not used. |
| **IBKR snapshot, LSE contract 881108665** | £8.20 (820.0 GBp), `is_close: true` | Matches yfinance's LSE *previous*-close field (820.0) one session behind the 818.0 Friday close — internally consistent, both sources agree Friday's close was 818.0/£8.18 once cross-checked against yfinance's own `previousClose`. |

**Price used: $10.84 (NASDAQ:WSE, Thu 2026-06-18 close)** as the primary live price for USD-denominated order setup, cross-checked against **£8.18 (LSE:WISE.L, Fri 2026-06-19 close)** converted at the live FX rate: $10.84 ÷ 1.319209 = £8.217 vs. the actual LSE print of £8.18 — a 0.45% difference, consistent with one extra trading session's movement (Thu→Fri) plus FX-rate timing noise, not a data error.

**52-week range:** NASDAQ:WSE $10.36–$17.47 (yfinance); LSE:WISE.L £7.54–£11.64 (754.0–1164.0 GBp). The stock is trading **near its 52-week low** on both listings — within 4.6% of the NASDAQ low and within 8.5% of the LSE low.

**Analyst consensus PT:** LSE (18 analysts, more statistically robust): mean **1167.4p (£11.674)**, median 1202.5p, range 760–1425p, recommendation "buy." NASDAQ (only 6 analysts): mean $16.99, median $16.70, range $16.00–$19.00, recommendation "strong_buy." Both imply substantial upside from the live price (+42.7% LSE mean, +56.8% NASDAQ mean) — used only as a bull-case sanity check per Rule 0 Step 4, not as an input to fair value.

**Why the price is depressed (fundamental driver, not unexplained price action):** WebSearch confirms a **Belgian AML (Anti-Money Laundering) investigation** became public around 2026-06-01 — Brussels prosecutors investigating ~€500M in suspicious transactions across 30+ European countries routed through Wise's Belgium-based EU subsidiary, reported as "in advanced stages, nearing conclusion." Shares fell 15-20% intraday on the news (Bloomberg, Finextra, CityAM, AML Intelligence). This is exactly the kind of **documented fundamental trigger** Rule 9 requires before any re-valuation — not a bare price move. **Wise's FY2026 (year ended 2026-03-31) full-year results are due Thursday 2026-06-25** (4 days from today) and are expected to address both the AML investigation and growth trajectory — matching the Telegram post's framing, used here only as confirmation that earnings are imminent, not as a data source.

---

## 2. Data Gathered (Phase 01 & 02 inputs)

### Annual financials (FY ends 31 March; GBP) — `t.financials`, WISE.L

| FY (ended) | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| FY2022 | £563.8M | £369.1M | £48.3M | £71.2M | £32.9M | £0.0318 |
| FY2023 | £986.3M | £638.2M | £156.5M | £179.7M | £114.0M | £0.1094 |
| FY2024 | £1,537.2M | £1,092.4M | £501.7M | £520.0M | £354.6M | £0.3373 |
| FY2025 | £1,806.2M | £1,307.8M | £580.2M | £598.6M | £416.7M | £0.3973 |

Only **4 fiscal years** of data exist via `yfinance` — Wise direct-listed on the LSE in July 2021, so FY2022 was its first full year as a public company. Gross margin 72.4% (FY25), net margin 23.1% (FY25) — both comfortably above Phase 01 thresholds, but the **multi-year trend (5.8%→11.6%→23.1%→23.1% net margin)** reflects a young, scaling business maturing into profitability, not a steady-state mature compounder. Flagged for context, consistent with this session's qualitative notes (§6).

### Annual cash flow (GBP) — `t.cashflow`, WISE.L

| FY | OCF | CapEx | "Free Cash Flow" (statement line) | "Change in Working Capital" |
|---|---|---|---|---|
| FY2022 | £3,138.0M | −£11.9M | £3,126.1M | £2,996.2M |
| FY2023 | £3,919.9M | −£8.8M | £3,911.1M | £3,808.4M |
| FY2024 | £3,248.9M | −£13.0M | £3,235.9M | £2,883.4M |
| FY2025 | £4,494.4M | −£35.4M | £4,459.0M | £4,096.4M |

**⚠️ Critical data-quality flag — the statement "Free Cash Flow" line is not usable as-is.** Wise is a regulated cross-border payments business that holds **customer/client balances in transit** (safeguarded/segregated funds — e.g. £19.7B in H1 FY2025 per Wise's own FY2025 annual report, confirmed via WebSearch). These balances flow through as "Change in Working Capital" / "Change in Payable" in the cash-flow statement and **dominate** the reported OCF and FCF lines — e.g. FY2025's £4,096.4M working-capital swing is 92% of the £4,459.0M "FCF" figure. This is float from money in transit on behalf of customers, not cash the company generates or can deploy for itself. Using the raw statement FCF would overstate FCF yield by roughly **10x** (see computed ratios below) — the same character of error this framework's Owner Earnings adjustment (Upgrade 1) and the SPGI price-inference lesson both warn against: using a reported number whose composition doesn't match what it's being used to measure.

**Adjustment applied (necessary to make any ratio meaningful, not a substitution for missing data):**
```
Adjusted FCF = Operating Cash Flow − Change in Working Capital + Capital Expenditure
```
This strips the customer-balance swing out of OCF, leaving the cash flow generated by Wise's own operations, then nets CapEx as normal.

| FY | Adjusted FCF (GBP) | Statement FCF (GBP, for contrast) |
|---|---|---|
| FY2022 | £129.9M | £3,126.1M |
| FY2023 | £102.7M | £3,911.1M |
| FY2024 | £352.5M | £3,235.9M |
| FY2025 | £362.6M | £4,459.0M |

All four years of Adjusted FCF are **positive** — satisfies Phase 01's "FCF positive 3+ consecutive years" on the corrected basis (statement-line FCF, despite being inflated, would also show all-positive years, but for the wrong reason — flagged so the pass isn't read as validating the unadjusted number).

### Balance sheet (GBP) — `t.balance_sheet`, WISE.L, plus company-disclosed "own cash"

| Metric | yfinance raw line | Correction applied |
|---|---|---|
| Total Debt (FY25) | £185.6M | Used as-is |
| "Cash And Cash Equivalents" (FY25, yfinance) | £8,175.3M | **Not used** — conflates ~£8B+ of safeguarded customer balances with Wise's own cash |
| **"Own cash"** (FY25, company-disclosed) | — | **£1.4B**, vs. £1.1B at FY2024 end — sourced via WebSearch directly from Wise's 5 June 2025 FY2025 results commentary, cross-checked: this is explicitly described as *"not related to customer funds... held in segregated safeguarding accounts"* |
| Stockholders' Equity (FY25, yfinance) | £1,386.2M | Consistent with (and corroborates) the £1.4B own-cash figure — Wise's customer balances sit as matched assets/liabilities that largely net out of equity |

**Corrected Net Debt (FY25) = £185.6M − £1,400M = −£1,214.4M** (net cash of £1,214.4M on Wise's *own* balance sheet) — materially different from the −£7,989.7M "net cash" figure the unadjusted yfinance cash line would imply.

### Computed ratios — corrected basis (FY2025 financials + live prices + live FX)

```
GBP/USD (live)         = 1.319209
Shares outstanding      = 1,000,264,562

Market Cap (USD, NASDAQ basis) = $10.84 × 1,000,264,562 = $10.843B
Market Cap (GBP, LSE basis)    = £8.18 × 1,000,264,562  = £8.182B   (cross-check: $10.843B / 1.319209 = £8.218B — 0.4% apart, consistent with the one-session price-timing gap noted in §1)

Net Debt (corrected)   = £185.6M − £1,400M = −£1,214.4M  (net cash)
EV (GBP)                = £8.182B + (−£1.2144B) = £6.968B
EV (USD, via live FX)   = $10.843B + (−£1.2144B × 1.319209) = $10.843B − $1.602B = $9.241B

EV/EBIT (FY25 EBIT £580.2M)    = £6.968B / £580.2M  = 12.01×   (USD cross-check: $9.241B / ($580.2M×1.319209=$765.4M) = 12.07× — consistent)
EV/EBITDA (FY25 EBITDA £598.6M)= £6.968B / £598.6M  = 11.64×
FCF Yield (Adj. FCF £362.6M / Mkt Cap £8.182B) = 4.43%   (USD basis: $478.3M / $10.843B = 4.41% — consistent)
Net Debt/EBITDA         = −£1,214.4M / £598.6M = −2.03×   (net cash position)
ROIC (NOPAT/Invested Capital, FY25) = (EBIT×(1−25% UK tax)) / (Total Debt + Equity) = £435.15M / £1,571.8M = 27.7%
Gross margin (FY25)     = £1,307.8M / £1,806.2M = 72.4%
Net margin (FY25)       = £416.7M / £1,806.2M = 23.1%
FCF/NI conversion (Adj. FCF / NI): FY25 = 87.0% | FY24 = 99.4% | FY23 = 90.1% | FY22 = 394.8% (FY22 flagged as an outlier off a very small NI base — first full year post-listing)
```

### Forward PE — the "0y vs +1y trap" (same issue flagged in the MU/DB1 precedent sessions)

`yfinance`'s raw `info['forwardPE']` field uses the **`+1y`** row of `eps_trend` (FY2027E, £0.38998) rather than the correct **`0y`** row. Confirmed via `info['lastFiscalYearEnd']` = 2025-03-31 (FY2025, already reported) and `info['nextFiscalYearEnd']` = 2026-03-31 (**FY2026 — the year about to be reported this Thursday, 6/25**) — so `0y` (FY2026E, **£0.36407**) is the correct forward-looking estimate to anchor "forward PE" on.

```
Correct Forward PE (GBP basis) = £8.18 / £0.36407 = 22.47×
Cross-check (USD price → GBP via live FX) = ($10.84 / 1.319209) / £0.36407 = £8.217 / £0.36407 = 22.57×
Forward PE used: 22.5× (average of the two cross-checked bases; both within 0.5% of each other)
```
(yfinance's raw, **uncorrected** fields would have shown 20.98× on WISE.L and 17.15× on WSE — both wrong, and inconsistent with each other, because they're built on the wrong fiscal-year row.)

### Revenue 3yr CAGR

```
FY2022 (£563.8M) → FY2025 (£1,806.2M): (1,806.2/563.8)^(1/3) − 1 = 47.42%
```
Far above both strategy.md's >10% and valuation-scoring.md's >8% thresholds — but flagged as a **young/scaling-company growth rate off a small base** (FY2022 was Wise's first full year public), not assumed to be a sustainable steady-state rate going forward. Management's own FY2026 guidance (15-20% underlying income growth, constant currency — sourced via WebSearch, used here as *context* only, never as a scored input per valuation-scoring.md's "Why Forward Guidance Is Not a Sub-score") suggests deceleration is already underway, consistent with a press report that "Wise shares fall[ing] 6.6% after reporting slowing revenue growth" at a recent trading update.

### Rate Environment Gate inputs

```
10Y US Treasury yield = 4.451% (yfinance ^TNX, Thu 2026-06-18 close — most recent available; weekend)
Earnings Yield = 1 / 22.5 = 4.444%
Spread = 4.444% − 4.451% = −0.007pp   (< +1.5% threshold)
```

### Comparables (Rule 5 — min 5 peers, ±50% revenue band, similar business model)

Wise's FY2025 revenue (£1,806.2M ≈ $2,383M at live FX) sets a Rule 5 ±50% band of **$1,191M–$3,574M**.

| Peer | TTM Revenue (USD-equiv) | In ±50% band? |
|---|---|---|
| PayPal (PYPL) | $33,734M | No — far too large |
| Western Union (WU) | $4,050M | No — too large |
| Euronet Worldwide (EEFT) | $4,340M | No — too large |
| Shift4 (FOUR) | $4,453M | No — too large |
| Global Payments (GPN) | $8,855M | No — too large |
| **Adyen (ADYEN.AS)** | **$2,724M** (€2,376M × live EURUSD 1.1464) | **Yes** — only confirmed in-band peer |
| Block / Square (SQ) | Revenue field unavailable via yfinance `info` | Data gap — not resolved |
| Revolut | Private, no public ticker/financials | Excluded — no public data |

**Only one confirmed in-band peer (Adyen)** — short of Rule 5's "minimum 5 peers" standard. Flagged explicitly: the multiples-based fair value in §5 rests on a thinner comparable set than the framework prescribes, because cross-border-payments-at-this-revenue-scale is a narrow peer set (most public payments companies are either much larger platforms or narrower remittance-only players that don't share Wise's multi-currency-account/Platform business mix). Adyen's metrics: EV/EBITDA 14.24×, EV/Revenue 6.26×, forward PE 18.57×, gross margin 68.1%, net margin 44.7%.

---

## 3. Phase 01 — Quality Gate

Using valuation-scoring.md's Quantitative Pre-Screen Filters (per task instruction, this threshold set governs over strategy.md's older summary where they differ):

| Check | WSE Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 72.4% (FY25) | >40% | ✅ PASS |
| Net margin | 23.1% (FY25) | >12% | ✅ PASS |
| ROIC | 27.7% (FY25, NOPAT/Invested Capital) | >15% | ✅ PASS |
| Revenue growth (3yr CAGR) | 47.4% (FY22→FY25) | >8% | ✅ PASS (flagged: small-base, decelerating per mgmt guidance — see §2) |
| FCF positive 3 consecutive years | Adjusted FCF positive all 4 years (£129.9M/£102.7M/£352.5M/£362.6M) | required | ✅ PASS (on corrected basis only — see §2 data-quality flag) |
| Net debt/EBITDA | −2.03× (net cash, own-cash-corrected basis) | <2.5× | ✅ PASS |
| FCF yield | 4.43% (Adj. FCF / Mkt Cap, GBP basis) | >4% | ✅ PASS — narrowly (4.43% vs 4.0% threshold, a ~0.4pp margin) |
| EV/EBIT | 12.01× (corrected EV basis) | <20× | ✅ PASS |

**8 of 8 criteria pass — but every pass on the cash/FCF/EV side depends on the two corrections in §2** (own-cash vs. gross cash; adjusted FCF vs. statement FCF). On the **unadjusted, as-reported** `yfinance` figures, this gate would have shown a wildly distorted EV/EBIT near zero and a nonsensical Net Debt/EBITDA near −13× — not failures exactly, but meaningless numbers that would have made the score engine produce garbage. This is flagged prominently because it's the single biggest judgment call in this session, fully shown rather than buried: the corrections are grounded in Wise's own public FY2025 disclosure (own cash £1.4B, customer balances ~£19.7B+) rather than an estimate, but a future re-look should re-verify the own-cash figure against Wise's next (FY2026, due 2026-06-25) report rather than assuming it's unchanged.

**Gate result: PASS.** Proceed to Phase 02.

---

## 4. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:** Spread = 4.444% − 4.451% = **−0.007pp**, below the +1.5% threshold → **+5 yellow-flag modifier applies** (raises the bar, not a veto, per the 2026-06-07 change).

**Step 2 — Rate Regime Modifier:** 10Y = 4.451%, in the **3.5–5% bracket → +5**.

**Combined Rate Environment Gate modifier: +5 + 5 = +10** (applied additively to the raw weighted score below, consistent with the MU-session precedent of applying both steps).

---

## 5. Phase 02 — Full Valuation Score

### Fast-Grower / PEG eligibility (Upgrade 3) — ruled out, redistribute to EV/EBIT

WSE's EPS technically grew well over 15%/yr across the 4 reported years (£0.0318 → £0.1094 → £0.3373 → £0.3973, i.e. +244%, +208%, +18% YoY). Per Upgrade 3's 2026-06-20 clarification, **"3+ years" requires a reliable, non-distorted earnings base** — a recent IPO or recently-profitable company does **not** qualify even if the percentage math clears 15%. WSE direct-listed in July 2021 and FY2022's EPS (£0.0318) is a near-zero base barely a year into being a public, audited reporter — the +244%/+208% growth rates in FY2023/FY2024 are mathematically an artifact of compounding off that tiny base, not a demonstrated multi-year compounding rate on a mature earnings base. **PEG is not applied; its 15% weight is redistributed to EV/EBIT (25% → 40%)**, exactly as the framework prescribes for this case.

### Sub-scores

**FCF Yield (40% weight):**
```
FCF_Score = clamp(100 × (1 − 4.43/10), 0, 100) = clamp(100 × 0.557, 0, 100) = 55.7
```

**EV/EBIT (40% weight — includes PEG's redistributed 15%):**
```
EV/EBIT_Score = clamp((12.01 − 12) / 23 × 100, 0, 100) = clamp(0.043, 0, 100) = 0.04
```
WSE's corrected EV/EBIT (12.01×) sits almost exactly at the 12× "cheapest" floor of this formula — a striking result given the AML-driven selloff has pushed the stock close to its 52-week low on both listings.

**Forward PE (20% weight) — No-history fallback:**
```
FwdPE_Score = 50.0  (neutral midpoint, flagged — no 5yr PE range/average exists; WISE.L IPO'd 2021-07, under 5yr of price history, and get_earnings_dates returns zero historical reported-EPS rows)
```

**PEG (15% weight):** Not applicable — redistributed to EV/EBIT above.

### Raw weighted score

```
Raw Score = (55.7 × 0.40) + (0.04 × 0.40) + (50.0 × 0.20)
          = 22.28 + 0.016 + 10.0
          = 32.30
```

(Minor rounding note: an earlier intermediate calculation in this session carried slightly more decimal precision on EV/EBIT_Score — 0.3179 vs. 12.07× EV/EBIT rather than 12.01× — before the GBP/USD cross-check was reconciled to the single EV/EBIT figure of 12.01× shown in §2; the difference is sub-0.2 points on the final score and does not change the action band. Raw score taken forward: **32.30**.)

### Rate Environment Gate modifier (additive)

```
Score after Rate Modifier = 32.30 + 10 = 42.30
```

---

## 6. Upside/Downside Modifier — Expected Return Build

Per valuation-scoring.md (Upgrade added 2026-06-20), this step folds the **forward** dimension into the score using the fair-value triangulation Rule 7/10 already require.

### Step 1 — Fair Value triangulation (GBP basis, then converted)

**Method A — DCF** (3 scenarios, Rule 7), built on Adjusted FCF (FY2025 base: £362.6M):

| Scenario | Yr 1–5 growth | Yr 6–10 fade | Terminal growth | WACC | DCF equity value | Per share |
|---|---|---|---|---|---|---|
| Bull | 20% | 18%→6% | 3.0% | 8.85% (base −1pp) | £17.78B | £17.78 |
| Base | 16% (mgmt FY26 guide midpoint) | 14%→4% | 2.5% | 9.85% (4.451% rfr + 1.2β × 4.5% ERP) | £10.94B | £10.94 |
| Bear | 8% | 6%→2% | 2.0% | 10.85% (base +1pp) | £5.69B | £5.69 |

Terminal value = 58.2% of total base-case DCF value — under Rule 4's 75% extend-Stage-2 trigger, no extension needed.

**Method B — Comparable multiples** (Rule 5, single in-band peer Adyen — flagged as a thin comp set in §2):
```
EV/EBITDA method: £598.6M EBITDA × 14.24× (Adyen) = £8.524B EV → +£1.214B net cash → £9.738B equity → £9.74/share
EV/Revenue method: £1,806.2M revenue × 6.26× (Adyen) = £11.30B EV → +£1.214B net cash → £12.52B equity → £12.51/share
Multiples-based FV = average of the two = £11.12/share (held constant across bull/base/bear — peer pricing is a market input, not a Wise-specific scenario lever)
```

**Triangulation (Step 1 formula: 40% DCF + 60% Multiples), per scenario:**

| Scenario | DCF (£/sh) | Multiples (£/sh) | Blended FV (£/sh) | Blended FV ($/sh, live FX) |
|---|---|---|---|---|
| Bull | 17.78 | 11.12 | **13.79** | $18.19 |
| Base | 10.94 | 11.12 | **11.05** | $14.58 |
| Bear | 5.69 | 11.12 | **8.95** | $11.81 |

```
PW Fair Value = 0.25×13.79 + 0.50×11.05 + 0.25×8.95 = £11.21/share = $14.79/share
```

### Step 2 — Expected annual return E

```
Gap Upside % = (PW FV £11.21 / Live Price £8.18) − 1 = +37.03%
Catalyst window: AML investigation (Belgian probe, described in press as "advanced stages, nearing conclusion" — no precise date) + FY2026 earnings 2026-06-25 (concrete, 4 days away) provide near-term clarity, but a hard resolution date for the legal probe itself isn't available — per Rule 10, default to the framework's 2-year window since no narrower dated catalyst exists for full resolution.
Annualized gap = 37.03% / 2 = 18.51%/yr

Intrinsic growth = 17.50%/yr — using the most recent clean YoY figures (FY24→FY25 revenue +17.50%, net income +17.51% — both closely matching management's own 15–20% medium-term underlying-income-growth guidance). The FY22-anchored 3yr Adjusted-FCF CAGR computed earlier (40.8%) was considered and explicitly NOT used here — FY2022's £129.9M base is itself a small, early-public-company figure (the same "young base" distortion already flagged for the EPS/PEG decision in §5), and using it would smuggle the same kind of unreliable-base growth rate into E that Upgrade 3 was just used to exclude from PEG.

Shareholder yield = Net buyback yield = (£72.6M buybacks − £1.0M issuance) / £8.182B market cap = 0.875%/yr. No dividend (payoutRatio = 0).

E = 18.51% + 17.50% + 0.875% = 36.89%/yr
```

### Step 3 — Map E to the modifier

```
H = 10%. E (36.89%) ≥ H, and E ≥ 25% → modifier caps at the maximum:
M = −15 × clamp((36.89 − 10)/15, 0, 1) = −15 × clamp(1.79, 0, 1) = −15.0
```

**Guardrail check (catalyst requirement):** A catalyst within 18–24 months is required to claim upside credit. Two qualify: (1) FY2026 earnings release, 2026-06-25 — 4 days away, concrete date; (2) the Belgian AML investigation, reported as nearing conclusion. Guardrail satisfied — no cap to −5 needed.

**Upside/Downside Modifier: −15.0** (maximum attractive-side modifier — strong expected upside pulls the score down a full band).

---

## 7. Final Phase 02 Score

```
Final Score = Raw weighted score + Rate Environment Gate modifier + Upside/Downside Modifier
            = 32.30 + 10.0 + (−15.0)
            = 27.30
```

Per the score boundary rule (round to nearest 0.1, round .X5 up): **Final Score = 27.3**

**Score band: 0.0–29.9 → "Very Cheap" → BUY, full position 6–8% of portfolio.**

This is a case the Upside/Downside Modifier was specifically designed for in reverse-but-related fashion to its worked example in valuation-scoring.md: a name whose raw cheapness sub-scores (32.30, itself already attractive) get pulled meaningfully lower once the forward dimension — a real, AML-driven dislocation from fair value with two near-term catalysts — is folded in.

---

## 8. Order Setup

**⚠️ Score supports a BUY, but the order setup below fails the mandatory Risk/Reward gate — see recommendation in §10.**

```
Blended FV (base case)   = £11.05/share = $14.58/share (live FX)
MoS (Score 0.0-29.9 band) = 18% (midpoint of the 15-20% range)
Buy Price                = $14.58 × (1 − 0.18) = $11.95

Live price ($10.84) is already BELOW the $11.95 buy-price ceiling
→ per fair-value-methodology.md's Score/MoS integration table: "Score 0.0-29.9 → at or below buy price → Enter now"
→ Entry price used for R/R = live price = $10.84

Primary Sell Target      = Blended FV (base case) = $14.58
Bull-Case Trim Target    = Bull blended FV × 0.90 = £13.79 × 0.90 × 1.319209 = $16.37

Stop Loss (Score 0.0-29.9 band: 20-25% max loss from BUY price):
  @ 20% (tightest allowed): Stop = $10.84 × 0.80 = $8.67  → R/R = ($14.58−$10.84)/($10.84−$8.67) = $3.74/$2.17 = 1.72:1
  @ 22.5% (midpoint):       Stop = $10.84 × 0.775 = $8.40 → R/R = $3.74/$2.44 = 1.53:1
  @ 25% (widest allowed):   Stop = $10.84 × 0.75 = $8.13  → R/R = $3.74/$2.71 = 1.38:1
```

**R/R Ratio: 1.38:1 – 1.72:1 across the entire allowed stop-loss range — below the framework's mandatory 2:1 minimum at every point.**

Per fair-value-methodology.md Step 6: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."* Even the most favorable allowed stop (20%, the tightest end of the Score 0.0–29.9 band's 20–25% range) only reaches 1.72:1. **No position size, share count, or $ allocation is computed** — per the framework, an R/R failure blocks order setup regardless of how attractive the score is; computing a position size against a trade that doesn't clear the R/R gate would be exactly the kind of black-box, rule-skipping output the operating brief prohibits.

---

## 9. Five Qualitative Questions

1. **Why are margins high?** Genuine operating leverage as Wise scales a software-driven, low-marginal-cost cross-border payments network — gross margin has risen from 65.5% (FY22) to 72.4% (FY25) as fixed compliance/infrastructure costs are spread over a fast-growing transaction base. This looks structural (consistent with the business model) rather than cyclical, but the company is young enough (4 years of public financial history) that "high margins are durable" is still a thesis being proven, not a 10+ year track record.
2. **What would it take to compete with them?** Real but moderate barriers: money-transmitter/payments licensing across dozens of jurisdictions, AML/compliance infrastructure at scale, and a large existing customer base with multi-currency balances already parked at Wise (a mild switching cost). Not a structural moat on the level of a network-effect platform — Revolut, traditional banks' own international-transfer products, and other fintechs (Remitly, WorldRemit) all compete directly, and the AML investigation itself is a reminder that compliance infrastructure is a genuine, costly, and imperfect barrier rather than a settled advantage.
3. **Capital allocation track record:** Limited history (4 years public) but reasonable so far — modest, disciplined CapEx (£8.8M–£35.4M/yr against £1.8B+ revenue, i.e. <2% of revenue — an asset-light model), a small buyback program started (£72.6M in FY2025, ~0.9% of market cap), no dividend, no debt-funded M&A binge visible in the data pulled. Too short a track record to fully evaluate through a cycle.
4. **Growth sources next 3–5 years:** Management's own guidance (context only, not scored) points to continued geographic/currency-corridor expansion, deepening business-customer (Wise Platform/B2B) adoption, and low penetration of the addressable cross-border-payments market (Wise itself estimates ~5% of addressable individuals reached, per the FY26 guidance commentary found via WebSearch). This is directionally consistent with the Telegram trigger's framing ("cross-border [payments] still growing").
5. **Best bear case:** The live, ongoing **Belgian AML investigation** is the dominant near-term risk — a serious regulatory failure finding could mean fines, restricted EU operations, reputational damage that slows business-customer adoption, or (in a worse scenario) management/compliance overhaul. This is layered on top of an already-decelerating growth rate (management guidance of 15-20% vs. the historical 47% 3yr CAGR) and a thin comparables set that makes the multiples-based half of fair value less robust than usual (only one confirmed in-band peer, Adyen). The framework's "NOT valid" exit-reason list explicitly excludes "macro fear" and "short-term earnings miss," but an AML investigation is closer to the "balance sheet crisis" / "growth thesis broken" category if it resolves badly — worth re-underwriting hard once Thursday's FY2026 results and any further AML disclosure land.
6. **Disruption vector check:** Low-to-moderate 5-year risk from a *new* technology directly displacing cross-border payments (stablecoins/crypto rails are the most-discussed potential disruptor in this space industry-wide, but regulatory and trust barriers to mainstream consumer/business adoption remain high). The more proximate "disruption" risk is competitive/regulatory rather than technological — well-capitalized neobanks (a digital-first, often app-only bank or financial-services company) and incumbent banks adding similar low-fee FX features could erode Wise's price advantage over time.

---

## 10. Recommendation

# **WATCHLIST ONLY — score supports BUY, but Risk/Reward fails the mandatory 2:1 gate. Do not enter at this time.**

**Final Phase 02 Score: 27.3** ("Very Cheap" band, 0.0–29.9) — driven by a genuinely cheap EV/EBIT (12.01×, corrected basis) compounding with a strong Upside/Downside Modifier (−15.0, the maximum) off a real ~37% gap to probability-weighted fair value with two near-term catalysts (FY2026 earnings 2026-06-25, and an AML investigation reported as nearing conclusion).

**However, the order-setup Risk/Reward ratio is 1.38:1–1.72:1 across the entire permitted stop-loss range (20–25% below entry) — below the framework's hard 2:1 minimum at every point.** Per fair-value-methodology.md Step 6, this is a "do not enter" condition regardless of how attractive the score is. The mechanical reason: the live price ($10.84) already sits below the calculated buy-price ceiling ($11.95), which compresses the loss side of the R/R ratio less than the reward side needs — the base-case fair value ($14.58) implies "only" ~34.5% upside, and the mandated 20-25% stop-loss band eats too much of that ratio to clear 2:1.

**No position should be opened.** This is recorded as a **watchlist entry**, not a pass-and-forget — the gap between the favorable score and the failing R/R gate is narrow enough that either (a) a further pullback toward the lower end of the 52-week range, or (b) Thursday's earnings resolving the AML overhang with clarity (even if the news itself is negative, removing uncertainty can repair the multiple), could flip the R/R gate without requiring any change to the underlying score. This is exactly the situation Phase 04 monitoring exists for.

---

## 11. Next Review Trigger

**Mandatory near-term trigger: Wise's FY2026 (year ended 2026-03-31) results, due Thursday 2026-06-25** — 4 days from this session. This is a Rule 9 mandatory re-valuation event regardless of outcome (quarterly/annual earnings release) and is expected to address both the AML investigation status and forward growth guidance directly — re-run the full Phase 01/02/order-setup sequence with the fresh financials, not just a price update.

Also re-score on any of:
- **Resolution (in either direction) of the Belgian AML investigation** — a clean resolution removes a real overhang and could re-rate the multiple upward (improving R/R from the reward side); a finding of serious AML failure would need to be re-evaluated against the Phase 06 "balance sheet crisis" / "growth thesis broken" exit criteria before any future entry consideration.
- **Any pullback toward or through the 52-week low** ($10.36 NASDAQ / £7.54 LSE) — would mechanically improve R/R from the entry-price side without requiring a fundamental change.
- **Confirmation of the FY2026/FY2027 growth deceleration** flagged in §2/§9 (mgmt guided 15-20% vs. historical 47% 3yr CAGR) over 2+ more quarters — would feed back into the Forward PE and intrinsic-growth inputs.
- Standard Rule 9 triggers: guidance revision, management change, M&A, macro shift, or a >15% unexplained move (none of which would apply to the AML-driven move already explained here).

**No position opened — nothing to log in `decisions/`.**

---

## 12. Data quality flags carried forward (summary)

1. **5yr historical PE: genuinely unavailable** (IPO 2021-07, <5yr price history; zero historical EPS rows via `get_earnings_dates`) — No-history fallback (FwdPE_Score = 50.0) used, not estimated.
2. **"Own cash" vs. gross balance-sheet cash:** this session used Wise's company-disclosed £1.4B "own cash" (FY2025) rather than yfinance's £8.175B "Cash And Cash Equivalents" line, which conflates ~£8B+ of safeguarded customer balances. Re-verify this figure against the FY2026 report (2026-06-25) rather than assuming it carries forward unchanged.
3. **Statement-line "Free Cash Flow" is not usable as-is** — dominated by customer-balance working-capital swings (up to 92% of the reported figure in FY2025). An adjusted FCF (OCF − ΔWC + CapEx) was computed and used throughout instead.
4. **Comparables set is thin** — only one confirmed in-band peer (Adyen) against Rule 5's "minimum 5" standard. The multiples half of the blended fair value rests on a single comparable; treat the resulting FV range as lower-confidence than a typical full comp set would produce.
5. **PEG/Fast-Grower status ruled out** on a "young/distorted earnings base" basis per Upgrade 3's 2026-06-20 clarification — consistent treatment with how the same session also avoided using the FY22-anchored 3yr Adjusted-FCF CAGR (40.8%) for the Upside/Downside Modifier's intrinsic-growth term, using the cleaner FY24→FY25 YoY figure (17.5%) instead.
6. **Revenue 3yr CAGR (47.4%) and the historical EPS growth rates are real, computed, reported figures** — not invented — but are flagged throughout as likely overstating WSE's *sustainable* forward growth rate, given management's own materially lower (15-20%) medium-term guidance.

---

## Glossary

- **AML (Anti-Money Laundering):** laws/controls to stop criminal proceeds moving through legitimate finance; an AML investigation is a regulator/prosecutor probe into control failures — a fundamental risk, not a price-action one.
- **bps (basis points):** 1 bps = 0.01 percentage points.
- **CAGR:** Compound Annual Growth Rate.
- **CapEx:** Capital Expenditure.
- **Cross-border payments:** sending money between different countries/currencies — Wise's core product category.
- **DCF (Discounted Cash Flow):** a valuation method estimating worth today from projected future cash, discounted back to present value.
- **Dual-listing:** the same company's shares trading on two exchanges (here, LSE primary + NASDAQ secondary) — same underlying business and financials, different currency/venue.
- **EBIT / EBITDA:** Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization — operating-profit measures.
- **EPS:** Earnings Per Share.
- **EV (Enterprise Value):** market cap + debt − cash; a company's total value to all capital providers.
- **EV/EBIT, EV/EBITDA, EV/Revenue:** Enterprise Value divided by operating profit or revenue — multiples for comparing how expensive companies are.
- **EY (Earnings Yield):** 1 ÷ Forward PE, compared against the 10-Year Treasury yield.
- **Fast Grower:** Peter Lynch's term for EPS growth >15%/yr for 3+ years on a reliable earnings base — this framework's PEG-sub-score trigger.
- **FCF (Free Cash Flow) / FCF Yield:** cash generated after running/maintaining the business / FCF ÷ market cap.
- **FCF/NI conversion ratio:** FCF ÷ Net Income — checks whether accounting profit is turning into real cash.
- **Forward PE:** price ÷ next-twelve-months expected EPS.
- **FV (Fair Value):** the analyst's estimate of intrinsic worth, independent of market price.
- **GAAP:** Generally Accepted Accounting Principles.
- **IRR:** Internal Rate of Return.
- **M&A:** Mergers & Acquisitions.
- **Moat:** a durable competitive advantage protecting profits from competitors.
- **MoS (Margin of Safety):** how far below fair value the buy price is set.
- **Neobank:** a digital-first, often app-only bank or financial-services company.
- **Own cash:** a payments company's own corporate cash, distinct from customer balances held in transit.
- **PE (Price-to-Earnings) ratio:** share price ÷ EPS.
- **PEG ratio:** PE ÷ earnings growth rate, used to judge whether a fast grower's multiple is justified.
- **pp (percentage points):** a direct difference between two percentages.
- **PT (Price Target):** an analyst's forecast of future share price.
- **PW (probability-weighted):** the bull/base/bear scenario blend (25/50/25).
- **R/R (Risk/Reward ratio):** expected gain ÷ expected loss on a trade; this framework requires ≥2:1.
- **ROIC:** Return on Invested Capital.
- **Safeguarded / segregated customer funds:** customer money a regulated payments company holds in ring-fenced accounts, separate from its own corporate cash; inflates raw balance-sheet cash/cash-flow lines if not stripped out.
- **TAM:** Total Addressable Market.
- **Treasury yield (10Y):** the US government's 10-year bond rate, this framework's risk-free-rate benchmark.
- **TTM (Trailing Twelve Months):** the most recent 12 months of reported results.
- **WACC:** Weighted Average Cost of Capital, the discount rate used in a DCF.
