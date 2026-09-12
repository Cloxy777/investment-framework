# NEW POSITION — WBD (Warner Bros. Discovery, Inc.) — 2026-09-12

**Task type:** NEW POSITION (Telegram-triggered — Routine 6 unattended run)
**Date:** 12 Sep 2026
**10Y US Treasury Yield:** 4.95% (FRED DGS10, 2026-09-10 close — most recent available)
**Rate Regime Modifier (would apply if the gate were reached):** +5 (10Y in the 3.5–5% bracket) — **not applied; this session does not reach the Rate Environment Gate (see §3)**
**Current WBD portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md)); no prior watchlist entry (first-ever session for this ticker)
**Sector:** Media & Entertainment — Content/Studios (Warner Bros. film/TV, HBO/Max streaming) + Global Linear Networks (cable/broadcast TV)
**Scoring methodology in force:** Quality Score + 80.0+ gate + Composite Score, version 2026-06-29 ([quality-scoring.md](../framework/quality-scoring.md), [valuation-scoring.md](../framework/valuation-scoring.md))

---

## 0. Trigger

Telegram post [tarasguk/11907](https://t.me/tarasguk/11907) (2026-09-12T06:45:11 UTC), evaluated per `/telegram-scan`:

> "Larry Ellison is selling $ORCL shares worth $7.5 billion. The funds are needed for his son to purchase $WBD (Warner Bros. Discovery). Ellison will retain Oracle stock valued at approximately $170 billion."

Per Rule 0, this text is used **only** as the prompt to identify WBD as a candidate ticker with no existing watchlist entry — every figure below is independently sourced from SEC EDGAR, a live market-data snapshot, and dated financial press, never from the Telegram post itself. (The companion claim about ORCL — a pre-arranged 10b5-1 insider-sale plan — was evaluated separately in this run's `/telegram-scan` mention log and logged as no-action: ORCL already has a same-day-old watchlist entry from 2026-09-11 and a scheduled 10b5-1 sale is not a Rule 9 trigger category; see [glossary.md](../framework/glossary.md) "10b5-1 Trading Plan.")

**Critical context the trigger post did not mention:** WBD is not an open-market acquisition candidate for "Ellison's son" to freely pursue — it is already the subject of a **signed, definitive $110.9B all-cash merger agreement with Paramount Skydance at $31.00/share**, announced 2026-02-27 (Larry Ellison's son David Ellison is Paramount Skydance's CEO — so the Telegram post's framing is describing an already-public, seven-month-old deal, not new information). That merger is currently **blocked in federal court** by a multi-state antitrust lawsuit, with trial set to conclude April 2027 pending settlement, and Paramount has agreed to **delay closing to as late as June 2027**, paying WBD shareholders a **$0.25/share/quarter "ticking fee"** (~$650M/quarter) during the delay. (Sources: [CNBC, "Paramount still plans to close WBD merger by end of September despite lawsuit," 2026-07-14](https://www.cnbc.com/2026/07/14/paramount-wbd-merger-lawsuit.html); [CNBC, "Paramount agrees to delay WBD acquisition to as late as June 2027 amid legal challenge," 2026-07-24](https://www.cnbc.com/2026/07/24/paramount-wbd-merger-delay.html); [CNBC, "Lost in limbo: Where the Paramount merger delay leaves WBD, and what may come next," 2026-08-26](https://www.cnbc.com/2026/08/26/paramount-merger-delay-wbd-limbo.html).) This makes WBD, as of today, a **merger-arbitrage situation** (its price trades relative to the pending $31.00 deal price and deal-completion odds/timeline, not primarily on standalone fundamentals) — flagged here for the record; the framework has no separate merger-arb sleeve, so this session proceeds through the standard Quality Value gate exactly as instructed, and the result below is decisive regardless of the merger overlay.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$28.04** (−0.57% on the day vs. prior close $28.37) | Yahoo Finance chart API live quote (regular session, 2026-09-12) |
| Cross-check | $28.27 (−0.37%) | WebSearch aggregation (heygotrade.com / CNN-sourced), same prior close ($28.37) — 0.8% apart, both genuine live prints |
| 52-week high / low | $30.00 / $17.08 | Yahoo Finance |
| Deal reference price | $31.00/share cash (Paramount Skydance merger agreement) | CNBC reporting (sources above) |

**IBKR unavailable this session:** `search_contracts` for WBD returned a repeated tool-level error (`-32400, "An error occurred. Please try again later."`) across three retries — flagged as a data-source degradation for `/healthcheck` to pick up, not silently worked around. Per Rule 0's live-price-first requirement, Yahoo Finance's live chart quote (cross-checked against an independent WebSearch aggregation, both citing the same $28.37 prior close) is used as the price of record instead. This does not affect the recommendation below (see §2 — the Quality Gate fails independent of price).

---

## 2. Phase 01 — Quality Score (per [quality-scoring.md](../framework/quality-scoring.md))

All figures sourced from WBD's FY2025 Form 10-K (fiscal year ended 2025-12-31, filed 2026-02-27) via SEC EDGAR XBRL `companyfacts` API, CIK 0001437107 — no figure estimated or inferred.

| Metric | FY2023 | FY2024 | FY2025 | Source |
|---|---|---|---|---|
| Revenue | $41,321M | $39,321M | $37,296M | SEC XBRL `RevenueFromContractWithCustomerExcludingAssessedTax` |
| Net Income (Loss) | −$3,126M | −$11,311M | **$727M** | SEC XBRL `NetIncomeLoss` |
| Operating Income (Loss) | −$1,548M | −$10,032M | $738M | SEC XBRL `OperatingIncomeLoss` |
| Operating Cash Flow | $7,477M | $5,375M | $4,319M | SEC XBRL `NetCashProvidedByUsedInOperatingActivities` |
| CapEx | $1,316M | $948M | $1,231M | SEC XBRL `PaymentsToAcquirePropertyPlantAndEquipment` |
| FCF (OCF − CapEx) | **$6,161M** | **$4,427M** | **$3,088M** | Computed |
| D&A | $7,985M | $7,037M | $5,684M | SEC XBRL `DepreciationDepletionAndAmortization` |
| Total Debt (LT + current) | $45,449M | $42,253M | $32,706M | SEC XBRL `LongTermDebt` + `LongTermDebtCurrent` |
| Cash & equivalents | $3,780M | $5,312M | $4,566M | SEC XBRL `CashAndCashEquivalentsAtCarryingValue` |
| Stockholders' equity (incl. NCI) | $46,307M | $34,829M | $37,147M | SEC XBRL `StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest` |
| Cost of revenue (excl. D&A) | $24,526M | $22,970M | $20,885M | SEC XBRL `CostOfGoodsAndServiceExcludingDepreciationDepletionAndAmortization` |
| Pretax income | −$3,863M | −$11,388M | $1,639M | SEC XBRL `IncomeLossFromContinuingOperationsBeforeIncomeTaxesExtraordinaryItemsNoncontrollingInterest` |
| Income tax expense | −$784M | $94M | $890M | SEC XBRL `IncomeTaxExpenseBenefit` |

**FY2025 is WBD's first GAAP-profitable year since the 2022 WarnerMedia/Discovery merger** — FY2022–FY2024 all carried large net losses driven by non-cash goodwill/intangible impairments (see [glossary.md](../framework/glossary.md) "Goodwill impairment") — the merger-integration/impairment cycle largely working through the P&L by FY2025.

### Sub-scores

| Sub-score (weight) | Computation | Value |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component = clamp((1.95/30)×100) = **6.5** (FY2025 Net Margin 1.95% = $727M/$37,296M); ROIC_Component = clamp((0.52/30)×100) = **1.7** (ROIC 0.52% = NOPAT $337M [$738M EBIT × (1−54.30% effective tax rate, $890M/$1,639M)] ÷ Invested Capital $65,287M [Debt $32,706M + Equity $37,147M − Cash $4,566M]); no FCF cap (FCF positive 3 consecutive years — see FCF Quality below) → (6.5+1.7)/2 | **4.1** |
| **Margins (15%)** | GrossMargin_Score = clamp((44.00/80)×100) = **55.0** (FY2025 Gross Margin 44.00% = ($37,296M−$20,885M)/$37,296M); gross margin is expanding (40.65%→41.59%→44.00%, FY2023→FY2025) but **no structural-trend bonus applies** — the +10 bonus is explicitly for margins expanding *while below 40%*; WBD's 44.00% is already above that threshold | **55.0** |
| **Growth (20%)** | Growth_Score = clamp((3.32/25)×100) = 13.3 (Revenue 3yr CAGR 3.32%, FY2022 $33,817M → FY2025 $37,296M, SEC XBRL); **−10 structural-deceleration modifier** — revenue has *declined* for two straight fiscal years since its FY2023 peak ($41,321M→$39,321M→$37,296M), the documented, well-reported effect of secular linear-TV-network subscriber decline outweighing HBO Max streaming growth (WBD's own FY2025 10-K MD&A discusses Global Linear Networks revenue decline as the primary revenue headwind) — not a one-off, a multi-year trend | **3.3** |
| **Balance Sheet (15%)** | Net Debt $28,140M (Debt $32,706M − Cash $4,566M) ÷ EBITDA $6,422M (Operating Income $738M + D&A $5,684M) = **4.38×** → BalanceSheet_Score = clamp(100×(1−4.38/4)) → negative, floors to 0.0. **No asset-light override**: WBD is a content/media conglomerate, not a payment network or exchange — the override doesn't apply regardless of interest-coverage specifics, and 4.38× exceeds even that override's 4× ceiling anyway | **0.0** — **independently fires the Quality Score's Net Debt/EBITDA hard disqualifier** (exceeds the 2.5× standard threshold) |
| **Moat (15%)** | 1 of 5 signals cited true: **Brand premium/pricing power** true — HBO Max raised prices across all plans in Oct 2025 (Standard $16.99→$18.49, +8.8%; similar increases on Basic-with-Ads and Premium tiers) while paying-subscriber count *grew* to 125.7M as of Q2 2026 — genuine price-increase-without-volume-loss evidence ([CNBC, "Warner Bros. Discovery's HBO Max is raising its prices across all plans," 2025-10-21](https://www.cnbc.com/2025/10/21/hbo-max-raising-prices-all-plans.html)). Marked **false** (no citable supporting third-party data found this session): **Market share** (linear-network share is well-documented as declining; no citable "stable or growing" data point for the combined entity); **Network effect** (no two-sided-marketplace mechanism); **Switching costs** (low — streaming subscriptions have minimal lock-in, month-to-month cancellation); **Scale cost advantage** (large content library, but no citable cost-per-unit data vs. competitors) | **20.0** |
| **FCF Quality (10%)** | FY2025 FCF/NI = $3,088M / $727M = **424.8%** → FCFQuality_Score clamps to **100.0** (≥100%). No hard-disqualifier concern — FY2025's ratio is far above the 70% floor; FY2024's ratio is not meaningfully comparable (negative NI base) and per the rolling-window convention the current completed fiscal year is the relevant test point | **100.0** |

```
Quality Score = 4.1×0.25 + 55.0×0.15 + 3.3×0.20 + 0.0×0.15 + 20.0×0.15 + 100.0×0.10
              = 1.025 + 8.25 + 0.66 + 0.00 + 3.00 + 10.00
              = 22.9
```

**Quality Score = 22.9 / 100.0 — fails the 80.0+ gate decisively, and independently fails via a hard disqualifier:**
1. The weighted score (22.9) is 57.1 points short of the 80.0 gate.
2. **Net Debt/EBITDA hard disqualifier fires** — 4.38× exceeds the 2.5× standard threshold (and the 4× asset-light-override ceiling, which doesn't apply to WBD's business model regardless).

Per [quality-scoring.md](../framework/quality-scoring.md): *"Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* **This session stops here.** No Rate Environment Gate, Phase 02 valuation score, or Composite Score is computed.

---

## 3. Recommendation

**PASS — do not enter, watchlist only.** WBD fails the Quality Score gate on both the weighted score (22.9 vs. 80.0 required) and an independent hard disqualifier (Net Debt/EBITDA 4.38× > 2.5×). This would already be a clear PASS on fundamentals alone, and is reinforced by the merger-arbitrage overlay described in §0: WBD's price today trades against a **pending, litigation-delayed $31.00/share cash buyout** (currently ~9-10% below the deal price, reflecting completion-timeline/antitrust risk), not against a standalone growth or quality thesis — a structurally different, event-driven risk/reward than this framework's Quality Value + Dynamic Trimming approach is built to evaluate. Next review trigger: resolution of the Paramount Skydance antitrust litigation (trial currently set to conclude April 2027) or a change to deal terms/price; WBD's next 10-K (FY2026, expected ~February 2027) for a fresh Quality Score read; any Rule 9 event before then.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Two terms newly added there this session: **Merger arbitrage**, **Ticking fee**. Other terms used in this file: 8-K, 10-K, 10b5-1 Trading Plan, CAGR, EBIT, EBITDA, EDGAR, Effective tax rate, FCF, FCF/NI conversion ratio, GAAP, Goodwill impairment, Hard disqualifier, HSR Act, Invested Capital, M&A, MD&A, NCI, NOPAT, Net Debt/EBITDA, Quality Score, Rate Regime Modifier, ROIC, Rolling-window (disqualifier/metric test), Rule 0, Rule 9, TTM, XBRL.
