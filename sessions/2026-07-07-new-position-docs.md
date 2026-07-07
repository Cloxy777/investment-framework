# NEW POSITION — DOCS (Doximity, Inc.) — 2026-07-07

**Task type:** NEW POSITION
**Date:** 7 Jul 2026
**Ticker:** DOCS (Doximity, Inc. — Class A common stock, NYSE)
**Sector:** Healthcare Information Services / Digital Health SaaS
**10Y US Treasury yield:** 4.49% (TradingEconomics, 7 Jul 2026 session)
**Current DOCS portfolio weight:** 0% — not held, not on [holdings.md](../portfolio/holdings.md)

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$22.87** | IBKR `get_price_snapshot`, contract_id 498661844 (NYSE), intraday snapshot, `ts` 1783406405, `is_close: false` |
| Bid / Ask | $21.70 / $23.00 | Same snapshot |
| Prior close | $22.86 | Same snapshot |
| 52-week range | $17.155 – $76.50 | IBKR `misc_statistics` |
| 13-week range | $17.155 – $26.67 | IBKR `misc_statistics` |
| Cross-check | $21.86 (2 Jul), $21.59 close (1 Jul) | WebSearch, Yahoo Finance / stockanalysis.com |
| Analyst consensus PT | Mean $24.37, median $24.00 (19–22 analysts), consensus "Buy" | yfinance `targetMeanPrice`; stockanalysis.com |
| Analyst PT range | $18.00 – $42.00 | yfinance `targetLowPrice`/`targetHighPrice` |

**Why the price collapsed (Rule 9 context — mandatory before scoring):** DOCS is down ~70% from its 52-week high. On its 13 May 2026 Q4/FY2026 earnings release, Doximity paired a slight EPS miss with FY2027 revenue guidance ($664–676M) meaningfully below the ~$699M Street consensus, and management flagged that ramping AI-compute investment will "weigh on near-term margins" while the HCP (healthcare-professional) digital-pharma-ad market stays soft (management's own words: overall market growth "modest, likely at or below 5%"). Shares fell ~23–26% that session and have continued grinding lower since (further ~35% premarket slide in early March on brokerage downgrades/guidance, per a separate report). This is a genuine, documented Rule 9 fundamental trigger (guidance revision), not an unexplained price move — proceeding to scoring is appropriate, but the deceleration is folded into Growth_Score below rather than ignored.

**Governance flag (not itself scored, tracked as an open risk):** Multiple law firms (Schall Law Firm, Pomerantz LLP, Halper Sadeh LLC) opened shareholder-rights/securities-class-action investigations in mid-2026 into whether Doximity adequately disclosed AI-cost margin pressure ahead of the 13 May guidance miss. This is an **open, unresolved allegation** — treated per this framework's convention for going-concern/accounting-integrity allegations: a risk to monitor, not a settled fact in either direction (see glossary). It is not a hard disqualifier and does not appear in any sub-score directly, but it materially informs the discretionary catalyst-confidence call in §5 below.

---

## 2. Quality Score (Phase 01) — [quality-scoring.md](../framework/quality-scoring.md), methodology version 2026-06-29

### Hard disqualifiers — checked first, none fire

| Disqualifier | Result |
|---|---|
| FCF/NI conversion <70% for 2+ consecutive years | **No** — 166.5% (FY2026), 122.4% (FY2025), both far above 70% |
| Net Debt/EBITDA over threshold | **No** — net **cash** position (no net debt at all) |
| Not FCF-positive for 3+ consecutive years | **No** — FCF positive every year FY2022–FY2026 (5 straight years) |

### Inputs (all sourced — none invented)

| Metric | Value | Source |
|---|---|---|
| Net Margin (FY2026) | 30.40% | stockanalysis.com financials (10-K/8-K sourced) |
| Gross Margin (FY2026) | 89.09% (87.24–90.20% range FY2023–FY2026, essentially flat/high) | stockanalysis.com |
| Revenue (FY2023 → FY2026) | $419.05M → $644.86M | stockanalysis.com |
| EBIT (FY2026) | $214.92M | stockanalysis.com |
| Effective tax rate (FY2026) | 21.58% ($53.95M tax / $250.01M pretax) | stockanalysis.com |
| Total Debt | $10.19M | yfinance `totalDebt` |
| Total Cash + ST investments | $748.60M | yfinance `totalCash` |
| Total Shareholders' Equity | $950.84M | stockanalysis.com balance sheet |
| FCF (FY2026 / FY2025) | $326.46M / $273.27M | stockanalysis.com cash flow statement |
| Net Income (FY2026 / FY2025) | $196.05M / $223.19M | stockanalysis.com |
| Market share | ~85% of US physicians on the network (up from 70% historically) | Doximity press releases (press.doximity.com), cross-checked via WebSearch |

### Profitability (25% weight)

```
NetMargin_Component = clamp((30.40/30)×100, 0, 100) = 100.0   (clamped — 30.40% ≥ 30%)

ROIC calculation (NOPAT ÷ Invested Capital, per this framework's glossary convention —
Invested Capital = Total Debt + Equity − Cash):
  NOPAT = EBIT × (1 − tax rate) = $214.92M × (1 − 0.2158) = $168.53M
  Invested Capital = $10.19M + $950.84M − $748.60M = $212.43M
  ROIC = $168.53M / $212.43M = 79.34%
ROIC_Component = clamp((79.34/30)×100, 0, 100) = 100.0   (clamped — well above the 30% ceiling)

  Sensitivity check (netting only "cash & equivalents" $219.18M, excluding short-term
  investments): Invested Capital = $741.85M → ROIC = 22.72% → component 75.7 (not clamped).
  Flagged: this framework's Invested Capital convention (net ALL cash, matching how
  Net Debt/EBITDA already nets cash) supports the primary (clamped) reading, but the
  gap between methodologies is real and worth carrying forward — third-party sources
  disagree just as widely (GuruFocus 67.6%, other aggregators 15–19% using a
  non-excess-cash-adjusted denominator).

Profitability_Score = (100.0 + 100.0) / 2 = 100.0   (no FCF cap — 5yr FCF-positive)
```

### Margins (15% weight)

```
GrossMargin_Score = clamp((89.09/80)×100, 0, 100) = 100.0   (clamped)
```
Gross margin has run 87–90% for 5 straight years — already at the ceiling; no separate trend bonus needed (would be clamped regardless).

### Growth (20% weight)

```
Revenue 3yr CAGR = (644.86/419.05)^(1/3) − 1 = 15.45%
Growth_Score (raw) = clamp((15.45/25)×100, 0, 100) = 61.8

Structural deceleration modifier: −10
```
Evidence (cited, not inferred): revenue growth has decelerated every year — 66.05% (FY2022) → 19.98% (FY2025) → 13.05% (FY2026) → guided ~3–4.8% for FY2027 ($664–676M vs. $644.86M). Management's own framing on the 13 May call — HCP digital-pharma-ad demand "soft," overall market growth "modest, likely at or below 5%" — is a documented, company-sourced statement about structural (not one-quarter/cyclical) demand softening, satisfying the "documented evidence" bar this modifier requires.

```
Growth_Score = 61.8 − 10 = 51.8
```

### Balance Sheet (15% weight)

```
Net Debt = Total Debt − Total Cash&STI = $10.19M − $748.60M = −$738.42M (net CASH position)
Net Debt/EBITDA = negative (net cash) → clamp(100×(1 − ratio/4), 0, 100) = 100.0
```

### Moat Signal (15% weight) — 3 of 5 TRUE, each with cited evidence

| Signal | Result | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Doximity press releases: reached >70% of US physicians (historical), now cited at ~85% of US physicians + two-thirds of NPs/PAs, "larger membership than the American Medical Association" (press.doximity.com, cross-checked via WebSearch) |
| Network effect | **TRUE** | Documented two-sided mechanism: 85%+ physician penetration makes Doximity the platform connecting pharma/health-system advertisers to the doctors who "decide over 70% of healthcare spending" — cited as "nearly unassailable" at this penetration level |
| Switching costs | **TRUE** | Documented mechanism: sequential product build-out (identity/network → Dialer/messaging/fax → drug reference → Scribe documentation → DoxGPT/Ask → telehealth → Photon prescribing) embeds multiple interconnected daily-workflow tools in one platform — each layer raises the cost of leaving, per company/press descriptions of the strategy |
| Brand premium (pricing power) | **FALSE** | No cited evidence of price increases without volume loss found this session |
| Scale cost advantage | **FALSE** | No cost-per-unit data vs. smaller competitors found this session |

```
Moat_Score = (3/5) × 100 = 60.0
```

### FCF Quality (10% weight)

```
FCF/NI ratio (FY2026) = 326.46/196.05 = 166.5%
FCFQuality_Score = clamp(((1.665 − 0.40)/0.60)×100, 0, 100) = 100.0   (clamped)
```
2-year check: FY2025 ratio 273.27/223.19 = 122.4% — both years far above the 70% hard-disqualifier threshold (elevated by heavy stock-based comp add-backs typical of asset-light SaaS, not a red flag on its own).

### Quality Score total

```
Quality Score = 100.0×0.25 + 100.0×0.15 + 51.8×0.20 + 100.0×0.15 + 60.0×0.15 + 100.0×0.10
              = 25.0 + 15.0 + 10.36 + 15.0 + 9.0 + 10.0
              = 84.36 → 84.4
```

**84.4 ≥ 80.0 — clears the gate.** Note the sensitivity: if the conservative (non-clamped) ROIC reading is used instead (Profitability_Score 87.9 instead of 100.0), Quality Score would be **81.3** — still clears, but the margin is genuinely sensitive to this one methodology choice, flagged rather than silently resolved. Either way, **DOCS clears the 80.0+ Quality Score gate** and proceeds to Phase 02.

---

## 3. Rate Environment Gate

**Step 1 — Earnings Yield Spread Test:**
```
Forward PE (yfinance) = 14.34
EY = 1/14.34 = 6.975%
Spread = 6.975% − 4.49% = +2.485%  ≥ +1.5% → PASS, no additive adjustment
```

**Step 2 — Rate Regime Modifier:** 10Y = 4.49% → 3.5–5% bracket → **+5** (applied to valuation score below)

---

## 4. Valuation Score (Phase 02) — [valuation-scoring.md](../framework/valuation-scoring.md), methodology version 2026-06-29

### Fast-Grower eligibility (PEG) — does not qualify

EPS/revenue growth is **decelerating** (66%→20%→13%→~3–5% guided), not sustaining >15%/yr for 3+ years on a clean base. **PEG not applicable — its 15% weight redistributed to EV/EBIT (→ 40%)**, per the Final Score Formula note.

### FCF Yield (40% weight)

```
FCF Yield = FCF (FY2026, filed) / Market Cap = $326.46M / $4,180.46M = 7.807%
FCF_Score = clamp(100×(1 − 7.807/10), 0, 100) = 21.9
```
(Flag: yfinance's own cached TTM `freeCashflow` field showed $255.26M — a stale/lagged read inconsistent with the filed FY2026 figure. Used the filed, 10-K/8-K-sourced FCF as the primary input per Rule 0's "never infer/never use stale data" spirit.)

### EV/EBIT (40% weight, redistributed)

```
EV (yfinance, live) = $3,442.04M
EBIT (FY2026, filed) = $214.92M
EV/EBIT = 16.02×
EV/EBIT_Score = clamp((16.02 − 12)/23 × 100, 0, 100) = 17.5
```

### Forward PE (20% weight) — no-history fallback

Attempted the framework's standard 5yr-PE-range reconstruction (`get_earnings_dates` → rolling TTM EPS → paired price history, per valuation-scoring.md's automated method). Result: only **17 of the required 20 quarters** reconstructable (Doximity IPO'd June 2021 — insufficient trading history exists for a full 5-year/20-quarter window; not a data-access failure).

```
FwdPE_Score = 50.0  (neutral, flagged — no-history fallback per framework's explicit <20-quarter rule)
```

### Final Score (raw, before modifiers)

```
Final Score (raw) = FCF_Score×0.40 + EV/EBIT_Score×0.40 + FwdPE_Score×0.20
                   = 21.9×0.40 + 17.5×0.40 + 50.0×0.20
                   = 8.76 + 7.00 + 10.0
                   = 25.76
```

### Rate Regime Modifier: **+5** (from §3)

### Upside/Downside Modifier — full calc shown

**Step 1 — Fair Value (bull/base/bear), via the two required methods (Rule 1: DCF + Multiples):**

*Method A — 3-stage DCF* (Rule 2: yrs 1–5 explicit, yrs 6–10 fade, yr 10+ terminal at 2.5% — GDP-capped per Rule 2). Base year FCF = $326.46M (FY2026, filed). Yr-1 FCF anchored to FY2027 adjusted-EBITDA guidance ($323–335M, vs. FY2026's $357.8M) at scenario-varied FCF-conversion assumptions; yrs 2–5 growth and WACC varied ±1–2pp per scenario per Rule 2/7:

| Scenario | Yr-1 FCF (Δ vs FY26) | Yrs 2–5 growth | WACC | DCF FV/share |
|---|---|---|---|---|
| Bear | $274.6M (−15.9%, 85% conversion of $323M low-end guide) | 3%/yr, fade to 2.5% | 12% | $20.18 |
| Base | $300.0M (−8.1%, ~91% conversion of $329M midpoint guide) | 8%/yr, fade to 2.5% | 11% | $28.66 |
| Bull | $318.3M (−2.5%, 95% conversion of $335M high-end guide) | 15%/yr, fade to 2.5% | 10% | $44.91 |

WACC built from: risk-free 4.49% (10Y, live) + beta 1.293 (yfinance) × 5% assumed equity risk premium = 10.955% cost of equity ≈ WACC (net-cash balance sheet, negligible debt weight); varied ±1pp per scenario per Rule 2.

*Method B — Peer multiples* (Rule 5: 5–10 peers, similar business model, median not mean, EV-based). Peer set: VEEV, CERT, PHR, HSTM (EV/EBITDA 23.4×, 13.4×, 21.4×, 18.9×); **DH and HCAT excluded as outliers** (EV/EBITDA 3.4× and 267.6× respectively — clearly distressed/distorted, per Rule 5's "trim outliers"). Applied to DOCS's TTM EBITDA ($228.79M, yfinance, GAAP-consistent with peer figures — not Doximity's own non-GAAP "adjusted EBITDA," to avoid mixing methodologies):

| Scenario | Peer EV/EBITDA used | Implied EV | + Net Cash $738.42M | ÷ 182.87M shares | Multiples FV/share |
|---|---|---|---|---|---|
| Bear | 13.4× (peer low) | $3,066.0M | $3,804.4M | | $20.80 |
| Base | 20.1× (median of 4) | $4,598.7M | $5,337.1M | | $29.18 |
| Bull | 23.4× (peer high) | $5,353.7M | $6,092.1M | | $33.31 |

**Triangulation (Rule 3-style weighting, per fair-value-methodology.md Step 1: 40% DCF + 60% Multiples):**

```
Bear:  0.40×$20.18 + 0.60×$20.80 = $20.55
Base:  0.40×$28.66 + 0.60×$29.18 = $28.97
Bull:  0.40×$44.91 + 0.60×$33.31 = $37.95
```

**PW Fair Value (Rule 7):**
```
PW Fair Value = 0.25×$37.95 + 0.50×$28.97 + 0.25×$20.55 = $29.11
```
Sanity check (Rule 4): PW FV $29.11 sits inside the analyst PT range ($18–$42, mean $24.37) — a bit above consensus mean but well within the distribution, not an outlier call.

**Step 2 — Expected annual return `E`:**

```
Gap Upside% = ($29.11 / $22.87) − 1 = +27.28%
Catalyst window = 2 years (default — see guardrail discussion below)
Annualized gap = 27.28% / 2 = 13.64%
Intrinsic growth = 6.33%/yr (analyst 3yr EPS growth consensus, stockanalysis.com — used
                   in preference to a self-generated DCF growth assumption, per "never invent")
Shareholder yield = 0% dividend + 3.08% net buyback
  (net buyback: shares outstanding fell 188.88M → 183.06M FY2025→FY2026, i.e. −3.08%,
   against $431.65M gross FY2026 repurchases per yfinance cash-flow statement — netted
   for SBC-driven share issuance, not the gross buyback-dollar/market-cap ratio)

E = 13.64% + 6.33% + 3.08% = 23.05%
```

**Step 3 — Map to modifier, with the catalyst guardrail:**

```
E (23.05%) ≥ H (10%) → M (uncapped) = −15 × clamp((23.05−10)/15, 0, 1) = −15 × 0.870 = −13.05
```

**Guardrail applied — capped at −5.0.** Rule 10 requires a documented catalyst + timeline before crediting large upside. Management has framed FY2027 as a one-year "AI investment" cycle implying FY2028 normalization (~12–24 months out) — a plausible but *management-stated, not independently verified* catalyst. Given the open securities-fraud/shareholder-rights investigations (§1) center specifically on whether management's own forward disclosures were adequate, this session treats that catalyst as **not solidly/independently confirmed** and applies the "no clear catalyst" conservative cap per the guardrail (upside side capped at −5), rather than crediting the full −13.05.

```
Upside/Downside Modifier applied = −5.0   (uncapped alternative shown for transparency: −13.05)
```

### Final Valuation Score

```
Final Score = 25.76 (raw) + 5.0 (Rate Regime) + (−5.0) (Upside/Downside, capped)
            = 25.76
Rounded: 25.8

[Uncapped alternative, if the catalyst is judged solidly confirmed: 25.76 + 5.0 − 13.05 = 17.7]
```

**Valuation Score = 25.8** (0.0–29.9 band either way).

---

## 5. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 84.4) + 0.50 × 25.8
                = 0.50 × 15.6 + 0.50 × 25.8
                = 7.8 + 12.9
                = 20.7

[Uncapped-modifier alternative: 0.50×15.6 + 0.50×17.7 = 7.8+8.85 = 16.65 → 16.7]
```

**Composite Score = 20.7** (uncapped alternative: 16.7) — both land firmly in the **0.0–29.9 → BUY, Full position 6–8%** band of the Phase 03 action table.

---

## 6. Fair Value & Order Setup — [fair-value-methodology.md](../framework/fair-value-methodology.md)

| Field | Value |
|---|---|
| Blended Fair Value (Base case) | $28.97 |
| PW Fair Value | $29.11 |
| Bull-Case Blended FV | $37.95 → Bull-Case Trim Target ($37.95×0.90) | $34.16 |
| Bear-Case Blended FV | $20.55 |
| MoS applied (Composite 0.0–29.9 band: 15–20%; used conservative 20% given open litigation/deceleration flags) | 20% |
| **Buy Price (naive, MoS-based)** | $28.97 × 0.80 = **$23.18** |
| Live price | $22.87 (already below the MoS-based buy price) |

### The R/R gate — the reason this is NOT "enter now"

```
If entered at live price ($22.87) with the tightest allowed stop for this band (20%):
  Stop Loss = $22.87 × 0.80 = $18.30
  R/R = ($28.97 − $22.87) / ($22.87 − $18.30) = $6.10 / $4.57 = 1.34:1   ← FAILS 2:1 minimum
```

Even at the tightest permitted stop, entering at the current live price does not clear the framework's mandatory 2:1 Risk/Reward floor. Per the explicit rule ("Below 2:1 = do not enter... wait for lower entry, find tighter stop, or pass entirely") and since the stop can't legally tighten further inside this score band, the fix is a **lower entry via limit order**, not entering now.

```
Solving for Entry E at R/R = 2.0, Sell Target = $28.97, Stop = E×0.80:
  (28.97 − E) / (E×0.20) = 2  →  E = 28.97 / 1.40 = $20.69

Limit set at $20.50 (small buffer below the $20.69 breakeven):
  Stop Loss = $20.50 × 0.80 = $16.40
  R/R = ($28.97 − $20.50) / ($20.50 − $16.40) = $8.47 / $4.10 = 2.07:1  ✓ clears 2:1
```

### Order Setup Checklist

```
[x] Valuation Score (incl. Upside/Downside Mod): 25.8 (capped) / 17.7 (uncapped alt) — both ≤ 29.9
[x] Expected annual return E / catalyst window:  23.05% / 2yr
[x] Upside/Downside Modifier applied:            −5.0 (capped; −13.05 uncapped)
[x] DCF Fair Value (base case):               $28.66
[x] Multiples-Based Fair Value (base case):   $29.18
[x] Blended Fair Value (base case):           $28.97
[x] Margin of Safety %:                       20%
[ ] BUY PRICE (limit order):                  $20.50   ← NOT live price; R/R-gated (see above)
[x] PRIMARY SELL TARGET:                      $28.97
[x] BULL-CASE TRIM TARGET:                    $34.16
[x] STOP LOSS:                                $16.40
[x] Risk/Reward Ratio:                        2.07:1   (meets ≥ 2:1 minimum)
[x] Max $ Risk:                               $873.39  (portfolio $58,226.21 × 1.5%)
[x] POSITION SIZE (shares):                   213
[x] POSITION SIZE ($):                        $4,366.50 (7.50% of portfolio)
[x] Thesis invalidation triggers:             see §7
```

Position sizing cross-check: Composite 0.0–29.9 band caps at 6–8% of portfolio. 7.50% sits inside that band and far under the hard 15% single-position cap (Upgrade 7) — no reduction needed.

---

## 7. Recommendation

# **SET LIMIT ORDER at $20.50 — NOT enter now, despite a Composite Score (20.7) deep in the "Buy, Full position" band.**

DOCS clears the 80.0+ Quality Score gate (84.4) on the strength of a dominant, well-evidenced network-effect/switching-cost moat (85% US physician penetration), a genuinely excellent balance sheet (net cash, no leverage), and strong cash-conversion — even after a full −10 penalty for the documented, management-guided structural growth deceleration. The Composite Score (20.7, or 16.7 under the uncapped-modifier alternative) reflects both that quality and a sharp, guidance-driven ~70% price collapse that leaves the stock statistically very cheap even under conservative bear-case assumptions.

**The catch: the mandatory 2:1 Risk/Reward gate fails at the current live price** ($22.87 → only 1.34:1 even at the tightest permitted stop), because the sell target (base-case blended FV $28.97) isn't far enough above the price to clear 2:1 against a 20% stop. This is exactly the discipline this framework's R/R check exists to enforce — a deep-value score alone isn't sufficient to enter; the entry price must also leave enough room to the stop. A ~10% further pullback to $20.50 (limit order, not a market order) restores a 2.07:1 R/R.

**Qualitative flag carried forward, not scored:** the open securities-fraud/shareholder-rights investigations into Doximity's pre-guidance disclosures are unresolved. They are the reason this session capped the Upside/Downside Modifier's catalyst credit conservatively (−5.0 instead of the uncapped −13.05) rather than a reason to pass outright — but if those investigations later surface a genuine disclosure failure (as opposed to remaining unsubstantiated solicitations), that would constitute a Full Exit-caliber "thesis broken" event under this framework's rules, independent of where the score sits. Monitor, don't ignore.

**Next review trigger:** Q1 FY2027 earnings (date not yet confirmed by this session — flagged as a gap; expected within the typical Aug–Sep reporting window based on FY2026's mid-May report date), OR a material update/resolution in the securities litigation, OR the $20.50 limit order filling, OR a >15% unexplained price move from here.

---

## 8. Qualitative Notes (5 Questions, per valuation-scoring.md)

1. **Why are margins high?** Near-zero marginal cost of serving an additional verified physician on an already-built network (89% gross margin, 5 years running) — a genuine network/platform economics effect, not a temporary cyclical margin.
2. **What would it take to compete?** Replicating NPI-verified physician identity plus 15+ years of accumulated network density (85% of US physicians) from scratch — LinkedIn is cited as the nearest analog but lacks the verification layer that makes referrals/credentialing usable.
3. **Capital allocation (5–10yr):** No dividend; aggressive buybacks ($431.65M gross in FY2026 alone, net share count down 3.08%); no debt raised; AI R&D funded entirely from internal FCF. No obviously wasteful M&A found this session.
4. **Growth sources, next 3–5 years:** AI product suite (Scribe documentation, DoxGPT/Ask, Photon prescribing), allied-health expansion (NPs/PAs), and eventual recovery in the currently-soft HCP pharma-ad market.
5. **Best bear case:** Pharma/digital-ad demand stays structurally soft for longer than management's "one investment year" framing suggests, AI-compute costs keep compressing margins faster than new AI products monetize, and the open securities-litigation overhang either uncovers a real disclosure problem or simply drags on as a multi-quarter distraction — while AI-native competitors chip into physician engagement time that Doximity currently owns.
6. **Disruption vector check:** Could an EHR vendor (e.g. Epic) or a consumer-AI platform build native physician-facing AI tools that bypass Doximity's network entirely? A real but distant risk given how deeply the multi-year workflow build-out (Dialer → Scribe → Ask → Photon) is embedded in physicians' daily routine (Moat Signal 3).

---

## 9. Files touched this session

- `sessions/2026-07-07-new-position-docs.md` — this file
- `watchlist/not-in-portfolio/DOCS/DOCS-2026-07-07.md` — new file (first-ever DOCS entry)
- `framework/glossary.md` — added "Securities class action / shareholder-rights investigation"
- No `decisions/` entry — no position opened, only a limit-order recommendation for the human investor to place (or not) directly in TWS/Client Portal

---

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session: 10-K, 8-K, Beta, Buyback yield (net buyback yield), CAGR, Composite Score, DCF, EBIT, EBITDA, Equity Risk Premium (ERP), EV, EV/EBIT, EV/EBITDA, EY (Earnings Yield), Fast Grower, FCF, FCF Yield, FCF/NI conversion ratio, Forward PE, FV (Fair Value), Going-concern/accounting-integrity allegation, Gross Margin, Hard disqualifier, Hurdle rate, Invested Capital, IRR, Moat, MoS (Margin of Safety), Net Debt/EBITDA, Net Margin, NOPAT, NPI (National Provider Identifier), PE ratio, PEG ratio, Effective tax rate, PT (Price Target), PW (Probability-Weighted) Fair Value, Quality Score, Rate Environment Gate, Rate Regime Modifier, ROE, ROIC, R/R (Risk/Reward ratio), Rule 0, Rule 9, SBC (Stock-Based Compensation), Securities class action / shareholder-rights investigation, Shareholder yield, TAM, Terminal Value, Treasury yield (10Y), TTM, Upside/Downside Modifier, Valuation score, WACC.
