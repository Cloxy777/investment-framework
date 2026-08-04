# New Position Evaluation — SPOT (Spotify Technology S.A.)

**Task type:** NEW POSITION (Rule 9 earnings-triggered re-check; SPOT is not currently held)
**Date:** 2026-08-04
**10Y US Treasury yield:** 4.75% (FRED `DGS10`, most recent print 2026-07-31 — Rate Regime band 3.5–5%)
**Trigger:** Hourly Telegram Stock-Mention Scan (Routine 6) — a `t.me/tarasguk` post at 2026-08-04T10:15:52Z ("🎶 $SPOT відзвітував / Цифри ок, але ринку не дуже сподобалось..." — "Spotify reported. Numbers OK but the market didn't like it") named $SPOT by ticker and quoted a set of Q2 metrics. Per Rule 0, **no figure from the post is used anywhere below** — the post is treated only as a signal to check SPOT's own documented "Next review trigger": [watchlist/not-in-portfolio/SPOT/SPOT-2026-07-05.md](../watchlist/not-in-portfolio/SPOT/SPOT-2026-07-05.md) names "Next earnings (standard re-score) or any Rule 9 event." Independently confirmed via SEC EDGAR (not the post): Spotify filed a **6-K on 2026-08-04** (accession `0001140361-26-031044`) containing its Q2 2026 shareholder letter (Exhibit 99.1) — a genuine, primary-sourced Rule 9 earnings event. A same-hour `t.me/FinnInvestChannel` post (superseded top post at the time of the prior check, `FinnInvestChannel/3036`, ~10:53 UTC) quoted nearly-identical revenue/MAU figures without ever naming a company or ticker — consistent with also being about this SPOT print, but per the "never guess a ticker" rule it was not independently actioned; it adds no incremental action since the tarasguk post already names $SPOT directly.

SPOT is **not a current holding** — its 1-share legacy position and matching GTC sell order both vanished from the 2026-08-02 sync with no session/decision-log record (see [holdings.md](../portfolio/holdings.md) flag and [watchlist/not-in-portfolio/SPOT/SPOT-2026-07-05.md](../watchlist/not-in-portfolio/SPOT/SPOT-2026-07-05.md)); unaffected either way by this session, which evaluates SPOT purely as a prospective new entry. Quality/Valuation Score methodology version unchanged since the last entry (2026-06-29), so this is a routine Rule 9 re-check on the current methodology, not a stale-score reconciliation.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EBITDA = operating profit before D&A; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; D&A = depreciation & amortization; capex = capital expenditure; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; CAGR = compound annual growth rate; pp = percentage points; EY = earnings yield (1 ÷ forward PE); NOPAT = net operating profit after tax; ROIC = return on invested capital; TTM = trailing twelve months; NI = net income; MAU = monthly active users; ARPU = average revenue per user; 6-K = the SEC form a foreign private issuer files to furnish material information (Spotify's quarterly-earnings vehicle, in place of a 10-Q).*

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price (used)** | **$465.00** | IBKR `get_price_snapshot` (contract_id 312496724, NYSE), `last.price`, `is_close: false`, timestamp epoch 1785845437 = **2026-08-04T12:10:37Z** (pre-market — NYSE regular session opens 13:30 UTC; earnings were released before the US open) |
| Change vs. prior close | **−$21.33 (−4.39%)** | IBKR `change` field; prior close $486.33 ties to `get_price_history`'s 2026-08-03 close (below) |
| 52-week range | **$405.00 – $748.00** | IBKR `misc_statistics` |
| Year-to-date change | **−19.93%** (−$115.71) | IBKR `year_to_date_change` |
| Analyst consensus PT | **$606.38** (Buy consensus; S&P Global via stockanalysis.com, dated 2026-08-03/04) | Bull-case sanity anchor only, never a score input |
| Prior session price (05 Jul 2026) | $485.97 | −4.32% since last review — nowhere near the 15% Rule 9 threshold on its own |

**Recent daily closes (IBKR `get_price_history`, ONE_DAY bars):** 2026-07-31 $499.94 → 2026-08-03 $486.33 → 2026-08-04 (pre-market) $465.00. The −4.39% move is a same-morning reaction to the earnings release below, not an unexplained Rule-9 price-move trigger in its own right (well under 15% regardless).

---

## 2. Rule 9 Trigger Check (2026-07-05 → 2026-08-04)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | **Yes** | Q2 2026 6-K filed 2026-08-04 (SEC EDGAR, accession `0001140361-26-031044`) — the actual Rule 9 event this session runs on |
| Guidance revision | No (routine quarterly guide, not a revision) | Q3 2026 outlook issued alongside Q2 results, per normal cadence — guidance is a trigger only when it *changes* previously-issued guidance mid-quarter, not on the standard quarterly reissue |
| M&A | No | None found |
| Management change | No — pre-existing, not new this quarter | The filing's segment-reporting footnote references "the Group's new Co-Chief Executive Officers" (Alex Norström and Gustav Söderström, with Christian Luiga as CFO) as the basis for a **Jan 1, 2026** revenue-reclassification, i.e. this leadership structure was already in place before the 2026-07-05 session — not a fresh Rule 9 trigger this quarter, noted for completeness only |
| Macro shift | No | 10Y moved 4.49% → 4.75%, still inside the "3.5–5%" bracket |
| >15% unexplained price move | No | −4.39% pre-market, and explained by the earnings release itself (§1) |

**Conclusion: quarterly earnings is the confirmed Rule 9 trigger.** Full Phase 01 + Phase 02 re-run below, sourced entirely from Spotify's own SEC 6-K filing and independent market-data providers — never from the triggering post.

---

## 3. SPOT — Data Collected (Q2 2026 6-K, Exhibit 99.1, filed 2026-08-04)

**Sector:** Communication Services — Audio Streaming & Podcasting.
**Source:** [Q2 2026 6-K Ex-99.1](https://www.sec.gov/Archives/edgar/data/1639920/000114036126031044/ef20078867_ex99-1.htm) for this quarter's figures; prior-quarter figures (Q3 2025, Q4 2025) carried forward from the 2026-07-05 session's own SEC-sourced table (unchanged, historical, not re-derived) — that session cited [Q3 2025 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036125040271/ef20057592_ex99-1.htm) and [Q4 2025 6-K](https://www.sec.gov/Archives/edgar/data/1639920/000114036126004482/ef20065075_ex99-1.htm) directly.

### Interim condensed consolidated statement of operations (EUR millions, unaudited)

| Line | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|---|
| Revenue | 4,193 | 4,272 | 4,531 | 4,533 | **4,777** |
| Gross Profit | 1,320 | 1,351 | 1,499 | 1,495 | **1,596** |
| Gross Margin | 31.5% | 31.6% | 33.1% | 33.0% | **33.4%** |
| Operating Income (EBIT) | 406 | 582 | 701 | 715 | **655** |
| Net Income/(Loss) | (86) | 899 | 1,174 | 721 | **545** |
| Income before tax | 48 | 827 | 1,021 | 937 | **720** |
| Income tax expense/(benefit) | 134 | (72) | (153) | 216 | **175** |
| Diluted EPS (EUR) | (0.42) | — | — | 3.45 | **2.61** |

**TTM (Q3 2025 → Q2 2026):** Revenue €18,113M · Gross Profit €5,941M (32.80% margin) · EBIT €2,653M · Net Income (GAAP) €3,339M · Pretax €3,505M · Tax €166M (4.74% effective — still distorted by the Q3/Q4 2025 deferred-tax-release quarters inside this TTM window, see §4).

### Balance sheet (EUR millions, as of 30 Jun 2026 vs. 31 Dec 2025)

| Item | 30 Jun 2026 | 31 Dec 2025 |
|---|---|---|
| Cash and cash equivalents | 5,938 | 5,258 |
| Short-term investments | 3,450 | 4,209 |
| Long-term investments (excluded — equity stakes, not cash-like) | 1,118 | 2,181 |
| Lease liabilities (non-current) | 404 | 433 |
| Exchangeable Notes | **0** (fully retired Q1 2026, was 1,458) | 1,458 |
| Total equity (attributable to owners) | 8,385 | 8,329 |
| **Total debt (used)** | **404** (lease liabilities only) | — |
| **Net debt (used)** | **−8,984** (net cash) | — |

### Cash flow (EUR millions)

| Item | Q2 2025 | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 |
|---|---|---|---|---|---|
| Net Cash from Operating Activities | 709 | 829 | 856 | 836 | **816** |
| Free Cash Flow (non-IFRS, company-defined) | 700 | 806 | 834 | 824 | **797** |
| D&A (dep. + amortization, cash-flow add-back) | 26 | 24 | 25 | 26 | **29** |

**TTM (Q3 2025 → Q2 2026):** FCF €3,261M · D&A €104M.

### Other collected inputs

| Item | Value | Source |
|---|---|---|
| Shares outstanding | 205.62M | stockanalysis.com, checked 2026-08-04 (cross-check: 205.62M × $465.00 = $95.61B implied market cap — ties to the site's own displayed figure allowing for its own slightly-stale price) |
| FY2026 consensus EPS | **€12.73** (36 analysts, S&P Global via stockanalysis.com/stocks/spot/forecast, "last updated Aug 3, 2026") | **Currency correction vs. the 2026-07-05 session:** that session labelled this figure "$12.79"; this session's page explicitly states *"EPS and Forward PE are based on non-GAAP adjusted numbers. Financial currency is EUR"* and the accompanying FY2026 revenue consensus (€19.46B) only reconciles against Spotify's own EUR-denominated actuals (FY2025 €17.19B shown on the same table) — confirming the EPS figure is EUR, not USD. Converted to USD below using a live FX rate, not assumed. |
| Live EUR/USD FX rate | **1.1515199** | IBKR `get_account_balances` (broker-reported live rate, per Rule 0 — never assumed) |
| Q3 2026 guidance (trigger only, never a score input) | Revenue €5.0B, Gross Margin 32.9%, Operating Income €670M, MAU 788M, Premium Subscribers 305M | Same Q2 2026 6-K, "Outlook" section |
| Buyback activity | $662M repurchased YTD through Aug 3 (+30% vs. 2025), ~2.2M shares (~1% of shares out.) since resuming in 2025 | Same 6-K |

---

## 4. Data Gaps, Corrections & Flags

1. **Currency correction on FY2026 consensus EPS (see table above).** The figure used this session (€12.73) differs from the 2026-07-05 session's "$12.79" — same underlying consensus estimate, corrected currency label. This session's Forward PE (§6) is computed from the euro figure converted at a live FX rate, not the prior session's dollar-labelled number.
2. **Prior-quarter (Q3/Q4 2025) net income and tax figures carried forward, not independently re-pulled this session.** These are historical, already-reported quarters that cannot change; the 2026-07-05 session sourced them directly from each quarter's own 6-K (URLs in that session's §3) and this session reuses them for the TTM roll-forward — standard practice, not an estimate.
3. **Deferred-tax distortion still present in this TTM window, same treatment as 2026-07-05.** TTM effective tax rate is 4.74% (€166M tax on €3,505M pretax) — still carrying the Q3/Q4 2025 deferred-tax-valuation-allowance-release benefit inside the trailing four quarters (see that session's §4.2 for the underlying mechanism, confirmed via Complete Music Update's coverage of the Q4 2025 release). **Normalization unchanged:** TTM pretax re-taxed at FY2024's clean 15.14% effective rate (€203M/€1,341M) → normalized TTM Net Income ≈ **€2,974.4M** (vs. €3,339M GAAP), used for Profitability's Net Margin sub-score and for NOPAT. Q1 2026 (23.1% effective) and Q2 2026 (24.3% effective) have both since reverted to more normal-looking rates — the distortion is aging out of the trailing window and should fully clear by the Q3 2026 TTM roll (next quarter).
4. **Forward PE — still no usable 5yr history.** SPOT's trailing 8 quarters still include a net-loss quarter (Q2 2025, −€86M) — nowhere near the 20 consecutive quarters of positive TTM EPS the 5yr PE range/average requires. **No-history fallback applies: `FwdPE_Score = 50.0`, flagged, unchanged rationale.**
5. **PEG still not applicable.** Only 2 clean full profitable fiscal years on record (FY2024, FY2025); the Fast-Grower eligibility bar (3+ years clean >15%/yr growth on a non-distorted base) is not cleared. **PEG's 15% weight redistributed to EV/EBIT** (40% total), unchanged from prior sessions.
6. **Owner Earnings (Upgrade 1) does not apply** — SPOT is not one of the four named businesses (MSFT/GOOGL/META/AMZN); TTM capex (€41M: €20M Q1 + €21M Q2 disclosed) is immaterial against €1,652M TTM operating cash flow (~2.5%). Raw FCF used.
7. **Total debt (€404M) is non-current lease liabilities only**, same convention as prior sessions — Exchangeable Notes fully retired in Q1 2026, no separately-disclosed current-lease line. Immaterial to the Net Debt/EBITDA conclusion given the large net-cash position.
8. **Live-price timing note.** $465.00 is a pre-market quote (12:10 UTC, ~80 minutes before the 13:30 UTC regular-session open) — the first tradable price after the 6-K's release. Flagged for transparency; this is still the most current, most Rule-0-compliant price available at the time of this session, not an assumption.

---

## 5. SPOT — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
Forward PE = Live Price ÷ (FY2026 consensus EPS € × live FX)
           = $465.00 ÷ (€12.73 × 1.1515199)
           = $465.00 ÷ $14.6588
           = 31.7215×
EY         = 1 ÷ 31.7215 = 3.1524%
Spread     = EY − 10Y Treasury = 3.1524% − 4.75% = −1.5976%
```
Pass threshold: Spread ≥ +1.5%. **Result: FAIL** (−1.60pp short) → **+5 additive.**

**Step 2 — Rate Regime Modifier**
10Y = 4.75% → "3.5–5%" bracket → **+5**

**Total Rate Modifier = +10.**

---

## 6. SPOT — Quality Score (2026-06-29 methodology, unchanged version)

```
Profitability (25%):
  Net Margin (normalized, ex-DTA-release — §4.3) = €2,974.41M ÷ €18,113M (TTM revenue) = 16.421%
  ROIC: NOPAT = TTM EBIT × (1 − FY2024 clean eff. tax rate 15.138%) = €2,653M × 0.84862 = €2,251.39M
    Invested Capital = Total Debt (€404M) + Total Equity (€8,385M) = €8,789M
    ROIC = €2,251.39M / €8,789M = 25.616%
  NetMargin_Component = clamp((16.421/30)×100, 0, 100) = 54.74
  ROIC_Component       = clamp((25.616/30)×100, 0, 100) = 85.39
  Profitability_Score  = (54.74 + 85.39) / 2 = 70.06   (no FCF cap — FCF-positive every quarter
    on record, TTM €3,261M strongly positive)

Margins (15%): TTM Gross Margin = €5,941M / €18,113M = 32.80%
  GrossMargin_Score = clamp((32.80/80)×100, 0, 100) = 41.00
  + 10 (documented structural 3yr+ trend, extended one more data point: FY2022 24.95% →
    FY2023 25.66% → FY2024 30.14% → FY2025 31.99% → TTM (to Q2'26) 32.80% — all SEC-filed GAAP
    figures, still below the 40% raw threshold so the trend bonus continues to apply per
    quality-scoring.md)
  Margins_Score (with bonus) = 51.00

Growth (20%): Revenue 3yr CAGR, FY2022 €11,727M → FY2025 €17,186M (unchanged inputs — FY2025 is
  still the latest complete fiscal year; next roll-forward happens at FY2026 year-end)
  CAGR = (17,186/11,727)^(1/3) − 1 = 13.59%
  Growth_Score = clamp((13.59/25)×100, 0, 100) = 54.35
  + 10 (pricing-power/TAM-expansion evidence continues, reported revenue growth *accelerated*
    this quarter rather than decelerated: Q1 2026 was +8% Y/Y, Q2 2026 came in at +14% Y/Y
    [+15% Y/Y constant-currency per the 6-K] — the opposite of a structural-deceleration signal,
    so no offsetting −10 penalty. Premium Subscribers still growing 9% Y/Y with continued ARPU
    growth (+7% Y/Y) through the prior price increases — genuine pricing-power evidence,
    consistent with prior sessions' finding)
  Growth_Score (with bonus) = 64.35

Balance Sheet (15%): Net Debt = €404M − (€5,938M + €3,450M) = −€8,984M (net cash)
  EBITDA = EBIT (€2,653M) + D&A (€104M TTM) = €2,757M
  Net Debt/EBITDA = −8,984/2,757 = −3.259× (net cash)
  BalanceSheet_Score = clamp(100×(1−(−3.259)/4), 0, 100) = clamp(181.5, 0, 100) = 100.0

Moat Signal (15%) — checklist, re-verified with fresh Q2 2026 evidence, unchanged conclusions:
  ✓ Market share stable/growing — Premium Subscribers +9% Y/Y to 300M, MAUs +12% Y/Y to 777M,
     growth across every region this quarter — consistent with the #1 position (MIDiA Research
     31.7% global share) holding or growing, not eroding.
  ✓ Brand premium — Premium ARPU €4.89, +7% Y/Y (+7.4% constant-currency), still rising off the
     Aug 2025 / Feb 2026 price increases with subscriber growth continuing alongside it — the
     same documented pricing-power-without-volume-loss pattern as the last session.
  ✓ Network effect — unchanged structural mechanism (two-sided marketplace: listeners attract
     artists/podcasters/audiobook publishers and vice versa; the recommendation engine improves
     with aggregate listening data).
  ✓ Switching costs — unchanged mechanism (playlists, follows, saved libraries, algorithmic-taste
     training, social/collaborative features).
  ✗ Scale cost advantage — still FALSE. Gross margin improved again this quarter (32.32%→32.80%
     TTM) but remains well below software-platform peer levels (70–80%), and no new cited
     cost-per-unit data this quarter shows a genuine unit-economics edge over smaller streaming
     competitors — the label-bargaining-power "scale paradox" finding from the last session
     stands unrevised.
  Moat_Score = (4/5) × 100 = 80.0

FCF Quality (10%): TTM FCF/NI (GAAP, unnormalized — this sub-score is the earnings-quality check
  itself, so intentionally uses reported, not normalized, NI) = €3,261M / €3,339M = 97.664%
  FCFQuality_Score = clamp(((0.97664 − 0.40)/0.60)×100, 0, 100) = 96.11
  (FY2024 FCF/NI 200.9%, FY2025 FCF/NI 129.9% — both far above 70%, no hard-disqualifier concern;
  this quarter's TTM ratio sits below 100% only because GAAP NI (€3,339M) now includes the two
  DTA-release quarters at their full, unnormalized benefit — a GAAP-earnings-quality artifact,
  not a cash-generation problem, given FCF itself grew every quarter)

Quality Score = 70.06×0.25 + 51.00×0.15 + 64.35×0.20 + 100.0×0.15 + 80.0×0.15 + 96.11×0.10
              = 17.515 + 7.650 + 12.870 + 15.000 + 12.000 + 9.611
              = 74.646 → rounds to 74.6
```

**Quality Score = 74.6 — FAILS the 80.0+ gate** (up from 73.2 on 2026-07-05 — a genuine +1.4pt improvement, driven mainly by a stronger normalized Profitability score as the DTA-release distortion ages out of the trailing window, plus continued margin/growth progress — not a data artifact).

**Hard disqualifier check:** none fire. FCF/NI comfortably clears 70% in every annual period and TTM; Net Debt/EBITDA is a deep net-cash position; FCF-positive every quarter on record.

**Why the failure is real, not an artifact:** same underlying story as 2026-07-05 — Margins (51.0, even after the structural-trend bonus) stays capped by a gross margin (32.8%) that this framework's own Moat Signal finding attributes to rights-holder bargaining power rather than a scale-driven cost edge, and Profitability (70.06), while improved, is still short of a truly exceptional score. Growth (64.35) is solid, not exceptional. **Second consecutive quarter SPOT's Quality Score has been computed and failed the 80.0+ gate** — the Phase 04 Quality Watch flag from 2026-07-05 stays open, now with two data points (73.2 → 74.6) showing gradual, genuine improvement rather than deterioration.

---

## 7. SPOT — Phase 02 Valuation Score

**Computed for transparency and cross-session continuity, per this ticker's own established precedent** ([2026-07-05 session](2026-07-05-rescore-spot.md) §10, itself following the GOOG/CSGP 2026-07-04 convention): *the Quality Score gate failure (§6) is decisive on its own for a not-currently-held candidate — SPOT does not qualify for entry regardless of what follows. The numbers below are shown in full per this framework's "no black-box output" rule and to keep this ticker's session-over-session record comparable, not because they change the entry decision.*

**FCF Yield — 40% weight** (Owner Earnings not applicable — §4.6; raw FCF used)
```
TTM FCF (EUR) = €3,261M → USD at live EUR/USD 1.1515199 = $3,755.11M
Market Cap = $465.00 × 205.62M shares = $95,613.30M
FCF Yield = $3,755.11M / $95,613.30M = 3.927%
FCF_Score = clamp(100 × (1 − 3.927/10), 0, 100) = 60.73
```
→ Contribution: 60.73 × 0.40 = **24.292**

**EV/EBIT — 40% weight** (PEG not applicable, see §4.5 → 15% redistributed here)
```
Net Debt (EUR −€8,984M) → USD = −$10,345.25M (net cash)
EV = Market Cap $95,613.30M + Net Debt (−$10,345.25M) = $85,268.05M
TTM EBIT (EUR €2,653M) → USD = $3,054.98M
EV/EBIT = $85,268.05M / $3,054.98M = 27.91×
EV/EBIT_Score = clamp((27.91 − 12)/23 × 100, 0, 100) = 69.18
```
→ Contribution: 69.18 × 0.40 = **27.672**

**Forward PE — 20% weight**
No usable 5yr history (§4.4 — still only 2 clean profitable years, trailing 8 quarters include a loss quarter).
```
FwdPE_Score = 50.0 (neutral fallback, flagged — unchanged rationale)
```
→ Contribution: 50.0 × 0.20 = **10.0**

**PEG — Fast-Grower test: still FAILS** (§4.5). 15% weight redistributed to EV/EBIT (used above).

**Raw weighted score:**
```
= 24.292 + 27.672 + 10.0 = 61.964
```
**+ Rate Modifier (+10) = 71.964** *(before the Upside/Downside Modifier)*

---

## 8. SPOT — Upside/Downside Modifier (Expected-Return Modifier)

**Scenario fair value (Rule 7, EV/EBIT-multiple method on forward EBIT).** Fresh scenario build this session, reflecting the updated TTM EBIT base (€2,653M):

| Scenario | Wt | Forward EBIT (EUR) | Exit EV/EBIT | Equity Value (EUR) = EBIT×Mult + Net Cash | FV/share (USD, ÷205.62M sh, ×1.1515199 FX) |
|---|---|---|---|---|---|
| Bull | 25% | €2,653M × 1.35 = €3,581.55M | 27.0× | €96,701.85M + €8,984M = €105,685.85M | **$591.87** |
| Base | 50% | €2,653M × 1.22 = €3,236.66M | 24.0× | €77,679.84M + €8,984M = €86,663.84M | **$485.34** |
| Bear | 25% | €2,653M × 1.05 = €2,785.65M | 16.0× | €44,570.40M + €8,984M = €53,554.40M | **$299.92** |

Assumptions unchanged from 2026-07-05: Bull = continued margin re-rating + durable Premium pricing power + audiobook/video mix shift sustaining a re-rated multiple; Base = steady-state margin expansion + subscriber growth continuing at the current pace; Bear = label-renegotiation margin squeeze (the "scale cost advantage" Moat Signal FALSE finding above is the specific mechanism) combined with growth deceleration back toward mid-single digits.

**Guardrail adjustment this session:** the Bull scenario's exit multiple is set to **27.0×** (vs. 30.0× used on 2026-07-05) specifically to keep Bull FV/share ($591.87) below the current $606.38 analyst consensus PT — Rule 4's guardrail that this framework's own bull case should never exceed the street's central tendency. The prior session's 30× multiple, applied to this quarter's higher EBIT base, would have produced a Bull FV of ~$652 — above consensus — so the multiple was trimmed rather than the growth assumption, to stay conservative on the input most sensitive to re-rating speculation.

```
PW Fair Value = 0.25×591.87 + 0.50×485.34 + 0.25×299.92 = $465.62
```

**Sanity check (Rule 4/0):** Bull case ($591.87) sits below the $606.38 consensus PT — guardrail satisfied.

**Step 2 — Gap, annualization, components**
```
Gap Upside %    = ($465.62 ÷ $465.00) − 1                = +0.132%    (price now sits almost
                   exactly at PW fair value — essentially flat, a reversal from 07-05's −10.7%
                   above-fair-value gap, driven by the pre-market earnings-day price drop landing
                   the stock right back near this framework's own estimate)
Catalyst window = 2 years (default — unchanged, no single hard re-rating catalyst within 18–24mo)
Annualized gap  = +0.132% ÷ 2                             = +0.066%/yr
Intrinsic growth = +10%/yr (unchanged, in line with the 3yr revenue CAGR of 13.59%, moderated for
                   margin-normalization/label-renegotiation risk per the Bear scenario)
Shareholder yield = +0.5%/yr (modest net buyback continues: $662M repurchased YTD vs. $306M in
                   Q1 2026 alone per the prior session, but weighted-average diluted share count
                   still fell Q1→Q2 2026, 209.28M → 208.86M, a small net reduction after issuance —
                   same order of magnitude as the last session's finding, not re-derived to the
                   decimal this session)
```
```
E (expected annual return) = +0.066 + 10.0 + 0.5 = +10.566%/yr
```

**Step 3 — Catalyst/timeline guardrail.** No hard catalyst within 18–24 months identified. Not binding — E landed just above the hurdle, not in the large-claimed-upside-with-no-catalyst zone the guardrail targets.

**Step 4 — Map E to the modifier** (hurdle H = 10%). E (10.566%) ≥ H (10%):
```
M = −15 × clamp((E − H)/15pp, 0, 1) = −15 × clamp((10.566 − 10)/15, 0, 1) = −15 × 0.0377 = −0.566
```

**Interpretation:** price now sits almost exactly at this framework's own probability-weighted fair value (07-05's −10.7% gap reversed by both the price decline and the scenario base moving up with earnings), and expected return (10.57%/yr) just barely clears the 10% hurdle — landing on the strong-upside/negative-modifier side of the mapping by the thinnest margin, so the deduction is tiny (−0.57, not the full −15 a genuinely rich expected return would earn).

---

## 9. SPOT — Final Valuation Score, Quality Score, Composite Score

```
FINAL VALUATION SCORE = Raw weighted (61.964) + Rate Modifier (+10) + Upside/Downside (−0.566)
                       = 71.398
```
Boundary rule: not a ".X5" → standard rounding → **Final Valuation Score = 71.4**

| | Value |
|---|---|
| Raw weighted | 61.964 |
| Rate Gate (Step 1 fail + Step 2) | +10 |
| Upside/Downside Modifier | −0.566 (E = +10.566%) |
| **FINAL VALUATION SCORE** | **71.4** |
| Prior valuation score | 84.2 (05 Jul 2026) |
| **Quality Score** | **74.6 (FAILS 80.0+ gate)** — up from 73.2 |

```
Composite Score = 0.50 × (100 − 74.6) + 0.50 × 71.4 = 0.50×25.4 + 0.50×71.4 = 12.7 + 35.7 = 48.4
```

**Composite Score = 48.4** — shown for transparency only (§7); **not the basis for the action call below**, per [valuation-scoring.md](../framework/valuation-scoring.md): *"Composite Score isn't computed for, and doesn't rescue, a company failing the quality gate."*

---

## 10. SPOT — Recommendation

**PASS — Quality Score (74.6) fails the 80.0+ gate. No new position opened. Watchlist only.**

This is a straightforward call for a not-currently-held candidate: [quality-scoring.md](../framework/quality-scoring.md) requires 80.0+ to become eligible for Phase 02 at all, let alone an actual entry — SPOT has now failed that bar in two consecutive quarterly computations (73.2 on 2026-07-05, 74.6 today). No fair-value/buy-price/position-sizing order setup is produced (operating-brief.md OUTPUT FORMAT step 6 applies only when an entry is actually being made).

**What's genuinely new this session, worth surfacing:**
- The Quality Score **improved** for a second straight read (73.2 → 74.6) — driven by the DTA-release distortion progressively aging out of the TTM window (normalizing Profitability upward) plus continued, real margin and growth progress. This is not a business in decline; it is a business that has not yet cleared this framework's own strict quality bar.
- Raw Valuation Score also **improved materially** (84.2 → 71.4, moving from "Very Expensive" 80.0–89.9 territory into the "Expensive" 70.0–79.9 band) on the combination of a lower price and higher TTM EBIT/FCF base — SPOT is cheaper on this framework's own bottom-up metrics than it has been in the last two prior sessions.
- On the framework's probability-weighted scenario model, price now sits almost exactly at fair value (+0.13% gap, vs. −10.7% "above fair value" on 07-05) — a name worth re-checking again promptly if the Quality Score continues its current improving trajectory, since a Quality Score clearing 80.0 at a similar valuation would flip this from PASS to a live BUY/watchlist candidate.

**Next review trigger:** Q3 FY2026 earnings (per this quarter's own guidance, standard quarterly cadence — historically early-to-mid November based on the Q3 2025 report pattern), or any Rule 9 event (guidance revision, M&A, management change, macro shift, or a >15% unexplained price move) in the interim. Specifically re-test whether the normalized-tax-rate distortion has fully cleared the TTM window (it should, once Q3 2025 rolls off), and re-verify the "scale cost advantage" Moat Signal for any cited unit-cost evidence as Spotify's scale continues to grow.

---

## 11. Watchlist & Portfolio Note

New dated entry written: [watchlist/not-in-portfolio/SPOT/SPOT-2026-08-04.md](../watchlist/not-in-portfolio/SPOT/SPOT-2026-08-04.md) (both Quality Score and Composite Score changed from the last entry — a fresh dated row, not a "last checked" line). This session does not touch `portfolio/holdings.md` (SPOT is not held; its undocumented-exit flag there is unaffected). No trade recommended or executed.

---

## 12. Glossary

(Pulled from [glossary.md](../framework/glossary.md) — all terms used in this output were already on file, none added this session)

| Term | Meaning |
|---|---|
| **52-week range** | The lowest and highest price a stock has traded at over the past year. |
| **6-K** | The SEC form a foreign private issuer files to furnish material information to investors — Spotify's quarterly-earnings vehicle, used in place of a 10-Q. |
| **ARPU** | Average Revenue Per User. |
| **Buyback yield** | The rate at which a company's share count shrinks per year from repurchases, net of new issuance. |
| **CAGR** | Compound Annual Growth Rate. |
| **CapEx** | Capital Expenditure. |
| **Catalyst window** | The timeframe (Rule 10, typically 18–24 months) within which a documented event is expected to close the price/fair-value gap. |
| **Composite Score** | This framework's blended 0.0–100.0 ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; not computed to "rescue" a company failing the Quality gate. |
| **D&A** | Depreciation & Amortization. |
| **Deferred tax valuation allowance release** | A one-off GAAP accounting event where a company reverses a prior write-down on its deferred tax assets, producing an artificially low effective tax rate and inflated net income in the recognition period. |
| **EBIT / EBITDA** | Operating profit before interest and taxes / before interest, taxes, D&A. |
| **EPS** | Earnings Per Share. |
| **EV / EV/EBIT** | Enterprise Value (market cap + net debt) / EV divided by EBIT. |
| **EY (Earnings Yield)** | 1 ÷ Forward PE, compared against the 10-Year Treasury yield. |
| **Fast Grower** | Lynch's term for >15%/yr EPS growth for 3+ years on a clean base — this framework's PEG-eligibility trigger. |
| **FCF / FCF Yield / FCF/NI conversion ratio** | Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks accounting-profit quality). |
| **Forward PE** | Price ÷ next-twelve-months expected EPS. |
| **FV / PW Fair Value** | Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear). |
| **FX (foreign exchange) rate** | This framework only uses live, broker-reported FX rates to convert non-USD figures to USD — never an assumed rate. |
| **Hard disqualifier** | One of three Quality Score conditions that fails a company regardless of its weighted score. |
| **Hurdle rate** | The minimum acceptable annual return (10% in this framework). |
| **MAU (Monthly Active Users)** | The number of unique users who engage with a product at least once in a given month. |
| **Moat** | A durable competitive advantage protecting a business's profits. |
| **Net Debt/EBITDA** | Leverage ratio — years of cash profit needed to pay off all debt. |
| **NI (Net Income)** | Accounting profit after all expenses. |
| **NOPAT** | Net Operating Profit After Tax — EBIT × (1 − effective tax rate); used to compute ROIC. |
| **PE (Price-to-Earnings) ratio / PEG ratio** | Share price ÷ EPS; PE ÷ earnings growth rate. |
| **pp (percentage points)** | A direct difference between two percentages. |
| **PT (Price Target)** | An analyst's forecast of future price. |
| **Quality Score** | This framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02. |
| **Rate Environment Gate / Rate Regime Modifier** | The pre-check comparing Earnings Yield to the 10-Year Treasury, plus the additive Treasury-bracket adjustment. |
| **ROIC** | Return on Invested Capital — NOPAT ÷ Invested Capital. |
| **Rule 0** | Always fetch a live price first — never infer from multiples or stale data. |
| **Rule 4** | The reward/risk and price-target sanity guardrails governing scenario fair-value construction. |
| **Rule 6** | Normalize earnings/margins/revenue/debt before valuing — strip out one-time items. |
| **Rule 9** | The list of fundamental events that force an immediate re-valuation. |
| **Shareholder yield** | Dividend yield + net buyback yield combined. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported results. |
| **Upside/Downside Modifier (Expected-Return Modifier)** | Additive ±15 score adjustment based on expected annual return vs the 10% hurdle. |
