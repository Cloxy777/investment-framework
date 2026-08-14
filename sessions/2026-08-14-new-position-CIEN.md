# New Position Evaluation — CIEN (Ciena Corporation)

**Task:** NEW POSITION
**Date:** 14 Aug 2026
**10Y US Treasury Yield:** 4.645% (13 Aug 2026 close, little-changed 14 Aug 2026 per CNBC/FRED — informational only, since Phase 02 is never reached)
**Rate Regime (informational only, not applied):** 3.5–5% band → would be a +5 modifier if a valuation score were computed
**Trigger:** Direct user request — routine re-check of an existing watchlist name. Prior entries: [2026-06-11 first evaluation](../watchlist/not-in-portfolio/CIEN/CIEN-2026-06-11.md) (Phase 01 FAIL) and a [2026-07-06 addendum](../watchlist/not-in-portfolio/CIEN/CIEN-2026-06-11.md) (first Quality Score: 57.7/100.0, fails the 80.0+ gate). This session is a fresh, full end-to-end re-run — not an addendum — per direct instruction, over 2 months after the last dated watchlist row.

---

## 1. Data gaps flagged

None that change the outcome. One methodology note, now resolved rather than open:

- **ROIC / Invested Capital convention:** the 2026-07-06 addendum flagged an open inconsistency between [glossary.md](../framework/glossary.md)'s written Invested Capital definition ("debt + equity − cash") and a different, non-cash-netted convention used in an earlier (CCL) session. Checked this session: glossary.md's **Invested Capital** entry (line 258) explicitly reads *"This framework nets out cash (debt + equity − cash) when computing it, consistent with how Net Debt/EBITDA already nets cash from gross debt."* This is the standing, documented convention — so the cash-netted reading (ROIC 15.32%, Quality Score 57.7) is used as primary here, not a 50/50 toss-up, with the non-netted figure shown only as a cross-check for transparency.
- No new fiscal quarter has been filed since the 07-06 addendum (confirmed below, §2/§4) — the TTM window (Q3 FY2025 through Q2 FY2026) and every underlying figure are unchanged and still current, not stale. Re-sourcing was not required; every figure below is the same real, filed data already sourced and cited in the 07-06 session, carried forward because the underlying fiscal facts have not changed.

---

## 2. Live Price (Rule 0)

Fetched directly from IBKR real-time market data (contract_id 41045553, NYSE), 14 Aug 2026, regular session, live/real-time — never inferred from multiples:

| Field | Value |
|---|---|
| **Live price (intraday, real-time)** | **$436.15** |
| Change vs. prior close | −$6.64 (**−1.5%**) |
| Today's range | $426.01 – $446.15 (open $438.10) |
| 52-week range | $84.46 – $637.09 |
| 52-week open (1yr ago) | $92.88 |
| Today's volume (partial session) | ~703K shares |
| Bid / Ask | $435.93 / $436.67 |

**Price-move check (Rule 9 trigger #6):** $436.15 today vs. $428.97 on 2026-07-06 = **+1.67%**, vs. $441.36 on 2026-06-11 = **−1.18%**. Both far short of the >15% unexplained-move threshold — no trigger.

---

## 3. Rule 9 fundamental-trigger check (all 6 categories, since the 07-06 addendum)

| Trigger | Result |
|---|---|
| Earnings | **No new report.** Q2 FY2026 (quarter ended 2 May 2026) remains the latest reported quarter. Q3 FY2026 is confirmed scheduled for **Thursday, 3 September 2026**, before market open (Ciena's own investor-relations reporting-date announcement) — not yet reported as of this session. |
| Guidance revision | None since 07-06. FY2026 revenue guidance remains $6.3B ±$100M (32% YoY at midpoint), raised 4 Jun 2026 and already reflected in both prior sessions. |
| Management change | None found. (Marc Graff became CFO 1 Aug 2025 — already old news, predates both prior sessions.) |
| M&A / capital raise | None new. The $2.875B convertible-note closing (11 Jun 2026) and the Nubis Communications acquisition (closed 7 Oct 2025) both predate the 07-06 addendum and were already reflected there. |
| Macro shift | None new. |
| >15% unexplained price move | No (+1.67% vs. 07-06, −1.18% vs. 06-11). |

**Conclusion: no Rule 9 trigger has fired since the 07-06 addendum.** The TTM window used for every fundamental figure below (Q3 FY2025 through Q2 FY2026) is identical to the 07-06 session's window, because no new fiscal quarter has been filed in the interim. Figures are carried forward as current, real, filed data — not re-estimated, not stale.

---

## 4. Phase 01 — Quality Score (0–100.0)

Per [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29 (current — no version bump since 07-06, so no stale-score concern here).

### Hard disqualifiers — checked first

| Disqualifier | Result | Evidence |
|---|---|---|
| Not FCF-positive for 3+ consecutive years | **Does not fire** | FY2023 $62.14M, FY2024 $377.89M, FY2025 $665.29M, TTM $832.66M — all positive. Rolling-window check (per the 2026-08-05 clarification): the most recently completed fiscal years (FY2023–FY2025) are all positive. |
| FCF/NI conversion <70% for 2+ consecutive years, no growth-capex explanation | **Does not fire** | The two most recently completed fiscal years — FY2024 (450.1%) and FY2025 (539.4%) — are both far above 70%. (FY2022 and FY2023 were below 70%, one negative-FCF year during the 2021–22 industry-wide component-shortage period, but that window has rolled out of the "most recently completed" test per the 2026-08-05 rolling-window clarification.) |
| Net Debt/EBITDA over threshold (2.5×) | **Does not fire** | 0.164× (company-disclosed Net Debt $138M ÷ TTM EBITDA $842.25M) — nowhere near the standard 2.5× threshold. |

**No hard disqualifier fires.**

### Sub-score calculations

**Profitability (25% weight)**
```
TTM Revenue      = $5,569.15M
TTM Net Income   = $438.30M
TTM Net Margin   = 438.30 / 5,569.15 = 7.87%

TTM EBIT (GAAP)  = $567.82M
Effective tax rate (TTM) = 8.85%
NOPAT            = 567.82 × (1 − 0.0885) = $517.57M

Invested Capital (glossary.md convention: debt + equity − cash)
  = Debt $1,531.12M + Equity $2,892.23M − Cash $1,045.13M = $3,378.22M
TTM ROIC         = 517.57 / 3,378.22 = 15.32%

NetMargin_Component = clamp((7.87/30)×100, 0, 100)  = 26.23
ROIC_Component       = clamp((15.32/30)×100, 0, 100) = 51.07
Profitability_Score  = (26.23 + 51.07) / 2 = 38.65
```
(No FCF-positivity cap — 3+ years positive, cap doesn't apply.)

*Cross-check, non-cash-netted Invested Capital (Debt + Equity, no cash netting) = $4,423.34M → ROIC 11.70% → ROIC_Component 39.00 → Profitability_Score (cross-check) = 32.62. Not used as primary — see §1.*

**Margins (15% weight)**
```
TTM Gross Margin = 2,397.33 / 5,569.15 = 43.05%
GrossMargin_Score = clamp((43.05/80)×100, 0, 100) = 53.81
```
No structural-trend bonus (bonus only applies while *below* the 40% static threshold — CIEN already clears it at 43.05%).

**Growth (20% weight)**
```
Revenue 3yr CAGR (FY2022 $3,632.66M → FY2025 $4,769.51M) = (4,769.51/3,632.66)^(1/3) − 1 = 9.51%/yr
Growth_Score (raw) = clamp((9.51/25)×100, 0, 100) = 38.03
```
**+10 documented TAM-expansion modifier applied** (unchanged evidence, still current — no newer figures exist since Q2 FY2026 is still the latest reported quarter):
- Record backlog of $7.7B, up >$600M sequentially in Q2 FY2026, with management stating >80% of current hardware backlog is expected to convert to revenue within 12 months.
- FY2026 revenue guidance raised to $6.3B ±$100M (32% YoY at midpoint).
- Dell'Oro Group: global optical-transport market +10% YoY to $16B in 2025; Ciena was the largest single 2025 US market-share gainer (+3pp) among major vendors.
```
Growth_Score = 38.03 + 10 = 48.03
```

**Balance Sheet (15% weight)**
```
Net Debt/EBITDA = $138M / $842.25M = 0.164×
BalanceSheet_Score = clamp(100 × (1 − 0.164/4), 0, 100) = 95.90
```
*Cross-check (Yahoo cash-only Net Debt $485.99M, same EBITDA) = 0.577× → 85.57 — same conclusion (very strong balance sheet either way).*

**Moat Signal (15% weight)** — checklist, cited evidence only:

| Signal | TRUE/FALSE | Evidence |
|---|---|---|
| Market share stable or growing | **TRUE** | Dell'Oro Group: ~50% US optical-transport share, largest single 2025 share gain among major vendors (+3pp), top-3 DCI (Data Center Interconnect) revenue share alongside Nokia and Cisco. |
| Brand premium | **TRUE** | Q2 FY2026 8-K: GAAP gross margin +380bps YoY to 44.0% (adjusted 44.9%), achieved simultaneously with 40% YoY revenue growth and continued share gains — margin expansion without discounting for volume. |
| Network effect | FALSE | Hardware equipment vendor, no marketplace/platform dynamics. |
| Switching costs | FALSE | Ciena's own OFC 2026 positioning explicitly promotes *open, interoperable* standards to *reduce* vendor lock-in — works against, not for, a lock-in-based moat. |
| Scale cost advantage | FALSE | No cost-per-unit-vs-competitor citation found this session. |

```
Moat_Score = (2/5) × 100 = 40.0
```

**FCF Quality (10% weight)**
```
TTM FCF = $832.66M   TTM Net Income = $438.30M
FCF/NI ratio = 832.66 / 438.30 = 190.0%
FCFQuality_Score = clamp(((1.90 − 0.40)/0.60)×100, 0, 100) = 100.0 (capped)
```

### Final Quality Score

```
Quality Score = (38.65×0.25) + (53.81×0.15) + (48.03×0.20) + (95.90×0.15) + (40.0×0.15) + (100.0×0.10)
              = 9.6625 + 8.0715 + 9.606 + 14.385 + 6.00 + 10.00
              = 57.7245 → rounded 57.7
```

*Cross-check (non-cash-netted ROIC convention, Profitability_Score 32.62): 32.62×0.25 + 53.81×0.15 + 48.03×0.20 + 95.90×0.15 + 40.0×0.15 + 100.0×0.10 = 8.155 + 8.0715 + 9.606 + 14.385 + 6.00 + 10.00 = 56.2 — same conclusion, still well short of 80.0.*

## QUALITY SCORE: 57.7 / 100.0 — GATE: **FAIL** (threshold 80.0)

Unchanged from the 07-06 addendum's first-ever computation (57.7) — expected, since no new fiscal quarter has been reported and every underlying input is identical. Per [quality-scoring.md](../framework/quality-scoring.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md), the evaluation stops here: **Phase 02 valuation scoring, the Rate Environment Gate, the Composite Score, and fair-value/order-setup work are not computed.** This is the correct, complete outcome for a gate this strict, not an incomplete session.

---

## 5. Why this matters despite the failing score — qualitative context

The operating story continues to look like a genuine inflection, not hype — but a TTM quality score is, by construction, still weighed down by the weaker FY2024/early-FY2025 years sitting inside the trailing window:

- Q2 FY2026 alone: +40% YoY revenue, gross margin 44.0% GAAP (+380bps YoY), record $7.7B backlog.
- FY2026 guidance raised to $6.3B ±$100M (32% YoY at midpoint), with management citing strong 2027 visibility despite ongoing supply constraints.
- Balance sheet materially de-risked by the $2.875B 0%-coupon convertible-note refinancing (closed 11 Jun 2026), which retired the prior term loan — Net Debt/EBITDA of 0.164× is now excellent.
- Two moat signals now clear the evidentiary bar (market share, brand premium/pricing power) — up from a middling starting point.

**None of this yet moves the Quality Score outcome.** TTM Net Margin (7.87%) and TTM Revenue 3yr CAGR (9.51%) remain the binding constraints — both still meaningfully below the Profitability/Growth sub-score thresholds (30% and 25% respectively) that would be needed to clear 80.0 overall. The single strongest quarter in the company's history (Q2 FY2026) is not yet enough, on a trailing basis, to outweigh FY2024's thinner-margin comparison base. This is exactly the kind of "story inflecting, track record not yet caught up" case the strict 80.0+ gate is designed to hold at watchlist rather than let straight through on one good quarter — consistent with how this framework has treated similar names (AAOI, LITE) in its most recent sessions.

---

## 6. Recommendation

**PASS — watchlist only, do not enter a position.** Quality Score 57.7/100.0 fails the 80.0+ gate by a wide margin (22.3 points short), with no hard disqualifier firing independently. No Composite Score exists to check against the Phase 03 [Action Table](../framework/strategy.md#action-table-summary), and no fair-value/order-setup work is produced, per [fair-value-methodology.md](../framework/fair-value-methodology.md) and [.claude/commands/new-position.md](../.claude/commands/new-position.md) (both gate that step on a passing Quality Score).

**Next review trigger:** Q3 FY2026 earnings, confirmed scheduled **3 September 2026** — re-run Phase 01/Quality Score with the new TTM window (which will roll in Q3 FY2026 and drop Q3 FY2025, likely pulling Net Margin and Revenue CAGR meaningfully higher given the current growth trajectory). Earlier if a guidance revision, management change, other Rule 9 event, or a >15% unexplained move from $436.15 occurs.

---

## Watchlist / stale-score bookkeeping

- **Watchlist:** [watchlist/not-in-portfolio/CIEN/CIEN-2026-06-11.md](../watchlist/not-in-portfolio/CIEN/CIEN-2026-06-11.md) updated with a "Last checked (no significant change)" entry rather than a new dated file — per [watchlist/README.md](../watchlist/README.md#significant-change--when-does-a-new-dated-entry-get-created), a new row is only warranted when the score changes, the scored↔unscored status changes, the action category changes, or a Rule 9 trigger fires. None of those apply here: the score is unchanged (57.7 → 57.7), the status is unchanged (Quality Score computed, fails gate), the action is unchanged (PASS — watchlist), and §3 above confirms no Rule 9 trigger fired since 07-06.
- **STALE.md:** CIEN does not appear in [watchlist/STALE.md](../watchlist/STALE.md) — it is explicitly excluded there as "Phase 01 FAIL / not scored" for Phase 02 purposes (no Valuation/Composite Score exists to go stale), and its Quality Score was already computed under the current 2026-06-29 methodology in the 07-06 addendum. No STALE.md edit needed.

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session:

- **8-K** — a US company's "current report" filed with the SEC disclosing a material event between regular filings; the source for Ciena's Q2 FY2026 earnings-release exhibit figures cited here.
- **Backlog** — the dollar value of signed customer orders not yet recognized as revenue; Ciena's stands at a record $7.7B, cited as Growth sub-score TAM-expansion evidence.
- **BalanceSheet_Score** — this framework's 0–100 Quality Score sub-score derived from Net Debt/EBITDA.
- **CAGR (Compound Annual Growth Rate)** — the smoothed yearly growth rate implied by a start and end value over several years.
- **Composite Score** — this framework's 50/50 blend of Quality Score and Valuation Score; not computed here since CIEN never clears the Quality Score gate.
- **Convertible senior notes** — a bond convertible into the issuer's shares at a preset strike price; Ciena closed $2.875B of 0.00%-coupon convertible senior notes due 2031 in June 2026, materially de-risking its balance sheet.
- **DCI (Data Center Interconnect)** — the optical-networking sub-segment linking separate data centers over fiber, where Ciena holds a top-3 vendor position by revenue share.
- **Dell'Oro Group** — an independent telecom/networking market-research firm, the third-party source for Ciena's market-share figures in this session.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation, and Amortization.
- **Effective tax rate** — the actual share of pretax income paid as tax.
- **FCF (Free Cash Flow)** — cash generated after running and maintaining the business.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income; checks whether reported accounting profit is actually turning into cash.
- **GAAP** — Generally Accepted Accounting Principles; the standard US accounting rulebook, used for all scored figures in this session (never non-GAAP/adjusted figures).
- **Gross Margin** — Gross Profit ÷ Revenue; one of the Quality Score's Margins sub-score inputs.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company outright regardless of its weighted sub-score total; none fire for CIEN this session.
- **Invested Capital** — the capital (debt + equity, netted for cash per this framework's glossary convention) deployed in a business; the ROIC denominator.
- **Moat** — a durable competitive advantage protecting a business's profits from competitors; scored here via a 5-signal checklist.
- **Net Debt/EBITDA** — net debt divided by EBITDA; this framework's primary balance-sheet leverage gate. CIEN's is 0.164×, very strong.
- **Net Margin** — Net Income ÷ Revenue; one of the Quality Score's Profitability sub-score inputs.
- **NOPAT (Net Operating Profit After Tax)** — EBIT × (1 − effective tax rate); the numerator of ROIC.
- **Quality Score** — this framework's 0.0–100.0 continuous quality grade across profitability, margins, growth, balance sheet, moat, and FCF quality; a company must score 80.0+ to proceed to Phase 02 valuation scoring. CIEN scores 57.7 and fails the gate.
- **ROIC (Return on Invested Capital)** — how efficiently a company turns invested capital into profit; a core Quality Score input.
- **Rule 0** — this framework's standing instruction to always fetch a live, current price before any valuation work.
- **Rule 9** — this framework's list of events that force an immediate re-valuation: earnings, guidance revision, management change, M&A, macro shift, or a >15% unexplained price move. None fired this session.
- **TAM (Total Addressable Market)** — the total revenue opportunity available if a company captured its entire target market.
- **TTM (Trailing Twelve Months)** — the most recent 12 months of reported results, as used throughout this session's sub-score calculations.
