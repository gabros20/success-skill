# Onboarding and Adoption

Purpose: Build the onboarding **program** — the implementation/adoption plan and the education
artifacts that live outside the product — and state explicitly where it stops, because a shipped
sibling already owns the in-product flow this canonical include sounds like it should claim.

Read when:
- Building an implementation or adoption plan, docs, a guide, or an enablement session that lives
  outside the product surface itself.
- Consuming time-to-first-value (TTFV) as an acceptance criterion someone else already defined.
- Adoption over time needs a cadence (30/60/90-day check-ins, a milestone plan) rather than a single
  onboarding moment.

Skip when:
- The request is in-product onboarding UX — wizard steps, empty states, progressive disclosure,
  onboarding copy, the aha-moment pattern itself → `design/references/journeys.md`. This file does
  not redesign that flow; it cites it.
- The question is whether a success function is warranted at all →
  [when-success-applies](when-success-applies.md).
- The request is KB/help-content structure or article strategy →
  [education-and-knowledge-base](education-and-knowledge-base.md).

Inputs: the product's PRD-stated TTFV and repeat-trigger acceptance criteria (if it exists),
whatever in-product onboarding flow design already shipped, and the audience/segment this plan
targets.

Produces: an implementation/adoption plan, education artifacts that live outside the product
(docs, guides, enablement sessions), an adoption-over-time cadence, and — where none exists yet — a
plain statement of the design/success seam so the plan does not read as a re-do of design's work.

## Contents

- [The seam, stated explicitly](#the-seam-stated-explicitly)
- [Consuming TTFV as an input, not deriving it](#consuming-ttfv-as-an-input-not-deriving-it)
- [The implementation/adoption plan](#the-implementationadoption-plan)
- [Education artifacts outside the product](#education-artifacts-outside-the-product)
- [Adoption over time](#adoption-over-time)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## The seam, stated explicitly

This is the sharpest contested seam in the family, and it must be named or this file reads as a
land-grab against a shipped sibling. `design/references/journeys.md:51-53` already ships a
dedicated onboarding doctrine: "Goal priority: get to first value fast > orient (**don't educate**)
> build confidence > reduce setup friction. Onboarding's job is the **aha moment**, not teaching the
product." Its patterns (progressive disclosure, setup wizard, sample-data demo, interactive tour)
and metrics (activation rate, time-to-activation, completion, drop-off by step, D7/D30 retention)
are design's, not this file's to redo. `design/references/content.md:45` also owns the copy layer:
"Empty states are onboarding moments in three beats: name what is empty, say why it matters, give
one button." And `design/references/content.md:58` sets the voice rule directly against this
canonical include's name: onboarding voice is "contextual, not a tutorial."

**The seam: `design` owns the in-product onboarding *flow* — patterns, empty states, wizard
mechanics, copy, the metrics that describe it. This file owns the onboarding *program* — the
implementation/adoption plan, the education artifacts that live outside the product (docs, guides,
enablement sessions), and adoption over time.** Design's own journey map already runs the arc
through the parts this pack also touches — "discovery → purchase → first run → onboarding → daily
use → failure → support/billing/offboarding" (`design/references/journeys.md:49`) — which is a
reason to cite that map rather than draw a second one, not a reason to avoid the program work.
"Education and enablement" as a canonical include is not in tension with design's "don't educate" —
design's rule is about the in-product moment; this file's education artifacts live *outside* it,
for the adopter who needs more than an empty-state prompt to get value.

## Consuming TTFV as an input, not deriving it

Product hands this file its acceptance criteria rather than a bare recommendation.
`product/references/surface-app-saas.md:35-36` states plainly: "Onboarding and the core loop are
always first-class scope sections, not implicit. State time-to-first-value and the loop's repeat
trigger as acceptance criteria." `:45` routes onboarding and support execution to this pack. Consume
that PRD input directly; do not re-derive a TTFV number from scratch, and do not present
"activate within N days → X% more likely to continue" style figures as measured — the underlying
evidence for TTFV-causes-retention claims is, per the family's web research, **unsourced vendor
folklore in every instance traced**, not a study. If TTFV framing is used at all, say "widely
believed, not measured," and use the PRD's own stated number, not a benchmark.

## The implementation/adoption plan

Build the plan around Lincoln Murphy's Desired Outcome framework, the most honestly-portable piece
of the CS canon (it is pitched by its own author as applying "regardless of company size"):

> "When our customer achieves their Desired Outcome through their Relationship with us, leading them
> to stay longer, buy more, and advocate for us." — https://www.sixteenventures.com/customer-success-definition/

Desired Outcome, current formula: **Goal + Appropriate Experience**. Murphy's own site states his
framework changed: the classic "Required Outcome + Appropriate Experience" formula is his
**pre-2024, superseded** formulation — cite the current "Goal + AX" form, or date the older one
explicitly if there is a specific reason to reference it. Appropriate Experience is "primarily the
Interaction Content, Channel(s), and Cadence that a customer segment requires to 'feel'
successful" (same source) — this is the plan's actual content: which content, on which channel, at
what cadence, gets this specific customer segment to their stated goal. A plan that names a generic
"onboarding sequence" without naming the segment's goal and appropriate channel/cadence has not done
this job.

## Education artifacts outside the product

Docs, setup guides, migration guides, and enablement sessions belong here, scoped by segment and
goal from the plan above — not as a generic content library. If the plan includes onboarding email
content, it inherits an obligation from a shipped sibling: `marketing/assets/email-compliance-checklist.md:81`
already assigns "Onboarding education after signup" to this pack inside a runnable compliance
checklist, not just in prose — treat that checklist item as binding, not optional. Dunning and
billing-failure recovery stay `product`'s per the same asset (`:82`); do not fold involuntary-churn
communication into onboarding education.

## Adoption over time

The program does not end at first value. Structure a cadence (e.g., 30/60/90-day check-ins, a
milestone sequence tied to the segment's Desired Outcome) rather than a single onboarding event, and
tie each milestone back to the Appropriate Experience the segment needs — a cadence with no stated
AX rationale is busywork, not adoption design. For the account-level version of this work in a
sales-assisted or high-touch motion — QBRs, executive sponsorship, portfolio cadence — see
[surface-b2b-high-touch](surface-b2b-high-touch.md), which carries Murphy's QBR-is-optional
critique at full depth; this file stays scoped to the plan and its content, not the meeting cadence
around it.

## Validation

- The plan states the seam against `design`'s onboarding flow rather than silently redoing it.
- TTFV and repeat-trigger criteria are consumed from the PRD, not invented.
- Any TTFV-causes-retention claim is labeled "widely believed, not measured."
- The Desired Outcome formula cited is the current "Goal + AX" form, or the older form is
  explicitly dated.
- Onboarding email content is checked against marketing's compliance checklist item, not assumed
  clean.

## Failure modes and handoff

- Redesigning the in-product onboarding flow (wizards, empty states, copy) instead of citing
  `design/references/journeys.md` and staying scoped to the program.
- Citing Murphy's pre-2024 "Required Outcome + AX" formula as if it were current.
- Presenting an unsourced "X% more likely to retain if activated by day N" figure as measured.
- Building a generic onboarding email sequence with no stated Desired Outcome or Appropriate
  Experience rationale, and skipping the compliance-checklist item marketing already ceded.
- Treating adoption-over-time cadence design as this file's business when the actual gap is
  account-level QBR/EBR machinery — route to
  [surface-b2b-high-touch](surface-b2b-high-touch.md) instead of inventing enterprise ritual here.
