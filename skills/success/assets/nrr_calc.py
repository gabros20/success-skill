#!/usr/bin/env python3
"""
nrr_calc.py -- Net/Gross Revenue Retention calculator, four SEC-verbatim mechanics
plus the ARR-bridge/GRR form, as selectable modes.

**Never compare NRR across definitions.** All four filings below call their metric
"net revenue retention," all four are cohort-based and exclude new-customer revenue --
but the measurement WINDOW, the revenue SCOPE, and the edge-case handling differ. A
reported 126% and a reported 131% computed under different mechanics are not the same
quantity. See references/renewals-and-expansion.md §2 for the full evidence trail;
every quote below is read directly from the filing text (via a declared-UA curl fetch
+ HTML strip), not a summarizer's paraphrase -- see research/_raw/_raw-web-canon-commercial.md.

Modes:

  snowflake_2yr_snapshot -- Snowflake, 10-K FY2025 (period ended Jan 31, 2025):
      "a measurement period consisting of the trailing two years... the population of
      customers under capacity contracts that used our platform at any point in the
      first month of the first year... net revenue retention rate as the quotient
      obtained by dividing our product revenue from this cohort in the second year...
      by our product revenue from this cohort in the first year." A single two-year
      snapshot -- no rolling average. Reported: 126% as of Jan 31, 2025.
      https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm

  rolling_12mo_weighted -- Datadog, 10-K FY2020, and Klaviyo, S-1 (2023):
      Datadog: "starting with the ARR from the cohort of all customers as of 12 months
      prior... Current Period ARR includes any expansion and is net of contraction or
      attrition... but excludes ARR from new customers... divide the total Current
      Period ARR by the total Prior Period ARR to arrive at the point-in-time...
      [then] average the trailing 12-month point-in-time... rates." Reported: "above
      130%" for FY2020 and FY2019. Datadog's own extracted text is ambiguous about
      whether that trailing average is ARR-weighted -- default here is an unweighted
      mean of the monthly point-in-time rates, the plainer reading.
      https://www.sec.gov/Archives/edgar/data/1561550/000156459021009770/ddog-10k_20201231.htm
      Klaviyo: the same rolling 12-month mechanic, but EXPLICIT that reactivated
      subscriptions within the window count as retained, and EXPLICIT that the
      average is "weighted... with the weightings determined by the total ARR at the
      end of each period." Pass weighted=True to reproduce Klaviyo's stated method.
      https://www.sec.gov/Archives/edgar/data/1835830/000162828023030618/klaviyoincs-1.htm

  monthly_cohort_annualized -- HubSpot, 10-K FY2024:
      "dividing Retained Subscription Revenue by Retention Base Revenue in the given
      period, calculating the weighted average of these rates using the Retention
      Base Revenue for the period, and then annualizing the resulting rates." Scoped
      to *subscription* revenue only (excludes services/other revenue). Reported (3
      most recent fiscal years, oldest first): 102.2% / 103.9% / 110.3%. HubSpot's own
      extracted text does not spell out the exact annualization formula beyond
      "annualizing" -- this implements the standard compounding convention
      (monthly_rate ** 12). Treat the self-test below as an internal-consistency
      check against that convention, not an independent verification of HubSpot's
      undisclosed internal formula.
      https://www.sec.gov/Archives/edgar/data/1404655/000095017025018873/hubs-20241231.htm

  grr / arr_bridge_nrr -- reference implementation: 0x416d6982/pypulate@main
      src/pypulate/kpi/business_kpi.py (MIT -- LICENSE + pyproject.toml agree; see
      research/_raw/_raw-gh-churn-health.md for the license audit). Anchored to a
      period-start revenue base (not a blended/average base), excludes new-logo
      revenue entirely, GRR excludes expansion while NRR-arr-bridge includes it.
      This ARR-bridge NRR form is a DIFFERENT quantity from the four cohort-anchored
      filings above -- Dave Kellogg's "Lazy NRR is Not NRR" distinguishes true
      cohort NRR (resists manipulation) from an ARR-bridge calculation over one
      period's own starting base (more gameable, dressed up to look the same). Ship
      the ARR-bridge NRR number labeled as such, never as equivalent to a filing's
      cohort NRR. GRR itself has no such ambiguity -- it excludes expansion by
      definition and is the more portable of the two for a solo/small operator.
      pypulate's own docstring claims GRR "is capped at 100%" but the code does not
      clip -- true only by construction for non-negative inputs, which are not
      validated here either. Evidence grade: MEASURED-WITH-METHOD (all four filings
      are primary-source audited disclosures); the ARR-bridge/GRR form is a reference
      implementation, not an audited filing.

Self-test anchors (run automatically at import, and again before any CLI use):
  - Snowflake-mechanic snapshot reproducing the reported 126% (illustrative inputs --
    Snowflake's own cohort dollar figures are not disclosed, only the percentage).
  - Datadog-mechanic snapshot reproducing the reported "above 130%" (same caveat).
  - HubSpot-mechanic annualization internally consistent with 110.3% under the
    standard compounding convention.
  - pypulate's own worked examples, verbatim: net_revenue_retention(10000, 2000, 500,
    1000) -> 105.0; gross_revenue_retention(10000, 500, 1000) -> 85.0.
"""
import argparse


def snowflake_2yr_snapshot(cohort_revenue_year1, cohort_revenue_year2):
    """Single two-year cohort snapshot. Returns a percentage.

    cohort_revenue_year1/2: product revenue from the SAME fixed cohort (customers
    active in month 1 of year 1) in each year of the window. A customer who
    churned contributes zero to year2 and remains in the denominator's cohort.
    """
    if cohort_revenue_year1 <= 0:
        raise ValueError("cohort_revenue_year1 must be positive")
    return cohort_revenue_year2 / cohort_revenue_year1 * 100


def rolling_12mo_point_in_time(prior_period_arr, current_period_arr):
    """One point-in-time snapshot of the rolling 12-month mechanic (Datadog/Klaviyo
    base unit, before averaging across months). Returns a percentage."""
    if prior_period_arr <= 0:
        raise ValueError("prior_period_arr must be positive")
    return current_period_arr / prior_period_arr * 100


def rolling_12mo_weighted(monthly_snapshots, weighted=False):
    """Average the trailing 12 monthly point-in-time rates.

    monthly_snapshots: iterable of (current_period_arr, prior_period_arr) pairs, one
      per month in the trailing 12-month window.
    weighted: False (default) -- unweighted mean, the plainer reading of Datadog's
      own text. True -- ARR-weighted mean (weight = that month's current_period_arr),
      Klaviyo's explicitly stated method.
    Returns a percentage.
    """
    snapshots = list(monthly_snapshots)
    if not snapshots:
        raise ValueError("monthly_snapshots must not be empty")
    rates = [rolling_12mo_point_in_time(prior, current) for current, prior in snapshots]
    if not weighted:
        return sum(rates) / len(rates)
    weights = [current for current, _prior in snapshots]
    total_weight = sum(weights)
    if total_weight <= 0:
        raise ValueError("total ARR weight must be positive for a weighted average")
    return sum(rate * w for rate, w in zip(rates, weights)) / total_weight


def monthly_cohort_annualized(monthly_rates, monthly_bases):
    """HubSpot mechanic: weighted average of monthly rates (weighted by that month's
    Retention Base Revenue), then annualized via the standard compounding convention.

    monthly_rates: iterable of monthly retention rates as percentages (e.g. 100.8).
    monthly_bases: iterable of Retention Base Revenue for the same months, same order.
    Returns the annualized percentage.
    """
    rates = list(monthly_rates)
    bases = list(monthly_bases)
    if len(rates) != len(bases) or not rates:
        raise ValueError("monthly_rates and monthly_bases must be equal-length and non-empty")
    total_base = sum(bases)
    if total_base <= 0:
        raise ValueError("total Retention Base Revenue must be positive")
    weighted_avg_monthly_rate = sum(r * b for r, b in zip(rates, bases)) / total_base
    return (weighted_avg_monthly_rate / 100) ** 12 * 100


def gross_revenue_retention(starting_arr, contraction_arr, churned_arr):
    """pypulate mechanic, verbatim formula. Excludes expansion entirely. Returns a
    percentage; not clipped at 100 -- true by construction only for non-negative,
    well-formed inputs."""
    if starting_arr <= 0:
        raise ValueError("starting_arr must be positive")
    retained = starting_arr - contraction_arr - churned_arr
    return retained / starting_arr * 100


def net_revenue_retention_arr_bridge(starting_arr, expansion_arr, contraction_arr, churned_arr):
    """pypulate mechanic, verbatim formula. An ARR-BRIDGE calculation over one
    period's own starting base -- NOT the same quantity as the four cohort-anchored
    filing mechanics above. See Kellogg's "Lazy NRR is Not NRR." Returns a
    percentage."""
    if starting_arr <= 0:
        raise ValueError("starting_arr must be positive")
    retained = starting_arr + expansion_arr - contraction_arr - churned_arr
    return retained / starting_arr * 100


def _self_test():
    # Snowflake mechanic: illustrative inputs reproducing the reported 126%
    # (Snowflake's own cohort dollar figures are not disclosed).
    r = snowflake_2yr_snapshot(cohort_revenue_year1=100, cohort_revenue_year2=126)
    assert r == 126.0, f"Snowflake anchor failed: got {r}, expected 126.0"

    # Datadog mechanic: illustrative single snapshot reproducing "above 130%".
    r = rolling_12mo_point_in_time(prior_period_arr=100, current_period_arr=131)
    assert r == 131.0, f"Datadog anchor failed: got {r}, expected 131.0"

    # Klaviyo-style ARR-weighted average across two illustrative months differs
    # from the unweighted mean -- confirms the weighted=True path is live, not a
    # no-op copy of the unweighted path.
    snaps = [(200, 100), (100, 100)]  # (current_period_arr, prior_period_arr)
    unweighted = rolling_12mo_weighted(snaps, weighted=False)
    weighted = rolling_12mo_weighted(snaps, weighted=True)
    assert unweighted == 150.0, f"unweighted mean failed: got {unweighted}, expected 150.0"
    assert abs(weighted - 166.66666666666666) < 1e-9, f"weighted mean failed: got {weighted}"

    # HubSpot mechanic: a monthly rate that compounds to 110.3% over 12 months,
    # by the standard convention -- internal-consistency check, not an
    # independent verification of HubSpot's undisclosed exact formula.
    monthly_rate = (110.3 / 100) ** (1 / 12) * 100
    r = monthly_cohort_annualized([monthly_rate], [1000])
    assert round(r, 1) == 110.3, f"HubSpot-convention anchor failed: got {r}, expected 110.3"

    # pypulate's own worked examples, verbatim.
    r = net_revenue_retention_arr_bridge(10000, 2000, 500, 1000)
    assert r == 105.0, f"pypulate NRR-arr-bridge anchor failed: got {r}, expected 105.0"
    r = gross_revenue_retention(10000, 500, 1000)
    assert r == 85.0, f"pypulate GRR anchor failed: got {r}, expected 85.0"


_self_test()  # runs at import, per this asset's self-testing requirement


def main():
    p = argparse.ArgumentParser(
        description="NRR/GRR calculator -- four SEC-verbatim mechanics plus GRR/ARR-bridge. "
                    "Never compare a result across modes.")
    p.add_argument("--mode", required=True,
                   choices=["snowflake_2yr_snapshot", "rolling_12mo_point_in_time",
                            "rolling_12mo_weighted", "monthly_cohort_annualized",
                            "grr", "arr_bridge_nrr"])
    p.add_argument("--values", nargs="+", type=float, required=True,
                   help="mode-specific positional values, see --mode's docstring in the module "
                        "header for argument order")
    p.add_argument("--weighted", action="store_true",
                   help="rolling_12mo_weighted only: use Klaviyo's ARR-weighted average "
                        "instead of the unweighted mean")
    args = p.parse_args()

    v = args.values
    if args.mode == "snowflake_2yr_snapshot":
        result = snowflake_2yr_snapshot(v[0], v[1])
    elif args.mode == "rolling_12mo_point_in_time":
        result = rolling_12mo_point_in_time(v[0], v[1])
    elif args.mode == "rolling_12mo_weighted":
        pairs = list(zip(v[0::2], v[1::2]))  # (current, prior), (current, prior), ...
        result = rolling_12mo_weighted(pairs, weighted=args.weighted)
    elif args.mode == "monthly_cohort_annualized":
        half = len(v) // 2
        result = monthly_cohort_annualized(v[:half], v[half:])
    elif args.mode == "grr":
        result = gross_revenue_retention(v[0], v[1], v[2])
    elif args.mode == "arr_bridge_nrr":
        result = net_revenue_retention_arr_bridge(v[0], v[1], v[2], v[3])
    else:
        raise SystemExit(f"unhandled mode {args.mode}")

    print(f"mode={args.mode}  result={result:.2f}%")
    print("Never compare this figure to a result computed under a different mode.")


if __name__ == "__main__":
    main()
