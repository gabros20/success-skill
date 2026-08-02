# Channel A · skills-ecosystem — report

Date: 2026-08-02 · Lead: channel-A sub-orchestrator · Workers: 3 × sonnet
Charter: `research/charter.md` · All claims trace to a `_raw` file below.

**Source files (every claim here is sourced in one of these):**
- [`_raw/_raw-skills-incumbent.md`](_raw/_raw-skills-incumbent.md) — A1: coreyhaines31/marketingskills deep-read, googleworkspace, anthropics/*, firecrawl false-positive verification
- [`_raw/_raw-skills-cs-packs.md`](_raw/_raw-skills-cs-packs.md) — A2: the 12 CS-dedicated small/mid packs, health-score weight census
- [`_raw/_raw-skills-registries.md`](_raw/_raw-skills-registries.md) — A3: skills.sh browse, awesome-lists, third-party directories, adjacent + vendor packs
- [`_raw/_raw-skills-lead-breadth.md`](_raw/_raw-skills-lead-breadth.md) — lead: exhaustive skills.sh API inventory + the three breadth repos nobody was assigned
- [`_raw/_data-skillssh-all-2747.tsv`](_raw/_data-skillssh-all-2747.tsv), [`_raw/_data-skillssh-cs-candidates.tsv`](_raw/_data-skillssh-cs-candidates.tsv) — the raw inventory
- [`_raw/skills-find-a3-raw.txt`](_raw/skills-find-a3-raw.txt) — A3's 18-term `npx skills find` sweep, raw

---

## 1. Verdict

**There is no incumbent of marketing's kind. The niche is OPEN — more open than marketing's was, and open in a different way than quality's was.**

Marketing faced one 42.5k★ pack that covered its territory well. Success faces **fragmentation**: the
canonical-includes list is split across three disjoint camps, none of which covers another's ground, and
**none of which cites a single piece of evidence.**

| Camp | Who | Covers | Never covers |
|---|---|---|---|
| **Reach** | `coreyhaines31/marketingskills` — churn-prevention 84.2K installs, onboarding ~94K combined | Cancel flows, dunning, activation checklists | Support, KB, health scores as a discipline, renewals, expansion, escalation |
| **Official/tactical** | `anthropics/knowledge-work-plugins/customer-support` — Apache-2.0, 23,246★ repo, pushed same-day | Ticket triage, escalation, response drafting, KB article authoring | Onboarding, health, VoC aggregation, renewals, expansion — zero |
| **Architectural** | `t0ddc3by/claude-for-customer-success` — 81 skills, 6 plugins, 58★, ~1 install each | CSM account work, renewals, CS rev-ops, portfolio health | Help content/KB (0 of 81 files), deflection (0), AI-support policy (0), support process design |

Three partial incumbents, zero overlap between them, and **nobody integrates**. Wedge hypothesis 4
(integration) is confirmed by the structure of the ecosystem itself, not just by absence.

**The strongest single finding: the evidence layer is empty everywhere, grep-verified.** Across
~35,000 lines of CS skill content from six independent corpora, the count of external research
citations is **zero**. Details in §4 — this is the quality-skill-shaped opening, and it is wider here
than it was there.

**Threat to flag honestly**: `t0ddc3by/claude-for-customer-success` already teaches the core judgment of
our flagship candidate ("does the health model actually predict churn, or does it just classify
accounts?"). It is unadopted, uncited, and enterprise-only — but it is not empty, and our flagship
framing must account for it rather than claim virgin territory. §3.3.

---

## 2. Inventory

### 2.1 Method and its limits

The `npx skills find` CLI truncates to 6 results. skills.sh exposes an undocumented JSON endpoint
(`GET /api/search?q=`, 30 req/min, silent rate-limit errors that look like empty results) returning up
to 100. A 35-term sweep yielded **2,747 unique skills**, of which **1,318** match a CS-domain keyword
regex. Both TSVs are in `_raw/`. Method and the rate-limit gotcha: `_raw-skills-lead-breadth.md` §1.

Three caveats that bound every number below:

1. **The search is semantic and lossy.** It never returned `coreyhaines31/marketingskills/onboarding`
   for any of the 35 terms, though the CLI returns it at 40.2K installs. The aggregate is a discovery
   net, not a census.
2. **Install counts double-count renames.** `onboarding-cro` (54.1K) and `onboarding` (40.2K) are the
   *same skill* — `README.md:230` and `VERSIONS.md:205` of marketingskills both carry the rename map
   `| onboarding-cro | onboarding |`. Combined exposure ≈94K for one skill, not two.
   (`_raw-skills-incumbent.md` §1a.)
3. **A registry listing is not a skill.** skills.sh indexes 22 `sylphxai/skills` CS skills; **16 of
   them do not exist at HEAD**. `mengto/skills@customer-support-verification` (140 installs) was
   deleted 2026-07-28, commit message `"Remove private customer support skills"`.
   `absolutelyskilled`'s three CS listings never existed — its own generated `skills.yaml` says
   `total_skills: 11`, all dev-SDLC. Clone and check HEAD before citing anything.
   (`_raw-skills-lead-breadth.md` §4; `_raw-skills-cs-packs.md` repo table.)

### 2.2 The distribution

```
84202  coreyhaines31/marketingskills/churn-prevention
54224  pbakaus/impeccable/onboard
24340  googleworkspace/cli/persona-customer-support        ← 39-line CLI persona, not a CS pack
 3738  claude-office-skills/skills/customer-success
 2447  anthropics/knowledge-work-plugins/audit-support
 2322  anthropics/knowledge-work-plugins/ticket-triage
 2198  anthropics/knowledge-work-plugins/customer-escalation
 2132  anthropics/knowledge-work-plugins/onboarding
   …then a flat tail; by rank ~40 everything is under 400 installs…
```

**Every purpose-built CS pack in the ecosystem sits between 1 and 200 installs.** Ranking repos by
*breadth* (count of CS-matching skills) instead of installs surfaces what install-ranking hides:
`t0ddc3by/claude-for-customer-success` (30), `sylphxai/skills` (22), `gtmagents/gtm-agents` (12),
`guia-matthieu/clawfu-skills` (9), `composio-community/support-skills` (8),
`ncklrs/startup-os-skills` (6). The #1 breadth repo has ~1 install per skill.

### 2.3 Per-pack inventory

Depth grades: **A** = router + references + genuine judgment; **B** = substantial single file, some
scaffolding; **C** = template/checklist; **D** = thin tool-driver or persona wrapper.

| Pack | Scale | License (file opened directly) | Depth | Covers | Disposition |
|---|---|---|---|---|---|
| **t0ddc3by/claude-for-customer-success** | 81 skills, 28,988 lines, 6 plugins, 660 files, 58★ | **Apache-2.0, © SuccessCOACHING** (GitHub API says `NOASSERTION` — lied again) | **A** | CSM account work, renewals, CS rev-ops, portfolio health, QBR, escalation memos | **DO NOT LIFT** — thin license on thick IP (§5.2) |
| **anthropics/knowledge-work-plugins** `customer-support/` | 5 skills, 1,544 lines; repo 23,246★, pushed 2026-08-02 | Apache-2.0 (root + per-plugin copy, byte-identical) | **B+** | ticket-triage, customer-escalation, draft-response, kb-article, customer-research | Liftable; the official tactical baseline to differentiate from |
| **coreyhaines31/marketingskills** (churn-prevention, onboarding) | ~1,628 lines + evals | MIT, © Corey Haines 2025 | **C** | Cancel flows, dunning, activation checklists, save offers | Cite his framing; do not launder his uncited numbers |
| **ncklrs/startup-os-skills** | 6 CS skills, thin router + 8–13 `rules/*.md` each | **NO LICENSE FILE** | **A** (best architecture in the small-pack cluster) | Health analysis, renewals, support ops, onboarding, QBR, CS strategy | **Cite only** — biggest licensing loss in the sweep |
| **composio-community/support-skills** | 38 skills, 2,612 lines (mean 69), 14★, dormant since 2026-04-21 | **NO LICENSE FILE** | **D** | Full support desk: triage, SLA, macros, CSAT, NPS, deflection-adjacent | Cite only |
| **guia-matthieu/clawfu-skills** | 7 CS files, 286–535 lines each | MIT | **C** | Health monitor, churn prediction, expansion signals, QBR, onboarding, renewals | Vendor-folklore exemplar (§4.2) |
| **onewave-ai/claude-skills** | churn-autopsy, renewal-predictor + references | MIT | **B** | Churn RCA, renewal scoring | Most epistemically honest small pack (§3.4) |
| **alirezarezvani/claude-skills** | CSM + churn + CCO advisor + references + python scripts | MIT | **B** | Health scoring w/ per-dimension rationale, CS metrics benchmarks | Benchmarks unsourced — do not cite |
| **claude-office-skills/skills** `customer-success` | 601 lines, one file, 3.7K installs | MIT | **C** | Onboarding, health, QBR, expansion, retention — all in one file | LLM-boilerplate; fabricated example numbers |
| **daffy0208/ai-dev-standards** | support-builder 587, feedback-analyzer 469, KB-manager 732 | MIT (dangling per-skill `LICENSE.txt` pointer that doesn't exist) | **B** | Builds help centers/chatbots/ticketing as CODE | **Seam flag** — this is build/product territory, not success (§6.4) |
| **gtmagents/gtm-agents** | 12 CS-matching, ~31-line stubs | Apache-2.0 | **D** | VoC, renewal playbooks, advocacy, SLA tracking, escalation | Breadth without content |
| **sylphxai/skills** | 6 CS at HEAD (22 indexed), 82–91 lines, 1★, 2 weeks old | MIT | **D** | Support ops, refund flow, feedback loop | Generative output, not practice |
| **borghei/claude-skills** | CSM skill ×2 copies | **Commons Clause v1.0 + MIT** — no commercial resale | **C** | Health scoring | Near-duplicate of alirezarezvani's; **count as one data point** |
| **manojbajaj95/claude-gtm-plugin** | 365 lines | MIT | **C** | CS + retention, "Part 1..9" | Fabricated lift numbers (§4.3) |
| **shawnpang/startup-founder-skills** `churn-analysis` | 122 lines | MIT | **C** | Churn for seed/Series A | **Only solo-honest pack found** (§3.5) |
| **hubspot/agent-cli-skills** `customer-retention` | 118 lines, 18★ | Apache-2.0 | **D** | HubSpot CRM filter automation | Honest "Known gaps" section; leaves strategy blank |
| **refoundai/lenny-skills** `retention-engagement` | 76 lines + references, 1,209★ | MIT | **B** | Practitioner canon, named attribution (Duolingo streaks, Sarah Tavel, Jason Cohen) | Cite the *speaker*, never "per lenny-skills" (§5.3) |
| **deanpeters/Product-Manager-Skills** | VoC-miner + saas-metrics (642 lines), 6,192★ | **CC BY-NC-SA 4.0** (API said `NOASSERTION`) | **B+** | VoC discipline, NRR/GRR/ACV formulas | **NonCommercial — cannot lift.** Richest adjacent pack, most restricted |
| **wondelai/skills** `improve-retention` | 235 lines, 1,816★ | MIT | **B** | Fogg Behavior Model (B=MAP), attributed to BJ Fogg | **Best evidence grade found anywhere** (§4.5) |
| **kostja94/marketing-skills** `retention-strategy` | 78 lines | MIT | **C** | Retention strategy | Ships both never-ship figures verbatim (§4.3) |
| **googleworkspace/cli** `persona-customer-support` | 39–40 lines, 24.3K installs | Apache-2.0 | **D** | `gws gmail +triage` wrapper | **Do not over-weight this install count** — it reflects a 30K★ parent CLI |

### 2.4 Verified false positives (do not count these as competitors)

- `firecrawl/skills@firecrawl-build-onboarding` (56.5K) — **developer** onboarding: getting a
  `FIRECRAWL_API_KEY` into a project. `_raw-skills-incumbent.md` §4.
- `firecrawl/firecrawl-workflows@firecrawl-knowledge-base` (30K) — a **RAG corpus builder**, not a
  customer help center. No mention of tickets, customers, or support anywhere in the file.
- `shopify/shopify-ai-toolkit@shopify-onboarding-dev` (6.1K) — explicitly "NOT for merchants."
  `@shopify-onboarding-merchant` (5.4K) is first-store-creation, i.e. signup-side, not post-signup.
- `okx/onchainos-skills@okx-ai-support` (1.9K) — **the skill does not exist**; the repo is crypto
  agent-identity tooling.
- `customware-ai/skills@customware-support-widget` (1.2K) — a React component embed. Frontend's, if
  anyone's.
- **`ComposioHQ/awesome-claude-skills` (71,597★) "Support & Helpdesk" section is entirely dead links.**
  `gh api contents/freshdesk-automation` etc. all return `"Not Found"`. Auto-generated marketing copy
  pointing at Composio's toolkit catalog. Do not cite. `_raw-skills-registries.md` §1d.

---

## 3. The incumbent question, answered three ways

### 3.1 By reach — `coreyhaines31/marketingskills`: real users, no depth

84.2K installs on churn-prevention is the only genuinely large CS-adjacent adoption number that isn't a
false positive or a parent-tool artifact. And it is **checklist, not judgment**, on A1's evidence:

- The skill is decision *tables* plus a fixed 5-step flow (`Trigger → Survey → Dynamic Offer →
  Confirmation → Post-Cancel`, `SKILL.md:70`). No passage anywhere asks when a health score applies,
  what to do with an ambiguous signal, or when not to build the thing.
- Its own eval suite grades template-conformance: assertions are `"Includes exit survey with 7
  categories"`, `"Applies dunning stack framework"`, `"Recommends health score model"`. **No eval tests
  an insufficient-data or don't-build-this-yet case.**
- The health score is asserted as settled fact (`SKILL.md:232-239`): `Login frequency × 0.30 + Feature
  usage × 0.25 + Support sentiment × 0.15 + Billing health × 0.15 + Engagement × 0.15` — no method, no
  citation, no "validate against your own churned cohort" caveat.
- `grep -n -i "http\|source:\|study\|research\|according to"` across SKILL.md + both reference files:
  **zero matches.**

The only judgment-teaching language in the entire repo lives in a peripheral 46-loop catalog:
`marketing-loops/references/loop-catalog.md:376-388` — *"**Self-check**: Is the 'drop' a real trend or a
weekend/holiday dip? Compare to the account's own baseline."* and `:432-444` — *"Is a theme a real
pattern or one loud voice? Require a minimum count before acting on it."* Two lines, not in either
flagship skill.

**Critically: the repo has no skill scoped to support, escalation, help-content/KB, health-score,
renewals, or expansion.** Those canonical includes are absent entirely.

### 3.2 By officialdom — `anthropics/knowledge-work-plugins`: strong, tactical, half the territory

This is the closest thing to an official incumbent, and A1/A3 both landed on it independently.
23,246★, Apache-2.0, pushed the same day we looked. Its `customer-support/README.md`:

> "A customer support plugin primarily designed for Cowork, Anthropic's agentic desktop application —
> though it also works in Claude Code. Provides ticket triage, escalation management, response
> drafting, customer research, and knowledge base authoring for support teams."

It has real judgment nuggets our siblings lack — `ticket-triage/SKILL.md:126`: *"When in doubt, lean
toward Bug — it's better to investigate than dismiss"*; `:121-124` root-cause-drives-category rules;
`kb-article/SKILL.md:349`: *"Maintain aggressively — a wrong article is worse than no article."*

But it is **day-to-day agent copilot work**, and it is **half the mission**: zero onboarding, zero
health scoring, zero VoC aggregation, zero renewals, zero expansion. And zero citations (same grep,
zero hits).

Two notes for positioning: `w95/awesome-claude-corporate-skills`'s "11-customer-success" folder is
largely a repackaging of this same content; and `anthropics/skills` itself is **confirmed empty** —
`grep -ril "customer\|onboarding\|support ticket\|churn" skills/` → zero matches across its 19 skills.

### 3.3 By architecture — `t0ddc3by/claude-for-customer-success`: the finding that most constrains us

Nobody had looked at this. It ranks #1 on breadth and ~last on adoption. 81 skills / 28,988 lines /
6 installable plugins / `shared/cs-domain-model.md` + `cross-skill-registry.md` / lint + cross-link +
eval-fixture scripts. Structurally it is the nearest neighbour to our own family shape that exists.

It self-describes as a demo, not a product (`README.md:13`): *"A reference implementation… not a
deployment-ready product."* Skills carry literal `[PROPOSED]` markers.

**And it already teaches our flagship's core question.** `cs-ops/skills/health-model-review/SKILL.md:18`:

> "Audit the health model at the portfolio level — does it actually predict churn, or does it just
> classify accounts?"

with guardrails:

> "G1: Health scores are heuristics — calibration findings must not be framed as churn predictions."
> "G2: Calibration assessment without historical churn data produces a description, not a verdict —
> surface the data gap explicitly rather than speculating on predictive accuracy."

This is not a one-off: **68 of 81** files carry `G1:`–`G9:` guardrails, **64 of 81** have a
`## Do NOT use for` section.

**Honest assessment.** Our flagship hypothesis ("what a health score can honestly predict") is *not*
virgin territory. What remains open, precisely:

1. **It is asserted, not evidenced.** Zero citations in 28,988 lines (§4.1). "Health scores are
   heuristics" is delivered at exactly the same evidentiary grade as the folklore it corrects.
2. **It is enterprise-only.** Everything assumes ARR tiers, a CRM, a CS platform, a portfolio, a
   renewal event. See §3.5.
3. **It never crosses into support.** 0 of 81 files mention help centers, KB articles, or deflection
   (§4.4).
4. **It is unadopted.** ~1 install per skill; nothing in the ecosystem builds on it.

Our differentiation must therefore be *evidence + honest scope + integration*, not *"nobody has thought
about health-score validity."* Someone has. They just couldn't show their work.

### 3.4 The two packs that argue for rigor

Worth knowing because they are the nearest thing to allies:

- **`onewave-ai/claude-skills`** teaches internal rigor rather than name-dropping vendors.
  `churn-autopsy/references/standards.md:17-18`: *"Quantify wherever possible. 'Usage declined' is not
  acceptable; 'Usage declined 47% over 3 months from X to Y' is."* / *"Compare to benchmarks. A 10%
  usage decline means nothing without context about what is normal."* Its `renewal-predictor` ties
  *confidence* to data completeness rather than claiming accuracy: *"Never score a dimension at 0
  unless there is affirmative evidence of a problem — absence of data is not evidence of a problem."*
- **`ncklrs/startup-os-skills`** ships the sweep's most sophisticated file on health-score rigor:
  `rules/health-model-validation.md` (350 lines) with a real validation-metric table — churn prediction
  accuracy, surprise churn rate, false positive rate, score-outcome Pearson correlation, lift at 10%,
  calibration error — plus anti-patterns *"Perfect-seeking — waiting for 100% accuracy vs. iterating"*
  and *"Set and forget — never validating after initial launch."*
  **It has no LICENSE file: cite only.** And as A2 notes, those metrics are standard classifier-
  evaluation concepts, not this pack's invention — we should source them from the calibration
  literature (channel D) rather than lift the file.

### 3.5 The solo question — wedge hypothesis 1 survives, sharpened

Almost every pack assumes a CSM-staffed portfolio with QBRs, executive sponsors, and dedicated CS
tooling. Two apparent exceptions, and only one is real:

- **`t0ddc3by`'s `deployment-cookbooks/solo-csm-cookbook.md`** (3,163 lines, `[PROPOSED]`) is the only
  deep solo-framed CS content anywhere — but its "solo" is *one CSM inside a company that has CSMs*:
  > "**Audience:** Individual CSMs deploying the claude-for-customer-success plugin suite for solo use"
  > "This cookbook does not cover team or enterprise deployment… If you're deploying this suite for a
  > team, contact SuccessCOACHING for enterprise deployment guidance."

  It still assumes a book of accounts, a CRM, a CS platform, ARR tiers, renewals, quota. A single-seat
  deployment guide, not a small-company methodology.
- **`shawnpang/startup-founder-skills@churn-analysis`** is the genuine one: explicitly targets
  *"seed/Series A teams managing customers manually without dedicated CS platforms like Gainsight or
  ChurnZero"* and assumes support inboxes, Slack, and spreadsheets. 122 lines.

**The charter's §1033 reader — the solo self-serve builder with no CSM, no ARR tier model, often no
renewal event — is addressed by one 122-line skill in the entire ecosystem.** Hypothesis 1 confirmed,
and sharpened: the gap is not "enterprise vs solo" but "CS-team-with-a-book vs builder-with-users."

---

## 4. Emptiness, grep-verified

Per the charter's instruction (and quality-skill's lesson) these are counts from actual greps, not
impressions.

### 4.1 The evidence layer is empty everywhere

| Corpus | Scale | External research citations |
|---|---|---|
| `t0ddc3by/claude-for-customer-success` | 81 skills / 28,988 lines | **0** |
| `coreyhaines31/marketingskills` churn-prevention + onboarding | ~1,628 lines | **0** |
| `anthropics/knowledge-work-plugins/customer-support` | 5 skills / 1,544 lines | **0** |
| `composio-community/support-skills` | 38 skills / 2,612 lines | **0** (only `composio.dev` ×59) |
| `sylphxai/skills` CS subset | 6 skills | **0** |
| `guia-matthieu/clawfu-skills` CS cluster | 7 files | **0** links; 7 vendor-name-only `## References` lists |

For `t0ddc3by`, `grep -rhoE 'https?://[^ )>"]+' --include=SKILL.md .` returns **no output at all** across
28,988 lines. Marker counts in that corpus: `Reichheld` 0, `Harvard Business Review` 0, `HBR` 0, `doi.`
0, `arxiv` 0, `according to research` 0, `study (found|shows|of)` 0, `peer-review` 0, `meta-analys` 0 —
against `Gainsight` 8 and `SuccessCOACHING` 12. The one `et al` hit is the substring in "has **met al**l
graduation criteria."

The single counter-example found in the whole channel: `wondelai/skills@improve-retention` attributes
the Fogg Behavior Model (B=MAP) to BJ Fogg by name and quote — and that is a psychology framework, not
evidence about customer success.

**This is the wedge.** Not "nobody teaches judgment" — `t0ddc3by` does, and `ncklrs` and `onewave-ai`
gesture at it. But **nobody can show their work**, which means every good instinct in the ecosystem
sits at the same grade as the folklore beside it.

### 4.2 Vendor-density is total (charter rule 5, confirmed)

The cleanest instance: all 7 `guia-matthieu/clawfu-skills` CS files open with `Based on **Gainsight X**
and **Y**` and close with a `## References` list of 3–4 vendor names (Gainsight / Totango / ChurnZero /
Lincoln Murphy / SaaStr / ProfitWell) — **never a link, page, date, or document.** Seven files, seven
vendor-name lists, zero traceable citations. `_raw-skills-cs-packs.md` §Architecture-2.

### 4.3 Falsification-strip harvest

New figures found in the wild this channel, all unsourced, all quoted verbatim in the `_raw` files.
Flagging by **class**, per the rule learned twice — the list is not the rule.

**Both charter never-ship figures found shipping together**, `kostja94/marketing-skills` retention
SKILL.md: *"Acquiring new customers costs 5–25× more than retaining; 5% retention improvement can
increase profitability 25–95%."* The folklore is load-bearing in the ecosystem — usable as a concrete
"here is the folklore, here is why it is untraceable" example in our flagship.

**Class: voluntary/involuntary churn split** — asserted at least three ways, never consistently.
`coreyhaines31/.../churn-prevention/SKILL.md:53`: *"Voluntary churn is typically 50-70% of total churn.
Involuntary churn is 30-50%."* `manojbajaj95/.../SKILL.md:139`: identical numbers. `kostja94`:
*"Voluntary 60–80% / Involuntary 20–40%."* `w95/.../churn-analysis`: *"Typical Rate: 60-70% of total
churn."* A2's tell is worth keeping: the ranges don't partition to 100%, which means they weren't
derived from one dataset.

**Class: save-rate / recovery-rate benchmarks** — `churn-prevention/SKILL.md:319-322` recovery benchmark
table (soft decline "Good" 70%+, hard decline 40%+, overall 60%+); `:336-339` (cancel-flow save rate
25-35%, dunning recovery 50-60%); `:369` *"Even a simple survey + one offer saves 10-15%"*;
`shawnpang/.../churn-analysis/SKILL.md:83,86,89,92` (pause saves 15-25% B2C / 10-15% B2B; cancel flow
saves 10-20%; dunning recovers 30-50%; reactivation 5-15%).

**Class: vendor marketing numbers laundered as tool facts** —
`churn-prevention/SKILL.md:390`: *"**Churnkey** | Full cancel flow + dunning | AI-powered adaptive
offers, 34% avg save rate"* — a vendor's own number presented unattributed as a comparison fact.

**Class: health-score predictive claims** —
`ncklrs/.../health-score-design.md:11`: *"A well-designed health score predicts customer outcomes 60-90
days before they happen."* `ncklrs/.../churn-prediction-modeling.md:11`: *"A well-calibrated model can
reduce churn by 15-30%."* `manojbajaj95/.../SKILL.md:49`: *"Intervention when metrics dip is worth 10x
intervention after cancellation request."*

**Class: activation-lift-by-milestone** — `manojbajaj95/.../SKILL.md:82-85`: Profile complete +8%, first
core action +15%, first value experience +25%, 3-day streak +35% — **with no defined baseline for what
the "+" is relative to.**

**Class: unsourced operational defaults with real staffing consequences** (new class, from my slice) —
`composio-community/support-skills/sla-monitor/SKILL.md:18-20,34`: *"**First Response Time:** 1 hour
(P0), 4 hours (P1), 8 hours (P2), 24 hours (P3)"*, resolution times, *"AT RISK - Over 75% of SLA target
elapsed"*; `merge-tickets/SKILL.md:33`: *">70% overlap"*. These aren't claims about the world, they're
commitments a reader will adopt — and they're shipped as bare defaults.

**Class: benchmark tables with a hand-wave for a source** —
`alirezarezvani/.../references/cs-metrics-benchmarks.md:259` sources an entire NRR/GRR/logo-churn/TTFV/
CSM-ratio table to *"Industry surveys, SaaS benchmarking reports, customer success community data
(2024-2025 data cycles)"* — no named survey, no report. Treat every number in it as unsourced.

**A named source left uncited** —
`t0ddc3by/.../rev-ops/skills/quota-sensitivity-analysis/SKILL.md:69-72` asks the reader to name the
**"KBCM actuals median (55–65%)"** for quota attainment and never cites it. KBCM = KeyBanc Capital
Markets' annual SaaS survey.

> **CORRECTION 2026-08-02 (channel-A lead, after channel D verification).** I originally flagged this
> to channel D as "a named source we can actually chase" and asked D to trace or kill it. **That flag
> was wrong on both counts and is withdrawn.** Channel D verified that the KBCM survey's quota-
> attainment figure is about **SALES/AE quota, not CSM quota** (KBCM's recent editions run ~70→75%,
> not 55–65%). Two consequences: (a) it is **outside success's domain** — I should have caught this
> from the skill's own formula two lines below, `Revenue = ae_required × ae_quota × 0.75`, which is
> plainly about account executives; (b) the pack's **55–65% does not match KBCM's published values**,
> so this is not an under-cited real figure but a **misattributed one**. It remains a good
> falsification exhibit — a pack instructing the reader to cite a named survey while stating a number
> that survey does not support — but it is a *sales* exhibit, and **channel D should not spend budget
> tracing it.** The surrounding §4.3 figure-classes are unaffected.

### 4.4 Coverage emptiness — what 81 CS skills never mention

`t0ddc3by`, files matching out of 81:

| concept | files |
|---|---|
| `knowledge base\|help cent\|help doc\|article` | **0** |
| `deflect` | **0** |
| `AI (agent\|bot\|chatbot)\|chatbot` | **0** |
| `community\|forum` | 1 |
| `support (process\|taxonom\|queue\|tier)` | 1 |

The two large counts are misleading and I checked every class of hit:

- **`ticket` (25 files) is support-as-INPUT, never support-as-DESIGN.** Every hit is a CSM reading
  ticket state as an account signal — `risk-flag/SKILL.md:174`: `| Open escalation or unresolved P1
  ticket | [Yes/No] | [ticket details] | High |`; `account-research/SKILL.md:315-318`: `**Support ticket
  summary**` / `- Open: [N] tickets — [P1: N / P2: N / P3-P4: N]`. No skill designs a queue, taxonomy,
  tiering model, macro library, or QA rubric.
- **`SLA` (63 files) is an internal escalation-routing placeholder, not a support SLA.**
  `risk-flag/SKILL.md:220-222`: `| Condition | Route to | Via | SLA |` / `| [Matching scenario] |
  [configured contact] | [configured channel] | [configured SLA] |`; `qbr-builder/SKILL.md:299`:
  `| Urgent issue | [Support channel] | [link] | [SLA from your contract] |`. Always `[configured]` or
  `[from your contract]` — **the pack never teaches how to SET one.**

### 4.5 Wedge hypothesis 3 (AI-support policy) — wide open, confirmed twice

A2, across 12+ repos: **zero mentions of AI chatbots as a policy question.** The single hit is
`daffy0208/customer-support-builder` naming "AI-powered chatbots" once as a Stage-4 maturity feature
(10K+ users) with no deflection-rate honesty. My slice: `chatbot` matches **0 of 81** files in the
largest CS pack in the ecosystem, and `deflect` matches **0**. A3: `AI support agent` / `chatbot
support` queries returned only tool-persona wrappers.

Nobody in the agent-skills ecosystem has written the policy layer for AI support agents. Given the
family already owns `ai` for the mechanics, this is the cleanest open ground channel A found.

---

## 5. Licensing (charter rule 3, all 5 clauses)

### 5.1 (a) The GitHub license API lied again — 8th+ instance

- `t0ddc3by/claude-for-customer-success`: API `NOASSERTION` → file is **Apache-2.0, © SuccessCOACHING**.
- `deanpeters/Product-Manager-Skills`: API ambiguous `other`/`NOASSERTION` → file is
  **CC BY-NC-SA 4.0**. Opening the file was the only way to find the NonCommercial clause.

**Never use the API. Open the file.**

### 5.2 (e) Thin license on thick IP — the clearest instance yet

`t0ddc3by/claude-for-customer-success` is Apache-2.0, and the substance is not the author's.
`README.md:15`: *"Methodology-opinionated (SuccessCOACHING Customer Success methodologies and
frameworks)"*. `README.md:90`: *"This suite is built on **SuccessCOACHING** Customer Success Management
methodologies… The **TARO Playbook** frame…"*. `README.md:100` names the **"CSMBOK Knowledge Graph"** —
"maps the body of knowledge for Customer Success as a discipline."

The Apache grant covers these files. It does not license SuccessCOACHING's TARO Playbook or CSMBOK.
**Disposition: DO NOT LIFT.** Anything we want from it must be independently derived and attributed to
SuccessCOACHING by name.

### 5.3 The other license rulings

| Repo | Ruling |
|---|---|
| `ncklrs/startup-os-skills` | **No LICENSE file → cite only.** Best small-pack architecture in the sweep and we cannot lift a line of it. |
| `composio-community/support-skills` | **No LICENSE file → cite only.** |
| `ComposioHQ/awesome-claude-skills`, `composio-community/awesome-codex-skills`, `Aradotso/trending-skills` | No LICENSE. Moot — dead links / no content. |
| `deanpeters/Product-Manager-Skills` | **CC BY-NC-SA 4.0 — NonCommercial. Cannot be lifted or adapted for a commercially-distributed pack.** The richest adjacent content is the most restricted. Cite only; do not adapt phrasing or structure. |
| `borghei/claude-skills` | **Commons Clause v1.0 + MIT** — no "Sell," which the text defines to include *"fees for hosting or consulting/support services related to the Software."* Also: near-duplicate of `alirezarezvani`'s plain-MIT design (identical `DIMENSION_WEIGHTS`, identical `python-tools:` metadata line). **Count the two as one data point** on weight convergence. |
| `refoundai/lenny-skills` | MIT covers RefoundAI's *compilation*, not the podcast guests' words. Any lift cites the original speaker and episode, never "per lenny-skills." |
| `coreyhaines31/marketingskills` | MIT, alive (commits through 2026-07-27). Covers Corey Haines's own phrasing. It does **not** validate his uncited numbers — do not launder folklore through a permissive license. |
| `anthropics/knowledge-work-plugins` | Apache-2.0, root + per-plugin copies byte-identical. Clean. |
| `daffy0208/ai-dev-standards` | MIT (root LICENSE + both package.json). **Gotcha:** `customer-support-builder/SKILL.md:4` declares `license: Complete terms in LICENSE.txt` and **no such file exists** in the skill folder. Dangling pointer; repo-root MIT governs. |
| `intercom/2x-skills`, `firecrawl/*`, `hubspot/agent-cli-skills`, `twilio/ai`, `wondelai`, `shopify`, `googleworkspace/cli`, `gtmagents`, `sylphxai`, and the remaining MIT packs | Clean, manifests consistent where present. No GeoLift-style dual-license traps found. |

### 5.4 Note for the licensing rule itself

The charter's 5 clauses held. Two observations worth carrying forward: **(a) fired twice in one
channel** (both times on the repos that mattered most), and clause **(c)** produced a new failure mode —
a per-skill license *pointer* to a file that doesn't exist. Suggested refinement: when a skill declares
its own license, verify the referenced file resolves; a dangling pointer is not a license.

---

## 6. Seam flags for the controller (charter rule 6 — recorded, not assigned)

1. **marketing ↔ success at SIGNUP: independently confirmed from marketing's side.**
   `coreyhaines31/marketingskills` `signup/SKILL.md:3` hands off explicitly: *"For post-signup
   onboarding, see onboarding."* And its `revops/SKILL.md:10` names customer success as an external
   system it *connects*, not something it does: *"...systems that connect marketing, sales, and customer
   success into a unified revenue engine."* Consistent with the charter's existing evidence, from a
   second angle.
2. **The `customer-research` name collision.** `marketingskills@customer-research` mines VoC for
   positioning and copy; `knowledge-work-plugins@customer-research` looks up an answer for one ticket.
   Same name, different jobs — and **neither does aggregate VoC trend analysis.** That job is
   genuinely unclaimed; success should claim it explicitly rather than assume the name is taken.
3. **`daffy0208/ai-dev-standards` builds support infrastructure as CODE** (help centers, chatbots,
   ticketing, KB — 587/469/732 lines). This is the charter's code-policy boundary in the wild: does
   success *specify* the KB and hand implementation to product/build, or scaffold it? Recommend
   success owns requirements + taxonomy + content strategy and cedes implementation — but it is the
   controller's call.
4. **Support tooling architecture is a real adjacent job with an existing occupant.**
   `twilio/ai@twilio-customer-support-architect` (199 lines) is an IVR/Studio/TaskRouter/Flex decision
   tree. Contact-center tooling selection is arguably `architecture`'s or `automation`'s, not success's.
5. **`shopify-onboarding-merchant` sits on the signup side of the seam**, not the adoption side —
   a useful concrete test case for where the charter's line falls.
6. **For channel C (github):** `t0ddc3by/claude-for-customer-success` is a skill repo so I read it, but
   its `managed-agent-cookbooks/` (11 managed agents via the Claude Managed Agents API) and its
   `scripts/` toolchain (`lint-skill-body.py`, `validate-cross-links.py`, `generate-eval-fixtures.py`)
   are general agent-architecture prior art beyond my lane. Flagging, not chasing.
7. ~~**For channel D:** the KBCM quota-attainment median (55–65%) — a named, findable primary source
   left uncited in the wild (§4.3).~~ **WITHDRAWN 2026-08-02** after channel D verification: the KBCM
   figure is sales/AE quota attainment (~70→75% in recent editions), not CSM quota, and 55–65% is a
   misattribution rather than an under-cited real figure. Out of success's domain; D should not trace
   it. Full correction note at §4.3.

---

## 7. Open questions

1. **How do we differentiate from `t0ddc3by` on the health-score flagship?** My reading: evidence
   (they cite nothing), scope honesty (their solo is a single-seat enterprise deployment), and
   integration (they never touch support). But the flagship's *framing* must not claim nobody has asked
   the question. Controller should adjudicate the framing before the pack is scoped.
2. **Does `anthropics/knowledge-work-plugins/customer-support` constrain what we should ship on
   ticket-triage and KB authoring?** It is official, Apache-2.0, actively maintained, and decent. My
   instinct is to route *to* it for the tactical layer and own the layer above (taxonomy design,
   deflection policy, escalation policy, QA rubrics) — the same posture other family packs take toward
   good incumbents. Needs a decision.
3. **Health-score weight convergence is not evidence.** The packs converge loosely on ~30/25/20/25
   across usage/engagement/support/relationship — but `borghei` is a near-duplicate of `alirezarezvani`
   (one data point, not two), and **no pack anywhere backtests its own weights.** Two describe how you
   *would* validate; none presents a completed backtest. If channel D finds no primary validation
   either, "the weights are folklore all the way down" becomes a defensible flagship claim — but that
   is D's finding to make, not mine.
4. **Is "no citations anywhere" a wedge or just the medium's norm?** Every skill pack in every domain
   under-cites. Growth and quality made evidence-grading a differentiator anyway. Worth confirming this
   is a *success-specific* opening (where folklore is unusually load-bearing) rather than a generic
   observation.

---

## 7b. Channel C cross-flag — resolved, verdict unchanged

Channel C's churn-health worker surfaced five Claude-skill repos incidentally
(`_raw/_raw-gh-churn-health.md` §"FLAG TO A"). Checked all five against
`_data-skillssh-all-2747.tsv`:

- **Already in my inventory:** `borghei/Claude-Skills` (13 rows — §2.3, Commons Clause + MIT
  near-duplicate) and `claude-office-skills/skills` (14 rows — §2.3, the 601-line single-file pack).
- **`afumu/wetrace-skill`** (41★, no license) — WeChat chat-log tooling. Out of domain.
- **`nimrodfisher/data-analytics-skills`** (337★, **no LICENSE → cite only**) — no CS content. Its six
  top-level dirs are data-analytics categories; the `health_score` code-search hit resolves to
  `03-data-analysis-investigation/cohort-analysis/` (`retention_metrics_glossary.md`,
  `retention_matrix.py`, `retention_matrix.html`). **Seam flag:** retention *cohort mechanics* are
  data/growth territory, not success's — worth noting only because it is a runnable artifact where
  most of this domain ships prose.
- **`majiayu000/claude-skill-registry`** (530★, MIT, pushed 2026-08-02) — **a fourth discovery surface
  my API sweep did not cover.** A mirror registry: 64,450 tree paths (the GitHub tree API reports
  `truncated: true`, so this is a floor, not a count), skills stored as
  `skills/<category>/<skill>-<owner>-<repo>/{SKILL.md,metadata.json}` across 16 categories.

  **It does not change the verdict.** Every CS entry in its `business/` category traces upstream to a
  repo already in this report or in the long tail I deliberately deferred (§8) — spot-checked via
  `metadata.json`: `cs-health-scorecard` → `mohitagw15856/pm-claude-skills` (already flagged as
  deferred mid-breadth, 12 CS-matching skills); `customer-retention-optimizer` →
  `briansunter/kungfu`; `portfolio-support-ops` → `evalops/open-associate-skills`. The visible
  entries also mirror `alirezarezvani`, `absolutelyskilled`, and `refoundai/lenny-skills`, all
  covered above. Its CS surface is aggregation of the same long tail, not new content.

  **Licensing note worth carrying forward:** the registry is MIT, but every mirrored skill's
  `metadata.json` carries its own `license` and `permission_note` field — verbatim for all three
  spot-checks: `"license": "NOASSERTION"` and *"Restricted or unknown license. Do not treat as MIT;
  verify upstream permissions."* An aggregator that explicitly disclaims its own repo license over
  mirrored content is a clean live instance of charter rule 3(e) — and a precedent worth imitating.
  It also means **skill-registry mirrors are never a licensing shortcut**: resolve to upstream.

---

## 8. What I did not cover, and why

- **Deep-reads of the mid-breadth repos** `mohitagw15856/pm-claude-skills` (12 CS-matching),
  `leadmagic/gtm-skills` (12), `eddiebelaval/squire` (12), `membranedev/application-skills` (9). Budget
  went to the three highest-breadth repos plus the assigned targets; the naming patterns and install
  counts (all <250) put them in the same generative long tail as `sylphxai`. Listed in
  `_data-skillssh-cs-candidates.tsv` if the controller wants them opened.
- **The ~1,300-row candidate list below rank ~150.** Diminishing returns — sub-50-install skills in
  repos with no CS focus. The data is preserved.
- **The 10 third-party directory sites** (claudeskillhub, awesomeskill.ai, LobeHub, Agensi et al).
  A3 confirmed they mirror GitHub listings rather than host content; existence recorded in
  `_raw-skills-registries.md` §1e, not crawled.
- **`mengto/skills@customer-support-verification`** — deleted from HEAD four days before this research
  (`"Remove private customer support skills"`, 2026-07-28). No source text exists to verify against.
- **General OSS support stacks** (Chatwoot, Zammad, FreeScout, Papercups) — channel C's territory per
  the charter; I stayed out.
- **`x-relay`** — channel B's exclusively; not touched.
