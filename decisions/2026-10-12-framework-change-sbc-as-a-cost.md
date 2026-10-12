# 2026-10-12 — Framework change: stock-based compensation (SBC) treated as a cost in Valuation and Quality

**Methodology version bumped to 2026-10-12** (valuation-scoring.md and quality-scoring.md). Stale-score run applied to the watchlist.

**What prompted it:**

Phase A ([2026-10-12-framework-change-advisory-flags-and-sbc-disclosure.md](2026-10-12-framework-change-advisory-flags-and-sbc-disclosure.md)) made SBC visible but left every score blind to it. Reported free cash flow adds SBC back, yet SBC is a real cost to owners through dilution. FCF yield is 40% of the Valuation Score and FCF Quality is 10% of the Quality Score. Three pilots on live holdings quantified the effect and refined the design: [08](../research/framework-review/08-phase-b-pilot-results.md) (Valuation side), [09](../research/framework-review/09-quality-sbc-pilot-results.md) (Quality side), [10](../research/framework-review/10-duol-filings-check.md) (DUOL checked against SEC filings). The user chose the "treat SBC as a cost" practice (Buffett/Munger, Damodaran, most value/quality shops) over the sell-side "add it back" convention.

**The decision:**

1. **Valuation — FCF Yield:** `FCF_Score` uses `(FCF − SBC) ÷ market cap` (TTM). **Owner-Earnings names (Upgrade 1) are exempt** — their net-income base already deducts SBC. `sbc_yield_pct` is a required input (pass `0` only if no SBC is reported; missing → stop and ask).
2. **Valuation — shareholder yield (double-count guard):** the Upside/Downside shareholder yield uses **gross cash buybacks**, not net of issuance, because the dilution is already deducted in the FCF yield. Input renamed `net_buyback_yield_pct` → `buyback_yield_pct`, with required `buyback_yield_basis = "gross_cash"`.
3. **Quality — FCF Quality (10%):** ratio becomes `(FCF − SBC) ÷ net income`. GAAP net income already deducts SBC while FCF adds it back, so the plain ratio compared unlike things. Input renamed `fcf_ni_ttm_pct` → `fcf_after_sbc_ni_ttm_pct`.
4. **Quality — net-income normalisation (required by the DUOL check):** if reported net income carries a one-time item (e.g. a tax valuation-allowance release), the analyst uses net income without it and cites what was removed, amounts and filing (`ni_normalised` + `ni_normalisation_text`; `fetch_fundamentals --normalised-ni … --normalisation-note …`). It is a documented judgement, never a default. This applies Rule 6 ("Normalize Before You Value") to the sub-score.
5. **Quality — new hard disqualifier:** SBC ≥ 100% of TTM FCF (or FCF ≤ 0 with SBC > 0), unless a one-off (e.g. IPO-year grants) is documented with amounts and source.
6. **Unchanged on purpose:** the existing `FCF/NI < 70% for 2+ years` disqualifier keeps the **plain** annual ratio. On the after-SBC ratio it would have disqualified MSFT, META, GOOG and CSGP — AI-capex names whose FCF is depressed by growth capex, which the rule's growth-capex exception already handles.

**Evidence and expected effect (pilots, 15–16 live holdings; sensitivity, not full re-scores):**

- Valuation: SBC-heavy names +3…+8 points (DUOL +8.4, CSGP +6.5, NOW +6.0, NKE +5.5, UBER +5.3, VEEV +4.2, ADBE +3.1); Owner-Earnings names 0; no gate-passer changed Composite band.
- Quality: 9 of 16 holdings move < 1 point; AVGO −3.2 and META −3.4 stay above 80.0. DUOL's apparent drop through the gate (83.2 → 77.3) was an artifact of a one-time $245.7M tax benefit in reported net income; on normalised net income it stays 83.2 — which is why item 4 exists.
- No SBC ≥ 100% of FCF among current holdings (highest: CSGP 84.6%).

**Known limits (stated, not hidden):**

- The pilots held the buyback input fixed. Switching to gross buybacks (item 2) raises the expected-return term for names with large share issuance and partly offsets the FCF-score increase for them; the true combined effect appears at each rescore, not in the pilot. NOW, DUOL and CSGP are the most exposed — rescore them first and compare.
- yfinance SBC/buyback rows can be missing (notably foreign IFRS filers such as NVO); the scorers then stop and ask. Read the figure from the filing.
- The FCF Quality scale (40%–100%) was built for the plain ratio; after-SBC ratios sit lower for share-paying firms. Not recalibrated here.
- XBRL-based verification covered DUOL only.

**Not changed:** the operating-margin Quality input (failed the pilot), action-band hysteresis (inconclusive), the three-state gate, scored cycle-peak/ceiling limits (no data source). Advisory flags from the earlier decision remain advisory.

**Alignment check ([investor-philosophy-alignment.md](../framework/investor-philosophy-alignment.md)):** Buffett/Munger (SBC is a real expense; consistent with Upgrade 1), Greenblatt (EBIT/earnings after SBC, systematic rule), Fisher/Lynch (earnings quality) — pass. Guidance test: not engaged. Turnover/price-action/macro: not engaged. Conscious divergence from the sell-side convention: recorded above.

**Graveyard test:** none of the seven cases is SBC-driven; the new disqualifier is a forward-looking guard (SBC consuming all cash flow).

**Impact:** methodology version 2026-06-29 → 2026-10-12. **Every watchlist entry with a numeric score is flagged stale** (`python -m scripts.stale_score --apply`) and clears as `/rescore` or `/new-position` brings the ticker current. Existing session logs and decision logs are history and are not edited. Suggested rescore order: held SBC-heavy names first — DUOL, NOW, CSGP, NKE, UBER, VEEV, ADBE, AVGO, META — then the rest as earnings come due. Rollback: revert this commit and the version stamp; the stale banners clear via the same mechanism.

**Files touched:**
- `scripts/scoring/valuation_score.py`, `scripts/scoring/quality_score.py`, `scripts/fetch_fundamentals.py`
- `scripts/tests/test_valuation_score.py`, `test_quality_score.py`, `test_composite_score.py`, `test_fetch_fundamentals.py`
- `framework/valuation-scoring.md`, `framework/quality-scoring.md`, `framework/strategy.md`, `framework/operating-calendar.md`, `framework/glossary.md`
- `.claude/commands/new-position.md`, `.claude/commands/rescore.md`
- `watchlist/STALE.md` and the stale banners on the flagged watchlist entries
- `decisions/` — this file.

## Glossary
- **SBC (stock-based compensation):** pay in shares or options; costs owners through dilution but is added back in reported free cash flow.
- **FCF yield after SBC:** (free cash flow − SBC) ÷ market cap.
- **FCF Quality:** how much of reported profit turns into real cash; now (FCF − SBC) ÷ net income.
- **Normalised net income:** net income after removing documented one-time items.
- **Gross cash buyback yield:** cash spent repurchasing shares ÷ market cap, ignoring new shares issued.
- **Owner Earnings (Upgrade 1):** net income + D&A − maintenance capex; used instead of FCF for businesses with heavy growth capex.
- **Hard disqualifier:** a rule failure that blocks a stock regardless of its other scores.
- **Methodology version bump / stale-score run:** changing the dated stamp on the scoring rules and flagging every score computed under the old rules until it is rescored.
- **Double counting:** penalising or rewarding the same fact twice in one score.
