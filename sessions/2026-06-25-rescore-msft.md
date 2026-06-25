# RESCORE — MSFT — 2026-06-25

**Task type:** RESCORE (single ticker)
**Date:** 25 Jun 2026 (Thursday — markets open)
**10Y US Treasury Yield:** 4.40% (TradingEconomics, 25 Jun 2026 — down from the 4.50% used in the 06-23 session; still in the "3.5–5%" bracket)
**Rate Regime Modifier (Step 2):** +5 (unchanged — 10Y still in the 3.5–5% bracket)
**Rate Environment Gate Step 1:** MSFT **FAILS** the Earnings Yield Spread Test → a **separate** +5 additive. **Total Rate Modifier = +10** (unchanged from 06-23).
**Purpose of this run:** routine 2-day interim check per Rule 9 (confirming nothing fired) and a full price-dependent refresh of the 06-23 score.
**Last review on record:** MSFT 34.0 ([sessions/2026-06-23-rescore-msft.md](2026-06-23-rescore-msft.md)).

---

## 1. Live Price (Rule 0)

| Ticker | Latest price used | Source | Note |
|---|---|---|---|
| **MSFT** | **$355.63** | IBKR `get_price_snapshot` (contract 272093), 25 Jun 2026, intraday | Markets open today (Thursday). |

- **Intraday range today:** **$349.20 – $364.23** (IBKR) — the $349.20 low is a **new 52-week low**, breaking the prior $356.28 low recorded on 06-23.
- **52-week range:** **$349.20 – $552.28** (IBKR `misc_statistics`); Yahoo's quoteSummary shows a slightly different high, **$555.45** — a normal small cross-source variance, not reconciled further since the IBKR figure is the framework's primary broker-reported source. Current price sits at the 52-week low and **~35.6% below the 52-week high**.
- **Year-to-date:** **−26.3%** (IBKR).
- **Dividend yield:** 0.97% (IBKR) vs. 1.00–1.02% (Yahoo / stockanalysis.com) — immaterial cross-source drift.
- **Analyst consensus price target (bull-case sanity check):** mean **$561.11**, median **$555**, high **$870**, low **$400** (55 analysts, Yahoo) — essentially unchanged from 06-23 ($561.39 mean).
- **Price drift since last review:** $370.00 (23 Jun intraday) → $355.63 (25 Jun intraday) = **−3.88%**. Well under the 15% Rule 9 threshold — no price-driven fundamental trigger.

---

## 2. Rule 9 Trigger Check (mandatory — 2-day window since 06-23)

News search run for MSFT between 2026-06-23 and 2026-06-25. Findings:

1. **BFA Law / City of St. Clair Shores securities class action (No. 26-cv-02071), surfaced this window.** This is **continued publicity for the same already-disclosed event** previously flagged via the Rosen Law Firm suit on 06-23 — the underlying class period (1 May 2025 – 28 Jan 2026, Copilot/Azure-capacity-constraint conduct) and lead-plaintiff deadline (11 Aug 2026) are unchanged. No new disclosure or financial restatement. **Not a fresh Rule 9 trigger.**
2. **Xbox / Gaming division layoffs — reported/planned, not yet executed or formally disclosed.** Coverage indicates job cuts are expected after FY26 closes (30 Jun 2026), under Gaming-division CEO Asha Sharma (a **divisional**, not corporate, executive — not a management-change trigger), with a previously-acknowledged ~$500M revenue headwind over 5 years. Since this is not yet an executed action or a formal company disclosure, it does **not** meet the Rule 9 bar today — flagged for monitoring; would become a trigger upon formal announcement/execution.
3. **EU Digital Markets Act (DMA) "gatekeeper" preliminary designation for Azure, announced 25 Jun 2026 (today).** This is a **preliminary** finding only — a 60-day consultation period follows, with a final decision expected ~Oct 2026 and compliance obligations (if confirmed) starting spring 2027. No financial impact has been quantified or disclosed yet. **Not a Rule 9 trigger today** — flagged for monitoring; would become one upon final designation or a disclosed compliance-cost estimate.
4. **Nature journal critique of Microsoft's quantum-computing claims (24 Jun 2026).** Reputational/scientific-credibility commentary, not tied to any disclosed financial or guidance impact. **Not a trigger.**
5. **Stifel cut its price target to $400 from $415 (24 Jun 2026).** A single analyst's opinion revision, not a company-disclosed fundamental event. **Not a trigger** (informational only — both old and new targets sit within the existing $400–$870 analyst range already reflected in the bear-case framing, §7).
6. **No earnings, guidance revision, or M&A occurred in the 06-23 → 06-25 window.** Next scheduled earnings remains **FY26 Q4, expected late July 2026**.

**Conclusion: no Rule 9 trigger fired in this window.** This is a routine price-refresh re-score.

---

## 3. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved (6th consecutive session).** MSFT still discloses no maintenance-vs-growth capex split, so Owner Earnings cannot be computed without inventing a figure (prohibited). **Raw TTM Free Cash Flow used** as the FCF_Score input, as in every prior session back to 06-07.
2. **Fundamentals reused from the 2026-06-12 session (no earnings since, confirmed again today — see §2).** Reused: TTM EBIT $148.929B, TTM FCF $72.916B, TTM Net Income $125.22B, net debt $24.922B, shares outstanding 7,428,434,704, EPS-growth Fast-Grower status (TTM +23.3%, unchanged). Only **price-dependent figures refreshed** (market cap, EV, EV/EBIT, FCF yield, forward PE, PEG).
3. **5-year average PE carried forward unchanged**: **31.9693×, range 24.1686×–38.8030×** (n=20 quarters) — no new earnings print since 06-20, so this was not re-derived this session (it was independently re-derived and confirmed identical on 06-23; no change in the underlying 20-quarter window since).
4. **Forward EPS — data-source reconciliation flag (read carefully).** `yfinance` itself was unusable this session: its underlying `curl_cffi` transport failed TLS negotiation through the egress proxy (`OPENSSL_internal: invalid library` — a browser-TLS-fingerprint-impersonation library that the proxy's CA-pinning setup doesn't support; confirmed plain `requests` calls to the same Yahoo hosts worked normally). Rather than disable TLS verification or bypass the proxy (both prohibited), a manual cookie+crumb authentication flow was built against Yahoo's `quoteSummary` API using `requests` directly (fetch a session cookie from `fc.yahoo.com`, then a crumb token, then the data endpoint) — this succeeded cleanly. Separately, three secondary web sources were checked and found **mutually inconsistent and inconsistent with the established session lineage** (~$19.08–19.35 NTM EPS used in 06-20/06-23): stockanalysis.com showed two different pages implying $16.84 and ~$18.01 FY26 EPS respectively, and MarketBeat showed FY26 $15.34 / FY27 $17.47. **Resolution:** used the direct Yahoo `quoteSummary` `forwardEps` figure, **$19.36884** (FY2027 consensus, fiscal year ending 2027-06-30) — nearly identical to 06-23's yfinance-sourced $19.3459 (+0.12% drift only) and the same underlying data source/methodology `yfinance` itself scrapes, making it the most lineage-consistent, authoritative choice. The secondary aggregators were set aside as likely reflecting different or staler consensus aggregations.
5. **Net debt methodology — kept the established figure, did not swap to Yahoo's aggregate.** Yahoo's `totalCash` ($78.228B) / `totalDebt` ($125.432B) fields would imply net debt ≈ $47.2B, materially different from the $24.922B figure sourced from the actual 10-Q balance sheet and reused since. Kept **$24.922B** for cross-session methodological consistency (the Yahoo aggregate likely nets differently, e.g. including/excluding short-term investments differently than the 10-Q-based figure). Cross-check: Yahoo's `sharesOutstanding` (7,428,434,704) matches the reused figure **exactly**, validating that the reused fundamentals remain accurate.
6. **FCF/Net Income conversion ratio** — unchanged from 06-23: 58.2% TTM; 89.6% / 82.2% / 84.0% / 70.3% (FY2022–FY2025). No new quarter available.
7. **Gross margin / ROIC / Revenue CAGR** — Phase 01 quality-gate inputs, not Phase 02 score inputs. No new data since 06-20 (no earnings). Not re-collected; flagged, not guessed.
8. **Scenario fair value carried forward from 06-23, recalculated at the new price.** No fundamental change occurred (§2) to justify revising the bull/base/bear PE multiples (31.0×/27.0×/21.0×), intrinsic growth (13%/yr), or shareholder yield (1.96%) assumptions. Only the live price and resulting NTM EPS, Gap Upside %, and E were recalculated.

---

## 4. MSFT — Inputs (price-refreshed)

**Sector:** Technology — Software, Cloud Infrastructure (Azure) & Productivity
**Current portfolio weight:** ~15.01% per the 2026-06-22 sync recorded in `holdings.md` (see §9 — likely stale given the price move since; not re-derived here).

| Item | Value | Basis |
|---|---|---|
| Live price | $355.63 | Rule 0, §1 |
| Shares outstanding | 7,428,434,704 | Reused (10-Q FY26 Q3 cover); cross-validated exactly against Yahoo today |
| **Market Cap** | 7,428,434,704 × $355.63 = **$2,641.774B** | Computed |
| Net debt | $24.922B | Reused (10-Q) — §3 flag 5 |
| **Enterprise Value (EV)** | $2,641.774B + $24.922B = **$2,666.696B** | Computed |
| TTM EBIT | $148.929B | Reused |
| **EV/EBIT** | 2,666.696 ÷ 148.929 = **17.9058×** | Computed (was 18.6226× at $370.00) |
| TTM FCF | $72.916B | Reused |
| **FCF Yield** | 72.916 ÷ 2,641.774 = **2.7601%** | Computed (was 2.6529%) |
| TTM Net Income | $125.22B | Reused |
| Forward EPS (NTM, FY2027 consensus) | **$19.36884** | Yahoo `quoteSummary` direct pull — §3 flag 4 |
| **Forward PE** | 355.63 ÷ 19.36884 = **18.3609×** | Computed (was 19.2592×) |
| 5yr avg PE (trailing anchor) | **31.9693×** (range 24.1686–38.8030×) | Reused unchanged — §3 flag 3 |
| EPS growth (Fast Grower test) | TTM +23.3% — **>15% → Fast Grower confirmed, unchanged** | Reused |
| PEG | **0.7880** (18.3609 ÷ 23.3) | Computed |
| FCF/NI conversion | 58.2% (TTM) | §3 flag 6 — unchanged |
| Net Debt/EBITDA | 0.131× | Reused — well within limits |

---

## 5. MSFT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 18.3609 = 5.4464%
Spread = EY − 10Y Treasury = 5.4464% − 4.40% = +1.0464%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+1.0464%, ~0.45pp short) → **+5 additive**.
(Spread improved materially vs. 06-23's +0.6923% — the lower price pushed Forward PE down faster than the 10Y yield fell — but still short of passing.)

**Step 2 — Rate Regime Modifier**
10Y = 4.40% → "3.5–5%" bracket → **+5** (unchanged)

**Total Rate Modifier for MSFT = +10** (unchanged from 06-23)

---

## 6. MSFT — Full Score Calculation (raw weighted + Rate Modifier)

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.7601 / 10), 0, 100) = 72.399
```
→ Contribution: 72.399 × 0.40 = **28.9596**

**EV/EBIT — 25% weight**
```
EV/EBIT_Score = clamp((17.9058 − 12) / 23 × 100, 0, 100) = 25.677
```
→ Contribution: 25.677 × 0.25 = **6.419**

**Forward PE (fallback formula — 5yr avg only) — 20% weight**
```
Deviation% = (18.3609 − 31.9693) / 31.9693 × 100 = −42.567%
FwdPE_Score = clamp(50 + (−42.567) × 2.5, 0, 100) = clamp(−56.418, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0** (floored — unchanged from every session since 06-20)

**PEG — 15% weight (Fast Grower confirmed, §4)**
```
PEG       = Forward PE ÷ TTM EPS growth% = 18.3609 ÷ 23.3 = 0.7880
PEG_Score = clamp((0.7880 − 0.5) / 2.0 × 100, 0, 100) = 14.401
```
→ Contribution: 14.401 × 0.15 = **2.160**

**Raw weighted score:**
```
= 28.9596 + 6.419 + 0.0 + 2.160
= 37.539
```
**+ Rate Modifier (+10) = 47.539** (before the Upside/Downside Modifier)

---

## 7. MSFT — Upside/Downside Modifier (refreshed at new price)

**Step 0 — Scenario fair value.** No fundamental change occurred since 06-23 (§2), so the bull/base/bear PE multiples, intrinsic growth, and shareholder yield assumptions remain defensible and are **carried forward** — only the live price and the resulting NTM EPS/Gap/E are recalculated.

NTM EPS = **$19.36884** (direct Yahoo `quoteSummary` figure, §3 flag 4 — used directly rather than back-solved from price ÷ forward PE, since the forward PE in §4 was itself derived from this same EPS figure).

| Scenario | Weight | PE applied | Rationale (unchanged from 06-23 — still defensible, no new information) | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | 31.0× | Azure/AI monetization re-accelerates; multiple re-rates to ~5yr average (31.97×). Still below the $561 analyst-mean PT and far below the $870 high. | $19.36884 × 31.0 = **$600.43** |
| **Base** | 50% | 27.0× | Consensus mid-teens EPS growth, haircut multiple vs. the 31.97× 5yr average to reflect the rate regime. | $19.36884 × 27.0 = **$522.96** |
| **Bear** | 25% | 21.0× | Growth decelerates / AI-capex returns disappoint; multiple de-rates near the low end of the 5yr band (24.17×). Bear FV $406.75 remains close to the analyst $400 low PT. | $19.36884 × 21.0 = **$406.75** |

```
PW Fair Value = 0.25×600.43 + 0.50×522.96 + 0.25×406.75 = $513.27
```
(Probability-Weighted. Sits below the $561 analyst mean and $555 median PT — still conservative, sanity-check passes. Up modestly from 06-23's $509.11, driven by the slightly higher direct-sourced NTM EPS.)

**Step 1 — Expected annual return E.**
```
Gap Upside %     = (513.27 ÷ 355.63) − 1                  = +44.327%
Catalyst window  = 2 years (unchanged — FY26 Q4 late-Jul-2026 print + FY27 Azure/AI
                   re-acceleration cycle; still within Rule 10's 18–24mo horizon)
Annualized gap   = 44.327% ÷ 2                             = +22.164%
Intrinsic growth = +13%/yr (unchanged)
Shareholder yield = dividend ~0.96% + net buyback ~1.0%    = +1.96% (unchanged;
                    today's IBKR dividend-yield read of 0.97% is immaterially different)

E = 22.164% + 13% + 1.96% = +37.124%
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 37.124% ≥ H → M = −15 × clamp((37.124 − 10)/15, 0, 1) = −15 × clamp(1.808, 0, 1) = −15.0
```
**Modifier M = −15.0** (the maximum attractive bound — unchanged from 06-20 and 06-23; E moved even further above the +25%/yr full-credit threshold, but the modifier is bounded and cannot go any more negative).

**Guardrail checks:**
1. **Catalyst:** documented (FY26 Q4 earnings + FY27 Azure/AI cycle), within 18–24 months → upside credit allowed. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($513.27) is below the analyst mean ($561) and median ($555); bear case underwritten near the $400 low PT. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** at the −15 floor. ✓

---

## 8. MSFT — Final Score & Action

```
Final Score = raw weighted 37.539 + Rate Modifier (+10) + Upside/Downside Modifier (−15)
            = 32.539
```
Boundary rule: not a ".X5" → standard rounding → **Final Score = 32.5**

# Final Score: 32.5 → Action band: BUY — Standard position 3–5% (30.0–49.9)

**Did the score change vs. 06-23?** **Yes** — 34.0 → 32.5 (**−1.5 points**). The entire move is attributable to the **raw weighted score** falling from 39.036 to 37.539 (−1.497) — driven by the lower live price making FCF Yield, EV/EBIT, and PEG all cheaper (their sub-scores all fell, since lower = more attractive on this scale). The **Rate Modifier (+10) and Upside/Downside Modifier (−15) were both unchanged** — the rate bracket didn't shift and the expected-return modifier was already pinned at its −15 floor in both sessions, despite E itself rising further (33.76% → 37.124%). **The action band did NOT change** — still BUY — Standard (30.0–49.9), the third consecutive session in this band.

---

## 9. Portfolio / Compliance Note (independent of valuation score)

`portfolio/holdings.md` shows MSFT at **~15.01%** as of the **2026-06-22** sync — marginally over the 15% hard cap (Upgrade 7), the same structural concentration issue flagged across the last 6 consecutive sessions (06-07, 06-11 backfill, 06-12, 06-20, 06-23, and now 06-25). **This figure is not re-derived here and is likely stale**: MSFT's price has fallen ~6% combined since that sync ($370.00 on 06-23 → $355.63 today), which mechanically shrinks its portfolio weight if other holdings' prices and total portfolio value haven't moved proportionally. An authoritative updated weight requires a fresh `/sync-portfolio` or `/rebalance` run — not estimated here, per the "orchestrator owns holdings.md weight" convention. The open compliance trim from the 2026-06-15 rebalance remains the nominal action item until that re-sync happens.

---

## 10. Order Setup (BUY band requires it — shown, with the gating flags)

Computed for completeness because the score lands in a BUY band, but **note the gating flags below** — the trade is not actionable, same headline conclusion as 06-20 and 06-23, though one secondary check has changed (see below).

```
Blended Fair Value (= PW FV):        $513.27
Margin of Safety (Score 30–49.9):    25%   (lower end; wide-moat proven compounder — unchanged rationale)
BUY PRICE (limit):                   $513.27 × (1 − 0.25) = $384.95
  → Live price $355.63 is BELOW the formal buy price (−7.62%) — nominally an actionable entry level.
PRIMARY SELL TARGET (blended FV):    $513.27
BULL-CASE TRIM TARGET (bull × 0.90): $600.43 × 0.90 = $540.39
STOP LOSS (Buy × (1 − 25%)):         $384.95 × 0.75 = $288.71   (below the new 52-week low $349.20 — a wide structural stop)
R/R at formal entry = (513.27 − 384.95) ÷ (384.95 − 288.71) = 128.32 ÷ 96.24 = 1.333:1
```

**⚠️ Formal R/R = 1.333:1 is BELOW the 2:1 minimum (Rule 6) — unchanged from 06-20 and 06-23.** This is not a coincidence of this particular price: under the framework's fixed parameters (MoS = MaxLoss = 25%), the formal R/R anchored to the calculated Buy Price is **algebraically invariant at exactly 1.333:1 regardless of fair value or live price** — `(FV − Buy)/(Buy − Stop) = (0.25·FV)/(0.25·0.75·FV) = 1/0.75 = 1.333`. It will not cross 2:1 at any price under the current MoS/MaxLoss settings; only a change to those parameters (or to the order-setup formula itself) could move it.

**Secondary check — live price as entry (informational, not the framework's operative gate):** using today's live price ($355.63) directly as the entry instead of the formal Buy Price gives R/R = (513.27 − 355.63) ÷ (355.63 − 288.71) = 157.64 ÷ 66.92 = **2.355:1** — **the first session in which this secondary check has crossed above 2:1** (up from ~1.66:1 implied on both 06-20 and 06-23), because the live price has now fallen further below the formal Buy Price than in prior sessions while the Sell Target and Stop Loss (both formula-anchored, not live-price-anchored) held steady in dollar terms. **This does not change the action**, since the framework's order-setup methodology evaluates R/R against the formal limit Buy Price, not an opportunistic live-tick entry — but it is flagged transparently as a real, measurable change worth tracking: if price continues lower toward the Buy Price itself, the formal and live-price R/R figures converge toward the same (sub-2:1) number.

**Net:** the same two independent gates still block adding capital here — (a) the ~15.01% position cap (per the 06-22 sync, likely stale and possibly smaller now — see §9), and (b) the formal sub-2:1 R/R (1.333:1, structurally fixed). The BUY-band **score** (32.5) stands and is the headline of this rescore; the **trade** does not execute.

---

## 11. Next Review Trigger

- **Routine:** MSFT FY2026 Q4 earnings (fiscal year ending June 2026), expected **late July 2026** — standard post-earnings re-score (will also refresh the TTM fundamentals reused here for the 7th consecutive session).
- **Open compliance item (6th flag):** dedicated `/rebalance` or `/sync-portfolio` run to get an authoritative current position weight — the ~15.01% figure on record is now ~3 days stale against a ~6% price decline and may already have narrowed or resolved.
- **Open methodology item:** Upgrade 1 (Owner Earnings) decision for non-disclosing mega-caps (§3 flag 1).
- **Monitoring items (new, not Rule 9 triggers):** (a) BFA Law/St. Clair Shores securities class action — track for escalation alongside the existing Rosen Law Firm suit; (b) Xbox/Gaming layoffs — would become a Rule 9 trigger upon formal announcement/execution (expected after FY26 closes 30 Jun 2026); (c) EU DMA "gatekeeper" preliminary designation for Azure — would become a trigger upon the final ~Oct 2026 decision or a disclosed compliance-cost estimate.
- **Watch:** the live-price-as-entry R/R (2.355:1, §10) is informational only — if price recovers toward the $384.95 formal Buy Price, it converges back down toward the still-failing 1.333:1 formal figure; if price falls further, the live-price R/R improves further but the formal gate (structurally fixed at 1.333:1 under current MoS/MaxLoss parameters) will not change. Re-derive everything at the next earnings print regardless.

---

## Glossary

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year — a quick gauge of where the current price sits within its recent trading history. |
| **bps (basis points)** | 1 bps = 0.01 percentage points. |
| **CAGR** | Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers). |
| **Catalyst window** | The timeframe (per Rule 10, typically 18–24 months) within which a documented, specific event is expected to close the gap between price and fair value — required before the Upside/Downside Modifier can credit large expected upside. |
| **D&A** | Depreciation & Amortization — the non-cash accounting expense that spreads the cost of long-lived assets over time. |
| **EBIT** | Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate. |
| **EPS** | Earnings Per Share — net income divided by number of shares outstanding. |
| **EV** | Enterprise Value — a company's total value to all capital providers: market cap + debt − cash. |
| **EV/EBIT** | Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE — the inverse of the PE ratio, expressed as a yield so it can be compared directly against bond yields (e.g. the 10-Year Treasury). |
| **Fast Grower** | Peter Lynch's term for a company growing earnings per share (EPS) faster than 15%/year for 3+ years — this framework's trigger for applying the PEG sub-score. |
| **FCF** | Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest. |
| **FCF Yield** | Free Cash Flow ÷ Market Cap — how much free cash a company throws off relative to its price; higher is cheaper. |
| **FCF/NI conversion ratio** | Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash. |
| **Forward PE** | Price ÷ next twelve months' expected earnings per share. |
| **FV (Fair Value)** | The analyst's estimate of what a company is intrinsically worth, independent of its current market price. |
| **Hurdle rate** | The minimum acceptable annual return for an investment to be worth making — this framework uses 10% as the hurdle the Upside/Downside Modifier measures expected return against. |
| **M&A** | Mergers & Acquisitions — one company buying or combining with another. |
| **MoS (Margin of Safety)** | How far below fair value the buy price is set, as a cushion against being wrong. |
| **Net Debt/EBITDA** | Net debt divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt. |
| **NI (Net Income)** | Net Income — accounting profit after all expenses, interest, and taxes ("the bottom line"). |
| **NTM (Next Twelve Months)** | The forward-looking 12-month period used for forward earnings estimates. |
| **Owner Earnings** | Warren Buffett's adjusted cash-flow measure: Net Income + D&A − Maintenance CapEx only — used instead of raw FCF for moat-building reinvestors like MSFT (Hybrid Upgrade 1). |
| **PE (Price-to-Earnings) ratio** | Share price ÷ earnings per share. |
| **PEG ratio** | PE ratio ÷ earnings growth rate — a PE adjusted for growth. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **PT (Price Target)** | An analyst's forecast of where a stock's price will be at a future date. |
| **PW (Probability-Weighted) Fair Value** | This framework's blended fair value estimate — 25% bull case + 50% base case + 25% bear case (Rule 7). |
| **R/R (Risk/Reward ratio)** | (Expected gain) ÷ (Expected loss) on a trade — this framework requires at least 2:1 before entering. |
| **Rate Environment Gate** | The mandatory pre-check run before every Phase 02 valuation score, comparing Earnings Yield against the 10-Year Treasury yield and applying a Rate Regime Modifier. |
| **Rate Regime Modifier** | An additive adjustment (−10 to +10) applied to the valuation score based on which Treasury-yield bracket the market is currently in. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause. |
| **Shareholder yield** | Cash returned to shareholders as a percentage of share price — dividend yield plus net buyback yield combined. |
| **Treasury yield (10Y)** | The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | An additive ±15 adjustment to the valuation score based on expected annual return (the gap to PW Fair Value, annualized over the catalyst window, plus intrinsic growth and shareholder yield). |
