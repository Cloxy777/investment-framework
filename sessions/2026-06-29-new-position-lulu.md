# NEW POSITION — LULU (Lululemon Athletica Inc.)

**Task type:** NEW POSITION
**Date:** 2026-06-29
**Current 10Y US Treasury yield:** 4.37% (yfinance `^TNX`, 2026-06-26 close — most recent completed trading session; today's session had only just opened pre-market at the time of this pull). Cross-checked against YCharts/TradingEconomics/Fed H.15, all clustered 4.37%–4.40% — consistent.
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket) — captured for the record only; **not applied**, since Phase 01 fails (see §4)
**Current portfolio weight:** 0% (not held — absent from [holdings.md](../portfolio/holdings.md), confirmed by grep)
**Sector:** Consumer Discretionary — Apparel, Accessories & Luxury Goods (athletic apparel: leggings, outerwear, footwear)

---

## 0. Trigger — why this session exists

Orchestrator-assigned NEW POSITION evaluation (not a Telegram-sourced trigger). **LULU has zero prior watchlist entries** (no `watchlist/not-in-portfolio/LULU/` or `watchlist/in-portfolio/LULU/` folder existed before this session) — first-ever evaluation of this ticker under the framework. The name is topical given a ~45% YTD share-price decline against a backdrop of guidance cuts, a leadership transition, and an activist campaign — exactly the kind of "quality compounder that got cheap (or got cheap for a real reason)" situation this framework is built to interrogate rigorously rather than react to on headline alone.

## 1. Ticker identity

- **NASDAQ: LULU** — Lululemon Athletica Inc. Resolved via IBKR `search_contracts("LULU", security_type="STK")`: contract_id **45157951**, NASDAQ, "LULULEMON ATHLETICA INC".
- **Disambiguation note:** the same ticker symbol "LULU" also resolves to an unrelated company, **LULU Retail Holdings PLC** (contract_id 789881626, Abu Dhabi Securities Exchange/ADX) — an Egyptian/UAE hypermarket retailer with no corporate relationship to Lululemon Athletica. This session concerns **NASDAQ:LULU only**; the ADX-listed entity is excluded from all data below.
- **Capital structure quirk — exchangeable shares.** Via a Canadian subsidiary (Lulu Canadian Holding, Inc.), a class of "exchangeable shares" exists that is economically and contractually equivalent to common stock (same voting/economic rights, exchangeable 1:1 into common shares) and which the company **itself includes in its own reported diluted EPS share count** (10-Q disclosure, confirmed via WebSearch of the filing language). Most recent 10-Q: common shares 109.308M + exchangeable shares 5.116M = **114.424M total economic shares outstanding** — this is the figure used for all live-price-based market cap/EV calculations below, not yfinance's `sharesOutstanding` field (108.438M, missing the exchangeable tranche) nor the FY2026 annual balance-sheet "Ordinary Shares Number" (116.496M, slightly stale relative to the most recent 10-Q and likely pre-buyback).

## 2. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$117.89** | IBKR `get_price_snapshot`, contract_id 45157951, ts 1782713162 (2026-06-29, pre-market, 06:06 UTC) |
| 52-week range | ~$117 (recent low) – ~$423 (year-ago high) | IBKR `misc_statistics` / yfinance `fiftyTwoWeekLow/High` (approximate; stock has declined almost continuously since its 2025 peak) |
| YTD change | **≈ −45%** | Derived from 52-week high/current price context, corroborated by multiple news sources (TheStreet: "41% YTD skid" as of early June 2026, before a further post-Q1 decline) |

**$117.89 is the live price used for all calculations below**, per Rule 0 — fetched directly from IBKR, not inferred from any valuation multiple.

## 3. Data Gathered

### Annual financials, FY2023–FY2026 (USD millions; fiscal year ends Jan 31; source: yfinance `t.financials`/`t.cashflow`/`t.balance_sheet`, cross-checked internally consistent)

*Labeling convention: "FY23" = fiscal year ended 2023-01-31, through "FY26" = fiscal year ended 2026-01-31 (the most recently completed fiscal year).*

| Metric ($M) | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Total Revenue | 8,110.5 | 9,619.3 | 10,588.1 | 11,102.6 |
| Gross Profit | 4,492.3 | 5,609.4 | 6,270.8 | 6,284.1 |
| Operating Income (EBIT) | 1,726.1 | 2,207.2 | 2,505.7 | 2,210.6 |
| Net Income | 854.8 | 1,550.2 | 1,814.6 | 1,579.2 |
| Operating Cash Flow | 966.5 | 2,296.2 | 2,272.7 | 1,602.5 |
| Capital Expenditure | 638.7 | 651.9 | 689.2 | 680.8 |
| Free Cash Flow | 327.8 | 1,644.3 | 1,583.5 | 921.7 |
| D&A | 291.8 | 379.4 | 446.5 | 496.2 |
| Total Debt | 1,070.3 | 1,403.3 | 1,575.8 | 1,798.4 |
| Cash & Equivalents | 1,154.9 | 2,244.0 | 1,984.3 | 1,807.2 |
| Inventory | 1,447.4 | 1,323.6 | 1,442.1 | 1,700.8 |
| Shares outstanding (annual BS) | 127.3 | 126.2 | 121.3 | 116.5 |

FY2022 (FYE 2022-01-31) is NaN/unavailable in yfinance's annual statements (only 4 years of annual history returned on the free tier) — flagged, not estimated. This does not block any calculation below since all required lookbacks (3yr CAGR, FCF/NI 2-year check) fit within the 4 available years.

**Data gap — quarterly TTM reconstruction not possible.** `t.quarterly_financials`/`t.quarterly_cashflow` return non-NaN data for only 2 of the most recent 6 quarters (2026-04-30 and 2026-01-31); the other 4 are NaN. A clean trailing-twelve-month figure cannot be reconstructed from quarterly data beyond those 2 points. **Per "never invent or estimate financial data," no TTM figure is fabricated** — the most recent full fiscal year (FY26, ended 2026-01-31) is used as the primary annual basis throughout, supplemented by the standalone Q1 FY2026 print (ended 2026-04-30, reported 2026-06-04) for qualitative/trigger context only (§6).

### Computed ratios, FY23–FY26 (derived from the table above; all arithmetic shown)

| Metric | FY23 | FY24 | FY25 | FY26 |
|---|---|---|---|---|
| Gross margin | 55.39% | 58.31% | 59.22% | 56.60% |
| Net margin | 10.54% | 16.12% | 17.14% | **14.22%** |
| Operating margin | 21.28% | 22.95% | 23.67% | 19.91% |
| FCF/NI conversion | 38.35% | 106.07% | 87.26% | **58.36%** |
| Capex / Revenue | 7.87% | 6.78% | 6.51% | 6.13% |
| Net debt ($M) | (84.5) net cash | (840.7) net cash | (408.6) net cash | (8.8) net cash |
| EBITDA (EBIT+D&A) | 2,017.9 | 2,586.6 | 2,952.2 | 2,706.8 |
| Net debt/EBITDA | (0.04)× | (0.33)× | (0.14)× | (0.00)× |
| ROIC, excl. cash (NI/(Equity+Debt−Cash)) | 27.90% | 45.71% | 46.34% | 31.88% |
| ROIC, incl. cash (NI/(Equity+Debt)) | 20.26% | 27.51% | 30.76% | 23.36% |

**Revenue 3yr CAGR (FY23→FY26):** (11,102.6 / 8,110.5)^(1/3) − 1 = **11.03%**

**Share count trend (FY23→FY26):** 127.3M → 116.5M = **−8.50%** — a buyback pattern (shares retired), not dilution.

### Live-price-based ratios (price $117.89, total economic shares 114.424M, FY26 financials)

| Metric | Value | Calculation |
|---|---|---|
| Market Cap | **$13.489B** | $117.89 × 114.424M |
| Net debt (FY26) | $(8.8)M (net cash) | $1,798.4M debt − $1,807.2M cash |
| Enterprise Value | **$13.481B** | Mkt Cap + Net Debt |
| FCF Yield | **6.83%** | $921.7M FCF ÷ $13,489M Mkt Cap |
| EV/EBIT | **6.10×** | $13,481M ÷ $2,210.6M FY26 operating income |
| Forward PE (consensus, yfinance `forwardEps` $11.44) | **10.31×** | $117.89 ÷ $11.44 |
| Forward PE (mgmt guide midpoint, FY26 EPS guide $10.95–$11.15 → mid $11.05) | **10.67×** | $117.89 ÷ $11.05 |

### 5-year historical PE reconstruction (yfinance `get_earnings_dates` TTM-rolling-sum recipe, per valuation-scoring.md)

`get_earnings_dates(limit=40)` returned 49 raw quarters → 46 with valid TTM EPS (4-quarter rolling sum) → last 20 quarters (≈5yr window) used:

| Metric | Value |
|---|---|
| 5yr Avg PE | 34.90× |
| 5yr Low PE | 9.22× |
| 5yr High PE | 65.94× |
| n (quarters) | 20 |

A full 5-year low/high range is available, so the **Primary FwdPE_Score formula** applies (not the fallback or no-history placeholder) — see §5.

### FCF/NI Quality Check — explicit resolution (strategy.md hard gate item)

strategy.md: *"FCF/Net Income conversion ratio >70% for 2+ consecutive years. If below 70% without growth capex explanation, do not proceed to Phase 02."*

| Year | FCF/NI | ≥70%? |
|---|---|---|
| FY23 | 38.35% | No |
| FY24 | 106.07% | Yes |
| FY25 | 87.26% | Yes |
| FY26 | 58.36% | **No** |

The most recent 2 consecutive years (FY25, FY26) do **not** both clear 70% — only FY25 does; FY26 falls to 58.36%. Checking for a "growth capex" explanation per the strategy.md carve-out: **capex as a % of revenue is declining, not rising** (7.87% → 6.78% → 6.51% → 6.13% over FY23–FY26) — the opposite of what a growth-investment explanation would require. The actual driver of the FY26 shortfall is a **$258.7M inventory build** (FY25 $1,442.1M → FY26 $1,700.8M) consuming operating cash flow ($2,272.7M → $1,602.5M, a 29.5% YoY decline) while net income fell only modestly — i.e., cash is being tied up in unsold/slow-moving goods, consistent with the well-documented comp-sales deceleration and weak product reception (§6), not capacity investment. **No growth-capex explanation exists. Per strategy.md's explicit instruction, this is a "do not proceed to Phase 02" condition on its own.**

## 4. Phase 01 — Quality Gate Walkthrough

Both threshold sets shown per task instructions: strategy.md's stricter Phase 01 criteria, and valuation-scoring.md's looser Quantitative Pre-Screen Filters, side by side.

| # | Criterion | strategy.md threshold | valuation-scoring.md threshold | LULU actual (FY26 basis) | Result (strict) | Result (loose) |
|---|---|---|---|---|---|---|
| 1 | Net margin | >15% | >12% | 14.22% | **FAIL** (0.78pp short) | PASS |
| 2 | ROIC | >15% | >15% | 23.36%–31.88% (both methods) | PASS | PASS |
| 3 | FCF positive | 3+ consecutive years | 3 consecutive years | Positive all 4 of FY23–FY26 | PASS | PASS |
| 4 | Gross margin | >40% or expanding | >40% | 56.60% (FY26); 55.4%→59.2%→56.6% range, all years >40% | PASS | PASS |
| 5 | Revenue growth | CAGR >10% (3yr) | CAGR >8% (3yr) | 11.03% | PASS | PASS |
| 6 | Net debt/EBITDA | <2× | <2.5× | Net cash every year (ratio negative) | PASS | PASS |
| 7 | No dilutive share issuance | required | — | Shares −8.5% over 3yr (buybacks) | PASS | n/a |
| 8 | FCF/NI conversion | >70% for 2+ consecutive years, no growth-capex carve-out available | — (not in pre-screen list) | FY25 87.3% / FY26 58.4% — only 1 of last 2 years clears 70%; capex/revenue declining (no carve-out) | **FAIL** | n/a |
| 9 | FCF Yield | — (not a strategy.md criterion) | >4% | 6.83% | n/a | PASS |
| 10 | EV/EBIT | — (not a strategy.md criterion) | <20× | 6.10× | n/a | PASS |

**Result: strategy.md's stricter gate — 6 of 8 criteria PASS, 2 of 8 FAIL (net margin, FCF/NI conversion). valuation-scoring.md's looser pre-screen — 7 of 7 applicable criteria PASS.**

The picture is genuinely mixed and worth stating plainly: by the *looser* pre-screen filter set, LULU would sail through Phase 01 — every quantitative input (margins, ROIC, growth, balance sheet, FCF yield, EV/EBIT) clears the looser bar comfortably, several by a wide margin. It is **specifically strategy.md's stricter, more conservative net-margin threshold (>15% vs. 14.22% actual) and — decisively — its explicit FCF Quality Check instruction** that produce a FAIL.

### Why the FCF Quality Check is treated as decisive, not just one-of-eight

strategy.md does not merely list "FCF/NI conversion >70% for 2+ years" as one item among equals — it appends an explicit, separately-stated instruction: *"If below 70% without growth capex explanation, do not proceed to Phase 02."* This is structured as a standalone stop-rule, the same way "no dilutive share issuance" or the Rate Environment Gate's individual steps function as discrete checks rather than being purely additive to a single pass/fail tally. Per §3 above, the growth-capex carve-out is checked and explicitly does not apply (capex intensity is falling, not rising) — so this stop-rule is triggered on its own terms, independent of the net-margin miss.

**Net margin is a second, independent reason for caution**, not just a rounding error to wave through: FY26 at 14.22% is below the >15% strategy.md threshold, and the trend is now moving the wrong direction (17.14% FY25 → 14.22% FY26, a 2.92pp compression in the most recent year) for reasons directly tied to the same operating deterioration (comp declines, markdowns, inventory overhang) driving the FCF/NI miss — these are not two unrelated marginal misses, they are two symptoms of the same underlying 2026 operating slowdown documented in real time by management's own guidance cut (§6).

### Turnaround Sub-Gate (Hybrid Upgrade 4) — checked for completeness, not cleanly available

LULU fails 2 of 8 strategy.md criteria (net margin, FCF/NI conversion) — numerically within Upgrade 4's "2–4 failing criteria" eligibility window, so it is worth checking the 5 conditions rather than dismissing it outright:

1. **ROIC historically >15% for ≥5 years in past decade** — only 4 fiscal years of financial history are retrievable from yfinance's free tier (FY23–FY26), all of which clear >15% comfortably (23–46% depending on method) — but a full 5-year-of-the-past-decade lookback cannot be independently verified from the data available in this session. **Not verifiable — flagged, not assumed.**
2. **CEO/CFO insider buying >$500K in past 6 months (Form 4 verified)** — WebSearch found: interim co-CEO André Maestrini bought 3,275 shares at $151.02 on 2026-04-01 (**$494,743 — just under the $500K threshold**); CFO/interim co-CEO Meghan Frank's only recent Form 4 activity was a routine performance-share-unit vesting (not an open-market purchase); board director Charles Bergh bought $500,346 in June 2026, but he is a **director, not CEO/CFO**, so does not satisfy this condition's specific role requirement. **FAIL** — no CEO/CFO purchase clears $500K.
3. **Independent FV estimate showing ≥40% MOS** — not computed in this session (moot given items 1–2 below threshold).
4. **Net Debt/EBITDA <3×** — net cash every year, **PASS** comfortably.
5. **Core moat still identifiable** — yes, qualitatively (premium athleisure brand, vertical retail model, loyal customer base) — **PASS**, see §6.

**Conditions 1 (unverifiable) and 2 (FAIL) both fall short — the Turnaround Sub-Gate is not cleanly available even though the failing-criteria count alone would put LULU in its eligibility window.** This is moot in any case: the FCF Quality Check's standalone "do not proceed to Phase 02" instruction is a Phase 01 gate-level stop, and Upgrade 4 is a path *into* Phase 03 sizing for names that fail Phase 01's *quality* bar on margin/ROIC-type grounds — it does not override strategy.md's explicit cash-flow-quality stop-rule.

**Phase 01 Quality Gate verdict: FAIL.** Per operating-brief.md, this means **STOP — do not proceed to Phase 02 valuation scoring.**

## 5. Rate Environment Gate

**NOT RUN.** Phase 01 failed; per operating-brief.md the Rate Environment Gate is a pre-check specifically for Phase 02 scoring and is not executed once Phase 01 has already failed. For the record only (not applied to any score, since none is computed):

- Forward PE (consensus EPS basis): 10.31×; Earnings Yield = 1/10.31 = 9.70%
- Spread vs 10Y (4.37%): 9.70% − 4.37% = **+5.33pp** (would clear the +1.5% threshold with no Step 1 adjustment if Phase 02 were reached — the stock's depressed multiple makes it look statistically cheap on this dimension)
- Rate Regime Modifier (10Y in 3.5–5% bracket): +5 (for the record only)

This is shown for completeness per the task brief's instruction to demonstrate the gate mechanics even where moot — it does not change the Phase 01 FAIL verdict.

## 6. Qualitative Notes (5 Questions + context)

1. **Why are margins high (historically) / what changed in FY26?** Historically, gross margins in the mid-to-high 50s reflect genuine pricing power (limited discounting, premium positioning) and a vertically-integrated direct-to-consumer/own-store model. FY26's margin compression (operating margin 23.67%→19.91%) and the inventory build are not a one-off accounting distortion — they trace to a real, multi-quarter operating slowdown: **5 consecutive quarters of Americas same-store-sales declines**, a viral marketing misstep in China (a Japanese drum prop used at a Great Wall promotional event, interpreted as culturally insensitive, generating 50M+ social-media views of negative commentary), and product launches that "failed to wow shoppers" per interim CEO Meghan Frank's own characterization on the Q1 FY2026 earnings call (2026-06-04).
2. **What would it take to compete with them? (Moat check)** Still a real, identifiable brand moat — premium positioning, a loyal core customer base, and a vertically-integrated retail/membership model that competitors have struggled to fully replicate. However, the moat is visibly **eroding at the margin**: competitors Alo Yoga and Vuori have taken documented share in the premium athleisure category over the past 1–2 years, and the brand-perception damage from the China controversy and weak recent product cycles is a real (if not yet fully quantifiable) dent in pricing power and customer loyalty — this is not the same low-risk moat picture LULU presented 2–3 years ago.
3. **How has management allocated capital over 5–10 years?** Consistent, disciplined buybacks (shares down ~8.5% over just the last 3 fiscal years) funded from genuine FCF rather than debt — a shareholder-friendly capital-allocation pattern, and one reason the balance sheet remains net-cash throughout the entire lookback. Capex intensity has been gently declining as a % of revenue, suggesting no aggressive new-store/capacity binge is underway (reinforcing that the FY26 FCF/NI miss is an inventory/demand problem, not an investment-cycle one).
4. **Where is growth coming from next 3–5 years?** Highly uncertain at this exact moment. Management itself just cut FY2026 guidance twice within the same fiscal year's narrative arc: original FY2026 guide (set 2026-03-17, at Q4 FY2025 results) called for revenue $11.35–11.50B and EPS $12.10–12.30; the **Q1 FY2026 release (2026-06-04) cut this to revenue $11.00–11.15B (implying a slight YoY revenue *decline*, vs. the original 2–4% growth guide) and EPS $10.95–11.15** — a >$1.00/share cut to the EPS guide. This is, on the record available in this session, a **single cut so far** (one guidance-setting event in March, one revision in June) — not yet the "2+ consecutive quarters of cuts without one-off cause" pattern that would independently escalate to a Phase 06 Growth-thesis-broken exit-review candidacy per Phase 04's Guidance discipline check. It is, however, a material, real-time-confirmed deterioration and a textbook Rule 9 trigger event in its own right — the next quarterly print (Q2 FY2026, guided to revenue $2.45–2.48B and EPS $1.76–1.81, both well below prior analyst expectations) is the test of whether this becomes a pattern.
5. **What is the best bear case against owning it?** That this is not a temporary, single-quarter air pocket but a genuine share-loss/brand-fatigue story in its largest market (Americas, 5 straight quarters of comp declines) compounding with self-inflicted reputational damage (the China incident) at exactly the moment leadership is in transition — interim co-CEOs running the company until **Heidi O'Neill (ex-Nike, 25+ years, most recently President of Consumer/Product/Brand) starts as permanent CEO on September 8, 2026** — a ~2.5-month leadership vacuum during an active turnaround. Layered onto this: founder **Chip Wilson's activist campaign** (an 8.7% stake, a proxy contest launched March 2026, settled in May 2026 with two of his board nominees seated and an 18-month non-disparagement clause) signals real governance friction even after a nominal settlement, and Elliott Management's reported ~4% stake adds a second activist voice. The market's own reaction to the O'Neill announcement (shares fell, described by multiple outlets as a "vote of no confidence" in the pick) suggests skepticism that an outside-the-category retread fixes a brand-and-product problem quickly. The bull case — a strong balance sheet, real buybacks, a still-real brand, and a historically cheap multiple (10.3–10.7× forward earnings vs. a 5yr average PE of 34.9×) — is real and shows up clearly in the Rate Environment Gate math above, but Phase 01's own gate is not a multiple/price question; it is a current cash-flow-quality and margin question, and on that specific, narrower test, FY26's numbers say the deterioration is real, not merely sentiment-driven.
6. **Disruption vector check** — no material technology/business-model disruption threat identified distinct from ordinary competitive share-shifting (Alo, Vuori, Nike, Athleta-style competitors); this is a brand/execution risk, not a structural-obsolescence risk.

## 7. Recommendation

**PASS — Phase 01 Quality Gate FAIL. Do not enter.**

LULU clears the *looser* valuation-scoring.md pre-screen filters comfortably (7 of 7 applicable criteria), and most of strategy.md's stricter criteria too (6 of 8) — this is a fundamentally different, much closer-run failure than a name like CBRS (7 of 8 failing) or TTWO (effectively every quantitative criterion failing). LULU is, on balance, a real, historically high-quality, balance-sheet-strong business trading at a genuinely depressed multiple. But Phase 01 is explicitly conjunctive, and strategy.md's FCF Quality Check carries its own standalone stop-instruction: FCF/Net Income conversion has not cleared 70% in 2 consecutive years (FY25 87.3%, FY26 58.4%), and there is no growth-capex explanation available to excuse it — capex intensity is falling, and the real driver is a $258.7M FY26 inventory build tied to the same comp-sales deceleration management has now twice acknowledged via guidance cuts. Net margin has also slipped just below strategy.md's stricter >15% bar in the same fiscal year (14.22%). The Turnaround Sub-Gate is numerically in-range (2 of 8 criteria failing) but not cleanly satisfied either — no qualifying CEO/CFO insider purchase clears the $500K Form-4 threshold, and the ≥5-of-past-10-years ROIC history cannot be verified from available data. **No Phase 02 score is computed; no order setup applies.** A `not-in-portfolio` watchlist entry is created marking this "Phase 01 FAIL, not scored," per `watchlist/README.md` convention.

This is a name to watch closely, not write off — the underlying business quality (margins, ROIC, balance sheet, buyback discipline, brand) remains real, and the gate failure is narrowly and specifically tied to one fiscal year's cash-conversion shortfall during an active, acknowledged operating rough patch, not a structural collapse in the business model. The next 1–2 quarterly prints, and whether the new CEO's first 90 days produce any stabilization in the Americas comp trend, are the things that would most plausibly flip this back to PASS.

## 8. Next Review Trigger

Re-evaluate on any of the following Rule 9 fundamental triggers:

- **Q2 FY2026 earnings release** (guided revenue $2.45–2.48B, EPS $1.76–1.81) — the mandatory next data point. If FCF/NI conversion recovers above 70% on a trailing basis and net margin stabilizes back above 15%, Phase 01 would warrant a fresh full run. If guidance is cut a *second* consecutive time without a new one-off cause, this escalates per Phase 04's Guidance discipline check toward Phase 06 Growth-thesis-broken consideration territory (moot for a non-held name, but relevant context for how negatively to weight a continued slide).
- **Heidi O'Neill's first public strategic commentary as CEO** (starts 2026-09-08) — a management-change Rule 9 trigger in its own right, and the first real signal of strategic direction under new leadership.
- **Any quarter showing the Americas comp-sales decline streak breaking** (5 consecutive quarters as of the Q1 FY2026 report) — the single clearest sign the operating deterioration behind today's FAIL is reversing.
- **A qualifying CEO/CFO Form 4 purchase >$500K** — would meaningfully strengthen (though not by itself satisfy) a future Turnaround Sub-Gate case.
- Routine news-flow (further activist headlines, additional product-launch coverage) absent a new quarterly filing or management statement should be logged as "last checked, no change," not a full re-run — the trailing financials behind today's FAIL will not change until Q2 FY2026 results are filed (expected ~September 2026 based on historical reporting cadence).

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Capex (Capital Expenditure)** | Cash spent on long-lived physical assets (stores, equipment, distribution infrastructure) — a use of cash that reduces Free Cash Flow relative to Operating Cash Flow. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV (Enterprise Value)** | A company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure. |
| **FCF (Free Cash Flow)** | Cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; a sustained shortfall (without a growth-capex explanation) can signal earnings quality or working-capital problems, as with LULU's FY26 inventory build. |
| **Forward PE** | Price ÷ next twelve months' expected EPS, as opposed to Trailing PE (last twelve months' actual earnings). |
| **Form 4** | A SEC filing disclosing an insider's (officer/director/10%+ owner's) purchase or sale of company stock — used to verify genuine insider buying, as opposed to relying on unverified claims. |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements. |
| **Moat** | A durable competitive advantage (brand, scale, network effects, switching costs) that protects a business's profits from competitors. |
| **MOS (Margin of Safety)** | Buying at a meaningful discount to estimated intrinsic/fair value, to protect against estimation error or bad luck. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; LULU has been net-cash (negative net debt) in every fiscal year examined. |
| **NI (Net Income)** | Net Income — accounting profit after all expenses, interest, and taxes ("the bottom line"). |
| **PE (Price-to-Earnings) ratio** | Share price ÷ earnings per share — the most common "how expensive is this stock" multiple. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. Not run here — Phase 01 already failed. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **SBC (Stock-Based Compensation)** | Employee pay in the form of company shares or stock options rather than cash; a real economic cost to existing shareholders through ongoing dilution. |
| **Turnaround Sub-Gate** | The conditional path (Hybrid Upgrade 4) that lets a company failing 2–4 quality criteria still enter as a small (2–3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat). Numerically in-range for LULU but not satisfied here (insider buying and historical-ROIC-depth conditions unmet/unverifiable). |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — not reconstructable for LULU this session due to a quarterly-data gap in yfinance; the most recent full fiscal year (FY26) is used instead, flagged explicitly. |
