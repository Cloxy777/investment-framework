# RESCORE — MSFT — 2026-07-30

**Task type:** RESCORE (mode `--both`)
**Date:** 30 Jul 2026
**10Y US Treasury Yield:** 4.70% (TradingEconomics, 30 Jul 2026 — up +0.02pp from the prior session)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket, unchanged)
**Last review on record:** MSFT **35.5** (2026-07-05, BUY-Standard band, raw Valuation Score basis — [sessions/2026-07-05-rescore-msft.md](2026-07-05-rescore-msft.md)); Quality Score 78.3 (primary)/81.3 (sensitivity), **failed the 80.0+ gate**; no Composite Score adopted.
**Current MSFT portfolio weight:** 14.62% per [holdings.md](../portfolio/holdings.md), as of the 26 Jul 2026 sync (**pre-earnings** — see §11, likely understated given today's price move).

**🚨 Rule 9 trigger fired this session: quarterly earnings (FY2026 Q4, reported 29 Jul 2026 after close).** Full fresh fundamentals pulled; the fiscal year just closed (30 Jun 2026 fiscal year-end), so FY2026 annual figures are a clean TTM window, not a rolling reconstruction.

> *Jargon decoded on first use: FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EBITDA = operating profit before depreciation/amortization; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; NOPAT = net operating profit after tax; ROIC = return on invested capital; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; TTM = trailing twelve months; NTM = next twelve months; RPO = remaining performance obligations (contracted future revenue not yet recognized).*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$449.40** | IBKR `get_price_snapshot` (contract_id 272093, NASDAQ), intraday `last` field, 30 Jul 2026 (not closed/frozen — `is_close: false`). Cross-validated against `yfinance` `currentPrice`/`regularMarketPrice` ($449.57/$449.50) — within 0.04%, consistent. |
| 52-week range | $349.20 – $552.28 | IBKR `misc_statistics` |
| Year-to-date change | −6.86% | IBKR (`year_to_date_change`) — a large improvement from −20.36% cited 07-05, driven almost entirely by today's earnings pop. |
| Analyst consensus PT | $555.77 mean (range $400–$870) | `yfinance` `targetMeanPrice`/`targetHighPrice`/`targetLowPrice`. **⚠️ Flag: may not yet reflect post-earnings analyst revisions** — pulled hours after the print; analysts typically take days to update formal targets after a beat this large. Used only as a bull-case sanity check (Rule 0 Step 4), not a scored input. |
| Price vs. 07-05 review ($390.49) | **+15.10%** | IBKR daily bars: 29 Jul close $390.54 → 30 Jul $449.42/last $449.40 — a >15% one-day move, but **fully explained by the earnings beat** (see §2) — not an "unexplained move" Rule 9 trigger in its own right; the earnings trigger already fired independently. |

---

## 2. Rule 9 Trigger Check (2026-07-05 → 2026-07-30)

| Trigger | Found? | Detail |
|---|---|---|
| **Quarterly earnings** | **YES** | FY2026 Q4 (quarter + fiscal year ended 30 Jun 2026), reported 29 Jul 2026 after close. **Major beat:** revenue $90.0B vs. $87.63B est. (+2.7%), EPS $4.74 (Street-comparable) vs. $4.24 est. (+11.8% surprise). Azure grew 43% YoY (vs. 39–40% guided), crossed $100B in annualized revenue. Commercial RPO +84% YoY to $678B. FY2027 Q1 guidance: Azure 45% cc growth, revenue $89.85–90.95B. **This alone is a mandatory re-valuation trigger (Rule 9) — full fresh data pull below.** |
| Guidance revision | No (routine) | FY27 Q1 guidance issued alongside earnings is the normal quarterly cadence, not a standalone revision event — folded into the earnings trigger already firing. |
| M&A (of an external company) | No | None found. |
| Management change | No | None found. |
| Macro shift | No | 10Y ticked 4.49% (07-05) → 4.70% (07-30) — still inside the "3.5–5%" bracket, no Rate Regime bracket change. |
| >15% unexplained price move | N/A | +15.10% one-day move, but fully explained by the earnings beat (see above) — not "unexplained." Moot regardless since the earnings trigger already fired. |

**Other items checked, none independently material beyond the earnings trigger already firing:**
1. **Workforce reduction — now company-confirmed and quantified (was press-sourced/escalating as of 07-05).** ~4,800–6,400 roles (2.1–2.8% of workforce) globally; Xbox division alone losing ~3,200 roles through FY2027 (1,600 immediate), confirmed by Chief People Officer Amy Coleman (early-to-mid July 2026, before this earnings report). Severance costs and an Xbox impairment charge are reflected in the Q4 results already captured below — not a fresh, separate trigger on top of the earnings print itself.
2. **Securities class action, case No. 26-cv-02071 — unchanged.** Lead-plaintiff deadline confirmed still **11 Aug 2026**; multiple law firms continue soliciting lead-plaintiff applicants for the same underlying Copilot-disclosure claims. No escalation.
3. **One-time items in Q4/FY26 GAAP results:** a $4.963B FY2026 net gain (Q4 portion $480M) from Microsoft's OpenAI equity stake (mark-to-market), adding $0.67 to FY26 GAAP diluted EPS ($0.07 in Q4) — **stripped out below per Rule 6 ("normalize before you value") for all scored inputs**; GAAP figures shown alongside for transparency. **Data-quality flag:** one secondary source (stocktitan.net) separately cited a "$3.2B Anthropic investment gain, +$0.27 Q4 EPS" — inconsistent with the OpenAI-labeled, differently-sized figure sourced independently from search results referencing Microsoft's own IR release. Used the OpenAI-labeled figures throughout (corroborated by two independent pulls landing on the same $4.963B/$0.67 FY26 numbers); flagging the discrepancy rather than silently picking one.

**Conclusion: Rule 9 quarterly-earnings trigger fired — full re-score required and performed below**, including the first fresh TTM window since 07-05 (previous 3 sessions' TTM figures were increasingly stale — see §3).

---

## 3. Tooling Note — Data Lag on Statement-Level Detail

`yfinance`'s quarterly/annual financial-statement endpoints (`quarterly_financials`, `financials`, `balance_sheet`, `quarterly_cashflow`) **had not yet ingested the FY2026 Q4/full-year statement data** as of this session (one day after the print) — they still cap out at Q3 FY2026 (3/31/2026) for quarterly data and FY2025 (6/30/2025) for annual data. Worked around by combining:
- `yfinance`'s **live snapshot fields** (`info` dict: price, forward PE, forward EPS, market cap, total debt/cash — these *are* current), and
- **Official Microsoft FY2026 Q4 earnings release figures** (via web search/fetch, cross-checked against two independent secondary sources — stocktitan.net and a Microsoft-IR-sourced search summary — which agreed on revenue, operating income, net income, EPS, and the OpenAI one-off), and
- **`stockanalysis.com`'s balance sheet and cash-flow-statement pages**, cross-validated by confirming they reproduced the *already-known* 3/31/2026 figures (stockholders' equity $414.367B, cash+ST investments $78.272B) exactly before trusting their fresh 6/30/2026 figures.

No SEC EDGAR direct fetch was possible this session (`sec.gov` returned 403 Forbidden on both the 10-K and the 8-K exhibit URLs) — relied on the cross-validated secondary sources instead, consistent with "never invent" (nothing here is estimated; everything is sourced and cross-checked, just not from the primary filing directly).

---

## 4. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved (8th consecutive session).** MSFT still discloses no maintenance-vs-growth capex split. Raw FY2026 (TTM-equivalent) Free Cash Flow used as the FCF_Score input, as in every session back to 06-07.
2. **One-time OpenAI investment gain stripped per Rule 6** — see §2 item 3. All Quality Score and Valuation Score net-income-based inputs below use the **normalized** figure (GAAP $133.7B − $4.963B = **$128.737B**); GAAP figures shown for reference.
3. **Q4FY26 buyback/dividend split not yet available** (same statement-lag pattern as §3) — shareholder yield computed from trailing-4-quarters-through-Q3FY26 cash-flow data (one quarter old), flagged explicitly rather than estimating the missing Q4 split.
4. **Total debt figure has two conventions in play, same as every prior session:** $40.3B (notes only — current $9.2B + long-term $31.1B, per the FY26 earnings release) vs. $56.8B (stockanalysis.com's broader convention, likely notes + operating lease liabilities). **Standard convention (notes only, $40.3B) used throughout**, consistent with prior sessions' methodology and the 07-05 session's SEC 10-Q robustness check.
5. **Position weight (14.62%) is pre-earnings** (26 Jul 2026 sync) — today's +15.1% price move has almost certainly pushed MSFT's actual current weight higher; not recomputed here (that's `/sync-portfolio`'s job) — flagged explicitly in §11 rather than assumed.
6. **Quality Score gate result is again NOT robust to one judgment call (Moat Signal, "Scale cost advantage")** — same open ambiguity as 07-05, margin now even narrower (0.1 point). See §6.
7. **5yr avg/range PE re-verified live, updated one quarter forward:** avg 31.546× (down slightly from 31.969×), range 24.169×–38.803× (n=20 quarters, through the 29 Jul 2026 earnings print) — the rolling window naturally shifts one quarter forward each earnings cycle.
8. **Gross margin — two-year compression trend now clearer:** FY2024 69.76% → FY2025 68.83% → FY2026 67.95%, a cumulative ~1.8pp decline over two years. **Does not (yet) meet the fair-value-methodology's ">3pp structural" sell-trigger threshold**, but flagged as a Phase 04 monitoring item given the scale of the ongoing AI-datacenter capex ramp.

---

## 5. MSFT — Inputs Collected (fresh this session, FY2026 = clean TTM window)

**Sector:** Technology — Software, Cloud Infrastructure (Azure) & Productivity

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 7,428,434,704 | `yfinance` (unchanged) |
| **Market Cap** | 7,428,434,704 × $449.40 = **$3,338.339B** | Computed |
| Total notes debt (current + LT) | $9.2B + $31.1B = **$40.3B** | FY26 Q4 earnings release |
| Cash + ST investments | $20.9B + $55.9B = **$76.8B** | FY26 Q4 earnings release |
| **Net Debt** | $40.3B − $76.8B = **−$36.5B (net cash)** | Computed |
| **EV** | $3,338.339B − $36.5B = **$3,301.839B** | Computed |
| FY2026 Operating Income (EBIT) | $37.961B + $38.275B + $38.398B + $40.566B = **$155.200B** | `yfinance` quarterly (Q1–Q3) + FY26 press release (Q4 + FY total, cross-checked to sum) |
| **EV/EBIT** | $3,301.839B ÷ $155.200B = **21.276×** | Computed |
| FY2026 Operating Cash Flow | **$182.935B** | stockanalysis.com (cross-validated methodology, §3) |
| FY2026 CapEx | **$115.948B** (+79.5% YoY vs. FY25's $64.551B — the AI/datacenter ramp) | stockanalysis.com |
| **FY2026 FCF** | $182.935B − $115.948B = **$66.987B** | Computed |
| **FCF Yield** | $66.987B ÷ $3,338.339B = **2.0067%** | Computed |
| FY2026 Net Income (GAAP) | **$133.7B** | FY26 earnings release |
| One-time OpenAI investment gain (FY26) | **+$4.963B** net income, **+$0.67** diluted EPS | FY26 earnings release (official-IR-sourced figure; see §2 item 3 discrepancy flag) |
| **FY2026 Net Income (normalized, Rule 6)** | $133.7B − $4.963B = **$128.737B** | Computed |
| FY2026 Revenue | $77.673B + $81.273B + $82.886B + $90.0B = **$331.832B** | `yfinance` (Q1–Q3) + press release (Q4/FY total, cross-checked) |
| **Net Margin (normalized)** | $128.737B ÷ $331.832B = **38.79%** | Computed |
| FY2026 D&A | **$38.534B** | stockanalysis.com |
| EBITDA (FY2026) | $155.200B + $38.534B = **$193.734B** | Computed |
| **Net Debt/EBITDA** | −$36.5B ÷ $193.734B = **−0.1884×** (net cash) | Computed |
| FCF/NI conversion (normalized) | $66.987B ÷ $128.737B = **52.04%** | Computed — below 70%, explained (§4 flag 3 below) |
| Forward EPS (NTM) | **$22.72328** | `yfinance` `forwardEps` |
| **Forward PE** | $449.40 ÷ $22.72328 = **19.779×** | Computed |
| 5yr avg PE (anchor) | 31.546× (range 24.169×–38.803×, n=20q) | Re-verified live, one quarter forward (§4 flag 7) |
| TTM EPS (Street-comparable series) | $17.28 (vs. $13.64 a year ago) → **+26.69%** growth | `yfinance` `get_earnings_dates` reconstruction — 3+ years of >15% growth confirms **Fast Grower** (FY2024 +21.8%, FY2025 +15.5%, current +26.69%) |
| PEG | 19.779 ÷ 26.69 = **0.7411** | Computed |
| Effective tax rate (FY2026) | Tax $32.185B ÷ Pretax $165.934B = **19.40%** | `yfinance` (Q1–Q3) + press release (Q4), summed across all 4 quarters |
| Total Stockholders' Equity (6/30/2026) | **$442.387B** | stockanalysis.com (cross-validated — see §3) |
| Gross Margin (FY2026) | $225.483B ÷ $331.832B = **67.95%** | Computed (Q1–Q3 `yfinance` + Q4 press release) |
| Revenue 3yr CAGR (FY2023 → FY2026) | (($331.832B/$211.915B)^(1/3)) − 1 = **16.13%** | `yfinance` annual + press release FY26 total |

---

## 6. MSFT — Quality Score (2026-06-29 methodology, refreshed post-earnings)

**Hard disqualifier check:**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | FY2026 52.04% (normalized) is the **first full fiscal year** below 70% — FY2025 was 70.3% (right at/above the line). Only 1 full year below threshold so far, with a standing, cited growth-capex explanation (FY26 capex +79.5% YoY). | disqualify if <70% for 2+ yrs *without* explanation | ✅ PASS (flagged as a trend to watch — a second consecutive sub-70% year would sharpen this) |
| Net Debt/EBITDA over threshold? | **−0.1884× (net cash)** | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | Yes, every year on record | disqualify if not | ✅ PASS |

No hard disqualifier triggers. Proceeding to the weighted score.

### Profitability (25% weight)
```
Net Margin (normalized) = $128.737B / $331.832B = 38.79%
NetMargin_Component = clamp((38.79/30)×100, 0, 100) = 100.0   (>30% cap)

ROIC:
  NOPAT = EBIT × (1 − effective tax rate) = $155.200B × (1 − 0.1940) = $125.097B
  Invested Capital = Total Debt ($40.3B) + Total Equity ($442.387B) = $482.687B
  ROIC = $125.097B / $482.687B = 25.91%
ROIC_Component = clamp((25.91/30)×100, 0, 100) = 86.38

Profitability_Score = (100.0 + 86.38) / 2 = 93.19
```

### Margins (15% weight)
```
Gross Margin (FY2026) = 67.95%
GrossMargin_Score = clamp((67.95/80)×100, 0, 100) = 84.93
```
No structural-trend bonus (bonus only applies to a below-40%-and-expanding margin). **Trend is now a mild, 2-year compression** (69.76% FY24 → 68.83% FY25 → 67.95% FY26, −1.8pp cumulative) — below the >3pp structural-break sell-trigger threshold, but flagged as a Phase 04 watch item given the scale of the capex ramp compressing near-term profitability.

### Growth (20% weight)
```
Revenue 3yr CAGR (FY2023 $211.915B → FY2026 $331.832B) = 16.13%
Growth_Score = clamp((16.13/25)×100, 0, 100) = 64.52
+ 10 (documented TAM expansion, cited, stronger evidence than 07-05):
  Azure crossed $100B annualized revenue, grew 43% YoY (accelerating vs. the 39–40% guided last
  session); commercial RPO +84% YoY to $678B (forward revenue visibility); FY2027 Q1 guidance
  further accelerates Azure to 45% constant-currency growth. Real, cited, company-disclosed evidence.
Growth_Score (with bonus) = clamp(64.52 + 10, 0, 100) = 74.52
```

### Balance Sheet (15% weight)
```
Net Debt/EBITDA = −0.1884× (net cash)
BalanceSheet_Score = clamp(100×(1 − (−0.1884)/4), 0, 100) = clamp(104.71, 0, 100) = 100.0
```

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Azure crossed $100B annualized revenue this quarter, grew 43% YoY (accelerating) — same basis as 07-05, strengthened by the fresh acceleration data and the guided 45% cc for next quarter. |
| Brand premium | **TRUE** | Microsoft 365 Copilot passed **30 million paid seats** this quarter (a fresh, company-disclosed milestone) at sustained premium pricing (Frontier Suite E7, $99/user/month) — continued adoption at a premium price point, not a price cut to defend volume. |
| Network effect | **TRUE** | LinkedIn two-sided network — unchanged mechanism from every prior session. |
| Switching costs | **TRUE** | Enterprise identity/security/productivity-stack integration (Entra ID, M365 tiers) — unchanged mechanism. |
| Scale cost advantage | **FALSE** | Same gap as every prior session: no MSFT-specific cost-per-unit citation found (only industry-wide hyperscaler PUE data, not MSFT's own disclosed figure against a named smaller competitor). |

```
Moat_Score = (4/5) × 100 = 80.0
```

**⚠️ Same close-call flag as 07-05, margin now even narrower:** if "scale cost advantage" were credited TRUE, Moat_Score = 100.0 and Quality Score below would be **82.9** (passes) instead of **79.9** (fails, by just 0.1 point). No new evidence resolved this ambiguity either way this session.

### FCF Quality (10% weight)
```
FCF/NI (normalized) = $66.987B / $128.737B = 52.04%
FCFQuality_Score = clamp(((0.5204 − 0.40)/0.60)×100, 0, 100) = 20.07
```

### Quality Score — Final
```
Quality Score = (93.19×0.25) + (84.93×0.15) + (74.52×0.20) + (100.0×0.15) + (Moat×0.15) + (20.07×0.10)

  With Moat_Score = 80.0 (primary determination):
  = 23.2975 + 12.7395 + 14.904 + 15.00 + 12.00 + 2.007
  = 79.9480 → rounds to 79.9

  Sensitivity — with Moat_Score = 100.0 (alternate read):
  = 23.2975 + 12.7395 + 14.904 + 15.00 + 15.00 + 2.007
  = 82.9480 → rounds to 82.9
```

# Quality Score = 79.9 (primary determination) — FAILS the 80.0+ gate, by only 0.1 point. Sensitivity: 82.9 (passes) if the one flagged Moat judgment call is read the other way.

This is the **second consecutive MSFT session failing the quality gate on the primary determination** (07-05: 78.3; today: 79.9) — the margin has narrowed materially (1.7pt short → 0.1pt short) on the back of the earnings beat improving Profitability, Growth, and Margins sub-scores, while the ambiguous Moat signal remains unresolved. **Per rescore.md, neither result forces an exit** — quality-gate failure alone is not a valid Phase 06 exit trigger — but this is a **continuing, sharpened Phase 04 Quality Watch escalation** (see §10–11).

---

## 7. MSFT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 19.779 = 5.0558%
Spread = EY − 10Y Treasury = 5.0558% − 4.70% = +0.3558%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.3558%, ~1.14pp short) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.70% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for MSFT = +10** (unchanged bracket, 9th consecutive session)

---

## 8. MSFT — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.0067/10), 0, 100) = 79.933
```
→ Contribution: 79.933 × 0.40 = **31.973**

**EV/EBIT — 25% weight**
```
EV/EBIT_Score = clamp((21.276 − 12)/23 × 100, 0, 100) = 40.33
```
→ Contribution: 40.33 × 0.25 = **10.083**

**Forward PE (fallback formula — 5yr avg only) — 20% weight**
```
Deviation% = (19.779 − 31.546)/31.546 × 100 = −37.30%
FwdPE_Score = clamp(50 + (−37.30)×2.5, 0, 100) = clamp(−43.25, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight (Fast Grower confirmed, §5)**
```
PEG = Forward PE ÷ TTM EPS growth% = 19.779 ÷ 26.69 = 0.7411
PEG_Score = clamp((0.7411 − 0.5)/2.0 × 100, 0, 100) = 12.06
```
→ Contribution: 12.06 × 0.15 = **1.809**

**Raw weighted score:**
```
= 31.973 + 10.083 + 0.0 + 1.809 = 43.865
```
**+ Rate Modifier (+10) = 53.865** (before the Upside/Downside Modifier)

---

## 9. MSFT — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture (bull/base/bear exit multiples 31.0×/27.0×/21.0×) carried forward unchanged** — still spans the fresh 5yr PE range (24.169×–38.803×) sensibly; no fundamental reason found this session to revise the multiples themselves (the *inputs* — forward EPS, live price — are what moved).

NTM EPS = $22.72328 (`yfinance` `forwardEps`, cross-checked: Live Price ÷ Forward PE = $449.40/19.779 = $22.72 — consistent)

| Scenario | Weight | PE applied | Rationale | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 31.0× | Azure/AI monetization re-accelerates further (guided 45% cc next quarter); multiple re-rates near the 5yr average (31.55×). Below the $555–870 analyst range. | $22.72328 × 31.0 = **$704.42** |
| **Base** | 50% | 27.0× | Consensus continued double-digit EPS growth but a haircut multiple vs. the 31.55× 5yr average for the litigation overhang, gaming-segment restructuring costs, and continued heavy capex/margin pressure. | $22.72328 × 27.0 = **$613.53** |
| **Bear** | 25% | 21.0× | Azure/AI capex spend disappoints relative to the huge RPO backlog, or margin compression from capex accelerates; multiple de-rates toward the low end of the 5yr band (24.17×). | $22.72328 × 21.0 = **$477.19** |

```
PW Fair Value = 0.25×704.42 + 0.50×613.53 + 0.25×477.19 = $602.17
```
**⚠️ Flag: PW Fair Value ($602.17) now sits *above* the $555.77 analyst consensus mean** — a reversal from every prior session (where PW FV sat below consensus). Driven by forward EPS jumping ~17% (from $19.37 to $22.72) on the earnings beat while the consensus PT itself likely hasn't been fully updated yet (§1 flag — analyst targets typically lag a beat this size by days). Still within the analyst range ($400–$870) and below the $870 high. Flagged transparently per "no black box," not adjusted to force a fit.

**Step 1 — Expected annual return E.**
```
Gap Upside %     = (602.17 ÷ 449.40) − 1                = +33.99%
Catalyst window  = 2 years (unchanged — FY27 Q1 earnings confirmed ~28 Oct 2026 +
                   continued Azure/AI reacceleration cycle; within Rule 10's 18–24mo window)
Annualized gap   = 33.99% ÷ 2                            = +16.995%
Intrinsic growth = +14%/yr   (raised 1pp from the 13% carried since 06-20, given the fresh,
                   company-disclosed acceleration evidence — Azure 43% actual vs. 39–40% prior
                   guidance, RPO +84% to $678B, FY27 Q1 Azure guided to 45% cc — still
                   deliberately below the 26.69% headline EPS growth or 18% revenue growth)
Shareholder yield = +1.4408%  (bottom-up: dividends $25.856B + buybacks $22.238B, both
                   trailing-4-quarters-through-Q3FY26 per the §4 flag 3 data lag,
                   ÷ market cap $3,338.339B)

E = 16.995% + 14% + 1.4408% = +32.44%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 32.44% ≥ H → M = −15 × clamp((32.44 − 10)/15, 0, 1) = −15 × clamp(1.496, 0, 1) = −15 × 1 = −15.0
```
**Modifier M = −15.0** (the maximum attractive bound — 9th consecutive session at this floor).

**Guardrail checks:**
1. **Catalyst:** documented (FY27 Q1 earnings ~28 Oct 2026 + continued Azure/AI reacceleration) → upside credit allowed. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($602.17) below the $870 analyst high; bear case underwritten near the low end of the historical PE range. ✓ (though flagged above vs. the *mean* consensus target)
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** at the −15 floor. ✓

---

## 10. MSFT — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (43.865) + Rate Modifier (+10) + Upside/Downside (−15.0)
                       = 38.865
```
Boundary rule: not a ".X5" case → standard rounding → **Final Valuation Score = 38.9**

| | Value |
|---|---|
| Raw weighted | 43.865 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −15.0 (E = +32.44%) |
| **FINAL VALUATION SCORE** | **38.9** |
| Prior valuation score | 35.5 (07-05) |
| **Quality Score** | **79.9 (FAILS 80.0+ gate — primary determination, by 0.1pt; 82.9 sensitivity, see §6)** |

**Composite Score: NOT computed** — MSFT's primary-determination Quality Score (79.9) fails the 80.0+ gate, same as 07-05.

*Reference only (not the operative Composite Score):*
```
If Quality = 79.9 (primary):  Composite = 0.50×(100−79.9) + 0.50×38.9 = 10.05 + 19.45 = 29.5
If Quality = 82.9 (alt/pass): Composite = 0.50×(100−82.9) + 0.50×38.9 =  8.55 + 19.45 = 28.0
```
Both reference numbers still land in the 0.0–29.9 "Very Cheap" band. **Not used to drive the action recommendation below.**

**Action recommendation basis:** as in 07-05, falls back to the **raw Valuation Score (38.9)** against the Action Table.

---

## 11. MSFT — Action Recommendation & Position Cap Check

**Raw Valuation Score 38.9 → nominally BUY — Standard position 3–5% (30.0–49.9 band)** — same band as 07-05's 35.5.

**THREE independent gates still block adding capital:**

1. **⚠️ Position cap (Upgrade 7) — status uncertain, flagged rather than assumed.** Last documented weight is **14.62%** (26 Jul 2026 sync — *before* today's earnings pop). Today's +15.1% one-day move almost certainly pushed MSFT's actual current weight materially higher than 14.62% — quite possibly back at or over the 15% hard cap, though this session does not recompute portfolio weights (that's `/sync-portfolio`'s job). **Recommend an immediate `/sync-portfolio` (or at minimum `/sync-positions`) run to get the actual current weight before any capital-allocation decision is made.**
2. **🚫 Risk/Reward ratio.** See §12 — both the formal-entry and live-price R/R checks fail the 2:1 minimum (1.33:1 and 1.38:1 respectively) — this remains the binding, unambiguous block regardless of the position-cap uncertainty above.
3. **🚫 Quality Score gate (primary determination), now an even closer call.** Quality Score 79.9 fails the 80.0+ bar by only 0.1 point (vs. 1.7 points short on 07-05) — the second consecutive session failing on the primary determination, though the gap has narrowed sharply on the back of the earnings beat. Still does not force an exit (quality-gate failure alone is not a valid Phase 06 exit trigger), and this is a large, pre-existing holding, not a new candidate — same Phase 04 Quality Watch treatment as 07-05, now with added urgency given how close the result is to flipping.

**Net: no fresh capital added.** The binding constraint has shifted somewhat — R/R is now the clearest, most unambiguous block (both gate checks) — but the practical conclusion is unchanged from 07-05: do not add, and the standing compliance trim from the 2026-06-15 rebalance remains overdue, now with a possibly-worse cap breach given today's price move. The open question of whether to log MSFT as a **Human Override** in [override-log.md](../portfolio/override-log.md) (per the ZS precedent, given the repeated quality-gate fail) remains flagged, not resolved, by this session.

---

## 12. Order Setup (shown for completeness — nominal BUY band — both gates below still block it)

```
Blended Fair Value (= PW FV):        $602.17
Margin of Safety (raw score 30–49.9 band): 25%   (lower end; wide-moat rationale — still contested
                                                   given §6's persistent, narrow quality-gate fail)
BUY PRICE (limit):                   $602.17 × (1 − 0.25) = $451.63
  → Live price $449.40 is now BELOW the formal buy price (−0.49%) — for the first time in
    several sessions, the live price technically clears the entry-trigger threshold on price
    alone. Does NOT change the outcome — R/R still fails below.
PRIMARY SELL TARGET (blended FV):    $602.17
BULL-CASE TRIM TARGET (bull × 0.90): $704.42 × 0.90 = $633.98
STOP LOSS (Buy × (1 − 25%)):         $451.63 × 0.75 = $338.72
R/R at formal entry = (602.17 − 451.63) ÷ (451.63 − 338.72) = 150.54 ÷ 112.91 = 1.333:1
R/R at live price   = (602.17 − 449.40) ÷ (449.40 − 338.72) = 152.77 ÷ 110.68 = 1.380:1
```

**⚠️ Both R/R checks still fail the 2:1 minimum (Rule 6).** Slightly improved vs. 07-05 (1.33:1/1.21:1) at the live-price check specifically, but still well short of 2:1. **Per Rule 6, R/R below 2:1 = do not enter, independent of the score band, the position cap, or the Quality Score question.**

---

## 13. Portfolio / Compliance Note (independent of valuation score)

MSFT's last documented weight (14.62%, 26 Jul 2026 sync) is now **stale by a material amount** given today's +15.1% price move — the actual current weight is unknown without a fresh sync, but is very likely higher and could be back over the 15% cap. This is the **9th consecutive session** flagging a position-cap concern for MSFT (06-07, 06-11 backfill, 06-12, 06-20, 06-23, 06-26, 07-05, and now 07-30 — with the added wrinkle that today's move may have made the breach worse, not better). Recommend prioritizing both a fresh `/sync-portfolio` run and the standing [2026-06-15 rebalance](../../../sessions/2026-06-15-rebalance.md) compliance trim.

---

## 14. Next Review Trigger

- **Routine:** MSFT FY2027 Q1 earnings, expected late Oct 2026 (per the FY27 Q1 guidance issued this quarter) — will refresh every fundamental used here on a genuinely fresh quarter (no more statement-lag workaround needed once `yfinance` catches up).
- **🚨 Open item (elevated priority): confirm current portfolio weight via `/sync-portfolio`.** Today's price move makes the last-documented 14.62% figure unreliable for the position-cap check — this is now the most time-sensitive open item.
- **🚨 Open item (unresolved, 2 sessions running): resolve the Quality Score gate question (§6).** The gap has narrowed to 0.1 point — either (a) obtain a harder, MSFT-specific cost-per-unit citation for the "scale cost advantage" moat signal, or (b) accept the primary 79.9 determination and decide how to treat a large held position sitting this close to the framework's own 80.0+ quality gate — log as a Human Override (per the ZS precedent) or continue as a Phase 04 monitoring item.
- **Open compliance item (9th flag): dedicated `/rebalance` execution of the position-cap trim** — still not executed, now potentially more urgent given today's move.
- **Open methodology item:** Owner Earnings (Upgrade 1) decision for non-disclosing mega-caps — 8th consecutive session.
- **Monitoring items (not Rule 9 triggers):** (1) the securities class action, case No. 26-cv-02071 (lead-plaintiff deadline 11 Aug 2026); (2) the now-confirmed workforce reduction (4,800–6,400 roles, Xbox −3,200 through FY2027) for any further quantification of financial impact; (3) the gross-margin compression trend (§4 flag 8) — watch for it approaching the >3pp structural-break sell trigger; (4) the analyst-consensus-vs-PW-FV flag (§9) — watch for target-price revisions in the days following this earnings beat.
- **Watch:** if analyst targets and/or the scenario multiples get revised upward following this beat, the PW Fair Value (and thus the Upside/Downside Modifier) could shift further; re-derive at the next earnings print regardless.

---

## Glossary

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchases, net of new issuance. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; not adopted for MSFT this session. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **Effective tax rate** | Tax provision ÷ pretax income for a given period — used to compute NOPAT for the ROIC calculation. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Gross Margin** | Gross Profit ÷ Revenue. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; flagged (not adopted) for MSFT this session pending user decision. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator of ROIC. |
| **IRR** | Internal Rate of Return. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means a net-cash position. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. MSFT: 79.9 (fails the gate by 0.1pt), sensitivity 82.9. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **RPO (Remaining Performance Obligations)** | Contracted future revenue not yet recognized — a forward-looking backlog metric; MSFT's commercial RPO grew 84% YoY to $678B this quarter. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; require a minimum 2:1 risk/reward before entering; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |
