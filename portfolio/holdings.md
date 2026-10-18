# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

> **2026-10-12 — account segregation (synced).** The framework now governs only IBKR account **U19421206** ([accounts.md](accounts.md)). **RGL, LM8 and TLT were transferred out in-kind** to the non-framework accounts — not sales or exits — and their rows are removed below. **Weights are now `position value ÷ U19421206 Net Liquidation Value`** ($48,635.06), not a blended IBKR+Freedom24 total. Statistics baseline: 2026-10-12.

**As of 2026-10-18 — live sync from [IBKR](snapshots/ibkr.md) account U19421206 (positions, cash balances, and active orders all refreshed 2026-10-18).** [Freedom Finance](snapshots/freedom-finance.md) is **not** part of the framework account and was not resynced (last snapshot 2026-08-22) — see the Freedom24 note below.

Framework account Net Liquidation Value = **$47,820.23** (IBKR U19421206, broker-reported BASE). Weight % = each row's USD-equivalent value ÷ this figure. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.**not** a broker-labeled "Net Asset Valuation", see prior flag in [freedom-finance.md](snapshots/freedom-finance.md)). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## 2026-10-18 sync — UUUU assigned (300 sh), new SOFI short put, USD cash now negative
>
> **UUUU:** the 3 short Oct-16 $8.50 puts expired in the money and the account now holds **300 UUUU @ $8.478 ($2,541, 5.31%)** — consistent with assignment (~$2,550 outlay); USD cash fell from $602 to **-$1,904.32** (margin debit) while €3,748 and A$952 sit idle. UUUU has an evaluation on file from 2026-09-10 but no decision to hold it as a position. **SOFI Oct30'26 $13 PUT, short 1** is a new ungoverned option position. **AVGO:** the BUY 5 @ 265.34 order was split into BUY 1 @ 266 + BUY 1 @ 243. Net Liquidation $48,635.06 → **$47,820.23**; every other share count unchanged. MSFT is 18.90% of NLV. See [ibkr.md](snapshots/ibkr.md), [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## 2026-10-12 sync — account segregation: 27 → 24 positions, weights re-based
>
> **RGL, LM8, TLT left the framework account by in-kind transfer** (not sales — see [accounts.md](accounts.md#known-transfers-out-of-the-framework-account)); scope guard passed (none appear in the live response). Net Liquidation $57,251.48 → **$48,635.06**, so every remaining weight rose (e.g. MSFT 13.36% → **18.77%**, above the 15% cap-headroom figure quoted below — now on a smaller base; review at next `/rebalance`). IBKR cash is unchanged in substance ($5,465.45 = 11.24%). Order set unchanged (8 working, NKE `REPLACED`). **Open question for you:** the Freedom24 account still holds TLT (~$9,680) and a DUOL leg (~$1,165) — outside the framework account; see the note near the bottom.
>
> ## 2026-10-11 sync (re-confirmed by Weekly Monday run) — two new positions (LM8, BULL short put), cash up $5.3k
>
> **New positions, both ungoverned (no session/decision/override entry):** **LM8** (1,800 sh, ASX, A$612 ≈ $427, 0.63%) — the BUY 1800 @ A$0.30 order flagged last sync as "verify intent" has filled; **BULL Feb19'27 $5 PUT, short 2 contracts** (mark -$71.29, -0.10%; a short put has assignment risk of up to $1,000 notional). **IBKR cash $117 → $5,465** (new EUR €3,748 and AUD A$952 balances) and Net Liquidation $50,411.80 → $57,211.16: not explained by any order or session — confirm whether a deposit/FX conversion. **New UUUU SELL 3 × Oct-16 $8.50 Put @ 0.03 GTC order** (no UUUU holding or evaluation; ~$2,550 notional if assigned). **NKE still has only a `REPLACED` order (no live sell).** Otherwise same 25 tickers/share counts as 2026-10-04; weights moved with the larger denominator and prices. MSFT 13.36% (cap headroom ≈ $1,120 of the 15% = $10,215), TLT 25.66%. All older flags below (ADBE/BKNG undocumented trades, RBRK/ZS overdue rescores, SPOT absent, TLT short call absent, MA/NOW/V orders) carry forward unresolved; their wording below is from 2026-09-27. See [ibkr.md](snapshots/ibkr.md), [ibkr-orders.md](snapshots/ibkr-orders.md).

> ## 🚨 URGENT — two undocumented trades this week: ADBE add (10 → 20 shares) and BKNG fill (new 10-share position)
>
> **ADBE:** position doubled with no matching order ever tracked in [ibkr-orders.md](snapshots/ibkr-orders.md) and no `sessions/`/`decisions/` entry. Implied purchase price ~$240.10/share for the added 10 shares.
>
> **BKNG:** the order flagged as undocumented for five consecutive syncs (483688084, BUY 10 @ $159.00 GTC) has filled. A fresh [2026-10-11 rescore](../sessions/2026-10-11-rescore-bkng.md) (Quality 91.9 / Valuation 20.8 / Composite 14.4) concludes **HOLD — keep the existing shares, do not add more** (the mandatory 2:1 R/R gate still fails at every authorized MoS/stop combination, best case 1.25:1 — same structural block as the original 2026-08-05 "WATCHLIST ONLY" conclusion, now applied to an actual holding instead of a prospective entry). **This rescore does not resolve why the fill happened without an order/decision on file** — that documentation gap remains open in override-log.md.
>
> Both logged in [override-log.md](override-log.md) this sync. **Flagged as urgent for the user: confirm both trades in TWS/Client Portal and either document the rationale (Rule 10) or treat as errors to unwind.** Full detail: [ibkr.md](snapshots/ibkr.md).
>
> ## ✅ AVGO's previously-flagged urgent order appears resolved
>
> The AVGO BUY 5 @ $310.60 GTC order (87937891) no longer appears in this sync's order fetch, and the AVGO position is unchanged — consistent with a manual cancellation. See [ibkr.md](snapshots/ibkr.md) for the caveat on this sync's order-fetch coverage.
>
> ## ✅ RBRK and ZS Rule 9 rescores done 2026-10-11 (issues [#801](https://github.com/Cloxy777/investment-framework/issues/801), [#802](https://github.com/Cloxy777/investment-framework/issues/802))
>
> The 2026-09-14 +15–16% moves were a sector-wide cybersecurity rally, not company news. **RBRK:** still fails the FCF-positive hard disqualifier (best-case Quality ≤65.0), still not scored — [session](../sessions/2026-10-11-rescore-rbrk.md). **ZS:** Valuation 47.9 → **65.7** (price +37.7%, 10Y now 5.24% → Rate Modifier +15), Quality 59.4 (fails gate), Composite 53.2 (ref only) — HOLD, in the 50–69.9 hold band; no `override-log.md` entry for either still outstanding — [session](../sessions/2026-10-11-rescore-zs.md).
>
> ## ⚠️ TRN BUY 900 @ £1.756 GTC — status changed to `PENDING_CANCEL`, not yet confirmed complete
>
> Order 1528612089 now shows `PENDING_CANCEL` (as of 2026-09-26) rather than `NEW` — a cancel appears to be in flight for the order that has contradicted TRN's HOLD/no-top-up rescore since 2026-09-11. Not yet confirmed resolved. See [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## Five previously-flagged, still-undocumented orders (GOOG, MA, NKE, NOW, V) remain open, unchanged
>
> See [ibkr-orders.md](snapshots/ibkr-orders.md) for the full carried-forward table. **The TLT short call order (1040104046) remains absent from the orders fetch, in any status, for a fourth consecutive sync** — still worth a manual TWS check.
>
> ## SPOT position and its sell order remain absent — now 10 consecutive syncs, still unresolved since 2026-08-02
>
> No new information this sync; still flagged for the user to confirm directly in TWS/Client Portal. Full detail in [ibkr.md](snapshots/ibkr.md) and [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## Cash swung sharply this sync (-$3,994.33 over 7 days), reconciled by this week's two undocumented trades
>
> IBKR USD-equiv cash: $4,097.84 → $103.51. The ADBE add (~$2,401 outlay) and BKNG fill (~$1,591 outlay) combined (~$3,992) reconcile essentially all of the swing — not unexplained drift, but a direct consequence of the two flagged trades above. **The still-unresolved +$2,523.36 cash jump flagged 2026-08-09** remains open and uninvestigated.
>
> **This sync's `get_account_orders` fetch returned notably fewer records than usual (7 vs. 13 last sync)** — several previously-tracked order IDs are absent in any status, not just excluded as inactive. See the coverage note in [ibkr.md](snapshots/ibkr.md).
>
> **AVGO's 2026-06-16 override is still marked "Open — under review" in [override-log.md](override-log.md)** despite having been resolved via the 2026-07-04 full rescore — carried forward as an open housekeeping item, not corrected this pass (outside `/sync-portfolio`'s scope).

**Score scale (2026-06-11):** Valuation scores run **0.0–100.0** (continuous, 0 = cheapest, 100.0 = most expensive) instead of the old 1–10 integers — see [valuation-scoring.md](../framework/valuation-scoring.md) and [decisions/2026-06-11-framework-change-score-precision-rescale.md](../decisions/2026-06-11-framework-change-score-precision-rescale.md).

**Quality Score / Composite Score columns added 2026-06-29** (see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md)) — every row that carries a numeric Last Score predates this change and does not yet have a Quality Score computed, so both new columns are marked **`?`** (never invented/backfilled) until that ticker's next `/rescore` pass fills them in. Rows already "not scored" (cash, non-equity, quality-gate fail, overrides) are left blank — there is nothing for the new columns to invalidate.

| Ticker | Weight % | Last Score | Quality Score | Composite Score | Last Review | Broker |
|--------|----------|------------|----------------|------------------|-------------|--------|
| **ADBE** | 10.26%🚨 | 0.0 | 83.3 | 8.4 | 11 Sep 2026 | IBKR |
| AMZN | 6.32% | 82.7 | 56.7 | 63.0 | 01 Aug 2026 | IBKR (Freedom24 leg sold — see note above) |
| AVGO | 4.17% | 71.4 | 86.3 | 42.6 | 12 Oct 2026 | IBKR |
| **BKNG** | 3.42%🚨 | 20.8 | 91.9 | 14.4 | 11 Oct 2026 | IBKR |
| CASH (Freedom24) | n/a — outside framework account | | | | | Freedom24 |
| CASH (IBKR) | 6.19% | | | | | IBKR |
| CSGP | 1.69% | 87.8 | 69.2 | 59.3 | 11 Oct 2026 | IBKR |
| **DOCS (short put)** | n/a — expired worthless 2026-08-21, position closed | n/a | | | n/a | IBKR |
| DUOL | 8.89% | 85.1 | 83.2 | 51.0 | 01 Sep 2026 | IBKR + Freedom24 |
| GOOG | 0.71% | 64.2 | 71.4 | 46.4 | 22 Jul 2026 | IBKR |
| **BULL (Feb19'27 $5 put, short 2)** | -0.17% | not scored — ungoverned option position, no evaluation ever run | | | n/a | IBKR |
| **MBGL** | 0.04% | not scored — fails quality gates | 51.0 | | 09 Aug 2026 | IBKR |
| META | 7.42% | 39.4 | 87.5 | 26.0 | 26 Aug 2026 (PM) | IBKR (Freedom24 leg sold — see note above) |
| MSFT | 18.90% | 38.9 | 79.9 | 29.5 (ref only, gate fail) | 30 Jul 2026 | IBKR (Freedom24 leg sold — see note above) |
| NFLX | 1.79% | 49.3 | 69.8 | 39.8 | 17 Jul 2026 | IBKR |
| NKE | 1.55% | 55.2 | 39.1 | 58.1 (ref only, gate fail) | 11 Oct 2026 | IBKR |
| NOW | 2.66%⚠️ | 75.9 | 73.2 | 51.4 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| NVDA | 8.54% | 36.2 | 90.3 | 23.0 | 17 Sep 2026 | IBKR |
| NVO | 0.41% | 51.4 | 67.2 | 42.1 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| RBRK | 0.71% | not scored — fails quality gates | | | 11 Oct 2026 | IBKR |
| **SOFI (Oct30'26 $13 put, short 1)** | -0.05% (new) | not scored — ungoverned option position, no evaluation ever run | | | n/a | IBKR |
| SPGI | 0.90% | 31.3 | 67.7 | 31.8 | 09 Aug 2026 | IBKR |
| TLT (Freedom24 leg only) | n/a — outside framework account | not scored — non-equity, framework gap | | | Jun 2026 | Freedom24 |
| TRN | 3.64%⚠️ | 10.0 | 66.4 | 21.8 (ref only, gate fail) | 10 Sep 2026 | IBKR |
| UBER | 0.44% | 37.4 | 59.3 | 39.1 (ref only, gate fail) | 15 Sep 2026 | IBKR |
| **UUUU** | 5.31% (new — assigned short puts) | not scored as held — prior [2026-09-10 evaluation](../sessions/2026-09-10-new-position-uuuu.md) pre-dates the position | | | 10 Sep 2026 | IBKR |
| V | 0.84% | 54.5 | 85.6 | 34.5 | 29 Jul 2026 | IBKR |
| VEEV | 1.95% | 65.9 | 86.0 | 40.0 | 30 Aug 2026 | IBKR |
| XEON | 3.53% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
| ZS | 0.43% | 65.7 | 59.4 | 53.2 (ref only, gate fail) | 11 Oct 2026 | IBKR |

**🚨 RBRK and ZS weights above are pre-Rule-9-rescore** — see the flag at the top of this file; both are overdue for `/rescore` per [#801](https://github.com/Cloxy777/investment-framework/issues/801) and [#802](https://github.com/Cloxy777/investment-framework/issues/802).

**🚨 ADBE and BKNG rows above carry the undocumented trades flagged at the top of this file** — ADBE's Last Score/Quality Score/Composite Score predate this week's undocumented share add (no rescore has run since); BKNG's figures are now current (rescored 2026-10-11, HOLD — see session), but the fill itself remains undocumented in override-log.md/decisions/.

**STIM (previously 2.47%) removed prior sync** — position fully exited via forced option assignment; unchanged this round. Moved to `watchlist/not-in-portfolio/STIM/`.

**SPOT (previously 0.83%) remains absent from this table** — its 1-share position has now been missing for ten consecutive syncs (2026-08-02 through 2026-09-27), undocumented; see the flag above and [ibkr.md](snapshots/ibkr.md).

**MSFT's weight (14.24%) is now IBKR-only** — the 2-share Freedom24 leg was sold (confirmed, see flag above). Composite Score for MSFT remains a reference figure only (not adopted) — its Quality Score (79.9) fails the 80.0+ gate by 0.1 point.

**NOW's weight (⚠️) still carries the 2026-08-10 undocumented 3-share trim** — unresolved, see [override-log.md](override-log.md).

**TRN's weight (⚠️) still reflects the 22.4% price drop from the 08-16→08-22 window** — caused by a CMA "drip pricing" investigation opened 2026-08-19, still open with no finding as of the [2026-09-10 rescore](../sessions/2026-09-10-rescore-trn.md). **HOLD, no top-up** — Quality Gate already blocked adding before this news; the CMA probe adds a second, independent reason. New CEO Ian Brown started 7 Sept 2026 (full handover 28 Sept). FY2026 FCF fell −17.0% YoY (£79.5M vs £95.9M FY2025) — flagged, not yet explained by disclosed management commentary.

**XEON is EUR-denominated** (€1,504.75 market value). USD-equivalent (**$1,685.57**) uses the live EUR→USD rate (1.1201705) from `get_account_balances`.

**TRN is GBP-denominated** (£1,246.80 market value, LSE — 600 shares). USD-equivalent (**$1,651.38**) uses the live GBP→USD rate (1.3244739) from `get_account_balances`.



**`CASH (IBKR)`** = **$2,961.09** (2026-10-18; USD -$1,904.32, EUR €3,747.94 ≈ $4,202.57, AUD A$951.80 ≈ $662.83; weight 6.19%). *Prior figure:* $5,465.45 broker-reported BASE USD-equivalent ($602.23 USD + €3,747.94 EUR ≈ $4,198.26 + A$951.80 AUD ≈ $664.27; full breakdown in the [IBKR snapshot](snapshots/ibkr.md)) = 11.24% of Net Liquidation. The EUR/AUD balances' origin remains unexplained, see the 2026-10-11 flag.

**`CASH (Freedom24)`** = $44.98 (last snapshot 2026-08-22; **outside the framework account — no weight computed**).

**Freedom24 is outside the framework account (open question):** per [accounts.md](accounts.md) the framework governs only IBKR U19421206, so this sync computes weights on that account's Net Liquidation Value only and does not blend in Freedom24. Freedom24 (last snapshot 2026-08-22) still holds **TLT ~$9,679.54** and a **DUOL leg ~$1,165.44**, plus $44.98 cash — the DUOL weight above counts the IBKR leg only. Tell me whether to keep these rows (as-is, unweighted), move Freedom24 into the out-of-scope set too, or fold it back into the denominator. AMZN, META and MSFT are IBKR-only (Freedom24 legs sold 2026-08-22); all other equity tickers are IBKR-only.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records). The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag in [override-log.md](override-log.md).

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-10-12, current — see [session](../sessions/2026-10-12-rescore-avgo.md)).*
