# RESCORE — META — 2026-09-28

**Task type:** RESCORE (single ticker) — routine ~33-day re-check (Composite Score last reviewed 2026-08-26 PM), also independently warranted this session by a **Rate Environment macro shift** (§2)
**Date:** 28 Sep 2026
**10Y US Treasury Yield:** **5.24%** (TradingEconomics.com, quote dated 28 Sep 2026 — "rose to 5.24%, +0.07pp vs prior session"; cross-checked via WebSearch against Seeking Alpha ("U.S. 10-Year Treasury tops 5.25%") and Babypips ("Treasury Yields Hit Near 20-Year High," 28 Sep 2026) — all sources agree on a 5.2%+ reading, a **new bracket** vs. every prior META session (4.65–4.70%, all in the "3.5–5%" bracket))
**Rate Regime Modifier (Step 2):** **+10** (bracket **>5%** — first time this ticker has crossed out of the "3.5–5%" bracket)
**Last review on record:** META **39.4** (2026-08-26 PM, Composite 26.0, Quality 87.5, BUY — Full position 6–8% — [sessions/2026-08-26-rescore-meta-2.md](2026-08-26-rescore-meta-2.md))
**Gap since last review:** 33 days.

> *Jargon decoded on first use (CLAUDE.md non-negotiable, for a non-finance reader): FCF = free cash flow; EV = enterprise value; EBIT = operating profit; EV/EBIT = enterprise value ÷ operating profit; PE = price-to-earnings ratio; forward PE = price ÷ next-twelve-months expected earnings; PEG = PE ÷ earnings growth rate; NOPAT = net operating profit after tax; ROIC = return on invested capital; MoS = margin of safety; R/R = reward-to-risk ratio; PW = probability-weighted; pp = percentage points; EY = earnings yield (1 ÷ PE); TTM = trailing twelve months; NTM = next twelve months; 10-Q = quarterly SEC filing; 8-K = SEC "current report" filing.*

---

## 0. Data-Source Note

`python -m scripts.fetch_fundamentals META` ran successfully this session (no `yfinance`/`curl_cffi` failure this time). Live price, 10Y Treasury, and forward-EPS consensus fetched via WebSearch/WebFetch (stockanalysis.com, TradingEconomics, cross-checked against additional WebSearch results — Google Finance and CNBC's direct quote pages both returned HTTP errors this session and were not usable, so a third live-price cross-check uses two independent WebSearch results instead of a second WebFetch; still meets the "at least two independent sources" bar every prior session has used). Two known **Yahoo/`yfinance` data-quality issues** recur this session, both previously flagged (08-05 / 08-26 sessions) and handled the same way — see §4.

---

## 1. Live Price (Rule 0)

| Item | Value | Source |
|---|---|---|
| **Live price** | **$715.62** | stockanalysis.com WebFetch, quote timestamp "as of Sep 28, 2026, 4:00 PM EDT" (regular-session close) |
| Cross-check | Independent WebSearch results corroborate: Forbes ("Zuckerberg Loses $11 Billion As Meta Shares Drop," 28 Sep 2026) and TradingKey ("META opened down 3.77% on Sep 28") both describe the same day's decline; a third WebSearch snippet (Robinhood cache) showed a stale $747.82 figure from the prior session and was **not used** — flagged as an unreliable/cached source this session, consistent with "never invent or estimate," relying on the two consistent, dated sources instead | WebFetch (stockanalysis.com) + WebSearch (Forbes, TradingKey) |
| Today's change | **−4.79% (−$36.04)** vs. prior close | stockanalysis.com; consistent with wire reports of Meta "falling ~4%" on 28 Sep 2026 profit-taking |
| 52-week range | **$520.26 – $779.82** | stockanalysis.com |
| Analyst consensus PT | **$761.01** (62 analysts, "Strong Buy," 6.36% implied upside) | stockanalysis.com — bull-case sanity check only (Rule 0 Step 4) |

**Context (qualitative, not scored):** Meta rallied strongly through September (+36% at one point intramonth) on enthusiasm for its new "Muse" AI agent (2.8M downloads in its first two weeks), before today's pullback on profit-taking, AI-capex-ROI skepticism (Goldman Sachs flagged the ~$300B/yr AI-services-revenue bar the industry needs to hit to merely break even on capex), and news Meta plans to tap Europe's bond market for the first time to help fund AI infrastructure. None of this is a Rule 9 trigger category (no earnings, no guidance revision, no M&A, no management change) — treated as context only, consistent with how prior "Meta Compute"/capex-story sessions (07-01, 07-09, 07-13) were handled.

---

## 2. Rule 9 Trigger Check (2026-08-26 PM → 2026-09-28)

| Trigger | Found? | Detail |
|---|---|---|
| Quarterly earnings | **No** | Confirmed via WebSearch (multiple earnings-calendar sites): Meta's Q3 2026 report is expected **28 Oct 2026, after close** — not yet due. |
| Guidance revision | **No — explicitly confirmed unrevised.** | WebSearch of settlement-related coverage confirms: **"Meta said its previously issued July guidance has not been revised as a result of the [teen-safety] settlement."** The ~$10B one-time Q3 legal charge (already known as of the 08-26 PM session) will still be booked in Q3 2026 results, but no *interim* guidance update has been issued. |
| Material M&A / JV | No new one this window. | The European AI-infrastructure bond issuance reported this week is a financing plan, not M&A. |
| Management change | No. | |
| **Macro shift** | **YES — flagged, but treated as feeding the existing Rate Regime Modifier mechanism rather than a separate Rule 9 event.** | The 10Y Treasury yield has moved from 4.65–4.70% (every prior META session) to **5.24%** — a genuine multi-decade-high bond selloff (wire coverage: "near 20-year high," driven by hawkish Fed commentary, lack of US-Iran de-escalation progress, and worsening fiscal-deficit concerns) — not a company-specific event, but exactly the kind of "macro shift (central bank policy...)" category Rule 9 names. Framework mechanics already route a rate-regime move through the **Rate Regime Modifier** (Step 2 of the Rate Environment Gate, §5) rather than a bespoke trigger process, so this session proceeds as a normal re-score with the new bracket applied — not treated as requiring separate action beyond that. |
| Litigation settlement developments | Confirmed still on track, nothing new scoreable | WebSearch (NPR, topclassactions.com, CT AG press release, EFF) confirms the settlement (cited $17–18B range across outlets, same normal reporting variance flagged 08-26) is proceeding; Meta will book the ~$10B Q3 charge **as previously known**. One update: a **separate** New Mexico AG trial (broader content-moderation claims, not part of the 51-state settlement) began 8 Sep 2026 — new information, but no disclosed financial figure or verdict yet, so **does not itself clear the Rule 9 bar**; flagged as a forward watch item. |
| >15% unexplained price move | **No** (today's −4.79% is explained; the cumulative +23.6% since 08-26 PM is also explained — AI-product enthusiasm, per wire coverage — not "unexplained") | |

**Conclusion:** No enumerated Rule 9 trigger independently fires this session in the "stop everything and re-score outside the normal cadence" sense. This proceeds as a **routine 33-day re-check**, with the Rate Regime Modifier's bracket shift (§5) as the most consequential single mechanical input this session.

---

## 3. META — Inputs Collected

**Sector:** Communication Services — Internet & Digital Advertising / Social Platforms
**Current portfolio weight:** **5.43%** (per [holdings.md](../portfolio/holdings.md), synced 2026-09-20 — up from 4.51% on 08-26, consistent with the stock's price appreciation since then; a portfolio-mechanics observation, not a scored input, out of `/rescore`'s scope to investigate further)

### `python -m scripts.fetch_fundamentals META` — raw output

```
Market Cap            = 1,823,046,369,280
Enterprise Value      = 1,936,916,480,000
Shares Outstanding    = 2,205,128,509
Forward PE            = 20.548
FCF Yield %           = 2.248
EV/EBIT               = 21.629
Net Margin %          = 29.835
Gross Margin %        = 81.748
ROIC % (NOPAT/InvCap) = 25.246  [tax_rate=0.2220, NOPAT=69,675,866,255, InvestedCapital=275,987,000,000]
Revenue 3yr CAGR %    = 19.894
Net Debt/EBITDA       = 0.209  [EBITDA_ttm=109,654,999,040]
FCF/NI TTM %          = 60.172
FCF/NI annual (oldest first) = [83.1%, 112.7%, 86.7%, 76.3%]
FCF positive 3yr+     = True
5yr PE avg/low/high   = 23.134 / 9.248 / 35.985  (n=20 quarters)
```

### Data-quality corrections applied (§4 has full detail) — same known issues as 08-05/08-26

The script's `Shares Outstanding`, `Enterprise Value`, `ROIC`, and (indirectly) `Net Debt/EBITDA` fields all trace back to two long-flagged `yfinance`/Yahoo data quality issues for this specific ticker (Class-A-only share count; a divergent `EBIT` field). **`Market Cap`, `FCF Yield %`, and the underlying TTM Revenue/Net Income/Gross Profit/FCF figures are unaffected and used as-is** — they reconcile exactly against the 08-26 PM session's TTM figures (no new fiscal quarter has reported), confirming no restatement:

| Item | Value | Cross-check |
|---|---|---|
| TTM Revenue | $228.247B | Matches 08-26 exactly |
| TTM Net Income | $68.098B | Matches 08-26 exactly |
| TTM EBITDA | $112.282B (carried) | Matches 08-26 exactly |
| TTM FCF | $40.976B | Matches 08-26 exactly |
| Gross profit (TTM) | $186.587B → Gross margin 81.7478% | Matches 08-26 exactly |
| Net cash (30 Jun 2026, latest filed balance sheet) | $6.596B (carried — no new 10-Q; Q3 2026 not due until 28 Oct) | Matches 08-26 exactly |
| **10-Q-verified TTM EBIT (authoritative, not Yahoo's field)** | **$86.927B** (carried — see §4 flag 2) | Matches 08-26 exactly |
| Buyback (TTM) | $3.327B (carried) | Matches 08-26 exactly |
| Dividend (TTM) | $5.367B (carried) | Matches 08-26 exactly |
| **Corrected shares outstanding (Class A + Class B)** | **2,548,378,209** (carried — 08-05 correction) | Not what the script's `Shares Outstanding` field shows (§4 flag 1) |

### Recomputed this session (price/consensus-dependent, using corrected shares + live price)

| Item | 08-26 PM value | 09-28 value (fresh) | Computation |
|---|---|---|---|
| Live price | $578.83 | **$715.62** | §1 |
| Market Cap | $1,475.0778B | **$1,823.6704B** | 2,548,378,209 × $715.62 |
| EV (Market Cap − net cash) | $1,468.4818B | **$1,817.0744B** | $1,823.6704B − $6.596B |
| **EV/EBIT** (using 10-Q-verified EBIT) | 16.8933× | **20.9035×** | $1,817.0744B ÷ $86.927B |
| **FCF Yield** | 2.7777% | **2.2469%** | $40.976B ÷ $1,823.6704B |
| Forward EPS (FY2026 consensus) | $31.16 | **$31.01** | stockanalysis.com/forecast, 59 analysts, **updated 28 Sep 2026** — see §4 flag 5: this is the first consensus pull since the ~$10B Q3 legal charge became known, and the implied FY2026 growth (+4.5% over FY2025's $29.68 consensus-basis EPS) looks materially slower than pre-charge trajectory, suggesting the charge is now at least partially reflected |
| Forward PE | 18.5761× | **23.0771×** | $715.62 ÷ $31.01 |
| 5yr avg/low/high PE (auto-reconstructed, fresh) | 23.152× / 9.255×–36.014× (n=20q) | **23.134× / 9.248×–35.985×** (n=20q) | Fresh `fetch_fundamentals` pull; essentially unchanged (same 20-quarter reconstruction window, still no new earnings date to shift it) |

### Fast-Grower (PEG eligibility) test — re-verified, still fails

No new fiscal year has completed since 08-26 (FY2025 diluted EPS is still the most recent complete year: −1.55% YoY). **Still FAILS** ">15% EPS growth for 3+ consecutive years on a clean base." **PEG not applicable; its 15% weight redistributed to EV/EBIT** — unchanged.

---

## 4. Data Gaps / Flags

1. **`yfinance`'s `sharesOutstanding` field (2,205,128,509) is the known Class-A-only vendor trap**, first caught 2026-08-05. `Market Cap` internally reconciles against the *correct* total share count (2,548,378,209 × implied price ≈ the reported Market Cap, verified by direct calculation this session) — so `Market Cap`/`FCF Yield %` are trustworthy as-is, but the standalone `Shares Outstanding` display field is not, and was not used. Corrected total carried forward per the 08-05 fix.
2. **`yfinance`'s `EBIT` field ($89.553B implied from this session's EV/EBIT=21.629× against EV=$1,936.916B) again diverges from the 10-Q-verified figure ($86.927B)**, same discrepancy flagged 08-05/08-26 (Yahoo's derived field appears to mix in non-operating items). **Continuing to use the 10-Q-verified $86.927B** as authoritative, not invented — this is a real, sourced number from Meta's own Q2 2026 filing, just not the one Yahoo's field currently shows.
3. **`yfinance`'s `enterpriseValue` field ($1,936.916B) is inconsistent with META's known net-cash position** — it implies ~$113.9B of net debt against a company that reported $6.596B of **net cash** as of the last 10-Q. This looks like the same class of Yahoo data-quality issue as flags 1–2 (likely compounding the wrong-shares-count and/or a stale debt figure). **Recomputed EV manually** from the corrected Market Cap and the carried, 10-Q-sourced net cash figure ($1,817.074B) — not invented, drawn entirely from figures already independently verified in this or prior sessions.
4. **Bull/Bear scenario EPS assumptions ($40.0 / $28.0) and both exit multiples (24×/13×) — carried unchanged for the 10th+ consecutive session.** No new sourced Bull/Bear-specific consensus exists to replace them (never invent/estimate) — but this is now more overdue than ever given how far the Base-case has moved and how far price has moved since these were last set (07-28 session origin). Flagged again, more urgently.
5. **Base-case consensus EPS ($31.01) is the first pull since the ~$10B Q3 2026 legal charge became known** (08-26 flag) — its slower year-over-year growth vs. the FY2025 consensus basis ($29.68, +4.5%) suggests the charge is now at least partially priced into analyst estimates, resolving (not definitively closing) last session's open flag. Not independently confirmed against a per-analyst EPS-revision breakdown — flagged as resolved-by-inference, not resolved-by-direct-confirmation.
6. **Forward PE sub-score methodology note (not a data gap, a methodology clarification):** every prior META session (06-12 through 08-26) manually applied the **Fallback ("avg-only") formula** for the Forward PE sub-score even though `fetch_fundamentals` has always returned a full `pe_mode: "range"` result (low/high both available, n=20 quarters). This session instead ran `scripts.scoring.valuation_score` directly, which correctly applies the **Primary ("range") formula** per valuation-scoring.md's stated priority ("Primary formula" used "when a trailing 5-year PE range is available" — which it is) — this is the first time this sub-score has been computed by the actual scoring script rather than hand-derived, and the script's behavior is the more literal reading of the framework text. **This is flagged for the record as a session-over-session methodology difference**, not a new framework change — worth a maintainer decision on whether to formally prefer "range" mode going forward (it was already the technically-correct mode every session, just not the one manually applied).
7. **Owner Earnings (Upgrade 1) — still unresolved.** Meta's most recent 10-Q (Q2 2026, unchanged) still doesn't disclose a maintenance-vs-growth capex split. Raw FCF continues to be used, as in every prior META session.
8. **A second, separate New Mexico AG trial** (broader content-moderation claims, outside the 51-state settlement) began 8 Sep 2026 — no verdict or disclosed financial figure yet, so not scored; flagged as a forward watch item (§13).
9. **Growth sub-score's TAM/pricing-power evidence text is carried unchanged for the 10th+ consecutive session** without an independent re-pull of underlying market-share data — flagged as increasingly due for a fresh citation, consistent with "never invent" (the qualitative basis itself hasn't been re-verified this window, only carried).
10. **Google Finance and CNBC's direct quote pages both returned HTTP errors (404/403) this session** when attempted as the second live-price cross-check source (§1) — worked around using two independent WebSearch article results instead; not a data-quality substitution (same underlying market data, different access path), flagged per the same "never invent" discipline as the 08-26 `curl_cffi` workaround.

---

## 5. META — Rate Environment Gate

**Step 1 — Earnings Yield Spread Test**
```
EY     = 1 ÷ Forward PE = 1 ÷ 23.0771 = 4.3333%
Spread = EY − 10Y Treasury = 4.3333% − 5.24% = −0.9067pp
```
Pass threshold: Spread ≥ +1.5pp. **Result: FAIL** (−0.9067pp — the *worst* (most negative) spread on record for this ticker; every prior session was in the +0.6 to +0.8pp "short by less than 1pp" range, this session is now actually negative) → **+5 additive.**

**Step 2 — Rate Regime Modifier**
10Y = 5.24% → **">5%" bracket (new — every prior session was "3.5–5%")** → **+10** (up from +5)

**Total Rate Modifier for META = +15** (up from +10 every prior session) — the single largest mechanical driver of this session's valuation-score jump, independent of META's own price or fundamentals.

---

## 6. META — Quality Score

```
python -m scripts.scoring.quality_score --input inputs.json
```

## Quality Score

**Profitability (25%)**
```
NetMargin_Component = clamp((29.8352/30)x100) = 99.45
ROIC_Component = clamp((21.1719/30)x100) = 70.57
Profitability_Score = (99.45 + 70.57) / 2 = 85.01
```
**Margins (15%)**
```
GrossMargin_Score = clamp((81.7478/80)x100) = 100.00
```
**Growth (20%)**
```
Growth_Score = clamp((19.89/25)x100) = 79.56
+10 TAM/pricing-power evidence: Documented ad-market-share growth and sustained ~28% YoY revenue growth (Q2 2026 10-Q); carried per every prior META session's basis, unchanged this window (no new fiscal quarter since Q2 2026 10-Q, filed 2026-07-29).
Growth_Score (final, clamped) = 89.56
```
**Balance Sheet (15%)**
```
BalanceSheet_Score = clamp(100x(1 - -0.05874/4)) = 100.00
```
**Moat Signal (15%)**
```
| Signal | True | Evidence |
|---|---|---|
| market_share_stable_or_growing | True | Sustained ~28% YoY ad revenue growth and stable-to-growing share of digital ad spend through Q2 2026 (10-Q); carried unchanged, no new erosion evidence this window. |
| brand_premium | True | Advertiser pricing power evidenced by ad-price growth alongside impression growth in filed 10-Qs through Q2 2026; carried unchanged. |
| network_effect | True | Two-sided marketplace dynamics across Facebook/Instagram/WhatsApp (3.4B+ family DAP per Q2 2026 10-Q); carried unchanged. |
| switching_costs | True | Social graph lock-in and Advantage+ ad-tooling integration depth for advertisers; carried unchanged. |
| scale_cost_advantage | True | 81.7% gross margin and industry-leading ad-infrastructure scale vs smaller platform competitors; carried unchanged. |
Moat_Score = (5/5) x 100 = 100.00
```
**FCF Quality (10%)**
```
FCFQuality_Score = clamp(((0.6017 - 0.40)/0.60)x100) = 33.62
```
**Quality Score — Final**
```
Quality Score = (85.01x0.25) + (100.00x0.15) + (89.56x0.20) + (100.00x0.15) + (100.00x0.15) + (33.62x0.10)
= 87.527 -> rounds to 87.5
```

# Quality Score = 87.5 — PASSES the 80.0+ gate

**Unchanged from every session since 08-26** — no new fiscal quarter has reported (§3), so every input is identical. Hard disqualifier check: unchanged — none fire (FCF/NI <70% for 2+ years does not fire, growth-capex explanation stands; Net Debt/EBITDA does not fire, net cash; FCF-positive 3+ years does not fire).

---

## 7. META — Phase 02 Valuation Score

```
python -m scripts.scoring.valuation_score --input inputs.json
```

## Valuation Score

**FCF Yield (40%)**
```
FCF_Score = clamp(100x(1 - 2.2469/10)) = 77.531
```
**EV/EBIT (40% — PEG not applicable, 15% redistributed here)**
```
EV/EBIT_Score = clamp((20.9035 - 12)/23 x 100) = 38.711
```
**Forward PE (20%) — Primary ("range") formula (see §4 flag 6)**
```
FwdPE_Score (raw) = clamp((23.0771 - 9.247937)/(35.985183 - 9.247937) x 100) = 51.722
Deviation vs 5yr avg (23.134209) = (23.0771 - 23.134209)/23.134209 x 100 = -0.247%
Historical PE Modifier: within +-10% of 5yr avg -> 0
FwdPE_Score = clamp(51.722 + 0) = 51.722
```
**PEG**
```
PEG not applicable (not a Fast Grower) -> 15% weight redistributed to EV/EBIT
```
**Rate Environment Gate**
```
EY = 1/23.0771 x 100 = 4.3333%
Spread = EY - 10Y (5.24%) = -0.9067pp -> Step 1 = +5 (fail, <1.5pp)
10Y = 5.24% -> Step 2 bracket modifier = +10
Total Rate Modifier = 5 + 10 = +15
```

**Raw Weighted Score**
```
Raw = FCF_Score x 0.4 + EV/EBIT_Score x 0.4 + FwdPE_Score x 0.2
= 77.531x0.4 + 38.711x0.4 + 51.722x0.2
= 56.841
```

---

## 8. META — Upside/Downside Modifier (Expected-Return Modifier)

**Decision:** Base-case EPS updated to the fresh $31.01 consensus; Bull/Bear EPS ($40.0/$28.0) and both exit multiples (24×/20×/13×) carried unchanged (§4 flag 4).

**Step 1 — Scenario fair values**

| Scenario | Weight | EPS assumption | Exit PE | Fair Value |
|---|---|---|---|---|
| **Bull** | 25% | $40.0 (carried) | 24× | **$960.00** |
| **Base** | 50% | $31.01 (fresh consensus) | 20× | **$620.20** |
| **Bear** | 25% | $28.0 (carried) | 13× | **$364.00** |

```
PW Fair Value = 0.25x960.0 + 0.50x620.2 + 0.25x364.0 = $641.10
```

Sanity check (Rule 0 Step 4 / Rule 4): PW FV $641.10 remains below the $761.01 analyst consensus PT.

**Live price ($715.62) is now ABOVE the PW Fair Value ($641.10) — a −10.41% "gap"** (i.e. the stock trades above this framework's blended fair value estimate, not below it), the first time this has happened on a sustained basis since the brief 07-13 crossing. This is driven entirely by price appreciation (+23.6% since 08-26 PM) outrunning the Base-case fair value (essentially flat — EPS consensus barely moved).

```
Gap Upside % = (641.10/715.62) - 1 = -10.4133%
Annualized gap = -10.4133% / 2yr = -5.2067%/yr
Intrinsic growth = +12.0%/yr (carried, unchanged basis)
Shareholder yield = ($3.327B buyback + $5.367B dividend) / $1,823.6704B market cap
                  = 0.1824% (buyback) + 0.2943% (dividend) = +0.4767%/yr
E (expected annual return) = -5.2067 + 12.0 + 0.4767 = +7.2700%/yr
```

**Step 2 — Catalyst/timeline (Rule 10 + Guardrail 1).** Same two standing catalysts (AI ad-monetization proof, capex-ROI demonstration), both still inside the 18–24-month window. Since `0 ≤ E < H`, Guardrail 1's catalyst cap is not in play (it only caps the *upside/negative-M* side).

**Step 3 — Map E to the modifier** (hurdle H = 10%):
```
0 <= E (7.2700%) < H -> M = 5 x (10.0-7.2700)/10.0 = 1.3650
```

**Upside/Downside Modifier M = +1.3650** — a sharp reversal from every prior session's negative modifier (which ranged from −3.4 to −15.0, always *lowering* the score because price sat below fair value). This is now a small *positive* (score-raising) modifier because price has, for the first time on a sustained basis, moved meaningfully above this framework's blended fair value.

---

## 9. META — Final Valuation Score, Quality Score, Composite Score

```
Final Score = Raw (56.841) + Rate Modifier (+15) + Upside/Downside Modifier (+1.365)
= 73.206 -> rounds to 73.2
```

| | Value |
|---|---|
| Raw weighted | 56.841 |
| Rate Gate (Step 1 fail +5, Step 2 bracket +10) | +15 |
| Upside/Downside Modifier | +1.365 (E = +7.27%) |
| **FINAL VALUATION SCORE** | **73.2** |
| Prior valuation score (08-26 PM) | 39.4 |
| **Quality Score** | **87.5 (unchanged)** |

```
python -m scripts.scoring.composite_score --set quality_score=87.5 --set valuation_score=73.2
Composite Score = 0.50x(100 - 87.5) + 0.50x73.2 = 42.850 -> rounds to 42.9
```

**Composite Score = 42.9** (up sharply from **26.0** on 08-26 PM) — driven by three factors, all valuation-side (Quality Score unchanged at 87.5): (1) price rose +23.6% while fair-value inputs barely moved, flipping the Upside/Downside Modifier from meaningfully negative to slightly positive; (2) the Rate Regime Modifier's bracket shifted from +5 to +10 as the 10Y crossed above 5% for the first time; (3) EV/EBIT and FCF Yield both re-rated materially more expensive on the higher price.

**⚠️ Note on the raw Valuation Score alone: 73.2 sits inside the 70.0–79.9 "TRIM 25–30%" band** if read in isolation (ignoring Quality). The Composite Score — the number this framework actually acts on once a Quality Score exists — pulls this back to 42.9 (BUY-Standard band) because META's exceptionally high Quality Score (87.5) is weighted equally against the now much-less-cheap valuation. This is exactly the kind of divergence the Composite Score mechanism (valuation-scoring.md) was built to handle — flagged explicitly here per "no black-box outputs," since a reader skimming only the Valuation Score would draw the wrong conclusion.

---

## 10. META — Action & Category Change

**Valuation Score alone: 39.4 → 73.2** — jumps two full bands (BUY-Standard → what would be TRIM 25–30% in isolation).

**Composite Score: 26.0 → 42.9 → Action band: BUY — Standard position 3–5%** (moves from the 0.0–29.9 band to the 30.0–49.9 band — **a genuine action-category change**, from "BUY — Full position 6–8%" to "BUY — Standard position 3–5%"). This is the first category change for META's Composite Score since it was first computed (07-01).

**Practical recommendation: HOLD — no automatic fresh capital, and current weight now exceeds the newly-indicated band.** META is an existing holding at **5.43%** (holdings.md, synced 2026-09-20) — this is now **0.43pp above the top of the new 3–5% Standard-position band** (it was comfortably inside the old 6–8% Full-position band as of 08-26). The framework does not treat "above the entry-sizing band for a BUY score" as itself a trim trigger (Phase 05 trims are driven by the score crossing into the 70.0+ Composite bands, not by being oversized relative to a BUY band's suggested entry range) — so **no forced trim fires from this alone** — but it is flagged prominently as a portfolio-mechanics item worth the investor's attention (§12, §13), especially given how close the raw Valuation Score now sits to an outright trim signal.

---

## 11. META — Order Setup (Composite Score in BUY-Standard band → required)

```
python -m scripts.scoring.order_setup --input inputs.json
```

Band: 30.0–49.9 ("Set limit order"). MoS and stop-loss both set at the **conservative (high) end of their applicable ranges** (30% each), consistent with every prior META session's choice of the most conservative option in-range for this wide-moat, high-Quality-Score name.

```
Band: 30.0-49.9 (Set limit order)
Buy Price = Fair Value (641.1) x (1 - 30%) = 448.7700
Live price 715.62 vs buy price ceiling 448.7700 -> limit order at buy price (live price above ceiling); entry price used = 448.7700
Primary Sell Target = Fair Value = 641.1000
Bull-Case Trim Target = Bull FV (960.0) x 0.90 = 864.0000
Stop Loss = Entry Price (448.7700) x (1 - 30%) = 314.1390
R/R Ratio = (Sell Target 641.1000 - Entry 448.7700) / (Entry 448.7700 - Stop 314.1390) = 192.3300/134.6310 = 1.4286:1
*** FLAG: R/R 1.4286:1 is BELOW the 2:1 minimum — per Step 6, wait for lower entry, tighter stop, or pass ***
Max $ Risk = Portfolio Value (61220.66) x 1.5% = 918.3099
Risk Per Share = Entry (448.7700) - Stop (314.1390) = 134.6310
Shares by risk-based sizing = 918.3099 / 134.6310 = 6.8209
Allocation cap = Portfolio Value (61220.66) x 5% = 3061.0330 -> 6.8209 shares
Position Size (shares) = min(risk-based, cap) = 6.8209  [binding: risk-based sizing]
Position Size ($) = 6.8209 x 448.7700 = 3061.0330
Current shares held (approx., 5.43% of $61,220.66 / $715.62) = 4.6453; gap vs. target = 2.1756
```

Live price ($715.62) is **$266.85 (59.5%) above** the $448.77 buy-price limit — the widest gap on record for this ticker (was 12.60% at 08-26 PM). **Base-case R/R is 1.43:1 (fails the 2:1 minimum)** — still fails, though notably *less badly* than the persistent exact 1.00:1 seen in every prior session (the wider MoS in this new band produces a lower buy price relative to the sell target, improving nominal R/R even though it remains below threshold). **No automatic qualifying entry fires this session.**

**Position sizing:** META at **5.43%** (holdings.md), now **above** the 30.0–49.9 band's 3–5% allocation-cap range by 0.43pp. No forced trim or top-up — order-setup gates (R/R, price-above-limit) govern, and neither is met.

---

## 12. Portfolio Note

META's Composite Score changing category for the first time (BUY-Full → BUY-Standard) is a real signal, even though the practical action remains unchanged (HOLD, no top-up, no forced trim). Two things are worth the investor's attention together:

1. **The raw Valuation Score (73.2) is now inside what would be a TRIM band in isolation** — only META's exceptionally high, unchanged Quality Score (87.5) is keeping the Composite Score out of trim territory. If price continues to rise without a matching move in fair-value inputs (still built on Bull/Bear assumptions unrevised since 07-28 — §4 flag 4), the next session could plausibly cross into an actual Composite-Score TRIM band.
2. **Current weight (5.43%) now sits above the newly-indicated 3–5% Standard-position band** (it fit inside the old 6–8% Full-position band). No trim is triggered by this alone — but it means fresh capital toward META specifically is *less* justified at today's price than it was a month ago, independent of the framework's action-table mechanics.

Both flags point the same direction: **watch this name closely at the next earnings-driven re-score (28 Oct 2026)**, which will be the first to reflect the ~$10B settlement charge in filed financials and may materially move the Quality Score's Profitability/FCF-Quality sub-scores for the first time since the settlement was announced.

---

## 13. Next Review Triggers

- **Q3 2026 earnings (confirmed 28 Oct 2026, after close)** — will be the first filing to incorporate the ~$10B settlement charge into filed TTM fundamentals; likely to move Profitability, FCF Quality, and possibly Balance Sheet sub-scores materially for at least one quarter. The single most important upcoming checkpoint.
- **Bull/Bear scenario assumptions ($40.0/$28.0 EPS, 24×/13× exit multiples)** — flagged stale for the 10th+ consecutive session, now more consequential than ever given how far price has moved; overdue for a dedicated review independent of the next routine re-score.
- **Rate Gate watch:** 10Y crossed above 5% for the first time this ticker has seen (5.24%) — watch whether this new regime persists or reverts; it alone is worth ~5 points of Rate Regime Modifier either way.
- **Valuation Score proximity to the TRIM band:** raw Valuation Score (73.2) sits inside what would be a TRIM 25–30% band if Quality weren't blended in; the Composite Score (42.9) has room (7.1pp) before it would cross into the 50.0–69.9 Hold band, and considerably more before any TRIM band — but the trend this session (26.0 → 42.9 in 33 days) is the largest one-session Composite Score move on record for this ticker.
- **New Mexico AG trial** (content-moderation claims, separate from the 51-state settlement, began 8 Sep 2026) — no disclosed financial figure yet; watch for a verdict or settlement.
- **META weight (5.43%)** — now above the Composite Score's indicated 3–5% Standard-position band; not itself an action trigger, but worth the investor's awareness (§12).
- **Forward PE sub-score methodology (§4 flag 6)** — this session used the Primary ("range") formula for the first time (matching the script's literal reading of valuation-scoring.md); flagged for a maintainer decision on whether prior sessions' "fallback formula" choice should be revisited or whether this represents an intentional, if previously undocumented, convention.
- **`yfinance` Shares Outstanding / EBIT / Enterprise Value field discrepancies (§4 flags 1–3)** — same three long-standing data-quality issues, corrected the same way as every prior session; worth a maintainer follow-up on the underlying data pipeline.
- **Owner Earnings (Upgrade 1) methodology decision** — still open; Meta still discloses no maintenance-vs-growth capex split.
- **Rule 9 fundamental triggers (standing):** any further guidance revision, management change, material M&A, or a >15% unexplained price move.

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
