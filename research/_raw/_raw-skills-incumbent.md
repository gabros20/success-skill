# _raw-skills-incumbent — Channel A / Worker A1

Method: shallow-cloned every target repo into `/private/tmp/claude-501/skills-a1/<repo>` and read files directly (no skills.sh summaries trusted for content). Commit SHAs below are from `git log -1` on the clone (2026-08-02).

---

## 1. coreyhaines31/marketingskills — THE PRIME SUSPECT

- Clone: `https://github.com/coreyhaines31/marketingskills` @ `7868cb9251fad80a73d26e488a5ad5f6c4a9f335` (2026-07-27 18:59:01 +0000)
- LICENSE (opened directly, not GitHub API): MIT, `Copyright (c) 2025 Corey Haines` — full permissive, no additional terms. `/private/tmp/claude-501/skills-a1/marketingskills/LICENSE`
- No per-skill license overrides found; no package manifest beyond the plugin structure (no package.json/pyproject shipped).
- 51 skills total in `skills/`. VERSIONS.md shows active maintenance (2.6.0 entry dated 2026-07-01, ads updated 2026-07-05, attribution 2026-07-23) — NOT stale/archived by evidence of commit dates.

### 1a. Install-count inflation finding (falsification-relevant)

`README.md:230` and `VERSIONS.md:205` both show the **rename map**:

> `| onboarding-cro | onboarding |` (README.md:230, VERSIONS.md:205)

README.md:188-190 (v2.0 upgrade notes) confirms `onboarding-cro` is not a separate skill — it is the **pre-v2.0 folder name** for the current `onboarding` skill. The task brief's two install figures (onboarding-cro 54.1K, onboarding 40.2K) are almost certainly **the same skill content counted twice** under old+new names on skills.sh (old-name installs accrued before the rename, new-name installs after) — combined exposure ~94K for one skill, not two distinct skills. This is a registry-artifact, not a depth signal. Flag for the controller: skills.sh install counts for this repo are not reliable as "number of distinct skills adopted" — dedupe by rename map before citing magnitudes.

### 1b. Full CS/success/retention-adjacent inventory (every skill in the repo touching the brief's keyword list)

| Skill | Touches | Verdict |
|---|---|---|
| `churn-prevention` (skills/churn-prevention/SKILL.md) | churn, retention, health score, save offers, dunning | **Core target — analyzed in depth below** |
| `onboarding` (skills/onboarding/SKILL.md) | onboarding, activation, time-to-value | **Core target — analyzed in depth below** |
| `customer-research` (skills/customer-research/SKILL.md) | VoC, support-ticket analysis, "why customers churn" | Adjacent — feeds success's VoC job but framed as *marketing* research (positioning/copy inputs), not a success workflow. Description (SKILL.md:3): `"...'support ticket analysis,' 'voice of customer,' 'VOC'... or 'find out why customers churn/convert/buy.'"` |
| `signup` (skills/signup/SKILL.md) | pre-onboarding handoff | Confirms the charter's SIGNUP seam from the marketing side: description explicitly hands off — `"For post-signup onboarding, see onboarding."` (SKILL.md:3) |
| `revops` (skills/revops/SKILL.md) | lifecycle, "connect marketing, sales, and customer success" | Explicitly names customer success as a *sibling* system it connects to, not something it does. SKILL.md:10: `"...help design and optimize the systems that connect marketing, sales, and customer success into a unified revenue engine."` |
| `referrals` (skills/referrals/SKILL.md) | advocacy (referral/ambassador programs) | Advocacy-adjacent but framed as growth-loop/acquisition, not success-owned relationship advocacy |
| `marketing-loops` (skills/marketing-loops/SKILL.md + references/loop-catalog.md) | churn-signal loop, voice-of-customer loop, onboarding-drop-off loop, feature-adoption loop | **Notable** — see 1c below, this is the most judgment-forward CS-adjacent content in the repo |
| `paywalls`, `popups`, `pricing`, `emails` | touch retention tangentially (win-back emails, upgrade paywalls) | Out of scope, cited only as "Related Skills" cross-refs from churn-prevention/onboarding |

No skill in the repo is named/scoped as support, escalation, help-content/KB-strategy, health-score-as-a-dedicated-skill, renewals, or expansion. Those canonical-includes are **absent** from this repo entirely.

### 1c. marketing-loops: churn-signal & voice-of-customer loops (the closest thing to judgment in this repo)

`skills/marketing-loops/references/loop-catalog.md:376-388` (churn-signal loop):
> "**Self-check**: Is the 'drop' a real trend or a weekend/holiday dip? Compare to the account's own baseline."
> "**Stop / bail-out**: No newly at-risk accounts → skip. Escalate high-value accounts to a human rather than auto-emailing."

`loop-catalog.md:432-444` (voice-of-customer loop):
> "**Self-check**: Is a theme a real pattern or one loud voice? Require a minimum count before acting on it."

These two "self-check" lines are the ONLY passages found anywhere in the marketingskills repo that ask "what can you honestly know / is this signal real" — i.e., actual judgment-teaching. They live in a peripheral 46-loop catalog skill, not in churn-prevention or onboarding themselves.

### 1d. DEPTH TEST — churn-prevention (skills/churn-prevention/SKILL.md, 425 lines + 2 reference files, 724 more lines: cancel-flow-patterns.md 316 lines, dunning-playbook.md 408 lines — total ~1149 lines)

**Structure**: single flat SKILL.md + `references/` (2 files) + `evals/evals.json` (8 behavioral evals). No router; this is the "thin front door + deep references" shape success-skill itself uses, just without judgment content.

**Citations**: `grep -n -i "http\|source:\|study\|research\|according to"` across SKILL.md + both reference files returned **zero matches**. No primary source is cited anywhere in this skill. Every number is asserted flat.

**Verdict: checklist/template, not judgment.** Evidence:
- The skill is organized entirely as decision *tables* (reason→offer mapping, decline-type→retry-strategy, metric→target) and a fixed 5-step flow (`Trigger → Survey → Dynamic Offer → Confirmation → Post-Cancel`, SKILL.md:70). There is no passage anywhere addressing "when does a health score honestly apply," "what if the signal is ambiguous," or "when NOT to build this."
- `evals/evals.json` confirms this pattern-conformance framing over judgment: eval assertions are things like `"Includes exit survey with 7 categories"`, `"Applies dunning stack framework"`, `"Recommends health score model"` — i.e. the eval suite grades whether the model reproduced the template, not whether it correctly judged an ambiguous situation. None of the 5+ eval prompts read include an "insufficient data / don't build a health score yet" test case.
- The health-score formula is presented as settled fact with no validation caveat: SKILL.md:232-239 —
  > ```
  > Health Score = (
  >   Login frequency score × 0.30 +
  >   Feature usage score   × 0.25 +
  >   Support sentiment     × 0.15 +
  >   Billing health        × 0.15 +
  >   Engagement score      × 0.15
  > )
  > ```
  Weights are asserted with no method, no citation, no "these weights are illustrative — validate against your own churned cohort" caveat.

**Falsification-candidate hard numbers (quote verbatim, file:line, all uncited):**
- SKILL.md:53: `"Voluntary churn is typically 50-70% of total churn. Involuntary churn is 30-50% but is often easier to fix."`
- SKILL.md:136: `"60-80% of pausers eventually return to active"`
- SKILL.md:277: `"Card updater services: Visa/Mastercard auto-update programs (reduces hard declines 30-50%)"`
- SKILL.md:319-322 (Recovery Benchmarks table): Soft decline recovery "Good" = `70%+`; Hard decline recovery "Good" = `40%+`; Overall payment recovery "Good" = `60%+`; Pre-dunning prevention "Good" = `20-30%`
- SKILL.md:336-339 (Key Churn Metrics table): Cancel flow save rate target `25-35%`; Offer acceptance rate target `15-25%`; Dunning recovery rate target `50-60%`
- SKILL.md:390: Vendor claim inline as fact — `"**Churnkey** | Full cancel flow + dunning | AI-powered adaptive offers, 34% avg save rate"` — this is a vendor's own marketing number presented without attribution as a tool-comparison fact (textbook vendor-folklore per charter rule 5).
- SKILL.md:369: `"Even a simple survey + one offer saves 10-15%"`

### 1e. DEPTH TEST — onboarding (skills/onboarding/SKILL.md, 221 lines + references/experiments.md 258 lines)

**Structure**: same shape — flat SKILL.md + 1 reference file + evals.json (6+ evals read).

**Citations**: same grep, zero matches. No primary source cited.

**Verdict: checklist/template, not judgment.** Evidence:
- Core content is prescriptive rules with fixed numbers presented as universal: "3-7 items" for checklists (SKILL.md:86), "Max 3-5 steps per tour" (SKILL.md:108), with no discussion of when these ranges don't apply (e.g., complex enterprise setup wizards that legitimately need more steps).
- Eval assertions again test template-conformance: `"Applies checklist pattern with 3-7 items"`, `"Limits to 3-7 total items"`, `"Orders by increasing commitment"` — the eval suite is checking the model recited the rule, not that it correctly judged an ambiguous/edge case.
- Genuinely useful method (not judgment per se, but not vendor folklore either) at SKILL.md:44-47: "Find Your Aha Moment... What do retained users do that churned users don't? What's the earliest indicator of future engagement?" — this is the right question, but the skill never teaches HOW to validate that correlation is causal, doesn't get flagged as a common growth-team error (correlation-as-causation on activation metrics), and cites no source (this exact "aha moment via retained-vs-churned diff" framing traces to Facebook/Chamath-era growth folklore, uncited here).

**Falsification-candidate hard numbers:**
- No hard hit-rate/benchmark numbers in onboarding SKILL.md itself (funnel example at SKILL.md:159-161 is a generic illustrative `100%→80%→60%→40%→25%` funnel, explicitly a template not a claim).

**Bottom line on the depth question**: both core skills are well-organized, non-trivial reference material (comparable file-count/depth to other siblings in this family) but are **pure practitioner-assertion / vendor-folklore grade** (charter rule 5) with **zero primary-source citation** and **zero judgment-under-ambiguity teaching** in the flagship files. The one place judgment-language appears (marketing-loops self-checks, section 1c) is peripheral and not part of either target skill.

---

## 2. googleworkspace/cli @ persona-customer-support

- Clone: `https://github.com/googleworkspace/cli` @ `a3768d0e82ad83cca2da97724e46bea4ff0e6dbd` (2026-04-01 02:51:15 +0800)
- Path: `skills/persona-customer-support/SKILL.md` (full file, 40 lines)
- LICENSE (opened directly): Apache License 2.0, top of repo. `/private/tmp/claude-501/skills-a1/cli/LICENSE`
- **Content**: a thin tool-orchestration persona wrapper, not a CS methodology skill. Full description (SKILL.md:3): `"Manage customer support — track tickets, respond, escalate issues."` The entire body is 5 bullet "Instructions" that just invoke Google Workspace CLI (`gws`) subcommands — e.g. SKILL.md:29: `"Triage the support inbox with \`gws gmail +triage --query 'label:support'\`."` No taxonomy, no priority framework, no judgment content, no reference files. This is a Gmail/Sheets/Chat/Calendar automation persona, not CS depth — should be characterized to the controller as **near-zero depth**, present mainly as a UI-glue example inside a broader Workspace-persona library (persona-event-coordinator, persona-sales-ops, persona-researcher, persona-exec-assistant sit alongside it at the same thinness).

---

## 3. anthropics/knowledge-work-plugins @ customer-support (+ sweep of anthropics/*)

- Clone: `https://github.com/anthropics/knowledge-work-plugins` @ `ea31164bad5e32f82b17e0d4129236e19cd9efb7` (2026-08-02 08:00:34 -0500 — same-day commit, actively maintained)
- Path: `customer-support/` plugin, 5 skills:

| Skill | Path | Lines |
|---|---|---|
| ticket-triage | `customer-support/skills/ticket-triage/SKILL.md` | 275 |
| customer-research | `customer-support/skills/customer-research/SKILL.md` | 252 |
| draft-response | `customer-support/skills/draft-response/SKILL.md` | 418 |
| customer-escalation | `customer-support/skills/customer-escalation/SKILL.md` | 248 |
| kb-article | `customer-support/skills/kb-article/SKILL.md` | 351 |

Total 1,544 lines — comparable depth to marketingskills' churn-prevention/onboarding pair, and covers a **different slice** of the canonical-includes list: ticket-triage (support process design), kb-article (help content/KB strategy), customer-escalation (escalation), customer-research (VoC-adjacent, but framed as "look up an answer for THIS ticket," not aggregate VoC), draft-response (support comms). **No churn/health-score/renewal/expansion/advocacy content anywhere in this plugin.**

- LICENSE (opened directly, both root and per-plugin copies checked, byte-identical via diff): Apache License 2.0. `/private/tmp/claude-501/skills-a1/knowledge-work-plugins/LICENSE` and `customer-support/LICENSE`.
- README.md states this is designed for **Cowork** (Anthropic's agentic desktop app) and Claude Code, ships default MCP connectors (Intercom, HubSpot, Guru/Notion, Atlassian, Slack, Microsoft 365) — `customer-support/README.md`.
- **Depth spot-check (ticket-triage, full file read)**: has a genuine judgment nugget absent from marketingskills — category-determination tiebreak rules, e.g. `ticket-triage/SKILL.md:126`: `"When in doubt, lean toward Bug — it's better to investigate than dismiss"` and `:121-124`: root-cause-drives-category rules ("If they can't log in due to a bug, category is Bug (not Account) — root cause drives the category"). Still template-first (fixed P1-P4 SLA table with hardcoded hour/day numbers, `ticket-triage/SKILL.md:130-168`, uncited), but has more explicit tie-break/ambiguity guidance than marketingskills' two core skills.
- **Depth spot-check (kb-article, full file read)**: includes lifecycle/maintenance judgment — `kb-article/SKILL.md:349`: `"Maintain aggressively — a wrong article is worse than no article"` and a full review-cadence table (`kb-article/SKILL.md:266-277`). No citations found in either file (same "http\|source:\|study" grep pattern, zero hits).
- No hard falsification-candidate benchmark numbers found in ticket-triage/kb-article comparable to churn-prevention's (SLA hour-counts are prescriptive process defaults, not empirical claims, and are explicitly framed as "SLA expectation" i.e. a target you set, not a measured fact).

### Sweep of anthropics/skills (the other anthropics/* repo named in the brief)

- Clone: `https://github.com/anthropics/skills` @ HEAD (checked same session)
- `grep -ril -i "customer\|onboarding\|support ticket\|churn" skills/` → **zero matches**. Confirmed empty: the repo's 19 skills (algorithmic-art, brand-guidelines, canvas-design, claude-api, doc-coauthoring, docx, frontend-design, internal-comms, mcp-builder, pdf, pptx, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing, xlsx, +2 more) are all authoring/dev-tooling skills. No CS/support/onboarding content anywhere in this repo.

---

## 4. firecrawl repos — FALSE POSITIVE VERIFICATION

### firecrawl/skills @ firecrawl-build-onboarding

- Clone: `https://github.com/firecrawl/skills` @ `7ad43730e76913c4d1e9f94bf6fa6f82e38fc12b` (2026-06-16 09:57:40 -0700)
- Path: `skills/firecrawl-build-onboarding/SKILL.md` (full file read, 103 lines)
- LICENSE: ISC (opened directly, `/private/tmp/claude-501/skills-a1/firecrawl-skills/LICENSE`); plugin manifest `.claude-plugin/plugin.json` also declares `"license": "ISC"` — consistent, no thin-license-on-thick-IP issue (this is genuinely Firecrawl's own thin dev-tooling content, not a compiled third-party framework).
- **VERDICT: CONFIRMED FALSE POSITIVE.** This is **developer/SDK onboarding** — getting a `FIRECRAWL_API_KEY` into a project, choosing an SDK, running the browser auth flow — not customer-facing product onboarding. Verbatim description (SKILL.md:3): `"Get Firecrawl credentials and SDK setup into a project. Use when an application needs \`FIRECRAWL_API_KEY\`, when an agent should add Firecrawl to \`.env\`..."` The word "onboarding" here means "onboarding a developer/project onto the Firecrawl API," matching the meaning used across the whole `firecrawl-build*` family (firecrawl-build, firecrawl-build-scrape, firecrawl-build-search, firecrawl-build-interact — all dev-integration skills). **Zero relevance to the success-skill's customer-onboarding job.**

### firecrawl/firecrawl-workflows @ firecrawl-knowledge-base

- Clone: `https://github.com/firecrawl/firecrawl-workflows` @ `1a6b302731139d6de6117d205efd8198d3775cc3` (2026-06-19 14:56:45 -0400)
- Path: `skills/firecrawl-knowledge-base/SKILL.md` (full file read, 87 lines)
- LICENSE: ISC (opened directly, `/private/tmp/claude-501/skills-a1/firecrawl-workflows/LICENSE`); plugin manifest confirms ISC too — consistent.
- **VERDICT: CONFIRMED FALSE POSITIVE.** This is a **content-ingestion/RAG-corpus builder** — it uses Firecrawl's scrape/map/search tools to turn arbitrary web URLs or topics into local markdown files, RAG chunks, or fine-tuning datasets. Verbatim description (SKILL.md:3): `"Build a knowledge base from web content with Firecrawl. Use for local reference docs, RAG-ready chunks, fine-tuning datasets, documentation mirrors, topic corpora, or LLM-ready markdown organized from web sources."` "Knowledge base" here means "a corpus of scraped reference material for an LLM/agent," not a customer-facing help-center/support-KB. No mention of tickets, customers, support, or self-service deflection anywhere in the file. **Zero relevance to the success-skill's help-content/KB-strategy job.** (Sits alongside 15 other `firecrawl-*` workflow skills in the same repo — firecrawl-seo-audit, firecrawl-lead-gen, firecrawl-competitive-intel, etc. — all outcome-focused Firecrawl-tool wrappers, none CS-scoped.)

---

## Licensing summary (charter rule 3, all 5 clauses applied)

| Repo | (a) LICENSE file opened directly | (b) manifest check | (c) per-skill license | (d) archived/alive | (e) thin-license-on-thick-IP? |
|---|---|---|---|---|---|
| coreyhaines31/marketingskills | MIT, Corey Haines, 2025 | none shipped beyond plugin dirs | none found | alive, commits through 2026-07-27 | **YES — flag.** MIT covers Corey Haines's own compiled frameworks (cancel-flow structure, health-score weights, dunning cadence). These frameworks are uncited practitioner synthesis; MIT licenses HIS phrasing/file, not any underlying primary research — there is none identified. Safe to cite Corey Haines's specific structure as his framing; do not launder uncited numbers through this license as if validated. |
| googleworkspace/cli | Apache-2.0 | N/A (Rust/Cargo project, persona is a thin doc) | none | alive, commit 2026-04-01 | No — content is trivially thin (CLI wrapper), nothing to launder |
| anthropics/knowledge-work-plugins | Apache-2.0 (root + per-plugin copy, byte-identical) | N/A | plugin.json exists, no separate license field | alive, commit same-day (2026-08-02) | No — first-party Anthropic content, Apache-2.0 straightforward |
| anthropics/skills | (not re-verified this run — no relevant content) | — | — | — | N/A (no relevant content) |
| firecrawl/skills | ISC, Firecrawl, 2026 | plugin.json declares `"license": "ISC"` — consistent | none | alive, commit 2026-06-16 | No — thin first-party dev-tooling, false positive anyway |
| firecrawl/firecrawl-workflows | ISC, Firecrawl, 2026 | plugin.json declares `"license": "ISC"` — consistent | none | alive, commit 2026-06-19 | No — false positive anyway |

---

## Open items / seam flags for controller

- **Boundary call**: marketingskills' `signup`→`onboarding` handoff and `revops` naming "customer success" as an external system it connects to are both consistent with the charter's already-documented marketing/success seam at SIGNUP — no new seam question, just confirms existing evidence from a second angle.
- **Boundary call**: `customer-research` (marketingskills) vs `customer-research` (knowledge-work-plugins) — SAME NAME, different scope. Marketing's version mines VoC for positioning/copy; Anthropic's version looks up an answer for one ticket. success-skill should not assume name-collision means overlapping content; both are legitimately siblings, not duplicates, of a success-owned VoC-aggregation job that neither fully covers (neither skill does health-score-grade VoC *aggregation and trend* — both are single-instance/tactical).
