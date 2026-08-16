# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

**As of 2026-08-16 — live sync from [IBKR](snapshots/ibkr.md) (positions, cash balances, and active orders all refreshed 2026-08-16) + [Freedom Finance](snapshots/freedom-finance.md) snapshot (last synced 2026-06-07, unchanged this run), including cash balances on both sides.**

Combined total ≈ **$65,888.42** = IBKR Net Liquidation Value $50,764.88 + Freedom24 Net Asset Valuation $15,123.54 (both broker-reported, **positions + cash**, in USD). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## ✅ MSFT back under the 15% position cap — 14.03% (was 16.42%)
>
> The `SELL 3 MSFT @ $500.00` GTC order flagged last sync (264783699) **filled 2026-08-10 at $503.34**, confirmed via `get_account_trades`. MSFT is now 17 shares (IBKR) + 2 shares (Freedom24, unchanged) = **14.03% combined weight**, back under the 15% cap (Upgrade 7) for the first time since the breach was first flagged. Its Quality Score (79.9, per [sessions/2026-07-30-rescore-msft.md](../sessions/2026-07-30-rescore-msft.md)) still fails the 80.0+ gate by 0.1 point, so its Composite Score (29.5) remains reference-only — the cap resolution doesn't change that. **Still no `sessions/`/`decisions/` entry documents this as an intentional trim** — the governance gap (a manual trade executed outside any `/rebalance` or `/rescore` session) is not closed by the fill itself, only the cap breach is.

> ## ⚠️ New this sync — undocumented NOW trim, 3 shares sold @ $125.00, no session/decision entry
>
> NOW went from 12 to 9 shares (order 1031203808, filled 2026-08-10, realized P&L +$95.59) with no prior flag anywhere — the order was placed and fully filled within this sync's window, so it was never visible as "active" first. No Phase 06 exit trigger or forced-trim signal is on record for NOW (Composite 51.4, reference-only, last reviewed 09 Aug 2026). **Logged as a new entry in [override-log.md](override-log.md)** — flagged for the user to confirm intent. Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).

> ## META back to 5 shares — the 2026-08-02 "undocumented +1" anomaly has reversed itself
>
> The META `SELL 1 @ $611.01` order previously shown as `REPLACED` with no live successor **did fill**, 2026-08-11 at $611.01 (realized P&L +$29.87) — confirmed via `get_account_trades`. This brings META back to 5 shares, undoing the unconfirmed 5→6 move flagged 2026-08-02. Treated as a continuation of the existing open [override-log.md](override-log.md) entry on META's share-count volatility (07-08–07-11 origin), not a new entry — the underlying governance gap (trims executed with no `sessions/`/`decisions/` authorization) is the same issue, not a new one.

> ## Cash swing this sync (+$2,491.88) fully explained by this week's three trade fills — no new anomaly
>
> MSFT + NOW + META sale proceeds ($1,510.02 + $375.00 + $611.01 = $2,496.03) less commissions ($3.05) = +$2,492.98, matching the USD cash-leg change to the cent. **The separate, still-unresolved +$2,523.36 cash jump flagged in the 2026-08-09 sync** (covering the window *before* this week's trades) remains open and uninvestigated — not the same event.

> ## SPOT position and its sell order remain absent — unchanged, still unresolved since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> **No other undocumented position changes this sync** — all 24 other IBKR positions (of 27) matched the 2026-08-09 sync exactly in share count and average cost; only prices moved. The open governance items from prior syncs (TLT's 2026-07-26 undocumented +23-share increase and its still-working undocumented short call, DOCS's unauthorized short put, RGL's still-unevaluated fully-filled position, MBGL) remain open and untouched — see [override-log.md](override-log.md).
>
> This week's [weekly brief](../sessions/weekly-briefs/2026-08-16-weekly-brief.md) has the full summary.

> **AVGO's 2026-06-16 override is still marked "Open — under review" in [override-log.md](override-log.md)** despite having been resolved via the 2026-07-04 full rescore — carried forward as an open housekeeping item, not corrected this pass (outside `/sync-portfolio`'s scope).

> **Weight column sums to ~100.6%, not 100%** — see the "Note on Gross Position Value vs. Net Liquidation" in [ibkr.md](snapshots/ibkr.md) for the live-vs-settled timing gaps, plus the STIM short-call market value (–$403.17) and the DOCS short-put market value (–$0.02), both intentionally excluded from any weight below. Not a calculation error — flagged for transparency rather than silently rescaled.

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Boundary-name rescore (2026-06-20):** the 8 holdings sitting in the 50–63 "Hold/watchlist" band were re-scored with fresh Rule 0 live prices under the new **Upside/Downside Modifier** (see [decisions/2026-06-20-framework-change-upside-downside-modifier.md](../decisions/2026-06-20-framework-change-upside-downside-modifier.md) and the per-ticker `sessions/2026-06-20-rescore-*.md` logs). Seven of the eight dropped a full band into the BUY zone once expected forward return was folded in (MSFT 51.2→35.0, UBER 52.9→34.8, V 54.9→39.2, NOW 59.3→42.3, ZS 61.1→36.3, NVDA 62.2→48.5); DUOL (55.6→50.7) and NFLX (63.2→61.2) stayed in HOLD. **Important:** a BUY-band *score* is not a BUY *order* — every one of the seven is currently blocked from adding by an independent gate (sub-2:1 risk/reward, the 15% position cap, or a Phase 01 quality-gate fail for ZS). No trades were executed; these are score/action-band updates only.

**Full scored-book rescore complete (2026-06-20).** The remaining 9 scored equities were also rescored under the modifier (per-ticker `sessions/2026-06-20-rescore-*.md`): ADBE 5.0→0.0, META 38.5→19.6, SPGI 43.3→33.4, NKE 34.1→43.1, NVO 35.8→47.6, AMZN 79.8→73.4, GOOG 83.7→73.1, CSGP 83.3→79.0, SPOT 82.0→80.5. The four richly-valued names (AMZN, GOOG, CSGP, SPOT) stayed in the trim bands — the modifier correctly did **not** rescue them (their forward return only modestly cleared the hurdle), confirming the bounded asymmetry. **The only currently actionable trade across the whole book is ADBE** (score 0.0): a partial-fill position with R/R 4.47:1 and room to its 6–8% target — top up ~7 shares (~$1,366). All other BUY-band names are gated by R/R, the position cap, or a quality-gate fail. Not rescored under the modifier: TLT, XEON, RBRK, STIM (non-equity / cash-equivalent / fails gates) and VEEV (never scored). **AVGO (new this week) is also not yet rescored under the modifier** — its 69.5 score predates the 2026-06-20 framework change.

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| ADBE | 4.01% | 0.0 | 83.9 | 8.1 | 29 Jul 2026 | IBKR |
| AMZN | 8.89% | 82.7 | 56.7 | 63.0 | 01 Aug 2026 | IBKR + Freedom24 |
| AVGO | 3.58% | 68.2 | 82.1 | 43.1 | 04 Jul 2026 | IBKR |
| CASH (Freedom24) | 0.16% | | | | | Freedom24 |
| CASH (IBKR) | 4.27% | | | | | IBKR |
| CSGP | 1.23% | 84.8 | 69.2 | 57.8 | 09 Aug 2026 | IBKR |
| **DOCS (short put)** | n/a — not an equity position, see note above | not scored — ungoverned position | | | n/a | IBKR |
| DUOL | 7.37% | 72.2 | 83.2 | 44.5 | 06 Aug 2026 | IBKR + Freedom24 |
| GOOG | 0.52% | 64.2 | 71.4 | 46.4 | 22 Jul 2026 | IBKR |
| **MBGL** | 0.03% | not scored — fails quality gates | 51.0 | | 09 Aug 2026 | IBKR |
| META | 5.37% | 41.2 | 87.5 | 26.9 | 05 Aug 2026 | IBKR + Freedom24 |
| MSFT | 14.03% | 38.9 | 79.9 | 29.5 (ref only, gate fail) | 30 Jul 2026 | IBKR + Freedom24 |
| NFLX | 1.43% | 49.3 | 69.8 | 39.8 | 17 Jul 2026 | IBKR |
| NKE | 1.24% | 13.9 | 44.4 | 34.8 | 1 Jul 2026 | IBKR |
| NOW | 1.69%⚠️ | 75.9 | 73.2 | 51.4 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| NVDA | 6.48% | 34.3 | 91.7 | 21.3 | 05 Jul 2026 | IBKR |
| NVO | 0.34% | 51.4 | 67.2 | 42.1 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| RBRK | 0.47% | not scored — fails quality gates | | | Jun 2026 | IBKR |
| **RGL** | 0.64% | not scored — ungoverned position, see note above | | | n/a | IBKR |
| SPGI | 0.64% | 31.3 | 67.7 | 31.8 | 09 Aug 2026 | IBKR |
| STIM | 2.47% | not scored — going-concern override, **EXIT recommended** (see [2026-08-09 exit review](../sessions/2026-08-09-exit-review-stim.md)) | | | 09 Aug 2026 | IBKR |
| TLT | 27.68% | not scored — non-equity, framework gap | | | Jun 2026 | IBKR + Freedom24 |
| TRN | 3.14% | 10.0 | 67.2 | 21.4 | 05 Jul 2026 | IBKR |
| UBER | 0.35% | 43.6 | 55.5 | 44.1 | 07 Aug 2026 | IBKR |
| V | 0.55% | 54.5 | 85.6 | 34.5 | 29 Jul 2026 | IBKR |
| VEEV | 1.11% | 45.1 | 85.7 | 29.7 | 01 Jul 2026 | IBKR |
| XEON | 2.63% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.28% | 43.1 | 59.4 | 41.9 | 05 Jul 2026 | IBKR |

**SPOT (previously 0.83%) remains absent from this table** — its 1-share position has now been missing for three consecutive syncs (2026-08-02, 08-09, 08-16), undocumented; see the flag above and [ibkr.md](snapshots/ibkr.md).

**MSFT's weight is now 14.03%, back under the 15% position cap** — see the resolution flag above. Composite Score for MSFT remains a reference figure only (not adopted) — its Quality Score (79.9) fails the 80.0+ gate by 0.1 point.

**NOW's weight (⚠️) carries an undocumented 3-share trim this sync** — see the flag above and the new [override-log.md](override-log.md) entry.

**XEON is EUR-denominated** (€1,500.40 market value). Its USD-equivalent (**$1,735.29**, used for the weight above) comes from the *live* EUR→USD rate (1.1565539) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**TRN is GBP-denominated** (£1,526.40 market value, LSE — up from £1,522.80 last sync, price +0.2%, share count unchanged at 600). Its USD-equivalent (**$2,066.70**, used for the weight above) comes from the *live* GBP→USD rate (1.3539723) returned by IBKR's `get_account_balances` — broker-reported, not assumed.

**RGL is AUD-denominated** (AUD $600.00 market value, ASX — unchanged from last sync, share count unchanged at 60,000). Its USD-equivalent (**$424.95**, used for the weight above) comes from the *live* AUD→USD rate (0.7082445) returned by IBKR's `get_account_balances` — broker-reported, not assumed. No Phase 01/02 evaluation exists for this ticker.

**STIM's weight above (2.47%) reflects the 500-share equity position only** ($1,625.00). A short 5-contract covered call (`STIM Aug21'26 $2.50 CALL`, market value –$403.17) is also held against this position — see [ibkr.md](snapshots/ibkr.md) for detail. Not folded into the weight % here; STIM's share price has risen sharply since the 2026-08-11 earnings beat (see [issue #522](https://github.com/cloxy777/investment-framework/issues/522), still open/overdue — the short call is now meaningfully in-the-money and its mark-to-market loss has widened to –$375.94 unrealized.

**DOCS's short put (`DOCS Aug21'26 $17.5 PUT`, market value –$0.02) has no equity position to attach a weight to** — see [override-log.md](override-log.md). Tracked in full in [ibkr.md](snapshots/ibkr.md).

**`CASH (IBKR)`** = **$2,813.98** USD-equivalent ($3,024.82 USD + €227.49 EUR ≈ +$263.10 + £0.00 GBP ≈ $0.00 − AUD $668.95 ≈ −$473.78, net of rounding — full per-currency breakdown in the [IBKR snapshot](snapshots/ibkr.md)). Up sharply vs. last sync ($322.10 → $2,813.98, +$2,491.88) — this week's increase is fully explained by the three trade fills above; the earlier, separate +$2,523.36 jump flagged 2026-08-09 remains unresolved.

**`CASH (Freedom24)`** = $106.85 (single-currency, USD — no FX conversion needed; unchanged since the 2026-06-07 Freedom Finance sync, no new screenshot this round). It ties out exactly: $15,016.69 (positions) + $106.85 (cash) = $15,123.54 (Net Asset Valuation) — see the [Freedom Finance snapshot](snapshots/freedom-finance.md) for the cross-check.

**Combined positions across both brokers:** AMZN, DUOL, META, MSFT, and TLT are each held in both IBKR and Freedom Finance — their weights above are the *sum* of both brokers' USD-equivalent market values. All other equity tickers are IBKR-only; both `CASH` rows are naturally broker-specific.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records), which is what the now-superseded "AVGO no longer appears in either broker account" placeholder note (removed in a prior sync) was referring to. The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag in [override-log.md](override-log.md).

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-07-04, current — see [session](../sessions/2026-07-04-rescore-avgo.md)).*
