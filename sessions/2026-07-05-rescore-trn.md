# RESCORE — TRN (Trainline plc, LSE:TRN) — mode `--both`

**Task type:** RESCORE (quarterly/interim held-position re-score; also TRN's first-ever **Quality Score** computation under the 2026-06-29 methodology)
**Date:** 2026-07-05
**10Y US Treasury Yield:** **4.48%** (FRED `DGS10`, most recent published daily close, dated 2026-07-01 — US Treasury cash markets were closed 2026-07-03 through the weekend for the Independence Day holiday observance, so this is the latest available reading, not a same-day quote; cross-checked against WebSearch reporting ~4.47–4.49% for 2026-07-02, consistent)
**Rate Regime Modifier in effect:** +5 (3.5–5% bracket)
**Last review:** 2026-06-24 (Rule 9 management-change re-run; Valuation Score 10.0, "BUY — Full position 6–8%"; Quality/Composite Score never computed — predates the 2026-06-29 methodology change, flagged in [watchlist/STALE.md](../watchlist/STALE.md))
**Position status:** Held, partial fill — 600 of a ~1,553-share target (see [sessions/2026-06-24-new-position-trn.md](2026-06-24-new-position-trn.md)); weight 3.04% per [holdings.md](../portfolio/holdings.md)'s last sync (2026-06-28)

---

## 0. Live orders check (context for the partial-fill question)

`get_account_orders` (fresh, this session) still shows order **1551402669** — `BUY 900 TRN @ GBX 161.50 limit`, placed 2026-06-24T16:31:15Z — in **`REPLACED`** status with `cum_shares_qty: 0`. No live successor order for the remaining ~900+ shares of the original target exists in this fetch. The position remains exactly 600 shares (`get_account_positions`, fresh), unchanged since 2026-06-24. This confirms the partial-fill status flagged in [ibkr-orders.md](../portfolio/snapshots/ibkr-orders.md) is still unresolved and no top-up action has been taken since — relevant context for §6's action recommendation below.

---

## 1. Live price (Rule 0 — fetched first)

- **IBKR `get_price_snapshot` (contract_id 371871705, Trainline plc, LSE:TRN):** last **218.00 GBX**, change −1.00 (−0.46%), prior close 219.00, mark (`plprice`) 218.0000067 — consistent with `last`. 52-week range (IBKR `misc_statistics`): low 178.00 / high 304.00 GBX; 13-week high 255.60.
- **Cross-check (Rule 0 — required, per this framework's recurring "IBKR snapshot can look stale" issue):** Yahoo Finance chart API for `TRN.L`, fetched live this session, returns `regularMarketPrice` **218.0** GBX, most recent daily close bar 218.0 — **exact match** to the IBKR snapshot. 52-week range from this source: 178.00–307.60 GBX (high differs from IBKR's 304.00 by ~1.2%; immaterial to any calc below, flagged for transparency, not resolved further).
- **Price of record for this session: 218.00 GBX = 2.1800 GBP.**
- **FX rate:** live GBP→USD rate from IBKR `get_account_balances` (fresh, this session) = **1.33505295** (broker-reported, per Rule 0 — never an assumed rate). → 218.00 GBX = 2.1800 GBP = **$2.9104 USD**.
- Price has risen **+6.54%** since the 2026-06-24 session (204.6186 → 218.00 GBX) — well under the 15% Rule 9 "unexplained move" threshold, and no specific news identified explaining it beyond general market drift (checked — see §2).

---

## 2. Data gaps flagged

- **5-year historical PE range:** still unavailable — same no-history fallback as every prior TRN session (`FwdPE_Score = 50.0`, flagged neutral).
- **EBIT / EBITDA / cashflow / balance-sheet fields via this session's live Yahoo `quoteSummary` pull returned null or internally-inconsistent values for `TRN.L`** (a data-vendor coverage gap for this ticker, not a fundamentals change):
  - `incomeStatementHistory.ebit` returned **0** for all four fiscal years (clearly wrong — FY26 net income alone is £79.8M).
  - `financialData.ebitda` returned **125,823,000 GBP** — this is **impossible** as a genuine EBITDA figure: EBITDA = EBIT + D&A, and D&A cannot be negative, yet 125,823,000 sits *below* the independently-verified FY26 EBIT of 126,429,000 GBP (see below). This corroborates the 2026-06-22 session's separate finding that this vendor's derived aggregate fields for `TRN.L` (there: `enterpriseValue`; here: `ebitda`) don't reconcile and shouldn't be trusted.
  - `cashflowStatementHistory` and `balanceSheetHistory` modules returned **no populated values** at all for this ticker this session.
  - **What *did* come through cleanly and was independently cross-checked:** `incomeStatementHistory.totalRevenue` (452,684,000 / 442,095,000 / 396,718,000 / 327,147,000 for FY26–FY23) and `netIncome` (79,813,000 for FY26) — both match the 2026-06-24 session's figures **exactly**, to the pound. Combined with the WebSearch confirmation (§5) that no new earnings report has been released since 2026-06-24 (next scheduled report is the FY2027 interim/H1, not yet due — FYE is end-February), this is sufficient basis to **carry forward unchanged** the FY26 figures this session's own pull couldn't retrieve: EBIT (126,429,000), EBITDA (167,243,000, the EBIT+D&A build used consistently since 2026-06-22 — not Yahoo's unreliable 125,823,000 field), FCF (79,547,000), Net Debt (167,426,000), Total Debt (261,946,000), Cash (59,703,000), and Invested Capital (431,498,000). None of these are invented — they are the same, previously live-sourced figures already on record, reused because no fundamental event has occurred to change them.
  - **Pre-existing (not new) minor inconsistency, carried forward unresolved:** the 06-22/06-24 sessions' "Net Debt" figure used for the Net Debt/EBITDA ratio (167,426,000) doesn't equal Total Debt − Cash (261,946,000 − 59,703,000 = 202,243,000) used for the EV bridge — two different debt/cash treatments for two different purposes, present since TRN's original evaluation. Flagged again for visibility, not re-derived (out of scope for a rescore).
- **Moat Signal evidence (Quality Score sub-score):** computed for TRN for the first time this session (Quality Score itself is new for this ticker). All five signals sourced fresh via WebSearch this session — citations and the true/false calls are in §3.
- **Freedom24 balance not re-synced this session** (last live sync 2026-06-07 per `holdings.md`) — used only as a carried-forward reference figure in the informational position-sizing calc in §7, not as a scored input. A full refresh is `/sync-portfolio`'s job, out of scope here.

---

## 3. Quality Score (first computation for TRN — 2026-06-29 methodology)

Per [quality-scoring.md](../framework/quality-scoring.md). All financial inputs are FY2026 (FYE 28-Feb-2026), reconfirmed/carried-forward per §2.

**Hard disqualifier check (must clear before the weighted score matters):**

| Disqualifier | TRN status | Result |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years w/o growth-capex explanation | FY26 99.67%, FY25 164.33% — both well above 70% | ✅ PASS (no disqualifier) |
| Net Debt/EBITDA over threshold (2.5× standard — TRN is a ticketing marketplace, not a payment network/exchange, so the asset-light override doesn't apply) | 1.001× | ✅ PASS |
| Not FCF-positive for 3+ consecutive years | FCF positive 4/4 reconstructable years | ✅ PASS |

No hard disqualifier fires — the weighted score below is the deciding factor.

**Profitability (25% weight):**
```
Net Margin = 79,813,000 / 452,684,000 = 17.632%   (fresh-confirmed this session)
ROIC = NOPAT (126,429,000 × 0.70) / Invested Capital 431,498,000 = 88,500,300 / 431,498,000 = 20.510%
  (carried forward; caveat unchanged since 06-22/06-24 — ROIC only clears >15% in FY26; FY23–25 were 7.24%/8.81%/14.80%)

NetMargin_Component = clamp((17.632/30)×100) = 58.77
ROIC_Component       = clamp((20.510/30)×100) = 68.37
Profitability_Score  = (58.77 + 68.37) / 2 = 63.57   (no FCF cap — 4/4 years positive)
```

**Margins (15% weight):**
```
Gross Margin = 82.59% (carried forward — expanding 3yr trend 77.10%→76.95%→79.69%→82.59%, unchanged fundamentals)
GrossMargin_Score = clamp((82.59/80)×100, 0, 100) = clamp(103.24, 0, 100) = 100.0
(No expansion-trend bonus applies — that bonus is only for margins still below the 40% static threshold; TRN's is already well above it and already clamped at the ceiling.)
```

**Growth (20% weight):**
```
Revenue 3yr CAGR = 11.43% (FY23 327,147,000 → FY26 452,684,000, fresh-confirmed)
Growth_Score (base) = clamp((11.43/25)×100) = 45.72
```
**TAM-expansion modifier (+10):** Documented — Trainline's International Consumer segment (European rail ticketing) is guided to reach break-even in FY2027, and Trainline Solutions (B2B API/white-label distribution into corporate-travel platforms and rail-operator branded booking interfaces) is an actively-growing, separate addressable market beyond the core UK consumer app. Cited: [Trainline FY2027 guidance commentary](https://joshthompson.co.uk/investing/trainline-fy2026-results-net-ticket-sales-up-7-percent-ebitda-rises-11-percent/), [Trainline: "Europe's Rail Operating System"](https://www.ad-hoc-news.de/boerse/news/ueberblick/trainline-plc-how-a-ticketing-platform-turned-into-europe-s-rail/68505078). → **+10**.

**Structural-deceleration modifier (−10):** Documented — YoY revenue growth has decelerated for two consecutive years (FY23→24 +21.27%, FY24→25 +11.44%, FY25→26 +2.40%), and **FY2027 guidance itself** (revenue £440–455M vs. FY26's actual £452.684M — i.e. guided to roughly **flat-to-down**) extends this trend rather than reversing it. Management attributes part of this explicitly to a **structural regulatory change** (UK industry refund-rule tightening effective April 2026 — a permanent policy shift, not a one-off) plus a **mix effect** (faster-growing International Consumer/Solutions segments diluting blended growth as they scale). This is a documented structural pattern, not a single cyclical quarter. Cited: [Trainline FY2027 guidance](https://www.directorstalkinterviews.com/trainline-reprts-net-ticket-sales-up-7-to-6-3bn-trading-in-line-with-guidance/4121244104), [FY2026 results summary](https://joshthompson.co.uk/investing/trainline-fy2026-results-net-ticket-sales-up-7-percent-ebitda-rises-11-percent/). → **−10**.
```
Growth_Score = 45.72 + 10 − 10 = 45.72   (both modifiers cited independently; they happen to net to zero)
```

**Balance Sheet (15% weight):**
```
Net Debt/EBITDA = 167,426,000 / 167,243,000 = 1.00109× (carried forward, unchanged)
BalanceSheet_Score = clamp(100×(1 − 1.00109/4), 0, 100) = 100×(1 − 0.25027) = 74.97
```

**Moat Signal (15% weight)** — computed for the first time for TRN this session; all five checked against fresh, cited evidence (WebSearch, this session):

| Signal | Verdict | Evidence |
|---|---|---|
| Market share stable/growing | **TRUE** | Trainline sells an estimated **51 of every 100** UK train tickets per a cited UK Competition & Markets Authority figure, and holds an estimated **~72% share of the UK *independent* online rail-retail market** as of 2025 (multiple third-party analyst reviews). Combined with Trainline's own revenue growth (11.43% 3yr CAGR) outpacing overall UK rail-journey volume growth, this supports "stable or growing," not merely "large." Sources: [MatrixBCG competitive landscape](https://matrixbcg.com/blogs/competitors/thetrainline), [compoundwithrene.com category-leader review](https://www.compoundwithrene.com/p/trainline-an-80-gross-margin-category). |
| Brand premium (pricing power) | **FALSE** | The opposite was found: independent comparative testing across multiple 2026 reviews consistently found Trainline to be **the most expensive booking option** (often £5–£20 more per journey than rivals) due to its booking fee, losing head-to-head price comparisons to TrainPal (zero booking fee, automatic split-ticketing) and Railboard in the majority of routes tested. This is evidence of *price competition pressure*, not a brand premium customers pay willingly. Not credited. Sources: [coolcuration.com TrainPal vs Trainline](https://coolcuration.com/trainpal-vs-trainline), [railboard.com comparison](https://www.railboard.com/articles/railboard-vs-trainline-vs-trainpal). |
| Network effect | **FALSE** | A documented two-sided-marketplace mechanism does exist (more passengers → more attractive to rail operators; a fuller operator roster → more passenger utility) — but the same source explicitly qualifies it as only "**moderate**," because "**multi-homing is pervasive**" (passengers routinely run several ticketing apps and price-compare, per the TrainPal/Railboard evidence above) — this "limits exclusive network effects." A diluted, explicitly-caveated mechanism doesn't meet the bar for a durable, exclusive moat signal. Not credited. Source: [investingwithwes.substack.com](https://investingwithwes.substack.com/p/trainline-plc-trnl). |
| Switching costs | **TRUE** | Documented mechanism: the app is built around high-frequency-user retention features — saved favourite journeys and payment methods, proactive delay/platform-change notifications — described as making the app "slightly addictive in a utilitarian sense... once your commute is set up, switching away carries real switching costs even if rivals offer similar basic functionality." Sources: [ad-hoc-news.de "Rail-First Super-App"](https://www.ad-hoc-news.de/boerse/news/ueberblick/trainline-plc-how-a-rail-first-super-app-is-quietly-becoming-europe-s/68441739), [northwestfrontiercapital.substack.com](https://northwestfrontiercapital.substack.com/p/from-subdued-guidance-to-competitive). |
| Scale cost advantage | **FALSE** | Qualitative "benefits of scale" language is documented (270+ integrated carrier partners, reinvestment capacity) but **no cost-per-unit figure versus smaller competitors** was found — the quality-scoring.md bar explicitly requires cost-per-unit data, not general scale narrative. Considered, not credited — consistent with how this framework has treated similarly qualitative-only scale claims elsewhere (e.g. NVDA's CoWoS/PUE evidence in the 2026-07-05 NVDA session). |

```
Moat_Score = (2 TRUE / 5) × 100 = 40.0
```

**FCF Quality (10% weight):**
```
FCF/NI = 79,547,000 / 79,813,000 = 99.667% (carried forward, unchanged)
FCFQuality_Score = clamp(((0.99667 − 0.40)/0.60)×100, 0, 100) = clamp(99.44, 0, 100) = 99.44
```

### Quality Score total

```
Quality Score = 63.57×0.25 + 100.0×0.15 + 45.72×0.20 + 74.97×0.15 + 40.0×0.15 + 99.44×0.10
             = 15.8925 + 15.00 + 9.144 + 11.2455 + 6.00 + 9.944
             = 67.23 → 67.2
```

**⚠️ Quality Score = 67.2 — FAILS the 80.0+ gate.** This is TRN's **first-ever** computed Quality Score (Quality Score column has read "?" in `holdings.md` since 2026-06-29). No individual hard disqualifier fires — every Phase 01 binary threshold from the original 06-22/06-24 evaluations still passes on its own terms. The failure is purely the weighted average: **middling Profitability** (63.57 — solid but not exceptional net margin/ROIC), a **weak Moat score** (40.0 — only 2 of 5 signals credited, with brand premium and network effect actively undercut by cited price-competition and multi-homing evidence respectively), and a **Growth score whose TAM-expansion and structural-deceleration modifiers net to zero** (45.72) rather than reinforcing each other. This is the strict gate working as designed — see quality-scoring.md's own commentary that this is "the intended behaviour of a strict gate."

---

## 4. Rate Environment Gate

- **Step 1 — Earnings Yield Spread Test:** Forward PE = 218.00/100 GBP ÷ 0.26552 GBP forward EPS = **8.2103×** (fresh live price ÷ forward EPS, unchanged from 06-24 — no new estimate revision found). EY = 1/8.2103 = **12.180%**. Spread = 12.180% − 4.48% = **+7.70pp** ≥ +1.5% → **no flag** (+0).
- **Step 2 — Rate Regime Modifier:** 10Y = 4.48%, in the 3.5–5% bracket → **+5**.
- **Combined Rate Gate modifier: +5** — same bracket as 06-24 (rates have drifted only slightly, 4.493%→4.48%).

---

## 5. Valuation Score (re-verifying the 10.0 Rule 9 score with fresh data, 11 days on)

**No new Rule 9 trigger found this session.** Checked explicitly via WebSearch: no new earnings release (next report, FY2027 interim, not yet due); a Non-Executive Director appointment (Niall McBride, Audit & Risk Committee Chair, effective 1 July 2026) occurred but is a **board-committee appointment, not a CEO/CFO-level management change** — doesn't rise to a Rule 9 trigger on its own; no new GBR-timeline news (still tracking toward 2027 full operational launch, consistent with "late 2026 at the earliest," see §5c below); no guidance revision (FY2027 guidance reconfirmed identical to the figures cited 06-24: revenue £440–455M, net ticket sales £6.2–6.45bn, adj. EBITDA margin ~2.9% up from FY26's 2.80%); price move +6.54% since 06-24, well under the 15% unexplained-move threshold and not itself a trigger.

### PEG (Upgrade 3) eligibility — unchanged

No new fiscal year reported, so the same ruling stands: **PEG N/A** (FY23's anomalous 4.0% effective tax rate still distorts the multi-year EPS-growth base; ROIC/net margin still only cross Phase 01's >15% bar in the single most recent year). PEG's 15% weight stays redistributed to EV/EBIT (→40%).

### Sub-scores (fresh price, fresh shares outstanding)

Shares outstanding (fresh, live pull) = **349,035,615** (down from 351,503,062 on 06-24 — continued buybacks, ~0.7% reduction over 11 days).
Market Cap = 349,035,615 × 2.1800 GBP = **760,897,641 GBP** (cross-checked against Yahoo's own `marketCap` field, 760,897,600 — matches to the pound).

**FCF Yield (40% weight):**
```
FCF Yield = 79,547,000 / 760,897,641 = 10.454%
FCF_Score = clamp(100×(1 − 10.454/10), 0, 100) = clamp(−4.54, 0, 100) = 0.00   (still saturated at the floor)
```

**EV/EBIT (40% weight, PEG-redistributed):**
```
EV = MarketCap 760,897,641 + Total Debt 261,946,000 − Cash 59,703,000 = 963,140,641 GBP
EV/EBIT = 963,140,641 / 126,429,000 = 7.618×
EV/EBIT_Score = clamp((7.618−12)/23×100, 0, 100) = clamp(−19.05, 0, 100) = 0.00   (still saturated at the floor)
```

**Forward PE + Historical PE Modifier (20% weight):**
```
Forward PE = 8.2103× (from §4). No 5yr PE history reconstructable (§2) → no-history fallback:
FwdPE_Score = 50.0 (neutral, flagged) — unchanged
```

**PEG:** N/A — redistributed to EV/EBIT.

### Raw weighted score

| Sub-score | Weight | Score | Weighted |
|---|---|---|---|
| FCF Yield | 40% | 0.00 | 0.00 |
| EV/EBIT | 40% | 0.00 | 0.00 |
| Forward PE | 20% | 50.00 | 10.00 |
| **Raw weighted score** | | | **10.00** |

Identical to 06-24 — both FCF and EV/EBIT remain deeply saturated at their floor even with fresh price/share-count inputs; only the price-independent no-history FwdPE fallback contributes.

**+ Rate Gate modifier: +5** → **15.00** (before Upside/Downside).

### 5c. Upside/Downside (Expected-Return) Modifier — full recalc

**Fair Value:**
- **DCF component: 345.6 GBX (carried forward, unchanged).** Same basis as 06-24 — FY26 financials/guidance are unchanged, so the 3-scenario DCF (Bull 560.5 / Base 325.2 / Bear 171.5 GBX, 25/50/25 weighted) is output-identical. The ~0.7% share-count drift from ongoing buybacks since 06-24 is immaterial at this model's 1-decimal precision and isn't re-derived.
- **Multiples component — fresh peer pull this session** (Rule 5 caveat unchanged: thin, size-mismatched peer set, 20% discount applied):
  - Peer EV/EBITDA (fresh): BKNG 14.084× / EXPE 12.485× / MMYT 34.325× / TRIP 13.367× (TCOM excluded, still negative EV/EBITDA) → median **13.7255×** (up from 12.317× on 06-24 — peers re-rated over the 11-day window) → implied EV = 13.7255 × TRN EBITDA 167,243,000 = 2,295,489,615 GBP → implied equity = 2,295,489,615 − Net Debt 167,426,000 = 2,128,063,615 GBP → implied FV/share = 2,128,063,615/349,035,615 = 609.70 GBX → discounted 20% → **487.76 GBX**.
  - Peer Forward PE (fresh): BKNG 15.001× / EXPE 11.633× / MMYT 25.988× / TRIP 8.861× → median **13.317×** × forward EPS 0.26552 GBP = 353.59 GBX → discounted 20% → **282.88 GBX**.
  - **Multiples-Based FV = average(487.76, 282.88) = 385.32 GBX.**
- **Blended FV = 0.40×345.6 + 0.60×385.32 = 138.24 + 231.19 = 369.43 GBX.**

**Sanity check:** 13-analyst consensus (fresh) mean **351.46 GBX** / median **350.0 GBX**, range 220–580 GBX — unchanged from 06-24. The independently-derived 369.43 GBX now sits **~5.1% above** consensus mean (widening from ~2% on 06-24), driven mainly by the peer-multiple re-rating above. Still comfortably inside the 220–580 analyst range — flagged as a widening but not extreme gap.

```
Gap Upside % = (369.43 / 218.00) − 1 = +69.46%
Catalyst window = 2.0 years (unchanged — see below)
Annualized gap = 69.46% / 2.0 = 34.73%/yr
Intrinsic growth = 11.5%/yr (carried forward — FY2027 guidance reconfirmed unchanged this session)
Shareholder yield = 0% dividend + 9.46% net buyback yield (FY26 annual figure, carried forward — corroborated qualitatively by the further ~0.7% share-count reduction observed this session, consistent with the buyback program continuing at pace)

E = 34.73 + 11.5 + 9.46 = 55.69%.  H = 10%.  E ≥ H → uncapped M would be −15.0 (hits the floor)
```

**Guardrail 1 re-checked this session (catalyst reliability) — WebSearch confirms GBR's timeline has not firmed up materially:** branding rollout is visibly underway (first GBR-liveried train, May 2026; first GBR-branded station, Cambridge South, opened 28 June 2026), but the government's own staged policy-publication timetable places **GBR's full operational launch in 2027, not before** — i.e. still outside a confidently-dated 18–24 month window from today. This is consistent with (arguably firming toward the back half of) the same "late 2026 at the earliest" uncertainty already on record since 06-22/06-24; nothing resolves the underlying timing risk. **Guardrail 1 stays applied — capped at −5.0.**

**M = −5.0.**

### Final Valuation Score

```
Final Score = 15.00 (raw + Rate Gate) + (−5.0) (Upside/Downside, guardrail-capped) = 10.00
```

**Final Valuation Score = 10.0 — unchanged from 06-24.** The 2026-06-24 Rule 9 re-run score holds up under fresh data 11 days later: both floor-saturated sub-scores (FCF Yield, EV/EBIT) and the guardrail-capped modifier are each individually robust to the price move and peer-multiple drift observed this session.

---

## 6. Composite Score

```
Composite Score = 0.50 × (100 − Quality Score) + 0.50 × Valuation Score
                = 0.50 × (100 − 67.2) + 0.50 × 10.0
                = 0.50 × 32.8 + 5.0
                = 16.4 + 5.0
                = 21.4
```

**Composite Score = 21.4** — numerically lands in the "**BUY — Full position 6–8%**" band (0.0–29.9) per the Phase 03 action table. **Per this framework's established practice for existing holdings whose Quality Score fails the 80.0+ gate (the 2026-07 rescore batch — AMZN, GOOG, MSFT, NOW, NFLX, NVO, SPGI, and NKE's 2026-07-01 session), this numeric result is a false green light and must not be acted on at face value.** The action call below is driven by the Quality Gate failure, not by this Composite number.

---

## 7. Action recommendation — HOLD existing 600 shares; do **NOT** complete the partial-fill top-up

Two things are true simultaneously here, and it's worth being explicit about which one is actually doing the work:

**(a) The order-setup mechanics do NOT independently block this trade** — unlike some other quality-gate-fail cases in this framework (e.g. NKE, where R/R also failed on its own terms), TRN's numbers would clear every other gate:

| Field | Value |
|---|---|
| Blended Fair Value | 369.43 GBX |
| Margin of Safety (Score 0.0–29.9 band, top of range) | 20% |
| Buy Price | 369.43 × 0.80 = 295.54 GBX |
| Live price (218.00 GBX) vs. Buy Price | 26.3% below → "enter now" if eligible |
| Primary Sell Target | 369.43 GBX |
| Bull-Case Trim Target | 560.5 × 0.90 = 504.45 GBX |
| **Stop Loss — re-anchoring required (same degeneracy as 06-24, transparently re-applied):** the formula `Buy Price × (1 − loss%)` produces stops (236.44–221.66 GBX at 20–25% loss) that sit *above* the live price — a live price fallen far below the theoretical Buy Price makes the Buy-Price-anchored stop meaningless. Re-anchored to the live entry price instead (same resolution as 06-24, consistent with how R/R already uses Entry Price): 20% from live entry → **174.40 GBX** (chosen, tightest end) | |
| Flag | Chosen stop (174.40) again sits below the 52-week low (~178.0 GBX) — same real consequence of price trading near 52-week lows, not a calculation error |
| **R/R** | (369.43 − 218.00) / (218.00 − 174.40) = 151.43 / 43.60 = **3.47:1** — clears the 2:1 minimum comfortably |

**(b) The sole, sufficient blocker is the newly-computed Quality Score (67.2 < 80.0).** Per [quality-scoring.md](../framework/quality-scoring.md): *"A company must score 80.0 or higher to be eligible for Phase 02 valuation scoring and the Composite Score at all... Below 80.0, stop — don't proceed to valuation, regardless of how cheap the stock looks."* Applied to the specific decision in front of this session — whether to place a fresh order for the remaining ~900+ shares to complete the original ~1,553-share target — that discipline points the same direction as it would for a brand-new candidate: **don't add**, however attractive the numbers otherwise look.

**The Turnaround Sub-Gate (Upgrade 4) doesn't offer an alternate path either:** it requires historical ROIC >15% for ≥5 of the past 10 years, and TRN's ROIC has only cleared 15% in the single most recent fiscal year (FY26) — the same "recently-profitable, unreliable base" pattern that already disqualifies PEG eligibility. TRN isn't a *formerly*-qualified company that stumbled (the Fallen Angel framing Upgrade 4 is built for); it's a company that has never yet cleared the bar on a graded basis. No conditional-entry path applies.

**Per [rescore.md](../.claude/commands/rescore.md) / operating-brief.md, an existing holding is not retroactively force-exited on quality alone** — so this session does **not** recommend selling the 600 shares already held. But a held position's first-ever Quality Score landing well below the gate is itself "a signal worth surfacing" (Phase 04 Quality Watch escalation) — this is not yet the kind of *actively deteriorating* moat evidence that drove NKE's harder-edged framing (Trainline's moat signals were never fully established, rather than documented as eroding from a formerly-stronger position), so this reads as a **"never quite cleared the bar" flag, not a value-trap red flag on NKE's order** — but it is exactly the situation the 80.0+ gate exists to catch before more capital goes in.

**Net: HOLD the existing 3.04%-weight, 600-share position. Do NOT re-initiate the ~900-share top-up order (the `REPLACED` order 1551402669 at GBX 161.50 should not be reissued at this price or any other price at this time).** The very-cheap-looking Composite Score (21.4) and the individually-clearing R/R (3.47:1) reflect a real price/expected-return gap, but neither overrides the newly-quantified quality shortfall — consistent with this framework's own instruction that the score "informs but never overrides" a quality-gate judgment call.

### Informational-only order setup (shown for transparency, per "no black-box outputs" — NOT being executed)

Had the Quality Gate not intervened, here is what completing the position would have looked like, using a same-day, non-fully-refreshed portfolio-value estimate (IBKR NLV $43,102.65, fresh this session, + Freedom24 NAV $15,123.54, last synced 2026-06-07 — a full combined refresh is `/sync-portfolio`'s job):

```
Entry (USD) = 2.1800 GBP × 1.33505295 = $2.9104/share
Stop (USD)  = 1.7440 GBP × 1.33505295 = $2.3288/share
Risk/share  = $2.9104 − $2.3288 = $0.5816
Max $ risk  = 1.5% × $58,226.19 ≈ $873.39
Risk-based total target shares ≈ $873.39 / $0.5816 ≈ 1,502 shares (≈$4,371, ≈7.51% of the estimated portfolio)
Allocation cap (Score 0.0–29.9): 6–8% ≈ $3,493.57–$4,658.10
Position Size = min(risk-based ≈$4,371, cap $4,658.10) ≈ $4,371 — well inside the 15% hard cap ($8,733.93)
Incremental top-up implied: ≈1,502 − 600 ≈ 902 shares (≈$2,624 at live price)
```
**Not executed. Shown only so the "if still BUY-eligible" check requested for this rescore is fully transparent — the answer to that check is that it would be size-eligible, but it is not gate-eligible, and the gate governs.**

---

## 8. Portfolio Rebalancing Summary

N/A — single-ticker rescore, no other position touched this session.

---

## 9. Next Review Trigger

- **Mandatory:** Trainline's FY2027 interim/H1 results (next scheduled report) — Rule 9; will also resolve this session's EBIT/cashflow/balance-sheet data-vendor gap (§2) with a fresh primary-source filing.
- **Quality Watch follow-up:** re-run the Moat Signal checklist at the next rescore — specifically whether TrainPal/Railboard price competition intensifies (would further weaken the already-uncredited Brand Premium signal) or whether Trainline responds with fee changes or bundled loyalty features that could newly support Switching Costs/Brand Premium evidence.
- Any GBR-related announcement in either direction (a confirmed operational launch date, or further delay/clarification of Trainline's continuing retailer role post-GBR) — still the binding constraint on Guardrail 1's cap.
- Ian Brown's full CEO/Board handover (28 Sept 2026, per the 06-24 Rule 9 session) — a check-in once he's in seat, not a re-score trigger on its own unless paired with a strategy reset, guidance revision, or M&A signal.
- Standard Rule 9 triggers: guidance revision, M&A, >15% unexplained price move, management change.

---

## 10. Glossary

- **CAGR** — Compound Annual Growth Rate.
- **Composite Score** — this framework's 0.0–100.0 blended ranking (0.0 = most attractive) combining Quality and Valuation Scores 50/50; computed only for reference here since Quality fails the gate.
- **D&A** — Depreciation & Amortization.
- **DCF** — Discounted Cash Flow.
- **EBIT / EBITDA** — operating profit before interest and taxes / before interest, taxes, depreciation and amortization.
- **EPS** — Earnings Per Share.
- **EV / EV/EBIT, EV/EBITDA** — Enterprise Value / Enterprise Value divided by operating-profit measures.
- **EY (Earnings Yield)** — 1 ÷ Forward PE.
- **Fast Grower** — Peter Lynch's term for >15%/yr EPS growth for 3+ years; this framework's PEG-eligibility trigger.
- **FCF / FCF Yield / FCF/NI conversion ratio** — Free Cash Flow; FCF ÷ Market Cap; FCF ÷ Net Income (checks earnings quality).
- **Forward PE** — Price ÷ next-12-months expected EPS.
- **FV / PW Fair Value** — Fair Value / Probability-Weighted Fair Value (25% bull + 50% base + 25% bear).
- **GBR (Great British Railways)** — UK rail-nationalization program; relevant to TRN as a regulatory/political risk to its retailer role.
- **GBX / pence (GBp)** — 1/100th of a British pound; LSE quoting convention.
- **Hard disqualifier** — one of three Quality Score conditions that fails a company regardless of weighted score.
- **Hurdle rate** — the minimum acceptable annual return (10% in this framework).
- **Moat** — a durable competitive advantage protecting a business's profits.
- **MoS (Margin of Safety)** — the discount below fair value demanded before buying.
- **Multi-homing** — customers using multiple competing platforms rather than committing to one, which dilutes an otherwise-plausible network effect; cited this session as the reason TRN's network-effect moat signal wasn't credited.
- **Net Debt/EBITDA** — leverage ratio; this framework's balance-sheet-risk gate.
- **NOPAT** — Net Operating Profit After Tax (EBIT × (1 − tax rate)).
- **PE (Price-to-Earnings) ratio**, **PEG ratio** — standard valuation multiples; PEG = PE ÷ growth rate.
- **PW (Probability-Weighted) Fair Value** — 25% bull + 50% base + 25% bear blended estimate.
- **Quality Score** — this framework's 0.0–100.0 score (0.0 = lowest quality) grading profitability, margins, growth, balance sheet, moat, and FCF quality; 80.0+ required to reach Phase 02 valuation scoring.
- **Rate Environment Gate / Rate Regime Modifier** — the mandatory pre-score interest-rate check.
- **R/R (Risk/Reward ratio)** — expected gain ÷ expected loss on a trade; 2:1 minimum required.
- **ROIC** — Return on Invested Capital.
- **Rule 0** — always fetch a live price before any valuation work.
- **Rule 5** — comparables-set quality requirement.
- **Rule 9** — fundamental events that force an immediate re-score.
- **Turnaround Sub-Gate** — the conditional path (Upgrade 4) letting a company failing some quality criteria still enter as a small position if it passes 5 specific tests; TRN doesn't qualify (fails the historical-ROIC condition).
- **Upside/Downside Modifier (Expected-Return Modifier)** — the ±15 additive score adjustment based on expected annual return.
- **Value trap** — a stock that looks statistically cheap but stays cheap because the underlying business quality was never strong enough (or is deteriorating) to support a re-rating — the risk the Quality Gate/Composite Score are designed to surface.
- **WACC** — Weighted Average Cost of Capital.
