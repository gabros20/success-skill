# _raw-skills-registries.md — Channel A / Worker A3

Scope: registries, awesome-lists, skills.sh browse, and the ADJACENT/VENDOR pack sweep.
Method: `gh api` / `curl` against the GitHub REST API (raw README + git-trees, contents API to
confirm files EXIST, not just that a README links them), WebFetch for skills.sh, `npx skills find`
for terms not run by the lead. All repo metadata (stars, license, pushed_at, archived) pulled live
2026-08-02. Raw npx output: `research/_raw/skills-find-a3-raw.txt` (415 lines, do not re-dump).

---

## Job 1 — registries and lists

### 1a. skills.sh browse (WebFetch, 2026-08-02)
URL: https://skills.sh/
- Nav: Browse (All/Trending/Hot/Official/Security audits), Topics (React, Next.js, Design & UI,
  Mobile, Agent workflows, Databases, Testing, Marketing), Agents, Docs, Project.
- **No customer-success, support, retention, or churn category or topic tab exists.** Marketing is
  the closest adjacent topic tab; nothing customer-ops-specific.
- 8-week leaderboard top 5: find-skills (vercel-labs/skills, 2.8M), frontend-design
  (anthropics/skills, 731.9K), grill-me / grill-with-docs (mattpocock/skills, 729.0K/618.5K),
  agent-browser (vercel-labs/agent-browser, 612.7K). None CS-related — confirms dev-tooling
  dominates the platform's own trending surface.

### 1b. `npx skills find` on the 18 uncovered terms
Full output: `research/_raw/skills-find-a3-raw.txt`. Highlights (install counts are skills.sh
install counts, not GitHub stars):

- **`escalation`**: `anthropics/knowledge-work-plugins@customer-escalation` (2.2K),
  `anthropics/knowledge-work-plugins@escalation` (169), `anthropics/claude-for-legal@escalation-flagger`
  (384), `louisblythe/salesskills@negative-sentiment-de-escalation` (192). → led to the **major find**
  below (§Job1c).
- **`customer education` / `user documentation` / `docs site`**: dominated by generic doc-generator
  and dev-docs-site skills (rspress, mkdocs, remotion docs, azure-site-recovery docs) — **zero**
  customer-education-specific hits. Confirms this sub-area is genuinely uncovered territory.
- **`community management`**: all social/marketing-community skills (xiaohongshu, "community
  manager" for marketing ops) — none framed as customer-retention community (matches marketing's
  acquisition-vs-retention split noted in the charter).
- **`customer advocacy` / `upsell` / `expansion revenue`**: `nexscope-ai/ecommerce-skills@shopify-upsell-cross-sell`
  (540), `deanpeters/product-manager-skills@saas-revenue-growth-metrics` (1.9K — see Job 2),
  `ncklrs/startup-os-skills@renewal-manager` (124), `ncklrs/startup-os-skills@qbr-facilitator` (125).
  `ncklrs/startup-os-skills` recurs across renewal/QBR/customer-lifecycle — worth a follow-up read if
  another worker hasn't covered it (I did not deep-read it; flagging for lead).
- **`QBR` / `account management`**: `anthropics/knowledge-work-plugins@quarterly-review` (1K).
- **`success playbook`**: `absolutelyskilled/absolutelyskilled@customer-success-playbook` (130).
- **`support automation` / `AI support agent` / `chatbot support`**: `googleworkspace/cli@persona-customer-support`
  (24.3K installs — see Job 2, this is a thin CLI persona, not a strategy pack), 
  `membranedev/application-skills@chatbot-builder` (225), `readdle/spark-cli-skills@spark-persona-support-agent` (107).
- **`csat` / `customer journey`**: `phuryn/pm-skills@customer-journey-map` (2K),
  `deanpeters/product-manager-skills@customer-journey-map` (1.9K, CC-BY-NC-SA — see Job 2 license flag).

### 1c. MAJOR FIND via `escalation` sweep: anthropics/knowledge-work-plugins has a full "Customer Support" plugin
`gh api repos/anthropics/knowledge-work-plugins` → 23,246 stars, Apache-2.0, pushed 2026-08-02
(today), not archived. Tree contains `customer-support/` — a self-contained plugin with its **own**
inner `customer-support/LICENSE` (Apache-2.0, verified — rule 3c: per-skill licenses exist inside
repos, checked and it matches repo license here) and 5 skills:
`customer-escalation`, `customer-research`, `draft-response`, `kb-article`, `ticket-triage`.

Verbatim from `customer-support/README.md`:
> "A customer support plugin primarily designed for Cowork, Anthropic's agentic desktop application —
> though it also works in Claude Code. Provides ticket triage, escalation management, response
> drafting, customer research, and knowledge base authoring for support teams."

Commands: `/triage`, `/research`, `/draft-response`, `/escalate`, `/kb-article`. This is the
**at-scale official incumbent** the charter asked about — but it is entirely **tactical/operational**
(day-to-day support-agent copilot for triage/response/escalation/KB drafting), with **zero** coverage
of onboarding, health scoring, VoC, renewals, or expansion. This directly supports wedge hypothesis
#4 (integration) and partially validates #1 (the strategic/process layer above ticket-handling is
undercovered even by Anthropic's own official pack).

Source: https://github.com/anthropics/knowledge-work-plugins/tree/main/customer-support
(`customer-support/skills/*/SKILL.md`, `customer-support/README.md`, `customer-support/LICENSE`)

Note: `w95/awesome-claude-corporate-skills`'s "11-customer-success" folder explicitly attributes
`ticket-triage`, `escalation`, `customer-research`, `response-drafting`, `knowledge-management`,
`slack-messaging`, `slack-search` to "Anthropic KWP" — i.e. it's a repackaging of this same
anthropics/knowledge-work-plugins content (confirms KWP = Knowledge Work Plugins, this repo).

### 1d. Awesome-lists sweep (all fetched + verified live, not trusted from README alone)

| List | Stars | License | CS/support entries | Verification note |
|---|---|---|---|---|
| ComposioHQ/awesome-claude-skills | 71,597 | **none** (no LICENSE file, GitHub API confirms) | README's "Support & Helpdesk" section lists Freshdesk/Freshservice/Help Scout/Zendesk **Automation**, plus Intercom Automation under a different section | **DEAD LINKS — false positive.** `gh api contents/freshdesk-automation` (and freshservice/helpdesk/zendesk/intercom/pagerduty/shopify/square/stripe-automation) all return `"message": "Not Found"` against the repo root. The repo's actual root dirs (verified via contents API) are generic dev/marketing skills (artifacts-builder, brand-guidelines, changelog-generator, mcp-builder, etc.) — none of the per-app "Automation" skills the README advertises exist in-repo. These are almost certainly auto-generated marketing copy pointing at Composio's [1000+ app toolkit](https://composio.dev/toolkits) (their generic `connect-apps` skill installs a plugin that dynamically wires ANY of 1000+ apps — there's no static Freshdesk/Zendesk/Intercom skill file). **Do not cite this list's Support & Helpdesk section as real skills.**
| composio-community/awesome-codex-skills | 15,544 | none | `support-ticket-triage/` — "Triage customer support tickets with categories, priority, next actions, and draft replies." | Real generic listing, single entry, not vendor-specific.
| w95/awesome-claude-corporate-skills | 132 | MIT | `11-customer-success/` — 10 skills (qbr-builder, churn-analysis, onboarding-playbook = "Custom"; ticket-triage, escalation, customer-research, response-drafting, knowledge-management, slack-messaging, slack-search = "Anthropic KWP") | **Verified real** — all 10 dirs exist via contents API. Custom-authored churn-analysis (516 lines) contains unsourced folklore numbers, e.g. verbatim: *"2.5% monthly churn = 30% annual churn... This is high for SaaS (1-2% monthly is typical)"* and voluntary-churn "Typical Rate: 60-70% of total churn" — no citation for either. Flag per charter's falsification-strip: figure-class hit.
| seb1n/awesome-ai-agent-skills | 141 | MIT | `customer-success/` folder — 5 skills: churn-analysis, customer-feedback-analysis, knowledge-base-article-writing, onboarding-playbook-creation, ticket-triage | README confirms via raw fetch (real folder structure, not verified file-by-file beyond README but README is internally consistent with repo structure elsewhere).
| Aradotso/trending-skills | 69 | none | **zero** CS/support entries | Confirmed empty for this topic.

### 1e. Other marketplaces/registries found (beyond skills.sh)
- **claudedirectory.org**, **claudeskillhub.com** (`/categories/customer-success-support`),
  **awesomeskill.ai** (`/tag/customer-success`), **claudskills.com**, **claudemarketplaces.com**,
  **mcpmarket.com/tools/skills**, **skillmarketplace.ai**, **skillsmp.com**, **LobeHub**
  (lobehub.com/skills), **Agensi** (agensi.io/skills) — all are third-party SEO/directory sites that
  mirror GitHub skill listings (not independent registries with their own hosted content). None is an
  "official Anthropic plugin marketplace" beyond `claude plugins add` / `anthropics/skills`. I did not
  deep-crawl each (low signal beyond what GitHub search already surfaces) — flagging existence only,
  per the job's ask to "record URL + what's there."
- No dedicated Smithery/ClaudeLog CS-specific presence found in this sweep.

---

## Job 2 — Adjacent/Vendor packs (all cloned/fetched shallow, LICENSE opened per rule 3)

| Pack | Repo stars | LICENSE (opened directly) | Skill verified? | Notes |
|---|---|---|---|---|
| hubspot/agent-cli-skills@customer-retention | 18 | Apache-2.0 | Yes, 118 lines | **Real vendor skill.** CRM-ops focused: finds inactive/at-risk customers via HubSpot filter expressions, flags past-due subscriptions, bulk-creates follow-up tasks. Explicit "Known gaps" section: *"No native churn-score / health-score property — track via a custom property. No Lists API, no sequences/cadences API — re-engagement enrollment is not CLI-available."* This is CLI-automation, not a health-score model or retention strategy — success owns the strategy layer this leaves blank.
| refoundai/lenny-skills@retention-engagement | 1,209 | MIT | Yes, 76 lines + `references/guest-insights.md` | Practitioner-canon, quote-attributed (Albert Cheng, Crystal W, Dan Hockenmaier, Jackson Shuttleworth/Duolingo streaks, Jason Cohen, Sarah Tavel — "50 sourced insights from 11 guests" of Lenny's Podcast). Evidence grade: **practitioner-report with named attribution** — better than folklore, still not measured-with-method. **Licensing gotcha (rule 3e, thin-license-on-thick-IP): the MIT license covers RefoundAI's compilation/repo, not the underlying IP of the podcast guests' quoted words** — any lift must cite the original speaker/episode, never "per lenny-skills."
| deanpeters/Product-Manager-Skills@voice-of-customer-miner (142) / @saas-revenue-growth-metrics (1.9K) | 6,192 | **CC BY-NC-SA 4.0** (GitHub API reported ambiguous `"other"/NOASSERTION` — opening the actual `LICENSE` file was required to find this, exactly the rule-3a warning) | Both real, well-built (voc-miner has a 3-question budget + Fact/Inference/Assumption discipline; saas-revenue-growth-metrics has 642 lines of MRR/ARR/NRR/GRR/ACV/ARPA formula + benchmark tables) | **NonCommercial clause — cannot be lifted for a commercially-distributed skill pack without violating NC.** Cite only, do not adapt phrasing/structure. Flag to controller: this is the single most content-rich adjacent pack found and it's the one we're most restricted from touching.
| wondelai/skills@improve-retention | 1,816 | MIT | Yes, 235 lines | Genuinely academic grounding: Fogg Behavior Model (B=MAP), attributed to BJ Fogg by name and quote, six-factor "Ability Chain." Best evidence-grade of the adjacent packs — a real citable framework, not vendor folklore. Growth-adjacent (activation/onboarding-friction), not success-core, but citable methodology for our onboarding/adoption references.
| kostja94/marketing-skills@retention-strategy (actual path: `skills/strategies/launch/retention/SKILL.md`) | 809 | MIT | Yes, 78 lines | **Falsification-strip catch — verbatim in the wild:** *"Acquiring new customers costs 5–25× more than retaining; 5% retention improvement can increase profitability 25–95%."* Both never-ship candidate figures appear together, unsourced, in a real shipped skill. Also unsourced: "Voluntary 60–80% / Involuntary 20–40%" churn-type split, "Proactive 60–80% vs Reactive 15–20%" conversion, "Loyalty programs: 5–15 percentage point retention lift." Strong evidence the folklore is load-bearing in the ecosystem — worth citing in success's flagship as a concrete "here's the folklore, here's why it's untraceable" example.
| twilio/ai@twilio-customer-support-architect | 26 (whole repo) | MIT | Yes, 199 lines | Real, but it's a **contact-center infrastructure decision tree** (IVR vs Studio vs TaskRouter vs Flex, self-service ladder, channel mix) — an architecture-advisor for support tooling, not support process/policy design. Adjacent-tooling, not success-core.
| customware-ai/skills@customware-support-widget | 2 | MIT | Yes, 92 lines | **Not a CS-process skill** — it's a frontend dev-integration skill for embedding Customware's own `<customware-chat>` web component into a specific React Router SPA template. Frontend/dev-tooling false-positive-adjacent; belongs nowhere near success's territory (frontend's, if anywhere).
| okx/onchainos-skills@okx-ai-support | 315 | **No LICENSE file at all** (API + root contents both confirm absence — cite only) | **False positive — does not exist.** The named skill "okx-ai-support" is not in the repo. `okx-ai` (merged from okx-agent-identity/task/watch/chat) is agent-economy/crypto-task-marketplace tooling (ERC-8004 identity, task marketplace, agent-to-agent chat) — nothing to do with customer support despite the name pattern. Confirmed via full SKILL.md read + references/ listing (24 files, all identity/task/watch/chat, zero support content).
| shopify/shopify-ai-toolkit@shopify-onboarding-merchant (5.4K) / @shopify-onboarding-dev (6.1K) | 484 | MIT | Both real, verified | **@shopify-onboarding-dev is a clean false positive** — explicitly "NOT for merchants managing stores," developer/theme/app scaffolding, out of success's territory entirely. **@shopify-onboarding-merchant is a borderline/partial false positive**: verbatim scope line — *"Preview-store creation for brand-new merchants... Set up and connect a Shopify store... This is for store owners — not developers."* It's a first-store-creation / signup-to-live-store CLI flow (bash-driven, telemetry-hooked), i.e. **PLG activation/signup tooling, not post-signup adoption/education content**. Sits on the marketing/success seam the charter already drew (pre-signup vs. post-signup) but skews toward the signup side, not ongoing success.

### Official support-tool vendor search (explicit ask: does Intercom/Zendesk/Front/HelpScout/Freshdesk ship an official pack?)
- **Intercom — yes, an official org repo exists**: `intercom/2x-skills` (222 stars, MIT, active,
  pushed 2026-07-09). But verified via full git-tree: all 9 SKILL.md files are **internal engineering
  tooling** (cc-cost-analysis, permissions-analyzer, tool-misses, thermo-nuclear-code-review,
  attach-github-assets, create-pr, secure-github-actions, skill-review, fix-flaky-tests) — repo's own
  description: *"claude skills we think are generic enough to be useful to everyone."* **Zero
  customer-support content.** Intercom-the-vendor ships dev-tooling skills, not a support-product
  skill pack.
- **Zendesk**: no official `zendesk/*` org repo found. Community packs only —
  `andmarios/zendesk-skill` (CLI+MCP, community), `davepoon/buildwithclaude` "zendesk-automation"
  (community aggregator), `mcpmarket.com` listing (third-party directory, not source).
- **Front, Help Scout, Freshdesk**: no official vendor repos found. Help Scout appears only via
  community packs (`membranedev/application-skills`, `OneWave-AI/claude-skills/scout`). No first-party
  Front skill found at all.
- **Conclusion: no support-tool vendor ships a genuine customer-success/support-strategy skill under
  their own org.** The one vendor with an official repo (Intercom) used it for their own engineering
  practices, not their product.

### Bonus: two other candidate "at-scale" packs worth the lead's attention
- `claude-office-skills/skills@customer-success` (352 stars whole repo, 3.7K installs, MIT, single
  601-line SKILL.md): covers onboarding, health scoring, QBRs, expansion, retention in one file.
  Health-score formula is verbatim unsourced: `total: (engagement × 0.4) + (relationship × 0.25) +
  (financial × 0.2) + (sentiment × 0.15)` — textbook unvalidated-weighting folklore, direct support
  for wedge hypothesis #2.
- `googleworkspace/cli@persona-customer-support` (24.3K installs — the single highest count I found
  under any CS-adjacent term) is **not** a strategy pack: it's a 39-line "persona" wrapper telling the
  agent to use `gws gmail +triage`, `gws workflow +email-to-task` etc. — a thin persona on top of a
  general-purpose Google Workspace CLI (30K-star parent repo). High install count reflects the parent
  tool's popularity, not CS-specific demand — flag so the lead doesn't over-weight this number.

---

## Sources index (all fetched/verified live 2026-08-02)
- https://skills.sh/ (WebFetch)
- research/_raw/skills-find-a3-raw.txt (18-term npx skills find sweep, raw)
- https://github.com/anthropics/knowledge-work-plugins/tree/main/customer-support
- https://github.com/w95/awesome-claude-corporate-skills (README + 11-customer-success/*)
- https://github.com/ComposioHQ/awesome-claude-skills (README + contents-API dead-link check)
- https://github.com/composio-community/awesome-codex-skills
- https://github.com/seb1n/awesome-ai-agent-skills
- https://github.com/Aradotso/trending-skills
- https://github.com/HubSpot/agent-cli-skills/blob/main/customer-retention/SKILL.md
- https://github.com/RefoundAI/lenny-skills/blob/main/skills/retention-engagement/SKILL.md
- https://github.com/deanpeters/Product-Manager-Skills (LICENSE, voice-of-customer-miner,
  saas-revenue-growth-metrics)
- https://github.com/wondelai/skills/blob/main/improve-retention/SKILL.md
- https://github.com/kostja94/marketing-skills/blob/main/skills/strategies/launch/retention/SKILL.md
- https://github.com/twilio/ai/blob/main/skills/twilio/twilio-customer-support-architect/SKILL.md
- https://github.com/customware-ai/skills/blob/main/skills/customware-support-widget/SKILL.md
- https://github.com/okx/onchainos-skills (skills/okx-ai — okx-ai-support confirmed non-existent)
- https://github.com/Shopify/Shopify-AI-Toolkit/blob/main/skills/shopify-onboarding-merchant/SKILL.md
- https://github.com/Shopify/Shopify-AI-Toolkit/blob/main/skills/shopify-onboarding-dev/SKILL.md
- https://github.com/intercom/2x-skills
- https://github.com/claude-office-skills/skills/blob/main/customer-success/SKILL.md
- https://github.com/googleworkspace/cli/blob/main/skills/persona-customer-support/SKILL.md
