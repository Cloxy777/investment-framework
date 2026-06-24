# NEW POSITION — CBRS (Cerebras Systems Inc., Class A)

**Task type:** NEW POSITION
**Date:** 2026-06-24
**Current 10Y US Treasury yield:** 4.50% (TradingEconomics/FRED `DGS10`, 2026-06-24 print — eased ~0.01pp from the prior session on signs of a possible US–Iran resolution plus a tech-sector flight-to-safety bid)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket) — captured for the record only; **not applied**, since Phase 01 fails (see §3)
**Current portfolio weight:** 0% (not held — absent from [holdings.md](../portfolio/holdings.md))
**Sector:** Technology — Semiconductors (AI accelerator chips / wafer-scale compute systems)

---

## 0. Trigger — why this session exists

Telegram post on [t.me/FinnInvestChannel](https://t.me/FinnInvestChannel) (post #2822, ~08:31 UTC 2026-06-24): discusses Cerebras positioning itself as an Nvidia alternative for AI chips, noting a revenue forecast that fell short of market expectations. **CBRS has zero prior watchlist entries** (no `watchlist/not-in-portfolio/CBRS/` or `watchlist/in-portfolio/CBRS/` folder existed before this session) — per `telegram-scan.md`'s trigger logic, any newly-named company with no existing entry is evaluated via `/new-position` regardless of how thin the triggering mention is, the same precedent as FDX/CCL/CVX/WSE/PLTR.

**The Telegram post text is used only as a trigger to select this ticker for evaluation.** None of its claims are used anywhere below as a financial input. All data in this session was independently sourced from yfinance, IBKR, and primary news/SEC sources (per Rule 0 and "never invent or estimate financial data"). Independent confirmation below: Cerebras reported its first quarterly results as a public company on 2026-06-23 after market close — a real Q1 2026 earnings beat-on-revenue/miss-on-bottom-line print with a full-year negative-operating-margin guide — which independently corroborates the post's "revenue forecast fell short" framing (more precisely: the *margin* outlook, not the headline revenue number, is what disappointed; see §6). The post's framing of CBRS as "an alternative to Nvidia" is a qualitative narrative claim, not independently verified here, and is not used as a financial input regardless.

---

## 1. Ticker identity

- **NASDAQ: CBRS** — Cerebras Systems Inc., Class A common stock. Resolved via IBKR `search_contracts("Cerebras", security_type="STK")`: contract_id **882732191**, NASDAQ, "CEREBRAS SYSTEMS INC - A".
- **IPO'd 2026-05-14** (~6 weeks before this session) at $185/share, closing its first trading day at $311.07 (yfinance `t.history()` confirms 2026-05-14 close = $311.07) — independently confirmed via WebSearch as "the largest semiconductor IPO of all time" per a 2026-06-24 wire story. This is a real, currently-tradable, already-public company, not a pre-IPO private one.
- No dual-listing or DLC structure applies.
- **2026-06-23 (yesterday) was CBRS's first quarterly earnings release as a public company** (Q1 2026, per yfinance `t.calendar`/`get_earnings_dates`) — a genuine Rule 9 fundamental trigger independent of the Telegram post, and the actual proximate cause of today's price move (see §6).

## 2. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$195.51** | IBKR `get_price_snapshot`, contract_id 882732191, ts 1782290435 (2026-06-24, live quote, `is_close: false`) |
| Change vs prior close | **−13.77%** ($−31.21) | IBKR `change`/`change_pct` |
| Bid / Ask | $195.00 / $195.50 | IBKR `bid_ask` |
| Cross-check — yfinance | `currentPrice` $226.72 (stale — reflects an earlier point in the session; see note) | yfinance `info` |
| 52-week range (cached) | $196.73 (low) – $386.34 (high) | IBKR `misc_statistics` / yfinance `fiftyTwoWeekLow/High` |
| Analyst consensus PT | Mean $294.00 / median $300.00 (10 analysts, "strong_buy") — **likely stale, pre-dates last night's earnings print**; shown for bull-case sanity check only, not relied upon | yfinance `info` |

**Note on the two-feed discrepancy:** the IBKR live snapshot ($195.51, ts 1782290435) is materially more current than the yfinance pull taken earlier in this session ($226.72) — both are legitimate prints from the same trading day, but CBRS has been falling continuously intraday (a second, slightly earlier IBKR pull this session showed $195.00–195.51 in successive minutes), so the most recent timestamp is used. **$195.51 (IBKR) is the live price used for all calculations below**, per Rule 0. Today's print is **below the cached 52-week-low field of $196.73** — i.e. CBRS has set a new intraday 52-week low today, independently corroborating (via live broker data, not the post's text) the kind of move the triggering Telegram post described.

## 3. Data Gathered

### Important data-availability caveat — recent IPO

CBRS IPO'd only ~6 weeks ago. yfinance's `t.financials`/`t.cashflow`/`t.balance_sheet` (annual) return **pre-IPO private-company financials for FY2022–FY2025** (fiscal year end Dec 31), sourced from the S-1/424B4 registration statement, not post-IPO 10-Qs. `t.quarterly_financials`/`t.quarterly_cashflow` are **empty** — no quarterly 10-Q breakdown has been parsed into yfinance yet (CBRS's first 10-Q, covering the quarter that was just reported 2026-06-23, has not yet propagated into yfinance's quarterly tables as of this session). Consequently:
- **No TTM reconstruction is possible** — only full-fiscal-year (FY2025, ended 2025-12-31, i.e. ~6 months stale relative to today) data is available, plus headline Q1 2026 figures from the earnings release itself (cited from primary news/SEC sources, §6).
- **No 3-year FCF/NI conversion or 5-year historical PE range can be computed** — fewer than 5 years of *public* trading history exist (none at all — CBRS has ~6 weeks of public price history), so the **no-history fallback** in valuation-scoring.md applies if Phase 02 is ever reached: `FwdPE_Score = 50.0` (neutral, flagged). This mirrors the PLTR precedent (`watchlist/not-in-portfolio/PLTR/PLTR-2026-06-23.md`) for a recent-IPO history gap, though as shown below, Phase 02 is not reached regardless.
- **Revenue 3yr CAGR is computable from the pre-IPO annual filings** (FY2022→FY2025) and is shown below for completeness, but it is a *private-company* growth rate off a very small base, not a public-market-disciplined track record.

### Critical data-quality finding — `info['sharesOutstanding']` / `marketCap` / `enterpriseValue` are wrong for this ticker

yfinance's `info` dict reports `sharesOutstanding = 34,500,000` and derives `marketCap = $49.79B` and `enterpriseValue = $13.47B` from it. This is **inconsistent with every other share-count source**:
- `t.balance_sheet` "Ordinary Shares Number" (FY2025): **215,110,345**
- `t.get_shares_full()` (actual reported share count, most recent 2026-05-20 print): **219,610,345**

`34.5M` almost certainly reflects only the IPO's freely-tradable Class A float (or a similar narrow slice), not total shares outstanding — using it understates EV by roughly $28.6B and would corrupt every EV-based ratio below. **Corrected using `get_shares_full`'s 219,610,345 shares:**

| Metric | yfinance `info` (wrong) | Corrected |
|---|---|---|
| Market Cap (@ $195.51) | $49.79B (using stale price + wrong share count) | **$42.94B** (219,610,345 × $195.51) |
| Enterprise Value | $13.47B | **$42.09B** (Mkt Cap + Total Debt $261.8M − Cash & ST Invest $1,108.2M, all FY2025) |

All ratios below use the **corrected** EV/market cap. This is the same category of yfinance data-integrity issue this framework has caught before (the EXPN currency-mixing case, the PLTR/MU forward-PE 0y-vs-+1y trap) — flagged explicitly per "never invent or estimate financial data," which cuts both ways: also never silently trust a vendor field that's internally inconsistent with the company's own balance sheet.

### Annual financials, FY2022–FY2025 (USD, pre-IPO S-1 data; source: yfinance `t.financials`/`t.cashflow`/`t.balance_sheet`)

| Metric | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Total Revenue | $24.6M | $78.7M | $290.3M | $510.0M |
| Gross Profit | $2.9M | $26.4M | $122.7M | $199.1M |
| EBIT | $(178.8)M | $(133.9)M | $(101.6)M | $(145.3)M |
| EBITDA | $(166.9)M | $(123.4)M | $(90.1)M | $(110.8)M |
| Net Income | $(177.7)M | $(127.2)M | $(481.6)M | $237.8M |
| Free Cash Flow | $(174.9)M | $(85.6)M | $428.5M | $(392.8)M |
| Stock-Based Compensation | $16.9M | $26.6M | $58.6M | $49.8M |

**FY2025 net income ($237.8M, positive) is not a clean operating result.** FY2025's income statement carries a **"Total Unusual Items" of $363.3M** ("Gain On Sale Of Security" — a non-operating, one-off item), while **EBIT remained deeply negative (−$145.3M)** the same year. Excluding the one-off gain, FY2025 pretax income is **−$118.5M**, not +$244.9M as reported — i.e., the one positive net-income year on record is an accounting artifact of a one-time gain sitting on top of a structurally unprofitable operating business, not a genuine inflection to profitability. This disqualifies the as-reported FY2025 net margin from being used as a "clean earnings base" the same way the PLTR/DUOL precedents disqualify a tax-driven or one-off-driven EPS spike.

### Balance sheet (most recent annual, FY2025; source: `t.balance_sheet`)

| Metric | Value |
|---|---|
| Total Debt | $261.8M |
| Cash & Short-Term Investments | $1,108.2M |
| Net Debt (cash position) | **$(846.4)M** (net cash) |
| Stockholders' Equity | **$(578.7)M** (negative — net liabilities exceed assets) |
| Ordinary Shares Number | 215,110,345 (FY2025); 219,610,345 most recent (`get_shares_full`) |

Stockholders' equity is **negative**, a structural balance-sheet weakness (common for a recently-IPO'd company that burned significant cash pre-IPO and only recently raised primary capital) — relevant context for the ROIC/Net-Debt-EBITDA criteria below.

### Computed ratios (FY2025 basis, only full fiscal year available; at corrected EV/Market Cap, live price $195.51)

| Metric | Value | Basis |
|---|---|---|
| Gross margin | **39.03%** | $199.1M / $510.0M |
| Net margin (as-reported) | 46.63% — **not used, see note above** | Inflated by the $363.3M one-off gain |
| Net margin (normalized, excl. one-off gain) | **≈ −24.6%** | ($244.9M − $363.3M − $7.1M tax) / $510.0M |
| ROIC | **Undefined / not meaningful** | NOPAT negative (EBIT −$145.3M → NOPAT −$114.8M at 21% statutory tax) **and** Invested Capital negative (Debt $261.8M + Equity $(578.7)M = $(316.8)M) — a negative-over-negative ratio has no economically meaningful sign or magnitude |
| Revenue 3yr CAGR (FY2022→FY2025, pre-IPO) | **174.6%** | ($510.0M / $24.6M)^(1/3) − 1 — off a very small base, private-company period |
| FCF positive, 3 consecutive years | **FAIL** | Negative in 3 of the last 4 fiscal years (FY2022, FY2023, FY2025); only FY2024 was positive |
| Net Debt/EBITDA | **Undefined / not meaningful** | Net cash ($(846.4)M) but EBITDA also negative ($(110.8)M) — ratio is mechanically a negative-over-negative and not interpretable as a leverage multiple |
| FCF Yield | **−0.91%** (Mkt Cap) / **−0.93%** (EV) | FCF $(392.8)M / Market Cap $42.94B (or EV $42.09B) — negative, i.e. the business consumed cash relative to its market value in FY2025 |
| EV/EBIT | **Undefined / not meaningful** (mechanically −290×) | EBIT negative — a negative multiple is not an "expensive/cheap" signal, just a sign that operating income doesn't exist to denominate the multiple |

## 4. Phase 01 — Quantitative Pre-Screen (valuation-scoring.md, 8 criteria)

| # | Criterion | Threshold | CBRS actual | Result |
|---|---|---|---|---|
| 1 | Gross margin | >40% | 39.03% (FY2025) | **FAIL** (marginal — 0.97pp short) |
| 2 | Net margin | >12% | −24.6% normalized (excl. one-off gain); +46.6% as-reported is not a clean basis | **FAIL** |
| 3 | ROIC | >15% | Undefined — NOPAT negative, Invested Capital negative | **FAIL** |
| 4 | Revenue growth (3yr CAGR) | >8% | 174.6% (pre-IPO, FY2022→FY2025) | **PASS** |
| 5 | FCF positive, 3 consecutive years | required | Negative 3 of last 4 fiscal years | **FAIL** |
| 6 | Net debt/EBITDA | <2.5× | Undefined — net cash but EBITDA also negative | **FAIL** |
| 7 | FCF yield | >4% | −0.91% (Mkt Cap) / −0.93% (EV) | **FAIL** |
| 8 | EV/EBIT | <20× | Undefined / mechanically negative (EBIT < 0) | **FAIL** |

**Result: 1 of 8 criteria PASS, 7 of 8 FAIL. Phase 01 Quality Gate: FAIL — decisively, on essentially every profitability and cash-generation criterion.**

Per operating-brief.md, a Phase 01 FAIL means **STOP — do not proceed to Phase 02 valuation scoring.**

### Turnaround Sub-Gate (Hybrid Upgrade 4) — not numerically eligible

Upgrade 4 is available only to "businesses failing 2–4 quality criteria." CBRS fails **7 of 8** — well outside that eligibility window. **The Turnaround Sub-Gate does not apply; it is not even reachable on the criteria count alone**, independent of any of its 5 individual conditions. (For the record, condition 1 — ROIC >15% for ≥5 of the past 10 years — would also close it structurally regardless, the same way it did for PLTR: CBRS has roughly 6 weeks of public history and only 4 years of any financial history at all, so a 10-year, or even 5-year, lookback cannot be satisfied. This is shown for completeness; the gate is already closed by the failing-criteria count.)

## 5. Rate Environment Gate

**NOT RUN.** Phase 01 failed; per operating-brief.md the Rate Environment Gate is a pre-check specifically for Phase 02 scoring and is not executed once Phase 01 has already failed. For the record only (not applied):
- Forward PE per yfinance `info['forwardPE']` = 252.74× (computed off the unreliable share count noted above and a very low forward EPS base — not independently re-verified, since it's moot)
- Earnings Yield = 1/252.74 ≈ 0.40%; Spread vs 10Y (4.50%) ≈ −4.10pp (would trigger Step 1's +5 additive flag if Phase 02 were reached)
- Rate Regime Modifier (10Y in 3.5–5% bracket): +5

## 6. Qualitative Notes

1. **What actually happened, independently confirmed?** Cerebras reported its first quarterly results as a public company on 2026-06-23 after market close (Q1 2026). Per multiple independent primary/news sources (StockTitan, Investing.com, Barron's-style coverage, an 8-K referenced via SEC EDGAR): **revenue beat** ($193.4M actual vs. $180.8M consensus / $154.4–181.1M analyst range), but **EPS missed** (a loss of $0.22/share vs. a consensus expectation of a $0.16/share loss — though one wire service's headline figure differs slightly, possibly a GAAP-vs-non-GAAP distinction not resolved in this session), and critically, **Cerebras guided full-year 2026 core operating margin to −28% to −32%**, citing the cost of AI infrastructure buildout. This is the real, primary-sourced trigger for the move — not the Telegram post, which merely summarized the same news (the post's "revenue forecast falling short of market expectations" framing is somewhat imprecise: revenue actually beat; it's the *margin* guide that disappointed).
2. **Is there a real, large business behind this?** Yes, qualitatively: Cerebras also announced new multi-year partnerships with OpenAI and AWS, reportedly valued at over $20B combined, positioning its wafer-scale chips as inference-capacity infrastructure. Analysts quoted in coverage flagged a customer-concentration risk ("concentration rotated, it didn't go away") — heavy historical reliance on a small group of customers, reportedly weighted toward the Middle East. None of this changes the Phase 01 outcome below: a large, fast-growing revenue base with negative margins and negative FCF is exactly the profile Phase 01's profitability/cash-generation criteria are designed to filter out at this stage, regardless of the narrative.
3. **Could a price decline alone make this pass?** No — unlike a name that's merely expensive (PLTR's case), CBRS's failing criteria here are not price-denominated multiples sitting too high; they are **negative absolute profitability and cash flow** (negative EBIT, negative EBITDA, negative FCF, negative/undefined ROIC). No price decline closes a gap measured against a negative number — Phase 01 would require the *business* (margins, FCF generation) to improve, which is exactly what management itself just guided will not happen in 2026 (the −28%/−32% operating margin guide is a deterioration commitment, not an improvement one).
4. **Is the one positive net-income year (FY2025) a red flag of the Valeant/Wirecard kind?** No — it's a one-off gain-on-sale-of-security sitting on top of consistently negative operating income, not a cash-vs-accrual earnings-quality mismatch. It is flagged and excluded from the net margin calculation, consistent with "never invent or estimate" cutting both ways (don't accept a vendor-reported number that conflicts with the underlying detail either).
5. **Is this a turnaround/Fallen-Angel candidate?** No — failing 7 of 8 criteria places it well outside Upgrade 4's 2–4-failing-criteria eligibility window; this isn't a formerly-qualified company that stumbled, it's a pre-profitability growth company that has never yet qualified.

## 7. Recommendation

**PASS — Phase 01 Quality Gate FAIL. Do not enter.**

Cerebras passes only 1 of 8 Phase 01 criteria (revenue growth, off a small pre-IPO base) and fails the other 7 decisively: negative EBIT and EBITDA in every year on record, FCF negative in 3 of the last 4 fiscal years, ROIC and Net Debt/EBITDA both undefined/not meaningful (numerator and denominator both negative), negative FCF yield, and an EV/EBIT multiple that is mechanically negative rather than merely high. The Turnaround Sub-Gate is not numerically reachable (7 failing criteria vs. the 2–4 eligibility window). No Phase 02 score was computed; no order setup applies. This is a structurally different — and more decisive — failure pattern than PLTR's (which passed 6 of 8 and failed only on price-denominated cheapness): CBRS is failing on absolute profitability and cash generation, not on being "too expensive for a good business." A `not-in-portfolio` watchlist entry is created marking this "Phase 01 FAIL / not scored," per `watchlist/README.md` convention.

## 8. Next Review Trigger

- **Any quarter where CBRS reports a positive EBIT/EBITDA and the company's own guidance turns toward operating-margin improvement** rather than the −28%/−32% deterioration just guided for FY2026 — the company's first 10-Q (covering the quarter just reported) propagating into yfinance's quarterly tables would also unlock a cleaner, fully post-IPO TTM recompute.
- **CBRS's next quarterly earnings release** — not yet confirmed/visible in yfinance's calendar beyond the one just reported (Q1 2026, 2026-06-23); check again once Q2 2026 guidance/date is disclosed. Mandatory Rule 9 re-check regardless of outcome.
- Any primary-sourced, quantified update on the OpenAI/AWS partnership economics (e.g., disclosed contract revenue recognition timeline) that materially changes the trailing or near-term EBIT/FCF picture — per the MU-deal precedent, this would be assessed at that time but could not on its own override a Phase 01 failure built on negative absolute profitability, only an actual realized improvement in EBIT/FCF could.
- Sufficient public trading history (5+ years) accumulating to make the 5yr historical-PE range and Turnaround Sub-Gate's historical-ROIC lookback computable in principle — not expected before 2031.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **DLC (Dual-Listed Company)** | A corporate structure where two separately-listed legal entities operate as a single combined economic business. Not applicable to CBRS — noted only because the term recurs across this framework's sessions. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **Fallen Angel** | This framework's term for a previously-qualified, formerly high-quality company that has stumbled — evaluated via the Turnaround Sub-Gate rather than the standard screen. Not applicable to CBRS, which has never yet qualified. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper; negative means the business is consuming cash relative to its market value. |
| **Fast Grower** | Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years on a clean earnings base — this framework's trigger for the PEG sub-score. Not reached here since Phase 01 already fails. |
| **Forward PE** | Price ÷ next twelve months' *expected* EPS (as opposed to Trailing PE, which uses the last twelve months' actual earnings). |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements. |
| **IPO (Initial Public Offering)** | The traditional process by which a private company first sells shares to the public on a stock exchange, typically underwritten at a set offer price. A recent IPO leaves a company with a short trailing public price/financial history, complicating multi-year lookback checks. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; undefined/not meaningful when EBITDA is itself negative. |
| **NI (Net Income)** | Net Income — accounting profit after all expenses, interest, and taxes ("the bottom line"). |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **PE (Price-to-Earnings) ratio** | Share price ÷ earnings per share — the most common "how expensive is this stock" multiple. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth. Not computed here; Phase 01 already fails. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. Not run here — Phase 01 already failed. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; undefined/not meaningful when both NOPAT and invested capital are negative. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **SBC (Stock-Based Compensation)** | Employee pay in the form of company shares or stock options — a non-cash expense added back in cash flow, but a real dilution cost to existing shareholders. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — not computable for CBRS yet, since no post-IPO quarterly data has propagated into yfinance. |
| **Turnaround Sub-Gate** | The conditional path (Hybrid Upgrade 4) that lets a company failing 2–4 quality criteria still enter as a small (2–3%) position if it passes 5 specific tests. Not reachable here — CBRS fails 7 of 8 criteria, outside the eligibility window. |
