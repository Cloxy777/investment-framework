# Investor Philosophy Alignment — Reference

*Companion reference to the [7 Hybrid Upgrades](strategy.md), which are explicitly built as "evidence-based upgrades from a 40-year cross-framework stress test vs Buffett · Munger · Lynch · Fisher · Marks."*

## Purpose

A high-level summary of the core tenets of the investors whose track records and published methods inform this framework. **Before adding or changing any framework rule, check it against this list.** The goal: every rule should be traceable to, and defensible under, at least one of these philosophies — and ideally contradicted by none of them. Where a rule *does* knowingly diverge (e.g. the 15% position cap vs. Verdad's 8% backtest — see [decisions/2026-06-07-framework-change-position-cap.md](../decisions/2026-06-07-framework-change-position-cap.md)), record that explicitly as a deliberate, conscious tradeoff rather than letting it sit as an unflagged inconsistency.

## The core five

### Warren Buffett — Berkshire Hathaway (~20% CAGR over six decades)
- Buy a wonderful business at a fair price, not a fair business at a wonderful price — quality over cheapness, always in that order.
- Circle of competence: only invest in what you can understand well enough to forecast.
- Owner Earnings over reported FCF — see through accounting conventions to true cash generation (this framework's Upgrade 1).
- "Our favorite holding period is forever" — selling a wonderful business is the exception, not the routine; compounding rewards patience more than precision timing.
- Interest rates are "gravity" on all asset values — a valuation *anchor*, never a binary switch that overrides the bottom-up case.
- Mr. Market is there to serve you, not instruct you — a falling price in a quality business is an opportunity, not a sell signal.

### Charlie Munger — Berkshire Hathaway / Daily Journal
- Multi-model thinking and inversion: before asking "why will this work," ask "what would make this fail" — and check the answer against several independent mental models at once.
- Concentration over diversification: "the wise diversify in a limited way… excessive diversification is what they do when they don't know what they're doing." Conviction in fewer, better-understood names beats spreading risk thin.
- "Sit on your ass investing": the fewer high-conviction decisions you need to make — and the less you trade around them — the better. The "croupier's take" (taxes and friction from excess turnover) is a real, compounding cost.
- Technical analysis is "a bunch of nonsense" — decisions come from the business, never the chart.

### Peter Lynch — Fidelity Magellan (~29% CAGR over 13 years)
- Categorize every holding (Stalwart, Fast Grower, Cyclical, Turnaround, Asset Play, Slow Grower) and size, value, and exit each *by its category* — one universal rule misprices most of them.
- "Know what you own and why you own it" well enough to explain the thesis in two minutes; sell when *that story* breaks, not when the price moves.
- "Don't pull the flowers and water the weeds" — don't trim winners with intact stories purely to fund laggards.
- Insider buying is one of the strongest signals available: "insiders might sell their shares for any number of reasons, but they buy them for only one."
- The PEG ratio — but only for businesses that are *actually* growing (Fast Growers); applying it to cyclicals or stalwarts misprices them.

### Joel Greenblatt — Gotham Capital (~40% CAGR over ~20 years, audited)
- Systematic, rules-based discipline beats discretionary cleverness for almost everyone — a repeatable, documented process compounds; one-off brilliance doesn't.
- Never rank quality and cheapness separately — combine Return on Capital (quality) with Earnings Yield (price) into one view of "good business at a good price."
- Use capital-structure-neutral metrics (EBIT / Enterprise Value) so businesses with different debt loads can be compared fairly.
- Publish the method and the results, warts and all — transparency over decades is what makes a record trustworthy.

### Howard Marks — Oaktree Capital
- "Second-level thinking": don't just ask "is this a good company" — ask "does the consensus already know this, and is it already in the price?"
- Cycle-awareness: markets swing between greed and fear; how much risk you should be willing to take changes with where you sit in that cycle — it isn't a constant.
- Risk *control*, not risk *avoidance* — the goal is to be paid appropriately for the risk you're taking right now, not to eliminate risk altogether.
- Be suspicious of mechanical mean-reversion: a historical average is only a useful anchor if the underlying business and regime haven't *structurally* changed. "What's different this time?" is usually the right question, not an excuse.

## Quick alignment check — run this before adopting or changing any rule

1. **Price-action test** — does the rule use a chart pattern, moving average, or price level as a *decision trigger* (not just a data input)? → If yes, Buffett/Munger/Graham would reject it outright, and this framework's own Rule 0 ("never act on price movement alone," [CLAUDE.md](../CLAUDE.md)) already forbids it. *(This is exactly what closed out the old Upgrade 6 — see the 2026-06-07 decision log.)*
2. **Turnover test** — does the rule increase trading frequency without a *fundamental* change (margin, moat, ROIC, growth thesis)? → Munger's "croupier's take" and Lynch's "don't water the weeds" both argue for caution here.
3. **Mean-reversion test** — does the rule assume a historical average/multiple is still the right anchor? → Check whether the business has structurally improved (Marks' "what's different this time"); if it has, a purely backward-looking comparison will misfire. *(This is the guardrail just added to Upgrade 2.)*
4. **Macro-veto test** — does the rule let a macro or rate view *override*, rather than just *inform*, an otherwise-strong bottom-up case? → Buffett treats rates as gravity (an input); Lynch ("thirteen minutes a year on the economy") and Munger would flag anything that lets macro *veto* a great business outright. *(This is what converted the Rate Environment Gate's Step 1 from a hard block to a modifier.)*
5. **Concentration test** — does the rule push toward diversification "for safety" beyond what the quality gate (Phase 01) already earns? → Munger and Buffett's own portfolios argue the opposite: fewer, better names, sized larger, is usually the more disciplined choice — provided the upstream quality screen is doing real work.

---

## Honorable mentions (not in the core five, but worth knowing)

- **Benjamin Graham** — Buffett's teacher; originated "margin of safety" and the "Mr. Market" allegory that underlies Phase 06's "price dropped ≠ sell."
- **Terry Smith (Fundsmith)** — "Buy good companies, don't overpay, do nothing." ~3–4% annual portfolio turnover; a live, modern proof that Munger's "sit on your ass" can still beat the market today.
- **Seth Klarman (Baupost)** — *Margin of Safety*: underwrite every position downside-first — "what do I lose if I'm wrong" before "what do I gain if I'm right."

---

This file is a living reference — whenever the framework changes (per [strategy.md](strategy.md)'s Hybrid Upgrades or otherwise), revisit this checklist and update both files together so they don't drift apart.
