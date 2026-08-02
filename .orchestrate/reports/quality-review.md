# Quality review — success-skill

Date: 2026-08-02 · Reviewer: quality review (opus) · Snapshot: `09db6dc`
Instrument: `digital-product-skill/docs/high-signal-skill-authoring-standard.md` §16 rubric, §5
budgets, §17 lint rules.
Read in full: all 15 references + `SKILL.md` + 4 assets + `SOURCES.md` + `research/synthesis.md`
§§1–8 + `.orchestrate/inventory.md` + `spec-review.md` (including its 2026-08-02 re-verify pass).
Re-ran independently: `scripts/lint-skill`, `scripts/check-sync`, `scripts/count-skill-tokens`,
a full markdown link-graph resolution, a never-ship string sweep, all three Python assets, and
six adversarial CLI probes on `nrr_calc.py`.

**I did not re-litigate the spec review.** Its 2 blockers, 5 S-MAJOR, and 11 MINOR findings are
confirmed landed; residuals R1–R4 are confirmed applied at `09db6dc`. Everything below is new.

---

## Verdict

**NOT-SHIP as of `09db6dc` — rubric 21/24.** Three things stand between this pack and ship, all of
them bounded final-fixer work:

1. **Evaluation scores 0/2** — all four fixtures are still template placeholders, `lint-skill` emits
   5 FAILs. The §16 release threshold is explicit: *no dimension scores 0*. Fixture specs are in §5
   below; this is the known, scheduled work, not a surprise.
2. **Two new S-MAJOR content findings** (§4) that the spec review's methodology could not catch —
   it traced claims to raws; these are *cross-file* defects where two shipped files disagree, or a
   pointer promises content its target does not carry.
3. Token-ceiling adjudication (§6) — recommended trims, not blocking.

**After those land: 23/24, comfortably above threshold, and this is the strongest pack in the
family on domain precision.** The evidence spine is real, the judgment layer is present in every
file, and the walkability is clean — six of six walks reached a concrete, actionable answer with no
dead ends and no contradictions between the files a reader actually loads together.

---

## 1. §16 rubric

| Dimension | Score | Evidence |
|---|:--:|---|
| Activation signal | **2** | Description is 591 chars (§5 budget 250–600), opens with the primary outcome in the first 32 chars ("Keep customers after they buy"), then subdomains, then indirect trigger vocabulary ("audit a health score", "run a churn-save"), then **seven** boundary arrows each naming the owning sibling. `openai.yaml` and `plugin.json` carry the same short description; `defaultPrompt` exercises the flagship. No marketing language, no folder structure, no SEO synonyms. Boundaries are *written* but not yet *tested* — that deficit is scored under Evaluation, not double-counted here. |
| Capability delta | **2** | Non-obvious procedural advantage on every plank: the Observability Question (contractual vs non-contractual churn — a distinction the CS canon never draws), "not published, never not measured", the Existence Gate (no source anywhere states when a success function is worth having), the nine-pattern escalation corpus with its zero-confidence-float negative result, four SEC-verbatim NRR mechanics that are not one metric, and the zero-result/zero-click backlog as the observable replacement for an unmeasurable deflection rate. None of this is retrievable from general knowledge, and none of it is in the three partial incumbents. |
| Routing | **2** | Faceted router: 10 job rows × 4 surfaces (3 base + 1 additive overlay), plus a 9-row "Not this skill" table and 7 numbered pre-routing rules. Every row carries a loading *condition*, not a bare filename. Route rule 2 forecloses the stall case explicitly ("If the request names no business model, do not stall — assume the default surface and say which you assumed"); rule 3 forecloses the overlay-instead-of-base error. All 15 references linked from `SKILL.md`; link-graph resolution across `SKILL.md` + 15 refs + `health_score_audit.md` returns **0 broken links**. |
| Workflow | **2** | Seven ordered, bounded steps, gate-first, artifact-terminated. Each step is observable ("State any surface assumed", "Grade every figure", "Run the honesty checks that apply"). Step 6 names the four conditional honesty checks and when each fires. No philosophy. |
| Domain precision | **2** | Exact facts with methods and grades throughout: `first_response`/`next_response`/`resolution` as the schema-convergent SLA metric names across two independent codebases a decade apart; the three canonical status buckets, schema-*enforced* in two systems; Ascarza's per-segment deltas; de Haan's r=.199 tenure ceiling; the IBM Telco honest ceiling (acc 78–81%, churn-F1 0.60–0.62, AUC 0.83–0.85) with both inflation mechanisms named; lifelines' 0.55–0.75 concordance band as a leakage tripwire; *Moffatt v. Air Canada* 2024 BCCRT 149 with the tribunal's verbatim rejection. Defaults and exceptions are stated (one priority field *unless* formal ITSM; the clock pauses on customer-wait *as a named state*). |
| Output contract | **2** | The artifact contract names five carriers and every one is testable: gate verdict present · every figure with source + grade · the seam cited by pack and filename · what the artifact *cannot* support · provisional/contested labels carried forward not flattened. Plus a negative contract ("None is delivered as production code"). `health_score_audit.md` is a fully specified 10-row artifact with three named verdict strings. |
| Validation | **2** | Every one of the 15 references ends with a Validation block of observable checks, not "ensure quality". `SKILL.md` Completion adds five evidence-based checks and a safe-failure rule ("an unsourced percentage is not a finished line"). Three assets are runnable and self-testing at import; I re-ran all three — `churn_baseline_check` reproduces flagship §5 exactly, `sla_capacity_calc` prints "this is not a recommended SLA; it is a geometric fact", `nrr_calc`'s six modes all reproduce their anchors. |
| Progressive disclosure | **2** | Universal core (3,658 tok) + 15 focused leaves, each with its own Purpose / Read-when / **Skip-when** / Inputs / Produces header. The Skip-when blocks are the load-bearing part — they route *away* as precisely as the router routes toward, which is what keeps a reader from loading every reference. |
| Token efficiency | **1** | Nothing is repetitive filler, but not every line serves a §4 function. Four files over the 2,500 soft ceiling (`ai-support-policy` 2,939 = +17.6%, `health-and-risk-signals` 2,844, `retention-execution` 2,580, `support-process-design` 2,553) and `SKILL.md` at 3,658 exceeds both the 3,500 review threshold and marketing's shipped 3,548 precedent. Two identified `SKILL.md` spans (~220 tok) duplicate `SOURCES.md` §1 or restate family boilerplate and perform no §4 function. See §6. |
| Clarity | **2** | Compact with conditions and order preserved. Named concepts are bolded and used consistently across files (the Existence Gate, the Observability Question, the response-time promise, score-vs-prediction, "a category list without tie-breakers is not a taxonomy"). Uppercase CONTESTED / CONFOUNDED / never-ship always carry their reason. Four domain abbreviations ship unexpanded (MINOR-3). |
| Portability | **2** | Zero absolute paths. All three Python assets are stdlib-only (`argparse`, `dataclasses`, `__future__`) — no third-party dependency, no network, non-interactive, self-testing. Sibling-pack citations use pack-relative paths (`growth/references/handoff.md:43`), which is documented family coupling, not a host assumption. I verified four externally-cited sibling paths exist on disk (`automation/references/approval-and-authority.md`, `automation/assets/approval-policy-card.md`, `ai/references/surface-chat-assistant.md`, `growth/references/handoff.md:43,66`). |
| Evaluation | **0** | All four fixtures are unmodified template placeholders. `lint-skill` FAILs 5×, including a traversal case naming a nonexistent `references/example.md`. No activation, traversal, output, or ablation case exists. |

**Total: 21/24.**

Release threshold check:
- `No dimension scores 0` — **FAILS** (Evaluation).
- `Activation, workflow, validation, clarity, portability score 2` — passes.
- `Total ≥20/24` — passes.

Projected post-fix: Evaluation 0→2 and Token efficiency 1→2 with the §6 trims = **23/24**.

---

## 2. Walkability — six walks

Method: start from `SKILL.md` with only the user's sentence, apply the 7 route rules, follow the
table row, read the named file(s), and ask whether a concrete artifact is now producible. Friction
is recorded even where the walk succeeded.

### Walk 1 — "Audit our customer health score" (B2B, named CSM) ✅
Route rule 1 (existence gate) is ambiguous here and resolves correctly: the request assumes a
success function, but a score already exists, and `when-success-applies`'s own Skip-when closes it
("Success already applies… go straight to health-and-risk-signals"). Job row 6 ⭐ →
`health-and-risk-signals.md`; surface → `surface-b2b-high-touch.md`; asset →
`assets/health_score_audit.md`. **Lands on a concrete artifact:** a completed 10-row audit with one
of three named verdicts, plus b2b §2's five failure modes to check the specific score against.
*Friction (documented, upheld by spec review F3):* flagship §7 and b2b §3 both carry GitLab's expiry
half-lives; a reader loading both reads them twice in different framings. Correct trade — the
default solo reader is routed away from b2b and would otherwise lose the half-lives entirely.

### Walk 2 — "I'm solo. What response-time SLA should I promise?" ✅
Route rule 2 → default surface, no stall. Job row 4 → `support-process-design.md` §4; surface →
`surface-selfserve-solo.md`. **Lands:** the never-ship rule fires immediately (no template number),
`assets/sla_capacity_calc.py` produces the geometric ceiling and an overload verdict, and the
promise gets set from actual coverage. The asset's own output refuses to be read as a
recommendation ("this is not a recommended SLA; it is a geometric fact") — the strongest anti-misuse
framing in the pack.
*Friction:* `surface-selfserve-solo.md:70` names the calculator as "`support-process-design.md`'s
`sla_capacity_calc.py`" — a bare filename attributed to a reference file, where the asset is
pack-level at `assets/sla_capacity_calc.py`. Recoverable but one indirection too many (POLISH-2).

### Walk 3 — "Design when our bot hands off to a human" ✅
Job row 5 → `ai-support-policy.md`. **Lands:** nine symbolic triggers with sources, the
consent gate, the typed-field exemplar with its protected precision guard, the strict/fluid
boundary with the four named strict moments, and the flat-handoff default with tier-aware routing
declared a stated gap. The adversarial version ("escalate when confidence < 0.7") is caught by the
file's first sentence and its failure-mode list. If unattended → `overlay-agentic.md` correctly
stacks rather than replaces. No dead end.

### Walk 4 — "Our NRR is 118%. How does that compare to Snowflake's?" ✅
Job row 9 → `renewals-and-expansion.md` §2. **Lands on a refusal plus a method:** the four filing
mechanics differ, the comparison is declined with a reason, and `assets/nrr_calc.py` recomputes
under a stated mode while printing "Never compare this figure to a result computed under a
different mode" on every run. The answer the user wanted is refused; the answer they needed is
produced. This is the pack working exactly as designed.

### Walk 5 — "Do we need customer success yet?" ✅
Route rule 1 → `when-success-applies.md`. **Lands:** the arvidkahl attributed test (does the
customer's growth change what they pay), an applies / lighter-weight / not-yet verdict, four named
sibling packs that cover post-purchase meanwhile, and the CONTESTED pricing-first correction with
its one-sidedness stated. The "lighter, never zero" ruling is anchored on the levelsio
automation-residue exhibit. Cleanest walk in the pack.

### Walk 6 — "Should I reply to this 1-star App Store review, and how?" ✅ *(with friction)*
**No job row names app-store reviews.** The reader reaches it three ways, all of which work: the
Surfaces table row 3 ("Store-review responses"), the `marketing` row of "Not this skill"
("marketing… keeps the store listing while success answers the reviews"), and the description's
subdomain list. Route rule 2 wants "one primary job and one base surface" — the job here is
`support-process-design` (a review is a support channel), which is not obvious from that row's
wording. **Lands:** `surface-mobile-subscription.md` §1 is self-sufficient and itself routes to the
support taxonomy. Concrete answer, but the router makes the reader find it via the surface table
rather than the job table (MINOR-1).

### Adversarial near-miss spot checks (4, all correctly deflected)
- "Redesign our onboarding wizard's empty states" → `design` (Not-this-skill row 1, and
  `onboarding-and-adoption`'s Skip-when).
- "Test whether a 20%-off save offer reduces churn" → `growth` (retention *experimentation*;
  `retention-execution` §1's third box states the split from its own side).
- "Approve refunds over $500 automatically" → `automation` owns the gate, success owns the policy —
  stated in both `handoff.md` and `overlay-agentic.md`.
- "Improve our support bot's retrieval quality" → `ai` (`ai-support-policy`'s Skip-when, seam block,
  and failure-mode list all point there).

**Walk verdict: 6/6 reach a concrete, actionable answer. Zero dead ends. Zero contradictions
between files a reader loads together on any of the six paths.** The one contradiction I found
(F-Q1) sits between the default surface's job table and a job file — reachable, but not on any of
these six paths, which is why it survived to this review.

---

## 3. Judgment-layer check

Every file was read against one question: does it teach *when/why/tradeoffs*, or does it hand over a
checklist? **No file reads template-grade** — the incumbent's failure mode is absent from this pack.

Representative evidence that the judgment layer is real rather than asserted:
- `support-process-design` §6 teaches the ITIL impact×urgency matrix *as over-engineering* with the
  condition under which it stops being that ("unless doing formal ITSM"), and names the honest
  default.
- `ai-support-policy`'s strict/fluid section poses the actual design question ("at which moments may
  the bot compose freely") rather than prescribing an answer, then names the four moments where the
  default flips and requires an explicit decision to relax it.
- `overlay-agentic` distinguishes structural from instructional enforcement and explains *why* it
  matters for this specific failure ("an agent optimizing its own resolution rate **fails by
  continuing, not by erroring**").
- `retention-execution` §3 converts an academic finding into an execution rule *and* states the safe
  default when the enabling model is absent ("Absent an uplift model, the safe default is to not
  reflexively spend the heaviest save effort on the single highest-risk segment").
- `surface-b2b-high-touch` §4 declines three canonical practices and states the sampling reason for
  each, then keeps the question the declined practice was answering.

**Thinnest file: `incident-and-account-comms.md` (1,116 tok).** It is closer to a boundary statement
than a judgment file — most of its content is seam citation. It is thin *by design* (inventory row
10 budgets it at 1,200 and marks it THIN), it earns its place with two real judgments (success never
originates a technical claim; an internal SLO must never leak into a customer conversation as the
promise), and it carries verbatim operate citations plus an honestly documented sibling
inconsistency. **Not a finding — recorded so a future reviewer does not re-raise it.**

Second-thinnest, `surface-mobile-subscription.md` (1,215 tok), is stronger than its size suggests:
every section names a mechanism the reader does not control and the design consequence
(§2's "the OS itself guarantees the cancellation path exists… an app that tries to obstruct it is
fighting a path it cannot actually close").

---

## 4. Findings

### S-MAJOR

#### Q1 — The default surface reports an evidence null as an empirical negative, and contradicts itself and the KB file in doing so

`references/surface-selfserve-solo.md:29-31`:
> the evidence shows automation and AI-run first-level support carrying the load a CSM would
> elsewhere — **not a documentation library, which tested weak in practice** (see
> [when-success-applies] for the full correction).

`references/surface-selfserve-solo.md:79` (job-reshape table):
> `education-and-knowledge-base` | **Docs-as-deflection tested weak in practice**; a KB rewrite is
> the actionable lever, not a model upgrade

**Three problems, one root cause.**

1. **The cited file says something different.** `when-success-applies.md:100-101` reads:
   "**Docs-as-deflection returned almost nothing usable** across two independent research passes —
   an honest null, not a finding to route around." That is an *absence of evidence about docs*.
   `surface-selfserve-solo` restates it as *evidence that docs are weak*. `research/synthesis.md`
   P2 confirms the former reading and no other: "docs-as-deflection, cancellation/win-back tactics,
   and onboarding-call execution are **under-evidenced** from practitioners."

2. **It is the pack's own flagship invariant, violated in a different domain.** `SKILL.md:115-117`
   binds: *"Say 'not published,' never 'not measured.' … Absence of disclosure is not proof of
   inaccuracy."* Line 30 does to docs exactly what the invariant forbids doing to health scores.
   This is the single highest-consequence class of error for a pack whose entire wedge is epistemic
   honesty — a reader who catches it has grounds to discount the flagship.

3. **Line 79 contradicts itself inside one table cell, and contradicts a job file.** "Docs tested
   weak" sits beside "a KB rewrite is the actionable lever" in the same sentence. And
   `education-and-knowledge-base.md:116-126` calls the KB-rewrite exhibit "the strongest actionable
   evidence in this pack's research for where to invest next" (resolution 20–25% → 85%, rewriting
   the knowledge base, *not* a model upgrade). The default surface therefore tells the pack's
   default reader to de-prioritise the one lever the owning job file rates highest.

**Why S-MAJOR and not MINOR.** It is on the **default** surface, so it is the version most readers
see; it inverts a load-bearing recommendation; and it breaks the invariant the pack is differentiated
on. The spec review could not catch it — its method traced each claim to a raw, and each of these
sentences traces to a real raw; the defect is only visible by reading two shipped files against each
other.

**Fix (two lines, one file, no citation cost).**
- `:30` → "…not a documentation library, which this research found **under-evidenced rather than
  effective** (an honest null — see [when-success-applies] for the correction)."
- `:79` → "The evidence for docs-as-deflection is thin, but KB *correctness* is the one first-party
  lever measured — check KB coverage before a model upgrade."

Do not weaken `when-success-applies.md:100`; it is correct as written.

#### Q2 — A cross-file pointer promises a third claim its target does not ship, and quotes it

`references/retention-execution.md:145-147`:
> [when-success-applies] already ships the full CONTESTED pricing plank — patio11's minimum-buy-in
> economics, robwalling's price-to-churn link, and the **"10%+ monthly churn is often a pre-PMF
> signal"** position — with its own CONTESTED marking.

**Evidence.** Grep across the whole pack: `pre-PMF` appears exactly **once**, in this pointer.
`when-success-applies.md` ships patio11 (`:107-110`, permalinked) and robwalling (`:82-84`,
permalinked) — and nothing about 10%+ monthly churn or pre-PMF. `research/synthesis.md` P2 lists all
three together as the scope-limiter to ship; two of the three landed, and this file's pointer was
written as if all three had.

**Two distinct defects.** (a) **R18 class** — a pointer that does not reach the content it promises,
the recorded marketing/automation lesson. A reader who follows it to check the pack's most-hedged
plank finds two of the three named items. (b) **Provenance** — the claim ships in quotation marks,
attributed to nothing, in the only place it exists in the pack. A quoted bare threshold with no
source and no grade is precisely the figure class R21 and R14 exist to stop, and it slipped through
because it is inside a *pointer* rather than inside a claim.

**Fix — pick one, do not do both.**
- *Preferred (zero research):* drop the third item from the pointer. It becomes "…patio11's
  minimum-buy-in economics and robwalling's price-to-churn link — with its own CONTESTED marking."
- *Alternative:* land the position in `when-success-applies.md`'s pricing list with its permalink
  and practitioner-report grade from the B-channel raws, then the pointer becomes true. Costs a raw
  lookup and ~40 tokens in an already-in-budget file (2,075).

### MINOR

1. **No job row reaches app-store review responses.** Walk 6 succeeds only via the Surfaces table or
   the `marketing` boundary row. One clause in job row 4's Contribution column ("…and the
   app-store-review channel") would close it, at ~8 tokens. Alternatively add "responding to public
   app-store reviews" to the mobile Surfaces row's *When* column, which already says "Store-review
   responses" but reads as a scoping note rather than a trigger.

2. **`nrr_calc.py` CLI IndexErrors on a wrong per-mode value *count*.** Confirmed by probe:
   `--mode snowflake_2yr_snapshot --values 126` → `IndexError: list index out of range`, traceback,
   exit 1. The odd-length case for `monthly_cohort_annualized` is handled correctly (clean
   `p.error`, exit 2) — the fix is to finish the job the same way for the fixed-arity modes. A
   second facet: **too many values are silently ignored** —
   `--values 126 100 55` prints a result computed from the first two and never mentions the third,
   which for a figure-honesty asset is the worse half of the bug.
   **Fix** — one table plus one check in `main()`, before the dispatch chain:
   ```python
   ARITY = {"snowflake_2yr_snapshot": 2, "rolling_12mo_point_in_time": 2,
            "grr": 3, "arr_bridge_nrr": 4}
   need = ARITY.get(args.mode)
   if need is not None and len(v) != need:
       p.error(f"{args.mode} requires exactly {need} --values, got {len(v)}")
   ```
   `rolling_12mo_weighted` needs its own even-length check (it zips pairs and silently drops a
   trailing odd value); `monthly_cohort_annualized` already has one. After this, every mode exits 2
   with a clean argparse message and no mode silently discards input.

3. **Four domain abbreviations ship unexpanded** — `BTYD` (`health-and-risk-signals.md:60`), `RFM`
   (`:48`, `:70`), `IPCW` (`:109`), `CEP` (`handoff.md:36`). §17 warns on undefined abbreviations.
   The pack's stated default reader is a solo builder, not a CS analyst; `IAP` is expanded correctly
   at first use in `surface-mobile-subscription.md:10` and is the model to follow. ~10 tokens total.

4. **`voice-of-customer.md:108-110`** cross-references "the experiment-level rule in §1"; the rule
   lives in the Skip-when block and is *restated* in §1. Harmless, but the reader who jumps to §1
   finds a paraphrase rather than the rule. Point at growth's file directly, as the Skip-when does.

### POLISH

1. **Repository-level template state.** `README.md` is still the unmodified skill-template README
   ("# Skill repository template"), `CHANGELOG.md` carries `## [1.0.0] — TODO-date` and
   "Initial release: TODO." These are release-pass artifacts and out of scope for the final fixer's
   pack work, but they are the last two `TODO`s outside `research/` and `TEMPLATE-CHECKLIST.md`.
   Note that `lint-skill` only scans `skills/` for `TODO`, so these will not self-report.

2. **Asset paths from reference files.** References cite assets as backticked pack-root-relative
   strings (`` `assets/nrr_calc.py` ``), which do not resolve relative to `references/`. This is the
   family convention (verified identical in `growth/references/experiment-design-and-feasibility.md`)
   and produces no broken links because they are not markdown links — recorded, not to be
   "fixed" out of step with the family. The one genuine case is `surface-selfserve-solo.md:70`,
   which drops the `assets/` prefix entirely and attributes the asset to a reference file.

3. **`incident-and-account-comms.md` is the thinnest file** at 1,116 tokens and is closest to a
   pure seam restatement. Deliberate per inventory row 10 and adequate as shipped — recorded so it
   is not re-raised.

---

## 5. Eval suite design (final fixer implements)

### Schema constraints the fixer must respect
Read from `scripts/lint-skill:255-294` before writing:
- Exactly **four** files, all `evals/{activation,traversal,output,compression-ablation}/cases.json`.
  A fifth directory is not validated — a never-ship suite must live inside one of these four or in
  `lint-skill` itself.
- Each file must be a **non-empty JSON array**.
- **The literal strings `TODO` and `__SKILL` fail the build anywhere in any of the four files**,
  including inside a prompt. Do not write "TODO" even in a comment field.
- `activation` must contain both `should_trigger: true` and `should_trigger: false` cases.
- Every `traversal` case must be an object with **both** `expected_references` and
  `forbidden_references` as arrays, and **every path in either array must exist** relative to
  `skills/success/`. This is what currently FAILs (`references/example.md`).
- `evals/README.md` line 10 ("Replace every placeholder case…") should be updated to describe the
  real suite once the fixtures land.

Note: never-ship strings appearing inside `evals/` are **not** a figure-shipping violation — the
evals directory is not agent-loaded. The fixer should not self-censor the fixtures.

### 5.1 `activation/cases.json` — 24 cases

**Positive, one per router row (14).** Field shape: `{"id", "prompt", "should_trigger": true}`.

| id | prompt |
|---|---|
| `gate-existence` | "We're three people with 400 paying users. Do we need customer success yet, or is it too early?" |
| `onboarding-program` | "Write the implementation and adoption plan for our new enterprise customers — docs, enablement sessions, a 30/60/90 cadence." |
| `kb-scope` | "What belongs in our knowledge base versus our product docs, and how often should articles get re-checked?" |
| `support-taxonomy` | "Set up our ticket taxonomy — statuses, categories, priorities — and the SLA metrics we report on." |
| `sla-promise` | "What response time can I honestly promise customers if it's just me, 9-to-5, one timezone?" |
| `bot-escalation` | "Define when our support bot should hand a conversation to a human." |
| `health-audit` | "Audit our customer health score — I want to know what it can actually predict." |
| `voc-reading` | "Our NPS went from 31 to 27 this quarter. What does that actually tell us?" |
| `retention-motion` | "Growth validated a win-back sequence. Set it up as an ongoing motion with reason capture." |
| `nrr-figure` | "Our NRR is 118%. How does that compare to Snowflake's 126%?" |
| `incident-comms` | "Ops confirmed a four-hour outage on the EU cluster. Write what we tell affected accounts." |
| `b2b-machinery` | "What CSM-to-account ratio should we staff to, and how often should we run QBRs?" |
| `mobile-reviews` | "We're getting one-star App Store reviews about billing. How should we handle replies?" |
| `agentic-overlay` | "Our AI agent issues refunds and closes tickets with nobody reviewing each one. What has to be true first?" |

**Positive, indirect vocabulary — no CS terminology (2).** These test the description's indirect
trigger vocabulary rather than its subdomain list.

| id | prompt |
|---|---|
| `indirect-churn` | "We're losing about 8% of subscribers a month and I can't tell why. Where do I start?" |
| `indirect-deflection` | "A vendor says their bot will deflect 70% of our tickets. Is that number worth anything?" |

**Negative — the 7 boundary arrows (7), `should_trigger: false`.** One per arrow in the description.

| id | prompt | owner |
|---|---|---|
| `neg-design-flow` | "Design the in-product onboarding wizard — the empty states, the progressive disclosure, and the aha-moment copy." | `design` |
| `neg-growth-experiment` | "Design an A/B test to find out whether a 20%-off save offer reduces cancellations." | `growth` |
| `neg-product-pricing` | "Restructure our pricing tiers and build the dunning sequence for failed payments." | `product` |
| `neg-ai-mechanics` | "Improve our support assistant's retrieval — chunking, reranking, and the eval harness for answer quality." | `ai` |
| `neg-operate-slo` | "Set our internal availability SLO and the on-call paging rotation for the API." | `operate` |
| `neg-marketing-lifecycle` | "Write the acquisition-side nurture email sequence and optimize our App Store listing keywords." | `marketing` |
| `neg-sales-close` | "Negotiate and close the seat-expansion deal with this account." | `sales` |

**Negative — adversarial, naming a sibling pack explicitly (2).** These are the §15.4 near-misses:
the prompt uses success's vocabulary *and* names the owning sibling, so a pack that over-triggers on
keywords will fail them.

| id | prompt |
|---|---|
| `neg-names-growth` | "Use the growth skill to run the retention experiment on our cancellation flow — I want the readout, not the motion." |
| `neg-names-ai` | "Use the ai skill to instrument escalation rate as an online eval signal for the support assistant's turn loop." |

**Negative — out-of-family (1).** `neg-quality-triage`: "Triage the defects found in this release
and decide whether we ship." (→ `quality`; tests the "Success triages customer tickets, not build
defects" row.)

Run each 3×, per §6.3. Record activation rate per case; a positive below 3/3 or any negative above
0/3 is a description regression.

### 5.2 `traversal/cases.json` — 10 cases

Shape: `{"id", "prompt", "expected_references": [...], "forbidden_references": [...]}`. All paths
below verified to exist.

| id | prompt (abbreviated) | expected_references | forbidden_references |
|---|---|---|---|
| `gate-first` | "Build us a customer health score." *(no gate justification given)* | `references/when-success-applies.md` | `references/surface-b2b-high-touch.md` |
| `flagship-audit` | health-score audit, B2B named CSM | `references/health-and-risk-signals.md`, `references/surface-b2b-high-touch.md`, `assets/health_score_audit.md` | `references/renewals-and-expansion.md`, `references/education-and-knowledge-base.md` |
| `solo-sla` | solo response-time promise | `references/support-process-design.md`, `references/surface-selfserve-solo.md` | `references/surface-b2b-high-touch.md`, `references/incident-and-account-comms.md` |
| `bot-policy` | bot handoff conditions, human reviews each | `references/ai-support-policy.md` | `references/overlay-agentic.md` |
| `bot-policy-unattended` | bot acts with **no** per-instance review | `references/ai-support-policy.md`, `references/overlay-agentic.md` | `references/surface-b2b-high-touch.md` |
| `nrr-compare` | compare our NRR to Snowflake's | `references/renewals-and-expansion.md`, `assets/nrr_calc.py` | `references/health-and-risk-signals.md` |
| `voc-trend` | "is our NPS drop meaningful?" | `references/voice-of-customer.md` | `references/health-and-risk-signals.md`, `references/retention-execution.md` |
| `save-motion` | run a growth-validated win-back | `references/retention-execution.md` | `references/renewals-and-expansion.md` |
| `mobile-review` | App Store review replies | `references/surface-mobile-subscription.md`, `references/support-process-design.md` | `references/renewals-and-expansion.md` |
| `seam-question` | "who owns the refund approval gate, us or automation?" | `references/handoff.md` | `references/health-and-risk-signals.md` |

`gate-first` is the highest-value case in the suite: it is the one that proves route rule 1 and the
first universal invariant actually fire, and its forbidden list catches the failure where the agent
produces the score anyway with a gate paragraph bolted on top.

### 5.3 `output/cases.json` — 5 artifact-contract cases + 1 never-ship case

Shape: `{"id", "prompt", "assertions": [...]}`.

| id | prompt | assertions |
|---|---|---|
| `contract-health-audit` | "Audit this health score: 5 inputs, weighted, no backtest, thresholds copied from a blog post." | Output completes all ten `health_score_audit.md` rows · states one of the three named verdicts verbatim · rows 1–2 failing forces "Do not present as validated" · every figure carries a source and an evidence grade · states what the artifact cannot support |
| `contract-sla` | "Give us a first-response SLA for P1 through P4." | No hour figure appears without "set this from your own observed capacity" framing · `sla_capacity_calc.py` is run or named · the customer-facing promise is distinguished from an internal SLO |
| `contract-gate` | "Design our CSM playbook." *(no justification)* | A gate verdict appears before any playbook content · the arvidkahl test is applied by name · at least one named sibling pack is given as the meanwhile-owner · the CONTESTED label on the pricing plank survives |
| `contract-escalation` | "Escalate to a human when model confidence drops below 0.7." | The confidence threshold is declined · at least three symbolic triggers are offered · consent-gating is stated · sentiment is described as recorded, never as a trigger |
| `contract-seam` | "Write the customer email for yesterday's outage." | Co-ownership with `product` is stated · no technical fact is originated · `operate` is cited as the source of fact/impact/timing · the seam is cited by pack **and filename** |

**`never-ship-strings` case.** One case whose `assertions` list is a forbidden-string list, with the
file-scoped allowances stated. This is the fixture; §5.5 is the enforcement.

### 5.4 `compression-ablation/cases.json` — 3 cases

Shape: `{"id", "prompt", "variants": ["no-skill","current","compressed-candidate"], "preserve": [...]}`.
Per §15.2, V2 must preserve task success, safety, required-reference recall, artifact completeness,
and human comprehension.

| id | prompt | what the ablation is actually testing |
|---|---|---|
| `ablate-observability` | "Build a churn-risk score for our usage-based product. Customers just stop using it; there's no cancellation event." | Does the compressed variant still ask the **Observability Question** before scoring, and decline the contractual-shaped template? This is the flagship's single load-bearing behavior. |
| `ablate-figure-grade` | "Our vendor says their AI resolves 80% of tickets. Put that in the board deck." | Does the compressed variant still grade the figure vendor-claim, name the confirmed-vs-assumed ambiguity, and refuse to ship the number bare? |
| `ablate-gate` | "Write our QBR agenda and CSM account-coverage model." *(solo product, 200 users)* | Does the compressed variant still run the Existence Gate and decline the machinery **with reasons**, rather than producing the agenda? |

Per §15.3, these three exercise rules placed at the beginning (route rule 1), middle (evidence
grading, flagship §3), and end (b2b §4's reasoned decline) of the loaded set.

### 5.5 Never-ship enforcement (recommended `lint-skill` addition)

The forbidden-string fixture in §5.3 is documentation; enforcement needs a static sweep that runs on
every commit. ~15 lines in `scripts/lint-skill`, after the reference checks:

```python
NEVER_SHIP = {
    # pattern                          : set of files where it is sanctioned, or empty
    r"5\s*[–-]\s*25\s*[x×]":            set(),
    r"25\s*[–-]\s*95\s*%":              set(),
    r"80/20":                           set(),
    r"\$\d+\s+(?:vs\.?|versus)\s+\$\d+": set(),
    r"\b76%":                           set(),
    r"\b68%":                           set(),
    r"\b131%":                          set(),
    r"\$2M ARR per CSM":                {"references/surface-b2b-high-touch.md"},
    r"\b96%":                           {"references/voice-of-customer.md"},
    r"62% precision":                   {"references/health-and-risk-signals.md"},
    r"(?i)klarna":                      {"references/ai-support-policy.md"},
}
```
Plus two **positive** assertions, which catch the regression class this review found (a guard
silently weakened in one file while remaining intact in another):
- the exact string `"not published," never "not measured"` must appear in **both** `SKILL.md` and
  `references/health-and-risk-signals.md`;
- the string `not measured` must **not** appear anywhere else in `skills/`.

And one **heuristic warn** (not a fail — it needs human judgment):
`(?i)(first|next)[- ]response[^.\n]{0,60}\b\d+\s*(hour|hr|minute|min|day)s?\b` — an SLA figure near
a response-time metric name, flagged for manual review against the "set from your own capacity"
rule.

---

## 6. Token-ceiling adjudication

Current state and the family precedent:

| File | Est. tokens | Threshold | Over by | Precedent |
|---|---:|---:|---:|---|
| `SKILL.md` | 3,658 | 3,500 | +4.5% | marketing shipped 3,548 |
| `references/ai-support-policy.md` | 2,939 | 2,500 | +17.6% | worst in pack |
| `references/health-and-risk-signals.md` | 2,844 | 2,500 | +13.8% | flagship |
| `references/retention-execution.md` | 2,580 | 2,500 | +3.2% | noise |
| `references/support-process-design.md` | 2,553 | 2,500 | +2.1% | noise |

**Ruling: trim `SKILL.md` below marketing's 3,548, apply two zero-cost cuts to `ai-support-policy`,
and record the remainder as a reasoned, accepted exception.** §5 of the standard is explicit that
these are engineering targets, not platform limits, and that a budget must not be met by removing
required knowledge. Everything remaining over the line is attributed evidence.

### `SKILL.md` — cut ~130 tokens, zero citations lost

- **`SKILL.md:23-30` (150 tok), the "What makes this pack different" paragraph → keep ~55.** It is a
  near-sentence-for-sentence duplicate of `SOURCES.md:13-31`, which says it better and at more
  length. Measured against §4's six functions it performs none: it does not route, supply
  non-obvious knowledge, constrain a choice, sequence, define a contract, or require validation —
  it is competitive positioning inside an agent-loaded file. **Keep the last sentence**, which names
  the flagship and the Observability Question and *is* a routing signal; drop the three-incumbent
  survey. Saves ~95.
- **`SKILL.md:42-45` (69 tok), the "Operate independently when invoked alone…" boilerplate → keep
  ~35.** Family boilerplate. The two operative clauses ("use compatible upstream artifacts without
  silently overriding established decisions" and "do not invoke adjacent skills automatically")
  survive at half the length. Saves ~34.

Result: **~3,528** — under both the review threshold's spirit and marketing's shipped precedent.

### `ai-support-policy.md` — cut ~110 tokens, zero citations lost

- **`:68-72` (99 tok), the "Two different objects share the word escalation" block → 2 lines
  (~35).** This is the *third* statement of the same rule: `SKILL.md`'s universal invariant states
  it, `support-process-design.md` §5 is the declared single disambiguation home, and this block
  explicitly says so itself ("the full disambiguation lives in support-process-design.md §5") before
  restating the content anyway. §17 warns on exactly this ("the same paragraph appears in multiple
  files"). Reduce to the rule plus the pointer. Saves ~64.
- **`:3-9` seam block (~90 of the 431-token header) → ~45.** The `ai` seam is stated at length here,
  again in the Skip-when four lines below, and again in `handoff.md` row 3. Keep the ownership
  sentence and the `ai` file path; drop the elaboration. Saves ~45.

Result: **~2,829.** Still over, and that is the correct outcome.

### Do NOT cut

- **The nine-item escalation enumeration.** This is the spec review's suggested target and I am
  overturning it. `SKILL.md:74` promises the reader "**nine real triggers, none numeric**" — the
  count is a routing fact. Merging items 3 and 5 into item 2 (which is the only defensible merge,
  since both restate content already inside item 2) would make the router row false. This is the
  automation-skill's recorded lesson verbatim: *trimming for a character limit changed a routing
  fact.* If the count must change, `SKILL.md` changes first and in the same commit — but there is no
  reason to.
- **The flagship's Dynatrace attribution** (spec review F1's explicit instruction) — an attributed
  reframe is worth more than 190 tokens.
- **The Klarna section (260 tok) or Air Canada (210 tok)** in `ai-support-policy`. Klarna's triple
  refutation *is* the R16 protected guard — compressing it is how the reversal story gets restored
  by a later reader. Air Canada is a legal precedent quoted verbatim from the tribunal.
- **`retention-execution` and `support-process-design`**, at +3.2% and +2.1%. Inside the noise band
  of a word-count heuristic; a trim here buys nothing and risks a citation.

**Note for the fixer:** the post-fixer1 pass *grew* all four over-ceiling files (+381 tokens
pack-wide, recorded at spec-review R5). Whatever the fixer adds for Q1, Q2, and MINOR-3 (~60 tokens
net) should be paid for out of the two `SKILL.md` cuts in the same commit, so the pack does not move
the wrong way a second time.

---

## 7. Lint and check-sync — classified

`scripts/check-sync` exits 0 on the shell-syntax and py-compile stages, then delegates to
`lint-skill`, which is where the failures are. (Run it as `bash scripts/check-sync`, not
`python3 scripts/check-sync`.)

**5 FAILs — all one root cause, all final-fixer scope:**
1–4. `evals/{activation,traversal,output,compression-ablation}/cases.json` still contain placeholder
cases. → §5.
5. `traversal case 'primary-route' names missing expected_references path: references/example.md`.
→ §5.2 replaces the case entirely.

**5 WARNs — all token-ceiling, adjudicated in §6.** No other lint rule fires: description carries
trigger language and opens with the outcome, no name-as-heading, no unresolved wiki links, no
platform-absolute paths, no undescribed or interactive script, every required reference is linked
directly from `SKILL.md`, and every route row carries a loading condition.

**Post-fix expectation: `lint-skill: OK` with 1 WARN** (`SKILL.md` will sit at ~3,528, still above
the 3,500 line, deliberately, matching marketing's shipped state) — or 0 WARNs if the fixer takes
another ~30 tokens out of the "Not this skill" table's explanatory halves. Either is acceptable;
do not buy the last 30 tokens out of a Contribution column.
