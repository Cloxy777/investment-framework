# Quality Score Engine Addendum: HY9H (SK hynix Inc., GDS) — 2026-07-09

**Task type:** QUALITY SCORE ENGINE ADDENDUM (mirrors the CCL, 2026-07-06, precedent)
**Ticker (tradable instrument):** HY9H — Frankfurt Stock Exchange (FWB), IBKR contract_id 517397504, EUR, 1 GDS = 1 ordinary share (ratio confirmed in the 06-20 session, not re-derived here)
**Underlying company:** SK hynix Inc. — primary listing KRX 000660 (KRW)
**Analyst:** Claude (automated session)
**Prior session:** [2026-06-20-new-position-hy9h.md](2026-06-20-new-position-hy9h.md) — Phase 01 **FAIL** (3 of 8 criteria: FCF positive 3yr, FCF yield >4%, EV/EBIT <20×), Phase 02 score 51.6 computed anyway for documentation only, not binding since Phase 01 fails. That evaluation predates the 2026-06-29 Quality Score engine — HY9H had never had a Quality Score computed until this session.

---

## 1. Why this session exists

HY9H is a not-in-portfolio watchlist entry last touched 2026-06-20, before the Quality Score engine ([quality-scoring.md](../framework/quality-scoring.md), versioned 2026-06-29) was added to the framework. Per the CCL precedent (2026-07-06), an already-Phase-01-FAIL ticker gets a first-time Quality Score computed as a dated addendum to its existing watchlist file, without redoing Phase 01 from scratch unless a Rule 9 trigger fires that actually changes the Phase 01 verdict.

## 2. Live price (Rule 0)

yfinance (the framework's usual primary source) was unreachable this session — a network/TLS-layer failure through the sandboxed proxy (`curl_cffi.requests.exceptions.SSLError` / `curl: (35) Recv failure: Connection reset by peer`), tried both with and without explicit CA-bundle env vars (`SSL_CERT_FILE`, `REQUESTS_CA_BUNDLE`, `CURL_CA_BUNDLE` all pointed at `/root/.ccr/ca-bundle.crt`). This is a data-availability/connectivity gap, not a "no data exists" gap, so it's flagged rather than worked around by inventing a number.

Fell back to IBKR (secondary source per the framework's price-fetch strategy) plus an independent WebSearch cross-check:

| Source | Last | Prior close | Timestamp |
|---|---|---|---|
| IBKR `get_price_snapshot`, contract_id 517397504 | €1,435.00 | €1,310.00 | 2026-07-09 18:11:24 UTC |
| Investing.com (via WebSearch, secondary cross-check) | €1,450.00 | €1,310.00 | "as of July 9, 2026" |

Both sources agree on prior close exactly and on the live print to within ~1% — high confidence. Live price used: **€1,435.00** (IBKR, the more precisely-timestamped of the two).

**Unresolved flag:** a KRX-side (000660.KS) cross-check via Google Finance returned ₩2,186,000 (prior close ₩2,076,000), which — converted at today's EUR/KRW spot (~1,756-1,765, WebSearch) — implies a GDS price of only ~€1,240-1,245, roughly 13-15% below the actual observed HY9H price. This is a much wider gap than the ≤1.5% the 06-20 session found on two prior dates. Candidate explanations (Frankfurt-KRX arbitrage friction during the acute IPO-period demand spike, a timing/session mismatch, or a secondary-source data error) are all plausible but none was confirmed within this session's scope — flagged as an open data-quality gap rather than resolved or silently ignored. Because the Quality Score's own sub-scores don't depend on price (see Section 4), this gap does not affect the Quality Score result; it only matters for order-setup/fair-value work, which is out of scope for this addendum anyway (Phase 01 still fails).

## 3. Rule 9 trigger check (all 6 categories, plus the two 06-20-flagged watch items)

- **Earnings:** Not yet reported. Q2 2026 (quarter ended 2026-06-30) is expected ~2026-07-29 (one source said 2026-07-22). TTM fundamentals are therefore unchanged since 06-20 — same four reported quarters.
- **Guidance revision:** None found.
- **Management change:** None found.
- **M&A / capital-markets event:** **YES, a major one** — SK hynix is executing a $28-29B primary ADR offering on Nasdaq, new ticker **SKHY**, ADS ratio 1 ordinary : 10 ADRs (a different instrument/ratio from HY9H's existing 1:1 Frankfurt GDR — they must not be conflated), listing 2026-07-10 (tomorrow, relative to this session). ~177.9M new ADRs (~17.79M ordinary-share equivalents, ~2.5% dilution) being issued, raising ~$28B of new capital for fab/equipment expansion. **Has not closed as of this session** and is not yet reflected in any reported financial statement, so it does not move a single Phase 01/Quality Score input today — flagged for the next re-score once post-money figures are reported.
- **Macro shift / HBM4-Vera Rubin allocation:** Confirmed supportive, not deteriorating. Nvidia certified SK hynix (along with Samsung and Micron) for Vera Rubin HBM4 supply on 2026-06-05; SK hynix holds an estimated ~60-70% of Vera Rubin HBM4 volume (tighter than 06-20's 54-80% range, same leadership conclusion). No memory-cycle downturn signal found — supply stays constrained through H2 2026 per SK hynix's own guidance, Q1 2026 operating margin hit a record 72%, and the earliest plausible oversupply risk is pushed to late 2027-2028.
- **>15% unexplained price move:** No (+9.5-10.7% vs. 06-20, and explained by the SKHY IPO's 7x-oversubscribed order book plus the broader AI/HBM narrative, not unexplained).

**Net effect: Rule 9 did not fire on earnings, and the one major event found (the SKHY IPO) has not yet closed or touched any reported financial-statement line — so the Phase 01 verdict is unchanged.** This confirmed an addendum (not a full re-evaluation) was the correct path, per the task's branching instruction.

## 4. Quality Score computation

Since no new quarter has been reported, the same TTM fundamentals sourced in the 06-20 session were reused (not re-invented — they remain the most current actual reported data): TTM Net Margin 56.89%, TTM ROIC 48.3-60.5%, TTM Gross Margin 68.34%, Revenue 3yr CAGR 29.61%, Net Debt/EBITDA −0.34× (net cash), TTM FCF ₩40.69T, TTM Net Income ₩75.14T (→ TTM FCF/NI 54.16%), and the FY2022-FY2025 FCF-positive/negative history.

| Sub-score (weight) | Value |
|---|---|
| Profitability (25%) | **40.0** (capped from an uncapped 100.0 — FCF-positive only 2 consecutive years, not 3) |
| Margins (15%) | **85.4** (Gross Margin 68.34%; no structural-trend bonus, since that bonus only applies below the 40% static threshold) |
| Growth (20%) | **100.0** (capped; Revenue 3yr CAGR 29.61% + documented TAM modifier, already at cap) |
| Balance Sheet (15%) | **100.0** (capped; Net Debt/EBITDA −0.34×, net cash) |
| Moat (15%) | **40.0** (2 of 5 signals cited true: market share, switching costs) |
| FCF Quality (10%) | **23.6** (TTM FCF/NI 54.16%) |

```
Quality Score = 40.0×0.25 + 85.4×0.15 + 100.0×0.20 + 100.0×0.15 + 40.0×0.15 + 23.6×0.10 = 66.2
```

**Quality Score = 66.2 / 100.0 — FAILS the 80.0+ gate**, on two independent grounds:
1. Weighted score 66.2 < 80.0.
2. **Hard disqualifier fires: "not FCF-positive for 3+ consecutive years"** (FY2022 and FY2023 both negative; only FY2024-FY2025 positive — 2 consecutive years, not 3). No carve-out is available for this specific hard disqualifier (unlike the FCF/NI-conversion check, which *is* carved out here on documented growth-capex grounds — ~42% of TTM operating cash flow is HBM4/EUV/P&T7 capacity capex, not discretionary spend).

This is the exact same root fact (FY2022/FY2023 FCF negative) that failed Phase 01's own binary "FCF positive 3 consecutive years" criterion on 06-20 — the Quality Score engine and the original gate agree completely on this name. No Composite Score computed (requires clearing the gate first).

## 5. Outcome

**Addendum appended** to the existing watchlist file — [watchlist/not-in-portfolio/HY9H/HY9H-2026-06-20.md](../watchlist/not-in-portfolio/HY9H/HY9H-2026-06-20.md) — as a dated 2026-07-09 section, not a new dated file, since no Rule 9 trigger changed the Phase 01 verdict. `watchlist/STALE.md` was not touched (HY9H isn't listed there, and this session doesn't change that). No `git` commands were run.

## Glossary

See [framework/glossary.md](../framework/glossary.md) for the standing definitions file. Terms used in this session (all already defined there): **ADR / ADS**, **BalanceSheet_Score**, **CAGR**, **Capital rotation**, **Dilutive (capital raise)**, **FCF/NI conversion ratio**, **GDR**, **HBM**, **Hard disqualifier**, **IPO**, **Moat**, **Net Debt/EBITDA**, **Quality Score**, **ROIC**, **Rule 0**, **Rule 9**, **TTM**.
