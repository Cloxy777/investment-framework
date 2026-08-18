# 2026-08-18 — SCREENING: North America — NA-1 (Tech, Communication Services, Consumer Discretionary)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-1](../framework/screening-coverage-log.md) (North America: US + Canada; sector emphasis Tech, Communication Services, Consumer Discretionary). Selected per the rotation rule: **2026-07-28 was the oldest "Last screened" date** on the matrix (re-verified fresh against [screening-coverage-log.md](../framework/screening-coverage-log.md) at the start of this session — all five other rows carry 2026-08-01 or later; no concurrent run had touched the log first).

This was run as an **unattended scheduled routine** ("Twice-Weekly Universe Screening Slice," Tuesday/Saturday) with no interactive user present. This is a **re-screen of a previously-covered slice**, three weeks after its last pass ([2026-07-28 session](2026-07-28-screening-na1.md)) — the point of the rotation cadence is to catch ETF-composition churn and valuation moves, not just cover new ground.

---

## 0. Methodology

No interactive TIKR/Koyfin screener export was available — there was no user to ask, so per Step 0's documented unattended-session exception, this session went straight to the ETF-holdings fallback. **Flagged prominently: this is an approximate starting pool (regional quality-factor ETF constituents), not a true full-universe sweep — small/mid-cap names outside MOAT/QUAL/QGRW's top-25 holdings are structurally invisible to this pass.**

- **EODHD was NOT used**, despite this run's task prompt again referencing an `EODHD_API_KEY`/"Path A" and calling this a "Monthly" slice. That path was deprecated and removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly says to treat that credential as compromised if it's ever needed again. The canonical [screen.md](../.claude/commands/screen.md) and [automation-schedule.md](../framework/automation-schedule.md) have no EODHD path, and automation-schedule.md documents Routine 4 as twice-weekly, not monthly. This is at least the sixth consecutive rotation session (after 2026-06-30 Japan, 2026-07-04 NA-2, 2026-07-07 NA-1, 2026-07-14, 2026-07-28 NA-1, 2026-08-04 EM) to hit this identical stale-prompt mismatch. CLAUDE.md instructs treating `framework/` as the source of truth over a stale prompt, so that's what this session did.
- **`yfinance`/direct Yahoo access was attempted first** (the framework's documented standard per-candidate source), installed cleanly, and failed immediately on a live request against `AAPL`:
  ```
  SSLError: Failed to perform, curl: (35) Recv failure: Connection reset by peer.
  ```
  Identical failure mode to every rotation session since 2026-07-07 — a persistent environment-level network block, not a transient rate limit.
- **Fell back to `stockanalysis.com`**, same precedent as every recent rotation session. Confirmed reachable before proceeding. Pulled three pages per candidate — `/stocks/<ticker>/financials/` (Gross Margin, Net Margin, Revenue history), `/stocks/<ticker>/financials/ratios/` (ROIC, EV/EBIT, Net Debt/EBITDA, FCF Yield), and `/stocks/<ticker>/financials/cash-flow-statement/` (Free Cash Flow history, for the 3-consecutive-year positivity check) — via `WebFetch`, parsed from each page's rendered tables.
- **Starting universe rebuilt from fresh ETF holdings** (MOAT, QUAL, QGRW top-25 each, pulled fresh via `stockanalysis.com/etf/<ticker>/holdings/`, current as of 2026-08-18). Composition has churned since the 2026-07-28 pass:
  - **New to the top-25 union this round:** CPRT (MOAT)
  - **Dropped out of the top-25 union this round:** WMT (re-entered 07-28, dropped again this round), FICO (was a QUAL top-25 name 07-28, no longer appears)
  - **Confirmed still absent (per task instruction, explicitly re-checked):** APP and QCOM, both 07-07 candidates dropped from all three ETFs' top-25 as of 07-28, remain absent from all three lists this round too — not re-tested, pure ETF-composition churn, can be pulled back via a direct `/new-position` on request.

---

## 1. Deduplicated starting universe → structural triage (Step 1)

Combining the three fresh ETF lists gives **57 raw names** (same count as the last two rounds, different composition). After removing current portfolio holdings ([holdings.md](../portfolio/holdings.md): ADBE, AMZN, AVGO, GOOG, META, MSFT, NFLX, NVDA, V, VEEV — 10 names present in this round's union, tracked via `/rescore` rather than re-discovered here), **47 candidates** remain.

Structural triage eliminated names on the same well-documented business-model grounds established in every prior NA-1/NA-2 rotation (flagged transparently so any can be pulled back on request):

| Eliminated | Why (structural, not measured) |
|---|---|
| COST, ROST, TJX | Large-volume retail — net margins structurally 2–6% |
| XOM | Integrated oil major — commodity-cyclical margins/revenue |
| MAS | Building products — mid-single-digit net margins, cyclical |
| MDLZ, KVUE, CLX, STZ, BF.B | Packaged consumer staples — low-single-digit revenue growth |
| BMY, MRK, JNJ | Large pharma, well-documented patent-cliff cycles |
| DHR, ZBH, GEHC, OTIS | Industrials/medtech stalwarts — mid-teens margins, mid-single-digit growth |
| CAT, GE, GEV | Cyclical industrials |
| EL | Documented margin-compression/turnaround phase |
| LIN | Industrial gases — ~20% margins but historically mid-single-digit growth |
| MU | Memory semiconductor — margin-*stability* failure by category |
| SCHW | Broker-dealer — same thin-margin brokerage-model exclusion as LPLA (tested quantitatively below) |

**24 names eliminated. 23 remain** for the real, sourced quantitative pull: **AAPL, ABNB, ADP, AMAT, AMD, ANET, BR, BRK.B, CPRT, CSCO, DDOG, FTNT, GOOGL, KLAC, LLY, LPLA, LRCX, MA, MRVL, ORCL, PANW, PLTR, TYL**.

Of these, 21 were also survivors of the 2026-07-28 triage; **CPRT** and **GOOGL** are new entrants this round — CPRT via fresh ETF composition churn (MOAT), GOOGL because it's a distinct ticker (Alphabet Class A) from the already-held GOOG (Class C) and appeared in QUAL's top-25 this round. **FICO** (tested 07-07/07-28) dropped out of all three ETFs' current top-25 and is not re-tested this round — same treatment as APP/QCOM.

---

## 2. Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, 2026-08-18)

Filters per [valuation-scoring.md](../framework/valuation-scoring.md#quantitative-pre-screen-filters-phase-01): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8%, FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, FCF yield >4%, EV/EBIT <20x. Basis is TTM (current) unless flagged otherwise; ROIC is stockanalysis.com's direct "Return on Invested Capital" line where shown, ROCE substituted (flagged) where ROIC wasn't rendered on the page.

| Ticker | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF Yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 48.65% ✅ | 27.62% ✅ | 101.57% ✅ | ~5.0% ❌ | ✅ | -0.37x ✅ | 3.06% ❌ | 28.40x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| ABNB | 82.90% ✅ | 20.45% ✅ | 25.70% ✅⚠️(ROCE) | 10.84% ✅ | ✅ | -3.47x ✅ | 4.49% ✅ | 36.02x ❌ | **FAIL — EV/EBIT only miss (tightest single-filter miss on filter count, though the gap itself is wide)** |
| ADP | 48.65% ✅ | 20.11% ✅ | 60.48% ✅ | 6.73% ❌ | ✅ | 0.18x ✅ | 4.88% ✅ | 18.64x ✅ | **FAIL — Revenue CAGR only miss, narrowly (6.73% vs 8%, −1.27pp) — TTM data clean this round, no artifact** |
| AMAT | 49.40% ✅ | 30.05% ✅ | 36.26% ✅ | ~5.2% ❌ | ✅ | -0.26x ✅ | 1.39% ❌ | 41.70x ❌ | FAIL — growth, FCF yield, EV/EBIT miss (EV/EBIT eased from 07-28's 49.33x) |
| AMD | 55.72% ✅ | 15.58% ✅ | 9.77% ❌ | 18.51% ✅ | ✅ | -0.92x ✅ | 1.02% ❌ | 125.05x ❌ | FAIL — ROIC, FCF yield, EV/EBIT miss (net margin newly clears vs. 07-28's 13.37%) |
| ANET | 63.00% ✅ | 38.37% ✅ | 284.77% ✅⚠️ | 24.3% ✅ | ✅ | -2.88x ✅ | 2.03% ❌ | 53.04x ❌ | FAIL — FCF yield, EV/EBIT miss (EV/EBIT widened further from 07-28's 48.78x) |
| BR | 31.78% ❌ | 15.04% ✅ | 17.03% ✅ | 7.8% ❌ | ✅ | 1.72x ✅ | 6.58% ✅ | 17.34x ✅ | **FAIL — Gross Margin & Revenue CAGR miss only; Rev CAGR miss is razor-thin (7.8% vs 8%, −0.2pp)** |
| BRK.B | 30.33% ❌ | 22.30% ✅ | 19.28% ✅⚠️ | 2.7% ❌ | ✅ | -1.81x ✅ | 2.27% ❌ | 7.13x ✅⚠️ | FAIL — conglomerate; margin, growth, FCF yield miss (ROIC read flipped to a pass this round — see data gaps) |
| CPRT | 47.52% ✅ | 33.48% ✅ | 29.98% ✅ | ~6.4% ❌ | ✅ | -2.09x ✅ | 4.56% ✅ | 14.41x ✅ | **FAIL — Revenue 3yr CAGR only miss (6.4% vs 8%, −1.6pp) — new candidate this round, clears 7 of 8 filters** |
| CSCO | 64.56% ✅ | 20.95% ✅ | 20.65% ✅ | 5.89% ❌ | ✅ | 0.73x ✅ | 2.88% ❌ | 28.40x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| DDOG | 79.54% ✅ | 4.48% ❌ | 2.91% ❌ | 27.2% ✅ | ✅ | -44.73x ✅⚠️ | 1.33% ❌ | 4424x ❌⚠️ | FAIL — margin, ROIC, FCF yield miss; EV/EBIT a near-zero-EBIT-denominator artifact, not meaningful |
| FTNT | 80.20% ✅ | 28.17% ✅ | 40.50% ✅⚠️(ROCE) | 12.7% ✅ | ✅ | -1.35x ✅ | 2.73% ❌ | 45.49x ❌ | FAIL — FCF yield, EV/EBIT miss (both eased slightly vs. 07-28's 2.22%/48.38x) |
| GOOGL | 60.90% ✅ | 54.75% ✅⚠️ | 24.93% ✅ | 15.1% ✅ | ✅ | -0.70x ✅ | 1.27% ❌ | 27.67x ❌ | **FAIL — FCF yield, EV/EBIT miss — new candidate this round; excellent quality/growth profile, blocked purely by valuation** |
| KLAC | 61.30% ✅ | 35.57% ✅ | 66.75% ✅ | 8.77% ✅ | ✅ | 0.21x ✅ | 1.40% ❌ | 47.71x ❌ | FAIL — FCF yield, EV/EBIT miss |
| LLY | 83.40% ✅ | 33.53% ✅ | 42.24% ✅ | 40.9% ✅⚠️ | ✅ | 1.08x ✅ | 1.69% ❌ | 28.27x ❌ | FAIL — FCF yield, EV/EBIT miss (both eased from 07-28's 1.11%/35.07x) |
| LPLA | n/a ⚠️ | 5.24% ❌ | 11.54% ❌ | 22.0% ✅ | ❌ | n/a ⚠️ | -3.24% ❌ | n/a ⚠️ | FAIL — thin-margin brokerage model; 4 of 5 measurable filters miss (3 unavailable this session, see data gaps) |
| LRCX | 50.47% ✅ | 31.27% ✅ | 70.06% ✅ | 10.7% ✅ | ✅ | -0.17x ✅ | 1.14% ❌ | 52.29x ❌ | **FAIL — FCF yield, EV/EBIT miss — but Revenue CAGR clears the 8% bar for the first time in this slice's history (was 2.29% on 07-28)** |
| MA | 100.00% ✅⚠️ | 46.34% ✅ | 93.78% ✅ | 12.9% ✅ | ✅ | 0.58x ✅ | 3.39% ❌ | 24.06x ❌ | **FAIL — FCF yield & EV/EBIT both close misses (3.39% vs 4%; 24.06x vs 20x)** |
| MRVL | 51.50% ✅ | 28.99% ✅ | 6.87% ❌ | 11.45% ✅⚠️ | ✅ | 0.53x ✅ | 0.81% ❌ | 144.44x ❌ | FAIL — ROIC, FCF yield, EV/EBIT miss (Rev CAGR corrected to FY-anchored 11.45%, see data gaps) |
| ORCL | 65.82% ✅ | 25.21% ✅ | 11.48% ❌ | 10.98% ✅ | ❌ | 4.45x ❌ | -5.61% ❌ | 24.93x ❌ | FAIL — AI/OCI capex surge continues to push FCF further negative (FY2026 FCF −$23.7B, matching 07-28); ROIC, leverage, EV/EBIT also miss |
| PANW | 71.96% ✅ | 7.95% ❌ | 3.65% ❌ | 18.6% ✅ | ✅ | -0.66x ✅ | 1.24% ❌ | 315.42x ❌ | FAIL — net margin still below 12% bar (unchanged story since 07-28); ROIC, FCF yield, EV/EBIT also miss (EV/EBIT worsened further from 252.61x) |
| PLTR | 84.80% ✅ | 49.00% ✅ | 363.80% ✅⚠️ | 37.2% ✅ | ✅ | -3.45x ✅ | 0.81% ❌ | 153.89x ❌ | FAIL — FCF yield, EV/EBIT miss (still one of the most extreme valuations on the list) |
| TYL | 47.21% ✅ | 13.36% ✅ | 8.57% ❌ | 8.97% ✅ | ✅ | 1.06x ✅ | 5.44% ✅ | 36.24x ❌ | **FAIL — ROIC & EV/EBIT miss only; Revenue CAGR now clears comfortably (was a repeated borderline pass, 8.02–8.03%, in the last two rounds)** |

*⚠️ = figure carries a data-quality caveat, see Section 4.*

Source: `stockanalysis.com` financials/ratios/cash-flow-statement pages per ticker, pulled 2026-08-18 via `WebFetch` (23 tickers × up to 3 page fetches = 68 page fetches, LPLA missing 3 of its 8 fields).

---

## ✅ Qualified Quality List — **0 names**

**Zero of the 23 candidates clear the full Phase 01 gate** — the fourth consecutive result of 0 for this slice (07-07, 07-28, and the original 06-07 pass also found 0). This continues to read as a real, sourced finding rather than a screening gap: every candidate that clears the business-quality filters (margins, ROIC, growth, balance sheet) is stopped by the valuation filters (FCF yield <4%, EV/EBIT <20x) — the near-misses below are overwhelmingly single- or double-filter misses on *growth* or *cheapness*, never on quality.

**Qualified-name count vs. prior round: 0 → 0, unchanged.** What changed underneath the unchanged headline number:
- **Three names now sit exactly one filter away from qualifying** (up from two on 07-28: ABNB, ADP, BR): **ADP** (Revenue CAGR only, −1.27pp), **CPRT** (Revenue CAGR only, −1.6pp, brand-new candidate), and **ABNB** (EV/EBIT only, unchanged story). BR is a close second at two misses, one of which (Revenue CAGR, −0.2pp) is the single tightest miss of any filter this round.
- **LRCX's Revenue 3yr CAGR cleared the 8% bar for the first time in this slice's recorded history** (2.29% on 07-28 → 10.7% now) — a real AI-capex-driven recovery from the FY2024 revenue dip, not a data artifact (cross-checked against the underlying FY revenue series). Still fails on FCF yield/EV/EBIT.
- **TYL's Revenue CAGR moved from a repeated knife-edge pass (8.02–8.03% the last two rounds) to a comfortable 8.97%** — same underlying quality story, just less fragile now.
- **ADP's data quality improved**: the 07-28 session flagged ADP's TTM column as internally inconsistent (a stockanalysis.com artifact) and substituted FY2025 figures. This round's TTM column is clean and self-consistent — no substitution needed.

**Near-misses worth flagging for a future rotation or a dedicated look regardless:**
- **ADP** (1 filter) — misses only Revenue 3yr CAGR (6.73% vs 8%, the narrowest gap of any single-filter-miss name this round in absolute terms); everything else clears comfortably, including EV/EBIT (18.64x) and FCF yield (4.88%). Third consecutive round flagging this exact story.
- **CPRT** (1 filter, **new candidate**) — Copart misses only Revenue 3yr CAGR (~6.4% vs 8%); every other filter clears, several strongly (ROIC 29.98%, EV/EBIT 14.41x, Net Debt/EBITDA −2.09x net cash). Worth a dedicated `/new-position` look.
- **ABNB** (1 filter) — misses only EV/EBIT (36.02x vs <20x, a wide absolute gap that has widened every round: 30.54x → 29.97x → 36.02x); every quality/growth/balance-sheet filter clears comfortably.
- **BR** (2 filters) — Broadridge misses Gross Margin (31.78% vs >40%) and Revenue 3yr CAGR, the latter by just 0.2pp (7.8% vs 8%) — the single tightest miss of the round on any filter. Every valuation filter (EV/EBIT 17.34x, FCF yield 6.58%, Net Debt/EBITDA 1.72x) clears comfortably.
- **TYL** (2 filters) — misses ROIC (8.57% vs >15%) and EV/EBIT (36.24x vs <20x); Revenue CAGR now clears solidly.
- **MA** (2 filters) — FCF yield 3.39% (vs >4%) and EV/EBIT 24.06x (vs <20x), both near the bar; every quality filter clears strongly (ROIC 93.78%, net margin 46.34%).

**Notable changes worth flagging (real events, not screening artifacts):**
- **LRCX** — Revenue 3yr CAGR jumped from 2.29% (07-28) to 10.7%, driven by a sharp FY2026 revenue recovery ($14,905M FY2024 → $18,436M FY2025 → $23,233M TTM/FY2026) consistent with continued AI-capex demand for wafer-fab equipment. First round this filter has cleared for LRCX in this slice's history.
- **MRVL** — Revenue growth also strengthened materially, reflecting its AI/custom-silicon ramp (FY2026 revenue $8,195M vs FY2023's $5,920M) — see data-gap note below on the exact CAGR figure used.
- **AI-capex-adjacent semicap/networking cohort (LRCX, AMAT, KLAC, ANET, FTNT) — EV/EBIT trend is now mixed, not uniformly widening.** AMAT (49.33x→41.70x) and FTNT (48.38x→45.49x) eased back from 07-28's extremes; LRCX (48.96x→52.29x), KLAC (45.92x→47.71x), and ANET (48.78x→53.04x) ticked further up. Reads as valuation dispersion within the cohort rather than a single-direction re-rating.
- **AMD, CSCO** — net margins improved meaningfully (AMD 13.37%→15.58%; CSCO 19.69%→20.95%), both now clearing the 12% bar more comfortably than 07-28; neither changes the overall FAIL (both still miss ROIC/FCF yield/EV/EBIT independently).
- **ORCL** — the AI/OCI capex-driven FCF collapse flagged 07-28 persists unchanged: FY2026 FCF −$23,686M (matches 07-28's −$23.7B almost to the dollar), still failing FCF-3yr-positivity, leverage, FCF yield, and EV/EBIT.
- **CPRT, GOOGL** — both new to the tested pool this round (ETF-composition churn for CPRT; GOOGL a distinct Class-A ticker from the already-held GOOG for the first time appearing in QUAL's top-25). Neither previously evaluated in this slice.
- **APP, QCOM** — still absent from all three ETFs' top-25 as of this round (confirmed per this run's explicit re-check instruction), unchanged since dropping out on 07-28. **FICO** newly dropped out this round (was tested 07-07 and 07-28).

---

## 3. Qualitative pass (Step 3)

**Not applicable this rotation** — zero candidates cleared the quantitative gate to advance to a qualitative review, per Step 3's scope ("For each name that clears the quantitative gate...").

---

## 4. Data gaps and caveats (Step 4)

- **`yfinance`/direct Yahoo access failed with the same TLS connection-reset error** seen in every rotation session since 2026-07-07 — flagged again for `/healthcheck` (Routine 7) to pick up; this is now a persistent environment-level network block, not a transient issue. `stockanalysis.com` covered every metric needed this session except LPLA's three gaps below; no estimation was used anywhere in the table (CLAUDE.md Rule 0).
- **LPLA — Gross Margin, Net Debt/EBITDA, and EV/EBIT were not rendered on stockanalysis.com's ratios/financials pages this session** (unlike 07-28, which reported 23.43% / 2.66x / 19.15x for these same fields). Re-fetched with an explicit "list every ratio row" prompt and confirmed the page genuinely omits a Gross Margin line (LPLA's income statement has no separate Cost-of-Revenue line, consistent with a brokerage-model business) and doesn't surface Debt/EBITDA or EV/EBIT at all this session — flagged as unavailable rather than estimated. Doesn't change the verdict: LPLA already fails decisively on Net Margin (5.24% < 12%), ROIC (11.54% < 15%), FCF-3yr-positivity (negative FY2024/FY2025), and FCF Yield (−3.24%).
- **GOOGL's TTM Net Margin (54.75%) is a clear outlier** against its own FY2025 figure (32.81%) and FY2024 (28.60%) — the fetch itself flagged this as "warrant[ing] further investigation into one-time gains or accounting adjustments" (plausibly an unrealized gain on Alphabet's equity/derivative investment portfolio, not independently confirmed this session). Shown as reported rather than substituted; doesn't change the PASS on this filter either way (32.81% would still clear >12%), and doesn't change GOOGL's overall FAIL (blocked on FCF yield/EV/EBIT, unrelated to net margin).
- **MRVL's Revenue 3yr CAGR — model auto-calculated a two-year (~22.5%) figure using an inconsistent window (TTM vs. FY2024); corrected here to the FY-anchored 3-year convention used throughout this log (FY2026 vs. FY2023: (8,195/5,920)^(1/3) − 1 = 11.45%)**, which also matches the 07-28 session's own MRVL figure computed the same way — shown as 11.45% ✅ in the table above, flagged rather than silently substituted.
- **BRK.B's ROIC read (19.28%) is materially higher than every prior round's figure** (10.47% on 07-07, 5.01% on 07-28) — likely reflects stockanalysis.com switching which "ROIC" definition/period it surfaces for a conglomerate whose earnings mix (insurance float, investment portfolio, operating businesses) makes any single ROIC figure a poor fit regardless of value, a caveat already standing since 07-07. Doesn't change BRK.B's overall FAIL (margin, growth, and FCF yield all miss independently of this read).
- **MA's Gross Margin (100.00%)** is a data-structure artifact, not a real COGS-based margin — Mastercard's income statement carries no separate Cost-of-Revenue line, same standing note since 06-07/07-07/07-28. Doesn't change the FAIL verdict (MA fails on FCF yield/EV/EBIT, not margin).
- **BRK.B's EV/EBIT (7.13x)** clears the <20x bar but isn't meaningfully comparable for the same conglomerate-earnings-mix reason as above — standing caveat, doesn't change BRK.B's overall FAIL.
- **DDOG's Net Debt/EBITDA (−44.73x) and EV/EBIT (4424x)** are both mathematical artifacts of a near-zero EBITDA/EBIT denominator on an asset-light, large-net-cash balance sheet — shown as-is, doesn't change the FAIL either way.
- **ANET's ROIC (284.77%) and PLTR's ROIC (363.80%)** are, as in every prior round, inflated by a small invested-capital denominator on asset-light, large-net-cash balance sheets — flagged, not independently re-derived, doesn't change either name's FAIL (both blocked on FCF yield/EV/EBIT regardless).
- **TYL's Net Debt/EBITDA moved from "net cash" (07-28) to 1.06x this round** — a real balance-sheet change (still comfortably under the 2.5x bar either way), not a data artifact; flagged for visibility rather than left silent.
- **Stale automation prompt (process note, not a data gap):** this routine's scheduled prompt again described itself as a "Monthly" slice referencing the removed `EODHD_API_KEY`/"Path A." [automation-schedule.md](../framework/automation-schedule.md) currently documents this as a twice-weekly cadence with no EODHD path at all. This is at least the sixth consecutive rotation session to hit this same stale-prompt mismatch — same handling as every prior instance (CLAUDE.md instructs following the current, authoritative framework docs over a stale scheduler prompt), documented again here for the audit trail.

---

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md)'s NA-1 row updated: Last screened → 2026-08-18, Qualified names found → 0 (unchanged from 07-28; near-misses tightened — ADP and CPRT now the closest single-filter misses, ABNB unchanged single-filter miss, BR's Revenue CAGR miss the tightest of any filter this round), Sources used → MOAT/QUAL/QGRW ETF holdings + `stockanalysis.com` quantitative gate (yfinance/direct Yahoo access still blocked by a TLS connection-reset error this session, same failure mode since 2026-07-07).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **EV/EBIT** — Enterprise Value ÷ EBIT, a multiple measuring how expensive a company is relative to its operating profit; lower is cheaper.
- **FCF (Free Cash Flow)** — cash a business generates after running/maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher means cheaper.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue dollar left after direct production/delivery costs.
- **Net Debt/EBITDA** — net debt ÷ EBITDA, this framework's primary balance-sheet-leverage gate; lower (or negative, i.e. net cash) is safer.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue dollar left as accounting profit after every expense.
- **Phase 01** — this framework's Universe Screening / quality-gate stage, the subject of this session.
- **Qualified Quality List** — the output of Phase 01 screening: companies that passed the quality gate and are eligible for Phase 02 valuation scoring.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital (debt + equity) into profit.
- **ROCE (Return on Capital Employed)** — a close cousin of ROIC used as a substitute where stockanalysis.com didn't render a direct ROIC figure this session; measures operating profit relative to capital employed (debt + equity).
- **Rotation Matrix** — the [screening-coverage-log.md](../framework/screening-coverage-log.md) table that tracks which region/sector slice was screened when, so `/screen` systematically rotates through the whole investable universe instead of re-covering familiar names.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of financial results, regardless of fiscal-year boundary; used here as the "current" basis for most ratios.
