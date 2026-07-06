# NEW POSITION RECHECK — BULL (Webull Corporation)

**Task type:** NEW POSITION (recheck / Quality Score Engine addendum, not a from-scratch re-evaluation)
**Date:** 2026-07-06
**Prior session:** [2026-06-21-new-position-bull.md](2026-06-21-new-position-bull.md) (Phase 01 FAIL — 3 of 9 criteria pass, 6 fail decisively; Phase 02 computed for the record = 100.0 "Extreme"; PASS/do-not-enter)
**Current portfolio weight:** 0% (not held — absent from [holdings.md](../portfolio/holdings.md); unchanged, not touched in this session)

---

## 0. Why this session exists

This is a **15-day recheck**, triggered by the [Quality Score Engine](../framework/quality-scoring.md) (added 2026-06-29, after the prior BULL session closed on 2026-06-21) — BULL has never had a Quality Score computed. Per the task scope, this session (a) runs a Rule 9 check to confirm nothing material changed since 06-21, and (b) computes BULL's first-ever Quality Score off the data already gathered in the prior session. The Phase 01 gate result and its reasoning are **not re-derived from scratch** — they stand as documented unless a Rule 9 trigger fires below.

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$7.14** | IBKR `get_price_snapshot`, contract_id 776352706 (NASDAQ: BULL, Webull Corp — same contract resolved in the 06-21 session), ts 1783309520 (2026-07-06, live quote, `is_close: false`) |
| Change vs prior close | −0.42% (−$0.03) | IBKR `change` |
| 52-week range (cached) | $4.50 (low) – $18.32 (high) | IBKR `misc_statistics` |
| 13-week range | $4.74 – $7.59 | IBKR `misc_statistics` |

**Price vs. 06-21 session:** $7.12 → $7.14, a **+0.28% move over 15 days** — negligible, well inside ordinary noise for a name with a $4.74–$7.59 13-week range. No unexplained move.

## 2. Phase 01 status — unchanged, not re-derived

No new quarterly filing or primary disclosure has appeared since 06-21 that would change any of the nine Phase 01 inputs (net margin, ROIC, revenue CAGR, gross margin, FCF positivity, net debt/EBITDA, FCF/NI conversion, share issuance, EV/EBIT). Webull's most recent earnings (Q1 2026, reported 2026-05-21) **predate** the 06-21 session and are already fully reflected in it. **Result stands: Phase 01 Quality Gate FAIL — 6 of 9 criteria fail** (net margin, ROIC, FCF/NI conversion ratio structurally unreliable, EV/EBIT, defensible FCF yield, dilutive share issuance). Phase 02 score (100.0, "Extreme") stands for the record; no order setup applies.

## 3. Rule 9 Trigger Check — 2026-06-21 → 2026-07-06 (per fair-value-methodology.md §"Rule 9 — Model Refresh Triggers")

| Trigger category | Checked? | Finding |
|---|---|---|
| **Quarterly earnings release** | Yes | None due in this window. Webull reported Q1 2026 on 2026-05-21 — before, and already fully captured in, the 06-21 prior session (revenue $159.9M vs $117.4M PY, +36% YoY; GAAP net loss attributable to company −$21.7M vs +$13.1M PY). Next earnings confirmed for **2026-08-27** (analyst EPS estimate $0.02) — outside this window. |
| **Guidance revision (up or down)** | Yes | No new guidance found. No press release, 6-K, or analyst-day guidance update located between 06-21 and 07-06. |
| **Management change** | Yes | WebSearch found no CEO/CFO/board change. Anthony Denier remains Group President and U.S. CEO, quoted in the same Q1 2026 release already on file. No management-change trigger. |
| **Material M&A announcement** | Yes | No new M&A found. One capital-structure item located — termination of the standby equity purchase agreement (SEPA) with Yorkville (YA II PN, Ltd.), notice sent 2026-04-01, effective 2026-04-06 — but this **predates** the 06-21 session and is not a new event in this window; not M&A in any case. |
| **Macro shift (central bank policy, commodity price shock)** | Yes | US 10Y Treasury: ~4.46–4.49% (early July 2026 prints, driven by a weak June jobs report — +57K jobs, unemployment 4.2%) vs. 4.46% used in the 06-21 session. Effectively flat; would not move the Rate Regime Modifier bracket (3.5–5%) even if Phase 02 were re-run. No macro-shift trigger. |
| **>15% stock-price move without a fundamental trigger** | Yes | $7.12 → $7.14, +0.28%. No trigger — nowhere near the 15% threshold. |

**Conclusion: no Rule 9 trigger fired in this window.** All six categories checked explicitly; none warrant a re-valuation beyond the 06-21 session.

## 4. Next Review Trigger — unchanged, restated from 06-21

Carried forward verbatim (no change warranted):
- Next earnings release (2026-08-27, confirmed) — re-test net margin, ROIC, and the FCF/NI conversion ratio with another quarter of data.
- Sooner, if a clean multi-quarter run of positive net income attributable to ordinary shareholders emerges (would at minimum clear the PEG-eligibility and earnings-quality concerns, even if valuation remained rich).
- Any Rule 9 event (guidance revision, M&A, major regulatory development).

## 5. Recommendation

**PASS — unchanged.** Phase 01 Quality Gate still FAIL (6 of 9 criteria). No Rule 9 trigger fired in the 2026-06-21 → 2026-07-06 window. No new dated watchlist file is created per `watchlist/README.md`'s "significant change" convention — a "Last checked" line plus the Quality Score addendum below are appended to the existing [BULL-2026-06-21.md](../watchlist/not-in-portfolio/BULL/BULL-2026-06-21.md) entry instead.

## 6. Quality Score Addendum (2026-06-29 Methodology Update)

**Why this section exists:** the framework's [Quality Score Engine](../framework/quality-scoring.md) (a continuous 0–100.0 grade plus a strict **80.0+ gate** for Phase 02 eligibility) was added 2026-06-29, after the prior BULL session (06-21) closed — BULL has never had a Quality Score computed. This addendum applies the new methodology to the data already gathered in the 06-21 session — reconfirmed current per §2/§3 above — **no new financial data was fetched.**

### Hard disqualifier check (per quality-scoring.md — fails regardless of weighted score)

| Hard disqualifier | Applies to BULL? | Basis |
|---|---|---|
| FCF/NI <70% for 2+ **consecutive** years, no growth-capex carve-out | **No** | Annual ratios (from 06-21 session): FY2022 −125.3%, FY2023 +7,678.9%, FY2024 −805.5%, FY2025 +2,266.9%. Two years fall below 70% (FY2022, FY2024) but they are **not consecutive** — FY2023 sits between them at a (mechanically) very high ratio. The literal ratios are themselves flagged as not meaningful (brokerage customer-cash/margin working-capital swings dominate the cash flow statement — see 06-21 session §2 "Why the FCF/Net Income conversion ratio is not meaningful here"), but the specific consecutive-year disqualifier condition, applied literally, does not fire. |
| Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light) | **No** | Deeply net-cash: −10.68× (Total Debt $77.52M vs. Cash $653.19M, FY2025) — the opposite of over-leveraged, and (unlike CBRS) EBITDA here is genuinely positive ($53.89M FY2025), so the ratio is well-defined, not just mechanically favorable. |
| Not FCF-positive for 3+ consecutive years | **No** | FCF mechanically positive in FY2023 (+$466.1M), FY2024 (+$182.8M), and FY2025 (+$561.5M) — three consecutive years. (Quality of this figure is separately questioned — see FCF Quality sub-score below — but the binary disqualifier test, as written, is a positive/negative test, and BULL clears it.) |

**No hard disqualifier fires for BULL** — a genuine difference from the CBRS precedent (where the FCF-positivity disqualifier fired outright). BULL's failure, if any, will have to come from the weighted score itself.

### Weighted Quality Score

| Sub-score (weight) | Inputs (from the 2026-06-21 session) | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net Margin (TTM) −1.64%; ROIC 6.20% (FY2025 basis — NOPAT $27.31M ÷ Invested Capital $440.63M; no separate TTM ROIC was computed in the source session, so the documented FY2025-basis figure is used as-is rather than fabricating a new TTM figure) | NetMargin_Component = clamp((−1.64/30)×100) = 0.0. ROIC_Component = clamp((6.20/30)×100) = 20.7. Avg = (0.0+20.7)/2 | **10.4** (no FCF cap — FCF mechanically positive 3 consecutive years, see disqualifier table) |
| **Margins** (15%) | Gross margin 77.45% (FY2025); 3yr trend 84.6% (2022) → 79.7% (2024) → 77.45% (2025) — **contracting** | clamp((77.45/80)×100) = 96.8. No structural-expansion bonus (trend is contracting, and margin is already far above the 40% bonus-eligibility threshold in any case) | **96.8** |
| **Growth** (20%) | Revenue 3yr CAGR 13.71% (FY2022→FY2025); documented TAM-expansion evidence: customer assets +81–90% YoY (~$24.6B), equity notional trading volume +104% YoY, EEA operating license obtained, Q1 2026 revenue +36% YoY — all per the company's own Q1 2026 release (05-21) and 06-21 session §8 | clamp((13.71/25)×100) = 54.8; **+10** TAM-expansion bonus (cited company-reported user/asset/volume growth and confirmed geographic expansion — no evidence of structural deceleration; Q1 2026 revenue growth is accelerating, not decelerating) | **64.8** |
| **Balance Sheet** (15%) | Net Debt/EBITDA −10.68× (net cash $575.7M net of debt; EBITDA $53.89M, genuinely positive) | clamp(100×(1−(−10.68)/4)) = clamp(367) | **100.0** |
| **Moat** (15%) | Per 06-21 session §8: no cited relative market-share data (only Webull's own absolute growth, not share vs. competitors); no pricing-power evidence (commission-free trading explicitly noted as commoditized industry-wide); community/social-trading layer and international/Asian-market access cited as differentiation but explicitly assessed as "not obviously a durable... network effects in retail brokerage are weaker than in, say, payment networks"; switching costs explicitly assessed as "real but not high"; no cost-per-unit data vs. smaller competitors | 0 of 5 signals meet the cited-evidence bar | **0.0** |
| **FCF Quality** (10%) | Literal FCF/NI ratios are not meaningful (see disqualifier table and 06-21 session §2/§5b) — brokerage customer-cash float dominates reported operating cash flow. **Judgment call:** the owner-earnings-style proxy already computed and disclosed in the 06-21 session (NI + D&A − CapEx = $23.12M, FY2025) is used as the cleaner numerator instead of the literal, wildly-swinging (−805% to +7,679%) reported ratios | Proxy ratio = $23.12M ÷ $24.77M (NI) = 93.3%. FCFQuality_Score = clamp(((93.3−40)/60)×100) = clamp(88.8) | **88.8** (override; the literal reported ratios would be nonsensical/misleading to score directly, consistent with the CBRS precedent's disclosed overrides) |

```
Quality Score = 10.4×0.25 + 96.8×0.15 + 64.8×0.20 + 100.0×0.15 + 0.0×0.15 + 88.8×0.10
              = 2.60 + 14.52 + 12.96 + 15.00 + 0.00 + 8.88
              = 53.96 ≈ 54.0
```

**Quality Score: 54.0 — fails the 80.0+ gate.** Unlike CBRS, no hard disqualifier fires mechanically for BULL — the failure is driven by the weighted score itself, principally a near-zero Moat sub-score (0.0, no cited durable competitive advantage) and weak Profitability (10.4, TTM net margin negative and ROIC well below the 15% reference point), only partly offset by a strong Balance Sheet score (100.0, genuinely net-cash) and a high Margins score (96.8, though on a contracting trend). One sub-score (FCF Quality) required an explicit, documented judgment-call override of a mechanically distorted ratio, disclosed here per this framework's "no black-box outputs" rule, mirroring the CBRS precedent. Per quality-scoring.md, **no Composite Score is computed** for a company that fails the Quality Gate. This does not change the Phase 01 FAIL / do-not-enter recommendation already reached in the 06-21 session.

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets. |
| **Composite Score** | `0.50×(100−Quality Score) + 0.50×Valuation Score` — combines quality and cheapness into one number, computed only for companies that clear the 80.0+ Quality Score gate. Not computed for BULL (gate fails). |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EBITDA** | Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash; flagged here as structurally distorted by brokerage customer-cash float. |
| **Hard disqualifier** | One of three quality-gate conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company outright regardless of its weighted Quality Score. None fires for BULL. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **Net Debt/EBITDA** | Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; deeply negative (favorable) for BULL, reflecting a net-cash balance sheet. |
| **NOPAT** | Net Operating Profit After Tax — EBIT adjusted for taxes, used as the numerator in ROIC. |
| **Owner Earnings** | Buffett's adjusted cash-flow measure: Net Income + D&A − Maintenance CapEx; used here as a data-integrity correction to a distorted reported FCF figure. |
| **Quality Score** | A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. BULL scores 54.0. |
| **ROIC** | Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **SEPA (Standby Equity Purchase Agreement)** | A financing arrangement letting a company sell shares to an investor on demand over time; Webull terminated its SEPA with Yorkville in April 2026, before this session's window. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
