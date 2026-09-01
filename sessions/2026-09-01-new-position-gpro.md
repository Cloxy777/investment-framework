# NEW POSITION — GoPro, Inc. (NASDAQ: GPRO) — 2026-09-01

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, automated/unattended run)
**Date:** 01 Sep 2026
**10Y US Treasury Yield:** 4.77% (TradingEconomics, 2026-09-01 — "highest level since January 2025") — would sit in the 3.5–5% Rate Regime bracket (+5 modifier) **if** Phase 02 were reached. It is not: see §2. Recorded here only for session-header completeness per operating-brief.md's output format.
**GPRO portfolio weight:** 0% — not held, no row in [holdings.md](../portfolio/holdings.md)
**Prior coverage:** None. No `watchlist/in-portfolio/GPRO/` or `watchlist/not-in-portfolio/GPRO/` folder existed before this session — this is GPRO's first-ever `/new-position` evaluation under this framework.
**Sector:** Consumer Electronics — wearable/action cameras (per company's own recent disclosures, in the process of diversifying into optical/photonics components — see §0).

---

## 0. Trigger — Telegram post, and what independent verification actually found

**Source (trigger only, not used as data):** `t.me/tarasguk`, post `tarasguk/11814` (2026-09-01T16:41:28 UTC). Translated claim: "Some YouTuber said he bought 8% of GoPro shares and they rose 100%." Per this framework's Rule 0/non-negotiable rule, **this post is used only as the reason to look at GPRO** — every fact below is independently sourced via WebSearch/WebFetch against primary/wire sources, not the Telegram post.

**Independent verification of the post's claim:**

| Claim | Verified? | What the record actually shows |
|---|---|---|
| A YouTuber bought a stake in GoPro | **Confirmed, and essentially accurate.** | YouTube creator Mark "Markiplier" Fischbach disclosed an **8.5%** stake in GoPro via an SEC **Schedule 13G** filing (a passive-stake disclosure — see Glossary), reported by Fast Company, Benzinga, Yahoo Finance, 24/7 Wall St., and netinfluencer.com (all independent outlets, not the Telegram source), making him GoPro's largest individual shareholder. Fischbach told Bloomberg: "I saw the stock and where it was, I was like that seems undervalued." |
| "Shares rose 100%" | **Directionally consistent, not a single clean 100% print.** | 24/7 Wall St. reported the stock "up 173%" since the prior Friday's close after a sequence of moves (an initial +22% on the stake disclosure, then a further, much larger move — see below); GPRO also touched an intraday high of $1.64 and briefly surged over 100% pre-market on 1 September per TradingKey. The claim is roughly in the right neighborhood of the real move, unlike some past Telegram triggers checked in this framework (e.g. the 2026-08-31 WSE session's "20% drop" mischaracterization) — but see the next row for the more important fact this post **missed entirely**. |

**What the post did NOT mention — the actual dominant catalyst, found independently:** the same day as this Telegram post (1 September 2026), GoPro filed an **8-K** and issued a press release disclosing a **definitive merger agreement with Starman Optical, Inc.**, a privately-held US optical-photonics company, independently confirmed via GoPro's own investor-relations site, a PRNewswire release, and wire coverage (StreetInsider, RTTNews, Yahoo Finance, Digital Camera World, Bicycle Retailer). Deal terms:

- GoPro shareholders receive **$1.14/share in cash** (~$285M aggregate), subject to net-working-capital adjustment
- Existing GoPro shareholders retain **~10%** of the combined, still-Nasdaq-listed company (a **Recapitalization** structure — see Glossary)
- GoPro's ~$92M of outstanding debt is repaid in full at closing
- Combined company intends to pursue AI-datacenter-infrastructure, government/defense, and aerospace optical-transceiver markets
- Closing expected **by year-end 2026**, subject to regulatory approval and a GoPro shareholder vote

**Why this matters more than the Telegram post's framing:** the Markiplier stake news and the merger announcement landed on essentially the same 24–48 hours, and together — not a single YouTuber's purchase — explain the extreme volume (490M+ shares traded intraday per the IBKR snapshot below, versus GoPro's normal multi-million-share daily volume) and price action. It also means GoPro's standalone fundamentals (scored below) may soon be superseded by a corporate transaction this framework has no merger-arbitrage module for — flagged explicitly in §5.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used (GPRO, NASDAQ, contract 158249582)** | **$1.18** | IBKR live snapshot, 2026-09-01 20:09:33 UTC (16:09 ET, regular session, `is_close: false`) |
| Change (IBKR) | +$0.3038 (**+34.67%**) intraday | IBKR `change` field |
| Bid/Ask (IBKR) | $1.18 / $1.19 | Tight in absolute terms, wide in % terms given the sub-$2 share price |
| Today's volume (IBKR) | **~490.5M shares** | Extreme vs. GoPro's typical multi-million-share daily volume — consistent with the two catalysts in §0, not a data error |
| 52-week range (IBKR) | $0.57 – $3.05 | `misc_statistics` |
| Cross-check (minutes later) | $1.24 (+41.52%) | stockanalysis.com overview page — a further intraday move, not a discrepancy: this is one of the most volatile trading sessions in GPRO's history (two independent catalysts same-day), and both prints are genuine live quotes captured seconds/minutes apart |
| Cross-check 52-week range | $0.57 – $3.05 | stockanalysis.com — exact match to IBKR |
| Shares outstanding | 184.50M (current) | stockanalysis.com; cross-checks against its own stated $228.79M market cap ÷ $1.24 = 184.51M ✓. (Note: SEC Q2 2026 10-Q's *weighted-average diluted* share count for the six months ended 30 Jun 2026 was 167.243M — lower, consistent with share issuance since, itself a data point discussed in §2's balance-sheet section.) |
| Market cap (at $1.18, used below) | **≈$217.7M** (1.18 × 184.50M) | Computed |
| Beta | 2.43 | stockanalysis.com |

**Price-integrity flag (documented, not acted on):** GPRO's live price is unusually volatile intraday (two large, real catalysts converging same-day, on a sub-$2, highly-shorted micro-cap). This session does not proceed to Phase 02/order-setup (see §2), so no buy/stop/target price depends on pinning down the "exact" tick — but any future session on this name should re-fetch price fresh per Rule 0 rather than reuse either figure above.

---

## 2. Quality Score — Phase 01 (methodology version 2026-06-29)

### 2.1 Data sourcing

Per quality-scoring.md, this uses the **most recently completed fiscal years** for the disqualifier windows (rolling, not fixed) and **TTM (trailing twelve months, ended 2026-06-30)** for the continuous sub-scores, reconciled two independent ways and cross-checked:

- **Method A:** FY2025 (SEC 10-K, filed 2026-03-12) minus H1 2025 (SEC 10-Q, filed 2026-08-11 comparative) plus H1 2026 (SEC 10-Q, filed 2026-08-10, period ended 2026-06-30)
- **Method B:** Sum of Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026 (stockanalysis.com quarterly data)

Both methods agree: TTM Revenue $568.5–568.6M, TTM Net Income −$162.18M (exact match on Net Income between methods and against stockanalysis.com's independently-stated overview figure). Annual figures (stockanalysis.com, cross-checked against SEC XBRL `DepreciationDepletionAndAmortization` via `data.sec.gov/api/xbrl/companyconcept`) are used for the 3+/2+ year disqualifier windows and the 3yr CAGR.

| Fiscal Year | Revenue ($M) | Rev Growth % | Gross Profit ($M) | Gross Margin % | Operating Income ($M) | Net Income ($M) | OCF ($M) | CapEx ($M) | FCF ($M) | FCF/NI |
|---|---|---|---|---|---|---|---|---|---|---|
| FY2021 | 1,161.0 | +30.18% | 478.33 | 41.20% | 115.59 | 371.17 | 229.15 | −5.55 | 223.61 | n/m (positive base year) |
| FY2022 | 1,094.0 | −5.82% | 414.97 | 37.95% | 47.55 | 28.85 | 5.75 | −3.45 | 2.30 | 7.97% |
| FY2023 | 1,005.0 | −8.05% | 323.48 | 32.17% | −73.90 | −53.18 | −32.86 | −1.52 | −34.38 | 64.67% |
| FY2024 | 801.47 | −20.29% | 272.05 | 33.94% | −108.27 | −432.31 | −125.14 | −4.04 | −129.18 | 29.88% |
| FY2025 | 651.54 | −18.71% | 219.18 | 33.64% | −58.80 | −93.49 | −20.67 | −3.36 | −24.03 | 25.70% |
| **TTM (to 2026-06-30)** | **568.59** | (H1'26 rev −29% YoY; Q2'26 −31% YoY) | 157.38 | 27.68% | −95.80 | **−162.18** | −19.67 | −3.66 | −23.33 | 14.39% |

Sources: stockanalysis.com financials/balance-sheet/cash-flow pages; SEC 10-K (`gpro-20251231.htm`, filed 2026-03-12); SEC 10-Q (`gpro-20260630.htm`, filed 2026-08-10, period 2026-06-30) — the latter's own words: **"substantial doubt about the Company's ability to continue as a going concern."** SEC XBRL `companyconcept` API for D&A (FY2023 $6.160M, FY2024 $6.491M, FY2025 $7.065M).

Balance sheet (2026-06-30, 10-Q): Cash $27.3M, Total debt $72.656M (current only, no long-term debt), Total stockholders' equity **$(32.671)M** (a deficit — down from $76.550M at 2025-12-31), Total current liabilities $404.9M vs. Total current assets $229.1M (current ratio 0.57×).

### 2.2 Hard disqualifiers — checked first (fail regardless of weighted score)

```
[X] Not FCF-positive for 3+ consecutive years
    FY2023: −$34.38M | FY2024: −$129.18M | FY2025: −$24.03M — all three most recently
    completed fiscal years negative. FIRES.

[X] FCF/Net Income conversion ratio <70% for 2+ consecutive years, no documented
    growth-capex explanation
    FY2023: 64.67% | FY2024: 29.88% | FY2025: 25.70% — all three years <70%.
    CapEx itself is trivial ($1.5M–$5.5M/yr, ~0.5% of revenue) — nowhere close to a
    "growth capex" pattern that could explain low conversion. FIRES.

[ ] Net Debt/EBITDA over its applicable threshold (2.5x standard / 4x asset-light)
    Not evaluated as a clean disqualifier trigger — EBITDA is itself negative (TTM
    EBITDA ≈ −$88.6M), which breaks the ratio's intended meaning (see §2.3 Balance
    Sheet sub-score for the full reasoning and how this was handled). The company's
    own going-concern disclosure and negative equity independently speak to the same
    underlying balance-sheet risk this disqualifier exists to catch.
```

**Two independent hard disqualifiers fire.** Per quality-scoring.md: "fail regardless of weighted score... a weighted average can't average away an outright balance-sheet or cash-flow-quality failure." Per the `/new-position` command file, the full weighted sub-score calculation is still shown below for transparency (no black-box outputs) — but the outcome is already decided by §2.2 regardless of §2.3's total.

### 2.3 Full sub-score calculation (shown for transparency, per operating-brief.md's "no black-box outputs")

**Profitability (25% weight):**
```
NetMargin_TTM = −162.18 / 568.59 = −28.53%
NetMargin_Component = clamp((−28.53/30)×100, 0, 100) = 0.0   (floored — negative)

EBIT_TTM = −95.80M (FY2025 −58.80 − H1'25 −59.20 + H1'26 −96.20)
NOPAT_TTM ≈ EBIT_TTM = −95.80M (0% effective cash tax rate assumed on the loss — a
  company with GoPro's multi-year loss history carries a full valuation allowance
  against deferred tax assets, so no cash tax benefit is realized; standard treatment)
Invested Capital (2026-06-30) = Total debt $72.656M + Equity $(32.671)M = $39.985M
ROIC_TTM = −95.80 / 39.985 = −239.6%  (magnitude inflated by near-zero invested
  capital — flagged, but sign and floor outcome are unambiguous either way)
ROIC_Component = clamp((−239.6/30)×100, 0, 100) = 0.0   (floored)

Profitability_Score = (0.0 + 0.0) / 2 = 0.0
  (the "cap at 40.0 if not FCF-positive 3yr" rule doesn't bind — raw score is
  already below 40)
```

**Margins (15% weight):**
```
GrossMargin_TTM = 157.38 / 568.59 = 27.68%
GrossMargin_Score = clamp((27.68/80)×100, 0, 100) = 34.6
Structural trend check: FY2023 32.17% → FY2024 33.94% → FY2025 33.64% → TTM 27.68%
  — the most recent (TTM) period shows a sharp step-down, not expansion. GoPro's own
  10-K attributes this to memory-component costs up "as much as 80%" YoY and US
  tariffs on Thailand/Malaysia-made cameras rising 10%→19% (Aug 2025) — a documented,
  cited, structural margin headwind, not evidence of expansion. No +10 bonus applies.
Margins_Score = 34.6
```

**Growth (20% weight):**
```
Revenue 3yr CAGR (FY2022 $1,094.0M → FY2025 $651.54M) = (651.54/1094.0)^(1/3) − 1
  = −15.87%
Growth_Score = clamp((−15.87/25)×100, 0, 100) = 0.0   (floored)
Modifier check: documented structural (not cyclical) deceleration — five straight
  years of revenue decline (FY2022 −5.82%, FY2023 −8.05%, FY2024 −20.29%,
  FY2025 −18.71%), continuing into TTM (H1 2026 revenue −29% YoY, Q2 2026 −31% YoY,
  per SEC 10-Q) — a −10 modifier would apply, but Growth_Score is already floored
  at 0.0 so it has no further numeric effect.
Growth_Score = 0.0
```

**Balance Sheet (15% weight):**
```
Net Debt (2026-06-30) = Total debt $72.656M − Cash $27.3M = $45.356M  (net debt,
  not net cash)
EBITDA_TTM = EBIT_TTM (−95.80M) + D&A_TTM (FY2025 $7.065M − H1'25 $3.416M +
  H1'26 $3.578M = $7.227M) = −$88.57M
Net Debt/EBITDA = 45.356 / (−88.57) = −0.512×

Literal formula: BalanceSheet_Score = clamp(100×(1 − (−0.512)/4), 0, 100) = 100.0

FLAGGED AS A FORMULA EDGE CASE, NOT APPLIED: the Balance Sheet formula assumes
  positive EBITDA. With negative EBITDA, the sign flip makes more debt relative to
  more-negative cash burn read as *safer*, producing a "perfect" 100.0 for a company
  that cannot service any debt from operations at all — the opposite of what this
  sub-score exists to measure. GoPro's own 2026-06-30 Form 10-Q states, in its own
  words: "substantial doubt about the Company's ability to continue as a going
  concern," alongside a stockholders' deficit of $(32.671)M. Given the formula
  breaks down on this input and the company's own filing states the going-concern
  doubt directly and explicitly, BalanceSheet_Score is floored at 0.0 here rather
  than allowed to register the literal 100.0 — a documented judgment call applied
  to real, cited figures (not an invented input). Flagged as a candidate
  methodology gap for decisions/ if a negative-EBITDA case recurs.
BalanceSheet_Score = 0.0 (applied)  |  100.0 (literal formula, shown, not used)
```

**Moat Signal (15% weight):**

| Signal | TRUE/FALSE | Evidence (cited) |
|---|---|---|
| Market share stable or growing | **FALSE** | No market-share percentage disclosed in GoPro's 10-K. Revenue down 41% cumulatively from FY2021 ($1,161M) to FY2025 ($651.5M) is directional evidence against stability — consistent with widely-reported competitive pressure from smartphone cameras, DJI, and Insta360. |
| Brand premium | **FALSE** | 10-K cites input-cost pressure (memory +80% YoY, tariffs 10%→19%) compressing margins, with no offsetting evidence of price increases sustaining volume — the opposite of documented pricing power. |
| Network effect | **FALSE** | GoPro's own 10-K: "Limited Network effects" — subscription services mentioned but explicitly not described as a primary differentiator. |
| Switching costs | **FALSE** | No documented lock-in mechanism found (contractual, integration-depth, or data-migration). Action cameras are a low-switching-cost consumer hardware category. |
| Scale cost advantage | **FALSE** | No cost-per-unit data vs. smaller competitors found; the company is explicitly disclosed as being squeezed by input costs and tariffs, the opposite of a scale-cost advantage. |

```
Moat_Score = (0/5) × 100 = 0.0
```

(Patent portfolio — 1,608 issued US patents plus 280 pending, per the 10-K — was considered but doesn't cleanly satisfy any of the five specific evidentiary tests above (no cited instance of it blocking a competitor or supporting pricing/share), so it is not credited as a TRUE signal, consistent with "never mark a signal true without a cited source.")

**FCF Quality (10% weight):**
```
FCF/NI_TTM = −23.33 / −162.18 = 14.39%
  (Both figures negative; the ratio is technically computable but not a meaningful
  "earnings quality" read here — it's designed to flag profitable companies whose
  reported income doesn't convert to cash, not loss-making ones. Regardless, it
  floors the sub-score either way, so no separate override needed.)
FCFQuality_Score = clamp(((0.1439 − 0.40)/0.60)×100, 0, 100) = clamp(−42.68) = 0.0
```

### 2.4 Final Quality Score

```
Quality Score = (0.0×0.25) + (34.6×0.15) + (0.0×0.20) + (0.0×0.15) + (0.0×0.15) + (0.0×0.10)
              = 0.00 + 5.19 + 0.00 + 0.00 + 0.00 + 0.00
              = 5.19 → rounds to 5.2
```

## **Quality Score = 5.2 / 100.0 — fails the 80.0+ gate decisively**, independently corroborated by two hard disqualifiers (§2.2). Per quality-scoring.md and the `/new-position` command file: **stop here.** No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is computed — doing so would fabricate a number this framework's own rules say not to produce for a company that hasn't cleared the quality gate.

---

## 3. Not computed (and why)

Per the strict 80.0+ Quality Score gate, the following are explicitly **not computed** for GPRO in this session:
- Rate Environment Gate (Earnings Yield Spread Test, Rate Regime Modifier)
- Phase 02 Valuation Score (FCF Yield, EV/EBIT, Forward PE, PEG sub-scores)
- Composite Score
- Fair Value (DCF/multiples blend), Buy/Sell/Stop prices, Position Size, R/R

This is not a data gap — it's the framework working as designed: a company that fails the quality gate this decisively (5.2 vs. an 80.0 bar, plus two independent hard disqualifiers) is not evaluated further regardless of how cheap its shares look.

---

## 4. Data gaps flagged

None that block this session's conclusion. One item flagged for future sessions if GPRO is ever revisited: the Balance Sheet sub-score formula (§2.3) is not designed for negative EBITDA and required an explicit, documented judgment call rather than a clean formula application — worth a `decisions/` note if this recurs on another name.

---

## 5. Recommendation

# **PASS — do not add to watchlist as a scored candidate; Quality Score gate fails decisively (5.2/100.0).**

GoPro fails the Phase 01 Quality Score gate by a wide margin (5.2 vs. the 80.0+ bar) and independently trips two of the framework's three hard disqualifiers: it has not been free-cash-flow positive for three consecutive fiscal years (FY2023–FY2025 all negative), and its FCF/Net Income conversion ratio has been below 70% for the same three years with no growth-capex explanation (capex is trivial). Revenue has declined for four of the last five fiscal years (cumulatively −41% from the FY2021 peak, continuing at −29% YoY through H1 2026), gross margin has compressed under documented input-cost and tariff pressure, no Moat Signal criterion is satisfied on cited evidence, and the company's own 30 June 2026 Form 10-Q discloses "substantial doubt about the Company's ability to continue as a going concern" alongside a stockholders' deficit. This is not a marginal or knife-edge case.

**Separately and importantly:** GoPro is not really being evaluated as an ongoing standalone camera business anymore. On the same day as this session, GoPro entered a **definitive merger agreement with Starman Optical, Inc.** — a cash-plus-10%-stub recapitalization (see §0) expected to close by year-end 2026. If it closes, the entity being scored today largely ceases to exist in its current form (debt repaid, ~90% new ownership, a pivot toward optical/photonics/AI-datacenter markets) — a materially different business this framework would need to score fresh, not a rescore of today's numbers. If it does *not* close, today's decisively-failing standalone fundamentals stand. Either way, this framework's Quality/Valuation/Composite scoring apparatus is not built for merger-arbitrage situations (evaluating a fixed cash-plus-stub consideration against deal-completion risk and timeline) — that would be a different kind of analysis this framework doesn't currently support, and is out of scope to improvise here.

**Next review trigger:** (a) the GoPro/Starman Optical merger closing, terminating, or being materially amended (Rule 9 material M&A trigger — would warrant a fresh look at whatever entity results, not a rescore of today's GPRO); (b) GoPro's Q3 2026 earnings release (expected ~November 2026), if the deal has not yet closed by then; (c) any resolution of the going-concern doubt (e.g. a financing event) independent of the merger.

---

## 6. Glossary

*(Pulled from [glossary.md](../framework/glossary.md); two new terms — Going Concern Doubt (audit disclosure) and Recapitalization (cash-and-stub merger structure) — were added there this session.)*

| Term | Meaning |
|---|---|
| **8-K** | The "current report" a US public company must file with the SEC within days of a material event (here, the merger agreement announcement). |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **FCF (Free Cash Flow)** | Cash generated by the business after capital expenditure; Operating Cash Flow minus CapEx. |
| **Going-concern / accounting-integrity allegation** | A claim — often from a short-seller — that a company's reported financials misrepresent its true condition. Not the concept used in this session (see next entry). |
| **Going Concern Doubt (audit disclosure)** | A company's own management/auditors disclosing, in the filing itself, "substantial doubt about the Company's ability to continue as a going concern" — its own admission of a real risk it may not fund operations or meet obligations over the next twelve months. Distinct from the short-seller "allegation" entry above. GoPro's Q2 2026 10-Q used this exact language. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. GoPro trips two of the three. |
| **Invested Capital** | The total capital (debt + equity) put to work in a business — the denominator in a Return on Invested Capital (ROIC) calculation. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **Moat Signal** | This framework's 5-point Quality Score checklist (market share, brand premium, network effect, switching costs, scale cost advantage), each markable TRUE only against a cited source. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; this framework's primary balance-sheet-risk gate. Breaks down as a signal when EBITDA is negative (see §2.3). |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Quality Score** | This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading profitability, margins, growth, balance sheet, moat, and FCF quality. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. |
| **Recapitalization (cash-and-stub merger structure)** | A merger structure paying shareholders a fixed cash amount per share plus a small residual equity stake in the combined company — the structure of GoPro's announced Starman Optical merger ($1.14/share cash + ~10% stub equity). |
| **ROIC** | Return on Invested Capital — how efficiently a company turns invested capital (debt + equity) into profit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. |
| **SC 13D / SC 13G** | SEC forms an investor must file within days of acquiring beneficial ownership above 5% of a public company's stock — Schedule 13D signals activist intent, Schedule 13G a passive stake. Markiplier's disclosed 8.5% GoPro stake was a 13G. |
| **Stockholders' Deficit** | When a company's Total Liabilities exceed its Total Assets, its equity line goes negative and is relabeled a "Deficit" — GoPro's was $(32.671)M as of 2026-06-30. |
| **TTM (Trailing Twelve Months)** | The most recent four reported quarters combined, used for a company's most current run-rate — the basis for this session's continuous Quality Score inputs. |
| **XBRL (eXtensible Business Reporting Language)** | A structured, machine-readable data format the SEC requires public companies to use, letting this framework pull precise line-item figures (here, D&A) directly from filings via `data.sec.gov`'s APIs. |
