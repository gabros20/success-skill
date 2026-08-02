---
name: success
description: >-
  Keep customers after they buy — does a success function apply yet, onboarding programs, help
  content and KB, support process, SLAs as promises, AI-support policy, health and churn-risk
  honesty, voice-of-customer interpretation, retention execution, renewals/expansion (NRR),
  incident comms. Use to design a support process, audit a health score, or run a churn-save or
  renewal. Not in-product onboarding flow (→ design), retention experiments (→ growth),
  pricing/dunning (→ product), agent mechanics/evals (→ ai), internal SLOs (→ operate), lifecycle
  email (→ marketing), the sale (→ sales).
---

# Customer Success

## Mission and boundary

**Hold the customer relationship after the sale, and be honest about what you can actually know
about it.** Success owns the post-purchase jobs — the onboarding program, help content, the support
process, AI-support policy, health and risk signals, voice-of-customer interpretation, retention
execution, renewals and expansion, and the customer's side of an incident — and it owns the
epistemics that come with them: which of those signals can carry a decision, and which cannot.

**What makes this pack different: it answers whether the score works.** The genre is fragmented —
one artifact has reach but almost none of the canonical jobs, one is official but purely tactical,
one is architecturally complete but cites nothing and assumes an enterprise CSM team. One of them
already asks whether a health score predicts churn rather than merely classifying accounts; none
answers it with evidence, with honest scope, or integrated across support and AI-agent policy. The
flagship, [health-and-risk-signals](references/health-and-risk-signals.md) ⭐, does all four — and
asks first what the canon never asks: **the Observability Question**, whether your churn event is
observable at all.

**The default reader is a builder with users, not a CS team with a book of accounts.** So the front
door is a gate, not a playbook: [when-success-applies](references/when-success-applies.md) decides
whether a distinct success function is worth having yet, because no source in the canon answers
that. Where the enterprise canon still teaches something, lift its *epistemics* — input expiry,
segmented thresholds, ignorance-as-a-finding, tie-breakers — and decline its *machinery* (CSM
ratios, QBR cadence) with reasons stated, never by omission.

`success` writes programs, policies, taxonomies, verdicts, and workflows — **no production code**,
no experiments, and no numbers it cannot source. See "Not this skill" below.

Operate independently when invoked alone. When compatible upstream artifacts are provided (a PRD's
time-to-first-value criteria, a growth readout, an operate incident statement), use them without
silently overriding established decisions. Recommend adjacent skills when useful; do not invoke them
automatically unless the user explicitly requested a composition workflow.

## Route before acting

1. **Run the existence gate first** whenever the request assumes a success function exists and has
   not justified it — read [when-success-applies](references/when-success-applies.md) before
   producing a health score, a CSM playbook, or a renewal workflow.
2. Identify the **one primary job** and the **one base surface**. Read one of each. **If the request
   names no business model, do not stall** — assume the default surface (self-serve solo) and say
   which you assumed.
3. Add the **agentic overlay on top of** a base surface, never instead of one:
   [overlay-agentic](references/overlay-agentic.md) when a model decides and acts on support,
   health, or retention without a human reviewing that instance.
4. **Grade every figure inline** — measured-with-method > practitioner-report > vendor-claim. A
   vendor number stays vendor-claim even when quoted in order to refute it.
5. **Never re-teach a sibling's owned mechanic.** NPS's definition and survey method are `design`'s;
   the metric tree is `product`'s; the retention *experiment* is `growth`'s; the turn loop and evals
   are `ai`'s — cite them by pack and filename, never re-derive them.
6. Read every selected reference completely before producing the affected artifact.
7. Do not load unrelated references.

### Jobs

| User intent | Read | Contribution |
|---|---|---|
| Decide whether a distinct success function is worth building yet, or whether a CS request should be answered by another pack for now | [when-success-applies](references/when-success-applies.md) | **The Existence Gate** — the attributed test (does the customer's growth change what they pay), what covers post-purchase meanwhile, and the CONTESTED pricing-first correction: at solo scale the replacement for CS process is pricing, then AI tier-1 support — not docs |
| Build an implementation/adoption plan, education artifacts outside the product, or an adoption cadence | [onboarding-and-adoption](references/onboarding-and-adoption.md) | The onboarding **program**, with the design seam stated up front — design owns the in-product flow and its orient-don't-educate rule; time-to-first-value consumed from the PRD, never re-derived; Murphy's current Goal + Appropriate Experience formula, with the superseded form dated |
| Decide what belongs in a knowledge base, keep it from rotting, or answer a deflection claim | [education-and-knowledge-base](references/education-and-knowledge-base.md) | The family's first definition of good help content (reactive KB vs proactive documentation); an article-lifecycle rule; **the zero-result/zero-click backlog as the observable replacement for an unmeasurable deflection rate**; check KB coverage before a model upgrade |
| Set up or audit a ticket taxonomy, SLA metrics, a response-time promise, or escalation vocabulary | [support-process-design](references/support-process-design.md) | Two taxonomy axes and the schema-converged three status buckets, plus the internal/"this isn't support" bucket; first/next/resolution SLA naming; **the response-time promise** — and the never-ship rule against any SLA default not derived from your own capacity; the one home for the "customer escalation" disambiguation |
| Define when a bot hands off, what "resolved" means, or how to read a vendor's automation claim | [ai-support-policy](references/ai-support-policy.md) | Success owns the policy, `ai` owns the mechanics: **escalation is symbolic, never a confidence float** (nine real triggers, none numeric), the typed-field-every-turn exemplar, strict-vs-fluid composition, resolution-rate honesty (confirmed vs assumed), pass^k against vendor claims, and the chatbot-promises-bind precedent |
| Build, buy, interpret, or audit a health score, churn model, or renewal-risk signal ⭐ | [health-and-risk-signals](references/health-and-risk-signals.md) | **Flagship.** Score-vs-prediction as different artifacts; **"not published, never not measured"** and the null-result triangle; **the Observability Question** (contractual vs non-contractual churn); four-study academic convergence; the honest ML ceiling with its leakage and base-rate exhibits; the reframe — score plus mandatory gap and action |
| Read an NPS/CSAT/CES score or a feedback trend honestly | [voice-of-customer](references/voice-of-customer.md) | Interpretation only — three siblings already define the metric; adds what none claims: aggregate trend reading, the Display-vs-Response denominator check, the NPS-growth and CES-superiority replication failures, and the corrected complaint-rate range |
| Run a churn-save, win-back, or renewal-nudge motion a test already validated | [retention-execution](references/retention-execution.md) | `growth`'s reserved job name, and **the third box** — standing is `operate`'s, experiment-bound is `growth`'s, a validated motion held as a relationship is success's; the reason→offer save structure; target by uplift, not risk rank; the one-click-reachable ethics test; voluntary/involuntary split before any conclusion |
| Run a renewal, evaluate an expansion signal, or report an NRR/GRR figure | [renewals-and-expansion](references/renewals-and-expansion.md) | Product models, success operates, sales closes (provisional); **four audited NRR definitions that are not one metric** — never compared across; NNR as the canon outcome that survives without the canon process; expansion signals labeled folklore; advocacy stops at qualification and consent |
| Communicate with customers during an incident or a decommission | [incident-and-account-comms](references/incident-and-account-comms.md) | Co-owned with `product`, always — `operate` states fact, impact, and timing; success manages the relationship and originates no technical claim; the customer-facing promise and the internal SLO kept as separate artifacts |

Emitting for downstream work, or naming a boundary → [handoff](references/handoff.md) — the seam map
from success's side, including the three rows success originates because it shipped after `product`,
`operate`, and `automation` did, and the community-retention fork it closes.

### Surfaces

| Surface | Read | When |
|---|---|---|
| Self-serve solo or small team — no dedicated CS function | [surface-selfserve-solo](references/surface-selfserve-solo.md) | **Default** |
| B2B high-touch — named CSM, service tier, account-level score | [surface-b2b-high-touch](references/surface-b2b-high-touch.md) | The canon's home turf: the epistemics to lift and the machinery to decline, with reasons |
| Mobile-app subscription | [surface-mobile-subscription](references/surface-mobile-subscription.md) | Store-review responses, a cancellation path the developer does not control, platform-run billing retry |
| **Agentic (additive overlay)** | [overlay-agentic](references/overlay-agentic.md) | **Stacks on a base surface.** A model decides and acts on support, health, or retention without per-instance human review |

## Not this skill

| Ask | Goes to |
|---|---|
| In-product onboarding UX — wizards, empty states, progressive disclosure, onboarding copy, the aha-moment pattern; NPS's definition and survey method; KB navigation and information architecture | `design`. Design owns the in-product onboarding **flow**; success owns the onboarding **program** — the plan, the education artifacts outside the product, and adoption over time |
| Whether a retention or resurrection mechanic works — designing or reading out that experiment | `growth` — provisional. `growth` owns retention *experimentation*; success owns retention *execution*, the motion a growth test validated. Cancellation dark-pattern ethics live in growth's monetization file; success applies the one-click-reachable test and ships none of it |
| Pricing tiers and the commercial-lifecycle model, the metric tree, PRD acceptance criteria, dunning and billing-failure recovery | `product`. Product models; success operates. Involuntary churn is product's mechanism — success requires the voluntary/involuntary split before drawing a retention conclusion |
| The support assistant's turn loop, retrieval, memory, prompts, and eval instrumentation | `ai`. Success sets the escalation condition, the resolution definition, and the bot boundaries; `ai` measures compliance with them |
| Internal SLOs, alerting, on-call paging, running the incident, decommission sequencing | `operate`. Operate states fact, impact, and timing; success manages the relationship. The customer-facing response-time **promise** is success's; the internal target is not |
| Positioning, acquisition-side lifecycle email, content, store listings and ASO, producing case studies and testimonials | `marketing`. Onboarding education and retention communication are success's; marketing produces the advocacy asset success qualified and got consent for, and keeps the store listing while success answers the reviews |
| The warehouse metric definition, the tracking plan, PII governance on free-text support content | `data`. Success inherits data's free-text-PII constraint rather than inventing one |
| The approval gate on an irreversible action — a refund above a threshold | `automation`. Success owns the support process that produces the request and the refund policy; automation owns the gate |
| Negotiating and closing an expansion sale | `sales` — provisional and contested; see [renewals-and-expansion](references/renewals-and-expansion.md) §6 |
| Verification, defect triage, the ship/no-ship gate | `quality`. Success triages customer tickets, not build defects |
| Implementing any of it in production code | `frontend` · `backend` · `ai`. Success ships programs, policies, and workflows, never code |

## Universal invariants

- **Run the Existence Gate before building the apparatus.** A health score, a CSM playbook, or a
  renewal workflow requested for a product that has not passed the gate gets the gate first, and a
  named sibling pack for the meantime — never a silently invented artifact.
- **Say "not published," never "not measured."** No source discloses a health-score or churn-model
  accuracy figure against real outcomes. Absence of disclosure is not proof of inaccuracy — but a
  reader cannot verify what was never published.
- **Ask the Observability Question before scoring anything.** In a contractual setting churn is
  observed on a known day; in a non-contractual one it is not observed at all, and a
  contractual-shaped template is the wrong instrument.
- **Score-vs-prediction are different artifacts.** A health diagnostic and a churn prediction are
  not the same thing even at the org that invested most visibly in both. A score alone next to a
  renewal date is folklore; a score with a stated gap and a mandatory action is a ranking device.
- **A category list without tie-breakers is not a taxonomy** — ticket categories, churn reasons, and
  feedback reasons alike. Write the rule for the boundary case, and name a default direction.
- **An SLA is a promise made to a specific person, never a copied template number.** No
  response-time figure ships without "set this from your own observed capacity" framing.
- **Grade every figure inline** — measured-with-method > practitioner-report > vendor-claim — and
  carry the method with the number, or say "method unknown."
- **A disclaimed figure is still a figure.** Never name a never-ship number in order to forbid it;
  state the mechanism and point at the primary source instead.
- **Always write "customer escalation."** The bare word is loaded across four sibling packs and
  three senses inside support process itself.
- **Lift the epistemics, decline the machinery — with reasons.** A stakeholder who asks for a CSM
  ratio or a QBR cadence gets a reasoned decline and the question it was trying to answer, never
  silence and never a borrowed benchmark.

## Core workflow

1. Establish whether success applies at all; then the one primary job and the base surface, adding
   the agentic overlay only if a model acts without per-instance review. State any surface assumed.
2. Name what is actually being decided, and who owns that decision once the artifact exists.
3. Consume upstream artifacts as given — the PRD's time-to-first-value, `design`'s onboarding flow
   and NPS definition, `growth`'s readout, `operate`'s stated fact — and cite them by pack and
   filename rather than re-deriving them.
4. Grade every figure, benchmark, or "best practice" relied on, and state where its evidence stops.
5. Produce the artifact — a gate verdict, program, taxonomy, policy, score audit, motion, or
   workflow — with a named proof source behind every claim.
6. Run the honesty checks that apply: the Observability Question for anything predictive, capacity
   for anything promised, the voluntary/involuntary split for anything about churn, and the
   denominator for anything about survey response.
7. State plainly what the artifact cannot support, and emit a compact handoff when downstream work
   is expected.

## Artifact contract

A success artifact is incomplete unless it carries: the gate verdict or an explicit statement that
success already applies · every figure with its source and evidence grade · the seam — which sibling
pack owns the adjacent half, cited by pack and filename · what the artifact **cannot** support (a
score that has never met an outcome, a promise not derived from capacity, a trend without its
denominator) · and, where a ruling is provisional or a position contested, that label carried
forward rather than flattened into confidence it does not have.

Programs, policies, taxonomies, audits, and workflows are delivered as documents. None is delivered
as production code.

## Completion and handoff

Before completion:

- Confirm every requested artifact exists and every claim in it has a proof source — an unsourced
  percentage is not a finished line.
- Confirm no figure travels without its method or an explicit "method unknown."
- Distinguish what was independently verified from what is vendor-reported, self-selected, or
  practitioner-reported.
- State plainly what this artifact will and will not be able to prove.
- When downstream work is expected, provide artifact paths, owners, residual risk, and a recommended
  next skill — typically `growth` to test a motion, `product` when the fix is pricing or the
  commercial model, `ai` to build the assistant this policy governs, `marketing` for a qualified
  advocacy handoff, or `operate` when the customer conversation depends on a technical procedure.

## Resources

The routing tables above link all 15 references. Assets are runnable and self-testing except the
checklist: [nrr_calc.py](assets/nrr_calc.py) — the four audited NRR definitions as selectable modes,
never blended · [churn_baseline_check.py](assets/churn_baseline_check.py) — headline accuracy against
the naive baseline, plus a concordance sanity band that flags leakage ·
[sla_capacity_calc.py](assets/sla_capacity_calc.py) — what response time your actual coverage can
honestly promise, and whether volume already exceeds capacity ·
[health_score_audit.md](assets/health_score_audit.md) — the ten-row audit a score must pass before
anyone trusts a color. Eval suites live in the repository's `evals/` directory.

Attribution, licences, and what this pack claims for itself — `SOURCES.md` at the repository root.
