# NEW POSITION — POET (POET Technologies Inc.) — 2026-08-14

**Task type:** NEW POSITION (direct user request)
**Date:** 2026-08-14 (Friday)
**10Y US Treasury Yield:** Not fetched this session — evaluation stops at the Phase 01 Quality Score gate (§3) before the Rate Environment Gate would otherwise apply, same precedent as the 2026-08-11 RKLB, 2026-08-11 HIMS, 2026-08-14 LITE, and 2026-08-14 COHR sessions.
**Current POET portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md)).
**Prior coverage:** None — first-ever `/new-position` evaluation of POET in this repo (confirmed absent from both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/`).
**Sector:** Technology / Semiconductors — Photonic Integrated Circuits (optical interposers) for AI/data-center interconnect, pre-mass-production / early-commercialization stage.
**Filer type:** Foreign private issuer — POET Technologies Inc. is incorporated in Ontario, Canada, and reports quarterly results to the SEC via **Form 6-K** rather than a domestic-filer 10-Q.
**IBKR contract used:** `contract_id` 547618418 — NASDAQ, symbol POET, description "POET TECHNOLOGIES INC," `country_code` US, security type STK. Confirmed via `search_contracts` against several look-alikes (a leveraged ETF product "POEL," a German exchange (FWB) cross-listing "RI4A," an OTC "VALUE" exchange line "PTK," and unrelated municipal-bond issuers with "Poet"/"Poetry" in their name) — the NASDAQ STK line is the correct primary listing.
**First-use jargon decode:** see closing Glossary (§9) — several new terms this session, added to [glossary.md](../framework/glossary.md) before being cited here.

---

## §1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$9.565** | IBKR `get_price_snapshot`, `contract_id` 547618418, `last.price`, timestamp Unix 1786718725 = **2026-08-14 14:45:25 UTC** (regular NASDAQ session — market opened 13:30 UTC) |
| Bid / Ask | $9.56 / $9.57 (size 1,518 / 365) | IBKR `bid_ask` |
| Change vs. prior close | +$0.655 (+7.35%) | IBKR `change` (`prior-close` field itself returned empty this snapshot — same vendor quirk documented in the 2026-08-11 RKLB/HIMS sessions; prior close derived as $9.565 − $0.655 = $8.91) |
| 52-week range | $3.87 (low) – $20.81 (high) | IBKR `misc-statistics`. 13-week high $20.27, 26-week high $20.81 — the 52-week high was set within the trailing 26 weeks. 13-week low $6.28, 26-week low $4.87, 52-week low $3.87 — the stock has been highly volatile, currently up sharply intraday. |
| Today's volume | ~6,580,394 shares | IBKR `volume` |

**$9.565 is used as the live price for all context below.** Price is currently ~54.0% below the 52-week high ($20.81) and ~147.2% above the 52-week low ($3.87) — a very wide trading range, noted for context only (price action is never a scored input or an action trigger on its own, per Rule 0/operating-brief.md). The +7.35% intraday move is noted; per Rule 9, only an *unexplained* >15% move is itself a mandatory re-valuation trigger — this smaller move isn't a trigger threshold and isn't investigated further here, since this session's own trigger is the direct user request, not a price move.

---

## §2. Data Sourcing

POET Technologies reports to the SEC via Form 6-K (foreign private issuer) rather than a 10-Q/10-K. Figures below are drawn from POET's own Q1 2026 and Q2 2026 earnings press releases (GlobeNewswire, via the company's own 6-K exhibits) for the two most recent quarters, and from a third-party financial-data aggregator (stockanalysis.com, itself sourced from POET's audited annual filings) for the FY2021–FY2025 annual income-statement, cash-flow, and balance-sheet series used in the hard-disqualifier and multi-year checks below. No figure in this session is inferred, estimated, or carried over from a Telegram post or any other secondary commentary.

### 2.1 Annual income statement & cash flow, FY2021–FY2025 ($M)

| Fiscal Year | Revenue | Net Income (Loss) | Gross Margin | Operating Income (Loss) | D&A | Operating Cash Flow | CapEx | **FCF = OCF − CapEx** |
|---|---|---|---|---|---|---|---|---|
| 2021 | 0.21 | (15.67) | 100.00% | — | — | (11.23) | (0.77) | **(12.00)** |
| 2022 | 0.55 | (21.04) | 100.00% | — | — | (12.33) | (3.01) | **(15.34)** |
| 2023 | 0.47 | (20.27) | 100.00% | (20.41) | 1.92 | (15.41) | (1.17) | **(16.58)** |
| 2024 | 0.04 | (56.70) | 100.00% | (30.06) | 2.02 | (23.29) | (6.78) | **(30.07)** |
| 2025 | 1.07 | (62.96) | 100.00% | (42.09) | 3.32 | (31.09) | (2.26) | **(33.34)** |

```
TTM proxy note: POET does not publish a single-source TTM roll-up. The two most recent quarters (Q1+Q2 2026) are
shown separately in §2.2 below rather than blended into a synthetic TTM, since the framework's "never invent" rule
extends to not fabricating a Q3/Q4 2025 split that wasn't independently sourced this session.
```

**Every one of the 5 full fiscal years POET has reported was FCF-negative — POET has never posted a single FCF-positive fiscal year.** This is the central finding of this session (see §3.1).

### 2.2 Most recent two quarters (Q1–Q2 2026), from POET's own press releases

| Quarter | Revenue | Net Loss | EPS | Operating Cash Flow |
|---|---|---|---|---|
| Q1 2026 | $503,389 | ($12.3M) | ($0.08) | ($8.8M) |
| Q2 2026 | $569,925 | ($11.3M) | ($0.07) | ($12.2M) |

Company's own characterization: Q2 2026 revenue "up 112% year-over-year," the "sixth consecutive quarter of sequential revenue growth" — both self-reported growth-narrative claims, cited here as context only, consistent with "guidance/forward commentary is a trigger, never a scored input" (see valuation-scoring.md's "Why Forward Guidance Is Not a Sub-score"). Revenue is described by the company itself as **NRE (Non-Recurring Engineering) and product revenue** — see Glossary (§9) — a caveat directly relevant to how much weight this revenue base can carry as a Growth-quality signal (§3.4).

### 2.3 Balance sheet

| | FY2024 (12/31/24) | FY2025 (12/31/25) | Most recent (Q2 2026, per company release) |
|---|---|---|---|
| Cash & equivalents | $37.14M | $39.96M | — |
| Cash + short-term investments (company-reported) | — | — | **$796.3M** |
| Total debt | $7.24M | $7.07M | ~$7.80M (aggregator estimate; no more precise primary-source figure sourced this session) |
| Total equity | $20.69M | $183.79M | — |

```
Net Debt FY2025 = Total Debt ($7.07M) − Cash ($39.96M) = −$32.89M (net cash)
Net Debt (Q2 2026, using company-reported cash+STI) = ~$7.80M − $796.3M ≈ −$788.5M (deep net cash)
```

The Q2 2026 cash position followed **completion of a $400 million financing in May 2026** — i.e. new capital raised (dilutive to existing shareholders), not cash generated from operations, which remained deeply negative in the same quarter (operating cash flow ($12.2M) in Q2 2026 alone). Flagged explicitly per §3.5 below, the same caveat pattern used for RKLB's 2026-08-11 session (net-cash position built by equity issuance, not self-funding).

### 2.4 Context (not scored inputs)

- **Design win / customer agreement:** an initial purchase order valued at **$50 million** from a customer named "Lumilens" for optical-interposer-based engines, which the company states "could scale to over $500 million in cumulative purchases over five years" (forward-looking, self-reported — the $500M figure is not used as a scored input anywhere below).
- **Post-quarter order:** a $2.4M purchase order from an existing customer, disclosed after quarter-end.
- **Partnership:** an agreement with an unnamed "Tier 1 laser company" to co-develop an external light-source engine.
- **Company's own stated timeline:** expects to "begin shipping substantial numbers of production units for qualification in the remaining quarters of 2026" — a forward-looking statement, not a scored input.
- **TAM framing:** company targets AI and data-center markets for high-speed optical engines and light sources — a real, plausible large-TAM category, but not independently sized this session.

Sources: POET Technologies Q1 2026 and Q2 2026 earnings press releases (GlobeNewswire, 2026-05-14 and 2026-08-13); stockanalysis.com (FY2021–FY2025 annual income statement, cash-flow statement, and balance sheet, itself sourced from POET's audited annual filings); IBKR live price snapshot (§1).

---

## §3. Phase 01 — Quality Score (methodology version 2026-06-29)

### 3.1 Hard disqualifier check

| Hard disqualifier | POET data (this session) | Verdict |
|---|---|---|
| **Net Debt/EBITDA over its applicable threshold (2.5×)** | Net cash position in every year reviewed (FY2025: −$32.89M net cash; Q2 2026: ~−$788.5M net cash after the May 2026 raise) — no net debt exists to test against the threshold at all. | **PASS** |
| **FCF/Net Income conversion ratio <70% for 2+ consecutive years without a documented growth-capex explanation** | Not the binding disqualifier here (see next row) — moot given the outright fail below, but noted for completeness: with both FCF and Net Income negative in every year on record, the raw ratio is not economically meaningful (see §3.7). | Not evaluated as decisive — superseded by the row below |
| **Not FCF-positive for 3+ consecutive years** | Per §2.1: FCF was negative in **every one of the 5 full fiscal years POET has reported** (FY2021 through FY2025 — $(12.00)M, $(15.34)M, $(16.58)M, $(30.07)M, $(33.34)M), and remains negative through Q1–Q2 2026 (operating cash flow $(8.8)M and $(12.2)M respectively). The "most recently completed fiscal years" rolling window (per the 2026-08-05 clarification in quality-scoring.md) is FY2023–FY2025 — **all three uniformly negative.** This is not a boundary case the rolling-window clarification could soften: the current window is uniformly negative, and so is every other 3-year window back to the earliest year with data (FY2021). | **FAIL — fires decisively** |

**A hard disqualifier fires.** Per [quality-scoring.md](../framework/quality-scoring.md): *"These mirror the existing Phase 01 non-negotiables — a weighted average can't average away an outright balance-sheet or cash-flow-quality failure."* POET has never posted a single FCF-positive fiscal year — this is about as unambiguous a case of this disqualifier as exists, not a marginal or judgment-call reading, and is directly consistent with the note in the task brief that POET is a "pre-revenue/early-commercialization semiconductor company."

**Per operating-brief.md/quality-scoring.md, this alone is sufficient to fail the Quality Score gate regardless of the weighted sub-score total.** The full weighted computation is still shown below (§3.2–§3.7) for transparency — consistent with "show every calculation, no black-box outputs" — and, as it turns out, independently confirms the fail by a wide margin on the weighted score alone as well (§3.8).

### 3.2 Profitability (25% weight)

```
FY2025 Net Margin = -62.96 / 1.07 = -5,857.78%  (sourced figure — revenue base is tiny, so the ratio is extreme)
  NetMargin_Component = clamp((-5857.78/30)x100) = clamp(-19,525.9) = 0.0

ROIC: only FY2023 figure available from this session's sources: -819.80%.
  ROIC_Component = clamp((-819.80/30)x100) = clamp(-2,732.7) = 0.0
  (FY2025 ROIC not separately sourced this session — but FY2025 ROE -61.58% and ROA -21.14% are both
   deeply negative too, so FY2025 ROIC would with near certainty also be deeply negative; this doesn't change
   the component score, since any negative input floors identically at 0.0 under this clamp.)

Profitability_Score = (0.0 + 0.0) / 2 = 0.0
  (The "cap at 40.0 if not FCF-positive 3yr" rule is moot here — both components already floor at 0.0
   independent of that cap, and §3.1 already establishes FCF-positivity fails outright.)
```
**Profitability_Score = 0.0**

### 3.3 Margins (15% weight)

```
Gross Margin = 100.00% in every one of FY2021-FY2025 (sourced figure)
GrossMargin_Score = clamp((100/80)x100) = clamp(125.0) = 100.0
```
**Heavily caveated, not taken at face value:** a 100% gross margin at a company with essentially no reported cost-of-revenue line is a strong signal that this figure reflects **pre-mass-production accounting** — POET's revenue is described by the company itself as "NRE and product revenue" (§2.2, Glossary §9), i.e. mostly one-off engineering-service fees rather than manufactured-unit sales with a real cost-of-goods-sold line yet. This is **not** evidence of real pricing power or manufacturing cost efficiency (the first of the framework's "5 Qualitative Questions Before Scoring" — "why are margins high?" — the answer here is "no COGS has been recognized yet," not "pricing power" or "scale"). The formula-literal 100.0 score is shown per "show every calculation, no black-box outputs," but should be read as **not decision-relevant** rather than as evidence of quality.

**Margins_Score = 100.0 (formula-literal; flagged as not meaningful — see caveat above)**

### 3.4 Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $0.55M -> FY2025 $1.07M) = (1.07/0.55)^(1/3) - 1 = 24.86%
Growth_Score(raw) = clamp((24.86/25)x100) = clamp(99.44) = 99.4
```
TAM-expansion modifier: a documented, company-disclosed initial purchase order ($50M from "Lumilens," §2.4) exists — real evidence of a signed commercial agreement, not pure guidance. Applying the **+10** modifier per quality-scoring.md's "documented evidence of TAM expansion... cite the specific evidence" rule:

```
Growth_Score = clamp(99.4 + 10, 0, 100) = 100.0  (saturates)
```

**Heavily caveated, not taken at face value:** the underlying revenue base is FY2021 $0.21M → FY2022 $0.55M → FY2023 $0.47M → **FY2024 $0.04M** → FY2025 $1.07M — a **91% collapse in FY2024 followed by a >25x rebound in FY2025.** A 3-year CAGR computed purely off the FY2022 and FY2025 endpoints ignores this collapse entirely and is not a statistically meaningful growth signal at this revenue scale (annual revenue is still under $1.1M — smaller than many companies' single-customer contracts). The formula-literal 100.0 score is shown per "show every calculation," but — like the Margins score above — should be read as **not decision-relevant** given how small and volatile the underlying base is, rather than as evidence of durable double-digit growth.

**Growth_Score = 100.0 (formula-literal; flagged as low-confidence given tiny/volatile revenue base — see caveat above)**

### 3.5 Balance Sheet (15% weight)

```
Net Debt (most recent, Q2 2026, company-reported cash+STI) = ~$7.80M (debt) - $796.3M (cash+STI) ~ -$788.5M (net cash)
```
POET holds a large net-cash position — no net debt exists, so the standard `clamp(100 × (1 − NetDebt/EBITDA / 4))` formula's numerator is already at its best-case floor regardless of EBITDA's sign (also negative here, given the ongoing operating loss). Consistent with this framework's established treatment of a net-cash balance sheet (e.g. the 2026-08-11 RKLB session, "no net debt exists... BalanceSheet_Score = 100.0"):

**BalanceSheet_Score = 100.0**

*Caveat, flagged explicitly — same pattern as the 2026-08-11 RKLB session:* this net-cash position was built almost entirely via a **$400 million dilutive equity financing completed in May 2026**, not from operating cash generation, which remains decisively negative every quarter on record (§2.1, §2.2). The Balance Sheet sub-score correctly measures balance-sheet *risk* (near-zero here — POET is in no near-term insolvency or covenant-breach risk), but says nothing about whether the underlying business is self-funding — that gap is exactly what the FCF-positivity hard disqualifier (§3.1) exists to catch, and does catch here.

### 3.6 Moat Signal (15% weight)

| Signal | Evidence found this session | Verdict |
|---|---|---|
| Market share stable or growing | No cited market-share data found for the optical-interposer/PIC sub-segment POET competes in. | **FALSE** |
| Brand premium | No cited pricing-power evidence (price increases without volume loss, premium vs. named competitors). | **FALSE** |
| Network effect | No two-sided-marketplace or user-growth-driven-value mechanism applies to a component-supplier business model. | **FALSE** |
| Switching costs | Plausible in principle (semiconductor/photonics design-in cycles typically carry re-qualification costs once a customer integrates a supplier's part), and the disclosed multi-year Lumilens purchase-order structure ("could scale to over $500M over five years") is suggestive of a locked-in multi-year relationship — but no specific documented mechanism (contractual lock-in terms, integration-depth data) was found and cited this session, so not credited, consistent with "never mark a signal true without a cited source." | **FALSE** |
| Scale cost advantage | No cost-per-unit data found showing a gap vs. competitors — POET is pre-mass-production, i.e. by definition not yet operating at meaningful scale. | **FALSE** |

```
Moat_Score = (0/5) x 100 = 0.0
```
**Moat_Score = 0.0**

### 3.7 FCF Quality (10% weight)

```
FY2025: FCF / NI = -33.34 / -62.96 = 0.5296 (52.96%)
FY2024: FCF / NI = -30.07 / -56.70 = 0.5304 (53.04%)
```
**Flagged explicitly, same treatment as the 2026-08-11 RKLB/HIMS sessions' identical edge case:** dividing two negative numbers (FCF and Net Income both negative in every year on record) produces an arithmetically positive ratio that is **not economically meaningful** — it does not represent real cash-conversion quality for a company with neither positive earnings nor positive cash flow. Two readings shown:

```
LITERAL (formula applied as written, FY2025 ratio): FCFQuality_Score = clamp(((0.5296-0.40)/0.60)x100) = clamp(21.6) = 21.6
CONSERVATIVE (flagged not-meaningful, floored): FCFQuality_Score = 0.0
```

This session uses the **conservative (0.0) reading** as its primary figure, for the same reason as the RKLB/HIMS precedent: crediting a partial-credit score to a company that has never generated positive free cash flow in any fiscal year (§3.1) would contradict the sub-score's own purpose. The literal reading is also carried through the final weighted total below for transparency (§3.8) — it does not change the FAIL outcome either way.

**FCFQuality_Score = 0.0 (primary, conservative reading) / 21.6 (literal formula reading, shown for comparison)**

### 3.8 Final weighted Quality Score

```
Quality Score (conservative FCFQ=0.0) = (0.0x0.25) + (100.0x0.15) + (100.0x0.20) + (100.0x0.15) + (0.0x0.15) + (0.0x0.10)
   = 0.000 + 15.000 + 20.000 + 15.000 + 0.000 + 0.000
   = 50.0

Quality Score (literal FCFQ=21.6) = 50.0 + (21.6x0.10) = 50.0 + 2.16 = 52.2
```

**Under either FCF-Quality reading, the weighted score (50.0–52.2) falls 27.8–30.0 points short of the 80.0+ gate** — the judgment call flagged in §3.7 does not change the outcome. Combined with the hard disqualifier that already fires outright in §3.1, this is a decisive, doubly-confirmed FAIL. Note also that two of the three sub-scores propping up this 50–52 total (Margins 100.0, Growth 100.0) are explicitly flagged above (§3.3, §3.4) as formula artifacts of a company with essentially no cost-of-revenue line yet and a sub-$1.1M, highly volatile revenue base — not genuine evidence of pricing power or durable growth. A version of this score that discounted those two flagged sub-scores to something more conservative would fall well short of even the 50–52 headline figure.

### Result: **Phase 01 FAIL — hard disqualifier (never FCF-positive) fires, and the weighted score (50.0–52.2) independently misses the 80.0+ gate by 27.8–30.0 points**

No Rate Environment Gate, no Phase 02 valuation score, and no Composite Score computed — consistent with the strict gate rule in quality-scoring.md and the hard-disqualifier rule that applies "regardless of weighted score."

---

## §4. Gate Result — Phase 02 / Composite Score / Order Setup NOT computed

Per quality-scoring.md: *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* And separately, hard disqualifiers "fail regardless of weighted score." POET fails on **both** independent tests — **this session stops here.** No fair-value work, no buy/sell/stop levels, no position sizing.

---

## §5. Recommendation

# **PASS — Quality Score gate FAILS both on a hard disqualifier (never FCF-positive in 5 years of reported financials) and independently on the weighted score (50.0–52.2/100.0, 27.8–30.0 points short of 80.0). No order setup, no fair-value work, no BUY/TRIM/EXIT action.**

POET Technologies is exactly what the task brief flagged it as going in: a pre-revenue/early-commercialization semiconductor company. It has real, independently-verifiable positives — a $50M initial purchase order from a named customer with a disclosed path to a much larger multi-year relationship, a second post-quarter $2.4M order, a partnership with an unnamed Tier-1 laser company, six consecutive quarters of sequential (if still tiny) revenue growth, and — following a $400M capital raise in May 2026 — a very strong balance sheet with effectively no near-term insolvency risk.

But the framework's central, non-negotiable gate is not met, and not narrowly: **POET has never reported a single fiscal year of positive free cash flow** across all 5 years of financial history reviewed (FY2021–FY2025), and cash burn has continued to widen ($12.0M → $15.3M → $16.6M → $30.1M → $33.3M annually) even as revenue nominally "grew." Profitability is floored at 0.0 (FY2025 net margin −5,858%, ROIC deeply negative), Moat evidence supports 0 of 5 signals with a cited source, and revenue itself is still under $1.1M/year on a highly volatile base (including a 91% collapse in FY2024) — too small and too erratic to be a reliable Quality Score Growth signal even before the FCF disqualifier is considered. This is exactly the "wonderful narrative, unproven self-funding capability" pattern the 80.0+ gate and FCF-positivity hard disqualifier exist to catch — see the same reasoning applied to RKLB (2026-08-11), HIMS (2026-08-11), and the repeat LITE/COHR fails from earlier today (2026-08-14).

**No position opened. Nothing to log in `decisions/`** (per task instructions, a `decisions/` entry is only required if a position is actually opened).

---

## §6. Watchlist Actions

- Created `watchlist/not-in-portfolio/POET/POET-2026-08-14.md` — first-ever entry for this ticker, so no "significant change" comparison test applies (per watchlist/README.md, a first entry is always created).
- No stale-score mark applies — POET has never been scored under any prior methodology version, so there is nothing to clear in `watchlist/STALE.md`.

---

## §7. Next Review Trigger

- **POET's Q3 2026 earnings release.** Based on this year's cadence (Q1 2026 reported 14 May 2026, Q2 2026 reported 13 Aug 2026), Q3 2026 would be expected roughly mid-November 2026. The single most direct path to a materially different result is a demonstrated, sustained turn toward positive free cash flow (operating cash flow improving faster than, or capex/opex moderating relative to, revenue growth as production ramps) — not yet observed in any of the 5+ fiscal periods reviewed this session.
- **Lumilens order conversion / mass-production ramp** — the company's own stated timeline is to "begin shipping substantial numbers of production units for qualification in the remaining quarters of 2026." A confirmed shift from NRE-fee revenue to real, COGS-bearing product revenue at scale would materially change the Margins and Growth sub-score readings (§3.3, §3.4) and is worth tracking even though it is not itself a scored input yet.
- Other standard Rule 9 events: a guidance revision, a management change, material new M&A, a macro/regulatory shift, or a >15% unexplained price move from $9.565.

---

## §8. Data Gaps Flagged (summary — none blocked the FAIL outcome)

1. **Q3 2025 and Q4 2025 individual quarterly figures** were not sourced this session (only the full FY2025 annual aggregate and the two most recent quarters, Q1–Q2 2026, were available from the sources used) — a true TTM window was not reconstructed as a result; §2.1's FY2025 annual figures and §2.2's Q1–Q2 2026 figures are shown separately rather than blended, consistent with "never invent or estimate."
2. **FY2025 ROIC** was not separately sourced (only FY2023's −819.80% was available from the data source used) — non-blocking, since any negative ROIC value floors the Profitability sub-score component identically at 0.0 (§3.2).
3. **Total debt at Q2 2026** (~$7.80M) is an aggregator estimate, not confirmed against POET's own primary-source balance sheet this session — non-blocking, since the net-cash conclusion (§3.5) is overwhelmingly robust to reasonable error in this line given cash+short-term-investments of $796.3M against single-digit-million debt.
4. **FCF/NI conversion ratio, "not economically meaningful" judgment call** (§3.7) — flagged prominently, same pattern as the 2026-08-11 RKLB/HIMS sessions; does not change this session's FAIL outcome under either reading.
5. **Switching-cost Moat evidence** — a plausible mechanism may exist (multi-year purchase-order structure, semiconductor design-in/re-qualification costs) but no specific contractual-lock-in or integration-depth citation was found this session; left FALSE per "never mark a signal true without a cited source." Non-blocking — see Moat sensitivity table below.

**Moat sensitivity (the main qualitative judgment call in this computation):**

| Moat reading | Moat_Score | Quality Score (conservative FCFQ) | Gate result |
|---|---|---|---|
| **Primary (this session, 0/5)** | **0.0** | **50.0** | **FAIL** |
| Generous (5/5 — credit every signal) | 100.0 | 65.0 | FAIL — still 15.0pts short |

None of these gaps or judgment calls are close to decisive to the outcome — the hard disqualifier (§3.1) and the wide weighted-score miss (§3.8) are both robust to every discretionary call made in this session.

---

## §9. Glossary

New terms added to [framework/glossary.md](../framework/glossary.md) this session (in alphabetical position) before being cited here: **6-K**, **NRE (Non-Recurring Engineering) revenue**, **Photonic Integrated Circuit (PIC) / Optical Interposer**.

| Term | Meaning |
|---|---|
| **6-K** | A report a foreign private issuer furnishes to the SEC to disclose quarterly/interim results and other material information, filed in lieu of the domestic-filer 10-Q — POET (Ontario, Canada-incorporated) reports this way. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit. |
| **EPS** | Earnings Per Share — Net Income (or loss) divided by shares outstanding. |
| **FCF (Free Cash Flow)** | Cash generated after running and investing in the business (Operating Cash Flow − CapEx) — the metric behind this session's decisive hard disqualifier (§3.1/§2.1): negative in every fiscal year POET has reported. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; not economically meaningful when both figures are negative (§3.7). |
| **GAAP** | Generally Accepted Accounting Principles — the standard this framework scores off. |
| **Gross Margin** | Gross Profit ÷ Revenue — POET's is reported at 100% every year, flagged in this session as a pre-mass-production accounting artifact rather than a real pricing-power signal (§3.3). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score; the "not FCF-positive for 3+ consecutive years" disqualifier fires decisively for POET this session (§3.1). |
| **Moat** | A durable competitive advantage; scored 0.0 (0 of 5 signals) for POET this session (§3.6) — no company-specific cited evidence found. |
| **Net Debt/EBITDA** | This framework's primary balance-sheet-risk gate; POET holds a large net-cash position (no net debt), so treated as a best-case (100.0) Balance Sheet score per this framework's established treatment (§3.5). |
| **Net Margin** | Net Income ÷ Revenue; FY2025 −5,857.78% for POET (§3.2) — extreme, given the tiny revenue base. |
| **NOPAT (Net Operating Profit After Tax)** | EBIT × (1 − effective tax rate) — the numerator this framework uses to compute ROIC. |
| **NRE (Non-Recurring Engineering) revenue** | A one-off fee a customer pays a hardware supplier for custom design/engineering work, distinct from recurring per-unit product revenue — POET's own description of most of its reported revenue this session, a caveat on the Growth sub-score (§3.4). |
| **Photonic Integrated Circuit (PIC) / Optical Interposer** | A chip that processes and routes light instead of, or alongside, electrical signals — POET's "optical interposer" product platform for AI/data-center interconnect. |
| **Quality Score** | This framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. POET scores 50.0–52.2 this session, and separately fails via a hard disqualifier. |
| **ROA (Return on Assets)** | Net Income ÷ Total Assets — a cross-check reference figure; −21.14% for POET in FY2025. |
| **ROE (Return on Equity)** | Net Income ÷ Shareholder Equity; −61.58% for POET in FY2025. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it into profit; −819.80% for POET in FY2023 (most recent figure sourced this session), decisively negative. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% unexplained stock-price move. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — not reconstructed as a single figure this session due to a data gap (§8.1); FY2025 annual and Q1–Q2 2026 quarterly figures shown separately instead. |
