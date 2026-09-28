# RESCORE — CSGP (CoStar Group, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-09-28
**10Y US Treasury Yield:** **5.21%** (TradingEconomics, US 10-Year Treasury Note yield, 2026-09-28 — "near its highest level since mid-2007," attributed to hawkish Fed commentary and persistent inflation concern).
**Rate Regime Modifier (Step 2):** +10 (5.21% is now **above the 5% bracket** — a new regime vs. the 08-09 session's 4.66%/"3.5–5%"/+5)
**Last review on record:** CSGP **84.8** (Valuation) / **69.2** (Quality) / **57.8** (Composite) — 2026-08-09, [sessions/2026-08-09-rescore-csgp.md](2026-08-09-rescore-csgp.md). Action: HOLD, no add/trim, flagged Phase 04 Quality Watch.
**Current CSGP portfolio weight:** 1.19% per [holdings.md](../portfolio/holdings.md) — nowhere near the 15% hard cap (Upgrade 7).
**Sector:** Real Estate — commercial real estate data, analytics & marketplaces (CoStar Suite, LoopNet, Apartments.com) plus the residential build-out (Homes.com, Domain) and, as of 2026-08-21, new-home construction data (Zonda). Treated as Technology/Growth-style for fair-value method (EV/EBIT multiples + scenario DCF) per Rule 1, given the software-like ~79% gross margin — unchanged reasoning from every prior session.

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$27.09** | IBKR `get_price_snapshot` (contract_id 6726677, NASDAQ/SMART), `last` field, ts 2026-09-28 19:55:13 UTC, `halted: false`. Also equals IBKR's `plprice` (mark price, $27.085) — internally consistent. |
| Change (session) | −$1.00 (−3.56%) | IBKR `change` |
| Cross-check | $27.035 | Yahoo `info.currentPrice`, fetched same session — consistent within pennies of IBKR. |
| 52-week range | $25.89 – $85.24 (52w-ago open $83.09) | IBKR `misc_statistics` |
| 13-week range | $25.89 – $33.82 | IBKR `misc_statistics` |
| 26-week range | $25.89 – $41.63 | IBKR `misc_statistics` |
| Analyst consensus PT | mean **$37.30**, n=20, recommendation "buy" | Yahoo `info.targetMeanPrice`/`numberOfAnalystOpinions`, fetched this session — sanity anchor only (Rule 0 Step 4), never a scored input. Roughly flat vs. 08-09's $37.10 (was as low as ~$37.0 mid-September per press coverage, e.g. Simply Wall St's Sept-4 "$37 mean, down from $48" report). |
| Dividend yield | 0.0% (no dividend) | IBKR + Yahoo consistent |

**IBKR $27.09 used as the Rule-0 primary price** — down **11.9%** from $30.75 at the 08-09 review, and down materially further from the $30.00–$34 range that has prevailed through most of this ticker's session history.

---

## 2. Data Gaps / Flags

1. **Price has fallen sharply (−11.9%) since the last review, driven by disclosed, cited events — not treated as a standalone Rule 9 "unexplained move" trigger (well under 15%) but the magnitude is real and explained by:** the FTSE All-World Index removal (2026-09-19, forced index-fund selling/ownership event — [Simply Wall St News, "How Index Removal Will Impact CoStar Stock Investors"](https://simplywall.st/stocks/us/real-estate-management-and-development/nasdaq-csgp/costar-group/news/how-index-removal-will-impact-costar-stock-investors/amp)), continued investor scrutiny over slowing net-new-bookings and the Homes.com turnaround (per Simply Wall St's September CSGP coverage), and the sector-wide GenAI/residential-portal competitive-pressure narrative cited in the same coverage. A Sept-16 data point independently corroborates the decline: shares at $30.36, "down 15.1% over the past 30 days and 57.6% year to date."
2. **Zonda acquisition CLOSED 2026-08-21 — a genuine Rule 9 material-M&A trigger, now realized rather than pending.** SEC 8-K ([sec.gov/Archives/edgar/data/0001057352/000105735226000072/costargroupcompletesacqu.htm](https://www.sec.gov/Archives/edgar/data/0001057352/000105735226000072/costargroupcompletesacqu.htm)): $800M cash, closed 2026-08-21. Zonda contributed ~$170M 2025 revenue at a 23% adjusted EBITDA margin, "a scaled, profitable, and highly recurring subscription business." **The financing source (existing cash vs. new debt vs. a mix) is not disclosed in the completion 8-K** — I did not find it in any other source checked. This means the $64.0M net-cash figure used throughout §4–8 below (the last *filed* balance sheet, Q2 FY2026, period ended 2026-06-30) is now **stale relative to the real, current balance sheet** — the $800M cash outflow happened but is not yet reflected in any filed financial statement (Q3 FY2026, ending 2026-09-30, has not yet been reported; next earnings 2026-10-27). Per Rule 0/never-invent, this session does **not** estimate a pro-forma post-close balance sheet. **Flagged sensitivity (using only the actual, disclosed $800M figure, not invented):** if funded entirely from cash with no offsetting new financing, the ~$800M outflow works out to **≈$1.97/share** (405.2M shares) of net-cash-per-share reduction — which would pull every fair-value scenario in §8 down by roughly that amount if applied, and would very likely flip the company from its filed net-cash position into a net-debt position. **This must be explicitly re-examined once the Q3 10-Q discloses the actual post-close balance sheet — not estimated here.**
3. **Homes.com leadership change — a second Rule 9 management-change trigger since 08-09.** Felix Kusch named President of Homes.com effective 2026-09-14 ([BusinessWire/Morningstar, 2026-09-14](https://www.businesswire.com/news/home/20260914121926/en/CoStar-Group-Names-Felix-Kusch-President-of-Homes.com); [HousingWire](https://www.housingwire.com/articles/costar-felix-kusch-homes-com/)) — an external hire (ex-CEO of Immoweb, Belgium's #1 portal, and Immowelt, Germany's #2 portal), distinct from the internal-promotion CFO transition (Rossmann) flagged at 08-09. This is a strategic segment-leadership change (not a continuity-only appointment like Rossmann's), coinciding with Homes.com's first profitable quarter (Q2 FY2026, $12M adjusted EBITDA, +$41M sequential improvement; Homes.com revenue +66% YoY to $28.5M — [Yahoo Finance/HousingWire coverage](https://finance.yahoo.com/real-estate/articles/costar-group-names-felix-kusch-203500355.html)). No moat-signal or quality-sub-score adjustment is made from this alone (no cited evidence yet of a strategy pivot) — carried as a Rule 9 trigger and a forward-monitoring item for the 2026-10-27 earnings call.
4. **No new quarterly financial data since the 08-09 session.** CoStar's fiscal Q3 2026 ends 2026-09-30 (today is 2026-09-28) and reports 2026-10-27 — so every TTM figure below (revenue, EBIT, EBITDA, net income, FCF, D&A, CapEx, tax rate) is drawn from the **same** Q2 FY2026 (period ended 2026-06-30) filed financials used at 08-09, refetched and re-verified this session, not restated. Only the live price, Treasury yield, and qualitative/Rule-9 fields are genuinely new this session.
5. **Script data-quality flag: `fetch_fundamentals.py`'s `net_debt_to_ebitda` and `roic_pct` this session used `t.balance_sheet` (ANNUAL, most recent column FY2025-end, 2025-12-31) rather than the quarterly (TTM-consistent, Q2 FY2026) balance sheet — a mismatch against the TTM-basis EBIT/NOPAT numerator used in the same calc.** Verified directly: `t.balance_sheet` (annual) shows Total Debt $1,184.0M / Cash $1,633.0M / Invested Capital $9,327.0M (FY2025-end), vs. `t.quarterly_balance_sheet` (Q2 FY2026) Total Debt $1,202.0M / Cash $1,266.0M / Invested Capital $8,926.0M — the same figures used in the 08-09 and 07-04 sessions. Using the annual denominator against a TTM numerator would understate ROIC and overstate net cash relative to the correct, period-matched basis. **This session uses the quarterly (Q2 FY2026) balance sheet figures for Net Debt/EBITDA and Invested Capital/ROIC** — real, directly-fetched yfinance data, not invented, just correctly period-matched, consistent with every prior CSGP session's convention. Flagged here rather than silently substituted; worth a PR fix to `scripts/fetch_fundamentals.py` (use `quarterly_balance_sheet`, matching the TTM basis used everywhere else in the script) — out of scope for this rescore to fix directly.
6. **5-year historical PE range is now genuinely available for the first time in this ticker's session history — a real methodological change, not an error.** `fetch_fundamentals.py`'s `_pe_history()` reconstructs the series from `get_earnings_dates()` (consensus/**non-GAAP** "Reported EPS," the same basis as the forward-EPS estimate used for Forward PE) paired with same-day-or-later close price, rather than the `fundamentals-timeseries` **GAAP** `quarterlyDilutedEPS` endpoint every prior session hit (which capped at 5 usable quarters and was itself too distorted by 2023–2025's GAAP EPS collapse). Verified directly: all 44 quarters back to 2015 have **positive** non-GAAP TTM EPS (no exclusions triggered), and the 20 quarters used span 2021-10-26 → 2026-07-28 (≈4.75 years) — a genuine, not-truncated 5yr-ish window. Result: **`pe_mode = "range"`, 5yr avg 69.583× / low 27.367× / high 113.750×, n=20 quarters** — used as the *primary* Forward-PE method (valuation-scoring.md) for the first time, replacing the `FwdPE_Score = 50.0` neutral no-history fallback used in every prior CSGP session. This materially changes the Forward PE sub-score (see §7) — flagged prominently as a structural change in how this input is computed, not a data error.
7. **PEG still not applicable.** Annual diluted EPS ($0.93 → $0.92 → $0.34 → $0.02, 2022–2025, GAAP) is declining, not growing >15%/yr on a clean base — CSGP is not a Fast Grower under this framework's definition. PEG's 15% weight redistributed to EV/EBIT (→ 40%), unchanged from every prior session.
8. **FY2026/FY2028 guidance confirmed unchanged since 08-09.** FY2026 revenue guide **$3.715–3.755B**, adjusted EBITDA guide **$780–820M** (reaffirmed, "+$30M at the midpoint vs. February 2026 guidance" — [StreetInsider](https://www.streetinsider.com/Corporate+News/CoStar+Group+forecasts+$3.8+billion+revenue+and+$770+million+adjusted+EBITDA+for+2026/25817035.html) coverage of the same 2026-07-28 release used at 08-09); Q3 FY2026 guide $935–945M revenue / $190–210M adjusted EBITDA. No new guidance revision found since 08-09 — this is the same 07-28 guide, re-confirmed via a second independent source, not a new Rule 9 event. FY2028 medium-term target ($1.25B adjusted EBITDA) not re-confirmed by any fresher release this session (no new press release found); carried forward per continuity.
9. **Q3 FY2026 net-new-bookings and net-cash figures not yet available** — next disclosure 2026-10-27. The 08-09 session's flagged bookings deceleration (Q2 FY2026: $69M, −26% YoY) is carried forward as an open monitoring item, not re-verified with fresher data this session (none exists yet).
10. **Framework-process flag (not a data gap, but material to this session's output — see §9):** valuation-scoring.md states explicitly, "A company only reaches this step after clearing the 80.0+ Quality Score gate... Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate." The 07-04 and 08-09 CSGP sessions both computed a Composite Score (56.1, 57.8) despite Quality Score failing the gate both times. This session follows the documented rule as written and does **not** compute a Composite Score — `composite_score.py` was not run, per this session's explicit instruction not to work around its refusal. This is flagged here, in the watchlist entry, and should be recorded in `decisions/` or otherwise reconciled by the user, since it's an inconsistency between two prior sessions' practice and the current documented methodology, not something this session is positioned to resolve unilaterally.

No data was invented anywhere below. Every fallback/flag is the documented one from the framework, or an explicitly-labeled, disclosed-data-only sensitivity — never an invented substitute.

---

## 3. Independent Data Corroboration

Live price cross-checked across two independent sources (IBKR $27.09, Yahoo $27.035 — consistent within pennies). Q2 FY2026 financials (unchanged since 08-09) were already cross-checked at that session across Yahoo, CoStar's own 8-K, and independent media coverage — not re-derived from scratch here since no new quarter has reported; instead, the raw balance-sheet/income-statement figures were re-fetched this session and verified to match the 08-09 session's figures exactly (see §2 flag 4–5), confirming data stability rather than staleness. The Zonda-close and Kusch-appointment items were each corroborated across 2+ independent sources (SEC 8-K + trade press for Zonda; BusinessWire + HousingWire + Yahoo for Kusch) before use.

---

## 4. Inputs Collected (this session)

| Item | Value | Basis |
|---|---|---|
| Shares outstanding | 405,197,588 | Yahoo `info.sharesOutstanding` — unchanged from 08-09 (no new quarter) |
| **Market Cap (live price)** | 405,197,588 × $27.09 = **$10,976.80M** | Computed on Rule-0 price |
| Total debt (Q2 FY2026, 2026-06-30) | $1,202.0M | yfinance `quarterly_balance_sheet` — unchanged from 08-09; see §2 flag 5 for why quarterly (not annual) is used |
| Cash & equivalents (Q2 FY2026) | $1,266.0M | yfinance `quarterly_balance_sheet` — unchanged |
| **Net cash (Q2 FY2026, filed)** | $1,266.0M − $1,202.0M = **+$64.0M** | Computed — **stale relative to the real post-Zonda-close balance sheet; see §2 flag 2** |
| **Enterprise Value (live price basis)** | $10,976.80M − $64.0M = **$10,912.80M** | Computed |
| Revenue (TTM, Q3'25–Q2'26) | **$3,555.5M** (unchanged) | yfinance quarterly series, re-verified this session |
| Gross Profit (TTM) | **$2,797.6M** — Gross Margin **78.68%** (unchanged) | Computed, re-verified |
| **EBIT (TTM)** | **+$77.0M** (unchanged) | yfinance `quarterlyEBIT`, re-verified |
| EBITDA (TTM) | **$394.0M** (unchanged) | Computed, re-verified — ties to `fetch_fundamentals` output (`ebitda_ttm=394,000,000`) |
| **Net Income (TTM)** | **$73.6M** (unchanged) — **Net Margin 2.070%** | Computed, re-verified |
| Pretax income (TTM) / Tax provision (TTM) | $101.1M / $27.5M — **effective tax rate 27.20%** (unchanged) | Computed, re-verified |
| FCF (TTM) | **$227.0M** (unchanged) | Computed, re-verified — ties to `fetch_fundamentals` (`fcf_yield_pct` implies FCF $227.0M at its own price basis) |
| Invested Capital (Q2 FY2026, quarterly basis) | **$8,926.0M** | yfinance `quarterly_balance_sheet` — see §2 flag 5 |
| Revenue FY2022 → FY2025 | $2,182.4M → $2,455.0M → $2,736.0M → $3,247.0M | Unchanged — FY2025 still the most recently *completed* fiscal year |
| **Revenue 3yr CAGR** | (3,247.0/2,182.4)^(1/3) − 1 = **14.16%** | Computed — unchanged inputs |
| Forward EPS (consensus, non-GAAP, FY2027 estimate) | **$1.77373** (up from $1.72529 at 08-09) | Yahoo `earnings_trend`, `+1y` row, `avg` column — genuinely refreshed this session |
| **Forward PE (recomputed on live price)** | $27.09 ÷ $1.77373 = **15.27×** | Computed |
| FCF/NI annual %, oldest first (4 fiscal years) | 104.17% / 92.53% / **−176.26%** / 585.71% | `fetch_fundamentals CSGP --json`, `fcf_ni_annual_pct` — one additional oldest year vs. the 08-09 session's 3-year table, no change to the disqualifier conclusion (still only one year below 70%, not 2+ consecutive) |
| FCF-positive 3yr+ (rolling window) | **False** | `fetch_fundamentals` (`fcf_positive_3yr_or_more: false`) — same FY2023–FY2025 window as 08-09 (FY2026 not yet complete); hard disqualifier still fires |
| 5yr PE avg / low / high (n=20 quarters) | **69.583 / 27.367 / 113.750** | `fetch_fundamentals CSGP --json` — first-ever usable range, see §2 flag 6 |

**`python -m scripts.fetch_fundamentals CSGP` raw output (pasted verbatim):**
```
## Fundamentals — CSGP

Market Cap            = 10,934,257,664
Enterprise Value      = 11,283,999,744
Shares Outstanding    = 405,197,588
Forward PE            = 15.214
FCF Yield %           = 2.076
EV/EBIT               = 146.545
Net Margin %          = 2.070
Gross Margin %        = 78.684
ROIC % (NOPAT/InvCap) = 0.601  [tax_rate=0.2720, NOPAT=56,055,391, InvestedCapital=9,327,000,000]
Revenue 3yr CAGR %    = 14.161
Net Debt/EBITDA       = -1.140  [EBITDA_ttm=394,000,000]
FCF/NI TTM %          = 308.424
FCF/NI annual (oldest first) = [104.2%, 92.5%, -176.3%, 585.7%]
FCF positive 3yr+     = False
5yr PE avg/low/high   = 69.583 / 27.367 / 113.750  (n=20 quarters)
```
**Note on divergence from the table above:** the script's own `Market Cap`/`Enterprise Value`/`Forward PE`/`FCF Yield`/`EV/EBIT` use *its own* yfinance-fetched price (~$26.98 at fetch time, not the Rule-0 IBKR live price) and its ROIC/Net-Debt-to-EBITDA use the annual (not quarterly) balance sheet — see §2 flag 5. This session recomputes Market Cap/EV/Forward PE/FCF Yield/EV-EBIT on the **Rule-0 live price ($27.09)** and recomputes ROIC/Net-Debt-to-EBITDA on the **quarterly (Q2 FY2026) balance sheet**, per Rule 0 and per the period-matching flagged above — consistent with the convention every prior CSGP session used. The script's raw `5yr PE avg/low/high` and `Revenue 3yr CAGR` and `FCF/NI` figures are used as-is (no basis mismatch in those).

---

## 5. CSGP — Quality Score (2026-06-29 methodology)

### Script output (`python -m scripts.scoring.quality_score --input csgp_quality.json`), pasted verbatim:
```
# FAILS GATE
Reason: Not FCF-positive for 3+ consecutive years
```
The script applies hard disqualifiers **before** computing the weighted score, per quality-scoring.md's documented order ("applying the hard disqualifiers BEFORE the weighted calculation") — so it does not print sub-scores once a hard disqualifier fires.

### Hard disqualifier check (fiscal-year rolling window, unchanged from 08-09)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years unexplained? | FY(oldest) 104.2% / 92.5% / **−176.3%** / 585.7% — only one year dips below 70%, not consecutive | disqualify if 2+ yrs | ✅ PASS |
| Net Debt/EBITDA over threshold? | −0.162× (net cash, filed Q2 FY2026 basis) | disqualify if >2.5× (standard) | ✅ PASS, comfortably (though see §2 flag 2 — real current position likely worse post-Zonda-close, not yet disclosed) |
| **FCF-positive 3+ consecutive years?** | Most recently completed FY window (FY2023–FY2025): FY2023 (+$347.0M) → **FY2024 (−$245.0M)** → FY2025 (+$41.0M) | disqualify if not | ⚠️ **TRIGGERS** — same window, same result as every session since 07-04. Won't clear until FY2027 completes (fresh FY2025–FY2027 window) *and* both FY2026 and FY2027 hold FCF-positive. FY2026 is tracking positive so far (TTM FCF +$227.0M). |

**CSGP fails the 80.0+ Quality Gate via this unwaivable hard disqualifier**, independent of the weighted score below — same status as every session since 2026-07-04.

### Supplementary manual weighted-score breakdown (for Phase 04 Quality Watch continuity — the script does not compute this once the hard disqualifier fires; shown here for transparency, matching every prior CSGP session's practice, but it does **not** override the FAILS GATE result above)

**Profitability (25% weight)**
```
Net Margin (TTM)        = $73.6M / $3,555.5M = 2.070%
NetMargin_Component     = clamp((2.070/30)x100) = 6.90

Effective tax rate (TTM)= $27.5M / $101.1M = 27.20%
NOPAT                   = EBIT(TTM, $77.0M) x (1 - 0.2720) = $56.06M
Invested Capital        = $8,926.0M (Q2 FY2026, quarterly basis - see S2 flag 5)
ROIC (TTM)               = $56.06M / $8,926.0M = 0.628%
ROIC_Component           = clamp((0.628/30)x100) = 2.09

Profitability_Score     = (6.90 + 2.09) / 2 = 4.50
```
FCF-positive-3yr cap (40.0) does not bind — 4.50 is already far below it.

**Margins (15% weight)**
```
Gross Margin (TTM) = $2,797.6M / $3,555.5M = 78.68%
GrossMargin_Score  = clamp((78.68/80)x100) = 98.35
```
No structural-trend bonus (gross margin still mildly declining YoY, as at every prior session).

**Growth (20% weight)**
```
Growth_Score = clamp((14.16/25)x100) = 56.64
+10 TAM/pricing-power evidence (see S2, moat evidence citations, and quality inputs JSON) - refreshed this
    session with the closed Zonda deal and Homes.com's first profitable quarter.
Growth_Score (with bonus) = clamp(56.64 + 10) = 66.64
```

**Balance Sheet (15% weight)**
```
Net Debt/EBITDA (Q2 FY2026, filed) = -$64.0M / $394.0M = -0.162x (net cash)
BalanceSheet_Score = clamp(100x(1 - (-0.162)/4)) = clamp(104.06) = 100.0
```
Flag (unchanged from 08-09, now sharper — see S2 flag 2): filed, pre-Zonda-close basis only.

**Moat Signal (15% weight)** — all 5 signals TRUE, evidence refreshed with Zonda close + Homes.com leadership/profitability data (full citations in `csgp_quality.json`, summarized in S2 and S4):
```
Moat_Score = (5/5) x 100 = 100.0
```

**FCF Quality (10% weight)**
```
FCF/NI (TTM) = $227.0M / $73.6M = 308.42%
FCFQuality_Score = clamp(((3.0842 - 0.40)/0.60)x100) = clamp(447.4) = 100.0
```
Same caution as every prior session: inflated by a thin (2.07% margin) Net Income base.

**Supplementary weighted total:**
```
Quality Score = (4.50x0.25) + (98.35x0.15) + (66.64x0.20) + (100.0x0.15) + (100.0x0.15) + (100.0x0.10)
              = 1.125 + 14.753 + 13.328 + 15.000 + 15.000 + 10.000
              = 69.206 -> 69.2 (rounded to nearest 0.1)
```

# Quality Score = 69.2 (supplementary calc) — FAILS the 80.0+ gate both by hard disqualifier and by weighted score, essentially flat vs. 08-09's 69.2

**Read carefully:** every input to this calc is identical to 08-09's, except the Growth-modifier citations, which were refreshed with genuinely new evidence (Zonda close, Homes.com's first profitable quarter, Kusch appointment) rather than merely carried forward — the underlying financial data has not changed because no new quarter has reported. This is a **Phase 04 Quality Watch escalation**, continued unchanged from 08-09 and 07-04 — CSGP is **not** force-exited on quality alone, but the persistent gate failure, now compounded by the not-yet-disclosed Zonda balance-sheet impact, merits continued closer-than-routine attention into the 2026-10-27 earnings report.

---

## 6. CSGP — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = $27.09 / $1.77373 = 15.27x
EY         = 1 / 15.27 = 6.549%
Spread     = EY - 10Y Treasury = 6.549% - 5.21% = +1.339pp
```
Pass threshold: Spread >= +1.5%. **Result: FAIL** (down from a razor-thin +0.951pp *fail* at 08-09, but now failing by a wider margin as the 10Y yield jumped sharply to 5.21% while forward PE also ticked up) -> **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 5.21% -> **">5%" bracket, a new regime vs. the 08-09 session's "3.5-5%"** -> **+10** (up from +5)

**Total Rate Modifier = +15** (up sharply from +10 at 08-09 — this is the single largest mechanical driver of this session's inputs, a rate-environment shift wholly unrelated to CSGP's own fundamentals).

---

## 7. CSGP — Phase 02 Valuation Score

**Full script output (`python -m scripts.scoring.valuation_score --input csgp_valuation.json`), pasted verbatim:**
```
## Valuation Score

**FCF Yield (40%)**
FCF_Score = clamp(100x(1 - 2.068/10)) = 79.320

**EV/EBIT**
EV/EBIT_Score = clamp((141.72 - 12)/23 x 100) = 100.000

**Forward PE**
FwdPE_Score (raw) = clamp((15.27 - 27.367)/(113.75 - 27.367) x 100) = 0.000
Deviation vs 5yr avg (69.583) = (15.27 - 69.583)/69.583 x 100 = -78.055%
Historical PE Modifier: >20% below 5yr avg -> -10
FwdPE_Score = clamp(0.000 + -10) = 0.000

**PEG**
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT

**Rate Environment Gate**
EY = 1/15.27 x 100 = 6.5488%
Spread = EY - 10Y (5.21%) = 1.3388pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.21% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15

**Upside/Downside Modifier**
PW Fair Value = 0.25x43.59 + 0.50x32.24 + 0.25x17.93 = 31.5000
Gap Upside % = (31.5000/27.09) - 1 = 16.2791%
Annualized gap = 16.2791% / 2yr = 8.1395%/yr
E = 8.1395 (annualized gap) + 12.0 (intrinsic growth) + 4.6900 (shareholder yield: 0.0 div + 4.69 buyback) = 24.8295%/yr
E (24.8295%) >= H (10.0%) -> M = -15 x clamp((24.8295-10.0)/15, 0, 1) = -14.8295
Upside/Downside Modifier (bounded [-15, +15]) = -14.8295

**Raw Weighted Score**
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 71.728

**Final Valuation Score**
Final Score = Raw (71.728) + Rate Modifier (+15) + Upside/Downside Modifier (-14.830)
= 71.898 -> rounds to 71.9

# Valuation Score = 71.9
```

**FCF Yield input:** $227.0M / $10,976.80M (live-price market cap) = 2.068%.
**EV/EBIT input:** $10,912.80M (live-price EV) / $77.0M = 141.72x.

**First-time-ever primary (range-based) Forward-PE treatment for CSGP** (§2 flag 6): the current forward PE (15.27x) sits **far below** its own reconstructed 5yr range (27.37x–113.75x low/high, 69.58x avg) — both the raw range-position formula and the Historical PE Modifier clamp to the 0.0 floor. This reflects that CSGP's own multiple has compressed dramatically over the past ~5 years (from a much richer growth-stock rating down to today's depressed, post-earnings-crash levels) — a real, disclosed-data-driven result, not an artifact; flagged since it's a first for this ticker's scoring history and swings the Forward-PE sub-score from a neutral 50.0 (08-09) to 0.0 this session.

---

## 8. CSGP — Upside/Downside Modifier (Expected-Return Modifier), detail

Same scenario architecture as every prior CSGP session (EV/EBIT-multiple method on normalized ~2027–2028 EBIT) — the underlying guided targets (FY2026 adjusted EBITDA $780–820M, confirmed unchanged §2 flag 8) support keeping the same Normalized EBIT / exit-multiple assumptions for continuity (per Guardrail 2, never re-inflating toward the rosy point). Only the live price changed vs. 08-09; net-cash add-back and share count are unchanged (no new quarter — see §2 flag 4).

| Scenario | Wt | Normalized EBIT | Exit EV/EBIT | FV/share |
|---|---|---|---|---|
| Bull | 25% | $800M | 22.0× | **$43.59** |
| Base | 50% | $650M | 20.0× | **$32.24** |
| Bear | 25% | $450M | 16.0× | **$17.93** |

```
PW Fair Value = 0.25x43.59 + 0.50x32.24 + 0.25x17.93 = $31.50 (unchanged from 08-09)
```

**Flagged sensitivity (§2 flag 2):** these FV/share figures still embed the *filed* +$64.0M net-cash add-back, not the real post-Zonda-close balance sheet. If the $800M acquisition were funded entirely from cash with no new financing (undisclosed either way), each scenario's FV/share would be reduced by roughly $1.97/share (≈$800M/405.2M shares) — Bull ≈$41.62, Base ≈$30.27, Bear ≈$15.96, PW FV ≈$29.53. **Not adopted as the primary figure** since the financing structure is undisclosed and this session does not invent it — shown only as a bounding sensitivity using real, disclosed transaction data.

- **Gap Upside %** = ($31.50 ÷ $27.09) − 1 = **+16.28%** — a large jump from 08-09's +2.44%, driven entirely by the price decline (FV held flat).
- **Catalyst & timeline (Rule 10):** Same documented, management-guided catalyst as every prior session — the Homes.com net-investment cut and the guided adjusted-EBITDA path (FY25 $191M actual -> FY26 $780-820M guide -> FY28 $1.25B target, unchanged). **2-year window** (unchanged). Annualized gap = 16.28% ÷ 2 = **+8.14%/yr**.
- **Intrinsic growth: +12%/yr** (unchanged — still conservative vs. the 14.16% 3yr revenue CAGR and the ~15% medium-term guided CAGR).
- **Shareholder yield: +4.69%/yr** (carried forward from 08-09's freshly-computed figure — no new diluted-share-count data since Q2 FY2026; flagged as not re-verified this session, since no new quarter has reported). No dividend (0.0%).

```
E = 8.14 (annualized gap) + 12.0 (intrinsic growth) + 4.69 (shareholder yield) = 24.83%
```

**Map to modifier** (H = 10%): E >= H -> M = -15 x clamp((24.83-10)/15, 0, 1) = -15 x 0.9887 = **-14.83** — very close to the full -15 floor, reflecting how far the price has fallen relative to an unchanged fair-value estimate.

**Guardrail check:** (1) catalyst exists within 18–24 months -> no −5 upside cap. (2) Bull/base/bear PW FV used, not the rosy point — Bull ($43.59) remains above the $37.30 consensus mean, same divergence flagged at 08-09, not mechanically adjusted. (3) Full calc shown. (4) Bounded ±15 — within range, near the floor.

---

## 9. CSGP — Final Scores and Action Recommendation

| | Value |
|---|---|
| Raw weighted (valuation) | 71.728 |
| Rate Gate (Step 1 fail +5, Step 2 +10) | +15 |
| Upside/Downside Modifier | −14.830 (E = +24.83%) |
| **FINAL VALUATION SCORE** | **71.9** |
| Prior valuation score (08-09) | 84.8 |
| **Quality Score** | **FAILS the 80.0+ gate** (hard disqualifier; supplementary weighted calc 69.2, essentially flat vs. 08-09's 69.2) |
| **Composite Score** | **Not computed** — per valuation-scoring.md, not computed for a gate-failing company (see §2 flag 10) |

**Raw Valuation Score alone (71.9) falls in the 70.0–79.9 "TRIM 25–30%" band** — one band *lower* than 08-09's 84.8 ("Trim to 50%"), because the deep Upside/Downside discount (−14.83, near the modifier's floor) more than offset the sharply larger Rate Modifier (+15 vs +10). **This raw signal is shown for context only and is not used to drive this session's action**, consistent with valuation-scoring.md's instruction to use the Composite Score (not the raw score) once a company has a Quality Score on file — and no Composite is computable this session (§2 flag 10).

**Action Recommendation: HOLD the existing position — no forced trim, no add, no order setup.**

Reasoning, since the framework does not provide an explicit action-table path for an existing holding that (a) fails the Quality gate and (b) therefore has no computable Composite Score:
- Per this session's explicit instruction and valuation-scoring.md's own text, a Composite Score is **not computed** — it is not this session's place to invent a substitute blended number or to act mechanically on the raw Valuation Score alone (which the framework explicitly says not to use once a Quality Score exists).
- Per rescore.md and this framework's Phase 04 practice: **"a held position dropping below the [quality] gate is itself a signal worth surfacing, even though existing holdings aren't retroactively force-exited on quality alone."** No Phase 06 full-exit trigger is present: still (filed) net-cash, gross margin intact at 78.68%, revenue growing unbroken, all 5 moat signals documented TRUE, and the raw Valuation Score has not sustained 90.0–100.0 for 2+ consecutive quarters (the only score-based exit trigger) — in fact it's well below that band this session.
- No new evidence of fundamental deterioration this quarter — the opposite in several respects (Homes.com's first profitable quarter, a new external segment president, the Zonda deal actually closing and adding a real, cited TAM-expansion asset).
- The genuinely new, material open item is the **undisclosed Zonda financing/post-close balance sheet** (§2 flag 2) — this is the single most important thing to resolve at the 2026-10-27 earnings report, since an all-cash-funded $800M outflow against a $64.0M net-cash cushion would flip the Balance Sheet sub-score and could plausibly bear on the Net-Debt/EBITDA hard-disqualifier check going forward.

**Net recommendation: HOLD the existing position — no forced trim, no add.** Current position: 1.19% of portfolio (per [holdings.md](../portfolio/holdings.md)) — already a small, tracking-sized position, unaffected by the 15% cap either way. **No order setup run** (operating-brief.md OUTPUT FORMAT step 6 applies only to BUY/TRIM actions; this session's action is HOLD).

**No full exit** — Phase 06 triggers absent, per the bullet list above.

---

## 10. Next Review Trigger

- **Next earnings: Q3 FY2026, confirmed 2026-10-27** (Yahoo `calendarEvents`). Standard re-score, with specific attention to:
  - **The Zonda acquisition's actual post-close balance-sheet/leverage impact** — financing structure, pro-forma net debt/cash, and whether it changes the Balance Sheet sub-score or the Net-Debt/EBITDA hard-disqualifier check (§2 flag 2).
  - Whether net new bookings stabilize or continue decelerating (carried from 08-09, §2 flag 9) — and whether that eventually shows up in realized revenue growth.
  - Whether FY2026 full-year FCF comes in positive (tracking positive so far on a TTM basis, +$227.0M) — needed, together with a positive FY2027, to finally clear the FCF-positivity hard disqualifier on the rolling 3-year basis.
  - How the new Homes.com president (Felix Kusch, effective 2026-09-14) beds in — any strategy shift.
  - Whether the Rate Environment (10Y Treasury) stays above 5% — a further sustained rise would push the Rate Regime Modifier no higher (already at its +10 ceiling) but keeps the Step 1 Earnings-Yield-Spread test under pressure.
- **Earlier if (Rule 9):** a guidance revision (up or down), a further management change, a >15% unexplained price move, or disclosure of the Zonda financing structure ahead of the Q3 report.
- **Quality Score watch:** re-check the hard disqualifier and the Profitability sub-score every quarter.
- **Framework process item (flagged, not resolved by this session):** reconcile the 07-04/08-09 sessions' Composite Score computation with valuation-scoring.md's explicit "not computed for a gate-failing company" rule (§2 flag 10) — via a `decisions/` entry or a framework clarification, at the user's discretion.

---

## 11. Housekeeping

- No `⚠️ STALE SCORE` banner existed on the [08-09 entry](../watchlist/in-portfolio/CSGP/CSGP-2026-08-09.md) to clear — CSGP has been scored under the current 2026-06-29 methodology continuously since 07-04.
- New dated watchlist entry created: [watchlist/in-portfolio/CSGP/CSGP-2026-09-28.md](../watchlist/in-portfolio/CSGP/CSGP-2026-09-28.md) — warranted per [watchlist/README.md](../watchlist/README.md)'s "significant change" criteria (valuation score changed 84.8 -> 71.9, and two independent Rule 9 triggers fired: Zonda close, Homes.com leadership change).
- `python -m scripts.watchlist_diff` run with `--old-score 84.8 --old-category HOLD --new-score 71.9 --new-category HOLD --fundamental-event` -> decision `new_file`, reason "Rule 9 fundamental-event trigger fired". Its `content` output was pasted verbatim into the new watchlist row.
- `python -m scripts.stale_score --apply` run — output: `{"version": "2026-06-29", "newly_stale": [], "resolved": []}`. CSGP appears in neither list, as expected — it carried no `⚠️ STALE SCORE` banner to clear (continuously current under the 2026-06-29 methodology since 07-04) and this session doesn't trigger a version bump.
- [holdings.md](../portfolio/holdings.md) is **not** updated by this session — left for the orchestrator, per this session's explicit instructions.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **Composite Score** | This framework's single ranking number (0.0–100.0, 0.0 = most attractive) blending the Quality Score and the Valuation Score 50/50 — `0.50 × (100 − Quality Score) + 0.50 × Valuation Score` — computed only for companies that have already cleared the 80.0+ Quality Score gate. Not computed this session (§2 flag 10, §9). |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **Effective tax rate** | The actual percentage of a company's pretax income paid as income tax in a given period (tax provision ÷ pretax income) — distinct from the statutory tax rate. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT, EV/EBITDA** | Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **Fast Grower** | Peter Lynch's term for a company growing EPS faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score. CSGP doesn't qualify (declining GAAP EPS). |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score; not every hard disqualifier has a carve-out (the FCF-positivity check does not). |
| **Hurdle rate** | The minimum acceptable annual return for an investment to be worth making — this framework uses 10% as the hurdle the Upside/Downside Modifier measures expected return against. |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator in a ROIC calculation. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **NI (Net Income)** | Accounting profit after all expenses, interest, and taxes. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Owner Earnings** | Net Income + D&A − maintenance CapEx only. Not triggered this session (Upgrade 1 test — see prior sessions). |
| **PEG ratio** | PE ÷ earnings growth rate — not applicable to CSGP (not a Fast Grower). |
| **Buyback yield (net buyback yield)** | The rate a company's share count shrinks per year from repurchasing its own stock, net of new issuance — this session's shareholder-yield component. |
| **PW (Probability-Weighted) Fair Value** | 25% bull + 50% base + 25% bear scenario blend (Rule 7). |
| **Quality Score** | This framework's 0.0–100.0 grading of profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to clear the gate. CSGP fails it this session (supplementary calc 69.2). |
| **R/R (Risk/Reward ratio)** | Reward-to-risk ratio for a trade — not computed this session (no BUY/TRIM action, no order setup). |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. +10 this session (5.21% 10Y, the highest bracket). |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital into profit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained price move. Two fired this session: Zonda close, Homes.com leadership change. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent four reported quarters combined, used instead of a single fiscal-year snapshot. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | An additive ±15 adjustment to the valuation score based on expected annual return — folds the forward-looking dimension into the score. −14.83 this session, near its floor, reflecting a large price decline against an unchanged fair-value estimate. |
| **Value trap** | A stock that looks statistically cheap but stays cheap because underlying business quality is deteriorating or was never strong enough to support a re-rating — the risk this session's Phase 04 Quality Watch is specifically monitoring for. |
