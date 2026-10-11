# Price (Gate 2): five lenses, regime bonus, price word — recovered formulas

Reference code: `engine_replica.py` (`lens_scores`, `price_check`, `price_word`, `verdict_check`). Evidence: 20 cards; every lens mismatch is explained by a printed hysteresis note (see 6).
Common inputs printed on every card: S&P 500 forward P/E **20.1** and S&P 500 EPS growth **+13.6 % (index, 2027)** (as of 03.10.2026; both are config/daily constants, source "FactSet Earnings Insight" per the old banner; no source/date printed on the card now). Good-yield threshold **4 %** ("рішення Тараса", no link to treasury yield).

## 1. Basis and the one EPS growth — Exact (as displayed inputs)
All 20 cards use basis NTM P/E (`NTM P/E = price / NTM EPS`; NTM EPS is "sum of 4 quarterly consensus forecasts" when quarterly estimates exist). `eps_growth` for PEG, growth lens, growth score and price word is the **single printed "ріст EPS +x % (для PEG, 24 міс.)"** (geometric mean of two steps; the normalised-base rule for tax one-offs is applied before). The card prints the analyst count of that number (e.g. ABNB 9). It is used as an input here (its internal computation from FY consensus is not reproduced).

## 2. Lenses (each -2..+2) — Exact (20/20 incl. hysteresis exceptions)
| Lens | Rule |
|---|---|
| PEG | `peg = NTM_PE / eps_growth_pct`. `<0.5 -> +2`; `<1.0 -> +1`; `<=1.3 -> 0`; `<=2.0 -> -1`; else `-2`. growth <= 0 -> PEG "не рахується: ріст відʼємний" and lens **-2** (CRM). Cycle-peak companies (card line "Можливий пік циклу…") cap this lens at **+1** (NVDA 0.35, AMD 0.52). |
| FCF yield after SBC | `y = 1/P_FCF x (1 - SBC/FCF)` trailing (TTM FCF and SBC from SEC). `>=4 % -> +2`, `>=3 -> +1`, `>=2 -> 0`, `>=1 -> -1`, `<1 -> -2` (negative -> -2). No FCF data (TSM, currency problem TWD) -> 0 and "немає". |
| vs S&P 500 | `r = NTM_PE / 20.1`. `r<=1.0 -> +1` only for levels A and B (else 0); `r<=1.3 -> 0`; `r<=2.0 -> -1`; else -2. Evidence: AAPL r=1.74 -> -1; COST r=2.01 -> -2; UBER (level C) r=0.82 -> 0. |
| vs own history | `cur` = today's trailing P/E, `mean3` = trailing 3-year mean, `min5`, `max3` from the monthly trailing-P/E series. `cur <= min5 x 1.05 -> +2`; `cur >= max3 x 0.95 -> -2`; `cur < 0.90 mean3 -> +1`; `cur > 1.10 mean3 -> -1`; else 0 (band +-10 %, **not** "any deviation"). If the series has fewer than 36 monthly points (GOOG: 28 points since 31.07.2024) the result is clamped to +-1 (GOOG +2 -> +1). No history (TSM, V) -> 0. Forward (NTM) history is not yet available ("10 днів знімків із 365 потрібних"), so trailing is used. |
| Growth vs market | `g >= 1.5 x 13.6 (=20.4) -> +1`; `g < 0.9 x 13.6 (=12.24) -> -1`; else 0. (ORCL 20.3 -> 0, GOOG 22.6 -> +1.) Index growth missing -> 13. |

## 3. Sum and regime bonus — Exact
`sum = PEG + FCF + S&P + history + growth` then `+1` if **market cap >= $200 B and NTM P/E <= 20 and level in {A,B}** (NVDA, NFLX). Level D/C companies never get it (ORCL, 410 B, P/E 16.7, D -> none). The lens chart shows 5 bars + "Сума".

## 4. Hysteresis — Exact observation, mechanism Unknown
Notes printed: "гістерезис: бал лінз «X» лишився з попередньої картки, вхід у смузі 5 % біля порога" for ABNB (S&P ratio 1.308 vs 1.3 -> stays 0), GOOG (PEG 1.05 stays +1 although >1.0), NVDA (history), V (FCF yield 3.0 % stays 0 instead of +1). All 4 residuals of the replica are exactly these. The lens keeps the previous day's score while the value is within 5 % of the threshold (band relative to the threshold). Needs previous state to replicate; a stateless implementation will disagree on such days.

## 5. Price word — Exact
```
if no multiple                      -> NO_MULTIPLE
if NTM_PE <= 15 and score < 60 and eps_growth < 10   -> VALUE_TRAP
if lens_sum >= 4                    -> CHEAP
if lens_sum >= 1                    -> FAIR
else: need = 14 (level A) or 15 (others)
      if eps_growth >= need         -> EXPENSIVE_GROWING
      elif base_CAGR_5y < need      -> EXPENSIVE_NO_GROWTH       (otherwise EXPENSIVE_GROWING with a note)
```
Evidence: META (sum -5, growth 9.3 %, base CAGR 16.5 >= 15) is "дорого, але росте"; AAPL (sum -5, growth 9.8, base CAGR 7.7) is "дорого без росту"; UBER (sum 0, growth 3.2, base CAGR 18.8) "але росте"; CRM (sum 0, growth -2.7, CAGR 7.1) "без росту".
Price flags (no penalty, never cap): `multiple_ceiling` (multiple > 30 and PEG not justifying: AAPL 35, COST 40), `multiple_absurd` (> 60: PLTR 91, TSLA 165), "дорого без росту".

## 6. Display facts
Lens table columns: lens | value | compared with | score; chart "Лінзи ціни: від -2 до +2" with the sum; start-page scatter x-axis = lens sum (range about -6..+8; max = 5x2 +1 regime = 11 theoretically).

---
# UPDATE 2026-10-03 (paid tier, 487 cards)
- **Lens evaluation: 2 435 lens scores, 45 mismatches; 43 of them carry a printed hysteresis note** ("гістерезис: бал лінз «X» лишився з попередньої картки, вхід у смузі 5 % біля порога") and every one lies within 5 % of a threshold (verified numerically for PEG, S&P ratio and FCF yield: max relative distance 0.049); 2 unexplained (CRWD and PANW own-history lens: replica 0 / +2, card -1 / -2). 44 cards print at least one hysteresis note. Hysteresis = the previous day's lens score is kept while the value is inside the 5 % band of the threshold; stateless replica error is ~1.8 %.
- **FCF yield recomputed from unrounded inputs**: `(FCF_TTM x (1 - SBC/FCF)) / market cap` matches the sign/bucket where the displayed one-decimal value sits exactly on a threshold (CSGP "+1,0 %" scores -2, SPOT "+3,0 %" scores 0, i.e. real values 0.97 / 2.97).
- **Cycle-peak cap on PEG applies only to "possible cycle peak" (trailing EPS growth > 100 %)**; a loss-to-profit turnaround note ("вихід зі збитку в прибуток", SNDK) does not cap PEG (+2 kept).
- **Multiple ceiling in the price word**: NTM P/E >= 30 and EPS growth < 30 % -> never CHEAP/FAIR whatever the lens sum (FIX 31.4 / 29.3 %, TPL 32.9 / 27.4 %) -> goes to the expensive branch.
- **Value trap word**: replica rule `P/E <= 15 and score < 60 and EPS growth < 10` fits 256/261 words but five cards disagree (AIG, CLX, OXY shown "дорого без росту" although they satisfy it; GPN and MET shown trap with growth >= 10 %). The card flag `вартісна пастка` ("Мультиплікатор X низький, але прибутки падають на Y %") does not decide the word (CTSH/DVN/UPS carry it but are FAIR). Status: Hypothesis (about 96 %); hidden state/hysteresis suspected.
- Word accuracy on displayed inputs: price word 454/467 (97.2 %).
