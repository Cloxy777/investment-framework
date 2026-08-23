# New Position Evaluation: BRK.B (Berkshire Hathaway Inc.) — 2026-08-23

**Task type:** NEW POSITION
**Ticker:** BRK.B — NYSE, IBKR contract_id 72063691
**Company:** Berkshire Hathaway Inc. — diversified holding company / conglomerate (insurance & reinsurance incl. GEICO, BNSF railroad, Berkshire Hathaway Energy (BHE), manufacturing/service/retailing businesses, plus a large publicly-traded equity-securities portfolio)
**Analyst:** Claude (automated session)
**10Y US Treasury yield:** Not fetched — evaluation stops at the Phase 01 Quality Score gate (Section 2h), before the Rate Environment Gate would run.

---

## 0. Trigger — and a correction to this session's own starting premise

**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) reported a first-time mention of BRK.B tied to disclosure that President Trump reportedly bought Berkshire Hathaway shares in June 2026. **This claim is used only as the reason to look at BRK.B again — no financial data, score, or conclusion below is drawn from it.**

**Independent fact-check of the trigger claim (not used as scored input):** confirmed real via multiple independent reports (CNBC, Bloomberg, Cryptopolitan) of Trump's periodic transaction report filed 2026-08-22: a $1M–$5M range purchase of BRK.B on 2026-06-18, alongside same-day purchases of Cintas, Visa, and Mastercard and sales of Meta and Motorola, as part of a broader ~1,051-transaction reshuffle disclosed for June. This is Trump's first-ever disclosed Berkshire purchase. Cited for completeness only — irrelevant to Berkshire's fundamentals and not used anywhere below. [CNBC](https://www.cnbc.com/2026/08/22/trump-reshuffled-his-portfolio-in-june-selling-names-like-meta-and-buying-berkshire-hathaway.html), [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-22/trump-s-stock-disclosure-shows-more-than-1-000-trades-in-june)

**This session's originating instructions asserted that "Berkshire Hathaway has no existing watchlist entry anywhere in this repo (checked `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` for BRK.B, BRK-B, BRKB — none exist)."** That check was incomplete: an entry **does** exist, at [watchlist/not-in-portfolio/BRK/BRK-2026-07-15.md](../watchlist/not-in-portfolio/BRK/BRK-2026-07-15.md), pointing to a full prior session, [sessions/2026-07-15-new-position-brk.md](2026-07-15-new-position-brk.md) — the folder is named `BRK` (no class suffix), which a literal string search for "BRK.B"/"BRK-B"/"BRKB" would miss. That 2026-07-15 session already ran a full Phase 01 Quality Score for this exact company/ticker (contract_id 72063691) and found a decisive **FAIL** (primary score 47.5, illustrative ceiling 56.7) — this is **not** a first-ever evaluation.

Per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 4, the bullet that actually applies here is not "no watchlist entry exists" but: *"Not held, has a prior `not-in-portfolio` entry, and the post claims materially new information beyond what that entry already reflects → `/new-position <TICKER>` again."* Two independent, legitimate reasons support re-running here rather than treating this as a routine "no action" mention:
1. The Trump-purchase disclosure is information the 2026-07-15 entry doesn't reflect (though, as fact-checked above, it carries no fundamental weight).
2. **Berkshire's Q2 2026 earnings (10-Q filed 2026-08-08)** were explicitly named in the 2026-07-15 session's own "Next review trigger" section as the next Rule 9 event that should prompt a fresh look — and that event has since occurred. This session incorporates that fresh data.

The Quality Score methodology version is unchanged since 2026-07-15 (still **2026-06-29** per [quality-scoring.md](../framework/quality-scoring.md)), so this evaluation is directly comparable to the prior one, and this is a genuine re-check with fresh TTM data, not a re-derivation under a new rule set. Everything below is computed independently from live/primary sources per Rule 0 — nothing is carried over from the July session except historical (unchanged) fiscal-year figures, each re-cited.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

| Source | Value | Note |
|---|---|---|
| **IBKR live snapshot** (contract_id 72063691) | **$496.28** | `get_price_snapshot`, `last` field. Today (Sunday 2026-08-23) markets are closed, so this is Friday 2026-08-21's closing print — the most recent price obtainable via a live fetch, per the same treatment as the 2026-07-19 AXP/SCHW Sunday-trigger sessions. (The API returned `is_close: false` on this field, which appears to be a data quirk given markets are shut on a Sunday; flagged rather than asserted as a genuine live intraday trade.) |
| IBKR `change` | −$0.58 (−0.12%) vs. prior close $496.86 | Small, unremarkable — no fundamental trigger implied by price action alone |
| IBKR `misc_statistics` | 52-week range: **$464.36 – $537.74**; 13-week/26-week high also **$537.74**; open 52 weeks ago **$491.13** | Currently ~7.7% below the 52-week high, roughly flat (+1.1%) vs. a year ago |
| IBKR `dividend_yield` | **0.0%** | Unchanged — Berkshire has never paid a dividend under Buffett or (so far) Abel |

**$496.28 is used throughout.** (For reference: the 2026-07-15 session used $490.19 — a +1.2% move over five weeks, unremarkable.)

---

## 2. Phase 01 Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

All figures sourced from Berkshire's own SEC filings — SEC EDGAR XBRL `companyconcept` API (CIK 0001067983) for exact filed tags, and Berkshire's own Q2 2026 earnings press release (`berkshirehathaway.com/news/aug0826.pdf`, read directly as a PDF, filed 2026-08-08) for the operating-earnings/segment breakdown Berkshire discloses but doesn't tag as a single XBRL concept. stockanalysis.com used only for balance-sheet/cash-flow figures not cleanly available via XBRL in the time available, each flagged as vendor-sourced. `yfinance` not attempted — recurring `curl_cffi` TLS failures documented across this repo's recent bank/conglomerate sessions (Citigroup, JPM, AXP, SCHW, and the 2026-07-15 BRK session itself).

### 2a. Profitability (25% weight)

**TTM basis** (FY2025 − H1 2025 + H1 2026, all SEC-XBRL "Revenues" / "NetIncomeLoss," the most recent complete-quarter window now available since Berkshire's Q2 2026 10-Q was filed 2026-08-08):

```
TTM Revenue    = $371,444M (FY2025) − $182,240M (H1 2025) + $195,483M (H1 2026) = $384,687M
TTM Net Income = $66,968M (FY2025) − $16,973M (H1 2025) + $35,773M (H1 2026)   = $85,768M

TTM Net Margin = 85,768 / 384,687 = 22.30%
NetMargin_Component = clamp((22.30/30)×100, 0, 100) = 74.32
```

**ROIC proxy: ROE**, per this framework's standing convention for financial/holding companies where a clean invested-capital ROIC isn't derivable without an assumed tax rate and an already-flagged unreliable EBIT figure (Section 2d):

```
Average Shareholders' Equity = ($667,989M [2025-06-30] + $747,910M [2026-06-30]) / 2 = $707,949.5M
TTM ROE = 85,768 / 707,949.5 = 12.12%
ROIC_Component (ROE proxy) = clamp((12.12/30)×100, 0, 100) = 40.40

Profitability_Score (primary, GAAP TTM basis) = (74.32 + 40.40) / 2 = 57.36
```

**FCF-positive-3-years check (feeds the Profitability cap):** **PASSES** — FCF positive every year FY2021–FY2025 (Section 2f, unchanged historical fact). No cap applied.

**Illustrative alternative — Operating Earnings basis** (Berkshire's own non-GAAP measure, excluding investment/derivative gains — the figure the company explicitly asks investors to focus on instead of GAAP net earnings; see Berkshire's Q2 2026 press release, "Use of Non-GAAP Financial Measures"):

```
TTM Operating Earnings = $44,490M (FY2025) − $20,801M (H1 2025) + $24,329M (H1 2026) = $48,018M
  (H1 2025/H1 2026 figures per Berkshire's own Q2 2026 press release, page 1)

Illustrative TTM Op-Earnings Net Margin = 48,018 / 384,687 = 12.48%  → Component = 41.60
Illustrative TTM Op-Earnings "ROE"      = 48,018 / 707,949.5 = 6.78% → Component = 22.60
Illustrative Profitability_Score (Op-Earnings basis) = (41.60 + 22.60) / 2 = 32.10
```

**Primary GAAP-basis score (57.36) is materially higher than the Op-Earnings illustrative (32.10) this period** — the mirror image of the 2026-07-15 session, where GAAP-basis (48.88) sat *above* Op-Earnings (31.17) too, but by a smaller margin. This TTM window (Jul 2025–Jun 2026) captured a particularly large non-cash swing: Q2 2026 alone included **$12.68B of investment gains**, mostly (**$10.9B**) from unrealized equity-portfolio mark-to-market moves per ASU 2016-01 (Berkshire's own press release, page 1) — not from anything the operating businesses did. This is exactly the volatility Section 0a of the 2026-07-15 session flagged: **the direction and magnitude of this distortion is not fixed, it swings with the market**, which is why a single-period GAAP Net Margin/ROE remains an unreliable standalone quality signal here even though it is used as the primary (per this framework's "score off filed GAAP figures" convention). **Primary computation (57.36) is used below**, consistent with prior sessions' treatment.

### 2b. Margins (15% weight)

```
GrossMargin_Score = clamp((29.53 / 80) × 100, 0, 100) = 36.91
```

Unchanged from 2026-07-15 — still FY2025's full-year figure (29.53%, stockanalysis.com vendor-computed, since Berkshire discloses no discrete "Gross Profit" line). **Deliberately not updated to a quarterly figure this session**: stockanalysis.com's *quarterly* "Gross Profit"/"Gross Margin" line for BRK was checked this session and found to be **identical to its "Operating Income" line every quarter** (Q2 2026: both $33,150M; Q1 2026: both $13,444M) and swings from 14.35% to 32.96% to 32.56% quarter-to-quarter — clear confirmation this vendor figure is not a real, independent gross-margin concept for Berkshire but is instead tracking whatever residual (including investment-gains noise) the vendor's template assigns to that line. Using the most recently **completed fiscal year's** figure (FY2025, the same convention this framework already uses for the annual CAGR and FCF/NI checks) avoids compounding that quarter-to-quarter artifact into the score. No structural-trend bonus applied — same reasoning as 2026-07-15 (segment-mix shift, not a documented single mechanism).

### 2c. Growth (20% weight)

```
Revenue 3yr CAGR (FY2025 $371,444M / FY2022 $302,089M) = 7.13%
Growth_Score = clamp((7.13/25)×100, 0, 100) = 28.52
```

Unchanged — FY2025 remains the most recently completed fiscal year (FY2026 doesn't close until 2026-12-31), so the 3-year annual CAGR window is identical to the 2026-07-15 session.

**TAM/pricing-power modifier: declined, same reasoning as before.** Fresh Q2 2026 segment evidence (Berkshire's own press release, page 2) shows real operating-earnings growth — Manufacturing/service/retailing +24%, BHE +27%, BNSF +6% YoY — but this is *segment operating-earnings growth*, not documented evidence of TAM expansion or pricing power at the whole-conglomerate level the modifier requires, and it's concentrated in specific segments rather than company-wide. **No −10 structural-deceleration modifier either**: total revenue continues growing (TTM $384.7B vs. FY2025 $371.4B), so GEICO's Q2 2026 underwriting deterioration (Section 2e) is a segment-specific profitability issue, not documented company-wide revenue deceleration.

### 2d. Balance Sheet (15% weight)

```
Total Debt (Q2 2026, 2026-06-30)        = $128,599M      (stockanalysis.com, vendor-sourced)
TTM D&A = $13,476M (FY2025) − $6,594M (H1 2025, SEC XBRL) + $7,116M (H1 2026, SEC XBRL) = $13,998M
```

**EBIT sourcing caveat — the same unresolved gap as 2026-07-15, now further confirmed.** Berkshire still reports no discrete "OperatingIncomeLoss" XBRL concept, and this session's fresh check of stockanalysis.com's quarterly financials page found its "Operating Income" line is **literally identical to its "Gross Profit" line in every quarter shown** (Section 2b) — reinforcing, rather than resolving, last session's flag that this vendor's BRK EBIT figure is internally inconsistent and not usable as a precise input. **Net Debt/EBITDA is therefore computed both ways again, using two different EBIT bases so each reading stays internally consistent within its own period:**

```
(a) Broad reading — combined cash + short-term (T-Bill) investments, per Berkshire's own Q2 2026
    disclosure ("cash pile... $365.5 billion at the end of June," widely reported and consistent with
    stockanalysis.com's combined cash+ST-investments figure of $365,514M):
    Net Debt = 128,599 − 365,514 ≈ −$236,915M   (a NET CASH position)
    → Net Debt/EBITDA negative regardless of the exact EBIT figure used → BalanceSheet_Score clamps to 100.0
    (Robust to the EBIT ambiguity above: as long as EBITDA is positive — trivially true for Berkshire —
    a $237B net cash position makes the ratio negative under any plausible EBIT figure.)

(b) Narrow reading — cash & equivalents only ($40,609M, Q2 2026, stockanalysis.com), using the
    FY2025 EBIT/EBITDA figures from the 2026-07-15 session (kept from the same period so the reading
    stays internally consistent, rather than mixing a FY2025 EBIT with a Q2 2026 debt figure from a
    different period is avoided by re-deriving Net Debt at today's balance-sheet date but holding
    EBITDA at its most recently fully-reported annual value):
    Net Debt = 128,599 − 40,609 = $87,990M
    EBITDA (FY2025) = $58,040M (vendor EBIT) + $13,476M (FY2025 D&A) = $71,516M
    Net Debt/EBITDA = 87,990 / 71,516 = 1.23×
    BalanceSheet_Score = clamp(100 × (1 − 1.23/4), 0, 100) = 69.25
```

**Broad reading (100.0) used as primary**, same justification as 2026-07-15 — T-Bills are functionally cash-equivalent and Berkshire's own disclosure already presents them as one combined liquidity figure. **Narrow reading (69.25) shown as the conservative alternative.** Either way, not the swing factor in this session's outcome (Section 2h).

**Conglomerate rule check:** Total Debt is Berkshire's fully consolidated figure, already including wholly-owned BNSF's and BHE's own reported debt — no further adjustment needed (unchanged from 2026-07-15).

### 2e. Moat Signal (15% weight)

| Signal | Evidence | Result |
|---|---|---|
| Market share stable/growing | GEICO ~18% US auto-insurance share (unchanged citation); BNSF/Union Pacific Western-US rail duopoly (unchanged, structural). **New, countervailing evidence this session:** GEICO's Q2 2026 combined ratio worsened 7.7 points to 91.2% (losses/LAE ratio +4.8pp to 76.6%, driven by rising claims frequency/severity), and GEICO's own expenses rose 27.3% YoY explicitly to "reignite policy growth" (per multiple independent Q2 2026 earnings reports) — language suggesting growth has been sluggish enough to warrant a deliberate marketing push, not a company claiming effortless share gains this quarter. No specific premiums-written or share-count decline was sourced this session, so the signal is not flipped to FALSE, but this is flagged as a real, documented headwind, not silently omitted. | ✅ TRUE (flagged) |
| Brand premium | See's Candies sustained pricing power (unchanged citation, 2026-07-15) | ✅ TRUE |
| Network effect | No documented two-sided-marketplace mechanism identified (unchanged) | ❌ not established |
| Switching costs | BNSF rail-shipper physical-infrastructure lock-in (unchanged) | ✅ TRUE |
| Scale cost advantage | No cost-per-unit citation vs. named competitors sourced this session; GEICO's own +27.3% expense growth to compete for volume this quarter is, if anything, mild evidence *against* an unassailable low-cost-acquisition advantage right now | ❌ not established |

```
Moat_Score = (3/5) × 100 = 60.0   (unchanged from 2026-07-15, with the GEICO underwriting deterioration
                                    newly documented as a headwind worth tracking, not yet enough to flip a signal)
```

### 2f. FCF Quality (10% weight) & the growth-capex hard-disqualifier question

Unchanged from 2026-07-15 — these are fixed historical annual figures, and FY2025 remains the most recently completed fiscal year (the "rolling window" the 2026-08-05 clarification in quality-scoring.md points to has not rolled forward, since FY2026 isn't complete):

```
FY2021 FCF/NI = 29.08%   FY2022 FCF/NI = negative NI   FY2023 FCF/NI = 30.96%
FY2024 FCF/NI = 13.05%   FY2025 FCF/NI = 37.40%

FCFQuality_Score (primary, FY2025 GAAP-NI basis) = clamp(((0.374−0.40)/0.60)×100, 0, 100) = 0.0  (clamped)
```

**Hard disqualifier check — "FCF/NI conversion <70% for 2+ consecutive years without a documented growth-capex explanation":** literal ratio below 70% every year of the 5-year window. **Resolution unchanged: treated as NOT firing**, on the same two grounds as 2026-07-15 — (1) documented, ongoing growth capex (BHE's $33.3B 2026–2028 plan; consolidated quarterly capex running $5.0–$5.6B in Q1–Q2 2026 per stockanalysis.com, consistent with continued elevated growth-driven spend, not a one-off), and (2) the same GAAP-investment-gains/losses distortion on the NI denominator documented in Section 2a. **This remains moot for the outcome below** — the weighted score fails the gate independent of this judgment call, same as 2026-07-15.

### 2g. Full Quality Score — primary computation

```
Quality Score = (Profitability×0.25) + (Margins×0.15) + (Growth×0.20) + (BalanceSheet×0.15) + (Moat×0.15) + (FCFQuality×0.10)

              = (57.36×0.25) + (36.91×0.15) + (28.52×0.20) + (100.0×0.15) + (60.0×0.15) + (0.0×0.10)
              = 14.34 + 5.5365 + 5.704 + 15.00 + 9.00 + 0.00
              = 49.58 → 49.6
```

### 2h. Range across every tested ambiguity (robustness check, not a search for 80.0)

**Conservative** (narrow-cash Balance Sheet reading, 69.25 instead of 100.0):
```
49.58 − (100.0 − 69.25)×0.15 = 49.58 − 4.6125 = 44.97 → 45.0
```

**Illustrative ceiling** (every ambiguous input resolved at its single most generous reading simultaneously — higher of the two Profitability bases [GAAP TTM, 57.36, is already the higher one this period]; +10 Margins structural bonus; +10 Growth TAM modifier; broad-cash Balance Sheet; a 4th Moat signal credited; Op-Earnings-basis FCF Quality):
```
(57.36×0.25) + (46.91×0.15) + (38.52×0.20) + (100.0×0.15) + (80.0×0.15) + (27.17×0.10)
= 14.34 + 7.0365 + 7.704 + 15.00 + 12.00 + 2.717
= 58.80
```

**The full range this session is 45.0–58.8, primary 49.6 — 21+ points below the 80.0 gate even at the single most generous reading of every ambiguous input simultaneously.** This is a wider, more decisive margin than the AXP (2026-07-19, ceiling 80.5, genuinely straddled the gate) or SCHW (2026-07-19, ceiling 75.96, a near-miss) sessions — Berkshire's Quality Score gap to 80.0 is not close under any tested reading, consistent with the 2026-07-15 finding (range 43.4–56.7, primary 47.5). The modest uptick this session (49.6 vs. 47.5 primary; 58.8 vs. 56.7 ceiling) traces almost entirely to Section 2a's large Q2 2026 non-cash investment gain lifting the TTM GAAP Profitability reading — not to any change in the underlying operating businesses.

### Gate Result: ❌ **FAIL** (decisive, not indeterminate)

- Primary computed Quality Score: **49.6** (range 45.0–58.8 across every tested ambiguity).
- Unlike the AXP session (where a genuinely un-resolvable ~1.5-point band straddled the 80.0 gate and the session stopped without a score), **this result is decisive**: even the single most generous possible resolution of every judgment call lands over 21 points short of 80.0. There is no version of this data that clears the gate.
- The hard-disqualifier question (Section 2f) is treated as not firing, but remains moot — the weighted score fails independent of that judgment call.
- Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), **this evaluation stops here — no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.**

---

## 3. Why this reads as confirmation of a known framework-calibration gap, not new information about Berkshire

This session reaches the same substantive conclusion as 2026-07-15 for the same reason: this framework's Profitability/Growth/Margins sub-scores are calibrated with ceilings (30% ROIC/margin, 25% revenue CAGR, 80% gross margin) built for high-growth, high-margin, capital-efficient businesses — a profile a ~$1.06T market-cap, mature, deliberately conservative insurance-float-funded conglomerate structurally cannot fit, regardless of how genuinely high-quality Buffett/Munger/Abel's capital allocation has been by this framework's own philosophical influences (see [investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)). Nothing in Berkshire's Q2 2026 results changes that picture — if anything, this session's fresh data illustrates the exact GAAP-investment-gains volatility flagged last time even more sharply (a single quarter's $12.68B non-cash gain moved the primary Profitability sub-score by nearly 9 points). This remains a **candidate framework-calibration gap** worth a future `decisions/` discussion (as flagged on 2026-07-15) — not resolved or re-litigated within this session, consistent with how repeat sessions on JPM/Citigroup/SOFI-class names have handled the same unresolved gap without unilaterally patching quality-scoring.md each time.

---

## 4. Additional context (not scored — informational only, since Phase 02 was not run)

- **Q2 2026 headline results** (Berkshire's own press release, 2026-08-08): net earnings attributable to shareholders $25,667M (vs. $12,370M Q2 2025), driven by $12,684M of investment gains (mostly non-cash, ASU 2016-01 mark-to-market); operating earnings $12,983M (vs. $11,160M Q2 2025, +16.3%).
- **Segment operating earnings, Q2 2026 vs. Q2 2025** (company-disclosed): Insurance-underwriting $1,731M (down from $1,992M, −13.1%); Insurance-investment income $3,059M (down from $3,367M, −9.1%); BNSF $1,558M (up from $1,466M, +6.3%); BHE $891M (up from $702M, +26.9%); Manufacturing/service/retailing $4,470M (up from $3,601M, +24.1%).
- **GEICO underwriting deterioration** (independently reported, not Berkshire's own press release, which doesn't break out GEICO specifically): pre-tax underwriting income −45.4% YoY to $994M; combined ratio 91.2% (+7.7pp); expenses +27.3% YoY on higher commissions/advertising "to reignite policy growth"; no significant catastrophe losses cited — the deterioration is attributed to claims frequency/severity and competitive/expense dynamics, not a one-off event. [The Insurer](https://www.theinsurer.com/ti/news/berkshire-hathaway-pre-tax-underwriting-earnings-fall-14-to-218-billion-in-q2-2026-08-08/), [Forbes](https://www.forbes.com/sites/maryroeloffs/2026/08/10/geico-earnings-plummet-45-in-hit-to-berkshire-hathaways-insurance-business/)
- **Capital allocation under CEO Greg Abel:** ~$4.5B in buybacks in Q2 2026 alone (~$4.8B for H1 2026) — a sharp acceleration from $235M in Q1 2026; per third-party reporting, Berkshire also swung to net equity purchases (~$20B) in Q2 2026 after 14 consecutive quarters of net selling. Cash + short-term investments fell from a record $397.4B (Q1 2026) to $365.5B (Q2 2026) as this capital was deployed. Insurance float ~$177.5B at 2026-06-30 (+$1.1B since 2025-12-31).
- **Trump BRK.B purchase** (Section 0): confirmed real, immaterial to fundamentals, not used in any calculation above.

---

## 5. Data sourcing note

SEC EDGAR XBRL `companyconcept` API (CIK 0001067983) for all officially filed figures (Revenues, NetIncomeLoss, StockholdersEquity, DepreciationDepletionAndAmortization — pulled directly from Berkshire's 10-K/10-Q tags); Berkshire's own Q2 2026 earnings press release (PDF, read directly via the PDF reader, not summarized secondhand) for the operating-earnings/segment breakdown; stockanalysis.com (WebFetch) for the handful of figures Berkshire doesn't file as a discrete XBRL concept (Total Debt, cash/short-term-investments breakdown, vendor "EBIT"/"Gross Profit" — the latter explicitly re-flagged this session as internally inconsistent, Section 2b/2d); WebSearch/independent reporting for GEICO's Q2 2026 combined-ratio detail (not in Berkshire's own press release) and the Trump-purchase fact-check (Section 0). IBKR `get_price_snapshot` and `search_contracts` (Rule 0 live price) worked normally. `yfinance` not attempted (recurring environment failures, documented across this repo's recent sessions). Every figure above is cited to its specific source; none is invented or estimated.

---

## 6. Recommendation: **PASS**

**The Phase 01 Quality Score gate fails, decisively.** Primary computed Quality Score **49.6** (range 45.0–58.8 across every tested reading), more than 21 points short of the 80.0 threshold even in the single most generous case. Per [.claude/commands/new-position.md](../.claude/commands/new-position.md), the evaluation stops here — **no Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work was performed.** This is not a genuinely indeterminate result (contrast the 2026-07-19 AXP session) — no plausible resolution of any ambiguous input gets this company near the gate.

This confirms, rather than revises, the 2026-07-15 finding on the same ticker: the previously-flagged framework-calibration gap for mega-cap, mature, insurance-float-funded conglomerates (Section 3) persists, and this session's modestly higher score (49.6 vs. 47.5) is fully explained by one quarter's large non-cash investment gain, not by any change in the operating businesses. **Not a BUY/TRIM/EXIT outcome** — no position exists or is proposed.

---

## 7. Watchlist entry

Updated (not newly created — a prior entry exists) at [watchlist/not-in-portfolio/BRK/BRK-2026-08-23.md](../watchlist/not-in-portfolio/BRK/BRK-2026-08-23.md) — a new dated row was added because the numeric score changed (47.5 → 49.6), per [watchlist/README.md](../watchlist/README.md)'s "significant change" criteria, even though the action category (PASS / not held) is unchanged.

---

## Glossary

| Term | Meaning |
|---|---|
| **ASU 2016-01** | The US GAAP accounting rule (effective 2018) requiring unrealized equity-security gains/losses through net income every period — the reason Berkshire's GAAP earnings swing sharply with stock-market moves (e.g. Q2 2026's $12.68B investment gain, $10.9B of it purely from unrealized mark-to-market) even when operating businesses perform consistently. |
| **BHE (Berkshire Hathaway Energy)** | Berkshire's regulated utility/energy subsidiary — one of its core operating segments. |
| **BNSF** | Burlington Northern Santa Fe, Berkshire's wholly-owned Class I freight railroad — one of only two major Western-US Class I railroads (with Union Pacific), a structural near-duopoly. |
| **CAGR** | Compound Annual Growth Rate. |
| **Combined ratio** | An insurer's loss ratio plus expense ratio; below 100% = underwriting profit. GEICO's Q2 2026 combined ratio was 91.2% (up 7.7pp YoY) — still an underwriting profit, but a real deterioration. |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization; flagged again this session as not cleanly filed by Berkshire, with a vendor-derived approximation shown this session to be internally inconsistent with the same vendor's own "Gross Profit" line. |
| **Float (insurance float)** | Policyholder premiums held before claims are paid, investable in the meantime — $177.5B at 2026-06-30. |
| **GAAP** | Generally Accepted Accounting Principles. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score — see [quality-scoring.md](../framework/quality-scoring.md). |
| **Moat** | A durable competitive advantage protecting a business's profits from competitors. |
| **Operating earnings (Berkshire)** | Berkshire's own non-GAAP profitability measure excluding investment/derivative gains and losses — the figure the company asks investors to focus on instead of GAAP net earnings. |
| **Quality Score** | This framework's 0.0–100.0 continuous score; 80.0+ required to proceed to valuation scoring. Berkshire's range this session: 45.0–58.8, primary 49.6 — a decisive FAIL. |
| **ROE** | Return on Equity — Net Income ÷ shareholder equity; used here as a proxy for ROIC. |
| **ROIC** | Return on Invested Capital. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work. |
| **Rule 9** | This framework's list of fundamental events forcing an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. Berkshire's Q2 2026 earnings (filed 2026-08-08) is the Rule 9 event underlying this session. |
| **T-Bills (Treasury Bills)** | Short-maturity US government debt, effectively cash-equivalent — part of Berkshire's ~$365.5B combined cash + short-term-investments position at 2026-06-30. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — this session used Jul 2025–Jun 2026 (FY2025 minus H1 2025 plus H1 2026). |
| **XBRL** | eXtensible Business Reporting Language — the SEC's structured filing-data format, allowing exact figures to be pulled directly from official filings. |
