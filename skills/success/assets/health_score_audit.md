# Health score audit checklist

Use this to audit an existing or proposed customer health score before trusting it. Full epistemics
and citations: `references/health-and-risk-signals.md`. Fill in each row; do not skip a row by
assuming "probably yes" — an unanswered row is a finding, not a pass.

| # | Check | Question | Pass looks like | Fail looks like |
|---|---|---|---|---|
| 1 | Outcome joined | Has the score ever been joined against a real, later outcome (actual churn, actual renewal, actual expansion) — not just computed and displayed? | A logged comparison of score-at-time-T vs. outcome-at-time-T+N exists, even informally. | The score is computed and acted on but never checked against what actually happened (the Buffer/Odoo pattern — see reference §2). |
| 2 | Backtested-or-goal | Is "this score predicts outcomes" a demonstrated result, or still a stated aspiration/goal? | A specific backtest exists with a date and a result, good or bad. | "Backtested and validated" appears as a listed objective/goal, not a completed result (GitLab's own handbook does this — reference §2). |
| 3 | Input expiry | Does every input have a stated staleness window, after which it is shown as missing rather than kept as a stale value? | Each measure has an explicit "stale after N days → NA" rule. | Inputs are used indefinitely with no staleness rule; a 6-month-old data point scores identically to a fresh one. |
| 4 | Override rules | Is there a human-override path, and is it disclosed as an override (not hidden inside "the algorithm")? | An explicit rule states who can override, when, and that the override is documented as human judgment. | A human field (e.g., "CSM sentiment") silently dominates the weighted arithmetic with no disclosure that this is what's happening. |
| 5 | Missing-data convention | Is missing data treated as a risk signal, a neutral signal, or silently redistributed to other weights? State which, on purpose. | The convention is stated and deliberately chosen (e.g., "missing data raises risk, does not neutralize it"). | Missing data is redistributed to remaining weights with no stated rationale, quietly shifting the score toward whichever input has the least missing data. |
| 6 | Segmented-or-copied thresholds | Are thresholds/bands set per segment (touch tier, contract type, usage pattern), or is one band copied across every account? | Thresholds are justified per segment, and low-touch/self-serve accounts have measures explicitly turned off where they're meaningless. | One threshold set (e.g., "1–5 tickets = green") is applied uniformly regardless of segment. |
| 7 | Observability | Is the churn/inactivity event actually observed (a subscription lapse, a cancellation), or inferred from a silence window (usage-based, non-contractual)? State which. | The business's contractual shape is named, and the scoring approach matches it. | A contractual-shaped scoring template (renewal-date-anchored) is applied to a non-contractual business with no cancellation event. |
| 8 | Reason tie-breakers | If the score or triage process assigns a churn "reason," does the reason taxonomy include disambiguation rules against its nearest-neighbor categories? | Each reason category states what distinguishes it from its closest neighbor (e.g., "loss of budget" vs. "corporate decision"). | A reason list exists with no rule for which one to pick when two plausibly apply — a category list without tie-breakers is not a taxonomy. |
| 9 | Recency thresholds justified | If "at risk" or "dormant" is defined by a silence window, is the window justified for *this* product's natural usage cadence? | The threshold is derived from the product's own observed return-visit distribution, and is stated as product-specific. | A copied inactivity window (e.g., a console's few-day "at risk" band applied to a monthly-invoicing tool) — a recency threshold copied across products is the most common way a health signal becomes noise. `dynatrace-oss/CustomerSuccess` (Apache-2.0) ships exactly this pattern with unexplained thresholds; it is the concrete artifact to point at. |
| 10 | Account/user rollup modelled | For a multi-seat account, is the account-level signal computed over a real membership edge, or by averaging users? | A membership relation exists with its own per-membership attributes, so a person's behavior *within this account* is distinct from the person and from the account. | User-level engagement is averaged into an account score with no membership model — a churned *user* is not a churned *account*, and an account with rotating staff gets mislabeled. (Schema exhibit: `usertour/usertour`'s user/company join table — licence AMBIGUOUS, cite the modelling idea only, lift no code.) |

## Verdict

After completing the checklist, state one of:

- **Usable as a prioritization device** — most rows pass; treat the score as a ranking tool paired
  with a stated gap and required action, never as a prediction.
- **Needs repair before use** — specific rows fail; list them and what closing each one requires.
- **Do not present as validated** — rows 1–2 fail; the score has never been checked against an
  outcome. It may still be usable as a prioritization device (per the reframe in
  `references/health-and-risk-signals.md` §6) but must never be described as predictive or
  accurate.
