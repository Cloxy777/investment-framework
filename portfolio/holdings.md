# Current Holdings

> Source of truth for what's actually owned. Update after every [portfolio sync](sync-sop.md) or trade. Each entry should carry the last valuation score and review date so [/rescore](../.claude/commands/rescore.md) knows what's due.

> **2026-10-12 — account segregation (synced).** The framework now governs only IBKR account **U19421206** ([accounts.md](accounts.md)). **RGL, LM8 and TLT were transferred out in-kind** to the non-framework accounts — not sales or exits — and their rows are removed below. **Weights are now `position value ÷ U19421206 Net Liquidation Value`** ($48,635.06), not a blended IBKR+Freedom24 total. Statistics baseline: 2026-10-12.

**As of 2026-11-08 — live sync from [IBKR](snapshots/ibkr.md) account U19421206 (positions, cash balances, and active orders all refreshed 2026-11-08).** [Freedom Finance](snapshots/freedom-finance.md) is **not** part of the framework account and was not resynced (last snapshot 2026-08-22) — see the Freedom24 note below.

Framework account Net Liquidation Value = **$46,477.10** (IBKR U19421206, broker-reported BASE). Weight % = each row's USD-equivalent value ÷ this figure. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.**not** a broker-labeled "Net Asset Valuation", see prior flag in [freedom-finance.md](snapshots/freedom-finance.md)). Weight % = each row's combined USD-equivalent value ÷ this total. *Score and review-date columns are intentionally blank/unchanged — they're populated by [/rescore](../.claude/commands/rescore.md), not by sync.*

> ## 2026-11-08 sync — NVDA doubled (19→40 sh), MSFT trimmed (17→13), TSM opened, USD cash now -$850.77
>
> **NVDA +21 sh** (avg $182.89; now 15.49%) and **MSFT -4 sh** (now 14.82%, down from 19.25%); **new TSM 1 sh @ $364.50**; **new short UUUU Jan15'27 $9 call ×3** against the 300 shares. **USD cash +$981.49 → -$850.77** (margin debit); total IBKR cash $1,992.38 (4.29%). NLV $46,102.05 → **$46,477.10**. **Orders:** new SELL 10 NVDA @ 200.50, BUY 2 SNDK @ 780, BUY 1 SNDK @ 800; NOW short-put order gone unfilled. Confirm the NVDA/MSFT share changes against `decisions/` (see [2026-11-02 rebalance](../sessions/2026-11-02-rebalance.md), [NVDA rescore](../sessions/2026-11-05-rescore-nvda.md)). See [ibkr.md](snapshots/ibkr.md), [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## 2026-11-01 sync — SOFI put expired, NLV -3.4% on price moves, order book reshuffled
>
> **SOFI Oct30'26 $13 short put** expired 2026-10-30 (no shares assigned) — row struck. Net Liquidation $47,714.19 → **$46,102.05**; share counts otherwise unchanged (24 positions). Biggest price moves: **NOW $158.96 → $106.00**, ADBE $263.82 → $250.23, DUOL $143.04 → $131.59 (verify NOW in TWS). **Orders:** new BUY 1 AMZN @ 216 and SELL 1 NOW Feb19'27 $85 put @ 5.00 (both undocumented); UUUU SELL 300 @ 8.99, MA, NOW-buy and V buy orders are gone without fills; NVDA BUY order `REPLACED` with no live successor; NKE still has no live sell. IBKR cash $3,841.98 (8.33%). MSFT 19.25% of NLV. See [ibkr.md](snapshots/ibkr.md), [ibkr-orders.md](snapshots/ibkr-orders.md).
>
> ## 2026-10-25 sync — CSGP sold (25 sh), USD cash positive again, new UUUU exit order
>
> **CSGP:** the standing SELL 25 @ $35.55 GTC (placed 2026-09-30) filled 2026-10-22 (realized +$11.73; proceeds $888.75) — position closed, row struck through; watchlist entry moved to `not-in-portfolio/`. **Cash:** an Oct-19 EUR→USD conversion (€1,783 ≈ $2,000) plus the CSGP proceeds took USD cash from -$1,904.32 to **+$981.49**; total IBKR cash **$3,852.63 (8.07%)**. **New order:** SELL 300 UUUU @ $8.99 GTC (placed 2026-10-19; position now 4.73%, price $7.52) — undocumented in sessions/decisions. Net Liquidation $47,820.23 → **$47,714.19**; all other share counts unchanged. MSFT 18.69% of NLV. NKE still has no live sell order. See [ibkr.md](snapshots/ibkr.md), [ibkr-orders.md](snapshots/ibkr-orders.md).
>
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
| **ADBE** | 10.29% | 0.0 | 83.3 | 8.4 | 11 Sep 2026 | IBKR |
| AMZN | 6.69% | 82.7 | 56.7 | 63.0 | 01 Aug 2026 | IBKR (Freedom24 leg sold — see note above) |
| AVGO | 3.81% | 67.1 | 83.1 | 42.0 | 24 Oct 2026 | IBKR |
| **BKNG** | 3.55% | 20.8 | 91.9 | 14.4 | 11 Oct 2026 | IBKR |
| CASH (Freedom24) | n/a — outside framework account | | | | | Freedom24 |
| CASH (IBKR) | 4.29% | | | | | IBKR |
| ~~CSGP~~ | n/a — fully sold 2026-10-22 (25 sh @ $35.55, standing GTC order), position closed | n/a | | | 11 Oct 2026 | IBKR |
| **DOCS (short put)** | n/a — expired worthless 2026-08-21, position closed | n/a | | | n/a | IBKR |
| DUOL | 10.35% | 85.1 | 83.2 | 51.0 | 01 Sep 2026 | IBKR + Freedom24 |
| GOOG | 0.61% | 39.7 | 70.7 (gate fail + SBC≥FCF hard DQ) | 34.5 (ref only, gate fail) | 12 Nov 2026 | IBKR |
| **BULL (Feb19'27 $5 put, short 2)** | -0.30% | not scored — ungoverned option position, no evaluation ever run | | | n/a | IBKR |
| **MBGL** | 0.04% | not scored — fails quality gates | 51.0 | | 09 Aug 2026 | IBKR |
| META | 6.57% | 39.4 | 87.5 | 26.0 | 26 Aug 2026 (PM) | IBKR (Freedom24 leg sold — see note above) |
| MSFT | 14.82% | 38.9 | 79.9 | 29.5 (ref only, gate fail) | 30 Jul 2026 | IBKR (Freedom24 leg sold — see note above) |
| NFLX | 1.64% | 41.3 | 69.0 (gate fail) | n/a (gate fail) | 02 Nov 2026 | IBKR |
| NKE | 1.66% | 68.7 | 35.4 | 66.7 (ref only, gate fail) | 13 Nov 2026 | IBKR |
| NOW | 1.98% | 78.4 | 71.3 (gate fail) | n/a (gate fail) | 02 Nov 2026 | IBKR |
| NVDA | 15.49% | 25.8 | 89.7 | 18.0 | 12 Nov 2026 | IBKR |
| NVO | 0.43% | 51.4 | 67.2 | 42.1 (ref only, gate fail) | 09 Aug 2026 | IBKR |
| RBRK | 0.68% | not scored — fails quality gates | | | 11 Oct 2026 | IBKR |
| ~~SOFI (Oct30'26 $13 put)~~ | n/a — expired 2026-10-30, position closed | n/a | | | n/a | IBKR |
| SPGI | 1.01% | 31.3 | 67.7 | 31.8 | 09 Aug 2026 | IBKR |
| TLT (Freedom24 leg only) | n/a — outside framework account | not scored — non-equity, framework gap | | | Jun 2026 | Freedom24 |
| TRN | 3.38% | 10.0 | 66.4 | 21.8 (ref only, gate fail) | 10 Sep 2026 | IBKR |
| TSM | 0.81% | not scored — see [2026-11-05 evaluation](../sessions/2026-11-05-new-position-tsm.md) | | | 05 Nov 2026 | IBKR |
| UBER | 0.44% | 37.4 | 59.3 | 39.1 (ref only, gate fail) | 15 Sep 2026 | IBKR |
| **UUUU** | 4.07% (300 sh + short Jan'27 $9 call ×3 marked -$105) | not scored as held — prior [2026-09-10 evaluation](../sessions/2026-09-10-new-position-uuuu.md) pre-dates the position | | | 10 Sep 2026 | IBKR |
| V | 0.91% | 54.5 | 85.6 | 34.5 | 29 Jul 2026 | IBKR |
| VEEV | 1.96% | 65.9 | 86.0 | 40.0 | 30 Aug 2026 | IBKR |
| XEON | 3.61% | not scored — cash-equivalent, out of scope | | | Jun 2026 | IBKR |
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



**`CASH (IBKR)`** = **$1,992.38** (2026-11-08; USD **-$850.77** margin debit, EUR €1,964.38 ≈ $2,189.0, AUD A$951.35 ≈ $653.2; weight 4.29%). *Prior figure:* $3,841.98 (2026-11-01).

**`CASH (Freedom24)`** = $44.98 (last snapshot 2026-08-22; **outside the framework account — no weight computed**).

**Freedom24 is outside the framework account (open question):** per [accounts.md](accounts.md) the framework governs only IBKR U19421206, so this sync computes weights on that account's Net Liquidation Value only and does not blend in Freedom24. Freedom24 (last snapshot 2026-08-22) still holds **TLT ~$9,679.54** and a **DUOL leg ~$1,165.44**, plus $44.98 cash — the DUOL weight above counts the IBKR leg only. Tell me whether to keep these rows (as-is, unweighted), move Freedom24 into the out-of-scope set too, or fold it back into the denominator. AMZN, META and MSFT are IBKR-only (Freedom24 legs sold 2026-08-22); all other equity tickers are IBKR-only.

**AVGO has a prior, untracked history on this account:** `get_account_trades` shows a 1-share AVGO position sold on 2026-05-26 (predating this framework's records). The 6-share position now held is a fresh, separate buy from 2026-06-16 — see the override flag in [override-log.md](override-log.md).

*Run `/sync-portfolio` (see [sync-sop.md](sync-sop.md)) to refresh weights/cash/brokers from the live [snapshots](snapshots/); run `/rescore` to populate score and review-date columns (VEEV scored 2026-07-01 — see [session](../sessions/2026-07-01-rescore-veev.md); AVGO rescored 2026-10-24, current — see [session](../sessions/2026-10-24-rescore-avgo.md)).*
