# NEW POSITION — FDX (FedEx Corporation) — 2026-06-21

**Task type:** NEW POSITION
**Date:** 21 Jun 2026
**10Y US Treasury Yield:** 4.451% (yfinance `^TNX`, Thu 18 Jun 2026 close — Fri 19 Jun 2026 was a US market holiday [Juneteenth observed]; markets reopen Mon 22 Jun 2026)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **for the record only, not applied — gate fails first, see §3**
**Current FDX portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md)), no prior watchlist entry
**Sector:** Industrials — Integrated Freight & Logistics

**Trigger:** Routine 6 (Telegram Stock-Mention Scan) — a post on [t.me/bolshegold](https://t.me/bolshegold) (post #9602, 2026-06-21 ~18:02 UTC) named $FDX in a "stocks reporting this week" round-up, with the author noting it could be a marker for international trade / parcel-volume trends and that they don't hold the company themselves. Per CLAUDE.md Rule 0 and this task's explicit instruction, **no number or claim from that post was used anywhere in this analysis** — it served only as the trigger to look at the ticker. All data below was pulled fresh from yfinance, IBKR, and SEC/WebSearch sources.

**Ticker identity:** $FDX = FedEx Corporation, NYSE, IBKR contract_id 5100583. Unambiguous, no dual-listing or identity issues.

---

## 0. Material corporate event flagged before any calculation — the FedEx Freight spin-off (2026-06-01)

**This is the single most important fact gathered in this session and materially limits what can be computed reliably.** WebSearch confirms FedEx completed the spin-off of FedEx Freight Holding Company (its less-than-truckload/LTL trucking segment) on **1 June 2026** — three weeks before this session. FedEx distributed 80.1% of FedEx Freight's shares to FDX shareholders (1 FDXF share per 2 FDX shares held as of 15 May 2026 record date), retained a 19.9% stake to be monetized within ~24 months, and received a **$4.1B pre-spin cash dividend** from FedEx Freight. FedEx Freight now trades independently as NYSE: FDXF. Management's own pro-forma targets for the *remaining* FedEx (ex-Freight) are ~$98B revenue and ~$8B operating income (~8% operating margin) **by FY2029** — a forward target, not a current reported figure, and explicitly not used as data here per "Why Forward Guidance Is Not a Sub-score."

**The data-consistency problem this creates:** every annual and quarterly financial-statement figure available via `yfinance` (`t.financials`, `t.cashflow`, `t.balance_sheet` — annual through FY2025 ended 31 May 2025; quarterly through the quarter ended 28 Feb 2026) is **pre-spinoff, consolidated FedEx including the now-divested Freight segment**. FedEx's first quarterly report to reflect the post-spinoff entity is its **Q4/full-year FY2026 release, due 23 June 2026 — two days after this session** — and even that report will likely show Freight as a discontinued operation for only part of the fiscal year, not a clean full-year post-spinoff baseline. Meanwhile, the **live price ($326.20) and current shares outstanding already reflect the smaller, post-spinoff entity** (no Freight segment, plus the $4.1B cash receipt). This means every per-share and per-dollar multiple below — built from pre-spinoff trailing financials divided into a post-spinoff price/market cap — mixes two different companies' worth of revenue/earnings/debt against one (smaller) company's current market value. This is exactly the kind of mismatch Rule 0 and Rule 9 exist to catch, and it is **flagged explicitly rather than smoothed over or estimated around** — there is no pro-forma restated financial history publicly available yet to correct for it.

**Why this doesn't change the recommendation, but does qualify it:** as shown in §3, FedEx fails Phase 01 decisively on the (overstated, pre-spinoff, includes-Freight) numbers below — gross margin, net margin, ROIC, and revenue 3yr CAGR all miss by wide margins, and Net Debt/EBITDA is meaningfully over threshold even before backing out the $4.1B spin-off cash inflow that arrived after the period measured. Removing the (generally lower-margin, working-capital-heavy) Freight segment and adding $4.1B of cash would, if anything, likely **improve** several of these ratios going forward — but "likely improve" is not a number this framework can score without inventing one. **Per "never invent or estimate financial data," no pro-forma adjustment is attempted here.** The clean, decisive nature of the Phase 01 failure (see §3) means this doesn't change today's recommendation, but it does mean a genuine re-look is warranted once FedEx reports its first full post-spinoff quarter — flagged in §8 as the dominant next-review trigger, ahead of even the routine earnings-release trigger.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$326.20** | yfinance `info['currentPrice']`/`regularMarketPrice`, cross-checked via `t.history(period="5d")` (6/17 close $325.93 → 6/18 close $326.20) and `regularMarketTime` (epoch 1781812803 → 2026-06-18 20:00 UTC) |
| 52-week range | $174.13 – $345.37 | yfinance `info` |
| Analyst consensus PT | Mean $339.71, median $355.86 (range $160.00–$425.00, 16 analysts), recommendation "buy" | yfinance `info` |
| Post-market (same session) | $326.99 | yfinance `postMarketPrice` |

⚠️ **Stale-feed flag (same pattern as the 2026-06-21 CCL and 2026-06-20 MU sessions):** IBKR's `get_price_snapshot` (contract_id 5100583) returned **$325.93** with `is_close: true` — this exactly matches yfinance's **prior-session** (6/17) close, not the latest (6/18) close. Friday 6/19/2026 was Juneteenth (observed), a confirmed US market holiday (markets reopen Mon 6/22) — so IBKR's feed had not rolled forward to the most recent trading session at call time. **Used yfinance's $326.20** as the live price: internally consistent across the snapshot field, the 5-day intraday history, and `regularMarketTime`. Per Rule 0, price was fetched before any valuation arithmetic.

**Context:** $326.20 sits in the upper portion of the 52-week range (~87% up from the 52-week low of $174.13, only ~5.5% below the 52-week high of $345.37) — close to a 52-week high, not a depressed price. It sits **~4% below** the analyst mean PT ($339.71) and **~8% below** the median PT ($355.86), with a "buy" consensus rating, though the analyst range is unusually wide ($160–$425) — plausibly reflecting dispersion in how analysts are modeling the FedEx Freight spin-off's pro-forma economics, though that is inference, not confirmed.

---

## 2. Data Gathered (Phase 01 & 02 Inputs)

**All figures below are pre-spinoff, consolidated FedEx (including FedEx Freight) — see §0.** FedEx's fiscal year ends 31 May.

### Annual financials (FY ends 31 May) — `t.financials`

| FY | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| FY2022 | $93.512B | $20.167B | $5.585B | $9.555B | $3.826B | $14.33 |
| FY2023 | $90.155B | $19.166B | $6.057B | $10.233B | $3.972B | $15.48 |
| FY2024 | $87.693B | $18.952B | $6.581B | $10.868B | $4.331B | $17.21 |
| FY2025 | $87.926B | $18.995B | $6.230B | $10.494B | $4.092B | $16.81 |

Source: `t.financials`. **Revenue has declined in 3 of the last 4 fiscal years** (FY2022 $93.512B → FY2025 $87.926B, a cumulative −6.0% decline) — not a growth story on any recent reading. EBIT and EBITDA show a modest recovery from FY2022's trough but remain below FY2024's level in FY2025.

### Annual cash flow — `t.cashflow`

| FY | FCF | OCF | CapEx |
|---|---|---|---|
| FY2022 | $3.069B | $9.832B | −$6.763B |
| FY2023 | $2.674B | $8.848B | −$6.174B |
| FY2024 | $3.136B | $8.312B | −$5.176B |
| FY2025 | $2.981B | $7.036B | −$4.055B |

Source: `t.cashflow`. CapEx has been declining steadily (−$6.763B FY2022 → −$4.055B FY2025) — consistent with the DRIVE/Network 2.0 transformation program's emphasis on capital discipline (see §6), though OCF has also been declining over the same period, so the CapEx reduction is not purely a "self-funding efficiency" story.

### Quarterly financials (5 most recent) — `t.quarterly_financials`

| Quarter end | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| 2025-02-28 | $22.160B | $4.731B | $1.476B | $2.542B | $0.909B | $3.76 |
| 2025-05-31 | $22.220B | $5.309B | $2.173B | $3.230B | $1.648B | $6.88 |
| 2025-08-31 | $22.244B | $4.694B | $1.298B | $2.390B | $0.824B | $3.46 |
| 2025-11-30 | $23.469B | $5.132B | $1.621B | $2.689B | $0.956B | $4.04 |
| 2026-02-28 | $24.000B | $5.123B | $1.615B | $2.727B | $1.056B | $4.41 |

Source: `t.quarterly_financials`. Revenue growth has resumed on a YoY quarterly basis (2026-02-28 $24.000B vs 2025-02-28 $22.160B, +8.3%) — this is the most recent and most relevant trend, and is corroborated independently by FedEx's own Q3 FY2026 earnings release (revenue $24.0B, beat expectations) found via WebSearch, used here only as confirmation of a number already pulled directly, not as a new data source.

### Quarterly cash flow (5 most recent) — `t.quarterly_cashflow`

| Quarter end | FCF | OCF | CapEx |
|---|---|---|---|
| 2025-02-28 | $1.015B | $2.012B | −$0.997B |
| 2025-05-31 | $1.046B | $2.519B | −$1.473B |
| 2025-08-31 | $1.093B | $1.716B | −$0.623B |
| 2025-11-30 | $1.194B | $1.951B | −$0.757B |
| 2026-02-28 | $1.038B | $1.993B | −$0.955B |

### TTM (trailing twelve months) reconstruction — sum of last 4 reported quarters (2026-02-28, 2025-11-30, 2025-08-31, 2025-05-31)

| Metric | TTM Value |
|---|---|
| Total Revenue | $91.933B |
| Gross Profit | $20.258B |
| EBIT | $6.707B |
| EBITDA | $11.036B |
| Net Income | $4.484B |
| Free Cash Flow | $4.371B |
| Operating Cash Flow | $8.179B |
| CapEx | −$3.808B |

### Balance sheet (most recent quarter, 2026-02-28) — `t.quarterly_balance_sheet`

| Metric | Value |
|---|---|
| Total Debt (incl. capital lease obligations $16.769B) | $42.022B |
| Cash & Cash Equivalents | $8.008B |
| Stockholders' Equity | $29.804B |
| Invested Capital | $55.057B |
| **Net Debt** (Total Debt − Cash) | **$34.014B** |

⚠️ **Note:** Total Debt jumped from $37.906B (quarter ended 2025-08-31) to $42.022B (quarter ended 2026-02-28) — confirmed via `t.quarterly_cashflow`'s `Issuance Of Debt` line: a **$3.692B new long-term bond issuance** in the quarter ended 2026-02-28, against only $67M of debt repayment in the same quarter. This is a real, sourced increase in leverage, not a data artifact. `Total Debt` already includes capital lease obligations ($16.769B of the $42.022B total) — consistent with strategy.md's instruction to "include operating leases" when assessing debt for a capital-intensive business; no further adjustment needed on that front.

### Computed ratios (TTM financials + most recent balance sheet + current market cap/EV)

```
Market Cap   = $77.834B   (yfinance info['marketCap'])
Enterprise Value = $111.637B   (yfinance info['enterpriseValue'])
Net Debt (balance-sheet basis, 2026-02-28) = $42.022B − $8.008B = $34.014B
Net Debt (EV-implied, cross-check) = $111.637B − $77.834B = $33.803B  (within $0.21B of balance-sheet basis — consistent)

Gross Margin (TTM)   = $20.258B / $91.933B = 22.04%
Net Margin (TTM)     = $4.484B / $91.933B = 4.88%
FCF Yield (TTM, FCF $4.371B / mkt cap $77.834B) = 5.62%
EV/EBIT (TTM, EV $111.637B / EBIT $6.707B)       = 16.64×
Net Debt/EBITDA (balance-sheet net debt $34.014B / TTM EBITDA $11.036B) = 3.08×
   (cross-check using EV-implied net debt $33.803B → 3.06× — same conclusion either way)
```

⚠️ **Discrepancy flag:** yfinance's `info['grossMargins']` field reports **27.55%**, materially different from the **22.04%** reconstructed directly from `t.financials`'/`t.quarterly_financials`'s `Gross Profit`/`Total Revenue` lines (which use `Reconciled Cost Of Revenue`, a slightly different cost classification than whatever `info['grossMargins']` derives from). The TTM reconstruction (22.04%) is used throughout this session because it is directly auditable from the financial-statement line items shown above, rather than a black-box `info` field — and it is also the more conservative (lower) of the two, consistent with "never invent or estimate" defaulting to the figure that can be shown, not assumed favorable. **Either figure is well below the >40% Phase 01 threshold**, so this discrepancy does not change the gate outcome.

### ROIC — using the actual TTM-weighted effective tax rate, not an assumed 21%

Per "never invent or estimate financial data," the actual effective tax rate is sourced directly from `t.quarterly_financials`'s `Tax Rate For Calcs` row rather than assumed, weighted by each quarter's pretax income:

```
Quarter        Pretax Income   Tax Rate
2026-02-28     $1.263B         16.4%
2025-11-30     $1.289B         25.8%
2025-08-31     $1.134B         27.3%
2025-05-31     $2.223B         25.87%

TTM weighted effective tax rate = Σ(Pretax × Rate) / Σ(Pretax) = 24.10%

NOPAT (TTM) = EBIT (TTM) × (1 − 24.10%) = $6.707B × 0.759 = $5.090B
ROIC (TTM)  = NOPAT (TTM) / Invested Capital (latest qtr, 2026-02-28, $55.057B) = 9.25%
```

### Revenue 3yr CAGR — actual reported endpoints, no smoothing

```
FY-basis: (FY2025 $87.926B / FY2022 $93.512B)^(1/3) − 1 = −2.03%
```

**This is a negative 3-year CAGR** — revenue has shrunk, not grown, over the trailing 3 fiscal years on the actual reported figures. This is the mirror opposite of the CCL session's COVID-recovery-inflated-CAGR problem: there, a depressed base year inflated an otherwise-unremarkable recovery into a 29.81% CAGR; here, there is no comparable distortion to flag — FY2022 was a *strong* year (post-pandemic freight demand peak, before the freight/logistics down-cycle that followed), and the decline to FY2025 is a real, multi-year top-line contraction. The most recent quarterly trend (§2, +8.3% YoY in the latest quarter) suggests this may be inflecting upward, but the **3yr CAGR check itself, as specified, reads negative** and is reported as computed.

### FCF/NI conversion ratio by fiscal year (strategy.md's separate FCF Quality Check)

```
FY2022: $3.069B / $3.826B = 80.21%
FY2023: $2.674B / $3.972B = 67.32%
FY2024: $3.136B / $4.331B = 72.41%
FY2025: $2.981B / $4.092B = 72.85%
```

FY2024 and FY2025 both clear the >70% threshold — **2 consecutive years, passes** strategy.md's separate FCF Quality Check (Phase 01's last bullet). This is the one quantitative check FedEx clearly passes.

### Capital expenditure split — Upgrade 1 (Owner Earnings) applicability check

Per the task instruction, Upgrade 1 applies only if Growth CapEx >30% of Total CapEx. **`yfinance`'s cash-flow statement does not break CapEx into a maintenance/growth split** (`t.cashflow` and `t.quarterly_cashflow` carry only a single aggregate `Capital Expenditure` line) — no further itemization is available via this data source, and none was independently sourced from FedEx's 10-K/10-Q segment disclosures within this session's scope. **This is a genuine data gap, flagged explicitly rather than guessed**: it is moot regardless, since (a) FedEx is not on Upgrade 1's affected-business list (MSFT/GOOGL/META/AMZN — businesses with very high-margin, software-economics moats where raw FCF understates quality), and (b) Phase 01 fails decisively below before this question would matter for scoring. **Upgrade 1 is not applied.**

### 5-year historical PE reconstruction (`get_earnings_dates(limit=40)` + rolling TTM EPS)

49 quarters of reported EPS available back to 2014-03-19 (well over the 5-year/20-quarter minimum). Rolling 4-quarter TTM EPS stays positive throughout the trailing 5-year window (no COVID-style earnings-base distortion for FedEx, unlike the CCL precedent). The trailing 20 quarters (2021-06-24 to 2026-03-19) give a clean, usable range:

```
5yr Avg PE = 10.70×
5yr Low PE = 6.10×  (2022-09-15)
5yr High PE = 14.48×  (2026-03-19, the most recent quarter)
```

### Forward PE — the same "0y vs +1y trap" flagged in prior sessions (MU, DB1, CCL, WSE)

`yfinance`'s raw `info['forwardPE']` (16.73×) uses `info['forwardEps']` ($19.503), which is the **`+1y`** (FY2027E) row of `t.eps_trend`, not the correct **`0y`** (FY2026E) row ($19.858). Confirmed via `info['lastFiscalYearEnd']` = 2025-05-31 (FY2025, already reported) and `info['nextFiscalYearEnd']` = 2026-05-31 — **FY2026 is the current, about-to-close fiscal year** (FedEx's Q4 FY2026 report is due 23 June 2026, two days from this session), so `0y` is the correct forward-looking estimate to anchor "forward PE" on.

```
Correct Forward PE = $326.20 / $19.858 = 16.43×
(Incorrect 1y-basis figure yfinance returns directly: $326.20 / $19.503 = 16.73×)
Trailing PE (sanity check) = $326.20 / $18.72 (trailingEps) = 17.43× — broadly consistent, forward below trailing as expected for a company guiding to EPS growth
```

### Rate Environment Gate inputs (for the record — see §3 on why not applied)

```
Earnings Yield = 1 / Forward PE (0y-basis) = 1 / 16.43 = 6.09%
Spread = 6.09% − 4.451% (10Y) = +1.64pp   (≥ +1.5% threshold → Step 1 would NOT trigger the +5 yellow-flag modifier)
Step 2 Rate Regime Modifier = +5 (10Y in 3.5–5% bracket)
```

### Comparables groundwork (for the record — not used, Phase 01 failed first)

Peers not pulled in detail since Phase 01 fails before any multiples-based fair value would matter. UPS (United Parcel Service) is the most obvious direct comparable in integrated parcel/freight; not independently verified here.

---

## 3. Phase 01 — Quality Gate

Using valuation-scoring.md's Quantitative Pre-Screen Filters (the threshold set specified for this task):

| Check | FDX Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 22.04% (TTM, reconstructed) | >40% | ❌ **FAIL** (by ~18pp — not a hairline miss) |
| Net margin | 4.88% (TTM) | >12% | ❌ **FAIL** (by ~7.1pp — well over halfway short of the threshold) |
| ROIC | 9.25% (TTM NOPAT / latest-qtr Invested Capital, actual ~24.1% weighted effective tax rate) | >15% | ❌ **FAIL** (by ~5.8pp) |
| Revenue growth (3yr CAGR) | **−2.03%** (FY2022→FY2025, actual reported endpoints) | >8% | ❌ **FAIL** (negative growth, ~10pp short of threshold) |
| FCF positive 3 consecutive years | FY2023–FY2025 all positive ($2.674B, $3.136B, $2.981B); FY2022 also positive ($3.069B) | required | ✅ PASS |
| Net debt/EBITDA | 3.08× (Net Debt $34.014B / TTM EBITDA $11.036B) | <2.5× | ❌ **FAIL** (by ~23% over threshold) |
| FCF yield | 5.62% (TTM FCF $4.371B / mkt cap $77.834B) | >4% | ✅ PASS |
| EV/EBIT | 16.64× (EV $111.637B / TTM EBIT $6.707B) | <20× | ✅ PASS |

**5 of 8 criteria fail.** This is a more decisive failure than the CCL precedent (which failed 3 of 8). Separately, strategy.md's **FCF Quality Check** (FCF/Net Income conversion ratio >70% for 2+ consecutive years) **passes** — FY2024 (72.41%) and FY2025 (72.85%) both clear 70%.

### Why this is a clean FAIL, not a judgment call to smooth over

- **Gross margin (22.04% vs >40%)** is the most structurally telling failure. FedEx is fundamentally an asset-heavy, labor-and-fuel-intensive logistics/transportation network — airplanes, trucks, sorting facilities, and a large unionized-adjacent workforce — not a software- or brand-margin business. A ~22% gross margin (or even the alternate ~27.6% `info`-field reading) is roughly half the framework's quality threshold and is a structural feature of the business model, not a one-off or cyclical dip. This is the single clearest signal that FedEx does not fit this framework's "high-margin compounder" profile, independent of any cyclicality or restructuring-program narrative.
- **Net margin (4.88% vs >12%)** confirms the same story from the bottom line: thin, single-digit net margins are the norm for FedEx across the FY2022–FY2025 window (computed from `t.financials`: 4.09%/4.41%/4.94%/4.65% by fiscal year — not independently re-tabled above since the TTM figure already tells the story), not an aberration in the trailing twelve months specifically.
- **ROIC (9.25% vs >15%)** fails by a wide margin even using the actual, sourced effective tax rate (24.10% TTM-weighted, not an assumed 21%) rather than a generic assumption — consistent with "never invent or estimate financial data." A capital-intensive logistics network with $55B of invested capital generating under 10% returns on that capital does not clear the framework's quality bar for durable compounding.
- **Revenue 3yr CAGR (−2.03%) is negative**, the most unambiguous of all eight checks: revenue actually shrank from FY2022 ($93.512B) to FY2025 ($87.926B). This was specifically flagged as a question to examine carefully per the task instructions — and the answer, on actual reported endpoints with no smoothing or substitution, is that FedEx has not grown its top line in 3 years. The most recent quarter shows a return to YoY growth (+8.3%), but a single recent quarter does not retroactively change a 3-year CAGR built on annual fiscal-year figures, and one data point is not yet a trend.
- **Net Debt/EBITDA (3.08× vs <2.5×)** fails by roughly 23% over the standard threshold. FedEx is not a payment network or asset-light financial — Upgrade 5's relaxed <4× threshold (which also requires >15× interest coverage and investment-grade rating, neither separately verified here) does not apply; the standard <2.5× governs. The recent $3.692B bond issuance (quarter ended 2026-02-28, per §2) pushed leverage further from the threshold, not closer to it, in the most recent data available. Capital lease obligations ($16.769B) are already folded into the Total Debt figure used here, consistent with strategy.md's "consolidate captive financial subsidiary debt" / "include operating leases" guidance for capital-intensive businesses — so this is not an understated figure being penalized; if anything the inclusion makes the ratio more conservative (higher) than an unadjusted "balance-sheet debt only" calculation would show.
- **Gross margin, net margin, ROIC, and revenue CAGR are not hairline misses** (contrast with the CCL precedent's 40.25% gross margin passing "by 0.25pp," or its 11.48% net margin missing "by 0.52pp") — every one of these four FDX failures misses its threshold by a wide margin (multiple percentage points to double-digit percentage points), and the debt failure is a real, recently-worsening leverage increase, not a legacy COVID scar that's actively healing (the CCL pattern). This is a structurally different kind of Phase 01 failure: not "a recovering business not yet proven durable," but "a mature, capital-intensive business whose unit economics do not clear this framework's quality bar at any point in the trailing window."

### Turnaround Sub-Gate (Upgrade 4) — considered and not pursued

Upgrade 4 allows a conditional 2–3% position for businesses failing 2–4 quality criteria if **all five** conditions are met: (1) historical ROIC >15% for ≥5 years in the past decade, (2) CEO/CFO insider buying >$500K in the past 6 months (Form 4 verified), (3) independent FV estimate showing ≥40% MOS, (4) Net Debt/EBITDA <3×, (5) core moat still identifiable.

FDX fails **2 of the 8** Phase 01 criteria-count threshold is exceeded regardless (5 failures, not "2–4" — Upgrade 4's own eligibility window), but even setting that aside, the path is independently closed on at least two grounds: **(4) Net Debt/EBITDA is 3.08×, above even the Turnaround Sub-Gate's own (looser) <3× threshold**, and **(2) no Form 4 insider-buying disclosure was found** (WebSearch returned FedEx Form 4 SEC filing index entries but no confirmed >$500K CEO/CFO buying transaction in the relevant window — a data gap, not a confirmed absence, so per "never invent or estimate" it cannot be assumed to pass). With 5 of 8 quantitative criteria failing (above the "2-4" window the Turnaround Sub-Gate is designed for) and two of its five mandatory conditions independently unmet, this path is closed.

**Gate result: FAIL.** Per operating-brief.md: "If it fails, STOP — report exactly why, do not proceed to scoring." **The Rate Environment Gate and full Phase 02 valuation score are not run** (inputs captured "for the record" in §2/§4 only).

---

## 4. Rate Environment Gate — NOT RUN

Per the operating brief, Phase 01 failure stops the process before this step. For the record only (see §2 for the underlying numbers): corrected Forward PE (0y-basis) 16.43× → Earnings Yield 6.09%; spread vs. 10Y (4.451%) = +1.64pp, which is **above** the +1.5% threshold, so Step 1 would **not** trigger its +5 yellow-flag modifier. Step 2's Rate Regime Modifier would be +5 (10Y in the 3.5–5% bracket). Neither is applied to any score — there is no score.

---

## 5. Phase 02 — Full Valuation Score — NOT RUN

Not applicable — Phase 01 failed. No FCF Yield, EV/EBIT, Forward PE, or PEG sub-scores are computed.

**Upgrade 3 (PEG ratio) — explicitly addressed and ruled out, regardless of gate outcome:** FedEx is not a Lynch Fast Grower — EPS growth over the trailing several years has been modest and uneven (FY2022 $14.33 → FY2023 $15.48 → FY2024 $17.21 → FY2025 $16.81, i.e. a recent *decline* FY2024→FY2025), well short of the >15%/yr-for-3+-years bar, and FedEx is also a **cyclical, capital-intensive logistics business** — Upgrade 3 explicitly states PEG is "never applied to cyclicals," independent of the growth-rate question. Had Phase 02 been reached, PEG's 15% weight would have been redistributed to EV/EBIT (making it 40%), per the same pattern as the MU, DB1.DE, and CCL precedent sessions. This judgment is recorded here per the task instruction not to silently skip it — it never became operative because Phase 01 already failed.

**Upgrade 1 (Owner Earnings) — explicitly addressed and ruled out:** as detailed in §2, FedEx is not on Upgrade 1's affected-business list (MSFT/GOOGL/META/AMZN), and the growth-vs-maintenance CapEx split needed to test the >30%-growth-CapEx trigger is not available via `yfinance` (a genuine data gap, flagged rather than estimated). Moot regardless, since Phase 01 fails before any FCF-yield refinement would matter.

Raw inputs gathered in case of a future re-look (not scored): TTM FCF $4.371B, TTM EBIT $6.707B, EV $111.637B, corrected Forward PE 16.43× (0y-basis), clean 5yr historical PE range (avg 10.70×, low 6.10×, high 14.48×, no COVID-style distortion), comparables groundwork incomplete (UPS identified as the most obvious peer, not pulled in detail).

---

## 6. Qualitative Notes (for the record, despite Phase 01 FAIL)

1. **Why are margins/returns where they are?** Structural, not a temporary dip. FedEx's ~22% gross / ~5% net margins and ~9% ROIC reflect the fundamental economics of an asset-heavy global air-and-ground parcel/freight network: fuel costs, aircraft and vehicle capital intensity, labor, and a historically fragmented, intensely competitive pricing environment (especially in the ground-parcel segment against UPS and Amazon's own in-house logistics build-out). The DRIVE cost-cutting program (per WebSearch: $1.8B in permanent savings in FY2024, $2.2B more in FY2025, a >$4B target surpassed, plus a $1B FY2026 target from DRIVE/Network 2.0 combined) and the Network 2.0 ground-network redesign (~35% of eligible volume now flowing through ~400 optimized facilities, targeting ~65% by next peak) are real, ongoing structural-margin initiatives — but they are working to *improve* a structurally thin-margin business model, not evidence the model is already high-margin. None of this was used as a scored input (guidance is never scored per valuation-scoring.md), only as qualitative context.
2. **Moat assessment:** Real scale/network moat, bounded by commoditized competitive dynamics. FedEx operates one of only a handful of truly global, integrated air-and-ground parcel networks (along with UPS and, in specific lanes, DHL) — the capital and regulatory (air rights, customs, sorting infrastructure) barriers to replicating this network from scratch are genuinely high. But parcel delivery itself is substantially a commoditized service on price and speed for most shippers, large-volume customers (notably Amazon, historically FedEx's largest and most contentious customer relationship) have significant negotiating leverage and the option to build their own logistics capacity, and the ground-parcel segment in particular has structurally thinner pricing power than the moat narrative might suggest.
3. **Capital allocation track record:** Capital-intensive but increasingly disciplined. TTM CapEx of $3.808B against TTM revenue of $91.933B (~4.1% of revenue) is down meaningfully from FY2022's $6.763B (~7.2% of revenue then) — a real, multi-year reduction in capital intensity, consistent with the DRIVE/Network 2.0 narrative of doing more with the existing network rather than continuing to expand it. Returns to shareholders have included both dividends (TTM dividend yield ~1.5%, payout ratio ~31%) and buybacks ($3.017B repurchased in FY2025 alone, per `t.cashflow`). The growth-vs-maintenance CapEx split itself is not available (§2 data gap), so Upgrade 1's applicability test could not be fully verified, though it is moot given FedEx is not on Upgrade 1's affected-business list regardless.
4. **Growth sources next 3–5 years:** The FedEx Freight spin-off (§0) is the dominant near-term structural event — management's own pro-forma target of ~$98B revenue / ~8% operating margin by FY2029 for the remaining (ex-Freight) entity implies a *more profitable but not dramatically larger* business than today's consolidated figures, a bet on margin expansion through Network 2.0 completion rather than top-line growth. FY2026 guidance (context only, not scored) of 6–6.5% consolidated revenue growth and a recent quarter's return to +8.3% YoY growth suggest near-term momentum, but the 3-year trailing CAGR is negative and the long-run growth story here reads as "operational turnaround / margin recapture," not "expanding TAM," which is a fundamentally different growth thesis than this framework's quality-compounder profile is built to score.
5. **Best bear case:** FedEx remains exposed to (a) global trade-volume and e-commerce-demand cyclicality — directly relevant to the Telegram trigger's own framing of FDX as a "marker for international trade" (noted here only as context for why someone might watch this name, not as data used in the analysis), (b) continued pricing pressure from Amazon's in-house logistics buildout and broader parcel-market overcapacity, (c) execution risk on the still-incomplete Network 2.0 rollout (~35% of eligible volume migrated, more than half still to go), and (d) integration/dis-synergy risk from the very recent Freight spin-off — the remaining FedEx now needs its own cost and parcel-growth plans to work without the diversification (and FY2025 standalone profitability) the Freight segment previously provided. A second leg of fuel-cost or freight-demand weakness layered on top of an already-thin-margin, recently-releveraged ($3.692B new debt issuance) balance sheet would have limited room to absorb the shock.
6. **Disruption vector check:** Low-to-moderate. Parcel/freight delivery has no credible near-term "new delivery mechanism" displacing the physical network itself (drone/autonomous-vehicle delivery remains a longer-horizon, niche-use-case technology, not a network-level disruptor within 5 years). The more proximate disruption-adjacent risk is **disintermediation**, not new technology — large shippers (again, principally Amazon) building out their own last-mile and increasingly long-haul logistics capacity reduces the addressable market available to FedEx/UPS-style third-party carriers over time, a structural/competitive risk rather than a pure technology one.

---

## 7. Recommendation

# **PASS — Phase 01 FAIL. Do not enter. Watchlist entry created (not scored).**

FDX fails the Phase 01 quality gate on **5 of 8 quantitative criteria** — gross margin (22.04% vs >40%), net margin (4.88% vs >12%), ROIC (9.25% vs >15%), revenue 3yr CAGR (**−2.03%**, actually negative, vs >8%), and net debt/EBITDA (3.08× vs <2.5×). This is a more decisive failure than the CCL precedent evaluated earlier in this same batch (3 of 8 criteria) — every one of FDX's four margin/growth/return failures misses by a wide margin rather than a hairline, and the debt failure reflects a *recent, worsening* leverage increase (a $3.692B bond issuance in the most recent reported quarter) rather than a legacy scar actively healing.

The pattern here is structurally different from CCL's "real recovery, not yet proven durable, on a healing balance sheet": FedEx is a mature, multi-decade-old business whose core unit economics — thin gross/net margins, sub-double-digit ROIC, and a genuinely negative 3-year revenue trend — are a feature of its capital-intensive, competitively-pressured logistics business model, not a temporary post-crisis dip. The DRIVE cost program and Network 2.0 network redesign are real and ongoing (per WebSearch, sourced as qualitative context only, never scored), and the FedEx Freight spin-off completed 2026-06-01 (see §0) is a genuine attempt to reset the remaining company's margin profile toward management's own ~8% operating-margin FY2029 target — but none of that changes today's gate result on the financial-statement data actually available, and per "never invent or estimate," no pro-forma adjustment for the spin-off was applied to any ratio above.

The Turnaround Sub-Gate (Upgrade 4) conditional 2–3% path was also evaluated and is independently closed: FDX's 5-of-8 criteria failure count exceeds the "2–4 criteria" window the path is designed for, its 3.08× net debt/EBITDA exceeds even that path's own <3× threshold, and no Form 4 insider-buying disclosure was found to satisfy that path's second mandatory condition.

**No Phase 02 score was computed. No fair value, order setup, or position sizing was produced** (gate failed before Phase 02). **No position should be opened** in FDX.

---

## 8. Next Review Trigger

**Dominant near-term trigger: FedEx's Q4/full-year FY2026 earnings release, confirmed for 23 June 2026** — 2 days from this session (per WebSearch/SEC sourcing) — is both a mandatory Rule 9 re-valuation event (quarterly/annual earnings release) **and, more importantly, the first quarterly report to reflect the post-Freight-spin-off entity** (see §0). This is the single most important re-look point: it should allow a Phase 01 re-run using financial-statement figures that actually match the company the current share price represents, rather than the pre-spinoff, includes-Freight figures used by necessity in this session. Re-run the full Phase 01/02 sequence with the fresh post-spinoff financials, not just a price update.

Also re-score on any of:
- **Confirmation of a sustained return to positive revenue growth** — the most recent quarter's +8.3% YoY uptick, if it persists for 2+ more quarters on a post-spinoff basis, would meaningfully change the revenue-CAGR picture that currently reads negative.
- **Net debt/EBITDA trending back under 2.5×** — particularly relevant given the $4.1B cash dividend FedEx received from FedEx Freight as part of the spin-off (per WebSearch), which could meaningfully delever the post-spinoff balance sheet if applied to debt paydown rather than buybacks; this has not yet shown up in any reported balance sheet pulled in this session (most recent data point, 2026-02-28, predates the 1 June 2026 spin-off close).
- **Gross margin / net margin / ROIC clearing their respective thresholds on a post-spinoff TTM basis** for 2+ consecutive quarters — would resolve the most structural of the Phase 01 failures, though given how wide the current misses are, this would likely require the spin-off's mix-shift effect plus continued DRIVE/Network 2.0 execution, not a single quarter's move.
- Any **>15% unexplained price move** from $326.20 (Rule 9).
- Any **further guidance revision, Network 2.0 milestone disclosure, or management change** (Rule 9).

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **EPS** — Earnings Per Share.
- **EV** — Enterprise Value.
- **EV/EBIT** — Enterprise Value divided by EBIT, a valuation multiple.
- **Fallen Angel / Turnaround Sub-Gate** — the conditional small-position path (Hybrid Upgrade 4) for companies failing some quality criteria, requiring 5 specific conditions including insider buying and a debt cap.
- **Fast Grower** — Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years on a clean earnings base; the trigger for the PEG sub-score.
- **FCF** — Free Cash Flow.
- **FCF Yield** — Free Cash Flow ÷ Market Cap.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **Forward PE** — Price ÷ next twelve months' expected EPS.
- **FV (Fair Value)** — the analyst's estimate of intrinsic worth.
- **GAAP** — Generally Accepted Accounting Principles.
- **LTL (Less-Than-Truckload)** — *(new term, added to glossary.md in this session)* a freight-trucking model where multiple shippers' smaller loads are consolidated onto a single truck/trailer, as opposed to a full truckload dedicated to one shipper. FedEx Freight (now FedEx Freight Holding Company / NYSE: FDXF) is FedEx's former LTL trucking segment, spun off 1 June 2026.
- **MoS (Margin of Safety)** — how far below fair value a buy price is set.
- **Moat** — a durable competitive advantage.
- **NI (Net Income)** — accounting profit after all expenses.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − tax rate)), the numerator of the ROIC calculation.
- **PEG ratio** — PE ratio ÷ earnings growth rate.
- **pp (percentage points)** — a direct difference between two percentages.
- **PT (Price Target)** — an analyst's forecast of future share price.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss.
- **ROIC** — Return on Invested Capital.
- **Spin-off** — *(new term, added to glossary.md in this session)* a corporate transaction where a company separates part of its business into a new, independently-traded public company, typically by distributing shares of the new entity to existing shareholders pro rata. FedEx's 1 June 2026 spin-off of FedEx Freight is an example.
- **TAM** — Total Addressable Market.
- **Treasury yield (10Y)** — the US government's 10-year borrowing rate, the framework's risk-free-rate benchmark.
- **TTM** — Trailing Twelve Months.
