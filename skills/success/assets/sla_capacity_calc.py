#!/usr/bin/env python3
"""
sla_capacity_calc.py -- honest support-capacity / response-time feasibility check
for success-skill.

An SLA is a PROMISE MADE TO SOMEONE ELSE, not a template default (see
support-process-design.md's never-ship-class: an unsourced SLA default,
ground-zero example being a hardcoded, uncited P1-P4 hour table shipped in a
first-party support-triage skill). This tool never prints "your SLA should be
N hours." It computes two things that ARE derivable from inputs you actually
have:

  1. utilization = required support-minutes / available support-minutes for
     a stated period. utilization > 1 means the promise is mathematically
     impossible before any SLA number is chosen -- fix capacity or ticket
     volume first, don't pick a number and hope.
  2. worst-case first-response ceiling = the longest gap between coverage
     windows in a day, computed from the coverage schedule you supply. This
     is the only honestly promisable "we will respond within X" bound for a
     non-24/7 team: a GEOMETRIC fact about your own schedule, not a
     benchmark or industry default.

Every open-source SLA-modelling stack examined (Chatwoot, Zammad, Frappe
Helpdesk, libredesk) converges on pausing the SLA clock during a customer-
wait state, always as a named status, never implicit -- see
support-process-design.md §3. This script is the solo/small-team mirror
image: it computes when the clock CANNOT be running at all, because nobody
is covering it, before any promise is made.

Honesty framing carried into the CLI output, cited to their sources
(practitioner-report grade, first-person, no independent audit):
  - ticket volume varies by channel by an order of magnitude (PayPal vs.
    card-only checkout, ~10x, a solo operator's own count) -- never assume
    your volume, measure it per channel.
  - LIFO triage (answer newest tickets first) is a named, reasoned response
    to overload: it deliberately trades fairness for giving SOME customers
    excellent service rather than everyone a mediocre average.
  - a ~$1M-revenue threshold is one solo operator's own point of moving off
    a personal inbox onto real support tooling -- a tooling upgrade, not a
    hiring one; don't transplant the number, only the shape of the decision.

Self-test anchors (hand-derivable):
  - single 09:00-17:00 coverage window -> worst-case gap 16h
  - two windows, 00:00-08:00 and 08:00-16:00 -> worst-case gap 8h
  - 50 tickets/day * 15 min avg handling / (1 person * 8h/day) -> utilization 1.5625
"""
import argparse


def _parse_window(s):
    """'09:00-17:00' -> (9.0, 17.0), hours since midnight as floats."""
    start, end = s.split("-")

    def to_hours(t):
        h, m = t.split(":")
        return int(h) + int(m) / 60

    start_h, end_h = to_hours(start), to_hours(end)
    if not (0 <= start_h < end_h <= 24):
        raise ValueError(f"window '{s}' must satisfy 0 <= start < end <= 24")
    return (start_h, end_h)


def worst_case_gap_hours(windows):
    """Longest uncovered gap across a 24h cycle, given non-overlapping
    (start, end) windows in hours-since-midnight. The gap after the last
    window wraps around to the first window the next day -- a schedule
    with one window has exactly one gap: 24 minus that window's length."""
    if not windows:
        return 24.0
    windows = sorted(windows)
    gaps = [windows[i + 1][0] - windows[i][1] for i in range(len(windows) - 1)]
    wrap = (24 - windows[-1][1]) + windows[0][0]
    gaps.append(wrap)
    return max(gaps)


def utilization(tickets_per_day, avg_handle_minutes, people, hours_per_person):
    """required support-minutes / available support-minutes for one day.
    > 1 means demand exceeds capacity -- no response-time number is
    honestly promisable at this ratio until capacity or volume changes."""
    if people <= 0 or hours_per_person <= 0:
        raise ValueError("people and hours_per_person must both be > 0")
    required = tickets_per_day * avg_handle_minutes
    capacity = people * hours_per_person * 60
    return required / capacity


def _self_test():
    g1 = worst_case_gap_hours([(9.0, 17.0)])
    assert abs(g1 - 16.0) < 1e-9, f"single-window anchor failed: got {g1}"

    g2 = worst_case_gap_hours([(0.0, 8.0), (8.0, 16.0)])
    assert abs(g2 - 8.0) < 1e-9, f"two-window anchor failed: got {g2}"

    u = utilization(tickets_per_day=50, avg_handle_minutes=15, people=1, hours_per_person=8)
    assert abs(u - 1.5625) < 1e-9, f"utilization anchor failed: got {u}"

    print(
        "self-test PASS: single-window gap 16h, two-window gap 8h, "
        "50-ticket/15-min/1-person/8h utilization 1.5625 reproduced exactly."
    )


def main():
    _self_test()
    p = argparse.ArgumentParser(
        description="Honest support-capacity / response-time feasibility check. "
        "Computes utilization and coverage-gap ceilings; never outputs a "
        "recommended SLA number -- see the module docstring."
    )
    p.add_argument(
        "--window",
        action="append",
        default=[],
        help="coverage window HH:MM-HH:MM, repeatable (non-overlapping, within one day)",
    )
    p.add_argument("--tickets-per-day", type=float)
    p.add_argument("--avg-handle-minutes", type=float)
    p.add_argument("--people", type=int)
    p.add_argument("--hours-per-person", type=float)
    args = p.parse_args()

    ran_something = False

    if args.window:
        windows = [_parse_window(w) for w in args.window]
        gap = worst_case_gap_hours(windows)
        print(
            f"worst-case first-response ceiling: {gap:.2f}h -- the longest gap in "
            f"your OWN coverage schedule. This is not a recommended SLA; it is a "
            f"geometric fact about when nobody is covering. Promising anything "
            f"faster than this number is a promise your schedule cannot keep."
        )
        ran_something = True

    if args.tickets_per_day is not None:
        missing = [
            name
            for name, val in (
                ("--avg-handle-minutes", args.avg_handle_minutes),
                ("--people", args.people),
                ("--hours-per-person", args.hours_per_person),
            )
            if val is None
        ]
        if missing:
            raise SystemExit(
                f"--tickets-per-day given but missing: {', '.join(missing)}"
            )
        u = utilization(
            args.tickets_per_day, args.avg_handle_minutes, args.people, args.hours_per_person
        )
        print(f"utilization: {u:.3f} (required support-minutes / available support-minutes)")
        if u > 1:
            print(
                "OVERLOADED: required support-minutes exceed available capacity. No "
                "response-time number is honestly promisable at this ratio. Two "
                "practitioner-reported options, not a universal prescription: "
                "add capacity/tooling (one solo operator's own threshold for moving "
                "off a personal inbox was ~$1M revenue -- a tooling upgrade, not a "
                "hire; don't transplant the number, only the shape of the decision), "
                "or triage LIFO -- answer the most recent tickets first so some "
                "customers get an excellent response rather than everyone getting a "
                "mediocre average -- while capacity gets fixed."
            )
        else:
            print(
                "Capacity covers stated volume at this utilization. This does NOT "
                "make a specific response-time number safe to promise on its own -- "
                "check the coverage-gap ceiling above too, and remember ticket volume "
                "varies by channel (one solo operator measured ~10x more support load "
                "from PayPal signups than card-only checkout): never assume your "
                "volume without measuring your own channels."
            )
        ran_something = True

    if not ran_something:
        print(
            "self-test only ran (no --window or --tickets-per-day given). Pass "
            "--window HH:MM-HH:MM (repeatable) for a coverage-gap check, and/or "
            "--tickets-per-day --avg-handle-minutes --people --hours-per-person "
            "for a utilization check."
        )


if __name__ == "__main__":
    main()
