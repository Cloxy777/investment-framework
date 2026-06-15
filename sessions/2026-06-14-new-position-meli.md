# NEW POSITION — MELI (MercadoLibre, Inc.) — 2026-06-14

**Task type:** NEW POSITION
**Date:** 14 Jun 2026
**10Y US Treasury Yield:** 4.49% (CNBC/TradingEconomics, market close Fri 12 Jun 2026 — most recent available; markets closed Sun 14 Jun)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket) — **not reached**, see below
**Current MELI portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md)); no prior watchlist entry exists
**Sector:** Latin American e-commerce (Mercado Libre marketplace + logistics) + Fintech (Mercado Pago — payments, credit/lending, asset management)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **~$1,589.60** | WebSearch: aggregator quote (Investing.com/Kraken-sourced), described as "current price," down −1.27% on the day. |
| Cross-check #1 | $1,607.80 (as of 5 Jun 2026; prior close $1,634.78) | WebSearch: aggregator quote (Investing.com-sourced) |
| Cross-check #2 | $1,672.83 (close, 2 Jun 2026) | WebSearch: stockanalysis.com price history reference |
| 52-week range | $1,495.00 – $2,645.22 | WebSearch (aggregator, Investing.com-sourced) |
| Analyst consensus PT | $2,216.96 average (24 analysts; high $2,800 / low $1,750); consensus rating "Buy" (20 buy / 0 sell / 4 hold) | WebSearch (aggregator, Investing.com-sourced) |

**Context:** The three price readings ($1,589.60 → $1,607.80 → $1,672.83, most-recent-first) form an internally consistent **declining sequence over the prior ~2 weeks**, all comfortably within the 52-week range and well below the 52-week high ($2,645.22, implying the stock has fallen ~40% from its high). $1,589.60 is the most recent of the three and is used as the live price. It sits **~6.3% above the 52-week low** ($1,495.00) and **~28% below the analyst consensus PT** ($2,216.96, i.e. ~39.5% upside implied by consensus).

⚠️ **Tooling flag:** Per the session brief, IBKR `get_price_snapshot`/`search_contracts` MCP tools were not attempted (returned "permission denied" for prior agents in this batch) — WebSearch used directly, with 2+ independent cross-checking queries as required.

---

## 2. Data Gathered (Phase 01 Inputs) & Sources

| Metric | Value | Threshold (strategy.md) | Source |
|---|---|---|---|
| **Net margin (TTM)** | **6.04%** (one reading) / **7.93%** (another TTM reading) | **>15%** | WebSearch aggregator (stockanalysis.com-derived), "as of June 12, 2026, profit margin is 6.04%"; alternate TTM reading 7.93% |
| Net margin (Q1 2026, most recent quarter) | 4.7% ($417M NI / $8.85B revenue) | >15% | WebSearch (8-K, SEC EDGAR via aggregator) |
| Net margin (annual history, computed) | FY2022 ≈4.6% ($482M/~$10.5B) · FY2023 ≈6.6–6.8% ($987M/~$14.5–15B) · FY2024 ≈9.1% ($1,911M/~$21B) · FY2025 9mo ≈7.1% ($1,438M/$20,134M) | >15% | WebSearch (8-K/10-K figures, SEC EDGAR via aggregator) |
| Gross margin | 50.68% | >40% | WebSearch (stockanalysis.com) |
| ROIC | 20.76% | >15% | WebSearch (stockanalysis.com-derived aggregator) |
| Revenue growth | Q1 2026 +49.0% YoY ($8.85B); TTM revenue $31.80B, +42.1% YoY | >10% (3yr CAGR) | WebSearch (stockanalysis.com) |
| Net debt | $4,682M (as of 31 Dec 2025) → $5,748M (as of 31 Mar 2026) — total debt $11.4–12.3B vs. cash & investments $6.6–6.7B | — | WebSearch (10-Q figures via aggregator) |
| Net Debt/EBITDA | ~2.36× (as of 24 Oct 2025, per Gurufocus-sourced aggregator); one source separately describes "leverage ratio <1x" (likely a different debt/EBITDA definition, e.g. gross debt vs. adjusted EBITDA on a different base) | <2× (strategy.md) / <2.5× (pre-screen) / <4× if Upgrade 5 (financial-subsidiary debt) applies | WebSearch (Gurufocus-derived aggregator; Fitch IG-upgrade commentary) |
| FCF (annual, "FCF" as reported by aggregators) | FY2024 $7.058B (+52.4% YoY) | positive 3yr | WebSearch (macrotrends-derived aggregator) |
| "Adjusted FCF" (company's own ex-fintech-funding metric) | FY2024 ~$1.3B (after $860M capex); Q2 2025 $454M; **Q1 2026 −$56M** | — | WebSearch (8-K commentary via aggregator) |

### Flags on data quality

1. **Net margin is the decisive Phase 01 metric and it fails by a wide margin.** Every reading found — TTM (6.04% / 7.93%), most recent quarter (4.7%), and every full fiscal year back to 2022 (4.6% / ~6.7% / 9.1% / ~7.1%) — is **well below the >15% threshold** in strategy.md (and below even the 12% pre-screen floor in valuation-scoring.md). MELI has **never** posted a >15% net margin in the years checked.
2. **FCF figures are conflicting and likely distorted by the fintech credit-portfolio business.** The headline "$7.058B FY2024 FCF, +52.4% YoY" (macrotrends-style) appears to be operating-cash-flow-based and swung heavily by Mercado Pago's loan originations/receivables — the company's own "adjusted free cash flow" (ex-fintech funding effects) is an order of magnitude smaller ($1.3B FY2024) and went **negative** in Q1 2026 (−$56M). This is exactly the kind of fintech/credit-flywheel distortion flagged in the session brief, but it is **moot** given the net margin failure below.
3. **Net Debt/EBITDA readings conflict** (~2.36× per one aggregator vs. "<1x leverage" per another) — likely different EBITDA/debt definitions (GAAP EBITDA vs. adjusted, gross debt vs. net). Not resolved, but also **moot** given the net margin failure.
4. Per the session brief's "Fast Grower" check (EPS growth >15% for 3+ years) — **not evaluated**, since Phase 01 fails before this question becomes relevant.
5. Per the session brief's FX/currency-distortion flag (Argentina, Brazil) — qualitatively, MELI's recent margin compression has been explicitly attributed (per company commentary found in search results) to **increased investment in shipping, credit, 1P retail, cross-border trade, fulfillment, and AI**, plus **competitive pressure in Brazil** and **higher loan-loss provisions** — i.e., the margin compression appears to be a **deliberate reinvestment + competitive-pressure story**, not primarily an FX-translation artifact, though FX effects on LatAm operations are a standing structural feature of this name not separately quantified here.

No metric in this table was invented or estimated — all figures trace to WebSearch results citing SEC 8-K/10-Q filings, stockanalysis.com, macrotrends, or Gurufocus via aggregator pages.

---

## 3. Phase 01 — Quality Gate

| Check | MELI Value | Threshold | Result |
|---|---|---|---|
| **Net margin** | **TTM 6.04–7.93%; Q1 2026 4.7%; FY2022–24 range ~4.6%–9.1%** | **>15%** (strategy.md) / >12% (pre-screen) | ❌ **FAIL — never above 15% in any period checked; currently ~6–8% and compressing further (4.7% most recent quarter)** |
| ROIC | 20.76% | >15% | ✅ PASS |
| Revenue CAGR / growth | TTM +42.1% YoY; Q1 2026 +49.0% YoY | >10% (3yr CAGR) / >8% (pre-screen) | ✅ PASS (on recent-growth basis; 3yr CAGR not separately computed — moot) |
| Gross margin | 50.68% | >40% or structurally expanding | ✅ PASS |
| FCF positive 3 consecutive years | Aggregator "FCF" figures positive (FY2024 $7.058B, +52.4% YoY); company's own "adjusted FCF" much smaller and went negative in Q1 2026 (−$56M) | required | ⚠️ Mixed / not cleanly resolved — moot given net margin fail |
| Net debt/EBITDA | ~2.36× (one source) vs. "<1x" (another, different basis) — conflicting | <2× (strategy.md) / <2.5× (pre-screen) | ⚠️ Conflicting readings — moot given net margin fail |
| FCF/NI conversion ratio 2yr | Not computed | >70% for 2+ consecutive years | Not evaluated — moot |
| Share issuance pattern | Not evaluated | not dilutive | Not evaluated — moot |
| Moat signal | Dominant LatAm e-commerce marketplace + Mercado Pago payments/credit flywheel — qualitatively strong, not formally scored | required | Not formally evaluated — moot |

### **Gate result: FAIL — on the Net Margin criterion (>15% required).**

MELI's net margin has **never exceeded ~9.1%** in any fiscal year from 2022 through the most recent TTM/quarterly readings (FY2022 ≈4.6%, FY2023 ≈6.6–6.8%, FY2024 ≈9.1%, FY2025 9-month ≈7.1%, TTM as of 12 Jun 2026 ≈6.04–7.93%, most recent quarter Q1 2026 = 4.7%). This is **less than half** the >15% threshold strategy.md's Phase 01 requires, and the trend is **currently compressing further** (most recent quarter is the lowest reading of the set), driven by deliberate reinvestment (logistics, credit, fulfillment, AI, cross-border, 1P retail) and competitive pressure in Brazil per company commentary.

Per the operating brief: **"If it fails, STOP — report exactly why, do not proceed to scoring."** Phase 02 (valuation scoring), the Rate Environment Gate, and the order-setup workup are **not performed** for MELI in this session.

---

## 4. Qualitative Notes (brief, for the watchlist record — not a scoring input)

- **Why margins are currently low:** Company commentary (via 8-K/earnings-release aggregation) attributes the Q1 2026 margin compression (operating margin fell to 6.9%, net margin to 4.7%) to ramped investment across shipping/logistics, credit (Mercado Pago lending), 1P retail, cross-border trade, fulfillment, and AI — alongside competitive pressure in Brazil and higher loan-loss provisions. Management guidance (per the same commentary) signals this is viewed internally as a **margin trough**, with a sequential recovery expected in H2 2026.
- **Moat assessment (qualitative, not gating):** MELI is the dominant e-commerce + payments platform across multiple Latin American markets, with a logistics network (Mercado Envios) and a credit/lending flywheel (Mercado Pago/Mercado Crédito) that together form a meaningful network-effect and switching-cost moat. This qualitative strength is **not sufficient** to override the quantitative Phase 01 net-margin failure under this framework's rules — Phase 01 is a hard quantitative gate, and Upgrade 4 (Turnaround Sub-Gate) is reserved for businesses that fail 2–4 *quality* criteria with insider buying and other specific conditions, which was not evaluated here (MELI fails on only one Phase 01 criterion, and the Turnaround path is for "fallen angels," not high-growth platforms in a deliberate reinvestment phase — a different situation than this sub-gate was designed for).
- **Bear/watch case:** If the margin trough described by management materializes into a durable recovery (net margin moving back toward or above the ~9% FY2024 level, and ideally trending toward the >15% Phase 01 bar over a longer horizon), MELI would merit a fresh Phase 01 pass attempt. Until then, the deliberate reinvestment thesis means **low margins are the current strategy**, not (yet) a "thesis broken" signal — this is explicitly **not** a Phase 06 exit-trigger situation (MELI isn't held), it's simply a **"not yet qualified"** situation for a new entry.

---

## 5. Recommendation

# **PASS (do not enter) — Phase 01 FAIL, not scored.**

MELI fails the Phase 01 quality gate on **net margin** (currently ~6–8% TTM / 4.7% most recent quarter, vs. the >15% threshold — never met in any period checked back to FY2022). Per the operating brief, scoring stops here: no Rate Environment Gate, no Phase 02 valuation score, and no order setup are produced.

This is **not a permanent "no"** — MELI is a high-quality LatAm platform business (ROIC 20.76%, gross margin 50.68%, revenue growth ~42–49% YoY) with a strong qualitative moat (e-commerce + logistics + fintech flywheel). The gate failure reflects a **currently deliberate reinvestment/margin-compression phase**, not a structurally broken business. Revisit if/when net margin shows a sustained recovery trend (management guidance points to H2 2026).

**Add MELI to the watchlist** (`not-in-portfolio/MELI/`) as "Phase 01 FAIL — not scored."

---

## 6. Next Review Trigger

**Date/event:** MELI's next quarterly earnings release (Q2 2026, expected ~August 2026) — re-check net margin trend specifically. If net margin shows a clear sequential recovery toward/above the FY2024 level (~9.1%) and a credible trajectory toward the >15% threshold, re-run the full Phase 01 gate. Earlier trigger if a >15% unexplained price move occurs (Rule 9) or a guidance revision / M&A / management-change event is announced.

**No position opened — nothing to log in `decisions/`.**
