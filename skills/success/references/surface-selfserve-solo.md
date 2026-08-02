# Surface: Self-Serve Solo (Default)

Purpose: State how success's jobs reshape when there is no CS team at all — the **default**
surface, because the family's own scoping note puts a solo or small-team, self-serve builder at
the center of this pack's likely reader (`digital-product-skill/docs/product-lifecycle-skill-packs-exploration.md:1033`).

Read when:
- No dedicated CS function exists — one founder or a small team is the entire success operation.
- Deciding whether to build tooling, adopt a paid tool, or keep handling it by hand.
- No surface has been chosen yet — this is where the router lands by default.

Skip when:
- A CSM-staffed portfolio, QBRs, or executive sponsors exist → [surface-b2b-high-touch](surface-b2b-high-touch.md).
- The product is a listed mobile app monetizing through app-store subscription →
  [surface-mobile-subscription](surface-mobile-subscription.md).
- An agent runs the success operation with no human in the loop by default →
  [overlay-agentic](overlay-agentic.md), layered on top of this surface, not instead of it.
- Whether success applies at all is still unsettled → [when-success-applies](when-success-applies.md).

Inputs: team size, whether an informal support channel already exists (a shared inbox, a founder's
personal email), and revenue scale.

Produces: which family jobs a solo operator does by hand versus automates, a tooling-adoption
threshold grounded in evidence rather than a guess, and an explicit no-CS-team statement instead of
borrowed enterprise machinery.

## Automation and AI tier-1 are the team, not a CSM

At this scale, the evidence shows automation and AI-run first-level support carrying the load a CSM
would elsewhere — not a documentation library, which tested weak in practice (see
[when-success-applies](when-success-applies.md) for the full correction). Two dated instances:
arvidkahl runs a "first-level AI CS agent" in production for Podscan
(https://x.com/arvidkahl/status/2081147490170991086, Jul 25 2026) and uses Crisp's live translation
to "speak fluent Japanese with my customers when needed" as a one-person answer to global coverage
(https://x.com/arvidkahl/status/1976293872926900665, Oct 9 2025). tylertringas folds a shared
support inbox into an agent loop that monitors errors, auto-pushes fixes, and reports back in Slack
(https://x.com/tylertringas/status/2074889104823664653, Jul 8 2026) — on-call collapsed into
automation for a team of one or two. Treat AI tier-1 as the default first line, with escalation
policy from [ai-support-policy](ai-support-policy.md) still applying at this scale, not relaxed
because the team is small.

## A tooling-adoption threshold, not a guess

Do not invent a number for "when do you professionalize support." The clearest evidence found is
dvassallo's own: "I'm in a stage in this business where I need a helpscout account. Almost $1M in
revenue and all email support happened from my personal email account (until now)." —
https://x.com/dvassallo/status/1736530664608989598 (Dec 17 2023). Note what changed: a tool, not a
hire — no first-hire-at-what-revenue number surfaced anywhere in this research, and that absence is
an honest gap, not a figure to invent.

## Coverage craft: what one person deliberately does not support

levelsio costs out why he refuses synchronous support calls on a self-serve product: "At $50k MRR
hourly rate of solo founder is $284/h… costs $852 to $1,420 to acquire one customer for a $99/mo
plan. No logic in doing calls for most ppl." — https://x.com/levelsio/status/1666385483935670273
(Jun 7 2023). Use this as the model — a stated, numerically justified refusal of a channel — not a
benchmark rate to copy. tylertringas's LIFO tactic (answer the most recent tickets first,
deliberately sacrificing average response time so some customers get an excellent one) is the
sharpest coverage trade-off found at this scale
(https://x.com/tylertringas/status/1287791800443441152, Jul 27 2020) — see
[support-process-design](support-process-design.md) for the full taxonomy this feeds.

## No-CS-team honesty on response-time and capacity

Never ship a default response-time number on this surface — the family's own research found "an
uncited SLA default becomes a promise made to someone else," and a solo operator is exactly the
reader least equipped to staff a borrowed template value. Derive a response-time commitment from
actual one-person (or small-team) capacity across whatever timezones apply, using
[support-process-design](support-process-design.md)'s `sla_capacity_calc.py`, rather than adopting
an example number from this file or anywhere else as a real commitment.

## Job-by-job reshape

| Job | How solo self-serve reshapes it |
|---|---|
| [onboarding-and-adoption](onboarding-and-adoption.md) | The adoption plan is lightweight — no QBR/EBR cadence; education artifacts are the highest-leverage spend |
| [support-process-design](support-process-design.md) | The "queue" is a shared inbox plus AI triage, not a tiered desk; capacity honesty replaces a borrowed SLA default |
| [education-and-knowledge-base](education-and-knowledge-base.md) | Docs-as-deflection tested weak in practice; a KB rewrite is the actionable lever, not a model upgrade |
| [ai-support-policy](ai-support-policy.md) | Escalation policy and deflection-rate honesty apply even at team-of-one — do not relax them because the team is small |
| [health-and-risk-signals](health-and-risk-signals.md) | Behavioral and tenure signals are cheaper and more honest here than a survey program requiring response volume this scale rarely has |
| [retention-execution](retention-execution.md) / [renewals-and-expansion](renewals-and-expansion.md) | Thin at this scale — a pricing-tier change (`product`'s) is often the actual lever; see the CONTESTED pricing-first correction in [when-success-applies](when-success-applies.md) |

## Failure modes

- Building CSM-portfolio machinery (QBR cadence, health-score tooling, a dedicated success hire) at
  a scale the evidence never shows anyone using it at — see
  [when-success-applies](when-success-applies.md)'s vocabulary-absence finding before recommending
  it.
- Shipping a bare response-time or SLA default instead of deriving one from actual capacity.
- Treating levelsio's or dvassallo's dollar figures as benchmarks rather than as one operator's
  own numbers, illustrating a judgment call.
- Recommending a hire when the evidence points at a tool, or vice versa — the dvassallo threshold
  above is a tooling change, not a headcount one; do not conflate the two.
