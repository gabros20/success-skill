# Incident and Account Comms

Purpose: Manage the customer relationship during an incident or a decommission without duplicating
or contradicting what `operate` states — success owns the relationship, never the technical fact.

Read when:
- An incident affects a specific account or a customer-facing status update is needed.
- A service, feature, or dependency is being decommissioned and affected customers need notifying.
- A promised response time is being confused with an internal SLO.

Skip when:
- The question is what response time is honestly promisable at all →
  `support-process-design.md` owns the SLA-as-promise mechanics and the capacity math; this file
  owns the relationship conversation once a promise already exists.
- The incident has no customer-facing dimension → `operate`'s incident-response.md handles it
  alone.

Inputs: operate's stated fact, impact, and timing (for an incident) or a decommission's sunset
date and technical sequencing (for a decommission), and the affected account(s).

Produces: customer-facing communication that stays inside success's lane — relationship
management — without restating or contradicting operate's technical facts, and a clear split
between the promise made to a customer and the internal target behind it.

## Co-ownership, always

Customer-facing incident and decommission communication is co-owned by `product` and `success` —
never success alone. `operate` states this from its own side, twice: "Writing customer-facing
incident copy or per-account outreach — that is `product`/`success`"
(`operate/references/incident-response.md:21`), and again at the point of decommission: an
unresolved customer-facing consequence "routes to `product`/`success` for the outreach — this file
owns the technical and data-disposition sequencing, not the customer conversation"
(`operate/references/decommissioning.md:186`).

## The split: operate states, success manages

Operate's own boundary, verbatim: "Operate states fact, impact, and timing; it does not manage the
relationship" (`operate/references/incident-response.md:159`). In practice: operate decides what
is true right now, the user-visible impact scoped honestly, and when the next update lands — never
a root-cause claim before the postmortem is done, never a severity downgrade framed as reassurance.
Success (with product) takes that stated fact and manages the account conversation around it —
acknowledging impact, setting expectations, handling an account's specific follow-up. Success does
not originate the fact, impact, or timing, and it does not soften or reframe them either — a
customer conversation that contradicts operate's stated timeline is a failure mode, not a
relationship-management choice.

## Decommission outreach

The same split applies to a decommission or dependency withdrawal: `operate` owns the technical and
data-disposition sequencing — what gets deleted, when, and the retention-obligation check before it
does; `product`/`success` own the outreach — the sunset date communicated, the migration path
offered, account-level follow-up. Operate's own artifact is inconsistent about this today: its
handoff table names only `product` as the customer-facing recipient of a decommission notice
(`operate/references/handoff.md:79`), while its prose cites both `product` and `success`
(`decommissioning.md:186`). That is a known, queued fix on operate's side, not a signal that
success's claim is wrong — until it lands, success should expect to originate this row in its own
handoff rather than find a reciprocal one waiting.

## Customer-facing promise vs. internal SLO

The response-time a customer is told ("we'll respond within X") and the internal target a team is
measured against are not the same artifact and must not collapse into one. The internal SLO belongs
to whichever team is accountable for the underlying work; the customer-facing promise is success's
to make, and it must be set from actual capacity, never copied from a template —
`support-process-design.md` covers the capacity math and the never-ship rule against unsourced SLA
defaults. This file's job is narrower: once a promise exists, keep the account conversation honest
against it during an active incident, and never let an internal target leak into a customer
conversation as if it were the promise made to them.

## Validation

- Every customer-facing incident or decommission message traces its factual content to operate's
  (or product's) stated fact, impact, and timing — success has not originated a technical claim.
- The message manages the relationship rather than restating operate's status-page content
  verbatim.
- A promised response time is checked against `support-process-design.md`'s capacity math, not
  assumed.

## Failure modes and handoff

- Success states a root cause before operate has confirmed one → wait for operate's stated fact;
  do not speculate in order to look responsive.
- A decommission notice ships before the retention-obligation check operate's own procedure
  requires → block the outreach until operate confirms the sequencing is done.
- An internal SLO is quoted to a customer as if it were their promised response time → apply the
  split above; restate as the actual promise.
- Recommended next: `operate`'s incident-response.md and decommissioning.md for the technical
  procedure this file's messaging depends on; `support-process-design.md` for the response-time
  promise mechanics.
