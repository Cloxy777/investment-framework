# RESCORE — MBGL (Mobility Global, Inc.)

**Task type:** RESCORE (in name, per [GitHub issue #493](https://github.com/cloxy777/investment-framework/issues/493) — "RESCORE: MBGL - earnings released 2026-08-07"), but structurally a **first-ever Phase 01 + Phase 02 evaluation**. MBGL has never been scored: no Phase 01/02 record, no `sessions/` entry, no `watchlist/` entry, and — confirmed at the top of this session — no `portfolio/override-log.md` entry either, despite [holdings.md](../portfolio/holdings.md) flagging it "not scored — ungoverned position" in every sync since 2026-07-01. This session runs the full gate-check flow a `/new-position` evaluation would (see `.claude/commands/new-position.md`), but keeps the RESCORE session-log filename/location since that's what the triggering issue and `holdings.md` track.

**Date:** 2026-08-09 (Sunday — markets closed; most recent regular session 2026-08-07, Friday)
**10Y US Treasury Yield:** not needed this session — see §9 (Quality gate fails, so Phase 02/Rate Environment Gate is never reached, per [quality-scoring.md](../framework/quality-scoring.md)'s "stop — don't proceed to valuation" rule).
**Last review on record:** none — first-ever evaluation.
**Current MBGL portfolio weight:** 0.03% per [holdings.md](../portfolio/holdings.md) — 1 share, ~$20 market value, immaterial to sizing/cap math (Upgrade 7's 15% cap is nowhere close to relevant).

> *Jargon decoded on first use — see closing Glossary section.*

---

## 0. What MBGL Actually Is — Identity Confirmation (before anything else)

Per the task's explicit instruction not to guess, identity was confirmed independently across three sources before any analysis:

| Source | Confirms |
|---|---|
| IBKR `search_contracts("MBGL")` | `contract_id 893054611`, NYSE, symbol `MBGL`, description "MOBILITY GLOBAL INC" (a second row shows a Mexico-listed `MBGL` under a different contract_id, 898555428 — not this position; the IBKR snapshot in [ibkr.md](../portfolio/snapshots/ibkr.md) uses `893054611`, confirming the NYSE listing is the one held). |
| `yfinance` (`MBGL`, via the documented `requests.Session()` TLS workaround) | `longName`: "Mobility Global, Inc."; sector "Technology" / industry "Software - Infrastructure" (Yahoo's own sector tagging — see caveat in §2). |
| SEC EDGAR (Form 10-12B/A, Exhibit 99.1 "Information Statement," and the Form 10-Q for the quarter ended 2026-06-30) | Full legal name **Mobility Global Inc.** (CIK 0002090312), spun off from S&P Global Inc. (SPGI), effective **2026-07-01, 12:01 a.m. ET**, via a tax-free, pro-rata 1-for-1 share distribution to SPGI holders of record 2026-06-15. Now an independent NYSE-listed public company; S&P Global retained no ownership stake. |

**What the business actually does:** Mobility Global is **not** a "mobility" company in the ride-share/EV sense — it is S&P Global's former **automotive data, analytics, and insights** division, comprising two reportable segments:
- **CARFAX** (67% of Q2 2026 revenue) — the consumer-facing vehicle-history-report brand (96% in-market awareness per the company's own survey data), plus dealer-facing products (Car Listings, CARFAX For Life service-loyalty, and a Banking & Insurance Group serving lenders/insurers).
- **B2B** (33% of revenue) — two lines: *Marketing & Sales* (automotiveMastermind, Polk Auto Marketing Solutions, Market Scan Pricing Solutions, Data Studio, VIN Solutions, Recall) and *Strategy & Planning* (vehicle/supply-chain forecasting, Global Reporting, FAST scenario tool, Procurement IQ).

Customer base per the Information Statement (as of 2026-12-31): 100% of the top 40 global carmakers, 94-98% of the top 100/40 automotive suppliers, 17 of the top 20 banks/insurers, 40,000+ dealer customers, 92,000+ dealer/service-shop data sources, 53M CARFAX consumer audience.

**Sector classification note:** Yahoo tags MBGL as "Technology — Software Infrastructure"; this session treats it functionally as a **data & analytics / information-services business** (its actual revenue model — subscription and data-licensing, not infrastructure software) for the qualitative Quality Score judgments below (moat signals, TAM framing), consistent with how the company describes itself in its own SEC filings.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$19.70** | Two independent sources agree exactly: IBKR `get_price_history` (contract_id 893054611, daily bars, `step=ONE_DAY`), most recent regular-session close = **2026-08-07** ($19.70); `yfinance` `currentPrice`/`regularMarketPrice` (via the documented `requests.Session()` TLS workaround) = **$19.70** exactly, `previousClose` $20.73 — matches IBKR's own `prior-close` field ($20.73) exactly, an internal cross-check. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$19.85** at timestamp 2026-08-07 21:44:53 UTC (5:44pm ET) — an **after-hours** print (regular session closes 4:00pm ET), not the regular-session closing price. Not adopted as primary (same precedent as the 2026-08-09 SPGI session): the $19.70 regular-session close is corroborated by two independent sources to the cent, the after-hours print is single-source and thin-volume. Flagged transparently, not silently substituted. |
| 52-week range | $17.72 – $26.00 | IBKR `misc_statistics` — note this "52-week" range is mechanically extended back through MBGL's pre-spinoff, when-issued/regular-way trading window; MBGL has traded as an independent security only since 2026-07-01, ~5.5 weeks as of this session. |
| Position held | 1 share, market value ≈ $19.70–20.38 depending on snapshot timing | [portfolio/snapshots/ibkr.md](../portfolio/snapshots/ibkr.md) — 0.03% of the combined portfolio, trivial. |
| Shares outstanding | **294,821,320** (SEC 10-Q, as of 2026-07-01) | Matches SPGI's own reported 294,800,000 shares at the 1-for-1 distribution ratio (SPGI's 2026-08-09 rescore session), essentially exact. `yfinance`'s `sharesOutstanding` field shows a rounded **320,000,000** — a vendor variance, not used; the SEC-filed figure is authoritative. Not decision-relevant this session since Phase 02 (which would need market cap) is never reached. |

---

## 2. Origin of the Position — Why This Is a RESCORE Issue With No Prior Record

Per every `/rebalance` and `/sync-portfolio` session since 2026-07-01 (most recently the [2026-08-03 rebalance](../sessions/2026-08-03-rebalance.md) and the [2026-08-09 SPGI rescore](../sessions/2026-08-09-rescore-spgi.md)'s spinoff discussion): the 1-share MBGL position first appeared in `get_account_positions` on 2026-07-01, the same day the SPGI→MBGL spinoff distribution completed, with a **$0.00 average cost basis**. This is the signature of an automatic corporate-action distribution, not a discretionary trade: SPGI holders of record 2026-06-15 received 1 MBGL share for every SPGI share held, and the portfolio's SPGI position (held pre-spin) generated exactly 1 MBGL share this way. No `sessions/`, `decisions/`, or `override-log.md` entry was ever made — because no discretionary decision was made; the share simply arrived. **This session closes that gap** — see §8 for the override-log entry this triggers.

---

## 3. Data Gaps / Flags

1. **MBGL has only ~5.5 weeks of trading history and one quarter (Q2 2026) of genuine standalone-reported financials as an independent public company.** Its only pre-spin financial history is **combined (carve-out) financial statements** — allocated out of S&P Global's consolidated books "as if" Mobility had always operated independently — covering FY2023, FY2024, and FY2025 (audited) plus Q1 2026 (unaudited), disclosed in the Information Statement (Exhibit 99.1 to Form 10-12B/A, filed ~2026-06). The company's own risk factors state explicitly: *"The condensed combined financial statements may not be indicative of future performance and do not necessarily reflect what the condensed combined statements of income, balance sheets and statements of cash flows would have been had the Company operated as a stand-alone business."* This is a real, structural data-thinness issue, not a sourcing failure — flagged per-sub-score below rather than papered over.

2. **Revenue 3yr CAGR — genuine data gap, best-available-proxy used (flagged, not fabricated).** The Growth sub-score formula calls for a 3-year revenue CAGR (FY*t*-3 → FY*t*). Mobility's combined financial statements go back only to **FY2023** — FY2022 was never disclosed anywhere (Mobility never reported separately before this Form 10, and S&P Global's own segment disclosures at the time didn't isolate a directly comparable Mobility-only FY2022 revenue figure). §6 below uses the **2-year CAGR (FY2023→FY2025)** — the entity's full disclosed history — as the best available, fully real (not estimated) proxy, flagged explicitly rather than either inventing an FY2022 figure or declining to score Growth at all.

3. **No company-disclosed Gross Margin / Cost of Revenue line.** MBGL's income statement presentation (both the Information Statement and the Q2 2026 10-Q) reports "Operating-related expenses," "Selling and general expenses," and "Depreciation and amortization" as the only expense lines — there is no separate "Cost of revenue" or "Gross profit" figure, and this was independently confirmed (the company does not disclose gross profit or gross margin in its financial statements). §6/§7 use **"Operating-related expenses" as the closest available proxy for Cost of Revenue** — a common presentation convention for subscription/data-licensing businesses where "cost of revenue" (data acquisition, hosting, content licensing) is often the dominant piece of that line — clearly labeled as a proxy, not a company-reported "gross margin," and shown with the full derivation so it isn't a black-box substitution.

4. **Net Debt/EBITDA — GAAP-derived EBITDA vs. the company's own "Adjusted EBITDA," material divergence, primary convention chosen and shown.** Consistent with this framework's standing practice (see the **Adjusted EBITDA** glossary entry and the 2026-08-09 SPGI session, both of which compute a GAAP-derived EBITDA from EBIT + D&A rather than trusting a company's own non-GAAP "adjusted" figure), §7 uses **GAAP EBIT + D&A**, not MBGL's self-reported "Adjusted EBITDA" (which strips out stock-based compensation and other items). The two conventions produce **materially different Net Debt/EBITDA ratios — 2.84× (GAAP, primary) vs. 2.43× (Adjusted EBITDA, sensitivity)** — both shown transparently in §7. This matters because 2.84× **fires the hard disqualifier** (>2.5× standard threshold) while 2.43× would not; see §5/§7 for the full reasoning on why the GAAP convention is adopted as primary.

5. **Post-spin capital structure is new and directly explains the leverage.** MBGL issued **$2.0 billion of new Senior Notes** ($650M 5.050% due 2029, $650M 5.450% due 2031, $700M 6.050% due 2036) in May 2026, ahead of the spin — and used **$1.9 billion of the proceeds to fund a cash payment to S&P Global** as separation consideration (a standard "leveraged spinoff" structure: the parent extracts cash via new debt raised by the spun-off entity, rather than by selling shares). This means MBGL began its life as an independent company already carrying $2.0B of debt for a reason unrelated to its own operations or growth investment — a real, cited, non-speculative explanation for why an otherwise profitable, cash-generative business shows a stressed Balance Sheet sub-score (§7). Flagged for context, not used to waive the disqualifier.

6. **Interest coverage — H1 2026 reported figure is not representative of the go-forward run-rate.** The 10-Q's H1 2026 interest coverage (Operating profit ÷ net interest expense) computes to a superficially strong 16.3×, but the $2.0B Senior Notes were only outstanding for ~1 month of that 6-month period (issued 2026-05-29). Annualizing the notes' own stated coupons ($650M×5.050% + $650M×5.450% + $700M×6.050% ≈ $110.6M/yr) against TTM operating profit ($322M, §6) gives a much lower **~2.9× run-rate interest coverage** — used in §7's Upgrade 5 eligibility check rather than the misleadingly high partial-period figure.

7. **10Y Treasury yield not fetched this session** — not needed, since the Quality gate fails and Phase 02 (which is where the Rate Environment Gate applies) is never reached. If a future rescore reaches Phase 02, fetch fresh per Rule 0.

No data was invented anywhere below. Every fallback/flag above is either a documented framework convention (GAAP-derived EBITDA, after-hours-print exclusion) or an explicitly-labeled, transparently-shown proxy for a genuinely undisclosed figure — never a silent guess.

---

## 4. Rule 9 / Trigger Context

The triggering GitHub issue (#493) cites "earnings released 2026-08-07" — this is MBGL's **Q2 2026 10-Q** (period ended 2026-06-30, its first quarterly report as an independent filer), not a distinct new event beyond what's analyzed below. There is no prior score to compare a trigger against; this session **is** the trigger response, run as a full first-time Phase 01 evaluation.

---

## 5. Phase 01 — Hard Disqualifier Check (per [quality-scoring.md](../framework/quality-scoring.md))

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | FY2023 230.4% (375/163), FY2024 198.1% (412/208), FY2025 208.6% (461/220), TTM 201.5% (413/205, §6) — every year comfortably above 70% | disqualify if <70% for 2+ yrs | ✅ PASS, comfortably |
| Not FCF-positive for 3+ consecutive years? | FCF positive every year FY2023–FY2025 and TTM (§6) | disqualify if not FCF-positive 3+ yrs | ✅ PASS |
| Net Debt/EBITDA over its applicable threshold? | **2.84×** (GAAP EBIT+D&A basis, primary — §7) | disqualify if >2.5× (standard) or >4× (Upgrade 5 asset-light override, **not applicable here** — see below) | ❌ **FAILS — hard disqualifier fires** |

**Upgrade 5 (asset-light override, 4× threshold) eligibility checked and rejected:** MBGL's debt is unsecured Senior Notes (100% financial debt, satisfying that prong), but run-rate interest coverage is only **~2.9×** (§3 flag 6) — nowhere near the required **>15×** — and MBGL is a data/analytics company, not a "payment network or exchange" (the override's stated examples), a stretch fit even before the interest-coverage test fails outright. **Upgrade 5 does not apply; the standard 2.5× threshold governs.**

**Per quality-scoring.md: "These mirror the existing Phase 01 non-negotiables — a weighted average can't average away an outright balance-sheet... failure." The Net Debt/EBITDA hard disqualifier fires. MBGL fails the Quality gate on this basis alone, independent of the weighted score below.** The full weighted score is still computed in §7, for the record and per this framework's "no black box, show every calculation" discipline — not because it could rescue the gate outcome (it can't: see §7's Final Quality Score, which fails independently and decisively even before the hard disqualifier is applied).

---

## 6. MBGL — Inputs Collected

**Sector:** Automotive data, analytics & insights (Technology per vendor tagging — see §0 caveat)

**Combined/standalone financial history (Information Statement, Exhibit 99.1 to Form 10-12B/A — audited for FY2023–FY2025, unaudited for Q1/Q2 2026):**

| Item (USD millions) | FY2023 | FY2024 | FY2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|---|
| Revenue | 1,485 | 1,613 | 1,750 | 455 | 468 |
| Operating-related expenses (COGS proxy, §3 flag 3) | 448 | 475 | 516 | 136 | 134 |
| Operating profit | 239 | 298 | 339 | 81 | 82 |
| Net income | 163 | 208 | 220 | 55 | 53 |
| Net margin | 10.98% | 12.90% | 12.57% | 12.09% | 11.32% |
| D&A | 307 | 309 | 310 | 78 | 77 |
| Operating cash flow | 393 | 427 | 485 | 54 | (H1'26: 189) |
| Free cash flow (company-disclosed non-GAAP) | 375 | 412 | 461 | 48 | (H1'26: 177) |
| Pretax income / tax provision | 224/61 | 284/76 | 326/106 | 78/23 | (H1'26: 153/45) |

*Source: summary combined financial data table, Information Statement pp. 23-25; Q2 2026 figures cross-derived from the 10-Q's H1 2026 totals minus the Information Statement's Q1 2026 figures (both filings agree to the dollar on every overlapping figure — a strong internal cross-check).*

**TTM (Q3'25 + Q4'25 + Q1'26 + Q2'26) — derived, not separately reported by the company:**

| Item | Calculation | TTM Value |
|---|---|---|
| Revenue | (1,750 − 420 − 439) + 455 + 468 | **$1,814M** |
| Operating-related expenses | (516 − 127 − 132) + 136 + 134 | **$527M** |
| Operating profit (EBIT) | (339 − 84 − 96) + 81 + 82 | **$322M** |
| Net income | (220 − 58 − 65) + 55 + 53 | **$205M** |
| D&A | (310 − 78 − 77) + 78 + 77 | **$310M** |
| GAAP EBITDA (EBIT + D&A) | 322 + 310 | **$632M** |
| Company "Adjusted EBITDA" (non-GAAP, sensitivity only) | (711 − 169 − 188) + 184 + 202 | **$740M** |
| Free cash flow (company-disclosed) | (461 − 62 − 163) + 48 + 129 | **$413M** |
| Pretax income | (326 − 81 − 92) + 78 + 75 | **$306M** |
| Tax provision | (106 − 23 − 27) + 23 + 22 | **$101M** |
| Effective tax rate | 101 / 306 | **33.0%** |

*(Q2 2025 figures used above — revenue $439M, Operating-related exp. $132M, operating profit $96M, net income $65M, Adjusted EBITDA $188M, D&A $77M — are from the Q2 2026 10-Q's own Q2 2025 comparative column.)*

**Balance sheet (most recent, 2026-06-30, 10-Q — post-spin, reflects the new capital structure):**

| Item | Value | Source |
|---|---|---|
| Total debt (Senior Notes) | $1,981M | 10-Q — $650M 5.050% '29 + $650M 5.450% '31 + $700M 6.050% '36 |
| Cash and cash equivalents | $186M | 10-Q |
| **Net Debt** | **$1,795M** | Computed |
| Total stockholders' equity | $9,835M | 10-Q (down from $11,485M at 2025-12-31, largely reflecting the $1,900M cash distribution to S&P Global funded by the Senior Notes issuance — §3 flag 5) |
| **Invested Capital (Debt + Equity)** | **$11,816M** | Computed |
| Total assets | $13,060M | 10-Q |

**Derived ratios and moat/growth evidence:**

```
NOPAT (TTM)          = EBIT × (1 − tax rate) = $322M × (1 − 0.330) = $215.74M
ROIC (TTM)            = $215.74M / $11,816M = 1.826%
FCF/NI (TTM)          = $413M / $205M = 201.5%
Gross margin (proxy)  = ($1,814M − $527M) / $1,814M = 70.95%
Revenue 2yr CAGR       = (1,750/1,485)^(1/2) − 1 = 8.56%  (flagged proxy for 3yr — §3 flag 2)
Net Debt/EBITDA (GAAP, primary)      = $1,795M / $632M = 2.840×
Net Debt/EBITDA (Adj. EBITDA, sensitivity) = $1,795M / $740M = 2.426×
Run-rate interest coverage            = $322M / $110.6M ≈ 2.91×  (§3 flag 6)
```

**TAM / pricing-power evidence (cited, Information Statement pp. 3-4, 118-119):**
- *"We believe...our strategic positioning enables us to achieve sustained growth, high retention and strong pricing power."* — company's own stated TAM/pricing-power claim.
- $75-81B total addressable market (2025 estimate, per the company's own segmentation: Core $13-15B, Extended Core $25-27B, Adjacencies $37-39B) — a large, mostly-untapped TAM relative to $1.75B FY2025 revenue.
- *"[CARFAX] is amplified by deep, embedded workflow partnerships that raise switching costs and support both pricing power and cross-sell."*

**Moat signal evidence (cited, Information Statement):**

| Signal | Marked | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** (flagged as a thinner-than-ideal proxy) | Cited near-universal customer penetration among the largest, most valuable accounts in its market: "100% of the top 40 global carmakers," "94% of the top 100 automotive suppliers" and "98% usage among the top 40 suppliers," "17 of the top 20 banks and insurers" (all as of 2025-12-31). This is real, company-filed, cited data — but it is a **single-point-in-time penetration statistic**, not a multi-year market-share-trend figure (no earlier-year comparison exists in the available filings), so it's a proxy for "stable or growing" rather than direct trend evidence. |
| Brand premium | **FALSE** | CARFAX's 96% in-market awareness / 85% mascot recognition is brand-*awareness* evidence, not the specific price-increase-without-volume-loss citation this framework's Moat checklist requires. No such citation found. |
| Network effect | **TRUE** | Documented two-sided mechanism: CARFAX "operates a consumer-pull, dealer-monetization model" (consumer demand/trust built first, then monetized through dealers) layered on a data-supply flywheel — "data acquired through long-standing 'give-get' relationships with tens of thousands of service shops, dealers and police agencies," where more data-sharing partners increase the value and completeness of the vehicle-history database, attracting more consumers and dealers, which in turn attracts more data partners. |
| Switching costs | **TRUE** | Explicitly documented: "deep, embedded workflow partnerships that raise switching costs," and separately, "Our solutions are deeply embedded in our customers' workflows, providing crucial support for their high-stakes decisions in product planning, supply chain management, marketing, sales and service." |
| Scale cost advantage | **FALSE** | Barriers-to-entry language is present (177,000+ data sources, 38B+ vehicle history records, "significant cost relative to potential monetization" for a new entrant to replicate) but no **cost-per-unit vs. smaller-competitor** citation was found — the framework's specific evidentiary bar for this signal. |

No FCF-positivity cap applies to Profitability (FCF positive every year on record, §5).

---

## 7. MBGL — Quality Score (2026-06-29 methodology)

### Profitability (25% weight)

```
Net Margin (TTM)     = $205M / $1,814M = 11.30%
NetMargin_Component  = clamp((11.30/30)×100, 0, 100) = 37.67

ROIC (TTM)            = $215.74M / $11,816M = 1.826%
ROIC_Component        = clamp((1.826/30)×100, 0, 100) = 6.09

Profitability_Score   = (37.67 + 6.09) / 2 = 21.88
```
ROIC is severely depressed not by weak operating performance (11.30% net margin, 322M/1,814M ≈ 17.75% operating margin are both respectable) but by an **Invested Capital base bloated with decades of parent-company goodwill/intangible allocation plus the new $2.0B spin-related debt** — the same IHS-Markit-merger-style dynamic this framework has already documented for SPGI itself, here more pronounced.

### Margins (15% weight)

```
Gross Margin (proxy, §3 flag 3) = 70.95%
GrossMargin_Score = clamp((70.95/80)×100, 0, 100) = 88.69
```
No structural-trend bonus needed — already well above the 40% threshold the bonus targets.

### Growth (20% weight)

```
Revenue 2yr CAGR (proxy for 3yr, §3 flag 2) = 8.56%
Growth_Score = clamp((8.56/25)×100, 0, 100) = 34.22
```
**+10 (documented TAM expansion / pricing power, cited above, §6):** company-stated $75-81B TAM against $1.75B FY2025 revenue, plus the explicit "sustained growth, high retention and strong pricing power" and "switching costs...support...pricing power" citations.

No −10 deceleration penalty: FY2024→FY2025 growth (+8.5%) and Q1 2026 YoY growth (+8.1%) are consistent; Q2 2026 YoY growth (+6.6%, $468M vs $439M) is modestly slower, but this is a single quarter with no documented structural cause (no company statement attributing it to a durable trend) — per the framework's rule to never infer this modifier without a cited source, no penalty applied, flagged here as a data point to watch.

```
Growth_Score (with bonus) = clamp(34.22 + 10, 0, 100) = 44.22
```

### Balance Sheet (15% weight)

```
Net Debt/EBITDA (GAAP, primary) = $1,795M / $632M = 2.840×
BalanceSheet_Score = clamp(100×(1 − 2.840/4), 0, 100) = 29.0
```
**Sensitivity (Adjusted EBITDA basis, §3 flag 4):** 2.426× → Score = clamp(100×(1−2.426/4)) = 39.35 — still a weak sub-score either way; the choice of convention changes the hard-disqualifier outcome (§5) but not the qualitative Balance Sheet picture.

### Moat Signal (15% weight)

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $413M / $205M = 201.5%
FCFQuality_Score = clamp(((2.015 − 0.40)/0.60)×100, 0, 100) = clamp(269.2, 0, 100) = 100.0
```

### Quality Score — Final

```
Quality Score = (21.88×0.25) + (88.69×0.15) + (44.22×0.20) + (29.0×0.15) + (60.0×0.15) + (100.0×0.10)
              = 5.470 + 13.304 + 8.844 + 4.350 + 9.000 + 10.000
              = 50.968 → rounds to 51.0
```

# Quality Score = 51.0 — FAILS the 80.0+ gate decisively (29.0 points short), AND the Net Debt/EBITDA hard disqualifier independently fires (§5).

Two independent reasons the gate fails, either sufficient alone:
1. **Hard disqualifier** — Net Debt/EBITDA 2.840× exceeds the 2.5× standard threshold (§5), driven almost entirely by the **$2.0B of new Senior Notes MBGL issued specifically to fund a $1.9B cash payment to S&P Global** as separation consideration (§3 flag 5) — a real, cited, one-time capital-structure event, not an operating-performance problem.
2. **Weighted score (51.0)** — even setting the disqualifier aside, the score falls far short of 80.0, driven mainly by a severely depressed ROIC (1.83%, an artifact of a large parent-allocated Invested Capital base plus the new debt, §7 Profitability) and the same Balance Sheet weakness.

**This is not a judgment that the underlying CARFAX/B2B business is low quality** — cash generation is excellent (FCF/NI 201.5%, FCF positive every year on record), margins are solid (net margin ~11-13%, proxy gross margin ~71%), and 3 of 5 moat signals are cited-true with real documented mechanisms (network effect, switching costs, and a thinner but real market-share-penetration proxy). The gate failure is driven by (a) a leverage structure imposed *by the spinoff mechanics themselves*, not by the operating business, and (b) an Invested Capital base still carrying legacy parent-company goodwill/intangible allocation that this framework's ROIC formula does not adjust for. Both are real, current facts about the company as it exists today, not modeling artifacts to explain away — this framework scores the company as it is, not as it might look after several years of deleveraging.

Per quality-scoring.md and rescore.md: **the gate fails, so Phase 02 (Rate Environment Gate + Valuation Score + Composite Score) is not run.** This matches the treatment already established in this repo for RBRK ("not scored — fails quality gates").

---

## 8. Action Recommendation

Per the task's own framing and this framework's established precedent for a trivial, ungoverned, quality-gate-failing position (RBRK, RGL): the realistic action space here is narrow.

**Recommendation: HOLD the existing 1-share position. No forced action, no BUY, no sizing decision.**

Reasoning:
- **Position is trivial** — 0.03% of the combined portfolio, ~$19.70 market value. Neither adding to it (blocked outright by the Quality gate failure — Phase 02 was never reached, so there's no valuation-driven entry signal even in principle) nor selling it out carries any meaningful capital consequence either way.
- **Quality gate fails decisively** (§7) — this is a genuine, documented finding, not a reason to force an exit on its own. This framework's Phase 06 Full Exit triggers require fundamental deterioration, a broken growth thesis, a balance-sheet crisis, or sustained 90+ overvaluation — none of which cleanly applies to a share received passively via corporate action with no purchase decision behind it to "exit" from in the framework's sense (same logic the 2026-07-02 rebalance session applied to RGL/MBGL: "not treated as Phase 06 exit cases... neither entered under Phase 01-03, so there's no framework-compliant position to 'exit' from — the correct lens is override/governance review").
- **Flagged for the human's discretion, not decided here:** given the position now carries a formal "fails quality gates" finding (rather than just "ungoverned/uninvestigated"), the human may reasonably choose to sell out the single share purely as portfolio-hygiene housekeeping (eliminating a governance-flagged line item for a de minimis, cost-basis-$0 position) — but that is a discretionary cleanup choice, not a framework-driven trade, and this session does not recommend it as an action, only surfaces it as an option.

---

## 9. Override Log Entry (closes the gap `holdings.md` has flagged since 2026-07-01)

Added to [portfolio/override-log.md](../portfolio/override-log.md)'s Override Log table (§10 below shows the exact row) — Type: **Quality waiver / no Phase 01-02 evaluation existed until now**. This is the first formal quality-gate finding for MBGL; the "Outcome" column records this session's result (Quality Score 51.0, hard disqualifier fired, fails the 80.0+ gate) and the "Lesson" column is marked **TBD**, consistent with this log's convention of leaving that field open until the annual Q1 override review.

---

## 10. Housekeeping — Files Updated This Session

- **[sessions/2026-08-09-rescore-mbgl.md](2026-08-09-rescore-mbgl.md)** — this file (new).
- **[portfolio/holdings.md](../portfolio/holdings.md)** — MBGL row updated: Last Score → "not scored — fails quality gates" (Quality Score 51.0 computed and shown in this session, consistent with the RBRK row's convention of leaving the Last Score / Composite Score columns blank for a gate failure rather than showing a Phase-02 number that was never computed); Last Review → 09 Aug 2026.
- **[portfolio/override-log.md](../portfolio/override-log.md)** — new row added (§9 above), closing the gap flagged in every sync since 2026-07-01.
- **[watchlist/in-portfolio/MBGL/MBGL-2026-08-09.md](../watchlist/in-portfolio/MBGL/MBGL-2026-08-09.md)** — new file (first-ever watchlist entry for this ticker), per [watchlist/README.md](../watchlist/README.md).
- **[watchlist/STALE.md](../watchlist/STALE.md)** — checked, confirmed no MBGL row exists (expected — MBGL was never scored before, so there was never a stale-methodology score to flag). Nothing to clear.
- **[framework/glossary.md](../framework/glossary.md)** — no new terms required; every jargon term used above already exists in the glossary (Spin-off, Form 10, Carve-out financial statements, Discontinued operations, Hard disqualifier, Adjusted EBITDA, Net Debt/EBITDA, ROIC, NOPAT, TTM, Moat, TAM, Interest coverage, Investment grade, Quality Score, Composite Score, Human Override, Rule 0, After-hours trading, 8-K/10-Q, CAGR, D&A, EBIT, EBITDA, Gross Margin, Net Margin, FCF/NI conversion ratio, Effective tax rate all pre-exist).

---

## 11. Next Review Trigger

- **Q3 2026 earnings** (MBGL's second quarterly report as an independent company) — will extend the standalone TTM window and is the first point at which a genuine like-for-like YoY comparison (Q3 2026 standalone vs. Q3 2025 combined) becomes available; also the point at which a full 4-quarter *standalone* TTM (rather than this session's mix of carve-out and standalone quarters) becomes possible.
- **Standing Rule 9 triggers apply as normal** going forward: quarterly earnings, guidance revision, M&A, management change, macro shift, or a >15% unexplained price move.
- If MBGL's leverage meaningfully de-levers (debt paydown or EBITDA growth bringing Net Debt/EBITDA under 2.5×) **and** the weighted score approaches 80.0, re-run the full Quality Score — until then, no near-term catalyst is expected to change the gate outcome, so this is not flagged as a high-priority follow-up the way SPGI's Mobility-discontinued-operations restatement is.
- Given the position's triviality (0.03%, ~$20), routine quarterly cadence (or whenever `holdings.md` next syncs) is sufficient — no urgency escalation warranted.

---

## Glossary

| Term | Meaning |
|---|---|
| **8-K** | A US company's "current report" filed with the SEC to disclose a material event between its regular quarterly/annual filings. |
| **10-Q (Quarterly Report)** | The quarterly financial-disclosure report a US public company files with the SEC, containing unaudited (reviewed) financial statements — MBGL's Q2 2026 10-Q (period ended 2026-06-30) is its first as an independent filer. |
| **Adjusted EBITDA** | A company's own non-GAAP variant of EBITDA that strips out items management deems non-recurring — this framework computes its own GAAP-derived EBITDA (EBIT + D&A) rather than trusting a company's adjusted figure; MBGL's own "Adjusted EBITDA" ($740M TTM) is shown only as a sensitivity check against the primary GAAP figure ($632M TTM). |
| **After-hours trading** | Trading after a US exchange's regular session closes (4:00pm ET) — thinner volume, wider spreads; a genuine traded price, but not adopted as this session's Rule 0 price when a corroborated regular-session close is available (§1). |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate connecting a start and end value over several years. |
| **Carve-out financial statements** | Historical financial statements prepared for a business unit that did not previously report standalone, derived by allocating a parent company's consolidated books to the unit "as if" independent — required for a spinoff's SEC registration (Form 10). MBGL's only pre-2026-07-01 financial history (FY2023-FY2025) is on this basis, not genuine standalone-operated results. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every EDGAR filer — MBGL's is 0002090312. |
| **Composite Score** | This framework's blended 0.0-100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate. Not computed for MBGL this session (gate failure). |
| **D&A** | Depreciation & Amortization. |
| **Discontinued operations** | The US GAAP accounting treatment that reclassifies a divested/spun-off business out of ongoing results, retroactively restated for all historical periods once the disposal is complete. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization. |
| **Effective tax rate** | Tax provision ÷ pretax income for a given period, distinct from the statutory rate. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is turning into real cash. MBGL's is very strong (201.5% TTM). |
| **Form 10 (registration statement)** | The SEC filing a company spinning off a subsidiary must file to register the new entity's stock before distribution — S&P Global's Form 10 (and its 12B/A amendment) registered Mobility Global ahead of the 2026-07-01 distribution. |
| **Gross Margin** | Gross Profit (Revenue − Cost of Revenue) ÷ Revenue. MBGL does not disclose this directly; this session uses "Operating-related expenses" as a labeled proxy for Cost of Revenue (§3). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted sub-score total — MBGL's Net Debt/EBITDA (2.840×, GAAP basis) exceeds the 2.5× standard threshold, firing this disqualifier independently of the weighted score. |
| **Human Override** | A position opened or held outside the framework's own rules — tracked in `override-log.md`. MBGL's origin (an unrequested spinoff distribution never formally evaluated) is logged as one this session. |
| **Interest coverage (ratio)** | EBIT ÷ interest expense — MBGL's H1 2026 reported figure (16.3×) is a partial-period artifact; the annualized run-rate figure (~2.9×) is far weaker and used for this session's Upgrade 5 eligibility check. |
| **Investment grade** | A credit rating (BBB-/Baa3 or higher) signaling low perceived default risk — MBGL's credit rating was not disclosed in the sources reviewed this session; not needed since the Upgrade 5 override was rejected on interest-coverage grounds alone. |
| **Moat** | A durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits — MBGL scores 3 of 5 cited moat signals true (market share proxy, network effect, switching costs). |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) ÷ EBITDA — this framework's primary balance-sheet-risk gate; MBGL's is 2.840× (GAAP basis), driven by the $2.0B of Senior Notes issued to fund a cash payment to former parent S&P Global. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **Quality Score** | This framework's 0.0-100.0 continuous score grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. MBGL: **51.0**, fails the gate (and independently fails via a hard disqualifier). |
| **ROIC** | Return on Invested Capital — NOPAT ÷ (Debt + Equity). MBGL's is severely depressed (1.83% TTM) by a large parent-allocated Invested Capital base plus new spin-related debt, not by weak operating margins. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: quarterly earnings, guidance revision, management change, material M&A, macro shift, or a >15% unexplained price move. |
| **Senior Notes** | Unsecured corporate bonds ranking ahead of subordinated debt (though behind secured debt) in a bankruptcy — MBGL issued $2.0B of these ($650M 2029, $650M 2031, $700M 2036 tranches) in May 2026, using $1.9B of the proceeds to fund a cash payment to S&P Global as part of the spinoff. |
| **Spin-off** | A corporate transaction separating part of a business into a new, independently-traded public company via a pro-rata share distribution — S&P Global's 2026-07-01 spinoff of Mobility Global is the origin of this position. |
| **TAM** | Total Addressable Market — MBGL's own cited $75-81B estimate against $1.75B FY2025 revenue. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — for MBGL this session, a derived figure blending 2 quarters of carve-out (Q3-Q4 2025) and 2 quarters of genuine standalone (Q1-Q2 2026) data, flagged in §3. |
