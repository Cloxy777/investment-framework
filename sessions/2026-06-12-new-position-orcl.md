# NEW POSITION — ORCL (Oracle Corporation) — 2026-06-12

**Task type:** NEW POSITION
**Date:** 12 Jun 2026
**10Y US Treasury Yield:** 4.46% (FRED DGS10, 11 Jun 2026 close)
**Rate Regime Modifier (would apply if scored):** +5 (10Y in the 3.5–5% bracket) — **not applied; Phase 01 gate fails before Phase 02 is reached**
**Current ORCL portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Technology — Enterprise Software / Cloud Infrastructure (Database, ERP/SaaS Applications, and Oracle Cloud Infrastructure — OCI — for AI/datacenter workloads)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$182.77** | WebSearch (intraday quote tagged "today, June 12, 2026"); IBKR `search_contracts`/`get_price_snapshot` permission denied, fell back to WebSearch per task instructions |
| Intraday range (12 Jun 2026) | $179.00 – $185.90 | WebSearch aggregation |
| 52-week high / low | $345.72 / $134.57 | WebSearch aggregation (stockanalysis.com-style forecast page) |
| Analyst consensus PT (12-mo) | ~$251–255 (43 analysts, avg ~$255.38 / ~$251.20 across two sources; range $155–$400) | WebSearch aggregation |
| Analyst consensus rating | 36 Buy / 6 Hold / 1 Sell | WebSearch aggregation |
| Trailing P/E (as quoted) | 31.58× | WebSearch aggregation |
| Market cap (at $182.77) | ~$525.74B | WebSearch aggregation |

**Context:** ORCL trades at $182.77, down sharply (~47%) from its 52-week high of $345.72 (set during the 2025 OCI/AI-datacenter re-rating), but still up ~36% from its 52-week low of $134.57. Search results explicitly attribute recent volatility to "Oracle's earnings announcement about increased AI infrastructure spending plans" — i.e., the market reaction to the same FY2026 Q4 results (reported 10 Jun 2026, two days before this session) that this session's Phase 01 analysis is built on. This is the live, intraday price used throughout — no price was inferred from multiples.

---

## 2. Data Gathered (Phase 01 Inputs) & Gaps Flagged

| Metric | Value | Source / Derivation |
|---|---|---|
| FY2022 Revenue (ended 31 May 2022) | $42.4B | Oracle FY2022 Q4 8-K |
| FY2023 Revenue | $50.0B | Oracle FY2023 Q4 8-K |
| FY2024 Revenue | $53.0B (+6% YoY) | Oracle FY2024 Q4 8-K |
| FY2025 Revenue | $57.4B (+8% YoY) | Oracle FY2025 Q4 8-K |
| **FY2026 Revenue** (ended 31 May 2026, reported 10 Jun 2026) | **$67.4B (+17% YoY)**, record, Cloud revenue $34.0B (+39%) | Oracle FY2026 Q4 8-K / earnings release |
| **Revenue CAGR 3yr** (FY2023 $50.0B → FY2026 $67.4B) | **10.46%** = (67.4/50.0)^(1/3) − 1 | Computed |
| FY2025 GAAP net income | $12.4B | Oracle FY2025 Q4 8-K |
| FY2025 net margin | **21.6%** ($12.4B / $57.4B) | Computed |
| **FY2026 GAAP net income** (available to common) | **$17.0B (+36% YoY)** | Oracle FY2026 Q4 8-K |
| **FY2026 net margin** | **25.2%** ($17.0B / $67.4B) | Computed |
| FY2025 ROIC | 12.27% | GuruFocus |
| **ROIC, most recent (Feb 2026, annualized)** | **9.05%** — down from 12.27% (FY2025) | GuruFocus |
| FY2024 quarterly FCF (OCF − CapEx): Q1 $9,455M / Q2 $10,104M / Q3 $12,258M / Q4 $11,807M | **FY2024 FCF ≈ $43.6B** | Oracle 8-Ks — summed |
| FY2025 quarterly FCF: Q1 $11,271M / Q2 $9,542M / Q3 $5,812M / Q4 **−$394M** | **FY2025 FCF ≈ $26.2B** (Q4 already negative as capex ramped) | Oracle 8-Ks — summed |
| **FY2026 full-year FCF** | **−$23.7B** (negative) — OCF $32B (+54% YoY) vs. capex that drove this deeply negative | Oracle FY2026 Q4 8-K / earnings release |
| FY2026 D&A | $7.62B (nearly doubled YoY) | Oracle FY2026 Q4 8-K |
| FY2026 capital raised | **$43B in debt + $5B in equity** during FY2026 | Oracle FY2026 Q4 8-K |
| Total debt (Q1 FY2026, Aug 2025) | $124.7B (up from $88.1B YoY) | companiesmarketcap.com / TradingEconomics |
| **Total debt (Q3 FY2026, Feb 2026)** | **$134.6B** (up from $92.6B nine months earlier) | Oracle Q3 FY2026 10-Q / earnings release |
| **Net debt (Q3 FY2026, Feb 2026)** | **$95.5B** | Oracle Q3 FY2026 earnings release |
| **EBITDA, annualized (Feb 2026)** | **$32.648B** (ST debt $9,887M + LT debt $143,230M components per GuruFocus debt schedule) | GuruFocus |
| **Net Debt/EBITDA (Feb 2026)** | **2.93×** = $95.5B / $32.648B | Computed |
| Debt-to-EBITDA, 10yr median (GuruFocus) | 4.28× (current 4.69× is "10% above" this median — gross-debt basis, not net) | GuruFocus |
| Equity financing FY2026 | $5B common stock raised; equity distribution agreements (ATM) for **up to $20B** of common stock; calendar-2026 plan to raise **$45–50B gross** (debt + equity + mandatory convertible preferred) to fund OCI buildout | SEC 424B5/FWP filings, Feb 2026 |
| Shares outstanding (30 Nov 2025) | 2,872,573,090 | SEC 424B2 filing |
| RPO (Remaining Performance Obligations) | $638B, +363% YoY — large AI-related contract backlog | Oracle FY2026 Q4 8-K |
| Gross margin | Not independently confirmed this session (FY2026 commentary flags an **expected step-down in FY2027 gross margin** "due to timing for the ramp-up of data center projects") | WebSearch — directional only, see Gap #3 |

### Data Gaps / Flags

1. **FY2026 10-K not yet filed** (fiscal year ended 31 May 2026; 10-K filed within 60–90 days). All FY2026 figures used here come from the 10 Jun 2026 earnings release (8-K) and earnings call commentary, which is the best currently-available primary source — but the detailed balance sheet (period-end total debt, cash, and EBITDA components as of 31 May 2026) is not yet available; the **$134.6B debt / $95.5B net debt / $32.648B EBITDA figures are as of Q3 FY2026 (28 Feb 2026)**, the most recent point for which a full balance sheet is available. Given debt issuance accelerated further in Q4 (part of the $43B FY2026 debt raise), the year-end Net Debt/EBITDA ratio is more likely to be **higher** than 2.93× than lower. This is a conservative (favorable-to-ORCL) gap, not one that could flip the FAIL to a PASS.
2. **Gross margin** was not independently confirmed as a clean $ figure this session (searches returned operating-margin data, not COGS/gross-margin breakdowns). Given (a) Phase 01 already fails decisively on three independent criteria below (FCF, Net Debt/EBITDA, ROIC, plus a flagged dilutive-issuance pattern), and (b) management's own commentary flags **further gross-margin compression** in FY2027 from data-center ramp timing — gross margin is very unlikely to be the swing factor, so this gap does not block the FAIL conclusion. Flagged rather than estimated, per "never invent or estimate financial data."
3. **ROIC source is a third-party aggregator (GuruFocus)** without visibility into the exact NOPAT/invested-capital formula — but the **direction** (12.27% FY2025 → 9.05% Feb 2026, a clear decline as the debt-funded capex base grows faster than incremental NOPAT) is consistent with the FCF and leverage data independently gathered, and is the relevant signal for Phase 01 regardless of the exact basis-point precision.

---

## 3. Phase 01 — Quality Gate

| Check | ORCL Value | Threshold | Result |
|---|---|---|---|
| Net margin (FY2026) | 25.2% | >15% | ✅ PASS |
| **ROIC (Feb 2026, annualized)** | **9.05%**, down from 12.27% (FY2025) | >15% | ❌ **FAIL** |
| Revenue CAGR 3yr (FY2023→FY2026) | 10.46% | >10% | ✅ PASS (narrow) |
| Gross margin | Not independently confirmed this session; management flags further FY2027 compression from datacenter ramp timing | >40% or expanding | ⚠️ Not confirmed — see Gap #2 (does not change gate outcome) |
| **FCF positive 3 consecutive years** | FY2024 ≈+$43.6B → FY2025 ≈+$26.2B → **FY2026 −$23.7B** | required | ❌ **FAIL** — most recent year deeply negative |
| **Net debt/EBITDA** | **2.93×** (Feb 2026, and likely higher by FY2026 year-end given continued debt issuance) | <2x (core) / <2.5x (Phase 01 pre-screen) | ❌ **FAIL** — exceeds both the 2× core threshold and the 2.5× pre-screen threshold |
| FCF/NI conversion ratio | Not meaningfully computable — FY2026 FCF is negative against positive net income, so the ratio is negative / not a quality signal in the conventional sense | >70% for 2+ years | ❌ **FAIL** (mechanically, given negative FCF) |
| **Share issuance pattern** | **$5B common equity raised in FY2026**, plus equity distribution (ATM) agreements for **up to $20B** of common stock and mandatory convertible preferred stock, as part of a $45–50B calendar-2026 capital plan | non-dilutive required | ❌ **FAIL** — explicitly dilutive issuance pattern, in progress |
| Moat signal | Dominant enterprise database franchise + fast-growing OCI (Cloud revenue +39% YoY to $34.0B) + record RPO $638B (+363%, large AI contracts) | required | ✅ Qualitatively strong — **moat is not the problem here** |

**Gate result: FAIL — Stopping per operating brief.**

> "Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring."

ORCL fails Phase 01 on **four independent criteria** — ROIC (9.05% vs >15%), FCF positive 3 consecutive years (FY2026 −$23.7B), Net Debt/EBITDA (2.93× vs <2x core / <2.5x pre-screen), and non-dilutive share issuance (explicit $5B raise + up to $20B ATM program + mandatory convertible preferred). Per the operating brief, this session **does not proceed** to the Rate Environment Gate, Phase 02 valuation score, or the fair-value/order-setup workup.

### Did the Debt Gate Context (Upgrade 5) change the threshold?

No. Upgrade 5's relaxed **<4× Net Debt/EBITDA** threshold applies only to "payment networks, exchanges, asset-light businesses where 100% of debt is financial," provided interest coverage >15× and investment-grade rated. Oracle is an enterprise software/cloud-infrastructure company financing **owned physical datacenter capex** with this debt — it is not asset-light and its debt is not "100% financial" in the Upgrade 5 sense. The **standard <2x (core) / <2.5x (pre-screen)** thresholds apply, and ORCL's 2.93× fails both.

### Did the Turnaround Sub-Gate (Upgrade 4) open an alternate path?

No — it requires **all five** of:
1. Historical ROIC >15% for ≥5 of the past 10 years — **not verified this session**, but the *direction* (12.27% FY2025 → 9.05% Feb 2026, declining as the debt-funded capex base scales) suggests Oracle's ROIC may have been historically modest even before the OCI buildout (Oracle has long carried a sizable legacy database/license business with a large debt-funded buyback history rather than a high-ROIC growth profile). Even if this condition were met historically, it doesn't matter given the next point.
2. CEO/CFO insider buying >$500K in past 6 months (Form 4-verified) — **not checked / no evidence found**.
3. Independent FV estimate showing ≥40% MOS — not built (gate fails before this step).
4. **Net Debt/EBITDA <3×** — ✅ would technically pass at 2.93× (Feb 2026), though this is razor-thin and likely to be exceeded by FY2026 year-end given continued debt issuance (Gap #1).
5. Core moat still identifiable — ✅ yes (database + OCI franchise).

Even granting condition 4 (borderline) and condition 5, conditions 1–3 cannot be confirmed — and more fundamentally, the Turnaround Sub-Gate exists for "businesses failing 2–4 quality criteria" with a path back via **demonstrated capital discipline and insider conviction**. Oracle's situation is the opposite of a fallen-angel turnaround: this is a **high-quality, moat-intact business in the middle of a massive, deliberate, debt-and-equity-funded capex super-cycle** — a fundamentally different risk profile than "deteriorating business, management buying the dip." The Turnaround Sub-Gate's framing doesn't fit, and it doesn't open a path here regardless.

---

## 4. Why This Is a Distinctive Case — and What Would Flip the Verdict

This is **not** a "broken business trading at a discount" Phase 01 fail (like CRM's structural ROIC shortfall) or a "too close to call" fail (like TTD's 0.44pp net-margin miss). ORCL's Phase 01 failure is the **direct, deliberate, and currently-still-accelerating mechanical consequence of a single capital-allocation decision**: management is choosing to spend far more on datacenter capex than operating cash flow can currently fund, financed by a $45–50B calendar-2026 debt+equity raise, in pursuit of a $638B RPO backlog (+363% YoY) of AI/OCI contracts.

**The bull case (not evaluated further here, since the gate stops the session) is essentially:** this capex is high-ROIC growth capex that will convert RPO into revenue and FCF over the next several years, at which point ROIC, FCF, and leverage all normalize favorably — i.e., today's Phase 01 metrics understate the steady-state business. Management's own commentary supports this directionally ("infrastructure business expected to have ROIC in the high 20s at steady state").

**The framework's own non-negotiables, however, are explicit that this kind of "trust the narrative, the trailing numbers will catch up" reasoning is exactly what Phase 01's trailing-financials gate exists to filter out** — "never invent or estimate financial data" and "act only on documented triggers ... never on price movement alone" cut both ways: a forward narrative of margin/ROIC/FCF normalization is not yet a documented trigger either.

**What would flip the verdict** — concretely, in order of most to least likely to resolve soon:
- **FY2026 10-K (within ~60–90 days)** confirms the year-end Net Debt/EBITDA and gross margin figures with full-year precision (Gap #1/#2) — unlikely to flip Net Debt/EBITDA below 2× given the trajectory, but should be re-checked.
- **FCF trajectory**: if FY2027 FCF returns to positive as RPO converts to billed/collected revenue and the capex super-cycle peaks, the "3 consecutive years" FCF check would need re-basing from FY2027 (FY2025 +$26.2B, FY2026 −$23.7B, FY2027 +X) — at least 2 more years of data needed.
- **ROIC**: needs to demonstrably stabilize and turn upward (toward >15%) as the new OCI capacity comes online and starts generating revenue against the now-larger asset base — likely a multi-quarter-to-multi-year process.
- **Net Debt/EBITDA**: needs EBITDA growth to outpace further debt issuance — currently moving the wrong direction (debt growing faster than EBITDA as of the Feb 2026 data point).
- **Equity issuance**: the $45–50B calendar-2026 plan is **ongoing** — a near-term re-check would likely still find dilutive issuance in progress.

None of these are likely to resolve within the next 1–2 quarters. This is a **multi-quarter-to-multi-year re-check**, not a "wait for next earnings" one.

---

## 5. Recommendation

# **PASS — do not open a position now.**

ORCL fails the Phase 01 quality gate on **four independent criteria** (ROIC 9.05% vs >15% required, FCF −$23.7B in FY2026 vs "positive 3 consecutive years" required, Net Debt/EBITDA 2.93× vs <2x/<2.5x required, and an explicit ongoing dilutive equity-issuance program), despite genuinely strong top-line growth (+17% revenue, Cloud +39%), a record $638B RPO backlog, and a qualitatively intact/strengthening moat (database + OCI). Per this framework's rules, a forward growth narrative — however well-supported by RPO and management commentary — is not sufficient to override a trailing-financials gate failure; that would be the same "trust the story, the numbers will catch up" reasoning the gate exists to filter, applied in the opposite direction from CIEN's case but with the same structure.

**Add ORCL to the watchlist** with a re-evaluation trigger at:
- **FY2026 10-K filing** (expected within ~60–90 days of 31 May 2026 fiscal year-end, i.e., by ~Aug–Sept 2026) — confirms year-end Net Debt/EBITDA, gross margin, and full FCF detail.
- **FY2027 Q1 earnings** (expected ~Sept 2026) — first read on whether FCF is recovering from the FY2026 trough and whether ROIC has stabilized/turned.
- Any **further guidance revision** on the FY2026/calendar-2026 capital plan (Rule 9 trigger) — e.g., if the $45–50B raise plan is revised up or down, or if management provides a more specific FCF-recovery timeline.

---

## 6. Next Review Trigger

**Date/event:** ORCL's FY2026 10-K filing (expected ~Aug–Sept 2026) and/or FY2027 Q1 earnings (expected ~Sept 2026) — re-run Phase 01 with refreshed full-year FCF, year-end Net Debt/EBITDA, ROIC trend, and gross margin. If FCF has returned to positive and Net Debt/EBITDA has stabilized below 2.5×, proceed to Rate Gate + Phase 02. Earlier trigger if a material capital-plan revision (Rule 9) is announced, or a >15% unexplained price move from $182.77 occurs.

**No position opened — nothing to log in `decisions/`.**
