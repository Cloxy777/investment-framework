# RESCORE — ZS (Zscaler, Inc.)

**Task type:** RESCORE (single ticker, mode `--both`)
**Date:** 2026-07-05 (Sunday — markets closed; most recent trading session 2026-07-02, ahead of the 3 Jul July 4th holiday observance and the weekend)
**10Y US Treasury Yield:** 4.485% (`yfinance` `^TNX`, 2026-07-02 close — most recent available)
**Rate Regime Modifier (Step 2):** +5 (10Y in the 3.5–5% bracket)
**Last review on record:** ZS **36.3** (2026-06-20, BUY-Standard band on score, but blocked at entry by a sub-2:1 R/R **and** the pre-existing Phase 01 GAAP quality-gate fail — [sessions/2026-06-20-rescore-zs.md](2026-06-20-rescore-zs.md)); Composite Score never computed (predates the 2026-06-29 Quality Score/Composite Score methodology change — flagged stale, see [watchlist/STALE.md](../watchlist/STALE.md)).
**Current ZS portfolio weight:** 0.24% per [holdings.md](../portfolio/holdings.md) — not recomputed this session (weight refresh is `/sync-portfolio`'s job).
**First-ever Quality Score / Composite Score computation for ZS this session.**
**Special case:** ZS is held as a **Human Override** — it fails the Phase 01 quality gate — per `watchlist/STALE.md`'s note. **This session found `portfolio/override-log.md` contains no actual ZS entry** despite multiple other records assuming one exists — see §3 flag 4. Not resolved here (out of scope); flagged for the orchestrator/user.

> *Jargon decoded on first use — see closing Glossary section.*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$147.33** | IBKR `get_price_history` (contract_id 310621426, NASDAQ), most recent daily bar close = **2026-07-02**. |
| ⚠️ Tooling flag | IBKR `get_price_snapshot`'s `last` field returned **$146.45** (`is_close: true`) — one session stale: `get_price_history` shows 2026-07-01 close = $146.45 and 2026-07-02 close = $147.33. Same recurring stale-snapshot pattern already flagged in the 2026-07-05 MSFT/NOW and 2026-07-04 AVGO sessions — used the fresher $147.33 instead. Cross-checked independently against `yfinance`'s `currentPrice`/`regularMarketPrice`, both reading $147.33, and IBKR's own `plprice` (mark) of $147.125 — consistent. |
| 52-week range | $114.625 – $336.99 | IBKR `misc_statistics` / `yfinance` `fiftyTwoWeekLow`/`fiftyTwoWeekHigh` |
| Analyst consensus PT | mean **$192.58**, median $187.50, range $145–$250, n=44 | `yfinance` `targetMeanPrice`/`targetMedianPrice`/`targetLowPrice`/`targetHighPrice` — bull-case sanity check only (Rule 0 Step 4), not a scored input. |
| Price vs. 06-20 review ($124.85) | **+18.0%** | Exceeds the 15% Rule 9 threshold — see §2. |

---

## 2. Rule 9 Trigger Check (2026-06-20 → 2026-07-05)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | No (predates window) | Last report was **26 May 2026** (fiscal Q3 2026): EPS $1.08 vs. $1.01 consensus (+7.1% surprise), revenue ~$850M (+25% YoY) — already reflected in the 06-20 review's inputs. Next report confirmed **2 Sep 2026** (`yfinance` `get_earnings_dates`). |
| Guidance revision | No | No new formal guidance found issued since 06-20. |
| M&A | No | None found. |
| Management change | No | None found. |
| Macro shift | No | 10Y ticked from 4.451% (06-18) to 4.485% (07-02) — still inside the "3.5–5%" bracket, no Rate Regime bracket change. |
| **>15% unexplained price move** | **Move found, but explained** | Price rose **+18.0%** ($124.85 → $147.33). Cause identified via web search: continued post-earnings drift following the 26 May beat, a **Guggenheim upgrade to Buy (PT $214, 1 Jun 2026)**, and further analyst commentary/AI-security-narrative support through late June (KeyBanc PT $176, 25 Jun; consensus PT drifted up to ~$192–$212 across sources). This is a documented, fundamentally-grounded continuation (a PEAD-type pattern), not an unexplained move — doesn't independently force an out-of-cycle re-score beyond this already-scheduled one. |

**Conclusion: no *new* Rule 9 trigger fired independent of this scheduled rescore.** The price move has an identified cause. This session's main substantive finding is the **first-ever ZS Quality Score computation** (§5) — new information regardless of Rule 9.

---

## 3. Data Gaps / Flags

1. **Fast-Grower / PEG eligibility — REVISED this session, diverging from 06-20's treatment.** The 06-20 session marked ZS a "CONFIRMED" Fast Grower using a reconstructed **non-GAAP** EPS series ($0.24 → $3.94 TTM) and applied PEG live (15% weight). Re-examining under the 2026-06-20 "clean, non-distorted earnings base" clarification (the DUOL precedent — [decisions/2026-06-20-framework-clarification-peg-clean-earnings.md](../decisions/2026-06-20-framework-clarification-peg-clean-earnings.md)): the clarification's disqualifying examples are a recent IPO, a company **only recently turned GAAP-profitable**, or trailing EPS distorted by a one-off. **ZS is a materially clearer case than any of those — it has never once recorded a GAAP-profitable fiscal year:**
   ```
   FY2022 Net Income  −$390.3M
   FY2023 Net Income  −$202.3M
   FY2024 Net Income   −$57.7M
   FY2025 Net Income   −$41.5M
   TTM    Net Income   −$77.4M   (Q2'26–Q1'27... i.e. quarters ending 2025-07-31 through 2026-04-30)
   ```
   There is no GAAP earnings base to be "clean" or "distorted" — it has simply never existed. The EPS series the 06-20 session and `yfinance`'s own `pegRatio` field are built on is the industry-standard **non-GAAP/adjusted** EPS analysts track, not real GAAP earnings — precisely the kind of adjusted, non-comparable metric this framework treats skeptically elsewhere (see "Adjusted EBITDA" in [glossary.md](../framework/glossary.md)). **PEG's 15% weight is redistributed to EV/EBIT (→ 40%) as the primary treatment this session.** Sensitivity check only (not scored): `yfinance` trailing `pegRatio` = 1.6 → would-be PEG_Score = clamp((1.6−0.5)/2.0×100) = **55.0**; the resulting raw weighted score barely moves (45.80 vs. 45.05 primary) since EV/EBIT is itself only a neutral 50.0 placeholder — flagged transparently rather than silently decided either way.

2. **FCF/Net Income hard-disqualifier — an open interpretive question, not resolved, doesn't change the bottom line.** ZS's FCF/NI ratio is negative every year for 5+ consecutive years (NI has never been positive) — see §5. A **literal** reading of the hard disqualifier ("<70% for 2+ consecutive years without a documented growth-capex explanation") is met, since ZS's modest capex (~6.6% of TTM revenue) isn't a growth-capex story — the GAAP-loss driver is heavy SBC (stock-based compensation), not capex. But this check's evident original intent (per the Valeant/Wirecard precedent in [graveyard-audit.md](../framework/graveyard-audit.md)) is to catch **positive** accounting profit that fails to convert to cash — the opposite pattern from ZS's **negative** accounting profit sitting alongside strongly positive cash generation. Flagged as an unresolved rule-interpretation gap for the framework maintainers; **does not change this session's conclusion**, since the weighted Quality Score (§5) already fails the 80.0+ gate decisively (59.4, a 20.6-point miss) independent of this question.

3. **Moat Signal "scale cost advantage" not credited** — the only citable evidence found ("70% savings on hardware/updates/licensing vs. traditional VPN") traces to Zscaler's own marketing content, not an independent cost-per-unit data source. Declined to credit, consistent with the rigor applied to MSFT's/NOW's own FALSE moat signals in the 2026-07-05 sessions (self-reported vendor claims aren't the "cost-per-unit data" the checklist specifically requires).

4. **`override-log.md` gap — ZS has no actual entry.** ZS has been referred to as "the ZS precedent" for logging a held, quality-gate-failing position as a Human Override (see the 2026-07-05 NOW session's §10) and `watchlist/STALE.md` explicitly says "held as override... see override-log.md" — but `portfolio/override-log.md`'s actual **Override Log** and **Historical Override Audit — Existing Portfolio** tables contain **no ZS row at all**. This looks like a position that has been treated *as if* documented for months (since at least the 06-07/06-11 sessions, which already noted "fails Phase 01 quality gate") without ever actually being logged per the framework's own stated rule ("If a position was opened when... any Phase 01 quality criterion was waived, it is an override. Log it here at time of entry"). **Not resolved here** (out of scope for this rescore — `override-log.md` is not edited by this session) — flagged prominently for the orchestrator/user to remediate.

5. **EV/EBIT placeholder re-verified, unchanged.** TTM GAAP EBIT is still negative (−$29.157M, computed from the last 4 reported quarters) → EV/EBIT remains genuinely undefined → the 06-20 session's neutral 50.0 placeholder treatment is still correct; not an invented number.

---

## 4. ZS — Inputs Collected (fresh this session, `yfinance` via `requests.Session()` + IBKR)

**Sector:** Technology — Cybersecurity (Zero Trust / SaaS)

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 161,709,525 | `yfinance` `sharesOutstanding` |
| **Market Cap** | 161,709,525 × $147.33 = **$23,824.66M** | Computed — matches `yfinance` `marketCap` ($23,824,664,576) essentially exactly |
| Total debt (2026-04-30) | $1,868.16M | `yfinance` quarterly balance sheet |
| Cash + ST investments (2026-04-30) | $3,539.11M | `yfinance` quarterly balance sheet — matches `totalCash` |
| **Net Cash** | $3,539.11M − $1,868.16M = **$1,670.94M** | Computed |
| **EV** | $23,824.66M − $1,670.94M = **$22,153.72M** | Computed — matches `yfinance` `enterpriseValue` ($22,153,719,808) essentially exactly |
| TTM EBIT (Q ending Apr'26–Jul'25) | $0.329M − $19.117M − $6.247M − $4.122M = **−$29.157M** | `yfinance` quarterly financials rollforward — still negative, confirms placeholder treatment (§3 flag 5) |
| TTM EBITDA (same quarters) | $49.786M + $26.941M + $35.037M + $30.218M = **$141.982M** | Same — positive; note `yfinance`'s `info["ebitda"]` field (−$60.8M) disagrees, likely a different definition; the directly-summed quarterly "EBITDA" line items are used for consistency with the 06-20 session's methodology |
| TTM Operating Cash Flow | $198.016M + $204.073M + $448.280M + $250.604M = **$1,100.97M** | `yfinance` quarterly cashflow rollforward — matches `operatingCashflow` |
| TTM CapEx | $62.062M + $34.944M + $34.984M + $78.683M = **$210.67M** | Same |
| **TTM FCF** | $1,100.97M − $210.67M = **$890.30M** | Computed — matches `freeCashflow` |
| **FCF Yield** | $890.30M ÷ $23,824.66M = **3.737%** | Computed |
| TTM Net Income | −$13.883M − $34.312M − $11.615M − $17.578M = **−$77.388M** | `yfinance` quarterly financials rollforward — matches `netIncomeToCommon` |
| TTM Revenue | $850.475M + $815.751M + $788.112M + $719.226M = **$3,173.56M** | Same — matches `totalRevenue` |
| Net Margin (TTM) | −$77.388M ÷ $3,173.56M = **−2.439%** | Computed — matches `profitMargins` (−0.02439) |
| Effective tax used for NOPAT | **21%** statutory rate (FY2025 annual `Tax Rate For Calcs`) — TTM effective rate is not meaningful (Tax Provision is *positive* against a *negative* Pretax Income, the same near-zero-pretax-income distortion documented for CSGP in this framework's 2026-07-04 session) | `yfinance` annual financials |
| **NOPAT** | −$29.157M × (1 − 0.21) = **−$23.034M** | Computed |
| Stockholders' Equity (2026-04-30) | $2,366.60M | `yfinance` quarterly balance sheet |
| **Invested Capital** (Debt + Equity − Cash convention, per [glossary.md](../framework/glossary.md)) | $1,868.16M + $2,366.60M − $3,539.11M = **$695.65M** | Computed |
| **ROIC (TTM)** | −$23.034M ÷ $695.65M = **−3.31%** | Computed — brackets `yfinance`'s `returnOnEquity` (−3.71%) reasonably closely |
| Gross Margin (TTM) | $2,435.28M ÷ $3,173.56M = **76.737%** | Computed — matches `grossMargins` |
| Revenue 3yr CAGR (FY2022 $1,090.95M → FY2025 $2,673.12M) | (2,673.12/1,090.95)^(1/3) − 1 = **34.81%** | `yfinance` annual financials — matches 06-20 session |
| Revenue growth trend (deceleration evidence) | Trailing 3yr CAGR 34.8% → most recent quarter YoY 25.4% (Apr'26 vs Apr'25, matches `revenueGrowth`) → FY2026 consensus +24.64% YoY → FY2027 consensus +17.02% YoY | `yfinance` `revenue_estimate`/`growth_estimates` — a consistent, multi-point, forward-documented deceleration, not a single cyclical blip |
| Forward EPS (NTM, non-GAAP consensus) | $4.597 | `yfinance` `forwardEps` / `earnings_estimate` "+1y" |
| **Forward PE** | $147.33 ÷ $4.597 = **32.048×** | Computed — matches `yfinance` `forwardPE` |
| 5yr avg/range PE (non-GAAP EPS reconstruction, 20 quarters) | avg **161.3×** (bubble-distorted by 2021–22 SaaS peaks) | `get_earnings_dates` + price-history reconstruction |
| 3yr post-bubble avg/range PE (12 quarters) | avg **67.02×**, range 32.08×–89.75× | Same — used as the representative benchmark, per the 06-20 session's established (and re-verified) reasoning: the raw 5yr average is bubble-distorted |
| FCF/NI conversion (TTM) | $890.30M ÷ −$77.388M = **−1150.5%** | Computed — negative because NI is negative, not because cash conversion is poor; see §3 flag 2 |
| Diluted avg shares (FY2022 → FY2025) | 140.895M → 154.404M | `yfinance` annual financials — CAGR = (154.404/140.895)^(1/3)−1 = **+3.10%/yr** dilution (SBC-driven) |
| Dividend yield | None (no dividend) | `yfinance` |

---

## 5. ZS — Quality Score (first-ever computation, 2026-06-29 methodology)

**Hard disqualifier check (all must pass before the weighted score matters):**

| Check | Value | Threshold | Result |
|---|---|---|---|
| FCF/NI conversion <70% for 2+ yrs unexplained? | Ratio negative every year FY2022–2025 and TTM (NI has never been positive) | disqualify if <70% for 2+ yrs *without* a growth-capex explanation | ⚠️ **Ambiguous — literally met, but see §3 flag 2.** ZS's capex is modest (~6.6% of TTM revenue), so no growth-capex explanation applies; the actual GAAP-loss driver is SBC. A strict literal reading disqualifies ZS here; the rule's evident original intent (catching *positive* NI that fails to convert to cash) doesn't obviously fit this reverse pattern. **Flagged, not resolved — doesn't change the outcome below either way.** |
| Net Debt/EBITDA over threshold? | **Net cash** ($1,670.94M net cash vs. $141.98M TTM EBITDA) | disqualify if >2.5× | ✅ PASS, comfortably |
| FCF-positive 3+ consecutive years? | FCF-positive every year FY2022–2025 ($231.3M / $333.6M / $585.0M / $726.7M) and TTM ($890.3M) | disqualify if not | ✅ PASS |

Proceeding to the weighted score (the ambiguous check above doesn't change the conclusion — see below).

### Profitability (25% weight)

```
Net Margin (TTM)     = −2.439%
NetMargin_Component  = clamp((−2.439/30)×100, 0, 100) = 0.0   (negative, floored)

ROIC (TTM)            = −3.31%
ROIC_Component        = clamp((−3.31/30)×100, 0, 100) = 0.0   (negative, floored)

Profitability_Score   = (0.0 + 0.0) / 2 = 0.0
```
FCF-positive-3yr cap (max 40.0) doesn't bind — ZS is FCF-positive every year on record; the cap only lowers a score, and 0.0 is already below it.

### Margins (15% weight)

```
Gross Margin (TTM) = 76.737%
GrossMargin_Score = clamp((76.737/80)×100, 0, 100) = 95.92
```
No structural-trend bonus applicable — gross margin is already well above the 40% threshold the bonus targets.

### Growth (20% weight)

```
Revenue 3yr CAGR (FY2022 $1,090.95M → FY2025 $2,673.12M) = 34.81%
Growth_Score (raw) = clamp((34.81/25)×100, 0, 100) = clamp(139.24, 0, 100) = 100.0
```
**−10 (documented structural deceleration, cited):** trailing 3yr CAGR 34.8% → most recent actual quarter YoY 25.4% → FY2026 consensus +24.6% → FY2027 consensus +17.0% (all four points from `yfinance` financials/estimates, §4). A consistent multi-point deceleration trend across trailing actuals and two forward consensus years — not a single cyclical quarter.
```
Growth_Score (with modifier) = clamp(100.0 − 10, 0, 100) = 90.0
```
(A +10 TAM-expansion credit was not separately pursued — the raw score already saturates the 0–100 ceiling before any modifier, so it would not change the net number.)

### Balance Sheet (15% weight)

```
Net Debt/EBITDA = −$1,670.94M / $141.982M = −11.77× (net cash)
BalanceSheet_Score = clamp(100×(1 − (−11.77)/4), 0, 100) = clamp(394.25, 0, 100) = 100.0
```
Standard /4 denominator — ZS isn't a payment network/exchange, the Upgrade 5 override doesn't apply (and isn't needed regardless, given the net-cash position).

### Moat Signal (15% weight) — checklist, cited evidence per signal

| Signal | Marked | Cited evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Zscaler is a **Leader in Gartner's Magic Quadrant for Security Service Edge (SSE) for the 4th consecutive year**, and reports **9,400+ enterprise customers** as of fiscal Q4 2025 — one of the largest deployed bases in the Zero Trust Network Access category. [Gartner MQ SSE page](https://www.zscaler.com/gartner-magic-quadrant-security-service-edge-sse); [Luminix Zscaler 2026 overview](https://www.useluminix.com/reports/company-overviews/zscaler-company-overview-zero-trust-security-platform-financials-and-market-position-2026) |
| Brand premium | **TRUE** | Zscaler implemented **35%+ list-price increases** on core SKUs (effective Aug 2025) affecting both new and renewing customers, while **Dollar-Based Net Retention stayed at 114% TTM** — evidence customers absorbed a real price increase rather than churning, a genuine (if margin-costly, see below) pricing-power signal. [NPI Financial — Zscaler price increase](https://www.npifinancial.com/knowledge-center/zscalers-price-increase-what-informed-it-buyers-are-doing-to-stay-ahead/) |
| Network effect | **TRUE** | Documented data-network-effect mechanism: Zscaler processes **500B+ daily transactions / 500T+ telemetry signals** across its customer base; threat intelligence gathered from one customer's traffic improves detection for all others in real time — a "more data → better product → more customers" flywheel, distinct from a classic two-sided marketplace but matching the checklist's "user-growth-driven value" criterion. [Sergeycyw — Zscaler Zero Trust market analysis](https://sergeycyw.substack.com/p/zscaler-leading-zero-trust-security) |
| Switching costs | **TRUE** | Documented mechanism: deep integration into an enterprise's network/identity architecture creates **vendor lock-in** — migrating away is "complex and costly" given the investment already sunk into onboarding — reinforced by standard **12–36-month enterprise contracts**. [Portnox — What is Zscaler?](https://www.portnox.com/cybersecurity-101/general-security/what-is-zscaler/); [Venn — Zscaler pricing](https://www.venn.com/learn/zscaler-pricing/) |
| Scale cost advantage | **FALSE** | The only figure found ("70% savings vs. traditional VPN") is Zscaler's own marketing claim, not independent cost-per-unit data showing a gap vs. smaller competitors — declined to credit, consistent with the rigor applied to MSFT's/NOW's own FALSE moat signals in the 2026-07-05 sessions. [Zscaler — "How to Cut IT Costs"](https://www.zscaler.com/blogs/product-insights/how-cut-it-costs-zscaler-part-1-enhancing-security-posture) (not credited) |

```
Moat_Score = (4/5) × 100 = 80.0
```

### FCF Quality (10% weight)

```
FCF/NI (TTM) = $890.30M / −$77.388M = −1150.5%
FCFQuality_Score = clamp(((−11.505 − 0.40)/0.60)×100, 0, 100) = clamp(−1984.2, 0, 100) = 0.0
```
Flagged: this 0.0 is a **mechanical artifact** of a negative denominator (NI), not evidence of poor cash conversion — ZS actually converts operating performance to cash exceptionally well ($890M TTM FCF against a small GAAP loss). The formula wasn't designed with a negative-NI base in mind; shown as computed, per "never invent," but the number should not be read as "FCF quality is terrible."

### Quality Score — Final

```
Quality Score = (0.0×0.25) + (95.92×0.15) + (90.0×0.20) + (100.0×0.15) + (80.0×0.15) + (0.0×0.10)
              = 0.000 + 14.388 + 18.000 + 15.000 + 12.000 + 0.000
              = 59.388 → rounds to 59.4
```

# Quality Score = 59.4 — FAILS the 80.0+ gate (by 20.6 points — a decisive miss, not a close call).

**This is ZS's first-ever computed Quality Score.** Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all."* Per [rescore.md](../.claude/commands/rescore.md) step 3, a held position dropping below the gate is a signal worth surfacing but doesn't force an exit on its own. **This is not new deterioration** — ZS has been known/flagged as failing the (old, ad hoc) Phase 01 GAAP quality gate since at least the 06-07 session; this is the first time that known condition has been formally, granularly quantified under the new engine. Per the established practice for existing holdings whose Quality Score fails the gate (AMZN/GOOG/MSFT/NOW/NKE 2026-07 sessions), the Valuation Score and a **reference-only** Composite Score are still computed below, explicitly flagged as not to be acted on at face value.

**Consistency check against the original override rationale (§3 flag 4's missing entry notwithstanding):** the prior sessions' stated basis for the GAAP quality-gate fail was "negative net margin/ROIC despite strong FCF and gross margin." The new engine's Profitability_Score (0.0, driven by the same negative net margin/ROIC) **confirms and corroborates that exact basis** — no divergence there. But the new engine also surfaces **two additional, previously-unquantified drags** that the old ad hoc GAAP check never scored: a documented growth-deceleration penalty (Growth_Score 90.0 vs. a would-be 100.0) and a mechanically-zero FCF Quality sub-score (§ above). Net effect: **the new engine's verdict is directionally consistent with the original override basis, but decisively broader and more negative** (59.4, a 20.6-point miss) than a single-metric "GAAP loss" read might have suggested. On the specific question of whether the new engine credits ZS's **SaaS-style non-GAAP profitability story** any differently than the old ad hoc check: **no** — both are GAAP-based (Net Margin%, ROIC% inputs), and Upgrade 1's Owner Earnings treatment is explicitly limited to MSFT/GOOGL/META/AMZN, not extended to ZS. The framework gives non-GAAP profitability **zero credit** in either version.

---

## 6. ZS — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 32.048 = 3.1203%
Spread = EY − 10Y Treasury = 3.1203% − 4.485% = −1.3647%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−1.36%, ~2.86pp short) → **+5 additive**.

**Step 2 — Rate Regime Modifier**
10Y = 4.485% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for ZS = +10**

---

## 7. ZS — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 3.737/10), 0, 100) = 62.63
```
→ Contribution: 62.63 × 0.40 = **25.052**

**EV/EBIT — 25% + 15% (PEG redistributed, §3 flag 1) = 40% weight**
```
EV/EBIT_Score = 50.0  (neutral placeholder — TTM GAAP EBIT still negative, −$29.157M, re-verified §3 flag 5)
```
→ Contribution: 50.0 × 0.40 = **20.000**

**Forward PE (fallback formula — 3yr post-bubble avg) — 20% weight**
```
Deviation% = (32.048 − 67.02)/67.02 × 100 = −52.18%
FwdPE_Score = clamp(50 + (−52.18)×2.5, 0, 100) = clamp(−80.46, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — 15% weight: N/A this session** (not a qualifying Fast Grower — ZS has never had a GAAP-profitable year, §3 flag 1) — weight redistributed to EV/EBIT above.
*Sensitivity only (not scored):* `yfinance` trailing `pegRatio` = **1.6** → would-be PEG_Score = clamp((1.6−0.5)/2.0×100) = **55.0** → alternate raw weighted = 62.63×0.40 + 50.0×0.25 + 0.0×0.20 + 55.0×0.15 = 25.05+12.50+0.0+8.25 = **45.80** (vs. 45.05 primary — an immaterial difference, since EV/EBIT is itself only a placeholder either way).

**Raw weighted score (primary treatment):**
```
= 25.052 + 20.000 + 0.0 = 45.052
```
**+ Rate Modifier (+10) = 55.052** (before the Upside/Downside Modifier)

---

## 8. ZS — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario architecture (Rule 7 bull/base/bear), built from live consensus data (§4):**

| Scenario | Weight | EPS (non-GAAP consensus) | Exit multiple | Rationale | Fair Value |
|---|---|---|---|---|---|
| **Bull** | 25% | $5.42 (FY+1 high estimate) | ~46× | Growth re-accelerates, AI-security narrative sustains a partial re-rate toward (not to) the 67× 3yr average; anchored to, not exceeding, the $250 analyst high PT (Rule 7 guardrail — never the rosy point). | **$250** |
| **Base** | 50% | $4.597 (FY+1 avg estimate) | ~40.7× | Consensus path; multiple sits between the current 32× trough and the 67× 3yr average, close to the $187.50 analyst median PT. | **$187** |
| **Bear** | 25% | $3.96 (FY+1 low estimate) | ~32× (no re-rating credit — current trough multiple held) | Growth decelerates further along the already-documented trend (§5 Growth); multiple compresses to today's cycle low, no recovery. Sits *below* the $145 analyst low PT — an honestly underwritten downside (Rule 7 guardrail). | **$127** |

```
PW Fair Value = 0.25×250 + 0.50×187 + 0.25×127 = 62.5 + 93.5 + 31.75 = $187.75
```
Sanity check (Rule 4): base ($187) sits almost exactly at the analyst median ($187.50); bull ($250) matches the analyst high PT exactly, not exceeding it; bear ($127) sits below the analyst low PT ($145) and the current price — appropriately conservative downside underwriting.

**Step 1 — Expected annual return E.**
```
Gap Upside %      = (187.75 ÷ 147.33) − 1                = +27.437%
Catalyst window   = 2 years (Rule 10 default — no narrower window; ongoing Zero Trust/SASE
                    adoption cycle, Gartner projecting 80% of enterprises on SASE/ZTNA by 2026
                    up from ~20%, plus the routine Sep 2026 earnings checkpoint)
Annualized gap    = 27.437% ÷ 2                            = +13.72%/yr
Intrinsic growth  = +11.37%/yr  (FY+1 consensus EPS growth, `yfinance` growth_estimates —
                    a directly-sourced figure, not an inferred "conservative deceleration" estimate)
Shareholder yield = −3.10%/yr  (no dividend; diluted share count CAGR FY2022→FY2025 = +3.10%/yr
                    from SBC-driven dilution → negative buyback yield, honestly counted)

E = 13.72% + 11.37% + (−3.10%) = +21.99%/yr ≈ +22.0%/yr
```

**Step 2 — Map E to the modifier (hurdle H = 10%).**
```
E = 22.0% ≥ H  →  M = −15 × clamp((22.0 − 10)/15, 0, 1) = −15 × clamp(0.800, 0, 1) = −15 × 0.800 = −12.0
```
**Modifier M = −12.0** — a smaller (less attractive) modifier than 06-20's floored −15.0: the price rally (+18.0% since 06-20) narrowed the gap to a *higher* fair value (updated bull/base/bear anchors rose alongside consensus estimates and PTs), so the forward-looking case, while still attractive, is no longer at the bound.

**Guardrail checks:**
1. **Catalyst:** documented (Zero Trust/SASE adoption cycle within Rule 10's 18–24mo window, plus quarterly earnings checkpoints) → upside credit allowed, not capped at −5. ✓
2. **Scenario-weighted, not the rosy point:** PW FV ($187.75) sits near, not above, the analyst median; bull matches (not exceeds) the analyst high PT; bear sits below the analyst low PT. ✓
3. **Full calc shown** (above). ✓
4. **Bounded ±15:** −12.0 sits within bounds, off the floor this session. ✓

---

## 9. ZS — Final Valuation Score, Quality Score, and Composite Score

```
FINAL VALUATION SCORE = Raw weighted (45.052) + Rate Modifier (+10) + Upside/Downside (−12.0)
                       = 43.052
```
Boundary rule: 43.052 is closer to 43.1 than 43.0 under ordinary rounding → **Final Valuation Score = 43.1**

| | Value |
|---|---|
| Raw weighted | 45.052 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −12.0 (E = +22.0%) |
| **FINAL VALUATION SCORE** | **43.1** |
| Prior valuation score | 36.3 (06-20) |
| **Quality Score** | **59.4 (FAILS 80.0+ gate by 20.6 points — see §5)** |

**Valuation Score band: 43.1 → 30.0–49.9 "Cheap" → nominally BUY, Standard 3–5%** — but see §10: this is gated independently by (a) the Quality Score fail, (b) R/R discipline, and (c) the pre-existing override status.

**Composite Score — reference only, per the established practice for a Quality-Score-gate failure on an existing holding (AMZN/GOOG/MSFT/NOW/NKE 2026-07 sessions):**
```
Composite Score = 0.50×(100 − 59.4) + 0.50×43.1 = 0.50×40.6 + 0.50×43.1 = 20.3 + 21.55 = 41.85 → rounds to 41.9
```
**Composite Score = 41.9 — lands in the "BUY — Standard position 3–5%" band (30.0–49.9), the same nominal band as the raw Valuation Score.** This is precisely the kind of **false green light this practice exists to flag**: blending in a decisively failed-gate Quality Score (59.4, 20.6 points below 80.0) still produces a numerically-attractive blended figure. **This Composite Score is NOT being adopted to drive the action recommendation below** — shown only for the record, per "no black box," mirroring the MSFT/NOW/AMZN/GOOG 2026-07-05 treatment.

---

## 10. ZS — Action Recommendation

**Three independent facts, any one of which alone is enough to conclude HOLD/no-add:**

1. **Quality Score (59.4) fails the 80.0+ gate decisively** (20.6 points below the bar) — per [quality-scoring.md](../framework/quality-scoring.md), a company below 80.0 doesn't proceed to a valuation-driven add "regardless of how cheap the stock looks."
2. **ZS is a pre-existing Human Override** for exactly this quality-gate fail (though see §3 flag 4 — the actual log entry documenting it is missing) — any *addition* to this position, beyond the existing 0.24%, would itself need fresh override documentation and explicit human sign-off, not just a favorable score.
3. **Order-setup R/R independently fails the 2:1 minimum anyway** (shown below for completeness) — so even setting aside the Quality Score question entirely, the disciplined entry math alone blocks a buy at current levels.

**Order setup — shown for completeness, testing the nominal Buy-Standard (30.0–49.9) band on the raw Valuation Score:**
```
Blended Fair Value (= PW FV):              $187.75
Margin of Safety (30.0–49.9 band, top of range given persistent GAAP losses,
  consistent with the 06-20 session's reasoning): 30%
BUY PRICE (limit):                         $187.75 × (1 − 0.30) = $131.43
PRIMARY SELL TARGET:                       $187.75
BULL-CASE TRIM TARGET (bull × 0.90):       $250 × 0.90 = $225.00
STOP LOSS (Buy × (1 − 28%)):               $131.43 × 0.72 = $94.63
R/R at formal entry = (187.75 − 131.43) ÷ (131.43 − 94.63) = 56.32 ÷ 36.80 = 1.53:1  ❌ below 2:1
R/R at live price   = (187.75 − 147.33) ÷ (147.33 − 94.63) = 40.42 ÷ 52.70 = 0.767:1  ❌ far below 2:1
```
To clear 2:1 at a 28% stop, entry would need to be ≈**$120.35** (≈36% MoS) — near, but not quite at, the 52-week low ($114.625). **Both R/R checks fail the 2:1 minimum (Rule 6) — do not enter, independent of the Quality Score question.**

**Net: HOLD the existing 0.24% override position. No fresh capital added** — blocked by three independent gates (Quality Score, override status, and R/R), the same practical conclusion as the 06-20 session, now with the Quality Score question formally quantified for the first time and the override-log documentation gap surfaced (§3 flag 4).

**No trim recommended either** — the position isn't overvalued (Valuation Score 43.1 sits in "Cheap," not an expensive band), and the framework's rules don't force an exit or trim on a quality-gate fail alone for an existing holding (per [rescore.md](../.claude/commands/rescore.md) step 3 and [strategy.md](../framework/strategy.md) Phase 06 — none of the four valid exit triggers apply here).

**Recommend the user/orchestrator remediate the `override-log.md` gap** (§3 flag 4) by adding a proper, retroactive Human Override entry for ZS — this session does not do so (out of scope; `override-log.md` is not edited here).

---

## 11. Next Review Trigger

- **Routine:** ZS fiscal Q4 2026 earnings, confirmed **2 Sep 2026** — will refresh every TTM fundamental used here and is the natural point to re-run the Quality Score with a fresh TTM window.
- **Open item (new, highest priority): the missing `override-log.md` entry (§3 flag 4)** — recommend the orchestrator add a retroactive Human Override entry for ZS.
- **Open interpretive item (unresolved, flagged not fixed):** whether the FCF/Net Income hard disqualifier should mechanically apply to a negative-NI/positive-FCF profile like ZS's, or whether its intent (catching inflated positive NI that fails to convert to cash) doesn't fit this reverse case (§3 flag 2) — doesn't change this session's conclusion but worth a `decisions/` entry if it recurs on other loss-making SaaS names.
- **Watch:** if price pulls back toward ≈$120 (restoring ≥2:1 R/R against the unchanged-methodology PW Fair Value) the entry math would clear — but the Quality Score gate and override status would still independently block a fresh add regardless.
- **Rule 9 triggers (standing):** guidance revision, M&A, management change, a >15% *unexplained* price move, or the 2 Sep 2026 earnings print itself.

---

## Glossary

| Term | Meaning |
|---|---|
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking combining Quality and Valuation Scores 50/50 — computed only for companies clearing the 80.0+ Quality Score gate; shown as a **reference-only, not-adopted** number for ZS this session (59.4 Quality Score fails the gate). |
| **D&A** | Depreciation & Amortization. |
| **DBNR (Dollar-Based Net Retention)** | The percentage of a subscription cohort's revenue retained/expanded a year later — 114% means the same customer base is spending 14% more, net of churn and downgrades. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean earnings base — this framework's PEG-eligibility trigger; ZS does not qualify this session, having never had a GAAP-profitable year (§3 flag 1). |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook. |
| **Hard disqualifier** | A Quality Score condition that fails a company regardless of weighted score. |
| **Human Override** | A position held outside the framework's own rules — meant to be tracked in `override-log.md`; ZS is treated as one but this session found no actual logged entry (§3 flag 4). |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | The total capital (debt + equity, netted for cash) put to work in a business — the denominator of ROIC. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt; negative means net cash. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **Net Margin** | Net Income ÷ Revenue. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **Non-GAAP / adjusted EPS** | Earnings per share with stock-based compensation and other items stripped out — the figure management and analysts headline; distinct from, and not directly comparable to, real GAAP earnings. |
| **NTM** | Next Twelve Months. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PEAD (Post-Earnings Announcement Drift)** | The documented tendency for a stock to keep drifting in the direction of an earnings surprise for weeks afterward. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02/Composite Score. ZS's first-ever computation this session: 59.4 (fails the gate by 20.6 points). |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0 / Rule 6 / Rule 9 / Rule 10** | This framework's standing instructions to always fetch a live price first; require a minimum 2:1 risk/reward before entering; force re-valuation on specific fundamental triggers; and separate intrinsic value from market price with a documented catalyst and timeline. |
| **SaaS (Software-as-a-Service)** | A software delivery model where customers pay a recurring subscription to access hosted software. |
| **SASE (Secure Access Service Edge)** | A network-security architecture combining networking and security functions into a single cloud-delivered service — the broader market category Zero Trust Network Access sits within. |
| **SBC (Stock-Based Compensation)** | Employee pay in company shares/options — a non-cash expense that lowers GAAP net income and dilutes existing shareholders, added back in cash-flow statements. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TAM** | Total Addressable Market. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs. the 10% hurdle. |
| **Zero Trust** | A security model that assumes no user or device is inherently trustworthy and continuously verifies every access request, regardless of network location — Zscaler's core product category. |
| **ZTNA (Zero Trust Network Access)** | The specific product category implementing Zero Trust principles for network access — the market Zscaler competes in. |
