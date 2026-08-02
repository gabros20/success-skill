# Live activation + traversal eval — `success` v0.1.0

Repo: `/Users/tamas/Documents/Personal/Projects/success-skill` @ 62a9820 (review-clean).
Neighbour catalog read from the 12 local sibling repos at
`/Users/tamas/Documents/Personal/Projects/<name>-skill/skills/<name>/SKILL.md` — all 12 present.
`sales` is named by three packs (marketing, growth, success) but **does not exist locally**.

Method: the router sees only frontmatter `description:` text. Every verdict below is decided by
quoting the competing description strings, never the body of any SKILL.md. Bodies were used only in
Pass 2, to confirm the destination content exists.

---

## Headline

| Verdict | Count |
|---|---|
| CORRECT | 20 |
| COLLISION (both plausible) | 4 |
| WRONG-PICK | 1 |
| ORPHANED | 1 |
| **Total** | **26** |

One description-level fix is warranted (the WRONG-PICK). The current description is **591 chars**
against the 600 limit — 9 chars of headroom, so the fix must be near net-zero. A 593-char
replacement is proposed in §3 that keeps every existing routing fact intact.

---

## 1. Pass 1 — activation

`S` = success. Deciding words are quoted from the competing descriptions verbatim.

### 1a. Clearly-success prompts

| # | Prompt | Router picks | Deciding words | Verdict |
|---|---|---|---|---|
| 1 | "Audit our customer health score — it's green for accounts that churn." | S | S: "audit a health score" (near-verbatim); "health and churn-risk honesty". No sibling description contains "health score". `data`'s claim is "metrics/semantic layer… design a tracking plan" — a warehouse metric, not a score audit | **CORRECT** |
| 2 | "Set a first-response SLA for our support inbox." | S | S: "SLAs as promises", "design a support process". `operate` says "SLOs and alerting" — SLO, not SLA — and S pre-empts with "internal SLOs (→ operate)". "support inbox" is the decider | **CORRECT** |
| 3 | "What should go in our knowledge base, and how do we keep articles from going stale?" | S | S: "help content and KB". `marketing`'s "content, landing pages" sits inside "create, capture, and attribute demand" — acquisition content. `ai` owns "RAG" over a KB, not its editorial scope | **CORRECT** |
| 4 | "Design a churn-save motion for accounts we've flagged at risk." | S | S: "run a churn-save" (verbatim) + "retention execution". `growth` says "retention" but its use-clause is "size a test, diagnose a funnel drop, or design/read out an experiment" — no test is being asked for. S's "retention experiments (→ growth)" draws the line | **CORRECT** |
| 5 | "Our biggest account renews in three weeks — how do we read the risk and run it?" | S | S: "run a churn-save or renewal", "renewals/expansion (NRR)". Only pack whose description contains "renewal" | **CORRECT** |
| 6 | "When should our support bot hand off to a human, and what counts as resolved?" | S (`ai` second) | S: "AI-support policy" — an exact category match. `ai`: "agents… guardrails" is generic; S pre-empts with "agent mechanics/evals (→ ai)", which a router reads as *this pack owns the policy, that one owns the loop* | **CORRECT** |
| 7 | "Build a 90-day onboarding and adoption program for new enterprise customers." | S | S: "onboarding programs" (plural noun = the program, not the screen). `design` owns "user journeys… interaction and state design"; S's "Not in-product onboarding flow (→ design)" separates them. "90-day", "program", "customers" all point away from UI | **CORRECT** |
| 8 | "Our NPS dropped from 42 to 31 this quarter — what does that actually tell us?" | S | S: "voice-of-customer interpretation". **No sibling description contains "NPS", "CSAT", or "CES".** `design` says "UX research", `product` says "user and market research" — neither names the instrument | **CORRECT** |
| 9 | "Write the customer-facing update for last night's outage." | S (`operate` second) | S: "incident comms". `operate`: "incidents… run an incident". "customer-facing" is the decider, and S's only operate-eject is "internal SLOs (→ operate)" — it does **not** cede incidents wholesale, so the comms half stays | **CORRECT** |
| 10 | "Reply to these one-star App Store reviews." | **`marketing`** | `marketing`: "app-store listings (ASO)" — the only description containing "app-store". **S's description says nothing about app reviews, stores, or mobile.** S's *body* owns this (`support-process-design` row: "including the app-store-review channel"; `surface-mobile-subscription.md:32` "App-review responses are a support workflow, not ASO copy") and `marketing`'s *body* cedes it (`app-store-optimization.md:18`: "app-review-response handling as a support workflow → `success`") — but neither cede survives into the descriptions, which is all a router sees | **WRONG-PICK** |
| 11 | "Do we even need a customer success function yet? We're 3 people with 400 users." | S | S: "does a success function apply yet" — uniquely claimed; no sibling description contains an existence/applicability gate for its own domain | **CORRECT** |
| 12 | "Set up a ticket taxonomy and status buckets for our helpdesk." | S | S: "support process", "design a support process". `automation` owns "cross-system… processes" but its examples are "wire Stripe, a CRM, email and Slack together" — integration, not classification | **CORRECT** |

### 1b. Boundary probes — should route AWAY from success

| # | Prompt | Router picks | Deciding words | Verdict |
|---|---|---|---|---|
| 13 | "Design an experiment to test whether a streak feature improves 30-day retention." | `growth` | `growth`: "experiment design and prioritization… retention", "size a test". S ejects verbatim: "retention experiments (→ growth)" | **CORRECT** |
| 14 | "Design the in-product onboarding flow — empty states, checklist, progressive disclosure." | `design` | `design`: "interaction and state design", "user journeys", "product UI". S ejects verbatim: "Not in-product onboarding flow (→ design)". Corroborated by `design`'s own shipped eval `trigger-onboarding-states` (should_trigger: true) | **CORRECT** |
| 15 | "Build the RAG pipeline for our support bot — chunking, reranking, eval harness." | `ai` | `ai`: "RAG… evals". S ejects verbatim: "agent mechanics/evals (→ ai)". Corroborated by `backend`'s eval `negative-ai-rag-core` on the same prompt shape | **CORRECT** |
| 16 | "What should our internal SLO be for API availability?" | `architecture` / `operate` | `architecture`: "set SLO/perf/cost budgets"; `operate`: "SLOs and alerting" but ejects "SLO targets… (→ architecture)". S ejects with "internal SLOs (→ operate)". S correctly stays out either way | **CORRECT** |
| 17 | "Write a 5-email lifecycle nurture sequence for trial users." | `marketing` | `marketing`: "marketing email and lifecycle campaigns". S ejects verbatim: "lifecycle email (→ marketing)". Bidirectionally consistent — `marketing` ejects "onboarding and retention (→ success)", and this is neither | **CORRECT** |
| 18 | "Design an NPS survey — question wording, scale, sampling, timing." | S (should be `design`) | S: "voice-of-customer interpretation" — "interpretation" is the limiter and it does most of the work, but S is still the **only** description naming NPS. `design`'s "UX research" is generic. A router plausibly lands on S; S's body then self-corrects (`voice-of-customer.md:17` cites `design`'s research file as owning the 0–10 scale and method) | **COLLISION** |
| 19 | "Build a churn prediction model — features, training, evaluation." | S | S: "health and churn-risk honesty" — the only description containing "churn-risk". `data`'s "build or model pipelines" is data pipelines; `ai` is "model-powered behavior" (LLM). **No pack in the family claims classical ML engineering.** S is the correct best home and its body covers building (`health-and-risk-signals.md:6` "building, buying, or interpreting a health score, churn model", §5 "Honest ceilings: what the ML actually achieves") | **CORRECT** (family gap noted) |
| 20 | "Our support tickets have customer PII in free text — what do we do?" | `data` | `data`: "governance/PII", "govern PII". **S's description says nothing about PII** — a clean, deliberate silence. S's body inherits rather than invents ("Success inherits data's free-text-PII constraint") | **CORRECT** |
| 21 | "Auto-approve refunds under $50 and route the rest for human approval." | `automation` | `automation`: "behind which approval", "design an approval gate", "human-in-the-loop processes". S's description names no refund/approval mechanic | **CORRECT** |
| 22 | "Close the expansion deal with this account — negotiate the upsell." | nothing installed | S ejects correctly: "the sale (→ sales)". `marketing` also ejects "sales pipeline or cold outbound (→ sales)", `growth` "cold outbound (→ sales)". **No `sales` pack exists locally**, so the prompt lands nowhere. S's competing pull is "renewals/expansion (NRR)", which could grab it | **ORPHANED** (by design; S's decline is correct and its body flags §6 as provisional/contested) |
| 23 | "Is our account retention actually improving? We sell annual B2B contracts." | S **and** `growth` | S: "renewals/expansion (NRR)", "retention execution". `growth`: "funnel diagnosis… retention", "diagnose a funnel drop". **`growth` ships this exact prompt as a positive**: `b2b-account-retention-composition` expects `surface-b2b-sales-assisted.md` + `funnel-and-cohort-diagnosis.md` and requires reading it "as logo retention and gross/net revenue retention". Both packs claim revenue-retention reading; neither description ejects to the other on it | **COLLISION** |
| 24 | "Our card-decline dunning emails aren't recovering revenue — fix the flow." | `marketing` or `automation` (not `product`) | S ejects correctly and specifically: "pricing/dunning (→ product)". But **`product`'s description contains neither "dunning" nor "billing"** — its nearest is "business-model and pricing". `marketing` ("marketing email and lifecycle campaigns") and `automation` ("wire Stripe, a CRM, email… together") are both stronger literal matches. S's decline is right; the receiving description is thin | **COLLISION** (S's side correct; the gap is in `product`'s description, out of scope for this fix) |
| 25 | "Should we use Intercom or Zendesk, and wire our helpdesk into Slack?" | split: S + `automation` | S: "design a support process" (tool choice for the support process); `automation`: "wire Stripe, a CRM, email and Slack together" (near-verbatim on the second clause). This is a genuinely two-part prompt and the split is the right answer, not a defect | **COLLISION** (benign — compound prompt) |
| 26 | "We're sunsetting the legacy plan — write the notice to affected customers." | S (`operate` second) | S: "incident comms". `operate`: "decommissioning… sunset a service". S's body co-owns this explicitly (`incident-and-account-comms.md:8` "a service, feature, or dependency is being decommissioned and affected customers need notifying"; :15 ejects the no-customer-facing-dimension case to operate). "write the notice to affected customers" is the decider | **CORRECT** |

---

## 2. Pass 2 — traversal

Eight correctly-activated prompts walked from the router table to the destination file. Spot-read
only; content confirmed present, not re-reviewed.

| # | Prompt | Router row → file | Promised content | Confirmed at |
|---|---|---|---|---|
| 1 | Health-score audit | "Build, buy, interpret, or audit a health score…" → `references/health-and-risk-signals.md` ⭐ | Score-vs-prediction; "not published, never not measured"; the Observability Question | `:24` §1 heading, `:37` §2 heading, `:59` §3 heading, `:33` and `:55` state the invariants; `:178` re-checks §3 before a non-contractual reader | **PASS** |
| 2 | First-response SLA | "Set up or audit a ticket taxonomy, SLA metrics, a response-time promise…" → `references/support-process-design.md` | first/next/resolution SLA naming; the never-ship rule against a copied default | `:26` "§4. The response-time promise, and the never-ship SLA default"; `:6-7` read-when covers "defining SLA metrics or a response-time promise"; `:18` produces "SLA metrics tied to an honest capacity check" | **PASS** |
| 3 | KB scope + staleness | "Decide what belongs in a knowledge base, keep it from rotting…" → `references/education-and-knowledge-base.md` | article-lifecycle rule; zero-result/zero-click backlog as the observable replacement for deflection rate | `:33` "§2. Article lifecycle: maintain aggressively or don't ship it"; `:34` "§3. Deflection is unmeasurable — the honest replacement"; `:28` produces "an observable backlog instrument instead of a percentage" | **PASS** |
| 6 | Bot escalation + "resolved" | "Define when a bot hands off, what 'resolved' means…" → `references/ai-support-policy.md` | escalation symbolic never a confidence float; nine real triggers, none numeric; resolution-rate honesty; pass^k | `:34` §heading "Escalation is symbolic, never a confidence float"; `:37` "Every trigger found is symbolic"; `:113` "No source defines 'resolution rate' precisely enough to audit"; `:140` "Reading pass^k against a vendor claim" | **PASS** |
| 7 | 90-day onboarding program | "Build an implementation/adoption plan, education artifacts outside the product…" → `references/onboarding-and-adoption.md` | TTFV consumed from the PRD, never re-derived; Murphy's current formula with the superseded form dated | `:34` and `:65` "Consuming TTFV as an input, not deriving it"; `:71` "do not re-derive a TTFV number from scratch"; `:73` grades the TTFV-causes-retention claim as "unsourced vendor folklore in every instance traced" | **PASS** |
| 8 | NPS trend reading | "Read an NPS/CSAT/CES score or a feedback trend honestly" → `references/voice-of-customer.md` | interpretation only, siblings own the metric; denominator check; replication failures | `:3` "Interpret NPS/CSAT/CES… what a score can support"; `:17` cites `design`'s research file for the 0–10 scale/method; `:19-20` consumes `product`'s metric tree; `:22` consumes `growth`'s NPS ruling | **PASS** |
| 11 | Existence gate | "Decide whether a distinct success function is worth building yet…" → `references/when-success-applies.md` | the attributed test; the CONTESTED pricing-first correction; AI tier-1 second | `:31`/`:37` "The Existence Gate"; `:42` "adapted from the one practitioner"; `:79` "1. Pricing first"; `:85` "2. AI tier-1 support second"; `:104` and `:131` carry the CONTESTED label forward | **PASS** |
| 5 | Renewal + NRR figure | "Run a renewal, evaluate an expansion signal, or report an NRR/GRR figure" → `references/renewals-and-expansion.md` | four audited NRR definitions that are not one metric; NNR; the sales seam at §6 | `:36` "§2. NRR/GRR: four audited definitions that are not one metric"; `:55` "Four SEC filings, read directly (not summarizer-paraphrased)"; `:37` §3 NNR; `:40` "§6. The sales seam — contested, not settled"; `:50-51` marks the sales clause provisional | **PASS** |

Extra spot-check for the WRONG-PICK (#10): the destination exists and is strong —
`references/surface-mobile-subscription.md:32` "App-review responses are a support workflow, not ASO
copy", `:15` records `marketing`'s cede, `:43-50` cover the platform cancellation path. **The
content is not the problem; only the description's silence is.**

**Traversal: 8/8 PASS.** Every router row reaches a file that delivers what the row promises.

---

## 3. Proposed description fix

Only one fix is warranted. It closes the single WRONG-PICK (#10) and is paid for by trimming three
phrases that lose no routing fact.

**Constraint:** current description = **591 chars**, limit 600 → 9 chars headroom.

### Recommended (593 chars, fits with 7 spare)

```
Keep customers after they buy — whether success applies yet, onboarding programs, help content and KB, support process, SLAs as promises, AI-support policy, health/churn-risk honesty, VoC/NPS interpretation, retention execution, renewals/expansion (NRR), app-review responses, incident comms. Use to design a support process, audit a health score, or run a churn-save or renewal. Not in-product onboarding flow (→ design), retention experiments (→ growth), pricing/dunning (→ product), agent mechanics/evals (→ ai), internal SLOs (→ operate), lifecycle email (→ marketing), the sale (→ sales).
```

Four word-level changes, nothing else:

| Change | Why | Δ |
|---|---|---|
| add `app-review responses,` before `incident comms` | fixes #10. Gives the router the only token that beats `marketing`'s "app-store listings (ASO)" on an app-review prompt. Matches `marketing`'s own file-level cede at `app-store-optimization.md:18` | +22 |
| `voice-of-customer interpretation` → `VoC/NPS interpretation` | pays for the above **and** strengthens #8/#18: surfaces the NPS token while keeping "interpretation" as the limiter against survey design | −10 |
| `does a success function apply yet` → `whether success applies yet` | same fact, fewer chars; still the unique existence-gate claim behind #11 | −6 |
| `health and churn-risk honesty` → `health/churn-risk honesty` | cosmetic; "churn-risk" token preserved for #1 and #19 | −4 |

Every `(→ pack)` eject is untouched, and every capability token that decided a CORRECT verdict above
(support process, SLAs as promises, AI-support policy, retention execution, renewals/expansion
(NRR), incident comms, onboarding programs, help content and KB) survives verbatim.

### Optional, only if 600 exactly is acceptable (600 chars, zero spare)

Adds `not survey design` to close COLLISION #18, paid for by `help content and KB` → `help
content/KB` and `VoC/NPS interpretation` → `VoC/NPS reading`:

```
Keep customers after they buy — whether success applies yet, onboarding programs, help content/KB, support process, SLAs as promises, AI-support policy, health/churn-risk honesty, VoC/NPS reading not survey design, retention execution, renewals/expansion (NRR), app-review responses, incident comms. Use to design a support process, audit a health score, or run a churn-save or renewal. Not in-product onboarding flow (→ design), retention experiments (→ growth), pricing/dunning (→ product), agent mechanics/evals (→ ai), internal SLOs (→ operate), lifecycle email (→ marketing), the sale (→ sales).
```

**Not recommended.** #18 is a *self-correcting* soft-fail — if success activates, `voice-of-customer.md:17`
immediately routes the survey-method half to `design`, so the user is not stranded. Spending the last
7 chars of headroom to save one hop is a bad trade against future edits.

### Collisions deliberately NOT fixed at the description level

- **#23 (NRR / account retention vs `growth`)** — real and confirmed by growth's shipped eval case.
  But the ambiguity is symmetric: `growth`'s description claims "retention" and "funnel diagnosis"
  without ceding revenue retention, while success claims "renewals/expansion (NRR)". Fixing this
  from success's side alone would need an eject that contradicts success's own ownership of NRR
  definitions (`renewals-and-expansion.md` §2, four audited SEC definitions). This is a **family
  seam that needs a two-sided ruling**, not a unilateral word change. Recommend logging it, not
  patching it.
- **#24 (dunning → `product`)** — success's eject is already correct and specific. The weakness is in
  `product`'s description, which never says "dunning" or "billing". Out of scope here.
- **#25** — benign; a compound prompt legitimately splitting across two packs.
- **#22 (`sales`)** — orphaned because the pack does not exist. Success's decline is correct and its
  body carries the provisional/contested label. Nothing to change until `sales` ships.

---

## 4. Reverse-capture check

Every sibling's eval directory was scanned for cases naming or implying `success`. Layouts differ:
eleven packs use `<repo>/evals/activation/cases.json`; `growth` uses
`<repo>/skills/growth/evals/{routing,never-ship,stats-cases}/cases.json`.

**Direct references to the success pack: 1 across all 12 siblings.**
A targeted grep for `→ success`, `` `success` ``, `to success`, `success pack`, `success skill`
across all sibling `evals/` returned **zero** matches — no sibling encodes a success handoff by name
in an eval assertion. The one case that targets success does so only in its `id`.

| Sibling case | Prompt | Sibling expects | Would success's description capture it? |
|---|---|---|---|
| `marketing/negative-success-onboarding` (`should_trigger: false`) | "Write the in-product onboarding checklist that teaches a new user how to set up their first workspace." | Declines it; the id points at success | **NO — and correctly so.** Success's description says "**Not in-product onboarding flow (→ design)**". The prompt's own words are "in-product onboarding checklist". This is a **three-way disagreement**: marketing declines toward success, success declines toward design, and `design`'s shipped positive `trigger-onboarding-states` ("Design an onboarding flow… every state from empty to error") confirms design wants it. **`design` is the right destination and both declines are correct** — marketing's case id is simply mislabeled (it should read `negative-design-onboarding`). No change to success. |

Secondary reverse-capture (siblings claiming success-domain prompts as their own positives, i.e.
the *other* direction of the failure mode):

| Sibling case | Prompt | Overlap with success | Assessment |
|---|---|---|---|
| `growth/b2b-account-retention-composition` | "We're a B2B SaaS selling annual contracts through a sales team. Is our account retention actually improving?" | Requires reading "gross/net revenue retention" — success claims "renewals/expansion (NRR)" | **Genuine two-sided collision** — see #23. Both packs would answer; both would answer competently but differently (growth as cohort diagnosis, success as the four audited NRR definitions). Needs a family ruling. |
| `growth/winback-and-streak-reaches-retention-file` | "We want to build a win-back campaign for lapsed users and are considering a streak feature to boost retention." | Success claims "retention execution" and lists win-back in its router | **Acceptable.** The prompt asks "good ideas?" — an evaluative/design question, which is growth's "experiment design". Success's claim is scoped to "a motion a test already validated". The descriptions agree at the boundary. |
| `architecture/positive-surface-agentic`, `ai/agent-construction-shape-first`, `automation/agentic-overlay-stacks-on-hosted-ipaas` | support-ticket triage/escalation agents | All touch support | **Clean.** Every one asks for harness, memory, eval gate, or platform wiring — success's eject "agent mechanics/evals (→ ai)" and its silence on platform wiring keep it out. Success would correctly not fire. |
| `product/positive-saas`, `product/retains-routing-discipline`, `design/*onboarding*`, `frontend/positive-compose-screen` | onboarding UI/PRD prompts | "onboarding" token | **Clean.** All are flow, screen, or PRD prompts; success's "onboarding **programs**" plus its explicit design eject keeps it out. |

**Reverse-capture verdict: PASS, with one mislabeled sibling case and one open family seam.**
No sibling eval expects success to capture a prompt that success's description would decline
incorrectly. The single case whose id names success is one whose prompt belongs to `design`, and
success declines it for the right stated reason.

---

## 5. Findings summary

1. **One description-level defect: app-review responses (#10).** Success owns the content and
   `marketing` cedes it in-file, but neither cede reaches the descriptions, so a router hands the
   prompt to `marketing`. Fixed by the 593-char replacement in §3.
2. **One open family seam: revenue retention / NRR, success vs `growth` (#23).** Confirmed against
   growth's shipped eval. Requires a two-sided ruling; do not patch unilaterally.
3. **One mislabeled sibling case:** `marketing/negative-success-onboarding` should be
   `negative-design-onboarding`. Cosmetic, in another repo, no behavioural impact.
4. **One family-wide gap (not success's):** `product`'s description never says "dunning" or
   "billing", so success's correct eject lands on a pack that does not visibly claim it (#24).
5. **Classical ML engineering has no home in the family (#19).** Success is the best available
   destination and its body handles it honestly (ceilings, leakage, base-rate theater). Noted, not
   a defect.
6. **Traversal is clean: 8/8.** No router row over-promises its destination.

No file was edited.
