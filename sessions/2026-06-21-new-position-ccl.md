# NEW POSITION — CCL (Carnival Corporation & plc) — 2026-06-21

**Task type:** NEW POSITION
**Date:** 21 Jun 2026
**10Y US Treasury Yield:** 4.451% (yfinance `^TNX`, `regularMarketTime` → Thu 18 Jun 2026 close; Fri 19 Jun 2026 was a US bond/equity market holiday [Juneteenth observed], confirmed via WebSearch; markets reopen Mon 22 Jun 2026)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **for the record only, not applied — see §4**
**Current CCL/CUK portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md)), no prior watchlist entry
**Sector:** Consumer Cyclical — Travel Services (global cruise lines)

**Trigger:** Routine 6 (Telegram Stock-Mention Scan) — a post on [t.me/bolshegold](https://t.me/bolshegold) (post #9602, 2026-06-21 ~18:02 UTC) named $CCL/$CUK in a "stocks reporting this week" round-up, with the author's personal opinion that the position carries Iran/Strait-of-Hormuz risk, heavy debt, and rate sensitivity. Per CLAUDE.md Rule 0 and this task's explicit instruction, **no number or claim from that post was used anywhere in this analysis** — it served only as the trigger to look at the ticker. All data below was pulled fresh from yfinance, IBKR, and SEC/WebSearch sources.

**Ticker identity:** $CCL (Carnival Corporation, NYSE, US primary listing, contract_id 878372298) and $CUK (Carnival plc, NYSE, UK-incorporated twin, contract_id 13796753) are a single global cruise-line business operated through a dual-listed company (DLC) structure. They report combined consolidated financials as one economic entity. This evaluation treats them as **one company**, using CCL as the reference ticker (the larger, primary US listing). CUK is the equivalent listed share class of the same business — not a separate evaluation.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used (CCL)** | **$30.87** | yfinance `info['currentPrice']`/`regularMarketPrice`, cross-checked via `t.history(period="5d")` (6/17 close $29.91 → 6/18 close $30.87) and `regularMarketTime` (1781812803 → 2026-06-18 20:00 UTC) |
| CUK reference price | $27.47 | yfinance `info['currentPrice']` (same DLC business, UK-incorporated twin listing) |
| 52-week range (CCL) | $22.58 – $34.03 | yfinance `info` |
| Analyst consensus PT (CCL) | Mean $35.05, median $35.00 (range $28.70–$45.00, 24 analysts), recommendation "buy" | yfinance `info` |
| Post-market (same session) | $30.90 | yfinance `postMarketPrice` |

⚠️ **Stale-feed flag (same pattern as the 2026-06-20 MU session):** IBKR's `get_price_snapshot` returned **$29.91** for CCL (contract_id 878372298) and **$27.47** for CUK (contract_id 13796753), both with `volume: 0` and `is_close: true` — a stale/non-refreshing quote signature. The CCL figure exactly matches yfinance's **prior-session** close (6/17), not the latest (6/18) close. Friday 6/19/2026 was Juneteenth (observed), a US market holiday — confirmed independently via WebSearch (NYSE/Nasdaq closed 6/19, reopen Mon 6/22) — so IBKR's feed had not rolled forward to the most recent trading session at call time. **Used yfinance's $30.87 as the live price** for CCL: internally consistent across the snapshot field, intraday 5-day history, and `regularMarketTime` timestamp, and is the more recent of the two prints. CUK's IBKR snapshot ($27.47) happens to match yfinance's CUK `currentPrice` exactly, so no discrepancy there. Per Rule 0, price was fetched before any valuation arithmetic.

**Context:** $30.87 sits roughly in the upper-middle of the 52-week range (~37% up from the 52-week low of $22.58, ~9% below the 52-week high of $34.03) — not at a cycle extreme in either direction. It sits **~12% below** the analyst mean PT ($35.05) and median PT ($35.00), with a "buy" consensus rating.

---

## 2. Data Gathered (Phase 01 & 02 Inputs)

### Share count and the DLC combined-entity market cap (important mechanical note)

yfinance's CCL `info['sharesOutstanding']` (1.239B) is the CCL-only share count. Its `info['marketCap']` ($42.759B) and `info['enterpriseValue']` ($67.960B) use a larger `impliedSharesOutstanding` (1.385B) — verified to equal CCL's 1.239B shares **plus** CUK's 146.6M shares (1.239B + 0.147B = 1.386B ≈ 1.385B). This confirms yfinance is already folding the dual-listed structure into one combined-entity market cap, consistent with this task's instruction to evaluate CCL+CUK as a single economic entity. **The combined-entity market cap/EV figures below are used throughout** rather than a CCL-shares-only calculation, which would understate the true economic capitalization by undercounting CUK's shares.

```
Combined Market Cap = $42.759B   (yfinance info['marketCap'], CCL+CUK basis)
Combined EV          = $67.960B  (yfinance info['enterpriseValue'])
Total Debt           = $26.607B  (most recent quarter, 2026-02-28)
Cash                 = $1.424B   (same quarter)
Net Debt             = $25.183B  (Total Debt − Cash)
Check: EV = Market Cap + Net Debt → $42.759B + $25.183B = $67.942B ≈ $67.960B (yfinance figure; small residual likely includes minority interest/other EV adjustments not separately itemized)
```

### Annual financials (fiscal year ends ~Nov 30) — the COVID scar, still inside the lookback windows

| FY | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| FY2022 | $12.169B | $0.412B | **−$4.471B** | **−$2.196B** | **−$6.093B** | **−$5.16** |
| FY2023 | $21.593B | $7.276B | $2.004B | $4.374B | **−$0.074B** | **−$0.06** |
| FY2024 | $25.021B | $9.383B | $3.670B | $6.227B | $1.916B | $1.44 |
| FY2025 | $26.621B | $10.674B | $4.121B | $6.911B | $2.760B | $2.02 |

Source: `t.financials` (yfinance annual income statement). **FY2022 is an outright trough/loss year** — negative EBIT, negative EBITDA, a $6.093B net loss, and FY2023 is still net-loss territory (−$74M). This is the COVID-era demand collapse and slow 2022-era reopening, not a one-off charge.

### Annual cash flow

| FY | FCF | OCF | CapEx |
|---|---|---|---|
| FY2022 | **−$6.610B** | −$1.670B | −$4.940B |
| FY2023 | $0.997B | $4.281B | −$3.284B |
| FY2024 | $1.297B | $5.923B | −$4.626B |
| FY2025 | $2.607B | $6.218B | −$3.611B |

Source: `t.cashflow`. FY2022 FCF is sharply negative — the most recent 4-fiscal-year lookback contains a clear FCF-negative year, though it sits just outside the literal "3 consecutive years" window (FY2023–FY2025 are all positive).

### Quarterly financials (5 most recent)

| Quarter end | Revenue | Gross Profit | EBIT | EBITDA | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|
| 2025-02-28 | $5.810B | $2.044B | $0.309B | $0.963B | **−$0.078B** | **−$0.06** |
| 2025-05-31 | $6.328B | $2.442B | $0.923B | $1.615B | $0.565B | $0.42 |
| 2025-08-31 | $8.153B | $3.768B | $2.174B | $2.892B | $1.852B | $1.33 |
| 2025-11-30 | $6.330B | $2.421B | $0.719B | $1.445B | $0.422B | $0.31 |
| 2026-02-28 | $6.165B | $2.226B | $0.571B | $1.267B | $0.258B | $0.19 |

Source: `t.quarterly_financials`. Note the seasonal pattern (cruise demand peaks in the Northern Hemisphere summer, reflected in the Q3-equivalent 2025-08-31 quarter) and that the year-ago comparable quarter (2025-02-28) was still **net-loss** — the recovery from COVID is recent, not deeply entrenched.

### Quarterly cash flow (5 most recent)

| Quarter end | FCF | OCF | CapEx |
|---|---|---|---|
| 2025-02-28 | $0.318B | $0.925B | −$0.607B |
| 2025-05-31 | $1.541B | $2.392B | −$0.851B |
| 2025-08-31 | $0.736B | $1.383B | −$0.647B |
| 2025-11-30 | $0.012B | $1.518B | −$1.506B |
| 2026-02-28 | $0.697B | $1.263B | −$0.566B |

Source: `t.quarterly_cashflow`.

### TTM (trailing twelve months) reconstruction — sum of last 4 reported quarters (2026-02-28, 2025-11-30, 2025-08-31, 2025-05-31)

| Metric | TTM Value |
|---|---|
| Total Revenue | $26.976B |
| Gross Profit | $10.857B |
| EBIT | $4.387B |
| EBITDA | $7.219B (yfinance `info['ebitda']` reports $7.255B — minor methodology difference, both used as noted below) |
| Net Income | $3.097B |
| Free Cash Flow | $2.986B |
| Operating Cash Flow | $6.556B |
| CapEx | −$3.570B |

### Balance sheet (most recent quarter, 2026-02-28)

| Metric | Value |
|---|---|
| Total Debt | $26.607B |
| Cash & Cash Equivalents | $1.424B |
| Stockholders' Equity | $13.031B |
| **Net Debt** (Total Debt − Cash) | **$25.183B** |
| Invested Capital (FY2025 annual basis — quarterly IC not separately reported) | $38.924B |

### Computed ratios (TTM financials + most recent balance sheet + combined-entity market cap/EV)

```
Gross Margin (TTM)      = $10.857B / $26.976B = 40.25%
Net Margin (TTM)        = $3.097B / $26.976B = 11.48%
FCF Yield (TTM, combined mkt cap $42.759B) = $2.986B / $42.759B = 6.98%
EV/EBIT (TTM, combined EV $67.960B)        = $67.960B / $4.387B = 15.49×
Net Debt/EBITDA (latest qtr net debt $25.183B / yfinance TTM EBITDA $7.255B) = 3.47×
   (cross-check using the manually-summed TTM EBITDA $7.219B → 3.49× — same conclusion either way)
ROE (TTM NI / latest equity) = $3.097B / $13.031B = 23.77%
```

### ROIC — using the actual effective tax rate, not an assumed 21%

Per "never invent or estimate financial data," CCL's actual effective tax rate is sourced directly rather than assumed. `t.financials.loc['Tax Rate For Calcs']`: FY2025 = **0.4329%**, FY2024 = 21%, FY2023 = 21%, FY2022 = 21%. Carnival's near-zero FY2025 effective rate reflects cruise lines' international shipping-income tax treatment (Panama/UK-incorporated parent entities, income earned in international waters largely outside standard corporate tax regimes) — this is a real, sourced figure, not an anomaly to discard.

```
NOPAT (TTM)  = EBIT (TTM) × (1 − FY2025 effective tax rate) = $4.387B × (1 − 0.004329) = $4.368B
ROIC (TTM)   = NOPAT (TTM) / Invested Capital (FY2025 annual) = $4.368B / $38.924B = 11.22%
ROIC (FY2025 only, for cross-check) = ($4.121B × 0.99567) / $38.924B = 10.54%
```

### Revenue 3yr CAGR

```
FY-basis: (FY2025 $26.621B / FY2022 $12.169B)^(1/3) − 1 = 29.81%
```
⚠️ **This is a COVID-recovery artifact, flagged explicitly rather than smoothed over.** FY2022 ($12.169B) was still a deeply depressed, early-reopening year — Carnival's pre-COVID FY2019 revenue was approximately $20.8B (not independently re-verified here since the gate fails decisively on other grounds; noted for context only, not used in any calculation). Using a trough year as the start point for a CAGR mechanically inflates the computed growth rate; this is the mirror image of the MU session's CAGR-suppression issue (there, a trough sat inside the window and dragged the CAGR down — here, a trough sits at the start of the window and inflates it). Per "never invent or estimate financial data," the FY-based figure using actual reported endpoints is reported as computed, flagged rather than substituted.

### Forward PE — the same "0y vs +1y" trap flagged in the MU and DB1 sessions

yfinance's raw `info['forwardPE']` (11.83×) uses `info['forwardEps']` ($2.60968), which is the **`+1y` (FY2027E)** row of `t.eps_trend`, not the correct **`0y` (FY2026E)** row ($2.22976). Confirmed via `info['lastFiscalYearEnd']` = 2025-11-30 and `info['nextFiscalYearEnd']` = 2026-11-30 that `0y` (FY2026E) is the fiscal year that should anchor "forward" PE.

```
Correct Forward PE = $30.87 / $2.22976 = 13.84×
(Incorrect 1y-basis figure yfinance returns directly: $30.87 / $2.60968 = 11.83×)
Trailing PE (sanity check) = $30.87 / $2.27 (trailingEps) = 13.60× — consistent with the corrected 13.84× forward figure
```

### 5-year historical PE reconstruction (`get_earnings_dates(limit=40)` + rolling TTM EPS) — COVID makes this a clean no-history fallback

50 quarters of reported EPS available back to 2015. Rolling 4-quarter TTM EPS only stays positive (PE-computable) for 21 quarters of the full 50-quarter history (2015–2020, pre-COVID) and then again for only **9 quarters** from 2024-03-27 through 2026-03-27 (the post-COVID recovery ramp). Every quarter in between (2020-06 through 2023-12, roughly 4 years) has negative or near-zero TTM EPS and is correctly excluded.

The **trailing 5-calendar-year window** (2021-06 to 2026-06, what the framework's formula calls for) therefore contains **only 9 valid (TTM EPS > 0) quarters**, all drawn from the same post-COVID recovery ramp where TTM EPS climbs mechanically from $0.34 (2024-03) to $2.32 (2026-03) — i.e., the entire "history" is one continuous recovery slope, not a stable trading range with a meaningful average/low/high. This is exactly the scenario valuation-scoring.md's own caveat anticipates: *"if fewer than 5 years (20 quarters) of TTM EPS are reconstructable, treat as the no-history fallback."*

```
FwdPE_Score = 50.0 (neutral, flagged) — would apply if Phase 02 were reached
```

⚠️ Flagged but not resolved into a usable 5yr avg/range — moot regardless, since Phase 01 fails first (§3).

### Rate Environment Gate inputs (for the record — see §4 on why not applied)

```
Earnings Yield = 1 / Forward PE (0y-basis) = 1 / 13.84 = 7.23%
Spread = 7.23% − 4.451% (10Y) = +2.78%   (≥ +1.5% threshold → Step 1 would NOT trigger the +5 flag)
Step 2 Rate Regime Modifier = +5 (10Y in 3.5–5% bracket)
```

### Comparables groundwork (for the record — not used, Phase 01 failed first)

Peers identified but not pulled in detail since Phase 01 fails before any multiples-based fair value would matter: Royal Caribbean Group (RCL), Norwegian Cruise Line Holdings (NCLH) — the other two scaled global cruise operators. Not pursued further; flagged here only so a future re-look doesn't start from zero.

---

## 3. Phase 01 — Quality Gate

Using valuation-scoring.md's Quantitative Pre-Screen Filters (the threshold set specified for this task):

| Check | CCL Value | Threshold | Result |
|---|---|---|---|
| Gross margin | 40.25% (TTM) | >40% | ✅ PASS (by 0.25pp — a hairline pass) |
| Net margin | 11.48% (TTM) | >12% | ❌ **FAIL** (just under, by 0.52pp) |
| ROIC | 11.22% (TTM NOPAT / FY2025 Invested Capital, using actual ~0.43% effective tax rate) | >15% | ❌ **FAIL** (by ~3.8pp) |
| Revenue growth (3yr CAGR) | 29.81% (FY2022→FY2025) | >8% | ✅ PASS — ⚠️ flagged as a COVID-recovery base-year artifact, not durable organic growth |
| FCF positive 3 consecutive years | FY2023–FY2025 all positive ($0.997B, $1.297B, $2.607B) | required | ✅ PASS — ⚠️ FY2022 was **−$6.610B**, just outside the literal 3yr window; the company's FCF profile turned positive only 3 fiscal years ago |
| Net debt/EBITDA | 3.47× (Net Debt $25.183B / TTM EBITDA $7.255B) | <2.5× | ❌ **FAIL** (by ~39% over threshold — not a hairline miss) |
| FCF yield | 6.98% (TTM FCF $2.986B / combined mkt cap $42.759B) | >4% | ✅ PASS |
| EV/EBIT | 15.49× (combined EV $67.960B / TTM EBIT $4.387B) | <20× | ✅ PASS |

**3 of 8 criteria fail.** Additionally, strategy.md's separate **FCF Quality Check** (FCF/Net Income conversion ratio >70% for 2+ consecutive years) only cleanly passes for **1 of the last 2 fiscal years**:

```
FY2025: FCF $2.607B / NI $2.760B = 94.5%  ✅ passes 70%
FY2024: FCF $1.297B / NI $1.916B = 67.7%  ❌ fails 70%
FY2023: FCF $0.997B / NI −$0.074B → ratio not meaningful (NI near-zero/negative — sign and magnitude distorted)
FY2022: FCF −$6.610B / NI −$6.093B → ratio not meaningful (both negative)
```
This is a fourth, separate strike against the gate (strategy.md: *"If below 70% without growth capex explanation, do not proceed to Phase 02"*) — FY2024's 67.7% has no growth-capex explanation on record (CapEx was actually higher in FY2024 than FY2025, the opposite direction from what would excuse a low conversion ratio via reinvestment).

### Why this is a clean FAIL, not a judgment call to smooth over

- **Net debt/EBITDA (3.47× vs <2.5×)** is the decisive, unambiguous failure. This was specifically flagged in the task instructions: Carnival is **not** a payment network or asset-light financial, so Upgrade 5's relaxed <4× threshold (which requires >15× interest coverage and investment-grade rating, neither checked here because it doesn't apply to this business model) does not apply — the standard <2.5× governs. At 3.47×, CCL is roughly 39% over the limit. This is the direct balance-sheet legacy of COVID-era debt issuance to survive a ~20-month period with near-zero revenue (FY2022 revenue of $12.169B was still barely half of pre-COVID levels) — Total Debt remains $26.607B against only $1.424B of cash, and Stockholders' Equity of $13.031B is itself a COVID-era-rebuilt base, not a deep capital cushion.
- **Net margin (11.48% vs >12%)** and **ROIC (11.22% vs >15%)** both fail — not by enormous margins, but cleanly. These reflect a business still mid-recovery: a cruise line with high fixed costs (ships, fuel, port fees, debt service) needs very high occupancy/pricing to convert revenue into the kind of returns this framework's quality bar requires, and at TTM revenue of $26.976B (still only modestly above the FY2025 annual figure), CCL has not yet demonstrated it can sustain >15% ROIC through a normal cycle — only that it has clawed back to modest profitability after a balance-sheet-threatening crisis.
- **FCF/NI conversion ratio** failing for FY2024 (67.7%, no growth-capex explanation) is the same earnings-quality check this framework added specifically to catch businesses where reported profit isn't reliably turning into cash — a real flag, even though FY2025's 94.5% is healthy in isolation.
- **Gross margin (40.25%) passing by only 0.25 percentage points** is a hairline pass, not a comfortable one — worth noting alongside the failures rather than treating it as unambiguous evidence of quality.
- **Revenue 3yr CAGR (29.81%) and "FCF positive 3 years"** both pass on the letter of the rule, but **both passes are mechanically dependent on the COVID trough sitting just outside (CAGR) or just inside the edge of (FCF) the lookback window.** Push the window back even one more year (to include FY2021, not available in yfinance's free-tier 4-year annual history, or to include FY2022's −$6.610B FCF) and both checks would read very differently. This is the same "boundary-window sensitivity" issue flagged in the MU session, but running in the opposite direction: there, a trough inside the window suppressed a CAGR that might otherwise look fine; here, a recent trough just outside the window inflates a CAGR and barely permits an FCF-positive streak. Per "never invent or estimate financial data," the actual reported-endpoint figures are used and flagged, not adjusted.

**Gate result: FAIL.** Per operating-brief.md: "If it fails, STOP — report exactly why, do not proceed to scoring." **The Rate Environment Gate and full Phase 02 valuation score are not run** (inputs captured "for the record" in §2/§4 only).

### Turnaround Sub-Gate (Upgrade 4) — considered and not pursued

Upgrade 4 allows a conditional 2–3% position for businesses failing 2–4 quality criteria if **all five** conditions are met: (1) historical ROIC >15% for ≥5 years in the past decade, (2) CEO/CFO insider buying >$500K in the past 6 months (Form 4 verified), (3) independent FV estimate showing ≥40% MOS, (4) Net Debt/EBITDA <3×, (5) core moat still identifiable. CCL fails this path on at least two independently fatal grounds without needing to check the rest: **(4) Net Debt/EBITDA is 3.47×, above even the Turnaround Sub-Gate's own (looser) <3× threshold**, and **(2) no Form 4 insider-buying data was found** (WebSearch returned no insider-buying disclosures for CEO Josh Weinstein or CFO David Bernstein in the relevant window — this is a data gap, not a confirmed absence, but per "never invent or estimate," it cannot be assumed to pass). Since two of five mandatory conditions are unmet, the Turnaround Sub-Gate path is closed without needing to evaluate conditions (1), (3), or (5).

---

## 4. Rate Environment Gate — NOT RUN

Per the operating brief, Phase 01 failure stops the process before this step. For the record only (see §2 for the underlying numbers): corrected Forward PE (0y-basis) 13.84× → Earnings Yield 7.23%; spread vs. 10Y (4.451%) = +2.78%, which is **above** the +1.5% threshold, so Step 1 would **not** trigger its +5 yellow-flag modifier (notable contrast with the MU session, where the spread failed). Step 2's Rate Regime Modifier would be +5 (10Y in the 3.5–5% bracket). Neither is applied to any score — there is no score.

---

## 5. Phase 02 — Full Valuation Score — NOT RUN

Not applicable — Phase 01 failed. No FCF Yield, EV/EBIT, Forward PE, or PEG sub-scores are computed.

**Upgrade 3 (PEG ratio) — explicitly addressed and ruled out, regardless of gate outcome:** CCL is not a Lynch Fast Grower under any honest reading — its EPS history over the trailing 3+ years is a recovery from a deeply negative COVID base (FY2022 EPS −$5.16, FY2023 −$0.06, FY2024 $1.44, FY2025 $2.02), the same "distorted earnings base" pattern Upgrade 3's 2026-06-20 clarification explicitly excludes ("a company only recently turned GAAP-profitable... does not yet qualify"). Even setting that aside, CCL is fundamentally a **cyclical** (travel/leisure demand, fuel costs, and now the explicit geopolitical-risk-sensitive routing/insurance costs noted as the original Telegram trigger's topic, though not used as data here) — Upgrade 3 explicitly states PEG is "never applied to cyclicals." Had Phase 02 been reached, PEG's 15% weight would have been redistributed to EV/EBIT (making it 40%), per the same pattern as the MU and DB1.DE precedent sessions. This judgment is recorded here per the task instruction not to silently skip it — it never became operative because Phase 01 already failed.

Raw inputs gathered in case of a future re-look (not scored): TTM FCF $2.986B, TTM EBIT $4.387B, combined EV $67.960B, corrected Forward PE 13.84× (0y-basis), 5yr historical PE unusable (only 9 valid quarters in the trailing 5yr window, all from one continuous post-COVID recovery ramp — see §2), comparables groundwork incomplete (RCL, NCLH identified as peers, not pulled in detail).

---

## 6. Qualitative Notes (for the record, despite Phase 01 FAIL)

1. **Why are margins/returns where they are?** Recovery, not yet structural proof. CCL's current 40.25% gross margin / 11.48% net margin / 11.22% ROIC reflect a business that has clawed back from a genuine near-death balance-sheet event (FY2022: −$4.471B EBIT, −$6.093B net loss, −$6.610B FCF) to modest, real profitability over the past 3 fiscal years. The improvement is real and not in question — but the framework's quality bar (>12% net margin, >15% ROIC) is calibrated for *durable*, cycle-tested quality, and CCL has had only 2-3 fiscal years of clean post-COVID data to demonstrate that, against a balance sheet (3.47× net debt/EBITDA) that is itself still working off COVID-era leverage.
2. **Moat assessment:** Real but bounded. Carnival is the largest global cruise operator by capacity (multiple well-known brands: Carnival Cruise Line, Princess, Holland America, Costa, Cunard, Seabourn, P&O, AIDA), with scale advantages in ship procurement, port relationships, and marketing reach — genuine barriers to new entry given the multi-year, multi-billion-dollar lead time to build new cruise capacity. But cruising is a discretionary, demand-elastic consumer product with real substitutes (other vacation types), direct competition from RCL and NCLH on similar value propositions, and exposure to fuel costs, geopolitical routing disruptions, and discretionary-spending downturns that a moat doesn't insulate against.
3. **Capital allocation track record:** TTM CapEx of $3.570B against TTM revenue of $26.976B (~13.2% of revenue) — largely fleet maintenance and new-ship delivery commitments already contracted pre-COVID and through the recovery; not independently decomposed into maintenance vs. growth CapEx here (Upgrade 1's Owner Earnings adjustment was not invoked since Phase 01 failed before any FCF-yield refinement would matter, and CCL is not on the Upgrade 1 affected-business list in any case).
4. **Growth sources next 3–5 years:** Continued post-COVID demand normalization, new ship deliveries already on order, pricing power in a currently strong cruise-demand environment, and onboard-spend growth. All plausible, but all sit on top of a balance sheet still working through COVID-era debt — growth here competes with deleveraging for any incremental cash generated.
5. **Best bear case:** A repeat or analog of a demand shock (whether pandemic-style, a severe travel-deterring geopolitical event, or a discretionary-spending recession) would hit a company still carrying $25.183B of net debt far harder than it would hit a lower-leverage peer — there is materially less balance-sheet cushion to absorb a second shock than there was capacity to absorb the first one (CCL entered COVID with a stronger balance sheet than it has today). Separately and independent of any cyclical shock, fuel-cost volatility and insurance/routing-cost increases tied to specific shipping-lane geopolitical risk are real, recurring operational cost variables for any global cruise/shipping operator — flagged here as a generic structural risk category for this business model, not as an endorsement of any specific claim from the Telegram trigger post (which was not used as data per the task's explicit instruction).
6. **Disruption vector check:** Low technological-disruption risk — cruising has no credible substitute "delivery mechanism" being displaced by new technology in a 5-year horizon. The relevant risk vectors are macro/cyclical (discretionary travel demand, fuel costs) and balance-sheet (leverage capacity to absorb the next shock), not disruption in the Upgrade-3/Clayton-Christensen sense.

---

## 7. Recommendation

# **PASS — Phase 01 FAIL. Do not enter. Watchlist entry created (not scored).**

CCL fails the Phase 01 quality gate on **3 of 8 quantitative criteria** (net margin 11.48% vs >12%; ROIC 11.22% vs >15%; net debt/EBITDA 3.47× vs <2.5×), plus a fourth, separate strike on strategy.md's FCF Quality Check (FY2024's FCF/Net Income conversion ratio of 67.7% misses the >70% threshold with no growth-capex explanation on record). The Net Debt/EBITDA failure is the most decisive and least ambiguous: at 3.47×, Carnival is meaningfully over even the relaxed Upgrade 5 threshold (<4×) that doesn't apply to it anyway (CCL is not a payment network or asset-light financial) — the standard <2.5× governs, and CCL misses it by ~39%. This is the direct, still-unresolved legacy of COVID-era debt issuance.

The Turnaround Sub-Gate (Upgrade 4) conditional 2–3% path was also evaluated and is independently closed: CCL's 3.47× net debt/EBITDA exceeds even that path's own <3× threshold, and no Form 4 insider-buying disclosure was found to satisfy that path's second mandatory condition.

The pattern here is **"real recovery, not yet proven durable quality, on a balance sheet still working off a crisis"** — distinct from MU's "priced for perfection at the cycle peak" pattern, but the same underlying instruction applies: a heavily-indebted, capital-intensive, historically cyclical/COVID-scarred business does not get smoothed over just because its trailing-3-year trend line looks like a strong recovery story.

**No Phase 02 score was computed. No fair value, order setup, or position sizing was produced** (gate failed before Phase 02). **No position should be opened** in CCL or CUK.

---

## 8. Next Review Trigger

**Date/event:** CCL's next earnings release — **Q2 FY2026, confirmed for 23 June 2026** (2 days after this session, per SEC/StockTitan disclosure of the upcoming earnings call) — is a mandatory Rule 9 re-valuation trigger and the most immediate re-look point. Also re-run Phase 01 on any of the following:
- **Sustained deleveraging**: Net debt/EBITDA crossing back under 2.5× (it has been trending down — 3.58× on a FY2025-annual basis vs 3.47–3.49× on the latest TTM basis — but is not there yet). Track this every quarter; this is the single gating metric most likely to flip the gate result if the recovery continues.
- **A second consecutive fiscal year of FCF/NI conversion >70%** (FY2026, when reported) — would resolve the FCF Quality Check strike.
- **ROIC and net margin both clearing their thresholds** (>15% and >12% respectively) on a TTM basis for 2+ consecutive quarters — would resolve the remaining two quantitative strikes.
- Any **>15% unexplained price move** from $30.87 (Rule 9).
- Any **guidance revision, geopolitical-routing/fuel-cost disclosure, or management change** (Rule 9) — including, but not limited to, anything related to the Strait of Hormuz/Iran risk theme the Telegram trigger post raised; if such an event is confirmed via a primary source (SEC filing, company guidance, credible news), it would be evaluated on its own merits as a fresh fundamental trigger, separate from and independent of the unverified social-media commentary that originally surfaced this ticker.
- If revisited: pull RCL/NCLH comparables in full, and reassess the 5yr historical-PE no-history-fallback status once 2026-2027 EPS data extends the trailing window further past the COVID distortion.

**No position opened — nothing to log in `decisions/`.**

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **CAGR** — Compound Annual Growth Rate.
- **CapEx** — Capital Expenditure.
- **DLC (Dual-Listed Company)** — *(new term, added to glossary.md in this session)* a corporate structure where two separately-listed legal entities (here, Carnival Corporation/CCL and Carnival plc/CUK) operate as a single combined economic business with shared management and combined consolidated financial reporting, while each entity's shares trade separately on an exchange.
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
- **MoS (Margin of Safety)** — how far below fair value a buy price is set.
- **Moat** — a durable competitive advantage.
- **NI (Net Income)** — accounting profit after all expenses.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − tax rate)), the numerator of the ROIC calculation.
- **PEG ratio** — PE ratio ÷ earnings growth rate.
- **pp (percentage points)** — a direct difference between two percentages.
- **PT (Price Target)** — an analyst's forecast of future share price.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss.
- **ROE** — Return on Equity.
- **ROIC** — Return on Invested Capital.
- **TAM** — Total Addressable Market.
- **Treasury yield (10Y)** — the US government's 10-year borrowing rate, the framework's risk-free-rate benchmark.
- **TTM** — Trailing Twelve Months.
