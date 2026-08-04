# success — Customer Success

**Family hub:** [digital-product-skill.vercel.app](https://digital-product-skill.vercel.app) — the 15-skill Digital Product family and its composer.

**Keep the customer relationship after the sale — and be honest about what you can actually know
about it.**

`success` is the **Improve** stage of the [Digital Product Skills](https://github.com/gabros20)
family, pairing with `growth`: growth learns what works, `success` does the work and holds the
relationship. It covers the post-purchase jobs a product needs once someone has already bought —
deciding whether a dedicated success function is worth building yet, the onboarding *program*, help
content and the knowledge base, support-process design and SLAs, AI-support policy, customer health
and churn-risk signals, voice-of-customer interpretation, retention execution, renewals and
expansion (NRR), and the customer's side of an incident.

## What makes this pack different

Customer-success skills already exist, but none of them integrate, and almost none of them cite a
source. One popular churn-prevention skill covers 2 of the 12 topics a CS function typically needs
and cites nothing. Anthropic's own official customer-support pack is well-built but ticket-triage
only — no onboarding, no health score, no renewals. The most complete example anywhere (81 skills)
cites zero external sources and is barely used. None of them ask the one question that actually
matters: **does a health score predict who's about to churn, or does it just sort accounts into
colored buckets?**

This pack asks that question and answers it, with evidence and honest limits, in its flagship
reference, [health-and-risk-signals](skills/success/references/health-and-risk-signals.md) ⭐. It
starts from **the Observability Question** — is your churn event even observable, or are you
running a contractual-shaped scoring template on a product where "churn" isn't a single dated
event? No health-score vendor, no open-source project, and not even GitLab's own in-house
data-science team has ever published a churn-model accuracy figure against real outcomes. This pack
says so plainly: **"not published," never "not measured."** A score with a stated gap and a
mandatory next action is a useful ranking device; the same score alone next to a renewal date is
folklore — and the pack shows the difference on real, cited evidence rather than asserting it.

The rest of the pack carries the same discipline. It opens with **the Existence Gate**
([when-success-applies](skills/success/references/when-success-applies.md)) because no source in
the customer-success canon says when a distinct success function actually becomes worth having —
the whole literature assumes the function exists and only asks how to staff it. At solo and
small-team scale, the pack teaches what the evidence actually shows replaces a dedicated CS
process: pricing first, then AI tier-1 support — not documentation, which was the working
hypothesis until the research contradicted it. Every figure in the pack is graded inline —
measured-with-method beats practitioner-report beats vendor-claim — and a long list of familiar
retention statistics (the "5% retention lift → 25–95% profit" claim, "5–25× cheaper to retain,"
NPS as "the best predictor of growth," the "96% of unhappy customers never complain" line) failed
verification against their own primary sources and are marked never-ship, with the honest version
taught in their place.

## Install

```bash
npx skills add gabros20/success-skill -g -y
```

Or use it in Codex with `$success`. Manual copy also works — copy `skills/success/` into your
client's skills directory.

## Examples

```text
$success are we big enough yet to need a dedicated success function, or is this still growth's job

$success design an onboarding program for our B2B tool — not the in-app flow, the plan around it

$success audit our customer health score and tell me what it can honestly predict

$success write the escalation policy for our support bot — when does it have to hand off to a human

$success set response-time SLAs we can actually keep, not a copied template number

$success report our NRR — and don't let me blend it with the wrong SEC definition
```

## What it does

A **faceted router**: pick one primary job × one base surface, then add the agentic overlay only
when a model acts on support, health, or retention without a human reviewing that instance.

**Primary jobs** — when-success-applies · onboarding-and-adoption · education-and-knowledge-base ·
support-process-design · ai-support-policy · **health-and-risk-signals ⭐** · voice-of-customer ·
retention-execution · renewals-and-expansion · incident-and-account-comms.

**Surfaces** — self-serve solo (default) · B2B high-touch · mobile-app subscription ·
**agentic (additive)**.

## Route by job

| User intent | Reads | Contribution |
|---|---|---|
| Decide whether a distinct success function is worth building yet | [when-success-applies](skills/success/references/when-success-applies.md) | **The Existence Gate** — the attributed test for whether CS earns its keep, what covers post-purchase work meanwhile, and the pricing-first correction for solo scale |
| Build an implementation/adoption plan and education artifacts outside the product | [onboarding-and-adoption](skills/success/references/onboarding-and-adoption.md) | The onboarding **program**, distinct from the in-product flow `design` owns; time-to-first-value consumed from the PRD, never re-derived |
| Decide what belongs in a knowledge base, keep it from rotting, or answer a deflection claim | [education-and-knowledge-base](skills/success/references/education-and-knowledge-base.md) | A working definition of good help content; an article-lifecycle rule; the zero-result/zero-click backlog as a measurable stand-in for an unmeasurable deflection rate |
| Set up or audit a ticket taxonomy, SLA metrics, or a response-time promise | [support-process-design](skills/success/references/support-process-design.md) | Two taxonomy axes, the three status buckets convergent across three decades of support tooling, first/next/resolution SLA naming, and the response-time promise |
| Define when a support bot hands off, what "resolved" means, or how to read a vendor's automation claim | [ai-support-policy](skills/success/references/ai-support-policy.md) | Escalation as a set of named triggers, never a confidence float; the typed-field-every-turn exemplar; resolution-rate honesty; vendor deflection claims graded against the one measured instrument that exists |
| Build, buy, interpret, or audit a health score, churn model, or renewal-risk signal ⭐ | [health-and-risk-signals](skills/success/references/health-and-risk-signals.md) | **Flagship.** Score-vs-prediction as different artifacts; "not published, never not measured"; the Observability Question; the honest ML ceiling, with its leakage and base-rate exhibits |
| Read an NPS/CSAT/CES score or a feedback trend honestly | [voice-of-customer](skills/success/references/voice-of-customer.md) | Interpretation only — the metric definitions belong to siblings; adds aggregate trend reading and the survey-response-denominator check |
| Run a churn-save, win-back, or renewal-nudge motion a test already validated | [retention-execution](skills/success/references/retention-execution.md) | The relationship-side motion `growth` validated and `operate` doesn't own; target by uplift, not risk rank; the voluntary/involuntary split before any conclusion |
| Run a renewal, evaluate an expansion signal, or report an NRR/GRR figure | [renewals-and-expansion](skills/success/references/renewals-and-expansion.md) | Four audited NRR definitions that are not one metric and are never compared across; expansion signals labeled folklore where the evidence doesn't hold up |
| Communicate with customers during an incident or a decommission | [incident-and-account-comms](skills/success/references/incident-and-account-comms.md) | Co-owned with `product`; `operate` states fact, impact, and timing, `success` manages the relationship and originates no technical claim |

Plus [handoff](skills/success/references/handoff.md) — the seam map to the rest of the family.

## Surfaces

| Surface | Reads | When |
|---|---|---|
| Self-serve solo or small team — no dedicated CS function | [surface-selfserve-solo](skills/success/references/surface-selfserve-solo.md) | **Default** |
| B2B high-touch — named CSM, service tier, account-level score | [surface-b2b-high-touch](skills/success/references/surface-b2b-high-touch.md) | The canon's home turf: which of its habits to lift and which to decline, with reasons |
| Mobile-app subscription | [surface-mobile-subscription](skills/success/references/surface-mobile-subscription.md) | Store-review responses, a cancellation path you don't control, platform-run billing retry |
| **Agentic (additive overlay)** | [overlay-agentic](skills/success/references/overlay-agentic.md) | **Stacks on a base surface.** A model decides and acts on support, health, or retention without per-instance human review |

## Outputs

A success artifact carries: the gate verdict, or a statement that a success function already
applies · every figure with its source and evidence grade (measured-with-method,
practitioner-report, or vendor-claim) · the seam — which sibling pack owns the adjacent half, cited
by pack and filename · and what the artifact **cannot** support: a score that has never met an
outcome, a promise not derived from real capacity, a trend read without its denominator.

Programs, policies, taxonomies, audits, and workflows are delivered as documents — never as
production code.

## Digital Product lifecycle

`success` sits at the **Improve** stage of the Digital Product Skills family, alongside `growth`:
growth learns what works through experimentation, `success` does the work of holding the customer
relationship afterward. It does not own the in-product onboarding flow (`design`), retention
*experiments* (`growth`), pricing tiers or dunning (`product`), the support assistant's mechanics
and evals (`ai`), internal SLOs (`operate`), lifecycle email (`marketing`), or closing an expansion
sale (`sales`, unbuilt). It consumes upstream artifacts — a PRD's time-to-first-value, `design`'s
onboarding flow, a `growth` readout, `operate`'s stated incident facts — when they're supplied,
works standalone when they aren't, and hands off a compact artifact, typically to `growth` to test a
motion, `product` for a pricing fix, `ai` to build the governed support assistant, `marketing` for a
qualified advocacy handoff, or `operate` when the conversation depends on a technical procedure.

## The family

| Skill | Stage | Repository |
|---|---|---|
| `product` | Shape | [product-skill.vercel.app](https://product-skill.vercel.app) |
| `design` | Shape | [designskill.vercel.app](https://designskill.vercel.app) |
| `architecture` | Shape | [architecture-skill.vercel.app](https://architecture-skill.vercel.app) |
| `frontend` | Build | [frontendengskill.vercel.app](https://frontendengskill.vercel.app) |
| `backend` | Build | [backendengskill.vercel.app](https://backendengskill.vercel.app) |
| `data` | Build | [data-skill.vercel.app](https://data-skill.vercel.app) |
| `ai` | Build | [aiengskill.vercel.app](https://aiengskill.vercel.app) |
| `automation` | Build | [automation-skill.vercel.app](https://automation-skill.vercel.app) |
| `quality` | Assure | [quality-skill.vercel.app](https://quality-skill.vercel.app) |
| `operate` | Run | [operate-skill.vercel.app](https://operate-skill.vercel.app) |
| `marketing` | Distribute | [marketing-skill.vercel.app](https://marketing-skill.vercel.app) |
| `growth` | Improve | [growthskill.vercel.app](https://growthskill.vercel.app) |
| `success` | Improve | this repository |

## Reference and asset library

15 references under `skills/success/references/` (10 primary jobs, 3 base surfaces, 1 agentic
overlay, 1 handoff contract) and 4 assets under `skills/success/assets/`, all runnable and
self-testing except the checklist:

- **Assets:** `nrr_calc.py` — the four audited NRR/GRR definitions as selectable modes, never
  blended · `churn_baseline_check.py` — headline accuracy checked against the naive baseline, with
  a leakage-flagging sanity band · `sla_capacity_calc.py` — what response time your actual coverage
  can honestly promise, and whether volume already exceeds it · `health_score_audit.md` — the
  ten-row audit a health score must pass before anyone trusts a color
- **Eval suites:** `evals/activation/` · `evals/traversal/` · `evals/output/` ·
  `evals/compression-ablation/`

## Repository layout

```text
skills/success/   runtime skill (SKILL.md + 15 references + 4 assets + evals)
research/         multi-channel research corpora + build-gate synthesis
docs/             installation, usage, and recipes
site/             optional visual guide (design/build in progress)
```

## Documentation & releases

- [docs/installation.md](docs/installation.md) · [docs/usage.md](docs/usage.md) ·
  [docs/recipes.md](docs/recipes.md)
- [CHANGELOG.md](CHANGELOG.md) — release history (current: v0.1.0)
- [SOURCES.md](SOURCES.md) — source attribution and license posture, including the evidence-grading
  rule this skill follows and the figures it refuses to ship
- [CONTRIBUTING.md](CONTRIBUTING.md) — local validation (`scripts/lint-skill`, `scripts/check-sync`)

## License

MIT — see [LICENSE](LICENSE).
