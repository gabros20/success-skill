# Site + Remotion hero — build report (success-skill, v0.1.0)

Agent: SITE BUILDER (orange identity). Scope: `site/index.html` + `remotion/`. Not deployed —
controller deploys.

## Status: BUILT

## What changed

- **`site/index.html`** — full rewrite from the TODO scaffold. Adapted growth-skill's shipped
  component library (post hero-rewrite state) to success's actual shape: a **gate before a router**,
  not a plain faceted router. Sections: hero (gate+router hero-fallback card) · mission (owns/hands
  off) · the existence gate (dedicated section — arvidkahl test, 3-verdict table, contested
  pricing-first correction) · the ten primary jobs (full table, real reference links) · three
  surfaces + one additive agentic overlay · flagship (health-and-risk-signals: score-vs-prediction,
  "not published never not measured," the Observability Question, four-study convergence, honest ML
  ceiling) · what's distinct (fragmented-not-empty framing, never-ship figures) · the ten universal
  invariants · artifacts (7-step core workflow + 4 self-testing assets + eval suites) · handoff
  seams (emits block + marketing/growth/ai downstream + the three originated rows) · family strip
  (all 12 shipped siblings incl. growth, only sales marked unshipped) · start here (real install
  commands, real trigger phrases).
- **`remotion/src/HeroAnimation.tsx`** — full rewrite from the theme-fade placeholder. Five-scene,
  reader-paced (~47s, 1420 frames @ 30fps) composition: **gate → router → flagship → observability →
  handoff**. Orange palette from `theme.ts` (unchanged, already correct).
- **`remotion/src/Root.tsx`** — `durationInFrames` updated 840 → 1420 to match the new timeline.
- **`site/assets/`** — rendered: `hero-light.mp4` (3.9 MB), `hero-dark.mp4` (3.6 MB),
  `hero-light-poster.png` / `hero-dark-poster.png` (poster at frame 780 — the flagship's headline
  correction, self-explanatory on its own).

## Hero copy (verbatim, for register check)

**Eyebrow:** `an agent skill · a gate before the playbook — onboarding, support, health scores, renewals`

**H1:** `/success`

**Lede:**
> **success** keeps the customers you already have. Ask it to plan onboarding and it writes the
> adoption program, not just an in-app checklist; ask it whether your health score is trustworthy
> and it checks the math before it trusts the color; ask whether you even need a customer-success
> function yet and it answers honestly — often "not yet," with a named pointer to whatever already
> covers the gap. Onboarding, help content, support process, AI-support rules, renewals, and the
> customer's side of an incident — 15 references and four self-testing calculators behind one
> router. What makes it different: most churn-and-health advice repeats a number nobody ever
> actually measured. This pack names which of those numbers have never been published anywhere —
> and builds your plan without needing one.

**Terminal example:**
> `/success` our beta customer's health score just flipped from green to red — is that signal or noise?

No banned jargon (wedge/null-result/observability-question-as-jargon/figure-class/posterior/incumbent/seam)
appears in the hero (eyebrow, H1, lede, terminal, hosts). "The Observability Question" is used only
inside the flagship body section as a defined, capitalized proper term (matching growth's own
"Ambition Tax" precedent), never in the hero.

## Verification performed

- `grep -c TODO site/index.html` → 0.
- Tag-balance check (section/div/table/header/footer open vs. close) → all matched.
- All internal `#anchor` links resolve to a defined `id` (76 anchors checked, 0 broken).
- Served via `python3 -m http.server`, curled `index.html` and all four rendered assets
  (`hero-{light,dark}.mp4`, `hero-{light,dark}-poster.png`) → all HTTP 200, non-trivial sizes.
- `npx tsc --noEmit` on `remotion/` → clean, no errors.
- Rendered stills at representative frames from all 5 scenes (light) plus 2 scenes (dark) and
  visually reviewed each — all legible, correctly themed, no clipping or premature fades.
- Full render completed for both `hero-light.mp4` and `hero-dark.mp4` (h264, crf 23).

## Not touched (outside assigned scope)

`site/llms.txt`, `site/og-source.html`, and `site/sitemap.xml` still carry TODOs (checked, not
edited) — my directive scoped this build to `site/index.html` and `remotion/` only. Flagging in case
no other agent owns them before deploy; the ship checklist in `site/README.md` requires them
TODO-free.

## Issues

None blocking. Video runs long by short-form standards (~47s) but matches the family's own pacing
rule (reader-first: content in → hold → fade out) and growth's precedent (~57s) — a faster cut would
fail the read-aloud test on the flagship's correction beat.
