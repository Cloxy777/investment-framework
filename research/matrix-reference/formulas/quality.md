# Quality score (Gate 1) — recovered formulas

Status legend: **Exact** = reproduces all 20 captured cards bit-for-bit (displayed rounding); **Fitted** = reproduces the sample but some constant/shape is inferred; **Hypothesis**; **Unknown**.
Reference code: `analysis/engine_replica.py` (`quality_from_card`, `discipline`, `flag_penalty_from_table`, `level_from`, run `python analysis/engine_replica.py`). Evidence: 20/20 cards for each of 8 components, penalty, score, level (data 2026-10-03, free tier).

## 0. Aggregation — Exact
```
score_raw = sum(8 components) - flag_penalty
score     = display_round_1dp(score_raw)            # Python float formatting '%.1f'; NOT decimal half-up
level     = A if score>=80, B if >=70, C if >=55 else D   # on the ROUNDED score
```
- Components are weight x fraction. Fractions are not integers: e.g. profitability 15x{1, .65, .35, 0}, EPS-growth 7x{1, .85, .60, .25, 0}. The displayed per-component value is rounded; the total uses unrounded values. Evidence: AAPL/ABNB/COST/UBER total 71.55/71.55/66.55/66.35 -> displayed 71.5/71.5/66.5/66.3 (binary float below .x5), META 72.75 -> 72.8 (exactly representable, half-even). If you round each component first you get 71.6 and fail 4/20 cards.
- A component can exceed its nominal maximum: Capital & SBC reaches **12 of 10** (MA, NFLX, V). No upper clamp; lower clamp 0 (TSLA raw -1 -> 0).
- Level caps applied after the score (see section 9). Level E exists only via rules (loss-making, SBC>=100 % of FCF, not understood); none in the free set.

## 1. Profitability (max 15) — Exact
`years_profitable` (SEC net income; "роки поспіль з прибутком"): >=5 -> 15 | >=2 -> 9.75 | 1 (profitable <2y) -> 5.25 | loss -> 0 | unknown -> 7.5. Config keys `quality.years_profitable.full=5`, `.partial=2`. (ABNB 4 years -> 9.75.)

## 2. Growth (max 20 = revenue 8 + EPS 7 + FCF 5) — Exact
Inputs: `revenue_growth_ntm`, `eps_growth_ntm` (the single "one EPS growth per card", consensus NTM; same value PEG uses), `fcf_growth_ntm` (**always unknown on the free data source: FMP has no FCF/OCF forecast**).
- revenue: <0 -> 0 | [0,10) -> 2.0 | [10,20) -> 4.8 | >=20 -> 8.0 | unknown -> 3.2 (=40 % of 8). Keys `quality.growth.revenue.weak=10 / .good=20`.
- EPS: <0 -> 0 | [0,10) -> 1.75 | [10,15) -> 4.2 | [15,25) -> 5.95 | >=25 -> 7.0 | unknown -> 2.8. Keys `eps.weak=10, .good=15, .great=25`.
- FCF: <0 -> 0 | [0,10) -> 1.2 | [10,15) -> 3.0 | >=15 -> 5.0 | unknown -> 2.0 (=`quality.unknown_weight` 0.40 x 5). All 20 cards currently take the unknown branch (+2.0).
Edge inclusivity: lower bound inclusive (card text "від X"); no card sits exactly on an edge (Hypothesis for ties).

## 3. Predictability (max 15) — Exact (lookup by registry tag)
`business_type` (registry, "оцінка Тараса/ШІ", dated 19.09.2026) -> points, config keys `quality.predictability_by_business_type.<type>`:
subscription 15 | payments_network 15 | data_ratings 15 | cloud_hyperscaler 14 (methodology: "cloud and contracts") | platform 12 | software 12 | retail_membership 10 (methodology: "club subscription") | advertising 9 | semis_monopoly 9 ("chips, lumpy sales") | brand_one_off 8 | rental 8 | manufacturer 6 | restaurant 6 | cyclical 3 | commodity 2 | bank 4 | pharma 3 | undefined 8. Types seen in sample: platform, software, manufacturer, cloud_hyperscaler, semis_monopoly, retail_membership, payments_network, advertising, subscription.
The assignment of the type to a company is registry data, not derivable.

## 4. Moat (max 15) — Exact
`moat` tag -> monopoly 15 | oligopoly 12 | network 12 | switching 10 | brand 8 | none 2 | unknown 6 (`quality.moat_points.*`) plus AI-risk adjustment (`ai_risk`: strengthens +2 | neutral 0 | unknown 0 | threat -3). All 20 cards have `ai_risk = unknown` (0). `market_share_trend` is also unknown (not live).

## 5. Margin (max 10) — Exact (3 special rules Fitted)
`m = min(net_margin, operating_margin_after_tax)` (both printed as fractions). Table (keys `quality.margin.*`): >=45 % -> 10 | [30,45) -> 8 | [20,30) -> 6 | [15,20) -> 4 | [10,15) -> 2 | <10 -> 0.
Modifiers (all seen on cards, texts quoted from "Пояснення"):
1. trend `down` ("маржа падає: мінус") -> -2, floor 0 (META 29.8 % -> 4, V 48.3 % -> 8). [Exact]
2. software rule of 40: if `business_type == software` and `revenue_growth_ntm + FCF_ttm/revenue_ltm >= 40 %` -> full 10 points (ADBE, CRM, PLTR). [Fitted: type restriction; FCF-margin uses card's TTM FCF over LTM revenue]
3. platform low-margin-growing: `trend == up` and `business_type == platform` and bucket <5 -> 5 ("не менше половини ваги") (UBER 9.6 % -> 5). [Hypothesis on the set of types; only platform observed]
Unknown margin -> 5.

## 6. Balance sheet (max 10) — Exact
`net_cash > 0` -> 10 | else `debt_to_EBITDA` <=1.5 -> 7 | <=3.0 -> 4 | >3.0 -> 1 | unknown -> 5 (keys `quality.debt_to_ebitda.ok=1.5, .tolerable=3`). Net cash is judged first (AMZN: net cash negative, 0.1x -> 7).

## 7. Capital & SBC (nominal max 10, observed 0..12) — Fitted, 20/20 exact
```
capital = max(0, S + R + H + B)
S  (SBC/FCF, or SBC/revenue when FCF-based ratio is unavailable/negative):
     < 5 %  -> 8 | [5,15) -> 7 | [15,30) -> 5 | >=30 -> 3 | unknown -> 5.5
     (thresholds keys quality.sbc_to_fcf.ideal=5, .ok=15, .minus=30; for AMZN and META the card switches to the revenue basis with
      red_flags.thresholds.sbc_revenue_{major,critical,hard} = 5/10/20 % as the bucket edges)
R  (ROIC):   >=30 -> +2 | [20,30) -> +1 | [10,20) -> 0 | <10 -> -2 | unknown -> 0       (keys quality.roic.excellent=30 .good=20 .weak=10)
H  (diluted share-count change, 1Y): <=0 -> +1 | (0,2) -> 0 | >=2 -> -1 | unknown 0   (key quality.dilution_max=2)
B  (capital return): buy-back yield "high" -> +1 | low buy-back -> 0 | dividend only -> -1 | neither -> -2
```
Derivation: methodology sub-score tables (SBC 6/5/3/1, ROIC 8/7/6/4, shares 7/6/5) are the same numbers shifted: S = table+2, R = table-6, H = table-6, i.e. `capital = (SBC_pts + ROIC_pts + share_pts) - 10 + B`, which is why a perfect company gets 11 (+1 buy-back bonus = 12).
Open: the "high buy-back" threshold lies between 1.7 % (AAPL, low) and 3.2 % (V, high) of market cap; replica uses 2 %. The S bucket edges are printed per card in the bucket text; AMZN/META use the revenue-basis edges (fits both). B_div/B_none are single-observation values (TSM; AMZN+TSLA).

## 8. Discipline (max 5) — Exact
`growth_source`: organic 5 | mixed 4 | acquisitions 2 | unknown 4 (when capex is covered by OCF). Then external capex financing (debt + issuance > 25 % of capex, `red_flags.capex_waiver.max_external_financing_to_capex`): if net cash > 0 and debt/EBITDA <= 1.5 (`max_debt_to_ebitda`) -> -1 ("1 of 2 points") else -2 ("0 of 2" and **cap B** on level, flag w/o penalty) (AMZN organic 5-2 = 3; GOOG/META/TSLA 5-1 = 4; ORCL mixed 4-2 = 2). No capex numbers (TSM): points by registry tag `capex_funding` (ocf 5 | unknown 4 | debt 3 for organic). Evidence: 20/20.

## 9. Flag penalty and level caps — Exact on 20 cards
Penalty = sum over flag rows: critical 8, serious 4, minor 0 — EXCEPT 0 when the card marks the row:
- "уже пораховано у складовій балу" (fact already graded in a component): SBC eats revenue, share dilution, external capex financing, debt >1.5x EBITDA, growth on promises, margin squeeze (+ opex outgrows revenue, AI risk by methodology text);
- "та сама подія, що в сусідньому прапорці": capex > OCF when FCF-negative-streak is present;
- price flags ("штрафу немає"): expensive without growth, multiple above ceiling, multiple beyond reason, value trap;
- minor flags.
Rows that did bite in the sample: FCF negative several quarters (critical, 8, "обмежує рівень"), customer concentration 2-3 clients (critical, 8), revenue up while earnings+margin not (critical, 8), dividend from debt (serious 4), customer concentration (serious 4), revenue from one country (serious 4), company misses own guidance (serious 4), profit from investment revaluation (serious 4).
Level caps observed: unreviewed-by-Taras (header lacks "Тарас переглянув") -> max B ("стеля: рівень не вище B: Тарас цю компанію не переглядав", ADBE 81.0 -> B); any quality-critical flag -> max C; external-capex-lands-on-balance-sheet -> max B. Price-category critical flags (PLTR "multiple beyond reason") do NOT cap.

## 10. Open / Unknown
- Which flags exist beyond the 22 seen, and their numeric thresholds (see flags-catalogue.md).
- Level E triggers on live data (no E company in the free set); hysteresis (needs previous-day state; the cards print "гістерезис" notes only for lenses in this sample).
- Normalised-EPS tax rule is applied inside `eps_growth_ntm` (ABNB text: "нормалізований EPS 4,46 проти 4,19 (+6,4 %)"); the normalisation arithmetic is not reproduced (the final growth is taken as a displayed input).

---
# UPDATE 2026-10-03 (paid tier, 487 cards, all baskets): additional rules and final status
Run `python analysis/run_all_cards.py` (output saved in `analysis/run_all_cards.out.txt`). Result: each of the 8 components **488/488 exact** (predictability and moat 456/456 where classified), flag penalty **488/488**, score **488/488**, level 477/488 (11 misses explained below).

## New rules found on the larger sample
1. **Unclassified company** (registry has no business type / moat): predictability and moat show `виключено, класифікації немає`; the sum line reads `складові разом X (без прогнозованості і моату, нормовано на відомі ваги)`; **score = (sum of known components) x 100 / (sum of known weights)** (ACGL: 48 / 70 x 100 = 68.6), then minus flag penalty, floor 0. 32 cards. Completeness loses the gap weights (data-completeness.md).
2. **Moat**: `market_share_trend == down` -> **-4** ("частка ринку падає: мінус": BA oligopoly 12->8, INTC unknown 6->2, NVO/SBUX brand 8->4); `ai_risk == negative` -> -3 (network 12 -> 9); moat tag `absent` = 2; floor 0.
3. **Discipline**: growth source `m&a` = 2; `unknown` = 4. With no OCF/capex numbers the registry funding tag moves the base: `ocf` 0, `unknown` **-1**, `debt` -2 (CRH mixed 4 -> 3). If capex > OCF and the waiver fails ("виняток для capex не пройдено: 0 балів") -> **-2** (GRAB unknown 4 -> 2). External financing > 25 % of capex: -1 / -2 as before.
4. **Margin, order of operations** (fixed on 488 cards): (a) bucket table on min(net, operating-after-tax); (b) **software rule of 40** -> 10, applies when the card's basket is `software` (registry basket, not business type: ADSK is type `subscription`) and `LTM revenue growth + LTM FCF margin >= 40 %` where LTM revenue growth = sum of last 4 quarters vs previous 4 (quarterly table), FCF margin = FCF_TTM / LTM revenue (14/14 software cards separate perfectly: applied >= 41.5, not applied <= 38.7; the NTM growth does **not** work); (c) **operating leverage bonus** ("важіль масштабу: маржа росте, бонус", also worded "для цього типу бізнесу низька маржа, що росте, дає не менше половини ваги"): trend `up` and bucket < 5 and business type in {platform, subscription, software} -> 5; (d) trend `down` -> **-2** (floor 0), applied last (PANW: rule of 40 gives 10, then falling -2 = 8).
5. **Level E** (verdict AVOID, shown even with a high score): fires when `years_profitable == 0` (loss-making) **or** SBC/FCF >= 100 % (ARM 110 %, CBOE 129 %, HOOD 160 %, HIMS 250 %, P 304 %, SWKS 118 %). 10 further E cards (AEP, BMY, CEG, NEE, SKM, VST, GEV, JPM, LMN, VIST) have neither trigger: they come from the registry tag "бізнес незрозумілий" (not derivable; utilities, pharma, telecom, banks). Header line `рівень E: збиткова, SBC з'їдає FCF або бізнес незрозумілий` is printed on such cards.
6. **Level caps seen** (card text): not reviewed by Taras -> max B (5 cards); AI-classified moat not confirmed by Taras -> A needs confirmed moat (`класифікація ШІ, Тарас цю компанію не переглядав: рівень A вимагає моату, підтвердженого Тарасом`, 4 cards, e.g. ANET); critical flags -> max C (ADYEN.AS, FICO); **level hysteresis**: `стеля: гістерезис: бал 54,2 у смузі 2,0 бала під порогом 55 (53,0), рівень C лишається з попередньої картки` (LHX): a score within 2 points below a threshold keeps the previous level. The only stateful level case in the sample.
7. **Flag penalty, same event**: `виручка росте, а маржа і FCF ні` is not penalised when `виручка росте, а прибутки і маржа ні` is present (GPN, MO) - only one 8-point penalty per event; `capex більший за операційний кеш` with a negative-FCF flag likewise.
8. Component label variants: revenue growth input is labelled `ріст виручки на 12 місяців` or `ріст виручки за 12 місяців` (parser must match by prefix).

## Remaining unexplained in quality
11 level mismatches (10 registry-E + 1 hysteresis); none in components/penalty/score.
