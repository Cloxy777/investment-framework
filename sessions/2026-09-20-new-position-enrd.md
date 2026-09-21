# NEW POSITION — ENRD (Einride AB, ADR, Nasdaq) — 2026-09-20

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6)
**Date:** 20 Sep 2026 (session run 2026-09-21, no market-moving news in the gap; live price is the last completed regular session, Friday 2026-09-18, per IBKR `is_close: true` — see §1)
**10Y US Treasury Yield:** ~5.00% (most recent posted observation, week of 2026-09-18/19) — recorded for header completeness only; **never used**, since Phase 02 is never reached (see §3).
**Rate Regime Modifier:** N/A this session — not reached.
**Current ENRD portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. No `watchlist/in-portfolio/ENRD/` or `watchlist/not-in-portfolio/ENRD/` folder existed before this session — this is ENRD's first-ever `/new-position` or `/rescore` pass in this repo. Not applicable to [watchlist/STALE.md](../watchlist/STALE.md) (no prior score exists to go stale).
**Sector:** Industrials / Freight Technology — autonomous & electric heavy-duty trucking-as-a-service (digital freight platform, AI routing/optimization, own EV fleet)
**Trigger:** FinnInvestChannel (Telegram) named the company; no `watchlist/ENRD/` entry existed and it is not in `holdings.md`, so per `/telegram-scan` step 4's decision tree this session independently derives the Quality Score from fresh, live-fetched fundamentals — the trigger post itself is not treated as a scored financial input.
**First-use jargon decode:** see closing Glossary (§5).

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$3.93** | IBKR `get_price_snapshot` (contract_id **890767847**), `last` field, `is_close: true` (most recent completed regular session — no live intraday quote available at fetch time) |
| Cross-check | **$3.93**, −$0.07 / −1.75% vs. prior close, as of Sep 18, 2026, 4:00 PM EDT (after-hours $3.86) | stockanalysis.com — matches IBKR to the cent |
| Bid / Ask | $3.44 (86) / $4.43 (185) | IBKR `get_price_snapshot` — a very wide ~26% spread on thin size, consistent with a recently-listed, thinly-traded ADR |
| Day's range (last session) | $3.82 – $4.00; Open $4.00; Volume 59,966 | stockanalysis.com |
| 52-week range | Low **$3.40** (also 13w/26w low) · High **$34.00** · Open (52w ago) $10.75 | IBKR `get_price_snapshot` `misc_statistics` |
| YTD change | **−63.88%** | IBKR `get_price_snapshot` |
| Market cap | ≈ $558.84M (142.20M ADS outstanding × $3.93) | stockanalysis.com |
| US 10Y Treasury yield | ~5.00% (header only, not used — see §0/§3) | market data, week of 2026-09-18/19 |

Einride completed its SPAC business combination with Legato Merger Corp. III on 10 June 2026 (ADR "ENRD" / warrants "ENRDW" began trading on Nasdaq that day, ~$1.35B pre-money valuation). The stock has fallen ~64% YTD from its post-listing highs (52w high $34.00) to a fresh 52-week low this week ($3.40) — a steep de-rating consistent with a recent de-SPAC name burning cash faster than the market is comfortable with (see §2, §3).

---

## 2. Quality Score — Phase 01 (per [quality-scoring.md](../framework/quality-scoring.md))

All financial data fetched fresh this session via stockanalysis.com's financial-statement pages (income statement, balance sheet, cash-flow statement), cross-checked against Einride's own SEC 6-K first-half/full-year results releases (Nasdaq/GlobeNewswire, 2026-08-18) and its SPAC-related SEC filings (F-1, 424B3). All figures in millions SEK unless noted.

### 2.1 Hard disqualifiers (checked first — fail regardless of weighted score)

| Disqualifier | Test window | Result |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FY2023 **−SEK 1,509M**, FY2024 **−SEK 554.93M**, FY2025 **−SEK 906.29M** (rolling window per the 2026-08-05 clarification — most recent 3 completed fiscal years); TTM (Jun '26) **−SEK 1,130M**, also negative | **FIRES.** Every one of the last 3 fiscal years is negative (burn narrowed FY2023→FY2024 but re-widened FY2024→FY2025, and the TTM figure is worse than any single full year) — no carve-out available for this disqualifier. |
| Net Debt/EBITDA over threshold (2.5× standard) | Net Debt (TTM, Jun '26): Total debt SEK 782.1M − Cash SEK 747.6M = **SEK +34.5M** (essentially break-even, not meaningfully net-debt-laden) ÷ TTM EBITDA (using TTM Operating Income −SEK 1,109M as a proxy — exact D&A not separately obtainable from available sources, flagged as a minor data gap) | **Does not substantively fire**, for a different reason than the typical case: with EBITDA deeply negative, the ratio (≈ −0.03×) is not a meaningful leverage read either way — mechanically it produces a near-100 (best-possible) Balance Sheet sub-score purely as a formula artifact (see §2.2), not because leverage is genuinely low-risk. The real balance-sheet story is liquidity, not leverage: Einride's FY2025 annual filing (SEC 6-K, filed ahead of the SPAC close) explicitly disclosed **"substantial doubt about the Group's ability to continue as a going concern,"** citing cash burn (SEK 741.7M used in FY2025 operating activities) against only SEK 278.8M cash on hand at 2025 year-end — resolved for now by the June 2026 SPAC close and its ~USD 113.3M PIPE, which lifted cash to SEK 747.6M by Jun '26, but the underlying cash-burn rate is unchanged and shareholders' equity is *more* negative post-close (TTM **−SEK 211M** vs. FY2025 **−SEK 58M**), driven by non-cash SPAC-accounting charges (see §2.2 Growth/Margin notes). Shown for completeness/audit trail; not the basis for the FAIL below. |
| FCF/NI conversion <70% for 2+ years w/o growth-capex explanation | Both FCF (TTM −SEK 1,130M) and Net Income (TTM −SEK 1,952M) are negative | **N/M** — not a genuine "conversion" scenario (both are losses, not profit converting to cash). Moot given the FCF-positivity disqualifier above already fires unconditionally. |

**One hard disqualifier fires outright** (not FCF-positive in any of the last 3 fiscal years). Per quality-scoring.md: "a weighted average can't average away an outright... cash-flow-quality failure." **Session stops here — Phase 02 valuation is not run.**

### 2.2 Full sub-score computation (shown for completeness/audit trail, per "no black-box outputs" — not what determines the outcome, the hard disqualifier above does)

| Input | Value | Source |
|---|---|---|
| Net Margin (TTM) | **−386.67%** (Net Income −SEK 1,952M ÷ Revenue SEK 504.9M) | stockanalysis.com income statement |
| ROIC (TTM) | Not separately disclosed; Operating Income (EBIT) deeply negative every period (TTM −SEK 1,109M, FY2025 −SEK 931.1M) → NOPAT negative → ROIC negative | stockanalysis.com income statement |
| Gross Margin (TTM + 3yr trend) | TTM **−51.28%** (negative — cost of revenue, dominated by owned-fleet vehicle/operating costs, exceeds revenue); 3yr trend FY2023 **−128.95%** → FY2024 **−36.79%** → FY2025 **−46.88%** → TTM **−51.28%** — improved sharply FY2023→FY2024 but has **worsened** the last two readings, not a clean structural-expansion trend | stockanalysis.com income statement |
| Revenue 3yr CAGR | Only 3 fiscal years of data available (FY2023 SEK 185.25M → FY2025 SEK 457.84M, a **2-year** span); a true "3yr CAGR" needs a 4th data point (FY2022), not obtainable from available sources within this session — **N/M**, left unscored rather than approximated with a mismatched window, per "never invent or estimate financial data." (For context only, not scored: the 2yr CAGR over the available window is ≈57%, and FY2025 grew +17.9%/+18% YoY per the company's own release, with H2 2026 guided to 60–73% YoY constant-currency growth — real, fast top-line growth, just not the specific 3yr-CAGR input the formula calls for.) | stockanalysis.com income statement; Einride H1 2026 results release |
| Net Debt/EBITDA | +SEK 34.5M net debt (near break-even) ÷ deeply negative EBITDA (see §2.1) | stockanalysis.com balance sheet |
| Moat signals | **0 of 5** meet the cited-evidence bar: no market-share % data exists for Einride specifically (only total-addressable-market context, e.g. "$4.6T global road freight market"); no pricing-power/brand-premium evidence (no price-increase-without-volume-loss data); no documented two-sided network-effect mechanism (this is a B2B logistics-as-a-service model, not a marketplace); a real, named blue-chip customer roster (Amazon, Maersk, GE Appliances, Heineken, PepsiCo) and ~$800M of potential long-term ARR in "Joint Business Plans" is documented, but no specific contractual-lock-in/integration-depth mechanism or cost-per-unit-vs-competitors data is cited alongside it, so it doesn't clear the checklist's evidentiary bar for either Switching Costs or Scale Cost Advantage | Einride/Amazon/Maersk press coverage (CNBC 2026-04-21, 2026-06-10); Einride F-1/424B3 SEC filings |
| FCF/NI ratio (TTM) | N/M (§2.1) — both FCF and NI negative | stockanalysis.com cash-flow statement |

```
NetMargin_Component = clamp((−386.67/30)×100, 0, 100) = 0.0
ROIC_Component       = 0.0 (negative EBIT/NOPAT)
Profitability_Score  = (0.0 + 0.0) / 2 = 0.0   (FCF cap of 40.0 moot — already 0)

GrossMargin_Score = clamp((−51.28/80)×100, 0, 100) = 0.0  (negative margin; no trend bonus —
  worsened, not expanded, over the last two readings)

Growth_Score = N/M (only a 2-year window available, not the specified 3yr CAGR) → treated as
  0.0, conservative, flagged rather than invented

BalanceSheet_Score = mechanically clamp(100×(1−(34.5/−1109)/4)) ≈ 100.0 (small positive net
  debt ÷ deeply negative EBITDA — a formula artifact, NOT a reliable "low leverage" signal;
  see §2.1's going-concern/cash-burn discussion for the real balance-sheet read)

Moat_Score = (0/5) × 100 = 0.0

FCFQuality_Score = N/M (both FCF and NI negative) → treated as 0.0, conservative

Quality Score (informational only, hard disqualifier already governs) =
  0.0×0.25 + 0.0×0.15 + 0.0×0.20 + 100.0×0.15 + 0.0×0.15 + 0.0×0.10
  = 0 + 0 + 0 + 15.0 + 0 + 0
  = 15.0   (using the mechanical Balance Sheet reading; a conservative reading that treats
  that unreliable, negative-EBITDA-driven sub-score as N/M→0.0 instead gives 0.0 — either
  way far below 80.0 and moot given the hard disqualifier)
```

**0.0–15.0 / 100.0 (either reading) < 80.0 — fails the gate**, independent of and in addition to the hard disqualifier.

---

## 3. Recommendation

**PASS — do not enter, do not track for entry.** Quality Score fails the strict 80.0+ gate decisively, and the primary hard disqualifier fires outright: Einride has not been FCF-positive in any of the last 3 fiscal years (FY2023 −SEK 1,509M, FY2024 −SEK 554.9M, FY2025 −SEK 906.3M — burn narrowed then re-widened, and the TTM figure is the worst of all). Gross margin is *negative* every period shown (TTM −51.3%) and has worsened over the last two readings rather than trending toward breakeven; 0 of 5 Moat Signals clear the framework's cited-evidence bar despite a real, named blue-chip customer list (Amazon, Maersk, GE Appliances, Heineken, PepsiCo).

The company's own FY2025 annual filing disclosed explicit "going concern" doubt ahead of its SPAC close — since resolved for the near term by the 10 June 2026 business-combination close and its ~$113M PIPE (cash rose from SEK 278.8M to SEK 747.6M), but shareholders' equity is *more* negative post-close (TTM −SEK 211M vs. FY2025 −SEK 58M, driven substantially by non-cash SPAC-accounting recapitalization and warrant fair-value items), and the underlying cash-burn rate driving the original going-concern flag is unchanged. Management's own stated target is cash-flow breakeven in **2028** — a multi-year runway that depends on scaling the current ~30-customer, ~200-truck fleet toward the ~1,500–2,000-truck 2028 target and converting the disclosed ~$800M of potential long-term "Joint Business Plan" ARR into actual signed, revenue-bearing contracts, none of which is assured.

Real revenue growth is genuine and fast (FY2025 +17.9% YoY, H2 2026 guided 60–73% YoY constant-currency) — this is not a moribund business — but it is not, on its own, sufficient to clear either the hard disqualifier or the 80.0+ Quality Score gate, both of which are FCF/margin/moat-driven, not growth-driven. The 64% YTD share-price decline (52-week high $34.00 to a fresh 52-week low $3.40 this week) tracks the market reaching the same conclusion, not a documented fundamental trigger this session is reacting to (per Rule 9, price movement alone is never itself a scored input, and none was used as one here).

No fair-value/order-setup section — Phase 02/03 not reached.

## 4. Next review trigger

Einride's next quarterly filing (Q3 2026 6-K, expected ~November 2026) — check whether FY2026 full-year FCF burn is narrowing toward the 2028 breakeven target, whether gross margin turns positive or continues to worsen as fleet utilization scales, and whether any of the ~$800M "Joint Business Plan" pipeline (with Amazon, Maersk, GE Appliances, Heineken, PepsiCo, or new logos) converts into disclosed, signed ARR. Also: any further capital raise/dilution event, a credible cited market-share or cost-per-unit disclosure that could newly satisfy a Moat Signal, or a going-concern-language recurrence in a future filing.

---

## 5. Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used above — all already defined there (no new terms needed this session): **Quality Score**, **Hard disqualifier**, **FCF** / **FCF/NI conversion ratio**, **EBITDA**, **EBIT**, **Net Debt/EBITDA**, **Net Margin**, **Gross Margin**, **ROIC**, **CAGR**, **TTM**, **Moat Signal**, **N/M (Not Meaningful)**, **52-week range**, **ADR (American Depositary Receipt)**, **SPAC**, **de-SPAC merger**, **PIPE (Private Investment in Public Equity)**, **Negative stockholders' equity (shareholders' deficit)**, **Warrant (fair-value adjustment)**.
