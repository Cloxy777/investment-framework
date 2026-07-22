# NEW POSITION — WAB (Westinghouse Air Brake Technologies Corporation / "Wabtec", NYSE) — 2026-07-22

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 22 Jul 2026 (Wednesday, regular session — evaluated intraday)
**10Y US Treasury Yield:** 4.64% (as of 2026-07-22, WebSearch/tradingeconomics.com — +0.02pp vs. 2026-07-21's 4.63%)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current WAB portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. Confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` before this session — this is WAB's first-ever evaluation under this framework.
**Sector:** Industrials — Railroads / Rail Equipment (locomotives, braking systems, signaling, digital/rail-tech)
**Filer type:** US domestic filer, NYSE-listed. Full 10-K/10-Q history available.
**First-use jargon decode:** see closing Glossary (§9).

---

## 0. Why this session exists — trigger source

A Telegram post today (2026-07-22, `myroslavkorol/2584`) noted Wabtec ($WAB) hitting a new all-time high, referencing a prior analysis video about freight-rail-doubling projections through 2050. Per the operating brief, **Telegram post text is never used as financial data** — it is a trigger only. Wabtec had no prior watchlist or holdings entry in this framework, so per `/telegram-scan`'s decision rule ("No watchlist entry exists at all → `/new-position`"), a full first-time evaluation is triggered regardless of how material the specific triggering item is. Independently (not from the Telegram post), this session confirms Wabtec did in fact make a new all-time high today, and separately that the freight-rail-doubling claim traces to real, citable third-party sources (IEA, European transport-ministry commitments) — see §1 and §5.2/§6 respectively.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$290.00** | Interactive Brokers `get_price_snapshot` (`mcp__Interactive-Brokers__search_contracts` → contract_id 661633, NYSE:WAB), `last` field, intraday |
| Day's change | +$26.47 (+10.04%) | IBKR snapshot `change` field |
| Implied prior close | ~$263.53 | Derived from IBKR change fields; cross-checked against stockanalysis.com's own reported prior close ($289.88 − $26.35 = $263.53) — consistent |
| Today's intraday range | $271.44 – **$295.41** | IBKR snapshot `low`/`high` fields — **$295.41 is a new all-time high**, above the pre-existing 52-week high of $284.79 |
| 52-week range (pre-today) | $183.96 – $284.79 | IBKR snapshot `misc_statistics` |
| Analyst consensus target | $304.09 (mean, 12 analysts, "Strong Buy") | WebFetch, stockanalysis.com; recent target raises: BofA $322, Morgan Stanley $318, Citi $311, Susquehanna $305 (WebSearch) |
| Market Cap | $49.19B | stockanalysis.com (169.6M shares × ~$290) |
| US 10Y Treasury yield | 4.64% | WebSearch, tradingeconomics.com/CNBC, 2026-07-22 |

**$290.00 is used as the live price for this session**, fetched directly via the IBKR MCP tool per Rule 0. **The +10.04% single-day move is fully, independently explained by a same-day fundamental event**: Wabtec reported Q2 2026 earnings before today's open — adjusted EPS $2.76 (vs. $2.63 consensus, +21.6% YoY), revenue $3.18B (vs. ~$3.11B consensus, +17.5% YoY), a 41.7% backlog surge to a record $30.9B, and raised FY2026 revenue guidance to $12.30–12.60B and adjusted EPS guidance to $10.60–10.90 (WebSearch: stocktitan.net, tradingpedia.com, progressiverailroading.com, gurufocus.com). This is a genuine Rule 9 earnings-release trigger, not an unexplained move — no separate >15% "unexplained move" re-score protocol applies. This also independently confirms the Telegram post's "new all-time high" claim from primary market data (IBKR), not from the post itself.

---

## 2. Data Gathered — Sources & Method

### 2.1 Primary data source

`yfinance` was attempted first per the standard tooling (`pip install --quiet yfinance lxml`), but hit the same `curl_cffi`-based TLS connection reset documented in this sandbox previously (`curl: (35) Recv failure: Connection reset by peer`), reproduced even after `pip install --upgrade curl_cffi`. Per the fallback instruction, all fundamentals below are sourced via WebFetch of **stockanalysis.com** (annual + quarterly income statement, balance sheet, cash-flow statement, ratios pages) and cross-checked/supplemented via WebSearch of primary sources — Wabtec's own Q2 2026 and Q4 2025 earnings releases (via stocktitan.net, progressiverailroading.com, theglobeandmail.com/SEC-filed transcripts, finance.yahoo.com/wabteccorp.com press releases), and third-party industry sources (Railway Age, FreightWaves, the IEA) for moat/TAM evidence. Every figure below is cited to its source; no figure is invented or estimated.

### 2.2 Income statement — annual (stockanalysis.com, $ millions)

| | FY2021 | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|---|
| Revenue | 7,822 | 8,362 | 9,677 | 10,387 | 11,167 |
| Gross Profit | 2,369 | 2,540 | 2,944 | 3,366 | 3,806 |
| Gross Margin | 30.29% | 30.38% | 30.42% | 32.41% | 34.08% |
| Operating Income (EBIT) | 876 | 1,011 | 1,266 | 1,609 | 1,793 |
| EBITDA | 1,367 | 1,490 | 1,797 | 2,112 | 2,294 |
| Net Income | 565 | 641 | 825 | 1,067 | 1,183 |
| Net Margin | 7.22% | 7.67% | 8.53% | 10.27% | 10.59% |
| EPS (diluted) | 2.96 | 3.46 | 4.53 | 6.04 | 6.83 |

**Revenue 3yr CAGR (FY2022→FY2025)** = `(11,167/8,362)^(1/3) − 1 = 10.10%`

**Gross margin has expanded every year for 4 consecutive years** (30.29% → 34.08%), a clear, structural (not one-quarter) trend — relevant to the Margins sub-score bonus below.

### 2.3 TTM reconstruction (Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026) — most recent 4 quarters, Q2 2026 reported today

| ($ millions) | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | **TTM** |
|---|---|---|---|---|---|
| Revenue | 2,886 | 2,965 | 2,950 | 3,179 | **11,980** (matches stockanalysis.com's reported TTM revenue $11.98B exactly) |
| Gross Profit | 1,002 | 966 | 1,061 | 1,161 | **4,190** (34.97% margin) |
| Operating Income (EBIT) | 491 | 356 | 517 | 600 | **1,964** |
| EBITDA | 619 | 492 | 656 | 743 | **2,510** |
| Net Income (GAAP) | 313 | 204 | 363 | 395 | **1,275** (10.64% margin — matches stockanalysis.com's reported TTM net income $1.27B exactly) |
| Pretax income | 425 | 291 | 469 | 518 | **1,703** |
| Tax provision | 112 | 87 | 106 | 122 | **427** |
| Operating Cash Flow | 367 | 992 | 199 | 441 | **1,999** |
| CapEx | 55 | 122 | 46 | 62 | **285** |
| **FCF (OCF − CapEx)** | 312 | 870 | 153 | 379 | **1,714** (internally consistent: 1,999 − 285 = 1,714 ✓) |

**TTM effective tax rate** = 427 / 1,703 = **25.07%** (source: stockanalysis.com quarterly pretax income / tax provision rows)

### 2.4 Balance sheet — quarterly (stockanalysis.com, $ millions)

| | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | **Q2 2026 (most current)** |
|---|---|---|---|---|---|
| Total Debt | 4,784 | 5,285 | 5,541 | 6,538 | **6,571** |
| Cash & Equivalents | 1,499 | 528 | 789 | 531 | **670** |
| Total Equity | 10,845 | 11,048 | 11,142 | 11,103 | **11,214** |
| Shares Outstanding | 171.7M | 171.1M | 171.1M | 170.6M | **169.6M** |

**⚠️ Debt jumped materially (+$997M) between Q4 2025 and Q1 2026 — independently investigated, not treated as a data anomaly.** WebSearch confirms Wabtec completed the **Dellner Couplers acquisition** (~$960M–$1B, Sweden-based rail-coupler/connection-systems maker) on 11 February 2026, funded substantially with new debt (sources: markets.financialcontent.com, gurufocus.com Q1 2026 earnings coverage). Wabtec's own Q2 2026 disclosure states it ended the quarter with "more than $2 billion in liquidity and a net debt leverage ratio of 2.2 times, remaining within the company's stated range of 2.0 to 2.5 times even after funding the roughly $1 billion Dellner acquisition" — the company's own figure is close to, and cross-checks, this framework's independently-computed ratio below.

**Net Debt (Q2 2026, most current)** = 6,571 − 670 = **5,901**
**Net Debt/EBITDA (TTM)** = 5,901 / 2,510 = **2.351×**

(This framework's own GAAP-EBITDA-based computation of 2.351× and the company's own stated 2.2× management-adjusted-EBITDA figure are in the same range and support the same conclusion — under the 2.5× standard threshold, narrowly.)

### 2.5 Q4 2025 one-off items — investigated for earnings-quality distortion (Rule 6)

Q4 2025 net margin (6.88%) is a clear outlier vs. the other four TTM quarters (10.85%–12.53%). WebSearch of Wabtec's own Q4 2025 earnings release (SEC-filed 8-K, via Yahoo Finance/wabteccorp.com/ir.wabteccorp.com) confirms this was driven by **$55M of net pretax restructuring, transaction, and purchase-accounting charges** — GAAP EPS fell 4.1% YoY to $1.18 even as adjusted EPS rose 25.0% YoY to $2.10. This is a documented, cited, one-off item (not invented), consistent with the Dellner acquisition integration. **No addback is applied to the primary GAAP figures used below** (a conservative choice — normalizing it out would only improve the Quality Score, and the TTM figures already dilute its effect to ~3–4% of TTM net income), but it is flagged per Rule 6 as the explanation for the Q4 dip, and is a genuine one-off rather than a sign of structural profitability deterioration.

### 2.6 Qualitative / Moat evidence (independently sourced, not from the Telegram post)

- **Market share:** Wabtec holds an estimated **~65–75% of the North American locomotive fleet installed base** and **~90% of new Tier 4-compliant locomotives**, in a structural **near-duopoly** with Caterpillar's Progress Rail (WebSearch, multiple independent sources including Railway Age/Cowen commentary, pestel-analysis.com competitive-landscape summaries) — reinforced by Wabtec's 2019 acquisition of GE Transportation. Backlog reached a **record $30.9B, +41.7% YoY** as of Q2 2026 (company's own Q2 2026 release, via stocktitan.net) — evidence the position is stable-to-growing, not merely a static historical share.
- **Pricing power:** Company-cited **190bps adjusted-gross-margin improvement** attributed to "pricing actions implemented across product lines," alongside the framework-independent, 4-consecutive-year GAAP gross-margin expansion trend in §2.2 (30.29%→34.08%). Industry commentary (WebSearch, ad-hoc-news.de coverage) separately notes Wabtec's pricing power is strongest in "safety-critical, qualified, or proprietary components" — consistent with an OEM-parts moat.
- **Switching costs:** Documented **long-term service agreements (LTSAs)** tied to an installed base of 23,000+ locomotives globally — cited specific contracts: a **$300M+ multi-year parts agreement with a Class I railroad**, a **$240M+ first multi-year service contract in Brazil**, and an Asia-market long-term parts agreement (WebSearch, Railway Age/Alphastreet coverage). **Aftermarket revenue is 61% of Freight segment revenue and 55% of Transit segment revenue** (WebSearch) — high-margin, recurring, and tied to OEM-parts sourcing norms in a safety-critical industry.
- **TAM/growth evidence (independently verified, not from the Telegram post):** The IEA's own published analysis states global rail freight/passenger activity is "more than double by 2050" under present trends; European transport ministers have separately committed to doubling rail freight volume by 2050 (WebSearch, iea.org "The Future of Rail," maritime-executive.com). This independently corroborates — from a primary/third-party source, not the triggering Telegram post — the general direction of the freight-rail-growth narrative that prompted this session, while remaining a long-horizon (2050) structural tailwind rather than a near-term catalyst (see §7 Upside/Downside guardrail discussion, not reached this session).

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check (fails regardless of weighted score)

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | FY2021 166.9% · FY2022 138.7% · FY2023 123.0% · FY2024 152.5% · FY2025 126.7% · TTM 134.4% | disqualify if 2+ **consecutive** years <70% w/o carve-out | **Does not fire** — every year shown is well above 70%, not below it at all. |
| Net Debt/EBITDA over threshold (2.5× standard — WAB is a capital-intensive industrial manufacturer, not asset-light/Upgrade-5-eligible) | **2.351×** (TTM, current Q2 2026 balance sheet — §2.4) | disqualify if exceeds 2.5× | **Passes, narrowly** — under the 2.5× line by ~0.15×, post-Dellner-acquisition debt increase. Company's own stated 2.2× (management/adjusted-EBITDA basis) is consistent. |
| FCF positive 3+ consecutive years | FY2021 $943M · FY2022 $889M · FY2023 $1,015M · FY2024 $1,627M · FY2025 $1,499M — all five years positive | disqualify if not 3 consecutive positive years | **Passes** — FCF positive every year shown, consistently in the $0.9–1.6B range. |

**No hard disqualifier fires.** Proceeding to the full weighted Quality Score.

### 3.2 Quality Score — full computation

```
PROFITABILITY (25% weight):
  Net Margin (TTM) = 1,275 / 11,980 = 10.64%
  NetMargin_Component = clamp((10.64/30)×100, 0, 100) = 35.5

  EBIT_TTM = 1,964
  Effective tax rate (TTM, actual: tax provision ÷ pretax income, §2.3) = 25.07%
  NOPAT = 1,964 × (1 − 0.2507) = 1,471.6
  Invested Capital (Q2 2026, most current) = Total Debt + Equity − Cash
                                            = 6,571 + 11,214 − 670 = 17,115
  ROIC = 1,471.6 / 17,115 = 8.60%
  ROIC_Component = clamp((8.60/30)×100, 0, 100) = 28.7
  (Cross-check: this framework's independently-computed 8.60% ROIC matches stockanalysis.com's
   own published "Return on Invested Capital: 8.60%" figure exactly — strong confirmation the
   methodology and inputs are consistent with a standard convention, not an artifact of this
   session's own tax-rate or invested-capital assumptions.)

  Profitability_Score = (35.5 + 28.7) / 2 = 32.1
  (FCF-positive-3yr cap does not apply — WAB is FCF-positive all 5 years shown)

MARGINS (15% weight):
  Gross Margin (TTM) = 34.97%
  GrossMargin_Score = clamp((34.97/80)×100, 0, 100) = 43.7
  3yr/multi-yr trend: 30.38% (FY22) → 30.42% (FY23) → 32.41% (FY24) → 34.08% (FY25) → 34.97% (TTM)
    — a clear, structural, 4-consecutive-year expansion (not a single-quarter blip), while still
    below the 40% static threshold. Per the rule ("structurally expanding even while below 40%,
    add +10"), this bonus applies.
  GrossMargin_Score = 43.7 + 10 = 53.7

GROWTH (20% weight):
  Revenue 3yr CAGR (FY2022→FY2025, §2.2) = 10.10%
  Growth_Score = clamp((10.10/25)×100, 0, 100) = 40.4
  TAM/pricing-power modifier: documented TAM-expansion evidence — IEA-sourced "rail freight/
    passenger activity to more than double by 2050" (§2.6, independently sourced, not from the
    Telegram trigger), record backlog +41.7% YoY to $30.9B, and Q2 2026 revenue growth
    accelerating to +17.5% YoY (from ~11.3% in Q1 2026 per WebSearch) — no documented structural
    deceleration found. +10 applies.
  Growth_Score = 40.4 + 10 = 50.4

BALANCE SHEET (15% weight):
  Net Debt/EBITDA (TTM, current Q2 2026 balance sheet, §2.4) = 2.351×
  BalanceSheet_Score = clamp(100×(1 − 2.351/4), 0, 100) = 41.2

MOAT SIGNAL (15% weight) — checklist, cited evidence only:
  Market share stable/growing: TRUE — ~65-75% of NA locomotive fleet installed base, ~90% of new
    Tier 4-compliant locomotives, near-duopoly with Progress Rail, record +41.7% YoY backlog
    growth (§2.6, multiple independent sources cited).
  Brand premium (pricing power): TRUE — company-cited 190bps adjusted-gross-margin improvement
    from "pricing actions implemented across product lines," corroborated by 4-consecutive-year
    independently-computed GAAP gross-margin expansion (§2.2, §2.6) — a real, cited pricing-power
    signal, not merely a self-reported claim.
  Network effect: FALSE — no two-sided-marketplace/user-growth-driven-value mechanism; not
    applicable to an industrial-equipment/OEM-parts business model.
  Switching costs: TRUE — documented LTSAs with specific cited contract values ($300M+ Class I
    railroad parts agreement, $240M+ Brazil service contract), 61%/55% aftermarket revenue mix
    (Freight/Transit), OEM safety-critical-parts sourcing norms (§2.6).
  Scale cost advantage: FALSE — no cited cost-per-unit data showing a gap vs. Progress Rail was
    found in this session's sourcing; installed-base scale (23,000+ locomotives) is suggestive
    but the checklist's evidentiary bar (cost-per-unit data) was not met with a citation.
  Moat_Score = (3/5) × 100 = 60.0

FCF QUALITY (10% weight):
  FCF/NI ratio (TTM, §2.3) = 1,714 / 1,275 = 134.4%
  FCFQuality_Score = clamp(((1.344 − 0.40)/0.60)×100, 0, 100) = clamp(157.3, 0, 100) = 100.0

QUALITY SCORE = 32.1×0.25 + 53.7×0.15 + 50.4×0.20 + 41.2×0.15 + 60.0×0.15 + 100.0×0.10
             = 8.025 + 8.055 + 10.08 + 6.18 + 9.00 + 10.00
             = 51.34 → rounds to 51.3
```

**Quality Score = 51.3 / 100.0 — fails the 80.0+ gate by a wide margin.**

**Gate result: FAIL.** Per quality-scoring.md, operating-brief.md, and this session's explicit instructions: **do not proceed to the Rate Environment Gate, Phase 02 valuation scoring, the Composite Score, or any order setup.**

---

## 4. Phase 02 / Order Setup — NOT PRODUCED

No Rate Environment Gate, valuation score, Composite Score, fair value, or order setup is computed this session. The Quality Score gate is a strict, non-negotiable prerequisite (quality-scoring.md: *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."*) and Wabtec's Quality Score (51.3) falls well short.

*(For context only, not used in any decision: at the current $290.00 price the stock trades at ~35.5× trailing PE and ~23.5× forward PE (stockanalysis.com) — up sharply today on the earnings beat — a valuation picture that would very likely have driven a rich-to-fair Phase 02 score even had the Quality Gate been cleared. Noted for completeness, not as a substitute for the gate result above.)*

---

## 5. Data gaps flagged

No required Quality Score input was missing this session — every figure in §3.2 traces to a cited source in §2. Two items are flagged for completeness (neither changed the gate outcome):

1. **Scale cost advantage moat signal** — no cost-per-unit data vs. Progress Rail was located via this session's sourcing (stockanalysis.com + WebSearch), so this checklist item is marked FALSE for lack of citation, not because the underlying claim is necessarily false. A future re-evaluation could revisit this if a specific cost-per-unit comparison becomes available.
2. **Company's own "2.2× net debt leverage" figure** (management/adjusted-EBITDA basis) is not identical to this framework's own 2.351× GAAP-EBITDA-basis computation — both are shown (§2.4) rather than silently picking one; the GAAP-basis figure is used as primary per this framework's documented convention, and both land on the same side of the 2.5× threshold.

---

## 6. Qualitative Notes

1. **The Quality Score failure is driven mainly by profitability and leverage, not growth or cash quality.** Profitability (32.1/100, 25% weight) is the single largest drag — WAB's TTM ROIC (8.60%, independently computed and cross-checked exactly against stockanalysis.com's own published figure) sits well below this framework's general 15%+ quality bar, and TTM net margin (10.64%) is respectable for an industrial but not high by this framework's 30%-ceiling scoring convention. Balance Sheet (41.2/100, 15% weight) reflects Net Debt/EBITDA moving to 2.351× — comfortably under the 2.5× hard-disqualifier line, but well up from historical levels after the debt-funded Dellner Couplers acquisition (§2.4/§2.6), which structurally caps the sub-score even though the deal itself appears to be a legitimate, on-strategy bolt-on (rail-coupler/connection-systems maker, consistent with WAB's core rail-equipment business).
2. **FCF quality and cash generation are genuinely excellent** — FCF/NI conversion has been comfortably above 100% every year for 5 consecutive years (126–167% range), the opposite of an earnings-quality red flag. This is the strongest individual sub-score (100.0/100) and is not what's holding the Quality Score back.
3. **Today's +10.04% move is a clean, fully-explained Rule 9 earnings event** (Q2 2026 beat + raised guidance + record backlog), not an unexplained price spike — confirmed independently via WebSearch of the company's own SEC-filed press release and multiple independent financial-news outlets, before this session ever considered the Telegram post's framing.
4. **The freight-rail "doubling by 2050" narrative referenced in the triggering Telegram post has real, citable third-party support** (IEA analysis, EU rail-freight-doubling policy commitment) — credited as TAM-expansion evidence in the Growth sub-score (+10 modifier, §3.2), but this is a multi-decade structural tailwind, not a near-term financial-statement input, and does not on its own change trailing profitability/leverage enough to clear the 80.0+ gate today.
5. **The stock has already re-rated sharply today** (a new intraday all-time high of $295.41, +10.04% on the day) on the earnings beat, meaning even a hypothetical Phase 02 valuation pass would have been evaluated against a freshly-elevated price (~35.5× trailing PE) rather than a settled one — a further reason (though not the deciding one, since Quality Gate failure is dispositive) this would not be a well-timed entry point even setting the gate result aside.

---

## 7. Recommendation

# **PASS — Quality Score gate FAILS (51.3, vs. the 80.0+ threshold). Do not proceed to valuation scoring. No position, no watchlist-only tracking beyond the "not held / gate FAIL" pointer below.**

Wabtec is a well-run, near-duopoly industrial franchise with genuinely strong cash-conversion quality (FCF/NI consistently >125%), 4 consecutive years of structural gross-margin expansion, a record and still-growing $30.9B backlog, and credible long-horizon TAM tailwinds (global/European rail-freight-doubling commitments through 2050, independently verified — not merely taken from the triggering Telegram post). But it fails this framework's strict, non-negotiable 80.0+ Quality Score gate by nearly 29 points (51.3), driven primarily by **modest ROIC (8.60%, well below this framework's 15%+ general quality bar)** and a **Balance Sheet sub-score depressed by post-acquisition leverage (2.351× Net Debt/EBITDA — passes the 2.5× hard-disqualifier line, but only narrowly)** following the debt-funded Dellner Couplers acquisition. Per operating-brief.md and quality-scoring.md, **this stops the evaluation before Phase 02** — no Rate Environment Gate, valuation score, Composite Score, or fair-value/order-setup work is produced. This is a capital-intensive industrial manufacturer whose returns on capital, while solidly profitable, do not clear this framework's deliberately high quality bar — a materially different profile from a software/platform business with 20%+ ROIC and asset-light economics.

---

## 8. Next Review Trigger

- **Any Rule 9 event**: guidance revision, management change, material M&A, or macro shift. Today's earnings beat and guidance raise are already reflected in this session's data (Q2 2026 figures used throughout).
- **A meaningful ROIC/leverage improvement** — if Wabtec's TTM ROIC climbs materially above ~15% (via margin expansion, debt paydown, or both) in a future quarter, or Net Debt/EBITDA de-levers back toward pre-Dellner levels, the Quality Score would be worth recomputing, since Profitability and Balance Sheet together account for 40% of the weighted score and are the two sub-scores furthest from a passing composite.
- **A first-ever watchlist entry is created this session** (`watchlist/not-in-portfolio/WAB/WAB-2026-07-22.md`) recording the "Phase 01 FAIL" outcome, per the standard `/new-position` convention for a first-time evaluation.

---

## 9. Glossary

- **8-K**: a US company's "current report" filed with the SEC to disclose a material event between regular filings; Wabtec's Q2 2026 and Q4 2025 earnings press releases were furnished this way.
- **Aftermarket (services/parts)**: revenue from servicing/supplying parts for equipment already in use, distinct from original-equipment (OE) sales — 61% of WAB's Freight segment revenue and 55% of Transit segment revenue, credited as switching-cost Moat Signal evidence (§2.6, §3.2).
- **All-time high (ATH)**: the highest price a stock has ever traded at; WAB's intraday high today ($295.41) exceeded its prior 52-week (and, per this session's sourcing, all-time) high of $284.79.
- **CAGR (Compound Annual Growth Rate)**: the smoothed yearly growth rate between a start and end value — used for WAB's 10.10% revenue 3yr CAGR (§2.2/§3.2).
- **Class I railroad**: the US regulatory classification for the largest freight railroads (six carriers, e.g. Union Pacific, BNSF) — WAB's core customer base, cited re: its $300M+ LTSA contract (§2.6).
- **Dellner Couplers acquisition**: Wabtec's ~$960M–$1B, debt-funded February 2026 acquisition of a Swedish rail-coupler maker — the primary driver of WAB's post-Q4-2025 debt increase and Balance Sheet sub-score pressure (§2.4, §3.1, §6).
- **Duopoly / near-duopoly**: a two-competitor market structure — North American freight-locomotive manufacturing is a near-duopoly between Wabtec and Caterpillar's Progress Rail (§2.6, §3.2).
- **EBIT / EBITDA**: Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — TTM EBIT $1,964M, TTM EBITDA $2,510M for WAB (§2.3).
- **Effective tax rate**: the actual % of pretax income paid as tax — WAB's TTM figure (25.07%) is computed directly from disclosed quarterly pretax income and tax provision, used in the ROIC calculation (§2.3, §3.2).
- **EPS (diluted)**: Earnings Per Share, adjusted for potential share dilution — WAB's FY2025 diluted EPS was $6.83 (§2.2).
- **FCF / FCF/NI conversion ratio**: Free Cash Flow; FCF ÷ Net Income — a cash-quality check. WAB's TTM ratio (134.4%) is the strongest individual Quality Score input this session (§3.2).
- **Forward PE / Trailing PE**: Price ÷ next-twelve-months'-expected vs. last-twelve-months'-actual EPS — WAB's forward PE is 23.53×, trailing 35.49× (stockanalysis.com), noted for context only in §4 since Phase 02 is never reached.
- **GAAP**: Generally Accepted Accounting Principles — the standard US accounting rulebook; WAB's figures in this session are GAAP unless noted otherwise (e.g. the company's own "adjusted EPS"/"adjusted operating margin," flagged as such wherever cited).
- **Gross Margin**: Gross Profit ÷ Revenue — WAB's TTM figure (34.97%) shows a clear 4-year structural expansion trend, driving the Margins sub-score's +10 bonus (§2.2, §3.2).
- **Hard disqualifier**: a Quality Score condition that fails a company regardless of weighted score — none fired for WAB this session (§3.1).
- **IEA (International Energy Agency)**: an intergovernmental energy-data/policy organization — its own analysis (rail freight/passenger activity to more than double by 2050) is the independently-sourced basis for this session's TAM-expansion Growth-sub-score credit, distinct from the triggering Telegram post's framing (§2.6, §3.2, §6). *(New term.)*
- **Invested Capital**: debt + equity − cash, the ROIC denominator ($17,115M for WAB as of 2026-06-30).
- **LTSA (Long-Term Service Agreement)**: a multi-year maintenance/parts contract between an equipment operator and the original manufacturer — documented switching-cost evidence for WAB, including a $300M+ Class I railroad parts agreement and a $240M+ Brazil service contract (§2.6, §3.2). *(New term.)*
- **Moat**: a durable competitive advantage protecting a business's profits — WAB scored 60.0 (3 of 5 signals: market share, brand premium/pricing power, switching costs; not credited: network effect, scale cost advantage) — see §3.2.
- **Net Debt/EBITDA**: this framework's primary balance-sheet-risk gate — 2.351× for WAB (TTM, current Q2 2026 balance sheet), passing the 2.5× standard threshold narrowly after the debt-funded Dellner acquisition (§2.4).
- **Net Margin**: Net Income ÷ Revenue — WAB's TTM figure is 10.64% (§2.3).
- **NOPAT**: Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the ROIC numerator ($1,471.6M for WAB, §3.2).
- **NYSE**: the US stock exchange WAB trades on.
- **Purchase accounting**: the GAAP/IFRS method for recording an acquired company's assets/liabilities at fair value on the acquisition date, which routinely produces one-off post-deal charges — cited alongside restructuring/transaction expenses as a driver of WAB's Q4 2025 GAAP-vs-adjusted earnings gap (§2.5). *(New term.)*
- **Quality Score**: this framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to reach Phase 02. WAB scored 51.3.
- **Restructuring charge**: a cost booked for reorganizing operations (severance, integration costs) — WAB's Q4 2025 $55M net pretax restructuring/transaction/purchase-accounting charge explains that quarter's GAAP earnings dip vs. adjusted EPS (§2.5). *(New term.)*
- **ROIC**: Return on Invested Capital — WAB's TTM figure is 8.60%, independently computed and cross-checked exactly against stockanalysis.com's own published figure, below the framework's general 15%+ quality bar (§3.2).
- **Rule 9 (model refresh trigger)**: this framework's list of events requiring mandatory re-valuation (earnings release, guidance revision, M&A, management change, macro shift, >15% unexplained move) — WAB's Q2 2026 earnings release is the Rule 9 event fully explaining today's price move (§1, §6).
- **Tier 4 (locomotive emissions standard)**: the strictest US EPA locomotive-emissions tier — WAB supplies an estimated ~90% of new Tier 4-compliant North American locomotives, cited as market-share Moat Signal evidence (§2.6, §3.2). *(New term.)*
- **Treasury yield (10Y)**: this framework's risk-free-rate benchmark (4.64% this session); not used in any calculation since Phase 02 is never reached, but recorded per the standard output format.
- **TTM (Trailing Twelve Months)**: the most recent 12 months of reported results — reconstructed for WAB this session from Q3 2025 through Q2 2026, since Q2 2026 reported this morning (§2.3).
