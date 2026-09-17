# NEW POSITION — LCID (Lucid Group, Inc., NASDAQ) — 2026-09-17

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6)
**Date:** 17 Sep 2026, ~18:08 UTC top post / session run ~20:04 UTC
**10Y US Treasury Yield:** 5.00% (FRED `DGS10`, most recent posted observation dated 2026-09-15) — recorded for header completeness only; **never used**, since Phase 02 is never reached (see §4).
**Rate Regime Modifier:** N/A this session — not reached.
**Current LCID portfolio weight:** 0% — not held (confirmed absent from [holdings.md](../portfolio/holdings.md))
**Prior coverage:** [`watchlist/not-in-portfolio/LCID/LCID-2026-07-14.md`](../watchlist/not-in-portfolio/LCID/LCID-2026-07-14.md) — first evaluation 2026-07-14 (Quality Score 23.0, hard disqualifiers fired: not FCF-positive 3yr, Net Debt/EBITDA effectively fails given negative EBITDA). Not on [watchlist/STALE.md](../watchlist/STALE.md).
**Sector:** Automotive — Electric Vehicles (luxury BEV manufacturer)
**First-use jargon decode:** see closing Glossary (§5).

---

## 0. Trigger — why this session exists, and why the post is not used as data

**tarasguk** channel, post `tarasguk/11966` (2026-09-17T18:08:15 UTC — this run's new top post; marker was `tarasguk/11963`, delta 3, two intervening posts (`#11964`, `#11965`) both re-covering the already-actioned NVDA/Jensen Huang chip-demand story from earlier today, not independently evaluated per the command's single-latest-post-per-run scope):

> "🚕 Bolt купить 25 000 роботаксі 4-го рівня автономності у Lucid для запуску їх по всій Європі 🇪🇺 Роботи будуть на базі майбутньої середньорозмірної платформи Lucid та технології Hyperion від Nvidia. 🚕Нагадаю, що $UKLON нещодавно оголосив про запуск автономного таксі в 🇺🇦 Борисполі і плани впровадження роботаксі."

(Translation: Bolt will buy 25,000 Level-4-autonomous robotaxis from Lucid to launch across Europe, built on Lucid's future midsize platform and Nvidia's Hyperion technology; also notes Ukrainian ride-hailing app Uklon recently announced an autonomous-taxi launch in Boryspil.)

Per CLAUDE.md Rule 0, this post is a **trigger only**. Independent verification via WebSearch confirms a real, same-day event: Lucid and Bolt (Bolt Autonomous Driving Solutions) announced a **non-binding memorandum** to deploy at least 25,000 Level-4 robotaxis across European cities starting 2028, built on Lucid's Midsize platform and Nvidia's Hyperion AV architecture — no money changing hands yet, no firm order. LCID shares rose on the news (up ~6-10% intraday across sources). Sources: [Yahoo Finance](https://finance.yahoo.com/markets/stocks/article/lucid-stock-jumps-on-25000-robotaxi-deal-with-europes-bolt-132433027.html), [InsideEVs](https://insideevs.com/news/808650/lucid-bolt-robotaxi-partnership-europe/), [247wallst.com](https://247wallst.com/investing/2026/09/17/lucid-surges-10-on-25000-vehicle-bolt-robotaxi-deal-for-europe-rivian-rises-5/), [autonext.co](https://www.autonext.co/news/bolt-lucid-25000-robotaxis-europe-2028-midsize-nvidia-hyperion).

`$UKLON` names a private Ukrainian company (Uklon) — not publicly traded, no ticker to resolve per Rule 0; not actioned. Nvidia (NVDA) is mentioned only incidentally as a technology partner in the Lucid/Bolt story, not the subject of a fresh claim — already actioned earlier today via this run's NVDA rescore (see `telegram-watch.md` mention log), no separate action here.

**Decision to trigger:** LCID is `Not held`, with a prior `watchlist/not-in-portfolio/` entry (2026-07-14). This post claims materially new information beyond that entry — a specific, large-scale (25,000-unit) commercial demand signal from a named counterparty, not previously reflected — so per `/telegram-scan` step 4, `/new-position LCID` is triggered again. This session independently re-derives the Quality Score from fresh data; it does not treat the deal claim itself as a scored input.

---

## 1. Live Price (Rule 0)

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$4.28** | IBKR `get_price_snapshot` (contract_id **810758322**, NASDAQ, "LUCID GROUP INC"), `last` field, fetched 2026-09-17 ~20:04 UTC, `is_close: false`, `halted: false` |
| Change vs. prior close | +$0.24 / **+5.94%** on the day | IBKR `get_price_snapshot` `change` field (prior close $4.04) — consistent with the Bolt/Lucid deal news |
| Bid / Ask | $4.28 (533) / $4.30 (491) | IBKR `get_price_snapshot` |
| 52-week range | Low $2.37 · High $25.23 · Open (52w ago) $19.67 | IBKR `get_price_snapshot` `misc_statistics` |
| YTD change | −59.51% | IBKR `get_price_snapshot` |
| US 10Y Treasury yield | 5.00% | FRED `DGS10`, as-of 2026-09-15 (header only, not used — see §0) |

Market cap at this price ≈ **$1.69B** (yfinance `marketCap`).

---

## 2. Quality Score — Phase 01 (per [quality-scoring.md](../framework/quality-scoring.md))

All financial data via `yfinance` (annual + quarterly financials/cashflow/balance sheet), fetched fresh this session. Cross-check: this session's FY2023–FY2025 FCF figures (−$3.400B / −$2.904B / −$3.800B) match the 2026-07-14 session's SEC-primary-sourced figures exactly — confirms `yfinance` reliability for this name.

### 2.1 Hard disqualifiers (checked first — fail regardless of weighted score)

| Disqualifier | Test window | Result |
|---|---|---|
| Not FCF-positive for 3+ consecutive years | FY2023 −$3.400B, FY2024 −$2.904B, FY2025 −$3.800B (rolling window per the 2026-08-05 clarification — most recent 3 completed fiscal years) | **FIRES.** Every year negative, no carve-out available for this disqualifier. |
| Net Debt/EBITDA over threshold (2.5× standard) | Net Debt (Q2 2026, latest) $2.521B ÷ TTM EBITDA **−$3.588B** | **FIRES (effectively).** EBITDA is deeply negative — the ratio is mechanically undefined/meaningless as a leverage multiple, meaning **zero capacity to service debt from operations**, which is worse than any finite multiple over the threshold. Same treatment as the 2026-07-14 session. |
| FCF/NI conversion <70% for 2+ years w/o growth-capex explanation | Both FCF and Net Income are negative every year (not a "conversion" scenario) | **N/M** — formula is not meaningful when both numerator and denominator are losses; moot given the two disqualifiers above already fire unconditionally. |

**Two hard disqualifiers fire.** Per quality-scoring.md: "a weighted average can't average away an outright balance-sheet or cash-flow-quality failure." **Session stops here — Phase 02 valuation is not run.**

### 2.2 Full sub-score computation (shown for completeness/audit trail, per "no black-box outputs" — not what determines the outcome, the hard disqualifiers above do)

| Input | Value | Source |
|---|---|---|
| Net Margin (TTM) | −249.2% (profitMargins) | yfinance `info` |
| ROIC (TTM) | Not separately disclosed; EBIT deeply negative every period (FY2025 EBIT −$2.605B) → NOPAT negative → ROIC negative | yfinance `financials` |
| Gross Margin (TTM) | −100.6%; 3yr trend FY2022 −170.6% → FY2023 −225.2% → FY2024 −114.3% → FY2025 −92.8% (improving, still deeply negative) | yfinance `financials` |
| Revenue 3yr CAGR | FY2022 $608.18M → FY2025 $1,353.79M = **+30.6%** CAGR; TTM revenue growth (yoy) +56.2% per `info` | yfinance `financials` |
| Net Debt/EBITDA | $2.521B / −$3.588B (see §2.1) | yfinance |
| Moat signals | Only **Brand Premium** cited true (MotorTrend 2022 Car of the Year; EPA longest-range-EV record — evidence carried forward from 2026-07-14 session, non-time-sensitive facts, not re-verified this session since immaterial to outcome) — 1/5 | Carried from 2026-07-14 session |
| FCF/NI ratio | N/M (§2.1) | — |

```
NetMargin_Component = clamp((−249.2/30)×100, 0, 100) = 0.0
ROIC_Component       = 0.0 (negative EBIT/NOPAT)
Profitability_Score  = (0.0 + 0.0) / 2 = 0.0   (FCF-cap of 40.0 moot — already 0)

GrossMargin_Score = clamp((−100.6/80)×100, 0, 100) = 0.0
  + 10 (structural improvement trend, −225.2%→−92.8% over 3yr, documented from own financials) = 10.0

Growth_Score = clamp((30.6/25)×100, 0, 100) = 100.0 (capped; no deceleration evidence)

BalanceSheet_Score = mechanically clamp(100×(1−(2.521/−3.588)/4)) = 100.0 (formula overflow —
  not used; hard disqualifier above governs. Shown only to demonstrate why this sub-score
  is not trustworthy in isolation for a negative-EBITDA business.)

Moat_Score = (1/5)×100 = 20.0

FCFQuality_Score = N/M (both FCF and NI negative — mechanically clamp(((0.872−0.40)/0.60)×100)
  = 78.7 if computed naively, but this is not a genuine "conversion" and is not used)

Quality Score (informational only, disqualifiers already govern) =
  0.0×0.25 + 10.0×0.15 + 100.0×0.20 + [0.0 corrected]×0.15 + 20.0×0.15 + [0.0 corrected]×0.10
  = 0 + 1.5 + 20.0 + 0 + 3.0 + 0 = 24.5   (using a corrected 0.0 for the two disqualifier-affected
  sub-scores, consistent with the 2026-07-14 session's treatment; the naive mechanical reading
  using the raw overflowed sub-scores would be ≈47.4 — either way, far below 80.0 and moot given
  the hard disqualifiers)
```

**24.5 / 100.0 < 80.0 — fails the gate, independent of and in addition to the two hard disqualifiers.**

---

## 3. Recommendation

**PASS — do not enter, do not track for entry.** Quality Score fails the strict 80.0+ gate decisively (two hard disqualifiers fire: not FCF-positive in any of the last 3 fiscal years; Net Debt/EBITDA effectively unmeasurable/failing given deeply negative EBITDA). The Bolt/Lucid robotaxi partnership is real (independently verified) but is a **non-binding memorandum for a 2028 deployment, no revenue yet** — it does not change any of the trailing financial facts that drive this Quality Score, and a single forward-looking commercial announcement cannot offset three consecutive years of severe cash burn and structurally negative gross margins. Per the framework's strict-gate design, this is the intended outcome, not a reason to loosen the gate.

No fair-value/order-setup section — Phase 02/03 not reached.

## 4. Next review trigger

Lucid's Q2 2026 10-Q/Q3 2026 quarterly report (next scheduled filing) — check whether the gross-margin improvement trend continues, whether FCF burn narrows, and whether the Bolt deal converts from a memorandum into a firm, revenue-bearing order (a firm order with disclosed pricing/timing would be a legitimate future Growth-sub-score input, still gated by the same hard disqualifiers until FCF/leverage fundamentals actually change). Also: any credible confirmation of additional capital raises, or a change in the Ayar-related liquidity dependency noted in the 2026-07-14 session.

---

## 5. Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used above: **Quality Score**, **Hard disqualifier**, **FCF** / **FCF Yield** / **FCF/NI conversion ratio**, **EBITDA**, **Net Debt/EBITDA**, **Net Margin**, **Gross Margin**, **ROIC**, **CAGR**, **TTM**, **Moat Signal**, **N/M (Not Meaningful)**, **AV (Autonomous Vehicle)** — all already defined, no new terms this session.
