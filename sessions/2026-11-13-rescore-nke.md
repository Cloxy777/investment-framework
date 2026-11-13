# RESCORE — NKE (NIKE, Inc.) — 2026-11-13

**Task type:** RESCORE (mode `--both`)
**Trigger:** Manual `/rescore NVO NKE`. **No new filing** since Q1 FY2027 (10-Q 2026-10-02, scored [2026-10-11](2026-10-11-rescore-nke.md)); Q2 FY27 reports ~17 Dec 2026. Market-data refresh plus first NKE score under **SBC-as-a-cost** (methodology 2026-10-12; the 10-11 entry was flagged STALE). All TTM financial inputs carried unchanged from 10-11 (rev 45,891 / GP 19,766 / NI 3,093 / EBIT 3,853 / FCF 2,105 / SBC 688 $M).
**10Y:** 5.14% (Yahoo ^TNX 13 Nov, intraday; 11 Nov close 4.998%, 12 Nov 5.10%). **Rate Regime +10.**
**Position:** 20 sh IBKR, cost $43.31, mark $38.07 (−12.1%), 1.66% of NLV (holdings.md). No live NKE sell order (flagged since 09-27).
**Last review:** 11 Oct 2026 (Valuation 55.2, Quality 39.1, Composite 58.1 ref, HOLD).

## 1. Live price (Rule 0)
**$38.07** (bid 38.07 / ask 38.08), +0.82% day — IBKR `get_price_snapshot` (contract 10291); Yahoo 38.075. +9.0% vs 10-11 ($34.92). 52-wk $31.98–$68.06. No news-driven trigger; far below the 15% unexplained-move line.
Shares 1,484.2M (10-Q diluted wtd. avg., as 10-11) → market cap $56,503M; EV = 56,503 + 7,893 debt − 8,368 cash = $56,028M.

## 2. fetch_fundamentals (pasted)
```
Market Cap 56,553M | Forward PE 24.641 | FCF Yield 3.722% | EV/EBIT 16.018 (vendor EBIT basis) | Net Margin 6.740% | Gross Margin 43.072%
ROIC 13.071% | Rev 3yr CAGR -3.240% | FCF/NI TTM 68.057% | (FCF-SBC)/NI 45.813% | SBC yield 1.217% | Gross buyback yield 0.035%
FCF/NI annual (oldest first) = [96.1%, 116.1%, 101.5%, 70.3%] | 5yr PE avg/low/high = 27.227 / 16.284 / 39.873 (n=20)
SBC 688M vs FCF 2,105M -> 32.7% (at/above 30% watch line) | FCF yield after SBC 2.51%
cycle_peak UNKNOWN | value_trap_candidate UNKNOWN
```
Scoring uses the 10-11 TTM construction (EV/EBIT 14.54× on EBIT 3,853; ROIC 13.22%) for consistency — no new filing. The 5yr PE series is now vendor-reconstructed (16.284/27.227/39.873), replacing the 10-11 carried-forward 18.2/29.5/40.3.
**Flags:** `flags_common --forward-pe 24.64 --eps-growth 21.0` → `multiple_ceiling NONE`; `cycle_peak`, `value_trap_candidate` UNKNOWN = data gaps (trailing EPS series unavailable); value-trap does not fit (fwd PE 24.6 > 15). SBC/FCF 32.7% is handled via SBC-as-a-cost in both scores.

**Estimates (Yahoo, 39–40 analysts):** FY27 (May-27) EPS $1.252 (was $1.32 on 10-11; 30d-ago 1.277, 90d-ago 1.724); FY28 $1.516. Company guide $1.15–1.35 adj. **Forward-PE basis change (disclosed):** 10-11 used FY27 consensus ($1.32 → 26.45×). Today uses Yahoo NTM EPS $1.545 → **24.64×**, consistent with other sessions' NTM convention. FY27-basis PE would be 30.4× — see sensitivity in §4.

## 3. Quality Score (script output)
```
Profitability: NetMargin 22.47 ; ROIC 13.22% -> 44.07 ; score 33.27
Margins: GM 43.07% -> 53.84
Growth: CAGR -3.24% -> 0.00
Balance sheet: ND/EBITDA -0.10x -> 100.00
Moat: 1/5 (scale only) -> 20.00   (evidence: Q1 FY27 revenue -4%, China -26% c-n, Converse -28%, Direct -8%)
FCF Quality: (2,105-688)/3,093 = 45.81% -> clamp((0.4581-0.40)/0.60) = 9.68
Quality Score = 8.318 + 8.076 + 0 + 15.0 + 3.0 + 0.968 = 35.361 -> 35.4
# Quality Score = 35.4 — FAILS the 80.0+ gate
```
39.1 → 35.4 solely from the methodology change (FCF Quality 46.8 → 9.7). No hard disqualifier: FY26 FCF/NI 70.3% (≥70%), SBC/FCF 32.7% (<100%). Phase 04 Quality Watch continues (4th sub-gate print).

## 4. Valuation Score (script output)
Inputs: FCF yield 3.725%, SBC yield 1.218%; EV/EBIT 14.54×; Fwd PE 24.638×; PEG n/a; scenarios bull $37.65 (10-11 bull EPS $1.47 × 1.252/1.32 × 27), base $27.55 (FY27 cons $1.252 × 22), bear $24.15 (guide-low $1.15 × 21, unchanged) — multiples unchanged from 10-11; no documented catalyst (window 2yr default); intrinsic growth 0%.
```
FCF yield after SBC = 3.725% - 1.218% = 2.507% -> FCF_Score 74.930
EV/EBIT_Score = (14.542-12)/23 = 11.052
FwdPE raw = (24.638-16.284)/(39.873-16.284) = 35.415 ; dev vs 27.227 avg = -9.509% -> within +-10% -> modifier 0
PEG n/a -> weights 40/40/20 ; Raw = 41.476
Rate: EY 4.0588% - 5.14% = -1.08pp -> +5 ; 10Y>5% -> +10 ; total +15
PW FV = 0.25x37.65 + 0.5x27.55 + 0.25x24.15 = 29.225 ; gap -23.23% ; annualised -11.62%/yr
E = -11.617 + 0 + 4.343 (div 4.308 + gross buyback 0.035) = -7.27%/yr -> M = 5 + 10x0.727 = +12.274
Final = 41.476 + 15 + 12.274 = 68.750 -> 68.7
# Valuation Score = 68.7 (was 55.2)
```
**Knife-edge vs the 70.0 trim line — sensitivities:**
- 10Y 4.99% (11 Nov close was 4.998%) → Step 2 +5 → **63.7**.
- Base FV at live price → **61.8**.
- FY27-EPS forward PE (30.40×, deviation +11.65%): the script **refuses** (framework gap: the 10–20% PE-deviation band has no defined modifier, strategy.md Upgrade 2). Illustration only, hand-calc with modifier 0: FwdPE raw (30.40−16.284)/23.589 = 59.85 → +4.9 raw → **≈73.6**.

So the band outcome depends on the forward-EPS basis — flagged, not resolved. The framework gap itself needs a decision (recommend defining the 10–20% band).

## 5. Composite
`composite_score --set quality_score=35.4 --set valuation_score=68.7` → **REFUSED** (Quality < 80.0). Hand-calc reference: 0.5×(100−35.4) + 0.5×68.7 = 32.30 + 34.35 = 66.65 → **66.7**, not actionable.

## 6. Action — HOLD existing 20 sh, do NOT add
- Valuation 68.7 is in the 50.0–69.9 hold band (just under the trim band); price rise alone is never a trigger, and no Rule 9 event fired (no guidance/management/M&A change). No trim.
- Gate fails by a wide margin (35.4). Live price is 30% above PW FV $29.23 — no buy. Order setup N/A (HOLD).
- **Open items for the user:** (1) still no live NKE sell order; (2) Upgrade 4 Turnaround Sub-Gate review + override-log entry overdue across six rescores; (3) dividend $1.64/sh exceeds the FY27 EPS guide; (4) this score is within 1.3 points of the 70.0 trim line.

## 7. Stale-score mechanism
Banner dropped from the new watchlist entry; NKE row removed manually from `watchlist/STALE.md` (`stale_score --apply` returned `resolved: []` and adds a duplicate header row to STALE.md, which was reverted).

## 8. Next review trigger
Q2 FY27 earnings ~17 Dec 2026; China marketplace reset (Jan 2027); dividend change; 10Y vs 5.00%; resolve the 10–20% Historical-PE-Modifier gap.

## Glossary
- **Composite Score**: 0.50×(100−Quality)+0.50×Valuation; valid only if Quality ≥ 80.0.
- **EV/EBIT**: enterprise value ÷ operating profit.
- **FCF / FCF Yield**: operating cash flow minus CapEx / ÷ market cap.
- **Forward PE (NTM)**: price ÷ next-12-month expected EPS.
- **Hard disqualifier**: rule failing a company regardless of weighted score.
- **Historical PE Modifier**: −10/0/+10 on the Forward-PE sub-score from deviation vs the 5yr average.
- **Moat**: durable competitive advantage.
- **PW Fair Value**: 25% bull / 50% base / 25% bear.
- **Quality Score**: 0–100.0 grade; 80.0+ is the gate.
- **Rate Environment Gate / Rate Regime Modifier**: earnings-yield-vs-10Y test plus bracket add-on.
- **SBC**: stock-based compensation, treated as a real cost.
- **Turnaround Sub-Gate (Upgrade 4)**: path for gate-failers to enter small if 5 tests pass.
- **Upside/Downside Modifier**: ±15 adjustment from expected annual return vs the 10% hurdle.
