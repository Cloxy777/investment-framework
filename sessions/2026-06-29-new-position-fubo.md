# New Position Evaluation — FUBO (fuboTV Inc.)

**Task type:** NEW POSITION
**Date:** 2026-06-29
**10Y US Treasury yield:** 4.38% (last trading day's close, 2026-06-26 — markets closed 2026-06-29, a Sunday; confirmed via WebSearch and cross-checked against yfinance `^TNX` daily history, which shows 4.388% on 2026-06-26, the most recent available print)
**Trigger:** Orchestrator-directed full NEW POSITION evaluation (not a Telegram-scan trigger). FUBO has no prior watchlist or session history in this repo (confirmed absent from [portfolio/holdings.md](../portfolio/holdings.md) and no file under `watchlist/*/FUBO/`).

FUBO is **not** a current holding. Per explicit instruction for this session: fuboTV underwent a major corporate transformation — it merged its North American streaming/vMVPD business with Disney's Hulu + Live TV in a transaction that closed **2025-10-29**, with Disney taking majority economic ownership (~70%, one source citing 72.9% per a later Schedule 13D/A amendment) of the combined entity via newly issued Class A and Class B shares, while FUBO continues as the publicly-traded parent. This session verifies the **current, post-merger** corporate structure, share count, and financials from primary/aggregator sources rather than assuming pre-merger historical financials still describe the entity today.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first, before any valuation work.

| Source | Price | Timestamp |
|---|---|---|
| **IBKR live snapshot** (primary, contract_id 864281476, NYSE, "FUBOTV INC") | **$9.92** | snapshot ts 1782695308, `is_close=false` (confirmed live, not a stale close) |

Contract-resolution note: `search_contracts("FUBO")` returned several unrelated matches that required disambiguation — a secondary Mexican Stock Exchange (MEXI) listing (contract_id 864281473) of the same underlying company, and numerous unrelated Taiwanese "Fubon" financial-group ETF/equity tickers that matched the search string. The NYSE primary listing (contract_id 864281476) was used throughout, consistent with this framework's convention of using the primary listing as the reference ticker.

**Live price used throughout this session: $9.92.**

---

## 2. Data Gaps Flagged / Data-Source Note

`yfinance` required `YF_DISABLE_CURL_CFFI=1` and `CURL_CA_BUNDLE=/root/.ccr/ca-bundle.crt` to run without network errors (per prior-session precedent); once set, it worked normally for quarterly/annual statements and `get_shares_full()`, with only a benign "curl_cffi not available, falling back to requests" notice on each call.

**Critical data-quality finding — Class A/Class B dual-class share structure understates true shares outstanding by ~3.7×.** yfinance's `t.info` fields read:

| Field (yfinance, as reported) | Value |
|---|---|
| `sharesOutstanding` | 29,435,597 |
| `marketCap` | $291,706,752 |
| `enterpriseValue` | $2,305,128,704 |

`t.balance_sheet`'s "Ordinary Shares Number" (29,435,597 at 2026-03-31) agrees with `sharesOutstanding` — internally consistent, but **both capture only the publicly-traded Class A share count.** Following the merger close, FUBO's capital structure became dual-class: Class A shares (publicly traded, the ~29.4M figure) and Class B shares (issued to Disney as merger consideration, **100% held by Disney**, not publicly traded). Independent WebSearch confirms FUBO's **true total shares outstanding (Class A + Class B) are ~108.43 million** — roughly **3.7× yfinance's reported figure**. This directly parallels (in symptom, though not in root cause) the CBRS session's (2026-06-24) finding of a vendor share-count field disagreeing with the true total — there it was a flat-out data error; here it is a real dual-class structure that a single-class-aware vendor field simply doesn't capture.

**Corrected figures used throughout this session:**

| Metric | yfinance (Class A only) | Corrected (Class A + Class B) |
|---|---|---|
| Shares outstanding | 29,435,597 | **108,430,000** (approx., per WebSearch) |
| Market cap (at live price $9.92) | $291.95M | **$1,075.65M** |
| Enterprise Value (corrected market cap + net debt $137.27M, 2026-03-31 balance sheet) | $2,305.13M (yfinance's own figure, itself likely built on a blend of stale/Class-A-only inputs) | **≈$1,212.92M** |

**Second data-quality finding — real, non-error share-count discontinuity from a 1-for-12 reverse stock split.** `get_shares_full()` shows Class A shares dropping abruptly from ~353.2M (2026-03-24) to ~29.4M (2026-03-26) — initially indistinguishable from a vendor bug, but confirmed via WebSearch (stocktitan.net, kavout.com, fastcompany.com, tipranks.com, theglobeandmail.com) to be a **real 1-for-12 reverse stock split effective 2026-03-24**, undertaken to support the post-merger share price. This is a genuine corporate action, not a data error — but it must be (and is) accounted for explicitly rather than silently propagated into ratios.

**Third finding — a massive, confirmed real dilutive share issuance tied to the merger itself.** The same `get_shares_full()` series shows Class A shares spiking from ~342.4M to **~1.29 billion** on 2025-10-31 (two days after the 2025-10-29 merger close), before settling back to ~342.7-353.2M by mid-November 2025 as the snapshot stabilized — this spike/settle pattern reflects new shares issued to Disney as merger consideration, a real and enormous one-time dilution event for pre-merger legacy shareholders, entirely separate from (and prior to) the March 2026 reverse split.

**Merger-transition data-comparability gap — TTM blends two different businesses.** The merger closed 2025-10-29, mid-way through the most recent four reported quarters. A naive trailing-twelve-month (TTM) sum (quarters ended 2025-06-30, 2025-09-30, 2025-12-31, 2026-03-31) mechanically blends:
- Two **legacy, standalone pre-merger fuboTV** quarters (2025-06-30, 2025-09-30): revenue ~$377-380M/quarter, gross margin ~20%
- Two **combined Disney/Hulu-Live-TV+Fubo** quarters (2025-12-31, 2026-03-31): revenue ~$1.55-1.57B/quarter, gross margin ~7.2-7.6%

This is not a meaningfully comparable TTM in the way the framework's gate intends — it is computed below for completeness (Revenue $3,879.7M, Gross Profit $386.98M, EBIT −$40.76M, Net Income −$34.97M, FCF −$466.03M, per `t.quarterly_financials`/`t.quarterly_cashflow`), but **the two cleanest, fully-combined-entity-only quarters (2025-12-31 and 2026-03-31) are used preferentially below** wherever a margin or profitability ratio is decision-relevant, following the same principle the TTWO session (2026-06-24) applied when a denominator (there, EBITDA) was itself unreliable across the lookback window: state plainly when a metric isn't meaningfully computable on a contaminated basis rather than present a misleading blended number.

**Annual statements (`t.financials`/`t.cashflow`/`t.balance_sheet`) are entirely pre-merger.** The most recent fiscal year available (FY2024, ended 2024-12-31) and all three years before it (FY2021-FY2023) describe **legacy, standalone fuboTV only** — none reflect the combined entity at all, since the merger didn't close until late October 2025. This means a clean, combined-entity multi-year revenue CAGR, ROIC trend, or margin trend **does not exist and cannot be estimated** — there is only one full reporting quarter of meaningfully clean combined data behind the live price (2026-03-31 quarter; 2025-12-31 is the first combined quarter but covers a partial integration period). This is flagged here as a genuine, real data gap — not invented or estimated — consistent with this framework's non-negotiable rule.

**Earnings-quality exclusion — Q1 2025 (legacy, pre-merger) net income/EBIT spike.** Legacy fuboTV's quarter ended 2025-03-31 showed an anomalous +$197.9M EBIT / +$188.5M net income, confirmed via WebSearch (Sportcal, SportBusiness, AInvest, SimplyWall.st) to be driven by a one-time **$220M Venu Sports litigation settlement gain** — not operating performance. This figure is excluded from any clean-earnings basis below, the same treatment the CBRS session (2026-06-24) gave its "Gain On Sale Of Security" one-off and the IBM session (2026-06-25) gave its earnings-quality cross-check per [graveyard-audit.md](../framework/graveyard-audit.md). It also explains why yfinance's raw `trailingPE` field reads an anomalously low **2.58×** — an artifact of that one-off gain inflating trailing EPS, not a sign of cheapness; it is not used anywhere in this session.

WebFetch could not reach SEC EDGAR directly (`sec.gov` returned HTTP 403 Forbidden) or wsj.com (fetch blocked outright); stockanalysis.com and stocktitan.net WebFetches succeeded and were used as secondary-source cross-checks, with figures cross-validated against yfinance's own structured quarterly data (e.g., stocktitan's six-month combined operating cash flow of −$412.4M matches yfinance's sum of the two combined quarters: −$200.31M + −$212.07M = −$412.38M — internally consistent).

---

## 3. Phase 01 — Universe Screening (Quality Gate)

The framework carries two slightly different Phase 01 threshold sets — [strategy.md](../framework/strategy.md)'s (stricter) and [valuation-scoring.md](../framework/valuation-scoring.md)'s "Quantitative Pre-Screen Filters" (looser on most lines). Both are shown below for completeness; FUBO fails decisively under **either** version.

All financial figures below use the two cleanest, fully-combined-entity quarters (ended 2025-12-31 and 2026-03-31) as the preferred basis where decision-relevant, with the contaminated 4-quarter TTM and pre-merger annual figures shown alongside for transparency per Section 2's data-gap note.

| Criterion | strategy.md threshold | valuation-scoring.md threshold | FUBO actual | Result |
|---|---|---|---|---|
| **Net margin** | **>15%** | **>12%** | **Combined-only quarters: −0.13%(Q ended 2025-12-31) / −0.38%(Q ended 2026-03-31) → blended ≈ −0.26%.** Contaminated TTM: −0.90%. Legacy pre-merger annual (not representative of current entity, shown for completeness): −10.62%(FY24) / −21.01%(FY23) / −55.68%(FY22) / −59.97%(FY21). Negative under every construction. | **FAIL (both)** |
| **ROIC** | **>15%** | **>15%** | NOPAT (EBIT × (1 − effective cash tax rate ≈5%), combined-only quarters) ≈ EBIT −$20.30M × 0.95 ≈ **−$19.3M**; Invested Capital (2026-03-31 balance sheet, includes Disney's ~$1.84B NCI) = **$1,187.06M**. **ROIC ≈ −1.6%.** Negative — driven by negative operating profit, not a small-base distortion | **FAIL (both)** |
| **FCF positive (3+ yrs)** | **3+ yrs** | **3 consecutive yrs** | Combined-only quarters: −$204.02M(Q ended 2025-12-31) / −$214.71M(Q ended 2026-03-31). Legacy annual: −$95.31M(FY24) / −$199.57M(FY23) / −$322.69M(FY22) / −$203.41M(FY21). **Negative in every available period, combined or legacy, with no exception** | **FAIL (both)** |
| **Gross margin** | **>40% OR structurally expanding** | **>40%** | **Combined-only quarters: 7.56%(Q ended 2025-12-31) / 7.24%(Q ended 2026-03-31) — the cleanest, most decision-relevant figures.** Contaminated TTM: 9.97%. Legacy annual (not representative): 12.57%(FY24) / 6.30%(FY23) / −4.07%(FY22) / −1.63%(FY21). The combined entity's margin (~7.2-7.6%) is **far below** the >40% threshold and is *lower*, not higher, than even fuboTV's own best recent legacy year — the merger materially diluted gross margin, the opposite of "expanding" | **FAIL (both)** |
| **Revenue growth** | **CAGR >10% (3yr)** | **CAGR >8% (3yr)** | **Not cleanly computable.** Legacy-only annual revenue (FY21 $638.4M → FY24 $1,622.8M, 3yr CAGR ≈36.5%) does not represent the current, ~6× larger combined entity (combined quarterly run-rate ~$1.55-1.57B, i.e. ~$6.2-6.3B annualized) — using the legacy CAGR would overstate confidence in a growth trend that has nothing to do with the business as it exists today. Only two combined-entity quarters exist; no 3-year combined-entity revenue base exists or can be estimated without inventing data | **Not meaningfully computable — treated as a FAIL given the absence of any clean multi-year combined-entity base to support the gate's intent** |
| **Net debt/EBITDA** | **<2×** | **<2.5×** | Net Debt (2026-03-31) = $137.27M. EBITDA, combined-only quarters: $33.75M(Q ended 2025-12-31) + $7.50M(Q ended 2026-03-31) = $41.25M (2 quarters) → annualized ≈$82.5M. **Net Debt/EBITDA ≈ 1.66×** | **PASS (both)** — the one criterion that clears either threshold, though built on a thin, recently-volatile EBITDA base (swinging from $33.75M to $7.50M quarter-over-quarter) that is not yet a stable, multi-quarter trend |
| **FCF/NI conversion** | **>70% for 2+ yrs** | (same check, implicit) | Combined-only quarters: FCF −$204.02M vs NI −$2.10M (Q ended 2025-12-31); FCF −$214.71M vs NI −$5.98M (Q ended 2026-03-31). FCF is **far more negative** than NI in both periods — cash burn running roughly 36-100× the accounting loss, the opposite of healthy conversion. Ratio is not meaningful/interpretable as a "conversion" in the way the gate intends | **FAIL (both)** |
| **FCF yield** | (not separately gated) | **>4%** | Annualized combined-only-quarters FCF (2 quarters × 2 ≈ −$837.46M) ÷ corrected market cap $1,075.65M = **≈ −77.9%** | **FAIL (valuation-scoring.md leg)**, extreme negative |
| **EV/EBIT** | (not separately gated) | **<20×** | EBIT (combined-only quarters) is negative (−$20.30M, 2-quarter sum) → **EV/EBIT mechanically undefined/negative** on the corrected EV (~$1,212.92M) | **FAIL (valuation-scoring.md leg)** |
| **Dilutive share issuance pattern** | **none** | **none** | **Two real, large, confirmed dilution events**, independent of each other: (1) the 2025-10-31 merger-consideration issuance spiking Class A-equivalent shares from ~342.4M to ~1.29B (a >3.7× increase, pre-split), the single largest dilution event in the company's history; (2) ongoing dual-class structure leaving Disney holding ~79M Class B shares (≈72.8% of the corrected ~108.43M total) that legacy public shareholders do not control. The 1-for-12 reverse split itself is not "dilutive" (it is share-count-reducing, cosmetic to per-share price only) but does not offset the merger-consideration issuance, which was real and economically dilutive to legacy holders' proportional claim on the business | **FAIL (both)** — a real, structurally significant dilution event has occurred |
| Moat signal | stable/growing share, brand, network effect | (qualitative, same) | The combined entity is genuinely the **6th-largest Pay-TV company in the US** post-merger (~6.2M subscribers, per WebSearch), with Disney's content library and live-sports rights now embedded in the offering — a real qualitative improvement in competitive position vs. legacy standalone fubo. But this is a recent, unproven integration (8 months old at the 2026-03-31 quarter), not a demonstrated durable moat with a financial track record yet | Mixed/qualitative PASS at best — does not offset the quantitative failures below |

### Result: **Phase 01 FAIL**

FUBO fails on a clear majority of independent, structural criteria under both threshold sets carried in this framework — and unlike a typical "growing-but-unprofitable" story, the *combined* entity's profitability profile is **worse**, not better, than legacy standalone fuboTV's own historical trend on the metric that matters most for this gate:

1. **Gross margin collapsed, not expanded, in the merger.** Legacy fuboTV's gross margin was trending toward profitability (−4.07% FY22 → 6.30% FY23 → 12.57% FY24) — still well short of the >40% gate, but moving the right direction. The combined Disney/Hulu-Live-TV+Fubo entity's gross margin in its first two clean quarters (7.56%, then 7.24%) is *lower* than legacy fubo's own most recent full year and shows no sign of the ">40% or structurally expanding" the gate requires. This is a structural feature of the vMVPD/live-TV-distribution business model (high content-licensing costs relative to subscription revenue), not a transitional blip expected to resolve quickly.

2. **Profitability and ROIC fail outright on every clean combined-entity data point available.** Net margin (−0.13% to −0.38%), EBIT margin (−0.10% to −1.11% derived from the combined quarters), and ROIC (≈−1.6%) are all negative in the only periods that cleanly describe the current entity. The gate requires **>15%** on net margin and ROIC; FUBO is not in the same order of magnitude, let alone close to threshold.

3. **Free cash flow is deeply and consistently negative, with FCF/NI conversion the opposite of healthy.** Both clean combined quarters show FCF running 36-100× more negative than the (already negative) net income figure — this reflects real cash consumption (working-capital strain from integrating a much larger subscriber base and content-cost structure), not merely an accounting-driven mismatch that would resolve with maturity.

4. **Revenue growth/CAGR is not honestly computable on a combined basis**, and using the legacy-only trend would be actively misleading (it describes a business roughly 1/4 to 1/6 the current entity's size). Per this framework's "never invent or estimate" rule, this is flagged as a genuine data gap rather than papered over with a number that doesn't describe the current FUBO.

5. **A massive, confirmed dilutive issuance occurred as direct merger consideration** (~342M → ~1.29B shares, pre-split, on 2025-10-31) — categorically disqualifying on the "no dilutive issuance pattern" criterion under both threshold sets, separate from (and in addition to) the cosmetic 1-for-12 reverse split that followed five months later.

The **one** criterion that passes under either threshold set is Net Debt/EBITDA (≈1.66×) — but this rests on a thin, two-quarter-old, highly volatile EBITDA base ($33.75M one quarter, $7.50M the next) that does not yet constitute a demonstrated trend, and Phase 01 is conjunctive: one passing leverage ratio does not offset failing profitability, ROIC, cash generation, gross margin, and a real, large dilution event simultaneously.

### Turnaround Sub-Gate (Hybrid Upgrade 4) eligibility check

Per [strategy.md](../framework/strategy.md), the Turnaround Sub-Gate is reachable only by companies failing **2-4** quality criteria (not more). FUBO fails **6 of 8** criteria in the table above (net margin, ROIC, FCF, gross margin, revenue CAGR, FCF/NI conversion, plus the separately-tracked FCF yield/EV/EBIT/dilution legs) — well outside the 2-4 window, the same disqualifying pattern seen in the CBRS (2026-06-24, failed 7 of 8) and TTWO (2026-06-24, failed 6+ of 8) sessions. Additionally, condition 1 of the Sub-Gate (historical ROIC >15% for ≥5 of the past 10 years) is structurally unreachable here regardless of the criteria-count test: legacy fuboTV's annual ROIC has never been close to 15% in any of its available history (deeply negative every year, FY21-FY24), and the combined entity has only 8 months of existence. **Not reachable.**

Per [operating-brief.md](../framework/operating-brief.md) and the new-position command: **"if it fails, stop and report why rather than proceeding to scoring."** Accordingly, **no Rate Environment Gate and no Phase 02 valuation score were computed.**

---

## 4. Qualitative Notes

1. **Is the Disney/Hulu Live TV merger a genuine strategic improvement, or a forced consolidation by a structurally weak business?** Both, plausibly. fuboTV had spent years as a thinly-margined, sub-scale vMVPD; combining with Hulu + Live TV creates the **6th-largest Pay-TV provider in the US** (~6.2M subscribers) with materially more negotiating leverage on content costs over time and access to Disney's content/ad-tech stack. But Disney taking ~70-73% economic ownership, and the combined entity showing *worse* gross margins than standalone fubo's own recent trend, suggests the deal was at least partly a consolidation of two structurally challenged distribution businesses rather than a clean value-accretive combination for FUBO's pre-merger shareholders specifically.

2. **Does the post-merger entity have a path to the gate's profitability thresholds, and on what timeline?** Not evidenced yet — only two combined quarters of data exist, both showing negative gross-margin-adjusted operating profit. No forward guidance is scored per this framework's rule (guidance is explicitly excluded from scored inputs), but qualitatively, a live-TV/vMVPD distribution business reaching >40% gross margin would require a fundamentally different content-licensing cost structure than the industry has historically achieved; this is a multi-year-or-never question, not a near-term one.

3. **Who actually controls the combined entity, and what does that mean for minority (FUBO-ticker) shareholders?** Disney holds ~70-73% of the combined economics via Class B shares and consolidates a ~$1.84B Noncontrolling Interest onto FUBO's balance sheet — meaning FUBO public shareholders (the Class A holders) own a minority economic stake in a business FUBO management continues to operate but does not majority-own. This is a materially different risk/reward profile than owning a normal controlling-interest public company.

4. **Is the share-count/dilution picture as bad as it looks, or partly an artifact of deal mechanics?** Real, not an artifact. The ~342M→~1.29B share spike on 2025-10-31 reflects actual new shares issued as merger consideration — a genuine, large transfer of economic ownership to Disney, not a cosmetic or temporary accounting entry. The subsequent 1-for-12 reverse split (2026-03-24) is cosmetic (share-price-management only) and does not reverse the underlying dilution.

5. **Is there a credible path to clean, comparable financial data soon?** Yes, but not yet. The next 1-2 quarterly filings (Q ended 2026-06-30, 2026-09-30) will be the third and fourth fully clean combined-entity quarters, beginning to allow a real trend read on gross margin, EBIT trajectory, and FCF — still short of the 3-year lookback the gate's CAGR/ROIC checks are designed around, which will not exist on a combined basis until roughly 2028.

---

## 5. Recommendation

**PASS.** Do not open a position. No order setup, no fair-value derivation, no position sizing — consistent with this framework's standing rule that this work is not meaningful for a name that fails the Phase 01 quality gate on a clear majority of criteria (here: 6 of 8, plus all three valuation-scoring.md-only legs), and producing it anyway would be "black-box theater" the CBRS/TTWO/IBM precedent sessions all explicitly declined to produce.

**Worth flagging for context (not a basis for any action):** the Turnaround Sub-Gate (Hybrid Upgrade 4) is not reachable here — FUBO fails 6 of 8 criteria (outside the 2-4 window) and condition 1's 10-year historical-ROIC lookback is structurally unreachable regardless, the same disqualifying pattern seen in CBRS and TTWO.

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance. [portfolio/holdings.md](../portfolio/holdings.md) is not touched by this session.

---

## 7. Next Review Trigger

- **Routine re-screen:** not scheduled — Phase 01 FAILs are not put on a recurring re-check cadence by default (per [watchlist/README.md](../watchlist/README.md): "Phase 01 FAIL / not scored" entries don't carry a numeric score to go stale).
- **Rule 9 fundamental trigger** that would warrant a fresh look regardless of schedule: FUBO's next 1-2 quarterly earnings releases (quarters ended 2026-06-30 and 2026-09-30) — these will be the third and fourth fully clean combined-entity quarters and the first real opportunity to assess whether gross margin, EBIT, and FCF are trending toward the gate's thresholds rather than just two data points. Any quarter showing the combined entity's gross margin breaking meaningfully above its current ~7.2-7.6% band, or EBIT/FCF turning durably positive, would warrant a fresh full evaluation. A full clean 3-year combined-entity revenue base, allowing the CAGR/ROIC checks to be computed on a basis that actually describes the current business, is not expected before approximately 2028 (three full fiscal years post-merger-close).

---

## 8. Quality Score Addendum (2026-06-29 Methodology Update)

**Why this section exists:** the framework's [Quality Score Engine](../framework/quality-scoring.md) (a continuous 0–100.0 grade plus a strict **80.0+ gate** for Phase 02 eligibility) and the [Composite Score](../framework/valuation-scoring.md) were added on 2026-06-29, after this session's Phase 01 analysis above was already complete. This addendum applies the new methodology to the same underlying data already gathered in §2/§3 above — **no new financial data was fetched.**

### Hard disqualifier check (per quality-scoring.md — fails regardless of weighted score)

| Hard disqualifier | Applies to FUBO? | Basis |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years, no growth-capex carve-out | Not mechanically meaningful, but substantively yes | Both clean combined quarters show FCF and NI both negative with FCF running **36–100× more negative** than NI — never a clean, interpretable conversion in any period, combined or legacy. Not relied upon as the primary citation below since the literal ratio isn't well-defined; see the unambiguous disqualifier below instead. |
| Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light) | **No** | ≈1.66× (thin two-quarter EBITDA base) — this is FUBO's one passing Phase 01 criterion, and it does not change here. |
| Not FCF-positive for 3+ consecutive years | **Yes — fires** | FUBO has **never recorded a single FCF-positive year or quarter** on any basis examined: legacy annual FY21 −$203.41M, FY22 −$322.69M, FY23 −$199.57M, FY24 −$95.31M; combined-entity quarters −$204.02M (Q ended 2025-12-31) and −$214.71M (Q ended 2026-03-31). Zero consecutive positive years exist, let alone three. |

**Hard disqualifier #3 fires, unambiguously and independently of the weighted score below.** No judgment call is needed for this conclusion — FUBO's FCF has not been positive in any reported period, combined or legacy.

### Weighted Quality Score — partial, by design

Two of the six sub-scores cannot be computed without inventing data, per this framework's "never invent or estimate financial data" rule (the same data gaps already flagged in §2/§3 above):

| Sub-score (weight) | Status | Basis |
|---|---|---|
| **Profitability** (25%) | Computable | Net margin ≈−0.26% (blended combined-only quarters), ROIC ≈−1.6% → NetMargin_Component = ROIC_Component = clamp(negative/30×100) = 0.0 each → **0.0** |
| **Margins** (15%) | Computable | Gross margin blended ≈7.40% (avg. of the two clean combined quarters, 7.56%/7.24%) → clamp((7.40/80)×100) = **9.25**; no trend bonus — the merger *diluted* margin versus legacy fubo's own trend, the opposite of expanding |
| **Growth** (20%) | **Data gap — not computed** | Revenue 3yr CAGR is "not meaningfully computable" per §3 above: the only clean combined-entity base is two quarters old, and the legacy-only multi-year trend describes a business ~1/4 to 1/6 the size of the current entity. Forcing a number here would misrepresent a genuine gap as a measurement. |
| **Balance Sheet** (15%) | Computable | Net Debt/EBITDA ≈1.66× → clamp(100×(1−1.66/4)) = **58.5** |
| **Moat** (15%) | Computable | 0 of 5 signals cited true: post-merger scale (6th-largest US Pay-TV provider) is a one-time M&A fact, not cited share-*trend* data; gross margin fell post-merger (contradicts brand-premium/pricing-power evidence); no network-effect, switching-cost, or cost-per-unit evidence cited | **0.0** |
| **FCF Quality** (10%) | **Not meaningful — not computed** | FCF/NI in both clean quarters mixes two negatives of very different magnitude (FCF 36–100× more negative than NI) — not an interpretable "conversion ratio" in the sense the sub-score is designed to grade. |

**No single weighted Quality Score number is presented for FUBO** — with Growth (20% weight) and FCF Quality (10% weight) genuinely not computable, forcing the remaining four sub-scores through the formula would produce a number with 30% of its weight silently defaulted to zero, which would understate rather than honestly represent the gap. This is moot for the gate decision: **hard disqualifier #3 above (never FCF-positive for 3+ consecutive years) fails FUBO's Quality Gate conclusively and independently**, exactly as the underlying Phase 01 quantitative failures already did in §3. Per quality-scoring.md, a fired hard disqualifier fails the company "regardless of weighted score" — so the partial score above does not need to be completed to reach a gate verdict.

**No Composite Score is computed** — per quality-scoring.md, the Composite Score is never computed for a company that fails the Quality Gate. This does not change the Phase 01 FAIL / do-not-enter recommendation already reached in §5 above.

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **Composite Score** — `0.50×(100−Quality Score) + 0.50×Valuation Score` — combines quality and cheapness into one number, computed only for companies that clear the 80.0+ Quality Score gate. Not computed for FUBO (gate fails via hard disqualifier).
- **Hard disqualifier** — one of three quality-gate conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company outright regardless of its weighted Quality Score. FUBO fails the "FCF-positive for 3+ consecutive years" disqualifier — it has never had even one positive year.
- **Quality Score** — a 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. Not fully computable for FUBO (two sub-scores are genuine data gaps), but moot — a hard disqualifier fails the gate regardless.
- **Dual-class shares** — A capital structure where a company has two or more classes of common stock with different rights, typically with one class publicly traded and another held privately. FUBO's Class A (publicly traded, ~29.4M shares) and Class B (100% held by Disney, ~79.0M shares) structure caused yfinance's `sharesOutstanding`/`marketCap` fields to understate true total shares (~108.43M) by roughly 3.7×.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures used in leverage and valuation ratios.
- **EPS** — Earnings Per Share — net income divided by number of shares outstanding.
- **EV** — Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to operating profit, independent of capital structure; undefined/meaningless when EBIT is negative.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper; negative means the business is consuming cash relative to its market value.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. Not meaningful when both figures are negative or of very different magnitudes, as here.
- **GAAP** — Generally Accepted Accounting Principles — the standard US accounting rulebook companies use for their official financial statements.
- **M&A** — Mergers & Acquisitions — one company buying or combining with another.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **NCI (Noncontrolling Interest, a.k.a. Minority Interest)** — The portion of a consolidated subsidiary's equity/earnings belonging to outside shareholders rather than the parent filing the statements. Disney's ~70-73% stake in the combined Fubo/Hulu Live TV entity is consolidated on FUBO's balance sheet as an NCI of ~$1.84B.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate. The one criterion FUBO passes here, on a thin two-quarter EBITDA base.
- **NI (Net Income)** — accounting profit after all expenses, interest, and taxes ("the bottom line").
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate) — operating profit after a tax adjustment but before financing costs; the numerator this framework uses to compute ROIC.
- **PE (Price-to-Earnings) ratio** — Share price ÷ earnings per share; not scored in this session since Phase 01 failed first. FUBO's raw trailing PE (2.58×) is a one-off-gain artifact, not a sign of cheapness.
- **Phase 01-06** — the six sequential stages of this framework: Universe Screening → Valuation Scoring → Entry/Position Sizing → Continuous Monitoring → Dynamic Trimming → Full Exit.
- **Qualified Quality List** — the output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring. (FUBO does not make this list.)
- **Reverse stock split** — A corporate action reducing share count by a fixed ratio while proportionally raising the per-share price, leaving market cap unchanged. FUBO executed a 1-for-12 reverse split effective 2026-03-24 — a real corporate action, not a data error, but distinct from (and not offsetting) the much larger merger-consideration share issuance five months earlier.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework. Negative for FUBO on the only clean combined-entity data available.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — this framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **SBC (Stock-Based Compensation)** — employee pay in the form of company shares or stock options rather than cash; a real economic cost to existing shareholders through ongoing dilution.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — the interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked in this session, since Phase 01 failed first, but cited in the header per the standard session template).
- **Turnaround Sub-Gate** — the conditional path (Hybrid Upgrade 4) that lets a company failing 2-4 quality criteria still enter as a small (2-3%) position if it passes 5 specific tests (historical ROIC, insider buying, margin of safety, debt level, identifiable moat). Not reachable here — FUBO fails 6 of 8 criteria, outside the eligibility window, and the 10-year historical-ROIC lookback is structurally unreachable regardless.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported financial results. Not used as the primary basis in this session because the relevant 4-quarter window straddles the merger close and blends two non-comparable businesses; the two cleanest fully-combined quarters were used preferentially instead.
