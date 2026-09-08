# 2026-09-08 — SCREENING: North America — NA-1 (Tech, Communication Services, Consumer Discretionary)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [NA-1](../framework/screening-coverage-log.md) (North America: US + Canada; sector emphasis Tech, Communication Services, Consumer Discretionary). Selected per the rotation rule: **2026-08-18 was the oldest "Last screened" date** on the matrix at session start (all five other rows carried 2026-08-22 or later — APAC-EX-JP 08-22, EM 08-25, EU 08-29, JP 09-01, NA-2 09-05).

This was run as an **unattended scheduled routine** with no interactive user present. Re-screen of a previously-covered slice, three weeks after its last pass ([2026-08-18 session](2026-08-18-screening-na1.md)).

---

## 0. Methodology

No interactive TIKR/Koyfin screener export was available — no user to ask, so per Step 0's documented unattended-session exception, this session went straight to the ETF-holdings fallback. **Flagged prominently: this is an approximate starting pool (regional quality-factor ETF constituents), not a true full-universe sweep — small/mid-cap names outside MOAT/QUAL/QGRW's top-25 holdings are structurally invisible to this pass.**

- **Stale scheduled-prompt mismatch, same as every rotation session since 2026-06-30:** this run's stored routine prompt again described itself as a "Monthly Universe Screening Slice" and instructed using an `EODHD_API_KEY` for automated "Path A" screening. Both are outdated. EODHD was deliberately removed from this framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which explicitly flags the committed `EODHD_API_KEY` as a **compromised credential not to be reused without rotation**. `framework/automation-schedule.md` documents Routine 4 as the **"Twice-Weekly Universe Screening Slice"** (Tuesday + Saturday, 14:00 UTC) — 2026-09-08 is a Tuesday, consistent with that real cadence, not the stale "first Saturday" description. The canonical `.claude/commands/screen.md` has no EODHD path at all. Per CLAUDE.md's instruction to treat `framework/` as the source of truth over a stale prompt, this session followed the current, authoritative `screen.md`/`automation-schedule.md` process end-to-end, including the Telegram/`.ics` steps Routine 4 specifies that the stale prompt omitted. `EODHD_API_KEY` was confirmed present in the environment but was **not** touched.
- **`yfinance`/direct Yahoo access was attempted first** (the framework's documented standard per-candidate source), installed cleanly, and failed immediately on a live request against `AAPL`:
  ```
  SSLError: Failed to perform, curl: (35) Recv failure: Connection reset by peer.
  ```
  Identical failure mode to every rotation session since 2026-07-07 — a persistent environment-level network block, not a transient rate limit.
- **Fell back to `stockanalysis.com`**, same precedent as every recent rotation session. Pulled three pages per candidate — `/stocks/<ticker>/financials/`, `/stocks/<ticker>/financials/ratios/`, `/stocks/<ticker>/financials/cash-flow-statement/` — via `WebFetch`, parsed from each page's rendered tables. Work was delegated across **5 parallel research agents** (1 for the ETF-holdings/structural-triage pass, 4 for the quantitative gate, 6 tickers each) to keep this session's own context bounded, matching the delegation pattern used in the 2026-09-05 NA-2 and 2026-08-25 EM sessions.
- **Revenue 3yr CAGR methodology tightened this round:** every batch was instructed to compute Revenue 3yr CAGR strictly as `(latest complete FY revenue / FY-3-years-earlier revenue)^(1/3) − 1`, never mixing a TTM numerator against an FY-anchored denominator. `valuation-scoring.md`'s Phase 01 filter list specifies "Revenue growth > 8% (3yr CAGR)" without pinning down the exact basis, and several approximate figures in the 08-18 log (flagged there with a `~` prefix, e.g. AAPL "~5.0%", AMAT "~5.2%") turn out to have blended bases. This is a **within-session rigor improvement, not a framework rule change** — no version bump needed (Phase 01 is a binary quality gate, not the scored valuation methodology `valuation-scoring.md`'s version header governs). Recomputed figures differ from 08-18's for several names (documented per-ticker below); no verdict flipped due to this alone **except CPRT** (see below), where the correction resolves what was actually a mixed-basis error in the prior two rounds' figure, not a business change.

---

## 1. Deduplicated starting universe → structural triage (Step 1)

Fresh MOAT/QUAL/QGRW top-25 holdings pulled 2026-09-08 via `stockanalysis.com/etf/<ticker>/holdings/`. Union = **58 raw names** (was 57 on 08-18). **All 57 of 08-18's names still appear this round — zero drop-outs, a first for this slice.** **CRM (Salesforce)** is the only new name, entering via QGRW's top-25.

After removing current portfolio holdings ([holdings.md](../portfolio/holdings.md): ADBE, AMZN, AVGO, GOOG, META, MSFT, NFLX, NVDA, V, VEEV — 10 names present in this round's union, tracked via `/rescore` rather than re-discovered here), **48 candidates** remain.

Structural triage eliminated names on the same well-documented business-model grounds established in every prior NA-1/NA-2 rotation (flagged transparently so any can be pulled back on request):

| Eliminated | Why (structural, not measured) |
|---|---|
| COST, ROST, TJX | Large-volume retail — net margins structurally 2–6% |
| XOM | Integrated oil major — commodity-cyclical margins/revenue |
| MAS | Building products — mid-single-digit net margins, cyclical |
| MDLZ, KVUE, CLX, STZ, BF.B | Packaged consumer staples — low-single-digit revenue growth |
| BMY, MRK, JNJ | Large pharma — well-documented patent-cliff cycles |
| DHR, ZBH, GEHC, OTIS | Industrials/medtech stalwarts — mid-teens margins, mid-single-digit growth |
| CAT, GE, GEV | Cyclical industrials |
| EL | Documented margin-compression/turnaround phase |
| LIN | Industrial gases — ~20% margins but historically mid-single-digit growth |
| MU | Memory semiconductor — margin-stability failure by category |
| SCHW | Broker-dealer — same thin-margin exclusion as LPLA |

24 eliminated, all recurring names with unchanged reasoning. **CRM (new name) — fresh judgment: not eliminated.** Salesforce is an enterprise SaaS/software business, the same category as other software names in the union (ORCL, ADP, PANW, FTNT, DDOG, TYL, BR) passed through to quantitative testing rather than structurally excluded — no business-model ground applies to it.

**24 names survive triage** — identical to 08-18's 23-name survivor list plus CRM: **AAPL, ABNB, ADP, AMAT, AMD, ANET, BR, BRK.B, CPRT, CRM, CSCO, DDOG, FTNT, GOOGL, KLAC, LLY, LPLA, LRCX, MA, MRVL, ORCL, PANW, PLTR, TYL**.

---

## 2. Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, 2026-09-08)

Filters per [valuation-scoring.md](../framework/valuation-scoring.md#quantitative-pre-screen-filters-phase-01): Gross margin >40%, Net margin >12%, ROIC >15%, Revenue 3yr CAGR >8% (FY-anchored, see methodology note above), FCF positive 3 consecutive years, Net Debt/EBITDA <2.5x, FCF yield >4%, EV/EBIT <20x. Basis is TTM/current unless flagged otherwise.

| Ticker | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF Yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| AAPL | 48.65% ✅ | 27.62% ✅ | 101.57% ✅ | 1.81% ❌ | ✅ | -0.37x ✅ | 2.93% ❌ | 29.75x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| ABNB | 82.90% ✅ | 20.45% ✅ | 25.70% ✅⚠️(ROCE) | 13.37% ✅ | ✅ | -3.47x ✅ | 4.53% ✅ | 35.68x ❌ | **FAIL — EV/EBIT only miss** (35.68x vs <20x) |
| ADP | 48.65% ✅ | 20.11% ✅ | 60.48% ✅ | 6.81% ❌ | ✅ | 0.18x ✅ | 4.76% ✅ | 19.13x ✅ | **FAIL — Revenue CAGR only miss** (6.81% vs 8%, −1.19pp) |
| AMAT | 49.40% ✅ | 30.05% ✅ | 35.64% ✅ | 3.23% ❌ | ✅ | -0.19x ✅ | 1.56% ❌ | 37.28x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| AMD | 55.72% ✅ | 15.58% ✅ | 9.77% ❌ | 13.64% ✅ | ✅ | -0.92x ✅ | 1.08% ❌ | 117.95x ❌ | FAIL — ROIC, FCF yield, EV/EBIT miss |
| ANET | 63.00% ✅ | 38.37% ✅ | 284.77% ✅⚠️ | 27.15% ✅ | ✅ | -2.88x ✅ | 2.11% ❌ | 50.82x ❌ | FAIL — FCF yield, EV/EBIT miss |
| BR | 31.78% ❌ | 15.04% ✅ | 17.03% ✅ | 7.25% ❌ | ✅ | 1.72x ✅ | 6.49% ✅ | 17.55x ✅ | FAIL — Gross Margin & Revenue CAGR miss only (6 of 8 clear) |
| BRK.B | 30.33% ❌ | 22.30% ✅ | 19.28% ✅⚠️ | 7.14% ❌ | ✅ | -1.81x ✅ | 2.24% ❌ | 7.27x ✅⚠️ | FAIL — conglomerate; margin, growth, FCF yield miss |
| **CPRT** | **47.52% ✅** | **33.48% ✅** | **29.98% ✅** | **9.90% ✅** | **✅** | **-2.09x ✅** | **4.29% ✅** | **15.47x ✅** | **✅ PASS — clears all 8 filters** |
| CRM | 77.28% ✅ | 21.99% ✅⚠️ | 10.96% ❌ | 9.82% ✅ | ✅ | 2.40x ✅⚠️ | 7.42% ✅ | 24.86x ❌ | **FAIL — ROIC & EV/EBIT miss only (new candidate, 6 of 8 clear)** |
| CSCO | 64.52% ✅ | 20.95% ✅ | 20.38% ✅ | 3.57% ❌ | ✅ | 0.82x ✅ | 2.97% ❌ | 27.73x ❌ | FAIL — growth, FCF yield, EV/EBIT miss |
| DDOG | 79.54% ✅ | 4.48% ❌ | 2.91% ❌ | 26.95% ✅ | ✅ | -44.73x ✅⚠️ | 1.55% ❌ | 3782.38x ❌⚠️ | FAIL — margin, ROIC, FCF yield miss; EV/EBIT a near-zero-EBIT-denominator artifact |
| FTNT | 80.20% ✅ | 28.17% ✅ | 40.50% ✅⚠️(ROCE) | 15.47% ✅ | ✅ | -1.35x ✅ | 2.77% ❌ | 44.72x ❌ | FAIL — FCF yield, EV/EBIT miss |
| GOOGL | 60.90% ✅ | 54.75% ✅⚠️ | 24.93% ✅ | 12.51% ✅ | ✅ | -0.70x ✅ | 1.29% ❌ | 27.21x ❌ | FAIL — FCF yield, EV/EBIT miss |
| KLAC | 61.30% ✅ | 35.57% ✅ | 66.75% ✅ | 8.96% ✅ | ✅ | 0.21x ✅ | 1.55% ❌ | 43.06x ❌ | FAIL — FCF yield, EV/EBIT miss |
| LLY | 83.40% ✅ | 33.53% ✅ | 42.24% ✅ | 31.69% ✅⚠️ | ✅ | 1.08x ✅ | 1.78% ❌ | 27.01x ❌ | FAIL — FCF yield, EV/EBIT miss |
| LPLA | n/a ⚠️ | 5.24% ❌ | 11.54% ❌ | 25.09% ✅ | ❌ | n/a ⚠️ | -3.32% ❌ | n/a ⚠️ | FAIL — thin-margin brokerage model; 4 of 5 measurable filters miss (3 unavailable) |
| LRCX | 50.47% ✅ | 31.27% ✅ | 70.06% ✅ | 10.06% ✅ | ✅ | -0.17x ✅ | 1.27% ❌ | 46.77x ❌ | FAIL — FCF yield, EV/EBIT miss |
| MA | 100.00% ✅⚠️ | 46.34% ✅ | 93.78% ✅ | 13.82% ✅ | ✅ | 0.58x ✅ | 3.29% ❌ | 24.77x ❌ | **FAIL — FCF yield & EV/EBIT miss only** |
| MRVL | 52.22% ✅ | 27.93% ✅ | 6.94% ❌ | 11.45% ✅⚠️ | ✅ | 0.48x ✅ | 0.88% ❌ | 124.24x ❌ | FAIL — ROIC, FCF yield, EV/EBIT miss |
| ORCL | 65.82% ✅ | 25.21% ✅ | 11.48% ❌ | 10.48% ✅ | ❌ | 4.45x ❌ | -5.18% ❌ | 26.49x ❌ | FAIL — AI/OCI capex FCF collapse persists (FY2026 FCF −$23,686M); ROIC, leverage, FCF yield, EV/EBIT also miss |
| PANW | 70.49% ✅ | 2.67% ❌ | 2.15% ❌ | 18.55% ✅ | ✅ | -0.31x ✅ | 1.51% ❌ | 269.42x ❌ | FAIL — net margin collapsed to 2.67% (was 7.95% on 08-18); ROIC, FCF yield, EV/EBIT also miss |
| PLTR | 84.80% ✅ | 49.00% ✅ | 363.80% ✅⚠️ | 32.90% ✅ | ✅ | -3.45x ✅ | 0.80% ❌ | 155.51x ❌ | FAIL — FCF yield, EV/EBIT miss |
| TYL | 47.21% ✅ | 13.36% ✅ | 8.57% ❌ | 8.02% ✅⚠️ | ✅ | 1.06x ✅ | 4.79% ✅ | 40.99x ❌ | **FAIL — ROIC & EV/EBIT miss only**; Rev CAGR a knife-edge pass (+0.02pp over the bar) |

*⚠️ = figure carries a data-quality caveat, see Section 4.*

Source: `stockanalysis.com` financials/ratios/cash-flow-statement pages per ticker, pulled 2026-09-08 via `WebFetch` (24 tickers × up to 3 page fetches, plus follow-up fetches for GOOGL FY2021/22 revenue and LPLA's exact ROIC/FCF-yield values).

---

## ✅ Qualified Quality List — **1 name: CPRT (Copart)**

**Copart clears all 8 Phase 01 filters this round** — the first full pass on this exact name after two consecutive single-filter misses (07-28: Rev CAGR ~6.4%; 08-18: Rev CAGR ~6.4%). The change is a **methodology correction, not a market move**: every other metric is materially unchanged from 08-18 (same TTM window, same balance sheet — Copart's Q4 FY2026 earnings hadn't yet rolled into stockanalysis.com's TTM column as of this pull). This session's Revenue 3yr CAGR, computed strictly FY-anchored per the tightened method above — FY2025 revenue $4,647M ÷ FY2022 revenue $3,501M, `(4647/3501)^(1/3)-1` = **9.90%** — clears the 8% bar; the prior two rounds' ~6.4% figure appears to have mixed a TTM numerator against an FY-anchored denominator, exactly the error this round's stricter convention was written to avoid.

**Flag: FCF Yield clears by only 0.29pp** (4.29% vs the >4% bar) — the tightest margin of any passing filter, and one that has moved *against* CPRT as price has risen (4.56% on 08-18 → 4.29% now). This qualification should be treated as fragile until Phase 02 valuation scoring re-confirms it with fresh live pricing (Rule 0 — fetch live price first, don't infer from this session's numbers).

**Qualified-name count vs. prior round: 0 → 1.**

**Other near-misses worth flagging:**
- **CRM (new candidate)** — misses only ROIC (10.96% vs >15%, −4.04pp) and EV/EBIT (24.86x vs <20x, +4.86x); every other filter clears, including a narrow Net Debt/EBITDA pass (2.40x vs the 2.5x cap). Worth a dedicated look regardless of the FAIL.
- **ADP** (1 filter) — misses only Revenue 3yr CAGR (6.81% vs 8%, −1.19pp); fifth consecutive round flagging this exact single-filter story, gap essentially unchanged since 08-18 (−1.27pp → −1.19pp).
- **ABNB** (1 filter) — misses only EV/EBIT (35.68x vs <20x); gap has narrowed slightly vs. 08-18's 36.02x but remains wide in absolute terms.
- **BR** (2 filters) — misses Gross Margin (31.78%, likely a revenue-recognition/cost-structure characteristic of the business, not a comparability defect) and Revenue 3yr CAGR (7.25% vs 8%, a genuine one-year window roll from 08-18's 7.8%, both narrow misses).
- **TYL** (2 filters) — misses ROIC (8.57%) and EV/EBIT (40.99x); Revenue CAGR is now a knife-edge pass at 8.02% under the strict FY-anchored method — worth watching, a small further deceleration would flip this to a 3-filter miss.
- **MA** (2 filters) — FCF yield (3.29%) and EV/EBIT (24.77x), both near the bar; every quality filter clears strongly.

**Notable changes worth flagging (real events, not screening artifacts):**
- **PANW's net margin collapsed from 7.95% (08-18) to 2.67% this round** — a real full-year (FY2026, ended Jul'26) figure, not independently confirmed as one-time/charge-driven this session. Doesn't change PANW's overall FAIL (already failing this filter before), but the magnitude of the drop is worth tracking.
- **ORCL's AI/OCI-capex-driven FCF collapse persists essentially unchanged** (FY2026 FCF −$23,686M, matching 08-18's −$23.7B); still failing FCF-3yr-positivity, leverage, FCF yield, and EV/EBIT.
- **CRM, CPRT** — CRM new to the tested pool this round (ETF-composition churn via QGRW). CPRT's flip to PASS is a methodology correction as detailed above, not new fundamentals.
- **APP, QCOM** remain absent from all three ETFs' top-25 (last tested 07-07, dropped 07-28) — not re-tested this round; can be pulled back via a direct `/new-position` on request. **FICO** (dropped 08-18) also not re-tested.

---

## 3. Qualitative pass (Step 3)

**CPRT (Copart, Inc.)** is the only candidate advancing to the qualitative pass this round. Answered against the 5 (+1 disruption-vector) questions in [valuation-scoring.md](../framework/valuation-scoring.md#5-qualitative-questions-before-scoring), from established business-model knowledge (not independently re-sourced against a live filing this session — a full news/filings check belongs to `/new-position` before any capital commitment):

1. **Why are margins high?** Copart runs a two-sided online-auction marketplace (VB3 platform) connecting insurance companies (sellers of total-loss vehicles) with licensed dismantlers, rebuilders, and exporters (buyers), largely on a fee/commission and storage-services basis rather than taking title to most inventory. Margins come from scale (200+ owned salvage yards across the US, UK, Germany, Spain, Brazil, Finland, UAE, Canada), a national real-estate footprint that's expensive and slow to replicate, and pricing power from being one of only two truly national US players (the other being Ritchie Bros/IAA, post its 2023 IAA acquisition) — not a lucky cycle.
2. **What would it take to compete with them?** A multi-year, capital-intensive buildout: acquiring/permitting salvage-yard real estate near population centers in every state, building the technology/bidding platform, and — hardest of all — winning multi-year national volume contracts with large insurers who need consistent, wide-coverage disposition capacity. High moat: real-estate + regulatory/licensing + relationship switching costs, reinforced by a rational two-player national structure.
3. **How has management allocated capital over 5–10 years?** Long-tenured leadership (Willis Johnson founder-era discipline, Jay Adair era) with a consistent pattern: buy land ahead of need (often years before a yard opens), keep leverage low (net cash most of the last decade, and again net cash this pull: −2.09x Net Debt/EBITDA), fund international expansion (UK/Germany/Spain/Brazil/Finland/UAE) from internally generated cash, and return capital via buybacks rather than a dividend. Reads as a disciplined, patient compounder track record.
4. **Where is growth coming from next 3–5 years?** International yard expansion (still early-stage outside the US/UK/Canada), continued penetration of non-insurance sellers (dealers, fleet/rental, charities), and a persistently elevated total-loss frequency as vehicle repair costs (parts, ADAS-sensor recalibration, labor) rise faster than vehicle values — a structural tailwind, not a cyclical one, over the last decade.
5. **What is the best bear case against owning it?** (a) Insurer concentration — a handful of large insurers account for an outsized share of volume, and any one renegotiating aggressively or building in-house disposition capacity would hurt take-rate; (b) used-vehicle/commodity (scrap metal, used parts) price volatility feeding directly into auction proceeds and Copart's own margin; (c) a duopoly structure inherently invites regulatory/antitrust scrutiny of pricing power; (d) macro auto-accident-frequency swings (e.g., a sustained shift to remote work reduced miles driven and total-loss volume during 2020-2021).
6. **Disruption vector check — could a new delivery mechanism/platform/technology make this moat irrelevant within 5 years?** The most credible long-horizon threats are (a) ADAS/active-safety technology structurally reducing accident frequency over time, and (b) EV-specific total-loss economics (battery-pack replacement cost can total a vehicle at far lower mileage/damage than an ICE car), which currently look like a net *tailwind* to total-loss volume rather than a disruption, but could reverse if battery costs fall sharply or repair-vs-replace economics shift. Not assessed as a 5-year moat-irrelevance risk today, but worth re-checking at each `/rescore`.

**Verdict:** clears the qualitative bar plausibly — no red flag identified serious enough to override the quantitative pass — but this is Phase 01 only. Per `screen.md` Step 4, valuation scoring is explicitly out of scope here; **CPRT is flagged as a `/new-position` candidate**, where live pricing (Rule 0), full valuation scoring, and a fresher qualitative/news check should happen before any position is considered.

---

## 4. Data gaps and caveats (Step 4)

- **`yfinance`/direct Yahoo access failed with the same TLS connection-reset error** seen in every rotation session since 2026-07-07 — flagged again for `/healthcheck` (Routine 7) to pick up; this is a persistent environment-level network block, not a transient issue. `stockanalysis.com` covered every metric needed this session except LPLA's three gaps below; no estimation was used anywhere in the table (CLAUDE.md Rule 0).
- **LPLA — Gross Margin, Net Debt/EBITDA, and EV/EBIT not rendered on stockanalysis.com's ratios/financials pages, third consecutive round** (present 07-28 at 23.43%/2.66x/19.15x, missing again 08-18 and 09-08) — explicitly re-verified with a "list every ratio row" prompt, confirmed genuinely absent rather than silently omitted. Doesn't change the verdict: LPLA already fails decisively on Net Margin (5.24% < 12%), ROIC (11.54% < 15%), FCF-3yr-positivity, and FCF Yield (−3.32%).
- **GOOGL's TTM Net Margin (54.75%) is again a clear outlier** against FY2025 (32.81%) and FY2024 (28.60%) — same anomaly flagged every round since 08-18, plausibly a one-time gain, not independently confirmed this session. Doesn't change the PASS on this filter or GOOGL's overall FAIL (blocked on FCF yield/EV/EBIT).
- **BRK.B's Revenue 3yr CAGR (7.14%) diverges materially from the 08-18 session's reported 2.7%** — could not reconcile the prior session's exact FY window from this session alone; shown here as freshly, explicitly FY-anchored (FY2025 $371,444M ÷ FY2022 $302,020M) per this round's tightened method. Doesn't change the verdict (both fail <8%). BRK.B's ROIC (19.28%) and EV/EBIT (7.27x) carry the same standing conglomerate-earnings-mix interpretation caveat as every round since 07-07 — doesn't change the FAIL (margin, growth, FCF yield all miss independently).
- **CRM's TTM Net Margin (21.99%) is an outlier against its own FY trend** (FY2026 17.96% → FY2025 16.35% → FY2024 11.87% → FY2023 0.66%), plausibly a one-time tax benefit or charge reversal, not independently confirmed. Doesn't change the PASS on this filter (FY2026's 17.96% would also clear >12%) or CRM's overall FAIL (blocked on ROIC/EV-EBIT).
- **LLY's Revenue 3yr CAGR** required a manual recomputation from raw FY2025/FY2022 figures (65,179 / 28,541) after the initial WebFetch extraction's stated CAGR was arithmetically inconsistent — corrected to 31.69%, shown in the table. Doesn't change the verdict (comfortably clears >8% either way).
- **MRVL's Revenue 3yr CAGR** explicitly computed FY-anchored (FY2026 $8,195M ÷ FY2023 $5,920M)^(1/3)−1 = 11.45%, matching the 08-18 session's own corrected figure computed the same way.
- **MA's Gross Margin (100.00%)** is a data-structure artifact (no separate Cost-of-Revenue line on Mastercard's income statement) — standing note since 06-07. Doesn't change the FAIL (blocked on FCF yield/EV/EBIT).
- **ANET's ROIC (284.77%) and PLTR's ROIC (363.80%)** are, as in every prior round, inflated by a small invested-capital denominator on asset-light, large-net-cash balance sheets — flagged, not independently re-derived, doesn't change either FAIL.
- **DDOG's Net Debt/EBITDA (−44.73x) and EV/EBIT (3782.38x)** are both mathematical artifacts of a near-zero EBITDA/EBIT denominator — shown as-is, doesn't change the FAIL.
- **ABNB, FTNT — ROIC not rendered**; ROCE substituted for both, flagged, doesn't change either verdict (both blocked by other filters/EV-EBIT specifically).
- **Revenue 3yr CAGR methodology tightened this round (see Section 0)** — several figures differ from 08-18's approximate values as a result (AAPL, AMAT, AMD, BR, BRK.B, CSCO, MA, ORCL, TYL all recomputed strictly FY-anchored). No verdict flipped by this alone except **CPRT**, whose prior ~6.4% figure is now understood to have been a mixed-basis calculation error, not a real deceleration.
- **Stale automation prompt (process note, not a data gap):** this routine's scheduled prompt again described itself as a "Monthly" slice referencing the removed `EODHD_API_KEY`/"Path A," and this is at least the seventh consecutive rotation session to hit this identical mismatch. Documented again here for the audit trail; same handling as every prior instance.

---

## 5. Coverage log update (Step 5)

[screening-coverage-log.md](../framework/screening-coverage-log.md)'s NA-1 row updated: Last screened → 2026-09-08, Qualified names found → **1 (CPRT, new — up from 0)**, near-misses refreshed (CRM new 2-filter miss, ADP/ABNB unchanged single-filter misses, BR/TYL/MA tightened or unchanged 2-filter misses), Sources used → MOAT/QUAL/QGRW ETF holdings + `stockanalysis.com` quantitative gate (yfinance/direct Yahoo still blocked by a TLS connection-reset error, same failure mode since 2026-07-07).

---

## Glossary

- **CAGR** — Compound Annual Growth Rate, the smoothed yearly growth rate between a start and end value.
- **EV/EBIT** — Enterprise Value ÷ EBIT, a multiple measuring how expensive a company is relative to its operating profit; lower is cheaper.
- **FCF (Free Cash Flow)** — cash a business generates after running/maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value); higher means cheaper.
- **Gross Margin** — Gross Profit ÷ Revenue; the share of each revenue dollar left after direct production/delivery costs.
- **Net Debt/EBITDA** — net debt ÷ EBITDA, this framework's primary balance-sheet-leverage gate; lower (or negative, i.e. net cash) is safer.
- **Net Margin** — Net Income ÷ Revenue; the share of each revenue dollar left as accounting profit after every expense.
- **Moat** — a durable competitive advantage that protects a business's profits from competitors.
- **Phase 01** — this framework's Universe Screening / quality-gate stage, the subject of this session.
- **Qualified Quality List** — the output of Phase 01 screening: companies that passed the quality gate and are eligible for Phase 02 valuation scoring.
- **ROIC** — Return on Invested Capital; how efficiently a company turns invested capital (debt + equity) into profit.
- **ROCE (Return on Capital Employed)** — a close cousin of ROIC used as a substitute where stockanalysis.com didn't render a direct ROIC figure this session; measures operating profit relative to capital employed (debt + equity).
- **Rotation Matrix** — the [screening-coverage-log.md](../framework/screening-coverage-log.md) table that tracks which region/sector slice was screened when, so `/screen` systematically rotates through the whole investable universe instead of re-covering familiar names.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of financial results, regardless of fiscal-year boundary; used here as the "current" basis for most ratios.
