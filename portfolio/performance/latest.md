# Framework-account performance - as of 2026-10-12

Time-weighted return (TWR) of **U19421206 with RGL / LM8 / TLT removed from the whole history** ("Framework"), next to IBKR PortfolioAnalyst's own TWR ("Reported", which only neutralises the transfer day). Method: [portfolio/performance/README.md](README.md).

| Window | From (close) | To | Framework TWR | Reported TWR | Framework - Reported | Annualised | Max drawdown | Volatility (ann.) |
|--------|--------------|----|--------------:|-------------:|---------------------:|-----------:|-------------:|------------------:|
| 1D | 2026-10-09 | 2026-10-12 | **+0.03%** | +0.03% | +0.01% | n/a | +0.00% | n/a |
| 1W | 2026-10-05 | 2026-10-12 | **+1.31%** | +1.27% | +0.03% | n/a | -0.38% | n/a |
| MTD | 2026-09-30 | 2026-10-12 | **+2.86%** | +2.35% | +0.51% | n/a | -0.38% | n/a |
| 1M | 2026-09-11 | 2026-10-12 | **+3.98%** | +2.53% | +1.45% | n/a | -2.77% | 15.7% |
| 3M | 2026-07-10 | 2026-10-12 | **+15.78%** | +11.30% | +4.48% | n/a | -5.56% | 19.8% |
| 6M | 2026-04-10 | 2026-10-12 | **+31.57%** | +22.62% | +8.95% | n/a | -12.97% | 21.2% |
| YTD | 2025-12-31 | 2026-10-12 | **+8.54%** | +9.01% | -0.48% | n/a | -24.20% | 22.6% |
| 1Y * | 2025-10-13 | 2026-10-12 | **+26.47%** | +11.68% | +14.79% | +26.55% | -28.65% | 23.2% |
| Since start * | 2025-10-13 | 2026-10-12 | **+26.47%** | +11.68% | +14.79% | +26.55% | -28.65% | 23.2% |

`*` window starts at the first history date (2025-10-13), not the nominal calendar date.

Annualised is shown only for windows of ~1 year or more; volatility only for windows of 20+ trading days. Past returns are descriptive statistics, not a forecast or advice.

## Glossary

- **TWR (time-weighted return)**: A return measure that removes the effect of when money was deposited or withdrawn, by chaining each day's percentage change — the standard way to judge an investment process rather than the timing of your own deposits. IBKR PortfolioAnalyst reports it; this framework recomputes it without the transferred-out positions ([portfolio/performance/README.md](../../portfolio/performance/README.md)). *(New term.)*
- **Max drawdown**: The largest peak-to-trough fall of the cumulative return within a window — how bad the worst stretch was. *(New term.)*
- **NLV (Net Liquidation Value)**: A broker's headline value for an account: all positions at current market price, plus cash, minus any liabilities — the broker's own summary number, distinct from manually summing position values and cash yourself (the two can differ slightly due to settlement timing).
- **Excluded sleeve**: The positions removed from the framework statistics (RGL, LM8, TLT): their value, trades and income are subtracted from the account's history so the remaining numbers describe only what the framework governs. *(New term.)*
- **In-kind (free-of-payment) transfer**: Moving the actual shares from one of your own brokerage accounts to another without selling them, so cost basis and holding period carry over. IBKR's own reports may still show it as a close-out/realized loss on the sending account — cosmetic only. This framework treats it as a transfer, never a sale, exit, or trim (see [portfolio/accounts.md](../../portfolio/accounts.md)). *(New term.)*
- **Framework account**: The one IBKR account (`U19421206`) whose positions the Quality Value + Dynamic Trimming framework selects, sizes, scores, and trims — and the only account its sync/safe-guard commands read. The other two accounts (Investment Supremacy channel, Capitalization channel) are persisted in [portfolio/accounts.md](../../portfolio/accounts.md) but ungoverned. *(New term.)*
