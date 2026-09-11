# NEW POSITION — DOCS (Doximity, Inc.) — 2026-09-11

**Task type:** NEW POSITION
**Date:** 11 Sep 2026
**Ticker:** DOCS (Doximity, Inc. — Class A common stock, NYSE)
**Sector:** Healthcare Information Services / Digital Health SaaS
**10Y US Treasury yield:** 4.95% (TradingEconomics, 11 Sep 2026 session — up sharply from 4.49% at the 2026-07-07 session; global bond selloff pushing 10Y yields toward the 5% mark, per Bloomberg 11 Sep 2026)
**Current DOCS portfolio weight:** 0% — not held. The only prior DOCS exposure was a short put (speculation sleeve) that expired worthless 2026-08-21 — see [portfolio/speculation-log.md](../portfolio/speculation-log.md) and the [override-log](../portfolio/override-log.md) entry; that is a separate, closed matter and does not block this core-framework evaluation.

**Pre-check (per this session's brief):** confirmed via `portfolio/holdings.md` and `portfolio/override-log.md` that DOCS is not a current core-framework holding. Confirmed via `sessions/` directory listing that no DOCS session exists between 2026-07-07 and today — this is a full fresh re-run, not a duplicate. No `watchlist/STALE.md` entry exists for DOCS.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$24.71** | IBKR `get_price_snapshot`, contract_id 498661844 (NYSE), `last.price` (flagged `is_close: true` — matches `prior_close` exactly, consistent with a snapshot taken outside regular NYSE trading hours; this is still a genuine live broker quote, not an inferred or stale portfolio-snapshot price, per Rule 0) |
| Bid / Ask | $24.50 / $25.70 | Same snapshot |
| 52-week range | $17.155 – $76.50 | IBKR `misc_statistics` |
| 13-week range | $19.65 – $40.00 | IBKR `misc_statistics` |
| YTD change | −44.2% | IBKR `year_to_date_change` |
| Cross-check | $24.07–$25.04 intraday, $24.19 prior close (5 Sep 2026) | WebSearch, Yahoo Finance/CNBC |
| Analyst consensus PT | Mean $29.78–$29.94 (18–21 analysts), consensus "Hold" | stockanalysis.com, yfinance `targetMeanPrice` |
| Analyst PT range | $18.00 – $47.00 | yfinance `targetLowPrice`/`targetHighPrice` |

**Rule 9 context since the 2026-07-07 session (mandatory before scoring):**

1. **Q1 FY2027 earnings (6 Aug 2026) — a beat-and-raise, not a further cut.** Revenue $156.6M (+7% YoY), beating guidance by 3%; Adjusted EBITDA $75M (48% margin), beating guidance by 8%. Full-year FY2027 revenue guidance was **raised** to $671–681M (from the 13 May 2026 guide of $664–676M) and Adjusted EBITDA guidance set at $309–329M. Workflow active-prescriber growth >30% YoY, AI Search query growth >25% QoQ. This is a materially different picture from the 2026-07-07 session, which was written directly after the 13 May guidance-cut shock.
2. **GAAP net income fell sharply this quarter despite the top-line beat** — Q1 FY2027 net income $24.3M vs. $53.3M in the prior-year quarter (net margin 15.5% vs. 36.5%), driven by the AI-compute investment ramp management had flagged. This is the real-time evidence of the margin-compression thesis playing out, now confirmed in filed financials rather than only guided.
3. **Securities litigation:** the case tracked in the 2026-07-07 session (Schall Law Firm, Pomerantz LLP, Halper Sadeh LLC investigations into the 13 May 2026 guidance-cut disclosures) remains an **open, unresolved investigation** — no filed class-action complaint found this session specific to the May 2026 event. Separately, an **older, unrelated** securities class action (covering the 24 Jun 2021–8 Aug 2023 purchase period) reached final settlement approval 11 Jun 2026 ($31M, ~$0.32/share average recovery) — that matter is fully concluded and not relevant to the open 2026 investigation.
4. **Next earnings date:** 5 Nov 2026 (Q2 FY2027), per `yfinance` `get_earnings_dates` — within this session's monitoring window.

---

## 2. Quality Score (Phase 01) — [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29

### Hard disqualifiers — checked first on the current rolling window, none fire

| Disqualifier | Result |
|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | **No** — 183.4% (TTM to Jun 2026), 166.5% (FY2026), 122.4% (FY2025) — all far above 70% |
| Net Debt/EBITDA over threshold | **No** — net **cash** position (Total debt $9.67M vs. cash & ST investments $687.79M, Q1 FY2027 10-Q) |
| Not FCF-positive for 3+ consecutive years | **No** — FCF positive every year FY2022–FY2026 plus current TTM |

### Inputs (all sourced — none invented)

| Metric | Value | Source |
|---|---|---|
| Net Margin (TTM to Jun 2026) | 25.48% | stockanalysis.com (TTM Net Income $167.05M / Revenue $655.57M) |
| Gross Margin (TTM) | 88.07% | stockanalysis.com |
| Revenue (FY2023 → FY2026, most recently completed FYs) | $419.05M → $644.86M | stockanalysis.com |
| Operating Income / EBIT (TTM to Jun 2026) | $200.43M | stockanalysis.com |
| Effective tax rate (TTM) | 26.13% | Derived: TTM pretax = FY2026 pretax ($250.01M) − Q1 FY2026 pretax ($64.14M, back-solved from reported NI $53.3M ÷ (1−16.9%) per Doximity's own 10-Q) + Q1 FY2027 pretax ($40.4M, filed 10-Q) = $226.27M; TTM tax = $53.95M − $10.84M + $16.0M = $59.11M → 59.11/226.27 = 26.13%. Cross-check: this reconstruction reproduces TTM Net Income of $167.05M exactly, matching stockanalysis.com's independently-reported TTM NI. |
| Total Debt (Q1 FY2027, 30 Jun 2026) | $9.67M | SEC 10-Q (docs-20260630) via stockanalysis.com |
| Total Cash + ST investments (Q1 FY2027) | $687.79M | Same |
| Total Shareholders' Equity (Q1 FY2027) | $916.07M | Same |
| FCF (TTM / FY2026 / FY2025) | $306.28M / $326.46M / $273.27M | stockanalysis.com cash flow statement |
| Net Income (TTM / FY2026 / FY2025) | $167.05M / $196.05M / $223.19M | stockanalysis.com |
| Market share | >85% of US physicians on the network (some third-party sources cite 80%+) | Doximity press releases; cross-checked WebSearch, unchanged from 2026-07-07 |

### Profitability (25% weight)

```
NetMargin_Component = clamp((25.48/30)×100, 0, 100) = 84.9

ROIC calculation (NOPAT ÷ Invested Capital, this framework's convention:
Invested Capital = Total Debt + Equity − Cash):
  NOPAT = EBIT × (1 − tax rate) = $200.43M × (1 − 0.2613) = $148.09M
  Invested Capital = $9.67M + $916.07M − $687.79M = $237.95M
  ROIC = $148.09M / $237.95M = 62.23%
ROIC_Component = clamp((62.23/30)×100, 0, 100) = 100.0   (clamped)

Profitability_Score = (84.9 + 100.0) / 2 = 92.5   (no FCF cap — FCF-positive every year through TTM)
```

Flag (unchanged from 07-07): a granular "cash & equivalents only, excluding ST investments" sensitivity breakdown was not sourced this session — the Invested Capital convention used matches how Net Debt/EBITDA already nets all cash, but the gap between methodologies (this framework's vs. some third-party ROIC readings) remains real and is carried forward as an open item, not resolved.

### Margins (15% weight)

```
GrossMargin_Score = clamp((88.07/80)×100, 0, 100) = 100.0   (clamped)
```
Gross margin has run 87–90% for 5+ straight years including the current TTM window — already at the ceiling; no trend bonus needed (would clamp regardless).

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2023→FY2026, most recently completed FYs) = (644.86/419.05)^(1/3) − 1 = 15.45%
Growth_Score (raw) = clamp((15.45/25)×100, 0, 100) = 61.8

Structural deceleration modifier: −10
```
Evidence (cited, not inferred, updated this session): revenue growth has decelerated every year — 66.05% (FY2022) → 19.98% (FY2025) → 13.05% (FY2026) → now guided to ~4.8% for FY2027 (raised range $671–681M vs. FY2026's $644.86M, midpoint +4.83%). Even though the Q1 FY2027 print was a beat-and-raise (positive surprise vs. the guide itself), the guide's own growth rate is still a steep structural deceleration versus FY2026's 13.05% and far below the historical run-rate — satisfying the "documented evidence" bar for this modifier, same conclusion as 2026-07-07 albeit off updated numbers.

```
Growth_Score = 61.8 − 10 = 51.8
```

### Balance Sheet (15% weight)

```
Net Debt = $9.67M − $687.79M = −$678.12M (net CASH position)
Net Debt/EBITDA = negative (net cash) → clamp(100×(1 − ratio/4), 0, 100) = 100.0
```

### Moat Signal (15% weight) — 3 of 5 TRUE, unchanged from 2026-07-07 (no new evidence sourced or refuting this session)

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | >85% of US physicians (Doximity press releases, cross-checked WebSearch) |
| Network effect | **TRUE** | Two-sided mechanism: 85%+ physician penetration connects pharma/health-system advertisers to physicians who "decide over 70% of healthcare spending" |
| Switching costs | **TRUE** | Sequential product build-out (identity/network → Dialer/messaging/fax → drug reference → Scribe → DoxGPT/Ask → telehealth → Photon prescribing) embeds multiple daily-workflow tools in one platform |
| Brand premium (pricing power) | **FALSE** | No cited evidence of price increases without volume loss found this session |
| Scale cost advantage | **FALSE** | No cost-per-unit data vs. smaller competitors found this session |

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI ratio (TTM) = 306.28/167.05 = 183.4%
FCFQuality_Score = clamp(((1.834 − 0.40)/0.60)×100, 0, 100) = 100.0   (clamped)
```
2-year check: FY2026 166.5%, FY2025 122.4% — both far above the 70% hard-disqualifier threshold (elevated by heavy SBC add-backs, typical of asset-light SaaS).

### Quality Score total

```
Quality Score = 92.5×0.25 + 100.0×0.15 + 51.8×0.20 + 100.0×0.15 + 60.0×0.15 + 100.0×0.10
              = 23.11 + 15.0 + 10.36 + 15.0 + 9.0 + 10.0
              = 82.47 → 82.5
```

**82.5 ≥ 80.0 — clears the gate**, though by a narrower margin than the 2026-07-07 session's 84.4. The delta is driven almost entirely by Profitability_Score falling from 100.0 (clamped) to 92.5 — TTM net margin (25.48%) is meaningfully below FY2026's full-year net margin (30.40%) because the AI-investment cost ramp Doximity flagged in May has now shown up in a filed quarter (Q1 FY2027 net margin only 15.5%). **DOCS clears the 80.0+ Quality Score gate** and proceeds to Phase 02.

---

## 3. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:**
```
Forward PE (stockanalysis.com) = 17.35   [yfinance's own forwardPE field reads 15.95 — a secondary, slightly more optimistic
                                           consensus-EPS-basis read; flagged, not resolved, doesn't change the Step 1 outcome
                                           either way, see sensitivity below]
EY = 1/17.35 = 5.764%
Spread = 5.764% − 4.95% = +0.814%  < +1.5% → FAILS Step 1 → additive +5 to the valuation score

Sensitivity (yfinance forwardPE 15.95): EY = 6.27%, Spread = +1.32% — still < +1.5%, same FAIL outcome either way.
```
This is a reversal from the 2026-07-07 session, where the spread (+2.485%, using a 4.49% 10Y) passed comfortably — the ~46bp jump in the 10Y yield since then, not a change in DOCS's own multiple, is what flipped this test.

**Step 2 — Rate Regime Modifier:** 10Y = 4.95% → 3.5–5% bracket → **+5**

**Total Rate Environment additive this session: +10** (both Step 1's spread-fail flag and Step 2's regime modifier fire — see the 2026-06-11 watchlist backfill note on why both apply as separate additive adjustments, not one-or-the-other).

---

## 4. Valuation Score (Phase 02) — [valuation-scoring.md](../framework/valuation-scoring.md), methodology version 2026-06-29

### Fast-Grower eligibility (PEG) — still does not qualify

Historical EPS/revenue growth is still **decelerating** (66%→20%→13%→~4.8% guided), and the one forward-looking analyst consensus figure that clears 15% (2027→2029 EPS CAGR ≈15.05%, see §5) is a forecast, not a realized, clean multi-year earnings base. **PEG not applicable — its 15% weight redistributed to EV/EBIT (→ 40%)**, unchanged from 2026-07-07.

### FCF Yield (40% weight)

```
Market Cap = Live Price × Shares Outstanding = $24.71 × 178.25M = $4,405.88M
  (178.25M = stockanalysis.com's live-quote share count; the 10-Q's period-end count was 179.85M
  at 30 Jun 2026 — the ~1.6M share gap is consistent with continued buybacks since quarter-end,
  not a data conflict)
FCF Yield = FCF (TTM to Jun 2026) / Market Cap = $306.28M / $4,405.88M = 6.953%
FCF_Score = clamp(100×(1 − 6.953/10), 0, 100) = 30.5
```

### EV/EBIT (40% weight, redistributed)

```
EV = Market Cap + Total Debt − Cash&STI = $4,405.88M + $9.67M − $687.79M = $3,727.76M
EBIT (TTM to Jun 2026) = $200.43M
EV/EBIT = 18.60×
EV/EBIT_Score = clamp((18.60 − 12)/23 × 100, 0, 100) = 28.7
```
Cross-check: `yfinance`'s own EV/EBITDA read (17.88×, EBITDA-basis) is directionally consistent with this EBIT-basis 18.60× (EBITDA > EBIT, so a slightly lower multiple on that base is expected).

### Forward PE (20% weight) — no-history fallback, unchanged conclusion from 2026-07-07

Re-ran the framework's automated 5yr-PE-range reconstruction (`yfinance.get_earnings_dates` → rolling TTM EPS → paired price history). Result: Doximity's full reportable earnings history (IPO June 2021, first reported EPS Aug 2021) yields only **18 of the required 20 quarters** of TTM-EPS-with-price data — one quarter more than the 07-07 session's 17, but still short of the threshold. Per the framework's explicit "<20 quarters → no-history fallback" rule:

```
FwdPE_Score = 50.0  (neutral, flagged — no-history fallback; will not qualify for the primary/fallback PE formulas
                     until DOCS has ~2 more reporting quarters, i.e. around Feb 2027)
```

### Final Score (raw, before modifiers)

```
Final Score (raw) = FCF_Score×0.40 + EV/EBIT_Score×0.40 + FwdPE_Score×0.20
                   = 30.5×0.40 + 28.7×0.40 + 50.0×0.20
                   = 12.20 + 11.48 + 10.0
                   = 33.68
```

### Rate Regime Modifier: **+10** (from §3)

### Upside/Downside Modifier — full calc shown

**Step 1 — Fair Value (bull/base/bear), via the two required methods (Rule 1: DCF + Multiples):**

*Method A — 3-stage DCF* (Rule 2: yrs 1–5 explicit, yrs 6–10 fade, yr 10+ terminal at 2.5%). Base-year (Yr-1) FCF anchored to the raised FY2027 Adjusted EBITDA guidance ($309–329M) at scenario-varied FCF-conversion assumptions (calibrated off FY2026's realized ~91% FCF/Adj.EBITDA conversion); yrs 2–5 growth and WACC varied per scenario per Rule 2/7. WACC built from risk-free 4.95% (10Y, live) + beta 1.25 (`yfinance`, close to the 07-07 session's 1.293) × 5% assumed ERP = 11.2% cost of equity ≈ WACC (net-cash balance sheet, negligible debt weight); varied ±1pp per scenario:

| Scenario | Yr-1 FCF (vs. TTM $306.28M) | Yrs 2–5 growth | WACC | DCF FV/share |
|---|---|---|---|---|
| Bear | $262.65M (−14.2%, 85% conversion of $309M low-end guide) | 3%/yr, fade to 2.5% | 12.2% | $19.79 |
| Base | $287.10M (−6.3%, ~90% conversion of $319M midpoint guide) | 8%/yr, fade to 2.5% | 11.2% | $29.27 |
| Bull | $312.55M (+2.0%, 95% conversion of $329M high-end guide) | 15%/yr, fade to 2.5% | 10.2% | $49.79 |

*Method B — Peer multiples* (Rule 5: 5–10 peers, similar business model, median not mean, EV-based, revenue scale ±50%). **Methodology correction this session:** the 2026-07-07 peer set (VEEV, CERT, PHR, HSTM) never actually checked Rule 5.2's revenue-scale requirement (±50% of DOCS's own revenue) — re-applying it now with fresh data: DOCS TTM revenue $655.57M implies a ±50% band of $327.8M–$983.4M. **VEEV excluded** (TTM revenue $3,458M, >5× DOCS — a clear scale violation, not caught last session). **DH excluded** (TTM revenue $232.7M, below the band, and its EV/EBITDA of 3.86× remains a clear distressed-multiple outlier). CERT ($421.7M) and PHR ($507.8M) sit cleanly inside the band; HSTM ($321.1M) and HCAT ($292.2M) sit modestly below it (2% and 11% short respectively) but share DOCS's asset-light healthcare-IT business model — retained given Rule 5.1's 5-peer minimum and the absence of a better-fitting alternative, flagged as a judgment call:

| Peer | TTM Revenue | EV/EBITDA |
|---|---|---|
| CERT (Certara) | $421.7M | 13.25× |
| PHR (Phreesia) | $507.8M | 14.31× |
| HSTM (HealthStream) | $321.1M | 17.62× |
| HCAT (Health Catalyst) | $292.2M | 16.71× |

Applied to DOCS's TTM EBITDA ($208.40M, `yfinance`, GAAP-consistent basis matching the peer figures — not Doximity's own non-GAAP Adjusted EBITDA):

| Scenario | Peer EV/EBITDA used | Implied EV | + Net Cash $678.12M | ÷ 178.25M shares | Multiples FV/share |
|---|---|---|---|---|---|
| Bear | 13.25× (peer low) | $2,761.3M | $3,439.4M | | $19.30 |
| Base | 15.51× (median of 4) | $3,232.3M | $3,910.4M | | $21.94 |
| Bull | 17.62× (peer high) | $3,672.0M | $4,350.1M | | $24.41 |

**Triangulation (40% DCF + 60% Multiples, per fair-value-methodology.md Step 1):**

```
Bear:  0.40×$19.79 + 0.60×$19.30 = $19.50
Base:  0.40×$29.27 + 0.60×$21.94 = $24.87
Bull:  0.40×$49.79 + 0.60×$24.41 = $34.56
```

**PW Fair Value (Rule 7):**
```
PW Fair Value = 0.25×$34.56 + 0.50×$24.87 + 0.25×$19.50 = $25.95
```
Sanity check (Rule 4): PW FV $25.95 sits just below the analyst PT mean ($29.78–$29.94) and comfortably inside the $18–$47 PT range — not an outlier call.

**Step 2 — Expected annual return `E`:**

```
Gap Upside% = ($25.95 / $24.71) − 1 = +5.02%
Catalyst window = 2 years (default — see guardrail discussion below)
Annualized gap = 5.02% / 2 = 2.51%
Intrinsic growth = 15.05%/yr — analyst consensus EPS CAGR, FY2027 ($1.38) → FY2029 ($1.83)
                   (stockanalysis.com forecast page; used in preference to a self-generated
                   DCF growth assumption, per "never invent")
Shareholder yield = 0% dividend + 4.06% net buyback
  (Ordinary shares outstanding fell 187,452,885 (30 Jun 2025) → 179,849,444 (30 Jun 2026),
   i.e. −4.06% over the trailing year, per yfinance quarterly balance sheet — the actual
   net share-count change, already netting any SBC-driven issuance against buybacks)

E = 2.51% + 15.05% + 4.06% = 21.62%
```

**Step 3 — Map to modifier, with the catalyst guardrail:**

```
E (21.62%) ≥ H (10%) → M (uncapped) = −15 × clamp((21.62−10)/15, 0, 1) = −15 × 0.7747 = −11.62
```

**Guardrail applied — capped at −5.0.** Rule 10 requires a documented catalyst + timeline before crediting large upside. Management's Q1 FY2027 beat-and-raise is real, filed evidence the AI-investment-cycle-then-normalization narrative may be playing out roughly as framed (a genuine improvement in confidence vs. the 07-07 session, where this was purely a management assertion made the same session as a guidance cut). However, the underlying shareholder-rights investigations into whether the 13 May 2026 disclosures were adequate remain **open and unresolved** (§1) — the same governance overhang the 07-07 session flagged. Given that overhang is still live, and the catalyst (FY2028 margin normalization) is still ~12–18 months out and still management-framed rather than independently confirmed, this session again applies the conservative "no clear catalyst" guardrail cap (upside side capped at −5) rather than crediting the improved-but-still-unconfirmed picture at full value.

```
Upside/Downside Modifier applied = −5.0   (uncapped alternative shown for transparency: −11.62)
```

### Final Valuation Score

```
Final Score = 33.68 (raw) + 10.0 (Rate Environment) + (−5.0) (Upside/Downside, capped)
            = 38.68 → 38.7

[Uncapped alternative, if the catalyst is judged solidly confirmed: 33.68 + 10.0 − 11.62 = 32.06 → 32.1]
```

**Valuation Score = 38.7** (uncapped alternative: 32.1) — both land in the **30.0–49.9 → BUY, Standard position 3–5%** band, a step up (more expensive/less-Buy) from the 2026-07-07 session's 25.8 (0.0–29.9 band). Drivers of the change: EV/EBIT rose on TTM-EBIT compression even as the multiple itself is only modestly higher; both Rate Environment steps now fire (vs. one in July); and the Upside/Downside gap compressed sharply (PW FV $25.95 vs. live $24.71 is only a 5% gap, vs. 27% in July) because the live price partially recovered while base-case FV barely moved.

---

## 5. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 82.5) + 0.50 × 38.7
                = 0.50 × 17.5 + 0.50 × 38.7
                = 8.75 + 19.35
                = 28.1

[Uncapped-modifier alternative: 0.50×17.5 + 0.50×32.1 = 8.75 + 16.05 = 24.8]
```

**Composite Score = 28.1** (uncapped alternative: 24.8) — both still land in the **0.0–29.9 → BUY, Full position 6–8%** band of the Phase 03 action table, per [valuation-scoring.md](../framework/valuation-scoring.md)'s instruction to score the Phase 03/05 action tables off the Composite, not the raw Valuation Score. The still-high Quality Score (82.5) keeps the blended number in the top band even though the standalone Valuation Score moved into the 30–49.9 band this session.

---

## 6. Fair Value & Order Setup — [fair-value-methodology.md](../framework/fair-value-methodology.md)

| Field | Value |
|---|---|
| Blended Fair Value (Base case) | $24.87 |
| PW Fair Value | $25.95 |
| Bull-Case Blended FV | $34.56 → Bull-Case Trim Target ($34.56×0.90) | $31.10 |
| Bear-Case Blended FV | $19.50 |
| MoS applied (Composite 0.0–29.9 band: 15–20%; used conservative 20%, same reasoning as 07-07 — open shareholder-rights investigation + confirmed margin-compression evidence) | 20% |
| **Buy Price (naive, MoS-based)** | $24.87 × 0.80 = **$19.90** |
| Live price | $24.71 (**above** the naive MoS-based buy price — no margin of safety currently available) |

### The R/R gate — why this is emphatically NOT "enter now"

```
Primary Sell Target = Base-case Blended FV = $24.87 (per fair-value-methodology.md Step 3)

If entered at live price ($24.71) with the tightest allowed stop for this band (20%):
  Stop Loss = $24.71 × 0.80 = $19.77
  R/R = ($24.87 − $24.71) / ($24.71 − $19.77) = $0.16 / $4.94 = 0.03:1   ← FAILS 2:1 minimum, badly
```

The gap between live price and the primary (base-case) sell target has compressed to almost nothing — $24.87 vs. $24.71 is only a 0.65% spread, essentially no room for the trade to work even before touching the R/R math. This is a far weaker entry setup than 2026-07-07, where the live price was already meaningfully below FV (1.34:1 R/R, close but failing) — here the stock has partially recovered off its lows while the fundamentals-driven fair value estimate has barely moved, closing nearly all the gap.

```
Solving for Entry E at R/R = 2.0, Sell Target = $24.87, Stop = E×0.80:
  (24.87 − E) / (E×0.20) = 2  →  E = 24.87 / 1.40 = $17.76

Limit set at $17.50 (small buffer below the $17.76 breakeven — notably, this sits just
$0.35 above DOCS's 52-week low of $17.155, effectively a "back to the lows" backstop bid
rather than a modest pullback entry):
  Stop Loss = $17.50 × 0.80 = $14.00
  R/R = ($24.87 − $17.50) / ($17.50 − $14.00) = $7.37 / $3.50 = 2.106:1  ✓ clears 2:1
```

### Order Setup Checklist

```
[x] Valuation Score (incl. Upside/Downside Mod): 38.7 (capped) / 32.1 (uncapped alt) — both in 30.0–49.9
[x] Composite Score:                          28.1 (capped) / 24.8 (uncapped alt) — both in 0.0–29.9
[x] Expected annual return E / catalyst window:  21.62% / 2yr
[x] Upside/Downside Modifier applied:            −5.0 (capped; −11.62 uncapped)
[x] DCF Fair Value (base case):               $29.27
[x] Multiples-Based Fair Value (base case):   $21.94
[x] Blended Fair Value (base case):           $24.87
[x] Margin of Safety %:                       20%
[ ] BUY PRICE (limit order):                  $17.50   ← NOT live price; R/R-gated (see above)
[x] PRIMARY SELL TARGET:                      $24.87
[x] BULL-CASE TRIM TARGET:                    $31.10
[x] STOP LOSS:                                $14.00
[x] Risk/Reward Ratio:                        2.106:1   (meets ≥ 2:1 minimum)
[x] Max $ Risk:                               $916.63  (portfolio ≈$61,108.83 × 1.5%)
[x] POSITION SIZE (shares):                   261
[x] POSITION SIZE ($):                        $4,567.50 (7.47% of portfolio)
[x] Thesis invalidation triggers:             see §7
```

**Portfolio value used:** $61,108.83 = live IBKR `get_pa_allocation` NAV ($50,218.87, 11 Sep 2026) + last-synced Freedom24 total ($10,889.96, unchanged since 2026-08-22 per [holdings.md](../portfolio/holdings.md) — not resynced this session, this evaluation is not a `/sync-portfolio` run).

Position sizing cross-check: Composite 0.0–29.9 band caps at 6–8% of portfolio. 7.47% sits inside that band and far under the hard 15% single-position cap (Upgrade 7) — no reduction needed.

---

## 7. Recommendation

# **SET LIMIT ORDER at $17.50 — NOT enter now**, despite a Composite Score (28.1) still in the "Buy, Full position" band.

DOCS again clears the 80.0+ Quality Score gate (82.5, though by a narrower margin than July's 84.4 — the AI-investment margin compression flagged in May has now shown up in a filed quarter's numbers, not just guidance) on the strength of the same dominant network-effect/switching-cost moat (85%+ US physician penetration) and pristine balance sheet (net cash, no leverage) as before. The Composite Score (28.1, or 24.8 uncapped) still sits deep in the "Buy, Full position" band because quality remains high even as the standalone valuation score has moved up a full band (25.8 → 38.7) since July.

**The entry setup itself is materially worse than in July, however.** The mandatory 2:1 Risk/Reward gate doesn't just narrowly fail at the live price — it fails almost completely (0.03:1), because the live price ($24.71) has partially recovered since May while the base-case fair value estimate ($24.87) has barely moved, leaving almost no gap between price and primary sell target. Solving for the entry price that restores a 2:1 R/R lands at $17.76 — essentially back at DOCS's 52-week low ($17.155) — a far larger required pullback (~29% from here) than July's ~10%. This is exactly the discipline the R/R check exists to enforce: a Composite Score deep in the Buy band is not, on its own, sufficient to enter; the entry price must leave enough room to a credible stop, and right now it doesn't.

**Qualitative flag carried forward, unresolved:** the open shareholder-rights investigations into whether Doximity's pre-13-May-2026 disclosures were adequate remain unresolved as of this session (distinct from the unrelated 2021–2023 case, which formally settled 11 Jun 2026). This is the reason the Upside/Downside Modifier's catalyst credit was again capped conservatively (−5.0 instead of the uncapped −11.62) rather than a reason to pass outright. If the investigation escalates into a filed complaint alleging a genuine disclosure failure, that would constitute a Full Exit-caliber "thesis broken" event under this framework's rules, independent of where the score sits.

**Next review trigger:** Q2 FY2027 earnings, 5 Nov 2026 (confirmed date, `yfinance` `get_earnings_dates`), OR a material update/resolution in the open shareholder-rights investigation, OR the $17.50 limit order filling, OR a >15% unexplained price move from here.

---

## 8. Qualitative Notes (5 Questions, per valuation-scoring.md) — unchanged reasoning from 2026-07-07, reconfirmed this session

1. **Why are margins high?** Near-zero marginal cost of serving an additional verified physician on an already-built network (88% gross margin TTM) — a genuine network/platform economics effect, not a temporary cyclical margin. Note the *operating* margin compression this session is a deliberate AI-investment choice layered on top of this structurally high gross margin, not evidence the underlying economics have changed.
2. **What would it take to compete?** Replicating NPI-verified physician identity plus 15+ years of accumulated network density (85%+ of US physicians) from scratch.
3. **Capital allocation (5–10yr):** No dividend; continued aggressive buybacks ($91.6M in Q1 FY2027 alone, per the 10-Q cash flow statement); no debt raised; AI R&D funded entirely from internal FCF.
4. **Growth sources, next 3–5 years:** AI product suite (Scribe, DoxGPT/Ask, Photon prescribing), allied-health expansion (NPs/PAs), and eventual recovery in the currently-soft HCP pharma-ad market — the Q1 FY2027 beat is early evidence some of this is already working, though management's own guide still implies a steep growth deceleration for the full year.
5. **Best bear case:** the AI-compute cost ramp keeps compressing GAAP margins faster than new AI products monetize (already visible in Q1 FY2027's net-income decline), the shareholder-rights investigation escalates into real litigation, and pharma/digital-ad demand stays structurally soft for longer than management's "one investment year" framing suggests.
6. **Disruption vector check:** unchanged — an EHR vendor or consumer-AI platform building native physician-facing AI tools remains a real but distant risk given how embedded the multi-year workflow build-out is in physicians' daily routine.

---

## 9. Files touched this session

- `sessions/2026-09-11-new-position-docs.md` — this file
- `watchlist/not-in-portfolio/DOCS/DOCS-2026-09-11.md` — new dated entry (score and Rule 9 trigger both changed since 2026-07-07)
- No `framework/glossary.md` additions — every jargon term used this session is already defined there
- No `decisions/` entry — no position opened, only a limit-order recommendation for the human investor to place (or not) directly in TWS/Client Portal

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session: 10-K, 10-Q, 8-K, Adjusted EBITDA, Beta, Buyback yield (net buyback yield), CAGR, Composite Score, DCF, EBIT, EBITDA, Equity Risk Premium (ERP), EV, EV/EBIT, EV/EBITDA, EY (Earnings Yield), Fast Grower, FCF, FCF Yield, FCF/NI conversion ratio, Forward PE, FV (Fair Value), Going-concern/accounting-integrity allegation, Gross Margin, Hard disqualifier, Hurdle rate, Invested Capital, IRR, Moat, MoS (Margin of Safety), Net Debt/EBITDA, Net Margin, NOPAT, NPI (National Provider Identifier), PE ratio, PEG ratio, Effective tax rate, PT (Price Target), PW (Probability-Weighted) Fair Value, Quality Score, Rate Environment Gate, Rate Regime Modifier, ROIC, R/R (Risk/Reward ratio), Rule 0, Rule 9, SBC (Stock-Based Compensation), Securities class action / shareholder-rights investigation, Shareholder yield, TAM, Terminal Value, Treasury yield (10Y), TTM, Upside/Downside Modifier, Valuation score, WACC.
