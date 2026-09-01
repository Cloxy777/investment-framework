# 2026-09-01 — SCREENING: Japan (JP) — Round 4 (fresh candidate pool)

**Task type:** SCREENING (Phase 01) — rotation-matrix slice [JP](../framework/screening-coverage-log.md) (Japan, all sectors). Selected per the rotation rule: oldest "Last screened" date in the matrix (2026-08-11, ahead of NA-2 08-15, NA-1 08-18, APAC-ex-JP 08-22, EM 08-25, EU 08-29).

This was run as an **unattended scheduled routine** (Routine 4, twice-weekly universe screening slice — see [automation-schedule.md](../framework/automation-schedule.md)) with no interactive user present.

The three prior JP sessions ([2026-06-30](2026-06-30-screening-japan.md), [2026-07-21](2026-07-21-screening-japan.md), [2026-08-11](2026-08-11-screening-japan.md)) together screened 46 names and closed out three full rounds of candidate pools. This session builds a **fresh 16-name candidate pool** from sectors not yet covered in JP (gaming/entertainment IP beyond what's already tested, SaaS/no-code collaboration software, scientific/analytical instruments, healthcare-data platforms and diagnostics, fintech-adjacent credit guarantee, fashion e-commerce, management consulting) rather than re-testing already-screened names.

---

## 0. Methodology and a stale-instruction flag

- **The scheduled task prompt for this run again referenced the deprecated `EODHD_API_KEY`-based "Path A" automation and a "monthly" cadence.** Both are stale: the actual configured cadence per [automation-schedule.md](../framework/automation-schedule.md) Routine 4 is **twice-weekly (Tuesday and Saturday)**, not monthly — today (2026-09-01) is a Tuesday, consistent with the real cadence. EODHD was removed from the framework on 2026-06-19 ([decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)), which instructs treating that exact credential as **compromised** if it's ever needed again. Per CLAUDE.md, `framework/` (the current, canonical [screen.md](../.claude/commands/screen.md)) is the source of truth over a stored prompt — this is the fifth consecutive JP-adjacent session flagging this identical stale-prompt situation (06-30, 07-21, 08-04 EM, 08-11, now this one). `EODHD_API_KEY` was **not used**.
- **Step 0/1**: no interactive TIKR/Koyfin screener session was available (unattended run) — went straight to the documented unattended-session exception. Continued the same **structural-triage-from-domain-knowledge** approach the three prior JP rounds used, built around sectors not yet tested in this slice, rather than the ETF-holdings fallback (which would just resurface the same large-cap names already covered in Round 1, most already in MOAT/QUAL/QGRW/IQLT). **Flagging prominently per the task's Step 0 instruction: this manual/structural-triage sourcing approach — like the ETF-holdings fallback it substitutes for — has the same fundamental limitation of missing small/mid-cap names that a live TIKR/Koyfin screener export would surface systematically; it is not a substitute for that screener access.**
- **Step 2 data source**: `yfinance` was tested first (`pip install yfinance` succeeded) but failed immediately with `yfinance.exceptions.YFRateLimitError: Too Many Requests` on the cookie/crumb endpoint for a test ticker (7203.T) — a genuine 429, the same failure mode as every JP session since 07-21. Switched to `stockanalysis.com` (via WebFetch: `/financials/ratios/`, `/financials/`, `/financials/cash-flow-statement/` pages per ticker, exchange code `tyo` confirmed against a live fetch), the same fallback used in every JP/EU/NA/APAC/EM session since 07-07.
- **Two WebFetch-summarization arithmetic errors caught and corrected this session** (see Data gaps section below for full detail): Nexon's 3-year revenue CAGR and Nihon Kohden's "3 consecutive positive FCF years" check were both mis-stated by the fetch tool's own summarization and independently recomputed from the raw sourced figures before scoring. This is a new, material finding for this slice's data-quality history — prior sessions flagged *labeling*/sign artifacts on stockanalysis.com pages, but this is the first time the WebFetch summarization layer's own arithmetic (not the source page) has been shown to be wrong on a pass/fail-determining figure.

### Structurally excluded (Step 1, before any quantitative pull)

| Ticker | Company | Why excluded |
|---|---|---|
| 9766.T | Konami Group | Diversified conglomerate blending high-margin Digital Entertainment IP (Yu-Gi-Oh, Metal Gear) with capital-intensive Sports/fitness-club operations and regulated casino/pachislot gaming-machine manufacturing — same blended-segment exclusion logic used for Sony Group/Panasonic Holdings in the 2026-08-11 JP session |

### Candidate pool this round (15 names, after the above exclusion)

| Ticker | Company | Sector |
|---|---|---|
| 9697.T | Capcom Co | Video games IP |
| 3659.T | Nexon Co | Video games IP |
| 4776.T | Cybozu Inc | SaaS collaboration/no-code software |
| 2492.T | Infomart Corp | B2B EDI/SaaS platform |
| 7701.T | Shimadzu Corp | Analytical/scientific instruments |
| 6856.T | Horiba Ltd | Precision measurement instruments |
| 6965.T | Hamamatsu Photonics | Photonics/optical sensors |
| 7164.T | Zenkoku Hosho Co | Rent/credit guarantee (asset-light fintech-adjacent) |
| 4483.T | JMDC Inc | Healthcare-data platform |
| 4544.T | H.U. Group Holdings | Diagnostics/clinical laboratory testing |
| 4587.T | PeptiDream Inc | Peptide drug-discovery platform (biotech) |
| 7564.T | Workman Co | Workwear retail (franchise-heavy format) |
| 3092.T | ZOZO Inc | Fashion e-commerce platform |
| 6532.T | BayCurrent Consulting | Management/IT consulting |
| 6849.T | Nihon Kohden Corp | Medical electronic equipment (patient monitors) |

---

## Step 2 — Quantitative Phase 01 gate (real, sourced data — stockanalysis.com, pulled 2026-09-01)

Filters: Gross margin >40% · Net margin >12% · ROIC>15% · Revenue growth >8% (3yr CAGR) · FCF positive 3 consecutive years · Net Debt/EBITDA <2.5x · FCF yield >4% · EV/EBIT <20x. The **current/TTM** column was used as the primary basis for margin/ROIC/leverage/valuation figures, consistent with the framework's TTM convention. **All 3-year revenue CAGRs were independently recomputed in Python from the raw annual revenue figures sourced from each ticker's `/financials/` page**, rather than trusting the WebFetch tool's own stated CAGR — see the Nexon finding below for why.

| Company (Ticker) | Gross M | Net M | ROIC | Rev 3yr CAGR | FCF 3yr+ | Net Debt/EBITDA | FCF yield (TTM) | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| Capcom Co (9697.T) | 58.11% ✅ | 30.19% ✅ | 52.68% ✅ | 15.76% ✅ | ✅ (5 yrs) | -1.66× ✅ | 2.45% ❌ | 18.01× ✅ | **FAIL — FCF yield only (7/8)** ⚠️ near-miss |
| **Nexon Co (3659.T)** | 60.10% ✅ | 26.35% ✅ | 34.22% ✅ | 10.33% ✅ ⚠️ recomputed | ✅ (5 yrs) | -5.58× ✅ | 4.50% ✅ | 13.64× ✅ | **PASS — 8/8** ✅ |
| **Cybozu Inc (4776.T)** | 90.12% ✅ | 19.07% ✅ | 80.76% ✅ ⚠️ very high | 19.26% ✅ | ✅ (3 consec.) | -0.63× ✅ | 5.21% ✅ | 12.39× ✅ | **PASS — 8/8** ✅ |
| Infomart Corp (2492.T) | 74.13% ✅ | 11.33% ❌ (narrow) | 19.88% ✅ | 19.58% ✅ | ✅ (5 yrs) | -3.24× ✅ | 2.20% ❌ | 43.63× ❌ | **FAIL — 5/8** |
| Shimadzu Corp (7701.T) | 44.87% ✅ | 11.50% ❌ (narrow) | 13.31% ❌ (narrow) | 5.16% ❌ | ✅ (3 consec.) | -1.49× ✅ | 3.39% ❌ | 13.58× ✅ | **FAIL — 4/8** |
| Horiba Ltd (6856.T) | 44.09% ✅ | 11.82% ❌ (narrow) | 17.38% ✅ | 7.23% ❌ (narrow) | ✅ (6 yrs) | -1.41× ✅ | 3.13% ❌ | 14.23× ✅ | **FAIL — 5/8** |
| Hamamatsu Photonics (6965.T) | 47.88% ✅ | 7.50% ❌ | 4.54% ❌ | 0.52% ❌ | ✅ (3 consec., declining) | -0.21× ✅ | 1.64% ❌ | 32.55× ❌ | **FAIL — 3/8** |
| Zenkoku Hosho Co (7164.T) | 100.00% ✅ ⚠️ business-model artifact | 56.05% ✅ | 17.42% ✅ | 5.33% ❌ | ✅ (4 yrs) | -1.90× ✅ | 7.68% ✅ | 8.33× ✅ | **FAIL — Rev CAGR only (7/8)** ⚠️ near-miss |
| JMDC Inc (4483.T) | 55.28% ✅ | 13.24% ✅ | 7.01% ❌ | 21.97% ✅ | ❌ (FY24 negative breaks streak) | 1.43× ✅ | 3.84% ❌ (narrow) | 22.89× ❌ | **FAIL — 4/8** |
| H.U. Group Holdings (4544.T) | 29.02% ❌ | 3.86% ❌ | 3.09% ❌ | -1.76% ❌ (declining) | ✅ (3 consec.) | 0.57× ✅ | 10.54% ✅ | 39.01× ❌ | **FAIL — 4/8** |
| PeptiDream Inc (4587.T) | 43.34% ✅ | -18.88% ❌ | -11.99% ❌ | -21.34% ❌ (declining) | ❌ (FY25 negative) | 2.81× ❌ | -3.82% ❌ | N/A ❌ (neg. earnings) | **FAIL — 1/8** |
| Workman Co (7564.T) | 38.11% ❌ (narrow) | 13.20% ✅ | 30.91% ✅ | 7.83% ❌ (narrow) | ✅ (5 yrs) | -2.46× ✅ ⚠️ data gap on "current" | 2.16% ❌ | 12.98× ✅ | **FAIL — 5/8** |
| ZOZO Inc (3092.T) | 93.16% ✅ | 21.02% ✅ | 70.43% ✅ | 7.58% ❌ (narrow) | ✅ (5 yrs) | -0.22× ✅ | 4.62% ✅ | 14.46× ✅ | **FAIL — Rev CAGR only (7/8)** ⚠️ near-miss |
| BayCurrent Consulting (6532.T) | 57.26% ✅ | 24.94% ✅ | 78.50% ✅ | 65.07% ✅ ⚠️ reconciled | ✅ (3 yrs) | -1.08× ✅ | 3.03% ❌ | 21.46× ❌ (narrow) | **FAIL — 6/8** (valuation only) |
| Nihon Kohden Corp (6849.T) | 51.99% ✅ | 5.86% ❌ | 7.16% ❌ | 4.40% ❌ | ✅ (3 consec.) ⚠️ recomputed | -1.25× ✅ | 7.17% ✅ | 14.03× ✅ | **FAIL — 5/8** |

---

## ✅ Qualified Quality List — 2 new names

### Nexon Co (3659.T) — passes 8/8

Japan-headquartered (Tokyo-listed, primary market since its 2011 IPO), South Korean-founded global live-service game publisher — owner of long-running franchise IP MapleStory (22 years) and Dungeon&Fighter (~20 years), plus newer hits including The First Descendant and the 2025-launched extraction shooter ARC Raiders (via its 2018 acquisition of Embark Studios). Clears every filter cleanly.

### Cybozu Inc (4776.T) — passes 8/8

Japanese enterprise SaaS vendor best known for **kintone**, a no-code/low-code business-application-building platform for SME back-office workflows, alongside legacy products cybozu Office and Garoon dating to the late 1990s. Clears every filter cleanly, with an unusually high ROIC (80.76% current) flagged below for context, consistent with the very-high-ROIC pattern already seen in other asset-light Japanese SaaS names this slice (Rakus, en Japan in prior rounds).

### Near-misses flagged for the watchlist (fail only 1 filter)

- **ZOZO Inc (3092.T)** — passes 7/8, the **tightest miss of this round**: fails only Revenue 3yr CAGR (7.58% vs. the >8% bar, a 0.42pp miss). Dominant Japanese fashion e-commerce platform (93.16% gross margin, 21.02% net margin, 70.43% ROIC, net-cash balance sheet, 4.62% FCF yield, 14.46× EV/EBIT). Worth an immediate re-check next JP rotation — a marginal acceleration would clear the bar.
- **Capcom Co (9697.T)** — passes 7/8: fails only FCF yield (2.45% vs. >4%). Exceptional margins (58.11% gross, 30.19% net), 52.68% ROIC, 15.76% revenue CAGR, net-cash balance sheet, cheap 18.01× EV/EBIT — quality is unambiguous, priced too richly on a cash-flow basis right now (game-industry capex/development-spend cycle can swing FCF year to year — see FY2025 FCF of ¥61.8B vs. TTM ¥44.4B in the raw data).
- **Zenkoku Hosho Co (7164.T)** — passes 7/8: fails only Revenue 3yr CAGR (5.33% vs. >8%, a 2.67pp miss — wider than ZOZO's/Capcom's but still the only failing filter). Rent/credit guarantee company (asset-light, fee-based guarantee model) with 56.05% net margin, 17.42% ROIC, net-cash balance sheet, 7.68% FCF yield, and a cheap 8.33× EV/EBIT — the cheapest valuation multiple of any name in this round's pool. Its "100.00% gross margin" is a business-model artifact (a fee-based guarantee company has no COGS in the traditional sense), not a data error — flagged for context, doesn't change the >40% PASS call.

No other candidate came within 1 filter of qualifying. Two names — **Workman Co (7564.T)** and **BayCurrent Consulting (6532.T)** — are worth a standing note even though each has 2-3 simultaneous misses (not single-filter near-misses by this framework's definition): Workman's Revenue CAGR miss (7.83% vs. 8%) is the single tightest individual-filter gap of the entire round at just 0.17pp, alongside a narrow Gross Margin miss (38.11% vs. 40%) — franchise-royalty-model workwear retailer, worth re-checking if a future print nudges growth over the bar. BayCurrent Consulting fails only on valuation (FCF yield 3.03%, EV/EBIT 21.46× — both narrow) despite exceptional quality metrics (78.50% ROIC, 65.07% revenue CAGR reconciled from FY2023) — the same "quality is real, valuation gate is the blocker" pattern already flagged for Keyence/Advantest/Disco/Tokyo Electron/Sanrio/Rakus across prior JP rounds.

---

## Step 3 — Qualitative pass (Nexon and Cybozu, the 2 clean PASSes)

Both handled directly (2 names, within the "small batch, no subagent needed" threshold per [new-position.md](../.claude/commands/new-position.md)'s batch-processing policy referenced in [screen.md](../.claude/commands/screen.md) Step 3).

### Nexon Co (3659.T)

1. **Why are margins high?** Live-service, free-to-play monetization: once a game is built, additional revenue from in-game virtual-item/cosmetic sales carries very high incremental margin, and Nexon's two flagship legacy franchises (MapleStory, 22 years old; Dungeon&Fighter, ~20 years old) continue generating large recurring revenue on a largely amortized development base — real operating leverage, not a lucky one-off cycle.
2. **What would it take to compete?** A rival needs a hit live-service franchise with an entrenched player community and years of monetization/content tuning behind it — game development is high-risk (most titles fail to reach scale), and Nexon's owned-IP catalog plus its 2025 hit ARC Raiders (via the 2018 Embark Studios acquisition) diversifies its hit-dependency somewhat versus a single-franchise competitor.
3. **Capital allocation (5-10yr):** Committed to returning >33% of prior-year operating income via semi-annual dividends and buybacks, targeting a minimum 10% ROE (aspiring to 15% mid-to-long-term); paid a special ¥324B dividend in 2026 on record MapleStory/ARC Raiders results, bringing cumulative shareholder returns since its 2011 IPO to over ¥900B by end-2026. Also running a multi-year "IP Growth Initiative" (vertical growth in existing franchises + horizontal new-IP creation) and continuing to fund studio acquisitions (Embark Studios).
4. **Where's growth coming from (3-5yr)?** Continued monetization of MapleStory (record 2026 quarters) and ARC Raiders' 2025-launch momentum; management has explicitly framed MapleStory's multi-decade extension as a "blueprint" for growing Dungeon&Fighter similarly, plus continued horizontal expansion into new IP/genres.
5. **Best bear case:** Heavy revenue concentration in a handful of blockbuster live-service titles — MapleStory and Dungeon&Fighter together have historically driven the bulk of revenue — and new-IP execution risk is real and recent: Nexon's own CEO described The First Descendant's player-retention problems as requiring "structural changes," not a patch. Both flagship franchises are 20+ years old, and live-service "content treadmill" games face real long-run content-fatigue risk; loot-box/gacha-style monetization also carries an ongoing regulatory overhang across Korea/China/EU.
6. **Disruption vector:** Moderate. Live-service gaming as a category is durable, and owning IP outright (vs. licensing) gives Nexon more control than a pure licensee, but game-industry hit-dependency means today's blockbuster franchise isn't guaranteed to still be the blockbuster in 5 years without continued reinvestment and successful new-IP execution (The First Descendant is the live counter-example) — an industry-inherent risk worth ongoing pipeline monitoring, not a company-specific red flag.

**Sources:** [Nexon Q2 2026 slides — special dividend](https://www.investing.com/news/company-news/nexon-q2-2026-slides-maplestory-record-324b-special-dividend-93CH-4857169), [Nexon 2026 Capital Markets Briefing](https://www.businesswire.com/news/home/20260331340550/en/Nexon-Presents-Transformation-Plan-at-Its-2026-Capital-Markets-Briefing), [Massively Overpowered — Q2 2026 special dividend](https://massivelyop.com/2026/08/14/nexon-q2-2026-maplestory-and-arc-raiders-made-so-much-money-that-nexon-paid-out-a-special-dividend/)

**Conclusion:** A genuine quality business (dominant owned-IP live-service portfolio, exceptional margins/ROIC, net-cash balance sheet) trading at a reasonable 13.64× EV/EBIT. **Recommend `/new-position Nexon` (3659.T)** for full Phase 02 scoring with live pricing.

### Cybozu Inc (4776.T)

1. **Why are margins high?** kintone is a subscription SaaS no-code/low-code platform — marginal cost of serving an additional customer/seat is low (mostly hosting infrastructure), giving the 90%+ gross margin typical of cloud software with minimal COGS.
2. **What would it take to compete?** A rival needs to replicate kintone's flexible no-code app-building depth plus Cybozu's decades of trust with Japanese SMEs (its legacy cybozu Office/Garoon products date to the late 1990s) and its now-expanding Southeast Asia partner-channel network; once an SME's core workflow/database tooling is embedded in kintone-built custom apps, switching carries real data-migration and retraining costs.
3. **Capital allocation (5-10yr):** Reinvesting into Southeast Asia expansion (a $6.4M investment establishing a Malaysia HQ for the region, per its March/August 2026 disclosures), continued product development (Kintone AI Lab, a partnership with Sarawak Digital Economy Corporation), and guiding to ¥42.17B in full-year sales — a growth-reinvestment posture rather than heavy capital return, consistent with its net-cash balance sheet.
4. **Where's growth coming from (3-5yr)?** Southeast Asia (Thailand +300% YoY subscriber growth, Malaysia customer count +160% in H1 2026, region-wide subscribers +13.4%), continued domestic SME digital-transformation demand (Kintone segment revenue +33.9% YoY in 2025), and new AI-native features layered onto the core no-code platform.
5. **Best bear case:** Growth is now meaningfully levered to unproven Southeast Asian markets where Cybozu is building brand/channel from scratch against better-capitalized global competitors (Microsoft Power Apps, Salesforce) and entrenched local players; domestically, the addressable market of Japanese SMEs needing this specific tool is finite and could saturate. The unusually high ROIC (80.76% current, above even Rakus's and en Japan's prior-round figures) reflects a genuinely asset-light model but also means a large share of value depends on defending a premium subscription price against a proliferating field of low-code/no-code alternatives, including tools hyperscalers bundle for free/cheap alongside their core cloud offerings.
6. **Disruption vector:** Moderate-to-low near-term — kintone's flexible, SME-workflow-specific no-code model is itself relatively disruption-resistant against one-size-fits-all ERP vendors — but AI-native "describe your app in natural language and it builds itself" tooling is an emerging category that could eventually commoditize part of the no-code value proposition Cybozu currently monetizes. Cybozu's own Kintone AI Lab initiative suggests management is investing to stay ahead of this shift rather than ignoring it, which is a mitigant but not a guarantee.

**Sources:** [Cybozu Southeast Asia 2026 strategy — Kintone press center](https://www.kintone.com/en-oceania/press-center/japans-cybozu-inc-to-focus-on-southeast-asia-growth-for-2026/), [Cybozu Malaysia expansion — Dealroom](https://app.dealroom.co/news/feed/cybozu-invests-6-4m-in-malaysia-expansion-as-kintone-revenue-jumps-33-9-to-138-72m), [Cybozu Southeast Asia funding — Technode Global](https://technode.global/2026/08/27/cybozu-funds-southeast-asia-expansion-kintone-customer-growth-malaysia/)

**Conclusion:** A genuine quality business (dominant Japanese no-code SME platform, exceptional margins/ROIC, net-cash balance sheet, credible new growth vector in Southeast Asia) trading at a reasonable 12.39× EV/EBIT. **Recommend `/new-position Cybozu` (4776.T)** for full Phase 02 scoring with live pricing — and treat the 80.76% ROIC as a figure to sanity-check again at that stage given how far outside typical ranges it sits (genuinely sourced, not a data error, but worth a second look).

---

## Data gaps flagged (per CLAUDE.md Rule 0 — none estimated)

- **Nexon (3659.T) — WebFetch summarization arithmetic error, material to the pass/fail call.** The fetch tool's own summary stated a 3-year revenue CAGR of "7.90%" (which would have been a narrow *fail*) from the same raw revenue figures (¥353,714M FY2022 → ¥475,102M FY2025) it had correctly sourced. Independently recomputing `(475102/353714)^(1/3) - 1` in Python gives **10.33%**, a clear pass. Used the recomputed figure, not the tool's stated one — the raw sourced revenue numbers themselves were correct, only the tool's own arithmetic on top of them was wrong. Flagging this as a new data-quality risk category for this slice: prior sessions caught stockanalysis.com *page*-level artifacts (sign/labeling); this is the first time the WebFetch summarization layer's own math has needed correction. **Recommend independently recomputing every CAGR from raw sourced figures going forward, rather than trusting a WebFetch-stated CAGR, for all future screening sessions** (already done for every name in this session's table).
- **Nihon Kohden (6849.T) — same category of error, non-material to the verdict.** The fetch tool stated the company "does not meet the criterion of 3 consecutive positive years" because it looked back to FY2023 (negative), but the filter only requires *any* 3 consecutive positive years, and FY2024/FY2025/FY2026 were all positive (¥11,981M / ¥8,160M / ¥15,328M) — corrected to a PASS on this filter. Nihon Kohden fails independently on Net Margin, ROIC, and Revenue CAGR regardless, so this correction doesn't change the overall FAIL verdict, but is recorded for the same "verify FCF-streak logic independently" reason as the Nexon finding above.
- **BayCurrent Consulting (6532.T) — revenue history fiscal-year mislabeling, reconciled rather than left as a gap.** The `/financials/` page's revenue table skipped from FY2024 straight to a row labeled "FY 2020" (¥32,978M) with no FY2021-FY2023 rows shown. Cross-checking against the page's own stated FY2024 revenue-growth rate (184.76%) shows ¥93,909M ÷ 2.8476 = ¥32,978M exactly — i.e., the ¥32,978M figure is mathematically FY2023's revenue, mislabeled "FY 2020" by the page (or by the WebFetch extraction of it). Used ¥32,978M as FY2023 revenue for the 3yr CAGR calc (yielding 65.07%, comfortably clearing the >8% bar either way this resolves) rather than leaving the filter unscored, since the reconciliation is arithmetically exact and consistent with the same-page growth-rate figure — flagged rather than silently substituted.
- **Workman Co (7564.T)**: Net Debt/EBITDA showed "—" (blank) for the "current" period specifically, while FY2026 (-2.46×), FY2025 (-2.86×), and FY2024 (-2.56×) were all populated and consistently net-cash. Used the FY2026 figure as the most recent known value rather than leaving the filter unscored — Workman fails independently on Gross Margin, Revenue CAGR, and FCF Yield regardless, so this gap doesn't change the verdict.
- **JMDC Inc (4483.T)**: FY2024 FCF (-¥910M) is a single-year dip bracketed by positive FY2023 (¥3,240M) and FY2025 (¥12,566M) — breaks the "3 consecutive positive years" filter on any 3-year window tested. Not a data gap (all years are populated, sourced figures), just a genuine FAIL on this filter — noted here for completeness since it's a narrower miss than the multi-filter fails elsewhere in the pool.
- **Zenkoku Hosho Co (7164.T)**: "100.00%" Gross Margin across every period shown is a business-model artifact (a fee-based rent/credit-guarantee company has no traditional cost-of-goods-sold line), not a data error or a rounding coincidence — flagged for analyst context but the >40% PASS call is correct and unaffected.
- **PeptiDream Inc (4587.T)**: EV/EBIT showed "—" (blank/N/A) for the current and FY2025 periods, consistent with the company's negative EBIT/net income in those periods — not estimated or backfilled; treated as a FAIL on this filter per the framework's "don't invent a multiple off negative earnings" convention, though PeptiDream fails independently on 6 of the other 7 filters regardless.

---

## Next steps

- **Two `/new-position` candidates from this rotation: `/new-position Nexon` (3659.T) and `/new-position Cybozu` (4776.T)** — full Phase 02 valuation scoring with live pricing for both; re-verify Cybozu's 80.76% ROIC from a primary source as part of that pull, per the qualitative-pass flag above.
- Watchlist (no formal entry created by `/screen`; re-check on next JP rotation or a fresher print): **ZOZO (3092.T)** — the tightest miss this round, Revenue 3yr CAGR only (7.58% vs. >8%, 0.42pp short); **Capcom (9697.T)** — FCF yield only (2.45% vs. >4%); **Zenkoku Hosho (7164.T)** — Revenue 3yr CAGR only (5.33% vs. >8%).
- Standing note carried forward: Japan's highest-quality asset-light franchises across all four JP rounds so far (Keyence, Advantest, Disco, Tokyo Electron from Round 1; Sanrio, Rakus from Round 3; now **BayCurrent Consulting** from this round) keep clearing quality/growth filters comfortably but fail specifically on valuation (FCF yield, EV/EBIT) — worth a standing watch for a future rotation if multiples compress.
- **New standing process note for future screening sessions of any slice, not just JP:** independently recompute every multi-year CAGR and "N consecutive positive years" check from the raw sourced figures rather than trusting a WebFetch tool's own stated summary math — this session caught one case (Nexon) where trusting the tool's arithmetic would have produced a false FAIL on an otherwise-qualifying name. Worth raising with the framework owner as a possible addition to the yfinance/stockanalysis.com methodology notes in [valuation-scoring.md](../framework/valuation-scoring.md).
- Deferred for a future JP deep-dive (not yet screened in any of the 4 rounds): further gaming names (Nexon/Capcom now tested; Nintendo, Square Enix, Bandai Namco already tested in prior rounds — remaining: smaller publishers), Japan's broader medtech/diagnostics field beyond Chugai/Sysmex/Terumo/Nihon Kohden/H.U. Group now tested, and smaller-cap SaaS/software names beyond Rakus/SHIFT/Obic/Cybozu/Infomart now tested (e.g. freee once sustainably profitable, Works Human Intelligence, Sansan).
- **Process flag for the automation owner:** the scheduled Routine 4 prompt still references a monthly cadence and the deprecated EODHD `Path A` automation, despite the actual configured cadence being twice-weekly (Tuesday/Saturday) per `automation-schedule.md`. This is the fifth consecutive JP-adjacent session flagging this same stale-prompt issue — recommend updating the scheduler's stored prompt text directly rather than continuing to re-flag it per run.
- Coverage log updated below.

---

## Glossary

- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **EBIT** — Earnings Before Interest and Taxes — operating profit, before the effects of debt financing and tax rate.
- **EBITDA** — Earnings Before Interest, Taxes, Depreciation, and Amortization — a rough proxy for cash operating profit.
- **EV** — Enterprise Value — a company's total value to all capital providers: market cap + debt − cash.
- **EV/EBIT** — Enterprise Value divided by EBIT — a multiple used to compare how expensive companies are relative to their operating profit, independent of capital structure.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF Yield** — Free Cash Flow ÷ Market Cap (or Enterprise Value) — how much free cash a company throws off relative to its price; higher is cheaper.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio measuring how many years of operating cash profit it would take to pay off all debt; this framework's primary balance-sheet-risk gate.
- **No-code / low-code (software)** — A category of software platform (like Cybozu's kintone) that lets non-programmers build business applications through visual/drag-and-drop tools instead of writing traditional code, lowering the cost and time to build custom internal tools.
- **pp (percentage points)** — A direct difference between two percentages, distinct from a "%" change.
- **Qualified Quality List** — The output of Phase 01 screening — the set of companies that passed the quality gate and are eligible for valuation scoring.
- **ROE** — Return on Equity — Net Income ÷ shareholder equity; how efficiently a company generates profit from shareholders' capital.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to never invent or estimate financial data — if a metric is missing, flag it and stop rather than infer it; also covers always fetching a live price before valuation work.
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
