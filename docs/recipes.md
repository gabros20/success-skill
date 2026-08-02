# Recipes

Use the invocation form supported by your client. The examples below use Codex's explicit
`$success` form.

## Deciding whether you need a dedicated success function yet

Use when: a founder or small team is being pushed toward CSM playbooks, health-score tooling, or a
QBR cadence, and nobody has checked whether the product actually needs any of it yet.

```text
Use $success to tell me whether we're big enough to need a dedicated customer-success function, or
whether growth/marketing/operate can still cover it.
```

Route: `when-success-applies` — the Existence Gate, anchored on the attributed test for whether CS
earns its keep: does the customer's growth change what they pay (seat expansion, usage-based
pricing, revenue share)? If yes, CS motion pays for itself; if the product is flat-rate self-serve,
a distinct function is optional until it visibly earns its cost. At solo/small-team scale the gate
also names what the evidence shows actually replaces a dedicated CS process — pricing first, then
AI tier-1 support, explicitly *not* documentation — carried as a contested-but-unopposed practitioner
position, not a settled fact. Output: an applies/lighter-weight/not-yet verdict naming which side of
the test the product is on, plus a pointer to whichever sibling pack (`marketing`, `growth`,
`operate`, `product`) already covers the gap in the meantime.

## Designing an onboarding program, not the in-app flow

Use when: "improve onboarding" has been requested and the actual gap is the plan and materials
around the product, not the in-product wizard or empty states.

```text
Use $success to design our onboarding program — the implementation plan and education artifacts
outside the product, not the in-app flow.
```

Route: `onboarding-and-adoption`, with the seam to `design` stated up front: design owns the
in-product onboarding *flow* (orient-don't-educate, wizards, empty states, aha-moment metrics);
success owns the onboarding *program* — the implementation/adoption plan, education artifacts
outside the product (docs, guides, enablement), and adoption over time. Time-to-first-value is
consumed from the PRD's acceptance criteria, never re-derived. Output: an onboarding program with
its education artifacts, and an explicit note of which flow-level decisions belong to `design`.

## Auditing a customer health score

Use when: a health score already exists — a red/yellow/green dashboard, a weighted formula, a
vendor tool — and nobody has checked whether it can actually predict anything.

```text
Use $success to audit our customer health score and tell me what it can honestly predict.
```

Route: `health-and-risk-signals` ⭐ — the flagship. Opens with the Observability Question: is your
churn event actually observable (a known cancellation date), or are you running a
contractual-shaped scoring template on a non-contractual product where "churn" isn't a single dated
event? Score-vs-prediction are treated as different artifacts even at the organization that
invested most visibly in both. The binding rule carried through the audit: **"not published," never
"not measured"** — no health-score vendor, no open-source project, and no in-house data-science team
studied in this pack's research has ever published a churn-model accuracy figure against real
outcomes; absence of disclosure is not proof of inaccuracy, but a reader can't verify what was never
published. Output: `assets/health_score_audit.md` completed — the ten-row checklist a score must
pass (input expiry dates, an outcome actually joined, override rules, a missing-data convention)
before anyone trusts the color it shows.

## Writing an AI support bot's escalation policy

Use when: a support bot is going into production and the handoff-to-human rule is still "when the
model isn't confident" — which no real implementation actually uses.

```text
Use $success to write our AI support bot's escalation policy — when it hands off, and how we'd know
if a vendor's "resolution rate" claim is trustworthy.
```

Route: `ai-support-policy` — success owns the policy, `ai` owns the mechanics. Escalation is
symbolic, never a confidence float: real implementations converge on named, non-numeric triggers
(scope boundary, explicit request or consent to an offered handoff, an admin-authored guardrail,
time-of-day, a structural pre-gate) — never a model-confidence threshold. The typed-field exemplar
(`anthropics/claude-quickstarts`) records mood alongside the redirect decision without ever letting
mood trigger it. Resolution-rate honesty: no source defines "resolution rate" precisely enough to
audit; a vendor headline stays graded vendor-claim regardless of how consistently it's repeated, and
τ-bench's pass^k is cited as the one measured instrument for reliability across repeated attempts —
never its specific published numbers, which the benchmark's own maintainers have since revised.
Output: a symbolic escalation-trigger set, a resolution definition paired with a
renewal/reopen signal, and an honest read of any vendor automation claim already in hand.

## Setting response-time SLAs you can actually keep

Use when: a support SLA needs setting and the instinct is to copy a template number ("First
Response: 1 hour") rather than derive one from actual coverage.

```text
Use $success to set our support response-time SLAs from our real capacity, not a copied template.
```

Route: `support-process-design` — first/next/resolution SLA naming, the three status buckets
convergent across decades of support-tooling schemas, and the never-ship rule against any SLA
default not derived from your own capacity: **an SLA is a promise made to a specific person, never
a copied template number.** Output: `assets/sla_capacity_calc.py` run against your actual coverage
(headcount, hours, time zones) to produce a response-time figure you can honestly promise, flagging
whether current volume already exceeds it.

## Reporting NRR without blending definitions

Use when: an NRR or GRR figure needs reporting, especially if it's about to be compared against a
competitor's or a previous quarter's number pulled from a different source.

```text
Use $success to report our NRR — and make sure I'm not comparing it to a number computed a different
way.
```

Route: `renewals-and-expansion` — four SEC filings (Snowflake, Datadog, HubSpot, Klaviyo), read
directly, each defining "net revenue retention" with a genuinely different mechanic: a two-year
snapshot, a rolling 12-month cohort, a monthly-cohort annualized average, and an ARR-weighted
rolling average with explicit reactivation handling. A reported 126% and a reported "above 130%"
computed under two of these are not the same kind of number and must never be compared as if they
were. Output: `assets/nrr_calc.py` run under one named, selected definition — self-tested against
the filings' own worked figures, never blended with another mode in the same report.

## Running a churn-save motion a growth test already validated

Use when: an experiment has shown a save offer works, and it needs to become a standing motion
someone actually runs on at-risk accounts.

```text
Use $success to turn this validated churn-save offer into a motion we run on at-risk accounts.
```

Route: `retention-execution` — success's reserved job name for the third box growth's own
standing-vs-experiment split leaves open: standing infrastructure is `operate`'s, the experiment
that proved the save works is `growth`'s, and the validated motion held as an ongoing relationship
is success's. The reason-to-offer save structure, targeting by uplift rather than raw risk rank, and
the voluntary/involuntary split applied before any churn conclusion. Output: a retention-execution
motion with its trigger, offer, and consent boundary, and the growth readout it was validated
against cited by name.
