import pandas as pd
import pytest

from scripts.fetch_fundamentals import fetch
from scripts.scoring.common import MissingInputError


def _dated_series(values, freq_years=False):
    """Build a pandas Series indexed by descending dates (most-recent-first, like yfinance)."""
    n = len(values)
    if freq_years:
        dates = pd.date_range(end="2026-06-30", periods=n, freq="365D")[::-1]
    else:
        dates = pd.date_range(end="2026-06-30", periods=n, freq="90D")[::-1]
    return pd.Series(values, index=dates)


class FakeTicker:
    """Minimal stand-in for yfinance.Ticker exposing exactly what fetch_fundamentals.fetch() reads."""

    def __init__(self, info, financials, cashflow, balance_sheet, quarterly_financials, quarterly_cashflow,
                 earnings_dates=None, history=None):
        self.info = info
        self.financials = financials
        self.cashflow = cashflow
        self.balance_sheet = balance_sheet
        self.quarterly_financials = quarterly_financials
        self.quarterly_cashflow = quarterly_cashflow
        self._earnings_dates = earnings_dates
        self._history = history

    def get_earnings_dates(self, limit=40):
        if self._earnings_dates is None:
            raise RuntimeError("lxml not installed")
        return self._earnings_dates

    def history(self, start=None, interval="1d"):
        return self._history


def _msft_like_annual():
    """4 annual FY columns reproducing the MSFT FCF/NI ratios committed in valuation-scoring.md.

    FCF/NI 2022-2025: 89.6%, 82.2%, 84.0%, 70.3% (oldest first per the doc). yfinance columns
    are most-recent-first, so this fixture stores them newest-first: 2025, 2024, 2023, 2022.
    """
    dates = pd.to_datetime(["2025-06-30", "2024-06-30", "2023-06-30", "2022-06-30"])
    ni = pd.Series([133_000_000_000, 120_000_000_000, 110_000_000_000, 100_000_000_000], index=dates)
    # fcf = ni * ratio/100, ratios newest-first: 70.3, 84.0, 82.2, 89.6
    ratios_newest_first = [70.3, 84.0, 82.2, 89.6]
    fcf = pd.Series([n * r / 100 for n, r in zip(ni, ratios_newest_first)], index=dates)
    revenue = pd.Series([280_000_000_000, 245_000_000_000, 212_000_000_000, 198_000_000_000], index=dates)
    return dates, ni, fcf, revenue, ratios_newest_first


def _build_fake_ticker(**overrides):
    dates, ni, fcf, revenue, ratios_newest_first = _msft_like_annual()

    financials = pd.DataFrame(
        {
            "Net Income": ni,
            "Total Revenue": revenue,
            "EBIT": revenue * 0.42,
            "Gross Profit": revenue * 0.68,
        }
    ).T
    cashflow = pd.DataFrame({"Free Cash Flow": fcf}).T

    bs_dates = dates
    balance_sheet = pd.DataFrame(
        {
            "Net Debt": pd.Series([19_000_000_000, 33_000_000_000, 12_500_000_000, 20_000_000_000], index=bs_dates),
            "Invested Capital": pd.Series(
                [386_000_000_000, 320_000_000_000, 253_000_000_000, 200_000_000_000], index=bs_dates
            ),
            "Total Debt": pd.Series([60_000_000_000, 67_000_000_000, 60_000_000_000, 55_000_000_000], index=bs_dates),
            "Stockholders Equity": pd.Series(
                [230_000_000_000, 206_000_000_000, 190_000_000_000, 166_000_000_000], index=bs_dates
            ),
            "Cash And Cash Equivalents": pd.Series(
                [30_000_000_000, 18_000_000_000, 34_000_000_000, 13_000_000_000], index=bs_dates
            ),
        }
    ).T

    q_dates = pd.date_range(end="2026-06-30", periods=4, freq="90D")[::-1]
    quarterly_financials = pd.DataFrame(
        {
            "EBIT": pd.Series([42_000_000_000] * 4, index=q_dates),
            "Net Income": pd.Series([33_000_000_000] * 4, index=q_dates),
            "Total Revenue": pd.Series([83_000_000_000] * 4, index=q_dates),
            "Gross Profit": pd.Series([56_000_000_000] * 4, index=q_dates),
            "Tax Provision": pd.Series([8_000_000_000] * 4, index=q_dates),
            "Pretax Income": pd.Series([41_000_000_000] * 4, index=q_dates),
        }
    ).T
    quarterly_cashflow = pd.DataFrame(
        {
            "Free Cash Flow": pd.Series([16_750_000_000] * 4, index=q_dates),
            "Depreciation And Amortization": pd.Series([5_000_000_000] * 4, index=q_dates),
        }
    ).T

    info = {
        "marketCap": 3_800_000_000_000,
        "enterpriseValue": 3_750_000_000_000,
        "sharesOutstanding": 7_400_000_000,
        "forwardPE": 30.0,
        "ebitda": 190_000_000_000,
    }

    kwargs = dict(
        info=info,
        financials=financials,
        cashflow=cashflow,
        balance_sheet=balance_sheet,
        quarterly_financials=quarterly_financials,
        quarterly_cashflow=quarterly_cashflow,
    )
    kwargs.update(overrides)
    return FakeTicker(**kwargs), ratios_newest_first


def test_fcf_ni_ratios_match_valuation_scoring_md():
    """FCF/NI 89.6%/82.2%/84.0%/70.3% (2022-2025, oldest first) — from valuation-scoring.md."""
    ticker, ratios_newest_first = _build_fake_ticker()
    result = fetch(ticker)
    expected_oldest_first = list(reversed(ratios_newest_first))
    assert result["fcf_ni_annual_pct"] == pytest.approx(expected_oldest_first, abs=0.05)


def test_fcf_positive_3yr_true_when_all_positive():
    ticker, _ = _build_fake_ticker()
    result = fetch(ticker)
    assert result["fcf_positive_3yr_or_more"] is True


def test_roic_and_margins_computed():
    ticker, _ = _build_fake_ticker()
    result = fetch(ticker)
    # NOPAT = EBIT_ttm * (1 - tax_rate); tax_rate = 32B/164B ≈ 0.1951; EBIT_ttm = 168B
    assert result["roic_pct"] == pytest.approx((168_000_000_000 * (1 - 8e9 * 4 / (41e9 * 4))) / 386_000_000_000 * 100, rel=1e-3)
    assert result["net_margin_pct"] == pytest.approx(33e9 * 4 / (83e9 * 4) * 100, rel=1e-6)
    assert result["ev_ebit"] == pytest.approx(3_750_000_000_000 / (42e9 * 4), rel=1e-6)


def test_5yr_pe_reconstruction_msft_like():
    """5yr avg PE ~32.0x, range ~24.2-38.8x (n=20 quarters) — from valuation-scoring.md."""
    q_dates = pd.date_range(end="2026-06-30", periods=24, freq="90D")[::-1]
    # ~0.25/quarter -> TTM EPS ~1.0, so price 24-38 reconstructs to a PE of ~24-38x
    eps = pd.Series([0.25 + 0.001 * i for i in range(24)], index=q_dates)
    earnings = pd.DataFrame({"Reported EPS": eps})
    # price such that reconstructed PE oscillates within the documented 24.2-38.8 band
    prices = [24.2 + (i % 5) * 3.65 for i in range(24)]
    hist = pd.DataFrame({"Close": prices}, index=q_dates)

    ticker, _ = _build_fake_ticker(earnings_dates=earnings, history=hist)
    result = fetch(ticker)

    assert result["pe_mode"] == "range"
    assert result["pe_5yr_quarters_used"] == 20
    assert 20 < result["pe_5yr_avg"] < 40
    assert result["pe_5yr_low"] < result["pe_5yr_avg"] < result["pe_5yr_high"]


def test_insufficient_pe_history_flags_no_history_never_averages_shorter_window():
    """<20 quarters must raise the no-history flag, never compute a partial average."""
    q_dates = pd.date_range(end="2026-06-30", periods=10, freq="90D")[::-1]
    eps = pd.Series([1.0 + 0.02 * i for i in range(10)], index=q_dates)
    earnings = pd.DataFrame({"Reported EPS": eps})
    hist = pd.DataFrame({"Close": [30.0] * 10}, index=q_dates)

    ticker, _ = _build_fake_ticker(earnings_dates=earnings, history=hist)
    result = fetch(ticker)

    assert result["pe_mode"] == "none"
    assert "pe_5yr_avg" not in result
    assert result["pe_5yr_quarters_used"] < 20
    assert "no_history_reason" in result


def test_missing_required_info_field_raises_missing_input_error():
    ticker, _ = _build_fake_ticker(info={"marketCap": 100})  # missing enterpriseValue etc.
    with pytest.raises(MissingInputError, match="enterpriseValue"):
        fetch(ticker)


def test_nan_required_field_raises_missing_input_error():
    ticker, _ = _build_fake_ticker()
    ticker.quarterly_financials.loc["EBIT"] = [None, None, None, None]
    with pytest.raises(MissingInputError, match="EBIT"):
        fetch(ticker)


def test_fewer_than_4_quarters_raises_missing_input_error():
    ticker, _ = _build_fake_ticker()
    ticker.quarterly_financials = ticker.quarterly_financials.iloc[:, :3]
    with pytest.raises(MissingInputError, match="4 quarters"):
        fetch(ticker)


def test_unreported_all_nan_quarter_column_is_ignored():
    ticker, _ = _build_fake_ticker()
    ref = fetch(_build_fake_ticker()[0])
    for name in ("quarterly_financials", "quarterly_cashflow"):
        df = getattr(ticker, name)
        placeholder = pd.Series(float("nan"), index=df.index, name=df.columns[0] + pd.Timedelta(days=90))
        if name == "quarterly_financials":
            placeholder["Diluted EPS"] = 0.79  # stray per-share line, as yfinance emits for an unreported quarter
        setattr(ticker, name, pd.concat([placeholder.to_frame(), df], axis=1))
    assert fetch(ticker)["ev_ebit"] == ref["ev_ebit"]


# --- advisory block (SBC disclosure + cycle-peak / value-trap flags; no score effect) ---


def _eight_quarters(eps_newest_first, sbc_newest_first=None):
    q_dates = pd.date_range(end="2026-06-30", periods=8, freq="90D")[::-1]
    base_f = {
        "EBIT": [42_000_000_000] * 8,
        "Net Income": [33_000_000_000] * 8,
        "Total Revenue": [83_000_000_000] * 8,
        "Gross Profit": [56_000_000_000] * 8,
        "Tax Provision": [8_000_000_000] * 8,
        "Pretax Income": [41_000_000_000] * 8,
        "Diluted EPS": eps_newest_first,
    }
    qf = pd.DataFrame({k: pd.Series(v, index=q_dates) for k, v in base_f.items()}).T
    base_c = {
        "Free Cash Flow": [16_750_000_000] * 8,
        "Depreciation And Amortization": [5_000_000_000] * 8,
    }
    if sbc_newest_first is not None:
        base_c["Stock Based Compensation"] = sbc_newest_first
    qcf = pd.DataFrame({k: pd.Series(v, index=q_dates) for k, v in base_c.items()}).T
    return qf, qcf


def test_advisory_unknown_when_rows_missing_never_raises():
    t, _ = _build_fake_ticker()
    adv = fetch(t)["advisory"]
    assert adv["sbc"] is None and adv["sbc_ttm"] is None
    assert adv["cycle_peak"]["flag"] == "UNKNOWN"
    assert adv["value_trap_candidate"]["flag"] == "UNKNOWN"


def test_advisory_cycle_peak_and_sbc_from_eight_quarters():
    qf, qcf = _eight_quarters([2.0] * 4 + [0.5] * 4, [2_000_000_000] * 8)
    t, _ = _build_fake_ticker(quarterly_financials=qf, quarterly_cashflow=qcf)
    adv = fetch(t)["advisory"]
    assert adv["eps_ttm_now"] == pytest.approx(8.0)
    assert adv["eps_ttm_1y_ago"] == pytest.approx(2.0)
    assert adv["cycle_peak"]["flag"] == "CYCLE_PEAK_CANDIDATE"  # +300%
    assert adv["sbc_ttm"] == pytest.approx(8_000_000_000)
    assert adv["sbc"]["sbc_pct_fcf"] == pytest.approx(8e9 / 67e9 * 100)
    assert adv["sbc"]["severity"] == "none"  # 11.9% of FCF


def test_advisory_gap_in_quarter_dates_is_unknown_not_guess():
    qf, qcf = _eight_quarters([2.0] * 8)
    # simulate a fiscal-year-change stub: shift older quarters back by an extra 60 days
    shifted = list(qf.columns)
    shifted[4:] = [d - pd.Timedelta(days=60) for d in shifted[4:]]
    qf.columns = shifted
    t, _ = _build_fake_ticker(quarterly_financials=qf, quarterly_cashflow=qcf)
    assert fetch(t)["advisory"]["cycle_peak"]["flag"] == "UNKNOWN"


def test_advisory_block_renders_in_markdown():
    from scripts.fetch_fundamentals import render_markdown

    qf, qcf = _eight_quarters([2.0] * 8, [20_000_000_000] * 8)
    t, _ = _build_fake_ticker(quarterly_financials=qf, quarterly_cashflow=qcf)
    text = render_markdown("TEST", fetch(t))
    assert "SBC block" in text and "SEVERE" in text  # SBC 80B > FCF 67B
    assert "cycle_peak" in text


# --- SBC inputs for the scores (methodology 2026-10-12) ---


def test_sbc_score_inputs_present_and_correct():
    qf, qcf = _eight_quarters([2.0] * 8, [2_000_000_000] * 8)
    qcf.loc["Repurchase Of Capital Stock"] = [-1_000_000_000] * 8
    t, _ = _build_fake_ticker(quarterly_financials=qf, quarterly_cashflow=qcf)
    r = fetch(t)
    mc = 3_800_000_000_000
    assert r["sbc_ttm"] == pytest.approx(8e9)
    assert r["sbc_yield_pct"] == pytest.approx(8e9 / mc * 100)
    # FCF TTM = 4 x 67e9/4 ; NI TTM = 132e9 ; (FCF - SBC)/NI
    assert r["fcf_after_sbc_ni_ttm_pct"] == pytest.approx((r["fcf_ttm"] - 8e9) / r["ni_ttm"] * 100)
    assert r["gross_buyback_yield_pct"] == pytest.approx(4e9 / mc * 100)
    assert r["ni_normalised"] is False


def test_sbc_inputs_none_when_yfinance_lacks_them():
    t, _ = _build_fake_ticker()
    r = fetch(t)
    assert r["sbc_ttm"] is None and r["sbc_yield_pct"] is None
    assert r["fcf_after_sbc_ni_ttm_pct"] is None and r["gross_buyback_yield_pct"] is None


def test_normalised_ni_changes_only_the_after_sbc_ratio_and_requires_a_note():
    qf, qcf = _eight_quarters([2.0] * 8, [2_000_000_000] * 8)
    t, _ = _build_fake_ticker(quarterly_financials=qf, quarterly_cashflow=qcf)
    base = fetch(t)
    norm = fetch(t, normalised_ni=60e9, normalisation_note="excludes $72B one-time tax benefit (10-Q 0000000000-00-000000)")
    assert norm["fcf_ni_ttm_pct"] == pytest.approx(base["fcf_ni_ttm_pct"])  # plain ratio untouched
    assert norm["fcf_after_sbc_ni_ttm_pct"] == pytest.approx((base["fcf_ttm"] - 8e9) / 60e9 * 100)
    assert norm["ni_normalised"] is True and "tax benefit" in norm["ni_normalisation_text"]
    with pytest.raises(MissingInputError):
        fetch(t, normalised_ni=60e9)
    with pytest.raises(MissingInputError):
        fetch(t, normalised_ni=-5.0, normalisation_note="x")
