# NEW POSITION — GTLB (GitLab Inc.) — 2026-06-12

**Task type:** NEW POSITION
**Date:** 12 Jun 2026
**10Y US Treasury Yield:** 4.46% (FRED DGS10, 11 Jun 2026 close — most recent available)
**Rate Regime Modifier (Step 2, would apply if scored):** +5 (10Y in the 3.5–5% bracket) — **not applied; Phase 01 gate fails before Phase 02 is reached**
**Current GTLB portfolio weight:** 0% — not currently held (not on [holdings.md](../portfolio/holdings.md))
**Sector:** Technology — DevOps & DevSecOps Software (AI-powered software development platform; competes with GitHub/Microsoft, Atlassian)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **~$28.00** (converging range $27.85–$28.92 intraday) | WebSearch aggregation (stockanalysis.com / Yahoo / CNN, 12 Jun 2026) — see note below |
| Prior close | $28.51 | WebSearch (stockanalysis.com-style aggregation) |
| Day's range | $27.85 – $28.92 | WebSearch aggregation |
| 52-week range | $18.73 – $52.38 (all-time low $18.73 hit 10 Apr 2026) | WebSearch aggregation (multiple sources consistent) |
| Analyst consensus PT | ~$33.61 ("Hold", 27 analysts) — recent post-Q1-earnings target raises: DA Davidson $24→$35 (Neutral), BofA $32→$34 (Neutral) | stockanalysis.com / WebSearch aggregation |
| Market cap | ~$4.8B | WebSearch aggregation |

⚠️ **Source variance flagged (Rule 0):** IBKR `search_contracts`/`get_price_snapshot` were attempted first per protocol but **permission to call the IBKR MCP tool was denied in this session** — WebSearch was used as the fallback per the task instructions. Two WebSearch passes returned slightly different "current price" figures ($28.14 in one pass, $25.62 in another, alongside a "previous close" of $28.40–$28.51 in both) — the $25.62 figure appears to be a stale or mis-scraped value, as it is inconsistent with every other source (day range $27.85–$28.92, prior close ~$28.51, and the post-earnings target raises which imply a price in the high-$20s). **$28.00 (midpoint of the converging $27.85–$28.92 day range / ~$28.51 prior close) is used as the working live price** — precise enough for this session given Phase 01 fails regardless of whether the exact price is $27.85 or $28.92 (a <4% band, immaterial to the gate outcome below).

**Context:** GTLB trades ~46% below its 52-week high ($52.38, set roughly a year ago) and is up ~50% off its 10 Apr 2026 all-time low ($18.73). The stock fell sharply earlier this year (guidance-driven selloff, per TIKR commentary on a prior quarter's "weak earnings guidance"), then rebounded on the Q1 FY2027 beat-and-raise reported 2 Jun 2026 (revenue +23% YoY to $264.2M, non-GAAP EPS $0.23 vs $0.21 expected, FY2027 revenue guidance raised to $1,112–1,118M).

---

## 2. Data Gathered (Phase 01 Inputs) & Gaps Flagged

| Metric | Value | Source / Derivation |
|---|---|---|
| TTM Revenue (through Q4 FY2026, ended 31 Jan 2026) | **$955.2M** (+26% YoY) | GitLab FY2026 Q4/FY earnings release (3 Mar 2026), via WebSearch aggregation |
| TTM Net loss (GAAP) | **-$55.96M** (FY2026 GAAP net loss "$56.0M") | SimplyWall.st TTM rollup / GitLab FY2026 earnings release — consistent across sources |
| **TTM Net margin (GAAP)** | **≈ -5.86%** (-$55.96M / $955.22M) | Computed |
| Non-GAAP operating margin (FY2026) | 17% (+680bps YoY) | GitLab FY2026 earnings release |
| GAAP operating margin (FY2026) | (7)% | GitLab FY2026 earnings release |
| Q1 FY2027 (most recent quarter, ended 30 Apr 2026) | Revenue $264.2M (+23% YoY); GAAP operating margin (6)%; non-GAAP operating margin 14% (+200bps YoY); non-GAAP EPS $0.23 (beat $0.21 est.); adjusted FCF $147M, FCF margin 56% | GitLab Q1 FY2027 earnings release (2 Jun 2026) |
| **ROIC (TTM)** | **≈ -4.57%** (also reported as -1.78% by an alternate source; ROCE improved from -24.1% to -9.4% over 3 yrs per Alpha Spread) | GuruFocus / Alpha Spread — all sources agree ROIC/ROCE is negative |
| Revenue: FY2022 (ended 31 Jan 2022) | $252.653M | GitLab FY2023 8-K (prior-year comparative) |
| Revenue: FY2023 (ended 31 Jan 2023) | $424.3M (+68% YoY) | GitLab FY2023 8-K |
| Revenue: FY2024 (ended 31 Jan 2024) | $579.9M (+37% YoY) | GitLab FY2024 8-K |
| Revenue: FY2025 (ended 31 Jan 2025) | $759.2M (+31% YoY) | GitLab FY2025 8-K |
| Revenue: FY2026 (ended 31 Jan 2026) | $955.2M (+26% YoY) | GitLab FY2026 8-K (3 Mar 2026) |
| **Revenue CAGR 3yr** (FY2023→FY2026) | **≈ 31.1%** = (955.2/424.3)^(1/3) − 1 | Computed |
| Gross margin (FY2026, GAAP) | **87%** | GitLab FY2026 10-K (per StockTitan summary) |
| Gross margin (non-GAAP, recent quarters) | 89–90% (Q1 FY2026: 90%; Q4 FY2026: 89%) | GitLab quarterly earnings releases |
| FY2027 gross margin guidance | 85–87% (down from 89% non-GAAP in FY2026), attributed to SaaS/Dedicated/Duo Agent Platform mix shift | GitLab FY2026 Q4 earnings release / management commentary |
| OCF — FY2024 | $35.0M (positive) | GitLab FY2024 earnings release |
| Non-GAAP FCF — FY2024 | $33.4M (positive) | GitLab FY2024 earnings release |
| OCF — FY2025 | **-$64.0M** (negative, GAAP) | GitLab FY2025 Q4/FY earnings release |
| Non-GAAP adjusted FCF — FY2025 | $120.0M (positive) | GitLab FY2025 Q4/FY earnings release |
| OCF — FY2026 | $232.9M (positive) | GitLab FY2026 Q4/FY earnings release |
| Non-GAAP adjusted FCF — FY2026 | $219.6M (positive) | GitLab FY2026 Q4/FY earnings release |
| Net debt | **Net cash** — $1.26B net cash position (~$7.46/share); total debt $0 (debt-free for 5+ years) | SimplyWall.st / multiple sources consistent |
| Shares outstanding (diluted, weighted avg FY2026) | ~166.79M | AlphaQuery |
| Stock-based compensation (TTM, through Jan 2026) | $215.0M (+16% YoY; 3yr avg growth +21%/yr) | GuruFocus |
| Insider buying (CEO Bill Staples / CFO Jessica Ross) | **Not found** — no Form 4 insider-purchase activity located via WebSearch | Gap — see Data Gaps below |

### Data Gaps / Flags

1. **TTM figures use FY2026 annual (ended 31 Jan 2026) as the base**, not a rolling TTM through the most recent quarter (Q1 FY2027, ended 30 Apr 2026). A true TTM (Q2–Q4 FY2026 + Q1 FY2027) was not separately reconstructed because the FY2026 annual net margin (-5.86%) and the most recent quarter's GAAP operating margin (-6%) both point in the same direction and the gap to the >15% threshold (≈21 percentage points) is far too large for a one-quarter roll-forward to close. **Doesn't change the gate outcome.**
2. **ROIC**: sources show a range from -1.78% to -4.57%, all negative, with ROCE trend improving from -24.1% to -9.4% over 3 years (still deeply negative). No source shows ROIC anywhere close to the >15% threshold. **Doesn't change the gate outcome.**
3. **FCF/NI conversion ratio — explicitly not computed.** Per the task brief and Phase 01 methodology: GitLab's GAAP net income is negative (TTM -$55.96M / FY2026 -$56.0M) while FCF is positive (FY2026 OCF $232.9M, non-GAAP adjusted FCF $219.6M). Dividing a positive FCF figure by a negative NI figure produces a negative ratio that is **not meaningful** as a "conversion" percentage — it would read as a large negative number that superficially looks like a "failure" of the >70% test but actually reflects the opposite situation (cash generation outpacing a GAAP accounting loss driven heavily by non-cash stock-based compensation, $215M TTM). This is flagged explicitly rather than computed, consistent with the task instruction.
4. **FCF positive 3 consecutive years — mixed on a GAAP-OCF basis, but positive on a non-GAAP-adjusted-FCF basis.** GAAP operating cash flow: FY2024 +$35.0M, FY2025 **-$64.0M** (negative), FY2026 +$232.9M. Non-GAAP adjusted FCF: FY2024 +$33.4M, FY2025 +$120.0M, FY2026 +$219.6M — all three years positive on this basis. The framework's "3 consecutive years positive FCF" check is ambiguous as to which FCF definition applies; both readings are presented here rather than picking the more favorable one silently.
5. **Insider buying** (relevant only if the Turnaround Sub-Gate, Upgrade 4, is reached) — no CEO/CFO Form 4 purchase activity was found via WebSearch. This is treated as "not found / likely none" rather than confirmed zero, but doesn't change the Upgrade 4 outcome (see §4).
6. **Share issuance / dilution**: GitLab has not raised dilutive equity beyond routine SBC-driven share count growth (166.79M diluted weighted-avg shares for FY2026, growing via SBC of $215M TTM, +16% YoY). The $400M share buyback authorization announced with FY2026 results (3 Mar 2026) is a partial offset. SBC-driven share count growth is a quality concern (diluting per-share economics even while OCF/FCF improve) but is not "dilutive equity issuance" in the sense of a secondary offering.

---

## 3. Phase 01 — Quality Gate

| Check | GTLB Value | Threshold | Result |
|---|---|---|---|
| **Net margin (TTM/FY2026)** | **≈ -5.86%** | >15% (strategy.md) / >12% (valuation-scoring.md pre-screen) | ❌ **FAIL** |
| **ROIC** | **≈ -4.57%** (range -1.78% to -4.57%, all negative) | >15% | ❌ **FAIL** |
| Revenue CAGR 3yr (FY2023→FY2026) | **≈ 31.1%** | >10% (strategy.md) / >8% (pre-screen) | ✅ **PASS — strongly** |
| Gross margin (FY2026, GAAP) | 87% (non-GAAP 89–90%) | >40% or expanding | ✅ PASS |
| FCF positive 3 consecutive years | Non-GAAP adjusted FCF: FY2024 +$33.4M, FY2025 +$120.0M, FY2026 +$219.6M — all positive and growing. GAAP OCF: FY2025 was **negative** (-$64.0M) | required | ⚠️ **Mixed** — pass on non-GAAP adjusted FCF basis, fail on strict GAAP-OCF basis for FY2025 |
| Net debt/EBITDA | Net cash position (~$1.26B net cash, $0 debt) — ratio not meaningful with negative/near-zero EBITDA and no debt | <2x | ✅ PASS (no debt to service) |
| FCF/NI conversion ratio | **Not computed — not meaningful** (NI negative, FCF positive; see Data Gap #3) | >70% for 2+ years | ⚠️ **N/A — flagged, not a pass/fail input** |
| Share issuance pattern | Non-dilutive equity issuance, but share count growing via SBC ($215M TTM, +16% YoY); $400M buyback authorization partially offsets | not dilutive | ⚠️ Mixed — SBC-driven share growth is a quality concern, no secondary offering |
| Moat signal | Leading independent DevSecOps "single application" platform (source code mgmt, CI/CD, security scanning); 118% net retention rate (FY2026); $1.1B total RPO (+20% YoY), cRPO $719.4M (+24% YoY); recently crossed $1B ARR | required | ✅ Qualitatively strong — durable enterprise relationships, expanding wallet share |

---

## 4. Gate Result: **FAIL** — Stopping Per Operating Brief

> "Walk the Phase 01 quality gate — if it fails, stop and report why rather than proceeding to scoring."

GTLB **fails Phase 01 decisively on Net Margin (TTM ≈ -5.86% vs >15% required) and ROIC (≈ -4.57% vs >15% required)** — both metrics are not just below threshold but **negative**, a ~21-percentage-point gap on net margin alone. Per the operating brief, this session **does not proceed** to the Rate Environment Gate, Phase 02 valuation score, or the fair-value/order-setup workup (Step 4 of `/new-position`).

Unlike CIEN (the 11 Jun 2026 session, where TTM figures were thin-but-positive and "close" to the threshold), GTLB's GAAP profitability gap to the Phase 01 bar is large and has been the company's persistent state since IPO — this is a structural characteristic of GitLab's current business model (heavy reinvestment in growth + large stock-based compensation expense), not a borderline or cyclical miss.

### Did the Turnaround Sub-Gate (Upgrade 4) open an alternate path?

No — it requires **all five** of:

1. **Historical ROIC >15% for ≥5 years in the past decade** — ❌ **FAILS immediately.** GitLab IPO'd in October 2021 and has never reported a GAAP-profitable year; ROIC/ROCE has been negative throughout its history as a public company (ROCE -24.1% → -9.4% over the last 3 years, still deeply negative). GitLab is simply too young as a public company, and has never crossed this bar even once, let alone for 5 of the past 10 years.
2. **CEO/CFO insider buying >$500K in past 6 months (Form 4-verified)** — ❌ **Not found.** No evidence of insider buying located via WebSearch (Data Gap #5).
3. **Independent FV estimate showing ≥40% MOS** — not built (gate fails before this step is reached; also moot given #1 and #2 already fail).
4. **Net Debt/EBITDA <3×** — ✅ would pass trivially (net cash position, $0 debt).
5. **Core moat still identifiable** — ✅ yes (118% net retention, $1.1B RPO, leading independent DevSecOps platform).

Since condition 1 fails outright (and condition 2 is unverified/likely absent), "all five" cannot be satisfied — **the Turnaround Sub-Gate path does not open**, regardless of how the other three conditions resolve.

---

## 5. Qualitative Discussion — Is This a Good Business That Simply Isn't GAAP-Profitable Yet?

**Short answer: plausibly yes, but the framework's gate is deliberately built on trailing financial proof, not narrative — and on that basis, GTLB isn't there yet.**

**The bull case for the underlying business is real:**
- Revenue CAGR ~31% (3yr) is among the strongest of any name evaluated under this framework — a genuine Fast Grower by the >15% EPS-growth-equivalent definition (note: EPS isn't meaningful here since EPS is negative, but revenue growth of this magnitude at this scale is rare).
- Non-GAAP operating margin improved +680bps YoY to 17% in FY2026, and +200bps YoY to 14% in Q1 FY2027 — a clear, multi-quarter trend of operating leverage emerging as the business scales.
- Adjusted FCF has grown from $33.4M (FY2024) → $120.0M (FY2025) → $219.6M (FY2026), with Q1 FY2027 alone delivering $147M (56% FCF margin) — cash generation is real and accelerating.
- 118% net retention rate and $1.1B total RPO (+20% YoY) indicate a durable, expanding enterprise customer base — moat signals (switching costs around an integrated DevSecOps platform, network effects within engineering organizations) are qualitatively strong.
- Balance sheet is pristine: $1.26B net cash, zero debt.

**Why this still fails the gate, and why that's arguably correct for this framework:**
- The >15% net margin and >15% ROIC thresholds exist to filter for businesses that have **already proven** they can convert revenue into owner profits at scale — not businesses that are *plausibly on a path* to doing so. GitLab's GAAP net margin is not "thin" (like CIEN's 7.9%) — it is **negative**, and has been negative every year since IPO. The gap to threshold (~21pp on net margin) is roughly **3x the size** of CIEN's gap (~7pp), which itself failed.
- A large share of the "improving profitability" narrative is a **non-GAAP** story (non-GAAP operating margin, adjusted FCF) that excludes a genuinely large and growing expense: $215M TTM stock-based compensation (+16% YoY, 21%/yr 3yr avg growth) on $955M revenue — SBC alone is ~22.5% of revenue. This is real economic dilution to existing shareholders even though it doesn't appear in OCF. The framework's >15% GAAP net margin gate is, in effect, designed to not be fooled by exactly this kind of non-GAAP-vs-GAAP gap.
- FY2025's GAAP operating cash flow was actually **negative** (-$64.0M) — even the "FCF positive 3 consecutive years" check is not a clean pass on a strict GAAP basis, only on a non-GAAP-adjusted basis (Data Gap #4).

**This is a case where "good business, not yet good enough for this framework's bar" is the honest read** — similar in spirit to ADBE's "good business, market mispricing it" finding from earlier today, but the opposite direction: here the business itself, not the market's perception of it, is the gating factor.

---

## 6. Recommendation

# **PASS — do not open a position now. Add to watchlist with explicit re-check conditions.**

GTLB fails the Phase 01 quality gate decisively on **GAAP Net Margin (TTM ≈ -5.86% vs >15% required)** and **ROIC (≈ -4.57% vs >15% required)** — both metrics are negative, not merely below threshold. The Turnaround Sub-Gate (Upgrade 4) does not open an alternate path because GitLab has never demonstrated a >15% ROIC year as a public company (failing condition 1 outright) and no insider-buying evidence was found (condition 2).

This is **not** a comment on the quality of GitLab's underlying business — revenue growth (~31% 3yr CAGR), net retention (118%), RPO growth (+20% YoY), and the FCF trajectory ($33M → $120M → $220M over 3 years) all point to a business executing well on its growth strategy with improving (non-GAAP) operating leverage. But the framework's Phase 01 gate is intentionally a **trailing GAAP-financials filter**, and on that basis GTLB is not yet a "quality" name by this framework's definition — the gap is large (~21pp on net margin) and has persisted since IPO, making it a structural characteristic rather than a near-term inflection.

**Add GTLB to the watchlist** with re-evaluation triggers at:
- **Next earnings release** (Q2 FY2027, expected ~early September 2026) — re-run Phase 01 with updated TTM net margin and ROIC. Given the size of the current gap (~21pp), a single quarter is very unlikely to close it, but the *trend* (non-GAAP operating margin +680bps YoY in FY2026, +200bps YoY in Q1 FY2027) is worth tracking for the pace of GAAP convergence.
- **Any quarter where GAAP net income turns positive** — this would be the clearest signal that the non-GAAP-to-GAAP gap (driven primarily by SBC) is closing structurally, not just via non-GAAP add-backs.
- **Any material SBC policy change** (e.g., a shift toward cash compensation, reducing the ~22.5%-of-revenue SBC load) — a Rule 9-style fundamental event that would directly affect the net-margin gate.
- **CEO/CFO insider buying** — if Form 4 filings show meaningful insider purchases, re-check the Turnaround Sub-Gate (Upgrade 4) conditions, though condition 1 (historical ROIC track record) would still need to resolve over time.

---

## 7. Next Review Trigger

**Date/event:** GTLB's Q2 FY2027 earnings release (expected ~early September 2026) — re-run Phase 01 with refreshed TTM Net Margin and ROIC, and check whether the non-GAAP operating margin improvement trend (+680bps FY2026, +200bps Q1 FY2027) is translating into a narrowing GAAP gap. Earlier trigger if GAAP net income turns positive in any quarter, or if a Rule 9 fundamental event (SBC policy change, M&A, management change, >15% unexplained move) occurs.

**No position opened — nothing to log in `decisions/`.**
