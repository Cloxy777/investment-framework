# 2026-11-13 — Framework change: position hard cap measured against max(NLV, $100k)

**What changed:** Upgrade 7 (single-position hard cap) is still 15%, but the base is now `max(account Net Liquidation Value, $100,000)`. While NLV < $100k the cap is a flat **$15,000** per position; above $100k it is a plain 15% of NLV.

**Why:** The framework account is ~$46k NLV. A pure 15% cap (~$7k) is too small to hold meaningful conviction positions at this portfolio size. The user kept the 15% rule but wants it computed from $100k when the portfolio is smaller.

**Effect today (NLV ≈ $46.5k):** cap goes from ~$6.97k (15%) to $15,000 (~32% of actual NLV). Note the cap is now much looser in *percentage-of-NLV* terms, so single-name concentration risk is higher until NLV grows; the tighter score-band allocation caps (order-setup table) are unchanged and still size new purchases.

**Files touched:** `framework/strategy.md`, `framework/operating-brief.md`, `framework/glossary.md`, `framework/automation-schedule.md`, `.claude/commands/rebalance.md`.

**Follow-up:** next `/rebalance` should apply the new base (NVDA ~15.5% and MSFT ~14.8% of NLV are now well within $15k; check dollar values).

## Glossary
- **NLV (Net Liquidation Value):** total account value if everything were sold today (positions + cash − debt).
- **Hard cap:** maximum size one position may ever reach, regardless of conviction.
