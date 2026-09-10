# RESCORE — TRN (Trainline plc, LSE:TRN) — mode `--both`

**Task type:** RESCORE (Rule 9 management-change trigger — incoming CEO Ian Brown's effective start date, 7 Sept 2026, has now occurred; user also asked directly about FCF growth and debt/equity ahead of Friday's H1 FY2027 trading update)
**Date:** 2026-09-10
**10Y US Treasury Yield:** **4.80%** (WebSearch, multiple sources converging on 4.77–4.83% for 8–9 Sept 2026; FRED/tradingeconomics not directly queried this session, consistent with the access issue flagged 08-22/08-31)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket — unchanged)
**Last review:** 2026-08-31 (Valuation Score 10.0, Quality Score 67.2 — fails 80.0+ gate, Composite 21.4 reference-only; HOLD, do not top up)
**Position status:** Held, 600 shares, unchanged since 2026-06-24 (per most recent `/sync-portfolio`, 2026-08-30 — not re-run this session); weight 2.51%⚠️ per [holdings.md](../portfolio/holdings.md)

---

## 0. Why this session was triggered

Two independent reasons:
1. **Rule 9 management-change trigger** ([fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 9) — incoming CEO Ian Brown's confirmed 7 Sept 2026 start date has now passed (full Board handover still pending, 28 Sept). A CEO transition mandates re-score + thesis review + moat re-evaluation, independent of price movement.
2. **User request ahead of Friday's report** — confirmed via Trainline's own investor financial calendar: **11 September 2026 = "Trading update for half year FY2027"** (a sales/KPI update, not the audited H1 financial statements — those land separately; see §10). This session establishes the pre-report baseline the Friday numbers will be checked against, and directly answers the user's FCF-growth and debt/equity questions using the latest available (FY2026 annual) data.

---

## 1. Live price (Rule 0 — fetched first)

- **IBKR `get_price_snapshot` (contract_id 371871705):** last **186.3 GBX**, no halt; change −0.20 (−0.11%) vs prior session.
- **Price of record for this session: 186.3 GBX = 1.8630 GBP.** Down from 199.1 GBX (08-31) — a −6.42% move over 10 days, inside the ±15% Rule 9 threshold on its own (no independent price-move trigger; the CEO-start trigger in §0 stands on its own).
- **52-week range (IBKR `misc_statistics`):** low **178.00 GBX**, high **304.00 GBX**.

---

## 2. What's new since 2026-08-31

- **Ian Brown started as CEO-designate on 7 Sept 2026** (confirmed via [AJ Bell](https://www.ajbell.co.uk/news/articles/trainline-appoints-flutters-ian-brown-ceo-president), [Trainline plc newsroom](https://www.trainlinegroup.com/media/news/ian-brown-appointed-trainline-plc-ceo)) — joining alongside outgoing CEO Jody Ford for an orderly transition; full handover remains scheduled for 28 Sept 2026. No strategic announcements from Brown yet — too early for any Moat signal to move (see §4).
- **CMA drip-pricing investigation: still open, no finding.** ([GOV.UK case page](https://www.gov.uk/cma-cases/trainline-consumer-protection-enforcement-case)) Trainline has stated it is cooperating and making changes to fee presentation; no fine, no formal finding as of this session.
- **Confirmed: Friday 11 Sept 2026 is a trading update (sales/KPI), not full financials** ([Trainline financial calendar](https://www.trainlinegroup.com/investors/shareholder-centre/financial-calendar/)) — the audited H1 FY2027 results are a separate, later event. Flagged explicitly so the Friday release isn't mistaken for a fundamentals refresh of the inputs below.
- **No other Rule 9 trigger:** no earnings release yet, no guidance revision, no M&A.

---

## 3. Data refresh (`yfinance`, live this session — access restored)

FY2026 fundamentals (fiscal year ended 28 Feb 2026) — **unchanged from every prior TRN session**, confirming no new fiscal year has reported yet:

| Field | FY2026 | FY2025 | FY2024 | FY2023 |
|---|---|---|---|---|
| Total Revenue | £452,684,000 | £442,095,000 | £396,718,000 | £327,147,000 |
| Gross Profit | £373,874,000 | £352,313,000 | £305,285,000 | £252,224,000 |
| EBIT | £126,429,000 | £88,993,000 | £56,485,000 | £32,360,000 |
| EBITDA | £167,243,000 | £132,160,000 | £98,147,000 | £73,527,000 |
| Net Income | £79,813,000 | £58,348,000 | £33,986,000 | £21,217,000 |
| **Free Cash Flow** | **£79,547,000** | **£95,886,000** | £81,846,000 | £4,387,000 |
| Operating Cash Flow | £133,019,000 | £138,197,000 | £121,729,000 | £39,606,000 |

Balance sheet (FY2026, fresh pull, unchanged from prior sessions):

| Field | Value |
|---|---|
| Total Debt | £261,946,000 |
| — of which Capital Lease Obligations | £34,817,000 |
| Cash & Equivalents | £59,703,000 |
| **Total Equity** | **£204,369,000** |
| Invested Capital | £431,498,000 |

**Data-quality fix this session — Net Debt figure reconciled.** Every prior TRN session (06-22 onward) used yfinance's packaged **"Net Debt"** field (£167,426,000) for the Net Debt/EBITDA leverage gate, while separately using **Total Debt − Cash** (£202,243,000) for the EV bridge — flagged as an unresolved inconsistency in every session since 07-05 but never re-derived ("out of scope for a rescore"). Traced this session: yfinance's packaged Net Debt = Total Debt − Capital Lease Obligations − Cash = 261,946,000 − 34,817,000 − 59,703,000 = **167,426,000 exactly** — i.e. it silently *excludes lease liabilities* from debt. [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 6 is explicit: *"Debt: Include operating leases, pension obligations, off-balance-sheet items."* The lease-inclusive figure is therefore the framework-correct one. **This session switches to Net Debt = Total Debt − Cash = £202,243,000** for the Balance Sheet sub-score (§5) and going forward — a data-quality correction, not a fundamentals change (see §5 for the resulting score impact).

**FCF/NI conversion, 2yr:** FY2026 99.667%, FY2025 164.33% — both far above the 70% disqualifier threshold. ✅ PASS
**FCF positive, 3+ yr:** 4/4 reconstructable years positive (FY2023 £4.387M thin but positive). ✅ PASS
**Net Debt/EBITDA disqualifier threshold (2.5× standard):** 1.209× (corrected figure, §5) — well clear. ✅ PASS

**5-year historical PE:** still unreconstructable via `t.get_earnings_dates()` (0 usable quarters returned, same result as every prior session) → no-history fallback stands (`FwdPE_Score = 50.0`, flagged).

Peer multiples (fresh `yfinance` pull this session):

| Peer | Forward PE | EV/EBITDA |
|---|---|---|
| BKNG | 14.012× | 12.871× |
| EXPE | 11.181× | 11.260× |
| MMYT | 19.762× | 30.889× |
| TRIP | 8.205× | 9.867× |
| TCOM | 9.273× | −1.331× (excluded — negative EV/EBITDA, same exclusion as every prior session) |

---

## 4. Direct answer to the user's questions (FCF growth, D/E, buyback runway)

**FCF growth: negative this fiscal year, not positive.** FY2026 FCF was **£79.547M, down −17.04% from FY2025's £95.886M** (79,547,000 / 95,886,000 − 1 = −17.04%). This reverses the prior two years' strong growth (FY2023 £4.4M → FY2024 £81.8M → FY2025 £95.9M) — FY2026 is the first down year in the reconstructable history. Cause not separately disclosed in the financials pulled here (CapEx rose from £42.3M to £53.5M FY25→FY26, +26.4%, which mechanically explains most of the FCF decline given Operating Cash Flow only fell −3.7M — i.e. this looks like a reinvestment-driven dip, not an operating deterioration, but that's an inference from the two line items, not a disclosed management explanation — flagged, not invented). **Friday's trading update is sales/KPI only (§0) and won't resolve this — the FCF trajectory won't get a fresh data point until the H1 FY2027 results.**

**Debt/Equity: 1.28×** — Total Debt £261,946,000 ÷ Total Equity £204,369,000 = **1.282×**. Inside your 1.5–1.7× comfort band, with room to spare. (Framework's own leverage gate uses Net Debt/EBITDA, not D/E — see §5 for that figure, now corrected to 1.209×, also comfortably inside its 2.5× disqualifier threshold.)

**Buyback runway:** FY2026 disclosed net buyback yield 9.46% (0% dividend — 100% of shareholder return is via buyback), carried forward from the FY2026 annual figure (no fresher disclosure exists pre-Friday). Share count fell from 343,820,000 (08-31 snapshot) to **339,754,852 today** — a further **−1.18% in 10 days**, confirming the program is still running at pace. Given the D/E headroom above, Trainline could lever further to sustain or accelerate buybacks without breaching your 1.5–1.7× ceiling — though doing so would push Net Debt/EBITDA up from its current comfortable 1.209×.

---

## 5. Quality Score — recomputed (Net Debt/EBITDA correction, §3)

Per [quality-scoring.md](../framework/quality-scoring.md).

**Hard disqualifier check:** all three ✅ PASS (detailed in §3).

**Profitability (25%):**
```
Net Margin = 79,813,000 / 452,684,000 = 17.631%
Tax rate = 34,502,000 / 114,315,000 = 30.183%
NOPAT = 126,429,000 × (1 − 0.30183) = 88,267,600
ROIC = 88,267,600 / 431,498,000 = 20.457%
NetMargin_Component = clamp((17.631/30)×100) = 58.77
ROIC_Component       = clamp((20.457/30)×100) = 68.19
Profitability_Score  = (58.77 + 68.19) / 2 = 63.48   (no FCF cap — 4/4 years positive)
```

**Margins (15%):** Gross Margin 82.591% (unchanged) → `GrossMargin_Score = clamp((82.591/80)×100, 0, 100) = 100.0`

**Growth (20%):** Revenue 3yr CAGR 11.43% (FY23 £327.147M → FY26 £452.684M, unchanged base) → base `Growth_Score = clamp((11.43/25)×100) = 45.72`. TAM (+10) and structural-deceleration (−10) modifiers carried forward, net 0 (no new evidence found this session to re-test either — see §2, nothing here bears on TAM/pricing power) → `Growth_Score = 45.72`

**Balance Sheet (15%) — corrected this session (§3):**
```
Net Debt = Total Debt 261,946,000 − Cash 59,703,000 = 202,243,000   (lease-inclusive, per Rule 6)
Net Debt/EBITDA = 202,243,000 / 167,243,000 = 1.2093×
BalanceSheet_Score = clamp(100×(1 − 1.2093/4), 0, 100) = 69.77
```
(Previously 74.97 using the lease-excluded 167,426,000 figure — see §3 for why this session switches.)

**Moat Signal (15%)** — re-examined against this session's news (§2); Ian Brown's start is too recent (3 days) for any strategic evidence to exist yet:

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** (unchanged) | No new evidence found this session. |
| Brand premium (pricing power) | **FALSE** (unchanged) | CMA investigation remains open, unresolved. |
| Network effect | **FALSE** (unchanged) | No new evidence. |
| Switching costs | **TRUE** (unchanged) | Unrelated to the fee controversy. |
| Scale cost advantage | **FALSE** (unchanged) | No new cost-per-unit data found. |

```
Moat_Score = (2/5) × 100 = 40.0   (unchanged)
```

**FCF Quality (10%):** `FCF/NI = 79,547,000 / 79,813,000 = 99.667%` → `FCFQuality_Score = clamp(((0.99667 − 0.40)/0.60)×100, 0, 100) = 99.44`

### Quality Score total

```
Quality Score = 63.48×0.25 + 100.0×0.15 + 45.72×0.20 + 69.77×0.15 + 40.0×0.15 + 99.44×0.10
             = 15.870 + 15.00 + 9.144 + 10.4655 + 6.00 + 9.944
             = 66.42 → 66.4
```

**Quality Score = 66.4 — still FAILS the 80.0+ gate.** Down from 67.2 (08-31), but this move is entirely the Net Debt/EBITDA data-quality correction (§3), not a fundamentals decline — FY2026's underlying financials are unchanged from the last three sessions. No escalation of Quality Watch status; it was already open.

---

## 6. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** Forward PE (yfinance, fresh) = **7.0402×**. EY = 1/7.0402 = **14.204%**. Spread = 14.204% − 4.80% = **+9.404pp** ≥ +1.5% → no flag (+0).
- **Step 2 — Rate Regime Modifier:** 10Y = 4.80%, in the 3.5–5% bracket → **+5**.
- **Combined Rate Gate modifier: +5** — same bracket as every prior TRN session.

---

## 7. Valuation Score

### Sub-scores

**FCF Yield (40% weight):**
```
MarketCap = 339,754,852 × 1.8630 GBP = 633,062,791 GBP
FCF Yield = 79,547,000 / 633,062,791 = 12.567%
FCF_Score = clamp(100×(1 − 12.567/10), 0, 100) = 0.00   (floor-saturated, unchanged pattern)
```

**EV/EBIT (40% weight, PEG-redistributed — TRN not a Fast Grower, same reasoning as every prior session):**
```
EV = MarketCap 633,062,791 + Total Debt 261,946,000 − Cash 59,703,000 = 835,305,791 GBP
EV/EBIT = 835,305,791 / 126,429,000 = 6.607×
EV/EBIT_Score = clamp((6.607−12)/23×100, 0, 100) = 0.00   (floor-saturated)
```

**Forward PE (20% weight):** 7.0402× (from §6). No 5yr PE history reconstructable → no-history fallback: `FwdPE_Score = 50.0` (neutral, flagged) — unchanged.

### Raw weighted score

| Sub-score | Weight | Score | Weighted |
|---|---|---|---|
| FCF Yield | 40% | 0.00 | 0.00 |
| EV/EBIT | 40% | 0.00 | 0.00 |
| Forward PE | 20% | 50.00 | 10.00 |
| **Raw weighted score** | | | **10.00** |

**+ Rate Gate modifier: +5** → **15.00** (before Upside/Downside).

### Upside/Downside (Expected-Return) Modifier

**Fair Value:**
- **DCF component: 345.6 GBX — carried forward, same caveat as every prior session.** No new fiscal-year data exists to re-derive a CMA-adjusted bear case; Friday's trading update (sales/KPI only, §0) won't change this either. **Treat as likely somewhat optimistic** pending the CMA investigation's resolution and the H1 FY2027 full results.
- **Multiples component — fresh peer pull this session (§3):**
  - **EV/EBITDA:** median(9.867, 11.260, 12.871, 30.889) = **12.0655×** → implied EV = 12.0655 × 167,243,000 = 2,017,870,417 GBP → implied equity = 2,017,870,417 − 202,243,000 (corrected Net Debt) = 1,815,627,417 GBP → implied FV/share = 1,815,627,417 / 339,754,852 = 5.3444 GBP = 534.44 GBX → discounted 20% (Rule 5) → **427.55 GBX**.
  - **Forward PE:** median(8.205, 11.181, 14.012, 19.762) = **12.597×** (no outlier exclusion needed this session — MMYT's 19.762× is back in a plausible range, unlike 08-31's 95.30× reading). Forward EPS = live price 1.8630 / Forward PE 7.0402 = 0.26463 GBP → 12.597 × 0.26463 = 3.3335 GBP = 333.35 GBX → discounted 20% → **266.68 GBX**.
  - **Multiples-Based FV = average(427.55, 266.68) = 347.12 GBX.**
- **Blended FV = 0.40×345.6 + 0.60×347.12 = 138.24 + 208.27 = 346.51 GBX.**

**Sanity check:** last session's consensus 12-month target (~352p, 13 analysts, "Strong Buy") — not re-pulled this session — sits close to this session's 346.51 GBX, a reasonable cross-check.

```
Gap Upside % = (346.51 / 186.3) − 1 = +86.00%
Catalyst window = 2.0 years (unchanged — GBR timeline still not firmed inside 18–24mo)
Annualized gap = 86.00% / 2.0 = 43.00%/yr
Intrinsic growth = 11.5%/yr (carried forward — flagged this session, see note below)
Shareholder yield = 0% dividend + 9.46% net buyback yield (FY26 disclosed figure, carried forward; corroborated directionally by the fresh −1.18%/10-day share-count decline, §4)

E = 43.00 + 11.5 + 9.46 = 63.96%.  H = 10%.  E ≥ H → uncapped M would be −15.0 (floor)
```

**Flag — intrinsic growth carry-forward now sits awkwardly next to §4's finding.** The 11.5%/yr intrinsic growth figure has been carried forward unchanged since the original 06-24 session; this session's §4 finding (FCF down −17.04% YoY in the very fiscal year that carry-forward is meant to represent) is new information that arguably should lower it. Not re-derived here — re-deriving requires the H1 FY2027 financials (revenue/margin trajectory), not yet available (Friday's release won't include them either, §0) — but flagged explicitly rather than silently left in place, per "never invent or estimate financial data." **Re-derive at the 30 Oct H1 FY2027 full results.**

**Guardrail 1 (catalyst reliability) — unchanged, still applied:** GBR's full operational launch is still tracked to 2027, outside the 18–24 month window. **Guardrail 1 stays applied — capped at −5.0.**

**M = −5.0.**

### Final Valuation Score

```
Final Score = 15.00 (raw + Rate Gate) + (−5.0) (Upside/Downside, guardrail-capped) = 10.00
```

**Final Valuation Score = 10.0 — numerically unchanged from every prior TRN session.** Both valuation sub-scores remain floor-saturated and the Upside/Downside Modifier remains guardrail-capped well before the uncapped `E` value (63.96% this session) matters — the framework absorbs the FV/price movement without the final number moving.

---

## 8. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 66.4) + 0.50 × 10.0
                = 16.8 + 5.0
                = 21.8
```

**Composite Score = 21.8** (vs 21.4 on 08-31 — the Quality Score's Net Debt correction, §5, moving it, not a fundamentals shift). Lands in the "BUY — Full position 6–8%" band by the numbers alone; per this framework's established practice for a held position whose Quality Score fails the 80.0+ gate, this remains a false green light and is not acted on — same standing rule as every prior TRN session.

---

## 9. Action recommendation — HOLD existing 600 shares; do **NOT** add; Quality Watch remains open

**Unchanged: HOLD, do not top up.** The Quality Score (66.4 < 80.0) remains the sole, sufficient blocker.

**Phase 06 triggers checked, none fire:**
- Balance sheet crisis: no — leverage improved on paper this session only due to the Net Debt correction (§3/§5), not a real deterioration; D/E 1.28× and Net Debt/EBITDA 1.209× both comfortably inside normal ranges.
- Management change: **Ian Brown has started (7 Sept), full handover 28 Sept** — a real, occurring management transition, but not yet a Phase 06 trigger (those require *fundamental deterioration* — margins broken, ROIC below cost of capital, moat eroded, or a balance-sheet crisis — a scheduled, orderly CEO handover on its own doesn't qualify). Tracked for thesis review once Brown sets out strategy post-handover.
- Growth thesis: not broken — TAM/pricing-power evidence unchanged (§5).

### Informational-only order setup (shown for transparency — NOT being executed, same as prior sessions)

```
Blended Fair Value = 346.51 GBX  (caveated — see §7, DCF component likely optimistic, intrinsic growth flagged for re-derivation)
Buy Price (20% MoS) = 346.51 × 0.80 = 277.21 GBX
Live price (186.3 GBX) vs. Buy Price: 32.79% below → would read "enter now" if gate-eligible
Primary Sell Target = 346.51 GBX
Stop Loss — re-anchored to live entry (same degeneracy as prior sessions):
  20% below live entry → 186.3 × 0.80 = 149.04 GBX
  Flag: this stop sits below the 52-week low (178.00 GBX) — a consequence of trading near the 52-week low, not a calculation error.
R/R = (346.51 − 186.3) / (186.3 − 149.04) = 160.21 / 37.26 = 4.30:1 — clears the 2:1 minimum by a wide margin

Position sizing not recomputed this session (portfolio balances not re-synced, out of scope for a single-ticker rescore per established practice).
```
**Not executed.** The Quality Gate governs, independent of how attractive these mechanics look.

---

## 10. Portfolio Rebalancing Summary

N/A — single-ticker rescore, no other position touched this session.

---

## 11. Next Review Trigger

- **Immediate, informational:** Friday 11 Sept 2026's H1 FY2027 trading update — sales/KPI figures only (confirmed via Trainline's own financial calendar), won't move any scored input here but should be checked against FY2026's guidance range for consistency.
- **Mandatory:** H1 FY2027 full results (date not yet located this session — confirm before 30 Oct if that's still accurate) — will refresh every financial-statement-derived input (FCF, EBIT, Net Debt, margins) for the first time since FY2026's annual report, and lets the flagged intrinsic-growth figure (§7) and the DCF bear case be properly re-derived with post-CMA, post-CEO-transition information.
- Ian Brown's full Board handover (28 Sept 2026) and his first strategic communications as CEO — Moat re-evaluation once there's actual evidence to assess (§5).
- Any CMA drip-pricing investigation update (finding, fine/remedy, fee-structure change).
- Any GBR-related announcement — still the binding constraint on Guardrail 1's −5 cap.
- Standard Rule 9 triggers: guidance revision, M&A, >15% unexplained price move.

---

## 12. Glossary

- **CAGR** — Compound Annual Growth Rate.
- **CMA (Competition and Markets Authority)** — the UK's competition/consumer-protection regulator; its drip-pricing investigation into Trainline remains open, unresolved this session.
- **Composite Score** — this framework's 0.0–100.0 blended ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; computed only for reference here since Quality fails the gate.
- **D/E (Debt-to-Equity ratio)** — Total Debt ÷ Total Equity; a balance-sheet leverage measure distinct from this framework's own Net Debt/EBITDA gate, computed here because the user asked for it directly.
- **DCF** — Discounted Cash Flow.
- **Drip pricing** — presenting mandatory charges later in a purchase flow rather than in the advertised headline price; the specific practice the CMA is investigating.
- **EBIT / EBITDA** — operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS** — Earnings Per Share.
- **EV / EV/EBIT, EV/EBITDA** — Enterprise Value / Enterprise Value divided by operating-profit measures.
- **EY (Earnings Yield)** — 1 ÷ Forward PE.
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks earnings quality).
- **Forward PE** — Price ÷ next-12-months expected EPS.
- **FV / PW Fair Value** — Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear).
- **GBR (Great British Railways)** — UK rail-nationalization program; relevant to TRN as a regulatory/political risk to its retailer role.
- **GBX / pence (GBp)** — 1/100th of a British pound; LSE quoting convention.
- **Hurdle rate** — the minimum acceptable annual return (10% in this framework).
- **Moat** — a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety)** — the discount below fair value demanded before buying.
- **Net Debt/EBITDA** — leverage ratio; this framework's balance-sheet-risk gate.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − tax rate)).
- **PE (Price-to-Earnings) ratio**, **PEG ratio** — standard valuation multiples; PEG = PE ÷ growth rate.
- **Phase 04 Quality Watch** — this framework's escalation flag for a held position whose Quality Score sits below the 80.0+ gate or is deteriorating.
- **Phase 06** — this framework's exit-review phase (balance-sheet crisis, management change, and other full-exit triggers).
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear blended estimate.
- **Quality Score** — this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 valuation scoring.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-score interest-rate check.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss on a trade; 2:1 minimum required.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — always fetch a live price before any valuation work.
- **Rule 5** — comparables-set quality requirement (discount applied for thin/mismatched peer sets).
- **Rule 6** — normalize the balance sheet before valuing, including leases and off-balance-sheet items — the rule this session's Net Debt correction (§3) applies.
- **Rule 9** — fundamental events that force an immediate re-score (>15% unexplained price move, guidance revision, M&A, management change); fired this session via the CEO-start-date trigger (§0).
- **Upside/Downside Modifier (Expected-Return Modifier)** — the ±15 additive score adjustment based on expected annual return.
