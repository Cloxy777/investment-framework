# RESCORE — MSFT & META — 2026-06-12

**Task type:** RESCORE
**Date:** 12 Jun 2026
**10Y US Treasury Yield:** 4.55% (close, 10 Jun 2026 — TradingEconomics/FRED via search aggregation; up marginally from the 4.52% used in the 2026-06-11 recompute)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Rate Environment Gate Step 1:** Both MSFT and META **FAIL** the Earnings Yield Spread Test this session → a **separate** +5 additive applies to each, per strategy.md (Step 1 and Step 2 are independent additive modifiers — see the "Possible Rate Environment Gate inconsistency" flag in [watchlist/README.md](../watchlist/README.md), point 6). **Total Rate Modifier = +10 for both tickers**, resolving that flag for these two names.
**Last review on record:** MSFT 52.9 (Jun 2026, new 0–100 scale, derived from 2026-06-07 data without a fresh price pull — see [sessions/2026-06-11-rescore-holdings-new-scale.md](2026-06-11-rescore-holdings-new-scale.md)); META 43.7 (same).

---

## 1. Live Price (Rule 0)

| Ticker | Live price used | Source | Note |
|---|---|---|---|
| **MSFT** | **$390.97** | IBKR `get_price_snapshot`, 12 Jun 2026 07:25:50 UTC, `is_close: false` | +0.16% / +$0.63 vs. prior close |
| **META** | **$567.76** | IBKR `get_price_snapshot`, 12 Jun 2026 07:19:26 UTC, `is_close: false` | −0.12% / −$0.67 vs. prior close |

Both are fresh, non-stale broker quotes pulled this session. Both are down meaningfully from the 2026-06-07 session prices:
- MSFT: $412.46 → $390.97 = **−5.21%**
- META: $589.50 → $567.76 = **−3.69%**

Neither move exceeds the 15% Rule 9 threshold — no fundamental-event trigger from price alone. Both moves are within the kind of broad-tape softness that's "not a valid reason" to act per the operating brief's exit-trigger list; they're folded into the valuation re-score below via the updated market caps.

---

## 2. Data Gaps / Flags

1. **Upgrade 1 (Owner Earnings) — still unresolved for both MSFT and META.** Upgrade 1 requires Owner Earnings = Net Income + D&A − *Maintenance* CapEx whenever growth capex >30% of total capex (mandatory for MSFT/META/GOOGL/AMZN). Both research passes this session confirmed **neither company discloses a maintenance-vs-growth capex split** — only qualitative commentary exists (MSFT: "roughly half of capex is short-lived GPU/server assets, other half long-lived datacenter buildout"; META: FY2026 capex guidance ~2× FY2025 actual, implying heavy growth weighting, but no $ split). Computing Owner Earnings would require **inventing** a maintenance-capex figure, which CLAUDE.md prohibits. **Used raw TTM FCF as the FCF_Score input for both** (same approach as the 2026-06-11 MSFT recompute). This is now the **third consecutive session** (06-07, 06-11, 06-12) this gap has surfaced for this group of tickers — recommend a `decisions/` entry to either (a) formally suspend Upgrade 1 for companies that don't disclose the split, or (b) define an approved sourced proxy.

2. **10-yr "avg PE" used in the FwdPE fallback formula is TRAILING PE, not forward-PE-specific, for both tickers.** No source surfaced a 10-year *forward*-PE average or range for either MSFT or META — only trailing-PE 10-yr averages (MSFT ≈30.95×–33.07×; META ≈26.86×, also cross-checked against a ~30.51× trailing 10yr mean from a second source). This mirrors the convention already used in the 2026-06-07 session (which compared current forward PE against trailing 10yr-avg PE). Continued for consistency, flagged for a possible framework clarification on whether the fallback formula should require forward-PE history specifically.

3. **MSFT TTM D&A — three-way discrepancy resolved.** Figures found: $41.5B (narrow, cash-flow-statement "D&A and other," reconciled bottom-up from 10-Q/10-K), $46.5B (GuruFocus broader "Depreciation, Depletion & Amortization" aggregate), $84.4B (internally inconsistent with the same source's own FY2025 annual figure — **discarded as a data error**). Used $41.5B. Doesn't feed any sub-score directly but is relevant to the Owner Earnings gap above.

4. **META TTM FCF — two figures, used the fully-derived one.** $45.65B (bottom-up: FY2025 actual $43.59B − Q1 2025 $10.33B + Q1 2026 $12.39B, all from press releases/10-Q) vs. $51.2B (aggregator, no breakdown shown). Used **$45.65B** (fully cited derivation). The $51.2B alternate is shown as a sensitivity check below — **doesn't change the action band**.

5. **Gross margin, ROIC, Revenue CAGR 3yr — not re-collected this session for either ticker.** These are Phase 01 quality-gate inputs (don't feed the Phase 02 valuation score) for two long-qualified mega-caps with no signal of quality deterioration. Flagged as "not refreshed" rather than guessed, per the rescore skill's instruction to flag gaps explicitly.

6. **MSFT Forward PE / PEG — cross-source disagreement, resolved via own calculation.** Forward PE found in a 20.0×–21.5× range (midpoint 20.75× used). PEG quoted anywhere from 0.79 to 1.33 depending on source/growth-rate methodology. Computed PEG directly from our own cited inputs: 20.75 ÷ 23.3% (TTM EPS growth) = **0.89**, within the cited cross-source range. Sensitivity shown below — doesn't change the action band (50.5–54.5, all within 50.0–69.9 HOLD/watch).

7. **FCF/NI conversion <70% for both (Phase 04 monitor)** — MSFT 58.2%, META 64.6% (or 72.5% on the alternate FCF figure). Both below the 70% quality threshold, but both are explained by well-documented, elevated AI/datacenter growth capex (the Phase 04 monitor's stated carve-out) — not treated as a quality-deterioration signal.

---

## 3. MSFT — Inputs Collected

**Sector:** Technology — Software, Cloud Infrastructure (Azure) & Productivity
**Current portfolio weight:** 16.35% (IBKR + Freedom24, per [holdings.md](../portfolio/holdings.md))

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 7,428,434,704 | [10-Q FY26 Q3 cover page](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526191507/msft-20260331.htm), period ended 3/31/2026 |
| Market Cap | 7,428,434,704 × $390.97 = **$2,904.30B** | Computed |
| Total debt | $103.194B | Same 10-Q balance sheet |
| Cash + ST investments | $32.105B + $46.167B = $78.272B | Same 10-Q |
| Net debt | $103.194B − $78.272B = **$24.922B** | Computed |
| **EV** | $2,904.30B + $24.922B = **$2,929.22B** | Computed |
| **TTM EBIT (operating income)** | **$148.929B** | FY2025 full-year op income $128.5B (SEC filing) + (9mo FY26 op income $114.634B − 9mo FY25 op income $94.205B) = $128.5B + $20.429B = $148.929B. *(9mo figures cross-checked via individual quarters: Q3 FY26 = $38.4B, Q2 FY26 = $38.3B.)* |
| **EV/EBIT** | $2,929.22B ÷ $148.929B = **19.67×** | Computed |
| TTM Operating Cash Flow | $170.14B | [stockanalysis.com cash flow statement](https://stockanalysis.com/stocks/msft/financials/cash-flow-statement/) |
| TTM CapEx | $97.225B | Same |
| **TTM FCF** | $170.14B − $97.225B = **$72.916B** | Computed |
| **FCF Yield** | $72.916B ÷ $2,904.30B = **2.5106%** | Computed |
| TTM Net Income | $125.22B | Prior research pass |
| TTM Revenue | $318.27B | Prior research pass |
| Net margin | $125.22B ÷ $318.27B = 39.34% | Computed |
| TTM D&A | $41.549B (see Data Gap #3) | Reconciled from 10-K/10-Q |
| EBITDA (= EBIT + D&A) | $148.929B + $41.549B = $190.478B | Computed |
| Net Debt/EBITDA | $24.922B ÷ $190.478B = **0.131×** | Computed — well within Upgrade 5 thresholds |
| FCF/NI conversion | $72.916B ÷ $125.22B = **58.2%** | Computed — below 70%, see Data Gap #7 |
| Forward PE (NTM) | 20.0×–21.5× (midpoint **20.75×**) | GuruFocus (20.68), other aggregators 20.00/21.46/21.49, ~11 Jun 2026 |
| 10-yr avg PE (trailing, used as anchor) | 30.95×–33.07× (midpoint **32.01×**) | fullratio, financecharts |
| EPS growth (Fast Grower test) | FY2024 +22%, FY2025 +15.5%, TTM +23.3% — **all >15% → Fast Grower** | fullratio earnings history |
| PEG | **0.89** (computed: 20.75 ÷ 23.3) | See Data Gap #6 |
| Gross margin / ROIC / Rev CAGR 3yr | Not refreshed this session | See Data Gap #5 |
| Last Score / Last Review | 52.9 / Jun 2026 | [holdings.md](../portfolio/holdings.md) |

---

## 4. MSFT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 20.75 = 4.8193%
Spread = EY − 10Y Treasury = 4.8193% − 4.55% = +0.2693%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.2693%, ~1.23pp short) → **+5 additive**.

*Robustness check across the full Forward PE source range (20.0×–21.5×):* spread ranges from +0.10% (at 21.5×) to +0.45% (at 20.0×) — **FAIL in all cases**, so the +5 is robust to the cited source disagreement.

**Step 2 — Rate Regime Modifier**
10Y = 4.55% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for MSFT = +10**

---

## 5. MSFT — Full Score Calculation

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.5106 / 10), 0, 100) = 74.8937
```
→ Contribution: 74.8937 × 0.40 = **29.9575**

**EV/EBIT — 25% weight**
```
EV/EBIT_Score = clamp((19.67 − 12) / 23 × 100, 0, 100) = 33.3415
```
→ Contribution: 33.3415 × 0.25 = **8.3354**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (20.75 − 32.01) / 32.01 × 100 = −35.18%
FwdPE_Score = clamp(50 + (−35.18) × 2.5, 0, 100) = clamp(−37.95, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight (Fast Grower — EPS growth >15% in FY24/FY25/TTM, see §3)**
```
PEG = Forward PE ÷ TTM EPS growth% = 20.75 ÷ 23.3 = 0.8906
PEG_Score = clamp((0.8906 − 0.5) / 2.0 × 100, 0, 100) = 19.528
```
→ Contribution: 19.528 × 0.15 = **2.9292**

> **Sensitivity (Data Gap #6):** cross-source PEG figures (0.79 / 0.83 / 1.33) → PEG_Score 14.5 / 16.5 / 41.5 → Final Score 50.5 / 50.8 / 54.5. **All land in the 50.0–69.9 HOLD/watch band** — the action recommendation is unaffected by which PEG figure is used.

**Raw weighted score:**
```
= 29.9575 + 8.3354 + 0.0 + 2.9292
= 41.2221
```
**+ Rate Modifier (+10) = 51.2221**

Boundary rule: not a ".X5" → standard rounding → **Final Score = 51.2**

---

## 6. MSFT — Final Score & Action

# Final Score: 51.2 → Action: HOLD — watch only, no new entry, no trim

51.2 sits at the **low end of the 50.0–69.9 Fair Value / HOLD band** — close to, but not crossing, the 49.9 boundary into the BUY-standard band. This is a modest move **down** from the 52.9 recorded on 2026-06-11 (driven primarily by the lower price: FCF yield and EV/EBIT both improved slightly as the price fell from the figures underlying the prior recompute), but the band is unchanged. No valuation-driven action required.

(Separate from the valuation score: see §8 for MSFT's ongoing 15% position-cap breach.)

---

## 7. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** 7.51% (IBKR + Freedom24, per [holdings.md](../portfolio/holdings.md))

| Item | Value | Source |
|---|---|---|
| Shares outstanding | ≈2.196B | [companiesmarketcap.com](https://companiesmarketcap.com/meta-platforms/shares-outstanding/), cross-ref Q1 2026 10-Q cover page (Class A/B split ambiguous in retrieved snippets — flagged, doesn't affect the result materially) |
| Market Cap | 2.196B × $567.76 = **$1,246.80B** | Computed |
| **TTM EBIT (operating income)** | FY2025 $83,276M − Q1 2025 $17,555M + Q1 2026 $22,900M = **$88,621M (~$88.62B)** | FY2025 10-K, Q1 2025 press release, Q1 2026 10-Q/press release |
| Cash + marketable securities | $23,426M + $57,754M = $81,180M | Q1 2026 8-K Ex-99.1 balance sheet (Mar 31, 2026) |
| Long-term debt (senior notes) | $58,748M | Same |
| Net cash position | $81,180M − $58,748M = **$22,432M net cash** (operating lease liabilities $28,021M excluded per standard EV convention) | Computed |
| **EV** | $1,246.80B − $22.432B = **$1,224.37B** | Computed |
| **EV/EBIT** | $1,224.37B ÷ $88.621B = **13.82×** | Computed |
| TTM FCF | FY2025 FCF $43.59B ($115.80B OCF − $72.22B capex) − Q1 2025 FCF $10.33B + Q1 2026 FCF $12.39B = **$45.65B** | FY2025/Q1 2025/Q1 2026 press releases (10-Q cash flow statements) |
| **FCF Yield** | $45.65B ÷ $1,246.80B = **3.6614%** | Computed |
| TTM Net Income | $70,629M (~$70.63B) | Same roll-forward as EBIT |
| TTM D&A | $20,719M (~$20.72B) | Same roll-forward |
| FCF/NI conversion | $45.65B ÷ $70.63B = **64.6%** (or 72.5% using the $51.2B alternate FCF) | Computed — see Data Gap #4/#7 |
| Forward PE (NTM) | **17.32×** | GuruFocus, 10 Jun 2026 (cross-checked: stockanalysis 17.81×, finbox 17.1× — cluster resolved to ~17.1–17.8×) |
| 10-yr avg PE (trailing, used as anchor) | **26.86×** | fullratio — see Data Gap #2 |
| EPS growth (Fast Grower test) | 2023→2024 +60.5% (low-comp "Year of Efficiency" base effect), 2024→2025 ≈ **−1.6%** (flat-to-down) | fullratio earnings history |
| Net Debt/EBITDA | net cash, ($22.432B) ÷ ($88.621B+$20.719B=$109.34B) = **−0.205×** | Computed — net cash position, no concern |
| Last Score / Last Review | 43.7 / Jun 2026 | [holdings.md](../portfolio/holdings.md) |

---

## 8. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 17.32 = 5.7737%
Spread = EY − 10Y Treasury = 5.7737% − 4.55% = +1.2237%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+1.2237%, only ~0.28pp short) → **+5 additive**.

This is the **closest-to-passing reading in the book** — even closer than the +0.94% gap recorded on 2026-06-07. If forward PE drifts down slightly further, or the 10Y yield ticks down, this gate could flip to PASS at the next review (removing the Step 1 +5).

**Step 2 — Rate Regime Modifier**
10Y = 4.55% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +10**

---

## 9. META — Full Score Calculation

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.6614 / 10), 0, 100) = 63.3863
```
→ Contribution: 63.3863 × 0.40 = **25.3545**

> **Sensitivity (Data Gap #4):** using the $51.2B alternate TTM FCF → FCF Yield 4.1065% → FCF_Score 58.9349 → contribution 23.5740 → Final Score **36.7** instead of 38.5. Both land in the same 30.0–49.9 BUY-standard band.

**EV/EBIT — weight 40% (PEG not applicable, redistributed — see below)**
```
EV/EBIT_Score = clamp((13.82 − 12) / 23 × 100, 0, 100) = 7.8947
```
→ Contribution: 7.8947 × 0.40 = **3.1579**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (17.32 − 26.86) / 26.86 × 100 = −35.52%
FwdPE_Score = clamp(50 + (−35.52) × 2.5, 0, 100) = clamp(−38.78, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — Fast Grower test: FAIL.** EPS growth was +60.5% in 2023→2024 (driven by the 2023 "Year of Efficiency" low-comp base, a one-off cost-cutting effect — not organic), then **≈−1.6% (flat-to-down) in 2024→2025**. This does not meet ">15% EPS growth for 3+ consecutive years" — **PEG is not applicable; its 15% weight is redistributed to EV/EBIT** (25% → 40%, as used above).

**Raw weighted score:**
```
= 25.3545 + 3.1579 + 0.0
= 28.5124
```
**+ Rate Modifier (+10) = 38.5124**

Boundary rule: not a ".X5" → standard rounding → **Final Score = 38.5**

---

## 10. META — Final Score & Action

# Final Score: 38.5 → nominally BUY — Standard 3–5%; actual action = HOLD, no fresh capital

38.5 sits in the 30.0–49.9 band, which the Action Table maps to "BUY — Standard position 3–5%" for a **new** entry. META, however, is an **existing holding already at 7.51%** of the portfolio — above that 3–5% standard band (though comfortably under the 15% hard cap). The Action Table has no trim trigger below 50.0, so this is not a sell signal; but adding fresh capital here would push an already-above-standard-band position further over, with no documented trigger (earnings, guidance change, etc.) to justify concentrating further. Consistent with the 2026-06-07 session's reasoning for META:

**Action: HOLD — no fresh capital deployed.**

This is a meaningfully **cheaper** reading than the 43.7 recorded on 2026-06-11 (driven by both the lower price and the corrected/redistributed EV/EBIT weighting), reinforcing the "don't trim" conclusion without creating a "buy more" trigger given the existing overweight-vs-standard-band position.

---

## 11. Order Setup

**Not applicable for either ticker.** Per the Action Table, order setups (Fair Value / Buy Price / Stop Loss / R-R / Position Size) are only computed for BUY (0.0–29.9) or TRIM (≥70.0) bands:
- MSFT (51.2) is in the HOLD/watch band — no order setup.
- META (38.5) nominally falls in a BUY band, but the actual recommendation is HOLD/no-fresh-capital given existing position size (§10) — computing a "buy price" for capital that isn't being deployed would be exactly the kind of black-box number-for-the-sake-of-the-template the framework warns against (cf. the NVDA session's treatment of an analogous case).

---

## 12. Portfolio Rebalancing Summary

**MSFT — 15% cap breach persists (Upgrade 7).** At 16.35% of the portfolio, MSFT remains **~1.35pp over the 15% hard cap** — unchanged in substance from the 2026-06-11 backfill note (16.84% → 16.35% reflects only the price/weight drift since 2026-06-07, not any reduction). This is a **structural/compliance issue, independent of the valuation score** — MSFT's score (51.2) sits in the HOLD/watch band and generates no valuation-driven trim signal. This is now the **third consecutive session** (2026-06-07, 2026-06-11 backfill, 2026-06-12) flagging this breach and recommending escalation to a dedicated `/rebalance` session for a structural reduction plan. **No ad-hoc trim is taken here** — consistent with "act only on documented triggers" and the prior sessions' explicit deferral to a dedicated REBALANCE session rather than folding a structural cap fix into a routine RESCORE.

**META — no portfolio-level action.** At 7.51%, META is comfortably under the 15% cap; its score generates no trim signal either.

---

## 13. Next Review Triggers

**MSFT:**
- Next earnings — MSFT FY2026 Q4 (fiscal year ending June 2026), expected **late July 2026**.
- **Open item carried forward: dedicated `/rebalance` session for the 15% cap breach** (§12) — not on the standard quarterly cadence, still not run as of this session.
- Owner Earnings (Upgrade 1) decision — see Data Gap #1.

**META:**
- Next earnings — META Q2 2026 (quarter ending June 2026), expected **late July 2026**.
- **Watch the Rate Gate Step 1 spread** — now +1.2237% vs. the +1.5% threshold, the closest-to-passing reading recorded yet (0.28pp short). A small move (forward PE down, or 10Y yield down) could flip this to PASS at the next review, removing the +5 Step 1 additive (Final Score would drop from 38.5 to ≈33.5 — still BUY-standard band, action likely unchanged, but worth re-deriving explicitly).
- Owner Earnings (Upgrade 1) decision — see Data Gap #1.
