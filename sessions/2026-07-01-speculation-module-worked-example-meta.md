# 2026-07-01 — Speculation Module worked example: META

**Task type:** SPECULATION EVALUATION (first live test of [framework/speculation-module.md](../framework/speculation-module.md), run same-day as the module's own design). Not a Phase 02 valuation session — no Rate Environment Gate applies (that gate runs before a valuation score; nothing here changes META's on-file valuation score).

**Why this session exists:** META moved +10.07% intraday today. The user asked, in the abstract, "should we sell, lock in the upside, and re-enter later" — this session answers that using the module's actual rules and real, live-fetched numbers rather than a hypothetical.

**Data gaps flagged up front:**
- META's Quality Score under the current (2026-06-29+) methodology is **not on file** — `holdings.md` shows `?`. Not estimated here; treated as missing per Rule 0 / "never invent or estimate financial data."
- The catalyst behind today's move is an **unconfirmed** media report — Meta has not verified it and Reuters could not independently confirm it (see Sources below). Treated as an open flag, not a fact.

---

## 1. What actually happened (live data, fetched this session)

| Field | Value | Source |
|---|---|---|
| Last price | $620.01 | IBKR live snapshot |
| Change | +$56.72 (+10.07%) | IBKR live snapshot |
| Implied prior close | $563.29 | derived (620.01 − 56.72) |
| Today's volume | ≈35.61M shares | IBKR live snapshot |
| Avg 90-day $ volume | ≈$10.30B/day | IBKR live snapshot |
| Today's approx. $ volume | ≈$21B (≈2.1× average) | derived |
| 13-week high | $691.52 | IBKR misc_statistics |
| 26-week high | $743.39 | IBKR misc_statistics |
| 52-week high / low | $794.42 / $520.26 | IBKR misc_statistics |
| Price 52 weeks ago | $735.17 | IBKR misc_statistics |
| 30-day historical (realized) volatility, annualized | 32.62% | IBKR live snapshot |
| Implied volatility (current, annualized) | 45.87% | IBKR live snapshot |

**Reported cause:** Bloomberg reported Meta is developing plans to sell excess AI compute capacity, competing directly with AWS/Azure/Google Cloud — reframing Meta's ~$125–145B 2026 capex guide as a potential revenue stream. Zuckerberg had called this "definitely on the table" at the May 2026 shareholder meeting. **Meta has not confirmed this; Reuters could not independently verify it.** Volume at ~2.1× average and IV running well above realized vol both confirm this is a real, market-moving piece of news — not noise — but "real news" and "confirmed fact" are different things.

**Context that tempers the "lock in the gain" framing:** despite today's headline move, $620.01 is still below META's own price on 26 Jun 2026 (~$650, implied by holdings.md's last published 7.10% weight) and well below its 13-week ($691.52), 26-week ($743.39), and 52-week ($794.42) highs. This is a recovery bounce, not a fresh high.

## 2. Current position (live, IBKR)

6 shares, average cost $597.805, market value $3,716.31, unrealized P&L **+$129.48** (+3.6% on cost). Daily P&L alone is +$336.57 — larger than the total unrealized gain, meaning this position was underwater (≈ **−$207**) before today's move. There is no large embedded long-term gain sitting here to protect; most of the visible gain is today's single print.

Approximate weight: ≈6.8% of the last synced combined portfolio total ($54,891.48 as of 2026-06-28 — not refreshed for other positions' moves today, so treat this weight as directional, not exact).

## 3. Does this trigger a core-framework re-score? (Rule 9 check)

**No, not on the information available today.** Rule 9's price-move trigger is a **>15%** move with *no identified cause* — this is 10.07% and has an identified (if unconfirmed) cause, so it doesn't mechanically fire. Whether the underlying substance (a potential new AI-compute-selling revenue line) is itself a strategic/fundamental trigger independent of the price move: treated the same way this framework already treats unconfirmed going-concern allegations in the bearish direction — **an open flag to monitor, not a settled fact to re-score against.** If/when Meta confirms this (earnings commentary, press release, 8-K), that confirmation is the real Rule 9 trigger, and `/rescore META` should run then — using that opportunity to also get META's first Quality Score under the current methodology.

## 4. Speculation Module gate check

**Rule 1 — Eligibility gate: FAILS (unconfirmed).** META has no current Quality Score on file under the 80.0+ gate methodology. Cannot be ruled eligible or ineligible for the sleeve without running `/rescore` — not assumed here even though META is a plausible high-quality name.

**Rule 6 — Documented catalyst + window: FAILS.** The only available "catalyst" is the unconfirmed Bloomberg report itself — no company confirmation, no dated event. Per Rule 6, an unconfirmed report is a thing to watch for confirmation of, not a catalyst to trade on.

**Rule 7 — Upside estimate (for reference, since we're here — not a green light):**

```
1-SD expected move (%) = IV(annual) × √(days ÷ 365)
```

- To Jul 17 '26 expiration (16 days): 45.87% × √(16/365) = 45.87% × 0.2094 = **9.61%** → $59.56 → range **$560.45 – $679.57**
- To Aug 21 '26 expiration (51 days): 45.87% × √(51/365) = 45.87% × 0.3738 = **17.15%** → $106.33 → range **$513.68 – $726.34**

Cross-check via the Jul 17 $620 (ATM) straddle: call mid $20.50 + put mid $18.875 = **$39.375**, i.e. 6.35% of spot — a bit under the IV-based figure, as expected for near-dated straddles (straddle price runs roughly 0.8× the 1-SD move). Cross-check via the Aug 21 $650 call's own quoted implied vol (43.38% annualized, vs. 45.87% for the underlying): 43.38% × 0.3738 = 16.22% → range $519.44–$720.58 — converges well with the underlying-based estimate (~16–17% either way).

**Reading this:** the options market is already pricing a further ~10% move (either direction) by Jul 17 as roughly a 1-standard-deviation event — plausible, not remarkable. A thesis of "another leg up from here" isn't a market-beating insight; it's close to what's already priced in.

**Rule 8 — Downside estimate:** symmetric to the above — the same bands give **$560–$680** (16 days) and **$514–$726** (51 days) as the 1-SD range in both directions. If expressed via a long call, max loss = premium paid (a known, capped number, see below). If expressed via shares, a 15–20% stop would sit around $496–$527 — but note this is a name currently the subject of unconfirmed, market-moving news, exactly the setup where a stop can gap through on an overnight confirm-or-deny headline.

**Rule 3 — Per-trade sizing: FAILS at current portfolio size.** Proposed per-trade cap ≈1% of total portfolio ≈ **$549**. The cheapest reasonably-directional structure priced above — one Aug 21 '26 $650 call — costs **≈$2,947.50 per contract** (100-share multiplier), roughly **5.4× over cap**, and larger than the entire proposed 5% sleeve (**≈$2,745**) on its own. A single share at $620 also doesn't fit inside a $549 per-trade cap. At this portfolio size, there is currently no options or share structure on META that fits the sizing discipline without bending the rule.

## 5. Conclusion

**Three independent gates (1, 6, 3) all say "not yet."** No trade entered — logged in [portfolio/speculation-log.md](../portfolio/speculation-log.md) under "Evaluated but not entered." This is the module working as designed on its first real test, not a missed opportunity: chasing a same-day, unconfirmed-news pop on a name with no confirmed Quality Score, using a structure that already breaks the sizing rule, is precisely the pattern the research behind this module (Barber & Odean, day-trading loss studies) says destroys wealth.

**Recommended next steps, in order:**
1. Leave the existing 6-share core position untouched — do not sell it to "lock in" a gain that's mostly today's single print on a small position near cost basis.
2. Watch for Meta's own confirmation or denial of the AI-compute-sales report — that event, not today's price move, is the real trigger (Rule 9 for the core score; Rule 6 for the sleeve).
3. Run `/rescore META` at a normal cadence (or immediately if the report is confirmed) to get a real, current Quality Score on file — needed before META can ever be ruled eligible for the sleeve either way.

## Glossary

- **Implied volatility (IV)** — the options market's own forward-looking estimate of how much a stock might move, expressed as an annualized percentage; higher IV means the market is pricing more uncertainty.
- **Historical (realized) volatility** — how much a stock has actually moved recently (here, the trailing 30 days), annualized — the backward-looking counterpart to implied volatility.
- **1-SD (one standard deviation) move** — the price range a stock is expected to stay within roughly 68% of the time, derived from implied volatility over a given time window; used here as a market-priced upside/downside band, not a prediction.
- **ATM (at-the-money) straddle** — buying both a call and a put at the same (current-price) strike and expiration; its combined cost is a market-priced estimate of how far the stock is expected to move by that expiration.
- **IV crush** — a sharp drop in implied volatility once the event driving it resolves (confirmed or denied), which can reduce an option's value even if the stock moves in the anticipated direction.
- **Going-concern / accounting-integrity allegation** — (see [glossary.md](../framework/glossary.md)) the framework's existing pattern for treating unconfirmed claims as open risk flags, applied here in the bullish direction to the unconfirmed AI-compute report.
- **Quality Score**, **Rule 9**, **Rule 0** — see [glossary.md](../framework/glossary.md).
- **Mad money account**, **house money effect**, **time-stop** — see the Behavioral-finance & speculation section of [glossary.md](../framework/glossary.md).

Sources:
- [Meta Platforms Jumps 10% on Potential Plans to Sell AI Compute — 24/7 Wall St.](https://247wallst.com/investing/2026/07/01/meta-platforms-jumps-9-on-potential-plans-to-sell-ai-compute-challenging-amazon-microsoft-google/)
- [Meta Platforms Jumps 10% on Potential Plans to Sell AI Compute — Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/meta-platforms-jumps-9-potential-143138489.html)
- [Why is Meta Platforms stock surging today? — Investing.com](https://www.investing.com/news/stock-market-news/why-is-meta-platforms-stock-surging-today-93CH-4770607)
