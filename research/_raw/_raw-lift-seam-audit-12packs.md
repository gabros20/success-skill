# Raw lift: seam audit across 12 shipped sibling packs

Mechanical, exhaustive audit of every shipped pack (design, frontend, backend, architecture,
product, data, ai, quality, operate, automation, marketing, growth) for places where the pack
CEDES a topic to `success`, NAMES success/customer-success, draws a customer-relationship
boundary, or CLAIMS territory `success` might otherwise want. LOCAL DISK ONLY. Every row cites
`<pack>/skills/<pack>/<file>:<line>`, line number verified by direct read.

Method: grepped the full term list (success|onboard|adopt|support|churn|retention|retain|renew|
expansion|upsell|customer health|health score|escalat|help cent|knowledge base|VoC|NPS|CSAT|CES|
customer|subscriber|account manage|advoca|loyalty|post-purchase|ticket|helpdesk|deflect|QBR|
enablement|win-back|winback) case-insensitively across each pack, split into a rare/high-signal
tier (read in full for every pack) and a high-frequency/noisy tier (success, onboard, adopt,
support, customer — word-boundary grepped and reviewed per pack), then classified every surviving
hit.

---

## marketing

Highest seam density of any pack — the only pack whose `SKILL.md` frontmatter, boundary table,
AARRR note, and full `handoff.md` seam-map row all name `success` explicitly.

| path:line | Quote | Class |
|---|---|---|
| marketing-skill/skills/marketing/SKILL.md:10 | "onboarding and retention (→ success)." | CESSION |
| marketing-skill/skills/marketing/SKILL.md:80 | "where lifecycle hands off to \`success\`" | CESSION |
| marketing-skill/skills/marketing/SKILL.md:108 | "Onboarding education, retention communication, in-product activation nudges \| \`success\`" | CESSION |
| marketing-skill/skills/marketing/SKILL.md:115-118 | "**The AARRR note.** ... AARRR spans three packs: \`marketing\` owns acquisition, \`growth\` owns the experiments that improve conversion across the funnel, \`success\` owns retention." | CESSION + CLAIM (marketing keeps acquisition explicitly) |
| marketing-skill/skills/marketing/references/surface-selfserve-saas.md:94-96 | "**Trial-to-paid nudges and win-back once someone is a user** — \`success\` owns onboarding education and retention communication; marketing owns the acquisition-side lifecycle (the newsletter, the pre-signup nurture)" | CESSION |
| marketing-skill/skills/marketing/references/surface-selfserve-saas.md:121 | "post-signup activation crosses to \`success\`" | CESSION |
| marketing-skill/skills/marketing/references/surface-selfserve-saas.md:134-135 | "Treating activation and retention as marketing's to claim credit for, rather than \`growth\`'s and \`success\`'s per the seam above." | NAMED-BOUNDARY (failure mode) |
| marketing-skill/skills/marketing/references/lifecycle-and-email.md:14 | "The email is in-product onboarding education after signup → \`success\`." | CESSION |
| marketing-skill/skills/marketing/references/lifecycle-and-email.md:136 | "**Onboarding education** (teaching a signed-up user how to use the product) → \`success\`." | CESSION |
| marketing-skill/skills/marketing/references/organic-social-and-community.md:17-18 | "The question is retention inside an existing community/product, not acquisition into it → \`success\` or \`growth\`." | CESSION |
| marketing-skill/skills/marketing/references/organic-social-and-community.md:135-136 | "The question is measuring an existing community's engagement or retention → \`growth\` or \`success\`, depending on whether it's acquisition or retention being measured." | CESSION |
| marketing-skill/skills/marketing/references/app-store-optimization.md:18 | "The question is app-review-response handling as a support workflow → \`success\`." | CESSION |
| marketing-skill/skills/marketing/assets/email-compliance-checklist.md:81 | "Onboarding education after signup → \`success\`" | CESSION |

### handoff.md inventory (marketing → rest of family)

`marketing-skill/skills/marketing/references/handoff.md` — one dedicated seam-map row for
`success`, plus the shipped AARRR note and a failure mode, all bidirectional:

- **Line 43** (table row, verbatim): "\`success\` | Acquisition-side lifecycle content
  (pre-signup nurture, the newsletter) and the narrative marketing used to acquire the user, for
  onboarding continuity | Retention and churn signal that feeds messaging and CEP work |
  Onboarding education and retention communication are \`success\`'s; marketing's lifecycle job
  stops at acquisition, per surface-selfserve-saas.md's seam-at-signup section" — TO success:
  acquisition-side lifecycle content + acquisition narrative; FROM success: retention/churn
  signal feeding messaging and Customer Engagement Platform (CEP) work.
- **Line 52**: "AARRR spans three packs in this family, acquisition here, funnel-wide
  experiments in \`growth\`, retention in \`success\`."
- **Lines 59-60** (failure mode): "Writing onboarding or retention copy inside a marketing
  deliverable instead of routing it to \`success\`, because the acquisition-to-activation line
  feels continuous from the writer's side."

### False positives

Count: **~275** of 290 raw hits. Overwhelmingly: "loyalty" in the Ehrenberg-Bass double-jeopardy
/ penetration-vs-loyalty marketing-science sense (evidence-grading a loyalty-program ROI claim,
not ceding loyalty programs to success); "escalat-" in DMARC policy escalation (`p=none` →
`p=quarantine` → `p=reject`) and inbox-provider enforcement ladders; "retention" as a data-privacy
term (audience-and-segmentation.md's consent-regime mechanics); "expansion" in Google Ads
final-URL expansion; "churn" describing journalist-query-service vendor churn; "subscriber" as a
newsletter-list technical term.

---

## growth

Second-highest density. Growth reciprocates marketing's AARRR split from its own side and adds a
third distinction success needs to internalize on day one: **retention *experimentation*** (does
a mechanic work — growth's) vs. **retention *execution*** (sending the validated message —
success's).

| path:line | Quote | Class |
|---|---|---|
| growth-skill/skills/growth/SKILL.md:10 | "onboarding comms (→ success)." | CESSION |
| growth-skill/skills/growth/SKILL.md:113 | "Onboarding education content, retention communications, churn-save messaging as sent \| \`success\` — provisional, per the AARRR split below" | CESSION (explicitly marked provisional) |
| growth-skill/skills/growth/SKILL.md:117-121 | "**AARRR spans three packs**: \`marketing\` owns acquisition channels, \`growth\` owns the experiments that improve conversion across the whole funnel — including referral loops and retention experimentation — \`success\` owns retention execution, the communications a growth test showed were worth sending." | CESSION + CLAIM (growth explicitly retains retention *experimentation*) |
| growth-skill/skills/growth/references/growth-model-and-loops.md:61-63 | "marketing's own shipped note states the split from its side: *\"AARRR spans three packs: \`marketing\` owns acquisition, \`growth\` owns the experiments that improve conversion across the funnel, \`success\` owns retention\"* (marketing-skill \`SKILL.md\`)." | CESSION (cross-pack citation, reciprocated) |
| growth-skill/skills/growth/references/growth-model-and-loops.md:71-74 | "**\`success\` owns Retention *execution*** — the onboarding education and retention communications a growth test showed were worth sending. Growth designs and reads out the test; \`success\` sends the message the test validated." | CESSION |
| growth-skill/skills/growth/references/retention-and-resurrection.md:168 | "A retention or resurrection mechanic is classified as operate's (standing) or growth's [experiment-bound]" | CLAIM (retention mechanic ownership split with operate, not success — success executes only the validated message) |

### handoff.md inventory (growth → rest of family)

`growth-skill/skills/growth/references/handoff.md`:

- **Line 43** (seam-map row, verbatim): "\`success\` (provisional) \| An experiment readout on a
  retention or resurrection mechanic \| Retention and churn signal that surfaces what's worth
  testing next \| \`growth\` owns retention *experimentation* — does a resurrection nudge work;
  \`success\` owns retention *execution* — sending the message a growth test validated." — TO
  success: experiment readout on a retention/resurrection mechanic; FROM success: retention and
  churn signal (what's worth testing next).
- **Lines 49-50** (AARRR note): "\`marketing\` owns Acquisition ...; \`growth\` owns the
  experiments that improve conversion across the whole funnel — Activation, Referral loop design
  and math, and Retention *experimentation*; \`success\` owns Retention *execution* — the
  onboarding education and retention communications a growth test showed were worth sending."
- **Line 69** (failure mode): "Silently invoking \`frontend\`, \`backend\`, \`design\`, \`data\`,
  \`marketing\`, \`product\`, \`operate\`, \`sales\`, or \`success\` instead of naming the actual
  sibling and the specific artifact it owns."

### False positives

Count: **~478** of 491 raw hits. The overwhelming majority is growth's own claimed territory:
retention-definition mechanics (N-day/rolling/survival), cohort diagnosis, CUPED-and-retention
variance-reduction limits, NPS-as-a-weak-retention-instrument, win-back/streak experiment
methodology — all in `retention-and-resurrection.md`, `funnel-and-cohort-diagnosis.md`,
`activation-and-onboarding.md`, and eval-harness `cases.json` prompts. These are CLAIM-side
content (growth teaching how to run and read a retention *experiment*) rather than seams — they
matter for success only insofar as success must not re-derive them, but they name no boundary
with success beyond the ones listed above. Also FP: "customer" in pricing-experiment population
examples; "support" as statistical/evidentiary support ("the data supports a real test").

---

## product

Product is where the family's `success` boundary was first drawn (product's `SKILL.md` predates
the other packs' shipped cessions) — both a top-level mission-boundary sentence and a
surface-specific "Recommends" line.

| path:line | Quote | Class |
|---|---|---|
| product-skill/skills/product/SKILL.md:27-28 | "onboarding, support, and adoption to \`success\`" (full sentence: "...qualification and CRM to \`sales\`; onboarding, support, and adoption to \`success\`; and business processes spanning systems the product does not own to \`automation\`.") | CESSION |
| product-skill/skills/product/references/surface-app-saas.md:45 | "**Recommends:** \`design\` for product UX, states, and IA; \`frontend\` for implementation; \`growth\` for funnel experiments and PLG loops; \`success\` for onboarding and support." | CESSION |
| product-skill/skills/product/SKILL.md:62 | "Activation/retention, pricing tiers, MRR/churn metric trees, commercial lifecycle" (App & SaaS surface-router contribution column) | CLAIM |
| product-skill/skills/product/references/surface-app-saas.md:28-32 | "Frame around activation (the \"aha moment\") and retention jobs ... churn is a discovery question ... Pricing is tiered and lives inside a commercial lifecycle (trial → paid → expansion → renewal/churn)." | CLAIM (product claims the metric/commercial framing even though success would execute retention comms) |
| product-skill/skills/product/references/surface-app-saas.md:38-42 | "The north star decomposes into an activation/retention/MRR/churn metric tree (HEART/AARRR) ... Guardrails watch churn and support load ... Track churn/retention risk, activation-drop risk..." | CLAIM |
| product-skill/skills/product/references/surface-app-saas.md:24,35 | "An onboarding + core-loop scope feeding [PRD](prd.md)." / "Onboarding and the core loop are always first-class scope sections" | CLAIM (tension with :45 — product claims onboarding *requirements/PRD scope*, cedes onboarding *execution* to success) |
| product-skill/skills/product/references/metrics.md:53 | "Health: NPS / CSAT, Support Ticket Rate, Error Rate" (metric-tree health branch) | CLAIM (product's own north-star tree ingests NPS/CSAT/support-ticket-rate as inputs, without ceding measurement) |
| product-skill/skills/product/references/risk-register.md:58 | "**L4** — a revenue or retention blocker: users refuse to pay, churn, or fail activation without it." | CLAIM |
| product-skill/skills/product/references/surface-mobile.md:36 | "uninstall rate) to the metric tree alongside in-app activation/retention." | CLAIM |
| product-skill/skills/product/references/discovery.md:15 | "access to users/customers or their proxies (support tickets, sales calls, forums)" | MENTION (support tickets as a discovery-research input, no boundary drawn) |
| product-skill/skills/product/references/discovery.md:75 | "mine public forums, review sites, support tickets, and competitor gaps for recurring complaints" | MENTION |

### handoff.md inventory

`product-skill/skills/product/references/handoff.md` (full read) names no `success` row at all —
`recommended_next` in the `handoff.yaml` schema (line 129) lists only `design`, `architecture`,
`marketing`, `growth` as valid downstream targets. This is consistent with product's SKILL.md
predating the other packs' `success` cessions but never having its own dedicated
build-artifact handoff to success (product hands off PRDs/strategy to design/architecture, not
to success).

### False positives

Count: **~198** of 211 raw hits. Mostly ordinary product-management vocabulary: "customer" in
discovery/positioning/business-model methodology (Customer Segments, Customer Jobs, Customer
Profile, JTBD discovery), "escalat-" for autonomy-level human-in-the-loop escalation paths on the
agentic surface, "adopt" for internal-tool adoption replacing acquisition on `surface-internal.md`.

---

## operate

Operate draws the boundary as a NAMED customer-relationship split every time an incident or
decommission surfaces something customer-facing — always co-assigned to `product` **and**
`success` together, never success alone.

| path:line | Quote | Class |
|---|---|---|
| operate-skill/skills/operate/SKILL.md:90 | "Customer-facing incident comms, per-account outreach \| \`product\` / \`success\`" | CESSION |
| operate-skill/skills/operate/references/decommissioning.md:185-187 | "If the decommission surfaces an unresolved customer-facing consequence (a user who still needs their data), that routes to \`product\`/\`success\` for the outreach — this file owns the technical and data-disposition sequencing, not the customer conversation." | CESSION + NAMED-BOUNDARY |
| operate-skill/skills/operate/references/incident-response.md:21 | "Writing customer-facing incident copy or per-account outreach — that is \`product\`/\`success\`." | CESSION |
| operate-skill/skills/operate/references/incident-response.md:158-159 | "Customer-relationship framing and per-account outreach are not operate's call — route to \`product\` / \`success\`. Operate states fact, impact, and timing; it does not manage the relationship." | CESSION + NAMED-BOUNDARY (sharpest boundary-language in the whole audit) |
| operate-skill/skills/operate/references/handoff.md:79 | "Decommission / dependency-withdrawal notice \| The owning build skill, or \`product\` if customer-facing \| A sunset date or a forced migration" | NAMED-BOUNDARY (routes to `product` only, does not name `success` here) |

### handoff.md inventory

`operate-skill/skills/operate/references/handoff.md` has no dedicated `success` row — its one
customer-facing row (line 79, above) routes to `product` only. The richer, more specific
success-naming boundary language lives in `incident-response.md` and `decommissioning.md`
instead of the handoff file.

### False positives

Count: **~359** of 364 raw hits (5 real: the 4 above plus the handoff.md row). Dominant patterns:
"retention" as data/log-retention (compliance, backup logs, observability windows — e.g.
`decommissioning.md`'s data-retention-obligation section, entirely about GDPR/legal retention,
not customer retention); "ticket" as an alert-severity tier (page/ticket/log, SLO burn-rate
routing) with zero connection to a support desk; "escalat-" as CTO/on-call escalation paths;
"renew-" as TLS-certificate and domain-registrar renewal; "support ticket" used twice
(`recoverability.md:119`, `surface-managed-platform.md:47-55,149`) to debunk the false assumption
that a *cloud-vendor's* support ticket is a valid restore mechanism — not customer support.

---

## automation

Automation is younger than success in family sequence and says so explicitly — it names
`success` as a not-yet-existing commercial upstream it defers to once shipped.

| path:line | Quote | Class |
|---|---|---|
| automation-skill/skills/automation/SKILL.md:104 | "Authoring the business rule, or customer-facing comms \| \`product\` · \`marketing\` · \`sales\` · \`success\`" | CESSION |
| automation-skill/skills/automation/references/process-capture.md:15-17 | "The rule already exists in writing, owned by \`product\`, \`marketing\`, \`sales\`, or \`success\` — read it and cite the owner; do not recapture it here. (At this pack's launch those three commercial upstreams do not yet exist as shipped skills — say that plainly rather than inventing an owner.)" | CESSION (explicitly forward-looking / provisional) |
| automation-skill/skills/automation/references/process-capture.md:162-163 | "No owner exists for the rule — do not invent one. Record the gap and route to the nearest commercial skill once it exists (\`product\`, \`marketing\`, \`sales\`, \`success\`)." | CESSION |
| automation-skill/skills/automation/assets/approval-policy-card.md:17,23 | "Refund over $500, generated by the refund-request automation from a matched support ticket" / "The original support ticket, the matched decision-table row..." | MENTION (worked example uses a support ticket as the automation trigger; no boundary drawn about who owns the ticket) |

### handoff.md inventory

`automation-skill/skills/automation/references/handoff.md` — grepped for success/customer:
**zero hits**. Automation's `success`-facing language lives entirely in `SKILL.md` and
`process-capture.md`, not in its handoff file.

### False positives

Count: **~296** of 299 raw hits. Dominant patterns: "escalat-" for approval-timeout policy
(deny/allow/escalate gates, universal invariant I13), "retention" for vendor data-retention
windows (sync-semantics.md's delete-detection caveats), "churn" for vendor/pricing-page churn
(re-verify-before-trusting notes).

---

## backend

| path:line | Quote | Class |
|---|---|---|
| — | — | none found |

Zero cessions, zero named boundaries, zero claims relevant to success. All 4 tier-A hits and all
tier-B (`success`, `onboard`, `customer`) hits are pure engineering usage: circuit-breaker
"success" (closes the breaker) in `service-integration.md:56,59`; idempotency-key "success" path
in `assets/idempotency-and-outbox-recipes.md:17`; "customer" in `service-integration.md:83`
means a webhook-consuming API customer (engineering sense); "onboarding" in
`async-and-messaging.md:11` is a generic multi-step-business-process example, not CS onboarding.
No `references/handoff.md` row names customer/success (grepped directly, zero hits).

### False positives

Count: **258** of 258 raw hits (100%).

---

## architecture

| path:line | Quote | Class |
|---|---|---|
| — | — | none found |

Zero cessions. "Customer" appears only as DDD teaching material (bounded-context canvas,
Customer/Supplier upstream-downstream pattern, "'Customer' in Billing vs 'Customer' in Support"
as a *ubiquitous-language split signal* — a modeling example, not a family-boundary statement).
"Retention" is data-classification/compliance retention. "Escalat-" is privilege escalation
(STRIDE) or HITL autonomy escalation on the agentic surface — both unrelated to customer
relationships. `references/handoff.md` grepped directly: zero success/customer hits.

### False positives

Count: **198** of 198 raw hits (100%).

---

## frontend

| path:line | Quote | Class |
|---|---|---|
| frontend-skill/skills/frontend/references/state-completeness.md:72 | "a clear, generic message plus a support/contact path; don't surface raw server detail" | MENTION (error-state UX names a support contact path, no boundary drawn) |
| frontend-skill/skills/frontend/references/client-app-wiring.md:150 | "fallback so support and logs correlate" | MENTION (correlation-ID logging so a support workflow can trace a request) |

No CESSION anywhere. `references/design-handoff-and-tokens.md` (frontend's handoff-shaped file,
in place of a `references/handoff.md`) has zero success/customer hits — its one "support" hit
is "if the target pipeline doesn't support it" (CSS-value engineering support, FP).

### False positives

Count: **~500** of 502 raw hits (2 MENTIONs above). Dominant patterns: "expansion" almost
entirely means i18n text-expansion (German/Finnish/Arabic string growth budgets); "retention" is
cache-eviction retention (`gcTime`, `staleTime`); "churn" is dependency-array/re-render churn;
"subscriber" is a React/Kotlin observer-pattern term (re-render subscribers, `SharedFlow`
subscribers); "escalat-" is Feature-Sliced-Design layer escalation; "support" is overwhelmingly
browser/API/platform support (~53 hits: CSS support, `@supports`, Stage Manager support, strict
mode support, etc.).

---

> **CORRECTION NOTE — added 2026-08-02 by channel lead E (`webdesign-lift-report.md` §3.3).**
> The heading below, and the "208 of 208 raw hits (100%) false positives" line, are correct about
> **cessions** and materially misleading about **territory**. Under this audit's own definition —
> *CLAIM = "the pack KEEPS a topic success might otherwise want"* — several design hits classified
> here as false positives are CLAIMs, and they bear on success's largest canonical include:
>
> - `design-skill/skills/design/references/journeys.md:51–53` is a dedicated **`## Onboarding`**
>   section: *"Goal priority: get to first value fast > orient (**don't educate**) > build confidence
>   > reduce setup friction. Onboarding's job is the **aha moment**, not teaching the product.
>   Patterns: progressive / setup wizard / sample-data demo / interactive tour (sparingly, **3–5 core
>   concepts, dismissable**)… Metrics: activation rate, time-to-activation, completion, drop-off by
>   step, D7/D30 retention."* Design's shipped doctrine is "orient, **don't educate**"; success's
>   canonical include is "education and enablement". That is a seam success must draw explicitly.
> - `journeys.md:3` names onboarding in the file's own Purpose line; `journeys.md:49` maps the arc
>   through *"support/billing/offboarding"* and audits the *"cancel flow"*.
> - `design/references/content.md:45` — *"**Empty states are onboarding moments in three beats**…
>   New users spend more time in empty states than in any other state"*; `content.md:58` —
>   *"| Onboarding | contextual, not a tutorial |"*.
> - `design/references/research.md:49` ships the **NPS** definition and survey method
>   (*"NPS 0–10 (Promoters 9–10, Detractors 0–6; NPS = %Promoters − %Detractors)"*, SUS, ~385
>   responses for ±5%) — success's VoC work must cite it, not redefine it.
>
> Why design shipped no cession despite holding this ground: design predates success, and its
> adjacency list (`design/SKILL.md:21–24`) does not name success at all; `journeys.md:11` routes
> product-level journeys to `product`, the only downstream that existed.
>
> The same qualification applies to two other "VERIFIED EMPTY" packs below:
> **`ai`** claims the support-assistant surface — `ai/references/surface-chat-assistant.md:9`,
> *"The request is a chatbot, **support assistant**, copilot side-panel…"* — and uses "knowledge
> base" for a retrieval corpus (`ai/references/memory.md:105–106`), colliding with success's
> customer-help sense. **`data`** constrains success's VoC data at
> `data/references/governance-pii-and-retention.md:69`: *"When PII lives in free text (**support
> tickets**, LLM traces, unstructured logs)…"*.
>
> **Nothing in this file's cession analysis or its false-positive counts is withdrawn** — those are
> corroborated by the lead's independent grep and are the authoritative source for the per-pack
> volumes. What is corrected is only the inference a reader would draw from the word EMPTY: emptiness
> of *cession* is confirmed; emptiness of *territory* is refuted for design and qualified for ai and
> data.

## design — VERIFIED EMPTY (charter claim confirmed)

| path:line | Quote | Class |
|---|---|---|
| — | — | none found |

Charter asserts zero cessions to success. **Confirmed.** Read every tier-A hit (11) in full and
every tier-B `success`/`onboard`/`adopt`/`customer`/`support` hit (17/11/2/4/13) individually.
What the raw hits actually are:
- **"success" (17 hits, all FP)** — the canonical 8-state interaction model
  (default/hover/focus/active/disabled/loading/error/**success**) repeated across
  `SKILL.md:89`, `interaction.md:35,82,98`, `design-systems.md:37,53`, `color.md:109-110`,
  `accessibility.md:51`, `surface-ios.md:52,64`; plus UX-research "task success"/"first-click
  success" metrics in `research.md:53,61` and `critique.md:116`.
- **"customer" (4 hits, all FP)** — service-blueprint methodology
  (`journeys.md:45,49` — frontstage/backstage/support lanes as a *technique*, not a family
  boundary) and vocabulary/naming guidance (`information-architecture.md:43,63`).
- **"onboard" (11 hits)** — all UX-onboarding-flow design craft (`journeys.md:53`'s aha-moment
  framing, empty-states-as-onboarding), not customer-success onboarding.
- **"support" (13 hits, all FP)** — browser/platform feature support (`@supports`, Display P3,
  Stage Manager) and the service-blueprint "support" lane.

One near-miss worth flagging for the record, not a correction: `interaction.md:74` and
`state-completeness.md`'s frontend echo both call a search zero-results state "a retention
moment" — this is UX-retention (don't lose the user's search intent), unrelated to customer
retention/churn. Not a cession.

### False positives

Count: **208** of 208 raw hits (100%). No corrections to the charter.

---

## data — VERIFIED EMPTY (charter claim confirmed)

| path:line | Quote | Class |
|---|---|---|
| — | — | none found |

**Confirmed empty**, with one adjacent-but-distinct near-miss flagged below.

- **"success" (2 hits)** — `lineage-and-observability.md:62` is a DQ-assertion JSON-schema field
  name (`{assertion, success, column, ...}`); `experiment-measurement-foundations.md:25` reads
  "success-metric selection for a specific initiative — → \`growth\`" — this **is** a real
  cession, but of KPI/success-*metric* selection to `growth`, not of anything to `success` the
  pack. Flagged as a near-miss, classified FP for this audit's purpose (wrong recipient).
- **"customer" (6 hits, all FP)** — data-governance/compliance usage: "customer compliance
  commitment" and "customer contract" (`surface-regulated.md:12,28`), `customers.sql` as a dbt
  marts-layer naming example (`transformation-and-modeling.md:53`), BigQuery customer-storage
  benchmark stat (`platform-and-cost.md:49`).
- **"onboard" — 0 hits.**
- **"adopt" (10 hits, all FP)** — tool/methodology adoption (Elementary, dbt Mesh, data
  contracts initiative).
- All 57 tier-A hits (retention/churn/escalat/knowledge-base/ticket/loyalty) read in full: every
  one is data-governance retention (GDPR Art.17 erasure schedules), materialization-tier
  escalation, or a `governance-pii-and-retention.md` cross-reference — zero customer-relationship
  content.

`references/handoff.md` grepped directly: the only hits are `retention-schedule enforcement
points` (line 80, routed to `operate` for dashboards/alerts — not a success seam) and a PII
cross-reference (line 61) — both data-retention-compliance, not customer-success.

### False positives

Count: **236** of 237 raw hits (1 near-miss noted above, not a correction).

---

## ai — VERIFIED EMPTY (charter claim confirmed)

| path:line | Quote | Class |
|---|---|---|
| — | — | none found |

**Confirmed empty.** Notably, **zero** "customer" hits anywhere in the pack (`grep -rniE
'\bcustomer'` returns nothing) — the strongest possible negative result. "Success" (5 hits) is
entirely eval/benchmark vocabulary: `pass@k` success-probability definitions
(`evaluation.md:126`, `assets/eval-harness-starter.md:86`), "build success criteria first, curate
context second" (`prompt-and-context-engineering.md:60`), and a vendor-naming "successor" (MS
Agent Framework succeeding AutoGen/Semantic Kernel, `SOURCES.md:19`,
`agent-construction.md:203`). "Support" (14 hits) is entirely API/model/provider support
(strict-mode support, logit-access support). One example worth noting but not a seam:
`surface-chat-assistant.md:9` lists "a chatbot, **support assistant**, copilot side-panel" as an
example product shape this surface covers — this is ai naming a use-case category (building the
model/prompt/retrieval layer of a support bot), not a boundary statement about who owns the
support relationship; no cession language accompanies it. `references/handoff.md` grepped
directly: zero hits.

### False positives

Count: **206** of 206 raw hits (100%). No corrections to the charter.

---

## quality — VERIFIED EMPTY (charter claim confirmed)

| path:line | Quote | Class |
|---|---|---|
| — | — | none found |

**Confirmed empty.** All 36 tier-A hits read in full: every one is either WCAG's own "Success
Criterion" terminology (`SOURCES.md:126`, `surface-regulated.md:71`, `accessibility-
conformance.md:95,137,147`, `oracles-and-evidence.md:187` — a formal W3C term, not a pack
boundary), or test/defect-tracking "ticket" (flake-quarantine tickets, severity-escalation
rounds in `release-gate-and-claims.md`, `defect-lifecycle.md`). The single "customer" hit
(`defect-lifecycle.md:130`) is defect-writing guidance — "state the harm in the user's domain
terms... 'the discount code is silently applied twice, overcharging or undercharging the
customer' is a finding" — about how to phrase a defect's impact, not a customer-success
boundary. `references/handoff.md` grepped directly: only hit is "Everything in this domain
churns" (line 93, FP — tool/threshold volatility, not customer churn).

### False positives

Count: **387** of 387 raw hits (100%). No corrections to the charter.

---

## Cross-pack contradiction check

No hard contradiction found. The five citing packs (marketing, growth, product, operate,
automation) agree on the same shape:

- **Onboarding education / in-product activation nudges / retention communication** →
  `success` (marketing, growth, product all agree).
- **Retention *experimentation*** stays `growth`'s; **retention *execution*** (sending the
  validated message) is `success`'s — stated identically from both marketing's and growth's
  sides (marketing `SKILL.md:118`, growth `SKILL.md:121` and `handoff.md:43,49-50`).
- **Customer-facing incident/decommission comms** are co-owned `product`/`success`, never
  `success` alone (operate, three separate files, identical phrasing each time).
- **product**'s own surface-app-saas.md contains an internal (not cross-pack) tension worth
  success knowing about: product claims onboarding as first-class **PRD scope** (line 24, 35)
  while recommending `success` for onboarding **execution/support** (line 45) — not a
  contradiction, but success should expect product to hand it a PRD's onboarding acceptance
  criteria, not just a bare recommendation.
- **automation** and **product**/**operate** were written at different points in the family's
  build sequence — automation's `process-capture.md:15-17` explicitly flags that `success`
  did not exist yet at automation's launch and treats the citation as provisional/forward-
  looking, exactly as growth's own handoff.md marks its `success` row "(provisional)".

## Total CESSION counts per pack

| Pack | CESSION | NAMED-BOUNDARY | CLAIM | MENTION | False positives (of raw hits) |
|---|---|---|---|---|---|
| marketing | 11 | 2 | 1 | 0 | ~275 / 290 |
| growth | 5 | 0 | 2 | 0 | ~478 / 491 |
| product | 2 | 0 | 6 | 2 | ~198 / 211 |
| operate | 4 | 2 | 0 | 0 | ~359 / 364 |
| automation | 3 | 0 | 0 | 1 | ~296 / 299 |
| frontend | 0 | 0 | 0 | 2 | ~500 / 502 |
| backend | 0 | 0 | 0 | 0 | 258 / 258 |
| architecture | 0 | 0 | 0 | 0 | 198 / 198 |
| design | 0 | 0 | 0 | 0 | 208 / 208 |
| data | 0 | 0 | 0 | 0 | 236 / 237 (1 near-miss to `growth`) |
| quality | 0 | 0 | 0 | 0 | 387 / 387 |
| ai | 0 | 0 | 0 | 0 | 206 / 206 |
