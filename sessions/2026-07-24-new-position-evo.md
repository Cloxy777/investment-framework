# NEW POSITION — EVO (Evolution AB, Stockholm-listed; traded here via EVVTY, OTC Pink ADR) — 2026-07-24

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 24 Jul 2026 (Friday, regular session)
**10Y US Treasury Yield:** 4.65% (carried forward from the 2026-07-22 GOOG rescore session — no newer independent read taken this session; unchanged bracket)
**Rate Regime Modifier:** +5 (10Y in the 3.5–5% bracket, unchanged)
**Current EVO/EVVTY portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — first-ever evaluation of this ticker under this framework.
**Sector:** Consumer Discretionary — Gambling/Gaming B2B (live-dealer casino & digital table-game solutions for licensed online operators)
**Filer type:** Swedish primary listing (Nasdaq Stockholm, IFRS reporting, EUR-denominated financials); traded on this account via the unsponsored US OTC Pink ADR **EVVTY** (1:1 ratio, confirmed independently — see §1).
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

A Telegram post today (`bolshegold/9828`, ~14:00 UTC, 2026-07-24) stated that the UK Gambling Commission (UKGC) had considered revoking Evolution AB's ($EVO) UK licence but settled for a fine instead. Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. No watchlist or holdings entry existed anywhere for EVO/EVVTY, so per `/telegram-scan`'s decision rule ("No watchlist entry exists at all → `/new-position`"), a full first-time evaluation is triggered regardless of how the post framed the story.

**Independently verified (WebSearch, not from the post):** Evolution agreed a **£4.75m settlement** with the UKGC, closing an 18-month licence review (launched Dec 2024) into AML-oversight weaknesses and content access via unlicensed operators/websites. The regulator did consider suspending the licence — "serious weaknesses" were found — but settled for the fine plus a mandated independent AML/safer-gambling audit. Sources: [sbcnews.co.uk](https://sbcnews.co.uk/europe/2026/07/15/evolution-settles-with-ukgc/), [casino.org](https://www.casino.org/news/evolution-agrees-4-75m-ukgc-settlement-over-unlicensed-gambling-sites/), [sbcnews.co.uk (licence-under-threat detail)](https://sbcnews.co.uk/europe/uk/2026/07/23/evolution-uk-licence/). The post's framing was accurate.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Contract identity** | Confirmed via `mcp__Interactive-Brokers__search_contracts`: primary listing "EVOLUTION AB" on **SFB** (Stockholm, contract_id 366244347); US line **EVVTY**, "EVOLUTION AB-ADR", **PINK**, contract_id 245152296 | IBKR |
| **ADR ratio** | 1:1 (unsponsored) | WebSearch (Citi Depositary Receipts); cross-checked internally (see below) |
| **Live price used** | **$71.72** (EVVTY, IBKR `get_price_snapshot`, `last`) | IBKR — bid $71.61 / ask $71.81, volume 10,998, prior close $70.69, +1.46% |
| Primary-listing cross-check | 695.00 SEK (+0.75%), same-day | stockanalysis.com `quote/sto/EVO/` |
| Implied FX cross-check | 695.00 / 71.72 = **9.690 SEK/USD** — internally consistent with a live EUR/USD IBKR quote (1.138575) and a separately-reported EUR/SEK proxy backed out from TTM EPS (€5.32 vs. SEK 59.3, ⇒ ≈11.15 SEK/EUR); no ratio adjustment needed | IBKR (EUR.USD), stockanalysis.com |
| **Data gap — IBKR has no market-data permission for SFB** (`get_price_snapshot`/`get_price_history` both returned empty/`"No market data permissions"` for contract_id 366244347). **Worked around by using the IBKR-tradable, 1:1 ADR (EVVTY) as the live-price and execution instrument instead** — this is the actual instrument this account would use to enter a position, so this is not a compromise on Rule 0, just the correct instrument for this account. | | IBKR |
| **Data gap — `yfinance`/Yahoo Finance unreachable this session.** Plain `curl` to `query1.finance.yahoo.com` returned **HTTP 429 "Too Many Requests"** (Yahoo's own edge, not a proxy failure — proxy status showed zero relay failures); `yfinance`'s `curl_cffi` client failed with a TLS reset on every ticker tried, **including US tickers (AAPL)** — this is a session-wide Yahoo-side rate-limit/block, not specific to EVO. Fundamentals below are sourced from **stockanalysis.com** (financial-statement pages) and cross-checked against IBKR/WebSearch where possible, consistent with this framework's established stockanalysis.com fallback (see TSLA/NOK/EFX/GLXZ sessions). Flagging for the next `/healthcheck` run. | | — |
| 52-week range | 515.40 – 887.60 SEK | stockanalysis.com |
| Analyst consensus 12-mo target | Avg **699.72 SEK**, high **1,103.24 SEK**, low **526.99 SEK**; rating **Neutral** (4 Buy / 6 Sell — genuinely split) | WebSearch (MarketScreener aggregation) |
| Market Cap | ≈$13.7B (191.49M shares × $71.72 ADR price) — cross-checks to $13.52B / SEK 132.09B reported independently by stockanalysis.com (~1.5% apart, consistent with snapshot-timing differences, not a data error) | Derived + stockanalysis.com |
| US 10Y Treasury yield | 4.65% (carried forward, see header) | 2026-07-22 GOOG session |

---

## 2. Quality Score (Phase 01) — full calculation

**Inputs sourced from stockanalysis.com's STO:EVO financial-statement pages** (income statement, balance sheet, cash-flow statement, ratios — TTM ended Jun 2026 plus FY2022–FY2025), reported in **EUR millions**.

| Metric | TTM (Jun'26) | FY2025 | FY2024 | FY2023 | FY2022 |
|---|---|---|---|---|---|
| Revenue | 2,104 | 2,118 | 2,214 | 1,799 | 1,457 |
| Operating Income (EBIT) | 1,238 | 1,257 | 1,420 | 1,143 | 908.1 |
| Net Income | 1,062 | 1,062 | 1,244 | 1,071 | 843.4 |
| Net Margin | 50.50% | 50.14% | 56.18% | 59.54% | 57.89% |
| Operating CF | 1,307 | 1,255 | 1,301 | 1,168 | — |
| CapEx | (71.6) | (64.6) | (65.3) | (42.2) | — |
| FCF | 1,236 | 1,191 | 1,236 | 1,126 | — |
| ROIC | — (n/a TTM) | 32.40% | 38.57% | 34.89% | 28.91% |
| Net Debt | 1,063 | 726.9 | 707.8 | 906.3 | — |

**Data caveat:** stockanalysis.com reports "Gross Profit = Revenue" (100% gross margin) for EVO — this data source doesn't break out a separate cost-of-revenue line for this business (a live-dealer-studio content licensor). Used as-reported per Rule 0 (never invent a COGS split); flagged since it caps the Margins sub-score at 100.0 rather than reflecting an economically "true" gross margin figure. The underlying economics (operating margin 58–64%, net margin 50–60%) independently support "very high margin" regardless of this line-item quirk. **ROIC TTM not separately disclosed** by this source — used FY2025's 32.40% (latest full-year figure) as the best-available proxy; flagged.

**Hard disqualifiers — checked, none fire:**
- FCF/NI <70% for 2+ years? No — 112–116% every year shown. **Clear.**
- Net Debt/EBITDA over threshold? No — **net cash** position (negative net debt) every year shown. **Clear.**
- Not FCF-positive 3+ years? No — positive all 4 years shown (€1,126M–€1,307M). **Clear.**

**Sub-scores:**

**Profitability (25%):** NetMargin_Component = clamp(50.50/30×100) = 100.0 (capped). ROIC_Component = clamp(32.40/30×100) = 100.0 (capped). No FCF cap (FCF-positive). **Profitability_Score = 100.0**

**Margins (15%):** GrossMargin_Score = clamp(100/80×100) = 100.0 (capped; caveat above). **Margins_Score = 100.0**

**Growth (20%):** Revenue 3yr CAGR (FY2022→FY2025) = (2,118/1,457)^(1/3) − 1 = **13.27%**. Growth_Score(raw) = clamp(13.27/25×100) = 53.08.
- **+10 TAM-expansion modifier:** North America live-dealer gaming is approved in only **7 of 50 US states** as of this session — a documented, long structural runway (WebSearch, Gambling Insider 2026-07 coverage), and Q1 2026 NA revenue grew +21.4% in local currency.
- **−10 structural-deceleration modifier:** Europe (EVO's largest region) posted **multi-quarter revenue declines** (Q1 2026 −11.9% YoY) driven by **stricter player-protection regulation in the UK, Germany, and Sweden (its home market)** — not a one-off, but a documented multi-quarter regulatory-driven trend; consolidated TTM revenue is down vs. the FY2024 peak (€2,104M vs. €2,214M).
- Both modifiers are independently documented and concern different segments of the same business (NA runway vs. Europe headwind) — applied together per the letter of the rule, net effect **0** this time. Flagging explicitly since this is a judgment call: a reader weighing only the currently-observable (Europe decline, already dragging consolidated TTM revenue down) vs. only the forward-looking (NA runway, not yet reflected in consolidated figures) could reasonably net this to −10 or +10 instead of 0 — shown transparently rather than picking one silently.
- **Growth_Score = 53.08** (unchanged after net-zero modifier)

**Balance Sheet (15%):** Net Debt/EBITDA is **negative** (net cash) every year shown — formula clamp(100×(1−ratio/4)) exceeds 100 for a negative ratio, clamped. **BalanceSheet_Score = 100.0**

**Moat Signal (15%)** — scored strictly; only signals with an actual cited source per the specific evidence type required are marked TRUE:
| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | ~60–70% global B2B live-casino market share vs. nearest rival Playtech's ~15% (WebSearch: Quartr, Willow Oak Asset Management, ad-hoc-news.de) |
| Switching costs | **TRUE** | Documented mechanism with a quantified figure: true cost of switching exceeds **€15–25M for a mid-sized operator**, ≈18–24 months of contract value, driven by proprietary-game/studio integration depth (WebSearch, financial-newsletter sourcing — secondary, not a primary filing; flagged as lower-confidence than a 10-K citation) |
| Brand premium | FALSE | No pricing-power evidence found (price increases without volume loss) — not credited without a citation |
| Network effect | FALSE | B2B content-licensing model, not a two-sided marketplace — no documented network-effect mechanism found |
| Scale cost advantage | FALSE | Scale itself is well documented (1,700+ tables, 20+ studios, 800+ operators) but the specific required evidence — **cost-per-unit data vs. smaller competitors** — was not found; scale ≠ the cited cost-per-unit gap this criterion strictly requires |

Moat_Score = (2/5) × 100 = **40.0**

**FCF Quality (10%):** FCF/NI (TTM) = 1,236/1,062 = **116.4%**. FCFQuality_Score = clamp(((1.164−0.40)/0.60)×100) = 127.3 → clamped. **FCFQuality_Score = 100.0**

```
Quality Score = 100.0×0.25 + 100.0×0.15 + 53.08×0.20 + 100.0×0.15 + 40.0×0.15 + 100.0×0.10
              = 25.0 + 15.0 + 10.616 + 15.0 + 6.0 + 10.0
              = 81.616 → 81.6
```

**⚠️ Quality Score = 81.6 — clears the 80.0+ gate by only 1.6 points.** This margin is thin enough to be sensitive to a single judgment call: if the Moat count were 1/5 instead of 2/5 (dropping the secondary-sourced "switching costs" figure), Quality Score would fall to **78.6 and FAIL the gate**. Flagging this prominently rather than presenting 81.6 as a confident, comfortable pass — the switching-cost citation is the single most load-bearing, lowest-confidence input in this calculation.

**PASSES the 80.0+ gate (marginally) — proceeds to Phase 02.**

---

## 3. Phase 02 — Valuation Score

**PEG eligibility check:** Is EVO a Fast Grower (EPS growth >15%/yr for 3+ years on a clean base)? **No.** Full-year EPS: FY2024 €5.93 → FY2025 €5.25 — a **−11.5% YoY decline**, the opposite of Fast-Grower criteria. **PEG not applicable — 15% weight redistributed to EV/EBIT (→ 40%).**

**FCF Yield (40%):** TTM FCF €1,236M × 1.138575 (live EUR/USD, IBKR) = $1,407.2M. Market Cap $13,733M (§1). FCF Yield = 1,407.2/13,733 = **10.25%**. FCF_Score = clamp(100×(1−10.25/10)) = clamp(−2.5) → **0.0**

**EV/EBIT (40%, PEG-redistributed):** Total Debt €90.2M→$102.7M; Cash €1,154M→$1,314.0M. EV = 13,733+102.7−1,314.0 = **$12,521.7M**. EBIT TTM €1,238M→$1,409.5M. EV/EBIT = 12,521.7/1,409.5 = **8.88×**. EV/EBIT_Score = clamp((8.88−12)/23×100) = clamp(−13.6%) → **0.0**

**Forward PE (20%):** Forward PE **10.71**, Trailing PE **11.72** (stockanalysis.com). 5yr PE range (WebSearch, wisesheets.io-sourced aggregation): Low **13.4×** (Dec 2024), High **52.0×** (2021), Avg **22.92×**. Primary formula: FwdPE_Score = clamp((10.71−13.4)/(52.0−13.4)×100) = clamp(−6.97%) → **0.0** (forward PE is already below the cited 5yr low). Historical PE Modifier: deviation from 5yr avg = (10.71−22.92)/22.92 = **−53.3%**, well beyond the −20% threshold → −10 modifier, but score already at floor. **FwdPE_Score = 0.0**

```
Raw weighted score = 0.0×0.40 + 0.0×0.40 + 0.0×0.20 = 0.0
+ Rate Regime Modifier: +5.0 (10Y 4.65%, 3.5–5% bracket)
```

### Upside/Downside Modifier

**Step 1 — Expected annual return E:**
- PW Fair Value inputs — used the analyst-consensus spread directly (WebSearch, MarketScreener) as the bull/base/bear scenario, rather than constructing independent multiple-reversion scenarios, to avoid inventing unsourced numbers: Bull $113.85 (1,103.24 SEK ÷ 9.690), Base $72.21 (699.72 SEK ÷ 9.690), Bear $54.38 (526.99 SEK ÷ 9.690).
- `PW Fair Value = 0.25×113.85 + 0.50×72.21 + 0.25×54.38 = $78.16`
- `Gap Upside % = (78.16/71.72) − 1 = +8.98%`
- Catalyst window: **2 years** (no narrower documented window — default per Rule 10). Grounded catalysts within this window: UKGC settlement now resolved (removes the near-term regulatory overhang), Europe already showing sequential improvement (Q2 2026 revenue +3.5% QoQ, ending several quarters of decline), the €2B buyback program running through the 2027 AGM, continued NA state-by-state approval.
- `Annualized gap = 8.98% / 2 = 4.49%/yr`
- Intrinsic growth: derived from the Forward-vs-Trailing PE ratio (11.72/10.71 − 1) = **+9.43%/yr** (a citable, non-invented proxy for near-term consensus EPS growth, rather than using the historical 3yr revenue CAGR which mixes in years before the current deceleration).
- Shareholder yield: **4.44%** dividend yield only (stockanalysis.com). The company's own EUR 2B / up-to-10%-of-shares buyback program (resolved 2026, running to the 2027 AGM) is real and citable, but is a **maximum authorization, not a confirmed realized pace** — deliberately **not** quantified into E to avoid overstating a forward-looking cash return off an un-executed ceiling; noted here as qualitative bull-case support instead.
- `E = 4.49 + 9.43 + 4.44 = 18.36%/yr`

**Step 2 — Guardrail check:** documented catalysts exist within 18–24 months (above) — no cap applied.

```
E (18.36%) ≥ H (10%): M = −15 × clamp((18.36−10)/15, 0, 1) = −15 × 0.557 = −8.36
```

```
Final Valuation Score = clamp(0.0 + 5.0 − 8.36, 0, 100) = clamp(−3.36, 0, 100) = 0.0
```

---

## 4. Composite Score

```
Composite Score = 0.50×(100 − Quality Score) + 0.50×Valuation Score
                = 0.50×(100 − 81.6) + 0.50×0.0
                = 9.2 + 0.0 = 9.2
```

**Composite Score = 9.2 — "Very Cheap" (0.0–29.9) band**, per the Phase 03 table this would normally call for entering now with a 6–8% position.

---

## 5. Fair Value & Order Setup ([fair-value-methodology.md](../framework/fair-value-methodology.md))

**Method A — DCF (simplified single-stage, flagged as such — not a full 10yr staged model given the qualitative growth-trajectory uncertainty documented in §2's Growth modifier):**
- FCF/share TTM: €1,236M ÷ 191.49M shares = €6.455 → $7.349 (×1.138575)
- Base-case near-term FCF growth: conservative **+3%/yr** (reflecting the Europe-stabilizing/NA-growing net picture, not the pre-deceleration historical CAGR) → FCF₁ = $7.57
- WACC: CAPM cost of equity = Rf(4.65%) + Beta(0.70, stockanalysis.com) × ERP(5%) = 8.15%, +1.35pp for foreign-domicile/regulatory-headwind risk premium → **WACC ≈ 9.5%**
- Terminal growth: **2.5%** (long-run GDP cap, Rule 2)
- `DCF FV/share = 7.57 / (0.095 − 0.025) = $108.14`

**Method B — Multiples (PW blend from §3):** **$78.16/share**

```
Blended FV = 0.40×108.14 + 0.60×78.16 = 43.26 + 46.90 = $90.15
```

**Margin of Safety:** Composite falls in the 0.0–29.9 "high-quality, predictable FCF" row (15–20% MoS) — but given the razor-thin 1.6-point quality-gate margin (§2) and genuine analyst disagreement (4 Buy/6 Sell), used the **conservative end, 20%**.

```
Buy Price = 90.15 × (1 − 0.20) = $72.12
```

Live price ($71.72) is at/marginally below this buy-price ceiling → nominally in "Enter Now" territory (Composite 0.0–29.9 + price at/under buy ceiling). **Entry price used for R/R = live price $71.72** (consistent with this framework's convention when live price already clears the buy ceiling — see 2026-07-05 NVDA session).

```
Sell Target (baseline FV)   = $90.15
Bull-Case Trim Target       = 113.85 × 0.90 = $102.47
Stop Loss (20% max loss — the tightest permitted for this Composite tier, 20–25%)
                            = 71.72 × 0.80 = $57.38

R/R = (90.15 − 71.72) / (71.72 − 57.38) = 18.43 / 14.34 = 1.29:1
```

**R/R = 1.29:1 — FAILS the mandatory 2:1 minimum**, even at the tightest stop this Composite tier permits (a wider, 25%-max-loss stop makes R/R worse, not better, since it enlarges the denominator faster than any assumption changes the numerator). Per fair-value-methodology.md Step 6: *"If R/R is below 2:1: wait for lower entry, find tighter stop, or pass on the trade entirely."*

---

## 6. Recommendation

**PASS — do not enter. Watchlist only.**

The Composite Score (9.2, "Very Cheap") and the underlying multiples (FCF yield ~10%, EV/EBIT ~8.9×, Forward PE below its own 5-year low) all say this is statistically one of the cheapest names this framework has evaluated. But two independent gates hold the recommendation back from a BUY:

1. **The Quality Score gate passes by only 1.6 points** (81.6 vs. 80.0), hinging on a single secondary-sourced Moat signal (switching costs) — a less comfortable pass than a typical BUY candidate in this book.
2. **The mandatory 2:1 Risk/Reward gate fails outright (1.29:1)** — the market's own analyst consensus (average target essentially at the current price, a genuinely split 4-Buy/6-Sell rating) implies the "cheap on trailing multiples" story is substantially offset by real, priced-in doubt about whether the European regulatory-driven revenue decline is temporary or structural. This is the same pattern this framework has already seen block seven current BUY-band holdings (see holdings.md's 2026-06-20 rescore note) and killed WSE's entry in June — a statistically cheap score is necessary but not sufficient without an adequate margin between entry and stop.

This is a name worth re-visiting if either (a) Europe's Q2 2026 sequential improvement (+3.5% QoQ) continues into a confirmed multi-quarter trend, which would raise the Base-case fair value and widen R/R, or (b) the price falls further without a fundamental deterioration, tightening the entry-to-stop gap from the other side.

---

## 7. Watchlist & Stale-Score Actions

- Created `watchlist/not-in-portfolio/EVO/EVO-2026-07-24.md` (first-ever entry for this ticker — nothing to supersede or mark stale).

---

## 8. Data Gaps Flagged (summary)

1. **IBKR has no market-data permission for EVO's primary Stockholm listing (SFB)** — worked around using the 1:1 ADR (EVVTY), which is also the actual tradable instrument for this account. Not a compromise of Rule 0, but flagged for the record.
2. **`yfinance`/Yahoo Finance was rate-limited/blocked this entire session** (HTTP 429 from Yahoo's own edge on a plain `curl`; `curl_cffi` TLS resets on every ticker including US names) — not EVO-specific. Fundamentals sourced from stockanalysis.com instead, per this framework's established fallback. **Flagging for `/healthcheck` to pick up** — this may recur on other tickers until Yahoo's rate limit clears.
3. **ROIC TTM not separately disclosed** by stockanalysis.com for EVO — used FY2025's ROIC (32.40%) as the best-available proxy.
4. **"Gross margin" as reported (100%) is a data-source artifact**, not a true COGS-based gross margin — EVO's cost-of-revenue isn't broken out separately by this source. Used as-reported per Rule 0; flagged rather than estimated.
5. **The "switching costs" Moat Signal citation is secondary-sourced** (financial newsletter aggregation, not a primary filing) — the single most load-bearing, lowest-confidence input in the Quality Score gate calculation (see §2's sensitivity note).
6. **The buyback program's EUR 2B / ≤10%-of-shares authorization was deliberately excluded from the Upside/Downside Modifier's shareholder-yield input** (used dividend yield only) since it's a maximum ceiling, not a confirmed realized pace — noted qualitatively instead.

None of these blocked scoring (all sub-scores were computable from real, cited data) — they're flagged for transparency and for the next `/healthcheck` pass, not as reasons to skip this evaluation.

---

## 9. Glossary

See [framework/glossary.md](../framework/glossary.md) for full definitions. Terms used in this session: **ADR (American Depositary Receipt)**, **Sponsored ADR / Unsponsored ADR**, **OTC Pink Sheets**, **UKGC (UK Gambling Commission)** *(new term added this session)*, **CAGR**, **TAM**, **Moat**, **Net Debt/EBITDA**, **EBITDA**, **Fast Grower**, **PEG ratio**, **Shareholder yield**, **Buyback yield (net buyback yield)**, **Beta**, **Equity Risk Premium (ERP)**, **WACC**, **Terminal Value**, **TTM (Trailing Twelve Months)**.
