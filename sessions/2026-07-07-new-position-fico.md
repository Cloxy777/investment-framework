# NEW POSITION (Quality Score Engine addendum) — FICO (Fair Isaac Corporation) — 2026-07-07

**Task type:** NEW POSITION — Quality Score Engine addendum (lightweight, per the CCL/CDR precedent), not a full re-evaluation
**Date:** 7 Jul 2026
**Ticker:** FICO (Fair Isaac Corporation, NYSE)
**Prior session:** [2026-06-14-new-position-fico.md](2026-06-14-new-position-fico.md) — Phase 01 FAIL on a single criterion (Net Debt/EBITDA 2.61× vs <2×/<2.5× thresholds; Upgrade 5's asset-light <4× exception inapplicable — Ba2, sub-investment grade). Predates the 2026-06-29 Quality Score engine addition — FICO has never had a Quality Score computed until this session.
**Current FICO portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session exists

FICO's 06-14 session failed Phase 01 on a single well-sourced criterion (Net Debt/EBITDA) — all 8 other criteria passed comfortably, several by wide margins — and was never scored under the new 0–100.0 Quality Score engine (added 2026-06-29, after this session's original date). Per this task's explicit scope, this session does two things:

1. A Rule 9 check, plus a specific check of the two conditions the 06-14 session flagged as capable of reversing the Phase 01 verdict: whether Net Debt/EBITDA fell back under 2.5×/2×, or whether Moody's upgraded FICO to investment grade. Also checked: any other Rule 9 trigger, and any new development specific to FICO's own business relating to the Mortgage Direct License Program (flagged for this batch given its relevance to credit-bureau moat questions).
2. Compute FICO's first-ever Quality Score under the current engine, with every sub-score shown, handling the previously-flagged negative-GAAP-equity ROIC issue carefully.

Per the task's branching instruction, a fuller Phase 01 re-check (or a new dated watchlist file) is only warranted if Net Debt/EBITDA or the credit rating actually changed, or another Rule 9 trigger fired. As detailed below, neither reversal condition fired and no Rule 9 trigger fired, so this stays an addendum appended to the existing watchlist file.

---

## 1. Live price (Rule 0) and Rule 9 check

**Live price:** $1,316.55 (IBKR `get_price_snapshot`, contract_id 269280, ts 1783451585 → 2026-07-07 19:13:05 UTC, `is_close: false`, intraday). Prior close $1,286.51 (+2.33%). 52-week range $871.13–$1,995.00; price is sitting near its 13-week high ($1,323.35). Versus the 06-14 baseline of $1,179.19, this is **+11.65%** — short of the >15% Rule 9 threshold, and explained regardless (strong market reception to Q2 FY2026 results, the 1 Jul 2026 FICO Score 10T data release, continued buyback execution).

**All 6 Rule 9 categories checked — none fires:**

| Category | Result |
|---|---|
| Earnings | **NO** — Q3 FY2026 not yet reported as of this session; expected ~29 Jul–3 Aug 2026 (analyst-estimate consensus, no company-confirmed date). |
| Guidance revision | None since 06-14 (the Q2 FY2026 guidance raise, 28 Apr 2026, predates 06-14 and is already reflected in that session's data). |
| Management change | None — Will Lansing (CEO), Steve Weber (CFO) unchanged. |
| M&A | None (a 2021 Collection & Recovery divestiture to Constellation Software is stale, unrelated to 2026). |
| Macro shift | No broad-macro event, but a flagged company-specific escalation: Florida AG opened a formal antitrust investigation (Civil Investigative Demand, ~2 Jul 2026, response due 5 Aug 2026) — a state-level escalation of the already-known federal-level Hawley/FTC pricing scrutiny (23 Mar 2026, predates 06-14). Investigation-stage only, no quantitative impact; flagged as moat-durability risk color. |
| >15% unexplained price move | No (+11.65%, explained regardless). |

**Net Debt/EBITDA and credit rating — unchanged, not reversed:** still 2.61× (last-disclosed, Q2 FY2026 earnings call, quarter ended 31 Mar 2026 — no newer quarterly data exists) and still Ba2/Moody's, stable, sub-investment grade (no rating action found in 2026). A new $1.5B incremental term loan (drawn 5 Jun 2026, funding a $1.5B ASR) postdates the 31 Mar 2026 balance-sheet date the 2.61× figure is computed from — no pro forma ratio is disclosed or computed here, but this flags that **actual current leverage is likely higher than 2.61×, not lower**.

**Mortgage Direct License Program (EXPN-linked batch flag):** no new threat to FICO's own business — the program continues to expand in FICO's favor (new reseller partnerships: Cotality, Ascend, Xactus, CIC Credit, MeridianLink; mortgage-royalty price increase $4.95→$10.00 in 2026). This is a threat to credit bureaus' (EXPN et al.) economics, not FICO's, and is cited as Growth/Moat evidence in the Quality Score below rather than as a Rule 9 trigger.

**Net effect: no Rule 9 trigger fires, and neither reversal condition (leverage, rating) fired.** Per this task's branching instruction, this session is an addendum, not a fuller Phase 01 re-check or new dated file.

---

## 2. Quality Score Engine — FICO's first-ever computation

Full detail, worked formula, and the ROIC negative-equity judgment-call note are in the [watchlist addendum](../watchlist/not-in-portfolio/FICO/FICO-2026-06-14.md); summarized here:

| Sub-score (weight) | Score |
|---|---|
| Profitability (25%) | 100.0 (capped both components) |
| Margins (15%) | 100.0 (capped) |
| Growth (20%) | 61.76 (51.76 base + 10 TAM/pricing-power modifier) |
| Balance Sheet (15%) | 34.75 |
| Moat (15%) | 80.0 (4 of 5 signals) |
| FCF Quality (10%) | 98.03 (TTM basis) |

```
Quality Score = 100.0×0.25 + 100.0×0.15 + 61.76×0.20 + 34.75×0.15 + 80.0×0.15 + 98.03×0.10
              = 25.00 + 15.00 + 12.352 + 5.2125 + 12.00 + 9.803
              = 79.3675 → rounds to 79.4
```

Cross-check using fiscal-year (rather than TTM) FCF/NI basis gives 79.6 instead. **Both bases fail the 80.0+ gate** (79.4–79.6, a narrow 0.4–0.6-point miss — the closest-to-passing score seen under this engine so far, vs. CCL's 57.7). FICO **also independently fails via the hard disqualifier** (Net Debt/EBITDA 2.61× > the engine's 2.5× standard threshold), which "fails regardless of weighted score" per quality-scoring.md — so the gate result is not in doubt even setting the near-miss weighted score aside.

**ROIC / negative-equity handling (flagged judgment call):** FICO's GAAP stockholders' equity is a deficit of −$2,101.650M as of 31 Mar 2026 (deepening from FY2025's −$1.7B to −$1.8B), making conventional NI/Equity ROIC undefined. Rather than force a distorted own computation, or arbitrarily pick one of several divergent third-party figures (GuruFocus 5yr avg 59.6%, GuruFocus quarterly point-in-time 42.09%/68.35%, AlphaSpread ex-cash-goodwill-intangibles 143.9%), I used the fact that quality-scoring.md's ROIC_Component clamps to 100.0 for any ROIC ≥30% — and every cited methodology, despite the spread, lands well above that clamp threshold. ROIC_Component = 100.0 (capped) on that basis, flagged explicitly as a judgment call driven by the negative-equity distortion rather than a single computed number.

**No Composite Score computed** (requires clearing the 80.0+ gate first). **No Phase 02 valuation work performed.**

---

## 3. Recommendation

**PASS — Quality Score 79.4/100.0 (79.4–79.6 depending on FCF/NI basis), fails the 80.0+ gate by a narrow 0.4–0.6 points; also independently failed by the Net Debt/EBITDA hard disqualifier (2.61× > 2.5×). Do not enter.**

No Rule 9 trigger fired and neither reversal condition (leverage, credit rating) flipped since 06-14. FICO's first Quality Score computation confirms the Phase 01 FAIL from a more granular angle: an exceptionally high-quality business on every dimension except leverage (Profitability, Margins near/at max, Moat 80.0), pulled to just under the gate almost entirely by the same buyback-funded leverage that fails the binary Phase 01 screen. This is a genuine near-miss worth a prompt re-check once Q3 FY2026 earnings (expected ~late July 2026) report actual post-ASR leverage.

**No position opened — nothing to log in `decisions/`.**

---

## 4. Files touched this session

- `watchlist/not-in-portfolio/FICO/FICO-2026-06-14.md` — appended the Rule 9 check + Quality Score addendum as a dated note (no new file — no Phase 01 verdict change)
- `framework/glossary.md` — added **CFR (Corporate Family Rating)** and **CID (Civil Investigative Demand)**
- `sessions/2026-07-07-new-position-fico.md` — this file

`watchlist/STALE.md` not touched — FICO is explicitly excluded there (Phase 01 FAIL / not-scored, no Phase 02 score to go stale). No `git` commands run.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **CFR (Corporate Family Rating)** — Moody's rating of a company's overall corporate-family credit risk. FICO's CFR is Ba2, sub-investment grade.
- **CID (Civil Investigative Demand)** — a subpoena-like investigative tool used by a state AG or the FTC to compel document production before any lawsuit is filed; Florida issued one to FICO around 2 Jul 2026.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income, an earnings-quality check.
- **GAAP** — Generally Accepted Accounting Principles.
- **GSE (Government-Sponsored Enterprise)** — Fannie Mae/Freddie Mac; their acceptance criteria are a key source of FICO's mortgage-market moat.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of its weighted score; FICO's Net Debt/EBITDA fires this one independently of the 79.4–79.6 weighted score.
- **Invested Capital** — total debt + equity (net of cash) put to work in a business; itself distorted for FICO by the same negative-equity issue that breaks conventional ROIC.
- **Moat** — a durable competitive advantage.
- **NOPAT** — Net Operating Profit After Tax, the numerator of ROIC.
- **Net Debt/EBITDA** — a leverage ratio; this framework's primary balance-sheet-risk gate.
- **Quality Score** — this framework's 0-100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02. FICO scores 79.4-79.6 on its first-ever computation.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move. None fired this session.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results.
