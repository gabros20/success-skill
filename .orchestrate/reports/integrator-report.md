# Integrator report — success-skill

Date: 2026-08-02 · Scope: SKILL.md router, metadata, SOURCES.md, §3b checkpoints, pack-wide
cross-checks. Read: inventory (whole), synthesis (whole), nav research §6–§9, all 6 writer reports,
all 15 references + 4 assets, 12 sibling SKILL.md descriptions.

**Verdict: PASS with flags.** The pack is internally consistent and every router row reaches the
content it promises. Two genuine citation errors were found and fixed; three never-ship
figure-class violations were found and fixed; one required Contents block was missing; one
substantive research finding was shipped as a conclusion with no attribution and now carries its
primary source. Remaining items are the fixer wave's (evals) and four token-ceiling flags.

---

## 1. Fixes made

### Broken / wrong cross-references (2 — both load-bearing)

| File | Was | Now |
|---|---|---|
| `references/support-process-design.md:98` | `design/references/niche-and-vertical-design.md` | `webdesign/references/niche-and-vertical-design.md:148-156` — **the file does not exist in the `design` pack.** It lives in the **webdesign** skill (`~/.claude/skills/webdesign/`), which is where E's channel actually swept it (see `research/webdesign-lift-report.md:111`). This is the sole prior mention backing orphan #2 (the response-time promise), so a wrong pack attribution would have been a fabricated provenance for the pack's own claimed orphan. Line range verified by reading the healthcare-vertical block. |
| `references/onboarding-and-adoption.md:68` | `product/references/surface-app-saas.md:24` | `:35-36` — the quoted TTFV sentence is at 35–36; line 24 is a different (adjacent) bullet. |

All other sibling line citations were verified by reading the exact target lines. **26 checked, 24
were already exact**: design journeys:49/51-53, design research:49, design content:45/58, product
saas:31-32/45, product metrics:45-53, product discovery:15/75, product mobile:35-36, product
SKILL:28, growth handoff:43/49/66-67, growth retention-and-resurrection:167/168-169, growth
surface-b2b-sales-assisted §6, growth monetization §5, marketing handoff:43, marketing
email-compliance-checklist:81/82, marketing organic-social:17-18, marketing ASO:18, operate
incident-response:21/158-159, operate decommissioning:185-187, operate handoff:79, operate
SKILL:90, automation process-capture:15-17, automation approval-policy-card:17-23, ai
surface-chat-assistant:9, `digital-product-skill/.../product-lifecycle-skill-packs-exploration.md:1033`.

### Never-ship figure-class violations (3)

The standing family rule — *a disclaimed figure is still a figure; never name a never-ship number in
order to forbid it* — was violated in three places. All three named the exact digits inside the
sentence banning them, which is precisely how the operate/growth builds learned the number still
ships.

- `ai-support-policy.md` — `**"76%" never ships.**` → `**No single "industry" automation figure
  ships.**`, and the Validation line rewritten to forbid *any* single-figure industry
  deflection/resolution percentage "including inside a sentence forbidding it."
- `health-and-risk-signals.md` §6 — the Shpigford `"reduce churn by 68%"` teaser → "a
  bare-percentage churn-reduction teaser with no visible method," permalink and date retained, digits
  dropped. The pedagogical point (the figure-class rule catches this pack's own best anchor) is
  intact and does not need the number.
- `renewals-and-expansion.md` — the `"$2M ARR per CSM"` string appeared in a *routing pointer* in a
  file that is not the exhibit's home → "the circulating ARR-per-CSM heuristic," with the pointer
  now stating that `surface-b2b-high-touch.md` §4 is **the only place the figure may appear**.

**Two deliberate survivals, judged correct, stated so spec review can overturn:**
- `surface-b2b-high-touch.md` §4 keeps the ARR-per-CSM figure — this is the sanctioned use
  (synthesis §3: "Never ship; use as propagation exhibit"), and both the debunking and the
  re-circulation are permalinked in the same bullet.
- `voice-of-customer.md` §6 keeps the "96%" string. The distinction I applied: the 96% is a
  *claim-with-a-number a reader will meet verbatim and must be able to identify and correct*, and
  the corrected stake-dependent range is what synthesis row 7 mandates shipping. 76% / 68% /
  ARR-per-CSM are *bare figures whose only function is to be re-quoted*. If spec review wants one
  rule with no exception, §6 can be reworded to "the near-universal complaint-rate claim."

### Structure and template residue

- **Deleted `references/example.md`** (template stub).
- **`ai-support-policy.md` had no `## Contents`** at 200 lines — added, in the flagship's compact
  one-line form (cheaper than a bullet list on a file already over ceiling). All 15 references now
  satisfy the >100-line rule; verified programmatically.
- **Four cross-repo links labelled with a filename pointed at a repo root** — three
  `[surface-chat-assistant.md](https://github.com/gabros20/ai-skill)` in `ai-support-policy.md` and
  one `[approval-and-authority.md](https://github.com/gabros20/automation-skill)` in
  `overlay-agentic.md`. A link that promises a file and delivers a repo index is the R18 failure at
  reference level. Converted to plain-text `pack`'s `references/<file>.md` citations, matching the
  convention every other file in the pack already uses. Zero `github.com/gabros20` links remain.

### Escalation vocabulary — W2's open question, decided

**Ruling: `support-process-design.md` §5 is the pack's single disambiguation home.** It already
carried the fullest treatment (the four-way family collision + support's own three senses), so it
was marked as the canonical home rather than rewritten. The three re-enumerations elsewhere were
converted to pointers, keeping the operative rule in place at each site:

- `ai-support-policy.md` — dropped the parenthetical re-listing of operate/automation/ai; keeps
  "always write **customer escalation**" and points to §5.
- `handoff.md` failure modes — dropped the four-pack enumeration; keeps the rule and points to §5.
- `surface-b2b-high-touch.md` §3 — GitLab's severity ladder relabelled "the organizational sense"
  (it was "a third, distinct sense," which only parses if you have read §5) with a pointer added.
- `overlay-agentic.md:82` — one bare "an escalation" qualified to "a customer escalation."

Sweep result: every remaining bare use sits inside a file whose local context has already fixed the
sense (the whole of `ai-support-policy.md` is the bot-to-human sense and states the rule; §5 *is*
the disambiguation).

### Single-homed canon

- **PROVE weights de-duplicated.** `health-and-risk-signals.md` §1 stated the full weight set
  (Product 50%, Risk 25%, Outcomes 10%, VoC 5%, Engagement 10%) that `surface-b2b-high-touch.md` §2
  also carries with sub-measures and banding. Per W6's ruling (depth in b2b, summary in flagship),
  the flagship now says "five weighted measure groups; full weights, banding, and failure modes in
  `surface-b2b-high-touch.md` §2." The weights aren't load-bearing for §1's argument, so this is a
  clean win that also relieves the flagship's budget.
- **No drift found** between the two files' GitLab material: input-expiry half-lives (60/90/120/30),
  Tech-Touch switched-off measures, CSM-Sentiment override, unbuilt VoC components, and non-monotone
  support volume are stated consistently in both. See flag F3 for the one duplication I did **not**
  remove, with reasons.

### Attribution gap closed (§3b checkpoint 1 — the significant finding)

See §3 below. `health-and-risk-signals.md` §6 shipped the flagship's central reframe with no source;
its primary source now appears, attributed and licensed.

---

## 2. Router walk (R18) — every row, walked

All 15 references and all 4 assets are linked from SKILL.md; **no reference is unlinked, and no
SKILL.md link is broken** (verified programmatically). Each row's promised content was then grepped
in its target file. **50/50 promises reached.** Selected walk:

| Row promise | Path | Confirmed at |
|---|---|---|
| The Existence Gate + CONTESTED pricing-first correction | `when-success-applies.md` | §"The Existence Gate"; §"What replaces the enterprise canon at solo scale" (pricing 1st, AI tier-1 2nd, docs an honest null) |
| Onboarding **program** + design seam + TTFV from PRD + current Goal+AX | `onboarding-and-adoption.md` | §"The seam, stated explicitly"; §"Consuming TTFV as an input"; §"The implementation/adoption plan" (pre-2024 form explicitly dated) |
| Reactive/proactive help-content test + zero-result/zero-click backlog | `education-and-knowledge-base.md` | §1, §2, §3, §4 |
| Two taxonomy axes + three status buckets + first/next/resolution + response-time promise + escalation home | `support-process-design.md` | §1–§5 (§5 now marked the single disambiguation home) |
| Escalation is symbolic, never a confidence float + typed field + strict/fluid + confirmed-vs-assumed + pass^k + Air Canada | `ai-support-policy.md` | all seven sections |
| ⭐ score-vs-prediction · "not published, never not measured" · Observability Question · four studies · honest ceilings · the reframe | `health-and-risk-signals.md` | §1–§6, each present verbatim where the guard requires verbatim |
| Aggregate trend + Display-vs-Response denominator + replication failures | `voice-of-customer.md` | §1–§4 |
| The third box + uplift-not-risk + one-click test + voluntary/involuntary | `retention-execution.md` | §1–§6 |
| Four audited NRR definitions never compared + NNR + folklore label + advocacy | `renewals-and-expansion.md` | §2, §3, §5, §7 |
| Co-owned always + operate states fact/success manages relationship + promise-vs-SLO | `incident-and-account-comms.md` | all four sections |
| Three originated rows + community-retention fork closed | `handoff.md` | §"Three rows this file originates"; §"Closing an open route" |
| Solo default: tooling-adoption threshold, AI tier-1 as the team | `surface-selfserve-solo.md` | §§2–3 + job-by-job table |
| Epistemics to lift, machinery to decline **with reasons** | `surface-b2b-high-touch.md` | §3, §4 |
| Review responses as support · platform-owned cancellation · store-run retry | `surface-mobile-subscription.md` | §1, §2, §4 |
| Additive overlay · configs-not-prose · kill switch · resolution gaming | `overlay-agentic.md` | all six sections |

One row was reworded after the walk: the onboarding row quoted design's rule as `"orient, don't
educate"` while the target file renders it `orient (**don't educate**)`. Quotation marks removed so
the row does not promise a verbatim string it cannot deliver.

---

## 3. §3b controller checkpoints

### Checkpoint 1 — `_raw-gh-voc-onboarding-csops.md` sweep (the inventory omission)

Swept the whole 810-line raw against the shipped pack. W5's two uses (Formbricks Display/Response,
churnkey/sdk) are in. **Five findings were unused. One of them was a real defect, not a gap:**

**(a) FIXED — `dynatrace-oss/CustomerSuccess` §8b.2.** The raw calls this "the best evidence channel
C found for charter wedge hypothesis 2" — the flagship's own wedge. It is Apache-2.0, LIFTABLE, and
it is *readable arithmetic from a named vendor's CS team*, which is the rarest evidence class in this
whole corpus. The flagship's §6 shipped its conclusion ("score + mandatory gap/action = a
prioritization device; the same number alone is folklore") **with no source attached** — the reframe
was lifted and the exhibit dropped. Added a compact attributed paragraph to §6: four
equally-weighted 25-point components on hand-picked round thresholds, **no outcome variable joined
anywhere**, and the paired Gaps-&-Actions tile that is exactly the redeeming half. This is an
attribution fix (R14/R20), not new doctrine.

**(b) FOLDED as checklist rows —** two teachable rules the raw states outright, added to
`assets/health_score_audit.md` (rows 9 and 10, which is the natural home for both and required no
new prose doctrine):
- **Recency thresholds** (§8b.3): Dynatrace's at-risk band is pure login recency with unexplained
  3d/14d thresholds. "A recency threshold copied across products is the most common way a health
  signal becomes noise," with the concrete artifact to point at.
- **Account/user rollup** (§3.1, Usertour): account-level health answered from user-level events
  needs a real membership edge with its own attributes; averaging users mislabels multi-seat
  accounts with rotating staff. Usertour's licence is AMBIGUOUS (flat `"license": "MIT"` in
  `package.json` contradicting a `LICENSE` carve-out scoped by what the *code does*, API says
  NOASSERTION) — cited as a modelling idea, marked ambiguous, no code.

**(c) REASONED SKIPS —** recorded rather than folded:
- §3.2 (onboarding progress pinned to a flow *version*; pre/post completion rates aren't comparable
  across onboarding changes unless segmented by version). Genuinely good and genuinely unused. It is
  a *measurement*-honesty rule and `onboarding-and-adoption.md` is deliberately scoped away from
  onboarding metrics (design owns them). Skipped rather than smuggled in — **but see flag F1**, it is
  the strongest candidate for the fixer wave if anyone wants one more thing in that file.
- §8b top-line ("what a dev-tools CS team publishes is overwhelmingly product best-practice
  documentation — enablement content, not CS methodology"). A good framing datum with no obvious
  home that isn't editorializing; skipped.
- §2.1 (Fider's feedback-board status taxonomy) — subsumed by the stronger, schema-enforced
  three-bucket convergence already shipped in `support-process-design.md` §1.

### Checkpoint 2 — Chatwoot Captain / liquid-template phrasing

**Clean.** Grepped the whole pack for `captain`, `liquid`, `{{`, `assign `, `handoff_tool`. Two hits,
both fine: `ai-support-policy.md:41` names Captain and explicitly states it is *describing the
pattern, not quoting the template* under the `enterprise/` source-available licence (W3's mid-draft
fix held); the second hit is a false positive on the word "assign." No template text, no liquid
syntax, no near-verbatim fragment anywhere — including in files by writers other than W3, which was
the point of the belt-and-braces check.

### Checkpoint 3 — never-ship grep across the ENTIRE pack incl. SKILL.md

Run after all edits. Full class sweep (5–25×, 5%→25–95%, 96%, 80/20, $1-vs-$6, ARR-per-CSM, 76%,
68%, 15–30%, CES-superiority, NPS-best-predictor, bare `N hour (P1)` SLA patterns). **Three hits
remain, all intended and all documented above**: the ARR-per-CSM propagation exhibit in its one
sanctioned home, and the "96%" correction. SKILL.md itself is clean and ships no figure at all.

### Checkpoint 4 — evidence-grade labels

Present inline throughout. Spot-checked every file: X citations carry the practitioner-report grade,
vendor numbers are labelled vendor-claim even when refuted, the academic table carries method/n/scope
per row, and `renewals-and-expansion.md` marks the median-NRR-decline figure "method unknown" rather
than dropping or laundering it.

---

## 4. Description + collision check

**Final description (591 chars, under the 600 ceiling), verbatim:**

> Keep customers after they buy — does a success function apply yet, onboarding programs, help
> content and KB, support process, SLAs as promises, AI-support policy, health and churn-risk
> honesty, voice-of-customer interpretation, retention execution, renewals/expansion (NRR), incident
> comms. Use to design a support process, audit a health score, or run a churn-save or renewal. Not
> in-product onboarding flow (→ design), retention experiments (→ growth), pricing/dunning (→
> product), agent mechanics/evals (→ ai), internal SLOs (→ operate), lifecycle email (→ marketing),
> the sale (→ sales).

**Collision check — all 12 sibling descriptions read in full.** The growth "prioritization" lesson
applied: no word a sibling claims is claimed bare here.

| Sibling-claimed word | Sibling's claim | How ours is qualified |
|---|---|---|
| retention | `growth`: "conversion optimization, **retention**, referral loops" | "retention **execution**" + arrow `retention experiments (→ growth)` — the sharpest collision in the set, and the one the reserved job name depends on |
| onboarding | `growth` and `marketing` both arrow it *to* success; `design` owns the flow | "onboarding **programs**" + arrow `in-product onboarding flow (→ design)` |
| SLA / SLO | `operate`: "SLOs and alerting" | "SLAs **as promises**" + arrow `internal SLOs (→ operate)` |
| agents / evals / guardrails | `ai`: "agents, RAG, memory, **evals**, guardrails" | "**AI-support policy**" + arrow `agent mechanics/evals (→ ai)` |
| incidents | `operate`: "**incidents**" | "incident **comms**" |
| content | `marketing`: "content"; `design`: "content design" | "**help** content and KB" |
| pricing | `product`: "business-model and **pricing**"; `growth`: "pricing tests" | not claimed; arrow `pricing/dunning (→ product)` |
| NPS / metrics | `product`: "**success metrics** and metric-trees" | "voice-of-customer **interpretation**"; the phrase "success metrics" is never used — this was the nastiest homonym available and is avoided outright |
| prioritization | `growth`: "experiment design and **prioritization**" | **the word does not appear**, even though the flagship's own reframe calls a health score a "prioritization device" |
| defect triage | `quality` | "triage" not used in the description at all |

Words this pack claims that **no sibling claims anywhere**: *support process · churn · health ·
renewals · expansion · NRR · voice-of-customer · customer success*. Those are the pack's clean
lexical territory.

Four rulings could not fit the 600-char budget alongside the job list (`data`, `automation`,
`quality`, plus VoC's design/product seams). All four are carried as full rows in SKILL.md's **"Not
this skill"** table instead, which has 11 rows covering every §4 ruling.

---

## 5. Metadata + SOURCES.md

- **`skills/success/agents/openai.yaml`** — TODO placeholder removed; display name "Customer
  Success", short description within the linter's 25–64-char window, real default prompt.
- **`.codex-plugin/plugin.json`** — placeholder `TODO` prompt and the generic three-verb description
  replaced; `shortDescription` matches openai.yaml exactly; `longDescription` carries the job list
  and the flagship's question; keywords extended (customer-success, customer-support, churn,
  retention). Version/homepage/repo untouched (release procedure owns those).
- **`SOURCES.md` created at repo root** — 8 sections: the wedge (with the flagship-framing
  constraint stated *against* this pack — `t0ddc3by` already asks the question, so we claim only
  that we answer it); the four planks and their evidence; a full licence ledger split
  LIFTABLE / CITE-ONLY / AMBIGUOUS with what each source was used *for*; the two new licence clauses
  (f) and (g) plus the manifest-contradicts-file lesson this build proved in both directions
  (usertour hides a carve-out behind flat MIT; trudesk reports NOASSERTION for clean Apache-2.0);
  academic and legal citations with method; practitioner sources with the verbatim-permalink
  discipline stated; the refusal list and its standing rules; what the pack claims for itself; and
  what it did not do (including the CONTESTED pricing plank shipped as one-sided-but-unopposed).

SKILL.md's Resources section references SOURCES.md and `evals/` as plain text rather than links —
this repo's linter (stricter than the one growth shipped against) fails any runtime link escaping
the skill root, and `[SOURCES.md](../../SOURCES.md)` is exactly that. Content and location are
unchanged from the mandate; only the link form.

---

## 6. Flags for spec review

**F1 — token ceilings (flagged, not butchered, per mandate).** By `scripts/count-skill-tokens`:

| File | Est. | Ceiling | Over |
|---|---:|---:|---|
| `SKILL.md` | 3,658 | 3,500 (lint WARN) | +4.5% — `marketing` shipped at 3,548 with the same WARN, so this is in-family. I trimmed ~40 tokens of Mission and table prose; further cuts would drop a routing fact. |
| `ai-support-policy.md` | 2,876 | 2,500 | **+15%, the worst in the pack.** Note W3 self-reported ~2,420 — the repo estimator disagrees with theirs by ~450, so this was already over before my +~50 (Contents block, net of the escalation trim). W3 named the nine-item escalation enumeration as the most compressible section; that remains the right target. |
| `health-and-risk-signals.md` | 2,764 | 2,500 | +10.6%. W4 reported 2,576 and asked for controller tolerance. Net of my edits: −PROVE weights, −68% digits, +Dynatrace attribution ≈ +190. **I judged the attribution non-optional** (a lifted reframe with no source is worse than an over-budget file), but if the fixer wave must cut, cut here rather than dropping it. |
| `retention-execution.md` | 2,521 · `support-process-design.md` | 2,530 | 2,500 | +1%, noise. |

**F2 — evals are still template placeholders** (all four suites) and `evals/traversal/cases.json`'s
`primary-route` case names `references/example.md`, which I deleted. This is the **only remaining
lint FAIL** and it is explicitly the final fixer's item per inventory §4 — flagging so the deleted
path is not mistaken for a regression I introduced.

**F3 — one duplication I deliberately did NOT remove, for spec review to overturn if it disagrees.**
`health-and-risk-signals.md` §7 and `surface-b2b-high-touch.md` §3 both carry the GitLab liftable
epistemics with the same concrete numbers (input expiry 60/90/120/30, Tech-Touch switched-off
measures, ignorance-is-a-finding, tie-breakers). Values agree exactly — no drift. Inventory row 6
mandates them in the flagship and row 13 mandates full depth in b2b, so the duplication is
authorized, and the ablation argues for keeping it: the default reader is solo self-serve and is
routed *away* from the b2b surface, so stripping §7's numbers would leave that reader with "inputs
should expire" and put the concrete half-lives behind a file they were told to skip. Framings
differ correctly (flagship: what transfers to a lean reader; b2b: what to audit an adopted score
against). I removed only the value with no reason to be in both (the PROVE weights).

**F4 — `assets/nrr_calc.py` is the one asset that does not run bare.** It self-tests at import
(verified: `import nrr_calc` passes) and all six CLI modes work, but `python3 nrr_calc.py` with no
args prints an argparse usage error where the other three print a self-test confirmation. Not a
correctness defect; a consistency wart. Left to W6's owner rather than risking their verified
six-mode CLI contract.

**F5 — the 96%/76% asymmetry** described in §1 is a judgment call, not a rule the synthesis states
explicitly. Recorded there in full so spec review can collapse it to one rule if preferred.

**F6 — `growth/references/handoff.md:66-67`** is cited across the pack as growth "reserving the
literal job name `retention-execution`." The literal string is there, but it appears inside a
*failure-mode bullet* about the AARRR seam rather than a dedicated reservation row. The claim holds;
the framing ("reserves the slot and builds nothing into it") is a slightly generous reading of a
sentence written for another purpose. Low risk, worth a second opinion.

**F7 — sibling PRs still queued** (synthesis §4, do NOT edit now, confirmed still true on disk):
`operate/references/handoff.md:79` names only `product` on the customer-facing decommission row
while its own prose at `decommissioning.md:186` says `product`/`success`;
`automation/references/process-capture.md:15-17` still says the three commercial upstreams "do not
yet exist as shipped skills," which success's release makes stale. Both one-liners.
`incident-and-account-comms.md` and `handoff.md` already document the first one honestly as
operate's known issue rather than treating it as evidence against success's claim.
