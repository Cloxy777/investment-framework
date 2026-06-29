# New Position Evaluation — CHTR (Charter Communications, Inc.)

**Task type:** NEW POSITION
**Date:** 2026-06-29
**10Y US Treasury yield:** 4.40% (most recent available value, FRED series DGS10, as of 2026-06-25 — markets closed 2026-06-27/28; this is the latest published print)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — [t.me/bolshegold/9645](https://t.me/bolshegold/9645), ~12:21:10 UTC 2026-06-29: *"📈🔥$CHTR Пока пре-маркет радует )"* ("CHTR, premarket is looking good so far"). This names $CHTR explicitly and unambiguously by cashtag. CHTR has **no prior watchlist entry anywhere** under `watchlist/` (checked both `in-portfolio/` and `not-in-portfolio/`) and **is not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). Per [.claude/commands/telegram-scan.md](../.claude/commands/telegram-scan.md) step 4's first bullet ("No watchlist entry exists at all → `/new-position <TICKER>`") and this repo's established precedent (FDX/CCL/CVX/MCD/NOK/TTWO/CBRS/PLTR/WSE/IBM all received a full evaluation on first mention "regardless of how thin the trigger is"), this proceeds as a standard `/new-position` run. **No figure from the Telegram post's text is used as a financial input anywhere below** — it is only the reason this ticker was looked at.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work.

| Source | Price | Detail |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 233674866, NASDAQ) | **$163.00** | last trade; bid $162.95 / ask $163.40 |
| Day change (same snapshot) | **+21.97% (+$29.36)** on the day | confirms the post's "premarket is looking good" framing reflects a real, large, same-day move — not used as a number, only as directional corroboration |
| 52-week range (IBKR) | low $124.05 / high $422.29 | CHTR is **far** below its 52-week high (−61.4%) despite today's pop |
| 52-week open | $395.69 | for context only |

**Live price used throughout this session: $163.00.**

**Why the stock is moving (context only, not used as financial data):** WebSearch confirms Charter Communications is in the middle of a previously-announced **$34.5B merger with Cox Communications** (FCC approval obtained, expected to close mid-2026) and a related **Liberty Broadband combination**. This is independently confirmed inside CHTR's own Q1 2026 Form 10-Q (the Transaction Agreement and Liberty Broadband Merger Agreement are both disclosed as pending, not yet closed, as of 2026-03-31). No figure from any news article was used below — every number in Sections 2–4 comes directly from CHTR's own SEC filings.

---

## 2. Data Source Note — yfinance blocked, fallback to SEC EDGAR primary filings

`yfinance` failed identically to the documented AAPL (2026-06-25) and WSE (2026-06-26) precedents in this environment: `curl_cffi.requests.exceptions.SSLError: ... TLS connect error: ... OPENSSL_internal: invalid library`. This is the same environment-level `curl_cffi` TLS-impersonation incompatibility previously diagnosed (not ticker-specific, not transient — confirmed again today).

**Fallback used, per Rule 0's documented contingency:** all fundamental data below was pulled directly from Charter Communications, Inc.'s own audited SEC filings —
- **Form 10-K, FY ended December 31, 2025** (filed 2026-01-30, accession 0001091667-26-000017, CIK 1091667)
- **Form 10-K, FY ended December 31, 2023** (filed 2024-02-02, accession 0001091667-24-000028) — pulled solely to obtain FY2022/FY2021 comparatives not shown in the FY2025 10-K
- **Form 10-Q, quarter ended March 31, 2026** (filed 2026-04-24, accession 0001091667-26-000028) — read for Cox/Liberty Broadband transaction status only

No required Phase 01 metric below is missing or invented — every figure has a cited primary-filing source.

---

## 3. Phase 01 — Universe Screening (Quality Gate)

Both threshold sets carried in this framework are shown, per the precedent set in the MCD/WSE/IBM sessions.

| Criterion | strategy.md threshold | valuation-scoring.md threshold | CHTR actual (source: 10-K) | Result |
|---|---|---|---|---|
| **Net margin** (Net income attrib. to Charter shareholders ÷ Revenue) | >15% | >12% | **9.10%** (FY25) / 9.23% (FY24) / 8.35% (FY23) — never clears either bar in any of 3 years | **FAIL (both)** |
| **ROIC** (NOPAT ÷ (Debt + Equity − Cash)) | >15% | >15% | **8.58%** (FY25: NOPAT $9,980M ÷ Invested Capital $116,245M) | **FAIL (both)** |
| **Revenue growth** (3yr CAGR) | >10% | >8% | **0.46%** (FY2022 $54,022M → FY2025 $54,774M) — essentially flat; revenue actually *declined* −0.6% FY25 vs FY24 | **FAIL (both), decisively** |
| **Net debt/EBITDA** | <2x | <2.5x | **4.15×** — CHTR's *own* disclosed figure ("net debt to the last twelve months Adjusted EBITDA was 4.15 times as of December 31, 2025"); independently recomputed here at **4.22×** (Total debt $96,203M − Cash $477M = Net debt $95,726M ÷ Adj. EBITDA $22,708M) | **FAIL (both)** — see note below |
| Gross margin (Revenue − Opex excl. D&A, as a proxy; CHTR does not present a "gross profit" subtotal) | >40% OR structurally expanding | >40% | 40.23% (FY25) / 39.79% (FY24) / 38.83% (FY23) — borderline, marginally expanding | PASS (strategy.md, narrowly, via the "or expanding" clause) / borderline on valuation-scoring.md's flat >40% line |
| FCF positive 3+ consecutive years | required | FCF positive 3 yrs | $4,418M(25) / $3,161M(24) / $3,318M(23) / $5,549M(22) / $8,604M(21) — positive every year shown (GAAP: OCF − CapEx) | PASS (both) |
| FCF/NI conversion ratio (2+ consecutive years) | >70% | (same check) | **88.6%** (FY25) / **62.2%** (FY24) / 72.8% (FY23) — only 1 of the last 2 years clears 70%; does not cleanly satisfy "2+ consecutive years" | **Mixed/FAIL on the literal "2+ consecutive years" reading** |
| FCF yield (live price $163.00) | (not separately gated) | >4% | GAAP-based FCF $4,418M ÷ market cap $20,641M = **21.40%**; company-reported FCF $5,004M ÷ market cap = **24.24%** | PASS (both, by a wide margin — this is the one metric where the post-merger-news price pop still leaves CHTR looking statistically "cheap") |
| EV/EBIT (live price) | (not separately gated) | <20x | EV $116,367M (market cap $20,641M + net debt $95,726M) ÷ FY25 Operating income $12,908M = **9.02×** | PASS (both) |
| Dilutive share issuance pattern | none | none | Class A shares outstanding: 152.65M (FY22) → 145.23M (FY23) → 141.95M (FY24) → 126.63M (FY25) — a **net repurchaser**, −17.0% over 3 years, funded by the buyback program | PASS (both) — no dilution |
| Moat signal | stable/growing share, brand, network effect | (same, qualitative) | Large regional broadband/cable footprint (Spectrum brand), but revenue has been flat-to-declining for 3+ years amid cord-cutting and fixed-wireless/fiber competition — see qualitative note below | Mixed — scale/footprint moat exists, but it is **not preventing top-line erosion**, which is itself evidence the moat is under real competitive pressure |

### Note on Net Debt/EBITDA — this is not a borderline or judgment-call failure

Hybrid Upgrade 5 (Debt Gate) only relaxes the leverage threshold to <4× for **payment networks, exchanges, and asset-light financial businesses** with very high interest coverage and investment-grade ratings. Charter is a capital-intensive cable/broadband infrastructure operator, not an asset-light financial business — it does not qualify for that exception. Even if it did, the **company's own stated, explicit target leverage policy is 4.0×–4.5× Adjusted EBITDA "in the period leading up to the Closing"** (of the Cox transaction), with a *post-merger* target of 3.5×–3.75× — meaning CHTR's management itself does not intend to run this business below the relaxed 4× ceiling, let alone the <2.5× general threshold this framework gates on. This is a deliberate, disclosed capital-structure choice, not a one-off spike.

### Note on Net Margin and ROIC — also structural, not a single bad year

Net margin has sat in a narrow 8.3%–9.2% band for all 3 fiscal years shown — nowhere close to either the >15% (strategy.md) or >12% (valuation-scoring.md) bar. ROIC of 8.58% is materially below the 15% quality bar this framework uses to define "high-quality business" in the first place. Both read as a structural feature of a heavily-levered, capital-intensive, low-growth cable business (the same profile the framework's MCD session flagged as a mismatch with this strategy's design), not a transient dip.

### Result: **Phase 01 FAIL**

CHTR fails on **four independent criteria** under both threshold sets carried in this framework: **net margin, ROIC, revenue growth, and leverage (Net Debt/EBITDA)** — plus a fifth metric (FCF/NI conversion) that fails the literal "2+ consecutive years" reading. Three of these (revenue growth, leverage, ROIC) are not single-year anomalies — they reflect CHTR's multi-year operating and capital-structure profile (flat-to-declining revenue against cord-cutting/competitive pressure, financed with a deliberately high, company-disclosed leverage target).

Per [new-position.md](../.claude/commands/new-position.md) step 2 and [operating-brief.md](../framework/operating-brief.md): *"if it fails, stop and report why rather than proceeding to scoring."* Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed.** This mirrors how MCD, IBM, NOK, CBRS, TTWO, and WSE (in its most recent re-run) were all handled in this repo's history — a Phase 01 FAIL never produces an invented score.

This is not a verdict on Charter as a business in absolute terms — the pending Cox/Liberty Broadband combination may well be a value-accretive scale play, and the company is a genuine net repurchaser with no dilution. But a structurally low-margin, low-ROIC, flat-revenue, heavily-levered (and about to add billions more in debt to fund an acquisition) capital-intensive operator does not fit the quality-plus-growth profile this framework's Phase 01 gate is built to select for — the same structural mismatch documented for MCD.

---

## 4. Recommendation

**PASS.** Do not open a position. No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate this framework uses to define what's even eligible for scoring.

The Telegram post's "premarket is looking good" framing is independently confirmed as directionally accurate (CHTR genuinely is up ~22% today) — but the underlying fundamentals pulled fresh from CHTR's own 10-K say nothing about *why* a quality-value investor should now own it: the move is most plausibly tied to M&A-related news flow (the pending Cox/Liberty Broadband transactions), not a fundamental improvement in margins, growth, or leverage. This is exactly the kind of gap Rule 0's independent-verification requirement exists to catch — a price reaction is not evidence of improved business quality.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

- **Routine re-screen:** not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric score and so don't go stale on a methodology-version bump.
- **Rule 9 fundamental triggers that would warrant a fresh full look:** (a) the Cox Communications acquisition and/or Liberty Broadband combination actually **closing** — this will materially change CHTR's balance sheet (more debt, more goodwill/franchise intangibles, a step-change in scale) and needs a full fresh Phase 01 pass on the combined entity, not an extrapolation from today's standalone numbers; (b) a sustained, multi-quarter reversal of the revenue decline back toward a CAGR durably above 8–10%; (c) a credible, management-articulated deleveraging path bringing Net Debt/EBITDA toward 2.5× (currently moving the *wrong* direction given the pending debt-funded Cox deal); (d) a management change or guidance revision.
- Absent any of the above, future Telegram mentions of CHTR (including further premarket-move commentary) should be treated as routine "last checked, no change" pings rather than triggering a full re-evaluation each time.

---

## Glossary

- **Adjusted EBITDA** — a non-GAAP measure CHTR defines as net income attributable to Charter shareholders plus noncontrolling interest, net interest expense, income taxes, depreciation and amortization, and stock compensation expense (among other adjustments) — the company's own primary leverage-ratio denominator.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money a business spends on physical, long-lived assets (e.g. network infrastructure).
- **D&A** — Depreciation & Amortization — a non-cash expense spreading the cost of long-lived assets over time.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and valuation ratios.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple comparing how expensive a company is relative to operating profit, independent of capital structure.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Form 10-K / 10-Q** — a company's annual / quarterly report filed with the SEC — primary, audited (10-K) or reviewed (10-Q) disclosure of financial results.
- **Invested Capital** — the total capital (debt + equity, minus cash) deployed in a business — the denominator of ROIC.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Phase 01–06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (CHTR does not make this list.)
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **Treasury yield (10Y)** — the interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
