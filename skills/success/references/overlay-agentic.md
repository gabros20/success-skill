# Surface: Agentic (Additive Overlay)

Purpose: Add what changes when an AI agent operates support, health-signal response, or retention
motions itself — deciding and acting — without a human approving each instance. **This is an
overlay** — it stacks on [ai-support-policy.md](ai-support-policy.md),
[health-and-risk-signals.md](health-and-risk-signals.md), and
[retention-execution.md](retention-execution.md), and never replaces any of them. The escalation
triggers, resolution definition, and strict/fluid composition boundary don't change because a model
runs the loop; if anything, an agent that can act on a health score or close a ticket faster than a
human reviews it makes those definitions more load-bearing, not less.

Read when:
- A support agent decides and executes escalation, refund, or account actions without a human
  reviewing that specific instance.
- An agent reads a health score or risk signal and acts on it (a save offer, an account flag, a
  win-back send) as an ongoing process, not a single reviewed recommendation.
- Policy content (guidelines, journeys, canned responses) is deployed as configuration an agent
  consults live, not prose a human reads before each conversation.

Skip when:
- A human reviews the bot's proposed action before it fires — that's the base policy's normal
  workflow, not this overlay.
- The question is retrieval, prompt, or turn-loop mechanics — that's `ai`'s territory throughout.
- The question is a deterministic ceiling on a non-support agentic step (an experiment, a growth
  loop) — see growth's and automation's own agentic overlays; this file scopes to success's motions.

Inputs: which decisions in the support/health/retention lifecycle are model-decided rather than
human-approved per instance, and the escalation contract and resolution definition already set for
the surface in question (from [ai-support-policy.md](ai-support-policy.md)).

Produces: a structural (not instructional) ceiling on how much an unattended agent may act; a
required audit trail for every action it takes; confirmation that the counter-metric discipline and
the observability honesty layer were applied to the agent's own decisions, not silently skipped
because no human was watching.

## Contents
- [Policy artifacts become configs, not prose](#policy-artifacts-become-configs-not-prose)
- [Auditability by construction is no longer optional](#auditability-by-construction-is-no-longer-optional)
- [Guardrails for autonomous support operations](#guardrails-for-autonomous-support-operations)
- [The observability honesty layer gets sharper, not softer](#the-observability-honesty-layer-gets-sharper-not-softer)
- [Resolution gaming under autonomy](#resolution-gaming-under-autonomy)
- [The refund-approval seam](#the-refund-approval-seam)
- [Failure modes](#failure-modes)

## Policy artifacts become configs, not prose

When a human reads a policy before each conversation, prose ambiguity gets caught in the moment. When
an agent runs unattended, [ai-support-policy.md](ai-support-policy.md)'s guidelines, exclusion edges,
journeys, and canned responses stop being reference material and become deployed configuration the
agent consults live: versioned, testable before deploy, diffed on change. A guideline conflict a human
would silently resolve by judgment becomes a runtime branch the agent must resolve from the exclusion
edge alone. Treat an unreviewed guideline change the same as an unreviewed code change.

## Auditability by construction is no longer optional

The typed escalation field ([ai-support-policy.md](ai-support-policy.md)'s exemplar — a required,
logged field emitted every turn) is optional polish when a human reviews conversations directly. It is
the *only* mechanism left to retroactively review what an unattended agent did. Require it, plus a
logged resolution category (confirmed vs. assumed) per closed conversation, before granting an agent
authority to act without per-instance review — an agent that escalates, refunds, or closes without a
queryable record of why is reviewable only before the fact, never after.

## Guardrails for autonomous support operations

This pack adopts the same independence move the family's other agentic overlays name for any
unbounded agentic step: **pre-commit the rule before the run, enforce it structurally, not by
instruction.** Applied to success's motions specifically:

- **A rollout ceiling on how many conversations or accounts an agent may act on unsupervised**, set
  in the platform's own rollout control — the staged-rollout hash pattern (bucketing a conversation
  inside or outside an AI rollout for its whole lifetime, from
  [ai-support-policy.md](ai-support-policy.md)) is the concrete mechanism, not a prompt asking the
  agent to stay within a target.
- **A kill switch independent of the agent's own reasoning** — a `ServiceMode=HumanOnly` style gate
  silencing the agent on a conversation or account from outside its own decision loop.
- **A wall-clock or volume trigger that pauses autonomous action and requires human review**,
  enforced outside the agent's loop — the family's usual "deadline independent of whether the model
  believes it's still making progress" move, scoped here to a support or retention action.

## The observability honesty layer gets sharper, not softer

An agent that reads a health score and acts on it (a save offer, a customer escalation, an account flag) as an
ongoing process inherits [health-and-risk-signals.md](health-and-risk-signals.md)'s full honesty
layer unchanged — but the stakes rise: a human acting on an unaudited score at least applies judgment
at the moment of action; an agent acting automatically applies none. **An agent may not treat a health
score as ground truth for an automated action unless the score's honesty checklist (backtested or
goal, expiry dates current, override rules present) has been verified for the specific score driving
that action** — not verified once at build time and assumed stable thereafter.

## Resolution gaming under autonomy

[ai-support-policy.md](ai-support-policy.md)'s counter-metric discipline (pair resolution with
renewal, never ship resolution alone) is a recommendation for a human-reviewed bot. For an unattended
agent it is a structural requirement: an agent optimizing its own resolution rate **fails by
continuing, not by erroring** — it keeps closing tickets the cheapest way available unless a
counter-metric is wired into the pipeline outside its own loop, not left as a dashboard a human might
check. Wire the renewal or human-override check between "conversation closes" and "counted as
resolved."

## The refund-approval seam

An agent that decides a refund is warranted *and* has authority to issue it is the sharpest instance
of this overlay's stakes: success owns the support process and refund policy (when a refund is
warranted, per what criteria); `automation` owns the irreversible-action approval gate itself. Cite
`automation`'s `references/approval-and-authority.md` for the gate
mechanism — do not re-derive an approval workflow here. This overlay only states that an
agent-decided refund still passes through that gate structurally, exactly as a human-initiated one
would.

## Failure modes

- An agent granted escalation or refund authority with no logged, queryable record of which trigger
  fired — auditability retrofitted after an incident is not auditability by construction.
- A rollout or volume ceiling enforced only by prompt instruction rather than the platform's own
  allocation control — the same gap the family's other agentic overlays flag as the single
  highest-consequence one.
- An agent acting on a health score whose honesty checklist was verified once at build time and never
  re-checked as the score's inputs drifted.
- Treating "the agent didn't report a problem" as evidence a counter-metric held, without confirming
  the renewal/override check actually ran against the agent's own closed conversations.
- A guideline or policy config changed without the same review discipline as a code change, because
  no human reads it per-conversation to catch the drift informally.
