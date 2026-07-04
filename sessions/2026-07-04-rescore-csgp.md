# RESCORE — CSGP (CoStar Group, Inc.)

**Mode:** `--both` (Quality Score + Valuation Score + Composite Score — first-ever Quality Score / Composite Score computation for CSGP)

> *Jargon decoded on first use (non-finance reader, per operating-brief.md): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EBITDA = operating profit before depreciation & amortization; EV/EBIT, EV/EBITDA = enterprise value ÷ operating profit (or ÷ EBITDA); PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; D&A = depreciation & amortization; capex = capital expenditure; opex = operating expense; Owner Earnings = net income + D&A − maintenance capex; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ forward PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; Invested Capital = total debt + shareholders' equity (the capital base ROIC is measured against); TAM = total addressable market; TTM = trailing twelve months; NI = net income.*

---

## 1. Session header

- **Task type:** RESCORE (single ticker, held position)
- **Date:** 2026-07-04
- **10Y US Treasury yield:** **4.485%** (source: `yfinance` `^TNX`, last close 2026-07-02 — the most recent trading day; the bond market was closed 2026-07-03, observed Independence Day holiday, and 2026-07-04, a Saturday)
- **Rate Regime Modifier in effect:** **+5** (10Y in the 3.5–5% band — "capital has a real cost")
- **Sector:** Real Estate — commercial real estate data, analytics & marketplaces (CoStar Suite, LoopNet, Apartments.com) plus the residential build-out (Homes.com, Domain). Treated as Technology/Growth-style for fair-value method (EV/EBIT multiples + scenario DCF) per Rule 1, given the software-like ~79% gross margin — unchanged reasoning from the 2026-06-20 session.

### Live price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price used** | **$30.00** | IBKR `get_price_snapshot` (contract_id 6726677) `plprice` (mark price) field, cross-verified against `yfinance`'s independently-sourced `regularMarketPrice` ($30.00) |
| 52-week range | **$28.18 – $97.43** | IBKR `misc_statistics` and `yfinance` `fiftyTwoWeekLow/High` (agree exactly) |
| Analyst consensus PT | mean **$47.50**, median $47.00, n=20 (`yfinance`) | Sanity anchor only, never a score input |

**Data-quality flag (Rule 0 diligence):** IBKR's `get_price_snapshot` returned **two internally inconsistent fields** for CSGP: `last.price = $29.36` (explicitly flagged `is_close: true`) and `plprice` (mark price) `= $30.00`. Both are stale-market-holiday reads (equity markets closed 2026-07-03 and 2026-07-04), so this is not a live intraday discrepancy — but the two fields disagree on what the most recent actual close was. Resolved by cross-check: `yfinance`'s independently-scraped quote shows `regularMarketPrice = $30.00` with `previousClose = $29.36`, and the reported `marketCap` ($12,250,671,104) ties out almost exactly to $30.00 × 408,355,715 shares (**$12,250,671,450**) — it does **not** tie out to $29.36 (which implies ~$11.99B). This confirms **$30.00 is the correct, most recent close** (Thursday 2026-07-02) and IBKR's `last` field is carrying forward the prior session's close ($29.36, Wednesday 2026-07-01) under its `is_close` flag. **$30.00 used throughout this session**, sourced from IBKR (as instructed) and cross-verified against an independent vendor — not invented, not inferred from multiples.

---

## 2. Data gaps flagged

- **Trailing EV/EBIT is still undefined.** TTM EBIT (four quarters ending Q1 FY2026) = **−$26.2M** — still an operating loss, though a smaller one than FY2025's full-year −$72M as Q1 FY2026 alone was EBIT-positive (+$3M). EV/EBITDA is substituted as a flagged proxy, same as the 2026-06-20 session.
- **No clean 5-year PE history — re-verified fresh, not carried forward blind.** Reconstructed the TTM-EPS-based PE series again this session (20 quarters, `get_earnings_dates`): avg PE **72.4×**, range **36.3×–113.8×** — materially unchanged from the 2026-06-20 figures (72.4×, 36.3–113.8×), confirming the earnings base is still too distorted by the 2023–2025 EPS collapse-and-recovery to serve as a usable historical-PE benchmark. Forward PE sub-score uses the **50.0 neutral fallback (flagged)**, per the distorted-base rule.
- **Owner Earnings (Upgrade 1) still does not rescue the FCF sub-score.** Growth capex remains >30% of total capex (FY2025: capex $389M, maintenance proxy = D&A $263M → growth capex $126M = 32.4%), which triggers Upgrade 1's test — but Owner Earnings = TTM NI ($24.8M) + D&A − maintenance capex (D&A) = **$24.8M**, an Owner Earnings *yield* of 0.20% — *worse* than the reported FCF yield of 1.65%. Confirms the 2026-06-20 finding: the earnings depression is driven by **growth operating expense** (Homes.com sales & marketing, expensed through the income statement), not capitalized growth capex, so Owner Earnings' capex-only add-back does nothing here. Reported FCF remains the honest input.
- **FCF/NI conversion ratio (TTM) is a denominator-distortion artifact, not a genuine quality signal.** TTM FCF $202.2M ÷ TTM NI $24.8M = **815%**, which clamps the FCF Quality sub-score to 100.0 — but this is an artifact of a near-zero TTM net income base, not evidence of durably excellent cash conversion. Flagged explicitly; shown in full below.
- **ROIC required a normalization judgment call (Rule 6), not an invented number.** TTM pretax income ($48.7M) and TTM tax provision ($23.9M) imply a TTM effective tax rate of **49.1%** — itself distorted by the same near-zero-earnings-base problem (a swing quarter with negative pretax income and positive tax provision skews the ratio). Per Rule 6 ("normalize before you value... use a clean, non-distorted period's effective tax rate"), NOPAT is computed using the **average of FY2022 (24.05%) and FY2023 (25.30%) effective tax rates ≈ 24.7%** — the last two years before the Homes.com-driven earnings distortion began. **This choice is immaterial to the final score**: TTM EBIT is negative (−$26.2M), so NOPAT is negative under *either* the normalized 24.7% rate or the raw distorted 49.1% rate, and the Profitability sub-score's ROIC component clamps to 0.0 either way — shown for transparency, not because the choice changes the outcome.
- **Balance sheet: net-cash cushion has shrunk sharply since the last review**, not a data gap but a real, flagged change: FY2025-end net cash was +$449M (cash $1.633B − debt $1.184B); as of the most recent balance sheet (Q1 FY2026, 2026-03-31), net cash is **+$25M** (cash & ST investments $1.215B − debt $1.190B). The drop is consistent with the ongoing **$700M 2026 share buyback** consuming cash, not a new liability or covenant issue. Still net cash (no leverage concern), but the cushion is now thin — worth watching if buyback pace continues.
- **No Rule 9 trigger since the 2026-06-20 review.** Checked explicitly: no new earnings release (next earnings is **2026-07-28**, confirmed via `yfinance` calendar and CoStar's own press release), no guidance revision (April 2026's raised FY2026 adjusted EBITDA guide of $780–820M is unchanged through today — confirmed via SeekingAlpha/StreetInsider coverage of the Q1 2026 print), no management change, no M&A, and price moved from $30.12 (06-20) to $30.00 (today) — a **−0.4%** move, nowhere near the 15% threshold. The Third Point/D.E. Shaw activist campaign that had pressured CoStar over Homes.com resolved in **April 2026** (Third Point exited its stake) — before, not during, this review window; noted for context only, not a new trigger.

---

## 3. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** EY = 1 ÷ Forward PE = 1 ÷ 16.7076 = **5.985%**. Spread = 5.985% − 4.485% (10Y) = **+1.500%**, which is **≥ +1.5% → PASS, no additive flag** (a razor-thin pass — down from +1.52% on 2026-06-20 as the 10Y yield rose 3.4bps while forward PE ticked down slightly; flagged as a boundary case worth re-checking next quarter).
- **Step 2 — Rate Regime Modifier:** 10Y 4.485% sits in the 3.5–5% band → **+5**.
- **Combined Gate additive: +5** (Step 2 only).

---

## 4. Quality Score (first computation for CSGP)

CSGP has never been scored under the Quality Score / Composite Score methodology added 2026-06-29 — its `holdings.md` row shows `?` for both columns. This is its first pass.

### Standard inputs (TTM unless noted; `yfinance` financial statements + `info`, fetched fresh this session)

| Metric | Value | Source / calc |
|---|---|---|
| Net Margin (TTM) | **0.727%** | TTM NI $24.8M ÷ TTM Revenue $3,411.8M |
| ROIC (TTM, normalized tax rate) | **≈ −0.22%** | NOPAT = TTM EBIT (−$26.2M) × (1 − 24.7% normalized rate) = −$19.7M; ÷ Invested Capital (Q1 FY2026, $8,907M) |
| Gross Margin (TTM) | **78.6%** | TTM Gross Profit $2,683.1M ÷ TTM Revenue $3,411.8M |
| Gross margin trend | Mildly declining (81.0% FY22 → 80.0% FY23 → 79.6% FY24 → 78.9% FY25) | `yfinance` annual financials — not a "structural expansion," but immaterial since already far above the 40% threshold |
| Revenue 3yr CAGR | **14.16%** | ($3,247M FY25 ÷ $2,182.4M FY22)^(1/3) − 1 |
| Net Debt/EBITDA | **−0.092× (net cash)** | Net debt −$25M (Q1 FY2026) ÷ TTM EBITDA $271.8M |
| FCF/NI conversion (by year) | FY22 104.2% / FY23 92.5% / FY24 **−176.3%** / FY25 585.7% / TTM 815.3% | FCF ÷ NI each period |
| FCF positive? (3yr) | FY23 (+$347.0M) → FY24 (**−$245.0M**) → FY25 (+$41.0M) | Streak broken by FY2024 |

### Sub-scores

**Profitability (25% weight):**
```
NetMargin_Component = clamp((0.727/30)×100, 0, 100) = 2.42
ROIC_Component       = clamp((−0.22/30)×100, 0, 100) = 0.00  (negative → floor)
Profitability_Score  = (2.42 + 0.00) / 2 = 1.21
```
FCF-positive-3yr cap (40.0) does not bind — 1.21 is already far below it.

**Margins (15% weight):**
```
GrossMargin_Score = clamp((78.6/80)×100, 0, 100) = 98.3
```
No structural-expansion bonus applies (that bonus is reserved for margins *below* the 40% threshold moving the right direction — CSGP's margin is already 78.6%, so the bonus doesn't apply either way regardless of the mild downward trend).

**Growth (20% weight):**
```
Growth_Score = clamp((14.16/25)×100, 0, 100) = 56.6
```
**+10 documented TAM/pricing-power evidence:** CoStar reported its **60th consecutive quarter of double-digit revenue growth** in Q1 FY2026 (+23% YoY to $897M) and **launched CoStar Platform in France on 2026-07-02** — active geographic TAM expansion ([CoStar Q1 2026 press release](https://investors.costargroup.com/news-releases/news-release-details/costar-group-q1-2026-revenue-grows-23-year-over-year-897-million); France launch reported same week). Growth is **accelerating**, not decelerating (FY23 +12.5% → FY24 +11.4% → FY25 +18.7% → Q1 FY26 +23% YoY), so no −10 deceleration penalty.
```
Growth_Score = 56.6 + 10 = 66.6
```

**Balance Sheet (15% weight):**
```
BalanceSheet_Score = clamp(100×(1 − (−0.092)/4), 0, 100) = clamp(102.3, 0, 100) = 100.0
```
Net cash position (thin but positive) — comfortably passes the Debt Gate regardless of standard vs. asset-light denominator.

**Moat Signal (15% weight)** — checklist, all 5 signals require cited evidence:

| Signal | TRUE/FALSE | Evidence (cited) |
|---|---|---|
| Market share stable or growing | **TRUE** | 60 consecutive quarters of double-digit revenue growth (Q1 FY2026 release) — durably outpacing the broader real-estate-services/data market; company describes itself as commercial real estate's leading information/analytics/marketplace provider |
| Brand premium | **TRUE** | Annualized Net New Bookings $67M in Q1 2026, +20% YoY ([CoStar Q1 2026 release](https://investors.costargroup.com/news-releases/news-release-details/costar-group-q1-2026-revenue-grows-23-year-over-year-897-million)) sustained without discounting against a scale competitor |
| Network effect | **TRUE** | Homes.com agent subscribers +205% YoY to 35,175 alongside audience growth to 131M average monthly unique visitors (Q1 FY2026) — two-sided marketplace reinforcement (listers and searchers growing together) across LoopNet/Apartments.com/Homes.com |
| Switching costs | **TRUE** | Homes.com subscriber retention rate rose to 86% in Q3 2025, up from ~62% a year earlier ([HousingWire](https://www.housingwire.com)) — rising stickiness as the product embeds into agent workflow; CoStar Suite is embedded in CRE broker/investor underwriting workflows |
| Scale cost advantage | **TRUE** | 1,600+ dedicated market researchers plus aerial/drone/data-feed infrastructure covering 6M+ properties and 11M+ lease/sale comps, built over 38 years with $5B+ cumulative investment ([costar.com/about/data-providers](https://www.costar.com/about/data-providers)) — a fixed-cost data-collection moat a new entrant cannot cheaply replicate |

```
Moat_Score = (5/5) × 100 = 100.0
```

**FCF Quality (10% weight):**
```
FCFQuality_Score = clamp(((8.153 − 0.40)/0.60)×100, 0, 100) = clamp(1292, 0, 100) = 100.0
```
(TTM FCF/NI ratio 815.3% — clamped to the 100.0 ceiling. **Flagged**: this is a near-zero-net-income denominator artifact, not evidence of genuinely excellent cash conversion; treat the 100.0 print with caution.)

### Hard disqualifier check (independent of weighted score)

| Hard disqualifier | Status | Detail |
|---|---|---|
| FCF/NI conversion <70% for 2+ consecutive years w/o growth-capex explanation | **PASS (does not trigger)** | Only FY2024 fell below 70% (it was negative); FY2023 (92.5%) and FY2025 (585.7%) both clear 70% — not 2 *consecutive* years |
| Net Debt/EBITDA over threshold | **PASS (does not trigger)** | Net cash position, both at FY2025-end and Q1 FY2026 |
| **Not FCF-positive for 3+ consecutive years** | **⚠️ TRIGGERS** | FY2023 (+$347.0M) → **FY2024 (−$245.0M)** → FY2025 (+$41.0M) — the most recent 3-year window contains a negative year, breaking the streak. **This disqualifier carries no carve-out** (unlike the FCF/NI-conversion check, which can be waived with a documented growth-capex explanation) — see [glossary.md](../framework/glossary.md)'s "Hard disqualifier" entry. This independently fails the Quality Gate regardless of the weighted score below. |

**CSGP fails the 80.0+ Quality Gate two ways: an unwaivable hard disqualifier AND a sub-80 weighted score (below).**

### Final Quality Score

```
Quality Score = (1.21×0.25) + (98.3×0.15) + (66.6×0.20) + (100.0×0.15) + (100.0×0.15) + (100.0×0.10)
              = 0.303 + 14.745 + 13.318 + 15.000 + 15.000 + 10.000
              = 68.365 → 68.4 (rounded to nearest 0.1)
```

**Quality Score = 68.4 — FAILS the 80.0+ gate** (both via the weighted score and via the hard disqualifier above). Per [rescore.md](../.claude/commands/rescore.md) step 3, this is flagged as a **Phase 04 Quality Watch escalation** — CSGP is **not** being force-exited on quality alone (existing holdings aren't retroactively exited this way), but the drop below the gate is itself a signal worth surfacing prominently.

**Read carefully, though:** the profitability weakness here is driven by a **deliberate, guided, self-funded operating-expense investment** (Homes.com sales & marketing), not by moat erosion or a declining competitive position — Growth, Margins, Balance Sheet, and Moat sub-scores are all strong-to-excellent (66.6, 98.3, 100.0, 100.0). This differs materially in *character* from a quality failure driven by genuine fundamental deterioration (contrast with the 2026-07-01 NKE rescore, where declining ROIC and moat-erosion evidence were the drivers). It's flagged here as an open framework observation, not resolved in this session: **Owner Earnings (Upgrade 1) exists specifically to avoid penalizing capex-funded reinvestment, but has no equivalent adjustment for opex-funded reinvestment** — a company investing heavily and successfully via operating expense (as CoStar is doing with Homes.com) gets no analogous credit in either the FCF sub-score or the Quality Score's Profitability sub-score. Worth flagging to the user as a candidate framework gap, not something this session should quietly work around.

---

## 5. Valuation Score

### Standard Re-Score inputs (TTM/most-recent; fetched fresh this session)

| Metric | Value | Source / calc |
|---|---|---|
| Live price | $30.00 | See §1 |
| Market cap | $12,250.7M | $30.00 × 408.356M shares |
| Net cash | +$25M (Q1 FY2026) | Cash & ST investments $1.215B − Total debt $1.190B |
| Enterprise value | $12,225.7M | Market cap − net cash |
| FCF yield (TTM) | **1.651%** | TTM FCF $202.2M ÷ market cap $12,250.7M |
| EV/EBIT (trailing) | **undefined** | TTM EBIT −$26.2M → EV/EBITDA substituted (flagged) |
| EV/EBITDA (TTM) | **44.98×** | EV $12,225.7M ÷ TTM EBITDA $271.8M |
| Forward PE | 16.71× | `yfinance` `forwardPE` |
| 5yr avg PE | 72.4× (distorted — not used) | Re-verified this session; unchanged from 06-20 |
| Revenue CAGR 3yr | 14.16% | See §4 |

**FCF (40% weight):**
```
FCF_Score = clamp(100×(1 − 1.651/10), 0, 100) = 83.49
```
(Owner Earnings does not improve this — see §2.)

**EV/EBIT (25% → 40% weight after PEG redistribution):**
```
EV/EBIT_Score = clamp((44.98 − 12)/23 × 100, 0, 100) = clamp(143.4, 0, 100) = 100.0
```
(EV/EBITDA proxy for undefined trailing EV/EBIT, same substitution as 2026-06-20. Forward sanity check: 2026E adjusted EBITDA guide $780–820M, reiterated/raised in April 2026 after Q1 results — unchanged since the last review — implies forward EV/EBIT in the low-to-mid-20s×, i.e., the franchise is meaningfully cheaper on a normalized forward basis; the trailing 100.0 is deliberately the honest, conservative read.)

**Forward PE (20% weight):**
```
FwdPE_Score = 50.0 (neutral fallback, flagged — 5yr base still too distorted, re-verified §2)
```

**PEG (15% weight):** **Not applicable.** Trailing EPS collapsed and is only partially recovering (TTM EPS ≈ $0.06); no 3+ years of clean >15% EPS growth on a reliable base. PEG's 15% redistributed to EV/EBIT (→ 40%), same as 2026-06-20.

**Raw weighted score:**
```
Raw weighted = (83.49×0.40) + (100.0×0.40) + (50.0×0.20)
             = 33.40 + 40.00 + 10.00 = 83.40
```

**After Rate Environment Gate:** 83.40 + 5 (Step 2) = **88.40** (pre-Upside/Downside).

### Upside/Downside Modifier

**Scenario fair value** (Rule 7 — EV/EBIT-multiple method on ~2027–2028 normalized EBIT; same normalized-EBIT and exit-multiple assumptions as the 2026-06-20 session, since guidance is unchanged since then; net cash add-back updated to the current, much-thinner +$25M; 408.356M shares):

| Scenario | Wt | Normalized EBIT | Exit EV/EBIT | FV/share |
|---|---|---|---|---|
| Bull | 25% | $800M | 22.0× | **$43.16** |
| Base | 50% | $650M | 20.0× | **$31.90** |
| Bear | 25% | $450M | 16.0× | **$17.70** |

(Each figure is ~$1.03–1.04 lower per share than the 2026-06-20 session's equivalent scenario — entirely explained by the net-cash cushion shrinking from +$449M to +$25M, i.e. the $700M buyback consuming the cash add-back, not a change in the operating assumptions themselves.)

Bull ($43.16) still sits below the analyst-consensus mean PT ($47.50) — sober bull anchor maintained.

- **PW Fair Value** = 0.25×43.16 + 0.50×31.90 + 0.25×17.70 = **$31.16**
- **Gap Upside %** = ($31.16 ÷ $30.00) − 1 = **+3.88%**
- **Catalyst & timeline (Rule 10):** Same documented, management-guided catalyst as before — the Homes.com net-investment cut (>$300M less in 2026, confirmed unchanged in April 2026 guidance) and the guided adjusted-EBITDA path ($442M FY25 → $780–820M FY26 → $1.25B FY28). **2-year window** (unchanged). Annualized gap = 3.88% ÷ 2 = **+1.94%/yr**.
- **Intrinsic growth: +12%/yr** (unchanged from 06-20 — if anything the actual trajectory is running slightly ahead of this: FY2026 guide reiterated at 18% revenue CAGR, Q1 2026 delivered +23% YoY — kept conservative per guardrail 2, not raised to the rosy point).
- **Shareholder yield: +4%** ($700M 2026 buyback, ≈5.7% of market cap, net of SBC dilution offset — unchanged).

```
E = 1.94 (annualized gap) + 12.0 (intrinsic growth) + 4.0 (shareholder yield) = 17.94%
```

**Map to modifier** (H = 10%): E ≥ H → M = −15 × clamp((17.94 − 10)/15, 0, 1) = −15 × 0.529 = **−7.94**

**Guardrail check:** (1) Catalyst exists within 18–24 months → no −5 upside cap. (2) Bull/base/bear PW FV used, not the rosy point. (3) Full calc shown. (4) Bounded ±15 — within range.

### Final Valuation Score

```
Final Valuation Score = 83.40 (raw) + 5 (Rate Regime) + (−7.94) (Upside/Downside)
                       = 80.46 → 80.5 (rounded to nearest 0.1)
```

| | Value |
|---|---|
| Raw weighted | 83.40 |
| Rate Gate (Step 1 pass + Step 2) | +5 |
| Upside/Downside Modifier | −7.94 (E = +17.94%) |
| **FINAL VALUATION SCORE** | **80.5** |
| Prior valuation score (2026-06-20) | 79.0 |

**Raw valuation score alone moved from 79.0 → 80.5 — one band more expensive** (70.0–79.9 "Trim 25–30%" → 80.0–89.9 "Trim to 50%"), driven mainly by the shrunk net-cash cushion pulling down all three scenario fair values and by the 10Y yield ticking up. This is a **smaller, mechanical drift**, not a fundamental deterioration — flagged for the divergence discussion below.

---

## 6. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 68.4) + 0.50 × 80.5
                = 0.50 × 31.6 + 0.50 × 80.5
                = 15.8 + 40.25
                = 56.05 → exactly on a ".X5" boundary → round UP (conservative) → 56.1
```

**Composite Score = 56.1.**

---

## 7. Final score + action recommendation

**Composite Score 56.1 → Action band: 50.0–69.9 → HOLD** (watch only, no new entry, no trim — Fair Value band).

**This must be read carefully, not taken as a routine, comfortable Hold — flagged as a Phase 04 Quality Watch escalation, per rescore.md step 3:**

- **The raw Valuation Score alone (80.5) says "Trim to 50%"** — one band *more* aggressive than last review's 79.0 ("Trim 25–30%"). On trailing multiples and the forward-return modifier alone, CSGP still reads as expensive.
- **The newly-computed Quality Score (68.4, FAILS the 80.0+ gate — including an unwaivable hard disqualifier)** pulls the blended Composite down into the Hold band. Per [valuation-scoring.md](../framework/valuation-scoring.md), "Use the Composite Score, not the raw Valuation Score... once a company has a Quality Score on file" — so HOLD is the letter-of-the-framework action.
- **Why this reads differently from the 2026-07-01 NKE case** (where an analogous quality-driven softening was overridden as "a false green light"): NKE's Quality Score failure was driven by *genuine deterioration* — declining ROIC, documented moat erosion. CSGP's Quality Score failure is driven almost entirely by a **temporarily suppressed profitability metric from a disclosed, guided, self-funded operating-expense investment** (Homes.com), while Growth, Margins, Balance Sheet, and Moat sub-scores are all strong (66.6–100.0). This is a different, and arguably less alarming, kind of quality concern — closer to "a good business having a rough profitability quarter by design" than "a business getting worse." On that basis, this session does **not** override the Composite-driven HOLD the way NKE's session overrode its Composite-driven BUY signal.
- **The hard disqualifier (not FCF-positive 3 consecutive years) is nonetheless real and should not be waved away.** It independently fails the Quality Gate regardless of any qualitative story about *why* FY2024's FCF went negative. Combined with the raw Valuation Score's independent "Trim to 50%" read, this position deserves closer-than-routine attention at the next earnings print.

**Net recommendation: HOLD the existing position — no forced trim, no add.** Current position: 25 shares, 1.38% of portfolio (per [holdings.md](../portfolio/holdings.md), as of the 2026-06-28 sync) — already a small, tracking-sized position. No order setup required (operating-brief.md OUTPUT FORMAT step 6 applies only to BUY/TRIM actions).

**No full exit** — Phase 06 triggers absent: still net-cash (no leverage crisis, despite the thinner cushion), gross margin intact at 78.6%, revenue growing and accelerating (60 consecutive quarters of double-digit growth), moat signals all documented intact. The FCF-positivity hard-disqualifier trigger is a real quality flag but is not, on its own, one of Phase 06's four valid exit triggers (fundamental deterioration / broken growth thesis / balance sheet crisis / sustained 90.0+ score) — none of those are present.

---

## 8. Portfolio rebalancing summary

Out of scope for a single-ticker rescore. Recommendation handed to the orchestrator: **HOLD** the 1.38%-weight CSGP position (no trim, no add), with an explicit **Phase 04 Quality Watch flag** given (a) the hard disqualifier trigger and (b) the raw Valuation Score's independent "Trim to 50%" read, both meriting closer attention at the 2026-07-28 earnings print. `portfolio/holdings.md` is **not** edited by this session (orchestrator handles it) — the update should carry Last Score 80.5, Quality Score 68.4, Composite Score 56.1, Last Review 04 Jul 2026.

---

## 9. Next review trigger

- **Next earnings: Q2 FY2026, 2026-07-28** (confirmed via `yfinance` calendar and CoStar's own press release). Standard re-score, with specific attention to:
  - Whether **FY2026 full-year FCF** comes in positive (it would, combined with FY2025's +$41.0M, restore a clean run and — if FY2027 also holds positive — eventually clear the FCF-positivity hard disqualifier on a rolling 3-year basis)
  - Progress on the Homes.com net-investment cut (>$300M less in 2026, targeting continued $100M+/yr cuts through 2030 per management's own reduction schedule)
  - Adjusted EBITDA progress against the (unchanged, reiterated) $780–820M FY2026 guide
  - Whether TTM EBIT turns positive, which would finally allow a clean EV/EBIT calculation instead of the EV/EBITDA proxy
- **Earlier if (Rule 9):** a guidance revision (up or down), a management change, material M&A, or a >15% unexplained price move.
- **Quality Score watch:** re-check the hard disqualifier and the Profitability sub-score every quarter — this is the one number in the whole Quality Score most likely to flip materially as the Homes.com investment cycle matures.

---

## 10. Glossary

*(New terms added to [glossary.md](../framework/glossary.md) in this session are marked **NEW**; all others are pre-existing entries cited here because this output used them.)*

- **CAGR** — Compound Annual Growth Rate.
- **Composite Score** — this framework's blended 0.0–100.0 ranking number, `0.50 × (100 − Quality Score) + 0.50 × Valuation Score`.
- **D&A** — Depreciation & Amortization.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization.
- **Effective tax rate** *(NEW)* — the actual percentage of a company's pretax income paid as income tax in a given period (tax provision ÷ pretax income); distinct from the statutory rate, and can swing sharply when pretax income is near zero.
- **EV / EV/EBIT / EV/EBITDA** — Enterprise Value and its operating-profit multiples.
- **EY (Earnings Yield)** — 1 ÷ Forward PE.
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow and its two standard framework ratios.
- **Forward PE** — Price ÷ next-twelve-months expected EPS.
- **Hard disqualifier** — a Quality Score condition that fails a company regardless of weighted score; not every hard disqualifier has a carve-out (the FCF-positivity check does not).
- **Hurdle rate** — the 10% minimum acceptable annual return the Upside/Downside Modifier measures expected return against.
- **Invested Capital** *(NEW)* — total debt plus shareholders' equity: the capital base ROIC is measured against (NOPAT ÷ Invested Capital).
- **Mark price (PL price)** *(NEW)* — a broker's own real-time estimate of an instrument's current fair value (used for margin and profit/loss calculations), which can differ briefly from the last recorded trade price, especially around market closures — as happened with IBKR's CSGP snapshot this session (see §1).
- **MoS (Margin of Safety)** — cushion below fair value at which a buy price is set.
- **NI (Net Income)** — accounting profit after all expenses.
- **NOPAT** — Net Operating Profit After Tax, EBIT × (1 − effective tax rate); the numerator of ROIC.
- **Owner Earnings** — Net Income + D&A − maintenance capex only.
- **PEG ratio** — PE ÷ earnings growth rate.
- **Quality Score** — this framework's 0.0–100.0 grading of profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to clear the gate.
- **R/R (Risk/Reward ratio)** — reward-to-risk ratio for a trade.
- **ROIC** — Return on Invested Capital.
- **Rule 0 / Rule 6 / Rule 7 / Rule 9 / Rule 10** — this framework's live-price, normalization, scenario-analysis, model-refresh-trigger, and intrinsic-vs-market-price rules respectively.
- **TAM** — Total Addressable Market.
- **TTM** — Trailing Twelve Months.
- **Upside/Downside Modifier** — the additive ±15 adjustment folding expected annual return into the valuation score.
