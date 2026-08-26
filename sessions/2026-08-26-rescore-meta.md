# RESCORE — META — 2026-08-26

**Task type:** RESCORE (single ticker) — **Telegram-triggered** (Routine 6 / `/telegram-scan`), unattended scheduled run — **P1 priority** (held position, per automation-schedule.md)
**Trigger:** New post [t.me/tarasguk/11775](https://t.me/tarasguk/11775) (2026-08-26 06:40:32 UTC): "$META stated that the states which had filed lawsuits against the company over harmful impact on teenagers have expressed a desire to reach a settlement" (translated from Ukrainian). Per CLAUDE.md Rule 0, the post's text is used only as a *trigger* — every figure below is independently re-pulled from Yahoo Finance data feeds (yfinance's own backing API, accessed directly after a local `curl_cffi` TLS-fingerprint failure — see §0), SEC EDGAR filings, wire coverage, and stockanalysis.com, not from the post.
**Date:** 26 Aug 2026
**10Y US Treasury Yield:** 4.65% (TradingEconomics.com, "current" as of 26 Aug 2026; cross-checked via Yahoo `^TNX` index quote — 4.639% regularMarketPrice, 4.653% previous close, timestamp 2026-08-25 ~19:00 UTC — both inside the same "3.5–5%" bracket. Down slightly from 4.70% used 08-05, same bracket → Rate Regime Modifier Step 2 unchanged at +5.)
**Rate Regime Modifier (Step 2):** +5
**Last review on record:** META **41.2** (2026-08-05, Composite 26.9, Quality 87.5, BUY — Full position 6–8% — [sessions/2026-08-05-rescore-meta.md](2026-08-05-rescore-meta.md))
**Gap since last review:** 21 days.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; NOPAT = net operating profit after tax; ROIC = return on invested capital; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; pp = percentage points; EY = earnings yield (1 ÷ PE); TTM = trailing twelve months; NTM = next twelve months; 10-Q = quarterly SEC filing; 8-K = SEC "current report" filing.*

---

## 0. Data-Source Note — `yfinance`/`curl_cffi` connection failure, worked around

The installed `yfinance` package (1.6.0, `curl_cffi` 0.16.2 backend) failed this session with a TLS-layer error (`curl: (35) Recv failure: Connection reset by peer`) on every call, including plain unauthenticated requests to `query1.finance.yahoo.com` with `curl_cffi`'s browser-impersonation mode — this environment's egress proxy re-terminates TLS, and `curl_cffi`'s raw-socket browser-fingerprint spoofing does not tunnel cleanly through that MITM layer (confirmed: plain Python `requests`, which doesn't do TLS fingerprint spoofing, reaches the same Yahoo endpoints without error). **Worked around, not skipped:** used `requests` directly against the same backing endpoints `yfinance` itself calls (`v10/finance/quoteSummary`, `ws/fundamentals-timeseries/v1/finance/timeseries`, `v1/test/getcrumb` for the anti-bot cookie/crumb), pulling the identical underlying data `yfinance`'s own Python wrapper would have returned — not a different, lower-quality source. Cross-checked price against stockanalysis.com and Google Finance (§1). This is a repo environment/library issue, not a data-quality substitution — flagged for the record per "never invent or estimate data," but no gap in the actual financial inputs resulted.

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$570.05** | Yahoo Finance `price` module (`regularMarketPrice`), regular-session close 2026-08-25 16:00:01 ET (20:00:01 UTC) — market had **not yet opened** for 2026-08-26 at the time of this session (Telegram trigger fired 06:40 UTC, well before the 13:30 UTC / 9:30am ET open), so the most recent actual trade is this prior close, not a same-day intraday print |
| Cross-check | $570.05 (stockanalysis.com, "+1.97% at close Aug 25, 2026") / $570.05 (Google Finance) | WebFetch of both — all three sources agree exactly |
| Pre-market indication (context only, not used in scoring) | $573.77–$574.00 (+0.65–0.69%), ~4:13am ET / 08:13 UTC 2026-08-26 | stockanalysis.com + Google Finance WebFetch — thin pre-market volume, not a regular-session print; noted directionally only, consistent with how this repo treats after-hours/pre-market quotes elsewhere (e.g. 08-05 session's after-hours note) |
| 52-week range | **$520.26 – $790.80** | Yahoo `summaryDetail` |
| YTD / vs 08-05 | $584.48 (08-05 close) → $570.05 today = **−2.47%** over 21 days | Computed |
| Analyst consensus PT | **$754.84** (62 analysts, "Strong Buy") | stockanalysis.com WebFetch — bull-case sanity check only (Rule 0 Step 4) |

---

## 2. Rule 9 Trigger Check (2026-08-05 → 2026-08-26) — Independent Verification of the Trigger Post

| Trigger | Found? | Detail |
|---|---|---|
| **Teen-safety lawsuit settlement talks (the post's claim)** | **Confirmed as real, wire-reported news — but NOT an official Meta statement, and NOT a settlement** | Independently verified via **Bloomberg** ("Meta, States Have Discussed Settling Teen Social Media Case," 2026-08-25), syndicated on Yahoo Finance, and picked up by Benzinga and multiple radio-station wire feeds. Per people familiar with the matter (unnamed sources, **not** an official Meta or state-AG statement): Meta and 29 state attorneys general (lead states California, Colorado, Kentucky, New Jersey) have held **preliminary discussions** about a possible **mid-trial** settlement of the federal case (now in its second week in Oakland, CA) alleging Facebook/Instagram were designed to addict teens. **No settlement has been reached.** Meta's own spokesperson gave "no immediate comment" on the settlement-talks report; Meta has previously and separately called the states' ask (up to **$1.4 trillion** by Meta's own estimate) "unreasonable" and an "outlandish payout." Mark Zuckerberg is expected to testify; Instagram head Adam Mosseri already has. **The Telegram post's core claim is independently verified true as a matter of wire reporting** (Bloomberg did report exactly this), but the underlying event itself is *discussions*, not a settlement, official filing, or company-confirmed disclosure. |
| **Does this clear the Rule 9 bar?** | **NO** | Rule 9 ([fair-value-methodology.md](../framework/fair-value-methodology.md)) enumerates: quarterly earnings, guidance revision, management change, material M&A, macro shift, >15% unexplained price move, or a credible short report. Unconfirmed, sourced-anonymously, mid-trial settlement *discussions* in an ongoing lawsuit fit none of these categories — no financial figure is disclosed or quantifiable (no accrual, no guidance change, no settlement terms), and Meta itself declined to confirm. **Same treatment as this ticker's own precedent**: the 07-09 session (Zuckerberg's on-the-record "may make sense" compute-leasing quote) and 07-13 session (Bloomberg's $250B capex estimate) were both found **not** to clear the Rule 9 bar for materially the same reason — real, sourced news, but not one of the enumerated trigger categories, and not yet a company-confirmed, quantifiable event. Session proceeds as a **routine re-check** (21 days since last review, price/consensus moved), not a triggered event. |
| **Quarterly earnings** | **NO — confirmed not yet due** | Task instructions correctly anticipated this: Meta's next scheduled print is **Q3 2026, typically late October/early November 2026**. Independently confirmed via SEC EDGAR search — the most recent Meta 8-K on file is still the 2026-07-29 Q2 2026 results filing; no new 8-K since. |
| **Guidance revision** | No | No new guidance issued since the 07-29 Q2 print (already captured in the 08-05 session). |
| Material M&A / JV | No new one | No new disclosure this window. |
| Management change | No | None found (searched explicitly). |
| Macro shift | No | 10Y ticked 4.70%→4.65%, still inside the "3.5–5%" bracket. |
| >15% unexplained price move | No | −2.47% over 21 days, in line with general market drift — not unexplained, not close to the 15% threshold. |

**Conclusion: Rule 9 trigger NOT independently confirmed as a scoreable event** (the settlement-talks story is real but doesn't meet any enumerated Rule 9 category, and no other trigger fired in this window). Proceeding as a routine 21-day re-check, consistent with this ticker's established practice of re-scoring on a Telegram-scan cadence even when the specific trigger claim doesn't independently clear the bar (see 07-09, 07-13 precedent).

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** **4.51%** (per [holdings.md](../portfolio/holdings.md), synced 2026-08-22 — down from 6.43% on 08-05 because the **Freedom24 broker leg of this position was sold** (confirmed 2026-08-22 sync), leaving only the IBKR leg; a portfolio-sync event, not a scored-input change, and out of `/rescore`'s scope to investigate further).

### TTM fundamentals — carried unchanged from 08-05 (no new fiscal quarter has reported; independently cross-verified fresh this session)

Because Q3 2026 earnings are confirmed not yet due (§2), the trailing-twelve-month window is still **Q3 2025 + Q4 2025 + Q1 2026 + Q2 2026** — identical to the 08-05 session. A fresh pull this session (via the workaround in §0) reproduced every one of these figures to the dollar, confirming no restatement occurred:

| Item | Value | Cross-check vs 08-05 |
|---|---|---|
| TTM Revenue | $228.247B | Matches exactly (51.242+59.893+56.311+60.801) |
| TTM Net Income | $68.098B | Matches exactly (2.709+22.768+26.773+15.848) |
| TTM EBITDA | $112.282B | Matches exactly (26.853+31.221+28.313+25.895) |
| TTM FCF | $40.976B | Matches exactly (11.170+14.831+13.229+1.746) |
| Gross profit (TTM) | $186.587B | Matches exactly (42.036+48.987+46.093+49.471) → Gross margin 81.7478% |
| Cash + marketable securities (30 Jun 2026) | $90.26B | Matches |
| Senior-note debt, excl. leases (30 Jun 2026) | $83.664B | Matches |
| Net cash | $6.596B | Matches |
| Total Stockholders' Equity (30 Jun 2026) | $261.221B | Matches |
| Buyback (TTM) | $3.327B | Matches — still $0 for 3 of the 4 TTM quarters (Q4'25/Q1'26/Q2'26); buyback suspension unchanged |
| Dividend (TTM) | $5.367B | Matches |

🚩 One data-quality note: Yahoo's raw `quarterlyEBIT` timeseries field (this session's fresh pull) diverges from the operating-income figures the 08-05 session verified directly against Meta's own 10-Q / press release (e.g. Q2 2026: Yahoo-derived field shows $19.539B vs. the 10-Q-verified $18.775B GAAP operating income — Yahoo's field appears to be pretax income + interest expense, which can diverge from GAAP operating income when a company carries material non-operating items, as Meta does via its equity-method investments). **Continuing to use the 10-Q-verified TTM EBIT ($86.927B) as the authoritative basis**, not Yahoo's diverging derived field — flagged explicitly per "never invent or estimate," this is a real discrepancy between two sourced figures, resolved in favor of the one independently matched to the filed financial statement.

**Shares outstanding: 2,548,378,209** (carried forward per the corrected Class A + Class B total established 08-05 — no new 10-Q to update this from; Yahoo's `quarterlyOrdinarySharesNumber` fresh pull this session shows 2,548,377,716 as of 30 Jun 2026, essentially identical, off by 493 shares / immaterial rounding).

### Refreshed this session (price/consensus-dependent)

| Item | 08-05 value | 08-26 value (fresh) | Computation |
|---|---|---|---|
| Live price | $584.48 | **$570.05** | §1 |
| Market Cap | $1,489.4761B | **$1,452.7030B** | 2,548,378,209 × $570.05 |
| EV | $1,482.8801B | **$1,446.1070B** | $1,452.7030B − $6.596B net cash |
| **EV/EBIT** | 17.0589× | **16.6359×** | $1,446.1070B ÷ $86.927B |
| **FCF Yield** | 2.7510% | **2.8207%** | $40.976B ÷ $1,452.7030B |
| Forward EPS (FY2026 consensus) | $30.93 | **$31.16** | stockanalysis.com, S&P Global consensus, 55 analysts, updated 2026-08-25 (up slightly from $30.93 — modest upward EPS revisions since the post-earnings trough) |
| Forward PE | 18.8969× | **18.2943×** | $570.05 ÷ $31.16 |
| 5yr avg/range PE (auto-reconstructed) | 23.152× (range 9.255×–36.014×, n=20q) | **Carried unchanged — 23.152× / 9.255×–36.014×, n=20q** | No new quarterly earnings date since 07-29 2026 to shift the 20-quarter reconstruction window (see §0 for why the live re-derivation itself wasn't re-run: the `curl_cffi`-based `get_earnings_dates` pipeline documented in valuation-scoring.md needs the same library that failed in §0; the underlying inputs — historical quarterly EPS/price pairs — are unchanged regardless, since no new earnings date exists to add and the oldest quarter in the trailing-20 window hasn't rolled off either) |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

No new fiscal year has completed since 08-05 (FY2025 diluted EPS still the most recent complete year: $8.59→$14.87→$23.86→**$23.49, −1.55%**). Most recent fiscal year still negative — **still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base." **PEG not applicable; its 15% weight redistributed to EV/EBIT** — unchanged.

---

## 4. Data Gaps / Flags

1. **`yfinance`/`curl_cffi` TLS failure, worked around (§0)** — not a data gap in the financial inputs (same underlying Yahoo data reached via a direct-`requests` workaround, cross-checked against two independent quote sites for price), but flagged as an environment issue worth a maintainer follow-up (the installed `curl_cffi` 0.16.2 doesn't tunnel through this environment's TLS-interception egress proxy).
2. **Owner Earnings (Upgrade 1) — still unresolved.** Meta's most recent 10-Q (Q2 2026, unchanged since 08-05) still does not disclose a maintenance-vs-growth capex split. Raw FCF continues to be used, as in every prior META session.
3. **Yahoo `quarterlyEBIT` field discrepancy (§3)** — resolved in favor of the 10-Q-verified figure, not invented, but flagged as a live-data-quality gap worth noting for future sessions using this workaround.
4. **5yr PE range not independently re-derived this session** (carried forward, §3) — justified because no new earnings date exists to shift the reconstruction window, not because the derivation was skipped for convenience. Should be re-run fresh once `yfinance` (or an equivalent working pipeline) is available again, and certainly at the Q3 2026 earnings re-score.
5. **Bull/Bear scenario EPS assumptions ($40.0 / $28.0) and both exit multiples (24×/13×) — carried unchanged for the 8th+ consecutive session** (flagged as increasingly stale in every session since 07-28; still not revisited here, consistent with "never invent or estimate" — no new sourced Bull/Bear-specific consensus exists to replace them). Still worth a dedicated review, now more overdue than ever.
6. **META weight (holdings.md): 4.51%**, down from 6.43% on 08-05 due to the confirmed Freedom24-leg sale (2026-08-22 sync) — a portfolio-mechanics change, not a scored-input change; not investigated further here (out of `/rescore`'s scope).
7. **Litigation contingency — not scored.** The teen-safety lawsuit (§2) carries a disclosed but unquantified worst-case exposure (Meta's own $1.4T estimate, per its litigation), with no accrued liability and no settlement terms to fold into any Balance Sheet, Quality, or Valuation sub-score. Not invented or estimated here — flagged as a qualitative risk to watch, consistent with "never invent or estimate financial data." If a settlement with disclosed terms (cash payment, mandated product changes) is later reached, that would be a clear, quantifiable Rule 9 trigger warranting an immediate re-score.

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 18.2943 = 5.4662%
Spread = EY − 10Y Treasury = 5.4662% − 4.65% = +0.8162%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (+0.8162%, ~0.68pp short) → **+5 additive.**

> Cushion widened somewhat vs 08-05's +0.5919% — forward PE fell (18.8969×→18.2943×) faster than the 10Y eased (4.70%→4.65%), so the earnings-yield spread improved even though it still fails the +1.5% bar.

**Step 2 — Rate Regime Modifier**
10Y = 4.65% → "3.5–5%" bracket → **+5**

**Total Rate Modifier for META = +10** (unchanged from 08-05).

---

## 6. META — Quality Score (recomputed — unchanged from 08-05, no new fundamentals this window)

```
Profitability (25%):
  Net Margin = TTM NI ÷ TTM Revenue = $68.098B ÷ $228.247B = 29.8352%   (unchanged)
  ROIC: NOPAT = TTM EBIT × (1 − 16% guided tax rate, unchanged basis) = $86.927B × 0.84 = $73.019B
    Invested Capital = Senior debt ($83.664B) + Total Equity ($261.221B) = $344.885B  (unchanged)
    ROIC = $73.019B ÷ $344.885B = 21.1719%   (unchanged)
  NetMargin_Component = clamp(29.8352/30×100, 0, 100) = 99.4507
  ROIC_Component       = clamp(21.1719/30×100, 0, 100) = 70.5730
  Profitability_Score  = (99.4507 + 70.5730) / 2 = 85.0119

Margins (15%): Gross margin 81.7478% (unchanged) → clamp(81.7478/80×100,0,100) = 100.0

Growth (20%): Revenue 3yr CAGR 19.89% (unchanged — FY2022–FY2025, FY2026 still incomplete)
  Growth_Score = clamp(19.89/25×100, 0, 100) = 79.56 + 10 (TAM-expansion bonus, same basis as
    every prior session: documented ad-market-share data + sustained ~28% YoY revenue growth) = 89.56

Balance Sheet (15%): Net Debt/EBITDA = −$6.596B ÷ $112.282B = −0.05874× (net cash, unchanged)
  BalanceSheet_Score = clamp(100×(1−(−0.05874)/4), 0, 100) = 100.0
  Still clamped at the ceiling — net cash position unchanged since Q2 2026 (no new balance sheet
  data this window); the "fastest one-quarter deterioration on record" flagged 08-05 remains the
  standing watch item for Q3 2026.

Moat Signal (15%): 5/5 signals unchanged (market share, brand premium, network effect, switching
  costs, scale cost advantage) — no new erosion evidence this window. The teen-safety-lawsuit
  settlement-talks news (§2) is a regulatory/reputational risk, not documented moat erosion (no
  market-share loss, no pricing-power loss, no competitive-substitution evidence) — not scored
  here, consistent with "never invent... without a cited source." → 100.0

FCF Quality (10%): FCF/NI = $40.976B ÷ $68.098B = 60.1721% (unchanged)
  FCFQuality_Score = clamp(((0.601721−0.40)/0.60)×100, 0, 100) = 33.6202

Quality Score = 85.0119×0.25 + 100.0×0.15 + 89.56×0.20 + 100.0×0.15 + 100.0×0.15 + 33.6202×0.10
              = 21.2530 + 15.0 + 17.912 + 15.0 + 15.0 + 3.3620
              = 87.5270 → rounds to 87.5
```

**Quality Score = 87.5 — unchanged from 08-05, comfortably PASSES the 80.0+ gate.** No genuine quality change this window — every TTM fundamental input is identical to the last session because no new fiscal quarter has reported (§2, §3).

**Hard disqualifier check:** unchanged from 08-05 — FCF/NI <70% does not fire (growth-capex explanation still stands); Net Debt/EBITDA does not fire (net cash); FCF-positive 3+ years does not fire.

---

## 7. META — Phase 02 Valuation Score

**FCF Yield — 40% weight**
```
FCF_Score = clamp(100 × (1 − 2.8207/10), 0, 100) = 71.7930
```
→ Contribution: 71.7930 × 0.40 = **28.7172**

**EV/EBIT — 40% weight** (PEG not applicable → 15% redistributed here)
```
EV/EBIT_Score = clamp((16.6359 − 12)/23 × 100, 0, 100) = 20.1561
```
→ Contribution: 20.1561 × 0.40 = **8.0624**

**Forward PE (fallback formula) — 20% weight**
```
Deviation% = (18.2943 − 23.152)/23.152 × 100 = −20.9818%
FwdPE_Score = clamp(50 + (−20.9818) × 2.5, 0, 100) = clamp(−2.4545, 0, 100) = 0.0
```
→ Contribution: 0.0 × 0.20 = **0.0**

**PEG — Fast-Grower test: FAIL** (re-verified §3). Weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 28.7172 + 8.0624 + 0.0 = 36.7796
```
**+ Rate Modifier (+10) = 46.7796** *(before the Upside/Downside Modifier)*

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision: update Base-case EPS to the fresh $31.16 consensus; Bull/Bear EPS and both exit multiples carried unchanged** — same practice as every prior session (see §4 flag 5 re: this growing stale).

**Step 1 — Scenario fair values**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 (carried) | 24× | **$960.00** |
| **Base** | 50% | $31.16 (fresh consensus) | 20× | **$623.20** |
| **Bear** | 25% | $28.0 (carried) | 13× | **$364.00** |

```
PW Fair Value = 0.25×960.00 + 0.50×623.20 + 0.25×364.00 = $642.60
```
(Up slightly from 08-05's $640.30 — the Base-case consensus EPS ticked up $30.93→$31.16.)

Sanity check (Rule 0 Step 4 / Rule 4): PW FV $642.60 remains well below the $754.84 analyst consensus PT.

Live price ($570.05) remains **below** the PW Fair Value ($642.60, **+12.73% gap**) — the gap widened from 08-05's +9.55% because price fell more than fair value moved.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($642.60 ÷ $570.05) − 1                    = +12.7270%
Catalyst window = 2 years (unchanged — AI ad-monetization proof points, capex-ROI
                   demonstration; no new dated milestone disclosed this window)
Annualized gap  = +12.7270% ÷ 2                               = +6.3635%/yr
Intrinsic growth = +12.0%/yr   (carried, unchanged basis)
Shareholder yield = ($3.327B buyback + $5.367B dividend) ÷ $1,452.7030B market cap
                  = $8.694B ÷ $1,452.7030B                    = +0.5985%/yr
```
```
E (expected annual return) = +6.3635 + 12.0 + 0.5985 = +18.9620%/yr
```

**Step 3 — Catalyst/timeline (Rule 10 + Guardrail 1).** Same two standing catalysts as prior sessions (AI ad-monetization proof, capex-ROI demonstration), both still inside the 18–24-month window. **Upside credit fully allowed; the −5 catalyst cap does NOT apply** (E ≥ H).

**Step 4 — Map E to the modifier** (hurdle H = 10%):
```
E = 18.9620% ≥ H → M = −15 × clamp((18.9620 − 10)/15, 0, 1)
                      = −15 × clamp(0.59747, 0, 1)
                      = −8.9620
```
**Upside/Downside Modifier M = −8.9620** — more negative (more attractive) than 08-05's −7.3589, driven by the widening price/fair-value gap as price fell further than fair value moved.

---

## 9. META — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (36.7796) + Rate Modifier (+10) + Upside/Downside (−8.9620)
                       = 37.8176
```
Boundary rule: not a ".X5" (hundredths digit is 8) → standard rounding → **Final Valuation Score = 37.8**

| | Value |
|---|---|
| Raw weighted | 36.7796 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −8.9620 (E = +18.96%) |
| **FINAL VALUATION SCORE** | **37.8** |
| Prior valuation score | 41.2 (08-05) |
| **Quality Score** | **87.5 (unchanged from 08-05 — no new fundamentals this window)** |

```
Composite Score = 0.50 × (100 − 87.5) + 0.50 × 37.8 = 0.50×12.5 + 0.50×37.8 = 6.25 + 18.9 = 25.15
```
Boundary rule: 25.15 falls exactly on a ".X5" → round **UP** (conservative) → **Composite Score = 25.2**

**Composite Score = 25.2** (down from 26.9 on 08-05 — an improvement in attractiveness, driven entirely by the valuation side: Quality Score unchanged, but Valuation Score fell from 41.2 to 37.8 as price declined faster than fair value, widening the discount and pushing the Upside/Downside Modifier further negative). Still comfortably inside the same BUY-Full band (0.0–29.9), now with more room (3.7pp from the boundary vs. 3.0pp on 08-05).

---

## 10. META — Action & Category Change

**Valuation Score alone: 41.2 → 37.8** — stays inside the BUY-Standard band (30.0–49.9), moving modestly back toward BUY-Full (a partial reversal of the 07-28→08-05 trend of moving away from it).

**Composite Score: 26.9 → 25.2 → Action band: BUY — Full position 6–8%** (0.0–29.9 band, unchanged; a modest improvement within the band). No action-category change.

**Practical recommendation: HOLD — no automatic fresh capital.** META is an existing holding at **4.51%** (per holdings.md — down from 6.43% due to the Freedom24-leg sale, §3/§4), well inside the 6–8% full-position band, with more headroom to the 8% ceiling than any prior session (3.49pp, vs. 1.57pp on 08-05) — but that headroom is a broker-mechanics artifact, not a scoring signal, and does not by itself trigger a top-up (order-setup gates below still govern).

---

## 11. META — Order Setup (Composite Score in BUY-Full band → required)

Confidence: wide-moat proven compounder (Quality Score 87.5) — same conservative 20% MoS used every prior session.

```
[x] Composite Score (drives action band):        25.2   (≤29.9 ✓ — Full-position entry permitted)
[x] Raw Valuation Score (incl. Upside/Downside):  37.8
[x] Expected annual return E / catalyst window:   +18.96% / 2yr
[x] Upside/Downside Modifier applied:             −8.9620
[x] Blended Fair Value (PW, Rule 7):              $642.60  (up slightly from $640.30 — consensus EPS ticked up)
[x] Margin of Safety %:                           20%
[x] BUY PRICE (limit):     $642.60 × (1 − 0.20)        = $514.08
[x] PRIMARY SELL TARGET:   = Blended FV                = $642.60
[x] BULL-CASE TRIM TARGET: $960.00 × 0.90               = $864.00
[x] STOP LOSS:             $514.08 × (1 − 0.25)        = $385.56   (25% max loss, high-conviction bracket)
[x] Risk/Reward Ratio (base-case target):  ($642.60 − $514.08) ÷ ($514.08 − $385.56) = $128.52 ÷ $128.52 = 1.00:1
[x] Risk/Reward Ratio (bull-case trim target): ($864.00 − $514.08) ÷ $128.52 = $349.92 ÷ $128.52 = 2.72:1
```

Live price ($570.05) is **$55.97 (10.89%) above** the $514.08 buy-price limit — the **closest sustained approach to a qualifying entry in this ticker's history** (was 14.10% on 08-05, 14.55% on 07-28), continuing the multi-session narrowing trend. **Base-case R/R still exactly 1.00:1 (fails the 2:1 minimum)**, the same recurring shape as literally every META session on record. **Net: no automatic qualifying entry fires this session either** — the R/R condition still fails, unchanged in kind, even as the price-limit gap keeps narrowing.

**Position sizing:** META is at **4.51%** (holdings.md — reduced by the Freedom24-leg sale, not by any framework-driven trim), inside the 6–8% band as the Composite Score's action-table lookup, with headroom to the 8% ceiling of **3.49pp**. No forced trim or top-up.

---

## 12. Portfolio Note

META at 4.51% is comfortably under the 15% hard cap (Upgrade 7) and — once weighed against the Composite-Score-driven 6–8% band — actually sits *below* its indicated full-position range (a consequence of the Freedom24 leg sale, not a framework signal; the framework doesn't force a top-up absent a qualifying order per §11). No portfolio-level action is forced by this score. **Consistent with this repo's recurring META pattern: a "BUY — Full position" *score label* has never once, across 10 sessions since 06-12, actually produced a qualifying automatic entry** — the independent price-limit and 2:1 R/R gates have failed every single time, including this session, though the price-limit gap has now narrowed to its tightest point on record (10.89%).

---

## 13. Next Review Triggers

- **Q3 2026 earnings** — Meta's next scheduled print (confirmed, per §2, typically late October/early November 2026) — will refresh every TTM fundamental in this log and is the natural next checkpoint.
- **Litigation watch (new this session, §2/§4).** The teen-safety lawsuit is mid-trial in Oakland federal court with reported (unconfirmed) settlement discussions underway. **If a settlement with disclosed financial or operational terms is reached, that is an unambiguous Rule 9 trigger** (quantifiable liability and/or mandated product changes) and should prompt an immediate re-score, independent of the regular quarterly cadence. Continue monitoring wire coverage for a confirmed settlement or an adverse jury verdict (trial concluding could itself also be a trigger if a verdict/damages figure is announced).
- **Buy-price / fair-value watch:** live price is 10.89% above the $514.08 buy limit — the tightest gap on record for this ticker, worth close attention; base-case R/R remains stuck at exactly 1.00:1 and would need either a lower entry price or a wider sell-target/stop-loss spread to clear 2:1.
- **Balance sheet watch (standing since 08-05):** net cash fell ~70% in Q2 2026 alone; 1–2 more quarters at that pace could flip Meta into net debt and start moving the Balance Sheet sub-score off its 100.0 ceiling — check explicitly at Q3 2026 earnings.
- **Rate Gate watch:** Step 1 FAILED again, cushion widened slightly (+0.82% vs +0.59% on 08-05) as the 10Y eased and forward PE fell.
- **Rule 9 fundamental triggers (standing):** any further guidance revision, management change, material M&A, or a >15% unexplained price move.
- **Bull/Bear scenario assumptions ($40.0/$28.0 EPS, 24×/13× exit multiples)** — flagged stale for the 8th+ consecutive session; increasingly overdue for a dedicated review.
- **`yfinance`/`curl_cffi` environment issue (§0)** — worth a maintainer follow-up so future sessions don't need the direct-`requests` workaround.
- **Owner Earnings (Upgrade 1) methodology decision** — still open; Meta still discloses no maintenance-vs-growth capex split.
- **holdings.md's 4.51% weight** — reflects the confirmed Freedom24-leg sale (2026-08-22), not a framework-driven action; no follow-up needed from `/rescore`.

---

## 14. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — terms actually used in this output; no new terms required this session)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **8-K** | The "current report" a US public company files with the SEC within days of a material event, most often to furnish an earnings press release ahead of the fuller 10-Q/10-K. |
| **10-Q** | The quarterly financial-disclosure report a US public company files with the SEC, containing unaudited financial statements. |
| **bps / pp (percentage points)** | A direct difference between two percentages, distinct from a "%" change. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; drives Phase 03/05 action-table lookups once a Quality Score exists. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **Effective tax rate** | The actual % of pretax income paid as tax in a period — distinct from the statutory rate. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **Invested Capital** | Debt + Equity used as the ROIC denominator. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **MoS (Margin of Safety)** | The discount to fair value demanded before buying. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); the numerator this framework uses to compute ROIC. |
| **NTM** | Next Twelve Months. |
| **Owner Earnings** | Net Income + D&A − maintenance capex only — used instead of raw FCF for moat-building reinvestors (Upgrade 1; unresolved for META). |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **R/R (Risk/Reward ratio)** | Expected gain ÷ expected loss — minimum 2:1 to enter. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the ±10 additive adjustment for the current Treasury-yield band. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **YTD (Year-to-Date)** | The cumulative change in price since the start of the calendar year. |
