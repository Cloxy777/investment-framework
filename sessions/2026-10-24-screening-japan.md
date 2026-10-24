# 2026-10-24 — SCREENING: Japan (JP) — Round 6 (fresh candidate pool)

**Task type:** SCREENING (Phase 01) — rotation slice [JP](../framework/screening-coverage-log.md). Picked per the rotation rule: oldest "Last screened" date (JP 2026-09-26, ahead of NA-2 09-29, APAC-ex-JP 10-06, NA-1 10-10, EM 10-17, EU 10-20). Unattended scheduled run (Routine, first-Saturday monthly slice).

## 0. Methodology and flags

- **Step 0:** no user available → unattended exception. As in prior JP rounds, a fresh pool was built by structural triage from domain knowledge (not ETF holdings, which would resurface already-covered large caps). **Flag: this approach is not an exhaustive screen** and can miss names.
- **EODHD (Path A) not used.** The prompt referenced `EODHD_API_KEY`; a test call to `/fundamentals` returned **403** (free plan), and EODHD was removed from the framework on 2026-06-19 ([decision](../decisions/2026-06-19-remove-eodhd-switch-to-yfinance.md)). Same stale-prompt precedent as earlier JP rounds.
- **Data source:** `python -m scripts.fetch_fundamentals` fails with `MissingInputError` (no TTM "EBIT" row; two tickers also lack `marketCap`) on **all 10 candidates** — the same systemic yfinance gap as 2026-09-26. Fallback: the same yfinance, **annual statements, latest fiscal year (FY basis, not TTM)**, computed with an ad-hoc script. Basis notes: Revenue CAGR = latest FY vs 3 FY earlier; ROIC = EBIT × (1 − 30% assumed tax) ÷ yfinance "Invested Capital" (tax rate is an **assumption**, ROIC therefore approximate); EV = market cap + total debt − cash & ST investments; FCF yield = latest FY FCF ÷ current market cap. Figures are FY-based and not directly comparable to earlier stockanalysis.com rounds.
- **Not run:** 4921.T Fancl and 7518.T Net One Systems — yfinance returned no statements/market cap → **data gap, not scored, not estimated**.

## Step 1 — Pool and structural triage

Fresh 10 names (none previously screened in JP): 6200 Insource, 3984 User Local, 6465 Hoshizaki, 7729 Tokyo Seimitsu, 6988 Nitto Denko, 4921 Fancl, 6526 Socionext, 9746 TKC, 4661 Oriental Land, 7518 Net One Systems. No structural exclusions (pool hand-picked to avoid excluded categories).

## Step 2 — Quantitative gate (yfinance annual, latest FY)

| Company | FY end | Gross M | Net M | ROIC* | Rev 3y CAGR | FCF last 3 FY | ND/EBITDA | FCF yield | EV/EBIT | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **Insource (6200.T)** | 2025-09 | 76.9% ✅ | 28.5% ✅ | 33.5% ✅ | 15.5% ✅ | ✅✅✅ | −1.33× ✅ | 7.56% ✅ | 8.2× ✅ | **PASS 8/8** |
| **User Local (3984.T)** | 2026-06 | 89.0% ✅ | 30.6% ✅ | 16.3% ✅ (narrow) | 17.6% ✅ | ✅✅✅ | −4.30× ✅ | 9.13% ✅ | 6.4× ✅ | **PASS 8/8** |
| Hoshizaki (6465.T) | 2025-12 | 37.3% ❌ | 7.9% ❌ | 10.2% ❌ | 14.8% ✅ | ✅ | −2.35× ✅ | 2.57% ❌ | 10.1× ✅ | FAIL 4/8 |
| Tokyo Seimitsu (7729.T) | 2026-03 | 41.3% ✅ | 14.8% ✅ | 11.4% ❌ | 4.4% ❌ | ❌ (neg. FY23/FY24) | −0.98× ✅ | 2.12% ❌ | 17.7× ✅ | FAIL 4/8 |
| Nitto Denko (6988.T) | 2026-03 | 38.0% ❌ | 13.0% ✅ | 11.4% ❌ | 3.4% ❌ | ✅ | −2.03× ✅ | 4.74% ✅ | 10.6× ✅ | FAIL 4/8 |
| Socionext (6526.T) | 2026-03 | 44.7% ✅ | 4.4% ❌ | 6.5% ❌ | 1.4% ❌ | ❌ | −1.52× ✅ | −4.94% ❌ | 21.3× ❌ | FAIL 2/8 |
| TKC (9746.T) | 2025-09 | 67.8% ✅ | 14.5% ✅ | 10.8% ❌ | 7.2% ❌ | ✅ | −1.73× ✅ | 4.14% ✅ | 10.7× ✅ | FAIL 6/8 (ROIC, CAGR 0.84pp) |
| Oriental Land (4661.T) | 2026-03 | 38.7% ❌ | 17.3% ✅ | 8.5% ❌ | 13.4% ✅ | ✅ | −1.13× ✅ | 1.82% ❌ | 29.6× ❌ | FAIL 4/8 |

*ROIC uses an assumed 30% tax rate (see §0). TKC is a 2-filter miss; no single-filter near-misses this round.

## Qualified Quality List — 2 new names (pending `/new-position`)

Both are net-cash, high-margin, asset-light Japanese service/software businesses. **Not valuation-scored.**

## Step 3 — Qualitative pass (2 names, handled directly — below batch threshold)

Sourcing is limited to one web search per name plus the quantitative data; items I could not source are marked and left for `/new-position`.

### Insource (6200.T) — corporate training (on-site training, open seminars, IT services)
1. **Why margins high?** Training is delivered through a large library of standardized, reusable courses and a contracted-instructor model, so incremental sessions are very profitable (76.9% gross). Cause of the premium (pricing power vs. scale) — *not verified*.
2. **Competing:** moderate barrier — course library, enterprise client relationships, instructor network; low capital need means competitors can enter. *Moat looks moderate, not hard.*
3. **Capital allocation:** net cash (ND/EBITDA −1.33×); FCF rose from ¥1.3bn (FY23) to ¥4.3bn (FY25). Dividend/buyback history *not sourced*.
4. **Growth:** company reports 9-month FY25 growth of On-Site +10.8%, Open Seminars +8.4%, IT +4.8%; DX/generative-AI training demand running 116–150% of prior year ([Insource IR, July 2026](https://www.insource.co.jp/resource/pdf/ir/__ie_26072108.pdf)).
5. **Bear case:** 1Q FY25 operating profit −4.0% on course-capacity/DX-plan shortfalls; sales per client fell in 1H; growth is slowing from 15.5% CAGR toward ~7–11%; Japanese labour tightness/instructor supply ([Insource IR, Jan 2026](https://www.insource.co.jp/resource/pdf/ir/__ie_26012604.pdf)).
6. **Disruption:** generative-AI self-learning could erode instructor-led training; the company currently sells AI-themed courses, but this is a live risk. **Verdict: PASS with FLAG (decelerating profit, AI-disruption).**

### User Local (3984.T) — AI/data analytics SaaS (website analytics, AI chatbot/text mining)
1. **Why margins high?** Software subscriptions at 89% gross margin; scale/pricing power split *not verified*.
2. **Competing:** moderate — many analytics/chatbot rivals globally; switching costs and Japanese-language specialization are plausible but *not verified*.
3. **Capital allocation:** net cash (ND/EBITDA −4.30×, equity ratio 84.5% per [edinetdb](https://edinetdb.jp/company/3984), secondary source); payout history *not sourced*.
4. **Growth:** not sourced beyond 17.6% FY revenue CAGR; the FY2026 filing ([TSE tanshin, 2026-08-06](https://www2.jpx.co.jp/disc/39840/081220260806511812_tse-anedjpsm-39840-20260806339840-ixbrl.htm)) wasn't readable here. **Data gap — read it in `/new-position`.**
5. **Bear case:** small (market cap ~¥24bn); ROIC buffer only 1.27pp and sensitive to my assumed tax rate; large AI platforms (LLM vendors) could commoditize chatbot/analytics products.
6. **Disruption:** high — foundation-model platforms are a direct substitute vector. **Verdict: PASS with FLAG (thin ROIC buffer, small cap, AI-substitution, qualitative gaps).**

## Step 4 — Data gaps (none estimated)

- 4921.T Fancl and 7518.T Net One Systems: no yfinance statements/market cap → unscored.
- All metrics are latest-FY, not TTM (wrapper failed); ROIC uses assumed 30% tax.
- User Local: growth drivers and capital-return history not sourced; the secondary-source revenue (¥5.3bn) was not reconciled to yfinance and may be quarterly/non-consolidated — verify.
- Insource: dividend/buyback history and the stated FY26 ¥20bn sales target (low-reliability source) not verified.
- Search results sources: [FilingReader](https://filingreader.com/news-wire/tokyo/2025-07-22/insource-reports-record-growth-driven-by-digital-training).

## Next steps

`/new-position 6200.T` and `/new-position 3984.T` (confirm with live prices, TTM data and filings). Remaining untested JP ideas: Fancl, Net One Systems (retry when yfinance has data).

## Glossary

- **Phase 01 / quality gate** — the 8 quantitative filters a company must pass before valuation scoring ([strategy.md](../framework/strategy.md)).
- **Gross / Net margin** — the share of revenue left after direct costs / after all costs.
- **ROIC** — return on invested capital: profit earned on the money tied up in the business.
- **Revenue 3yr CAGR** — compound annual revenue growth over three years.
- **FCF (free cash flow) / FCF yield** — cash left after capex; yield = FCF ÷ market cap.
- **Net Debt/EBITDA** — debt minus cash relative to operating cash earnings; negative = net cash.
- **EV/EBIT** — enterprise value (market cap + debt − cash) ÷ operating profit; a valuation multiple.
- **Moat** — durable competitive advantage.
- **TTM** — trailing twelve months. **FY** — fiscal year.
- **Near-miss** — fails exactly one filter.
