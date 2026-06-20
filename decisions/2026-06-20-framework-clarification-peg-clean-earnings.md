# 2026-06-20 — Framework clarification: PEG Fast-Grower eligibility requires a clean, non-distorted earnings base

**What prompted it:**

DUOL (Duolingo) was scored two different ways across two sessions, exposing an ambiguity in the PEG sub-score (Upgrade 3) eligibility rule:

- **2026-06-12 session:** judged DUOL **not a confirmed Fast Grower** — its GAAP EPS series is distorted by a one-off $256.7M FY2025 deferred-tax-valuation-allowance release, and forward consensus EPS was actually declining — so it **redistributed PEG's 15% weight to EV/EBIT**.
- **2026-06-20 rescore (under the new Upside/Downside Modifier):** applied **PEG live** as a Fast Grower (PEG 1.58 via a revenue-CAGR proxy → sub-score 53.82).

Both landed in the same HOLD band, but the framework should produce one answer, not two.

**The ruling:**

The existing PEG gate — *"Fast Growers only — EPS growth >15% for 3+ years"* — is clarified: **the "3+ years" must be a reliable, non-distorted earnings base.** A genuinely fast-growing business that lacks 3+ years of clean EPS — a recent IPO, a company only recently turned GAAP-profitable, or one whose trailing EPS is distorted by a one-off item (e.g. a deferred-tax release) — does **not** yet qualify for a live PEG sub-score. In that case **redistribute PEG's 15% weight to EV/EBIT** (the standard non-Fast-Grower treatment) rather than forcing a PEG off an unreliable base. A revenue-CAGR-proxy PEG may still be computed as a *sensitivity check*, but it is not the scored input.

This formalizes the more conservative 2026-06-12 treatment as the standing rule; the 2026-06-20 live-PEG application was the deviation.

**Alignment check ([investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)):**
- **Lynch:** PEG is "only for businesses that are *actually* growing" with real, measurable earnings — applying it to a company without a reliable multi-year earnings base misprices it, the same way applying it to a cyclical or stalwart does.
- **Greenblatt:** the score should run on reliable, audited inputs; a PEG built on distorted or sub-3-year EPS is exactly the kind of shaky input to keep out of the weighted score.
- **"Never invent or estimate financial data"** (CLAUDE.md): forcing a PEG off a proxy when the real earnings base doesn't support one is a form of estimation. Redistribution is the honest treatment.

No tension with the other checklist items (no price-action trigger, no turnover change, no macro veto, no concentration effect).

**Impact — DUOL re-scored under the ruling (2026-06-20 fresh-price inputs):**

Redistribute PEG's 15% to EV/EBIT (→ 40% weight):
```
FCF yield 6.93%   → 30.74 × 0.40 = 12.30
EV/EBIT 29.08×    → 74.24 × 0.40 = 29.70
Forward PE        → 50.00 × 0.20 = 10.00   (no-history fallback)
Raw weighted                      = 51.99
+ Rate Regime Modifier            + 10.0
+ Upside/Downside Modifier        −  8.25   (unchanged — independent of sub-scores)
FINAL                             = 53.7
```
DUOL **50.7 → 53.7**. Still HOLD (Fair Value band, 50.0–69.9) — action unchanged. holdings.md, the DUOL session log, and the DUOL watchlist entry corrected to 53.7.

**Files touched:**
- `framework/valuation-scoring.md` — PEG section: added the clean-earnings clarification + redistribution instruction.
- `framework/strategy.md` — Upgrade 3: added the clarification note.
- `framework/operating-brief.md` — Upgrade 3 line: added the clarification.
- `portfolio/holdings.md` — DUOL score 50.7 → 53.7.
- `sessions/2026-06-20-rescore-duol.md` + `watchlist/in-portfolio/DUOL/DUOL-2026-06-20.md` — correction note appended.
- `decisions/` — this file.
