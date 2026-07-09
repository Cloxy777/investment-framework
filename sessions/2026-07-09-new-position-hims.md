# NEW POSITION (Quality Score Engine addendum) — HIMS (Hims & Hers Health, Inc.) — 2026-07-09

**Task type:** NEW POSITION / Quality Score Engine addendum (mirrors the CCL 2026-06-21→07-06 precedent)
**Date:** 9 Jul 2026
**Trigger for this session:** HIMS's 06-12 evaluation predates the 2026-06-29 Quality Score engine addition — HIMS had never had a Quality Score computed. This session backfills that first-ever score and checks whether any Rule 9 trigger fired since 06-12 that would change the Phase 01 verdict.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$35.66** | IBKR `get_price_snapshot`, contract_id 466188387 (NYSE, HIMS & HERS HEALTH INC), real-time snapshot, `is_close: false` |
| Implied prior close | ~$36.07 (derived from `change` field: −$0.41 / −1.14%) | IBKR (the `prior_close` field itself returned empty on two separate requests — the `change` field's delta was used instead) |
| 52-week range | $13.74 – $70.42 | IBKR `misc_statistics` |
| 13-week range | $18.97 – $39.04 | IBKR `misc_statistics` |
| Volume (intraday) | 5,388,294 | IBKR |

Price change vs. the 06-12 session's $28.87: **+23.5%** — above the 15% magnitude Rule 9 threshold, but (per §2 below) treated as *explained*, not *unexplained*.

---

## 2. Rule 9 Trigger Check (all 6 categories)

| Category | Fired? | Finding |
|---|---|---|
| Earnings | **NO** | Q2 2026 not yet reported. Multiple sources confirm expected report date **10 August 2026**. Last reported quarter remains Q1 2026 (11 May 2026), already reflected in the 06-12 session. |
| Guidance revision | **NO** | FY2026 guidance (revenue $2.8B–$3.0B, Adj. EBITDA $275M–$350M) unchanged since the Q1 2026 8-K, already incorporated into 06-12. |
| Management change | **NO** | CEO Andrew Dudum / CFO Yemi Okupe unchanged. COO transition (Kabbani→Chi) was announced 28 Sep 2025 — predates 06-12. Chief Communications Officer hire was Feb 2026 — also predates 06-12. |
| M&A | **NO (new)** | Eucalyptus Health acquisition (~$1.15B) announced 19 Feb 2026, **completed 2 Jun 2026** — both before 06-12. Cited as current Growth sub-score TAM-expansion evidence regardless, since it's still current documented information about the business. |
| Macro/regulatory shift | **NO (new)** | FDA PCAC review of 7 peptides (excludes semaglutide/tirzepatide) scheduled 23–24 Jul 2026, announced via Federal Register 16 Apr 2026 — predates 06-12, and hasn't occurred yet as of this session. Flagged to monitor, not a fired trigger. |
| >15% unexplained price move | **NO (explained)** | +23.5% move is large but has multiple cited, documented causes: Q2 2026 momentum (~+67% over the quarter per Benzinga), user-growth acceleration (website traffic +35% YoY, app MAU +21% YoY in May), a new $400M receivables facility, and a cluster of early-July analyst price-target increases (Canaccord $32→$40, BofA $25→$36, Barclays $29→$39), several explicitly tied to anticipation of the pending FDA PCAC review. Per Rule 9's own "no identified cause" standard, this has identified causes even though the underlying catalyst (PCAC outcome) remains unresolved. |

**Net effect: no Rule 9 trigger fired.** Per the task's branching instruction, since nothing changes any of the three previously-failing Phase 01 criteria (TTM Net Margin, TTM ROIC, FCF/NI conversion) — and no new quarter has even been reported since 06-12 — this session appends a **Quality Score addendum**, not a full Phase 01 re-evaluation or a new dated file.

---

## 3. Quality Score Engine Addendum — First-Ever HIMS Quality Score

Computed under the 2026-06-29 quality-scoring.md engine. All inputs are TTM figures rolled forward from FY2025 (exact 8-K dollar figures, confirmed via WebFetch of the SEC 8-K) + Q1 2026 − Q1 2025 — unchanged in substance from 06-12 since no newer quarter exists.

Key sourced figures (all traced to SEC 8-Ks/10-Qs or named aggregators, none invented):
- FY2025 (Y/E 31 Dec 2025): Revenue $2,347.637M, Gross Profit $1,733.378M, Net Income $128.365M (SEC 8-K, WebFetch-confirmed)
- Q1 2025: Revenue $586.0M, Gross Profit $430.7M (73% margin), Net Income $49.5M
- Q1 2026: Revenue $608.1M, Gross Profit $396.8M (65.3% margin), Net Income −$92.1M
- TTM Revenue $2,369.737M, TTM Gross Profit $1,699.478M (71.72% margin), TTM Net Income −$13.235M (−0.56% margin)
- TTM ROIC −19.43% (GuruFocus, unchanged since 06-12 — no new quarter)
- Q1 2026 10-Q balance sheet: convertible senior notes, net $974.106M; cash $222.266M; ST investments $528.609M → net debt $223.231M
- Adjusted EBITDA: FY2025 $318.0M, Q1'25 $91.1M, Q1'26 $44.3M → TTM $271.2M
- FCF: FY2023 $47.0M, FY2024 $198.3M, FY2025 $57.4M (all positive — 3yr FCF-positive criterion met), Q1'25 $50.1M, Q1'26 $53.0M → TTM FCF +$60.3M against TTM NI −$13.235M (ratio not meaningful, negative denominator)
- FCF/NI: FY2024 157.4%, FY2025 44.7% (only 1 of last 2 fiscal years <70% — hard disqualifier does not fire)

| Sub-score (weight) | Value |
|---|---|
| Profitability (25%) | 0.0 (NetMargin_Component 0.0, ROIC_Component 0.0 — both floor at 0; no FCF cap needed since HIMS is FCF-positive 3yr) |
| Margins (15%) | 89.65 (TTM Gross Margin 71.72%; no structural-trend bonus — margin is contracting, and the bonus only applies below 40%) |
| Growth (20%) | 100.0 (capped; Revenue 3yr CAGR 64.6%; +10 TAM-expansion modifier [Eucalyptus] and −10 structural-deceleration modifier [Q1 2026 YoY growth cratered to +4%] both cited, net 0 since already capped) |
| Balance Sheet (15%) | 79.4 (Net Debt/EBITDA 0.82x primary; 68.5 on a conservative cross-check using 06-12's aggregator-based net-debt figure — same conclusion either way) |
| Moat (15%) | 20.0 (1 of 5 signals true — market share/scale, cited FierceHealthcare + company subscriber growth + May 2026 traffic/MAU data; brand premium, network effect, switching costs, and scale cost advantage all marked false for lack of, or internally-contradictory, citable evidence) |
| FCF Quality (10%) | 7.8 (TTM ratio not meaningful; FY2025 44.7% used as primary — clamp(((0.447−0.40)/0.60)×100)) |

```
Quality Score = 0.0×0.25 + 89.65×0.15 + 100.0×0.20 + 79.4×0.15 + 20.0×0.15 + 7.8×0.10
              = 0.000 + 13.448 + 20.000 + 11.910 + 3.000 + 0.780
              = 49.1
```

**Quality Score = 49.1 / 100.0 — fails the 80.0+ gate**, decisively (30.9 points short). No hard disqualifier independently fires. The failure is driven almost entirely by the Profitability sub-score flooring at 0.0 (both TTM Net Margin and TTM ROIC are negative), consistent with — and quantifying — the 06-12 Phase 01 FAIL verdict.

---

## 4. Where This Was Recorded

- **Addendum appended to:** [watchlist/not-in-portfolio/HIMS/HIMS-2026-06-12.md](../watchlist/not-in-portfolio/HIMS/HIMS-2026-06-12.md) — the "Last checked (2026-07-09)" row, full Rule 9 trigger table, Quality Score Engine addendum table/formula, updated Next Review Trigger, and closing Glossary section.
- **watchlist/STALE.md:** not touched (HIMS was never listed there — this addendum predates and is unrelated to any stale-score flag).
- **No git commands run** this session, per instruction.
- **No position opened — nothing logged in `decisions/`.**

---

## 5. Data Gaps / Flags

1. TTM ROIC (−19.43%) is unchanged from 06-12 since no new quarter has been reported — this is a carry-forward, not a fresh computation, and is flagged as such.
2. Two different net-debt bases exist (exact Q1 2026 10-Q line items: $223.231M net debt, vs. 06-12's more conservative aggregator-based $341.3M) — both are shown, and the conclusion (fails the 80.0+ gate) is unchanged either way.
3. Adjusted EBITDA is company-defined non-GAAP (adds back one-time items including the Q1 2026 restructuring charge) — same caveat carried forward from 06-12.
4. Moat signal evidence for "switching costs" was found in one third-party source but explicitly self-contradicted within that same source ("moat is not yet deep... customers can switch with limited friction") — marked false rather than true, erring toward the framework's "never mark a signal true without a cited source" discipline.
5. No metric in this session was invented or estimated — every figure traces to a specific SEC filing, 8-K, 10-Q, or named source (IBKR, GuruFocus, FierceHealthcare, Benzinga, Invezz), with derivations (TTM roll-forwards, net debt, sub-scores) shown explicitly.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session log beyond those already covered by the 06-12 session's glossary: **BalanceSheet_Score**, **DTC**, **PCAC** — all defined in the addendum's own closing Glossary section in the HIMS watchlist file (see link above).
