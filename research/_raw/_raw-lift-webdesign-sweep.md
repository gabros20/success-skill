# Webdesign skill sweep — completeness audit for the success pack

Scope: exhaustive read of `/Users/tamas/.claude/skills/webdesign/` — SKILL.md + all 22
`references/*.md` files (3707 lines total, all read in full, none grepped-and-skipped).
Division of labour: `niche-and-vertical-design.md`, `persuasion-and-conversion.md`,
`trust-proof-and-structure.md`, `section-archetypes.md` are the channel lead's deep-read
files — they were still read here for completeness, but notes below are kept brief per
instruction; depth was spent on the other 19 files.

Verdict up front: **webdesign is a prospect-facing marketing/brand/build skill.** Its entire
subject is "get a visitor to notice, trust, and convert" — pre-purchase persuasion, visual
craft, and the frontend build that ships it. The success pack's territory (onboarding,
help/KB, support process, health/risk, VoC, escalation, churn, renewals, expansion,
feedback loops, existing-customer comms) is almost entirely **absent** from this skill. Only
a handful of generically-phrased UX/critique/copy principles happen to also apply to an
existing-customer surface; they are lifted below. There is no dedicated onboarding,
empty-state, help-center, support-workflow, health-score, or retention content anywhere in
the 23 files.

---

> **CORRECTION NOTE — added 2026-08-02 by channel lead E (`webdesign-lift-report.md`).**
> Three amendments to this file, all from disk-grep after it was written. The file's *findings*
> stand; what changes is their availability to `success`.
>
> 1. **Lift item #1 is NOT available to success — it is already shipped, three times.** The
>    "would a real user contact support over this?" P1 boundary test is live in
>    `quality-skill/skills/quality/references/defect-lifecycle.md:138`,
>    `quality-skill/skills/quality/assets/severity-map.md:51`,
>    `quality-skill/skills/quality/assets/release-gate-checklist.md:37`, and
>    `design-skill/skills/design/references/critique.md:78`. Disposition is corrected
>    **LIFT → SIBLING:quality (already lifted)**. Success may cite quality's test; it must not
>    re-ship it.
> 2. **Lift item #3 is likewise already lifted, by `design`.** The "More on writing in design"
>    doctrine survives near-verbatim at `design-skill/skills/design/references/content.md:31`,
>    and design went *further* than webdesign did: `content.md:45` already states **"Empty states
>    are onboarding moments in three beats: name what is empty, say why it matters, give one
>    button. New users spend more time in empty states than in any other state,"** and
>    `content.md:58` sets the rule **"| Onboarding | contextual, not a tutorial |"**. Disposition
>    corrected **REWRITE → SIBLING:design (already lifted, and extended)**.
> 3. **The file swept a stale copy.** `~/.claude/skills/webdesign/` is **v1.2.0**; the canonical
>    source repo at `/Users/tamas/Documents/Personal/Projects/webdesign/skills/webdesign/` is
>    **v1.3.2** (`git log`: `cce0fac fix(skill): exclude app dashboards/product UI from activation
>    (v1.3.2)`), and every reference file there is 20–30 lines longer. The lead diffed the two
>    copies for success-relevant additions: **the delta contains none** (the only success-term
>    lines added are a scope *narrowing* — v1.3.2's SKILL.md:9 now excludes "app dashboards and
>    product UI" and "growth planning"). The completeness statement below therefore holds against
>    **both** versions, and holds *more strongly* against v1.3.2.
>
> 4. **Lift item #4 (Zeigarnik) is also largely already shipped.** `design-skill/skills/design/
>    references/interaction.md:90` carries "**Zeigarnik:** show progress ('Step 2 of 3') on
>    multi-step tasks. **Peak-end:** engineer a delight peak and a strong close." The growth pack's
>    own prior extraction of this same skill
>    (`growth-skill/research/webdesign-growth-extraction.md:82`) already claimed the residue design
>    did *not* ship — the profile-completion meter and the engagement-farming pitfall — as growth's
>    activation/habit-ethics material. Disposition corrected **REWRITE → SIBLING:design + growth**.
> 5. **Context this file lacked: webdesign has been extracted twice before.** See
>    `marketing-skill/research/webdesign-extraction.md` (720 lines) and
>    `growth-skill/research/webdesign-growth-extraction.md` (501 lines). Growth's run records the
>    method that matters here (`:16–19`): cross-check every already-lifted claim against the
>    sibling's **actually-shipped** references, not against the prior run's disposition table —
>    *"This step changed four verdicts: the marketing table listed items as LIFT that did not
>    survive into the shipped pack."* Applying that test to this file's candidates plus the lead's
>    own, **eight of ten collapsed** as already-shipped. Full grep-verified table in
>    `webdesign-lift-report.md` §2.3.
>
> Item #2 (the undefined "help & documentation" heuristic) survives and is upgraded: it is a
> **grep-verified orphan** — zero hits for help-content ownership across all twelve shipped packs.
> Item #5 (the FAQ field shape) is unamended. The whole Part 2 completeness statement is unamended
> and its conclusion is strengthened, not weakened, by these corrections.

## Part 1 — the lift-list

### 1. The "would a real user contact support over this?" severity test

- **Source:** `references/design-critique.md:58`
- **Quote:** `- **P1** — the test: **"would a real user contact support over this?"** If yes, it's at least P1.`
- **Disposition:** LIFT
- **Why:** This is a direct, usable severity heuristic for triaging defects/friction by whether
  they generate a support contact — exactly the kind of test a success pack would want for
  scoring in-product friction against support-deflection goals. Usable near-verbatim as a
  triage rule in an escalation/support-process reference.

### 2. Nielsen's "help & documentation" heuristic (named but not built out)

- **Source:** `references/design-critique.md:14-17`
- **Quote:** `Score each heuristic 0 (broken) → 4 (exemplary): visibility of system status · match to the real\nworld · user control & freedom (undo/redo, escape hatches) · consistency & standards · error\nprevention · recognition over recall · flexibility & efficiency · aesthetic & minimalist design ·\nhelp users recognize/diagnose/recover from errors · help & documentation.`
- **Disposition:** REWRITE
- **Why:** "help & documentation" and "help users recognize/diagnose/recover from errors" are
  named as heuristics to score, but the file never says what good help content or error
  recovery actually looks like — that's an empty judgment slot a success pack's help-content
  and error-design guidance should fill; the label is reusable, the substance is not present
  here.

### 3. "More on writing in design" — copy/voice principles for empty states and errors

- **Source:** `references/frontend-design-principles.md:159-183`
- **Quote (the most success-relevant lines, 177-179):** `Treat failure and emptiness as moments for direction, not mood. Explain what went wrong and how to\nfix it, in the interface's voice rather than a person's. Errors don't apologize, and they are never\nvague about what happened. An empty screen is an invitation to act.`
- **Also quote (166-169):** `Write from the end user's side of the screen. Name things by what people control and recognize,\nnever by how the system is built. A person manages notifications, not webhook config. Describe what\nsomething does in plain terms rather than selling it. Being specific is always better than being\nclever.`
- **Disposition:** REWRITE
- **Why:** This is generic UI-copy doctrine written for a design system, not for an existing
  customer's in-app/help surfaces specifically — but "empty screen is an invitation to act" and
  the error-voice rule are directly the seed of empty-state/error-messaging guidance a success
  pack needs for onboarding empty-states, in-app education, and help-content voice. Needs
  rewriting to be framed around post-signup/existing-customer surfaces (the source frames it as
  general design-system copy, not success-specific).

### 4. Zeigarnik effect → progress bars / profile-completion meters (onboarding pattern)

- **Source:** `references/persuasion-and-conversion.md:44-45`
- **Quote:** `- **Zeigarnik** — unfinished tasks nag toward completion: progress bars ("Step 2 of 3"), profile-completion\n  meters. *Pitfall:* manufactured endless incompletion = engagement-farming.`
- **Disposition:** REWRITE
- **Why:** The device (progress/completion meters) is a real onboarding-checklist UI pattern
  success packs use for activation/adoption — but the source frames it purely as a
  pre-purchase conversion trick (Cialdini/cognitive-bias catalog for landing pages). Worth
  lifting the mechanism and rewriting it around post-signup onboarding-checklist design,
  including the pitfall (don't gamify incompletion — same caution applies to onboarding
  checklists that never resolve).

### 5. FAQ section content schema (one-liner — lead's file)

- **Source:** `references/section-archetypes.md:173`
- **Quote:** `` | `faq` | faq | `heading:string` · `items:list[ question:string*, answer:rich ]` | faq | ``
- **Disposition:** REWRITE (brief — channel lead owns this file)
- **Why:** A trivial question/answer content schema; reusable as a starting field-shape for a
  help-center/FAQ content model, but it's a one-line generic schema with no help-content
  strategy attached — noted for completeness, not elaborated since the lead reads this file
  directly.

### Items considered and rejected (not written up as lift-list entries)

- **Testimonials / case-study machinery** (`trust-proof-and-structure.md §3, §6`;
  `niche-and-vertical-design.md` throughout; `persuasion-and-conversion.md §1`;
  `section-archetypes.md:178`): every instance frames testimonials/case studies as
  **prospect-facing conversion proof** (named+photographed quotes next to a CTA/form, logo
  walls, case-study anatomy for a buyer's decision) — not existing-customer advocacy
  collection or an advocacy/reference program. **SIBLING:marketing** (and growth, which the
  system reminder says already did its own extraction from this skill). Not lifted in detail
  per the instruction to keep growth-owned items to one line.
- **E-E-A-T / SEO / IA (`trust-proof-and-structure.md §2, §4, §5`):** credibility and
  findability for a prospect evaluating a business before contact — **SIBLING:design /
  SIBLING:marketing**. Not success (pre-relationship, not post-purchase).
- **Cialdini/CCD/pricing psychology (`persuasion-and-conversion.md` whole file except the one
  Zeigarnik line above):** landing-page conversion mechanics — **SIBLING:marketing/growth**.
- **Vertical playbooks (`niche-and-vertical-design.md` whole file):** all structured around
  winning a *new* client's trust before they contact the business (architect/law/healthcare/
  SaaS demo-request funnels) — **SIBLING:design/marketing**. The B2B SaaS playbook's funnel
  ends at "demo request or trial signup," i.e. stops exactly where success's remit (onboarding
  an already-signed customer) begins — confirms no overlap rather than a miss.
- **Section-archetype catalog structure/IA methodology (`section-archetypes.md` main body,
  lines 1-170):** sitemap/content-modeling procedure for a marketing site build —
  **SIBLING:product/design**. Only the FAQ leaf field-shape (#5 above) touches success.

**Lift-list disposition counts:** LIFT: 1 · REWRITE: 4 · CITE: 0 · SIBLING (detailed): 0 ·
SIBLING (one-line, growth-owned testimonials/case-study/persuasion cluster): acknowledged
above, not itemized further.

---

## Part 2 — completeness statement (all 23 files)

| File | Lines | Success-relevant? | What it's actually about / owner |
|---|---|---|---|
| `SKILL.md` | 164 | No | Router for the whole webdesign skill (workflow arc, pick-by-job table, the 7 non-negotiable design laws). Pure design/frontend orchestration; no success content. Owner: **design**. |
| `references/anti-default-catalog.md` | 64 | No | Named 2026 "AI design tell" catalog (cream/sand OKLCH band, reflex-reject fonts, ghost-card CSS defects). Owner: **design**. |
| `references/color-and-rhythm.md` | 82 | No | Palette + section-rhythm CSS technique (OKLCH, light/dark alternation, duotone imagery). Owner: **design**. |
| `references/design-critique.md` | 96 | **Yes** (2 items lifted) | Scored Nielsen/cognitive-load/persona critique rubric + P0–P3 severity routing for design QA gates. Mostly generic UX-review methodology; owner **design/quality**, with the two support-adjacent lines lifted above. |
| `references/design-thinking.md` | 97 | No | How a designer composes a section and critiques a design (contrast/hierarchy/rhythm principles, "one bold move" doctrine). Owner: **design**. |
| `references/decoration.md` | 105 | No | Decorative CSS devices (SVG patterns, dividers, blobs, grain, cutout objects). Owner: **design**. |
| `references/trust-proof-and-structure.md` | 111 | No (lead's file; no new items beyond persuasion cluster already flagged) | Prospect-facing credibility/proof/IA/SEO structure (E-E-A-T, testimonial placement, case-study anatomy, semantic HTML/JSON-LD). Owner: **design/marketing**. |
| `references/typography.md` | 114 | No | Type-scale, fluid clamp(), display/kinetic typography CSS craft. Owner: **design/frontend**. |
| `references/tailwind-v4-theme.md` | 118 | No | Mapping DESIGN.md tokens onto Tailwind v4 `@theme` namespaces (spacing/container collision gotchas). Owner: **frontend**. |
| `references/SOURCES.md` | 124 | No | Provenance/citation index for the other reference files' techniques (external blog/doc links per file). Meta/bibliography file, not itself a content pack; no owner needed — it's an index, not a claim. |
| `references/motion-and-interaction.md` | 129 | No | Scroll-driven CSS/JS motion patterns (reveals, pinned scrollytelling, magnetic buttons, marquee). Owner: **design/frontend**. |
| `references/persuasion-and-conversion.md` | 139 | **Yes** (1 item lifted) | Cialdini principles, cognitive biases, Conversion-Centered Design, pricing psychology, dark-pattern ethics table — all for converting a *prospect*. One onboarding-relevant mechanism (Zeigarnik/progress meters) lifted; rest is **SIBLING:marketing/growth**. |
| `references/section-design-workflow.md` | 142 | No | The craft router: device map + working method + anti-boring checklist for building one section. Owner: **design**. |
| `references/experimental-and-creative.md` | 143 | No | Awwwards-tier WebGL/shader/particle/custom-cursor/View-Transitions techniques. Owner: **design/frontend**. |
| `references/design-direction.md` | 178 | No | How to author/lint/export a `DESIGN.md` design-system contract (the `design.md` CLI tool). Owner: **design**. |
| `references/frontend-design-principles.md` | 183 | **Yes** (1 item lifted) | The taste/point-of-view layer (register, anti-default process, restraint) plus a UX-copy section at the end. Overwhelmingly design direction-setting; owner **design**, with the copy-voice section (empty states/errors) lifted above. |
| `references/depth-and-texture.md` | 186 | No | Z-plane/grain/aurora-glow/glassmorphism/3D-tilt/parallax CSS depth techniques. Owner: **design/frontend**. |
| `references/imagery.md` | 189 | No | Non-rectangular image presentation (masks, scrims, masonry, device mockups, Ken Burns, collage). Owner: **design/frontend**. |
| `references/section-archetypes.md` | 211 | No (lead's file; only the FAQ leaf touches success — see lift #5) | Sitemap/nav/footer/section-catalog + IA procedure for a marketing-site rebuild, plus a reusable section-archetype library (hero, features, stats, testimonial, collections…). Owner: **design/product**. |
| `references/art-review.md` | 213 | No | Art-direction QA process — capture tooling, per-section walk, A0–A3 severity, revise/approve loop, judging a build against its `DESIGN.md`. Owner: **design/quality**. |
| `references/niche-and-vertical-design.md` | 220 | No (lead's file; no items beyond the persuasion/marketing cluster) | Vertical playbooks (architecture, law, healthcare, finance, SaaS, real estate…) for winning a *prospective* client's trust pre-contact; the premium↔information dial. Owner: **design/marketing**. |
| `references/layout-and-composition.md` | 226 | No | Grid/breakout/bento/asymmetry/whitespace/Gestalt layout CSS techniques. Owner: **design/frontend**. |
| `references/frontend-build-patterns.md` | 473 | No | Next.js/Tailwind build scaffolding, section-component registry pattern, asset-library discipline, HTML/CSS/JS/TS engineering craft. Owner: **frontend** (JS/TS appendix could equally sit in **backend**'s general-craft notes, but nothing here is success-specific). |

**Orphan check:** no file in this skill contains content that is unclaimed by an existing
shipped pack. Every file maps cleanly to **design** (the overwhelming majority — craft/CSS/
motion/imagery/layout/critique/direction), **frontend** (build patterns, Tailwind theming),
or **marketing/growth** (persuasion, vertical playbooks, testimonials/case studies, trust/SEO
structure). There is no genuine orphan file to flag.

**Bottom line for the lead:** abandoning webdesign loses essentially nothing for success —
of 3707 lines, only ~30 lines across 4 files contain anything reusable, and all 4 are
generic UX/copy mechanisms (a support-triage test, a heuristic label, empty-state/error
voice, and a progress-meter pattern) that need rewriting into success-specific language
rather than lifting as-is. The skill's actual subject — prospect persuasion, visual
craft/build, and site IA — has zero native onboarding, help-content, support-process,
health-score, VoC, escalation, or retention material.
