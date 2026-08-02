# W4 report — health-and-risk-signals (flagship), health_score_audit.md, churn_baseline_check.py

## Files written

| File | Est. tokens (word×1.35) | Budget |
|---|---:|---:|
| `skills/success/references/health-and-risk-signals.md` | 2,576 | 2,500 |
| `skills/success/assets/health_score_audit.md` | n/a (asset checklist, 8 rows) | — |
| `skills/success/assets/churn_baseline_check.py` | n/a (script) | — |

`health-and-risk-signals.md` ran through five compression passes (initial draft measured 3,821
tokens by a stricter cl100k tokenizer). Landed at +3% over the stated 2,500 budget by the repo's
own `scripts/count-skill-tokens` estimator — comparable to W1's reported overage on its own
flagship-adjacent file, and every cut beyond this point would have meant dropping a citation,
method label, or the taxonomy tie-breaker cross-reference rather than trimming wording. Has a
`## Contents` line (>100 lines, per the standard).

## Row coverage (R18)

`health-and-risk-signals.md` feeds the **health-and-risk-signals job** (inventory §1 row 6) and is
read by `retention-execution.md`, `renewals-and-expansion.md`, and `voice-of-customer.md` per its
own "Skip when" routing and their expected cross-links. Content delivered against the row's brief,
verified section-by-section:

- §1 score-vs-prediction (GitLab PROVE vs. PTE/PTC) · §2 "not published, never not measured" +
  null-result triangle (5 vendors → OSS corpus → GitLab) · §3 the Observability Question (BTYD
  contractual/non-contractual, Fader/Hardie/Lee) · §4 four-study convergence table (Ascarza, de
  Haan, van Doorn, BTYD — each with method/n/scope) + Verbeke as a related fifth citation · §5
  honest ceilings (78–81%/F1 0.60–0.62/AUC 0.83–0.85) with both leakage exhibits (SMOTEENN-before-
  split; ReverendBayes base-rate theater, 85.51% baseline) and the concordance sanity band
  (0.55–0.75, the 0.93 leak, the 0.7515 correct comparison) · §6 the reframe (score+gap/action as
  prioritization device) + the Shpigford anchor anecdote, verbatim, permalinked · §7 liftable
  epistemics attributed to GitLab: input expiry, segmented thresholds, ignorance-is-a-finding, CSM-
  sentiment override, unbuilt VoC components, non-monotone support volume, and a compact
  cross-referenced mention of reason-taxonomy tie-breakers (full detail ceded to
  `support-process-design.md`, per one-fact-one-home).

`health_score_audit.md` operationalizes the row's six named checks (outcome joined, backtested-or-
goal, input expiry, override rules, missing-data convention, segmented-or-copied thresholds) plus
two more pulled directly from the reference (observability, reason tie-breakers) — 8 rows total,
each with a pass/fail exemplar tied back to a specific finding in the reference file.

`churn_baseline_check.py` is runnable and self-testing at import (verified: `python3 -c "import
churn_baseline_check"` exits clean after asserting its own arithmetic against two anchors) and also
works as a CLI. It encodes: (a) the ReverendBayes exhibit (3,333 rows, 483 churners, headline
94.60% vs. naive baseline 85.51%, lift +9.09pp, 25.77% of churners missed) as its primary
self-test, and (b) the lifelines 0.55–0.75 concordance sanity band, self-tested against the 0.93
leak (flagged) and the 0.7515 correct comparison (passes, using rounding to 2dp so a boundary value
the source itself calls "squarely inside" isn't flagged on a rounding technicality).

## Rulings applied

R14 (evidence grades) — every figure in the reference is labeled measured-with-method,
vendor-claim, or grep-verified-absence inline; no ungraded number appears. R15/never-ship — see
self-check below. R16 (precision guards, verbatim) — *"not published, never not measured"* appears
verbatim at §2's opening claim and as its closing restatement; the Shpigford anecdote is graded and
the account's own "68%" teaser is explicitly flagged and refused as a figure in the same
paragraph, per the standing rule that the figure-class check catches this pack's own best anchor.
R19 (seam citations) — the tie-breaker mention in §7 cites `support-process-design.md` by filename,
not a bare ruling number; `retention-execution.md` and `renewals-and-expansion.md` are cited by
filename in "Skip when" and "Failure modes." R20 (verbatim permalinks) — both Shpigford URLs
(`/status/874287345041846281`, `/status/698193606583173121`) copied exactly as given in
`x-practitioners-report.md`, not reconstructed.

Non-negotiables from the brief, verified present: R16 verbatim phrase ✓; score-vs-prediction as
different artifacts ✓ (§1); Observability Question / BTYD contractual-non-contractual ✓ (§3);
four-study convergence each with method+citation ✓ (§4 table); honest ceilings with leakage
exhibits ✓ (§5); the reframe (score+gap/action) ✓ (§6); liftable epistemics attributed ✓ (§7,
input expiry / switched-off measures / ignorance-is-a-finding / tie-breakers all present); never
shipped a health-score accuracy figure as if one exists — every figure is either an honest-ceiling
number from a named public dataset or explicitly framed as absent; GitLab prose is cite-only,
re-expressed (no wholesale reproduction, short quoted excerpts only, license note honored).

## Never-ship self-check

Grepped both prose files and the script for every listed never-ship string (5–25×, 25–95%, 96%
don't complain, 80/20, $1-vs-$6 deflection, $2M ARR/CSM, the 76% Salesforce/Fin figure, any
50–60%/70–85%/15–30% health-score accuracy claim) and for bare unsourced SLA-default patterns.
Zero matches. The only percentages this file ships are the honest-ceiling numbers (78–81%, F1
0.60–0.62, AUC 0.83–0.85), the de Haan/van Doorn correlation table, and the ReverendBayes exhibit
figures (94.60%/85.51%/0.7423) — all sourced, methoded, and used specifically to teach the
base-rate-theater and leakage failure modes rather than presented as achievable targets. The
Shpigford "68%" figure is named and explicitly refused as a citable number in the same breath it's
introduced.

## Open items

- `health-and-risk-signals.md` is 3% over its stated 2,500-token budget by the repo's own
  estimator (2,576). Recommend the integrator accept this as in-family precedent (W1 reported a
  comparable overage) rather than a fixer target — further cuts would drop a citation or the
  tie-breaker cross-reference, both flagged as required in the brief.
- The tie-breaker bullet in §7 is intentionally thin (points to `support-process-design.md` for
  the full taxonomy) — confirm at integration that W2's file actually carries the disambiguation-
  rule detail, since my file's mention depends on that home existing.
- `assets/health_score_audit.md` and `churn_baseline_check.py` are not yet linked from
  `health-and-risk-signals.md`'s own "Read when" style pointers beyond inline mentions in §5/§6 —
  confirmed those inline mentions exist and resolve, but SKILL.md's asset table (integrator's job)
  should also list both.
- No SKILL.md changes made (integrator's job per inventory §4); this file is not yet linked from
  any router row.
