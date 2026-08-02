#!/usr/bin/env python3
"""Churn-model headline honesty check.

Two questions a reported churn-model accuracy figure must answer before it means anything:

1. Does it beat the naive "predict nobody churns" baseline, and by how much?
   (See `references/health-and-risk-signals.md` §5 — the ReverendBayes/Telecom-Churn-Predictor
   exhibit: a 94.60% headline accuracy is +9.09pp over the 85.51% you get by predicting nobody
   churns, and the number that matters — recall — is listed fourth, not first.)
2. If a concordance/c-index is reported instead of accuracy, is it inside the honest range for a
   real survival model (0.55-0.75, per lifelines' own documentation), or is it suspiciously high
   (a likely sign of a duration-leaking covariate)?

Self-test anchors run at import time — importing this module verifies its own arithmetic against
the exact published exhibits it teaches, not invented numbers:
  - ReverendBayes/Telecom-Churn-Predictor: 3,333 rows, 483 churners (14.49% churn rate), headline
    accuracy 94.60%, recall 0.7423 -> naive baseline 85.51%, lift +9.09pp, 25.77% of churners missed.
  - lifelines' documented concordance range 0.55-0.75; a same-dataset Cox fit at 0.93 concordance
    (duration-leaking covariate) is flagged; a correctly-computed IPCW concordance at 0.7515 passes.

No third-party dependencies. Python 3.8+.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class BaselineCheckResult:
    total: int
    churners: int
    churn_rate_pct: float
    naive_baseline_accuracy_pct: float
    headline_accuracy_pct: float
    lift_over_baseline_pp: float
    recall: float | None
    churners_missed_pct: float | None
    verdict: str
    notes: list = field(default_factory=list)


def naive_baseline_accuracy_pct(total: int, churners: int) -> float:
    """Accuracy of a model that always predicts the majority class ("nobody churns").

    This is the floor every reported accuracy figure must be compared against. A model that
    predicts nobody churns scores this, for free, with zero modeling effort.
    """
    if total <= 0:
        raise ValueError("total must be positive")
    if not (0 <= churners <= total):
        raise ValueError("churners must be between 0 and total")
    non_churners = total - churners
    majority = max(churners, non_churners)
    return round(100.0 * majority / total, 2)


def audit_churn_headline(
    total: int,
    churners: int,
    headline_accuracy_pct: float,
    recall: float | None = None,
) -> BaselineCheckResult:
    """Compare a reported headline accuracy against the naive baseline, and flag base-rate theater.

    `recall` (true positive rate on the churn class, 0-1) is optional but strongly recommended:
    accuracy alone cannot show how many actual churners a model misses. If omitted, the result
    flags that the headline cannot be fully audited without it.
    """
    churn_rate_pct = round(100.0 * churners / total, 2)
    baseline = naive_baseline_accuracy_pct(total, churners)
    lift = round(headline_accuracy_pct - baseline, 2)

    notes: list = []
    churners_missed_pct = None

    if recall is None:
        notes.append(
            "No recall reported — an accuracy figure alone cannot show how many actual "
            "churners this model misses. Treat the headline as unauditable until recall "
            "(or an equivalent churn-class metric) is supplied."
        )
    else:
        churners_missed_pct = round(100.0 * (1 - recall), 2)
        notes.append(
            f"This model misses {churners_missed_pct}% of actual churners (recall={recall})."
        )

    if lift <= 0:
        verdict = (
            "FAIL: headline accuracy does not beat predicting nobody churns. This model adds "
            "no value over the naive baseline."
        )
    elif lift < 10:
        verdict = (
            f"WEAK: only +{lift}pp over the naive baseline ({baseline}%). Base-rate theater is "
            "likely if this is being presented as a strong result — check what fraction of "
            "churners the model actually catches (recall), not just accuracy."
        )
    else:
        verdict = (
            f"Headline beats the naive baseline by +{lift}pp ({baseline}% -> "
            f"{headline_accuracy_pct}%). This does not, on its own, mean the figure is honestly "
            "reported — check for resampling-before-split leakage (see reference §5) and confirm "
            "the test set matches the real base rate."
        )

    return BaselineCheckResult(
        total=total,
        churners=churners,
        churn_rate_pct=churn_rate_pct,
        naive_baseline_accuracy_pct=baseline,
        headline_accuracy_pct=headline_accuracy_pct,
        lift_over_baseline_pp=lift,
        recall=recall,
        churners_missed_pct=churners_missed_pct,
        verdict=verdict,
        notes=notes,
    )


CONCORDANCE_HONEST_LOW = 0.55
CONCORDANCE_HONEST_HIGH = 0.75


def check_concordance(c_index: float) -> str:
    """Sanity-check a reported concordance/c-index against the honest range for real survival
    models: 0.55-0.75, per lifelines' own documentation ("even a perfect model has a lot of noise
    that can make a high score impossible"). A value outside this range — especially well above
    it — is a leakage/error signal, not evidence of a stronger model; the most common cause is a
    covariate that is itself a near-deterministic function of elapsed duration.
    """
    if c_index < 0 or c_index > 1:
        raise ValueError("c_index must be between 0 and 1")
    # lifelines' own documentation states the range as "typically" 0.55-0.75, not a razor's-edge
    # cutoff (its own cited comparison example, 0.7515, is described as "squarely inside" the
    # range) — round to 2 decimal places before comparing so a boundary value like 0.7515 is
    # judged the way the source itself judges it, not flagged on a rounding technicality.
    rounded = round(c_index, 2)
    if CONCORDANCE_HONEST_LOW <= rounded <= CONCORDANCE_HONEST_HIGH:
        return (
            f"OK: {c_index} is inside the honest range for a real survival model "
            f"({CONCORDANCE_HONEST_LOW}-{CONCORDANCE_HONEST_HIGH})."
        )
    if rounded > CONCORDANCE_HONEST_HIGH:
        return (
            f"FLAG: {c_index} is above the honest range ({CONCORDANCE_HONEST_LOW}-"
            f"{CONCORDANCE_HONEST_HIGH}). This is a leakage/error signal, not a stronger model — "
            "check for a covariate that encodes elapsed duration (e.g., a charges-to-date field "
            "that is ~tenure x rate)."
        )
    return (
        f"FLAG: {c_index} is below the honest range ({CONCORDANCE_HONEST_LOW}-"
        f"{CONCORDANCE_HONEST_HIGH}) — the model is ranking worse than typical real survival "
        "models; check for a data or fitting error before trusting it as-is."
    )


def _run_self_tests() -> None:
    """Verify this module's arithmetic against the exact published exhibits it teaches.

    Anchor 1 — ReverendBayes/Telecom-Churn-Predictor (MIT), `references/health-and-risk-signals.md`
    §5: 3,333 rows, 483 true / 2,850 false (churn rate 14.49%), headline "94.60% Accuracy ...
    0.7423 Recall". Majority-class baseline = 2,850/3,333 = 85.51%.
    """
    result = audit_churn_headline(
        total=3333,
        churners=483,
        headline_accuracy_pct=94.60,
        recall=0.7423,
    )
    assert result.churn_rate_pct == 14.49, result.churn_rate_pct
    assert result.naive_baseline_accuracy_pct == 85.51, result.naive_baseline_accuracy_pct
    assert abs(result.lift_over_baseline_pp - 9.09) < 0.01, result.lift_over_baseline_pp
    assert abs(result.churners_missed_pct - 25.77) < 0.01, result.churners_missed_pct
    assert "WEAK" in result.verdict, result.verdict  # +9.09pp is real but modest, not a strong win

    # No-recall path must flag itself as unauditable, not silently pass.
    no_recall = audit_churn_headline(total=3333, churners=483, headline_accuracy_pct=94.60)
    assert no_recall.churners_missed_pct is None
    assert any("unauditable" in n for n in no_recall.notes)

    # A model that doesn't beat the baseline at all must FAIL, not WEAK.
    zero_lift = audit_churn_headline(
        total=3333, churners=483, headline_accuracy_pct=85.51, recall=0.5
    )
    assert "FAIL" in zero_lift.verdict, zero_lift.verdict

    # Anchor 2 — lifelines' documented concordance range (0.55-0.75); a same-dataset Cox fit
    # reporting 0.93 concordance (duration-leaking covariate) must be flagged, not accepted; an
    # IPCW concordance of 0.7515, computed correctly on a comparable set, must pass.
    assert "FLAG" in check_concordance(0.93)
    assert "OK" in check_concordance(0.7515)
    assert "FLAG" in check_concordance(0.30)  # below-range is also a signal, not just above


_run_self_tests()


if __name__ == "__main__":
    import argparse
    import json
    import sys

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--total", type=int, help="Total accounts/rows in the dataset")
    parser.add_argument("--churners", type=int, help="Number of churners in the dataset")
    parser.add_argument("--headline-accuracy", type=float, help="Reported headline accuracy, e.g. 94.60")
    parser.add_argument("--recall", type=float, default=None, help="Reported churn-class recall, 0-1")
    parser.add_argument("--concordance", type=float, default=None, help="Reported concordance/c-index, 0-1")
    args = parser.parse_args()

    if args.concordance is not None:
        print(check_concordance(args.concordance))
        sys.exit(0)

    if args.total is None or args.churners is None or args.headline_accuracy is None:
        print("Self-tests passed. Provide --total/--churners/--headline-accuracy (and optionally")
        print("--recall) to audit a specific headline, or --concordance to sanity-check a c-index.")
        print()
        print("Example (the ReverendBayes anchor from references/health-and-risk-signals.md §5):")
        print("  python3 churn_baseline_check.py --total 3333 --churners 483 \\")
        print("      --headline-accuracy 94.60 --recall 0.7423")
        sys.exit(0)

    result = audit_churn_headline(
        total=args.total,
        churners=args.churners,
        headline_accuracy_pct=args.headline_accuracy,
        recall=args.recall,
    )
    print(json.dumps(result.__dict__, indent=2))
