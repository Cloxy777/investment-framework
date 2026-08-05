# New Position Evaluation — MELI (MercadoLibre, Inc.)

**Task type:** NEW POSITION (Rule 9 earnings-triggered re-check; MELI is not currently held)
**Date:** 2026-08-05
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `t.me/tarasguk` post at 2026-08-05T20:04:23Z ("$MELI відзвітували" — "$MELI reported [results]") named $MELI by ticker and claimed an earnings release, attached to a grouped-media chart image (image content not read, text only, per Rule 0). Per Rule 0, **no figure from the post is used anywhere below** — the post is treated only as a signal to check MELI's own documented "Next review trigger": [watchlist/not-in-portfolio/MELI/MELI-2026-06-14.md](../watchlist/not-in-portfolio/MELI/MELI-2026-06-14.md) (2026-07-10 addendum) names "MELI's Q2 2026 earnings release (**confirmed 5 August 2026, after close**) — the actual first test of whether net margin shows a sequential recovery toward/above the FY2024 level (~9.1%)." Independently confirmed via SEC EDGAR (not the post): MercadoLibre filed an **8-K on 2026-08-05** (accession `0001099590-26-000021`, Exhibit 99.1 shareholder letter, filed 16:00:58 UTC) — a genuine, primary-sourced Rule 9 earnings event, and the exact trigger this ticker's own file was already watching for.

A same-check `t.me/tarasguk` post (superseded, `tarasguk/11607`, ~17:40 UTC) claimed Demis Hassabis is leaving his role as DeepMind CEO, with $GOOG shares reacting downward — a potential management-change-adjacent Rule 9 signal for GOOG (a current holding, 0.58% weight). Per this routine's design, only the current top post per channel is evaluated each run; this post is not the top post as of this check and is not actioned here. Flagged explicitly for visibility (see the Telegram-watch mention log) given GOOG is a current holding — not independently verified this run, and not treated as data regardless.

MELI is **not a current holding** — no watchlist status change on that front. Quality Score methodology version unchanged since the last entry (2026-06-29), so this is a routine Rule 9 re-check on the current methodology, not a stale-score reconciliation.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): TTM = trailing twelve months; NI = net income; ROIC = return on invested capital; NOPAT = net operating profit after tax; D&A = depreciation & amortization; EBITDA = operating profit before D&A; CAGR = compound annual growth rate; FCF = free cash flow; Adjusted Free Cash Flow = MELI's own non-GAAP FCF measure stripping out fintech-funding working-capital swings; TPV = Total Payment Volume (Mercado Pago); GMV = Gross Merchandise Volume (Marketplace); 8-K = a US-listed company's SEC filing disclosing a material event (here, quarterly earnings); pp = percentage points.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price (used)** | **$1,840.00** | IBKR `get_price_snapshot` (contract_id 45602025), `last.price`, `is_close: false`, timestamp epoch 1785960711 = **2026-08-05T20:11:51Z** |
| Change vs. prior close | **−$48.50 (−2.57%)** | IBKR `change` field |
| Bid/Ask | $1,830.00 / $1,859.96 | IBKR `bid_ask` |

**Timing note:** this snapshot was taken ~7 minutes after the triggering post and essentially at the US regular-session close (20:00 UTC) — it reflects the **regular-session close print, not yet any after-hours reaction** to the 8-K filed at 16:00:58 UTC (which itself may be an EDGAR-processing timestamp rather than the market's actual first reaction time; the filing was headlined as reporting "today"). No fair-value/order-setup work is produced this session regardless (§2 gate result), so this timing nuance doesn't affect the recommendation below — flagged for transparency only.

---

## 2. Rule 9 Trigger Check

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | **Yes** | Q2 2026 8-K filed 2026-08-05 (SEC EDGAR, accession `0001099590-26-000021`) — the confirmed trigger MELI's own 2026-07-10 addendum was explicitly watching for |
| Guidance revision | No | No forward guidance revision beyond the standard shareholder-letter qualitative commentary found in this filing |
| M&A | No | None found |
| Management change | No | None found |
| Macro shift | Not separately assessed | Moot — Phase 02 not reached (§3 gate result); no rate-regime dependency this session |
| >15% unexplained price move | No | −2.57% same-session move, small and not unexplained (earnings-day) regardless |

**Conclusion: quarterly earnings is the confirmed Rule 9 trigger**, and specifically the exact trigger MELI's own file was already tracking. Full Quality Score re-run below, sourced from MercadoLibre's own SEC 8-K (Exhibit 99.1) for the new quarter, cross-checked against `yfinance`-sourced trailing quarters — never from the triggering post.

---

## 3. MELI — Quality Score (2026-06-29 methodology, unchanged version)

**Sources:** Q2 2026 figures from [MELI Q2'26 8-K, Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1099590/000109959026000021/meli-20260805xex991.htm) (filed 2026-08-05) — Consolidated Statements of Income (3-month period), Balance Sheet as of 2026-06-30, and Statement of Cash Flows (6-month period), all SEC-filed GAAP figures. Prior quarters (Q3 2025, Q4 2025, Q1 2026) carried forward unchanged from `yfinance` `quarterly_financials`/`quarterly_balance_sheet`/`quarterly_cashflow` — the same source and the same figures the 2026-07-10 addendum used for its own TTM window (cross-checked: this session's Q1 2026 figures match that addendum's exactly). TTM window rolls forward one quarter: **Q3 2025 → Q2 2026** (replacing the prior addendum's Q2 2025 → Q1 2026 window).

### Quarterly inputs (USD millions, GAAP unless noted)

| Line | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|
| Revenue | 7,409 | 8,759 | 8,845 | **10,169** |
| Net Income | 421 | 559 | 417 | **466** |
| Operating Income | 724 | 889 | 611 | **683** |
| Gross Profit | 3,209 | 3,784 | 3,862 | **4,159** |
| Pretax Income | 636 | 784 | 579 | **606** |
| Income Tax | 215 | 225 | 162 | **140** |
| D&A | 209 | 238 | 246 | **292** (= 6mo 2026 D&A $538M − Q1'26's $246M) |
| Adjusted FCF (company-disclosed) | 206 | 763 | −56 | **214** (letter narrative states "$214mn" directly; cross-checks against the 6mo reconciliation table: H1 2026 Adjusted FCF $158M − Q1'26 −$56M = $214M) |

**TTM (Q3 2025 → Q2 2026):** Revenue $35,182M · Net Income $1,863M · Operating Income $2,907M · Gross Profit $15,014M · Pretax $2,605M · Tax $742M · D&A $985M · Adjusted FCF $1,127M.

**Balance sheet, as of 2026-06-30** (Exhibit 99.1): Loans payable and other financial liabilities — current $6,482M + non-current $4,144M = **$10,626M**; Total equity **$7,834M**; Cash and cash equivalents $3,649M + Short-term investments $2,081M + Long-term investments $1,715M = **$7,445M**. Same "Loans payable and other financial liabilities" convention as the 2026-07-10 addendum (excludes "Funds payable to customers," the fintech-float liability, and operating-lease liabilities from the primary basis — MELI is a marketplace + logistics + consumer-credit hybrid, not a payment network/exchange, so **no asset-light override** applied, unchanged from precedent).

### Sub-scores

```
Profitability (25%):
  TTM Net Margin = $1,863M / $35,182M = 5.2953%
  Effective tax rate (TTM) = $742M / $2,605M = 28.4837%
  NOPAT = TTM Operating Income $2,907M × (1 − 0.284837) = $2,078.98M
  Invested Capital = $10,626M (loans payable, current+non-current) + $7,834M (equity) = $18,460M
  ROIC = $2,078.98M / $18,460M = 11.2621%
  NetMargin_Component = clamp((5.2953/30)×100, 0, 100) = 17.6511
  ROIC_Component       = clamp((11.2621/30)×100, 0, 100) = 37.5403
  Profitability_Score  = (17.6511 + 37.5403) / 2 = 27.5957   (no FCF cap — FCF-positive every
    fiscal year FY2022–FY2025 per prior sessions, unchanged)

Margins (15%): TTM Gross Margin = $15,014M / $35,182M = 42.6752%
  GrossMargin_Score = clamp((42.6752/80)×100, 0, 100) = 53.3440
  Trend check: quarterly gross margin Q2'25 45.57% → Q3'25 43.32% → Q4'25 43.20% → Q1'26 43.67%
    → Q2'26 40.90% — a genuine compressing trend, not expanding, and already above the 40%
    threshold where the structural-trend bonus would apply anyway. No bonus, no formula penalty
    (Margins has no explicit deceleration penalty — Growth does; see below). Flagged qualitatively:
    this is the second consecutive data point (after Q1'26) of margin compression, not expansion.
  Margins_Score = 53.3440

Growth (20%): Revenue 3yr CAGR, FY2022 $10,780M → FY2025 $28,893M (unchanged inputs — FY2025 is
  still the latest complete fiscal year; annual figures don't change intra-year)
  CAGR = (28,893/10,780)^(1/3) − 1 = 38.9072%
  Growth_Score = clamp((38.9072/25)×100, 0, 100) = 100.0 (capped)
  TAM/pricing-power modifier: Q2'26 revenue grew 50% YoY — per the shareholder letter, "the
    fastest pace in four years" — clear acceleration, not deceleration, so no −10 penalty; +10
    bonus moot given the score is already capped at 100.0.
  Growth_Score = 100.0000

Balance Sheet (15%): Net Debt = $10,626M − $7,445M (cash + ST + LT investments) = $3,181M
  TTM EBITDA = TTM Operating Income $2,907M + TTM D&A $985M = $3,892M
  Net Debt/EBITDA = $3,181M / $3,892M = 0.8173×
  BalanceSheet_Score = clamp(100×(1 − 0.8173/4), 0, 100) = 79.5671
  (comfortably clear of the 2.5× hard-disqualifier threshold; down from the 2026-07-10 addendum's
  0.65× / 83.63 as the credit-portfolio-funded debt base grows faster than the cash/investments
  cushion this quarter — a leverage trend worth watching, not yet a gate concern)

Moat Signal (15%) — carried forward from the 2026-07-10 addendum, no new evidence this quarter
  materially changes any of the five signals (checked against this quarter's letter — no new
  cited market-share, pricing, or unit-cost data that would flip a signal):
  ✓ Market share stable/growing — Q2'26 unique Commerce buyers +26% YoY, Fintech MAUs +30% YoY,
     "ecosystemic" (both-sides) users +37% YoY — consistent with a growing, not eroding, position.
  ✗ Brand premium — still FALSE (unchanged): marketplace take rate has held roughly flat, and
     MELI selectively cut commissions in some categories in early 2026 to stay price-competitive —
     the opposite of a clean "price increases without volume loss" signal.
  ✓ Network effect — unchanged mechanism (two-sided Marketplace + the 5-service closed-loop
     ecosystem: Marketplace, Mercado Pago, Mercado Envios, Mercado Ads, Meli+; this quarter's
     letter explicitly reinforces this via the "ecosystemic users" flywheel data).
  ✓ Switching costs — unchanged mechanism (sellers integrate logistics + payments + working-
     capital lending; documented >60% of SMEs' first-ever credit access via Mercado Pago).
  ✓ Scale cost advantage — unchanged mechanism (documented Brazil unit-shipping-cost data from
     the 2026-07-10 addendum; not re-derived this quarter, no new cited figure to update it with).
  Moat_Score = (4/5) × 100 = 80.0000

FCF Quality (10%): TTM Adjusted FCF / NI = $1,127M / $1,863M = 60.4938%
  FCFQuality_Score = clamp(((0.604938 − 0.40)/0.60)×100, 0, 100) = 34.1564
  (down from the 2026-07-10 addendum's 71.2%/52.0 — Adjusted FCF is used in preference to the
  GAAP OCF−CapEx figure for the same reason as that addendum: GAAP operating cash flow is heavily
  inflated by Mercado Pago's credit-portfolio funding dynamics, and the company's own Adjusted FCF
  strips that out. Q2'26 Adjusted FCF ($214M) was explicitly reported as depressed by "$441mn of
  capex and $2.1bn of investment in the expansion of our credit portfolio" — a documented
  growth-capex explanation, consistent with the framework's hard-disqualifier carve-out language)

Quality Score = 27.5957×0.25 + 53.3440×0.15 + 100.0×0.20 + 79.5671×0.15 + 80.0×0.15 + 34.1564×0.10
              = 6.8989 + 8.0016 + 20.0000 + 11.9351 + 12.0000 + 3.4156
              = 62.2512 → rounds to 62.3
```

**Quality Score = 62.3 — FAILS the 80.0+ gate**, down from 65.7 (2026-07-10 addendum) and 71.2 (2026-06-14 original session).

**Hard disqualifier check:**
- FCF/NI conversion <70% for 2+ consecutive years without a documented growth-capex explanation: TTM ratio is 60.49%, and 2026-07-10's TTM ratio was 71.2% (barely above). This is a **TTM-rolling-window** comparison, not two distinct fiscal years, so the "2+ consecutive years" hard-disqualifier language is not triggered on its own terms — and regardless, the depression is explicitly, contemporaneously documented as growth capex (credit-portfolio expansion) by the company itself, the exact carve-out this disqualifier allows. **No disqualifier fires**, but flagged as worth watching if this persists through another quarter.
- Net Debt/EBITDA over threshold: 0.82× vs. 2.5× standard (no asset-light override applies) — **PASS, comfortably**.
- FCF-positive 3+ consecutive years: positive every fiscal year FY2022–FY2025 (GAAP) per the 2026-07-10 addendum, unchanged — **PASS**.

**Net effect: the specific test this session was triggered to run — "does net margin show a sequential recovery toward/above ~9.1%?" — comes back negative.** Q2 2026 net margin was 4.6% (company-reported: "$466 million, with a 4.6% margin"), *below* Q1 2026's already-weak 4.7%, continuing the trend the 2026-06-14/2026-07-10 sessions already flagged rather than reversing it. The TTM Quality Score fell again as a direct result (71.2 → 65.7 → 62.3 across three consecutive reads), driven by both a weaker TTM net margin/ROIC (Profitability 30.95 → 27.60) and a weaker TTM Adjusted-FCF/NI ratio (FCF Quality 52.0 → 34.16) as the credit-portfolio investment scales up faster than accounting profit. Growth remains exceptional (100.0, capped, revenue accelerating not decelerating) and the balance sheet remains sound (0.82× ND/EBITDA, nowhere near the disqualifier threshold) — this is not a distressed business, but it is one whose quality-gate-relevant profitability metrics have now moved the wrong direction for three straight reads.

Per [quality-scoring.md](../framework/quality-scoring.md)'s Strict 80.0+ Gate: **"stop — don't proceed to valuation, regardless of how cheap the stock looks."** No Phase 02 valuation score or Composite Score is computed this session — consistent with the 2026-07-10 addendum's own precedent ("No Phase 02 valuation work performed — out of scope... moot given the gate result"), which this session follows rather than SPOT's alternate for-transparency-only convention (MELI's own file has never computed Phase 02).

---

## 4. MELI — Recommendation

**PASS — Quality Score (62.3) fails the 80.0+ gate, by a wider margin than either prior read. No new position opened. Watchlist only.**

MELI has now failed this framework's strict quality gate in three consecutive computations (71.2 on 2026-06-14, 65.7 on 2026-07-10, 62.3 today), each one *lower* than the last. The specific event this session was triggered to check — whether Q2 2026 earnings would show the net-margin recovery the 2026-07-10 addendum was watching for — resolved in the negative: net margin fell further (4.7% → 4.6%), not toward the ~9.1% FY2024 reference point. No fair-value/buy-price/position-sizing order setup is produced (operating-brief.md OUTPUT FORMAT step 6 applies only when an entry is actually being made).

**What's genuinely new this session, worth surfacing:**
- Growth remains outstanding and, per the company's own letter, is *accelerating* (Q2'26 revenue +50% YoY, "the fastest pace in four years") — this is not a growth-quality problem.
- The margin/profitability weakness is explicitly management's own stated tradeoff, not a surprise: "we continue to set the dial in a way that prioritizes long-term value creation over short-term profitability." The framework's quality gate is deliberately agnostic to that narrative — it scores trailing profitability as reported, not management's forward-looking rationale for suppressing it.
- Net Debt/EBITDA (0.82×) ticked up from 0.65× (2026-07-10) as the credit-portfolio funding base grows faster than the cash/investments cushion — still nowhere near the 2.5× disqualifier threshold, but the direction is worth tracking if it continues for several more quarters.
- FCF Quality (34.16, down from 52.0) is now the joint-weakest sub-score alongside Profitability — both trace to the same root cause (heavy, explicitly-disclosed reinvestment in the credit book), not two independent problems.

**Next review trigger:** MELI's Q3 2026 earnings release (standard quarterly cadence, historically early November based on this company's reporting pattern), or any Rule 9 event (guidance revision, management change, M&A, macro shift, or a >15% unexplained price move) in the interim. Specifically re-test whether net margin has begun recovering (now three consecutive quarters — Q4'25 6.4%, Q1'26 4.7%, Q2'26 4.6% — of the underlying quarterly margin sitting below the ~9.1% FY2024 reference point) or whether this is a multi-quarter structural reinvestment cycle that should be evaluated on its own multi-year timeline rather than quarter-to-quarter.

---

## 5. Watchlist & Portfolio Note

New dated entry written: [watchlist/not-in-portfolio/MELI/MELI-2026-08-05.md](../watchlist/not-in-portfolio/MELI/MELI-2026-08-05.md) (renamed from `MELI-2026-06-14.md`) — a fresh dated file per [watchlist/README.md](../watchlist/README.md)'s rule that a confirmed Rule 9 fundamental-event trigger warrants a new dated pointer even when the score/action category (fails gate → PASS) is unchanged, and the Quality Score itself also changed (65.7 → 62.3). This session does not touch `portfolio/holdings.md` (MELI is not held). No trade recommended or executed.

---

## 6. Glossary

(Pulled from [glossary.md](../framework/glossary.md); one new term added this session — TPV)

| Term | Meaning |
|---|---|
| **8-K** | A US-listed company's SEC filing disclosing a material event to investors — here, the vehicle for MELI's quarterly earnings release. |
| **Adjusted Free Cash Flow** | MercadoLibre's own non-GAAP FCF variant that strips out swings in fintech customer-fund cash/investments, loans receivable, and fintech loans payable — used as the primary FCF basis for this ticker's Quality Score because the raw GAAP figure is inflated by Mercado Pago's credit-portfolio funding dynamics. |
| **CAGR** | Compound Annual Growth Rate. |
| **D&A** | Depreciation & Amortization. |
| **EBITDA** | Operating profit before interest, taxes, D&A. |
| **FCF / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Net Income (checks accounting-profit quality). |
| **GMV (Gross Merchandise Volume)** | The total dollar value of goods sold through a marketplace before the platform's own take-rate is deducted. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score. |
| **Invested Capital** | The total capital (debt + equity, netted for cash in this framework's convention) put to work in a business — the ROIC denominator. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; this framework's primary balance-sheet-risk gate. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator this framework uses for ROIC. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 valuation scoring. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples or stale data. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **TPV (Total Payment Volume)** | Mercado Pago's term for the total dollar value of payments processed through its fintech platform — the fintech-side analog of GMV. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
