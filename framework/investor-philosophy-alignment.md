# Investor Philosophy Alignment — Reference

*Companion reference to the [7 Hybrid Upgrades](strategy.md), explicitly built as "evidence-based upgrades from a 40-year cross-framework stress test vs Buffett · Munger · Lynch · Fisher · Marks."*

## Purpose

High-level summary of core tenets of investors whose track records and published methods inform this framework. **Before adding or changing any framework rule, check it against this list.** Goal: every rule traceable to, and defensible under, at least one of these philosophies — ideally contradicted by none. Where a rule *does* knowingly diverge (e.g. 15% position cap vs. Verdad's 8% backtest — see [decisions/2026-06-07-framework-change-position-cap.md](../decisions/2026-06-07-framework-change-position-cap.md)), record that explicitly as a deliberate, conscious tradeoff rather than letting it sit as an unflagged inconsistency.

## The core five

### Warren Buffett — Berkshire Hathaway (~20% CAGR over six decades)
- Buy wonderful business at fair price, not fair business at wonderful price — quality over cheapness, always in that order.
- Circle of competence: only invest in what you can understand well enough to forecast.
- Owner Earnings over reported FCF — see through accounting conventions to true cash generation (this framework's Upgrade 1).
- "Our favorite holding period is forever" — selling a wonderful business is the exception, not the routine; compounding rewards patience more than precision timing.
- Interest rates are "gravity" on all asset values — a valuation *anchor*, never a binary switch overriding the bottom-up case.
- Mr. Market is there to serve you, not instruct you — falling price in a quality business is opportunity, not sell signal.

### Charlie Munger — Berkshire Hathaway / Daily Journal
- Multi-model thinking and inversion: before asking "why will this work," ask "what would make this fail" — check the answer against several independent mental models at once.
- Concentration over diversification: "the wise diversify in a limited way… excessive diversification is what they do when they don't know what they're doing." Conviction in fewer, better-understood names beats spreading risk thin.
- "Sit on your ass investing": fewer high-conviction decisions, less trading around them, the better. "Croupier's take" (taxes and friction from excess turnover) is real, compounding cost.
- Technical analysis is "a bunch of nonsense" — decisions come from the business, never the chart.

### Peter Lynch — Fidelity Magellan (~29% CAGR over 13 years)
- Categorize every holding (Stalwart, Fast Grower, Cyclical, Turnaround, Asset Play, Slow Grower) and size, value, exit each *by its category* — one universal rule misprices most of them.
- "Know what you own and why you own it" well enough to explain the thesis in two minutes; sell when *that story* breaks, not when price moves.
- "Don't pull the flowers and water the weeds" — don't trim winners with intact stories purely to fund laggards.
- Insider buying is one of strongest signals available: "insiders might sell their shares for any number of reasons, but they buy them for only one."
- PEG ratio — only for businesses *actually* growing (Fast Growers); applying to cyclicals or stalwarts misprices them.

### Joel Greenblatt — Gotham Capital (~40% CAGR over ~20 years, audited)
- Systematic, rules-based discipline beats discretionary cleverness for almost everyone — repeatable, documented process compounds; one-off brilliance doesn't.
- Never rank quality and cheapness separately — combine Return on Capital (quality) with Earnings Yield (price) into one view of "good business at a good price."
- Use capital-structure-neutral metrics (EBIT / Enterprise Value) so businesses with different debt loads compare fairly.
- Publish the method and results, warts and all — transparency over decades is what makes a record trustworthy.

### Howard Marks — Oaktree Capital
- "Second-level thinking": don't just ask "is this a good company" — ask "does the consensus already know this, and is it already in the price?"
- Cycle-awareness: markets swing between greed and fear; how much risk you should take changes with where you sit in that cycle — not a constant.
- Risk *control*, not risk *avoidance* — goal is to be paid appropriately for risk you're taking now, not eliminate risk altogether.
- Be suspicious of mechanical mean-reversion: historical average only useful anchor if underlying business and regime haven't *structurally* changed. "What's different this time?" usually right question, not an excuse.

## Quick alignment check — run before adopting or changing any rule

1. **Price-action test** — does rule use chart pattern, moving average, or price level as *decision trigger* (not just data input)? → If yes, Buffett/Munger/Graham would reject it outright, and this framework's own Rule 0 ("never act on price movement alone," [CLAUDE.md](../CLAUDE.md)) already forbids it. *(Exactly what closed out old Upgrade 6 — see 2026-06-07 decision log.)*
2. **Turnover test** — does rule increase trading frequency without *fundamental* change (margin, moat, ROIC, growth thesis)? → Munger's "croupier's take" and Lynch's "don't water the weeds" both argue for caution here.
3. **Mean-reversion test** — does rule assume historical average/multiple is still right anchor? → Check whether business structurally improved (Marks' "what's different this time"); if so, purely backward-looking comparison will misfire. *(This is the guardrail just added to Upgrade 2.)*
4. **Macro-veto test** — does rule let macro or rate view *override*, rather than just *inform*, an otherwise-strong bottom-up case? → Buffett treats rates as gravity (an input); Lynch ("thirteen minutes a year on the economy") and Munger would flag anything letting macro *veto* a great business outright. *(This is what converted Rate Environment Gate's Step 1 from hard block to modifier.)*
5. **Concentration test** — does rule push toward diversification "for safety" beyond what quality gate (Phase 01) already earns? → Munger and Buffett's own portfolios argue the opposite: fewer, better names, sized larger, is usually the more disciplined choice — provided the upstream quality screen is doing real work.
6. **Guidance test** — does rule treat a company's own forward guidance as a hard, scoreable input rather than a qualitative signal to verify independently? → Guidance is unaudited and a number management has both means and incentive to manage — exactly the kind of self-reported, gameable input the Valeant/Wirecard gap-fixes (the FCF/Net Income conversion check) were built to guard against in reported financials. Buffett/Dimon's 2018 call to end quarterly guidance and Greenblatt's audited-inputs-only Magic Formula both argue against baking it into the quantitative score. *(This is why guidance changes are a re-valuation trigger — Rule 9 in fair-value-methodology.md — and a Phase 04 qualitative monitoring check, never a weighted sub-score — see valuation-scoring.md.)*

**Conscious divergence on record — the Upside/Downside Modifier (added 2026-06-20).** This modifier folds expected forward return (from the analyst's scenario-weighted DCF) into the valuation score, partially relaxing the "audited/observable inputs only" discipline behind the Guidance test. A *deliberate, bounded* tradeoff — recorded here as such (like the 15% position cap), not an unflagged inconsistency — because it resolves a genuine contradiction: the framework quotes Buffett's "wonderful business at a *fair* price" yet its entry gate demanded *cheap*, so the best compounders were systematically excluded. The forecast discretion is fenced (±15 cap, scenario-weighted not management-guided, catalyst required, fully shown) so it informs rather than dominates. See [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md).

---

## Honorable mentions (not in core five, but worth knowing)

- **Benjamin Graham** — Buffett's teacher; originated "margin of safety" and "Mr. Market" allegory underlying Phase 06's "price dropped ≠ sell."
- **Terry Smith (Fundsmith)** — "Buy good companies, don't overpay, do nothing." ~3–4% annual portfolio turnover; a live, modern proof Munger's "sit on your ass" can still beat the market today.
- **Seth Klarman (Baupost)** — *Margin of Safety*: underwrite every position downside-first — "what do I lose if I'm wrong" before "what do I gain if I'm right."

---

This file is a living reference — whenever framework changes (per [strategy.md](strategy.md)'s Hybrid Upgrades or otherwise), revisit this checklist and update both files together so they don't drift apart.
