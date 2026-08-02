# _raw-skills-lead-breadth — Channel A / lead slice

Author: channel-A lead. Date: 2026-08-02.
Scope: territory nobody was assigned — (1) an exhaustive registry inventory via the skills.sh JSON API
(the CLI truncates to 6 results, the API does not), (2) the three BREADTH repos that inventory surfaced
and that no worker was tasked with: `t0ddc3by/claude-for-customer-success`, `sylphxai/skills`,
`composio-community/support-skills`.

Companion files: `_raw-skills-incumbent.md` (A1), `_raw-skills-cs-packs.md` (A2),
`_raw-skills-registries.md` (A3). Nothing here contradicts those.

---

## 1. Method: the skills.sh JSON API beats the CLI

`npx skills find <q>` prints only the top 6 hits. The site exposes an undocumented JSON endpoint that
returns up to 100:

```
curl -s --get --data-urlencode "q=customer success" https://skills.sh/api/search \
  -H 'User-Agent: Mozilla/5.0 ... Chrome/131.0.0.0 Safari/537.36'
```

Response shape: `{"query":..., "searchType":"semantic", "skills":[{"id","skillId","name","installs","source"},...]}`.
**Rate limit is 30 requests/minute**, enforced with
`{"error":"rate_limit_exceeded","message":"Rate limit exceeded. Maximum 30 requests per minute. For higher
limits, use the official API at /api/v1/ with an API key."}` — a silent-zero failure mode if you don't
check the payload (my first sweep returned "0 results" for 30 terms and they were all rate-limit errors,
not empty result sets). Space requests ~2.6s apart.

Swept 35 CS-domain terms. Aggregated + deduped by `.id`:

- **2,747 unique skills** returned across all queries → `_data-skillssh-all-2747.tsv`
- **1,318** whose id matches a CS-domain keyword regex → `_data-skillssh-cs-candidates.tsv`
  (regex: customer|churn|retention|onboard|support|helpdesk|success|renewal|nps|csat|advocacy|upsell|
  expansion|voice-of|knowledge-base|ticket|escalat|adoption|winback|cancel|deflect|faq|help-center|
  documentation|csm|account-health|health-score|survey|feedback|community|education|enablement|
  service-desk|sla|qbr)

Both TSVs are `installs<TAB>owner/repo/skill`, sorted by installs desc.

**Caveat on the search itself**: `searchType` is `semantic`, and it is lossy. It never returned
`coreyhaines31/marketingskills/onboarding` for any of the 35 terms even though the CLI returns it for
`onboarding` at 40.2K installs. Treat the aggregate as a wide net for DISCOVERY, never as a complete
census, and never as an authority on install magnitudes.

### The install-count distribution (the shape of the whole answer)

Top of `_data-skillssh-cs-candidates.tsv`:

```
84202	coreyhaines31/marketingskills/churn-prevention
54224	pbakaus/impeccable/onboard
24340	googleworkspace/cli/persona-customer-support
 9115	github/awesome-copilot/add-educational-comments
 4346	affaan-m/everything-claude-code/customer-billing-ops
 3738	claude-office-skills/skills/customer-success
 2447	anthropics/knowledge-work-plugins/audit-support
 2409	eronred/aso-skills/retention-optimization
 2322	anthropics/knowledge-work-plugins/ticket-triage
 2198	anthropics/knowledge-work-plugins/customer-escalation
 2132	anthropics/knowledge-work-plugins/onboarding
```

then a long flat tail: by rank ~40 the counts are under 400, and every purpose-built CS pack in the
ecosystem (see §2) sits between 1 and 200 installs.

### Repos ranked by BREADTH (count of CS-matching skills), not by installs

This is the ranking that found what install-count ranking hides:

```
30  t0ddc3by/claude-for-customer-success
22  sylphxai/skills
12  mohitagw15856/pm-claude-skills
12  leadmagic/gtm-skills
12  gtmagents/gtm-agents            (A2 covered)
12  eddiebelaval/squire
 9  membranedev/application-skills
 9  guia-matthieu/clawfu-skills     (A2 covered)
 8  composio-community/support-skills
 7  absolutelyskilled/absolutelyskilled
 6  ncklrs/startup-os-skills        (A2 covered)
 6  onewave-ai/claude-skills        (A2 covered)
```

The #1 breadth repo has 1–3 installs per skill. Nobody had looked at it.

---

## 2. t0ddc3by/claude-for-customer-success — the real architectural incumbent

Source: https://github.com/t0ddc3by/claude-for-customer-success
Clone: `git clone --depth 1` → `/tmp/lead-a/cfcs`, HEAD `b7c22f6556b31ce78cae8a052b4963933a733466`
(2026-05-29 13:14:57 -0700, commit subject: `chore(dist): remove stale auq-resilience-v1.0.1.plugin; fix QUICKSTART versions`).

`gh api repos/t0ddc3by/claude-for-customer-success`: **58 stars**, `archived: false`,
`created_at 2026-05-15`, `pushed_at 2026-05-29T20:15:30Z`, `license.spdx_id: "NOASSERTION"`.

### 2a. LICENSE — the GitHub API lies again (charter rule 3a, 8th+ instance)

API says `NOASSERTION`. The LICENSE file itself, opened directly, is:

> ```
> Copyright 2026 SuccessCOACHING
>
>                                  Apache License
>                            Version 2.0, January 2004
> ```

So: **Apache-2.0, copyright SuccessCOACHING** — a real commercial CS training/certification company,
not an individual.

### 2b. Thin-license-on-thick-IP — the clearest instance we have hit (charter rule 3e)

`README.md:15`:
> "Methodology-opinionated (SuccessCOACHING Customer Success methodologies and frameworks), tool-agnostic."

`README.md:90`:
> "This suite is built on **SuccessCOACHING** Customer Success Management methodologies because those
> methodologies are what makes the domain knowledge operational. The **TARO Playbook** frame..."

`README.md:100`: names the **"CSMBOK Knowledge Graph"** — "maps the body of knowledge for Customer
Success as a discipline."

`README.md:332`:
> "**TARO plays are leads, not mandates.** The CSM reads the play, validates the trigger, and owns the
> decision to run it. The agent does not run plays autonomously."

**Disposition: DO NOT LIFT.** The Apache-2.0 grant covers this repo's files. It does not license
SuccessCOACHING's TARO Playbook or CSMBOK body-of-knowledge, which are the substance. Anything we take
would have to be independently derived and attributed to SuccessCOACHING by name. Their own
`company-profile.md:85` treats the methodology as a pluggable proprietary choice:
`**Methodology:** [PLACEHOLDER — SuccessCOACHING TARO / custom playbook / both / none formally]`.

### 2c. Scale and architecture

660 files. README badges: `plugins-6`, `skills-81`. Verified by count: 81 `SKILL.md` files,
**28,988 total lines**. Six independently-installable plugins, pre-built `.plugin` bundles in `dist/`:

| Plugin | Skills (counted from disk) | Audience per `README.md:39-44` |
|---|---|---|
| `csm/` | 17 | "Customer Success Managers on daily account work" |
| `renewals/` | 12 | "Renewals managers and AMs owning GRR/NRR" |
| `rev-ops/` | 34 | "CS revenue operations — the infrastructure CS needs to report and forecast like a revenue center" |
| `cs-ops/` | 9 | "CS Operations handling portfolio analytics and systems" |
| `onboarding/` | ~9 | "Onboarding teams and implementation managers" |
| `auq-resilience/` | 0 (one command) | Infra: fallback when `AskUserQuestion` fails to render |

Supporting architecture, all present on disk: `shared/cs-domain-model.md`,
`shared/cross-skill-registry.md`, `shared/revops-domain-model.md`, `shared/which-tenant-am-i-on.md`,
`handoff/CLAUDE.md`, `deployment-cookbooks/`, `managed-agent-cookbooks/`, `docs/`, and a `scripts/`
directory containing `lint-skill-body.py`, `validate-cross-links.py`, `check-config-completeness.py`,
`generate-eval-fixtures.py`, `review-sweep.sh`.

This is a more elaborate build than anything else channel A found, and structurally the nearest
neighbour to our own family shape (thin front door + on-demand references + cross-pack seams + evals).

### 2d. It self-describes as a reference build, not a product

`README.md:13`:
> "A reference implementation showing what AI-native Customer Success looks like when built on deep
> domain knowledge — not a deployment-ready product, but a working demonstration of what's possible and
> what a minimum viable architecture requires."

Individual skills carry a literal `[PROPOSED]` status marker in the body
(e.g. `cs-ops/skills/health-model-review/SKILL.md:22`).

### 2e. THE EVIDENCE FINDING — grep-verified emptiness

```
$ grep -rhoE 'https?://[^ )>"]+' --include=SKILL.md .
(no output)
```

**81 skills, 28,988 lines, ZERO external URLs.** Citation-marker counts across the same corpus
(files matching, case-insensitive):

| marker | files |
|---|---|
| `et al` | 1 — and it is a false positive: `onboarding/skills/handoff-doc/SKILL.md:113` contains the substring in "…has **met al**l graduation criteria…" |
| `Reichheld` | 0 |
| `Harvard Business Review` | 0 |
| `\bHBR\b` | 0 |
| `doi\.` | 0 |
| `arxiv` | 0 |
| `according to research` | 0 |
| `study (found\|shows\|of)` | 0 |
| `peer-review` | 0 |
| `meta-analys` | 0 |
| `Gainsight` | 8 |
| `SuccessCOACHING` | 12 |
| `benchmark` | 12 |

Repo-wide (`*.md`, not just skills), the only external hosts are product/infra URLs —
`pivot.claude.ai` (10), `graph.microsoft.com` (9), `img.shields.io` (7), `github.com` (6),
`login.microsoftonline.com` (4), `learn.microsoft.com` (3), `claude.com` (3), `successhacker.co` (2,
SuccessCOACHING's own domain), `semver.org`/`keepachangelog.com` (2 each), plus placeholder hosts
(`yourbucket.s3.amazonaws.com`, `internal.yourcompany.com`). **No research citation anywhere in the repo.**

So: the most architecturally serious CS pack in the ecosystem cites nothing. Its entire authority is
"SuccessCOACHING says so."

### 2f. It DOES teach judgment — and this partially occupies our flagship

This is the finding that most constrains wedge hypothesis 2, so it is quoted at length.

`cs-ops/skills/health-model-review/SKILL.md` (388 lines). Frontmatter description:
> "Audit the portfolio health model — distribution analysis, component weight validation, threshold
> calibration, signal freshness, and predictive accuracy assessment."

Body, line 18:
> "Audit the health model at the portfolio level — does it actually predict churn, or does it just
> classify accounts?"

Reasoning-protocol constraints (verbatim):
> "- G1: Health scores are heuristics — calibration findings must not be framed as churn predictions.
>    Decompose into observable component signals.
>  - G2: Calibration assessment without historical churn data produces a description, not a verdict —
>    surface the data gap explicitly rather than speculating on predictive accuracy.
>  - G4: Coverage gaps vs. score problems require different corrective actions — never conflate missing
>    data with poor health."

And a CLASSIFY branch:
> "**Predictive Accuracy Audit**: Health classifications vs. actual renewal outcomes — do Red accounts
> churn more than Green? Requires historical data. Separate false positives (over-flagging) from false
> negatives (missing churners)."

The "G-code" guardrail pattern is systemic, not a one-off: **68 of 81** SKILL.md files contain a
`G1:`–`G9:` guardrail line, and **64 of 81** carry an explicit `## Do NOT use for` section.

Compare to `csm/skills/account-research/SKILL.md:336`, which teaches signal-not-prediction framing at
the account level:
> will churn." Frame as specific signals observed: "usage is down 18% week-over-week,

**Honest reading**: this is real epistemic hygiene about health scores, asserted well, and it is
*upstream of* the flagship we hypothesised. What it is NOT: evidenced (§2e — zero citations, so
"health scores are heuristics" is an assertion of the same grade as the folklore it corrects), and
not applicable outside an enterprise CS org (§2g).

### 2g. Its "solo" is not our solo

`deployment-cookbooks/solo-csm-cookbook.md` is 3,163 lines and status `[PROPOSED]`. It is the only
solo-framed CS content of any depth found in the ecosystem — but the audience line is:

> "**Audience:** Individual CSMs deploying the claude-for-customer-success plugin suite for solo use"

and:

> "This cookbook is written for a **single CSM deploying the plugin suite for personal use** — not an
> enterprise IT rollout, not a team administrator provisioning for multiple users."

> "This cookbook does not cover team or enterprise deployment — multi-user provisioning, shared
> connector configurations, admin-level permission management, or rollout coordination across a CS
> team. If you're deploying this suite for a team, contact SuccessCOACHING for enterprise deployment
> guidance."

So "solo" here means *one CSM inside a company that has CSMs*, still assuming a book of accounts, a
CRM, a CS platform, ARR tiers, renewals, and quota. It is a single-seat deployment guide, not a
small-company methodology. It also concedes the whole thing needs tailoring before it works:

> "**Every deployment requires tailoring before it produces useful output.**"
> "the Provisional Outcome Catalog is generated from public product information and must be reviewed
> and validated against your actual customer outcomes before agents use it"

**This leaves the charter's §1033 reader — the solo self-serve builder with no CSM, no ARR tier model,
often no renewal event — entirely unaddressed.** Confirms wedge hypothesis 1 rather than threatening it.

### 2h. COVERAGE GREP — what 81 CS skills never touch

Files matching each concept, out of 81:

| concept (regex) | files |
|---|---|
| `knowledge base\|help cent\|help doc\|article` | **0** |
| `deflect` | **0** |
| `AI (agent\|bot\|chatbot)\|chatbot` | **0** |
| `community\|forum` | 1 |
| `support (process\|taxonom\|queue\|tier)` | 1 |
| `self-serve\|self-service\|PLG\|product-led` | 7 |
| `voice of customer\|VoC` | 9 |
| `education\|enablement\|training\|academy\|tutorial` | 11 |
| `CSAT\|NPS` | 18 |
| `ticket\|helpdesk\|service desk\|inbox\|macro` | 25 |
| `SLA\|first response` | 63 |

The two large counts are misleading and I checked every class of hit:

- **`ticket` (25 files) is support-as-INPUT, never support-as-DESIGN.** Every hit is a CSM reading
  ticket state as an account signal. Verbatim:
  `csm/skills/risk-flag/SKILL.md:174`: `| Open escalation or unresolved P1 ticket | [Yes/No] | [ticket details] | High |`
  `csm/skills/account-research/SKILL.md:315-318`: `**Support ticket summary**` / `- Open: [N] tickets — [P1: N / P2: N / P3-P4: N]` / `- Oldest open ticket: [date]`
  `csm/skills/account-research/SKILL.md:205`: `> - Support: [open tickets, any P1/P2 escalations, ticket trend]`
  There is no skill that designs a queue, a taxonomy, a tiering model, a macro library, or a QA rubric.
- **`SLA` (63 files) is an internal escalation-routing placeholder, not a support SLA.** Verbatim:
  `csm/skills/risk-flag/SKILL.md:79`: `- **G4**: No escalation recommendation without a named contact, channel, and SLA from the configured matrix`
  `csm/skills/risk-flag/SKILL.md:220-222`: `| Condition | Route to | Via | SLA |` / `| [Matching scenario from matrix] | [configured contact] | [configured channel] | [configured SLA] |`
  `csm/skills/qbr-builder/SKILL.md:299`: `| Urgent issue | [Support channel] | [link] | [SLA from your contract] |`
  The SLA is always `[configured]` or `[from your contract]` — the pack never teaches how to SET one.

**Net**: 81 skills covering CSM account work, renewals, and CS rev-ops, with **zero** help-content/KB
strategy, **zero** deflection, **zero** AI-support-agent policy, and support present only as a signal
it consumes.

### 2i. Numbers it ships

Nearly all numerics in cfcs are config placeholders or illustrative example values, not asserted
benchmarks — which is more disciplined than the packs A2 surveyed. Examples of the illustrative class:
`csm/skills/health-score-review/SKILL.md:186` ("users dropped 22% over 30 days, which puts this below
the configured Yellow…"), `renewals/skills/renewal-forecast/SKILL.md:180` (`| **At risk** | Active churn
signals; escalation in progress or needed | 25% |`), `renewals/skills/cold-start-interview/SKILL.md:160`
(`Logo retention target: (e.g., 92%)`).

Two exceptions worth logging:

- `renewals/skills/churn-rca/SKILL.md:17` — a hardcoded escalation threshold with no derivation:
  > "**`cohort`** — multi-account pattern analysis; surfaces systemic drivers and generates
  > portfolio-level escalation when churn rate meets or exceeds 25%"
  (repeated at :44, :63, :232-233, :328). Why 25%? Never said.
- `rev-ops/skills/quota-sensitivity-analysis/SKILL.md:69-72` — names a real external benchmark source
  and then does not cite it:
  > "Is the planning rate (75%) declared as an assumption, not a universal benchmark? The 75th…"
  > "top-quartile performance" without naming the KBCM actuals median (55–65%) is unactionable
  "KBCM" = KeyBanc Capital Markets' annual SaaS survey. The pack asks the reader to name the KBCM
  median but never gives a citation, edition, or link for it. ~~**Falsification-strip candidate for
  channel D**: KBCM SaaS survey sales-quota-attainment median 55–65%; trace to the actual published
  report or kill.~~

  > **CORRECTION 2026-08-02 (author, after channel D verification).** The channel-D referral above is
  > **withdrawn.** D verified that KBCM's quota-attainment figure covers **sales/AE quota, not CSM
  > quota**, and that KBCM's recent editions run **~70→75%**, not 55–65%. So (a) the item is outside
  > success's domain — I should have caught that from the formula two lines below it in the same file,
  > `Revenue = ae_required × ae_quota × 0.75`, which is plainly about account executives; and (b) the
  > 55–65% is a **misattribution**, not an under-cited real figure. The observation that the pack
  > names a survey without citing it still stands and is still a good falsification exhibit — but it
  > is a *sales* exhibit, and **D should not spend budget tracing it**. Nothing else in §2i changes.
  > Mirrored at `skills-ecosystem-report.md` §4.3 and §6 item 7.

---

## 3. composio-community/support-skills — the support-side complement

Source: https://github.com/composio-community/support-skills
Clone HEAD `83382c4b055fc4e5b055044adb5bfb7585484c9a` (2026-04-21 23:48:53 +0530).
`gh api`: **14 stars**, `archived: false`, `license: null`, `pushed_at 2026-04-21` (dormant ~3.5 months).
Repo description: "Customer support skills for Claude Code and AI agents. Ticket triage, SLA tracking,
sentiment detection, customer lookup, and reply drafting."

**LICENSE: no LICENSE file at root** (verified by `ls -a`). Per charter rule 3d → **cite only, do not lift.**

38 skills, one flat directory each:
`angry-customer-playbook, auto-tag, bug-report, call-summary, chatbot-review, contact-sync,
csat-followup, customer-360, customer-winback, draft-reply, email-verify, escalate, feedback-digest,
freshdesk-triage, handoff-notes, inbox-zero, intercom-resolve, knowledge-search, lead-enrich,
macro-builder, merge-tickets, nps-collect, outreach-campaign, proposal-draft, qa-response,
refund-processor, response-templates, root-cause, sentiment-check, sla-monitor, support-metrics,
ticket-summarize, ticket-triage, tone-rewriter, translate-ticket, vip-alert, weekly-digest,
whatsapp-support, zendesk-triage, zoho-desk-triage`

**Depth: thin tool-drivers.** 2,612 lines across 38 files — mean 69 lines; the longest is
`sentiment-check/SKILL.md` at 96 lines. Every skill is a Composio-API driver, not methodology. The only
external URLs in the entire corpus are 59 links to `composio.dev` (its own toolkit docs).

Verbatim shape, `sla-monitor/SKILL.md:10`:
> "You are an SLA compliance monitor. Check all open [Gorgias](https://composio.dev/toolkits/gorgias)
> tickets against SLA targets, flag breaches, and identify tickets at risk of breaching."

**Falsification-strip candidates (unsourced numeric defaults presented as "these defaults"):**
- `sla-monitor/SKILL.md:18`: `**First Response Time:** 1 hour (P0), 4 hours (P1), 8 hours (P2), 24 hours (P3)`
- `sla-monitor/SKILL.md:19`: `**Resolution Time:** 4 hours (P0), 24 hours (P1), 48 hours (P2), 72 hours (P3)`
- `sla-monitor/SKILL.md:20`: `**Next Reply Time:** 2 hours after customer responds`
- `sla-monitor/SKILL.md:34`: `**AT RISK** - Over 75% of SLA target elapsed`
- `merge-tickets/SKILL.md:33`: `Same customer email + similar subject (>70% overlap)`
- `customer-winback/SKILL.md:20,23`: `Customers with 3+ tickets in the last 30 days` /
  `Customers with unresolved tickets older than 7 days`

These are exactly the "a disclaimed figure is still a figure" class — except they are not even
disclaimed. A P0 first-response SLA of 1 hour is a real operational commitment with staffing
consequences, shipped as a default with no derivation.

**Why it matters structurally**: cfcs (§2) covers CSM/renewals/rev-ops and no support desk;
composio-support covers the support desk and no CS. Nobody covers both — direct support for
wedge hypothesis 4.

---

## 4. sylphxai/skills — breadth that evaporates on inspection

Source: https://github.com/sylphxai/skills
Clone HEAD `73eb0962d394507a012dc6394e1304534a97d19d` (2026-08-02 12:49:24 +0000 — same-day).
`gh api`: **1 star**, MIT, `created_at 2026-07-18` (two weeks old), `archived: false`.
LICENSE opened directly: `MIT License / Copyright (c) 2026 SylphxAI` — consistent with the API.

skills.sh indexes **22** sylphxai CS skills (29–66 installs each): `customer-success-health-review`,
`support-quality-qa-review`, `help-center-architecture`, `support-deflection-knowledge-base-review`,
`in-product-education-review`, `customer-training-academy-review`, `enterprise-onboarding-implementation-review`,
`partner-support-enablement-review`, `support-automation-governance-review`, and 13 more — a naming set
that reads like a near-complete map of our canonical includes.

**At HEAD, 16 of those 22 do not exist.** The repo has 112 skill directories, of which **6** match
CS keywords: `customer-data-migration-review`, `customer-success-operations-review`,
`customer-support-case-resolution`, `customer-support-operations`, `product-feedback-learning-loop`,
`refund-and-support-flow-review`. The two I sized are 82 and 91 lines. External URLs across the CS
skills: 3 × `github.com`, 1 × `enact.sylphx.com` — no research citations.

Two takeaways:
1. **A registry listing is not a skill.** skills.sh install counts persist after the underlying skill is
   deleted or renamed (A1 found the same failure mode from the other direction — `onboarding-cro` and
   `onboarding` are the same skill double-counted under a rename). Never cite a skills.sh count as
   evidence a skill exists; clone and check HEAD.
2. This is a two-week-old, 1-star repo generating ~112 skills, several per day. The breadth is
   generative output, not accumulated practice.

---

## 5. Cross-cutting: nobody in the ecosystem cites anything

Consolidating the evidence greps across every corpus channel A read (mine + workers'):

| corpus | scale | external research citations |
|---|---|---|
| `t0ddc3by/claude-for-customer-success` | 81 skills / 28,988 lines | **0** (§2e) |
| `composio-community/support-skills` | 38 skills / 2,612 lines | **0** (only composio.dev ×59) |
| `sylphxai/skills` CS subset | 6 skills | **0** |
| `coreyhaines31/marketingskills` churn-prevention + onboarding | ~1,628 lines | **0** (A1 §1d, §1e — grep for `http\|source:\|study\|research\|according to` returned zero) |
| `anthropics/knowledge-work-plugins/customer-support` | 5 skills / 1,544 lines | **0** (A1 §3) |
| `guia-matthieu/clawfu-skills` CS cluster | 7 files | 0 links; 7 vendor-name-only `## References` lists (A2 §2) |

The single exception found anywhere in channel A is `wondelai/skills@improve-retention`, which
attributes the Fogg Behavior Model (B=MAP) to BJ Fogg by name and quote (A3, Job 2) — and that is a
psychology framework, not evidence about customer success.

**Emptiness is confirmed by grep, not asserted.** The judgment layer is not uniformly empty —
cfcs's G-codes are real judgment (§2f) — but the EVIDENCE layer is empty everywhere, including
underneath cfcs's judgment.

---

## 6. Artifacts

- `_data-skillssh-all-2747.tsv` — every unique skill returned by the 35-term API sweep, `installs<TAB>id`
- `_data-skillssh-cs-candidates.tsv` — the 1,318 CS-keyword-matching subset
- Clones (ephemeral): `/tmp/lead-a/{cfcs,sylphx,composio-support}`
