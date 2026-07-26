# Weekly Portfolio Brief — week of 2026-07-26

**Task type:** Weekly Monday Portfolio Sync & Brief (Routine)
**Date:** 26 Jul 2026

---

## 1. Portfolio Sync Summary

Full IBKR sync (positions + cash balances + active orders) completed for account U19421206. Freedom Finance unchanged (last synced 2026-06-07 — no new screenshot provided this round). See [holdings.md](../../portfolio/holdings.md), [ibkr.md](../../portfolio/snapshots/ibkr.md), and [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md) for full detail.

**Combined portfolio total: $57,832.61** (IBKR Net Liquidation $42,709.07 + Freedom24 NAV $15,123.54), down from $59,142.82 on 2026-07-20 (–$1,310.21). The drop is almost entirely the IBKR side: Net Liquidation fell from $44,019.28 to $42,709.07 (–$1,310.21), which lines up closely with a cash drawdown flagged below, not a broad price decline.

### ⚠️ Not a quiet sync — TLT share count jumped, undocumented, funded from cash

Unlike the last two syncs, this one is **not** clean. `TLT` grew from **77 to 100 shares** (+23) since 2026-07-20, with the blended average cost dropping from $88.79 to $87.6030 (implying the 23 added shares cost roughly ~$83.63 each). This is funded by a matching cash swing: IBKR USD-equivalent cash fell from **–$264.11 to –$2,189.32** (–$1,925.21), almost exactly the implied cost of the new shares. A previously-flagged working order — `TLT BUY 13 @ $83.54` — has vanished from `get_account_orders` entirely (not filled, not `REPLACED`, not `CANCELLED`), the same "vanished order" anomaly seen with the AMZN bracket on 2026-07-20, but its 13-share size doesn't fully match the 23-share increase, so it only partially explains what happened. **No session or decision-log entry in this repo documents this trade.**

A second undocumented item appeared alongside it: a new working order, `Sell 1 TLT SEP 30 '26 90 Call` (order 1040104046, limit 0.25 GTC, placed 2026-07-21), i.e. an uncovered/undocumented short call against the TLT position. Also not filled yet, also not documented anywhere in this repo.

**Practical consequence: TLT's book weight is now 31.75%**, up from 27.93% last sync — well above the 15% single-position cap (Upgrade 7), though TLT is a non-equity holding the framework doesn't currently gate the same way scored equities are (see the standing "TLT, non-equity, framework gap" note in `holdings.md`). Worth flagging to the user regardless, given the position-cap logic exists specifically to bound concentration risk like this.

**The open governance items from prior syncs remain open and unresolved:**

| Ticker | Issue | Status |
|---|---|---|
| **TLT** | 77 → 100 shares (+23), undocumented; new undocumented short call working | **New this sync** — see above |
| **META** | 6 → 5 shares (-1), unauthorized sale | Still open — no session/decision/override explains the mechanism |
| **DOCS** | Unauthorized short PUT (Aug21'26 $17.50 strike) | Still open — logged in override-log.md, expires 2026-08-21 |
| **RGL** | 60,000-share position, no Phase 01/02 evaluation ever run | Still open — a sub-cent ASX gold explorer with no quality-gate screen |
| **MBGL** | Ungoverned position, no evaluation on file | Still open |

All other 27 IBKR positions matched the 2026-07-20 sync exactly in share count and average cost — only prices moved. The carried MA/V/PDD/NOW/META order-level flags persist unchanged, and the four `REPLACED`-with-no-successor orders (HDSN, META BUY, TRN BUY, CSGP SELL) are unchanged too — full detail in [ibkr-orders.md](../../portfolio/snapshots/ibkr-orders.md).

**Notable price move (informational):** RGL (RiversGold, ASX) rose ~20% in AUD terms this week (AUD $0.0075 → $0.009/share) — a partial reversal of last week's ~6% decline; still no Phase 01/02 evaluation exists for this ticker.

**Ticker lookup CSV:** the live source (`interactivebrokers.com/download/fracshare_stk.csv`) was reachable this sync (HTTP 200) — fetched and re-committed as the stored fallback. No held ticker needed the lookup (all resolved via `contract_description`).

Full per-ticker detail is in [ibkr.md](../../portfolio/snapshots/ibkr.md) and [override-log.md](../../portfolio/override-log.md) (unchanged this sync — none of the five items above have been closed out yet).

---

## 2. Upcoming Earnings (next 7 days)

`EODHD_API_KEY` is present in the environment again this run. **Not used** — [decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md) records this specific key as a **compromised credential** that should be rotated before any reuse, and the current `framework/automation-schedule.md` Routine 2 prompt directs earnings-date checks to `yfinance` instead — consistent with the calls already made repeatedly in [issues #294](https://github.com/Cloxy777/investment-framework/issues/294), [#337](https://github.com/Cloxy777/investment-framework/issues/337), and [#361](https://github.com/Cloxy777/investment-framework/issues/361).

`yfinance` itself hit the same `curl_cffi` TLS-reset-through-proxy failure documented in those issues (confirmed again this run — every ticker's `.calendar` call failed with `SSLError: Recv failure: Connection reset by peer`). Worked around it the same way those issues did: direct `requests` calls to Yahoo's `quoteSummary` endpoint (crumb handshake, no browser-TLS-impersonation layer), `calendarEvents` module, for all 22 current equity holdings.

**Earnings in the next 7 days (26 Jul – 02 Aug 2026):**

| Ticker | Earnings Date | Current Weight |
|---|---|---|
| **MSFT** | 29 Jul 2026 | 14.62% |
| **AMZN** | 30 Jul 2026 | 9.48% |
| **META** | 29 Jul 2026 | 6.16% |
| **SPGI** | 28 Jul 2026 | 0.74% |
| **V** | 28 Jul 2026 | 0.62% |
| **CSGP** | 28 Jul 2026 | 1.20% |

Six holdings report this week, including the two largest positions in the book (MSFT, AMZN) plus META — together **~30% of the combined portfolio**. Expect Routine 1 to open `rescore-due` issues for each as their releases land; none has reported yet as of this sync.

**Data-quality caveat:** Yahoo's `calendarEvents.earnings.earningsDate` field showed **GOOG** and **NOW** as "2026-07-22" — that's the date they *already* reported (GOOG already rescored same-day per [sessions/2026-07-22-rescore-goog.md](../../sessions/2026-07-22-rescore-goog.md); NOW has an open rescore issue, #361, due tomorrow) — the field appears to not roll forward to the next estimate immediately post-earnings for some tickers. Excluded both from the table above since neither is a genuinely upcoming release. `MBGL` (ungoverned position) returned no calendar data at all — likely too small/thinly covered for Yahoo's calendar module; not flagged as an error given its ungoverned status.

---

## 3. Overdue `rescore-due` Issues

Two of the three open `rescore-due` issues are overdue as of today (26 Jul 2026):

| Issue | Ticker | Trigger | Due | Days Overdue |
|---|---|---|---|---|
| [#337](https://github.com/Cloxy777/investment-framework/issues/337) | STIM | Rule 9 — unexplained +24.38% move on 2026-07-20 | 2026-07-23 | **3 days** |
| [#294](https://github.com/Cloxy777/investment-framework/issues/294) | NFLX | Earnings released 2026-07-16 | 2026-07-21 | **5 days** |

Both remain stuck on the same underlying cause: several Standard Re-Score fields (EV/EBIT, FCF Yield, Net Debt/EBITDA, 5yr Avg PE) can't be reliably auto-filled given the Yahoo/`yfinance` data degradation documented in both issues (and again in section 2 above) — a manual TIKR/Koyfin/Macrotrends pull is needed to close either one out.

**Not yet overdue:** [#361](https://github.com/Cloxy777/investment-framework/issues/361) — "RESCORE: NOW - earnings released 2026-07-22" — due tomorrow, 2026-07-27.

---

## 4. Quarterly / Annual Items Due

**None due this week.** Today (26 Jul 2026) falls outside the first-7-days-of-quarter window (1–7 Jul) that triggers the Quarterly Rate Environment Gate Review for Q3 2026 — that window has already passed, and Q4's (1–7 Oct) hasn't started.

---

## Glossary

See [framework/glossary.md](../../framework/glossary.md) for the standing definitions file. Terms used in this brief: Composite Score, GTC (Good-Till-Cancelled order), NAV (Net Asset Valuation), Net Liquidation Value, Override, Phase 01/02 (the framework's quantitative quality-gate and valuation-scoring passes), Position Cap (Upgrade 7 — the 15% single-holding weight ceiling), Quality Score, R/R (Risk/Reward ratio), Rescore, Rule 9 (mandatory immediate re-score trigger on an unexplained >15% move or an earnings release), Valuation Score.
