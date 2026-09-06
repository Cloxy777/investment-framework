# NEW POSITION — FICO (Fair Isaac Corporation) — 2026-09-06

**Task type:** NEW POSITION (re-check of a previously-passed candidate; requested via `/rescore FICO`, redirected to `/new-position` since FICO carries no [holdings.md](../portfolio/holdings.md) row — it has never been entered).
**Date:** 2026-09-06. **10Y US Treasury yield:** not fetched — moot, since the Quality Score gate fails decisively before Phase 02/Rate Environment Gate would ever run (see below).
**Prior record:** [2026-06-14 new-position session](2026-06-14-new-position-fico.md) (Phase 01 FAIL) and [2026-07-07 addendum](2026-07-07-new-position-fico.md) (first Quality Score: 79.4–79.6, narrow near-miss). This session supersedes both.

---

## 1. Live price (Rule 0)

IBKR `get_price_snapshot`, contract_id 269280 (NYSE, FAIR ISAAC CORP): **last $934.52**, timestamp 2026-09-04 23:56:16 UTC (Friday's close — markets closed over the 2026-09-05/06 weekend, so this is the most recent live tick available, not an inferred price). Prior close $1,118.93 → **−16.48%** in the referenced session. 52-week range $871.13–$1,995.00.

This large move is **explained**, not unexplained (see Rule 9 check below) — it does not independently trigger anything beyond what the underlying event already triggers.

## 2. Data gaps flagged

None for the Quality Score inputs below — all sourced from primary filings (10-Q/8-K exhibits) or corroborated news reporting of a named regulatory action. Fair-value/Phase 02 inputs (forward PE, 5yr PE range, EV/EBIT) were **not fetched** — moot given the gate result (see step 5 of the `/new-position` procedure: stop before Phase 02 if the gate fails).

## 3. Rule 9 trigger check — one fires, decisively

| Category | Fired? | Detail |
|---|---|---|
| Earnings | Yes (informational) | Q3 FY2026 (quarter ended 30 Jun 2026) reported 30 Jul 2026 — already reflected in the fundamentals below. No new print since. |
| Guidance revision | Yes (informational) | FY2026 guidance raised at Q3 print: revenue $2.45B→$2.53B, GAAP EPS $35.60→$36.86. Reflects strong underlying demand — does not offset the item below. |
| Management change | No | Will Lansing (CEO), Steve Weber (CFO) unchanged. |
| M&A | No | None found. |
| **Macro/regulatory shift** | **YES — fires** | **FHFA (Federal Housing Finance Agency) Director Bill Pulte announced, 2026-09-03, immediate approval of VantageScore 4.0 for all GSE-eligible (Fannie Mae/Freddie Mac) mortgage originations** — ending FICO's decades-long sole-model requirement in that market. Pulte's announcement explicitly cited FICO's pricing power (per-score cost cited as up ~1,800% since 2020) as the rationale. Reported by [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/09/61634335/fico-stock-slides-friday-what-investors-need-to-know), [The Motley Fool](https://www.fool.com/investing/2026/09/04/why-fair-isaac-stock-crashed-today/), [StockStory](https://stockstory.org/us/stocks/nyse/fico/news/why-up-down/why-fair-isaac-corporation-fico-shares-are-getting-obliterated-today), [TIKR](https://www.tikr.com/blog/fair-isaac-stock-plunges-mixed-q3-results-2026). |
| >15% unexplained price move | No (explained) | −16.48% single-session move is the market's reaction to the FHFA/VantageScore news above, not unexplained. |

**This is exactly the disruption vector both prior FICO sessions had already flagged as a bear-case risk** (Sen. Hawley's 23 Mar 2026 FTC letter, the Florida AG's 2 Jul 2026 CID) — it has now materialized as an actual regulatory action with immediate effect, not just an investigation.

## 4. Quality Score recomputation (per [quality-scoring.md](../framework/quality-scoring.md), methodology v2026-06-29)

### Fundamental inputs (TTM = Jul 2025–Jun 2026, rollforward: FY2025 full year − 9mo FY2025 + 9mo FY2026, all figures from primary SEC exhibits)

| Metric | FY2025 (10-K/8-K exhibit, [source](https://www.sec.gov/Archives/edgar/data/814547/000081454725000026/exhibit991erq42025.htm)) | 9mo FY2025 (Q3 FY25 8-K, [source](https://www.sec.gov/Archives/edgar/data/814547/000081454725000024/exhibit991erq32025.htm)) | 9mo FY2026 (Q3 FY26 8-K, [source](https://www.sec.gov/Archives/edgar/data/0000814547/000081454726000031/exhibit991erq32026.htm)) | **TTM (rollforward)** |
|---|---|---|---|---|
| Revenue | $1,990.9M | $1,475.1M | $1,877.8M | **$2,393.6M** |
| Operating income | $924.9M | $687.7M | $999.1M | **$1,236.3M** |
| Net income | $651.9M | $496.9M | $660.0M | **$815.0M** |
| D&A | $15.0M | $10.9M | $12.1M | **$16.2M** |
| Free cash flow | $739M (FY25) | — | — | **$961M** (Q3 FY26 8-K states TTM FCF directly, +28% YoY) |

Balance sheet, as of 30 Jun 2026 (Q3 FY2026 10-Q/8-K): **Total debt $5,582.4M**, **cash $248.4M** → **Net debt $5,334.0M**. Stockholders' deficit **−$4,097.1M** (deepened from −$1,745.8M at FY2025-end, driven by $3,046.0M of YTD FY2026 share repurchases funded substantially by new debt — total debt roughly doubled from $3,055.7M at FY2025-end to $5,582.4M).

TTM EBITDA = Operating income + D&A = $1,236.3M + $16.2M = **$1,252.5M**
**Net Debt/EBITDA = $5,334.0M ÷ $1,252.5M = 4.26×**

Credit rating: **Ba2 (Moody's), sub-investment grade** — no rating action found in 2026 despite the leverage increase (last confirmed affirmation 2021-12-14; a 2026-03 $1B senior notes issuance retired $400M of near-term maturities but did not reduce net leverage). Asset-light override (Upgrade 5, requires investment-grade rating) **does not apply**.

### Sub-scores

| Sub-score (weight) | Calculation | Value |
|---|---|---|
| **Profitability (25%)** | NetMargin_Component: TTM Net Margin 34.06% ($815.0M/$2,393.6M) → clamp((34.06/30)×100) = 100.0 (capped). ROIC_Component: **judgment call, unchanged from 07-07 precedent** — GAAP equity remains deeply negative (−$4,097.1M, deeper than the −$1.7B–$1.8B checked in July), making conventional NI/Equity ROIC undefined; every aggregator methodology checked in the prior session landed comfortably above the 30% cap threshold, and NI has grown further since (TTM $815.0M vs. the prior session's $759.6M), so the direction of evidence is unchanged → 100.0 (capped). FCF positive throughout, no cap. | **100.0** |
| **Margins (15%)** | GrossMargin_Score: TTM/YTD gross margin 85.9% (9mo FY26, up from FY2025's 82%) → clamp((85.9/80)×100) = 107.4 → capped **100.0** | **100.0** |
| **Growth (20%)** | Growth_Score(base) = clamp((12.94/25)×100) = 51.76 (Revenue 3yr CAGR unchanged — FY2025 is still the latest complete fiscal year; FY2026 doesn't close until 30 Sep 2026). **Modifier flips from +10 to −10**: the prior sessions' +10 TAM/pricing-power modifier was explicitly built on GSE sole-acceptance status and uncapped mortgage-royalty pricing — the FHFA/VantageScore action of 2026-09-03 is *documented evidence of a structural (regulatory, not cyclical) threat to that exact TAM/pricing-power thesis* in FICO's largest and most profitable use case, so the framework's "−10: documented evidence growth is decelerating structurally" modifier applies instead. 51.76 − 10 = **41.76** | **41.76** |
| **Balance Sheet (15%)** | BalanceSheet_Score = clamp(100×(1 − 4.26/4), 0, 100) = clamp(−6.5, 0, 100) → **0.0**. **Also independently fires the hard disqualifier** (4.26× > 2.5× standard threshold, asset-light override inapplicable — sub-investment grade) | **0.0** |
| **Moat (15%)** | Re-scored against the same 5-signal checklist used 2026-07-07, in light of the FHFA action: **Market share** — **FALSE** (was TRUE; FHFA's own release describes "ending FICO's decades-long single-model monopoly" in GSE mortgages, its largest and highest-margin use case). **Brand premium/pricing power** — **TRUE**, unchanged (the $0.60→$10.00 5yr price climb was realized without documented volume loss to date; the disruption is prospective, not yet reflected in trailing pricing realization). **Network effect** — **FALSE** (was TRUE via a judgment call resting entirely on GSE-mandated single-standard reliance — that premise is now gone for GSE loans). **Switching costs** — **FALSE** (was TRUE via the same GSE-validation-process evidence that FHFA just short-circuited by approving VantageScore 4.0 immediately, rather than after further multi-year validation). **Scale cost advantage** — FALSE, unchanged (no cost-per-unit data ever found). Signals true: 1 of 5. Moat_Score = (1/5)×100 = 20.0 | **20.0** |
| **FCF Quality (10%)** | TTM FCF/NI = $961M ÷ $815.0M = 117.9% → clamp(((1.179−0.40)/0.60)×100, 0, 100) → capped **100.0**. Cross-check, FY2025 basis: $739M/$651.9M = 113.4% — also capped. Hard disqualifier does not fire on this basis. | **100.0** |

```
Quality Score = 100.0×0.25 + 100.0×0.15 + 41.76×0.20 + 0.0×0.15 + 20.0×0.15 + 100.0×0.10
              = 25.00 + 15.00 + 8.352 + 0.00 + 3.00 + 10.00
              = 61.352 → rounds to 61.4
```

**Quality Score = 61.4 / 100.0 — fails the 80.0+ gate by 18.6 points**, a sharp deterioration from the 07-07 session's 79.4–79.6 (a narrow, near-passing miss). **Also independently fails the hard disqualifier** (Net Debt/EBITDA 4.26× vs. the 2.5× standard threshold) — this alone is sufficient to fail regardless of the weighted score, per quality-scoring.md.

**What changed, in one line each:**
- **Leverage exploded, not improved.** Net Debt/EBITDA moved from 2.61× (07-07) to 4.26× — the opposite of the "credible near-term deleveraging path" the 07-07 session flagged as the one thing that could flip this name. Total debt roughly doubled (funding $3.05B of YTD buybacks) while EBITDA grew only modestly in comparison.
- **The moat thesis's central pillar broke.** 4 of 5 moat signals were true in July; now 1 of 5 is, because three of those four rested directly or indirectly on FICO's sole-acceptance status in GSE mortgage underwriting — the exact status FHFA just ended.
- **The Growth modifier reversed** for the same reason — the TAM/pricing-power evidence that justified +10 in July is now evidence of prospective deceleration, justifying −10.

Per this task's step 2 branching instruction (Quality Score below 80.0 or a hard disqualifier fires → stop, don't proceed to scoring): **no Rate Environment Gate, no Phase 02 valuation score, no Composite Score, and no fair-value/order-setup work was performed** — all would be moot.

## 5. Recommendation

# **PASS — do not enter. Quality Score 61.4/100.0, fails the 80.0+ gate by 18.6 points; also independently fails the Net Debt/EBITDA hard disqualifier (4.26× vs. 2.5×).**

This is now a clear, non-marginal fail — a meaningful step down from the 06-14/07-07 near-miss read. Two things happened simultaneously since 07-07: FICO levered up aggressively to fund buybacks (leverage nearly doubling instead of the hoped-for deleveraging), and its central regulatory moat (sole-acceptance in GSE mortgage underwriting) was structurally broken by FHFA's 2026-09-03 approval of VantageScore 4.0. Both are documented, dated events — not price action — consistent with Rule 9. The stock's −16.48% move is the market correctly repricing a real fundamental deterioration, not noise to buy into.

**Watch item for next check:** whether the market response to VantageScore's approval actually shows up in lender adoption / FICO Score volume data over the next 1–2 quarters (the approval removes a regulatory requirement but doesn't force lenders to switch), and whether Q4 FY2026 (reports ~Nov 2026) shows any deleveraging. Given the scale of this quality deterioration, this is no longer the "closest to passing" name on the watchlist — a full re-check is warranted only if either (a) net debt materially declines, or (b) FICO discloses concrete evidence its GSE mortgage volumes/pricing are holding despite the VantageScore approval.

**No position opened — nothing to log in `decisions/`.**

## 6. Next review trigger

- Q4 FY2026 earnings (fiscal year end 30 Sep 2026; expected report ~early Nov 2026) — check for (a) actual net debt/EBITDA trend (deleveraging vs. further buyback-funded leverage), (b) any disclosed lender/volume impact from the VantageScore approval.
- Any further FHFA/GSE guidance operationalizing the VantageScore approval (timelines, lender adoption mandates or incentives).
- Any Moody's rating action given the near-doubling of debt.

---

## Files touched this session

- `sessions/2026-09-06-new-position-fico.md` — this session log
- `watchlist/not-in-portfolio/FICO/FICO-2026-06-14.md` — new dated row added (score, moat, and underlying thesis changed materially since 07-07)
- `framework/glossary.md` — added **GSE (Government-Sponsored Enterprise)**, **FHFA (Federal Housing Finance Agency)**, **VantageScore**

`watchlist/STALE.md` not touched — FICO was never listed there (no Phase 02 score exists for the 2026-06-29 methodology change to invalidate; this session computes fresh under the current methodology regardless).

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **CFR (Corporate Family Rating)** — Moody's rating of a company's overall consolidated credit risk; FICO's CFR is Ba2, sub-investment grade.
- **CID (Civil Investigative Demand)** — a subpoena-like investigative tool a state AG (or the FTC) uses to compel document production before any lawsuit is filed; Florida's AG issued one to FICO in July 2026, still a separate, ongoing item from this session's FHFA/VantageScore development.
- **FHFA (Federal Housing Finance Agency)** — the US federal regulator overseeing Fannie Mae and Freddie Mac; approved VantageScore 4.0 for all GSE-eligible mortgages on 2026-09-03, ending FICO's sole-model requirement there.
- **GSE (Government-Sponsored Enterprise)** — Fannie Mae and Freddie Mac; their FHFA-set acceptance criteria for conforming mortgages had long required the FICO Score specifically.
- **Hard disqualifier** — a Quality Score condition (Net Debt/EBITDA over threshold, FCF/NI conversion <70% for 2+ years, or not FCF-positive for 3+ years) that fails a company regardless of its weighted score.
- **Quality Score** — this framework's 0–100.0 continuous quality grade; a company must score 80.0+ to proceed to Phase 02 valuation scoring. FICO scores 61.4, down sharply from 79.4–79.6 in July.
- **ROIC (Return on Invested Capital)** — undefined via the conventional NI/Equity route for FICO due to negative GAAP equity; handled here via the same capped-score judgment call used in the 2026-07-07 session.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move. The macro/regulatory-shift category fires this session (FHFA/VantageScore).
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results.
- **VantageScore** — a rival credit-scoring model owned jointly by the three major credit bureaus; FHFA's approval of VantageScore 4.0 for GSE-eligible mortgages ends FICO's exclusivity in that market.
