# NEW POSITION — Motorola Solutions (MSI)

**Task:** NEW POSITION
**Date:** 2026-08-23
**Trigger:** Automated Telegram scan (Routine 6) — first-ever mention of MSI in a monitored channel, reporting that Trump reportedly sold MSI shares in June. This is a third-party political-trading disclosure, **not financial data**, and carries no scored weight in this evaluation — it only surfaced the ticker for a mandatory first-ever `/new-position` evaluation, since no watchlist entry existed for MSI anywhere in the repo prior to this session (confirmed by directly listing both `watchlist/in-portfolio/` and `watchlist/not-in-portfolio/` — no folder-naming mismatch, unlike the earlier BRK.B case today).

---

## 1. Live Price (Rule 0)

Fetched via IBKR `search_contracts` → `get_price_snapshot` (never inferred from multiples):

- **Contract:** NYSE, MOTOROLA SOLUTIONS INC, contract_id 81581011 (STK)
- **Last price: $480.47** (+$6.84 / +1.44% vs. prior close $473.63), not halted, live tick
- 52-week range (IBKR `misc_statistics`): $358.40 – $491.88
- Dividend yield (IBKR): 0.98%
- Cross-checked against stockanalysis.com's independently-quoted $480.47 — matches exactly.

---

## 2. Data Gaps Flagged

Per "never invent or estimate financial data," the following Moat Signal inputs were searched for but **could not be confirmed with a specific, credible, cited figure**, and are scored FALSE below rather than assumed true from general reputation:

- **Quantified market share:** MSI's own FY2025 10-K describes it only as "a global leader in the two-way radio category" with **no cited percentage**. A third-party aggregator (MarketsAndMarkets, via web search) returned a "3% market share" figure that is inconsistent with MSI's well-known leadership position and looks like a global-fragmented-market artifact, not a reliable public-safety-segment figure — rejected as not credible rather than used at face value.
- **Documented price-increase-without-volume-loss evidence** (brand premium test): no specific price-increase event found in earnings materials or press coverage.
- **Cost-per-unit vs. smaller competitors** (scale cost advantage test): no comparative unit-cost data found.

These gaps affect only the Moat Signal sub-score (see §3.6) — they do **not** block the gate determination. A sensitivity check (§3.8) shows the Quality Score fails the 80.0+ gate even under the most generous possible reading of all three unconfirmed signals, so the session proceeds to a definitive result rather than stopping on the gap.

---

## 3. Phase 01 — Quality Score (2026-06-29 methodology)

### 3.1 Hard disqualifier check — none fire

| Disqualifier | MSI status | Fires? |
|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | TTM ~126%, FY2025 119%, FY2024 135%, FY2023 105%, FY2022 115%, FY2021 128% — all years comfortably >100% | No |
| Net debt/EBITDA over threshold (2.5× standard) | 2.37× (current/TTM, stockanalysis.com) | No — under 2.5× |
| Not FCF-positive for 3+ consecutive years | FCF positive every year FY2021–FY2025 ($1,594M / $1,567M / $1,791M / $2,134M / $2,572M) | No |

No hard disqualifier fires. MSI's fate is decided by the weighted score below.

### 3.2 Inputs (sourced — TTM/current unless noted; source: stockanalysis.com "Current"/TTM column, period ending Q2 2026 / Aug 21 2026, cross-checked against SEC 10-K FY2025 and Q2 2026 earnings release)

| Metric | Value | Source |
|---|---|---|
| Net Margin (TTM) | 17.44% | stockanalysis.com financials (TTM, period ending Jul 4 2026) |
| ROIC (TTM/current) | 21.70% | stockanalysis.com ratios ("Current," Aug 21 2026) |
| Gross Margin (TTM) | 52.11% | stockanalysis.com financials (TTM) |
| Gross Margin 3yr trend | 49.88% (FY23) → 51.07% (FY24) → 51.80% (FY25) | stockanalysis.com financials (annual) |
| Revenue 3yr CAGR | 8.64% ($9,112M FY22 → $11,682M FY25) | stockanalysis.com financials (annual) |
| Net Debt/EBITDA | 2.37× | stockanalysis.com ratios ("Current") |
| FCF/NI ratio (TTM & multi-year) | ~126% TTM; 119%/135%/105%/115%/128% FY25–FY21 | stockanalysis.com cash-flow statement + ratios |
| FCF positive years | 5 of 5 (FY2021–FY2025) | stockanalysis.com cash-flow statement |

### 3.3 Profitability (25% weight)

```
NetMargin_Component = clamp((17.44/30)×100) = 58.13
ROIC_Component       = clamp((21.70/30)×100) = 72.33
Profitability_Score  = (58.13 + 72.33) / 2 = 65.23   (no FCF-positivity cap — 5/5 years positive)
```

### 3.4 Margins (15% weight)

```
GrossMargin_Score = clamp((52.11/80)×100) = 65.14
```
No structural-trend bonus: the +10 bonus only applies when gross margin is *below* 40% but expanding (quality-scoring.md). MSI's 52.11% is already well above 40%, so it doesn't qualify for that bonus (the 3yr uptrend is real — 49.88%→51.80% — but the rule as written gates the bonus on being below the 40% threshold).

**Margins_Score = 65.14**

### 3.5 Growth (20% weight)

```
Growth_Score = clamp((8.64/25)×100) = 34.58
```

**TAM/pricing-power modifier — documented evidence, +10 applied:**
- Completed $1.5B acquisition of D-Fend Solutions (counter-drone technology) — closed Aug 19 2026, a genuine adjacent-market entry (Source: Motorola Solutions press release / news coverage).
- Q2 2026 backlog hit a **record $15.6B**, +11% YoY (Software & Services backlog $11.8B, Products & Systems Integration $3.8B) — Source: Q2 2026 earnings press release / TradingView news summary.
- Full-year 2026 guidance raised to ~$12.98B revenue (~11% YoY vs. FY2025's $11.68B) and EPS $17.62–$17.72, explicitly citing "record backlog and safety-tech demand" (Source: company guidance, BigGo Finance summary).

**No structural-deceleration penalty applied**, despite the FY2021→FY2025 annual growth rate trend genuinely slowing (11.52%→9.50%→8.41%→8.00%): Q2 2026 actual revenue grew **+13% YoY** and full-year guidance was just *raised*, not cut — the most recent, most reliable evidence points to reacceleration (driven by AI/software suite expansion and the D-Fend deal), not structural deceleration. Applying the −10 penalty against the freshest data would contradict the framework's own "never invent or estimate" spirit by ignoring the latest reported quarter in favor of an older multi-year slope.

```
Growth_Score = 34.58 + 10 = 44.58
```

### 3.6 Balance Sheet (15% weight)

Standard company — not a payment network, exchange, or 100%-financial-debt asset-light business, so the standard /4 denominator applies (no Upgrade 5 override).

```
BalanceSheet_Score = clamp(100 × (1 − 2.37/4)) = 100 × (1 − 0.5925) = 40.75
```

### 3.7 Moat Signal (15% weight)

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **FALSE** | No credible, cited quantified share figure found (see §2 data gap) |
| Brand premium | **FALSE** | No documented price-increase-without-volume-loss evidence found |
| Network effect | **FALSE** | No documented network-effect mechanism for LMR/two-way-radio hardware or public-safety software found |
| Switching costs | **TRUE** | FY2025 10-K: customers' public-safety radio systems "often have multi-year or multi-decade lifespans" — deep infrastructure/interoperability lock-in; corroborated by record $15.6B Q2 2026 backlog (+11% YoY), $11.8B of which is Software & Services (recurring, contract-locked) — Sources: SEC 10-K FY2025, Q2 2026 earnings release |
| Scale cost advantage | **FALSE** | No comparative cost-per-unit data found |

```
Moat_Score = (1/5) × 100 = 20.0
```

### 3.8 FCF Quality (10% weight)

```
FCFQuality_Score = clamp(((1.26 − 0.40)/0.60)×100, 0, 100) = 100.0   (ratio ≥100% clamps to the ceiling)
```

### 3.9 Final Quality Score

```
Quality Score = (65.23×0.25) + (65.14×0.15) + (44.58×0.20) + (40.75×0.15) + (20.0×0.15) + (100.0×0.10)
              = 16.3075 + 9.7710 + 8.9152 + 6.1125 + 3.0000 + 10.0000
              = 54.107 → rounds to 54.1
```

**Quality Score = 54.1 / 100.0 — fails the 80.0+ gate by a wide margin.**

### 3.10 Sensitivity check — is this conclusion robust to the flagged data gaps?

The three unconfirmed Moat signals (§2) are the most judgment-dependent inputs in this session. Re-running with the maximally generous assumption — **all 5 Moat signals TRUE** (Moat_Score = 100.0) instead of 1/5:

```
Quality Score(best case) = 16.3075 + 9.7710 + 8.9152 + 6.1125 + 15.0000 + 10.0000 = 66.11
```

Even under that maximally generous reading, MSI tops out at **66.1 — still well short of 80.0.** The gate failure is driven primarily by Balance Sheet (40.75, Net Debt/EBITDA 2.37×) and Growth (44.58, 8.64% 3yr CAGR) rather than by the Moat uncertainty, so the conclusion below does not hinge on the unresolved data gaps.

**No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order setup is computed this session** — per quality-scoring.md, a company must clear 80.0+ before proceeding to any of that, "regardless of how cheap the stock looks."

---

## 4. Recommendation

# **PASS — Quality Score gate FAILS (54.1, or at most 66.1 under the most generous possible reading of unconfirmed Moat evidence; both well below the 80.0+ threshold). Do not proceed to valuation scoring. No position, no watchlist-only tracking beyond the standard not-in-portfolio pointer below — this ticker does not clear the framework's first screening gate.**

MSI is a genuinely solid, profitable, cash-generative business (double-digit ROIC, FCF comfortably exceeding net income every year, a real and growing backlog, credible recent reacceleration via AI/software and the D-Fend counter-drone acquisition). But under this framework's strict, June-2026-introduced 80.0+ continuous Quality Score bar, it falls well short — driven mainly by moderate balance-sheet leverage (2.37× net debt/EBITDA, scoring only 40.75/100 on a 0-at-4× scale), a 3-year revenue CAGR (8.64%) that clears the old binary Phase 01 threshold (>8%) but scores weakly on the continuous 0–25% growth scale, and — independent of any judgment call — a Moat Signal score capped by the framework's insistence on cited, quantified evidence rather than reputational assumption.

This is the expected, by-design behavior of a deliberately strict gate (quality-scoring.md: *"if it screens out too many otherwise-reasonable candidates, lower the threshold... and record why"* — this session doesn't recommend that; MSI simply isn't a >80.0 name under the framework as currently calibrated).

The triggering Telegram post (a third-party disclosure about a since-June-sold position) added no fundamental information and is not the basis for this outcome — the Quality Score gate result is independent of, and far more decisive than, that post's content.

**Next review trigger:** Standard Rule 9 events (quarterly earnings, guidance revision, M&A, management change, macro shift) or a >15% unexplained price move — any of which would warrant a fresh `/new-position` (or, if the framework's quality methodology version changes, an automatic stale-score reflag). No calendar-based re-check scheduled otherwise, consistent with how other Quality-Gate-fail names are tracked in this framework.

---

## 5. Glossary

- **CAGR**: Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT**: Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EV/EBIT, EV/EBITDA**: Enterprise Value divided by EBIT or EBITDA — multiples used to compare how expensive companies are relative to their operating profit, independent of capital structure. (Referenced in inputs gathered but not scored, since Phase 02 was never reached.)
- **FCF Yield**: Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **Hard disqualifier**: A Quality Score condition that fails a company regardless of its weighted score. None fired for MSI this session (see §3.1) — the failure here is on the weighted score alone.
- **LMR (Land Mobile Radio)**: A category of two-way radio communication systems used by public-safety agencies (police, fire, EMS) and enterprises for mission-critical voice/data communication, typically requiring dedicated licensed spectrum and dedicated infrastructure rather than commercial cellular networks. Motorola Solutions describes itself as "a global leader in the two-way radio category" spanning the P25, TETRA, and DMR standards (Source: FY2025 10-K), cited as this framework's context for the (unconfirmed) market-share Moat Signal and the (confirmed) switching-costs signal in this framework's 2026-08-23 MSI session. *(New term.)*
- **Moat Signal**: This framework's 5-point Quality Score checklist that turns the general "Moat" concept into a scored input: market share stable/growing, brand premium, network effect, switching costs, and scale cost advantage, each markable TRUE only against a cited source — `Moat_Score = (count of TRUE signals ÷ 5) × 100`. MSI scored 1/5 (20.0) this session, with two of the false signals flagged as genuine data gaps rather than confirmed absent.
- **Net Debt/EBITDA**: Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **Net Margin**: Net Income ÷ Revenue — the percentage of each revenue dollar left as accounting profit after every expense, interest, and tax.
- **Quality Score**: This framework's 0.0–100.0 continuous score (0.0 = lowest quality, 100.0 = highest) grading the Phase 01 criteria instead of treating them as simple pass/fail. A company must score 80.0+ to proceed to Phase 02 valuation scoring at all. MSI scored 54.1 this session — fails the gate.
- **ROIC**: Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **TAM**: Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **TTM**: Trailing Twelve Months — the most recent four reported quarters combined, used instead of a single fiscal-year snapshot to reflect the most current run-rate.
