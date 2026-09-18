# NEW POSITION — JOBY (Joby Aviation, Inc., NYSE) — 2026-09-18

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6)
**Date:** 18 Sep 2026, trigger post ~15:59 UTC / session run ~16:06 UTC
**10Y US Treasury Yield:** 5.01% (FRED `DGS10`, most recent posted observation dated 2026-09-16) — recorded for header completeness only; **never used**, since Phase 02 is never reached (see §3).
**Rate Regime Modifier:** N/A this session — not reached.
**Current JOBY portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** None. No `watchlist/in-portfolio/JOBY/` or `watchlist/not-in-portfolio/JOBY/` folder existed before this session — this is JOBY's first-ever `/new-position` or `/rescore` pass in this repo. Not applicable to [watchlist/STALE.md](../watchlist/STALE.md) (no prior score exists to go stale).
**Sector:** Aerospace — Advanced Air Mobility (eVTOL / aerotaxi developer, pre-commercial)
**First-use jargon decode:** see closing Glossary (§5).

---

## 0. Trigger — why this session exists, and why the post is not used as data

**FinnInvestChannel**, post `#3237` (2026-09-18 15:59 UTC):

> "Joby Aviation completed its first fully autonomous flight across the USA — 3,199 miles without pilot intervention, handling taxiing/takeoff/routing/landing independently; remote operators supervised from 2,300+ miles away — a milestone for aerotaxi development (cargo delivery, medical, military logistics applications)."

Per CLAUDE.md Rule 0, this post is a **trigger only**. Independent verification via Joby's own investor/newsroom page confirms a real, same-day event: **"Joby Completes First-Ever Fully Autonomous Flight Across the United States,"** dated 2026-09-18 — consistent with the Telegram post's description (coast-to-coast, no pilot intervention, remote supervision). This is a genuine operational/technical milestone toward eventual FAA certification and commercial aerotaxi service, but it is **not itself a scored financial input**: no revenue, margin, or balance-sheet effect is disclosed alongside it, and this framework never treats a single news item as a Quality/Valuation Score input without independently-sourced fundamentals behind it.

**Decision to trigger:** `watchlist/in-portfolio/JOBY/` and `watchlist/not-in-portfolio/JOBY/` are both absent, and JOBY is not in [holdings.md](../portfolio/holdings.md). Per `/telegram-scan` step 4's decision tree: "No watchlist entry exists at all → `/new-position <TICKER>`." This session independently derives the Quality Score from fresh, live-fetched fundamentals; it does not treat the autonomous-flight claim itself as a scored input.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$6.06** | IBKR `get_price_snapshot` (contract_id **507188246**, NYSE, "JOBY AVIATION INC"), `last` field, fetched 2026-09-18 ~16:06 UTC (12:06pm EDT), `is_close: false`, `halted: false` |
| Cross-check | **$6.06**, −$0.13 / −2.10%, prior close **$6.19** | stockanalysis.com, quoted as of 2026-09-18 12:06pm EDT — matches IBKR to the cent |
| Change vs. prior close | −$0.13 / **−2.10%** on the day | IBKR `get_price_snapshot` `change` field (IBKR's own `prior_close` field returned empty, but the change is internally consistent with stockanalysis.com's stated $6.19 prior close) |
| Bid / Ask | $6.06 (1,645) / $6.07 (3,233) | IBKR `get_price_snapshot` |
| 52-week range | Low **$5.94** (also the 13w and 26w low — i.e. today/this week set a fresh 52-week low) · High $19.975 · Open (52w ago) $14.34 | IBKR `get_price_snapshot` `misc_statistics` |
| YTD change | −54.09% | IBKR `get_price_snapshot` |
| Market cap | ≈ $5.99B (989.12M shares outstanding × $6.06) | stockanalysis.com |
| US 10Y Treasury yield | 5.01% | FRED `DGS10`, as-of 2026-09-16 (header only, not used — see §0/§3) |

---

## 2. Quality Score — Phase 01 (per [quality-scoring.md](../framework/quality-scoring.md))

All financial data fetched fresh this session via stockanalysis.com's financial-statement pages (income statement, balance sheet, cash-flow statement), cross-checked internally (e.g. market cap = shares × price ties out). Joby has never filed a 10-K showing meaningful commercial revenue — it remains pre-commercial, generating revenue mainly from government/demonstration/services contracts alongside its eVTOL certification and production program.

### 2.1 Hard disqualifiers (checked first — fail regardless of weighted score)

| Disqualifier | Test window | Result |
|---|---|---|
| **Not FCF-positive for 3+ consecutive years** | FY2023 −$344.43M, FY2024 −$476.88M, FY2025 −$563.81M (rolling window per the 2026-08-05 clarification — most recent 3 completed fiscal years) | **FIRES.** Every year negative and worsening; no carve-out available for this disqualifier. |
| Net Debt/EBITDA over threshold (2.5× standard) | Net Debt (most recent quarter, Q2 2026): Total debt $747.71M − (Cash $629.86M + ST investments $1,634M) = **−$1,516.15M** (i.e. a **net CASH** position of ~$1.52B, not net debt) ÷ TTM EBITDA (using TTM Operating Income −$882.91M as a proxy — exact D&A not separately obtainable from available sources, flagged as a minor data gap that doesn't change the qualitative conclusion below) | **Does NOT substantively fire**, unlike a typical negative-EBITDA case. Net debt itself is *negative* — Joby holds far more cash + short-term investments ($2.26B) than total debt ($748M), funded by repeated equity/convertible raises. Mechanically, clamp(100×(1−(−1516.15/−882.91)/4)) = 57.1 (both negative terms cancel to a positive ratio ≈1.72×), but this is a coincidental artifact of the formula, not a meaningful leverage read. The substantive fact — a company with a $1.5B+ net cash cushion is not balance-sheet distressed, regardless of negative EBITDA — is the opposite situation from LCID's 2026-07-14/2026-09-17 sessions (positive net debt **and** negative EBITDA there = zero capacity to service debt from operations). Shown for completeness/audit trail; not the basis for the FAIL below. |
| FCF/NI conversion <70% for 2+ years w/o growth-capex explanation | Both FCF (TTM −$743.33M) and Net Income (TTM −$878.16M) are negative | **N/M** — this is not a genuine "conversion" scenario (both are losses, not profit converting to cash); mechanically clamp(((0.8467−0.40)/0.60)×100) = 74.45 if computed naively, but not used. Moot given the FCF-positivity disqualifier above already fires unconditionally. |

**One hard disqualifier fires outright** (not FCF-positive in any of the last 3 fiscal years). Per quality-scoring.md: "a weighted average can't average away an outright... cash-flow-quality failure." **Session stops here — Phase 02 valuation is not run.**

### 2.2 Full sub-score computation (shown for completeness/audit trail, per "no black-box outputs" — not what determines the outcome, the hard disqualifier above does)

| Input | Value | Source |
|---|---|---|
| Net Margin (TTM) | −755.11% | stockanalysis.com income statement (TTM period ended Jun 2026) |
| ROIC (TTM) | Not separately disclosed; Operating Income (EBIT) deeply negative every period (TTM −$882.91M, FY2025 −$719.59M) → NOPAT negative → ROIC negative | stockanalysis.com income statement |
| Gross Margin (TTM + 3yr trend) | TTM **34.29%**; 3yr trend FY2023 80.62% → FY2024 50.73% → FY2025 45.10% → TTM 34.29% (**declining**, not expanding — the early 80%+ readings reflect a tiny, non-representative revenue base of ~$1M/year before commercial-scale activity began) | stockanalysis.com income statement |
| Revenue 3yr CAGR | FY2022 revenue not meaningfully disclosed (rounds to ~$0 in the summary fetched — Joby was pre-revenue at that point); FY2023 $1.03M → FY2024 $0.14M → FY2025 $53.43M. **N/M** — a 3yr CAGR from a ~$0 base is mathematically undefined, not a case of "never invent," so left unscored rather than approximated | stockanalysis.com income statement |
| Net Debt/EBITDA | −$1,516.15M net cash (see §2.1) | stockanalysis.com balance sheet |
| Moat signals | **0 of 5** meet the cited-evidence bar: no market-share data exists (pre-commercial); no pricing-power/brand-premium evidence (no unit sales yet); no documented two-sided network-effect mechanism; no documented switching-cost mechanism with a citable source; no cost-per-unit data for "scale cost advantage" (a Jun 2026 Toyota manufacturing alliance and an Aug 2026 Atoms vertiport-network partnership are real and documented via Joby's newsroom, but neither yet produces citable cost-per-unit or market-share data, so neither clears the checklist's evidentiary bar) | Joby Aviation newsroom (jobyaviation.com/news); stockanalysis.com |
| FCF/NI ratio (TTM) | N/M (§2.1) — mechanically 84.67% if computed naively | stockanalysis.com cash-flow statement |

```
NetMargin_Component = clamp((−755.11/30)×100, 0, 100) = 0.0
ROIC_Component       = 0.0 (negative EBIT/NOPAT)
Profitability_Score  = (0.0 + 0.0) / 2 = 0.0   (FCF cap of 40.0 moot — already 0)

GrossMargin_Score = clamp((34.29/80)×100, 0, 100) = 42.9  (no trend bonus — declining, not expanding)

Growth_Score = N/M (undefined 3yr CAGR from a ~$0 base year) → treated as 0.0, conservative, flagged
  rather than invented

BalanceSheet_Score = mechanically clamp(100×(1−(−1516.15/−882.91)/4)) = 57.1 (both terms negative,
  cancel to a positive ratio — NOT a reliable signal for a negative-EBITDA, net-cash-rich business;
  shown only to demonstrate the formula's limits here, not used to determine the outcome)

Moat_Score = (0/5) × 100 = 0.0

FCFQuality_Score = N/M (both FCF and NI negative) → treated as 0.0, conservative
  (naive mechanical reading: clamp(((0.8467−0.40)/0.60)×100) = 74.45, not used)

Quality Score (informational only, hard disqualifier already governs) =
  0.0×0.25 + 42.9×0.15 + 0.0×0.20 + 57.1×0.15 + 0.0×0.15 + 0.0×0.10
  = 0 + 6.44 + 0 + 8.57 + 0 + 0
  = 15.0   (using conservative 0.0 for the N/M-flagged sub-scores; a naive reading that also
  plugged in the mechanical FCFQuality figure would give ≈22.4 — either way, far below 80.0
  and moot given the hard disqualifier)
```

**~15.0–22.4 / 100.0 (either reading) < 80.0 — fails the gate**, independent of and in addition to the hard disqualifier.

---

## 3. Recommendation

**PASS — do not enter, do not track for entry.** Quality Score fails the strict 80.0+ gate decisively, and the primary hard disqualifier fires outright: Joby has not been FCF-positive in any of the last 3 fiscal years (FY2023 −$344.4M, FY2024 −$476.9M, FY2025 −$563.8M — burn is *worsening*, not narrowing). Revenue is real but tiny and pre-commercial ($53.4M TTM against an $882.9M TTM operating loss); gross margin is trending down, not up, as the revenue base shifts from small demonstration contracts toward early scaled activity; and no Moat Signal clears the framework's cited-evidence bar yet.

**One distinguishing note vs. the LCID precedent** (2026-07-14 / 2026-09-17 sessions, also Phase 01 FAILs): unlike LCID, Joby's balance sheet is **not** distressed — it holds a ~$1.52B **net cash** position (Q2 2026) against only $747.7M of total debt, funded by repeated equity raises rather than debt. The Net Debt/EBITDA hard disqualifier does not substantively fire here. This means Joby's path back to the 80.0+ gate runs specifically through sustained FCF improvement and real commercial revenue scale (not a balance-sheet repair), which is at least a plausible trajectory if FAA type certification and the recently-announced autonomous-flight capability convert into paying, revenue-generating routes — worth tracking, though not warranting a watchlist "buy candidate" framing today.

Today's autonomous-flight milestone (independently confirmed — see §0) is a genuine technical achievement toward that path, but it changes none of the trailing financial facts driving this Quality Score: no disclosed revenue or margin impact accompanies it.

No fair-value/order-setup section — Phase 02/03 not reached.

## 4. Next review trigger

Joby's next quarterly filing (Q3 2026 10-Q, expected ~November 2026) — check whether FCF burn is narrowing or still worsening, whether the gross-margin decline stabilizes as revenue scales, and whether any of the Toyota manufacturing alliance, Virgin Atlantic UK service deal, or Atoms vertiport partnership converts into disclosed, revenue-bearing commercial activity (as opposed to the current pilot/demonstration/government-services revenue mix). Also: any FAA Type Certification milestone announcement with a credible commercial-service timeline, or a material new capital raise/dilution event given the ongoing heavy cash burn.

---

## 5. Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used above: **Quality Score**, **Hard disqualifier**, **FCF** / **FCF/NI conversion ratio**, **EBITDA**, **EBIT**, **Net Debt/EBITDA**, **Net Margin**, **Gross Margin**, **ROIC**, **CAGR**, **TTM**, **Moat Signal**, **N/M (Not Meaningful)**, **52-week range**, **Aerotaxi / eVTOL (electric Vertical Takeoff and Landing aircraft)** (new term, added to glossary.md this session).
