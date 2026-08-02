# Storefront report — success-skill v0.1.0

Writer: storefront agent. Scope: README.md, docs/, AGENTS.md, CLAUDE.md, TEMPLATE-CHECKLIST.md
removal. Did not touch skills/, evals/, scripts/, research/, .orchestrate/, site/, remotion/.

## Files rewritten

- `README.md` — full rewrite from the template stub. Mission/boundary, "What makes this pack
  different" (fragmentation of incumbents, the Observability Question, "not published, never not
  measured", the never-ship retention-folklore strip), install, examples, faceted-router job/surface
  tables (10 jobs, 4 surfaces incl. agentic overlay, matching skills/success/SKILL.md), outputs,
  Digital Product lifecycle paragraph (Improve stage, pairs with growth), family table (13 shipped
  packs; sibling links point at each pack's live *.vercel.app site per family-rule instructions,
  curl-verified 200 for all 13 — including designskill.vercel.app, no hyphen, and
  frontendengskill.vercel.app/backendengskill.vercel.app/aiengskill.vercel.app/growthskill.vercel.app
  overrides), reference/asset library, repo layout, docs & release links, license.
- `docs/usage.md` — replaced all TODOs: activation triggers/anti-triggers, mission/boundary, 7-step
  workflow, full route-by-job table (10 refs + 4 assets), outputs/completion table.
- `docs/recipes.md` — replaced the single TODO scaffold with 6 full recipes (existence gate,
  onboarding program vs. flow, health-score audit, AI escalation policy, SLA-from-capacity, NRR
  without blending definitions, churn-save motion), each with route/citation detail pulled from the
  actual shipped references (verified against when-success-applies.md, ai-support-policy.md,
  renewals-and-expansion.md, support-process-design.md).
- `docs/installation.md` — replaced the one remaining TODO (prerequisites line) with success's
  actual tool-agnostic posture, matching sibling phrasing.
- `AGENTS.md` — full rewrite: ownership boundary (non-negotiable) against all 8 sibling seams, the
  10 universal invariants from SKILL.md restated as numbered agent rules, required behavior section.
- `CLAUDE.md` — rewritten pointer file naming the four highest-signal invariants.
- `docs/README.md` — left as-is; already generic/correct, matches sibling convention.
- `CONTRIBUTING.md` — left as-is; byte-identical to operate-skill's shipped version, no
  skill-specific customization needed there per family convention.

## Placeholders removed

- Deleted `TEMPLATE-CHECKLIST.md` (release checklist, no longer needed post-release).
- Grepped repo-wide for `__SKILL`, `TODO`, `<skill>` outside site/remotion/research/skills/evals/
  scripts/.orchestrate/.git — zero residual hits in any file this agent owns. Remaining hits are all
  inside excluded directories (research/skills-ecosystem-report.md, site/README.md,
  .orchestrate/reports/*) and are out of scope by the task's own instruction.

## check-sync state

`scripts/check-sync` — OK (package, routes, references, metadata, eval fixtures, and scripts
validated) both before and after this pass. Pre-existing WARNs unrelated to storefront changes:
SKILL.md and 4 references exceed the review token threshold — not this agent's scope.
