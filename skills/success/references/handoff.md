# Handoff

Purpose: Map every seam between `success` and the rest of the family from success's side —
including three seams no sibling has drawn yet, because success ships after they did.

Read when:
- Downstream or upstream work is expected: a sibling pack will act on something success produced,
  or success needs an artifact a sibling owns.
- A request looks like it belongs partly to success and partly to another pack, and the boundary
  needs to be named rather than assumed.
- A sibling's own handoff file names no reciprocal row for success — that is not a gap in this
  pack's mandate, it is a pack that shipped before success existed.

Skip when:
- The request is fully inside one job with no downstream consumer in view — do the work in the
  relevant job reference and stop.

Inputs: whichever job produced the artifact in question, and which sibling pack is the named next
consumer or prior producer.

Produces: a named handoff — artifact, owner, and the line success does not cross — not a
restatement of the artifact itself.

## Contents

- The seam map
- Three rows this file originates
- Closing an open route: community retention
- The third box: retention execution
- Failure modes

## The seam map

| Sibling | What success hands it | What success consumes from it | The line success does not cross |
|---|---|---|---|
| `marketing` | Retention and churn signal that feeds messaging and CEP (customer engagement platform) work | Acquisition-side lifecycle content and the acquisition narrative, for onboarding continuity | Marketing's lifecycle job stops at acquisition; onboarding education and retention communication are success's — stated flatly, as marketing itself states it (`marketing/references/handoff.md:43`, its `surface-selfserve-saas.md` seam-at-signup section) |
| `growth` (provisional) | A validated retention motion sent — see "the third box" below | An experiment readout on a retention or resurrection mechanic | `growth` owns retention *experimentation* — does a nudge work; success owns retention *execution* — sending the message a growth test validated (`growth/references/handoff.md:43,49`) — cited provisional, matching growth's own hedge on this row, not flattened to marketing's confidence |
| `ai` | Policy artifacts — guidelines, exclusion edges, escalation policy, deflection-rate honesty (see [ai-support-policy](ai-support-policy.md)) | The support-assistant surface mechanics and its evaluation (`ai/references/surface-chat-assistant.md:9`) | `ai` owns mechanics, success owns policy — full seam in [ai-support-policy](ai-support-policy.md) |
| `design` | Nothing produced for design's own artifact; success states the seam explicitly instead | The in-product onboarding flow, and NPS's definition + survey method (`design/references/journeys.md:51-53`, `research.md:49`) | Design predates success and cedes nothing on disk; success draws this line from its own side. See [onboarding-and-adoption](onboarding-and-adoption.md) and [voice-of-customer](voice-of-customer.md) |
| `sales` (unbuilt, provisional) | The renewal workflow, up to a complex deal that needs negotiation | The expansion sale itself in a sales-assisted motion | Provisional, like growth drew its own sales seam. Lincoln Murphy's complexity-gated CS-native position — renewals should go to a dedicated CS-native resource, not "Account Management carryover" — is cited as contested vocabulary, not adjudicated. See [renewals-and-expansion](renewals-and-expansion.md) |

## Three rows this file originates

`product`, `operate`, and `automation` cede work to success in prose and router tables, but none of
their own `handoff.md` files carries a success row — success ships after all three, so there is no
reciprocal row to mirror. State that plainly rather than treating the absence as an oversight.

- **`product`.** `product/SKILL.md:28` cedes "adoption to `success`"; `surface-app-saas.md:45` routes
  "onboarding and support" here. Success hands back support, satisfaction, and churn evidence as
  discovery input, and consumes TTFV/repeat-trigger acceptance criteria from the PRD (see
  [onboarding-and-adoption](onboarding-and-adoption.md)). Product still models the commercial
  lifecycle — pricing tiers, metric trees, and the renewal/expansion terms named inside its own
  lifecycle (`surface-app-saas.md:31-32`) — success operates the renewal workflow and expansion
  signals, it does not re-derive the metric definitions or the pricing model (see
  [renewals-and-expansion](renewals-and-expansion.md)).
- **`operate`.** Its prose cedes to `product`/`success` in three places
  (`SKILL.md:90`, `incident-response.md:21,158-159`, `decommissioning.md:185-187`) with the family's
  sharpest boundary language: "Operate states fact, impact, and timing; it does not manage the
  relationship." But operate's own `handoff.md:79` names only `product` on its one customer-facing
  row. Success's row here: operate hands success the fact, impact, and timing of an incident or
  decommission; success (co-owned with product, never alone) turns it into customer-facing comms and
  manages the relationship. See [incident-and-account-comms](incident-and-account-comms.md).
- **`automation`.** Its `process-capture.md:15-17` already logged the gap in writing: the business
  rule behind a customer-facing action "is owned by `product`, `marketing`, `sales`, or `success` —
  read it and cite the owner… at this pack's launch those three commercial upstreams do not yet
  exist as shipped skills." Success's arrival closes part of that gap. Concretely: automation's
  refund-approval flagship (`assets/approval-policy-card.md:17,21,23`) is a support workflow end to
  end — success owns the support process that produces the ticket and the refund policy behind it;
  automation owns the approval gate. Neither owns the other's half.

## Closing an open route: community retention

`marketing/references/organic-social-and-community.md:17-18` routes retention inside an existing
community or product to "`success` **or** `growth`" — an unresolved fork shipped in a sibling. This
file resolves it: **success owns community-as-retention as a program; growth owns any retention
experiment run inside that community.** State explicitly, when this route is used, that it is
closing a previously open fork rather than picking a side silently.

## The third box: retention execution

`growth/references/handoff.md:43,66-67` names a job slot — `retention-execution` — that exists
nowhere else in the family and reserves it for this pack; use that literal name for the job (see
[retention-execution](retention-execution.md)). Growth's own working rule
(`growth/references/retention-and-resurrection.md:168-169`) classifies a retention or resurrection
mechanic into only two boxes: **standing** (`operate`'s) or **experiment-bound** (`growth`'s). This
pack draws the third box from its own side: a **validated motion, held as an ongoing customer
relationship**, is success's — the churn-save, win-back, or renewal-nudge sequence a growth test
already validated, now running as part of how success holds the relationship, not as a standing
system threshold or a live experiment.

## Failure modes

- Reporting a growth-validated retention readout as success's own finding, or reading a marketing
  handoff row and a growth handoff row as carrying equal confidence — mirror each sibling's own
  framing (marketing flat, growth provisional), never flatten the two.
- Reading `product`'s, `operate`'s, or `automation`'s missing success row in their own `handoff.md`
  as evidence success has no seam there — it means success shipped after they did; use the
  originated rows above.
- Treating the community-retention fork as still open after this file has resolved it.
- Claiming sole ownership of incident or decommission comms — always co-owned with `product`.
- Using the bare word "escalation" without qualifying it — the term is loaded across several
  sibling packs and inside support process itself. Success's escalation is always **customer
  escalation**; say so on every use, and read
  [support-process-design](support-process-design.md) §5 for the one disambiguation table this
  pack keeps.
- Silently invoking a sibling instead of naming the actual pack and the specific artifact it owns —
  the same discipline growth's own handoff requires of itself.
