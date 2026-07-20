# New Position Evaluation — AMD (Advanced Micro Devices, Inc.) — Re-evaluation

**Task type:** NEW POSITION
**Date:** 2026-07-20
**10Y US Treasury yield:** 4.57% (source: search aggregation of TradingEconomics/CNBC/FRED-tracking outlets, 2026-07-20)
**Trigger:** Telegram post (FinnInvestChannel, post 2961, ~16:05 UTC 2026-07-20) naming AMD in connection with its "Helios" rack-scale AI system launch and a Microsoft Azure deployment. Per Rule 0/CLAUDE.md, **the Telegram post text itself is never used as a financial input** — it is only the reason this ticker was looked at again. The underlying claim was independently re-verified via WebSearch/WebFetch this session (see §2) before any analysis proceeded.

AMD has a **prior watchlist entry**: [watchlist/not-in-portfolio/AMD/AMD-2026-06-30.md](../watchlist/not-in-portfolio/AMD/AMD-2026-06-30.md) — Phase 01 **FAILED** (Quality Score 55.7, gate is 80.0+), last checked 2026-07-05 with no change. AMD is **not a current holding** (confirmed against [portfolio/holdings.md](../portfolio/holdings.md)). That file's "Next review trigger" section explicitly lists *"cited, third-party evidence becoming available on AMD's AI-accelerator market share trajectory"* as a re-evaluation trigger — a named hyperscaler (Microsoft) confirming a flagship AI-infrastructure deployment is exactly that kind of evidence, warranting this full re-run rather than another "last checked" note.

---

## 1. Live Price (Rule 0)

Per [fair-value-methodology.md](../framework/fair-value-methodology.md) Rule 0, live price fetched first via Interactive-Brokers MCP tools, before any valuation work.

| Source | Value | Detail |
|---|---|---|
| **IBKR live snapshot** (contract_id 4391, NASDAQ) | **$517.86** | last trade |
| Day change (same snapshot) | **+4.46% (+$22.10)** on the day |
| 52-week range (IBKR `misc_statistics`) | low **$149.22** / high **$584.73** | Live price is below the 52-week high (made **after** the 06-30 session's recorded $562.99 high — the stock printed a fresh 52-week high of $584.73 at some point between 06-30 and today, then pulled back to today's $517.86, a −11.4% move off that high). This is a real price move but not itself a scoring input (Rule 0's price-inference ban) nor an independent trigger (no >15% single-day unexplained move; today's ±4.46% move is well inside that threshold and *is* fundamentally explained by the Helios/Azure news below). |

**Live price used throughout this session: $517.86.**

---

## 2. Re-verification of the Telegram Trigger — Microsoft/Azure "Helios" News

Independently confirmed via WebSearch/WebFetch (not taken from the Telegram post text):

- **What happened:** On **2026-07-20**, AMD launched "Helios," its first rack-scale AI system (72× AMD Instinct MI455X GPUs with >31TB HBM4 memory, 6th-gen AMD EPYC "Venice" CPUs, Pensando DPUs, and the ROCm software stack), and confirmed **Microsoft Azure as its first publicly announced customer**, with shipments targeted for **H2 2026**. Azure will use Helios for inference workloads (frontier models, Azure AI services, customer applications), add two new AMD-EPYC-CPU-powered VM series, and broaden Pensando DPU use in Azure's own networking. Other early Helios customers cited: Meta, OpenAI, Oracle.
- **Corroborating sources** (independent of the Telegram post and of each other): [CNBC, 2026-07-20](https://www.cnbc.com/2026/07/20/amd-helios-microsoft-ai-nvidia.html) ("AMD launches Helios, its first rack AI system to rival Nvidia, adding Microsoft as newest buyer"); [Manila Times/GlobeNewswire, 2026-07-20](https://www.manilatimes.net/2026/07/20/tmt-newswire/globenewswire/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership/2387672); [Blockonomi](https://blockonomi.com/amd-stock-surges-5-on-microsoft-azure-helios-ai-partnership-announcement/); [Invezz](https://invezz.com/news/2026/07/20/amd-stock-gets-a-big-boost-from-microsoft-ahead-of-ai-event/); [Windows News](https://windowsnews.ai/article/amds-helios-racks-land-in-azure-by-late-2026-heres-what-azure-ai-users-need-to-know-today.439649); [Stocktwits](https://stocktwits.com/news-articles/markets/equity/amd-microsoft-first-customer-helios-rack-ai-system-nvda-connection/cZZidowR7un). **Conclusion: this is genuine, dated (2026-07-20), multiply-corroborated news, not a fabrication or a stale repost.**
- **Q2 FY2026 earnings status:** AMD reports **Tuesday, August 4, 2026, after market close** ([StockTitan](https://www.stocktitan.net/news/AMD/amd-to-report-fiscal-second-quarter-2026-financial-uxy30dtkyyhk.html)) — **not yet reported** as of this session. So the last available quarterly filing remains Q1 FY2026 (10-Q, quarter ended March 28, 2026), the same filing the 06-30 session used. **No new quarterly financial statements exist to re-pull.**
- **SEC filing check since 06-30:** Confirmed via SEC EDGAR that AMD filed only two things since 06-30: (1) a **Form 10-K/A** (filed 2026-02-04, i.e. pre-dating 06-30 — a trivial correction of transposed Client-segment ASP/unit-shipment figures in the MD&A, explicitly stated to not otherwise "amend, update or change any other items or disclosures"); (2) a **Form 8-K dated 2026-07-01** disclosing routine annual **base-salary increases and equity-award grants** for five named executives (Su, Hu, Papermaster, Grasby, Norrod), effective July 1/August 15, 2026 — compensatory arrangements only, **no departure, election, or appointment of any officer/director**. Neither filing is a Rule 9 trigger (no earnings, no guidance revision, no management change, no M&A, no restated financials).

**Net effect:** the Phase 01 financial inputs (profitability, margins, growth, balance sheet, FCF quality) are **unchanged** from 06-30 — same TTM period, same underlying filings. The one substantively new thing this session has to work with is (a) the Helios/Azure news itself and (b) additional third-party market-share research surfaced this session that the 06-30 session did not have — both bear on the **Moat_Score**, re-assessed in full below.

---

## 3. Data Sources

- **SEC EDGAR primary filings** (CIK 0000002488): Form 10-K FY2025 (year ended Dec 27, 2025), Form 10-Q Q1 FY2026 (quarter ended Mar 28, 2026) and Q1 FY2025 comparative — same filings used 06-30, re-confirmed current (no restatement) via the SEC filing-history check above.
- **stockanalysis.com** — used this session as an independent cross-check against the 06-30 session's SEC-reconstructed figures (see §4 for the comparison; both land in the same range, confirming no material drift).
- **IBKR `get_company_themes`** (contract_id 4391) — AI/data-center thematic peer rankings, re-pulled this session.
- **Mercury Research / The Register / Tom's Hardware** — third-party x86 CPU market-share research, surfaced independently this session (originally located while researching a same-day INTC session) and cross-checked directly for this AMD evaluation — see Moat evidence table below.
- WebSearch for the Helios/Azure news corroboration and AMD's Q2 FY2026 earnings date (§2).

No required Phase 01 metric is missing or invented; every figure below has a cited source.

---

## 4. Phase 01 — Quality Score (Gate)

### Hard disqualifier check (fails regardless of weighted score)

| Hard disqualifier | Applies to AMD? | Basis |
|---|---|---|
| FCF/NI <70% for 2+ consecutive years, no growth-capex carve-out | No | TTM FCF/NI ≈ **174.7%** (stockanalysis.com TTM: FCF $8,574M ÷ Net Income $4,907M), consistent with the 06-30 session's SEC-reconstructed 171.2% TTM figure — both far above 70%. |
| Net Debt/EBITDA over threshold (2.5× standard / 4× asset-light) | No | Net **cash** position confirmed again this session: cash & equivalents $5,585M vs. total debt $3,871M (stockanalysis.com, latest balance sheet) — net cash, consistent with 06-30's finding. |
| Not FCF-positive for 3+ consecutive years | No | FCF positive FY23/FY24/FY25 (unchanged from 06-30) and TTM FCF $8,574M — still positive. |

**No hard disqualifier fires.**

### Weighted Quality Score

| Sub-score (weight) | Inputs | Calculation | Result |
|---|---|---|---|
| **Profitability** (25%) | Net Margin (TTM) 13.37% (SEC-reconstructed, normalized-tax basis, unchanged from 06-30; cross-checked against stockanalysis.com's un-normalized automated TTM figure of 13.10% — consistent, no material drift); ROIC (TTM, normalized-tax NOPAT basis) 6.71% (unchanged — same underlying filings, no new quarter; cross-checked against stockanalysis.com's un-normalized automated TTM ROIC of 7.75%, same ballpark) | NetMargin_Component = clamp((13.37/30)×100) = 44.57. ROIC_Component = clamp((6.71/30)×100) = 22.37. Avg = 33.47. No FCF-cap (FCF-positive 5/5 years) | **33.47** |
| **Margins** (15%) | Gross Margin (TTM) 50.28% — unchanged, exact match to stockanalysis.com's independently-fetched TTM figure this session | clamp((50.28/80)×100) = 62.85; no trend bonus (bonus only applies below 40%, AMD is already above) | **62.85** |
| **Growth** (20%) | Revenue 3yr CAGR (FY2022 $23,601M → FY2025 $34,639M) = 13.64% — unchanged; documented TAM-expansion evidence unchanged from 06-30 (Taiwan/UK AI investment, EPYC "Venice" ramp, Meta/Nutanix partnerships), **now further corroborated** by the new Microsoft/Azure Helios deployment (§2) as additional, independent TAM-expansion evidence — does not add a second +10 (the modifier is a flat cap, not cumulative per new evidence item), but strengthens the basis for the bonus already applied | Base = clamp((13.64/25)×100) = 54.56. +10 (cited TAM evidence, now with a stronger evidentiary base) = 64.56. No deceleration modifier (Data Center segment revenue accelerating: +32% FY24→FY25 per 10-K, +57% YoY in Q1 FY2026 per company earnings release) | **64.56** |
| **Balance Sheet** (15%) | Net cash position confirmed (see hard-disqualifier table); standard /4 denominator | Any net-cash position clamps to the formula's maximum regardless of exact magnitude: clamp(100×(1−(negative ratio)/4)) = 100 | **100.00** |
| **Moat** (15%) | See evidence table below — **1 of 5** signals now clear the cited-evidence bar (up from 0 of 5 on 06-30) | (1/5)×100 | **20.00** |
| **FCF Quality** (10%) | FCF/NI (TTM) ≈174.7% (stockanalysis.com), consistent with 06-30's 171.2% | clamp(((1.747−0.40)/0.60)×100) = clamp(224.5) | **100.00** |

### Moat signal evidence — full re-assessment (cited, per signal)

| Signal | Evidence found/re-checked this session | Verdict | Change vs. 06-30? |
|---|---|---|---|
| **Market share stable/growing** | **TRUE (new).** Two independent lines of evidence: **(1) AI-accelerator/GPU segment** — still weak: third-party estimates (SiliconAnalysts, commandlinux.com, tech-insider.org) put AMD at ~5-7% of the AI GPU/accelerator market vs. NVIDIA ~80% (same figure the 07-05 "last checked" note found; unchanged). Real, filed comparison for the same quarter: AMD's Data Center segment revenue grew **+57% YoY in Q1 FY2026** ($5.8B, per AMD's own Q1 FY2026 earnings release) vs. **NVIDIA's Data Center revenue growing +92% YoY in the directly comparable quarter** (Q1 FY2027, ended April 2026, $75.2B, per [NVIDIA's Q1 FY2027 press release](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000051/q1fy27pr.htm)) — NVIDIA is still growing *faster*, in both dollars and percentage, meaning AMD is **not yet closing the gap** in AI accelerators on filed results; the Helios/Azure win (§2) is real but ships H2 2026 and has not yet shown up in any reported revenue or share figure. **This segment alone would not clear the bar.** **(2) CPU segment (client + server x86)** — clears the bar: [Mercury Research Q1 2026 data](https://substack.com/@hypertechinvest/note/c-271783284) (corroborated by [The Register, 4 Jun 2026](https://www.theregister.com/systems/2026/06/04/amd-takes-a-third-of-server-cpu-market-as-shipments-grow/5251283)) shows AMD reaching a **record 32.6% overall x86 CPU market share** (Intel down to 67.4%, from 72.9% a year earlier) — a documented, multi-quarter, realized (not projected) share-gain trend from a named third-party research firm. In the higher-margin server segment specifically, [Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/amd-reaches-46-percent-of-server-x86-cpu-revenue-intel-still-controls-70-percent-of-the-consumer-pc-market-share) reports AMD's server x86 CPU *revenue* share reached **46.2%**. This is exactly the "cited share data (company filings, third-party market-share reports)" the framework's Moat methodology requires, for a real, substantial AMD product line (EPYC server CPUs feed directly into the Data Center segment alongside Instinct GPUs). **Verdict: TRUE, with the caveat clearly flagged that the picture is mixed — AMD is gaining real, documented share in x86 CPUs (client + server) while still trailing badly and not (yet) demonstrably gaining share in AI GPUs/accelerators specifically, the segment the Helios/Azure news pertains to.** | **TRUE** | **Changed FALSE → TRUE.** The 06-30 session only checked IBKR's AI-theme peer rankings (accelerator/data-center-specific) and found no supporting evidence; it did not pull CPU-market-share research. This session found genuinely new, cited, third-party evidence in a different (but real, material) AMD product segment. |
| **Brand premium** | No new evidence found this session. AMD's commercial positioning remains a price/performance challenger, not a premium-pricing brand; no documented instance of AMD raising prices without volume loss located. | **FALSE** | Unchanged |
| **Network effect** | No two-sided marketplace / user-growth-driven value mechanism applies to AMD's hardware business model. The Helios/ROCm software ecosystem could in principle develop network-effect dynamics (more developers → better tooling → more adoption), but no evidence of that dynamic actually operating was found or cited this session — noting it as a watch item, not crediting it without evidence. | **FALSE** | Unchanged |
| **Switching costs** | Re-examined in light of the Helios/Azure deal specifically: Azure committing to build two new dedicated AMD-EPYC-powered VM series and broadening Pensando DPU use in its own networking is genuine infrastructure integration depth, but — consistent with how the 06-30 session treated the Meta/Nutanix partnership announcements — this is still a **deployment/customer-win announcement**, not a documented switching-cost *mechanism* (no disclosed contractual lock-in terms, no migration-cost data, no evidence customers who evaluated switching away chose to stay). Applying the same evidentiary bar used elsewhere in this framework today (see the INTC session's identical treatment of the shared x86-ISA mechanism), a customer win alone — even a large, credible one — is not the same as documented lock-in. **Not credited.** | **FALSE** | Unchanged (reasoning re-examined, same conclusion) |
| **Scale cost advantage** | No cost-per-unit data vs. smaller competitors sourced this or last session. AMD remains fabless (TSMC-dependent, same foundry most competitors also use), so no manufacturing-scale edge is evidenced. | **FALSE** | Unchanged |

```
Quality Score = 33.47×0.25 + 62.85×0.15 + 64.56×0.20 + 100.00×0.15 + 20.00×0.15 + 100.00×0.10
              = 8.3675 + 9.4275 + 12.912 + 15.00 + 3.00 + 10.00
              = 58.7075  →  58.7 (rounded to nearest 0.1)
```

### Result: **Quality Score 58.7 — still fails the 80.0+ gate** (up from 55.7 on 06-30)

Per [quality-scoring.md](../framework/quality-scoring.md): a company must score 80.0+ to proceed to Phase 02. Accordingly, **no Rate Environment Gate, no Phase 02 valuation score, and no Composite Score were computed this session** — the same stopping point as 06-30.

**Why the score moved (55.7 → 58.7) but the outcome didn't:** the entire 3.0-point increase is attributable to the Moat sub-score improving from 0.0 to 20.0 (1 of 5 signals now clears the cited-evidence bar, on newly-surfaced x86 CPU market-share research — see above). Every other sub-score is unchanged, because no new AMD quarterly financial statements exist to move them (Q2 FY2026 reports August 4, 2026). Even crediting the Moat signal fully, the gap to 80.0 (21.3 points) is still large and structurally driven by the same two factors identified 06-30:
1. **ROIC (6.71% TTM)** — still well below the quality bar, still explained by the 2022 Xilinx acquisition's $41.5B of goodwill + intangibles inflating invested capital.
2. **Moat_Score (20.0/100, i.e. 1 of 5 signals)** — even with the CPU-share evidence now credited, AMD still lacks cited evidence for 4 of the 5 signals, most importantly in the AI-accelerator segment specifically (where the Helios/Azure news lives) — NVIDIA's Data Center revenue is still growing faster than AMD's on the latest comparable filed quarters (92% vs. 57% YoY), so the framework's strict, cited-evidence bar isn't yet cleared there.

This is not a verdict that the Helios/Azure news is unimportant — it is real, credible, multiply-corroborated evidence of a major hyperscaler win, and it is the single most positive AMD-specific data point either AMD session (06-30 or today) has found. But it is a **forward-looking design win** (ships H2 2026, no revenue yet) layered on top of an ROIC and moat-evidence base that remains structurally short of this framework's deliberately strict 80.0+ gate.

---

## 5. Recommendation

**PASS — do not open a position.** No Rate Environment Gate, no Phase 02 valuation score, no DCF/comparables fair-value work, no Upside/Downside Modifier, and no order setup — none of that work is meaningful for a name that fails the quality gate, consistent with 06-30.

Note for context only (not used as a scoring input): Forward PE sourced from stockanalysis.com this session at **56.08×** against a trailing PE of **165.32×** (both still reflecting the FY2025 tax-benefit earnings distortion noted 06-30) — directionally consistent with 06-30's 61.83×/179.90× (some compression, consistent with the stock trading below its recent 52-week high). Had AMD cleared the quality gate, a 5-year historical PE range/average still was not established this session (out of scope once Phase 01 failed) — the framework's **No-history fallback (FwdPE_Score = 50.0, neutral, flagged)** would apply if this were ever reached.

---

## 6. Portfolio Rebalancing Summary

N/A — not a holding, no position opened, nothing to rebalance.

---

## 7. Next Review Trigger

- **Routine re-screen:** still not scheduled — per [watchlist/README.md](../watchlist/README.md), "Phase 01 FAIL / not scored" entries don't carry a numeric Phase 02 score and so don't go stale on a methodology-version bump.
- **Rule 9 / fundamental triggers that would warrant another full look:**
  (a) **Q2 FY2026 earnings (August 4, 2026)** — the next real update to Profitability/Margins/Growth/Balance-Sheet/FCF-Quality sub-scores; also the first quarter that could show whether Data Center segment growth is closing the gap with NVIDIA's, or whether the Helios/Azure ramp is starting to show up in bookings/backlog commentary.
  (b) **AI-accelerator-specific market-share evidence** — this session's biggest open item. The CPU/x86 market-share signal is now credited, but the AI-GPU/accelerator segment specifically (where Helios/Azure lives) still shows AMD trailing badly on the latest filed comparison (57% vs. 92% YoY Data Center revenue growth). Re-check this specifically once Helios shipments begin (H2 2026) and any subsequent quarter's Data Center segment growth rate is reported — a rate closing on NVIDIA's, or a credible third-party AI-accelerator share estimate showing realized (not projected) AMD gains, would be the next swing factor.
  (c) A sustained ROIC improvement as the Xilinx-related goodwill/intangibles base amortizes (NOPAT growing faster than invested capital for 2+ consecutive years) — unchanged from 06-30, still not observed.
  (d) A management change or material M&A — none this session (the July 1 8-K was routine compensation only, not a departure/appointment).
  (e) A >15% unexplained single-day price move — today's ±4.46% (explained by the Helios news) does not qualify, nor did 06-30's +7.1%.
- Absent any of the above, future Telegram mentions of AMD should continue to be logged as "last checked, no change" rather than triggering a full re-evaluation each time — **unless** the mention specifically concerns Q2 FY2026 earnings, AI-accelerator market-share data, or a management/M&A event, any of which should trigger a fresh full run per (a)-(d) above.

---

## Glossary

- **8-K** — A US company's "current report" filed with the SEC to disclose a material event between its regular quarterly/annual filings.
- **ASP** — Average Selling Price — the average price a company sells a unit of its product for.
- **CAGR** — Compound Annual Growth Rate — the smoothed yearly growth rate that gets you from a start value to an end value over several years.
- **CapEx** — Capital Expenditure — money spent buying or upgrading physical assets (factories, equipment, data centers).
- **Composite Score** — `0.50×(100−Quality Score) + 0.50×Valuation Score` — combines quality and cheapness into one number, computed only for companies that clear the 80.0+ Quality Score gate. Not computed for AMD this session (gate still fails).
- **DPU (Data Processing Unit)** — A specialized processor (e.g. AMD's Pensando line) offloaded to handle networking, storage, and security tasks in a data center, freeing the main CPU/GPU from that work — part of the AMD Helios rack-scale system architecture referenced in this session.
- **EBIT / EBITDA** — Earnings Before Interest and Taxes / before Interest, Taxes, Depreciation & Amortization — operating-profit measures.
- **EPYC** — AMD's server/data-center CPU (central processing unit) product line — the "Venice" generation is the CPU component of AMD's new Helios rack-scale AI system.
- **EPS** — Earnings Per Share — net income divided by number of shares outstanding.
- **FCF** — Free Cash Flow — cash a business generates after running and maintaining itself, available to return to shareholders or reinvest.
- **FCF/NI conversion ratio** — Free Cash Flow ÷ Net Income — checks whether reported accounting profit is actually turning into real cash.
- **Forward PE** — Price ÷ next-twelve-months expected EPS — a forward-looking valuation multiple.
- **Goodwill / Intangible assets** — Goodwill is the premium paid above a target's net asset value in an acquisition (e.g. AMD's 2022 Xilinx deal); intangible assets include identifiable items like acquired technology and customer relationships. Both inflate a company's invested-capital base without adding tangible operating capacity, depressing ROIC.
- **GPU (Graphics Processing Unit)** — A processor originally built for rendering graphics, now the dominant chip type for AI training/inference workloads (AMD's "Instinct" line, NVIDIA's data-center GPUs) due to its ability to run many calculations in parallel.
- **Hard disqualifier** — One of three Quality Score conditions (FCF/NI conversion, Net Debt/EBITDA, FCF positivity) that fails a company regardless of its weighted Quality Score. None fire for AMD.
- **HBM (High-Bandwidth Memory)** — A premium, stacked-DRAM memory format used in AI accelerator GPUs — AMD's Helios system uses HBM4, the newest generation.
- **Helios** — AMD's first rack-scale AI system (announced 2026-07-20), combining Instinct MI455X GPUs, EPYC "Venice" CPUs, Pensando DPUs, and the ROCm software stack into one integrated product — the subject of the Microsoft Azure deployment news that triggered this session.
- **Hyperscaler** — An operator of very-large-scale, globally-distributed cloud/data-center infrastructure (e.g. Microsoft Azure, AWS, Google Cloud).
- **Instinct** — AMD's data-center AI accelerator GPU product line, positioned as a direct competitor to NVIDIA's data-center GPUs.
- **Invested Capital** — The total capital (debt + equity, minus cash) deployed in a business — the denominator of ROIC.
- **Moat** — Warren Buffett's term for a durable competitive advantage (brand, network effect, switching costs, scale) that protects a business's profits from competitors.
- **Net Debt/EBITDA** — Net debt (total debt minus cash) divided by EBITDA — a leverage ratio; negative means net cash. AMD remains net cash this session.
- **NOPAT** — Net Operating Profit After Tax — EBIT × (1 − effective tax rate) — the numerator used to compute ROIC.
- **Quality Score** — A 0–100.0 grade (0 = lowest quality, 100 = highest) blending profitability, margins, growth, balance sheet, moat, and FCF quality into one number; a company must score ≥80.0 to be eligible for Phase 02 valuation scoring at all. AMD scores 58.7 this session (up from 55.7).
- **ROCm** — AMD's open-source software stack for programming its GPUs for AI/HPC workloads — the AMD analog to NVIDIA's CUDA platform, and the software layer underpinning the Helios system.
- **ROIC** — Return on Invested Capital — how efficiently a company turns the capital invested in it (debt + equity) into profit; a core quality signal in this framework.
- **Rule 0** — This framework's standing instruction to always fetch a live, current price before any valuation work — never infer price from multiples or stale data.
- **Rule 9** — This framework's list of fundamental events that force an immediate re-valuation regardless of schedule: quarterly earnings, a guidance revision, a management change, material M&A, a macro shift, or a >15% stock-price move with no identified cause.
- **TAM** — Total Addressable Market — the total revenue opportunity available if a company captured 100% of its target market.
- **Treasury yield (10Y)** — The interest rate the US government pays on its 10-year bonds — the standard "risk-free rate" benchmark used throughout this framework's Rate Environment Gate (not actually invoked this session, since Phase 01 failed first).
- **TTM (Trailing Twelve Months)** — The most recent 12 months of reported financial results, as opposed to a fiscal-year or forward-looking figure.
- **VM (Virtual Machine)** — A software-based emulation of a physical computer, letting a cloud provider (e.g. Azure) run multiple isolated workloads on shared hardware; Azure's new AMD-EPYC-powered "VM series" referenced in this session are specific virtual-machine product offerings built on AMD hardware.
- **x86** — The dominant CPU instruction-set architecture used in most servers and PCs (as opposed to ARM); both Intel and AMD build x86-compatible chips, and the Mercury Research market-share data cited this session tracks share within this architecture family.
