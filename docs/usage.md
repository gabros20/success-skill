# Usage reference

## Activation

`success` should trigger on requests about the customer relationship **after** the sale: deciding
whether a dedicated success function is worth building yet, planning or auditing onboarding as a
program (not the in-app flow), defining what belongs in a knowledge base, designing or auditing a
support-ticket taxonomy or SLA, setting policy for an AI support bot, building or auditing a health
score or churn model, interpreting an NPS/CSAT/CES score or feedback trend, running a churn-save or
renewal-nudge motion, running a renewal or reporting NRR/GRR, or writing customer-facing incident or
decommission communication. Realistic triggers: "do we need a customer-success function yet,"
"design our onboarding program," "what should our knowledge base cover," "set up our support ticket
taxonomy and SLAs," "write our AI support bot's escalation policy," "audit our health score," "is
our NPS trend actually meaningful," "run this churn-save motion," "report our NRR," "write the
customer email for this incident."

It should **not** trigger on: "build the in-product onboarding flow, wizard, or empty state"
(`design`), "does this retention or resurrection mechanic actually work" (`growth` — an
*experiment*, not the relationship it validates), "set pricing tiers, or fix dunning/billing-failure
recovery" (`product`), "build the support assistant's retrieval, memory, or evaluation harness"
(`ai`), "set the internal SLO or page an on-call engineer" (`operate`), "write the acquisition
lifecycle email or the case study copy" (`marketing`), "close the expansion sale" (`sales`,
unbuilt), "grade tests or decide the ship gate" (`quality`), or "implement any of this in
production code" (`frontend` / `backend` / `ai`) — unless the request also requires the CS program,
policy, or relationship judgment itself.

Use `/success` as documentation shorthand only. Codex explicit invocation is `$success`; other
clients use an `@` mention, a skill tool, or natural-language activation.

## Mission and boundary

`success` holds the customer relationship after the sale, and owns the epistemics that come with
it — which signals about that relationship can carry a decision, and which cannot. It writes
programs, policies, taxonomies, verdicts, and workflows: onboarding programs, help content and KB
strategy, support-process design, AI-support policy, health and churn-risk audits,
voice-of-customer interpretation, retention-execution motions, renewal and expansion workflows, and
incident/decommission communication. It never writes production code and never invents a figure it
cannot source. Its nearest handoffs are `growth` (retention experiments and readouts), `design`
(the in-product onboarding flow and NPS survey method), `product` (pricing and dunning), `ai` (the
support assistant's mechanics and evals), `operate` (internal SLOs and incident facts), and
`marketing` (acquisition-side lifecycle communication and case-study production).

## Workflow

1. Establish whether a distinct success function applies at all — the Existence Gate — then the one
   primary job and the base surface, adding the agentic overlay only when a model acts on support,
   health, or retention without per-instance human review. State any assumed surface explicitly.
2. Name what is actually being decided, and who owns that decision once the artifact exists.
3. Consume upstream artifacts as given (a PRD's time-to-first-value, `design`'s onboarding flow,
   `growth`'s readout, `operate`'s stated incident fact) and cite them by pack and filename rather
   than re-deriving them.
4. Grade every figure relied on — measured-with-method, practitioner-report, or vendor-claim — and
   state where its evidence stops.
5. Produce the artifact with a named proof source behind every claim.
6. Run the honesty checks that apply: the Observability Question for anything predictive, capacity
   for anything promised, the voluntary/involuntary split for anything about churn, the denominator
   for anything about survey response.
7. State plainly what the artifact cannot support, and emit a compact handoff when downstream work
   is expected.

## Route by job

| User intent | Reference or script | Expected contribution |
|---|---|---|
| Decide whether a distinct success function is worth building yet | `references/when-success-applies.md` | The Existence Gate — the attributed test, what covers post-purchase work meanwhile, the pricing-first correction at solo scale |
| Build an onboarding implementation/adoption plan | `references/onboarding-and-adoption.md` | The onboarding **program**, distinct from the in-product flow; TTFV consumed from the PRD |
| Decide what belongs in the knowledge base, or answer a deflection claim | `references/education-and-knowledge-base.md` | A definition of good help content; article-lifecycle rule; zero-result/zero-click backlog |
| Set up or audit a ticket taxonomy, SLA, or response-time promise | `references/support-process-design.md` | Two taxonomy axes, three convergent status buckets, SLA naming, the response-time promise |
| Define bot handoff, "resolved," or read a vendor automation claim | `references/ai-support-policy.md` | Symbolic escalation triggers, the typed-field exemplar, resolution-rate honesty |
| Build, buy, interpret, or audit a health score or churn model ⭐ | `references/health-and-risk-signals.md` | **Flagship.** Score-vs-prediction, "not published, never not measured," the Observability Question |
| Read an NPS/CSAT/CES score or feedback trend | `references/voice-of-customer.md` | Interpretation only; aggregate trend reading; the survey-response-denominator check |
| Run a churn-save, win-back, or renewal-nudge motion | `references/retention-execution.md` | The validated motion held as a relationship; target by uplift; voluntary/involuntary split |
| Run a renewal or report an NRR/GRR figure | `references/renewals-and-expansion.md` | Four audited NRR definitions, never compared across; expansion signals graded |
| Write incident or decommission customer communication | `references/incident-and-account-comms.md` | Co-owned with `product`; success manages the relationship, originates no technical claim |
| Compute NRR/GRR under a selected, named definition | `assets/nrr_calc.py` | Self-testing calculator; four modes, never blended |
| Check a churn model's headline accuracy | `assets/churn_baseline_check.py` | Naive-baseline comparison plus a leakage-flagging sanity band |
| Derive an honest response-time promise | `assets/sla_capacity_calc.py` | What your actual coverage supports, and whether volume already exceeds it |
| Audit an existing health score | `assets/health_score_audit.md` | Ten-row checklist a score must pass before anyone trusts a color |

## Outputs and completion

| Output | Complete when |
|---|---|
| Existence-gate verdict | Names which side of the attributed test the product is on, not a size-based guess |
| Onboarding program | States the design-owned in-product flow as a separate artifact; TTFV cited from its source |
| KB / help-content plan | Article set tied to observed zero-result/zero-click queries, not guessed coverage |
| Support taxonomy / SLA | Every category has a tie-breaker; every response-time figure is derived from stated capacity |
| AI-support policy | Every escalation trigger is named and non-numeric; resolution and deflection claims carry their grade |
| Health-score / churn audit | The Observability Question is answered; "not published" stated where no accuracy figure exists |
| VoC read | The response denominator is stated; no NPS/CES claim exceeds its replication evidence |
| Retention-execution motion | Voluntary/involuntary split made before any churn conclusion; targeting is by uplift, not raw risk |
| Renewal / NRR report | The exact definition used is named and never blended with another |
| Incident/account comms | Technical claims are attributed to `operate`/`product`; the relationship framing is success's own |

When downstream work is expected, the skill provides artifact paths, owners, the residual risk, and
a recommended next skill — typically `growth`, `product`, `ai`, `marketing`, or `operate` — without
duplicating the full artifact.
