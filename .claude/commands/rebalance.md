---
description: Run a portfolio-wide rebalance / trim review across current holdings
---

Run a `REBALANCE` session per the [operating brief](../../framework/operating-brief.md).

Steps:
1. Pull current holdings and weights from [holdings.md](../../portfolio/holdings.md) — if it looks stale, suggest running a [portfolio sync](../../portfolio/sync-sop.md) first.
2. For any holding whose last score is stale (no review since its most recent earnings — see [operating-calendar.md](../../framework/operating-calendar.md)), flag it as needing `/rescore` before it can be reliably rebalanced.
3. For holdings with current scores, apply Phase 05 dynamic trimming and Phase 06 exit triggers from [strategy.md](../../framework/strategy.md):
   - Score 50.0–69.9 → hold, watch only — no trim (raised from a trim trigger 2026-06-07; fair value alone is not a sell signal)
   - Score 70.0–79.9 → trim 25–30%, recycle into Score 0.0–29.9 names
   - Score 80.0–89.9 → trim to 50%
   - Score 90.0–99.9 → trim to 1–2% tracking
   - Score 90.0–99.9 sustained 2+ quarters → full exit review
4. Check the 15% single-position hard cap (Upgrade 7) across the whole book.
5. Propose a recycling plan: where trimmed capital should go (current Score 0.0–29.9 names only), and the resulting target weights.
6. Show full reasoning per position — no black-box recommendations.

Save as `sessions/YYYY-MM-DD-rebalance.md`. Log any executed trims/exits in `decisions/`.
