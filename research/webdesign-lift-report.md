# Channel E report — webdesign lift + family seam audit

Date: 2026-08-02 · Lead: channel E · Domain: local disk only (no web, no GitHub, no x-relay)
Linked raw files:
- [`_raw/_raw-lift-webdesign-sweep.md`](_raw/_raw-lift-webdesign-sweep.md) — exhaustive 23-file sweep of the legacy webdesign skill (worker, sonnet), with a dated lead correction note at its head.
- [`_raw/_raw-lift-seam-audit-12packs.md`](_raw/_raw-lift-seam-audit-12packs.md) — mechanical 12-pack seam grep, 433 lines (worker, sonnet), with a dated lead correction note at its `## design` section. It independently reproduced the cession set in §3 and is the authoritative source for per-pack false-positive volumes.

Prior-run extraction records of the same legacy skill, read in full and treated as authoritative
precedent (both outside this repo, neither to be duplicated):
- `/Users/tamas/Documents/Personal/Projects/marketing-skill/research/webdesign-extraction.md` (720 lines) — the marketing slice.
- `/Users/tamas/Documents/Personal/Projects/growth-skill/research/webdesign-growth-extraction.md` (501 lines) — the growth slice, whose grep-against-shipped-text method (`:16–19`) is the one this channel followed.

---

## 1. Verdict

**The webdesign lift is nearly empty, and that emptiness is itself the finding.** Of 3,707 lines
across 23 files, ten candidates were identified and **eight collapsed on grep** — they are already
shipped by `design`, `marketing`, `growth`, `product`, or `quality`, in several cases with better
sourcing than webdesign had. This is the skill's *third* extraction (marketing and growth each ran
one), which is why the collapse rate is so high.

**Exactly two items survive, and both are grep-verified orphans no pack in the family owns:**

1. **The help-content slot is empty family-wide.** Webdesign scores Nielsen's "help & documentation"
   heuristic (`design-critique.md:14–18`) and never defines it. Grep for `help (and|&)
   documentation|help content|documentation heuristic` across all twelve shipped packs: **zero hits.**
2. **Nobody owns the customer-facing response-time promise.** A healthcare vertical playbook
   (`niche-and-vertical-design.md:148–156`) carries the only expectation-setting doctrine in the
   skill — "explicit response-time commitments", stated at the point of action. Grep across twelve
   packs: **zero hits.** Operate owns internal SLOs; nobody owns when a human replies.

Both are direct support-process material, and both are the kind of grep-verified empty judgment layer
that justified the quality pack's narrow wedge. Abandoning webdesign costs `success` nothing else.

**The seam audit is where this channel's value is, and it produces one correction that changes the
pack's shape.** All 26 line-references in the charter verify *exactly* against disk — not one is
wrong. But the charter's most consequential sentence is materially misleading:

> charter.md:56 — "design/data/quality/ai/frontend/backend/architecture: ZERO cessions on disk
> (verified by grep; raw hits were 'success state' UI false positives). Success draws those seams
> from its own side."

The *cession* count is right (verified independently: zero occurrences of `` `success` `` in all
seven). The inference is wrong. **`design` is not a blank space — it is a shipped incumbent on
`success`'s single largest canonical include.** `design-skill/skills/design/references/journeys.md`
carries a dedicated `## Onboarding` section, an end-to-end arc that runs through *support* and
*offboarding*, the empty-state-as-onboarding rule, and the activation metric set;
`design/references/research.md:49` already owns the **NPS** definition and survey method. Design
shipped no cession to success because design predates success and its adjacency list
(`design/SKILL.md:21–24`) does not mention success at all. Success cannot simply claim onboarding.
It must negotiate a seam against design's shipped text — and against `product`, which claims the
churn/renewal/expansion commercial lifecycle and the NPS/CSAT/support-ticket-rate health metrics.

Three of `success`'s twelve canonical includes are therefore **contested, not vacant**: onboarding
(design), VoC/NPS (design + product), and churn/renewal/expansion (product).

---

## 2. Part A — the webdesign lift-list

### 2.1 Provenance correction: the mandate pointed at a stale copy

The mandate named `~/.claude/skills/webdesign/`. That is **v1.2.0** (`SKILL.md:3`, `version: 1.2.0`).
The canonical source repo is `/Users/tamas/Documents/Personal/Projects/webdesign/skills/webdesign/`,
at **v1.3.2** (`git log`: `cce0fac fix(skill): exclude app dashboards/product UI from activation
(v1.3.2)`). Every reference file in the repo is 20–30 lines longer; `SKILL.md` was rewritten to the
skill-template standard (164 → 114 lines).

The lead diffed both copies for success-relevant additions. **The v1.3.2 delta contains none.** The
only added lines matching success terms are a scope *narrowing*:

- `webdesign/skills/webdesign/SKILL.md:9` — "…component API engineering, **app dashboards and
  product UI**, full accessibility audits, general SEO"
- `webdesign/skills/webdesign/SKILL.md:10` — "strategy, **growth planning**, or standalone design
  critique of work it did not build…"

v1.3.2 explicitly pushes app/product UI and growth planning *out* of webdesign. The completeness
statement below holds against both versions and holds more strongly against the newer one.

### 2.2 Webdesign has already been extracted twice — every candidate was grep-tested against shipped text

This is the third extraction of this skill. Two prior-run records exist and both were read:

- `marketing-skill/research/webdesign-extraction.md` (720 lines) — the marketing slice.
- `growth-skill/research/webdesign-growth-extraction.md` (501 lines) — the growth slice.

Growth's run recorded a method note that proved decisive here
(`webdesign-growth-extraction.md:16–19`): *"Cross-checked every ALREADY-LIFTED claim against
marketing's actually-shipped references … **This step changed four verdicts: the marketing table
listed items as LIFT that did not survive into the shipped pack.**"* Following that precedent, every
candidate below was grepped against the **shipped** sibling packs, not against the prior disposition
tables. Six of ten candidates collapsed.

Licensing (from growth's run, `webdesign-growth-extraction.md:7–9`, re-verified): webdesign declares
`license: MIT` in `SKILL.md:16` with source repo `github.com/gabros20/webdesign` (`SKILL.md:18`);
there is **no LICENSE file** in the installed directory, the frontmatter field is the only artifact.
It is the user's own skill, so verbatim lift is permitted. Two references self-declare adaptation
from `pbakaus/impeccable` (Apache-2.0) at `design-critique.md:9` and
`frontend-design-principles.md:38`; neither adapted portion is in the success slice.

### 2.3 The lift-list (final dispositions, all grep-verified)

| # | Source (v1.2.0 path:line) | Content | Disposition — with the shipped file that already carries it |
|---|---|---|---|
| 1 | `design-critique.md:58` | "**P1** — the test: **'would a real user contact support over this?'**" | **SIBLING:quality — shipped** at `quality/references/defect-lifecycle.md:138`, `quality/assets/severity-map.md:51`, `quality/assets/release-gate-checklist.md:37`, `design/references/critique.md:78` |
| 2 | `design-critique.md:14–18` | Nielsen's 10 scored heuristics, including **"help & documentation"** and "help users recognize/diagnose/recover from errors" — **named but never defined** | **ORPHAN → REWRITE for success** (see §2.4) |
| 3 | `frontend-design-principles.md:159–183` | UI-copy doctrine, empty states and error voice | **SIBLING:design — shipped and extended** at `design/references/content.md:31,45,58` |
| 4 | `persuasion-and-conversion.md:44–45` | Zeigarnik progress bars / profile-completion meters | **SIBLING:design + growth** — design shipped the mechanic at `design/references/interaction.md:90` ("**Zeigarnik:** show progress ('Step 2 of 3')… **Peak-end:** engineer a delight peak and a strong close"); growth's run claimed the completion-meter and engagement-farming residue as activation/habit-ethics (`webdesign-growth-extraction.md:82`) |
| 5 | `persuasion-and-conversion.md:35`, `:127–128`, `:135–136` | Cancellation / retention **ethics**, FTC blacklist | **SIBLING:marketing + growth — shipped, and better sourced than webdesign** (see §2.4) |
| 6 | `niche-and-vertical-design.md:148–156` | "3) **Process Expectations** (first-visit details, **response timelines**)… **Anxiety reducers:** state pre-visit expectations near the submit button; **explicit response-time commitments**; staged intake" | **ORPHAN → REWRITE for success** (see §2.4) |
| 7 | `trust-proof-and-structure.md:49–58` | IA doctrine: 2–7 nav items, flat hierarchy, plain labels, progressive disclosure | **SIBLING:design — shipped** at `design/references/information-architecture.md:43,51` (verbatim: "Plain labels beat clever ones on every usability metric"; "Primary nav **2–7 items**… any page reachable in **2–3 clicks**") |
| 8 | `trust-proof-and-structure.md:83–95` | Case-study anatomy, Challenge → Solution → Results | **SIBLING:marketing + product — shipped** at `marketing/references/landing-pages-and-conversion.md:86` ("Anatomy: challenge → approach"), `marketing/assets/landing-page-requirements-brief.md:41`, `product/references/surface-website.md:35` ("Challenge → Solution → Results, with quantified outcomes"). **The advocacy-sourcing seam it implies is NOT shipped** — §5 Q1 |
| 9 | `design-critique.md:52–60` | The P0–P3 severity ladder | **SIBLING:quality — shipped** |
| 10 | `section-archetypes.md:173` | `` `faq` `` field shape `items:list[question, answer]` | **SIBLING:design** (thin; a generic content schema) |

**Counts: ORPHAN/REWRITE-for-success 2 · SIBLING already shipped 8 · LIFT 0 · CITE 0.**

**Nothing in webdesign is available to `success` as a pure lift, and only two items are available at
all.** Every other candidate is already live in a shipped sibling — in several cases with better
sourcing than webdesign had. Success must cite those, never restate them.

### 2.4 The two orphans — and the two collapses worth knowing about

**Orphan #1 — the empty help-content slot (`design-critique.md:14–18`).** Webdesign scores Nielsen's
"help & documentation" and "help users recognize/diagnose/recover from errors" as heuristics, then
never says what good help content *is*. Grep across all twelve shipped packs for `help (and|&)
documentation|help content|documentation heuristic` returns **zero hits**. Nobody in the family
defines help content. Design owns error *copy* (`content.md:45`) and IA (`information-architecture.md`),
`docs-writer` is a global skill aimed at developer docs, and no pack owns customer-facing help/KB
strategy. This is a grep-verified empty judgment layer — the same class of evidence that justified
the quality pack's narrow wedge.

**Orphan #2 — expectation-setting and response-time commitments (`niche-and-vertical-design.md:148–156`).**
Buried in a healthcare *vertical playbook* is the only proto-SLA doctrine in the skill: set process
expectations, commit to a response time explicitly, and state it **at the point of action** ("near
the submit button"), with staged intake so routing-critical fields come first. Grep across all twelve
packs for `response.time commitment|state (the )?response time|what happens next|expectation setting`
returns **zero hits**. Operate owns internal SLOs and incident timing; nobody owns the customer-facing
promise of *when a human will reply*. That is support process design, and it is unclaimed.

**Collapse #1 — retention ethics is already double-shipped, and success must stay off it.** I
initially read the cancellation/dark-pattern material as success's churn-prevention ethics. It is
not available. Marketing shipped the table nearly verbatim at
`marketing/references/landing-pages-and-conversion.md:161–177`, including "**Endowment \|
Personalizing a real free trial \| Easy sign-up, deliberately hard cancellation**" (`:171`),
"**Default / progress \| Smart defaults, true progress state \| Forced continuity, a gamified bar
that never completes**" (`:170`), and the FTC framing at `:174–175`. Growth then shipped a
peer-reviewed deepening at `growth/references/monetization-and-pricing-experiments.md:143–158` —
Mathur et al. 2019 (11,000 shopping sites, **11.1% carried at least one dark pattern**), the roach-motel
pattern, and the FTC negative-option/cancellation-friction case — routed from `growth/SKILL.md:83`
and scoped at `monetization-and-pricing-experiments.md:14,33`. **Success must not ship a
cancellation-ethics section.** If a churn-save reference needs the line, it cites growth's file.

**Collapse #2 — the IA doctrine I wanted for KB structure is design's.** `design/references/
information-architecture.md:43,51` already carries plain-labels-beat-clever, 2–7 nav items, flat
hierarchy at 2–3 clicks, depth-vs-breadth at 3 levels, and card-sort/tree-test validation. A success
KB-strategy reference should cite design's IA file for *structure* and contribute only what design
does not have: what belongs in a KB at all, deflection honesty, and article lifecycle/staleness.

### 2.5 Completeness statement — what is NOT lifted, and why that is safe

The worker read all 23 files in full; the file-by-file table is in
[`_raw-lift-webdesign-sweep.md`](_raw/_raw-lift-webdesign-sweep.md) Part 2. Summary of what is left
behind and where it lands:

- **17 of 23 files (≈2,900 lines) are visual craft and build**: layout, typography, color, depth,
  decoration, imagery, motion, experimental/WebGL, section-design-workflow, design-direction,
  anti-default-catalog, art-review, design-thinking, tailwind-v4-theme, frontend-build-patterns,
  section-archetypes' main body, SOURCES. Owner: **`design`** and **`frontend`**, both shipped.
- **3 files are prospect persuasion and site strategy**: `persuasion-and-conversion.md`,
  `niche-and-vertical-design.md`, `trust-proof-and-structure.md`. Owner: **`marketing`** (positioning,
  landing pages, SEO structure, ASO) and **`growth`** (funnel mechanics, pricing psychology), both
  shipped, and growth already ran its own extraction from this skill in a prior run.
- **`design-critique.md` and `art-review.md`** are review gates. Owner: **`quality`** (which already
  carries the P1 boundary test verbatim) and **`design`** (`critique.md`).
- **Orphan check: none.** The worker found no file whose content is unclaimed by a shipped pack.

**Therefore: abandoning webdesign loses nothing for `success`.** The one thing it *does* lose —
Nielsen's "help & documentation" heuristic being scored but never defined (#2) — is a gap in
webdesign, not content in it. That empty slot is an argument *for* the success pack, not a loss from
retiring the old one.

---

## 3. Part B — the authoritative seam table (disk-verified)

### 3.1 Charter line-reference verification: 26 of 26 correct

Every line reference in charter.md:39–55 was opened and read. **All verify exactly.** No corrections.

| Charter claim | Ref | Verified text (excerpt) |
|---|---|---|
| marketing seam at signup | `marketing/SKILL.md:10` | "onboarding and retention (→ success)." |
| " | `marketing/SKILL.md:108` | "\| Onboarding education, retention communication, in-product activation nudges \| `success` \|" |
| " | `marketing/SKILL.md:118` | "improve conversion across the funnel, `success` owns retention." |
| " | `marketing/references/surface-selfserve-saas.md:94` | "**Trial-to-paid nudges and win-back once someone is a user** — `success` owns onboarding" |
| " | `marketing/references/surface-selfserve-saas.md:121` | "Pre-signup nurture and free-tier upgrade nudges; post-signup activation crosses to `success`" |
| " | `marketing/references/lifecycle-and-email.md:14` | "The email is in-product onboarding education after signup → `success`." |
| " | `marketing/references/lifecycle-and-email.md:136` | "**Onboarding education** (teaching a signed-up user how to use the product) → `success`." |
| app-review responses | `marketing/references/app-store-optimization.md:18` | "app-review-response handling as a support workflow → `success`." |
| community splits | `marketing/references/organic-social-and-community.md:136` | "`success`, depending on whether it's acquisition or retention being measured." |
| marketing handoff row | `marketing/references/handoff.md:43` | full two-way row, quoted in §3.2 |
| growth seam | `growth/SKILL.md:10`, `:113`, `:121` | "onboarding comms (→ success)"; "\| Onboarding education content, retention communications, churn-save messaging as sent \| `success` — provisional"; "`success` owns retention execution" |
| " | `growth/references/handoff.md:43` | full row, quoted in §3.2 |
| " | `growth/references/growth-model-and-loops.md:71–74` | "**`success` owns Retention *execution***… Growth designs and reads out the test; `success` sends the message the test validated." |
| product cedes adoption | `product/SKILL.md:28` | "and adoption to `success`; and business processes spanning systems the product does not own to" |
| " | `product/references/surface-app-saas.md:45` | "funnel experiments and PLG loops; `success` for onboarding and support." |
| operate | `operate/SKILL.md:90` | "\| Customer-facing incident comms, per-account outreach \| `product` / `success` \|" |
| " | `operate/references/incident-response.md:159` | "`success`. Operate states fact, impact, and timing; it does not manage the relationship." |
| " | `operate/references/decommissioning.md:186` | "that routes to `product`/`success` for the outreach — this file owns the technical" |
| automation | `automation/SKILL.md:104` | "\| Authoring the business rule, or customer-facing comms \| `product` · `marketing` · `sales` · `success` \|" |
| " | `automation/references/process-capture.md:15`, `:163` | "owned by `product`, `marketing`, `sales`, or `success` — read it"; "commercial skill once it exists" |

### 3.2 Cessions the charter MISSED (all newly verified)

| Pack | Ref | Verbatim | Why it matters |
|---|---|---|---|
| marketing | `references/handoff.md:59–60` | "Writing onboarding or retention copy inside a marketing deliverable instead of routing it to `success`, because the acquisition-to-activation line feels continuous from the writer's side." | A named **failure mode**, i.e. an enforcement clause, not just a routing row. |
| marketing | `references/handoff.md:61–62` | "Reading this pack's absence of `activation`, `retention`, or `referral` jobs as an oversight instead of the AARRR seam stated above." | Marketing pre-declares its own gap as intentional and success-shaped. |
| marketing | `references/handoff.md:51–52` | "AARRR spans three packs in this family, acquisition here, funnel-wide experiments in `growth`, retention in `success`" | The three-way AARRR contract, stated from marketing's side. |
| marketing | `references/surface-selfserve-saas.md:134–135` | "Treating activation and retention as marketing's to claim credit for, rather than `growth`'s and `success`'s per the seam above." | Second enforcement clause. |
| marketing | `references/organic-social-and-community.md:17–18` | "The question is retention inside an existing community/product, not acquisition into it → `success` or `growth`." | **Unresolved two-way route** — success must settle it (§5, Q3). |
| marketing | `SKILL.md:80` | "…where lifecycle hands off to `success`" | Router-row level cession. |
| marketing | **`assets/email-compliance-checklist.md:81`** | "- [ ] Onboarding education after signup → `success`" | **A cession inside a runnable asset**, not prose. Success inherits an email-compliance obligation. |
| marketing | `assets/email-compliance-checklist.md:82` | "- [ ] Dunning / billing-failure recovery → `product`" | **Involuntary churn is `product`'s, not success's** — contradicts CS-canon default (§5, Q2). |
| growth | `references/handoff.md:47–50` | "…`growth` owns the experiments that improve conversion across the whole funnel — Activation, Referral loop design and math, and Retention *experimentation*; `success` owns Retention *execution*" | The reciprocated AARRR note. |
| growth | `references/handoff.md:66–67` | "Reading this pack's absence of `acquisition` and **`retention-execution`** jobs as an oversight instead of the AARRR seam stated above." | **Growth names a job slot — `retention-execution` — that exists nowhere and is reserved for success.** Strong naming signal for success's job table. |
| growth | `references/handoff.md:68–69` | "Silently invoking `frontend`, `backend`, `design`, `data`, `marketing`, `product`, `operate`, `sales`, or `success` instead of naming the actual sibling and the specific artifact it owns." | Sibling-naming discipline success must reciprocate. |
| growth | `references/growth-model-and-loops.md:59–63` | "## The AARRR split, reciprocated… marketing's own shipped note states the split from its side" | Proof the seam is bilateral, not asserted once. |
| operate | `references/incident-response.md:21` | "Writing customer-facing incident copy or per-account outreach — that is `product`/`success`." | **Second operate cession** (charter had only `:159`). |

### 3.3 CLAIMS — what shipped packs keep, which constrains success

This is the half the charter does not have at all.

| Pack | Ref | Verbatim | Constraint on success |
|---|---|---|---|
| **design** | `references/journeys.md:3` | "Purpose: Design in-product flows and end-to-end journeys — breadboards, task flows, journey/service maps, **onboarding**, and guided multi-step paths" | Design owns onboarding **as a designed flow**. |
| **design** | `references/journeys.md:51–53` | "## Onboarding … Goal priority: get to first value fast > orient (**don't educate**) > build confidence > reduce setup friction. Onboarding's job is the **aha moment**, not teaching the product. Patterns: progressive / setup wizard / sample-data demo / interactive tour (sparingly, **3–5 core concepts, dismissable**)… Metrics: activation rate, time-to-activation, completion, drop-off by step, D7/D30 retention. Name the aha moment explicitly." | **The sharpest constraint in the family.** Design's shipped doctrine is *"orient, don't educate"* — success's canonical include is literally "education and enablement". These are not compatible by default; the seam must be drawn explicitly. |
| **design** | `references/journeys.md:49` | "Map the full arc: discovery → purchase → first run → onboarding → daily use → failure → **support/billing/offboarding**… audit the unseen surfaces (404, error copy, settings, loading, emails, invoices, **cancel flow**)" | Design's journey scope already runs through support and the cancel flow. |
| **design** | `references/journeys.md:45` | Service blueprint lanes: "physical evidence / customer actions / frontstage (visible) / backstage (invisible) / **support**… Trace a customer pain through frontstage → backstage → support" | "Support" here is the service-design *lane*, a naming collision with success's support process. |
| **design** | `references/content.md:45` | "**Empty states are onboarding moments in three beats**: name what is empty, say why it matters, give one button. New users spend more time in empty states than in any other state." | Onboarding UI copy is design's. |
| **design** | `references/content.md:58` | "\| Onboarding \| contextual, not a tutorial \|" | A voice rule that pre-empts in-product tutorial content. |
| **design** | `references/research.md:49` | "**NPS** 0–10 (Promoters 9–10, Detractors 0–6; NPS = %Promoters − %Detractors). **SUS** validated 10-question, 0–100, **68 = average, >80 good**… **~385 responses = ±5% at 95% confidence**" | **NPS's definition and survey method are already shipped in `design`.** Success's VoC work must cite, not redefine. |
| **design** | `references/journeys.md:11` | "The task is product-level journeys, roadmaps, or business metrics → product." | Design's escape hatch routes to `product`, never to success — design predates success. |
| **product** | `SKILL.md:62` | "\| Web or SaaS application \| App & SaaS \| Activation/retention, pricing tiers, MRR/churn metric trees, **commercial lifecycle** \|" | Product owns the commercial lifecycle as a *modeling* job. |
| **product** | `references/surface-app-saas.md:31–32` | "Pricing is tiered and lives inside a commercial lifecycle (**trial → paid → expansion → renewal/churn**)" | **`renewal` and `expansion` are named inside product's shipped lifecycle** — success's renewal-workflow claim is contested. |
| **product** | `references/surface-app-saas.md:38–39` | "The north star decomposes into an activation/retention/MRR/churn metric tree (HEART/AARRR)… **Guardrails watch churn and support load**, not bounce rate." | Churn and support load are product guardrail metrics. |
| **product** | `references/metrics.md:45–53` | "├─ Driver: **Signup → First-Value Time** / └─ Driver: **Onboarding Completion Rate** … ├─ Input: Retention Rate … └─ Driver: **Reactivation Rate** … ├─ Health: **NPS / CSAT, Support Ticket Rate**, Error Rate" | **Success's headline metrics are already defined in product's metric tree.** Success consumes them; it must not re-derive them. |
| **product** | `references/surface-app-saas.md:41` | "Track **churn/retention risk**, activation-drop risk, and pricing-tier cannibalization as named entries" | Churn *risk* is a product risk-register entry. |
| **product** | `references/business-model.md:76` | "Name one **expansion lever** (usage overage, add-on, seat growth) as a secondary revenue path" | Expansion as a pricing lever is product's. |
| **product** | `references/discovery.md:15`, `:75` | "access to users/customers or their proxies (**support tickets**, sales calls, forums)"; "mine public forums, review sites, **support tickets**, and competitor gaps for recurring complaints" | Product **consumes** support tickets as discovery input — the customer-to-product feedback loop already has a receiver. |
| **growth** | `references/handoff.md:49` | "`growth` owns … Activation, Referral loop design and math, and Retention *experimentation*" | Success may not claim activation, referral, or retention experiments. |
| **growth** | `references/retention-and-resurrection.md:168–169` | "A retention or resurrection mechanic is classified as **operate's (standing) or growth's (experiment-bound)** before work starts, per §7." | **A binary classification rule with no success option**, shipped inside growth's own retention file. Growth's handoff cedes retention *execution* to success, but its working rule offers only two boxes. Success must close this gap explicitly — it is the sharpest instance of "success is named in the contract but absent from the mechanics". |
| **growth** | `references/retention-and-resurrection.md:167` | "NPS never stands alone as a retention experiment's primary metric." | A fourth shipped NPS constraint (see design, product). |
| **product** | `references/risk-register.md:58` | "**L4** — a revenue or retention blocker: users refuse to pay, **churn**, or fail activation without it." | Churn is a product evidence-level, used to justify build-now. |
| **product** | `references/surface-mobile.md:35–36` | "Add the install→activation funnel and store-health metrics (rating, review velocity, **uninstall rate**) to the metric tree alongside in-app activation/retention." | Mobile churn (uninstall) is product's metric too — pairs with marketing's ASO cession of app-*review responses* to success. |
| **automation** | `assets/approval-policy-card.md:17,21,23` | Worked example: "Refund over $500, generated by the refund-request automation **from a matched support ticket**"… "an unreviewed refund does not go out; **the customer waits**, the money doesn't move"… evidence logged includes "**The original support ticket**" | Automation's flagship approval asset is a **customer-support workflow end to end**. Success owns the support process that produces the ticket and the refund policy; automation owns the gate. The seam is real and unstated. |
| **ai** | `references/surface-chat-assistant.md:9` | "The request is a chatbot, **support assistant**, copilot side-panel, or any 'talk to it' interface." | **`ai` claims the support-assistant surface**, with zero cession to success. Charter wedge #3 (success owns AI-support *policy*) is unstated on disk and must be drawn from success's side against this. |
| **ai** | `references/memory.md:105–106` | "`retrieval-and-rag.md` retrieves from an external, largely static **knowledge base** (docs, code, a wiki)" | Naming collision: ai's "knowledge base" = retrieval corpus; success's = customer help content. |
| **quality** | `references/defect-lifecycle.md:138`, `assets/severity-map.md:51` | "**'Would a real user contact support over this?'** If yes, it's at least P1." | The support-contact severity test is quality's. |
| **data** | `references/governance-pii-and-retention.md:69` | "When PII lives in free text (**support tickets**, LLM traces, unstructured logs)" | Support-ticket data is PII-bearing; success inherits data's governance constraint. |
| **architecture** | `references/decomposition.md:54–55` | "the same word meaning different things in different parts of the domain ('Customer' in Billing vs 'Customer' in **Support**) — that's a split signal" | Architecture already models Support as its own bounded context. |
| **sales (unbuilt)** | `marketing/SKILL.md:107` | "Pipeline, CRM stages, revenue operations, **sales enablement**, cold outbound and prospecting \| `sales`." | Naming collision: *sales* enablement ≠ *customer* enablement. Success must disambiguate. |

### 3.4 The handoff.md inventory

Eleven of twelve packs ship `references/handoff.md`; **`frontend` does not** (its nearest file is
`references/design-handoff-and-tokens.md`, which is a design-to-code token handoff, not a sibling
contract). Success-token hits per handoff file:

| Pack | handoff.md | success rows | Verdict |
|---|---|---|---|
| marketing | 62 lines | 3 | **Real** — row at `:43`, AARRR note `:51–52`, failure mode `:59–60`. |
| growth | 69 lines | 3 | **Real** — row at `:43`, AARRR note `:47–53`, failure modes `:66–69`. |
| design | 92 lines | 1 | **False positive** — `:39` "empty, loading, error, success" (UI state list). |
| product | 143 lines | 1 | **False positive** — `:103` "the success metrics from". **Product has no success row at all.** |
| backend, architecture, data, ai, quality, operate, automation | 116–149 lines | 0 | None. |

**The asymmetry is load-bearing, and in operate's case it is an outright inconsistency.** Only
`marketing` and `growth` gave `success` a *formal* handoff contract. `product`, `operate`, and
`automation` cede to success in prose and router tables but **never in their handoff file** — the
artifact the family treats as the binding two-way contract.

Operate is the clearest case. Its prose cedes to `product`/`success` in three separate files, but its
handoff table's only customer-facing row names **`product` alone**:

> `operate/references/handoff.md:79` — "\| Decommission / dependency-withdrawal notice \| The owning
> build skill, **or `product` if customer-facing** \| A sunset date or a forced migration (I8…) \|"

compared with its own prose at `operate/references/decommissioning.md:185–187`: "that routes to
**`product`/`success`** for the outreach". The formal contract and the reference text disagree about
whether success exists. Worth a one-line PR to operate at success's release.
Success's own handoff.md must therefore *originate* the rows for product, operate, and automation
rather than mirror them, and should expect no reciprocal row to point back at.

The two real contracts, verbatim:

- `marketing/references/handoff.md:43` — "\| `success` \| Acquisition-side lifecycle content
  (pre-signup nurture, the newsletter) and the narrative marketing used to acquire the user, for
  onboarding continuity \| Retention and churn signal that feeds messaging and CEP work \| Onboarding
  education and retention communication are `success`'s; marketing's lifecycle job stops at
  acquisition, per surface-selfserve-saas.md's seam-at-signup section \|"
- `growth/references/handoff.md:43` — "\| `success` (provisional) \| An experiment readout on a
  retention or resurrection mechanic \| Retention and churn signal that surfaces what's worth testing
  next \| `growth` owns retention *experimentation* — does a resurrection nudge work; `success` owns
  retention *execution* — sending the message a growth test validated \|"

**Note the asymmetry in confidence.** Marketing states the seam flatly; growth labels its own
"(provisional)". Marketing's `SKILL.md:118` says "`success` owns retention" without qualification.
Success should adopt growth's provisional framing when citing growth, and marketing's firm framing
when citing marketing — not flatten the two.

### 3.5 Emptiness verified for the seven silent packs

Independently grepped: **zero occurrences of `` `success` `` in design, frontend, backend,
architecture, data, ai, quality.** Raw hits for the term "success" in those packs resolve to UI/
engineering senses — form and fetch state machines (`design/references/interaction.md:82`,
`frontend/references/state-and-data.md:51–52`, `frontend/references/forms.md:105`), the 8-state
component model (`design/references/design-systems.md:53`), empty/error/success taxonomy
(`frontend/references/accessibility.md:240`), and "success metrics"/"success criteria". "Support"
resolves overwhelmingly to browser/platform/library support; "churn" to framework, content, and
pricing-layer churn; "escalation" to incident escalation (`operate`), approval escalation
(`automation`), model-tier escalation (`ai`), reviewer escalation (`quality`), and isolation-level
escalation (`backend`).

The worker's independent sweep reproduced this and supplies the volumes behind it — the evidence that
emptiness was *verified*, not assumed:

| Pack | CESSION | NAMED-BOUNDARY | CLAIM | False positives / raw hits |
|---|---|---|---|---|
| marketing | 11 | 2 | 1 | ~275 / 290 |
| growth | 5 | 0 | 2 | ~478 / 491 |
| product | 2 | 0 | 6 | ~198 / 211 |
| operate | 4 | 2 | 0 | ~359 / 364 |
| automation | 3 | 0 | 0 | ~296 / 299 |
| frontend | 0 | 0 | 0 | ~500 / 502 |
| backend | 0 | 0 | 0 | 258 / 258 |
| architecture | 0 | 0 | 0 | 198 / 198 |
| design | 0 | 0 | 0 | 208 / 208 |
| data | 0 | 0 | 0 | 236 / 237 |
| quality | 0 | 0 | 0 | 387 / 387 |
| ai | 0 | 0 | 0 | 206 / 206 |

**Emptiness of *cession* is confirmed. Emptiness of *territory* is refuted for `design`** (§3.3) and
qualified for `ai` (support-assistant surface) and `data` (support-ticket PII). The charter's
sentence should be amended accordingly — and so should the raw file's own "design — VERIFIED EMPTY"
heading, which is why a dated correction note sits at that section.

Two refinements from the worker worth carrying:

- **`automation` pre-dated success and says so.** `automation/references/process-capture.md:15–17`:
  "The rule already exists in writing, owned by `product`, `marketing`, `sales`, or `success` — read
  it and cite the owner; do not recapture it here. (**At this pack's launch those three commercial
  upstreams do not yet exist as shipped skills** — say that plainly rather than inventing an owner.)"
  Success's arrival closes a gap automation explicitly logged.
- **Operate's boundary language is the sharpest in the family** and should be the model for success's
  own reciprocal wording — `operate/references/incident-response.md:158–159`: "Customer-relationship
  framing and per-account outreach are not operate's call — route to `product` / `success`. **Operate
  states fact, impact, and timing; it does not manage the relationship.**"
- **Customer-facing incident and decommission comms are co-owned `product`/`success`, never `success`
  alone** — operate says so in three separate files with identical phrasing (`SKILL.md:90`,
  `incident-response.md:21,158–159`, `decommissioning.md:185–187`). Success must not claim sole
  ownership of incident comms.
- **Product hands success a PRD, not a bare recommendation.** `product/references/surface-app-saas.md:24,35`
  makes onboarding first-class PRD scope ("**Onboarding and the core loop are always first-class scope
  sections, not implicit.** State time-to-first-value and the loop's repeat trigger as acceptance
  criteria") while `:45` recommends success for onboarding execution. Success should expect onboarding
  acceptance criteria as an input.

---

## 4. Corrections to the charter (dated 2026-08-02)

1. **charter.md:56 — amend.** "ZERO cessions on disk … Success draws those seams from its own side"
   is true about cessions and misleading about territory. Replace the inference with: *design ships
   a full onboarding reference (`journeys.md:51–53`) and owns NPS's definition (`research.md:49`);
   ai claims the support-assistant surface (`surface-chat-assistant.md:9`); data constrains
   support-ticket PII (`governance-pii-and-retention.md:69`). These are contested seams success must
   negotiate, not empty space it may occupy.*
2. **charter.md:51 — reclassify.** The "Doc evidence map: 'Adoption, support, satisfaction, and churn
   evidence → /success'" is presented under a heading that says "verify from disk — binding seam
   contracts **already shipped by siblings**". It is not shipped by product. It lives at
   `digital-product-skill/docs/product-lifecycle-skill-packs-exploration.md:1180`, inside §5.3
   "Research ownership in detail" — a **planning table for the whole family**, not a product-pack
   seam. It should be cited as a mandate (success owns adoption/support/satisfaction/churn
   *research*) with its real provenance, and moved out of the shipped-seams section.
3. **charter.md:50–51 — extend.** The product entry describes product only as a ceder. Product is
   also the family's largest **claimant** against success: the commercial lifecycle including
   renewal and expansion (`surface-app-saas.md:31–32`) and the metric definitions for onboarding
   completion, time-to-first-value, reactivation, NPS/CSAT and support-ticket rate
   (`metrics.md:45–53`).
4. **charter.md:52 — extend.** Operate has a second cession at `incident-response.md:21`, not only
   `:159`.
5. **charter.md:39–45 — extend.** Marketing has cessions in seven more places than listed, including
   one inside an **asset** (`assets/email-compliance-checklist.md:81`) and two enforcement clauses
   in `handoff.md:59–62`. Marketing is a 9-surface ceder, not 8-file.
6. **charter.md:124 — note.** The mandate's webdesign path is the stale v1.2.0 install; canonical is
   the v1.3.2 repo. Immaterial to the lift-list (§2.1), but any future extraction should use the repo.

---

## 5. Open questions for the controller

1. **Advocacy sourcing.** Who identifies and qualifies a referenceable customer — success (it owns
   "expansion and advocacy" and holds the relationship) or marketing (it owns case studies and
   testimonials as conversion proof, `webdesign/trust-proof-and-structure.md:83–95` →
   `marketing`)? No shipped pack draws this line. Recommended: success qualifies and secures consent;
   marketing produces and publishes.
2. **Involuntary churn.** `marketing/assets/email-compliance-checklist.md:82` assigns "Dunning /
   billing-failure recovery" to **`product`**. The CS canon treats involuntary churn (failed cards,
   dunning) as core retention work. Does success accept product's ownership of dunning and confine
   itself to voluntary churn? This needs an explicit ruling; it is the kind of gap the pack will be
   judged on.
3. **Community retention.** `marketing/organic-social-and-community.md:17–18` routes retention inside
   an existing community to "`success` **or** `growth`" — an unresolved fork shipped in a sibling.
   Success should resolve it in its own handoff and state that it is resolving a previously open route.
4. **Onboarding: education vs orientation.** `design/journeys.md:53` ships "orient (**don't
   educate**)"; success's canonical include is "education and enablement". Recommended seam: design
   owns the in-product onboarding *flow* (patterns, empty states, wizard mechanics, copy); success
   owns the onboarding *program* — the implementation/adoption plan, the education artifacts that
   live outside the product (docs, KB, guides, enablement sessions), and adoption over time. This
   needs stating in success's SKILL.md or it will read as a land-grab against a shipped pack.
5. **The word "escalation" is already three-way loaded** — incident (`operate`), approval
   (`automation`), model-tier (`ai`), reviewer (`quality`). Success's "escalation" means *customer*
   escalation. It must be qualified on every use.
6. **A sibling will need an edit when success ships.** `automation/references/process-capture.md:16–17`
   reads "(At this pack's launch those **three** commercial upstreams do not yet exist as shipped
   skills — say that plainly rather than inventing an owner.)" It lists four owners at `:15`
   (`product`, `marketing`, `sales`, `success`), of which only two were unshipped at automation's
   launch. The count is already wrong, and success shipping leaves only `sales` unbuilt. Worth a
   one-line PR to automation at success's release, and a reminder that success's own forward
   references to `sales` will age the same way.
7. **NPS is claimed three times over** before success exists: `design/research.md:49` (definition +
   survey method), `product/metrics.md:53` (health metric), and `growth/references/
   retention-and-resurrection.md:167` ("NPS never stands alone as a retention experiment's primary
   metric"). Success's VoC/health work should consume all three and add only what none has — which, per the charter's flagship hypothesis, is the *interpretation*
   question (what an NPS number can honestly support), not the arithmetic.

---

## 6. What this channel did NOT cover

- **No external tracing.** Every CITE (the FTC negative-option rule, Stanford Web Credibility,
  Kurosu & Kashimura, the "47% expect <2s" and "75% judge credibility on design" figures in
  `niche-and-vertical-design.md:41,46` and `trust-proof-and-structure.md:10`) is handed to channel D
  untraced — local-disk mandate.
- **No skill-ecosystem or repo scanning** — channels A and C.
- **The `sales` seam is inspected only from the shipped side.** Every pack that names `sales` treats
  it as unbuilt (`automation/process-capture.md:163`: "commercial skill once it exists"). The
  renewals/expansion boundary against a future sales pack cannot be verified from disk.
- **The `success`-side of every seam is unwritten by design.** This channel establishes what the
  siblings already committed to; it does not draft success's reciprocal handoff rows. The writers
  own that, and §3.4 flags that product, operate and automation rows must be *originated*, not
  mirrored.
- **No pack was edited.** Two sibling defects are recorded for the controller (§5 Q6 on automation's
  stale count; §4 on the charter) but nothing outside `success-skill/research/` was touched.
