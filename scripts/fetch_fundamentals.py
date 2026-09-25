#!/usr/bin/env python3
"""Data-fetch wrapper for Phase 01/02/04 fundamentals — Stage 2 of scripts/TOKEN-OPTIMIZATION-PLAN.md.

Wraps the yfinance logic documented in framework/valuation-scoring.md's "Screening Tools"
section (verified working 2026-06-14 / 2026-06-20) so it isn't hand-retyped every session.

Usage:
    python -m scripts.fetch_fundamentals MSFT
    python -m scripts.fetch_fundamentals MSFT --json

Output fields (map onto scripts/scoring/quality_score.py and valuation_score.py's JSON
input schemas — see their module docstrings; qualitative/manual fields like moat evidence,
TAM evidence, fair values, and the Rate Gate 10Y input are NOT produced here, Claude's job):

    fcf_yield_pct, ev_ebit, forward_pe
    pe_mode ("range" | "none"), pe_5yr_avg, pe_5yr_low, pe_5yr_high, pe_5yr_quarters_used
    fcf_ni_ttm_pct, fcf_ni_annual_pct (oldest fiscal year first)
    fcf_positive_3yr_or_more
    roic_pct, net_margin_pct, gross_margin_pct, revenue_cagr_3yr_pct
    net_debt_to_ebitda
    shares_outstanding, market_cap, enterprise_value

Known documentation drift (flagged per Stage 2 instructions, not silently adapted): the
"Screening Tools" section says "`t.info['ebit']`/`enterpriseValue` give EV/EBIT directly."
As of yfinance 0.2.66, `t.info["ebit"]` returns None for MSFT (verified 2026-09-25) — the field
was apparently removed/renamed upstream. This script uses `t.financials.loc["EBIT"]` /
`t.quarterly_financials.loc["EBIT"]` instead, which yfinance 0.2.66 still populates. Flagged in
the PR description; framework/valuation-scoring.md should be corrected separately.

Hard requirement: every required field is validated non-None/non-NaN before use. If yfinance
returns nothing, or 5yr PE history has fewer than 20 usable quarters, this script raises
MissingInputError / prints the no-history flag rather than defaulting, zero-filling, or
computing over a shorter undisclosed window. Never invent or estimate financial data.
"""

from __future__ import annotations

import argparse
import json
import sys

import pandas as pd

from scripts.scoring.common import MissingInputError

PE_HISTORY_QUARTERS = 20


def _row(df: "pd.DataFrame", name: str, context: str) -> "pd.Series":
    if name not in df.index:
        raise MissingInputError(f"yfinance field missing from {context}: row '{name}' not found")
    return df.loc[name]


def _value(series: "pd.Series", idx: int, context: str):
    if idx >= len(series):
        raise MissingInputError(f"{context}: fewer than {idx + 1} periods of history available")
    value = series.iloc[idx]
    if value is None or pd.isna(value):
        raise MissingInputError(f"{context}: value at period index {idx} is missing/NaN")
    return float(value)


def _info_value(info: dict, key: str, context: str) -> float:
    value = info.get(key)
    if value is None:
        raise MissingInputError(f"yfinance info field missing: '{key}' ({context})")
    return float(value)


def _ttm_sum(quarterly_df: "pd.DataFrame", row_name: str, context: str) -> float:
    series = _row(quarterly_df, row_name, context)
    if len(series) < 4:
        raise MissingInputError(
            f"{context}: need 4 quarters to compute TTM '{row_name}', only {len(series)} available"
        )
    window = series.iloc[:4]
    if window.isna().any():
        raise MissingInputError(f"{context}: NaN found in trailing 4 quarters of '{row_name}'")
    return float(window.sum())


def _fcf_ni_annual(financials: "pd.DataFrame", cashflow: "pd.DataFrame") -> list[float]:
    ni_series = _row(financials, "Net Income", "annual FCF/NI conversion")
    fcf_series = _row(cashflow, "Free Cash Flow", "annual FCF/NI conversion")
    n = min(len(ni_series), len(fcf_series))
    if n < 2:
        raise MissingInputError(
            "Need at least 2 fiscal years of Net Income and Free Cash Flow to compute the "
            f"FCF/NI conversion history, only {n} available"
        )
    ratios = []
    # yfinance annual columns are most-recent-first; the framework's hard-disqualifier check
    # and worked examples list years oldest-first, so reverse before returning.
    for i in range(n):
        ni = ni_series.iloc[i]
        fcf = fcf_series.iloc[i]
        if ni is None or pd.isna(ni) or fcf is None or pd.isna(fcf):
            continue
        if ni == 0:
            raise MissingInputError(
                f"Fiscal year at annual-column index {i} has Net Income of 0 — FCF/NI ratio undefined"
            )
        ratios.append(fcf / ni * 100)
    if len(ratios) < 2:
        raise MissingInputError("Fewer than 2 fiscal years had usable (non-NaN, non-zero-NI) FCF/NI data")
    return list(reversed(ratios))


def _fcf_positive_3yr(cashflow: "pd.DataFrame") -> bool:
    fcf_series = _row(cashflow, "Free Cash Flow", "FCF positivity check")
    if len(fcf_series) < 3:
        raise MissingInputError(
            f"Need 3 fiscal years of Free Cash Flow for the 3yr-positive check, only {len(fcf_series)} available"
        )
    recent_3 = fcf_series.iloc[:3]
    if recent_3.isna().any():
        raise MissingInputError("NaN found in the most recent 3 fiscal years of Free Cash Flow")
    return bool((recent_3 > 0).all())


def _revenue_cagr_3yr(financials: "pd.DataFrame") -> float:
    revenue = _row(financials, "Total Revenue", "3yr revenue CAGR")
    if len(revenue) < 4:
        raise MissingInputError(
            f"Need 4 annual fiscal years of Total Revenue for a 3yr CAGR, only {len(revenue)} available"
        )
    latest = _value(revenue, 0, "3yr revenue CAGR (latest FY)")
    three_yr_ago = _value(revenue, 3, "3yr revenue CAGR (3 FY ago)")
    if three_yr_ago <= 0:
        raise MissingInputError("Revenue 3 fiscal years ago is <= 0 — 3yr CAGR undefined")
    cagr = ((latest / three_yr_ago) ** (1 / 3) - 1) * 100
    return cagr


def _net_debt_to_ebitda(balance_sheet: "pd.DataFrame", ebitda_ttm: float) -> float:
    if "Net Debt" in balance_sheet.index and not pd.isna(balance_sheet.loc["Net Debt"].iloc[0]):
        net_debt = float(balance_sheet.loc["Net Debt"].iloc[0])
    else:
        total_debt = _value(_row(balance_sheet, "Total Debt", "Net Debt fallback"), 0, "Total Debt (latest)")
        cash = _value(
            _row(balance_sheet, "Cash And Cash Equivalents", "Net Debt fallback"), 0, "Cash (latest)"
        )
        net_debt = total_debt - cash
    if ebitda_ttm == 0:
        raise MissingInputError("TTM EBITDA is 0 — Net Debt/EBITDA undefined")
    return net_debt / ebitda_ttm


def _roic(balance_sheet: "pd.DataFrame", ebit_ttm: float, tax_provision_ttm: float, pretax_income_ttm: float) -> tuple[float, dict]:
    if pretax_income_ttm <= 0:
        raise MissingInputError("TTM Pretax Income is <= 0 — effective tax rate for ROIC/NOPAT is undefined")
    tax_rate = tax_provision_ttm / pretax_income_ttm
    nopat = ebit_ttm * (1 - tax_rate)

    if "Invested Capital" in balance_sheet.index and not pd.isna(balance_sheet.loc["Invested Capital"].iloc[0]):
        invested_capital = float(balance_sheet.loc["Invested Capital"].iloc[0])
    else:
        total_debt = _value(_row(balance_sheet, "Total Debt", "Invested Capital fallback"), 0, "Total Debt")
        equity = _value(
            _row(balance_sheet, "Stockholders Equity", "Invested Capital fallback"), 0, "Stockholders Equity"
        )
        cash = _value(
            _row(balance_sheet, "Cash And Cash Equivalents", "Invested Capital fallback"), 0, "Cash"
        )
        invested_capital = total_debt + equity - cash

    if invested_capital == 0:
        raise MissingInputError("Invested Capital is 0 — ROIC undefined")

    roic_pct = nopat / invested_capital * 100
    detail = {
        "tax_rate": tax_rate,
        "nopat": nopat,
        "invested_capital": invested_capital,
    }
    return roic_pct, detail


def _pe_history(ticker) -> dict:
    """Reconstruct the trailing 5yr PE series per valuation-scoring.md's documented method.

    Requires `lxml` (get_earnings_dates dependency). Never averages over fewer than
    PE_HISTORY_QUARTERS quarters — falls back to the framework's no-history mode instead.
    """
    try:
        earnings = ticker.get_earnings_dates(limit=40)
    except Exception as exc:  # pragma: no cover - network/dependency failure path
        return {
            "pe_mode": "none",
            "pe_5yr_quarters_used": 0,
            "no_history_reason": f"get_earnings_dates failed: {exc}",
        }

    earnings = earnings.sort_index().dropna(subset=["Reported EPS"])
    earnings["TTM_EPS"] = earnings["Reported EPS"].rolling(4).sum()
    earnings = earnings.dropna(subset=["TTM_EPS"])

    if earnings.empty:
        return {
            "pe_mode": "none",
            "pe_5yr_quarters_used": 0,
            "no_history_reason": "no quarters with a reconstructable TTM EPS",
        }

    hist = ticker.history(start=earnings.index.min().date().isoformat(), interval="1d")
    if hist.empty:
        return {
            "pe_mode": "none",
            "pe_5yr_quarters_used": 0,
            "no_history_reason": "no price history available to pair with earnings dates",
        }
    hist.index = hist.index.tz_localize(None)

    pe_series = []
    for dt, row in earnings.iterrows():
        ttm_eps = row["TTM_EPS"]
        if ttm_eps <= 0:
            continue  # PE undefined for negative/zero TTM EPS — exclude, never fabricate
        after = hist[hist.index >= dt.tz_localize(None)]
        if after.empty:
            continue
        pe_series.append(after["Close"].iloc[0] / ttm_eps)

    usable = pe_series[-PE_HISTORY_QUARTERS:]
    if len(usable) < PE_HISTORY_QUARTERS:
        return {
            "pe_mode": "none",
            "pe_5yr_quarters_used": len(usable),
            "no_history_reason": (
                f"only {len(usable)} quarters of reconstructable TTM-EPS PE history available, "
                f"need {PE_HISTORY_QUARTERS} (5yr) — no-history fallback per valuation-scoring.md, "
                "never averaging over an undisclosed shorter window"
            ),
        }

    series = pd.Series(usable)
    return {
        "pe_mode": "range",
        "pe_5yr_avg": float(series.mean()),
        "pe_5yr_low": float(series.min()),
        "pe_5yr_high": float(series.max()),
        "pe_5yr_quarters_used": len(usable),
    }


def fetch(ticker) -> dict:
    """Compute the Stage 2 fundamentals bundle from a yfinance.Ticker-like object.

    `ticker` needs: .info, .financials, .cashflow, .balance_sheet, .quarterly_financials,
    .quarterly_cashflow, .get_earnings_dates(limit=...), .history(...).
    """
    info = ticker.info
    financials = ticker.financials
    cashflow = ticker.cashflow
    balance_sheet = ticker.balance_sheet
    qf = ticker.quarterly_financials
    qcf = ticker.quarterly_cashflow

    market_cap = _info_value(info, "marketCap", "market cap")
    enterprise_value = _info_value(info, "enterpriseValue", "enterprise value")
    shares_outstanding = _info_value(info, "sharesOutstanding", "shares outstanding")
    forward_pe = _info_value(info, "forwardPE", "forward PE")

    ebit_ttm = _ttm_sum(qf, "EBIT", "TTM EBIT")
    ni_ttm = _ttm_sum(qf, "Net Income", "TTM Net Income")
    revenue_ttm = _ttm_sum(qf, "Total Revenue", "TTM Revenue")
    gross_profit_ttm = _ttm_sum(qf, "Gross Profit", "TTM Gross Profit")
    tax_provision_ttm = _ttm_sum(qf, "Tax Provision", "TTM Tax Provision")
    pretax_income_ttm = _ttm_sum(qf, "Pretax Income", "TTM Pretax Income")
    fcf_ttm = _ttm_sum(qcf, "Free Cash Flow", "TTM Free Cash Flow")

    if info.get("ebitda") is not None:
        ebitda_ttm = float(info["ebitda"])
    else:
        da_ttm = _ttm_sum(qcf, "Depreciation And Amortization", "TTM D&A (EBITDA fallback)")
        ebitda_ttm = ebit_ttm + da_ttm

    fcf_yield_pct = fcf_ttm / market_cap * 100
    ev_ebit = enterprise_value / ebit_ttm
    net_margin_pct = ni_ttm / revenue_ttm * 100
    gross_margin_pct = gross_profit_ttm / revenue_ttm * 100

    fcf_ni_ttm_pct = fcf_ttm / ni_ttm * 100 if ni_ttm != 0 else None
    if fcf_ni_ttm_pct is None:
        raise MissingInputError("TTM Net Income is 0 — TTM FCF/NI ratio undefined")

    fcf_ni_annual_pct = _fcf_ni_annual(financials, cashflow)
    fcf_positive_3yr_or_more = _fcf_positive_3yr(cashflow)
    revenue_cagr_3yr_pct = _revenue_cagr_3yr(financials)
    net_debt_to_ebitda = _net_debt_to_ebitda(balance_sheet, ebitda_ttm)
    roic_pct, roic_detail = _roic(balance_sheet, ebit_ttm, tax_provision_ttm, pretax_income_ttm)
    pe_history = _pe_history(ticker)

    result = {
        "market_cap": market_cap,
        "enterprise_value": enterprise_value,
        "shares_outstanding": shares_outstanding,
        "forward_pe": forward_pe,
        "fcf_yield_pct": fcf_yield_pct,
        "ev_ebit": ev_ebit,
        "net_margin_pct": net_margin_pct,
        "gross_margin_pct": gross_margin_pct,
        "roic_pct": roic_pct,
        "revenue_cagr_3yr_pct": revenue_cagr_3yr_pct,
        "net_debt_to_ebitda": net_debt_to_ebitda,
        "fcf_ni_ttm_pct": fcf_ni_ttm_pct,
        "fcf_ni_annual_pct": fcf_ni_annual_pct,
        "fcf_positive_3yr_or_more": fcf_positive_3yr_or_more,
        "ebitda_ttm": ebitda_ttm,
        "_roic_detail": roic_detail,
    }
    result.update(pe_history)
    return result


def render_markdown(ticker_symbol: str, result: dict) -> str:
    lines = [f"## Fundamentals — {ticker_symbol}\n"]
    lines.append("```")
    lines.append(f"Market Cap            = {result['market_cap']:,.0f}")
    lines.append(f"Enterprise Value      = {result['enterprise_value']:,.0f}")
    lines.append(f"Shares Outstanding    = {result['shares_outstanding']:,.0f}")
    lines.append(f"Forward PE            = {result['forward_pe']:.3f}")
    lines.append(f"FCF Yield %           = {result['fcf_yield_pct']:.3f}")
    lines.append(f"EV/EBIT               = {result['ev_ebit']:.3f}")
    lines.append(f"Net Margin %          = {result['net_margin_pct']:.3f}")
    lines.append(f"Gross Margin %        = {result['gross_margin_pct']:.3f}")
    d = result["_roic_detail"]
    lines.append(
        f"ROIC % (NOPAT/InvCap) = {result['roic_pct']:.3f}  "
        f"[tax_rate={d['tax_rate']:.4f}, NOPAT={d['nopat']:,.0f}, InvestedCapital={d['invested_capital']:,.0f}]"
    )
    lines.append(f"Revenue 3yr CAGR %    = {result['revenue_cagr_3yr_pct']:.3f}")
    lines.append(f"Net Debt/EBITDA       = {result['net_debt_to_ebitda']:.3f}  [EBITDA_ttm={result['ebitda_ttm']:,.0f}]")
    lines.append(f"FCF/NI TTM %          = {result['fcf_ni_ttm_pct']:.3f}")
    annual = ", ".join(f"{v:.1f}%" for v in result["fcf_ni_annual_pct"])
    lines.append(f"FCF/NI annual (oldest first) = [{annual}]")
    lines.append(f"FCF positive 3yr+     = {result['fcf_positive_3yr_or_more']}")
    if result["pe_mode"] == "range":
        lines.append(
            f"5yr PE avg/low/high   = {result['pe_5yr_avg']:.3f} / {result['pe_5yr_low']:.3f} / "
            f"{result['pe_5yr_high']:.3f}  (n={result['pe_5yr_quarters_used']} quarters)"
        )
    else:
        lines.append(
            f"5yr PE history        = NO-HISTORY FALLBACK (n={result['pe_5yr_quarters_used']} usable quarters) "
            f"— {result['no_history_reason']}"
        )
    lines.append("```")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("ticker", help="Ticker symbol, e.g. MSFT, 0388.HK")
    parser.add_argument("--json", action="store_true", help="Print raw JSON instead of the markdown block")
    args = parser.parse_args(argv)

    import yfinance as yf

    t = yf.Ticker(args.ticker)

    try:
        result = fetch(t)
    except MissingInputError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json:
        printable = {k: v for k, v in result.items() if not k.startswith("_")}
        print(json.dumps(printable, indent=2, default=str))
    else:
        print(render_markdown(args.ticker, result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
