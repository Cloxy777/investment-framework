# Stale-score registry

A central, at-a-glance list of watchlist entries whose **valuation score predates the current scoring methodology** and is therefore not comparable to current scores. This is the general staleness mechanism — see [README.md](README.md#stale-scores--when-the-scoring-methodology-changes) for how it works.

**How an entry lands here:** when the scoring methodology version (see [valuation-scoring.md](../framework/valuation-scoring.md)) is bumped, every watchlist entry that carries a *numeric* score computed under an older version is flagged stale (a banner is added to the entry file and a row is added below). Entries that are "Phase 01 FAIL / not scored" are **not** flagged — there is no Phase 02 score for a methodology change to invalidate.

**How an entry leaves here:** when `/rescore` (held) or `/new-position` (not held) writes a fresh entry under the current methodology, that command removes the entry's banner **and** deletes its row here.

---

## Current methodology version: **2026-10-12**
*(Stock-based compensation treated as a cost in the FCF yield (Valuation) and FCF Quality (Quality), plus a new SBC ≥ 100% of FCF hard disqualifier — see [decisions/2026-10-12-framework-change-sbc-as-a-cost.md](../decisions/2026-10-12-framework-change-sbc-as-a-cost.md), [valuation-scoring.md](../framework/valuation-scoring.md) and [quality-scoring.md](../framework/quality-scoring.md).)*

Every entry with a numeric score dated before 2026-10-12 is flagged; the per-ticker table is the machine-owned block at the bottom of this file (`stale-score:auto version=2026-10-12`). Each row clears automatically when `/rescore` or `/new-position` writes a fresh entry. Suggested order: held SBC-heavy names first (DUOL, NOW, CSGP, NKE, UBER, VEEV, ADBE, AVGO, META), then the rest as earnings come due. Entries that are "Phase 01 FAIL / not scored" were not flagged (no score to invalidate).

---

## Previous methodology version: **2026-06-29** (all its entries have since been rescored or resolved — the table below is empty)
*(Quality Score + 80.0+ gate + Composite Score added — see [decisions/2026-06-29-framework-change-quality-score-and-composite.md](../decisions/2026-06-29-framework-change-quality-score-and-composite.md) and [quality-scoring.md](../framework/quality-scoring.md).)*

This version adds a new score (Quality Score) and a new combined number (Composite Score) on top of the existing valuation score — it does not change how the valuation score itself is computed, but every entry below still needs both new numbers computed before it's current. Per-ticker rows only — no blanket notes — so each one clears individually the moment `/rescore` or `/new-position` touches that ticker.

## Stale entries — 2026-06-29 methodology (Quality Score / Composite Score pending)

| Ticker | Location | Score | Scored (date) | Flagged stale |
|--------|----------|-------|----------------|----------------|

*Not listed (no real Phase 02 score for this addition to invalidate): every not-in-portfolio entry that is Phase 01 FAIL / not scored (CBRS, CCL, CHTR, CIEN, CRM, CVX, DASH, FDX, FICO, FUBO, GTLB, HIMS, IBM, LULU, MCD, MELI, MU, NOK, ORCL, PLTR, PYPL, TTD, TTWO, WSE) and the in-portfolio rows that are cash/non-equity/override/quality-gate-fail (RBRK, STIM, TLT, XEON). BULL, HY9H, SOFI, and SSU also excluded — each is Phase 01 FAIL with a Phase 02 number computed only for the record, never a binding score. (CBRS, CHTR, FUBO, and LULU additionally now carry a Quality Score under the engine added this same date — see each ticker's session file — but that score still fails the 80.0+ gate, so no Phase 02/Composite Score exists to go stale either way.)*

**SGE resolved 2026-08-24:** rescored under the current Quality Score engine — Quality Score 66.8, **fails the 80.0+ gate** (a clear fail, not a knife-edge one). Per quality-scoring.md's strict gate, no Phase 02 valuation score or Composite Score was computed this session (same treatment as CBRS/CHTR/FUBO/LULU above) — see [sessions/2026-08-24-rescore-sge.md](../sessions/2026-08-24-rescore-sge.md) and [not-in-portfolio/SGE/SGE-2026-08-24.md](not-in-portfolio/SGE/SGE-2026-08-24.md), which supersedes the old 21.1 (pre-Quality-Score) figure.

**AVGO resolved 2026-07-04:** rescored under the full current methodology (Quality 82.1, Valuation 68.2, Composite 43.1) — see [sessions/2026-07-04-rescore-avgo.md](../sessions/2026-07-04-rescore-avgo.md) and [in-portfolio/AVGO/AVGO-2026-07-04.md](in-portfolio/AVGO/AVGO-2026-07-04.md), which supersedes both the old 69.5 and the never-adopted 74.8 figures. `watchlist/not-in-portfolio/AVGO/` remains a leftover duplicate folder (AVGO is held, per `holdings.md`) that `/sync-portfolio` should still fold into `in-portfolio/`.

## Stale entries — 2026-06-20 methodology (Upside/Downside Modifier) — pending rescore

| Ticker | Location | Stale score | Scored (methodology) | Flagged stale |
|--------|----------|-------------|----------------------|---------------|

*SGE removed 2026-08-24 (see the 2026-06-29 table above — resolved to a Quality Gate fail, no Phase 02 score exists to be stale under either methodology version now).*

*MA removed from this table during the 2026-06-29 update: `MA-2026-06-22.md` already carries a fresh post-modifier score (38.0, scored 2026-06-22) and never carried a 2026-06-20 banner — the row was simply never cleared when that rescore happened. Corrected here as a registry bookkeeping fix, not a re-score.*

*Not listed (not affected by the 2026-06-20 Phase 02 change): the 10 not-in-portfolio entries that are Phase 01 FAIL / not scored (CIEN, CRM, DASH, FICO, GTLB, HIMS, MELI, ORCL, PYPL, TTD) and MU (Phase 01 FAIL). All in-portfolio holdings except AVGO (see note above) were rescored under the current methodology on 2026-06-20 and are current on that axis.*

<!-- stale-score:auto version=2026-06-29 -->
<!-- /stale-score:auto -->

<!-- stale-score:auto version=2026-10-12 -->
| Ticker | Location | Scored (date) |
|--------|----------|----------------|
| ADBE | in-portfolio/ADBE/ADBE-2026-09-11.md | 2026-09-11 |
| AMZN | in-portfolio/AMZN/AMZN-2026-08-01.md | 2026-08-01 |
| BKNG | in-portfolio/BKNG/BKNG-2026-10-11.md | 2026-10-11 |
| BULL | in-portfolio/BULL/BULL-2026-08-20.md | 2026-08-20 |
| CSGP | not-in-portfolio/CSGP/CSGP-2026-10-11.md | 2026-10-11 |
| DUOL | in-portfolio/DUOL/DUOL-2026-09-01.md | 2026-09-01 |
| META | in-portfolio/META/META-2026-08-26.md | 2026-08-26 |
| MSFT | in-portfolio/MSFT/MSFT-2026-07-30.md | 2026-07-30 |
| NFLX | in-portfolio/NFLX/NFLX-2026-07-17.md | 2026-07-17 |
| NKE | in-portfolio/NKE/NKE-2026-10-11.md | 2026-10-11 |
| NOW | in-portfolio/NOW/NOW-2026-08-09.md | 2026-08-09 |
| NVDA | in-portfolio/NVDA/NVDA-2026-09-17.md | 2026-09-17 |
| NVO | in-portfolio/NVO/NVO-2026-08-09.md | 2026-08-09 |
| SPGI | in-portfolio/SPGI/SPGI-2026-08-09.md | 2026-08-09 |
| TRN | in-portfolio/TRN/TRN-2026-09-10.md | 2026-09-10 |
| UBER | in-portfolio/UBER/UBER-2026-09-15.md | 2026-09-15 |
| V | in-portfolio/V/V-2026-07-29.md | 2026-07-29 |
| VEEV | in-portfolio/VEEV/VEEV-2026-08-30.md | 2026-08-30 |
| ZS | in-portfolio/ZS/ZS-2026-10-11.md | 2026-10-11 |
| 0700-HK | not-in-portfolio/0700-HK/0700-HK-2026-08-12.md | 2026-08-12 |
| AAOI | not-in-portfolio/AAOI/AAOI-2026-08-14.md | 2026-08-14 |
| AAPL | not-in-portfolio/AAPL/AAPL-2026-07-06.md | 2026-07-31 |
| ABNB | not-in-portfolio/ABNB/ABNB-2026-08-24.md | 2026-08-24 |
| ADSK | not-in-portfolio/ADSK/ADSK-2026-08-23.md | 2026-08-23 |
| ANTA | not-in-portfolio/ANTA/ANTA-2026-08-26.md | 2026-08-26 |
| APP | not-in-portfolio/APP/APP-2026-09-21.md | 2026-09-21 |
| ASML | not-in-portfolio/ASML/ASML-2026-09-11.md | 2026-09-11 |
| ASML.AS | not-in-portfolio/ASML.AS/ASML.AS-2026-09-17.md | 2026-09-17 |
| AXP | not-in-portfolio/AXP/AXP-2026-07-19.md | 2026-07-19 |
| BE | not-in-portfolio/BE/BE-2026-08-24.md | 2026-08-24 |
| BRK | not-in-portfolio/BRK/BRK-2026-08-23.md | 2026-08-23 |
| C | not-in-portfolio/C/C-2026-07-12.md | 2026-07-12 |
| CAJPY | not-in-portfolio/CAJPY/CAJPY-2026-07-27.md | 2026-07-27 |
| CDR | not-in-portfolio/CDR/CDR-2026-06-29.md | 2026-06-29 |
| CIEN | not-in-portfolio/CIEN/CIEN-2026-06-11.md | 2026-07-06 |
| COHR | not-in-portfolio/COHR/COHR-2026-08-14.md | 2026-08-14 |
| COIN | not-in-portfolio/COIN/COIN-2026-07-31.md | 2026-07-31 |
| CRDO | not-in-portfolio/CRDO/CRDO-2026-08-14.md | 2026-08-14 |
| CRM | not-in-portfolio/CRM/CRM-2026-06-12.md | 2026-07-06 |
| CRWD | not-in-portfolio/CRWD/CRWD-2026-08-27.md | 2026-08-27 |
| DB1 | not-in-portfolio/DB1/DB1-2026-07-07.md | 2026-07-07 |
| DOCS | not-in-portfolio/DOCS/DOCS-2026-09-11.md | 2026-09-11 |
| DOCU | not-in-portfolio/DOCU/DOCU-2026-07-19.md | 2026-07-19 |
| E | not-in-portfolio/E/E-2026-07-19.md | 2026-07-19 |
| ENPH | not-in-portfolio/ENPH/ENPH-2026-07-25.md | 2026-07-25 |
| EXPN | not-in-portfolio/EXPN/EXPN-2026-07-07.md | 2026-07-07 |
| GPRO | not-in-portfolio/GPRO/GPRO-2026-09-01.md | 2026-09-01 |
| GTLB | not-in-portfolio/GTLB/GTLB-2026-09-02.md | 2026-09-02 |
| HD | not-in-portfolio/HD/HD-2026-08-16.md | 2026-08-16 |
| HIMS | not-in-portfolio/HIMS/HIMS-2026-08-11.md | 2026-08-11 |
| HOOD | not-in-portfolio/HOOD/HOOD-2026-07-25.md | 2026-07-30 |
| HTO | not-in-portfolio/HTO/HTO-2026-06-30.md | 2026-06-30 |
| INTU | not-in-portfolio/INTU/INTU-2026-08-23.md | 2026-08-23 |
| JPM | not-in-portfolio/JPM/JPM-2026-07-14.md | 2026-07-14 |
| KO | not-in-portfolio/KO/KO-2026-07-28.md | 2026-07-28 |
| LITE | not-in-portfolio/LITE/LITE-2026-08-14.md | 2026-08-14 |
| LLY | not-in-portfolio/LLY/LLY-2026-08-25.md | 2026-08-25 |
| LMND | not-in-portfolio/LMND/LMND-2026-07-29.md | 2026-07-29 |
| LMT | not-in-portfolio/LMT/LMT-2026-07-19.md | 2026-07-19 |
| MA | not-in-portfolio/MA/MA-2026-09-11.md | 2026-09-11 |
| MCD | not-in-portfolio/MCD/MCD-2026-06-24.md | 2026-09-06 |
| MCO | not-in-portfolio/MCO/MCO-2026-09-11.md | 2026-09-11 |
| MELI | not-in-portfolio/MELI/MELI-2026-08-05.md | 2026-08-05 |
| MORN | not-in-portfolio/MORN/MORN-2026-08-26.md | 2026-08-26 |
| MRK | not-in-portfolio/MRK/MRK-2026-08-19.md | 2026-08-19 |
| MRNA | not-in-portfolio/MRNA/MRNA-2026-08-19.md | 2026-08-19 |
| MSI | not-in-portfolio/MSI/MSI-2026-08-23.md | 2026-08-23 |
| MU | not-in-portfolio/MU/MU-2026-07-29.md | 2026-07-29 |
| NET | not-in-portfolio/NET/NET-2026-08-07.md | 2026-08-07 |
| NOVO-B.CO | not-in-portfolio/NOVO-B.CO/NOVO-B.CO-2026-09-17.md | 2026-09-17 |
| ONON | not-in-portfolio/ONON/ONON-2026-09-18.md | 2026-09-18 |
| PDD | not-in-portfolio/PDD/PDD-2026-08-26.md | 2026-08-26 |
| PGHN | not-in-portfolio/PGHN/PGHN-2026-08-26.md | 2026-08-26 |
| PLTR | not-in-portfolio/PLTR/PLTR-2026-08-04.md | 2026-08-04 |
| POET | not-in-portfolio/POET/POET-2026-08-14.md | 2026-08-14 |
| PROYA | not-in-portfolio/PROYA/PROYA-2026-08-26.md | 2026-08-26 |
| PYPL | not-in-portfolio/PYPL/PYPL-2026-08-28.md | 2026-08-28 |
| QCOM | not-in-portfolio/QCOM/QCOM-2026-09-08.md | 2026-09-08 |
| RACE | not-in-portfolio/RACE/RACE-2026-08-17.md | 2026-08-17 |
| RACE.MI | not-in-portfolio/RACE.MI/RACE.MI-2026-09-17.md | 2026-09-17 |
| RDDT | not-in-portfolio/RDDT/RDDT-2026-08-14.md | 2026-08-14 |
| RKLB | not-in-portfolio/RKLB/RKLB-2026-08-11.md | 2026-08-11 |
| RMV | not-in-portfolio/RMV/RMV-2026-08-26.md | 2026-08-26 |
| SCHW | not-in-portfolio/SCHW/SCHW-2026-07-19.md | 2026-07-19 |
| SHOP | not-in-portfolio/SHOP/SHOP-2026-08-05.md | 2026-08-05 |
| SKHY | not-in-portfolio/SKHY/SKHY-2026-07-17.md | 2026-07-17 |
| SNDK | not-in-portfolio/SNDK/SNDK-2026-08-05.md | 2026-08-13 |
| SOUN | not-in-portfolio/SOUN/SOUN-2026-08-24.md | 2026-08-24 |
| SPOT | not-in-portfolio/SPOT/SPOT-2026-08-04.md | 2026-08-04 |
| TM | not-in-portfolio/TM/TM-2026-07-12.md | 2026-07-12 |
| TSM | not-in-portfolio/TSM/TSM-2026-09-06.md | 2026-09-06 |
| TTD | not-in-portfolio/TTD/TTD-2026-09-11.md | 2026-09-11 |
| TTWO | not-in-portfolio/TTWO/TTWO-2026-08-07.md | 2026-08-07 |
| VOW3 | not-in-portfolio/VOW3/VOW3-2026-09-04.md | 2026-09-04 |
| VRSN | not-in-portfolio/VRSN/VRSN-2026-07-19.md | 2026-07-19 |
| VST | not-in-portfolio/VST/VST-2026-08-27.md | 2026-08-27 |
| WBD | not-in-portfolio/WBD/WBD-2026-09-12.md | 2026-09-12 |
| WISE | not-in-portfolio/WISE/WISE-2026-08-27.md | 2026-08-27 |
| WMT | not-in-portfolio/WMT/WMT-2026-08-20.md | 2026-08-20 |
<!-- /stale-score:auto -->
