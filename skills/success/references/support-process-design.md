# Support Process Design

Purpose: Design the ticket taxonomy, SLA metrics, and escalation vocabulary a support operation
runs on — an SLA is a promise made to a specific person, never a copied template number.

Read when: setting up or auditing a ticket status/priority/category taxonomy; defining SLA
metrics or a response-time promise; "escalation" is used and its meaning is unclear; a solo/small
team needs an honest answer on what response time it can cover.

Skip when: the question is AI-agent escalation policy or bot boundaries →
[ai-support-policy](ai-support-policy.md); KB content or deflection measurement →
[education-and-knowledge-base](education-and-knowledge-base.md); a standing on-call/paging policy
for internal incidents → `operate`'s SLO, not this file's customer-facing promise.

Inputs: current/planned ticket fields, team size and coverage hours, any existing SLA numbers (and
their source).

Produces: a taxonomy with tie-breakers, SLA metrics tied to an honest capacity check, and a
qualified escalation vocabulary.

## Contents

- [1. Two taxonomy axes: state and topic](#1-two-taxonomy-axes-state-and-topic)
- [2. A category list without tie-breakers is not a taxonomy](#2-a-category-list-without-tie-breakers-is-not-a-taxonomy)
- [3. SLA metrics: three names, one convergent shape](#3-sla-metrics-three-names-one-convergent-shape)
- [4. The response-time promise, and the never-ship SLA default](#4-the-response-time-promise-and-the-never-ship-sla-default)
- [5. "Customer escalation" — always qualified](#5-customer-escalation--always-qualified)
- [6. Priority: one field, unless you're doing formal ITSM](#6-priority-one-field-unless-youre-doing-formal-itsm)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## 1. Two taxonomy axes: state and topic

A ticket needs two independent classifications, and conflating them is the most common taxonomy
error: **what state is it in**, and **what is it about**.

**State — three canonical buckets, independently converged.** Four systems built 30 years apart —
RT (1996, `initial`/`active`/`inactive`), Frappe Helpdesk (`category` ∈ Open/Paused/Resolved,
*enforced* on every custom status), libredesk (`conversation_status_category` ENUM
`open`/`waiting`/`resolved`, same enforcement), Zammad (`state_type` categories collapsing to the
same shape) — schema-verified, converge on **something-to-do / something-paused-on-someone-else /
something-finished**. Frappe and libredesk are strongest: they *constrain* admin-defined labels to
one of exactly three machine-meaningful categories, not just document the convention. Divergences
worth keeping: "resolved" vs "closed" (most: distinct; FreeScout: same) and how many flavors of
"paused" exist (most: one; Zammad: two — personal snooze vs waiting-on-someone-external;
django-helpdesk: none by default). Frappe's `label_agent`/`label_customer` split — the same status
reads differently to agent vs customer — is the best small idea here.

**Topic — an eight-category first-party taxonomy, with an off-ramp bucket.** Anthropic's own
shipped reference (`anthropics/claude-quickstarts@main:customer-support-agent/app/lib/
customer_support_categories.json`, MIT) categorizes contacts as `account`/`billing`/`feature`/
`internal`/`legal`/`other`/`technical`/`usage`. The teachable row is **`internal`** (auto-reply,
forward, ignore, spam, sales reroute) — a first-class bucket for contacts that are **not support at
all**. No open-source helpdesk schema examined reserves such a bucket. Ship it explicitly: a
taxonomy that forces every inbound message into a support category will misclassify spam, sales
leads, and auto-replies as support work.

## 2. A category list without tie-breakers is not a taxonomy

A list of category names resolves nothing when a real ticket sits on the boundary between two of
them. Two sources converge on the same fix — write the tie-break rule down, not just the
categories:

- **Root-cause-drives-category, with an explicit default.** Anthropic's ticket-triage skill
  (`anthropics/knowledge-work-plugins@ea31164:customer-support/skills/ticket-triage/SKILL.md:121-
  124,126`, Apache-2.0): "If they can't log in due to a bug, category is Bug (not Account) — root
  cause drives the category," and for the genuinely ambiguous case, "When in doubt, lean toward
  Bug — it's better to investigate than dismiss." The second line is the pattern worth copying: a
  named default direction, stated as policy.
- **GitLab's health-score risk taxonomy** applies the same discipline elsewhere: two axes (risk
  impact, cause) with explicit exclusion rules for the boundary case. **"A category list without
  tie-breakers is not a taxonomy"** — hold this line for every taxonomy this pack ships.

## 3. SLA metrics: three names, one convergent shape

**first_response / next_response / resolution** is the convergent metric set: Chatwoot's schema
(`chatwoot/chatwoot@bc7ae88:db/schema.rb:1374-1385`, MIT, Ruby, 2019-era) names
`first_response_time_threshold`/`next_response_time_threshold`/`resolution_time_threshold`;
libredesk's schema (`abhinavxd/libredesk@main:schema.sql:19-22`, Go, 2026-era) independently names
an ENUM with the same three — different language and decade, near-identical fields. Zammad's
exception is instructive: **four** timers, with a validation **forbidding** `response_time` and
`update_time` on the same policy at once (`zammad/zammad@develop:app/models/sla.rb:17-20,38-42`) —
pick one "next contact" metric, not both.

**The clock stops while waiting on the customer — universally, and always a named state, never
implicit.** Frappe makes `Paused` a first-class value of `agreement_status`, with `on_hold_since`/
`total_hold_time` accounting fields and `first_response_failed_by`/`resolution_failed_by` duration
fields that quantify *how badly* a breach missed, not just that it did (AGPL-3.0 — structure/naming
LIFTABLE as ideas, not code). Zammad puts a `pending_time` column directly on the ticket row —
the pause-until instant. libredesk's `applied_sla_status` stays `pending` until a deadline
resolves, and typed-enums a **pre-breach warning** distinct from the breach itself. Ship "the clock
pauses on customer-wait, as a named state" as settled design, not a choice to relitigate.

## 4. The response-time promise, and the never-ship SLA default

**The response-time promise is unclaimed territory.** `operate` owns internal SLOs; nobody owns the
customer-facing promise of *when a human will reply*. It surfaces once, buried in a healthcare
vertical playbook (`webdesign/references/niche-and-vertical-design.md:148-156`, grep-verified
nowhere else across twelve shipped packs): state a response time **at the point of action** — near
the submit button, not a buried FAQ — and stage intake so routing-critical fields come first. This
pack owns that doctrine generally; cite webdesign's file as the one prior mention.

**The never-ship class: an unsourced SLA default becomes a promise made to someone else.** The
ground-zero example is in this pack's own research corpus: Anthropic's shipped ticket-triage skill
hardcodes a P1–P4 hour-count table with no citation or stated source
(`anthropics/knowledge-work-plugins@ea31164:customer-support/skills/ticket-triage/SKILL.md:130-
168`) — a template default, framed as prescriptive, from a first-party official skill. **Never ship
an SLA number without "set this from your own observed capacity" framing** — a response-time
commitment is a number you owe someone, not a fact to look up.

**Solo capacity honesty.** Run `assets/sla_capacity_calc.py` to check whether a stated response
time is geometrically possible given the actual coverage schedule, and whether volume already
exceeds capacity before any SLA number is chosen. Grounding data points (practitioner-report,
first-person, no independent audit): ticket volume varies by channel by an order of magnitude —
"PayPal users need about 10x more support emails than credit card signups through Stripe"
(x.com/levelsio/status/657777387866824704, Oct 24 2015) — so measure per channel, never assume; under overload,
**LIFO triage** ("switch to Last In, First Out… so at least some customers will get exceptionally
fast support rather than all of them getting the (probably not great) average response time,"
x.com/tylertringas/status/1287791800443441152, Jul 27 2020) trades fairness for some excellence
over uniform mediocrity; and one operator's professionalization point was **tooling, not hiring** —
"almost $1M in revenue and all email support happened from my personal email account until now"
(x.com/dvassallo/status/1736530664608989598, Dec 17 2023).

## 5. "Customer escalation" — always qualified

**This section is the pack's single disambiguation home** — every other file states the rule and
points here rather than re-listing the senses. The bare word "escalation" is loaded four ways
family-wide (operate's on-call paging, automation's workflow escalation, ai's confidence-based
handoff, quality's severity escalation). Support process adds **two distinct meanings of its own**;
conflating them is a real error, not a style nit:
- **SLA-breach notify-and-reassign** — the default meaning in every stack but one. Chatwoot's
  `automation_rules` is the most quotable template: conditions (`status`, `priority`,
  `assignee_id`, …) × actions (`assign_team`, `change_priority`, `resolve_conversation`, …), with an
  `execution_delay` knob for "escalate if still true after N minutes"
  (`chatwoot/chatwoot@bc7ae88:app/models/automation_rule.rb:35-42`, MIT).
- **Automatic priority bump** — django-helpdesk's distinct mechanism: `Queue.escalate_days` raises
  an unresolved ticket's priority after N days
  (`django-helpdesk/django-helpdesk@main:src/helpdesk/settings.py:145-151`, BSD-3-Clause). Name it
  separately rather than treat the two as synonyms.

Always write **"customer escalation"**, never the bare word. A support *organization's*
escalation-for-visibility policy ("escalate early — visibility across GitLab, up to and including
the CEO, is always better earlier rather than later," GitLab support handbook, CITE-ONLY) is a
third, distinct
object — who gets told, not which ticket state changes — note it, don't merge it in.

## 6. Priority: one field, unless you're doing formal ITSM

Every pure support tool in the sample uses a single ordinal priority field, 4–5 levels, or
free-text with none (libredesk). **GLPI alone implements the ITIL impact×urgency matrix**
(`glpi-project/glpi@11.0/bugfixes:src/CommonITILObject.php:3329-3333`, GPL-3.0, structure-only):
priority is *computed* from two inputs via a configurable lookup table. GLPI also carries 8 live
statuses against a helpdesk's 4–6, because ITSM must model scheduled work and change-approval
gates that don't exist in support — **ITSM taxonomy ⊃ support taxonomy.** Teach the matrix as
over-engineering unless doing formal ITSM: the honest default for a solo/SMB team is one field.

**A monetization boundary worth naming.** FreeScout's open-source core ships no priority field, SLA
model, or automation engine — confirmed by an empty `Modules/` directory
(`freescout-help-desk/freescout@dist:Modules/.gitkeep`); those are paid add-ons — informative about
what "process" costs to build.

## Validation

- Every shipped taxonomy states both axes (state, topic) and names its tie-breaker, per §2.
- No SLA number appears without a citation or "set this from your own observed capacity" framing,
  per §4, and a solo/small-team claim has been run through `sla_capacity_calc.py` first.
- "Escalation" never appears bare; always "customer escalation," mechanism named when it matters,
  per §5.

## Failure modes and handoff

- **A borrowed SLA table (industry defaults, a competitor's numbers, an AI-generated table) ships
  as this team's commitment** — stop; recompute from `sla_capacity_calc.py` and the team's own
  coverage schedule, per §4.
- **A taxonomy ships categories but no stated tie-breaker** — not a taxonomy per §2.
- **"Escalation" appears unqualified in a cross-pack artifact** — a reader may resolve it against
  the wrong pack's meaning; qualify it as "customer escalation."
- **AI-agent escalation policy or bot-boundary design is being decided here** — route to
  [ai-support-policy](ai-support-policy.md); this file owns the human-process vocabulary the AI
  layer inherits, not the agent's decision logic.
- **Deflection or help-content questions surface mid-taxonomy-work** — route to
  [education-and-knowledge-base](education-and-knowledge-base.md) instead of answering them here.
