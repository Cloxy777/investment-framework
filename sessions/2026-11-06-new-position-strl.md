# NEW POSITION — Sterling Infrastructure Inc. (STRL) — 2026-11-06

**Task type:** NEW POSITION (first evaluation of this ticker; not held)
**Date:** 06 Nov 2026 | **10Y Treasury:** 4.90% (FRED `DGS10`, 2026-11-04, latest posted) | **Rate Regime Modifier that would apply:** +5 (3.5–5% bracket) — *not applied: valuation scoring did not run (gate failed)*
**Portfolio weight:** 0% (not held)

**Outcome in one line:** Quality Score **63.0 — FAILS the 80.0+ gate → PASS (Phase 01 FAIL).** No valuation score, Composite Score, or order setup computed, per the `/new-position` instruction to stop at a failed gate.

---

## 1. Why this session ran
User-initiated `/new-position strl`. Context: the stock is down ~75% from its 52-week high (IBKR: 52w high $1,005.68, 13-week high $606.11, 52w low $239.35) and fell ~35% in the month to 2026-11-05, immediately after a strong Q3 report (2026-10-28 after close / call 2026-10-29).

## 2. Live price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$252.86** (+$8.52, +3.49% on the day; last trade REALTIME) | IBKR snapshot, contract 27778176 (NASDAQ: STRL) |
| Bid / ask | $245.00 / $269.29 — **unusually wide** (thin/stale book at the time of the read) | IBKR |
| Prior close | $244.34 | implied by IBKR change; matches yfinance `lastPrice` |
| 52-week range | $239.35 – $1,005.68 | IBKR `misc_statistics` |
| Analyst targets (sanity check only) | mean $693.43 / median $680 / high $834 / low $565 (Cantor lowered $742→$565 on 2026-11-02) | yfinance |

Price is irrelevant to the Quality Score. The fundamentals script ran off yfinance's $244.34 market cap; price-dependent figures below are shown as the script printed them (see §3 note).

## 3. Fundamentals — `python -m scripts.fetch_fundamentals STRL` (verbatim)

```
Market Cap            = 7,452,989,440
Enterprise Value      = 7,448,859,136
Shares Outstanding    = 30,502,537
Forward PE            = 8.696
FCF Yield %           = 6.324
EV/EBIT               = 9.369
Net Margin %          = 12.851
Gross Margin %        = 23.778
ROIC % (NOPAT/InvCap) = 43.209  [tax_rate=0.2394, NOPAT=604,741,051, InvestedCapital=1,399,566,000]
Revenue 3yr CAGR %    = 12.062
Net Debt/EBITDA       = -0.045  [EBITDA_ttm=901,379,968]
FCF/NI TTM % (plain)  = 85.022
(FCF - SBC)/NI TTM %  = 79.117  [reported NI]
SBC yield %           = 0.439
Gross buyback yield % = 1.783
FCF/NI annual (oldest first) = [148.6%, 298.7%, 161.6%, 125.0%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 23.977 / 9.077 / 63.665  (n=20 quarters)

SBC block (TTM, advisory — no score effect)
  SBC 32,736,000.0   FCF 471,299,000.0   Market cap 7,452,989,440.0
  SBC/FCF = 6.9%
  FCF yield (reported)  = 6.32%
  FCF yield after SBC   = 5.88%
Advisory flags (no score effect; † = uncalibrated placeholder threshold)
  cycle_peak             UNKNOWN                EPS TTM now or 1y ago unavailable
  value_trap_candidate   UNKNOWN                forward PE or trailing EPS growth unavailable
```

*Note:* the script's market-cap-based lines (Forward PE, FCF yield, EV/EBIT, SBC yield, buyback yield) use yfinance's $244.34 prior close, not the $252.86 live price. They do not feed the Quality Score, so nothing below depends on them. The first two yfinance attempts were rate-limited (`YFRateLimitError`) and the third succeeded; no data was estimated.

### 3.1 Advisory flags — how each was handled
`python -m scripts.scoring.flags_common --eps-now 20.05 --eps-prior 9.08 --forward-pe 9.0 --eps-growth 28.7`:
```
  cycle_peak             CYCLE_PEAK_CANDIDATE   EPS TTM +121% > 100%† — state why the multiple is compared with a normalised base
  multiple_ceiling       NONE                   forward PE 9.0, EPS growth 28.7%
  value_trap_candidate   NONE                   forward PE 9.0, EPS TTM growth +120.8%
```
- **Basis caveat (data gap):** yfinance's quarterly statements gave only 5 quarters, so the script's GAAP-EPS flags stayed `UNKNOWN`. The run above uses **reported adjusted EPS** from yfinance `earnings_dates` — TTM now 7.58+5.80+3.59+3.08 = **$20.05**; a year ago 3.48+2.51+1.63+1.46 = **$9.08** — a proxy, not the GAAP basis the flag defines. GAAP TTM now = 6.92+5.00+3.09+2.81 = $17.82 vs. FY2025 GAAP $9.38 (the exact GAAP prior-TTM figure is **UNKNOWN**).
- **`cycle_peak` — RAISED (proxy basis).** Handling: the gate fails regardless, so no multiple is being "normalised" for a decision; recorded as a standing caution for any future re-evaluation (earnings roughly doubled year over year, including an acquisition; a forward PE of ~9× is partly a peak-earnings artefact if AI-data-center site work normalises).
- `multiple_ceiling`, `value_trap_candidate`: NONE. SBC/FCF = 6.9% (well under the 30% line).

## 4. Phase 01 — Quality Score (script output, verbatim)

Inputs file built from the fundamentals above plus manual fields. Manual/qualitative inputs and sources:
- **Gross-margin structural trend = True:** yfinance annual statements — gross profit/revenue FY2022 15.5% → FY2023 17.1% → FY2024 20.1% → FY2025 23.0% → TTM 23.8%.
- **TAM evidence = True** (cited in the input): STRL Q3 2026 call (2026-10-29, Motley Fool transcript) — total scoped work ~$8B (+~90% YoY); E-Infrastructure scoped work ~$7B (+130%); Q3 revenue $1.56B (+127%, ~70% organic); FY2026 revenue guidance raised to $4.63–4.73B (adjusted EPS $21.70–$21.96).
- **Growth decelerating = False** (revenue +127% YoY).
- **Moat:** only two signals have any evidence — market share (growth proxy, no independent share statistic) and brand premium (margin expansion, partly mix). Network effect, switching costs and scale advantage are **False because no evidence was obtained**, not because they were disproven; this is conservative, and §4.1 tests the opposite assumption.
- Hard disqualifiers: FCF positive 3+ years ✔; annual FCF/NI all >70% ✔ (a very high ratio mostly reflects a working-capital-light, growing contractor); Net Debt/EBITDA −0.05× ✔; SBC/FCF 6.9% ✔. None fired — the failure is purely the weighted score.

```
## Quality Score

**Profitability (25%)**
NetMargin_Component = clamp((12.851248923701384/30)x100) = 42.84
ROIC_Component = clamp((43.209184207043656/30)x100) = 100.00
Profitability_Score = (42.84 + 100.00) / 2 = 71.42
**Margins (15%)**
GrossMargin_Score = clamp((23.778259069308298/80)x100) = 29.72
+10 structural-trend bonus -> clamp(29.72+10, 0, 100) = 39.72
**Growth (20%)**
Growth_Score = clamp((12.061821692444695/25)x100) = 48.25
+10 TAM/pricing-power evidence (see above)
Growth_Score (final, clamped) = 58.25
**Balance Sheet (15%)**
BalanceSheet_Score = clamp(100x(1 - -0.045271696120054/4)) = 100.00
**Moat Signal (15%)**
market_share_stable_or_growing True | brand_premium True | network_effect False | switching_costs False | scale_cost_advantage False
Moat_Score = (2/5) x 100 = 40.00
**FCF Quality (10%)**
FCFQuality_Score = clamp(((0.7912 - 0.40)/0.60)x100) = 65.19  [ratio = (FCF - SBC)/NI]
**Quality Score — Final**
Quality Score = (71.42x0.25) + (39.72x0.15) + (58.25x0.20) + (100.00x0.15) + (40.00x0.15) + (65.19x0.10)
= 62.982 -> rounds to 63.0
```

# Quality Score = 63.0 — FAILS the 80.0+ gate

### 4.1 Sensitivity (each re-run through `quality_score.py`)

| Variant | Quality Score | Gate |
|---|---|---|
| **Base (evidence-backed moat only)** | **63.0** | FAIL |
| All five moat signals True (no evidence for three of them) | 72.0 | FAIL |
| All five moat signals True **and** revenue CAGR forced to 40% (vs. actual 12.1%, which is blended with a pre-boom base) | 80.3 | pass — *only* under two unsupported assumptions together |

The failure is driven by **net margin 12.85%** (sub-score 42.8; the 30% saturation point is a high bar for a contractor), **gross margin 23.8%** (sub-score 39.7 even with the trend bonus), and a thin moat. It is a structural fit problem — a project-based construction/site-development contractor does not look like the high-margin compounders the gate is built around — not a data glitch. The sharp recent growth is real but is captured only in part by the 3-year revenue CAGR; the forward-looking evidence already earned its +10 bonus.

## 5. Why the stock fell despite a strong quarter (context only, not a score input)
Sources (secondary, not primary filings): Q3 call transcript and slide summaries (Oct 29), plus commentary pieces. No company-issued reason exists.
- **Q3 results (company):** revenue $1.56B (+127%, ~70% organic, rest from the CEC acquisition); adjusted EPS $7.58 (+118%) vs ~$6.17 expected; GAAP EPS $6.92; adjusted EBITDA $337.8M (margin 21.6%, ~100bp lower YoY); total scoped backlog ~$8B (+11% QoQ); net cash $122M ($217M cash, $95M debt); 9-month operating cash flow $427M; buybacks $107M year to date. FY2026 guidance raised to revenue $4.63–4.73B, adjusted EPS $21.70–21.96.
- **Concerns raised in commentary:** possible peak in E-Infrastructure margins (management guides Q4 margin lower, ~19% implied vs 21.6% in Q3, with non-core CEC wind-down and weather); a signed-backlog softness worry before the report (signed $4.1B plus $2.0B unsigned awarded and $1.7B in design — more of the visibility is unsigned); Building Solutions (residential) revenue −5% and adjusted operating income −39%; Texas permitting friction; and spillover from a wider AI/data-center equity selloff (one commentator). Trefis put the 10/6–10/23 decline at 37%.
- **Not verified:** the exact trigger of the last leg down (−21%/−14% daily figures in search snippets conflict; one source shows +4.9% on report day). Per Rule 9 the >15% move is a re-evaluation trigger, which this session is; the framework never acts on price alone.
- **CEC acquisition** date, price and funding were **not found** in the sources read — not estimated.

## 6. Recommendation
**PASS — Phase 01 FAIL (Quality Score 63.0 < 80.0). Not valuation-scored; no order set; no decision log (no trade).** The business is growing extremely fast, is net-cash and cash-generative, and trades at ~9× forward earnings, but the framework's quality gate screens on margin level and moat evidence, and STRL's 12.9% net / 23.8% gross margins and evidence-thin moat keep it ~17 points short. Reconsider only if (a) a better-evidenced moat case is documented (each additional moat signal adds +3.0 points to the score), and/or (b) margins keep expanding — the gate needs roughly +17 points, which no realistic single change delivers — so this is a durable pass absent a structural shift. A cheap-looking stock after a 75% drawdown is exactly where the graveyard-audit lessons (cycle-peak earnings, backlog quality) apply.

## 7. Known risks, open items, honest caveats
- Cycle-peak flag raised on a proxy EPS basis; GAAP prior-TTM EPS is a data gap (§3.1).
- Moat inputs: three of five signals False for **lack of evidence**, not disproof (§4, §4.1).
- Rate Gate and valuation not run (gate failed) — no fair value was derived.
- Bid/ask on the live read was wide (245.00/269.29); last-trade price used.
- Backlog/guidance figures come from secondary transcript summaries, not the 10-Q/8-K.

## 8. Next review trigger
None scheduled (Phase 01 FAIL has no score to go stale). Re-evaluate on: a documented structural change in margins or moat evidence; the Q4 2026 report (~2027-02-24) only if a user request or Rule 9 event warrants.

---

## Glossary

**Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria (profitability, margins, growth, balance sheet, moat signal, FCF quality) instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. See [quality-scoring.md](quality-scoring.md).
**Rule 0**: This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
**Rule 9**: This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
**SBC (Stock-Based Compensation)**: Employee pay in the form of company shares or stock options rather than cash. A non-cash expense added back in cash-flow statements (inflating FCF relative to GAAP net income), but a real economic cost to existing shareholders through ongoing dilution — worth tracking alongside FCF/NI conversion and share-count trend, not just the headline FCF figure. Since the 2026-10-12 methodology it is treated as a cost in both the FCF yield (Valuation) and FCF Quality (Quality).
**FCF**: Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
**FCF Yield**: Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
**EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure.
**Forward PE**: Price ÷ next twelve months' *expected* earnings per share (vs. Trailing PE, which uses the last twelve months' actual earnings).
**ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
**Moat**: Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
**Hard disqualifier**: One of three Quality Score conditions ([quality-scoring.md](quality-scoring.md)) that fails a company regardless of its weighted sub-score total: not FCF-positive for 3+ consecutive years, Net Debt/EBITDA over its applicable threshold, or an FCF/Net Income conversion ratio under 70% for 2+ consecutive years without a documented growth-capex explanation. A weighted average can't average away an outright balance-sheet or cash-flow-quality failure.
**Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
**EPS**: Earnings Per Share — net income divided by number of shares outstanding.
**Backlog**: The dollar value of signed customer orders not yet recognized as revenue — a forward demand-visibility signal for hardware/equipment makers with long order-to-delivery cycles. Ciena's backlog grew >$600M sequentially to a record $7.7B in Q2 FY2026, with management stating >80% of current hardware backlog is expected to convert to revenue within 12 months — cited as documented TAM-expansion evidence for the Growth sub-score's +10 modifier in this framework's CIEN sessions.
**Cycle peak**: The top of a business cycle, when earnings are temporarily inflated (e.g. memory-chip prices at a high). A stock then looks cheap on trailing earnings exactly when it is most expensive on normal earnings. This framework flags it when trailing EPS grew more than 100% in a year.
**TTM (Trailing Twelve Months)**: The most recent 12 months of reported financial results (the last four quarters added together), as opposed to a single fiscal year or a forward-looking estimate. *(New term.)*
**Scoped work (STRL)**: Sterling Infrastructure's broader backlog measure — signed backlog plus unsigned awards and next phases still in design — that management quotes (~$8B at 2026-09-30) alongside the narrower "signed backlog" ($4.1B). Only signed backlog is contractually firm; the gap between the two is a visibility-quality question. Cited in this framework's 2026-11-06 STRL session. *(New term.)*
**CEC (Sterling acquisition)**: An electrical-contracting business Sterling Infrastructure acquired and now reports inside its E-Infrastructure segment (about a third of that segment's Q3 2026 revenue). The sources read for the 2026-11-06 STRL session did not give the full name, acquisition date, price or funding, so none of those are stated. *(New term.)*
