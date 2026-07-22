# NEW POSITION — E (Eni S.p.A., NYSE-listed ADR) — 2026-07-19

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 19 Jul 2026 (Sunday, session executed 2026-07-20 00:xx UTC)
**10Y US Treasury Yield:** 4.57% (FRED `DGS10`, most recent posted observation dated 2026-07-16 — recorded for completeness only; this session stops before the Rate Environment Gate would apply, see §4)
**Current E portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/E/` or `watchlist/not-in-portfolio/E/`)
**Sector:** Energy — Integrated oil & gas major (exploration & production, refining, chemicals, gas-fired power, renewables)
**First-use jargon decode:** see closing Glossary (§7)

---

## 0. Why this session exists — trigger source, and ticker disambiguation

A post on **bolshegold** (Telegram, post bolshegold/9795, ~09:46 UTC 2026-07-19), previewing the upcoming earnings-reporting week, said: *"$LMT, $E - можно тоже посмотреть насчет их прогнозов на энергетику и ВПК"* ("LMT and E — also worth checking their energy/defense-sector forecasts"), in a context discussing Strait-of-Hormuz/Iran-related energy and defense demand. LMT (Lockheed Martin) was evaluated separately in this framework's 2026-07-20 LMT session. This session covers **only** "$E".

**Ticker disambiguation (performed before any scoring work, per Rule 0's "never invent or estimate" discipline extended to ticker identity):** A bare single-letter cashtag is inherently ambiguous, so this was checked explicitly via IBKR's `search_contracts` tool before proceeding:

- `search_contracts("E")` returned exactly one primary, actively-traded NYSE listing for the literal symbol "E": **contract_id 2007205, symbol "E", description "ENI SPA-SPONSORED ADR", exchange NYSE, country_code US** — i.e. the ADR of Eni S.p.A., the Italian integrated energy major.
- The only other bare-"E" equity match was **contract_id 198500875, "ENTERPRISE GROUP INC"** on the Toronto Stock Exchange (Canada) — a small, unrelated industrial-services company with no connection to energy exploration/production or the post's "энергетику" (energy sector) framing.
- A second search, `search_contracts("Eni")`, confirmed the same NYSE contract_id 2007205 as the primary US-listed ADR (distinguishing it from Eni's home-market Borsa Italiana listing "ENI" on BVME, its Mexican cross-listing, and unrelated similarly-named tickers like Square Enix or Enigma-Bulwark).

Given (a) the post's own energy-sector framing ("энергетику"), (b) the fact that Eni is a large, globally-recognized energy major with an actively-traded NYSE ADR under the exact bare ticker "E", and (c) the only alternative bare-"E" match being a tiny, unrelated Canadian company with no energy connection, this resolves confidently and without real ambiguity to **Eni S.p.A. (NYSE: E)**. Proceeding with the full evaluation.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$49.77** | IBKR `get_price_snapshot`, `last` field, contract_id **2007205** (NYSE). `is_close: true` — last completed-session close, not a live intraday trade, because at fetch time (2026-07-20 00:32 UTC ≈ Sunday 20:32 ET) US markets are closed; per Rule 0 this is still the most recent price obtainable via a live fetch attempt (same situation as the 2026-07-19 AXP session). Cross-checked against Yahoo Finance's `regularMarketPrice` (also $49.77, `exchangeName: NYQ`) — consistent. |
| 52-week high | $57.36 (IBKR) / $58.00 (Yahoo) | IBKR `misc_statistics` `high_52w`; Yahoo `fiftyTwoWeekHigh` |
| 52-week low | $31.18 (IBKR) / $32.99 (Yahoo) | IBKR `misc_statistics` `low_52w`; Yahoo `fiftyTwoWeekLow` |
| 13-week high | $56.34 | IBKR `misc_statistics` `high_13w` |
| 26-week high | $57.36 | IBKR `misc_statistics` `high_26w` |
| Open 52 weeks ago | $31.52 | IBKR `misc_statistics` `open_52w` |
| Dividend yield | 4.91% | Yahoo `summaryDetail.dividendYield` |
| US 10Y Treasury yield | 4.57% | FRED `DGS10`, as-of 2026-07-16 |

$49.77 sits in the upper-middle of its 52-week range, up materially (+58% from the 52-week open) — consistent with elevated global energy prices amid the Strait-of-Hormuz/Iran tensions the triggering post referenced. Context only, not scored. **IBKR's live bid/ask snapshot returned an unusually wide, likely-stale quote (bid $48.25 / ask $54.80) at fetch time — not used for anything; the `last` trade price is used instead, per standard practice when a live two-sided quote isn't reliably available outside market hours.**

---

## 2. Data Gathered — Sources & Method

### 2.1 Source note

`yfinance`'s default `curl_cffi` transport hit a TLS/connection-reset error in this session's environment (same class of issue documented in several prior sessions). **Fallback used:** Yahoo Finance's own `quoteSummary` and `fundamentals-timeseries` JSON APIs, queried directly via `requests` (with a valid session cookie + crumb) rather than through the `yfinance` package wrapper — the same underlying data source `yfinance` itself uses, just accessed directly. All figures below are Eni's own reported figures as carried by Yahoo's structured financial-statement feed (10-K/20-F-sourced), reported in **USD** (Yahoo's `financialCurrency`/`price.currency` both read `USD` for this feed — confirmed, not assumed) for FY2022–FY2025 (fiscal year end 31 Dec).

**Sanity check on the USD figures:** Eni files in EUR at home, but Yahoo's US-listed "E" feed is denominated in USD. Cross-check: implied market cap ($72.3B) against shares outstanding (1.4533B ADR-equivalent shares) is internally consistent with Eni's real-world scale (~€60–65B at prevailing EUR/USD), and the reported FY2022 revenue figure ($132.5B) matches Eni's own widely-reported FY2022 EUR revenue (~€132.7bn) to within rounding — no currency-conversion distortion found.

### 2.2 Income statement (annual, FY2022–FY2025)

| FY (end 31-Dec) | Revenue | Cost of Revenue | Gross Profit | EBIT | EBITDA | Net Income | Diluted EPS |
|---|---|---|---|---|---|---|---|
| 2022 | $132,512M | $109,734M | $22,778M | $31,382M | $38,587M | $13,887M | $7.90 |
| 2023 | $93,717M | $81,315M | $12,402M | $18,341M | $25,820M | $4,771M | $2.80 |
| 2024 | $88,797M | $78,714M | $10,083M | $15,469M | $23,069M | $2,624M | $1.56 |
| 2025 | $82,151M | $74,405M | $7,746M | $13,948M | $21,297M | $2,608M | $1.56 |

TTM (most recent trailing-twelve-month window per Yahoo `financialData`, extending slightly past FY2025 into early-2026 quarters): Revenue $84,479M, Net Margin 2.97%, ROE 5.91%.

### 2.3 Cash flow (annual, FY2022–FY2025)

| FY | Operating Cash Flow | CapEx | Free Cash Flow | FCF/NI |
|---|---|---|---|---|
| 2022 | $17,460M | −$8,059M | $9,401M | 67.70% |
| 2023 | $15,119M | −$9,215M | $5,904M | 123.76% |
| 2024 | $13,092M | −$8,490M | $4,602M | 175.38% |
| 2025 | $13,330M | −$9,229M | $4,101M | 157.29% |

**Company is FCF-positive in all 4 fiscal years shown.** FCF/NI ratio is below 70% in exactly **one** year (FY2022, 67.70%) and comfortably above 100% in each of the following three years — not 2+ consecutive years below 70%, so the FCF/NI hard disqualifier does **not** fire (§3.1).

**Data-quality flag:** Yahoo's TTM `freeCashflow` field (`financialData.freeCashflow`) reads **−$939M** (negative) — a materially different, more recent window than the FY2025 annual figure above (+$4,101M), implying the trailing four quarters through roughly Q1 2026 turned cash-flow negative (likely elevated capex and/or working-capital swings amid the recent price volatility). This is flagged explicitly as a monitoring item (§6) but **not** substituted for the annual-basis FCF/NI computation above, consistent with this framework's existing precedent (the 2026-06-20 MSFT worked example in valuation-scoring.md) of computing this ratio on full, audited fiscal-year figures rather than an unaudited in-year TTM stitch.

### 2.4 Balance sheet (annual, FY2022–FY2025)

| FY | Total Debt | Net Debt | Cash | Stockholders' Equity | Invested Capital |
|---|---|---|---|---|---|
| 2022 | $31,868M | $15,904M | $10,058M | $54,759M | $80,721M |
| 2023 | $34,065M | $17,785M | $9,988M | $53,184M | $80,957M |
| 2024 | $36,843M | $20,383M | $8,129M | $52,785M | $81,297M |
| 2025 | $34,202M | $19,298M | $8,099M | $47,940M | $75,337M |

```
Net Debt/EBITDA (FY2025) = 19,298 / 21,297 = 0.906×
```
Well under the 2.5× standard Debt Gate threshold (Eni is not an asset-light payment network/exchange, so the Upgrade 5 <4× override does not apply). No disqualifier fires (§3.1).

### 2.5 ROIC construction

Yahoo does not directly publish a TTM ROIC figure for this feed, so it is derived from reported EBIT, effective tax rate, and invested capital (each individually a real, reported Yahoo figure — not an invented value):

```
NOPAT (FY2025) = EBIT × (1 − effective tax rate) = 13,948 × (1 − 0.24) = 10,600.5M
ROIC (FY2025)  = NOPAT / Invested Capital = 10,600.5 / 75,337 = 14.07%
```
Effective tax rate (24.0% for FY2025, per Yahoo `annualTaxRateForCalcs`) cross-checked against FY2025 Pretax Income ($5,778M) and Tax Provision ($3,020M): implied rate 52.3% — a large discrepancy, likely reflecting a different treatment of non-controlling-interest/exceptional items in the "tax rate for calcs" field versus the raw pretax-income/tax-provision ratio. **Flagged as a data-interpretation caveat** (§6): using the higher implied 52.3% rate would instead give NOPAT = 13,948 × 0.477 = $6,653M and ROIC = 8.83% — materially lower. Both readings are shown; the sensitivity is addressed in §3.2 and does not change the gate outcome either way (§3.5).

### 2.6 Growth and moat evidence

- Revenue has **declined every year** from FY2022 ($132.5B, the global energy-price-crisis peak year) through FY2025 ($82.2B) — a 3-year CAGR of **−14.73%** (§3.2), consistent with global oil/gas prices normalizing well off their 2022 peak, not a company-specific growth story.
- **No documented TAM-expansion or pricing-power evidence was sourced this session** for the Growth sub-score's qualitative modifier — not researched in depth given the modifier is immaterial to the outcome (§3.2, §3.5).
- **Moat-signal evidence was not gathered/cited this session** (no sources pulled for market share, brand premium, network effect, switching costs, or scale-cost-advantage). This is an explicit, disclosed gap (§6), not a guess — and it is immaterial to the Quality Gate outcome regardless of how it would resolve (§3.5 shows the gate fails even under the most generous possible Moat Score).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a growth-capex explanation | 67.70% / 123.76% / 175.38% / 157.29% (FY2022–FY2025) — only **one** year (FY2022) below 70% | disqualify if 2+ consecutive years sub-70% | ✅ **PASS** — not 2 consecutive years |
| Net Debt/EBITDA over threshold | 0.906× (FY2025) | disqualify if >2.5× (standard; Eni is not asset-light, so no 4× override) | ✅ **PASS**, comfortably clean |
| FCF-positive 3+ consecutive years | All 4 of the last 4 fiscal years positive | disqualify if not | ✅ **PASS**, clean |

**No hard disqualifier fires.** Eni's failure below (§3.5) is driven entirely by the weighted Quality Score, not by a balance-sheet or cash-flow-quality trip-wire — a materially different shape of result than several prior financial-company sessions in this framework (JPM/C/SOFI/AXP), where an un-computable or borderline sub-score was the blocking issue. Here, every sub-score **is** computable; the business itself is simply thin-margin and shrinking in its current reported financials.

### 3.2 Quality Score — full calculation

**PROFITABILITY (25% weight):**
```
Net Margin (TTM) = 2.97%  (Yahoo financialData.profitMargins; cross-checks to FY2025 annual 2,608/82,151 = 3.18%)
NetMargin_Component = clamp((2.97/30)×100, 0, 100) = 9.90

ROIC (FY2025, used as TTM proxy — no quarterly EBIT/invested-capital breakdown available for this
foreign-filer feed):
  Primary reading (24.0% effective tax rate, Yahoo's own "tax rate for calcs"):
    NOPAT = 13,948 × (1 − 0.24) = 10,600.5M
    ROIC  = 10,600.5 / 75,337 = 14.07%
    ROIC_Component = clamp((14.07/30)×100, 0, 100) = 46.90
  Sensitivity (52.3% implied rate from raw Pretax Income/Tax Provision, §2.5):
    NOPAT = 13,948 × 0.477 = 6,653M
    ROIC  = 6,653 / 75,337 = 8.83%
    ROIC_Component (sensitivity) = clamp((8.83/30)×100, 0, 100) = 29.43

Profitability_Score (primary)     = (9.90 + 46.90) / 2 = 28.40   (no FCF-positivity cap — 4yr positive, §3.1)
Profitability_Score (sensitivity) = (9.90 + 29.43) / 2 = 19.67
```

**MARGINS (15% weight):**
```
Gross Margin (FY2025) = 7,746 / 82,151 = 9.43%
Trend: 17.19% (2022) → 13.24% (2023) → 11.36% (2024) → 9.43% (2025) — monotonically
CONTRACTING, not expanding — no +10 structural-trend bonus applies.
GrossMargin_Score = clamp((9.43/80)×100, 0, 100) = 11.79
```

**GROWTH (20% weight):**
```
Revenue 3yr CAGR = (82,151 / 132,512)^(1/3) − 1 = −14.73%
Growth_Score = clamp((−14.73/25)×100, 0, 100) = 0.00   (floored — formula clamps negative growth to 0)
```
No TAM-expansion/pricing-power modifier applied — no documented evidence sourced (§2.6). No structural-deceleration −10 modifier applied either — the decline reads as **cyclical** (global energy-price normalization off the 2022 crisis peak), and the modifier requires *structural* (not cyclical) deceleration evidence, which wasn't sought given immateriality (§3.5).

**BALANCE SHEET (15% weight):**
```
Net Debt/EBITDA (FY2025) = 19,298 / 21,297 = 0.906×
BalanceSheet_Score = clamp(100 × (1 − 0.906/4), 0, 100) = 77.34
```

**MOAT SIGNAL (15% weight):**

Not evidenced this session (§2.6) — no signals cited true or false with sources. Shown as a **[0, 100] range** rather than guessed:
```
Moat_Score ∈ [0.00, 100.00]   (contribution to final score: 0.00 – 15.00 points)
```

**FCF QUALITY (10% weight):**
```
FCF/NI (FY2025) = 4,101 / 2,608 = 157.28%
FCFQuality_Score = clamp(((1.5728 − 0.40)/0.60)×100, 0, 100) = clamp(195.5, 0, 100) = 100.00
```

### 3.3 Quality Score — weighted total

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

Fixed components (primary ROIC reading):
  0.25×28.40 + 0.15×11.79 + 0.20×0.00 + 0.15×77.34 + 0.10×100.00
  = 7.10 + 1.77 + 0.00 + 11.60 + 10.00 = 30.47

Adding Moat's full [0, 100] range:
  Floor  (Moat=0):    Quality Score = 30.47
  Ceiling (Moat=100): Quality Score = 30.47 + 15.00 = 45.47

Sensitivity — using the higher 52.3% effective-tax-rate ROIC reading instead (§3.2):
  Fixed components: 0.25×19.67 + 1.77 + 0.00 + 11.60 + 10.00 = 4.92 + 1.77 + 0.00 + 11.60 + 10.00 = 28.29
  Floor–ceiling range: 28.29 – 43.29
```

**Under every combination of the unresolved inputs (ROIC tax-rate reading, Moat Score anywhere from 0 to 100), the Quality Score ranges 28.3–45.5 — decisively and by a wide margin (at least ~34.5 points) below the 80.0 gate.** Unlike the 2026-07-19 AXP session (where the plausible range straddled 80.0 and the gate outcome was genuinely undetermined), this is not a close call: even the single most generous possible reading of every unresolved input falls far short.

### 3.4 Gate result: **FAIL — decisive, not close**

Quality Score (plausible range): **28.3 – 45.5**, vs. the required **80.0+**. **Fails the Quality Gate.** Per `quality-scoring.md` and this session's instructions, this evaluation **stops here: no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.**

---

## 4. Why Eni fails — plain-English summary

Eni is a large, real, financially solvent energy major (comfortable balance sheet at 0.906× Net Debt/EBITDA, free-cash-flow-positive every year, no hard disqualifier fires) — but its **current reported financials are those of a business well past its energy-price-cycle earnings peak**: Net Margin has fallen from double digits at the 2022 energy-crisis peak (implied by FY2022 net income of $13.9B on $132.5B revenue, a 10.5% margin) to just **2.97% TTM**; Gross Margin has contracted every year for four straight years (17.2% → 9.4%); and revenue has shrunk at a **−14.7%** 3-year CAGR. Three of the six Quality Score sub-scores (Profitability, Margins, Growth) are structurally weak in the current reporting window, and even crediting the two unscored/uncertain inputs (ROIC tax-rate treatment, Moat Signal) at their most generous plausible values cannot lift the total anywhere near 80.0.

This reads as a genuine cyclical-commodity-business result, not a framework mapping gap (unlike the JPM/C/SOFI/AXP sessions) — Eni's income statement maps cleanly onto every Quality Score sub-score formula; the formula simply returns a low score for a company currently earning thin margins on falling revenue, which is exactly the kind of result the 80.0+ gate is designed to screen out regardless of how cheap the stock might otherwise look on a valuation basis.

---

## 5. Recommendation: **PASS (no entry) — fails the 80.0+ Quality Gate decisively**

**Do not enter E (Eni) this session.** No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed, consistent with the standing rule that a sub-80.0 Quality Score stops the evaluation before Phase 02. The triggering Telegram post (a routine "worth checking their energy/defense forecasts" mention, itself just a reason to run this first-ever evaluation) was not relied upon for any figure or conclusion above.

---

## 6. Next Review Trigger / Data Gaps Flagged

**Data gaps (disclosed, not guessed around):**
1. **Moat Signal evidence not gathered** this session (§2.6, §3.2) — immaterial to the gate outcome (even Moat Score = 100.0 leaves the total at 45.5, §3.3), so not pursued further, but flagged for a future rescore if this name is ever revisited.
2. **TAM-expansion/pricing-power evidence not gathered** for the Growth modifier (§2.6) — also immaterial (Growth_Score is floored at 0.0 regardless; a +10 modifier would only apply to a positive base score, which doesn't exist here).
3. **Effective tax rate for the ROIC/NOPAT calculation is ambiguous** — Yahoo's own "tax rate for calcs" (24.0%) diverges sharply from the raw Pretax-Income/Tax-Provision ratio (52.3%), likely a non-controlling-interest or exceptional-item treatment difference (§2.5). Shown as a sensitivity range (§3.2); does not change the gate outcome either way.
4. **TTM free cash flow (per Yahoo's `financialData.freeCashflow`) is negative (−$939M)**, materially different from the FY2025 full-year figure (+$4,101M) used in this session's FCF/NI computation — flagged as a live monitoring item worth checking again at Eni's next earnings release, since a sustained negative-FCF quarter run (rather than a single volatile window) could eventually affect the FCF-positivity hard disqualifier if it persists.

**Next review trigger:**
- Eni's next earnings release (Q2/H1 2026 results) — would refresh the TTM window and confirm whether the recent negative-FCF quarter(s) are transient or the start of a trend.
- A sustained recovery in global refining/E&P margins (which would mechanically lift Net Margin, Gross Margin, and likely reverse the revenue decline) — the standard Rule 9 "macro shift" trigger.
- The standard Rule 9 triggers: guidance revision, management change, material M&A, or a >15% unexplained price move.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Glossary

| Term | Meaning |
|---|---|
| **ADR (American Depositary Receipt)** | Full entry in [glossary.md](../framework/glossary.md). Eni's NYSE ticker "E" is a sponsored ADR of the Borsa Italiana-listed ordinary share, USD-denominated. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. Eni's revenue CAGR (FY2022→FY2025) is −14.73% (§3.2). |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / — before Interest, Taxes, Depreciation, and Amortization — operating-profit measures used in this framework's Balance Sheet and ROIC calculations (§2.2, §2.5). |
| **Gross Margin** | Full entry in [glossary.md](../framework/glossary.md). Eni's Gross Margin has contracted every year, 17.2% (FY2022) to 9.4% (FY2025) (§3.2). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. None fired for Eni this session (§3.1). |
| **Invested Capital** | Full entry in [glossary.md](../framework/glossary.md). The denominator in this session's ROIC calculation — $75,337M for Eni at FY2025 (§2.4, §2.5). |
| **Net Debt/EBITDA** | Net Debt ÷ EBITDA — this framework's core leverage/Balance Sheet check. Eni's is 0.906× (FY2025), well under the 2.5× threshold (§2.4). |
| **NOPAT (Net Operating Profit After Tax)** | Full entry in [glossary.md](../framework/glossary.md). EBIT × (1 − effective tax rate); the numerator this framework uses to compute ROIC (§2.5). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. Eni's plausible range this session is 28.3–45.5 — a decisive fail (§3.3–3.4). |
| **ROIC (Return on Invested Capital)** | Full entry in [glossary.md](../framework/glossary.md). Eni's computed ROIC is 8.8–14.1% depending on the effective-tax-rate reading used (§2.5, §3.2). |
| **TTM (Trailing Twelve Months)** | Full entry in [glossary.md](../framework/glossary.md). The most recent 12 months of reported financial results, distinct from the FY2025 full fiscal year used for several of this session's sub-score computations (§2.3, §2.6). |
| **XBRL** | Full entry in [glossary.md](../framework/glossary.md). Not directly used this session (Eni is a foreign private issuer filing a 20-F, not a domestic 10-K filer under the SEC's XBRL `companyfacts` regime in the same way) — Yahoo Finance's structured financial-statement feed was used instead (§2.1). |
