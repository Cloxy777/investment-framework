# NEW POSITION — RKLB (Rocket Lab Corporation) — 2026-08-11

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6 — unattended run)
**Date:** 2026-08-11 (Tuesday)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (§3) before the Rate Environment Gate would otherwise apply, same precedent as the 2026-08-11 HIMS, 2026-08-07 NET, and 2026-08-10 KSPI sessions.
**Current RKLB portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None — first-ever `/new-position` evaluation of RKLB in this repo (confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`).
**Sector:** Industrials / Aerospace — Space launch services and satellite/spacecraft manufacturing ("Space Systems")
**Filer type:** US SEC filer, CIK 0001819994 ("Rocket Lab Corporation," formerly "Rocket Lab USA, Inc." — renamed per its FY2025 10-K), Delaware-incorporated, calendar fiscal year. Public since 25 August 2021 via SPAC merger (Vector Acquisition Corporation).
**IBKR contract used:** `contract_id` 787273575 — NASDAQ, symbol RKLB, description "ROCKET LAB CORP," `country_code` US, security type STK. Confirmed via `search_contracts` against several look-alike results (a Mexico-listed cross-listing, a Swiss CFD-style USD line, and three leveraged/inverse ETF products — RKLX, RKLZ, RKX — none of which are the underlying equity); the NASDAQ STK line is the correct primary listing.
**First-use jargon decode:** see closing Glossary (§9) — several new terms this session, added to [glossary.md](../framework/glossary.md) before being cited here.

---

## §0. Why this session exists — trigger source

**Trigger:** A Telegram post on `FinnInvestChannel` (post `FinnInvestChannel/3082`, ~16:04 UTC 2026-08-11) discussed Rocket Lab's Q2 2026 results, reportedly citing figures including revenue ~$234M, backlog ~$2.36B, EPS −$0.08, and a P/S ratio around 61.

**Per Rule 0 / CLAUDE.md, no figure from the Telegram post is used as financial data anywhere below — it is only the trigger.** Every number in this session is independently pulled from Rocket Lab's own SEC filings (the Q2 2026 10-Q, the FY2025 10-K, and the SEC's structured XBRL company-facts/company-concept API), and the live price is fetched fresh via IBKR, never inferred. As it happens, the independently-verified Q2 2026 GAAP figures (§2) turn out to closely match the Telegram post's claimed revenue ($234.066M), EPS (−$0.08), and backlog (~$2.356B) — but that similarity is a byproduct of this session's own independent SEC sourcing, not evidence used to justify skipping verification; the numbers below were pulled from the primary filing before any comparison was made.

| Telegram claim | Independent verification against primary SEC filing (Q2 2026 10-Q, filed 2026-08-10) |
|---|---|
| Q2 2026 revenue ~$234M | ✅ **Confirmed.** GAAP total revenue $234.066M (three months ended 2026-06-30), vs. $144.498M in Q2 2025 — **+62.0% YoY**. |
| Q2 2026 backlog ~$2.36B | ✅ **Confirmed.** Backlog $2,355.949M as of 2026-06-30, ~45% expected to convert to revenue within 12 months. |
| Q2 2026 EPS −$0.08 | ✅ **Confirmed.** Basic & diluted EPS −$0.08 for the three months ended 2026-06-30 (net loss $49.258M ÷ weighted-average 629.68M shares). |
| P/S ≈ 61 | ⚠️ **Not independently checked as a scored input.** A trailing P/S near that level is broadly consistent with a ~$47B market cap (598.18M shares × today's $78.82 live price ≈ $47.15B, §1) against TTM revenue of $769.146M (§3.2) — implied P/S ≈ 61.3× — but P/S is not a metric this framework scores anywhere in the Quality or Valuation engines, so it plays no role in the analysis below beyond this sanity note. |

**Net effect:** the trigger is real and well-corroborated — Rocket Lab did report Q2 2026 results on schedule (filed 2026-08-10), and the headline figures check out closely against the primary filing. This session proceeds on the confirmed Q2 2026 earnings release as the Rule 9 trigger, using only independently SEC-sourced figures throughout.

---

## §1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$78.82** | IBKR `get_price_snapshot`, `contract_id` 787273575, `last.price`, timestamp Unix 1786464661 = **2026-08-11 16:11:01 UTC** (regular NASDAQ session — market opened 13:30 UTC) |
| Bid / Ask | $78.71 / $78.82 | IBKR `bid_ask` |
| Change vs. prior close | −$1.22 (−1.52%) | IBKR `change` (`prior-close` field itself returned empty this snapshot — used the `change`-derived prior close instead, consistent with the vendor-quirk workaround used in the 2026-08-11 HIMS/2026-08-10 KSPI sessions) |
| 52-week range | $37.57 (low) – $151.00 (high) | IBKR `misc-statistics`. The 13-week, 26-week, and 52-week highs are all identical ($151.00) — the high was set within the trailing 13 weeks, i.e. recently. |
| Dividend yield | 0.0% | IBKR `dividend-yield` |
| Implied market cap (context only) | ≈$47.15B (598,180,438 common shares outstanding as of 2026-06-30, per Q2 2026 10-Q, × $78.82) | Derived, not a scored input |

**$78.82 is used as the live price for all context below.** Price is currently ~47.8% below the recent 52-week high and ~109.8% above the 52-week low — a large trading range, noted for context only (price action is never a scored input or an action trigger on its own, per Rule 0/operating-brief.md).

---

## §2. Data Sourcing

All figures below are sourced directly from SEC EDGAR: the Q2 2026 10-Q (CIK 1819994, accession `0001819994-26-000062`, filed 2026-08-10, covering the quarter and six months ended 2026-06-30), the FY2025 10-K (accession `0001819994-26-000013`, filed 2026-02-26), and the SEC's structured XBRL company-concept API (`data.sec.gov/api/xbrl/companyconcept/CIK0001819994/...`) for the multi-year annual series (FY2020–FY2025) used in the hard-disqualifier and 3-year-CAGR checks. Every dollar figure was independently pulled from a primary filing or the XBRL API — none carried over from, or cross-checked against, the Telegram trigger post.

**TTM window: Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026**, reconstructed as **FY2025 − H1 2025 + H1 2026** (the standard rolling-TTM technique used throughout this framework, e.g. the 2026-08-11 HIMS session), since Rocket Lab does not separately publish quarterly figures for Q3/Q4 2025 or Q1 2026 in a single source — the six-month (H1) and full-year (FY) figures below are the actual filed aggregates this reconstruction is built from.

### 2.1 Reconstructed TTM income statement ($M)

| | FY2025 | H1 2025 | H1 2026 | **TTM = FY2025 − H1 2025 + H1 2026** |
|---|---|---|---|---|
| Revenue | 601.799 | 267.067 | 434.414 | **769.146** |
| Gross Profit | 207.181 | 81.635 | 161.069 | **286.615** |
| Operating Income (Loss) | (228.838) | (118.827) | (113.483) | **(223.494)** |
| Net Income (Loss) | (198.209) | (127.030) | (94.280) | **(165.459)** |

```
TTM Gross Margin = 286.615 / 769.146 = 37.264%
TTM Net Margin   = -165.459 / 769.146 = -21.512%
```

### 2.2 Annual cash-flow series, FY2020–FY2025 (XBRL company-concept API, $M) — for the hard-disqualifier check

| Fiscal Year | Net Cash from Operating Activities | CapEx (Purchases of PP&E) | **FCF = OCF − CapEx** |
|---|---|---|---|
| 2020 | (27.757) | (25.121) | **(52.878)** |
| 2021 | (71.791) | (25.699) | **(97.490)** |
| 2022 | (106.538) | (42.412) | **(148.950)** |
| 2023 | (98.867) | (54.707) | **(153.574)** |
| 2024 | (48.890) | (67.093) | **(115.983)** |
| 2025 | (165.521) | (156.285) | **(321.806)** |
| H1 2026 (6mo, partial year, informational) | (134.407) | (53.112) | **(187.519)** |

**Every single fiscal year on record — all six full years since Rocket Lab began SEC reporting (FY2020 stub through FY2025), plus the first half of FY2026 — shows a decisively negative free cash flow.** Rocket Lab has never reported a single FCF-positive fiscal year. This is the central finding of this session (see §3.1).

### 2.3 Balance sheet, as of 2026-06-30 (Q2 2026 10-Q, $M)

| | Value |
|---|---|
| Cash and cash equivalents | 2,129.485 |
| Marketable securities (current) | 172.700 |
| Convertible senior notes, net | 13.129 |
| Long-term borrowings, net | 1.716 |
| **Total debt** | **14.845** |
| Total stockholders' equity | 3,492.153 |
| Common shares outstanding | 598,180,438 |

```
Net Debt = Total Debt - Cash - Marketable Securities = 14.845 - 2,129.485 - 172.700 = -2,287.340M  (net cash position)
```

Rocket Lab's balance sheet strengthened sharply in H1 2026: cash rose from $828.660M (2025-12-31) to $2,129.485M (2026-06-30), driven overwhelmingly by **$1,529.639M raised via At-The-Market (ATM) equity offerings** in the six months (financing-activities cash flow) — i.e. new share issuance, not operating cash generation. Two acquisitions closed in the period (Mynaric, $160.802M; Motiv, $44.539M), following the GEOST acquisition in August 2025.

### 2.4 Context (not scored inputs)

- **Backlog:** $2,355.949M as of 2026-06-30 (~45% expected to convert within 12 months) — a demand-visibility metric, not a scored Quality/Valuation input.
- **Customer concentration:** a single government customer represented 42% of total revenue for the six months ended 2026-06-30.
- **Neutron rocket:** Rocket Lab's medium-lift reusable launch vehicle has not yet flown; first flight targeted Q4 2026. Rocket Lab has been "on-ramped" (made eligible to bid, not yet certified to win task orders) to the US Space Force's National Security Space Launch (NSSL) Phase 3 Lane 1 program (ceiling tripled from $5.6B to $17B in July 2026), but per Motley Fool (16 Jul 2026) and Rocket Lab's own release, it **cannot win individual NSSL task orders until Neutron completes a successful first flight** — a real, dated, forward-looking dependency, cited here as qualitative context only, consistent with "guidance/forward commentary is a trigger, never a scored input."
- **Recent contract win:** a $266M US Space Force Rocket Systems Launch Program (RSLP) suborbital-launch contract, awarded 2026-07-27 (Alaska/Kodiak launches).

Sources: SEC EDGAR (10-Q, 10-K, XBRL API, as cited above); The Motley Fool, "The Space Force's $5.6 Billion Launch Program Has a New Contender" (16 Jul 2026); Rocket Lab investor-relations press releases (27 Jul 2026 RSLP contract; NSSL Phase 3 Lane 1 on-ramp release).

---

## §3. Phase 01 — Quality Score (methodology version 2026-06-29)

### 3.1 Hard disqualifier check

| Hard disqualifier | RKLB data (this session) | Verdict |
|---|---|---|
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Not the binding disqualifier here (see next row) — moot given §3.1's other outright fail, but noted for completeness: with both FCF and NI negative in every year on record, the raw ratio is not economically meaningful (see §3.5). | Not evaluated as decisive — superseded by the row below |
| **Net Debt/EBITDA over its applicable threshold (2.5×)** | Net cash position of **−$2,287.340M** as of 2026-06-30 (§2.3) — no net debt exists to test against the threshold at all. | **PASS** |
| **Not FCF-positive for 3+ consecutive years** | Per §2.2: FCF was negative in **every one of the 6 full fiscal years Rocket Lab has reported as an SEC filer** (FY2020 through FY2025), and remains negative through H1 2026. The "most recently completed fiscal years" rolling window (per the 2026-08-05 clarification in quality-scoring.md) is FY2023–FY2025 — **all three uniformly negative** ($(153.574)M, $(115.983)M, $(321.806)M). This is not a boundary case the rolling-window clarification could soften: the current window is uniformly negative, and so is every other 3-year window back to the company's first reported year. | **FAIL — fires decisively** |

**A hard disqualifier fires.** Per [quality-scoring.md](../framework/quality-scoring.md): *"These mirror the existing Phase 01 non-negotiables — a weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* Rocket Lab has never posted a single FCF-positive fiscal year since it began SEC reporting — this is about as unambiguous a case of this disqualifier as exists, not a marginal or judgment-call reading.

**Per operating-brief.md/quality-scoring.md, this alone is sufficient to fail the Quality Score gate regardless of the weighted sub-score total.** The full weighted computation is still shown below (§3.2–§3.6) for transparency — consistent with "show every calculation, no black-box outputs" — and, as it turns out, independently confirms the fail by a wide margin on the weighted score alone as well (§3.6).

### 3.2 Profitability (25% weight)

```
TTM Net Margin = -165.459 / 769.146 = -21.512%
  NetMargin_Component = clamp((-21.512/30)x100) = clamp(-71.71) = 0.0

Invested Capital = Total Debt ($14.845M) + Equity ($3,492.153M) - Cash ($2,129.485M) - Marketable Securities ($172.700M)
                 = $1,204.813M
TTM effective tax rate not used (pretax loss makes any effective-rate reading distorted, same treatment as
  loss-making companies in prior sessions, e.g. HIMS 2026-08-11) — standard 21% US corporate rate used instead:
NOPAT = TTM EBIT x (1 - 0.21) = -223.494 x 0.79 = -$176.560M
ROIC = -176.560 / 1,204.813 = -14.655%
  ROIC_Component = clamp((-14.655/30)x100) = clamp(-48.85) = 0.0

Profitability_Score = (0.0 + 0.0) / 2 = 0.0
  (The "cap at 40.0 if not FCF-positive 3yr" rule is moot here — both components already floor at 0.0
   independent of that cap, and §3.1 already establishes FCF-positivity fails outright.)
```
**Profitability_Score = 0.0**

### 3.3 Margins (15% weight)

```
TTM Gross Margin = 286.615 / 769.146 = 37.264%
GrossMargin_Score(raw) = clamp((37.264/80)x100) = 46.58
```
Structural-trend check: gross margin is below the 40% static threshold but has expanded every year on record — FY2023 21.02% → FY2024 26.63% → FY2025 34.43% → TTM 37.26% (computed from the same XBRL series as §2.1/§2.2: FY2023 GP $51.409M / Rev $244.592M; FY2024 GP $116.149M / Rev $436.214M; FY2025 GP $207.181M / Rev $601.799M). This is a clear, multi-year, structural (not cyclical) expansion — qualifies for the **+10** structural-trend bonus under quality-scoring.md's Margins rule.

```
Margins_Score = 46.58 + 10 = 56.58
```
**Margins_Score = 56.58**

### 3.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $210.996M -> FY2025 $601.799M) = (601.799/210.996)^(1/3) - 1 = 41.816%
Growth_Score(raw) = clamp((41.816/25)x100) = clamp(167.26) = 100.0  (saturates)
```
TAM-expansion modifier: documented evidence exists (Space Systems segment growth via M&A-driven vertical integration — Mynaric, Motiv, GEOST acquisitions; NSSL Phase 3 Lane 1 ceiling tripled to $17B in Jul 2026, §2.4) — **moot, already capped at 100.0.** Structural-deceleration modifier: does **not** apply — Q2 2026 revenue growth (+62.0% YoY) *reaccelerated* sharply vs. FY2025's own +37.9% YoY full-year growth, the opposite of a deceleration signal.

**Growth_Score = 100.0**

### 3.5 Balance Sheet (15% weight)

```
Net Debt = $14.845M (total debt) - $2,129.485M (cash) - $172.700M (marketable securities) = -$2,287.340M (net cash)
```
Rocket Lab holds a large net cash position — no net debt exists, so the standard `clamp(100 × (1 − NetDebt/EBITDA / 4))` formula's numerator is already at its best-case floor regardless of the (also negative, given the operating loss) EBITDA denominator. Consistent with this framework's established treatment of a net-cash balance sheet (e.g. the 2026-07-25 ENPH session, "net cash position... Balance Sheet 100.0"):

**BalanceSheet_Score = 100.0**

*Caveat, flagged explicitly:* this net-cash position was built overwhelmingly via new equity issuance ($1,529.639M raised through ATM equity offerings in H1 2026 alone, §2.3) rather than from operating cash generation, which is itself decisively negative every year (§2.2). The Balance Sheet sub-score correctly measures balance-sheet *risk* (near-zero here — Rocket Lab is not at any near-term insolvency or covenant risk), but says nothing about whether the underlying operating business is self-funding — that gap is exactly what the FCF-positivity hard disqualifier (§3.1) exists to catch, and does catch here.

### 3.6 Moat Signal (15% weight)

| Signal | Evidence | Verdict |
|---|---|---|
| Market share stable or growing | Rocket Lab's Electron is the world's third most frequently launched orbital rocket (behind SpaceX's Falcon 9 and China's Long March series) as of early 2026, with 35 launches since the start of 2025 (Yahoo Finance/Motley Fool, "Better Space Stock to Buy Before 2026 Runs Out," Jul 2026). Government business is expanding, not just holding share: a $266M US Space Force RSLP suborbital-launch contract awarded 27 Jul 2026 (Rocket Lab investor-relations press release), and NSSL Phase 3 Lane 1 program eligibility with its contract ceiling tripled from $5.6B to $17B in Jul 2026 (though task-order eligibility itself is still gated on Neutron's first flight, §2.4 — cited as context, not counted toward this signal). | **TRUE** |
| Brand premium | No cited evidence of price increases sustained without volume loss, or of a documented pricing premium vs. named competitors, found this session. | **FALSE** |
| Network effect | No two-sided-marketplace or user-growth-driven-value mechanism applies to a launch-services/spacecraft-manufacturing business model. | **FALSE** |
| Switching costs | No specific documented mechanism found this session (e.g. contractual lock-in terms, integration-depth data) for either Launch Services or Space Systems customers — plausible in principle (satellite-bus design integration, government program certification overhead) but not backed by a citation, so not credited, consistent with "never mark a signal true without a cited source." | **FALSE** |
| Scale cost advantage | No cost-per-unit data found showing a gap vs. smaller launch competitors (Firefly Aerospace, ABL Space Systems, Relativity Space) — Rocket Lab's Electron ($7.5M/mission per Motley Fool reporting) is itself a small-payload vehicle competing against much larger-scale SpaceX (Falcon 9, 22,800kg to LEO vs. Electron's ~300kg), so no scale advantage is evidenced in either direction. | **FALSE** |

```
Moat_Score = (1/5) x 100 = 20.0
```
**Moat_Score = 20.0**

### 3.7 FCF Quality (10% weight)

```
TTM FCF = TTM OCF + TTM CapEx = (-222.461) + (-148.678) = -$371.139M
  (TTM OCF = FY2025 OCF - H1 2025 OCF + H1 2026 OCF = -165.521 - (-77.467) + (-134.407) = -222.461
   TTM CapEx = FY2025 CapEx - H1 2025 CapEx + H1 2026 CapEx = -156.285 - (-60.719) + (-53.112) = -148.678)
TTM Net Income = -$165.459M

Raw ratio: FCF / NI = -371.139 / -165.459 = 2.243 (224.3%)
```
**Flagged explicitly, same treatment as the 2026-08-11 HIMS session's identical edge case:** dividing two negative numbers (FCF and NI both negative) produces an arithmetically large *positive* ratio that is **not economically meaningful** — it would perversely reward Rocket Lab for its cash burn growing *faster* than its net loss, the opposite of what "FCF quality" is meant to measure. Two readings shown:

```
LITERAL (formula applied as written): FCFQuality_Score = clamp(((2.243-0.40)/0.60)x100) = clamp(307.2) = 100.0
CONSERVATIVE (flagged not-meaningful, floored): FCFQuality_Score = 0.0
```

This session uses the **conservative (0.0) reading** as its primary figure, since crediting a "perfect" cash-conversion score to a company that has never generated positive free cash flow in any fiscal year (§3.1) would directly contradict the sub-score's own purpose. The **literal reading is also shown and carried through the final weighted total below** for transparency (§3.8) — it does not change the FAIL outcome either way.

**FCFQuality_Score = 0.0 (primary, conservative reading) / 100.0 (literal formula reading, shown for comparison)**

### 3.8 Final weighted Quality Score

```
Quality Score (conservative FCFQ=0.0) = (0.0x0.25) + (56.58x0.15) + (100.0x0.20) + (100.0x0.15) + (20.0x0.15) + (0.0x0.10)
   = 0.000 + 8.487 + 20.000 + 15.000 + 3.000 + 0.000
   = 46.487 -> rounds to 46.5

Quality Score (literal FCFQ=100.0) = 46.487 + 10.0 = 56.487 -> rounds to 56.5
```

**Under either FCF-Quality reading, the weighted score (46.5–56.5) falls 23.5–33.5 points short of the 80.0+ gate** — the judgment call flagged in §3.7 does not change the outcome. Combined with the hard disqualifier that already fires outright in §3.1, this is a decisive, doubly-confirmed FAIL.

### Result: **Phase 01 FAIL — hard disqualifier (never FCF-positive) fires, and the weighted score (46.5–56.5) independently misses the 80.0+ gate by 23.5–33.5 points**

No Rate Environment Gate, no Phase 02 valuation score, and no Composite Score computed — consistent with the strict gate rule in quality-scoring.md and the hard-disqualifier rule that applies "regardless of weighted score."

---

## §4. Gate Result — Phase 02 / Composite Score / Order Setup NOT computed

Per quality-scoring.md: *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* And separately: hard disqualifiers "fail regardless of weighted score." RKLB fails on **both** independent tests — **this session stops here.** No fair-value work, no buy/sell/stop levels, no position sizing.

(Also noted, though moot: Rocket Lab's SPAC-merger IPO was August 2021, giving it enough full-fiscal-year history for the 3-year lookbacks Phase 01 requires — this session did **not** need to invoke any "insufficient history" carve-out. Had the Quality gate cleared, the subsequent Phase 02 Forward-PE and PEG sub-scores would very likely have needed their no-history/PEG-ineligible fallbacks, given negative trailing earnings throughout — but that question is moot since Phase 02 is never reached.)

---

## §5. Recommendation

# **PASS — Quality Score gate FAILS both on a hard disqualifier (never FCF-positive in 6 years of SEC reporting) and independently on the weighted score (46.5–56.5/100.0, 23.5–33.5 points short of 80.0). No order setup, no fair-value work, no BUY/TRIM/EXIT action.**

Rocket Lab is a real, fast-growing business by several honest measures independently confirmed this session: revenue reaccelerated to +62.0% YoY in Q2 2026, 3-year revenue CAGR is a strong 41.8%, gross margin has expanded every year for four straight years (21.0%→26.6%→34.4%→37.3% TTM), and the balance sheet carries a large net-cash cushion ($2.29B) after a $1.53B H1-2026 equity raise. The Growth (100.0), Balance Sheet (100.0), and Margins (56.6) sub-scores reflect this genuinely improving trajectory.

But the framework's central, non-negotiable gate is not met, and not narrowly: **Rocket Lab has never reported a single fiscal year of positive free cash flow — not FY2020, not FY2021, ..., not FY2025, and not H1 2026 either.** Operating cash burn has actually *widened* in dollar terms even as revenue has scaled (FY2024 FCF −$116.0M → FY2025 FCF −$321.8M), because capital expenditure (Neutron development, Space Systems capacity, M&A integration) has grown faster than operating losses have narrowed. This is precisely the pattern the FCF-positivity hard disqualifier exists to catch — a company that looks statistically attractive on growth and balance-sheet-safety grounds but has not yet demonstrated it can self-fund from its own operations. Profitability is also floored at 0.0 (TTM net margin −21.5%, ROIC −14.7%), and Moat evidence supports only 1 of 5 signals (market share) with a documented citation.

This is the intended behavior of a strict 80.0+ gate applied to a genuinely fast-growing but still cash-burning, pre-profitability company — see the **Value trap** glossary entry and the same reasoning applied to HIMS (2026-08-11) and ENPH (2026-07-25) this framework cycle.

**No position opened. Nothing to log in `decisions/`** (per task instructions, a `decisions/` entry is only required if a position is actually opened).

---

## §6. Watchlist Actions

- Created `watchlist/not-in-portfolio/RKLB/RKLB-2026-08-11.md` — first-ever entry for this ticker, so no "significant change" comparison test applies (per watchlist/README.md, a first entry is always created).
- No stale-score mark applies — RKLB has never been scored under any prior methodology version, so there is nothing to clear in `watchlist/STALE.md`.

---

## §7. Next Review Trigger

- **Rocket Lab's Q3 2026 earnings release.** Based on this year's cadence (Q1 2026 reported ~May, Q2 2026 reported 10 Aug 2026), Q3 2026 would be expected roughly early-to-mid November 2026. The single most direct path to a materially different result is a demonstrated, sustained turn toward positive free cash flow (operating cash flow improving faster than, or capex moderating relative to, revenue growth) — not yet observed in any of the 6+ fiscal periods reviewed this session.
- **Neutron's first flight** (targeted Q4 2026) is a material qualitative catalyst worth tracking even though it is not itself a scored input — a successful first flight would open eligibility for NSSL Phase 3 Lane 1 task orders (up to a $17B program ceiling) and is the single largest disclosed growth catalyst on the horizon (§2.4).
- Other standard Rule 9 events: a guidance revision, a CEO/CFO-level management change, material new M&A, a macro/regulatory shift, or a >15% unexplained price move from $78.82.

---

## §8. Data Gaps Flagged (summary — none blocked scoring)

1. **Quarterly (non-cumulative) breakdowns for Q3 2025, Q4 2025, and Q1 2026 individually** were not separately available from a single source this session — the TTM figures in §2.1/§2.2/§3.7 were reconstructed as FY2025 − H1 2025 + H1 2026 (a standard, exact arithmetic identity for full-year and half-year filed aggregates, not an estimate), rather than by summing four discrete quarters. This is mathematically equivalent to a direct quarterly sum and does not represent invented or estimated data.
2. **FCF/NI conversion ratio, "not economically meaningful" judgment call** (§3.7) — flagged prominently, same pattern as the 2026-08-11 HIMS session; does not change this session's FAIL outcome under either reading.
3. **Switching-cost and scale-cost-advantage Moat evidence** — a plausible mechanism may exist (e.g. satellite-bus design lock-in, government-certification overhead) but no specific cost-per-unit or contractual-lock-in citation was found this session; both left FALSE per "never mark a signal true without a cited source." Non-blocking (does not change the outcome even under the most generous 5-of-5 Moat sensitivity — see below).
4. **Earnings-call commentary** (if any) beyond the filed 8-K/10-Q written materials was not sourced this session, consistent with this framework's "primary filing over secondary commentary" discipline.

**Moat sensitivity (the main qualitative judgment call in this computation):**

| Moat reading | Moat_Score | Quality Score (conservative FCFQ) | Gate result |
|---|---|---|---|
| Conservative (0/5) | 0.0 | 43.5 | FAIL |
| **Primary (this session, 1/5)** | **20.0** | **46.5** | **FAIL** |
| Generous (5/5 — credit every signal) | 100.0 | 58.5 | FAIL — still 21.5pts short |

None of these gaps or judgment calls are close to decisive to the outcome — the hard disqualifier (§3.1) and the wide weighted-score miss (§3.6/§3.8) are both robust to every discretionary call made in this session.

---

## §9. Glossary

New terms added to [framework/glossary.md](../framework/glossary.md) this session (in alphabetical position) before being cited here: **ATM (At-The-Market) equity offering** *(cross-referenced existing "ATM Program" entry — no new entry needed, see below)*, **Backlog** *(already present)*, **NSSL (National Security Space Launch)**, **On-ramp (procurement)**, **RSLP (Rocket Systems Launch Program)**.

| Term | Meaning |
|---|---|
| **10-K / 10-Q** | Annual / quarterly SEC financial-disclosure filings — this session's primary sourcing for Rocket Lab's income statement, balance sheet, and cash-flow data. |
| **ATM Program (At-the-Market Offering Program)** | A facility letting a company sell newly issued shares directly into the open market over time at prevailing prices — Rocket Lab raised $1,529.639M this way in H1 2026, the primary driver of its net-cash balance-sheet position (§2.3/§3.5). |
| **Backlog** | The dollar value of signed customer orders not yet recognized as revenue — Rocket Lab's was $2,355.949M as of 2026-06-30, a demand-visibility metric, not a scored Quality/Valuation input. |
| **CAGR** | Compound Annual Growth Rate. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every EDGAR filer (Rocket Lab's is 0001819994). |
| **EBIT** | Earnings Before Interest and Taxes — operating profit; used as the ROIC numerator basis in §3.2. |
| **FCF (Free Cash Flow)** | Cash generated after running and investing in the business (Operating Cash Flow − CapEx) — the metric behind this session's decisive hard disqualifier (§3.1/§2.2): negative in every fiscal year Rocket Lab has reported. |
| **GAAP** | Generally Accepted Accounting Principles — the standard this framework scores off, distinct from any company-reported non-GAAP figure. |
| **Gross Margin** | Gross Profit ÷ Revenue — Rocket Lab's has expanded every year on record (§3.3), though still below the framework's 40% static threshold. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score; the "not FCF-positive for 3+ consecutive years" disqualifier fires decisively for Rocket Lab this session (§3.1). |
| **Invested Capital** | Debt + Equity − Cash (and equivalents), the ROIC denominator; $1,204.813M for Rocket Lab this session. |
| **Moat** | A durable competitive advantage; scored 20.0 (1 of 5 signals — market share) for Rocket Lab this session (§3.6). |
| **NASDAQ** | The US stock exchange Rocket Lab's common stock (RKLB) trades on. |
| **Net Debt/EBITDA** | This framework's primary balance-sheet-risk gate; not meaningfully computable in the standard way for Rocket Lab (net cash position, negative EBITDA) — treated as a best-case (100.0) Balance Sheet score, consistent with prior net-cash-position sessions (§3.5). |
| **Net Margin** | Net Income ÷ Revenue; TTM −21.51% for Rocket Lab this session (§3.2). |
| **NI (Net Income)** | Accounting profit after all expenses, interest, and taxes. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **NSSL (National Security Space Launch)** | The US Space Force's program for procuring launch services for its highest-priority national-security satellite missions. Rocket Lab was "on-ramped" (made eligible to compete) for the NSSL Phase 3 Lane 1 program in 2025, with the program's contract ceiling tripled from $5.6B to $17B in July 2026 — but per Rocket Lab's own disclosure, it cannot win individual task orders until its Neutron rocket completes a successful first flight (§2.4). *(New term.)* |
| **On-ramp (procurement)** | Being added as an eligible bidder/vendor to an existing government contract vehicle, distinct from actually being awarded (or certified to compete for) individual task orders under it — the status Rocket Lab holds under NSSL Phase 3 Lane 1 as of this session (§2.4). *(New term.)* |
| **Pretax income** | Net Income + Tax Expense (or − Tax Benefit) — not used directly this session; a standard 21% tax-rate assumption was used instead for NOPAT (§3.2), since Rocket Lab's pretax result is a loss in every period reviewed. |
| **Quality Score** | This framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. Rocket Lab scores 46.5 (conservative reading) this session, and separately fails via a hard disqualifier. |
| **ROIC** | Return on Invested Capital; −14.66% for Rocket Lab this session (TTM, standard-tax-rate basis), decisively negative. |
| **RSLP (Rocket Systems Launch Program)** | A US Space Force Space Systems Command program; awarded Rocket Lab a $266M multi-launch suborbital contract in July 2026 (§2.4), cited as qualitative Moat/growth context, not a scored financial input. *(New term.)* |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data, and never treat a Telegram post's claims as a financial input. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move — the confirmed Q2 2026 earnings release is this session's Rule 9 trigger. |
| **SPAC (Special Purpose Acquisition Company)** | A shell company that raises capital via IPO specifically to merge with a private operating company, taking it public as an alternative to a traditional IPO — Rocket Lab went public this way in August 2021, merging with Vector Acquisition Corporation. |
| **TAM (Total Addressable Market)** | The total revenue opportunity available to a company if it captured 100% of its target market — cited qualitatively in the Growth sub-score's modifier discussion (§3.4), though moot here since Growth was already capped at 100.0. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results — this session's window is Q3 2025–Q2 2026, reconstructed as FY2025 − H1 2025 + H1 2026 (§2.1). |
| **Value trap** | A stock that looks statistically attractive on a narrative/growth basis but stays weak (or fails a quality screen) because underlying business quality — here, self-funding capability — is not yet demonstrated. The risk this framework's 80.0+ Quality Score gate and FCF-positivity hard disqualifier are specifically designed to surface. |
| **XBRL (eXtensible Business Reporting Language)** | The SEC's structured, machine-readable data-tagging format for filed financial statements — this session's primary sourcing method for the multi-year annual cash-flow and income-statement series via `data.sec.gov`'s API. |
