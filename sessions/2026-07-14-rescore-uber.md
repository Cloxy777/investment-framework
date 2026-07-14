# RESCORE — UBER (Uber Technologies, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Trigger:** Routine 6 (Telegram Stock-Mention Scan, hourly) — [t.me/tarasguk](https://t.me/tarasguk) post `tarasguk/11385` (~2026-07-14T18:28:28Z, edited), naming $UBER, $LCID, and NVIDIA tech. Per CLAUDE.md Rule 0, the post's text is a **trigger only** — nothing in it was used as a scored input; every figure below was pulled independently (IBKR live price, SEC-derived TTM figures carried forward from the 2026-07-05 session where unchanged, WebSearch/company statements for the news claims).
**Date:** 2026-07-14
**10Y US Treasury Yield:** ~4.62% (day range 4.57–4.62%, open 4.61% — TradingEconomics/CNBC-sourced WebSearch snapshot for 2026-07-14; FRED `DGS10`'s own series lags to 2026-07-10 = 4.56%, consistent with the same upward move, attributed in market commentary to Middle East-tension-driven oil/inflation concerns). Same 3.5–5% bracket as the 2026-07-05 session's 4.49% figure — **no Rate Regime bracket change.**
**Rate Regime Modifier (Step 2):** +5 (unchanged)
**Last review on record:** UBER **41.6** (Valuation) / **61.0** (Quality) / **40.3** (Composite, reference-only) — 2026-07-05, [sessions/2026-07-05-rescore-uber.md](2026-07-05-rescore-uber.md). Action: HOLD existing, no add (blocked by sub-2:1 R/R and by the Quality Score's 80.0+ gate failure).
**Current UBER portfolio weight:** 0.38% per [holdings.md](../portfolio/holdings.md) — nowhere near the 15% hard cap (Upgrade 7).

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$72.10** | IBKR `get_price_snapshot` (contract_id 365207014, NYSE), `last` field, `is_close: false` (genuinely live, not a stale prior-session close). |
| Cross-check | $72.10 (exact match) | stockanalysis.com "Current Stock Price," fetched live this session — corroborates the IBKR figure to the cent. |
| Mark price (`plprice`) | $72.32 | IBKR `get_price_snapshot` — consistent with `last`. |
| Prior close | $74.26 | IBKR `get_price_snapshot` `prior_close`. |
| 1-day change | −$2.16 (−2.91%) | IBKR `get_price_snapshot` `change`. Independently corroborated: TradingKey reported UBER "moved down by 3.56% on Jul 14" (a slightly different intraday-vs-close window, same direction/magnitude). |
| 52-week range | $67.21 – $101.98 | IBKR `misc_statistics` (unchanged from 07-05). |
| Year-to-date change | −11.76% (−$9.61) | IBKR `year_to_date_change`. |
| Analyst consensus PT | mean **$104.41**, range $70–$150, 49 analysts, "Strong Buy" | stockanalysis.com — bull-case sanity check only (Rule 0 Step 4), not a scored input. Materially unchanged from 07-05's $104.48/53-analyst figure. |
| Price vs. 07-05 review ($74.43) | **−3.13%** | Well under the 15% Rule 9 threshold — not, on its own, a Rule 9 price-move trigger. |

---

## 2. Independent Verification of the Telegram Post's Claims

Per Rule 0/CLAUDE.md, the Telegram post itself was never used as a data input — both of its claims were independently checked via WebSearch/company sources before anything was accepted as real:

**Claim 1 — "Uber showed off its luxury robotaxi made with Lucid using Nvidia technology."** ✅ **Real, but not new — no fresh Rule 9 trigger.** The Lucid/Nuro/Uber robotaxi partnership is genuine: originally announced July 2025 (Uber to deploy Lucid Gravity SUVs as robotaxis, since expanded from 20,000 to 35,000+ vehicles), the production-intent vehicle and Uber-designed cabin were unveiled at **CES 2026 in January**, and the vehicle's compute stack does run on **NVIDIA DRIVE AGX Thor**. A Houston 2027 launch was also announced back in June 2026. Nothing about this partnership is new as of 2026-07-14 — the post (edited, per the trigger metadata) appears to have recirculated older robotaxi imagery/facts in the same breath as the fresh Lucid news below, not reported a new Uber disclosure. **Independent finding:** Uber does hold a direct financial stake tied to this partnership — a cumulative **$500M investment in Lucid** ($300M Sept 2025 + $200M expansion, April 2026), for an **11.5% equity stake** in Lucid Group (Reuters/TechCrunch/Electrek reporting, cross-checked across multiple outlets) — confirming the Telegram post's "$500M from Uber" figure as accurate, even though the post's framing implies that investment already failed.

**Claim 2 — "Lucid denied bankruptcy rumors; $500M from Uber didn't save Lucid; the company is considering filing for bankruptcy."** ⚠️ **Partially accurate, materially overstated.** On 2026-07-14, an EV-industry blog report (citing anonymous sources) claimed Lucid was weighing a Chapter 11 filing or going private on restructuring-firm AlixPartners' advice; LCID shares fell as much as ~40–50% intraday (its largest-ever single-day drop) before partially recovering. **Lucid's own chief communications officer told TechCrunch the same day the rumors are "completely false,"** stating the company "has sufficient liquidity to carry its operations well into next year" per its own most recent quarterly filings, and that AlixPartners' mandate is limited to operational improvement, "nothing else," with no bankruptcy recommendation made to management or the board. Corroborated by Bloomberg, CNBC, and Electrek. **So: Lucid has not filed for bankruptcy, disputes the rumor on the record, and states it isn't imminent — the Telegram post's "did not save Lucid" framing pre-judges an outcome that, as of this session, hasn't happened.** Genuine facts independently confirmed: Lucid's Q2 2026 deliveries were weak (3,953 vehicles, barely above Q2 2025), it recently announced layoffs and cut a production shift at its Arizona plant — real operating distress, but distinct from an actual bankruptcy filing.

**Net assessment for UBER specifically:** this is a real, dated (2026-07-14), material development concerning a minority equity stake and robotaxi-fleet partner of Uber's — legitimate grounds to run this rescore, consistent with the watchlist's own "AV-partner monetization update" trigger category. But it does **not** amount to a hard Rule 9 trigger (no Uber earnings, guidance, M&A, management change, macro-bracket shift, or >15% unexplained UBER move occurred) and, critically, **produces no new Uber-reported financial figure to plug into any sub-score** — Uber's own equity-method mark-to-market impact of a potential LCID value decline would only show up in Uber's **Q3 2026** results (not yet reported; Q2 2026 earnings, covering the period through June, are still ~3 weeks out). Inventing an estimate of that future impact would violate "never invent or estimate financial data." **Flagged below as a qualitative bear-case risk note and a watch item for the Q2/Q3 2026 earnings review — not as a change to any quantitative sub-score this session.**

---

## 3. Rule 9 Trigger Check (2026-07-05 → 2026-07-14)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No | Q2 2026 not due until early August 2026 (per the 07-05 review's own "next review trigger"). |
| Guidance revision | No | No new guidance issued since the 6 May 2026 Q1 print. |
| M&A / material investment (Uber's own) | No new Uber-side action | The Lucid stake itself (§2) predates this window (last expanded April 2026); no new Uber capital commitment found dated between 07-05 and 07-14. |
| Management change | No | None found for Uber. |
| Macro shift | Marginal, no bracket change | 10Y ticked from 4.49% (07-05) to ~4.62% (07-14) — still inside the 3.5–5% bracket. |
| >15% unexplained price move | No | −3.13% since 07-05 — modest, and not unexplained (broad market/AI-adjacent softness around the Lucid news cycle is a plausible, if imprecise, contributor). |

**Conclusion: no hard Rule 9 trigger fired.** This remains a routine, trigger-prompted refresh — the live price, the 10Y yield, and the qualitative AV-partner risk note (§2) are updated; every fundamental figure that depends on Uber's own **unreported** Q2 2026 results (revenue, EBIT, FCF, margins, balance sheet, moat evidence) is **carried forward unchanged from the 2026-07-05 session**, since no newer Uber-filed data exists yet to replace it.

---

## 4. Data Gaps / Flags

1. **`yfinance` unreachable this session** — same recurring `curl_cffi`/TLS-impersonation failure pattern documented across many prior sessions (most recently the 07-05 UBER session itself). Used IBKR (live price) + stockanalysis.com (forward EPS consensus, cross-checked price) + WebSearch/WebFetch as the Rule-0-compliant fallback, consistent with the 07-05 session's own contingency.
2. **All TTM fundamentals (revenue, EBIT, FCF, net debt, shares outstanding, margins, ROIC, moat evidence) are carried forward from the 2026-07-05 SEC-EDGAR-sourced session, unchanged** — Uber's next 10-Q (covering Q2 2026) has not yet been filed, so there is no fresher SEC data to pull. Only the **live price**, the **10Y yield**, and the resulting price-dependent figures (Market Cap, EV, FCF Yield, EV/EBIT, Forward PE, Rate Gate, Upside/Downside Modifier) are recomputed this session.
3. **Lucid's financial-distress risk to Uber's AV-partner-monetization growth story is a qualitative flag only, not a quantified score input this session** (§2) — no Uber-reported dollar figure exists yet to normalize into any sub-score without inventing one. Explicitly flagged as a Q2/Q3 2026 earnings watch item (§8).
4. Every other 07-05 data gap (dated March-2024 market-share citation, no-history Forward-PE fallback, PEG non-eligibility) still applies unchanged — see that session for full detail; not re-derived here to avoid redundant recomputation of unchanged inputs.

---

## 5. UBER — Quality Score (carried forward, unchanged)

No new Uber-reported financial data exists since the 2026-07-05 session's first-ever Quality Score computation. Per rescore.md, quality is recomputed only when new fundamental data would move it — none does this session (no new 10-Q/10-K/8-K). Carrying forward in full for the record:

```
Profitability_Score (normalized) = 33.95   (25% weight)
GrossMargin_Score                = 51.29   (15% weight)
Growth_Score (with +10 TAM bonus)= 80.92   (20% weight)
BalanceSheet_Score               = 84.19   (15% weight)
Moat_Score (2/5 signals TRUE)    = 40.0    (15% weight)
FCFQuality_Score                 = 100.0   (10% weight)

Quality Score = 33.95×0.25 + 51.29×0.15 + 80.92×0.20 + 84.19×0.15 + 40.0×0.15 + 100.0×0.10
              = 8.4875 + 7.6935 + 16.184 + 12.6285 + 6.000 + 10.000 = 60.9935 → 61.0
```

# Quality Score = 61.0 — still FAILS the 80.0+ gate, decisively (unchanged from 07-05).

Hard disqualifier checks (FCF/NI <70% 2+ yrs, Net Debt/EBITDA over threshold, FCF-positive 3+ yrs) all still PASS, per the same 07-05 figures — none of these depend on a newer 10-Q that doesn't yet exist.

**Qualitative note (not a score change):** Lucid's disclosed financial distress (§2) is a real risk to the Growth sub-score's forward-looking AV-partner-monetization narrative and to the Moat checklist's underlying "network effect"/platform thesis (Uber aggregates *many* AV partners — Waymo, WeRide, Nuro, Rivian, Volkswagen/MOIA, and Lucid — so a single partner's distress doesn't structurally break the aggregator model, but it is one data point worth tracking into Q2/Q3 2026 reporting). No number changed as a result.

---

## 6. UBER — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = Live Price ÷ Forward EPS consensus = $72.10 ÷ $3.33 = 21.652×
EY         = 1 ÷ 21.652 = 4.6184%
Spread     = EY − 10Y Treasury = 4.6184% − 4.62% = −0.0016pp
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (essentially at par with the 10Y, ~1.50pp short of passing) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y ≈ 4.62% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for UBER = +10** (unchanged from 07-05)

---

## 7. UBER — Phase 02 Valuation Score

Fundamentals (revenue, EBIT, net debt, FCF) carried forward unchanged from the SEC-sourced 2026-07-05 TTM window (Q2'25–Q1'26) — only price-dependent figures recomputed with today's live price.

**Market Cap / EV (recomputed)**
```
Shares outstanding (unchanged, 10-Q filed 2026-05-06, no newer filing) = 2,035,599,013
Market Cap = 2,035,599,013 × $72.10 = $146,766.69M
Net Debt (unchanged, 2026-03-31)    = $4,423M
EV = $146,766.69M + $4,423M = $151,189.69M
```

**FCF Yield — 40% weight**
```
TTM FCF (unchanged) = $9,799M
FCF Yield = $9,799M ÷ $146,766.69M = 6.677%
FCF_Score = clamp(100 × (1 − 6.677/10), 0, 100) = 33.23
```
→ Contribution: 33.23 × 0.40 = **13.29**

**EV/EBIT — 25% + 15% (PEG redistributed) = 40% weight**
```
TTM EBIT (unchanged) = $6,260M
EV/EBIT = $151,189.69M ÷ $6,260M = 24.152×
EV/EBIT_Score = clamp((24.152 − 12)/23 × 100, 0, 100) = 52.83
```
→ Contribution: 52.83 × 0.40 = **21.13**

**Forward PE — no-history fallback (unchanged rationale) — 20% weight**
```
FwdPE_Score = 50.0  (neutral midpoint, flagged — same no-history fallback as 07-05:
   Uber's GAAP-loss-making history through FY2022 still makes a 5yr PE range/average
   not meaningful; Forward PE itself is shown above (21.65×, matching stockanalysis.com's
   displayed 21.67× to within rounding) purely for the Rate Gate's EY calculation)
```
→ Contribution: 50.0 × 0.20 = **10.0**

**PEG — 15% weight: still N/A** (redistributed to EV/EBIT above, same non-eligibility as 07-05).

**Raw weighted score:**
```
= 13.29 + 21.13 + 10.0 = 44.42
```
**+ Rate Modifier (+10) = 54.42** (before the Upside/Downside Modifier)

---

## 8. UBER — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture (carried forward from 07-05 — same P/FCF approach, unchanged inputs since no new Uber fundamental data exists):**

| Scenario | Weight | FY2026 FCF | Shares | FCF/share | Exit P/FCF | Fair Value |
|---|---|---|---|---|---|---|
| Bull | 25% | $11.5B | 2.036B | $5.65 | 24× | **$135.60** |
| Base | 50% | $11.02B | 2.036B | $5.41 | 18× | **$97.40** |
| Bear | 25% | $9.5B | 2.036B | $4.67 | 12× | **$56.00** |

```
PW Fair Value = 0.25×135.60 + 0.50×97.40 + 0.25×56.00 = $96.60   (unchanged from 07-05)
```
Sits below today's $104.41 analyst consensus mean PT (Guardrail 2). **Qualitative note (§5):** Lucid's disclosed distress adds further supporting evidence to the Bear scenario's already-cited "AV-disruption risk" line, without changing its $56.00 figure — no new Uber-disclosed dollar impact exists yet to justify moving it (avoiding an invented number per Rule 0/Rule 6).

**Step 1 — Expected annual return E (recomputed with today's live price):**
```
Gap Upside %     = ($96.60 ÷ $72.10) − 1                = +33.98%
Catalyst window  = 2 years (unchanged — Rule 10 default, same ongoing Uber One/AV-monetization
   catalysts as 07-05)
Annualized gap   = 33.98% ÷ 2                            = +16.99%
Intrinsic growth = +12.0%/yr  (unchanged assumption)
Shareholder yield = +2.5%/yr  (unchanged — no newer share-count data)

E = 16.99% + 12.0% + 2.5% = +31.49%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 31.49% ≥ H → M = −15 × clamp((31.49 − 10)/15, 0, 1) = −15 × clamp(1.433, 0, 1) = −15.0
```
**Modifier M = −15.0 (floored)** — same floor as 07-05 (and 06-20), now driven by a slightly wider price gap since the live price fell further below the unchanged PW Fair Value.

**Guardrail checks:** Catalyst still documented and within 18–24 months ✓ (Uber's AV strategy is multi-partner, not solely Lucid-dependent — see §5 note); PW FV still below analyst consensus mean ✓; full calc shown ✓; bounded ±15, sits at the floor ✓.

---

## 9. UBER — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (44.42) + Rate Modifier (+10) + Upside/Downside (−15.0)
                       = 39.42
```
Boundary rule: not a ".X5" case → **Final Valuation Score = 39.4**

| | Value |
|---|---|
| Raw weighted | 44.42 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −15.0 (floored; E = +31.49%) |
| **FINAL VALUATION SCORE** | **39.4** |
| Prior valuation score (07-05) | 41.6 |
| **Quality Score** | **61.0 (unchanged — FAILS 80.0+ gate, decisively, see §5)** |

**Valuation Score band: 39.4 → 30.0–49.9 "Cheap" → nominally BUY, Standard position 3–5%** — same band as 07-05 (41.6). No action-band change from the valuation score alone.

**Composite Score — reference only, per the established practice for a Quality-Score-gate failure on an existing holding:**
```
Composite Score = 0.50×(100 − 61.0) + 0.50×39.4 = 0.50×39.0 + 0.50×39.4 = 19.5 + 19.7 = 39.2
```
**Composite Score = 39.2** (vs. 40.3 on 07-05) — also lands in the same 30.0–49.9 band. **Not adopted to drive the action recommendation** — shown for the record only, per "no black box," consistent with the 80.0+ gate rule that a Composite Score is never computed to rescue a gate-failing name.

---

## 10. UBER — Action Recommendation

**Same two independent blockers as 07-05, both still active:**

1. **Quality Score (61.0) still fails the 80.0+ gate decisively** (§5, unchanged) — this remains a genuine value-trap flag (see glossary): a raw Valuation Score that reads "Cheap" (39.4) sitting on a business that hasn't cleared this framework's quality bar.
2. **Order-setup R/R check, recomputed with today's live price:**

```
Blended Fair Value (= PW FV):              $96.60   (unchanged)
Margin of Safety (30.0–49.9 band):         28%       (unchanged convention)
BUY PRICE (limit):                         $96.60 × (1 − 0.28) = $69.55
PRIMARY SELL TARGET:                       $96.60
BULL-CASE TRIM TARGET (bull × 0.90):       $135.60 × 0.90 = $122.04
STOP LOSS (Buy × (1 − 28%)):               $69.55 × 0.72 = $50.08
R/R at formal entry = (96.60 − 69.55) ÷ (69.55 − 50.08) = 27.05 ÷ 19.47 = 1.389:1  ❌ below 2:1 (unchanged — depends only on PW FV/MoS%, not price)
R/R at live price   = (96.60 − 72.10) ÷ (72.10 − 50.08) = 24.50 ÷ 22.02 = 1.112:1  ❌ still below 2:1 (improved from 0.910:1 on 07-05, since the price fall widened the gap to fair value — still fails the minimum)
```

**Net: HOLD the existing 0.38% position. No fresh capital added — doubly blocked, unchanged from 07-05: an independent R/R failure and the Quality Score's decisive gate failure.**

**Position cap check:** 0.38% is nowhere near the 15% hard cap (Upgrade 7) — not binding, included for completeness.

**No action-band change.** Both the Valuation Score (41.6 → 39.4) and the Composite Score (40.3 → 39.2) moved modestly but stayed inside the same 30.0–49.9 band; the Quality gate status, the R/R-fail status, and the recommendation are all unchanged from 07-05.

**Open item, carried forward:** the 07-05 session recommended the user consider logging a **Human Override** entry (mirroring the ZS/NOW precedent for a held, quality-gate-failing position) — still flagged, not decided or written by this session (`override-log.md` is out of this RESCORE's scope).

---

## 11. Next Review Trigger

- **Routine:** UBER Q2 2026 earnings, expected early August 2026 (unconfirmed exact date) — will refresh every TTM fundamental used here with real Q2 2026 SEC data for the first time since 2026-05-06.
- **New watch item this session:** Lucid's (LCID) financial condition into Q2/Q3 2026 reporting. Uber holds an 11.5% equity stake (~$500M invested) and a 35,000+-vehicle robotaxi-fleet commitment with Lucid; Lucid's own denial of bankruptcy rumors (2026-07-14) is on the record, but real operating distress (weak Q2 deliveries, layoffs, a cut production shift) is independently confirmed. Not a quantified score input this session (§2/§5) — a genuine item to check when Uber next reports (equity-method mark-to-market impact, any AV-partnership-specific disclosure).
- **Open item, carried forward:** the value-trap / Quality Watch flag from 07-05 — still recommend the user decide on a Human Override log entry.
- **Open data item, carried forward:** the March 2024 US rideshare market-share citation is still stale; a fresher independent share-tracker figure would tighten the Moat Signal's "Market share stable/growing" call.
- **Rule 9 triggers (standing):** guidance revision, M&A/material AV investment, management change, a >15% unexplained price move, or the Q2 2026 earnings print itself.

---

## Glossary

| Term | Meaning |
|---|---|
| **AV (Autonomous Vehicle)** | A self-driving vehicle; "robotaxi" refers specifically to an AV operated as an on-demand ride-hailing service. Uber partners with (rather than builds) AV developers — e.g. Lucid/Nuro, Rivian, WeRide, MOIA, Waymo — to deploy AVs on its platform. |
| **CAGR** | Compound Annual Growth Rate. |
| **Chapter 11 (bankruptcy)** | The section of the US Bankruptcy Code covering business reorganization — lets a financially distressed company keep operating while restructuring its debts under court supervision (distinct from Chapter 7, which liquidates the company). A company "considering" or "weighing" Chapter 11 is not the same as having filed — an unconfirmed report and a company's own on-record denial of it are each just a claim, not a settled fact, until an actual filing (or its confirmed absence) is independently verified. Cited here regarding unconfirmed, company-denied 2026-07-14 bankruptcy rumors about Uber's AV-partner Lucid Group (LCID). |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; shown as a **reference-only, not-adopted** number for UBER this session (61.0 Quality Score still fails the gate). |
| **D&A** | Depreciation & Amortization. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Gross Bookings** | The total dollar value of activity transacted through Uber's platform before Uber's own take-rate/revenue is deducted. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Human Override** | A position held outside the framework's own rules — tracked in `override-log.md`; flagged (not adopted) as an open item for UBER, carried forward from 07-05. |
| **MAPC (Monthly Active Platform Consumers)** | The number of unique consumers who used at least one Uber offering in a given month. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **P/FCF (Price-to-Free-Cash-Flow)** | Market capitalization ÷ Free Cash Flow — an earnings-multiple analog used in this framework's UBER scenario architecture since GAAP EPS is too distorted by one-off items to build a reliable EPS×PE scenario set. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. UBER: 61.0, unchanged, still fails the gate. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **Robotaxi** | An autonomous vehicle operated as an on-demand ride-hailing service — see AV above. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; normalize before valuing / require a minimum 2:1 risk/reward; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
| **Value trap** | A stock that looks statistically cheap but stays cheap (or keeps falling) because the underlying business quality is deteriorating or was never strong enough to support a re-rating — the specific risk UBER's Quality Score gate failure is flagged as an example of. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |
