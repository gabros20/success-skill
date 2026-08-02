# W1 report — when-success-applies, onboarding-and-adoption, handoff, surface-selfserve-solo

## Files written (all under `success-skill/skills/success/references/`)

| File | Est. tokens | Budget |
|---|---:|---:|
| `when-success-applies.md` | 2,054 | 1,800 |
| `onboarding-and-adoption.md` | 1,827 | 2,000 |
| `handoff.md` | 1,728 | 2,000 |
| `surface-selfserve-solo.md` | 1,423 | 1,400 |

Estimates via `scripts/count-skill-tokens`. `surface-selfserve-solo.md` runs slightly over its
target (+1.6%) after two trim passes. `when-success-applies.md` runs +14% over target after a
controller-directed fold-in (below) that was explicitly "don't drop it" — both are well inside the
inventory's stated 1,200–2,200 band and the 2,500 hard ceiling; further cuts would have meant
dropping a citation or a ruling, which the standard says not to do to hit a budget.

**Post-report fold-in.** Controller assigned levelsio's "last part of customer support I still get
and can't automate" find (billing-confusion → chargeback, `_raw-x-solo-topup.md`,
https://x.com/levelsio/status/2035010864487555379, verified by tweet ID before use) into
`when-success-applies.md`'s AI-tier-1 point — the honest residue even a fully-automated solo stack
keeps. Added, then trimmed twice to limit the budget overrun; re-ran the never-ship grep after
(clean, exit 1/no matches).

Both files >100 lines (`when-success-applies.md`, `onboarding-and-adoption.md`) carry an early
`## Contents` block per the authoring standard; `handoff.md` (107 lines) also has one.
`surface-selfserve-solo.md` is 93 lines, no TOC needed.

## Router-row coverage (R18)

- **when-success-applies.md** — feeds the front-door job. Answers "does success apply yet," names
  the Existence Gate (arvidkahl test), states what covers post-purchase meanwhile, ships the
  CONTESTED pricing-first correction, and the canon-outcomes-survive/process-doesn't finding.
- **onboarding-and-adoption.md** — feeds the onboarding-program job. States the design/success seam
  explicitly (flow vs. program) before doing anything else, consumes TTFV from product's PRD,
  carries Murphy's current "Goal + AX" formula, and the marketing email-compliance cession.
- **handoff.md** — the full seam map from success's side: mirrors marketing (flat) and growth
  (provisional) with their own framing, *originates* rows for product/operate/automation (all three
  cede to success in prose but have no reciprocal handoff row — E's finding), closes the
  marketing-shipped community-retention fork (ruling 6), states growth's reserved
  `retention-execution` name and draws the third box (ruling 9), and states the escalation-vocabulary
  discipline as a failure mode.
- **surface-selfserve-solo.md** — the DEFAULT surface. Operationalizes the pricing/AI-tier-1
  correction job-by-job, gives the dvassallo tooling-adoption threshold (not a hire), the levelsio
  and tylertringas coverage-craft citations, and reinforces the never-ship SLA-default rule at the
  surface where it's most likely to be violated.

Every file's "Read when / Skip when" pair routes to a named sibling reference (design, product,
marketing, growth's handoff, or a sibling success job file) rather than a bare filename.

## Rulings applied

R1 (ruling 1, onboarding seam) — stated explicitly in `onboarding-and-adoption.md`'s first section,
not buried. R4 (involuntary churn → product) — cited via marketing's compliance-checklist line in
the same file. R6 (community-retention fork) — closed explicitly in `handoff.md`, stated as closing
a previously-open route, not a silent pick. R8 (AI-support seam) — referenced from `handoff.md` and
`surface-selfserve-solo.md`, full ruling deferred to W3's `ai-support-policy.md`. R9
(retention-execution name + third box) — implemented in `handoff.md`. R13 (no numbered invariants,
bolded named concepts) — "the Existence Gate" is the one named concept coined in this partition.
R14 (evidence grades inline) — every practitioner quote is graded P (practitioner-report, no
published method) in context. R16 (precision guards) — Murphy's CURRENT "Goal + AX" form cited, the
pre-2024 "Required Outcome + AX" explicitly dated as superseded; pricing plank marked CONTESTED in
two files, never presented as resolved. R17 (licensing) — no lifted text; all citations are
attributed quotes from cite-only/X sources. R18/R19 — sibling citations use pack+filename+line, and
growth is cited "provisional" while marketing is cited flat, matching each sibling's own framing
(never flattened). R20 — every X permalink was grep-verified against its raw file by tweet ID before
this report was written (11/11 verified against `_raw-x-solo-support.md`, `_raw-x-solo-topup.md`,
`_raw-x-lead-slice.md`); none reconstructed.

## Never-ship self-check

Grepped all four files for every listed string (5–25×, 5%→25–95%, 96% don't complain, 80/20, the
$1-vs-$6 deflection ratio, $2M ARR/CSM, the 76% Salesforce/Fin figure, 60–90-day/15–30%/68%
health-score and churn claims) and for bare SLA-default patterns (1 hour / 4 hour / 24-hour). Zero
matches (`grep` exit 1) across all four files. No figure in these four files is presented without
its source and P-grade; no response-time number is shipped as a default anywhere, including on the
solo surface where the temptation is highest — `surface-selfserve-solo.md` states the rule and
points to W2's `sla_capacity_calc.py` instead of an example number.

## Open items

- `handoff.md` still links to `voice-of-customer.md` and `retention-execution.md`, which did not
  exist at write time (W5's files); `renewals-and-expansion.md` and `incident-and-account-comms.md`
  (W6's) landed mid-session and those links now resolve. Not a defect in this partition — expected
  until all writers land; recommend the integrator's link-walk (R18) re-check after all six writers
  report.
- `onboarding-and-adoption.md` and `surface-selfserve-solo.md` cite `surface-b2b-high-touch.md`
  (W6's) for QBR/EBR machinery and mobile-subscription handling respectively — same as above, will
  resolve once W6 lands.
- SKILL.md's router table is untouched (integrator's job per inventory §4); none of my four files
  are yet linked from it, which `lint-skill` correctly flags and which is out of scope for a writer.
- The pricing-first-vs-support-quality contest (CONTESTED marking) is carried in both
  `when-success-applies.md` and echoed briefly in `surface-selfserve-solo.md`'s job table — intentional
  duplication is a one-line pointer, not a restatement, per R19 discipline.
