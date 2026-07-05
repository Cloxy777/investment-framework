# RESCORE — SPOT (Spotify Technology S.A.) — 2026-07-05

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 5 Jul 2026
**10Y US Treasury Yield:** 4.49% (TradingEconomics/CNBC, 2026-07-02 close — most recent print available; US Treasury market observed the July 4th holiday on Fri 3 Jul, then the weekend, so 2 Jul is the latest available yield — same figure already established across this batch's 2026-07-05 sessions, e.g. NVO)
**Rate Regime Modifier in effect:** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** SPOT **80.5** (2026-06-20, TRIM to 50% — [sessions/2026-06-20-rescore-spot.md](2026-06-20-rescore-spot.md)). Quality Score / Composite Score had never been computed for SPOT — flagged stale per [watchlist/STALE.md](../watchlist/STALE.md) 2026-06-29 methodology table. SPOT was previously flagged as one of the four "richly-valued names" (AMZN, GOOG, CSGP, SPOT) that stayed in the trim band even after the Upside/Downside Modifier ([holdings.md](../portfolio/holdings.md) 2026-06-20 note).
**First-ever Quality Score / Composite Score computation for SPOT this session.**

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EBITDA = operating profit before D&A; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; D&A = depreciation & amortization; capex = capital expenditure; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ forward PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; TAM = total addressable market; TTM = trailing twelve months; NI = net income; CER = constant exchange rate; MAU = monthly active users.*

---

## 1. Live Price (Rule 0) — data-quality flag

IBKR returned **three internally inconsistent price fields** for SPOT this session:

| Field | Value | Note |
|---|---|---|
| `get_price_snapshot` → `last` | $472.48 (`is_close: true`) | Stale — matches Wednesday 1 Jul close, one trading day behind |
| `get_price_snapshot` → `plprice` (mark price) | $489.86 | Broker mark; also matches `get_account_positions`' live `market_price` for the SPOT position |
| `get_price_history` (ONE_DAY bars, most recent close) | **$485.97** (Thursday 2 Jul 2026) | Most recent actual trading-day close — markets were closed Fri 3 Jul (Independence Day, observed) and the weekend (4–5 Jul), so 2 Jul is the last real trading day |

**Resolved via independent cross-check (Rule 0 diligence, same method used in the 2026-07-04 CSGP session):** stockanalysis.com's SPOT page (dated 2026-07-03) shows Market Cap $99.93B ÷ Shares Outstanding 205.62M = **$486.03/share** — this ties out almost exactly to the `get_price_history` close ($485.97), not to either IBKR field. **$485.97 used throughout this session**, sourced from `get_price_history`'s most recent close and independently corroborated — consistent with the task brief's explicit instruction to cross-check a stale-looking snapshot against price history.

| Item | Value | Source |
|---|---|---|
| **Live price (used)** | **$485.97** | IBKR `get_price_history` (contract_id 312496724, NYSE), close of 2026-07-02, cross-checked against stockanalysis.com implied price ($486.03) |
| 52-week range | **$405.00 – $748.00** | IBKR `misc_statistics` |
| Year-to-date change | **−18.64%** (−$108.23) | IBKR `year_to_date_change` |
| Analyst consensus PT | **$599.07** (40 analysts, S&P Global via stockanalysis.com, "Buy") | Bull-case sanity anchor only, never a score input |
| Prior session price (20 Jun 2026) | $468.08 | +3.82% since last review — nowhere near the 15% Rule 9 threshold |

---

## 2. Rule 9 Trigger Check (2026-06-20 → 2026-07-05)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Next report: Q2 FY2026, expected ~28–29 Jul 2026 (based on Q1 2026's 28 Apr report date and Q2 2025's 29 Jul report date pattern) |
| Guidance revision | No | No new guidance since Q1 2026 (28 Apr 2026) |
| M&A | No | None found |
| Management change | No | None found |
| Macro shift | No | 10Y ticked 4.45%→4.49%, still inside "3.5–5%" bracket |
| >15% unexplained price move | No | +3.82% over 2 weeks |

**Conclusion: no Rule 9 trigger fired.** This is a routine, schedule-free re-score whose real substance is the first-ever Quality Score computation for SPOT.

---

## 3. SPOT — Data Collected

**Sector:** Communication Services — Audio Streaming & Podcasting. Treated as Technology/Growth for fair-value method per Rule 1.
**Current portfolio weight:** 0.84% (1 share, IBKR only) — per [holdings.md](../portfolio/holdings.md).

`yfinance` is unreachable this session (`curl_cffi` TLS SSL error, the same persistent failure documented across recent sessions — e.g. AMZN 2026-07-04). **All figures below sourced directly from Spotify's own SEC 6-K filings (Exhibit 99.1 quarterly shareholder updates) via SEC EDGAR, not yfinance.**

### Quarterly income statement, EUR millions (SEC 6-K Exhibit 99.1, each quarter's own filing)

| Quarter | Revenue | Gross Profit | GM% | Operating Income (EBIT) | Net Income | Pretax Income | Tax (benefit)/expense |
|---|---|---|---|---|---|---|---|
| Q2 2025 | 4,193 | 1,320 | 31.5% | 406 | **(86)** | 48 | 134 |
| Q3 2025 | 4,272 | 1,351 | 31.6% | 582 | 899 | 827 | (72) |
| Q4 2025 | 4,531 | 1,499 | 33.1% | 701 | 1,174 | 1,021 | (153) |
| Q1 2026 | 4,533 | 1,495 | 33.0% | 715 | 721 | 937 | 216 |
| **TTM (to 31 Mar 2026)** | **17,529** | **5,665** | **32.32%** | **2,404** | **2,708** | **2,833** | **125** |

Sources: [Q2 2025 6-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1639920/000114036125027654/ef20052398_ex99-1.htm), [Q3 2025 6-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1639920/000114036125040271/ef20057592_ex99-1.htm), [Q4 2025 6-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1639920/000114036126004482/ef20065075_ex99-1.htm), [Q1 2026 6-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1639920/000114036126017211/ef20071303_ex99-1.htm).

### Full-year annual figures (EUR millions, for 3yr CAGR / gross-margin-trend evidence)

| FY | Revenue | Gross Profit | GM% | Operating Income | Net Income | Pretax Income | Tax |
|---|---|---|---|---|---|---|---|
| 2022 | 11,727 | 2,926 | 24.95% | (659) | (430) | (370) | 60 |
| 2023 | 13,247 | 3,397 | 25.66% | (446) | (532) | (505) | 27 |
| 2024 | 15,673 | 4,724 | 30.14% | 1,365 | 1,138 | 1,341 | 203 |
| 2025 | 17,186 | 5,496 | 31.99% | 2,198 | 2,212 | 2,224 | 12 |

Sources: [Q4 2022 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036123003467/brhc10047269_ex99-1.htm), [Q4 2023 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036124005769/ef20020473_ex99-1.htm), [Q4 2024 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036125002936/ef20042791_ex99-1.htm), [Q4 2025 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036126004482/ef20065075_ex99-1.htm).

### Cash flow (EUR millions, TTM to 31 Mar 2026 — directly disclosed LTM line, Q1 2026 6-K)

| Item | TTM value | Source |
|---|---|---|
| Net cash from operating activities | 3,230 | Q1 2026 6-K LTM table |
| Capital expenditures | (68) | Q1 2026 6-K LTM table |
| **Free Cash Flow (non-IFRS, company-defined)** | **3,164** | Q1 2026 6-K LTM table (ties out exactly to the sum of the four quarters above: 700+806+834+824) |
| D&A (Depreciation of PP&E + lease ROU + intangible amortization), TTM | 101 | Sum of quarterly cash-flow-statement add-backs (Q2'25 26, Q3'25 24, Q4'25 25, Q1'26 26) |

### Balance sheet, as of 31 Mar 2026 (EUR millions)

| Item | Value | Source |
|---|---|---|
| Cash and cash equivalents | 5,255 | Q1 2026 6-K balance sheet |
| Short-term investments | 3,491 | Q1 2026 6-K balance sheet |
| Long-term investments (excluded from net-debt calc — not cash-like, largely equity stakes) | 1,194 | Q1 2026 6-K balance sheet |
| Lease liabilities (non-current) | 414 | Q1 2026 6-K balance sheet |
| Exchangeable Notes | **0** — fully retired in Q1 2026 (was €1,458M at 31 Dec 2025) | Q1 2026 6-K — "retired €1.3 billion of exchangeable notes" |
| Total equity (attributable to owners) | 8,010 | Q1 2026 6-K balance sheet |
| **Total debt (used)** | **414** (lease liabilities only) | Computed |
| **Net debt (used)** | **−8,332** (net cash of €8,332M) | 414 − 5,255 − 3,491 |

### Other collected inputs

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 205.62M | stockanalysis.com, dated 2026-07-03 (cross-checked: 205.62M × $485.97 = $99.93B, matches the site's displayed market cap) |
| FY2026 consensus EPS | $12.79 (40 analysts) | stockanalysis.com/stocks/spot/forecast, dated 2026-07-03 |
| Live EUR/USD FX rate | **1.1436323** | IBKR `get_account_balances` (broker-reported live rate, per Rule 0 — never assumed) |
| Global music-streaming subscriber market share | **31.7%** (#1, >2× #2 Tencent Music's 14.4%) | MIDiA Research 2025 Music Subscriber Market Shares report |
| Premium price increases | Aug 2025 (EU/LatAm/APAC/MEA, €10.99→€11.99); Feb 2026 (US, $11.99→$12.99 — 2nd US hike in 7 months) | Music Business Worldwide, TechCrunch |
| Subscriber growth through price hikes | Premium subscribers +9–12% YoY every quarter through the hike cycle (no churn uptick disclosed) | Company 6-K filings (§3 above) |
| MAU acceleration | 761M Q1 2026, +12% YoY — "accelerating to 12% Y/Y growth" (up from ~11% in prior quarters) | Q1 2026 6-K Ex-99.1 |

---

## 4. Data Gaps, Corrections & Flags

1. **Live price — three-way IBKR discrepancy, resolved (§1).** Used $485.97 (price-history close), cross-checked against an independent vendor, per the task's explicit stale-snapshot-handling instruction.
2. **Deferred tax valuation allowance release — one-off, normalized out (Rule 6).** Spotify's Q4 2025 tax line shows a **€153M tax benefit** (not expense) despite €1,021M of pretax income — confirmed via [Complete Music Update's coverage](https://completemusicupdate.com/spotify-made-17-billion-last-year-with-profits-of-2-billion-and-paid-just-12-million-in-tax/) of the same earnings release: "Rather than paying tax in Q4, the company received a net tax credit of €153 million... stem[ming] from Spotify recognising a large pool of tax credits built up from years of historical losses." FY2025's overall effective tax rate was **0.5%** (€12M tax on €2,224M pretax income) — clearly not sustainable. Q3 2025 shows a smaller version of the same effect (€72M benefit). **Normalization:** TTM pretax income (§3, €2,833M) is re-taxed at **FY2024's 15.14% effective rate** (203/1,341 — the last full fiscal year before this release pattern began) rather than the actual, DTA-release-distorted TTM rate, giving **normalized TTM Net Income ≈ €2,404.15M** (vs. €2,708M GAAP) — used for the Quality Score's Profitability sub-score (§5) and for NOPAT (also using the 15.14% rate on EBIT directly). This is the same treatment this repo has applied to AMD's uncertain-tax-position release and DUOL's deferred-tax release (see [glossary.md](../framework/glossary.md)) — flagged as an estimate based on the nearest clean full-year rate, not invented from nothing.
3. **Forward PE — no usable 5-year history, unchanged rationale from 06-20.** SPOT has only 2 clean profitable fiscal years (FY2024, FY2025) and even the most recent 8 quarters include a net-loss quarter (Q2 2025, −€86M) — nowhere near the 20 consecutive quarters of positive TTM EPS a 5yr PE range/average requires. **No-history fallback applies: `FwdPE_Score = 50.0`, flagged** (same conclusion as 2026-06-20, independently re-verified this session with the fresh Q2 2025 loss-quarter data point).
4. **Owner Earnings (Upgrade 1) does not apply.** SPOT is not one of the four named businesses (MSFT/GOOGL/META/AMZN), and its capex is immaterial in any case — TTM capex is €68M against €3,230M of TTM operating cash flow (~2.1%), so Owner Earnings and reported FCF would not differ materially regardless of the growth/maintenance split. Raw FCF used.
5. **Forward PE's own inconsistency vs. stockanalysis.com's displayed figure.** Computing Forward PE directly (Rule 0 live price ÷ FY2026 consensus EPS) gives $485.97 ÷ $12.79 = **38.00×**, materially above the site's own displayed "Forward PE" of 32.96 — likely because vendor-displayed forward PE commonly uses a blended NTM (next-twelve-months) EPS estimate rather than a strict calendar-FY2026 figure, and/or a different live-price snapshot. This session uses the explicit Rule-0-compliant 38.00× calculation (shown in full in §6) for full auditability rather than the vendor's opaque headline number; flagged for transparency, doesn't change the outcome since Forward PE is on the no-history fallback (50.0 neutral) regardless.
6. **Total debt figure (€414M) is non-current lease liabilities only.** The balance sheet doesn't separately break out a current-lease-liabilities line (likely folded into "Accrued expenses and other liabilities," current); Exchangeable Notes are fully retired (§3). Immaterial to the Net Debt/EBITDA conclusion given the enormous net-cash cushion (net debt/EBITDA ≈ −3.3×).

---

## 5. SPOT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = Live Price ÷ FY2026 consensus EPS = $485.97 ÷ $12.79 = 38.0008×
EY         = 1 ÷ 38.0008 = 2.6315%
Spread     = EY − 10Y Treasury = 2.6315% − 4.49% = −1.8585%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−1.86pp short) → **+5 additive.**

**Step 2 — Rate Regime Modifier**
10Y = 4.49% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +10.**

---

## 6. SPOT — Quality Score (first-ever computation, 2026-06-29 methodology)

```
Profitability (25%):
  Net Margin (normalized, ex-DTA-release — §4.2) = €2,404.15M ÷ €17,529M (TTM revenue) = 13.721%
  ROIC: NOPAT = TTM EBIT × (1 − FY2024 clean eff. tax rate) = €2,404M × (1 − 0.15138) = €2,039.56M
    Invested Capital = Total Debt (€414M) + Total Equity (€8,010M) = €8,424M
    ROIC = €2,039.56M / €8,424M = 24.222%
  NetMargin_Component = clamp((13.721/30)×100, 0, 100) = 45.74
  ROIC_Component       = clamp((24.222/30)×100, 0, 100) = 80.74
  Profitability_Score  = (45.74 + 80.74) / 2 = 63.24   (no FCF cap — FCF-positive every year since
    FY2019 at least, TTM €3,164M strongly positive)

Margins (15%): TTM Gross Margin = €5,665M / €17,529M = 32.32%
  GrossMargin_Score = clamp((32.32/80)×100, 0, 100) = 40.40
  + 10 (documented structural 3yr+ trend: FY2022 24.95% → FY2023 25.66% → FY2024 30.14% →
    FY2025 31.99% → TTM 32.32%, all SEC-filed GAAP figures — genuine multi-year structural
    expansion via price increases + audiobook-bundling economics + podcast-cost discipline,
    not a single-quarter blip; still below the 40% raw threshold so the trend bonus applies
    per quality-scoring.md)
  Margins_Score (with bonus) = 50.40

Growth (20%): Revenue 3yr CAGR, FY2022 €11,727M → FY2025 €17,186M (both SEC-filed annual figures)
  CAGR = (17,186/11,727)^(1/3) − 1 = 13.56%
  Growth_Score = clamp((13.56/25)×100, 0, 100) = 54.26
  + 10 (documented TAM expansion / pricing-power evidence, no structural-deceleration penalty
    applied): MAU accelerating to +12% Y/Y (761M, Q1 2026, up from ~11% prior quarters) and two
    successful Premium price hikes since Aug 2025 with subscriber growth *continuing* through
    them (+9-12% Y/Y every quarter, no churn uptick disclosed) — genuine pricing-power evidence.
    Reported revenue growth *has* decelerated on a headline basis (FY2024 +18.3% → FY2025 +9.65%
    → Q1 2026 +8% Y/Y), but Spotify's own Q1 2026 filing attributes ~600bps of that Q1 2026 gap to
    FX ("14% Y/Y constant currency" vs. 8% reported) — a currency effect, not a fundamental
    slowdown, so no offsetting −10 structural-deceleration penalty is applied.
  Growth_Score (with bonus) = 64.26

Balance Sheet (15%): Net Debt = €414M − (€5,255M + €3,491M) = −€8,332M (net cash)
  EBITDA = EBIT (€2,404M) + D&A (€101M TTM) = €2,505M
  Net Debt/EBITDA = −8,332/2,505 = −3.327× (net cash)
  BalanceSheet_Score = clamp(100×(1−(−3.327)/4), 0, 100) = clamp(183.2, 0, 100) = 100.0

Moat Signal (15%) — checklist, cited evidence:
  ✓ Market share stable/growing — TRUE. MIDiA Research's 2025 Music Subscriber Market Shares
     report puts Spotify at 31.7% of the global music-streaming subscriber market, more than
     double #2 Tencent Music (14.4%) — the clear #1, with Premium subscribers still growing
     9-12% Y/Y every quarter (§3), consistent with a stable-to-growing, not eroding, position.
  ✓ Brand premium — TRUE. Two Premium price increases since Aug 2025 (EU/LatAm/APAC/MEA
     €10.99→€11.99; US $11.99→$12.99, Feb 2026, the second US hike in 7 months) with subscriber
     growth continuing at 9-12% Y/Y through both — documented pricing power without volume loss
     (Music Business Worldwide, TechCrunch).
  ✓ Network effect — TRUE. Documented two-sided-marketplace mechanism: more listeners attract
     more artists/podcasters/audiobook publishers to the platform, and vice versa, while the
     recommendation/personalization engine improves with more aggregate listening data — a
     data-network-effect mechanism (Harvard Digital Innovation & Transformation case writeup on
     Spotify's platform business model).
  ✓ Switching costs — TRUE. Documented mechanism: playlists, follows, saved libraries, and years
     of algorithmic-taste training create real migration friction (a new platform can't replicate
     a user's trained recommendation history), reinforced by social/collaborative features (Jam,
     shared playlists) that embed the product in group behavior.
  ✗ Scale cost advantage — FALSE. No cited cost-per-unit data shows Spotify has a genuine
     unit-economics advantage over smaller streaming competitors. To the contrary: content
     licensing (the largest cost line, ~70% of revenue) is set by a highly concentrated
     rights-holder market (Universal/Sony/Warner ≈ 70-75% of global recorded-music market share)
     and does **not** improve with Spotify's scale — cited analysis (FourWeekMBA) explicitly frames
     this as a "scale paradox": gross margin (32%) remains structurally capped well below
     software-platform peers (70-80%) regardless of subscriber count, because label bargaining
     power, not Spotify's own scale, sets the largest cost line. Margin expansion achieved to
     date (§6 Margins) is attributed to price increases and mix (audiobooks/podcasts), not a
     scale-driven unit-cost edge — this signal does not clear the "cited cost-per-unit gap" bar.
  Moat_Score = (4/5) × 100 = 80.0

FCF Quality (10%): TTM FCF/NI (GAAP, unnormalized — this sub-score is the earnings-quality check
  itself, so it intentionally uses reported, not normalized, NI) = €3,164M / €2,708M = 116.84%
  FCFQuality_Score = clamp(((1.1684 − 0.40)/0.60)×100, 0, 100) = clamp(128.1, 0, 100) = 100.0
  FY2024 FCF/NI = 2,285/1,138 = 200.9%; FY2025 FCF/NI = 2,874/2,212 = 129.9% — both far above 70%,
  no hard-disqualifier concern.

Quality Score = 63.24×0.25 + 50.40×0.15 + 64.26×0.20 + 100.0×0.15 + 80.0×0.15 + 100.0×0.10
              = 15.81 + 7.56 + 12.852 + 15.0 + 12.0 + 10.0
              = 73.222 → rounds to 73.2
```

**Quality Score = 73.2 — FAILS the 80.0+ gate.**

**Hard disqualifier check:** none fire. FCF/NI comfortably clears 70% in every year checked; Net Debt/EBITDA is a deep net-cash position, nowhere near either threshold; FCF-positive every year on record including TTM.

**Why the failure is real, not an artifact:** unlike the price-field discrepancy (§1, a data-quality resolution), this Quality Score genuinely reflects a business whose Profitability (63.24) and Margins (50.40, even after the structural-trend bonus) sub-scores are held back by a still-recovering net margin (13.7%, normalized) and a gross margin (32.3%) that — per the Moat Signal finding above — is structurally capped by rights-holder economics rather than being on a clear path to software-platform-like levels. Growth (64.26) is solid but not exceptional on the framework's 25%-CAGR scale. This is **SPOT's first-ever computed Quality Score**, so there's no "drift" to speak of yet, but it establishes a new baseline finding worth surfacing as a **Phase 04 Quality Watch escalation** per rescore.md step 3 — a held position whose quality, now measured for the first time under this engine, sits meaningfully below the strict 80.0 bar despite genuinely strong moat and balance-sheet characteristics.

---

## 7. SPOT — Phase 02 Valuation Score

**FCF Yield — 40% weight** (Owner Earnings not applicable — §4.4; raw FCF used)
```
TTM FCF (EUR) = €3,164M → USD at live EUR/USD 1.1436323 = $3,618.21M
Market Cap = $485.97 × 205.62M shares = $99,925.15M
FCF Yield = $3,618.21M / $99,925.15M = 3.622%
FCF_Score = clamp(100 × (1 − 3.622/10), 0, 100) = 63.78
```
→ Contribution: 63.78 × 0.40 = **25.512**

**EV/EBIT — 40% weight** (PEG not applicable, see below → 15% redistributed here)
```
Net Debt (EUR −€8,332M) → USD = −$9,528.98M (net cash)
EV = Market Cap $99,925.15M + Net Debt (−$9,528.98M) = $90,396.17M
TTM EBIT (EUR €2,404M) → USD = $2,749.37M
EV/EBIT = $90,396.17M / $2,749.37M = 32.87×
EV/EBIT_Score = clamp((32.87 − 12)/23 × 100, 0, 100) = 90.74
```
→ Contribution: 90.74 × 0.40 = **36.296**

**Forward PE — 20% weight**
No usable 5yr history (§4.3 — only 2 clean profitable years, and even the trailing 8 quarters include a loss quarter).
```
FwdPE_Score = 50.0 (neutral fallback, flagged — unchanged rationale from 06-20, independently re-verified)
```
→ Contribution: 50.0 × 0.20 = **10.0**

**PEG — Fast-Grower test: FAILS.** EPS trajectory: FY2022/FY2023 net losses → FY2024 +€1,138M → FY2025 +€2,212M is a recovery off losses, not 3+ years of clean >15%/yr growth on a non-distorted base (only 2 clean profitable years exist, and one of the trailing 4 quarters — Q2 2025 — was itself a net loss). **PEG's 15% weight redistributed to EV/EBIT** (used above). No trailing PEG figure available from stockanalysis.com this session to record as a sensitivity check (page did not display one) — not invented.

**Raw weighted score:**
```
= 25.512 + 36.296 + 10.0 = 71.808
```
**+ Rate Modifier (+10) = 81.808** *(before the Upside/Downside Modifier)*

---

## 8. SPOT — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario fair value (Rule 7, EV/EBIT-multiple method on forward EBIT).** Fresh scenario build this session (not carried forward), reflecting the updated TTM EBIT base (€2,404M) and the fresh margin/growth evidence in §6:

| Scenario | Wt | Forward EBIT (EUR) | Exit EV/EBIT | Equity Value (EUR) = EBIT×Mult + Net Cash | FV/share (USD, ÷205.62M sh, ×1.1436323 FX) |
|---|---|---|---|---|---|
| Bull | 25% | €2,404M × 1.35 = €3,245.4M | 30.0× | €97,362M + €8,332M = €105,694M | **$587.90** |
| Base | 50% | €2,404M × 1.22 = €2,932.9M | 24.0× | €70,389.6M + €8,332M = €78,721.6M | **$438.13** |
| Bear | 25% | €2,404M × 1.05 = €2,524.2M | 16.0× | €40,387.2M + €8,332M = €48,719.2M | **$271.14** |

Assumptions: Bull = continued margin re-rating + durable Premium pricing power ("ubiquity strategy") + audiobook/video mix shift sustaining a re-rated multiple; Base = steady-state margin expansion + subscriber growth continuing at the current pace; Bear = label-renegotiation margin squeeze (consistent with the Moat Signal "scale cost advantage" finding above — the labels' bargaining power is a real risk to further margin expansion) combined with growth deceleration back toward mid-single digits.

```
PW Fair Value = 0.25×587.90 + 0.50×438.13 + 0.25×271.14 = $433.83
```

**Sanity check (Rule 4/0):** Bull case ($587.90) sits below the $599.07 analyst consensus PT — consistent with Rule 7's guardrail (never use the rosy point as the scored input; this framework's bull case should not exceed the street's own central tendency).

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($433.83 ÷ $485.97) − 1                = −10.727%   (price sits ABOVE PW FV)
Catalyst window = 2 years (default — no single hard re-rating catalyst within 18–24mo identified;
                   the margin-expansion/pricing-power story is a multi-year one)
Annualized gap  = −10.727% ÷ 2                            = −5.364%/yr
Intrinsic growth = +10%/yr (in line with the 3yr revenue CAGR of 13.56%, moderated for margin
                   normalization risk flagged in the Bear scenario / Moat Signal finding)
Shareholder yield = +0.5%/yr (no dividend; modest net buyback — diluted weighted-average shares
                   fell from 210.24M (Q1 2025) to 209.28M (Q1 2026), a −0.46% Y/Y reduction, net
                   of stock-comp issuance and the Q1 2026 €306M repurchase — a real but small
                   net buyback yield, not the 0% "fully offset by dilution" case seen elsewhere
                   in this repo)
```
```
E (expected annual return) = −5.364 + 10.0 + 0.5 = +5.136%/yr
```

**Step 3 — Catalyst/timeline guardrail.** No hard catalyst within 18–24 months identified — the guardrail caps the *upside* (negative M) side at −5 if claiming large upside with no path to realize it. Not binding here: E landed on the positive-modifier (thin-return) side of the mapping, not the large-upside-claim side.

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
0 ≤ E < H → M = +5 × (H − E)/H = +5 × (10 − 5.136)/10 = +5 × 0.4864 = +2.432
```

**Interpretation:** price now sits modestly *above* this framework's own probability-weighted fair value (a reversal in sign from 06-20's +5.1% gap to this session's −10.7% gap), but durable intrinsic growth (+10%/yr) keeps expected return just above the 10% hurdle rather than pushing it negative — hence only a mild +2.4 trim-pressure modifier, not the large positive seen when E is genuinely negative.

---

## 9. SPOT — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (71.808) + Rate Modifier (+10) + Upside/Downside (+2.432)
                       = 84.240
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 84.2**

| | Value |
|---|---|
| Raw weighted | 71.808 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | +2.432 (E = +5.136%) |
| **FINAL VALUATION SCORE** | **84.2** |
| Prior valuation score | 80.5 (06-20) |
| **Quality Score** | **73.2 (FAILS 80.0+ gate)** |

```
Composite Score = 0.50 × (100 − 73.2) + 0.50 × 84.2 = 0.50×26.8 + 0.50×84.2 = 13.4 + 42.1 = 55.5
```

**Composite Score = 55.5.**

---

## 10. SPOT — Action & the divergence between the two scores (read carefully — see GOOG/CSGP 2026-07-04 precedent)

**Raw Valuation Score alone: 80.5 → 84.2** (stays in, and moves deeper into, the **80.0–89.9 "Trim to 50%"** band) — SPOT has gotten *more* expensive on this framework's own bottom-up metrics since 06-20, not less, confirming the prior session's flag that this is one of the portfolio's richly-valued names that the Upside/Downside Modifier correctly does not rescue.

**Composite Score (55.5) → nominally the 50.0–69.9 "HOLD — watch only" band.** Per [valuation-scoring.md](../framework/valuation-scoring.md): *"Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate."* **This numeric result must not be read as a comfortable, reassuring Hold — it is shown for transparency (this repo's established practice, per the NKE/GOOG precedent) but is not the basis for the action call below.** The action call is instead governed by the raw Valuation Score's own band and the newly-surfaced Quality Watch flag, consistent with the orchestrator's guidance for this batch and with how the GOOG 2026-07-04 session treated an analogous divergence.

**Net action: HOLD the existing 1-share position — no forced trim, no add.** Two independent, mutually-reinforcing reasons:

1. **Position-size reality (primary reason, same logic as CSGP 2026-07-04).** SPOT is held at **1 share (0.84% of portfolio)** — there is no record in `sessions/` or `decisions/` of this position ever having been larger; it appears to be a tracking-sized legacy holding from before this repo's session-log discipline began. **A mechanical "Trim to 50% of original size" instruction is not practically executable at this size** — 50% of 1 share is 0.5 shares, and even if IBKR's fractional-share support made that technically possible, the resulting change (≈$243 of proceeds, portfolio weight 0.84%→0.42%) is immaterial to portfolio risk either way. Per the task brief's own requirement, the full trim detail is shown below for the record, but is not being enacted.
2. **Quality Watch escalation (new this session).** SPOT's first-ever computed Quality Score (73.2) fails the 80.0+ gate — not by a hard disqualifier, but by a genuinely thin normalized net margin (13.7%) and a gross margin (32.3%) that a cited source frames as structurally capped by rights-holder bargaining power rather than a scale-driven advantage (§6 Moat Signal finding). This does **not** meet the Phase 06 Full Exit bar (no fundamental deterioration, no broken thesis — moat signals are mostly TRUE and the balance sheet is a deep net-cash position) — it is a **Phase 04 Quality Watch flag**, on record for the first time, worth re-checking at the next earnings print (~28-29 Jul 2026) and particularly whether the "scale cost advantage" moat signal ever earns a TRUE via a genuine cited cost-per-unit gap as scale continues to grow.

**Full trim detail (for the record, per task brief — not enacted, per reason 1 above):**

| Field | Value |
|---|---|
| Current position | 1 share, cost basis $509.00 (unrealized P&L: −$23.03 at $485.97) |
| Valuation Score band | 80.0–89.9 → "Trim to 50% of original size" |
| Recorded "original size" | None found — 1 share is the only size ever held on record |
| 50% of current holding | 0.5 shares |
| Estimated proceeds if executed | 0.5 × $485.97 ≈ $242.99 (≈0.44% of the ~$54,891 combined portfolio) |
| **Decision** | **Not enacted — immaterial at this position size; see reasons 1–2 above** |

**No standard BUY/TRIM order setup is otherwise produced** (operating-brief.md OUTPUT FORMAT step 6 applies to an enacted BUY/TRIM; this session's net action is HOLD).

**Cap note:** at 0.84%, SPOT is nowhere near Upgrade 7's 15% hard cap — not a cap-driven consideration either way.

---

## 11. Portfolio Note

This session does not change `portfolio/holdings.md` — that update (Last Score 84.2, Quality Score 73.2, Composite Score 55.5, Last Review 5 Jul 2026) is handled by the orchestrator across the batch. No trade is recommended or executed this session. SPOT's row in [watchlist/STALE.md](../watchlist/STALE.md) (2026-06-29 methodology table) should be removed by the orchestrator now that both scores are computed.

---

## 12. Next Review Triggers

- **Next earnings — SPOT Q2 FY2026, expected ~28-29 Jul 2026** — the natural near-term checkpoint; also the point at which a 3rd consecutive clean profitable quarter (if delivered without a loss quarter) starts to rebuild the case for a usable Forward-PE history and, eventually, PEG eligibility (still short of the 3+-clean-year Fast Grower bar).
- **Phase 04 Quality Watch (new this session).** SPOT's first-ever Quality Score decisively fails the 80.0+ gate (73.2) — re-verify at the next rescore whether Profitability/Margins are improving as the margin-expansion story matures, and specifically re-test the "scale cost advantage" moat signal (currently FALSE) for any cited evidence of a genuine unit-cost gap vs. smaller competitors as Spotify's scale continues to grow.
- **Label-renegotiation / rights-holder bargaining power** — the single largest identified risk to further gross-margin expansion (§6 Moat Signal finding); watch for any renegotiated major-label deal terms as a Rule 9 M&A-adjacent trigger.
- **Rule 9 fundamental triggers (standing):** any guidance revision, management change, material new M&A, or a >15% unexplained price move.
- **IBKR price-field discrepancy (§1):** re-verify at the next session whether `get_price_snapshot`'s `last` field has caught up to the correct most-recent close — this is at least the second consecutive SPOT-adjacent session (after CSGP 2026-07-04) where IBKR's snapshot fields required an independent cross-check.

---

## 13. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchases, net of new issuance. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **CER (Constant Exchange Rate)** | A growth-rate presentation that strips out currency movements by recalculating a prior period at the current period's FX rates — isolates real underlying growth from FX noise. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists — not computed to "rescue" a company failing the Quality gate. |
| **D&A** | Depreciation & Amortization. |
| **Deferred tax valuation allowance release** | A one-off GAAP accounting event where a company reverses a prior write-down on its deferred tax assets once it judges those assets are now usable — produces an artificially low effective tax rate and inflated net income in the recognition period. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean base — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **FX (foreign exchange) rate** | This framework only uses live, broker-reported FX rates to convert non-USD figures to USD — never an assumed rate. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **MAU (Monthly Active Users)** | The number of unique users who engage with a product at least once in a given month. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-bracket adjustment. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples or stale data. |
| **Rule 6** | Normalize earnings/margins/revenue/debt before valuing — strip out one-time items. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
