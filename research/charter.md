# success-skill research charter

Date: 2026-08-02 · Controller: main session · Run: nested hierarchical research (5 opus channels × 2–3 sonnet workers)
Repo: this file lives in the AUTHORITATIVE research home (`success-skill/research/`). Every agent writes here.

## Mission (canonical, §4.14 of digital-product-skill/docs/product-lifecycle-skill-packs-exploration.md)

> "Help customers adopt the product, realize value, receive support, renew, and expand."

Tier: **Improve** (pairs with growth — growth learns what works, success does the work and holds the
relationship). 13th of 14 family packs. Family = faceted-router skills: thin SKILL.md (jobs × surfaces)
+ on-demand references, description ≤600 chars with boundary arrows, NO numbered invariants.

**Canonical Includes (12):** customer onboarding · implementation/adoption plans · education and
enablement · help content + knowledge-base strategy · support process design · customer health and
risk signals · voice-of-customer collection · escalation · churn prevention · renewals · expansion
and advocacy · customer-to-product feedback loops.
**Produces:** onboarding plan, success playbook, education materials, support taxonomy, KB
requirements, health-score model, escalation paths, renewal workflow, VoC reports.
**Code policy:** operational artifacts/config/content/lightweight workflows; product changes →
product + build packs; substantial workflows → automation.

**The §1033 conditional (shapes everything):** success is first-class for B2B/high-touch; "for simple
self-serve consumer products, /growth, /marketing, and /operate may cover most post-purchase needs
until a distinct success workflow emerges." Our default reader IS the solo self-serve builder — the
pack must honestly teach WHEN it applies, not assume an enterprise CS team.

## The axis

**success is the family's relationship owner**: every touchpoint whose purpose is that an *existing*
customer succeeds — teaching (onboarding education, docs, enablement), helping (support process,
escalation), watching (health/risk signals, VoC), keeping (churn-save execution, renewals, expansion).
Contrasts: marketing persuades prospects / success enables customers; growth learns what works /
success executes and holds the relationship; operate keeps the SYSTEM healthy / success keeps the
CUSTOMER healthy ("operate states fact, impact, and timing; it does not manage the relationship").

## Binding seam contracts already shipped by siblings (verify from disk — channel E owns this)

- **marketing (richest, 8 files):** seam at SIGNUP. Pre-signup nurture/newsletter = marketing;
  post-signup activation, onboarding education, retention comms, in-product activation nudges →
  success (SKILL.md:10,108,118; surface-selfserve-saas.md:94,121; lifecycle-and-email.md:14,136).
  App-review RESPONSES = support workflow → success (app-store-optimization.md:18); ASO listing stays
  marketing. Community splits by acquisition-vs-retention intent (organic-social-and-community.md:136).
  handoff.md:43: marketing hands the acquisition narrative "for onboarding continuity"; receives
  retention/churn signal back.
- **growth (4 files, drawn 2026-08-02, provisional):** "growth owns retention EXPERIMENTATION — does
  a resurrection nudge work; success owns retention EXECUTION — sending the message a growth test
  validated" (handoff.md:43; SKILL.md:10,113,121; growth-model-and-loops.md:71-74). Growth keeps
  activation, referral design/math, retention experimentation.
- **product:** cedes "adoption to success" (SKILL.md:28); surface-app-saas.md:45 routes onboarding
  and support to success. Doc evidence map: "Adoption, support, satisfaction, and churn evidence → /success".
- **operate (3 files):** customer-facing incident comms, per-account outreach, decommissioning
  outreach → product/success (SKILL.md:90; incident-response.md:159; decommissioning.md:186).
- **automation:** authoring business rules / customer-facing comms → commercial packs incl. success
  (SKILL.md:104; process-capture.md:15,163).
- **design/data/quality/ai/frontend/backend/architecture:** ZERO cessions on disk (verified by grep;
  raw hits were "success state" UI false positives). Success draws those seams from its own side.
- **sales (UNBUILT):** renewals/expansion boundary — success owns renewal workflow + expansion
  SIGNALS; sales owns the expansion SALE in sales-assisted motions. Third provisional unbuilt seam.

## Wedge hypotheses (research must confirm, refute, or replace — growth's wedge pivoted twice; that's fine)

1. **The CS canon is enterprise-CSM-team literature** (Gainsight school, CSM ratios, QBRs, health
   scores); the honest solo/self-serve version is docs + automation + product signals — under-taught.
2. **Health scores are largely unvalidated vendor folklore** — flagship candidate:
   health-and-risk-signals ("what a health score can honestly predict"), heir of marketing's
   attribution and growth's feasibility flagships.
3. **The AI-support-agent era (2024–26) is under-canonized**: deflection-rate honesty, escalation
   policy, bot boundaries. Family uniquely has `ai` for mechanics; success owns POLICY.
4. **Integration wedge**: nobody unifies onboarding + support + health + renewal with honest seams.

## Falsification-strip / never-ship candidates (trace to PRIMARY source; a disclaimed figure is still a figure)

- "It costs 5–25× more to acquire than retain" — Reichheld-adjacent, likely untraceable. Trace or kill.
- "5% retention increase → 25–95% profit increase" — Reichheld/Sasser HBR 1990; growth already
  flagged the trace as open. Find the original method + scope limits.
- NPS claims ("best predictor of growth") — Kohavi 7,600-response power point + Hiten Shah critique
  already shipped in growth's corpus; find the ACADEMIC critiques (Keiningham et al replication failure).
- Health-score accuracy claims, "80% of revenue from 20% of customers", "96% of unhappy customers
  don't complain", CSAT/CES benchmark tables, "10× cheaper to deflect" — trace every figure met.
- Rule learned twice: the never-ship LIST is not the RULE — flag figure-CLASS, not just known strings.

## Hard research rules (all channels)

1. **Nothing lost**: every worker writes its own doc in `research/_raw/` (`_raw-<channel>-<topic>.md`)
   with FULL source links (URL, repo@commit, tweet ID/permalink, skill path). Channel leads write
   `research/<channel>-report.md` synthesizing worker files — NEVER contradicting a _raw file without
   a dated correction note at source.
2. **Load-bearing numbers**: never trust WebFetch's summarizer for magnitudes (it fabricated CUPED
   20-40% and a model table in prior runs). Download the PDF/page and read the text. curl with a
   Chrome UA beats 403s (ftc.gov, ico.org.uk opened that way). Crawl4AI is BROKEN in this env
   (litellm ImportError) — do not debug it; use WebFetch/curl.
3. **Licensing, 5 clauses** (for anything we might lift): (a) open the LICENSE file itself — the
   GitHub license API lied 7+ times; (b) read package-ecosystem manifests (DESCRIPTION,
   package.json, pyproject.toml) — GeoLift declared MIT + GPL(>=2) simultaneously; (c) per-skill
   licenses exist inside repos (anthropics/skills); (d) archived:false ≠ alive, no-license = cite
   only; (e) thin-license-on-thick-IP — an MIT repo compiling a book's frameworks does not license
   the book; cite the original author, never the compiler's phrasing.
4. **xrelay operating point**: max 3 concurrent procs session-wide (4 degrades wall-clock);
   `archive user`/`user-posts` UNWRAP RETWEETS — split on `retweetedBy` or you misattribute
   timelines; 15–20s backoff recovers timeouts; authority routing (`from:<handle>`) beats topical
   search where vendors dominate the topic terms.
5. **Vendor-density warning**: CS/support literature is Gainsight/Intercom/Zendesk/HelpScout content
   marketing. Grade every claim: measured-with-method > practitioner-report > vendor-folklore.
   The "Customer Success" book (Mehta/Steinman/Murphy) is Gainsight-authored — treat as canon-with-
   interest, not evidence.
6. **Boundary calls**: when a finding straddles a seam (growth/marketing/operate/sales/product),
   record it WITH the seam question attached — the controller adjudicates; do not silently assign.

## Channel assignments

- **A · skills-ecosystem** (find-skills + skill registries): existing CS/support/onboarding/
  retention/churn skills & packs; the incumbent question (is there an at-scale CS pack like
  marketing's 42.5k★ incumbent?); what they cover, what they miss, licenses.
- **B · x-practitioners** (x-relay): CS/support/retention practitioners via authority routing;
  AI-support-agent discourse 2024–26; solo-founder support reality; health-score skepticism.
- **C · github** (github-relay + gh): helpdesk/KB/health-score/churn-model repos; open-source
  support stacks (Chatwoot, Zammad, FreeScout, Papercups…); docs-as-deflection tooling; AI support
  agent frameworks; licenses per rule 3.
- **D · web-research** (WebSearch/WebFetch/curl): the CS canon and its critics; churn/health-score
  evidence vs folklore; the falsification strips above; support-ops literature (SLAs, taxonomies,
  QA rubrics like Klaus/MaestroQA); onboarding/adoption evidence; renewal/expansion mechanics
  (NRR/GRR definitions with primary sources); VoC methods.
- **E · webdesign-lift + family seam audit**: full read of ~/.claude/skills/webdesign/ — extract
  EVERYTHING success-relevant (nothing left behind; the old skill will be abandoned); verify the
  seam inventory above from disk across all 12 shipped packs; deliver the lift-list with
  per-item disposition (lift / rewrite / cite / belongs-to-sibling).

## Output contract recap

Worker: `research/_raw/_raw-<channel>-<topic>.md`, every claim sourced. Lead:
`research/<channel>-report.md` <2500 lines, dense synthesis + open questions + seam flags, linking
every _raw file. Controller synthesizes after all five reports land.
