# _raw-gh-voc-onboarding-csops

Channel C (github) — **lead slice**, written by the channel-C sub-orchestrator (not a worker).
Date: 2026-08-02. Scope: territory not assigned to the three workers — VoC / feedback-board tooling,
in-product onboarding tooling, churn-save (cancel-flow) code, the CS "awesome"/knowledge layer on
GitHub, the AI-support-policy incumbent (Parlant), and skill-pack flags for channel A.

All star counts, licence facts and timestamps read live on **2026-08-02** via `gh api` / raw.githubusercontent.
Every licence verdict below was reached by **opening the LICENSE file itself** (charter rule 3a) — the
GitHub API's `license` field is recorded alongside so the divergences are visible.

Raw search dumps backing the inventory: `_scan-gh-1.json` … `_scan-gh-6.json` in this directory
(commands are in the `=== header ===` lines of each file).

---

## 1. The negative space: customer success has no GitHub infrastructure layer

This is the single most important channel-C finding and it is an **absence**, so here is the evidence.

### 1.1 The topic terms are not even owned by this domain

`gh search repos --topic churn --limit 25 --sort stars` (dump: `_scan-gh-6.json`) returns, in order:

| stars | repo | what it actually is |
|---:|---|---|
| 1822 | benedekrozemberczki/awesome-fraud-detection-papers | fraud papers |
| 410 | julianrubisch/attractor | **code churn** complexity metrics |
| 295 | simonrenoult/code-complexity | **code churn**/complexity ratio |
| 52 | Phauthentic/cognitive-code-analysis | code complexity |
| 44 | mirzayasirabdullahbaig07/Customer-Churn-Prediction-Model | first actual customer-churn repo |
| 27 | antichainalysis/xmr-churner | **Monero** churning |
| 11 | bonedaddy/mychurnero | **Monero** churning |

The first customer-churn repo under `topic:churn` ranks **5th, at 44 stars**. Two of the top seven are
about Monero laundering and two are about source-code churn.

`gh search repos --topic retention --limit 25 --sort stars` is worse — the top eight are **backup
retention policies** (cv4pve-autosnap 561, Butterfly-Backup 123, btrfs-sxbackup 119, btrfs-backup 73,
BASH-RaspberryPI-System-Backup 45, backup-warden 35 …). The first customer-retention repo is
`churnkey/sdk` at 20 stars, 9th.

**Reading:** customer retention/churn is not a category with infrastructure on GitHub. It has no
namespace of its own; the words are squatted by unrelated engineering domains.

### 1.2 The `customer-success` topic

`gh search repos --topic customer-success --limit 30 --sort stars`:

| stars | repo | licence (API) | note |
|---:|---|---|---|
| 18225 | emcie-co/parlant | Apache-2.0 | AI **agent-control** framework — see §5 |
| 2670 | abhinavxd/libredesk | AGPL-3.0 | helpdesk (worker 1's slice) |
| 316 | zapier/gtm-cheat-codes | MIT | **agent-skill repo → channel A** |
| 93 | Gingiris/gingiris-b2b-growth | MIT | growth playbook |
| 33 | LeadMagic/gtm-skills | MIT | **agent-skill repo → channel A** |
| 24 | keon/awesome-customer-success | CC0-1.0 | see §4 |
| 11 | citizenjosh/customer-success-skills | other | **→ channel A** |

Excluding Parlant (an AI framework that tags itself `customer-success`) and libredesk (a helpdesk),
**the largest thing in the `customer-success` topic that is actually about customer success is a
24-star link list.** Third place is an agent-skill collection.

### 1.3 Contrast with the sibling packs

marketing's incumbent was a 42.5k★ repo. For success, the largest domain-native artifact found
anywhere in channel C's sweep is a **24-star vendor link directory** (§4). This strongly supports the
charter's wedge framing and is a cleaner "open niche" result than architecture's.

---

## 2. VoC / feedback-board tooling — the customer-to-product feedback loop, as modelled in code

### 2.1 Fider — the feedback-board status taxonomy

`getfider/fider` — 4,445★, AGPL-3.0 (LICENSE file is verbatim AGPLv3, no carve-out; root
`package.json` has **no** `license` field, `"private": true`), pushed 2026-08-01.

`getfider/fider@HEAD:app/models/enum/post_status.go` defines the complete taxonomy:

```go
PostOpen      PostStatus = 0   // "the default status"
PostStarted   PostStatus = 1   // "accepted and work is in progress"
PostCompleted PostStatus = 2   // "accepted and already implemented"
PostDeclined  PostStatus = 3   // "organizers decide to decline"
PostPlanned   PostStatus = 4   // "accepted and it's on the roadmap"
PostDuplicate PostStatus = 5   // "already been posted before"
PostDeleted   PostStatus = 6   // "completely removed ... should never be shown again"
```

Seven states, of which **`declined` and `duplicate` are first-class** — the two dispositions that a
feedback loop most often leaves implicit and that most damage trust when left implicit.

`getfider/fider@HEAD:app/models/entity/post.go` encodes the rule that terminal states stop
accumulating demand signal:

```go
func (i *Post) CanBeVoted() bool {
	return i.Status != enum.PostCompleted && i.Status != enum.PostDeclined && i.Status != enum.PostDuplicate
}
```

Note `planned` and `started` **remain votable** — demand keeps accruing while work is in flight.
Same file models the closing-the-loop artifact explicitly:

```go
//PostResponse is a staff response to a given post
type PostResponse struct {
	Text        string        `json:"text"`
	RespondedAt time.Time     `json:"respondedAt"`
	User        *User         `json:"user"`
	Original    *OriginalPost `json:"original"`   // the post this one duplicates
}
```

A status change without a `PostResponse` is structurally possible but the model clearly intends the
pairing — **status + written response + (for duplicates) a pointer to the original**. That is the
minimum honest shape of a "we heard you" reply and it is worth teaching as such.

### 2.2 Formbricks — impressions are modelled, so response rate has a denominator

`formbricks/formbricks` — 12,703★. **API license field: `NOASSERTION`.** The LICENSE file
(`formbricks/formbricks@HEAD:LICENSE`) is a multi-tier declaration:

> "Portions of this software are licensed as follows:
> - All content that resides under the "apps/web/modules/ee" directory … is licensed under the license defined in "apps/web/modules/ee/LICENSE".
> - All content that resides under the "packages/js/", "packages/android/", "packages/ios/" and "packages/api/" directories … is licensed under the "MIT" license …
> - … Content outside of the above mentioned directories or restrictions above is available under the "AGPLv3" license as defined below."

`formbricks/formbricks@HEAD:apps/web/modules/ee/LICENSE` is a commercial EE licence:

> "This software and associated documentation files (the "Software") may only be used in production, if you (and any entity that you represent) have agreed to, and are in compliance with, the Formbricks Subscription Terms of Service…"

Root `package.json` declares **no** `license` field at all (`"private": true, "version": "0.0.0"`).

**The teachable structure** — `formbricks/formbricks@HEAD:packages/database/schema/main.prisma`:

```prisma
model Display {
  id        String    @id @default(cuid())
  survey    Survey    @relation(...)
  contact   Contact?  @relation(...)
  response  Response?          // ← optional
  @@index([contactId, createdAt])
}
```

`Display` = *the survey was shown to someone*. `Response` = *someone answered*. A `Display` with
`response: null` is a **shown-and-ignored** event, recorded as first-class data. This is the schema
admitting what most NPS/CSAT reporting hides: **you cannot state a response rate unless you record
impressions**, and any NPS computed only over responders is a self-selected sample. The pack should
teach this shape directly — it is the honest-measurement content the charter wants, sourced to code
rather than to a vendor blog.

The same model carries the **survey-fatigue controls** as explicit fields on `Survey`:

```prisma
displayOption       displayOptions @default(displayOnce)  // displayOnce | displayMultiple | displaySome | respondMultiple
recontactDays       Int?
displayLimit        Int?
displayPercentage   Decimal?
delay               Int            @default(0)
autoClose           Int?
publishOn           DateTime?
closeOn             DateTime?
segmentId           String?
```

…plus targeting via `Segment.filters` (JSON), `SurveyAttributeFilter`, and event-driven firing via
`SurveyTrigger → ActionClass` where `ActionType` is `code | noCode`. And `SurveyQuota`, with
`countPartialSubmissions Boolean @default(false)` — an explicit decision about whether a partial
answer counts toward a sample quota.

**Why this matters for the pack:** "ask the right customer at the right moment, not everyone always"
is expressible as a concrete field list (`recontactDays`, `displayLimit`, `displayPercentage`,
segment filter, event trigger), not as advice.

### 2.3 The rest of the feedback-board tier

| repo | stars | API says | LICENSE file says | verdict |
|---|---:|---|---|---|
| getfider/fider | 4445 | AGPL-3.0 | AGPLv3, no carve-out | **CITE-ONLY** (structure quotable; AGPL) |
| astuto/astuto | 2352 | AGPL-3.0 | AGPLv3 | **CITE-ONLY + DEAD** — `archived: true`, last push **2026-01-09**. Still ranks 3rd in `topic:feedback`. Charter clause (d) in action. |
| logchimp/logchimp | 1112 | NOASSERTION | AGPLv3 + `packages/server/ee` and `packages/theme/src/ee` under a separate EE licence | **AMBIGUOUS** |
| chroxify/feedbase | 674 | AGPL-3.0 | (not opened — not load-bearing) | not assessed |
| clearflask/clearflask | 446 | Apache-2.0 | file is `COPYING`, verbatim Apache-2.0 | **LIFTABLE** |

---

## 3. In-product onboarding — Usertour's model, and the B2B account/user duality

`usertour/usertour` — 2,132★, pushed 2026-08-02 (actively developed).

**Licence (charter clause b fires here).** API says `NOASSERTION`. Two files exist:
`LICENSE` and `LICENSE.enterprise`.

`usertour/usertour@HEAD:LICENSE`:
> "Source code files that contain "enterprise" or "ee" in their dirname are licensed under the license defined in "LICENSE.enterprise". — **Any code controlling feature, permission, role and plan enablement.** — Content outside of the above mentioned directories or restrictions above is available under the "MIT Expat" license…"

`usertour/usertour@HEAD:LICENSE.enterprise`:
> "This software … may only be used in production if you … have agreed to, and are in compliance with, the applicable Usertour commercial subscription terms … Subject to the foregoing sentence, you are free to copy and modify this Software for development, testing, evaluation, and integration planning purposes."

But `usertour/usertour@HEAD:package.json` declares a flat **`"license": "MIT"`** — which contradicts
the LICENSE file's carve-out (the second bullet is not even directory-scoped; it is scoped by what the
code *does*). **Verdict: AMBIGUOUS.** This is a textbook charter-3(b) catch: the manifest hides the
carve-out, and a reader who trusted either the API (`NOASSERTION`) or the manifest (`MIT`) would be
wrong in opposite directions.

### 3.1 The account/user duality — the B2B success modelling fact

`usertour/usertour@HEAD:apps/server/prisma/schema.prisma`:

```prisma
model BizUser    { externalId String; bizCompanyId String?; bizUsersOnCompany BizUserOnCompany[]; … }
model BizCompany { externalId String; bizUsersOnCompany BizUserOnCompany[]; … }
model BizUserOnCompany {
  bizCompanyId String
  bizUserId    String
  data         Json     @db.JsonB       // ← per-membership attributes
  @@unique([bizCompanyId, bizUserId])
}
```

An explicit join table with **its own attribute bag** — a person's role/behaviour *within this
account* is distinct from the person and from the account. Segments then target either side:

```prisma
model Segment { bizType Int @default(1); source String? @default("internal"); sourceId String?; … }
model BizUserOnSegment    { … }
model BizCompanyOnSegment { … }
```

`Segment.source`/`sourceId` are documented in-schema as *"Source of the segment (e.g., "mixpanel",
"heap", etc.)"* / *"Source ID … (e.g., "mixpanel_cohort_id")"* — cohorts are imported from the
analytics stack rather than recomputed.

**Teachable:** health, adoption and risk are **account-level** questions answered from **user-level**
events, and the rollup needs a real membership edge. Every naive health score that averages user
engagement without a membership model gets multi-seat accounts wrong.

### 3.2 Onboarding progress is a session pinned to a flow *version*

```prisma
model BizSession {
  state         Int      @default(0)
  progress      Int      @default(0)
  currentStepId String?  @default("")
  bizUserId     String
  bizCompanyId  String?
  contentId     String   // the flow
  versionId     String   // ← the exact version the user saw
}
model Content { type String @default("flow"); publishedVersionId String? … }
model Version { sequence Int @default(0); steps Step[]; @@unique([contentId, sequence]) }
model Step    { sequence Int; type String?; target Json?; trigger Json?; @@unique([versionId, sequence]) }
```

`BizSession.versionId` means **onboarding analytics are pinned to the flow version actually shown**.
Change your onboarding and pre/post completion rates are not comparable unless you segment by version
— enforced in the schema, not left to discipline. This is a concrete measurement-honesty rule for the
onboarding section.

`Content.publishedVersionId` even carries an in-schema deprecation warning:

> `/// @deprecated Legacy field from before 'contentOnEnvironments' existed. … Reading this field directly picks the wrong version in multi-environment setups.`

`model BizAnswer { numberAnswer Int?; textAnswer String?; listAnswer String[]; @@unique([bizSessionId, cvid]) }`
— in-flow micro-survey answers, one answer per step per session.

### 3.3 The rest of the onboarding/engagement tier

`laudspeaker/laudspeaker` (2,615★) is a **self-contradicting licence**: the file
`laudspeaker/laudspeaker@HEAD:LICENSE` opens with `MIT License / Copyright (c) 2022 Tachyon Transfer,
Inc.` and then states *"Content outside of the above mentioned directories or restrictions above is
available under the "AGPLv3" license as defined below"* — with the AGPLv3 text following. API says
`NOASSERTION`. **Verdict: AMBIGUOUS** (an MIT header on an AGPL body is exactly the GeoLift-class
defect the charter warns about).

`dittofeed/dittofeed` (2,881★) — API MIT, LICENSE file is clean MIT, but **last push 2026-03-28**
(~4 months stale at time of writing). **LIFTABLE but check aliveness before depending.**

---

## 4. The CS knowledge layer on GitHub is a vendor directory that vendors edit themselves

### 4.1 keon/awesome-customer-success — 24★, CC0-1.0

LICENSE file opened: verbatim CC0 1.0 Universal. Created 2024-10-25. 202-line README.

Content is **exclusively vendor links** — 19 sections (Customer Success Platforms, Customer
Intelligence and Analytics, CRM, Helpdesk, Onboarding and Training, Feedback and Survey, BI,
Knowledge Base, Communication, Engagement, Churn Prediction and Retention, LMS, Project Management,
Advocacy, NPS, Community, Journey Mapping, Integration, Additional Resources), each a bullet list of
commercial products with one-line marketing descriptions. Gainsight, Totango, ChurnZero,
ClientSuccess, Planhat, UserIQ, Custify, SmartKarrot, Vitally, CustomerSuccessBox lead the first
section. **There is no method, no definition, no framework, no number anywhere in the file.**

**Provenance is the finding.** `gh api repos/keon/awesome-customer-success/commits?per_page=15`:

```
2026-07-31  Merge pull request #13 from Hellomatik-2/add-hellomatik
2026-07-31  Merge pull request #14 from pbbosshat/add-workforce-wave
2026-07-31  Add Workforce Wave to Customer Support and Helpdesk Software
2026-07-20  Add Hellomatik
2026-07-20  Merge pull request #12 from bwook00/patch-1
2026-07-20  Add Runbear to collaboration tools
2026-06-05  Merge pull request #6 from khushi-churnkey/patch-1
2026-06-05  Added Churnkey
2026-05-22  Merge pull request #5 from nadyyym/add-beton-inspector
2026-05-22  Add Beton Inspector to Customer Intelligence and Analytics
2026-05-01  Add Frigade to Onboarding and Training Tools
2026-02-17  Add Quackback - open source feedback platform
2026-01-20  Merge pull request #2 from levalex/add-feedback-tools
```

Every post-creation commit is a **vendor adding its own product**, from branches named after the
vendor and accounts named after the vendor (`Hellomatik-2`, `pbbosshat/add-workforce-wave`,
`khushi-churnkey`). 20 forks, 4 open issues, ~13 PRs lifetime.

**Verdict: LIFTABLE (CC0) but worthless to lift.** Its value is as *evidence*: the one curated CS
list on GitHub is a vendor self-promotion channel. Cite it for that, never as a source of practice.
This is charter rule 5 (vendor-density) confirmed at the infrastructure layer, not just the content layer.

### 4.2 mutedblues/Customer-Success-Management — 39★, **NO LICENSE FILE**, dead since 2020-01-24

`gh api repos/mutedblues/Customer-Success-Management/contents` returns **no** file matching
`licen|copying|notice`. API license: `NONE`. Last push **2020-01-24**. **Verdict: CITE-ONLY**
(charter clause d: no-license = cite only).

Structurally it is the *better* artifact — 209 lines organised as a curriculum (Core 1: what is CSM /
becoming a CSM / getting the job done / **measuring customer success** with sub-sections for ABF,
CLV, NPS, RFM / organizing your team / customer fit / journey mapping / onboarding; Core 2:
software, books, newsletters, blogs, podcasts, training; Core 3: interviews, case studies,
communities, thought leaders; Core 4: interview prep) with **pull-quoted definitions** rather than
bare links.

It also documents the vendor-density problem in miniature. Its "What is customer success?" section
quotes five definitions, of which the Gainsight one is presented alongside Lincoln Murphy's and the
Customer Success Association's without distinction:

> "Customer success is when your customers achieve their desired outcome through their interactions with your company." — Lincoln Murphy, sixteenventures.com
> "Customer Success is a long-term, scientifically engineered, and professionally directed strategy for maximizing customer and company sustainable proven value." — The Customer Success Association
> "The business methodology of ensuring customers achieve their desired outcomes while using your product or service…" — Gainsight

**FLAG TO D:** the Lincoln Murphy "desired outcome" definition (sixteenventures.com) is the most-cited
CS definition in the wild and appears to be the origin of the phrasing the whole canon reuses.
Channel D should trace it — and note that "scientifically engineered" (Customer Success Association)
is an unfalsifiable marketing phrase presented as a definition.

---

## 5. Parlant — the AI-support-policy incumbent nobody has named

`emcie-co/parlant` — **18,225★**, created 2024-02-15, pushed 2026-07-12, `archived: false`.
Topics include `customer-service` **and** `customer-success`.

**Licence: LIFTABLE.** `emcie-co/parlant@HEAD:LICENSE` is verbatim Apache-2.0; `pyproject.toml`
declares `license = "Apache-2.0"`, `version = "3.3.1"` — **manifest and LICENSE agree** (the only
repo in my slice where they do). No `ee/` directory in the root tree.

It self-describes as *"Looking for an open-source alternative to Ada, Decagon, or Sierra?"* —
i.e. it positions directly against the AI-support-agent vendors — and as *"The interaction control
harness for customer-facing AI agents"*.

### 5.1 Why this is success-pack content, not ai-pack content

Parlant's primitives are **policy artifacts**, which is exactly the seam the charter draws
(*"family uniquely has `ai` for mechanics; success owns POLICY"*). From
`emcie-co/parlant@HEAD:README.md`:

- **Guidelines** — *"Behavioral rules as condition-action pairs; the engine matches only what's relevant per turn."*
- **Relationships** — dependency and **exclusion** edges between guidelines. Verbatim example:
  ```python
  # In conflicting reads of the customer, set which takes priority
  await for_beginners.exclude(for_experts)
  ```
  A support policy needs conflict resolution, and here it is a first-class edge rather than prose ordering.
- **Journeys** — *"Multi-turn SOPs (Standard Operating Procedures) … The agent follows the flow but adapts — it can fast-forward states, revisit earlier ones, or adjust pace"*. A support playbook as a state machine that is allowed to be entered out of order.
- **Canned Responses** — *"Pre-approved response templates that eliminate hallucination at critical moments."*
- **Glossary** — domain vocabulary.
- **Explainability** — *"Full OpenTelemetry tracing — every guideline match and decision is logged."*

### 5.2 The strict/fluid output split — the bot-boundary mechanism, in a diagram

The engine flowchart in the README branches after tool-calling:

```
C["Call Contextually-Associated Tools and Workflows"]
C -->|Fluid Output Mode?| D["Generated Message"]
C -->|Strict Output Mode?| E["Canned Message"]
```

**Two output modes**: generate freely, or emit only pre-approved text. This is the cleanest
statement in code of the policy question the success pack owns — *at which moments is the bot
allowed to compose, and at which must it only select?* Refunds, cancellations, legal/compliance
statements, outage acknowledgements are the obvious "strict" moments. Parlant makes the choice a
per-interaction configuration rather than a prompt hope.

### 5.3 Stated design rationale (quote-worthy, and honest about the tradeoff)

> "**System prompts** work until production complexity kicks in. The more instructions you add to a prompt, the faster your agent stops paying attention to any of them.
> **Routed graphs** solve the prompt-overload problem, but the more routing you add, the more fragile it becomes when faced with the chaos of natural interactions."

and, on its own cost:

> "That approach adds complexity, but it gives teams tighter control over how the agent behaves in real conversations."

**Caveats to carry forward.** The README's evidence for reliability is (a) an arXiv citation and (b)
named-practitioner testimonials (Slice Bank, JPMorgan Chase, "Orcale" [sic]) plus the unsourced claim
*"Parlant is deployed in production at the most stringent organizations, including banks."*
**Testimonials are not measurement** — grade as practitioner-report, and do not repeat the
banks claim as fact.

**FLAG TO D:** arXiv **2503.03669** — "Attentive Reasoning Queries (ARQs)", cited by Parlant as the
research its anti-misalignment design is built on. Channel D should read the actual paper and check
what was measured, on what, and whether the claimed consistency gains are reproducible. Parlant is
the vendor of the idea, so this is exactly a "read the primary source" case.

**Cross-check for worker 3:** worker 3 was pointed at tau-bench/eShopSupport/Rasa and *not* at
Parlant. If worker 3's report does not mention Parlant, this section is the only coverage of it.

---

## 6. Churn-save execution: the cancel-flow taxonomy

`churnkey/sdk` — 20★, pushed 2026-07-30. LICENSE file opened: MIT, `Copyright (c) 2026 Churnkey, Inc.`
API agrees (MIT). **Verdict: LIFTABLE**, with the caveat that it is vendor-published OSS with a
hosted upsell (`@churnkey/node` exists *"Only needed if Churnkey is handling billing actions for
you"*, and the README links a free-account signup).

Small repo, but it encodes the **churn-save artifact** the growth seam assigns to success (growth
tests whether a save offer works; success executes it). From `churnkey/sdk@HEAD:README.md`:

```tsx
<CancelFlow
  steps={[
    { type: 'survey', title: 'Why are you leaving?',
      reasons: [
        { id: 'expensive',  label: 'Too expensive',           offer: { type: 'discount', couponId: 'STRIPE_SAVE20', percentOff: 20, durationInMonths: 3 } },
        { id: 'not-using',  label: 'Not using it enough',     offer: { type: 'pause', months: 2 } },
        { id: 'missing',    label: 'Missing features' },      // ← deliberately no offer
      ] },
    { type: 'feedback', title: 'Anything else?' },
    { type: 'confirm' },
  ]}
  handleDiscount={...} handlePause={...} handleCancel={...}
/>
```

The teachable structure: **cancellation reason → matched save offer**, where the offer *type* is a
function of the *reason* (price → discount; low usage → pause; missing feature → **no offer, just
capture**). Followed by free-text feedback and an unobstructed confirm step. Three steps, three
distinct jobs: diagnose, attempt save, exit cleanly.

The third reason having no `offer` is the honest part — some reasons have no save, and the flow
records them as churn-with-a-reason rather than fighting. The `survey` step is simultaneously the
**exit-interview VoC instrument**, which is the highest-signal VoC moment a self-serve product gets.

**Boundary note for the controller:** the *design* of which offer to make to which reason, and
whether discounting works at all, is a growth **experiment** question. The *flow, the reason
taxonomy, the exit-interview capture, and running it* are success **execution**. Recording per
charter rule 6 rather than assigning.

---

## 7. Skill-pack repos — FLAG TO CHANNEL A

Encountered in `topic:customer-success`, `"customer success"` and `"customer support ticketing"`
searches. Not investigated (channel A's territory). Star counts 2026-08-02:

| stars | repo | licence (API) | self-description |
|---:|---|---|---|
| 360 | gtmagents/gtm-agents | apache-2.0 | "GTM agents and specialized skills for claude…" |
| 316 | zapier/gtm-cheat-codes | mit | "field guide for go to market teams using coding agents. Installable skills" |
| 132 | w95/awesome-claude-corporate-skills | mit | "166 production-ready Claude AI skills organized by corporate role" |
| 58 | t0ddc3by/claude-for-customer-success | other | "Claude Cowork/Code plugin for Customer Success" |
| 33 | LeadMagic/gtm-skills | mit | "205 production GTM agent skills for Claude Code" |
| 18 | etrebels/claude-code-growth-os | mit | "Sales, Marketing, Product and Retention" |
| 11 | citizenjosh/customer-success-skills | other | "open-source skills library for Agentic Customer Success Operations" |
| 9 | alphaparkinc/genpark-customer-support-ticket-sentiment-router-skill | NONE | ticket sentiment/priority router |
| 9 | alphaparkinc/genpark-agentic-customer-onboarding-skill | NONE | onboarding skill |
| 9 | alphaparkinc/genpark-commerce-dispute-resolution-skill | NONE | dispute resolution |
| 5 | quivly/skills | mit | "Customer Engineering, Post-Sales, and Customer Success" |
| 4 | Adri3l-R3nan/cognify-skills | other | "19 business operation skills" |
| 3 | stephenrogan/augmented-csm | mit | "38 agent skills for the complete CSM operational surface area" |
| 2 | varshatulsani032/AI-Customer-Success-Playbook | mit | CS prompts/workflows/templates |
| 1 | harybudiarto-create/ai-customer-success-toolkit | mit | CS workflows incl. onboarding |
| 1 | LukeJMadden/Veltrix-skills | mit | 16 business-ops skills |

**Signal for A:** the CS-specific agent-skill layer tops out around **58★**
(`t0ddc3by/claude-for-customer-success`); everything above that is GTM/sales-adjacent
(`gtm-agents` 360, `gtm-cheat-codes` 316) or a generic corporate-skills bundle (132). Several are
days old and duplicate each other's scope ("38 skills", "205 skills", "166 skills"). Consistent with
§1: **no CS incumbent.**

---

## 8. Licence verdict table (lead slice)

| repo | stars | API field | LICENSE file (opened) | manifest | verdict |
|---|---:|---|---|---|---|
| emcie-co/parlant | 18225 | Apache-2.0 | Apache-2.0 verbatim | pyproject `license = "Apache-2.0"` ✅ agrees | **LIFTABLE** |
| formbricks/formbricks | 12703 | **NOASSERTION** | AGPLv3 + MIT for `packages/js,android,ios,api` + **commercial EE** for `apps/web/modules/ee` | package.json: **no license field** | **AMBIGUOUS** (per-directory; the SDK packages are MIT) |
| getfider/fider | 4445 | AGPL-3.0 | AGPLv3, no carve-out | package.json: no license field | **CITE-ONLY** |
| dittofeed/dittofeed | 2881 | MIT | MIT verbatim | package.json `"license": "MIT"` ✅ | **LIFTABLE** — but last push 2026-03-28 |
| laudspeaker/laudspeaker | 2615 | **NOASSERTION** | **MIT header over an AGPLv3 body** + `packages/server/src/ee/` EE | — | **AMBIGUOUS** (self-contradicting) |
| astuto/astuto | 2352 | AGPL-3.0 | AGPLv3 | — | **CITE-ONLY + ARCHIVED** (`archived:true`, push 2026-01-09) |
| usertour/usertour | 2132 | **NOASSERTION** | MIT-Expat **except** `enterprise`/`ee` dirs **and any code controlling feature/permission/role/plan enablement** → `LICENSE.enterprise` (commercial) | package.json **`"license": "MIT"`** ❌ contradicts | **AMBIGUOUS** |
| logchimp/logchimp | 1112 | **NOASSERTION** | AGPLv3 + `packages/server/ee`, `packages/theme/src/ee` under EE | — | **AMBIGUOUS** |
| clearflask/clearflask | 446 | Apache-2.0 | `COPYING`, Apache-2.0 verbatim | — | **LIFTABLE** |
| churnkey/sdk | 20 | MIT | MIT verbatim, © 2026 Churnkey Inc. | — | **LIFTABLE** (vendor OSS w/ hosted upsell) |
| keon/awesome-customer-success | 24 | CC0-1.0 | CC0 1.0 verbatim | — | **LIFTABLE but valueless** (vendor directory) |
| mutedblues/Customer-Success-Management | 39 | NONE | **no licence file exists** | — | **CITE-ONLY** (+ dead since 2020-01-24) |

**Pattern worth naming for the pack:** the modern customer-facing SaaS tier (formbricks, usertour,
logchimp, laudspeaker) has converged on **open-core with an `ee/` carve-out**, which the GitHub API
reports as `NOASSERTION` — 4 of 12 repos in this slice. The API told us nothing useful in every one
of those cases, and in `usertour`'s case the package manifest actively contradicted the LICENSE file.
Charter rule 3(a)+(b) earned its place again.

---

## 8b. What real vendor CS teams publish — and a health score whose arithmetic we can read

Three repos are published *by a named vendor's Customer Success team*. Two are archived, and their
content turns out not to be CS methodology at all.

| repo | stars | licence (LICENSE file opened) | state | what it actually contains |
|---|---:|---|---|---|
| prefect-archive/prefect-recipes | 260 | Apache-2.0 | **archived**, last push 2025-01-01 | `flows-starter/`, `flows-advanced/`, `configuration/`, `devops/` — **Prefect usage recipes**. "Customer Success patterns" means *product* patterns. |
| puppetlabs/best-practices | 119 | Apache-2.0 | **archived**, last push 2023-09-07 | `puppet-module-design.md`, `scaling-puppet-enterprise.md`, `control-repo-contents.md`, … — **Puppet configuration best practice**. Also ships `best-practice-template.md` (a doc template) and `data-escalation-path.md`. |
| dynatrace-oss/CustomerSuccess | 35 | Apache-2.0 | **alive**, push 2026-07-02 | Actual CS artifacts: `Dynatrace Tenant Review/`, `Platform Adoption/`, `Software Obsolescence Management/` |

**Finding:** what a dev-tools CS team ships publicly is overwhelmingly **product best-practice
documentation** — enablement content, not customer-success process. That is itself a useful datum
for the pack's honest framing of the job ("education and enablement" is the visible output; the
methodology stays internal). Both non-Dynatrace examples are also dead, so cite them as evidence of
the pattern, not as live practice.

### 8b.1 The Dynatrace Platform Adoption dashboard — the adoption-measurement taxonomy

`dynatrace-oss/CustomerSuccess@HEAD:Platform Adoption/Dynatrace Platform Adoption v1.4.0.json` —
Apache-2.0, **LIFTABLE**. 59 tiles. README carries an honesty note: *"The content of this repo is not
officially supported by Dynatrace!"*

Tile titles give a real CS team's adoption metric set (verbatim):

- **Engagement**: `Daily Active Users`, `Active Users (Unique)`, `Returning Users (2+ days active)`,
  `Weekly Returners (2+ weeks active)`, `Stickiness (DAU/MAU)`, `userSession Depth (Avg userActions/userSession)`, `Weekly Growth`, `Week-over-Week Comparison`
- **Risk**: `Dormant Users (Inactive last 14d+)`, `User Lifecycle Cohorts`, `Lifecycle Cohorts - At Risk & Churned`
- **Breadth**: `Platform Breadth`, `Platform Capability Usage`, `Feature Usage Map`, `App Ranking`, `App Usage Trend`, `Users per App (Trend)`, `Domain Coverage`
- **Migration**: `Gen3 Adoption Rate`, `Gen3 Adoption Breakdown`, `Classic-Only Users (Migration Backlog)`, `Legacy Feature Usage`, `Platform vs Classic API Migration`
- **People**: `Top 20 Power Users`, `User Engagement Scorecard`
- **Automation**: `Human vs Automation`, `Workflow Health`, `Workflow Execution Trend`
- **Score**: `Maturity Score`, `Maturity Score - Gaps & Actions`

`Stickiness (DAU/MAU)` is computed correctly as mean-DAU/MAU:
`summarize activeDays = countDistinct(day), by:{userEmail} | summarize stickiness = round(100.0 * avg(toDouble(activeDays)) / 30.0, decimals:1)`
(averaging per-user active-days over a 30-day window is algebraically mean DAU ÷ MAU).

### 8b.2 The Maturity Score — a primary-source exhibit for the health-score flagship

**This is the best evidence channel C found for charter wedge hypothesis 2**, because unlike a vendor
blog it is the actual arithmetic, under Apache-2.0, from a large observability vendor's CS team.

`dynatrace-oss/CustomerSuccess@HEAD:Platform Adoption/Dynatrace Platform Adoption v1.4.0.json`,
tile `Maturity Score`, verbatim DQL:

```
| summarize uniqueUsers = countDistinct(if(`request.source` == "BROWSER", `user.id`, else:null)),
            totalApps  = countDistinct(`dt.app.id`),
            apiCalls   = countIf(`request.source` == "OTHER"),
            aiCalls    = countIf(contains(toString(resource), "/davis/"))
| fieldsAdd userPts = if(uniqueUsers >= 10, then:25, else:uniqueUsers * 2 + 5)
| fieldsAdd appPts  = if(totalApps  >= 5,   then:25, else:totalApps * 5)
| fieldsAdd apiPts  = if(apiCalls   > 100,  then:25, else:if(apiCalls > 0, then:15, else:0))
| fieldsAdd aiPts   = if(aiCalls    > 50,   then:25, else:if(aiCalls  > 0, then:12, else:0))
| fieldsAdd maturityScore = userPts + appPts + apiPts + aiPts
| fields maturityScore
```

Read what this is:

1. **Four equally-weighted components, 25 points each, summing to 100.** The equal weighting is
   asserted, not derived.
2. **Every threshold is a round hand-picked number** — 10 users, 5 apps, 100 API calls, 50 AI calls.
   The partial-credit ramps are arbitrary too (`uniqueUsers * 2 + 5`; why the `+5` floor, why `12`
   for nonzero AI usage and `15` for nonzero API usage).
3. **There is no outcome variable anywhere.** Nothing is fitted, calibrated, or validated against
   renewal, expansion, churn, or support load. It cannot be — no outcome is joined.
4. **Every component is something the vendor wants more of.** The companion tile
   `Maturity Score - Gaps & Actions` makes the intent explicit in its generated action strings:

   ```
   userAction = concat("Need ", toString(10 - uniqueUsers), " more users  - invite & run enablement sessions")
   appAction  = concat("Need ", toString(5 - totalApps),   " more apps  - drive Notebooks, Workflows, Problems")
   apiAction  = if(apiCalls==0, then:"No API usage detected  - set up tokens or MCP agents", else:"Increase to >100 API calls")
   aiAction   = if(aiCalls==0,  then:"No AI usage detected  - enable Davis Copilot and Analyzers", else:"Increase to >50 AI/Davis calls")
   ```

**Conclusion to carry into the flagship:** this is not a prediction, it is a **product-adoption
checklist rendered as a number** — and the things it rewards are the vendor's own expansion surface
(more seats, more modules, more API usage, more AI-feature usage). It is a perfectly reasonable
*enablement prompt* and a completely unvalidated *risk predictor*, and the failure mode is that the
100-point framing invites people to treat it as the latter.

**The honest reframe the pack can teach, sourced here:** the score's *paired* tile is what redeems
it. A score that always ships with "here is the specific gap and the specific action" is a
prioritisation device; the same number reported alone, on a dashboard, next to a renewal date, is
folklore. **Score + mandatory gap/action beats score alone** — and this repo demonstrates both halves.

### 8b.3 The at-risk definition is pure recency, at user level

Same file, tile `User Lifecycle Cohorts`:

```
| summarize firstSeen = min(timestamp), lastSeen = max(timestamp), by:{user.id}
| fieldsAdd cohort = if(daysSinceFirstSeen <= 7,  then:"1-New",
                   else:if(daysSinceLastSeen <= 3,  then:"2-Active",
                   else:if(daysSinceLastSeen <= 14, then:"3-At Risk",
                   else:"4-Churned")))
```

and tile `Dormant Users (Inactive last 14d+)`: `| filter lastSeen < now()-14d`.

**"At risk" = "hasn't logged in for 3–14 days". "Churned" = "hasn't logged in for 14+ days."**
No revenue, no contract, no support history, no seat count. Two caveats the pack should state:

- These are **user**-level cohorts. A churned *user* is not a churned *account* — see §3.1 on the
  account/user duality. Rolling this up naively mislabels healthy accounts with rotating staff.
- The thresholds (3d / 14d) are unexplained and product-specific. An observability console has a
  very different natural login cadence than a monthly-invoicing tool. **A recency threshold copied
  across products is the most common way a health signal becomes noise** — and this file is the
  concrete artifact to point at when teaching that.

---

## 8c. Grep-verified absences (CS-ops tooling)

Searches run 2026-08-02, dumps in `_scan-gh-7.json`. These are **absence findings** and the commands
are recorded so they can be re-run.

### `gh search repos "quarterly business review" --limit 20 --sort stars`
Top result: **1 star** (`sasrath/buzzwordAI`, a joke repo). Every other result is 0 stars — student
coursework, Tableau dashboards, or 2026-vintage LLM slide generators (`aparajithn/qbr-deck-automator`,
`swsounds42/qbr-deck-mcp`, `garyhe231/QBRAgent`, `NebulaLumino/ai-quarterly-business-review`).
**There is no QBR tooling on GitHub.** The nearest real artifact is Dynatrace's `Tenant Review`
dashboard (§8b) — i.e. a QBR at a mature vendor is a *product-telemetry review*, not a deck generator.

### `gh search repos "customer playbook automation" --limit 20 --sort stars`
**Zero results.** "Playbooks-as-code" for customer success does not exist as open source. (Contrast
with the runbook/incident space, which is dense.)

### `gh search repos "escalation policy" --limit 20 --sort stars`
Top result 32 stars (`lyft/opsreview`, MIT — a PagerDuty alert report). **Every single result on the
first page is on-call/incident escalation** — PagerDuty, VictorOps, GoAlert, Terraform providers for
escalation policies. Not one is *support* escalation.

**This matters for the seam.** The phrase "escalation policy" is, in open source, owned entirely by
the **operate/SRE** meaning (who gets paged, in what order, after how long). The success meaning
(when does a ticket leave tier 1, when does a bot hand to a human, when does an account go to a
named owner) has **no code representation at all** — except inside helpdesk automation engines
(worker 1's slice) and inside Parlant's guideline/journey model (§5). Recommend the pack name this
collision explicitly rather than inheriting SRE vocabulary by accident.

### `gh search repos --topic voice-of-customer --limit 15 --sort stars`
Top result **216 stars** (`joeseesun/qiaomu-app-review-insights`, MIT — *"Turn App Store reviews into
product research evidence"*), then a cliff to 32, 21, and a long tail of 1–2 star repos. Nearly every
entry was created or last touched in **2026** and is LLM/agent-shaped (`voc-mcp`, `CustomerMind`,
`insightloop`, `voice-of-customer-agent`).

**Reading:** VoC as a *tooling* category on GitHub is a few months old and entirely AI-native. There
is no established open-source VoC stack to inherit from — which is consistent with §1 and means the
pack is describing practice, not wrapping tools.

**Seam flag (marketing ↔ success):** `joeseesun/qiaomu-app-review-insights` (216★, MIT) turns app-store
reviews into product evidence. Per the charter, marketing keeps the ASO *listing* while app-review
*responses* are a support workflow owned by success. Review **mining for product evidence** is a third
thing again and probably belongs to success's VoC job feeding product. Recording, not assigning.
Also `vladharl/crumb` (1★, AGPL-3.0) — *"ties every feature request to revenue"* — the right idea
(feedback weighted by account value) at negligible maturity.

---

## 8d. A self-contained exhibit of the churn-accuracy trap (lead cross-check into worker 2's slice)

Found while sweeping `topic:churn-prediction`; **worker 2's brief did not name this repo**, so it is
recorded here. It is the cleanest teaching exhibit channel C found, because the repo ships the
dataset that refutes its own headline.

`ReverendBayes/Telecom-Churn-Predictor` — 6★, **MIT** (LICENSE file opened, verbatim MIT), last push
2025-08-21. Tree includes `churn-in-telecom-dataset.csv`, `churn_model/train.py`, `churn_model/predict.py`,
and four `.joblib` artifacts.

`ReverendBayes/Telecom-Churn-Predictor@HEAD:README.md` headlines, verbatim:

> **94.60% Accuracy | 0.8968 AUC | 0.8675 Precision | 0.7423 Recall**
> Evaluation done on 80/20 stratified train/test split. Base learners trained using k-fold CV. Meta-learner trained on out-of-fold predictions.

**The check.** I downloaded the repo's own shipped CSV
(`ReverendBayes/Telecom-Churn-Predictor@HEAD:churn-in-telecom-dataset.csv`) and counted the label column:

```
rows: 3333
Counter({'False': 2850, 'True': 483})     →  churn base rate 14.49%
majority-class baseline accuracy = 2850/3333 = 85.51%
```

**A model that predicts "nobody churns" scores 85.51% on this dataset.** The advertised 94.60%
is **+9.09 percentage points over doing nothing**. The metric that actually matters to a retention
team — recall 0.7423, i.e. **the model misses 25.8% of the customers who churn** — is listed fourth,
after the number that is 85% floor.

The methodology itself is not dishonest (stratified split, out-of-fold meta-learner, AUC reported).
**The dishonesty is the headline ordering**, and that is the pattern the pack should teach: *an
accuracy figure for churn is uninterpretable without the base rate, and any vendor or model card
quoting accuracy without it is either careless or selling.*

Two further notes:

1. **This is a second monoculture dataset, not the IBM Telco one.** 3,333 rows / 14.49% churn
   ("Churn in Telecom's dataset", the `churn-bigml` lineage), distinct from the IBM Telco Customer
   Churn set (7,043 rows, ~26.5% churn) that worker 2 was asked to count. Worker 2's monoculture
   tally should treat these as two separate canonical datasets.
2. **A never-ship figure class, spotted in the wild.** The same README states:
   > *"For context, Charter Communications, the telecom company this was built for, was previously relying on a spaCy-based model that achieved only ~40% accuracy."*

   An unverifiable third-party claim about a named public company, and internally implausible on its
   face — 40% accuracy is far *below* the 85.51% you get by predicting nothing, and below a coin
   flip. Per charter rule ("flag the figure-CLASS, not just known strings"), the class is:
   **"our model beats the old one" comparisons where the old one's number is unsourced and
   nonsensical.** Never repeat; useful only as an example of the genre.

**Also flagged for worker 2** (both outrank most of what worker 2's brief named, in
`topic:churn-prediction --sort stars`):
- `ragulpr/wtte-rnn` — **774★, MIT**, "WTTE-RNN a framework for churn and time to event prediction".
  The **most-starred churn-prediction repo on GitHub**, and it is a *survival / time-to-event*
  framing (Weibull), not a classifier. Strong corroboration for the censoring argument.
- `jdmaturen/shifted_beta_geometric_py` — 62★, Apache-2.0, *"An implementation of the
  shifted-beta-geometric (sBG) model from Fader and Hardie"*. sBG is the **contractual**-setting
  churn model, the direct counterpart to BTYD's non-contractual assumption — exactly the
  contractual-vs-non-contractual distinction worker 2 was asked to source. Charter clause (e)
  applies: the Apache licence covers the code, **not** Fader & Hardie's model — cite the authors.
- `derrynknife/SurPyval` — 53★, MIT, survival analysis package (worker 2's §B list did not include it).

---

## 8e. Cross-flag verification (added 2026-08-02, after the channel report was first written)

Two controller cross-flags verified by the lead. **Full write-up with quotes is in
`../github-report.md` §7b** — sourced facts recorded here so nothing is lost if the report is rewritten.

### Channel B's claim: Anthropic published a public RAG support-agent reference — CONFIRMED, name stale

- **RENAME**: `gh api repos/anthropics/anthropic-quickstarts --jq .full_name` resolves to
  **`anthropics/claude-quickstarts`** (17,356★). The old name still redirects, so a stale citation
  looks alive. Cite the new name.
- **Licence LIFTABLE**: `anthropics/claude-quickstarts@main:LICENSE` opened — plain MIT,
  `Copyright (c) 2023 Anthropic`. Tree grep of `^customer-support-agent/` for `licen` returns nothing
  (only `README.md`, `package.json`) → **no per-directory carve-out**.
- **RAG is via a managed service, not shipped**: `customer-support-agent/README.md` —
  *"leveraging **Amazon Bedrock Knowledge Bases** for knowledge retrieval."* No vector store, no
  ingestion, no chunking in-repo; needs an AWS account. A UI-and-prompt reference, not a retrieval one.
- **Escalation as a typed output contract** — `customer-support-agent/app/api/chat/route.ts:26-41`:
  ```ts
  user_mood: z.enum(["positive","neutral","negative","curious","frustrated","confused"])
  redirect_to_agent: z.object({ should_redirect: z.boolean(), reason: z.string() })
  ```
  Three symbolic triggers stated in the system prompt (same file, lines 140/144/146): no relevant
  information available; question out of scope of products/services; user explicitly asks for a human.
- **Precision caveat — do not overclaim**: `user_mood` is *recorded alongside* the decision, **never
  stated as a trigger**. The worked example pairs `"frustrated"` with `should_redirect: true`, but no
  rule causes it. This is sentiment tracked as an observed dimension with a **scope-based** escalation
  rule — a better design than sentiment-triggers-handoff. Never write "Anthropic escalates on frustration."
- **First-party support taxonomy, MIT**: `customer-support-agent/app/lib/customer_support_categories.json`
  — 8 categories with keyword sets: `account`, `billing`, `feature`, **`internal`** (auto-reply,
  forward, ignore, spam, other, *sales reroute*), `legal`, `other` (job inquiry, 3rd party company),
  `technical`, `usage`. The `internal`/`other` rows reserve buckets for **traffic that should leave
  the support queue entirely** — an axis absent from every helpdesk schema in worker 1's slice.

### Channel A's flag: `t0ddc3by/claude-for-customer-success` architecture (content is A's, not mine)

58★, API **NOASSERTION** (A resolved it: Apache-2.0 © SuccessCOACHING — **DO NOT LIFT**, A's ruling
stands), last push **2026-05-29**. Architecture only, from a recursive tree listing:
`managed-agent-cookbooks/<motion>/{agent.yaml, steering-examples.json, subagents/*.{md,yaml}}` with
motions incl. `adoption-motion` (subagents `adoption-gap-identifier`, `motion-planner`,
`product-surface-analyzer`) and `advocacy`; `deployment-cookbooks/solo-csm-cookbook.md`;
`docs/agent-capability-model/claude-for-cs-agent-capability-model.yaml`; per-surface `.mcp.json`
(`cs-ops/`, `csm/`); an AUQ hook layer (`auq-resilience/hooks/{auq_hook.py,auq_parser.py,hooks.json}`,
`run_auq_hook.sh`). Only artifact in the corpus decomposing CS work into **named motions with typed
subagents** — same instinct as Parlant's journeys (§5), expressed as config not runtime.
**`solo-csm-cookbook.md` flagged to A** (charter §1033 solo conditional); not opened — A's lane.

---

## 9. Open questions / seam flags from this slice

1. **Cancel-flow ownership (growth ↔ success).** See §6. Recommend: success owns the flow, the reason
   taxonomy and the exit-interview capture; growth owns whether a given offer *works*.
2. **Parlant sits on the ai ↔ success seam.** Mechanics (context assembly, ARQs, model choice) → ai.
   Guidelines/journeys/canned-responses/strict-mode-boundaries as *policy artifacts* → success.
   Worth an explicit handoff line since it is the largest repo either pack would claim.
3. **Feedback boards straddle success ↔ product.** Fider's status taxonomy is a *product* roadmap
   communication device operated by *success*. The `PostResponse` + `declined`/`duplicate` states are
   the closing-the-loop artifact — probably success's, since it is the customer-facing reply.
4. **Formbricks' Display/Response split should become a pack invariant-in-spirit**: never state a
   satisfaction metric without stating its denominator and its self-selection. Sourced to schema, not folklore.
5. **`topic:churn`/`topic:retention` being squatted** is worth one sentence in the pack's honest
   framing of the domain's maturity — but check with channel D whether the academic literature is
   equally thin before over-claiming.
