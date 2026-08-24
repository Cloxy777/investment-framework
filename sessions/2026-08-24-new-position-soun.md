# New Position Evaluation: SOUN (SoundHound AI, Inc.) — 2026-08-24

**Task type:** NEW POSITION (Telegram-scan trigger, Routine 6, first-ever evaluation)
**Ticker:** SOUN — NASDAQ (Class A), IBKR contract_id 558869874
**Company:** SoundHound AI, Inc. — conversational/voice AI platform (voice assistants, restaurant/drive-thru ordering, automotive voice interfaces); also markets its own Polaris speech model and an "OASYS" agentic-AI platform
**Fiscal year end:** December 31
**10Y US Treasury yield:** not fetched this session — the FRED and CNBC endpoints tried both returned HTTP 403/503 for an unauthenticated fetch, and the Rate Environment Gate is never reached (see §3), so this is recorded as a gap rather than guessed
**First-use jargon decode:** every term used below is already defined in [glossary.md](../framework/glossary.md) (10-K, CIK, EDGAR, XBRL, GAAP, Fiscal Year, TTM, Rolling-window, Rule 0, Rule 9, Quality Score, Hard disqualifier, FCF, CapEx) — see closing Glossary (§6)

---

## 0. Why this session exists — trigger source, and watchlist check

A Telegram post on `t.me/FinnInvestChannel` (post FinnInvestChannel/3136, ~2026-08-24 12:14 UTC) discussed SoundHound "betting on AI to dramatically improve margins," citing Q2 revenue growth of 45% to $61.9M, the OASYS agentic-AI platform, and the company's proprietary Polaris speech model. **This text is not financial data — it is only the reason this session was triggered.** Per this repo's standing convention, a first-ever mention of a ticker with no existing watchlist entry triggers a full `/new-position` evaluation regardless of the mention's substance, and regardless of whether the post describes a Rule 9 event.

Watchlist check performed before assuming no entry exists: `grep`/`find` against `portfolio/holdings.md`, `watchlist/in-portfolio/`, and `watchlist/not-in-portfolio/` for "SOUN"/"SoundHound" returned **no matches anywhere**. Confirmed genuine first-ever evaluation.

**The triggering post's Q2 revenue figure is not used as a financial input anywhere below** — all figures in §3 are independently pulled from SoundHound's own SEC-filed, XBRL-tagged annual data.

---

## 1. Live Price (Rule 0 — fetched first, never inferred)

Contract confirmed via `search_contracts("SOUN")`: contract_id **558869874**, NASDAQ, "SOUNDHOUND AI INC-A" — the correct primary US listing (other results were a Mexico cross-listing (MEXI), an unrelated leveraged single-stock ETF "SOUX," and several unrelated "Sound..."-named tickers — none used).

| Field | Value | Source |
|---|---|---|
| **Live price used** | **$7.20** | IBKR `get_price_snapshot`, `last` field, contract_id 558869874. `is_close: false`, `halted: false`, timestamp resolves to 2026-08-24 12:19 UTC — a live, current-session print. |
| Change vs. prior close | −$0.12 (−1.64%) | IBKR `change` |
| 52-week high / low | $22.17 / $5.6501 | IBKR `misc_statistics` |
| 13-week / 26-week high / low | $9.52 / $5.6501 · $10.045 / $5.6501 | IBKR `misc_statistics` |
| Open 52 weeks ago | $12.16 | IBKR `misc_statistics` |
| Dividend yield | 0.0% (no dividend) | IBKR `dividend_yield` |

$7.20 sits near the low end of the 52-week range ($5.65–$22.17) — context only, not scored. No order-setup arithmetic is performed this session (see §3 for why).

---

## 2. Data Sourcing

**Primary source used throughout:** SEC XBRL `companyconcept` API (`data.sec.gov`, CIK **0001840856**), specifically `NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`, and `NetIncomeLoss` — audited, tagged, company-filed figures from SoundHound's own 10-K filings, fiscal-year-labeled by the SEC's own structured data (not a vendor's re-derivation). `yfinance` was not attempted given its documented SSL breakage since 2026-07-07 (repo precedent, see the AFRM/other recent sessions).

10Y Treasury yield fetch attempts (FRED CSV/JSON API, CNBC) both returned HTTP error codes for this unauthenticated environment — flagged as a data gap in the header, not decision-relevant since this session stops at the Quality Gate (§3) before the Rate Environment Gate would ever be reached.

---

## 3. Phase 01 — Quality Score: Hard Disqualifier Check

Per [quality-scoring.md](../framework/quality-scoring.md), three hard disqualifiers fail a company **regardless of weighted score**. Checking the FCF-positive-streak test first, since SoundHound's SEC-filed cash flow history is unambiguous and decisive on its own.

### 3.1 — Not FCF-positive for 3+ consecutive years

Per the 2026-08-05 rolling-window clarification, this test uses **the most recently completed fiscal years available at the time of scoring**. SoundHound's FY2026 10-K has not yet been filed, so the current window is **FY2023–FY2025**:

| Fiscal Year | Operating Cash Flow | CapEx | **FCF** | Source |
|---|---|---|---|---|
| FY2021 | −$864,358 | $636,000 | **−$1,500,358** | SEC XBRL, primary |
| FY2022 | −$94,019,000 | $1,329,000 | **−$95,348,000** | SEC XBRL, primary |
| FY2023 | −$68,265,000 | $392,000 | **−$68,657,000** | SEC XBRL, primary |
| FY2024 | −$108,878,000 | $640,000 | **−$109,518,000** | SEC XBRL, primary |
| FY2025 | −$98,222,000 | $902,000 | **−$99,124,000** | SEC XBRL, primary |

Every one of the last five reported fiscal years is FCF-negative — not merely the required 3-year window (FY2023–FY2025), but the entire disclosed operating history back to FY2021. This is a clean, decisively-supported result — no ambiguity, no growth-capex carve-out available (this disqualifier carries none per [quality-scoring.md](../framework/quality-scoring.md)), and no judgment call required.

### **HARD DISQUALIFIER FIRES: not FCF-positive for 3+ consecutive years.**

Per [quality-scoring.md](../framework/quality-scoring.md) ("a weighted average can't average away an outright balance-sheet or cash-flow-quality failure") and [.claude/commands/new-position.md](../.claude/commands/new-position.md) step 2, **this session stops here**. No weighted Phase 01 Quality Score (Profitability/Margins/Growth/Moat/FCF-Quality sub-scores), Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work is performed.

*(For completeness, not decision-relevant: FY2021–FY2025 Net Income was also negative every year — SEC XBRL `NetIncomeLoss` shows losses in each reported fiscal year — so the FCF/Net Income conversion-ratio hard disqualifier is not meaningful to compute in any year either, same convention as AFRM's FY2024 in this framework's 2026-08-23 session. Net Debt/EBITDA was not checked — unneeded once §3.1 fires cleanly and decisively.)*

---

## 4. Context — the triggering post's substance, not scored

Nothing below is scored — it's qualitative color on what the triggering Telegram post actually referenced, for the record.

SoundHound's own public disclosures (Q2 2026 earnings release, referenced generically by the triggering post) do report accelerating revenue growth and management commentary around margin improvement plans (OASYS platform monetization, proprietary Polaris speech model reducing third-party model licensing costs). None of this changes §3.1's conclusion: revenue growth and a stated *intent* to improve margins are not the same as demonstrated free-cash-flow generation, and this framework's hard disqualifiers are bright-line tests on realized cash flow, not on management's forward narrative (consistent with the "guidance/self-reported metrics are not scored" principle applied throughout this framework).

---

## 5. Recommendation: **PASS (no entry) — Quality Gate FAILS on a clean hard disqualifier**

**Do not enter SOUN this session.** A hard disqualifier fires cleanly and decisively across the company's entire disclosed operating history (FY2021–FY2025, every year FCF-negative), verified against SoundHound's own SEC-filed, XBRL-tagged cash flow figures. Unlike some other Telegram-triggered evaluations in this repo where a disqualifier is a near-miss (e.g. AFRM, 2 of 3 required years), this is not a close call — there is no recent trend suggesting FCF profitability is imminent. **No Rate Environment Gate, Phase 02 valuation score, Composite Score, or fair-value/order-setup work was performed**, consistent with the command specification's instruction to stop at a hard-disqualifier failure.

**The triggering Telegram post** (a routine channel post citing SoundHound's Q2 revenue growth and AI-margin narrative) was used only as the reason to run this first-ever evaluation; it is not, and was never treated as, a financial input.

---

## 6. Next Review Trigger

No routine re-check is scheduled on a numeric-score basis (no Phase 02 score exists to go stale — the Quality Gate never cleared). Re-evaluate on any of the following, whichever comes first:

- SoundHound's FY2026 10-K (once filed) — even if FY2026 alone were to close FCF-positive for the first time, the rolling window (FY2024–FY2026) would still contain two negative years (FY2024, FY2025), so this disqualifier will not clear until at least the FY2027 10-K at the earliest, absent a dramatic operating-cash-flow inflection.
- A material, documented shift toward sustained positive operating cash flow (not merely a single favorable quarter) — a genuine Rule 9-style fundamental change, as opposed to routine quarterly commentary.
- The standard Rule 9 triggers: guidance revision, management change, material M&A, macro/rate shift, or a >15% unexplained price move.

Absent a qualifying trigger, a future Telegram mention of SOUN should be logged as "last checked, no change" rather than triggering a full re-evaluation.

**No position opened — nothing to log in `decisions/`.**

---

## 7. Glossary

| Term | Meaning |
|---|---|
| **10-K (Annual Report)** | The annual financial-disclosure report a US public company must file with the SEC, containing full audited financial statements — the primary source for SoundHound's FY2021–FY2025 cash flow figures above. |
| **CapEx** | Capital Expenditure — money spent buying or upgrading physical assets; small and stable for SoundHound ($0.4M–$1.3M/year), not a material driver of its FCF shortfall. |
| **CIK (Central Index Key)** | The unique numeric identifier the SEC assigns to every EDGAR filer — SoundHound AI, Inc.'s is 0001840856, used to construct the SEC XBRL API paths this session pulled from. |
| **EDGAR** | The SEC's free public database of every US-registered company's filings — the source for SoundHound's CIK and filing history. |
| **FCF (Free Cash Flow)** | Operating cash flow minus capital expenditure — cash a business generates after running and maintaining itself. Negative in every one of SoundHound's last five reported fiscal years (§3.1), the basis for this session's hard-disqualifier fail. |
| **Fiscal Year (FY)** | A company's 12-month accounting year. SoundHound's fiscal year matches the calendar year (ends December 31). |
| **GAAP** | Generally Accepted Accounting Principles — the standard US accounting rulebook; all figures above are GAAP, company-filed, not a non-GAAP or adjusted metric. |
| **Hard disqualifier** | One of three Quality Score conditions ([quality-scoring.md](../framework/quality-scoring.md)) that fails a company regardless of its weighted sub-score total. SoundHound fails on "not FCF-positive for 3+ consecutive years" (§3.1). |
| **Quality Score** | This framework's 0.0–100.0 continuous score (higher = better); 80.0+ required to proceed to valuation scoring. Not computed for SOUN this session — a hard disqualifier fired first (§3.1). |
| **Rolling-window (disqualifier test)** | This framework's convention that the FCF-positive-streak hard-disqualifier test uses the most recently completed fiscal years available at the time of scoring, rolling forward as each new fiscal year reports. Used here to set the FY2023–FY2025 window (§3.1), though SoundHound's full FY2021–FY2025 history is shown since every year fails regardless. |
| **Rule 0** | This framework's standing instruction to always fetch a live, current price before any valuation work, and to never treat a Telegram post's claims as a financial input — the live price (§1) was fetched via IBKR before any other work in this session. |
| **Rule 9** | This framework's list of fundamental events that force an immediate re-valuation: earnings, guidance revisions, management changes, M&A, macro shifts, or a >15% unexplained price move. |
| **TTM (Trailing Twelve Months)** | The most recent 12 months of reported financial results — not used in this session since the evaluation stopped at the annual-fiscal-year hard-disqualifier check before any TTM-based sub-score would have been computed. |
| **XBRL** | The SEC's structured, machine-readable data format for financial-statement figures — the format this session's `companyconcept` API pulls (`NetCashProvidedByUsedInOperatingActivities`, `PaymentsToAcquirePropertyPlantAndEquipment`, `NetIncomeLoss`) came in. |
