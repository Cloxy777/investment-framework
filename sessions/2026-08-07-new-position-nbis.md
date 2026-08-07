# New Position Evaluation — NBIS (Nebius Group N.V., NASDAQ)

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — fully automated, no human in loop)
**Date:** 2026-08-07
**10Y US Treasury Yield:** 4.63% (FRED `DGS10`, most recent posted observation as of this session, dated 2026-08-05 — normal FRED reporting lag; fetched directly via `fredgraph.csv?id=DGS10`)
**Rate Regime Modifier:** N/A this session — Phase 02 is never reached (see §3.4). For reference only, the bracket in force would be **+5** (10Y in the 3.5–5% range), per [strategy.md](../framework/strategy.md).
**Current NBIS portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md)).
**Prior coverage:** None — first-ever evaluation of this ticker. No entry existed in either [watchlist/in-portfolio/](../watchlist/in-portfolio/) or [watchlist/not-in-portfolio/](../watchlist/not-in-portfolio/) before this session.
**Sector:** Communication Services / classified by data vendor as "Internet Content & Information," but operationally an AI cloud-infrastructure provider (GPU compute, data centers) — evaluated here on its full consolidated financials as reported.
**Corporate background (context only, not a scored input):** The entity trading as NBIS is the continuation of Yandex N.V. following its 2024 sale of Yandex's Russian operating businesses; the remaining international entity retained the AI-infrastructure/cloud business and was renamed Nebius Group N.V. This is well-documented public corporate history, cited here only to explain the FY2021→FY2022 revenue collapse visible in §3.1 (from ~$4.76B to ~$13.5M) — it is **not** used as a scored Growth or Moat input, consistent with Rule 6 ("normalize before you value" / adjust for divestitures).
**First-use jargon decode:** see closing Glossary (§8).

---

## 0. Why this session exists — trigger source

Telegram channel **tarasguk**, post **tarasguk/11622** (~06:49 UTC, 2026-08-07): *"🤗 Майкл Баррі шортить Яндекс $NBIS. Наш козак 💪"* ("Michael Burry is shorting Yandex $NBIS. Our guy 💪").

**Per Rule 0, this post's claim is never used as financial data or as evidence of anything** — it is only the reason this ticker was looked at. The post names ticker `$NBIS` explicitly (removing any ticker-resolution ambiguity per [telegram-scan.md](../.claude/commands/telegram-scan.md) step 3), and no watchlist entry existed for NBIS in either `in-portfolio/` or `not-in-portfolio/` — per that command's step 4 decision tree, "No watchlist entry exists at all → `/new-position <TICKER>`" fires unconditionally, independent of whatever the post claims. The "Michael Burry short" claim itself was **not independently verified** and is not relied on anywhere below; every figure in this session is sourced directly from stockanalysis.com's financial statements (cross-checked against the page's own raw HTML, §2) and Interactive Brokers live pricing.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive Brokers MCP tools, before any other work. **NASDAQ:NBIS, contract_id 88819736** (confirmed via `search_contracts` — the primary US listing "NEBIUS GROUP NV," distinct from `NBISN` (Mexico BDR), `NEBX`/`NBIG`/`NBIZ`/`NBIC` (2x/short leveraged ETF products tracking the same ticker root), and `3NBI`/`NBI3` (London/Amsterdam leveraged ETPs)).

| Field | Value | Detail |
|---|---|---|
| **Last trade** | **$196.88** | Live intraday print (not a stale/inferred price), as of 2026-08-07 08:12:26 UTC. |
| Change (intraday) | +$7.00 / **+3.69%** | Not scored as evidence — price action alone is never a Rule 9 trigger per CLAUDE.md. |
| YTD change | +$113.18 / **+135.21%** | |
| 52-week high | $299.86 | |
| 52-week low | $62.01 | |
| 13-week / 26-week high | $299.86 | |

**Live price used throughout this session: $196.88.**

---

## 2. Data Source Note

Same environment constraint documented in prior sessions (e.g. 2026-07-19/07-23 TSLA): `yfinance`'s `curl_cffi` backend fails through this session's proxy (`SSLError: Recv failure: Connection reset by peer`) even though plain `curl` through the same proxy succeeds — confirmed by testing both this session. Fundamentals were sourced via `WebFetch` against **stockanalysis.com**'s overview/financials/balance-sheet/cash-flow/ratios pages, then **independently cross-checked against the pages' own raw HTML** (fetched directly via `curl` and parsed) rather than relying on the `WebFetch` tool's AI-generated summary alone — this caught a real discrepancy (§7). The 10-Year Treasury yield was sourced directly from FRED's public CSV endpoint. No required input was invented or estimated; every figure below is cited to its source and, where flagged, to the specific cross-check performed.

---

## 3. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29)

### 3.1 Raw financial inputs (all sourced, cited)

**TTM (trailing twelve months, period ended ~2026-03-31):**

| Metric | Value | Source |
|---|---|---|
| Revenue | $877.9M | [stockanalysis.com/stocks/NBIS/financials](https://stockanalysis.com/stocks/NBIS/financials/), independently confirmed against the page's raw HTML |
| Gross Profit | $632.6M | same |
| Gross Margin | 72.06% | same (raw HTML confirms 632.6/877.9 = 72.06%, matches displayed figure) |
| Operating Income | −$603.9M | same, raw-HTML confirmed |
| Operating Margin | −68.79% | same (raw HTML confirms −603.9/877.9 = −68.79%, matches displayed figure) |
| Net Income | $836.4M | same, raw-HTML confirmed |
| Net Margin (computed) | **95.27%** | Computed directly as Net Income ÷ Revenue = 836.4/877.9, both raw-HTML-confirmed figures from the same table row-index. See §7 — the site's own displayed "Profit Margin" TTM figure (76.61%) does **not** reconcile to these same two cited numbers; flagged as a data-quality gap, computed figure used instead since it's directly reconcilable. |
| ROIC (TTM) | **−9.15%** | [.../financials/ratios](https://stockanalysis.com/stocks/NBIS/financials/ratios/) "Return on Invested Capital (ROIC)" row, raw-HTML confirmed |
| Operating Cash Flow (TTM) | $2,840M | [.../cash-flow-statement](https://stockanalysis.com/stocks/NBIS/financials/cash-flow-statement/), raw-HTML confirmed |
| CapEx (TTM) | −$5,995M | same, raw-HTML confirmed |
| Free Cash Flow (TTM) | **−$3,155M** (= 2,840 − 5,995) | same |

**Annual figures (fiscal years, for the 3+/2+ consecutive-year hard-disqualifier tests and 3yr CAGR):**

| FY | Revenue | Net Income | Operating CF | CapEx | FCF |
|---|---|---|---|---|---|
| FY2025 | $529.8M | $82.5M | $384.8M | −$4,066M | **−$3,681.2M** |
| FY2024 | $91.5M | −$641.4M | $245.6M | −$807.5M | **−$561.9M** |
| FY2023 | $9.8M | $241.3M | $829.8M | −$82.9M | **+$746.9M** |
| FY2022 | $13.5M | $745.6M | $697M | −$14.6M | +$682.4M |
| FY2021 | $4,762M | −$196.13M | $124.25M | −$596.6M | −$472.35M |

**Balance sheet (TTM, most recent quarter ~2026-03-31):** Total Debt $9,496M, Cash & Equivalents $9,298M, Total Shareholders' Equity $7,242M → **Net Debt = 9,496 − 9,298 = +$198M** (net debt position, not net cash). **Net Debt/EBITDA (TTM, as reported) = 5.41×.** Source: [.../balance-sheet](https://stockanalysis.com/stocks/NBIS/financials/balance-sheet/) and [.../ratios](https://stockanalysis.com/stocks/NBIS/financials/ratios/), both raw-HTML confirmed.

### 3.2 Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | NBIS data | Verdict |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | Rolling-window test (per [quality-scoring.md](../framework/quality-scoring.md)'s 2026-08-05 clarification) on the most recently completed fiscal years: FY2023 **positive** (+$746.9M), FY2024 **negative** (−$561.9M), FY2025 **negative** (−$3,681.2M). Not uniformly positive. | **FIRES.** |
| **Net Debt/EBITDA over threshold (2.5× standard)** | 5.41× (TTM, as reported) — more than double the 2.5× standard threshold. NBIS is a capital-intensive AI-infrastructure/data-center operator, not a payment network, exchange, or asset-light financial, so the Upgrade 5 asset-light override (4× threshold) does not apply — and 5.41× would exceed even that threshold. | **FIRES.** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | TTM FCF/NI = −3,155/836.4 = **−377%**; FY2025 = −3,681.2/82.5 = **−4,462%**; FY2024 NI itself is negative (−$641.4M), making the ratio not meaningful in the conventional sense. All are far below the 70% bar. A documented growth-capex explanation *is* available and citable — TTM CapEx (−$5,995M) is a >7× jump over FY2024 CapEx (−$807.5M), consistent with a large AI data-center/GPU buildout — which could arguably exempt this specific disqualifier from firing. **Not resolved either way**, since it's moot: the two disqualifiers above already fail the company independently. | **Moot — not resolved.** |

**Two independent hard disqualifiers fire.** Per [quality-scoring.md](../framework/quality-scoring.md): "a weighted average can't average away an outright balance-sheet or cash-flow-quality failure." Proceeding to the full weighted score below anyway, for transparency (no black-box outputs) — it is not needed to reach the conclusion.

### 3.3 Sub-score calculation

| Sub-score (weight) | Formula & inputs | Result |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((95.27/30)×100, 0, 100) = **100.0**. ROIC_Component = clamp((−9.15/30)×100, 0, 100) = **0.0** (negative ROIC clamps to floor). Raw Profitability_Score = (100.0+0.0)/2 = 50.0. **Not FCF-positive for 3+ consecutive years (§3.2) → capped at 40.0** per the formula's explicit rule ("sustained quality requires sustained cash generation, not just accounting profitability") — directly on point here, since the 95.27% net margin is inflated by a large **non-operating gain** (Operating Income is deeply negative at −68.79% margin; see Glossary). | **40.0** |
| **Margins (15%)** | GrossMargin_Score = clamp((72.06/80)×100, 0, 100) = **90.08**. Gross margin is already well above the 40% threshold (and has been improving: 52.24% FY2024 → 68.63% FY2025 → 72.06% TTM), so the "+10 below-40%-but-expanding" bonus doesn't apply (it's specifically for sub-40% gross margins). No modifier applied. | **90.08** |
| **Growth (20%)** | Revenue 3yr CAGR (FY2022 $13.5M → FY2025 $529.8M) = (529.8/13.5)^(1/3) − 1 = **+239.8%/yr**. **Flagged as distorted**, not organic like-for-like growth: FY2022 sits right after the 2024 Yandex-Russia divestiture rebased the company to a near-zero revenue floor (§ header), so this CAGR reflects rebuild-from-almost-nothing arithmetic, not a comparable operating trend (Rule 6, "normalize before you value"). Mechanically, Growth_Score = clamp((239.8/25)×100, 0, 100) = **100.0** (far past the 25% cap regardless of the distortion). No TAM-expansion/pricing-power modifier applied — no citation gathered this session (see §7) — and no structural-deceleration modifier applies (growth is accelerating, not decelerating, on this base). | **100.0** (flagged) |
| **Balance Sheet (15%)** | Net Debt/EBITDA = 5.41× (TTM, as reported) → clamp(100×(1 − 5.41/4), 0, 100) = clamp(100×(1−1.3525), 0, 100) = clamp(−35.25, 0, 100) = **0.0**. | **0.0** |
| **Moat Signal (15%)** | **Not researched this session.** Two independent hard disqualifiers (§3.2) already fail the Phase 01 gate regardless of this sub-score, so the qualitative moat-evidence research (Rule 5's "5 Qualitative Questions," citation-per-signal) was not performed, to avoid spending unattended-run time/tokens on a sub-score that cannot change the outcome. Per the rule ("never mark a signal true without a cited source"), zero cited signals → **0.0** by the formula's own mechanics, not a substantive claim that NBIS lacks a moat. **This is a genuine data gap, not a scored finding — flagged explicitly (§7) and should be filled in on any future re-evaluation of this ticker** (e.g. if a subsequent Rule 9 trigger materially changes the FCF/leverage picture enough to warrant revisiting the gate). | **0.0** (unresearched — flagged) |
| **FCF Quality (10%)** | FCF/NI (TTM) = −3,155/836.4 = **−377.3%** → clamp(((−3.773−0.40)/0.60)×100, 0, 100) = clamp(−695.5, 0, 100) = **0.0**. | **0.0** |

### 3.4 Final weighted Quality Score

```
Quality Score = (40.0 × 0.25) + (90.08 × 0.15) + (100.0 × 0.20) + (0.0 × 0.15) + (0.0 × 0.15) + (0.0 × 0.10)
              = 10.0 + 13.512 + 20.0 + 0.0 + 0.0 + 0.0
              = 43.512 → 43.5 (rounded to nearest 0.1)
```

**43.5 < 80.0 — fails the gate by 36.5 points**, and independently, **two hard disqualifiers fire** (§3.2: FCF not positive for 3 consecutive years; Net Debt/EBITDA 5.41× vs. 2.5× threshold). Either finding alone is sufficient to fail Phase 01.

### Result: **Phase 01 FAIL — weighted Quality Score 43.5, misses the 80.0+ gate by 36.5 points. Two hard disqualifiers also fire independently.**

Per [new-position.md](../.claude/commands/new-position.md) step 2: stop here rather than proceeding to scoring. **No Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work were computed.**

---

## 4. Recommendation

**PASS.** Do not open a position, and do not place a limit order. Nebius Group's TTM figures show a company still deep in an AI-infrastructure capital buildout (Operating Margin −68.79%, CapEx up more than 7× year-over-year, negative free cash flow in the two most recently completed fiscal years and on a TTM basis) — a profile the framework's Quality Score deliberately penalizes via its FCF-positivity and leverage hard disqualifiers, regardless of the eye-catching headline net income and revenue-growth figures, both of which are themselves distorted by, respectively, a large non-operating gain (net income) and a post-divestiture near-zero comparison base (revenue CAGR). The Telegram post's "Michael Burry short" claim was never independently verified and played no role in this conclusion either way — this is a verdict about the framework's strict quantitative quality bar applied to the audited financials as reported, not a comment on the short-rumor itself or on the AI-infrastructure buildout's long-run prospects.

---

## 5. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 6. Next Review Trigger

No routine re-check scheduled (Phase 01 FAIL, no numeric Phase 02 score to go stale). Re-evaluate on any of the following Rule 9-style fundamental triggers: (a) a sustained shift to positive free cash flow over 2+ consecutive quarters (the current buildout is the direct cause of the FCF-positivity disqualifier); (b) a credible deleveraging path bringing Net Debt/EBITDA back under 2.5×; (c) the next quarterly earnings release (Q2 2026 results are scheduled for **2026-08-12**, per stockanalysis.com) or a guidance revision; (d) a management change or material M&A/strategic-investment event; (e) a >15% stock-price move with no identified cause (today's +3.69% intraday move does not qualify). If a future session reaches this gate again, **the Moat Signal sub-score (§3.3) still needs its qualitative research performed** — it was left unresearched this session since it couldn't change the outcome. Absent any of the above, future Telegram mentions of NBIS should be logged as "last checked, no change" rather than triggering a full re-evaluation each time.

---

## 7. Data gaps flagged (Rule 0)

- **`yfinance` unusable this session** — same `curl_cffi`/proxy `SSLError` as prior sessions, confirmed again this session even though plain `curl` through the identical proxy succeeded. Worked around via `WebFetch` against stockanalysis.com, cross-checked against the same pages' raw HTML (fetched directly via `curl`) rather than trusting the `WebFetch` summary alone.
- **Net Margin discrepancy (material to catch, immaterial to the outcome):** `WebFetch`'s AI-generated summary of the stockanalysis.com financials page reported TTM "Profit Margin" as 76.61% — this figure genuinely appears in the page's raw HTML (not a `WebFetch` hallucination), but does **not** reconcile with the same table's own cited Net Income ($836.4M) ÷ Revenue ($877.9M) = 95.27%, both of which independently reconcile against Gross Margin and Operating Margin at the same row-index (§3.1). Used the directly-reconcilable 95.27% figure for scoring. Immaterial to the outcome either way, since the Profitability sub-score is capped at 40.0 by the FCF-positivity hard disqualifier regardless of which margin figure is used.
- **Moat Signal (§3.3) not researched this session** — a genuine data gap, not a finding. Two independent hard disqualifiers already fail Phase 01, so the qualitative moat-evidence work (5 signals, cited sources) was skipped to conserve unattended-run resources. Should be filled in on any future re-evaluation that reaches this gate again.
- **EBITDA** not independently derived from a primary filing this session — used the Net Debt/EBITDA ratio (5.41×) as directly reported by stockanalysis.com's ratios page rather than re-deriving it from EBITDA and Net Debt separately; not needed for the conclusion since 5.41× unambiguously exceeds the 2.5×/4× thresholds either way.
- **"Michael Burry shorting NBIS" claim (the Telegram post's own content):** not independently verified, and not used as evidence anywhere in this session, consistent with Rule 0 — cited only as the reason this ticker was looked at (§0).

---

## 8. Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. NBIS's headline 3yr CAGR (+239.8%/yr) is flagged as distorted by a near-zero comparison base, not treated as a clean organic-growth signal.
- **CapEx** — Capital Expenditure — money a business spends on physical or capitalized long-lived assets. NBIS's TTM CapEx (−$5,995M) is more than 7× its FY2024 level, reflecting an AI data-center/GPU buildout.
- **Composite Score** — This framework's single ranking number (0.0–100.0) blending the Quality Score and Valuation Score 50/50 — not computed for NBIS since it never clears the 80.0+ Quality Score gate.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. Negative for NBIS in the two most recently completed fiscal years (FY2024, FY2025) and on a TTM basis.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. Deeply negative for NBIS (TTM −377%), since FCF is negative while Net Income is positive (driven by a non-operating gain, not operating cash generation).
- **Gross Margin** — Gross Profit ÷ Revenue — the percentage of each revenue dollar left after direct production/delivery costs. NBIS's TTM figure is 72.06%, and has been expanding.
- **Hard disqualifier** — One of three Quality Score conditions that fails a company regardless of its weighted score. Two fire for NBIS this session: not FCF-positive for 3+ consecutive years, and Net Debt/EBITDA over its 2.5× threshold.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; NBIS carries a net debt position (not net cash) at a reported 5.41× ratio, more than double this framework's standard 2.5× threshold.
- **Net Margin** — Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax. NBIS's computed TTM figure (95.27%) is inflated by a large non-operating gain — see the **Non-operating gain/loss** and **Operating Margin** entries below.
- **Non-operating gain/loss** — Income-statement items below Operating Income (investment gains/losses, interest income/expense, fair-value remeasurement, one-off disposal gains) that aren't part of a company's core, repeatable operating business. NBIS's TTM Net Income ($836.4M) is positive despite TTM Operating Income being deeply negative (−$603.9M) — a sign the reported "profit" isn't coming from the AI-infrastructure business actually running profitably yet.
- **Operating Margin** — Operating Income ÷ Revenue — the percentage of each revenue dollar left after operating expenses, before interest and taxes. NBIS's TTM figure is −68.79%, sharply negative despite a positive Net Margin — see **Non-operating gain/loss**.
- **Quality Score** — This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. NBIS scores **43.5** this session, its first evaluation.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it into profit. NBIS's TTM ROIC is **−9.15%** (negative — currently destroying, not creating, value on invested capital).
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 6** — This framework's fair-value-methodology instruction to normalize financial statements before valuing a business — strip out one-time items, adjust for M&A/divestitures, and value the underlying business rather than the raw accounting statements as reported. Applied here to flag (not silently use) NBIS's divestiture-distorted revenue CAGR and non-operating-gain-inflated Net Margin.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of financial data, rolling forward each quarter, as distinct from a fixed fiscal year.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
