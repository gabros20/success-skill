# Agent guide — `success` (Customer Success)

This repository is the released `success-skill`: an installable agent skill for holding the
customer relationship after the sale and being honest about what its signals can actually support.
The runtime skill lives under `skills/success/`; the repository and Codex plugin use the `-skill`
suffix. Read this before editing.

## Ownership boundary (non-negotiable)

`success` holds the post-purchase relationship — the existence gate for whether a dedicated
function is worth having, the onboarding *program*, help content and the knowledge base,
support-process design and SLAs, AI-support policy, customer health and churn-risk signals,
voice-of-customer interpretation, retention execution, renewals and expansion (NRR), and the
customer's side of an incident. It writes programs, policies, taxonomies, verdicts, and workflows —
**no production code**, no experiments, and no number it cannot source. It does **not** own:

- the in-product onboarding flow, wizards, empty states, or NPS's definition and survey method →
  **design** (success owns the onboarding *program* and interprets NPS, never re-derives it)
- whether a retention or resurrection mechanic works → **growth**, provisional (growth owns
  retention *experimentation*; success owns retention *execution*, the motion a growth test
  validated)
- pricing tiers, the commercial-lifecycle model, or dunning/billing-failure recovery → **product**
  (product models; success operates; involuntary churn is product's mechanism)
- the support assistant's turn loop, retrieval, memory, or eval instrumentation → **ai** (success
  sets the escalation condition and resolution definition; ai measures compliance with them)
- internal SLOs, alerting, on-call, or running the incident itself → **operate** (operate states
  fact, impact, and timing; the customer-facing response-time *promise* is success's, the internal
  target is not)
- acquisition-side lifecycle email, content, or producing the advocacy asset → **marketing**
  (success qualifies and consents; marketing produces and publishes)
- negotiating and closing an expansion sale → **sales**, provisional and contested, unbuilt
- the ship/claim decision or grading tests → **quality**
- implementing any of it in production code → **frontend** / **backend** / **ai**

`success` consumes upstream artifacts (a PRD's time-to-first-value, `design`'s onboarding flow, a
`growth` readout, `operate`'s stated incident fact) when they exist, works standalone when they
don't, recommends siblings for work it doesn't own, and never silently invokes them.

## Non-negotiable invariants

1. **Run the Existence Gate before building the apparatus.** A health score, a CSM playbook, or a
   renewal workflow requested for a product that hasn't passed the gate gets the gate first, and a
   named sibling pack for the meantime — never a silently invented artifact.
2. **Say "not published," never "not measured."** No source discloses a health-score or churn-model
   accuracy figure against real outcomes. Absence of disclosure is not proof of inaccuracy — but a
   reader cannot verify what was never published.
3. **Ask the Observability Question before scoring anything.** In a contractual setting churn is
   observed on a known day; in a non-contractual one it is not observed at all, and a
   contractual-shaped template is the wrong instrument.
4. **Score-vs-prediction are different artifacts.** A health diagnostic and a churn prediction are
   not the same thing even at the org that invested most visibly in both. A score alone next to a
   renewal date is folklore; a score with a stated gap and a mandatory action is a ranking device.
5. **A category list without tie-breakers is not a taxonomy** — ticket categories, churn reasons,
   and feedback reasons alike. Write the rule for the boundary case and name a default direction.
6. **An SLA is a promise made to a specific person, never a copied template number.** No
   response-time figure ships without "set this from your own observed capacity" framing.
7. **Grade every figure inline** — measured-with-method > practitioner-report > vendor-claim — and
   carry the method with the number, or say "method unknown."
8. **A disclaimed figure is still a figure.** Never name a never-ship number in order to forbid it;
   state the mechanism and point at the primary source instead.
9. **Always write "customer escalation."** The bare word is loaded across four sibling packs and
   three senses inside support process itself.
10. **Lift the epistemics, decline the machinery — with reasons.** A stakeholder who asks for a CSM
    ratio or a QBR cadence gets a reasoned decline and the question it was trying to answer, never
    silence and never a borrowed benchmark.

## Required behavior

1. Run `scripts/check-sync` (and `scripts/lint-skill`) before any release; never replace the generic
   gate with domain-only checks.
2. Keep runtime frontmatter to `name` and `description`. Versions/metadata live in
   `.codex-plugin/plugin.json`, `CHANGELOG.md`, tags, and releases — never in `SKILL.md`.
3. Keep `SKILL.md` the direct router: one primary job × one base surface (+ additive agentic
   overlay), plus the "Not this skill →" decline table. References are flat, directly linked,
   self-describing, loaded only when their conditions apply.
4. Every reference begins with `Purpose / Read when / Skip when / Inputs / Produces`; add a
   `## Contents` when it exceeds ~100 lines.
5. Keep repository docs, eval fixtures, research, and site assets outside `skills/success/`.
6. Release through matching plugin version, changelog entry, tag, and GitHub Release; set the
   GitHub About area (family-style description, canonical site alias as homepage, base + domain
   topics).

Do not mark the repository complete because structural lint passes. Activation, traversal, and
output evaluations must show the skill changes agent behavior usefully.
