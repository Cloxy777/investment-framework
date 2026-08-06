# NEW POSITION — EPAM (EPAM Systems, Inc.)

**Date:** 2026-08-06 | **Task type:** NEW POSITION (Telegram-triggered re-run) | **Trigger:** [Routine 6 — Telegram Stock-Mention Scan](../framework/automation-schedule.md#routine-6--telegram-stock-mention-scan), tarasguk/11614 (~10:38:13 UTC, 2026-08-06): `"$EPAM після звіту -10% ..."` reporting Q2 2026 results and a raised FY26 guide. Per EPAM's existing not-in-portfolio entry ([EPAM-2026-07-05.md](../watchlist/not-in-portfolio/EPAM/EPAM-2026-07-05.md)), this matches its own documented "Next review trigger" (b) "a guidance revision" — the post's own text/figures were **not** used as data (Rule 0); every number below was independently re-sourced.

**Sector / Industry:** Technology — Information Technology Services (software engineering / digital-transformation outsourcing).

---

## Step 0 — Live price (Rule 0)

Fetched via the Interactive Brokers connector (`get_price_snapshot`, contract_id 101898880, NYSE — resolved via `search_contracts`), not inferred from any multiple or from the Telegram post:

| Metric | Value |
|---|---|
| **Live price (last trade)** | **$93.50** |
| Prior close | $109.87 |
| Change | **−14.90%** on the day |
| Bid / Ask | $94.20 / $96.49 |
| 52-week range | $73.06 – $222.18 |

The live IBKR move (−14.90%) is in the same direction and general magnitude as the Telegram post's "-10%" claim — noted only as rough real-world corroboration that an earnings reaction is genuinely underway, **not** used as a data input anywhere below.

---

## Step 1 — Independent data sourcing (Rule 0) and gaps flagged

`yfinance` (via a plain `requests` session — its default `curl_cffi`-impersonated session was hitting `Recv failure: Connection reset by peer` against Yahoo's endpoints this run, worked once routed through a standard session) still reflects the **same trailing-quarter window as the 2026-07-05 session** (`profitMargins` unchanged at 6.961%) — Yahoo's fundamentals pipeline has not yet ingested today's Q2 2026 print (a normal same-day lag). This is a genuine data gap for the freshest quarter via that source alone.

**Independently cross-checked via SEC EDGAR** (not the Telegram post): EPAM filed an **8-K today, 2026-08-06** (accession `0001352010-26-000043`), Item 2.02, furnishing Exhibit 99.1 — the Q2 2026 (quarter ended 2026-06-30) earnings press release. Pulled directly from `sec.gov` and used as the source for the freshest quarter's income statement and balance sheet below, blended with `yfinance` quarterly data (Q3 2025 – Q1 2026) for a genuine trailing-twelve-month (TTM) window ending 2026-06-30.

**Remaining data gap (flagged, non-blocking):** the Exhibit 99.1 press release gives only a single summary cash-flow line — "cash used in operating activities was $38.8M for the first six months of 2026" — with **no capex figure and no full cash-flow statement** (that level of detail typically arrives with the 10-Q, not yet filed). This means a true TTM-through-Q2'26 FCF/NI ratio **cannot** be independently computed this session. Per this framework's established fallback (see the 2026-08-05 CRCL session, same situation), the **FCF Quality sub-score and FCF-positive/FCF-NI hard-disqualifier checks below use the most recently completed full fiscal year (FY2025)** — audited, complete, unchanged from the July session — rather than an incomplete/estimated TTM. Flagged explicitly: 1H2026 operating cash flow swung to **−$38.8M from +$77.4M in 1H2025**, a real deterioration that this fallback does not capture; it doesn't change the outcome below (see Step 2), but is worth carrying forward to the next full evaluation once the 10-Q is filed.

**Moat-signal evidence and TAM/pricing-power evidence:** not sourced/cited this session either (same gap as 2026-07-05) — no citation pulled, so all 5 Moat Signal checklist items stay unmarked and no Growth modifier applies. As before, this does not change the outcome (see Step 2).

---

## Step 2 — Phase 01 Quality Score

### Hard disqualifier checks (fail regardless of weighted score)

| Disqualifier | Result |
|---|---|
| FCF/NI conversion <70% for 2+ **consecutive** years, no growth-capex explanation | **Not triggered** — FY2022–2025 (unchanged, most recent complete FY): 91.2%, 128.1%, 115.9%, 162.2%. All four years clear 70% comfortably. |
| Net Debt/EBITDA over threshold (2.5× standard) | **Not triggered** — company remains in a **net cash** position as of 2026-06-30 (Net Debt/EBITDA ≈ −1.06×, see below) — more debt was paid down (long-term debt $143.7M → $25.0M) than cash spent on buybacks reduced the cash pile. |
| Not FCF-positive for 3+ consecutive years | **Not triggered** — FY2023–2025 all FCF-positive (unchanged). |

No hard disqualifier is being relied upon to fail this company — same as July, the weighted score fails decisively on its own.

### Sub-score calculations

**Profitability (25% weight)** — TTM = Q3'25 + Q4'25 + Q1'26 (`yfinance`) + Q2'26 (SEC 8-K Exhibit 99.1):

```
TTM Revenue    = $1,394.373M + $1,407.548M + $1,400.061M + $1,414.767M = $5,616.749M
TTM Net Income = $106.816M + $109.354M + $82.521M + $102.979M = $401.670M
Net Margin (TTM) = 401.670 / 5,616.749 = 7.15%

ROIC = NOPAT / Invested Capital
  TTM EBIT (=GAAP Income from operations) = $144.943M + $149.254M + $116.768M + $152.222M = $563.187M
  TTM Tax Provision   = $36.802M + $34.467M + $38.127M + $37.572M = $146.968M
  TTM Pretax Income   = $143.618M + $143.821M + $120.648M + $140.551M = $548.638M
  TTM effective tax rate = 146.968 / 548.638 = 26.79%
  NOPAT = 563.187 × (1 − 0.2679) = $412.35M
  Invested Capital (as of 2026-06-30, SEC 8-K balance sheet) = Total Debt $25.000M + Total Equity $3,519.301M − Cash $789.397M = $2,754.904M
  ROIC = 412.35 / 2,754.904 = 14.97%

NetMargin_Component = clamp((7.15/30)×100, 0, 100) = 23.83
ROIC_Component       = clamp((14.97/30)×100, 0, 100) = 49.90
Profitability_Score  = (23.83 + 49.90) / 2 = 36.87
```
FCF-positive-3-consecutive-years cap check: FY2023–2025 all positive (see hard-disqualifier table) — no 40.0 cap applies. (Essentially flat vs. July's 37.24 — one strong quarter barely moves a 4-quarter blend.)

**Margins (15% weight):**
```
TTM Gross Profit = Revenue − Cost of revenues (excl. D&A), each quarter:
  Q3'25 $411.204M + Q4'25 $423.202M + Q1'26 $388.009M + Q2'26 ($1,414.767M − $985.199M = $429.568M)
  = $1,651.983M
Gross Margin (TTM) = 1,651.983 / 5,616.749 = 29.41%
GrossMargin_Score = clamp((29.41/80)×100, 0, 100) = 36.76
```
3yr trend (FY2022→FY2025, unchanged annual data, most recent complete fiscal years): 31.88% → 30.57% → 30.68% → 28.83% — still **mildly contracting**, not expanding. No structural-expansion bonus applies.

**Growth (20% weight):**
```
Revenue FY2022 = $4,824.698M → Revenue FY2025 = $5,457.056M (3-year span, unchanged — FY2026 not yet a complete fiscal year)
Revenue 3yr CAGR = (5,457.056 / 4,824.698)^(1/3) − 1 = 4.19%
Growth_Score = clamp((4.19/25)×100, 0, 100) = 16.76
```
No TAM-expansion/pricing-power evidence cited this session (data gap, see Step 1) — no +10 modifier applied. FY26 guidance (revenue growth raised to 3.2%–4.2%) is a forward *projection*, not filed/audited data — per [valuation-scoring.md](../framework/valuation-scoring.md) "Why Forward Guidance Is Not a Sub-score," guidance is a **trigger**, never a scored input, so it isn't folded into this CAGR.

**Balance Sheet (15% weight):**
```
Net Debt = Total Debt − Cash (as of 2026-06-30, SEC 8-K) = $25.000M − $789.397M = −$764.397M (net cash)
TTM EBITDA (≈ TTM EBIT + each quarter's D&A) = $563.187M + ($41.671M + $41.118M + $41.974M + $32.101M) ≈ $720.051M
  (Q2'26 D&A of $32.101M sourced from the 8-K's own income-statement line; Q3'25–Q1'26 D&A backed out from yfinance's EBITDA−EBIT, methodology not perfectly identical — flagged, but immaterial here: the ratio is deeply net-cash either way.)
Net Debt/EBITDA = −764.397 / 720.051 = −1.06×
BalanceSheet_Score = clamp(100 × (1 − (−1.06)/4), 0, 100) = clamp(126.5, 0, 100) = 100.0
```

**Moat Signal (15% weight):**
```
0 of 5 signals cited/documented this session (see Step 1 data-gap flag — unchanged from July)
Moat_Score = (0/5) × 100 = 0.0
```

**FCF Quality (10% weight):**
```
FCF/NI (FY2025, most recent complete fiscal year — TTM unavailable, see Step 1 gap) = $612.691M / $377.678M = 162.24%
FCFQuality_Score = clamp(((1.6224 − 0.40)/0.60)×100, 0, 100) = clamp(203.7, 0, 100) = 100.0
```

### Final Quality Score

```
Quality Score = (36.87×0.25) + (36.76×0.15) + (16.76×0.20) + (100.0×0.15) + (0.0×0.15) + (100.0×0.10)
              = 9.22 + 5.51 + 3.35 + 15.00 + 0.00 + 10.00
              = 43.08 → rounds to 43.1
```

**43.1 < 80.0 — still fails the Quality Score gate, by 36.9 points — essentially unchanged from the 2026-07-05 session's 43.1.** Even crediting the maximum possible Moat_Score (100.0, unattempted) would only raise the score to ~58.1 — still well short of the gate. A strong Q2 beat (revenue +4.5% YoY, non-GAAP EPS +22.0% YoY) and a raised FY26 guide barely move the needle because: (a) the Quality Score is TTM-blended across 4 quarters, so one quarter has limited leverage; (b) net margin (7.15%) and gross margin (29.41%) both remain far under the >15%/>40% thresholds that would meaningfully lift Profitability/Margins; (c) the two sub-scores that *are* strong (Balance Sheet, FCF Quality) were already maxed at 100.0 in July and can't add further headroom.

---

## Step 3 — Recommendation

**PASS. Stop before Phase 02** — same outcome as 2026-07-05. Per [quality-scoring.md](../framework/quality-scoring.md), a company must score 80.0+ to be eligible for valuation scoring, fair value, or order setup — EPAM misses by 36.9 points. No Phase 02 valuation score, Rate Environment Gate application, fair value, or order setup is computed.

No hard disqualifier is involved — this remains a straightforward weighted-score failure on margin and growth metrics, not a balance-sheet or cash-flow-quality failure. The Rule 9 guidance-revision trigger that prompted this re-run is now **resolved as "checked, no change to the gate outcome"** — this was not the "sustained (not one-quarter) recovery" the existing watchlist entry's "Next review trigger" was looking for.

**Watchlist status:** existing not-in-portfolio entry ([EPAM-2026-07-05.md](../watchlist/not-in-portfolio/EPAM/EPAM-2026-07-05.md)) — score, gate-fail status, and action category (PASS/watchlist-only) are all **unchanged** from the last dated entry, so per [watchlist/README.md](../watchlist/README.md) this session appends a "Last checked (no significant change)" line rather than a new dated row.

**Next review trigger (unchanged):** Rule 9 event (quarterly earnings, guidance revision, management change, M&A, macro shift, or >15% unexplained move) showing a *sustained* — not one-quarter — recovery in net margin (>15%), gross margin (>40%), or revenue growth (3yr CAGR >10%). Also worth a closer look next time: the 1H2026 operating-cash-flow swing to negative (Step 1) once the 10-Q is filed and a real TTM FCF/NI figure becomes computable.

**Not a BUY/TRIM/EXIT action** — no `.ics`/priority-tier alert applies beyond the standard P2 run-summary tier for this Telegram-scan run (no ≥5% holding or trim/exit trigger involved).

---

## Glossary

All terms used in this session (CAGR, EBIT, EBITDA, Free Cash Flow, FCF/NI conversion ratio, Gross Margin, Hard disqualifier, Net Debt/EBITDA, Net Margin, NOPAT, Quality Score, Rate Regime Modifier, ROIC, Rule 0, Rule 9, TTM, 8-K, Guidance revision) already exist in [glossary.md](../framework/glossary.md) — no new terms required this session.
