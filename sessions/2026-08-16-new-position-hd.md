# NEW POSITION — HD (The Home Depot, Inc., NYSE)

**Task type:** NEW POSITION (unattended Telegram-scan trigger, Routine 6, first-ever evaluation)
**Date:** 2026-08-16
**10Y US Treasury yield:** ~4.68–4.70% (secondary reporting, TradingEconomics/Investing.com/Seeking Alpha snapshots as of 2026-08-14 close — recorded for the record only per the standard session template; the Rate Environment Gate is never reached this session, see §4)
**Current HD portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None — first-ever `/new-position` or `/rescore` pass on this ticker (no existing file in `watchlist/in-portfolio/HD/` or `watchlist/not-in-portfolio/HD/`, confirmed before this session started)
**Sector:** Consumer Discretionary — Home Improvement Retail (big-box)

---

## 0. Why this session exists — trigger source

Post on **bolshegold** (Telegram, post bolshegold/9986, ~09:37 UTC 2026-08-16), previewing the upcoming earnings-reporting week: *"Отчеты на неделе... $HD, $WMT - можно посмотреть, но лето, season-adjusted будет норм..."* ("Earnings reports this week... $HD, $WMT — worth a look, but it's summer, season-adjusted should be fine either way"). HD has no existing watchlist entry and is not a current holding, so per `telegram-scan.md` step 4 ("no watchlist entry exists at all") this triggers a full `/new-position` evaluation regardless of the mention's substance (established precedent — see the 2026-08-14 RDDT and 2026-07-19 DOCU first-ever evaluations). **The Telegram post's text is not used as a financial input anywhere below** — it is the reason this session exists, nothing more. Per Rule 0, all financial data below is independently sourced from HD's own SEC filings and a cross-check vendor.

Note: as of this session's run date (2026-08-16), HD had **not yet reported** its Q2 fiscal-2026 earnings (the "earnings this week" the post refers to) — HD's historical cadence points to a mid-to-late-August release. This session is therefore built on the most recent data actually filed: the FY2025 10-K (filed 2026-03-18) and the Q1 fiscal-2026 10-Q (filed 2026-05-27, quarter ended 2026-05-03). No forward-looking assumption about the pending earnings release is made anywhere below.

---

## 1. Live Price (Rule 0)

Contract confirmed via `search_contracts("HD")`: contract_id **7930**, exchange **NYSE**, description "HOME DEPOT INC" — correct primary US listing (MEXI and TSE cross-listings returned but not used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$338.55** | IBKR `get_price_snapshot`, `last` field, contract_id 7930 |
| Prior close | $341.70 | IBKR `get_price_snapshot` |
| Change | −$3.15 (−0.92%) | IBKR `get_price_snapshot` |
| 52-week high / low | $420.92 / $289.10 | IBKR `misc_statistics` |
| 26-week high / low | $391.48 / $289.10 | IBKR `misc_statistics` |
| 13-week high / low | $358.80 / $289.10 | IBKR `misc_statistics` |
| Open 52 weeks ago | $394.73 | IBKR `misc_statistics` |
| Dividend yield | 2.71% | IBKR `get_price_snapshot` |

**Cross-check:** stockanalysis.com's same-session snapshot showed $338.86 (−0.83%), Market Cap $337.88B, 52-week range $289.10–$426.75 — consistent with (small timing gap from) the IBKR figure; no material divergence. $338.55 sits **~19.5% above** its 52-week low and **~19.6% below** its 52-week high — roughly mid-range, not at an extreme. Analyst consensus 12-month price target (per stockanalysis.com, 36 analysts): mean $374.06 ("Buy" consensus, +10.4% implied) — noted for context only, not used in any calculation below.

---

## 2. Data Sourcing & Method

**`yfinance` was not attempted this session**, per the documented environment failure in prior sessions (2026-08-14 RDDT, 2026-07-19 DOCU/VRSN) — went straight to the established fallback: **SEC EDGAR XBRL `companyfacts` API** (CIK **0000354950**, primary source, directly filed figures) for every quantitative Quality Score input, cross-checked against **stockanalysis.com**'s independently-computed TTM figures via WebFetch. Every cross-checked figure below matched to the dollar or within immaterial rounding (see §3.1).

**Fiscal year convention:** Home Depot's fiscal year ends the Sunday closest to January 31. "Fiscal 2025" = the year ended **February 1, 2026** (10-K filed 2026-03-18); "fiscal 2026" is the current, in-progress year, whose first quarter ended **May 3, 2026** (10-Q filed 2026-05-27). All "FY20XX" labels below use this convention (HD's own, not calendar-year).

**Primary filings used:** FY2025 Form 10-K (accession 0001628280-26-019436, filed 2026-03-18) and Q1 FY2026 Form 10-Q (accession 0001628280-26-038247, filed 2026-05-27, period ended 2026-05-03).

---

## 3. Data Gathered

### 3.1 Income statement — SEC XBRL, cross-checked against stockanalysis.com

| Period | Revenue | Gross Profit | Operating Income (EBIT) | Net Income | Pretax Income | Tax Expense |
|---|---|---|---|---|---|---|
| FY2022 (ended 2023-01-29) | $157,403M | $52,778M | $24,039M | $17,105M | $22,477M | $5,372M |
| FY2023 (ended 2024-01-28) | $152,669M | $50,960M | $21,689M | $15,143M | $19,924M | $4,781M |
| FY2024 (ended 2025-02-02) | $159,514M | $53,308M | $21,526M | $14,806M | $19,406M | $4,600M |
| FY2025 (ended 2026-02-01) | $164,683M | $54,865M | $20,890M | $14,156M | $18,602M | $4,446M |
| Q1 FY2025 (ended 2025-05-04) | $39,856M | $13,459M | $5,133M | $3,433M | $4,542M | $1,109M |
| Q1 FY2026 (ended 2026-05-03) | $41,765M | $13,781M | $4,981M | $3,289M | $4,377M | $1,088M |

**TTM (12 months ended 2026-05-03), computed as FY2025 − Q1 FY2025 + Q1 FY2026:**
```
TTM Revenue          = 164,683 − 39,856 + 41,765  = $166,592M
TTM Gross Profit     = 54,865 − 13,459 + 13,781   = $55,187M   (33.13% gross margin)
TTM Operating Income = 20,890 − 5,133 + 4,981      = $20,738M   (12.45% operating margin)
TTM Net Income       = 14,156 − 3,433 + 3,289      = $14,012M   (8.41% net margin)
TTM Pretax Income    = 18,602 − 4,542 + 4,377      = $18,437M
TTM Tax Expense      = 4,446 − 1,109 + 1,088       = $4,425M   (24.00% effective tax rate — clean, unremarkable, no one-off distortion found)
```
**Cross-check:** stockanalysis.com independently reports HD's TTM revenue as **$166,592M**, TTM gross profit **$55,187M**, TTM operating income **$20,738M**, TTM net income **$14,012M** (net margin 8.41%), TTM EPS **$14.08** — an **exact match** to this session's own SEC-derived TTM reconstruction on every line. No distortion or one-off item found in any of the four quarters used.

### 3.2 Cash flow — SEC XBRL

| Fiscal Year | OCF | CapEx | FCF (OCF−CapEx) | Net Income | FCF/NI |
|---|---|---|---|---|---|
| FY2022 | $14,615M | $3,119M | $11,496M | $17,105M | 67.2% |
| FY2023 | $21,172M | $3,226M | $17,946M | $15,143M | 118.5% |
| FY2024 | $19,810M | $3,485M | $16,325M | $14,806M | 110.3% |
| FY2025 | $16,325M | $3,679M | $12,646M | $14,156M | 89.3% |
| Q1 FY2025 | $4,325M | $806M | $3,519M | — | — |
| Q1 FY2026 | $6,032M | $844M | $5,188M | — | — |

**TTM:**
```
TTM OCF   = 16,325 − 4,325 + 6,032 = $18,032M
TTM CapEx = 3,679 − 806 + 844      = $3,717M
TTM FCF   = 18,032 − 3,717         = $14,315M
TTM FCF/NI = 14,315 / 14,012        = 102.16%
```
**D&A (for EBITDA):**
```
TTM D&A = 3,514 (FY2025) − 855 (Q1 FY2025) + 910 (Q1 FY2026) = $3,569M
TTM EBITDA = TTM EBIT ($20,738M) + TTM D&A ($3,569M) = $24,307M
```
**FCF positive every year shown** (FY2022–FY2025, 4 consecutive years) — comfortably clears the "FCF-positive 3+ consecutive years" hard disqualifier. **FCF/NI ratio above 70% in both of the two most recently completed fiscal years** (FY2024 110.3%, FY2025 89.3%) — clears the "FCF/NI <70% for 2+ consecutive years" hard disqualifier with room to spare.

### 3.3 Balance sheet — SEC XBRL, most recent 10-Q (quarter ended 2026-05-03), verified against the filed balance sheet text

| Item | Feb 1, 2026 (FY2025 year-end) | May 3, 2026 (Q1 FY2026, most recent) |
|---|---|---|
| Cash and cash equivalents | $1,389M | **$1,601M** |
| Short-term debt (commercial paper) | $4,464M | $3,503M |
| Current installments of long-term debt | $4,967M | $5,178M |
| Long-term debt, excluding current installments | $46,341M | $44,828M |
| **Total debt (financial debt only — see §3.4)** | $55,772M | **$53,509M** |
| Current operating lease liabilities | $1,418M | $1,484M |
| Long-term operating lease liabilities | $8,160M | $8,164M |
| Total stockholders' equity | $12,813M | **$13,874M** |
| Total assets | $105,095M | $107,904M |
| Shares outstanding (cover page, most recent) | 996,011,466 (2026-03-04) | **997,116,682** (2026-05-19) |

Figures taken directly from the balance sheet captions in HD's own Q1 FY2026 10-Q text (fetched directly from the filing, not just the XBRL tag values) — HD's balance sheet presents **"Short-term debt," "Current installments of long-term debt," and "Long-term debt, excluding current installments"** as three distinct captions, wholly separate from **"Current operating lease liabilities"** and **"Long-term operating lease liabilities"**, which are their own separate captions. This company-chosen presentation is the basis for the debt-definition judgment call in §3.4.

### 3.4 Net Debt/EBITDA — a genuine judgment call, shown both ways

This framework's Net Debt/EBITDA hard-disqualifier threshold (2.5×) is close enough to HD's actual ratio that **which debt definition is used changes the outcome** — flagged explicitly, per "never invent or estimate financial data" / no black-box outputs.

**Primary calculation — "debt" per HD's own balance-sheet captions (financial debt: short-term debt + current LT debt + long-term debt only, excluding lease liabilities, which HD presents as separate captions):**
```
Total Debt = $3,503M + $5,178M + $44,828M = $53,509M
Net Debt   = $53,509M − $1,601M (cash) = $51,908M
Net Debt/EBITDA = $51,908M / $24,307M (TTM EBITDA) = 2.14×
```
**Sensitivity — "debt" broadened to include operating lease liabilities** (a defensible alternative convention for a real-estate-heavy capital-intensive retailer, and the one this framework's 2026-06-21 FDX session used, citing strategy.md's capital-intensive-business guidance; also closer to stockanalysis.com's own independently-computed "Total Debt" figure of $63,731M for HD, which appears to net operating leases in):
```
Total Debt (incl. op leases) = $53,509M + $1,484M + $8,164M = $63,157M
Net Debt (incl. op leases)   = $63,157M − $1,601M = $61,556M
Net Debt/EBITDA (incl.)      = $61,556M / $24,307M = 2.53×
```
**2.14× clears the 2.5× hard-disqualifier threshold; 2.53× narrowly breaches it.** This session adopts the **primary (excl. operating leases)** convention as the scored basis, for three reasons: (1) it matches HD's own balance-sheet captioning, which treats debt and lease liabilities as distinct line items rather than commingling them; (2) HD owns (not leases) **90% of its store square footage** (per the FY2025 10-K's Item 2 Properties table), unlike a fully-leased retail chain — its operating-lease book is a comparatively modest fraction of its real estate footprint, weakening the case for treating it identically to financial debt; (3) this framework's own glossary defines Net Debt/EBITDA simply as "total debt minus cash," without an explicit instruction to consolidate lease liabilities (unlike the explicit "Conglomerate rule" for captive financial-subsidiary debt). **This determination does not end up being outcome-determinative for this session** — see §3.9's sensitivity check, which shows the Quality Score fails the 80.0+ gate by a wide enough margin that neither debt convention changes the recommendation.

### 3.5 Growth drivers — SRS/GMS acquisitions and comparable sales (SEC filings, primary-sourced)

- **SRS Distribution acquisition** (closed 2024-06-18, ~$18.25B) — a residential/commercial specialty-trade distributor (roofing, landscape, pool supplies) serving professional contractors.
- **GMS Inc. acquisition** (closed 2025-09-04, by SRS) — a specialty building-products distributor (drywall, ceilings, steel framing). Per the FY2025 10-K's goodwill note: the acquisition's goodwill is attributed to "(i) growth acceleration in the residential and commercial Pro market; (ii) expanded capabilities and product categories; (iii) **additional addressable market opportunities**; (iv) enhanced delivery network capabilities; and (v) growth in sales force." At fiscal 2025 year-end, SRS (including GMS) operated **over 1,250 locations** across the US and Canada.
- **Q1 FY2026 10-Q, MD&A (filed 2026-05-27):** "The increase in net sales for the first quarter of fiscal 2026 was primarily driven by sales from GMS, which was acquired on September 4, 2025[,] and contributed **$1.3 billion of net sales** during the first quarter of fiscal 2026." Total Q1 FY2026 net sales growth was +4.8% YoY ($41.8B vs. $39.9B) — **the majority of that growth is directly attributable to the GMS acquisition, not organic (comparable-store) growth.**
- **Comparable sales (like-for-like, SEC-filed):** Q1 FY2026 **+0.6%**, vs. Q1 FY2025 **−0.3%** — a modest, cyclical improvement (still barely positive), not a re-acceleration. The 10-K's Item 1 "Our Strategy" section states HD is "focused on leveraging its distinct competitive advantages... to take advantage of the significant growth opportunities in the highly fragmented markets in which we operate," with "Win with Pros through our differentiated value proposition and ecosystem of capabilities" as an explicit named strategic pillar.

This is filed, dated evidence of a genuine TAM-expansion move (SRS/GMS opening HD to the larger-scale professional/commercial specialty-trade market, adjacent to but distinct from its core DIY retail business) — used as the Growth sub-score's TAM-expansion modifier (§3.7). It is also the reason HD's revenue is growing measurably faster than its underlying comparable-sales trend: **most of the top-line growth over the last two fiscal years is M&A-driven, not organic** — relevant context for the low 3-year revenue CAGR computed below.

### 3.6 Moat signal evidence — SEC filings + independent market-share data

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Independent industry data (NRF's "2026 Top 100 Hardware & Building Supply Dealers" market-share aggregation, cited via secondary web search) puts HD at **~51% share of the US home-improvement retail market**, vs. Lowe's ~28.8% and Menards ~4.6% — a commanding, multi-decade #1 position. HD's own FY2025 10-K states it is "the world's largest home improvement retailer based on net sales for fiscal 2025." Flagged nuance: the same aggregate data shows HD's own Q1 2026 comparable sales roughly flat (+0.6%, per §3.5) while Lowe's posted stronger relative momentum (+2.5% cited in the same secondary source) — so while HD's *absolute* leadership position is not in question, its *relative* momentum vs. its #2 competitor was softer in the most recent quarter. Marked TRUE on the "stable" leg (share materially unchanged, still commanding), with this nuance noted rather than smoothed over. |
| Brand premium | **FALSE** | No specific price-increase/ASP (average-selling-price) evidence independent of volume was found in the 10-K or Q1 FY2026 10-Q. HD's average ticket rose 2.3% YoY in Q1 FY2026 ($92.76 vs. $90.71) but comparable *customer transactions* fell −1.3% over the same period — consistent with mix/inflation effects on ticket size, not demonstrated pricing power (a price increase *without* volume loss, this framework's specific bar). Not credited. |
| Network effect | **FALSE** | No two-sided-marketplace or user-growth-driven-value mechanism documented — HD is a traditional physical/omnichannel retailer, not a platform business. |
| Switching costs | **TRUE** | Documented, filed mechanism specific to the Pro (professional contractor) segment: the 10-K describes "a dedicated sales force, a broad and deep assortment of Pro-focused products and brands, an extensive delivery network, our **Pro Xtra loyalty program**, and **enhanced credit offerings**" — a loyalty-program-plus-trade-credit-plus-job-site-delivery-integration bundle that raises the switching cost for a Pro's day-to-day purchasing relationship, distinct from a casual DIY shopper who can switch retailers with no friction. |
| Scale cost advantage | **FALSE** | No cost-per-unit or procurement-cost data benchmarked against a named smaller competitor (e.g. Lowe's) was found in the 10-K, 10-Q, or a search this session. HD's scale is real (~$166.6B TTM revenue, ~51% category share) but the specific evidentiary bar this checklist item requires (a cited cost-per-unit gap) was not found. |

```
Moat_Score = (2/5) × 100 = 40.0
```

---

## 4. Phase 01 — Quality Score (2026-06-29 methodology)

### 4.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years without a documented growth-capex explanation | FY2024 110.3% / FY2025 89.3% (the two most recently completed fiscal years) — **both comfortably above 70%** | disqualify if 2+ consecutive years sub-70% | ✅ **PASS**, clean |
| Net Debt/EBITDA over its applicable threshold (2.5× standard) | **2.14×** under this session's primary (financial-debt-only) convention — see §3.4 for the full sensitivity showing 2.53× under the alternative (operating-lease-inclusive) convention | disqualify if >2.5× | ✅ **PASS** under primary convention (would **FAIL** under the alternative — flagged, does not change §4.5's outcome) |
| FCF-positive 3+ consecutive years | Positive every year FY2022–FY2025 (4 consecutive years) | disqualify if not | ✅ **PASS**, clean |

**No hard disqualifier fires under this session's primary (documented, reasoned) debt convention.**

### 4.2 Profitability (25% weight)

```
Net Margin (TTM) = 14,012 / 166,592 = 8.41%
NetMargin_Component = clamp((8.41/30)×100, 0, 100) = 28.04
```

**ROIC:**
```
Invested Capital (2026-05-03) = Total Debt ($53,509M) + Equity ($13,874M) − Cash ($1,601M) = $65,782M
Effective tax rate (TTM) = 4,425 / 18,437 = 24.00%
NOPAT (TTM) = TTM EBIT × (1 − 0.2400) = 20,738 × 0.76 = $15,760.7M
ROIC = NOPAT / Invested Capital = 15,760.7 / 65,782 = 23.96%
ROIC_Component = clamp((23.96/30)×100, 0, 100) = 79.86
```
Cross-check: stockanalysis.com's independently-computed "current" ROIC is 20.56% — same order of magnitude; the gap is fully explained by their broader debt definition (including operating leases would raise Invested Capital's denominator and lower ROIC to ~20.9%, very close to their figure) — a methodology-consistency artifact of the §3.4 judgment call, not a data error.

```
Profitability_Score = (28.04 + 79.86) / 2 = 53.95   (no FCF-positivity cap — clean 4yr positive FCF, §3.2)
```

### 4.3 Margins (15% weight)

```
Gross Margin (TTM) = 55,187 / 166,592 = 33.13%
GrossMargin_Score = clamp((33.13/80)×100, 0, 100) = 41.41
```
**No +10 structural-trend bonus:** gross margin has been essentially flat-to-slightly-declining over the trailing period (33.53% FY2022 → 33.38% FY2023 → 33.42% FY2024 → 33.32% FY2025 → 33.13% TTM) — below the 40% static threshold, but **not expanding**, so the bonus (reserved for a below-threshold margin that is structurally improving) does not apply.

`Margins_Score = 41.41`

### 4.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $157,403M → FY2025 $164,683M) = (164,683/157,403)^(1/3) − 1 = 1.52%
Growth_Score (raw) = clamp((1.52/25)×100, 0, 100) = 6.07
```
**TAM-expansion modifier (+10):** documented, filed evidence (§3.5) — the SRS Distribution (2024) and GMS Inc. (2025) acquisitions, explicitly cited in the FY2025 10-K's own goodwill note as driving "growth acceleration in the residential and commercial Pro market" and "additional addressable market opportunities," with GMS alone contributing $1.3B of net sales in Q1 FY2026 — a genuine, filed expansion into the larger-scale professional/commercial specialty-trade distribution market, adjacent to but distinct from HD's core DIY retail business.

**No deceleration modifier:** comparable sales moved from −0.3% (Q1 FY2025) to +0.6% (Q1 FY2026) — a modest *improvement*, not an accelerating decline, and consistent with a cyclical (mortgage-rate-driven housing-turnover) headwind rather than a structural, moat-eroding one. The −10 structural-deceleration modifier does not apply.

```
Growth_Score = 6.07 + 10 = 16.07
```

**Important context (not a scored input, flagged for transparency):** most of HD's *reported* revenue growth over the last two fiscal years is M&A-driven (SRS/GMS), not organic — the 3-year CAGR above, built on total reported revenue, already reflects that M&A contribution and is still just 1.52%. Underlying comparable-store growth is barely positive.

### 4.5 Balance Sheet (15% weight)

```
Net Debt/EBITDA = 2.14×   (§3.4 — primary convention)
BalanceSheet_Score = clamp(100 × (1 − 2.14/4), 0, 100) = clamp(46.60, 0, 100) = 46.60
```
`BalanceSheet_Score = 46.60`

### 4.6 Moat Signal (15% weight)

Per §3.6: 2 of 5 signals TRUE (Market share, Switching costs).
```
Moat_Score = (2/5) × 100 = 40.0
```

### 4.7 FCF Quality (10% weight)

```
TTM FCF/NI = 14,315 / 14,012 = 102.16%
FCFQuality_Score = clamp(((1.0216 − 0.40)/0.60)×100, 0, 100) = clamp(103.6, 0, 100) = 100.0
```
`FCFQuality_Score = 100.0`

### 4.8 Quality Score — final calculation

```
Quality Score = (Profitability × 0.25) + (Margins × 0.15) + (Growth × 0.20)
              + (BalanceSheet × 0.15) + (Moat × 0.15) + (FCFQuality × 0.10)

              = (53.95 × 0.25) + (41.41 × 0.15) + (16.07 × 0.20)
              + (46.60 × 0.15) + (40.0 × 0.15) + (100.0 × 0.10)

              = 13.4875 + 6.2115 + 3.214 + 6.99 + 6.00 + 10.00

              = 45.90
```

### 4.9 Gate result: **FAIL — 45.90 < 80.0** (34.1 points short)

**Sensitivity check — is this close under any plausible generous reading?** No. Stacking *every* individually-defensible generous assumption simultaneously:
- Moat_Score generously credited 5-of-5 (100.0 instead of 40.0): +9.0
- BalanceSheet_Score at its theoretical best case (Net Debt/EBITDA → 0, unrealistically favorable): +8.0
- Margins_Score given the (evidentially unsupported — margin is flat/declining, not expanding) +10 structural bonus: +1.5

Even summing all three simultaneously: 45.90 + 9.0 + 8.0 + 1.5 = **64.4 — still 15.6 points below the 80.0 gate.** The §3.4 Net Debt/EBITDA debt-definition judgment call (2.14× vs. 2.53×) is likewise immaterial to the outcome either way — whichever convention is used, the Quality Score itself fails by a wide margin, and even if the alternative convention's implied hard disqualifier were applied instead, the result (stop, do not proceed) is identical. **This is a decisive, structural fail, not a knife's-edge case.**

**This session stops here per the command specification: no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.** Home Depot does not clear the 80.0+ Quality Score gate.

---

## 5. Why this reads as a genuine (structural) miss, not a framework gap

Two sub-scores are strong — **FCF Quality (100.0)**, reflecting a business that converts accounting profit into cash cleanly (TTM FCF/NI 102%), and a respectable **ROIC (23.96%)** feeding a middling Profitability score — and no hard disqualifier fires under this session's primary (reasoned, documented) balance-sheet convention. The shortfall is concentrated in three places that are all structural features of a mature, physical, real-estate-anchored big-box retailer rather than one-off weaknesses:

1. **Margins (41.41/100, 15% weight)** — a genuinely thin-by-this-framework's-standard 33.13% gross margin. This framework's Margins sub-score is calibrated with 80% gross margin as its ceiling (software/platform economics); a retailer/distributor selling physical goods at retail markup structurally cannot approach that, independent of how well-run the business is.
2. **Growth (16.07/100, 20% weight)** — a 3-year revenue CAGR of just 1.52%, even *after* two sizeable acquisitions (SRS, GMS) that are doing most of the heavy lifting; underlying comparable-store sales are barely positive (+0.6% most recent quarter) after a multi-quarter stretch of a rate-driven housing-turnover headwind suppressing large-ticket remodeling activity.
3. **Balance Sheet (46.60/100, 15% weight)** — Net Debt/EBITDA of 2.14–2.53× (depending on lease-liability treatment) reflects a business that runs meaningfully levered relative to this framework's 0×-anchored scoring scale, even though it clears the pass/fail disqualifier threshold under the primary convention.

This is the same pattern this framework has now documented for several mature, real-economy compounders (MCD's 2026-06-24 session — revenue growth and leverage both structural fails; FDX's 2026-06-21 session — leverage and margin fails) — a legitimate, evidence-grounded application of a strict, deliberately conservative gate calibrated primarily around software/platform/asset-light compounders, applied here to a real, profitable, cash-generative, #1-in-category retailer that simply doesn't fit that specific quality profile. Not a framework limitation requiring a fix — flagged per the quality-scoring.md instruction to note (not silently patch) cases like this.

---

## 6. Recommendation: **PASS (no entry) — Quality Gate FAIL at 45.9 (need 80.0+)**

**Do not enter HD this session.** The Quality Score of 45.9 is 34.1 points below the strict 80.0+ gate — a decisive, structural fail (§4.9's sensitivity check shows no combination of defensible generous readings closes more than about half the gap). **No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup was computed**, consistent with the command specification's instruction to stop at the Quality Gate.

The triggering Telegram post (a routine "worth a look" seasonal-earnings preview, offering no specific claim about HD's own fundamentals) was used only as the reason to run this first-ever evaluation and was not relied upon for any figure or conclusion above.

---

## 7. Informational only — legacy 8-criterion Phase 01 screen

Not the binding gate (the graded Quality Score above supersedes it) — shown for template completeness per operating-calendar.md's New Position Evaluation data structure. Market cap and EV use today's live price ($338.55 × 997,116,682 shares) — informational only, not scored inputs.

| Criterion | Threshold | HD (TTM) | Pass? |
|---|---|---|---|
| Gross margin | >40% | 33.13% | ❌ |
| Net margin | >12% | 8.41% | ❌ |
| ROIC | >15% | 23.96% | ✅ |
| Revenue growth (3yr CAGR) | >8% | 1.52% | ❌ |
| FCF positive 3 consecutive years | required | Yes (4 consecutive) | ✅ |
| Net debt/EBITDA | <2.5× | 2.14× (primary convention) / 2.53× (alt. convention) | ✅ / ❌ (borderline, see §3.4) |
| FCF yield | >4% | 4.24% (FCF $14,315M / Mkt Cap $337,624.6M) | ✅ (marginal) |
| EV/EBIT | <20× | 18.79× (EV $389,532.6M / EBIT $20,738M) | ✅ (marginal) |

```
Market Cap = 997,116,682 × $338.55 = $337,624.6M
EV = Market Cap + Total Debt (primary, $53,509M) − Cash ($1,601M) = $389,532.6M
```

4–5 of 8 fail (depending on the debt-convention read) — the same underlying story as the graded score: a dominant, cash-generative, well-moated #1-in-category retailer whose margin structure and organic growth rate simply sit outside this framework's quality-gate calibration.

---

## 8. Next Review Trigger

No routine numeric re-check is scheduled (Phase 01 FAILs don't carry a numeric score to go stale — per watchlist/README.md). A future re-look is warranted on:
- **HD's pending Q2 FY2026 earnings release** (not yet reported as of this session — see §0) — the freshest complete-quarter data would shift the TTM window meaningfully once filed, and is the most immediate concrete trigger.
- A **sustained, multi-quarter re-acceleration in comparable sales** materially above the low-single-digit range seen in Q1 FY2026 (+0.6%) — e.g. driven by a mortgage-rate decline unlocking pent-up large-ticket remodeling/housing-turnover activity — which would be the most direct lever on the Growth sub-score (currently the second-largest drag after Margins).
- Standard Rule 9 triggers: guidance revision, management change, material M&A beyond SRS/GMS, macro/rate shift, or a >15% unexplained price move.

Absent any of the above, a future Telegram mention of HD should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 9. Data Gaps Flagged

1. **`yfinance`/Yahoo Finance access not attempted this session** — per the documented environment failure in prior sessions (2026-08-14 RDDT, 2026-07-19 DOCU). Worked around by pulling primary-sourced XBRL data directly from SEC EDGAR's `companyfacts` API and cross-checking against stockanalysis.com — every income-statement TTM figure matched exactly (§3.1). This is a tooling note, not a data gap in any scored input.
2. **Net Debt/EBITDA debt-definition judgment call (§3.4):** whether to include HD's ~$9.6B of operating lease liabilities in "total debt" for the Net Debt/EBITDA ratio is a genuine, documented ambiguity this framework's rules don't explicitly resolve for a real-estate-heavy retailer (unlike the explicit "Conglomerate rule" for captive-financial-subsidiary debt). This session adopted the narrower, company-balance-sheet-caption-consistent convention (2.14×, clears the hard-disqualifier threshold) as primary, with the broader convention (2.53×, breaches it) shown as an explicit, reasoned sensitivity — flagged since it is outcome-relevant to the *hard disqualifier specifically*, even though it is not outcome-relevant to the *overall recommendation* (the Quality Score fails the 80.0+ gate by 34+ points regardless of which convention is used, per §4.9).
3. **Q2 FY2026 earnings not yet reported** (§0) — this session is necessarily built on data one quarter older than what the market will have within days of this session's run date. Flagged as the most concrete near-term re-review trigger (§8), not treated as a blocking gap since every figure actually used was itself fully filed and complete, not estimated ahead of a release.

None of these gaps is silently patched around — each is the explicit reason for a flagged caveat rather than an invented number, and §4.9's sensitivity check shows none of them are outcome-determinative for the gate result.

---

## 10. Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CIK (Central Index Key)** | Full entry in [glossary.md](../framework/glossary.md). Home Depot's SEC EDGAR identifier, 0000354950, used to pull this session's primary-sourced financial data (§2). |
| **Commercial paper** | Full entry in [glossary.md](../framework/glossary.md) *(new — added this session)*. Short-term, unsecured debt HD uses as part of its working-capital financing; $3,503M outstanding as of 2026-05-03 (§3.3), included in this session's Total Debt figure. |
| **Comparable sales (comps)** | Full entry in [glossary.md](../framework/glossary.md). HD's like-for-like sales metric — +0.6% in Q1 FY2026 vs. −0.3% in Q1 FY2025 (§3.5, §4.4), the primary evidence this session's Growth sub-score modifier treats the recent softness as cyclical rather than structural. |
| **DIY / DIFM (Do-It-Yourself / Do-It-For-Me)** | Full entry in [glossary.md](../framework/glossary.md) *(new — added this session)*. HD's own terms for its two core consumer customer types — DIY customers who complete projects themselves vs. DIFM customers who buy materials/products but hire a professional installer — distinct from the separate "Pro" (professional contractor) customer segment. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used throughout this session's Balance Sheet and Profitability sub-scores. |
| **Effective tax rate** | The actual share of pretax income paid as tax in a period — 24.00% TTM for HD (§4.2), unremarkable and used to convert TTM EBIT into NOPAT for the ROIC calculation. |
| **FCF (Free Cash Flow) / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (a cash-quality check). HD's FCF/NI ratio ran 89–119% across FY2022–FY2025 (§3.2, §4.7), reflecting a business that converts accounting profit into cash cleanly. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total. None independently fires for HD under this session's primary balance-sheet convention (§4.1), though the Net Debt/EBITDA check is a close, documented judgment call (§3.4) — moot either way since the overall Quality Score fails decisively (§4.9). |
| **Invested Capital** | The total capital (debt + equity, netted for cash) deployed in a business — the denominator of this session's ROIC calculation, $65,782M for HD (§4.2). |
| **Moat Signal** | This framework's 5-point qualitative checklist (market share, brand premium, network effect, switching costs, scale cost advantage) — HD scored 2 of 5 TRUE this session (§3.6, §4.6). |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC (§4.2). |
| **Operating lease liability** | Full entry in [glossary.md](../framework/glossary.md) *(new — added this session)*. A balance-sheet liability (present and long-term) representing a company's obligation under leases it has elected not to treat as owned-asset financing (ASC 842) — HD reports these as distinct captions from its financial debt, the basis of this session's §3.4 Net Debt/EBITDA sensitivity analysis. |
| **Pro (Professional customer)** | Full entry in [glossary.md](../framework/glossary.md) *(new — added this session)*. HD's own term for a contractor/tradesperson customer buying for commercial/professional (not personal) use — the customer segment its Pro Xtra loyalty program, trade credit offerings, and the SRS/GMS acquisitions specifically target (§3.5, §3.6). |
| **Quality Score** | This framework's 0.0–100.0 continuous score grading the Phase 01 criteria; a company must score 80.0+ to proceed to Phase 02 valuation scoring at all. HD scores 45.9 this session — a decisive FAIL (§4.8–4.9). |
| **Rate Environment Gate** | The Phase 02 pre-check (Earnings Yield Spread Test + Rate Regime Modifier) run before every valuation score; never reached this session since the Quality Score gate fails first. |
| **ROIC (Return on Invested Capital)** | How efficiently a company turns invested capital into profit; a core quality signal in this framework. HD's ROIC (23.96% TTM) is healthy despite the overall gate failure (§4.2). |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work, and never treat a Telegram post's claims as a verified financial input without independent confirmation. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results; the primary basis for this session's sub-score inputs, reconstructed as FY2025 annual − Q1 FY2025 + Q1 FY2026 from SEC XBRL. |
| **XBRL (eXtensible Business Reporting Language)** | The structured, machine-readable data format the SEC requires companies to file financial statements in; this session's `companyfacts` API pull is XBRL data. |
