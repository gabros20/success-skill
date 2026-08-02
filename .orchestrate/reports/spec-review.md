# Spec review — success-skill

Date: 2026-08-02 · Reviewer: spec review (opus) · Snapshot reviewed: 9f0dcc6
Read in full: `research/synthesis.md`, `.orchestrate/inventory.md`, `.orchestrate/reports/integrator-report.md`,
all 15 references + SKILL.md + 4 assets + `SOURCES.md`; 12 raws consulted for tracing; 8 sibling
pack files opened directly to verify line citations.

**Verdict: 2 BLOCKERS, 5 S-MAJOR, 11 MINOR.** The pack's evidence spine is genuinely strong — the
four-study convergence table, the GitLab exhibit, the honest-ceilings section, the Air Canada
anchor, and every academic method line trace exactly to primary text. The blockers are both
provenance failures (a permalink that does not contain the claim it is cited for; a figure ordering
reversed against the filing), not doctrine failures. Nothing here requires re-architecting a file.

Fact-check tally: **70 claims traced. 58 PASS · 4 FAIL-wrong · 1 FAIL-form · 7 DRIFT.**

---

## BLOCKERS

### B1 — A load-bearing permalink does not contain the claim it is cited for (2 files)

`references/when-success-applies.md:87-88`:
> tylertringas folds a "shared support inbox" into an agent loop that auto-triages and auto-fixes
> (https://x.com/tylertringas/status/2074889104823664653, Jul 8 2026)

`references/surface-selfserve-solo.md:33-35` carries the same permalink for "an agent loop that
monitors errors, auto-pushes fixes, and reports back in Slack."

**Evidence.** `research/_raw/_raw-x-solo-support.md:165-170` shows what tweet `2074889104823664653`
(2026-07-08) actually says — a list of what an in-house monolith handles, including a "**shared
support inbox**." The agent-loop content is a *different tweet*, `_raw-x-solo-support.md:172-177`:
"bugs and stability is a bunch of agent loops monitoring performance and errors and automatically
pushing fixes… agents just check it and create PRs automatically (and report back in slack when
fixed)" — **2026-07-16, https://x.com/tylertringas/status/2077828747752005676**.

Additionally, "auto-triages" appears in neither tweet. The loops monitor performance/errors and
create PRs from a Slack bug-report channel; nothing describes support-ticket triage.

**Why blocker.** R20 makes false permalink provenance top-severity ("a reconstructed permalink is a
fabricated citation that survives review"). This is one of exactly two exhibits carrying P2's
mechanism correction — "the solo replacement for CS process is PRICING first, **AI tier-1 support
second**" — which the synthesis explicitly ships CONTESTED and which the router row promises. A
reader who opens the cited permalink to check the pack's most-hedged plank finds it does not support
the sentence.

**Fix.** Cite both permalinks (the inbox from `2074889104823664653`, the agent loop from
`2077828747752005676`, Jul 16 2026); drop "auto-triages."

### B2 — HubSpot's NRR trend is reported in reversed order, in a reference and in a runnable asset

`references/renewals-and-expansion.md:66-67`:
> Reported 102.2% / 103.9% / 110.3% across three fiscal years (**oldest to newest**).

`assets/nrr_calc.py:46`:
> Reported (3 most recent fiscal years, **oldest first**): 102.2% / 103.9% / 110.3%.

**Evidence.** `research/_raw/_raw-web-canon-commercial.md:225-226`, from the extracted filing text:
> Reported (3-year trend in the same filing): "Net Revenue Retention 102.2% 103.9% 110.3%"
> (**most-recent-first** across three fiscal years).

As shipped, the pack asserts HubSpot's NRR *rose* 102.2 → 110.3. The filing shows it *fell*
110.3 → 102.2. The four-SEC-definitions section is the pack's own strongest measured-with-method
claim and the mandate's named must-check; the error is then duplicated into the docstring of the
asset that implements it.

**Fix.** One word in each place: "most recent first."

---

## S-MAJOR

### S1 — A CITE-ONLY source's paraphrase is presented as its quotation

`references/education-and-knowledge-base.md:59-64` introduces the block with "the prose license is
scoped to 'the GitLab Software,' not the handbook content, so describe and link, **never reproduce
verbatim**" — and then renders as a GitLab blockquote:

> Knowledge Articles are **reactive** — ticket-triggered, for a specific broken-in-this-config
> problem. Documentation is **proactive** — feature-complete, for learning intended behavior. "When
> in doubt, create a knowledge article… it can always be promoted to documentation."

**Evidence.** `research/_raw/_raw-gh-ai-support-kb.md:318-322` quotes only the final sentence. The
reactive/proactive sentences are the researcher's own summary, italicised in the raw, not GitLab
prose. GitLab is CITE-ONLY (synthesis §6; `SOURCES.md:90-96`). So the file (a) contradicts its own
stated rule in the next line, and (b) attributes to a CITE-ONLY source words it did not write.

**Fix.** Un-blockquote the two paraphrase sentences into the file's own prose; keep the one real
quotation, which is short, attributed, and fine.

### S2 — Two GitLab measures assigned to the wrong PROVE group

`references/surface-b2b-high-touch.md:76-78`:
> Three of four Voice-of-Customer measures (CSAT, NPS Surveys, two Engagement measures) are marked
> "Not started" in GitLab's own maturity column

**Evidence.** `research/_raw/_raw-gh-gitlab-cs-handbook.md:172-181` maturity table: VoC rows are
Support-CSAT (Not started), NPS Surveys (Not started), Support-Engagement (70%). Executive
Sponsorship / Events / Certifications are rows of the **Engagement** group (10%), a different group
in the same table. The parenthetical names four items to support a "three of four" count and
misassigns two of them.

Related DRIFT, lower severity: `health-and-risk-signals.md:157` says "the VoC group (5%) is
three-quarters unbuilt." That inherits the raw's own "three of its four measures are unbuilt"
phrasing (`:183`), which the raw's own table shows as two-of-three. Correcting b2b should correct
the flagship's fraction at the same time.

### S3 — Broken GitHub handle inside a shipped asset's licence attribution

`assets/nrr_calc.py:55` cites the reference implementation as `0x416d6982/pypulate`.
`SOURCES.md:81` and all three research occurrences say `0x416d6972/pypulate`. One character off in
an owner handle is a citation that does not resolve — and it sits on the line that establishes the
MIT grant under which the asset's arithmetic was modelled.

### S4 — The figure-class rule is applied unevenly; three surviving bare figures do no work

The integrator correctly stripped 76% / 68% / an ARR-per-CSM figure from a routing pointer. Three
survivals of the same class remain, and I did not find a principle that separates them:

| Location | Figure | Why it fails the class test |
|---|---|---|
| `health-and-risk-signals.md:41-42` | "62% precision, 58% recall" | Synthesis §3 row 12 names health-score accuracy claims a never-ship class. The teaching here is that pulserevops' *citations* are NIH/CDC/WHO/JAMA — medical sources for a SaaS score. The digits contribute nothing and are exactly the shape that gets re-quoted. |
| `renewals-and-expansion.md:108-110` | "80–85% of plan allotment", "converts to seat expansion at 65%", "20% increase in upsell opportunities" | §5's own verdict is "none cites a study, a company, an n, or a method." These are bare figures shipped inside the sentence forbidding them — the operate/growth lesson verbatim. |
| `renewals-and-expansion.md:73, 80` | a bare "131%"; "~105% to ~101%" | The raw flags 131% as WebSearch-synthesised and unverified (`_raw-web-canon-commercial.md:252`); the median-decline pair is shipped under "method-unknown," and a disclaimed figure is still a figure. |

Keep (my ruling, see F5 below): the 96% (`voice-of-customer.md`), the ReverendBayes arithmetic
(`health-and-risk-signals.md:96-100`), the $2M/CSM propagation exhibit
(`surface-b2b-high-touch.md:116-123`), and Klarna's `$40M / 25%` (`ai-support-policy.md:164`) — the
last because it is the claim the reader will meet verbatim and must be able to identify as
never-audited, which is the whole point of that paragraph.

### S5 — A "ship none of its content" sentence that ships its content

`references/retention-execution.md:95-99`:
> `growth/references/monetization-and-pricing-experiments.md` §5 already ships the dark-patterns
> evidence… — Mathur et al. (CSCW 2019, 11.1% of 11,000 crawled sites…), the **roach motel** pattern
> name…, and the FTC's 2022 enforcement signal (the Vonage $100M negative-option settlement). Cite
> that file; ship none of its content here.

The three data points verify exactly against `growth/.../monetization-and-pricing-experiments.md:146-155`
— the facts are right. The sentence is false about itself, and it is the pack's own model for how a
cite-don't-restate seam should read (ruling: cancellation ethics = pointer only). Either restate to
"the mechanism, not the evidence, is summarised here" or drop the three figures and keep the
pointer.

---

## MINOR (11)

1. **Quotation fidelity, three sites.** `support-process-design.md:117-119` quotes tylertringas'
   LIFO tactic as "…so at least some customers get exceptionally fast support rather than all of
   them getting the average"; verbatim (`_raw-x-solo-topup.md`) is "so at least some customers
   **will** get exceptionally fast support rather than all of them getting the (**probably not
   great**) average **response time**." · `support-process-design.md:142-143` drops "across GitLab"
   from "Visibility across GitLab, up to and including the CEO…" · `surface-b2b-high-touch.md:100-101`
   drops "/ experience" from "didn't see / experience value."
2. **`voice-of-customer.md:99-101`** — "the strongest single *customer-feedback* correlate of actual
   retention explains roughly 4% of variance." 4% is tenure's (.199² ≈ 3.96%), and tenure is not a
   feedback metric; the best feedback metric is top-2-box .184 ≈ 3.4%
   (`_raw-web-lead-cfm-evidence.md:234`). The conclusion ("a single score is close to noise") is
   unaffected.
3. **`voice-of-customer.md:124-126`** presents the stake-dependent range as "TARP's own breakdown."
   `_raw-web-falsification-churn-evidence.md:103-109` is explicit that primary text was never
   obtained and this is convergent secondary paraphrase.
4. **`retention-execution.md:122`** describes one launch as two ("a photorealism model upgrade, a v2
   launch"); the tweet says "Interior AI v2 launched and it outputs are way better… Photorealistic
   interiors."
5. **`retention-execution.md:115`** calls the Nov 22 2017 tweet "confirmation it shipped"; the quoted
   text is "i'll add a PAUSE button to subscription soon!" — an intent statement. The raw's own
   header over-reads it identically, so the pack inherits rather than introduces this.
6. **`health-and-risk-signals.md:78`** — "93 Dutch **B2C** firms." The raw says "Dutch service firms"
   across 18 industries; B2C is an inference, not the paper's scope word.
7. **`health-and-risk-signals.md:79`** splices van Doorn's abstract and discussion into one quoted
   string across an ellipsis ("equally poor for predicting *future* sales growth… no single best
   metric" — two separate sentences, two separate sections).
8. **`ai-support-policy.md:164`** — "~700 agents" compresses "the equivalent work of 700 full-time
   agents"; the raw flags the unreconciled 700-vs-3,000 discrepancy
   (`_raw-web-supportops-ai-agents.md:337-342`).
9. **`ai-support-policy.md:146-147`** cites "Yao et al. 2024 and the SABER error-taxonomy paper"; the
   raw's licence note requires Barres et al. 2025 as well (`_raw-gh-ai-support-kb.md:78-79`,
   restated at `SOURCES.md:74` in the same partial form).
10. **Permalink dating is inconsistent.** `support-process-design.md:116,118,121` and
    `surface-b2b-high-touch.md:119-122,142,145` ship X permalinks with no date; every other file
    dates them. R20 doesn't require dates, but the pack's own convention does.
11. **`nrr_calc.py`** — `--mode monthly_cohort_annualized --values 1.02 1.03 1.04` raises a bare
    `ValueError` because the flag is split into halves internally; an odd-length list should be an
    argparse error. Same class as F4, not a correctness defect.

---

## Never-ship enforcement — full sweep result

Grepped the whole pack (SKILL.md + 15 refs + 4 assets) for every synthesis §3 string *and* judged
figure-class on every bare number and dollar figure found (85 numeric tokens reviewed).

- **Clean:** 5–25×, 5%→25–95%, 80/20, $1-vs-$6, CES-superiority-as-fact, NPS-best-predictor-as-fact,
  76%, 68%, any bare `N hour (P1)` SLA default. `SKILL.md` ships no figure at all.
- **Present and correct:** the NPS and CES claims appear only with their replication failures
  attached (`voice-of-customer.md:60-79`); the unsourced-SLA-default class is taught with the
  first-party ground-zero example named (`support-process-design.md:103-109`).
- **Present and adjudicated:** see S4.

**The integrator's two documented survivals:**
- **$2M ARR per CSM propagation exhibit (`surface-b2b-high-touch.md:116-123`) — UPHELD.** Synthesis
  §3 sanctions exactly this use, both the debunking (2 permalinks) and the re-circulation (2
  permalinks) are in the same bullet, and `renewals-and-expansion.md:148-150` correctly routes to it
  as the only permitted home. Verified against `_raw-x-cs-canon.md`.
- **96% (`voice-of-customer.md:122-128`) — UPHELD.** Synthesis §3 row 4's ship rule is "never ship
  the 96%" *as a claim*; the corrected stake-dependent range is what the row mandates teaching, and
  a reader cannot correct a figure they cannot recognise. But see S4: the rule the integrator
  applied is right and should be stated once, not left as an asymmetry — because as written it does
  not catch three other survivals.

---

## Precision guards (R16) — all six present, none weakened

| Guard | Where | State |
|---|---|---|
| "not published, never not measured" | `health-and-risk-signals.md:37` (heading), `:51`; `SKILL.md:115-117` | Verbatim, with "absence of disclosure isn't proof of inaccuracy" attached in both places |
| `user_mood` recorded, never a trigger | `ai-support-policy.md:87-94` | Strongest form in the pack: marked "Precision guard, protected," names the `frustrated`/`should_redirect:true` worked example as the trap, and adds "Never report this as 'escalates on frustration'" |
| No Klarna reversal narrative | `ai-support-policy.md:160-171`, Validation `:193`, failure mode `:202` | Never told; triple refutation stated; tier-design lesson substituted |
| Pricing plank CONTESTED-marked | `when-success-applies.md:101-104`, `:129`; `SKILL.md:70`; echoed in `retention-execution.md:23,142-144` and `surface-selfserve-solo.md:81` | Marked at every mention, with the one-sidedness stated as "evidence *for* a reframe, not proof of a settled contest" |
| levelsio cancel-flow CONFOUNDED | `retention-execution.md:118-129`, Validation `:153-154`, failure mode `:163-164` | Flagged, with the "I guess" hedge shipped verbatim as the model |
| Murphy formula in CURRENT form only | `onboarding-and-adoption.md:85-88`, `:121`, `:130` | Current "Goal + AX"; the superseded form named and dated pre-2024. Verified against `_raw-web-canon-commercial.md:68-73` |

---

## Seam rulings R1–R12 — conformance

All twelve implemented where inventory §1 places them. Verified by opening the sibling files, not by
trusting the integrator's table:

- **R1 onboarding** — `onboarding-and-adoption.md` opens with the seam, quotes design's
  orient-don't-educate rule from `journeys.md:51-53`, consumes TTFV from `surface-app-saas.md:35-36`
  (verified verbatim). ✓
- **R2 renewal/expansion** — three verbs/three owners at `renewals-and-expansion.md:45-51`, sales
  clause marked provisional there and again at `:116-123` and `handoff.md:40`. ✓
- **R3 VoC** — `voice-of-customer.md:50-58` cites design, product, and growth by pack + filename +
  line and claims *only* interpretation and aggregate trend. ✓
- **R4 involuntary churn** — `email-compliance-checklist.md:82` cited by line in
  `retention-execution.md:25-27,133` and `surface-mobile-subscription.md:69`; verified on disk
  ("Dunning / billing-failure recovery → `product`"). ✓
- **R5 advocacy** — `renewals-and-expansion.md:125-131`: success qualifies + consents, marketing
  produces. ✓
- **R6 community retention** — `handoff.md:71-77` closes the fork and says it is closing it;
  `organic-social-and-community.md:17-18` verified as the open fork. ✓
- **R7 incident comms** — co-ownership stated three times, sole ownership never claimed; operate's
  `incident-response.md:159` quoted verbatim and confirmed on disk. ✓
- **R8 AI-support** — the split is stated as "by content" with `ai` ceding nothing
  (`ai-support-policy.md:5-9`); parlant Apache-2.0 and claude-quickstarts under its **renamed** name
  both cited. ✓
- **R9 retention execution** — reserved name used; the third box drawn in both
  `retention-execution.md:51-60` and `handoff.md:79-89`; growth's binary rule cited at
  `retention-and-resurrection.md:168-169`, verified verbatim. ✓
- **R10 escalation vocabulary** — `support-process-design.md:124-144` is the single disambiguation
  home; every other site states the rule and points there. Zero unqualified uses survive outside a
  file whose local context fixes the sense. ✓
- **R11 support-ticket PII** — `SKILL.md:104` inherits data's free-text-PII constraint rather than
  inventing one. ✓
- **R12 automation refund gate** — stated in `handoff.md:63-69` and `overlay-agentic.md`; both halves
  named. ✓

**Growth cited provisional, marketing flat** — held correctly and *named as a discipline*
(`handoff.md:37` "cited provisional, matching growth's own hedge on this row, not flattened to
marketing's confidence"; failure mode at `:93-95`). **Cancellation ethics** — pointer only, one
operative test added (one-click-reachable), no content beyond the S5 sentence. **Escalation
qualified** — see R10.

---

## Licensing — 8 citations spot-checked

| Source | SOURCES.md verdict | Use in pack | Verdict |
|---|---|---|---|
| GitLab handbook | CITE-ONLY | Short attributed excerpts in flagship, b2b, KB, support-process | **S1** on the KB blockquote; the other excerpts are short, attributed, and consistent with SOURCES.md's stated "quotes only short excerpts" policy |
| Chatwoot `enterprise/` (Captain) | CITE-ONLY | `ai-support-policy.md:46-51` | Clean — states outright it is "describing the pattern, not quoting the template." Re-grepped for template/liquid syntax: no hits |
| AGPL stacks (Zammad/Frappe/libredesk/FreeScout) | CITE-ONLY, naming only | `support-process-design.md:38-92` | Clean — field names and schema shapes only, each marked (Frappe explicitly "AGPL-3.0 — structure/naming LIFTABLE as ideas, not code") |
| GLPI | CITE-ONLY, structural | `support-process-design.md:149-154` | Clean — marked "GPL-3.0, structure-only" |
| `usertour` | AMBIGUOUS, nothing lifted | `health_score_audit.md` row 10 | Clean — cited as a modelling idea, licence ambiguity stated inline, no code |
| `uvdesk`, `HELPDESK.AI` | AMBIGUOUS, do not touch | — | Clean — zero occurrences pack-wide |
| `pypulate` | LIFTABLE MIT | `nrr_calc.py` | **S3** — owner handle wrong by one character |
| `dynatrace-oss/CustomerSuccess` | LIFTABLE Apache-2.0 | flagship §6, audit row 9 | Clean and accurate — the four 25-point components, the 10-users/5-apps thresholds, "no outcome variable joined," and the Gaps-&-Actions action string all verified against `_raw-gh-voc-onboarding-csops.md:566-599` |

No CITE-ONLY source is quoted verbatim beyond short attributed excerpts, except the S1 case, where
the problem is that a *paraphrase* is dressed as a quotation.

---

## Assets — all four run; self-tests pass

| Asset | Bare run | Import | CLI | Docstring honesty vs. refs |
|---|---|---|---|---|
| `churn_baseline_check.py` | "Self-tests passed" | OK | `--total 3333 --churners 483 --headline-accuracy 94.60 --recall 0.7423` → baseline 85.51%, lift +9.09pp, misses 25.77%, verdict WEAK. Reproduces flagship §5 exactly | Matches. `--concordance 0.93` → "FLAG… above the honest range (0.55–0.75)… check for a covariate that encodes elapsed duration" — the flagship's `TotalCharges` lesson, correctly generalised |
| `sla_capacity_calc.py` | "self-test PASS" (three anchors) | OK | `--window 09:00-17:00 --tickets-per-day 50 …` → 16h ceiling, utilization 1.562, OVERLOADED | Best docstring honesty in the pack: output states "this is not a recommended SLA; it is a geometric fact," and the dvassallo threshold ships as "don't transplant the number, only the shape of the decision" |
| `nrr_calc.py` | argparse usage error (F4) | OK — self-tests run at import | 6 modes exercised; `snowflake_2yr_snapshot 126 100` → 79.37% correct | "Never compare this figure to a result computed under a different mode" printed on every run — matches renewals §2. **But** carries B2 and S3 in its docstring |
| `health_score_audit.md` | n/a (checklist) | n/a | n/a | 10 rows as SKILL.md promises; rows 1–2 correctly gate the "Do not present as validated" verdict; licence honesty on the usertour row is exemplary |

---

## Adjudications on the integrator's flags

**F3 (kept duplication, flagship §7 ↔ b2b §3) — UPHELD.** I re-verified both against
`_raw-gh-gitlab-cs-handbook.md:218-243`: expiry half-lives, switched-off measures, and the
tie-breaker rule agree exactly, no drift. The ablation argument is the deciding one — the default
reader is self-serve solo and is routed *away* from the b2b surface, so stripping §7's numbers would
leave that reader with "inputs should expire" and the half-lives behind a file they were told to
skip. Framings differ correctly. Removing the PROVE weights was the right single cut.

**F5 (96%/76% asymmetry) — PARTIALLY OVERTURNED.** The integrator's instinct is right but the rule
is stated as an exception rather than a principle, which is why it doesn't catch S4's three cases.
The rule that works, and that I'd have the fixer state once:

> A figure may ship when (a) the reader will meet it verbatim and must be able to recognise and
> correct it, (b) its arithmetic *is* the teaching, or (c) both sides are permalinked as a
> propagation exhibit. It may not ship when the digits do no work beyond being re-quotable.

That keeps 96%, the ReverendBayes pair, and $2M/CSM; it removes the pulserevops 62/58, the three
expansion-folklore percentages, and the 131% / 105→101 pair.

**F6 (growth "reserved job name") — UPHELD; widen the citation.** I read the line myself.
`growth/references/handoff.md:66` is verbatim: "Reading this pack's absence of `acquisition` and
`retention-execution` jobs as an oversight instead of the AARRR seam stated above." So growth does
use the literal string as a job name, and does state that its absence is deliberate — "names the
slot and builds nothing into it" is accurate, not generous. What :66-67 does *not* carry is the
"for **this pack**" half; that lives at `handoff.md:43` (the `success` (provisional) row) and in the
AARRR note at `:47-49` ("`success` owns Retention *execution*"). Cite `growth/references/handoff.md:43,66`
in `retention-execution.md:53` and `handoff.md:81`. Substance holds; the line range is too narrow
for what it is asked to prove.

**F1 (token ceilings) — not ship-blocking.** In-family per marketing's 3,548 precedent. If the fixer
must cut, `ai-support-policy.md` (+15%, worst in pack) is the target and the nine-item escalation
enumeration compresses without losing a routing fact. Do not cut the flagship's Dynatrace
attribution to buy budget — an attributed reframe is worth more than 190 tokens.

**F2 (evals placeholders) — confirmed on disk.** `python3 scripts/lint-skill` reproduces exactly:
4 placeholder FAILs plus `traversal case 'primary-route' names missing expected_references path:
references/example.md`. Final-fixer work, not a regression.

**F4 (`nrr_calc.py` bare run) — confirmed, cosmetic.** Self-tests do run at import; all six CLI
modes work. See MINOR 11 for the adjacent argparse wart.

**F7 (sibling PRs) — confirmed still true.** `operate/references/handoff.md:79` names only `product`
on the decommission row; `incident-and-account-comms.md` documents it honestly as operate's known,
queued issue rather than as evidence against success's claim. Correct handling.

---

## Deviation from the gate that I am UPHOLDING against the inventory

**τ-bench numbers deliberately dropped.** Inventory row 5 and synthesis P3 both mandate shipping
"gpt-4o <50%, pass^8 <25% retail vs vendor 70–90%." `ai-support-policy.md:144-158` ships the pass^k
*mechanism* and explicitly instructs "**Cite the mechanism, never the specific published numbers**."

**The pack is right and the gate is wrong.** `_raw-gh-ai-support-kb.md:43-45` says of the very table
those numbers come from: "never trust the README table — it's frozen at 2024 models and the retail
table has literal '??' cells," and `:69-70` instructs "Cite this mechanism (not the specific numbers,
which the vendor itself calls stale)." Synthesis's own preamble — "where this document and a report
disagree, the report's raw evidence wins" — makes this the correct call, and the writer independently
supplied the two reasons (the v1.0.1 grading-comparability warning and SABER's 75+ task fixes, both
verified verbatim at `_raw-gh-ai-support-kb.md:20-27`). Record it as a gate correction, not a gap.

---

## Router (R18) spot-check

All 15 references and 4 assets are linked from SKILL.md; zero broken links pack-wide (re-verified
programmatically, including the digit-bearing `surface-b2b-high-touch.md` path the integrator's
regex class would have missed). Description is 591 chars, under the 600 ceiling, and the word
"prioritization" is genuinely absent. Row promises I re-walked independently and confirmed reach
their content: the Existence Gate row, the flagship row (all six named concepts present verbatim
where the guard requires verbatim), the response-time-promise row, the third-box row, the four-NRR
row, and the `internal`-bucket row.

**Independent verification of the pack's sharpest self-claim:** I re-ran the orphan grep myself
across all twelve shipped sibling packs for a customer-facing response-time promise — **zero hits**;
the only prior mention family-wide is `webdesign/references/niche-and-vertical-design.md:148-156`,
which I opened and confirmed contains "explicit response-time commitments" and "staged intake
(routing-critical fields first)" in the healthcare block. The integrator's `design` → `webdesign`
pack correction was load-bearing and is correct.

---

# RE-VERIFY PASS — 2026-08-02 (post-fixer1)

Method: `git diff 9f0dcc6 -- skills/` read span-by-span (12 files, +100/−76), every changed factual
claim re-traced to the named raw, all four assets re-run, never-ship class re-swept pack-wide, lint
and link graph re-checked. I did not accept the fixer's counts or dates — each was re-derived.

**Verdict: NOT-CLEAR — 2 one-line residuals.** Both blockers and all five S-MAJOR findings landed.
Two items are incompletely applied, neither ship-blocking, both single-line.

## Blockers — CONFIRMED FIXED

**B1 — resolved, both files.** `when-success-applies.md:87-90` and `surface-selfserve-solo.md:33-37`
now split the claim across its two real sources: the "shared support inbox" phrase to
`/2074889104823664653` (Jul 8 2026) and the agent loop to `/2077828747752005676` (Jul 16 2026).
Both re-checked against `_raw-x-solo-support.md:166-177`; the new tweet's date verifies as
`2026-07-16` in the raw. "auto-triages" is gone pack-wide (grep: zero hits).

**B2 — resolved, both sites.** `renewals-and-expansion.md:66-67` and `nrr_calc.py:46` now read
"most recent first," matching `_raw-web-canon-commercial.md:225`. Grep for `oldest first` /
`oldest to newest`: zero hits. The asset's HubSpot-convention self-test still reproduces 110.3%.

## S-MAJOR — all five landed; two carry residuals

**S1 — substantially fixed, two residuals.** The paraphrase is no longer blockquoted; only GitLab's
real sentence is (`education-and-knowledge-base.md:47-52`). Residual R3 below.

**S2 — CORRECT, independently re-derived.** I re-counted from
`_raw-gh-gitlab-cs-handbook.md:172-181` without reference to either party's claim. The maturity
table carries exactly **three** VoC rows — Support-CSAT (Not started), NPS Surveys (Not started),
Support-Engagement (70%) — so **two of three unbuilt** is what the recorded evidence supports.
Executive Sponsorship / Events / Certifications are Engagement rows. The raw's own prose at `:183`
("three of its four measures are unbuilt") is contradicted by its own table and was the source of
the error; the fixer corrected in the right direction, and `surface-b2b-high-touch.md:76-79` plus
`health-and-risk-signals.md:160-161` now agree. Cross-checked against the PROVE block at `:50`
("Voice of the customer (VoC): Support + Surveys: 5%"), which decomposes cleanly into those three
rows. *Recorded caveat:* "only Support-Engagement (70%) is live" asserts the VoC row set is
exhaustive, where the raw introduces the table as "several measures… marked Not started" — a
selection. The PROVE decomposition makes the inference sound; it is an inference, not a quotation.

**S3 — fixed.** `nrr_calc.py:55` now `0x416d6972/pypulate`, matching `SOURCES.md:81` and all three
research occurrences. Grep for the old handle: zero hits.

**S4 — two of three fully applied; one incomplete (residual R1).**
- Expansion folklore (80–85% / 65% / 20%) — **digits gone**, three claim-shapes preserved
  (`renewals-and-expansion.md:109-113`). Verified no figure survives.
- 131% and 105%→101% — **gone from the reference.** The comparison now runs between two
  primary-verified figures already established earlier in the same file (Snowflake 126% vs Datadog
  "above 130%"), which is a better fix than removal. The median-decline sentence keeps the
  claim-shape and drops the digits; "benchmarking-service… softened across 2021–2024" matches
  `_raw-web-canon-commercial.md:271`.
- pulserevops 62%/58% — **kept, upheld.** The rewrite now names the URL, states the digits are
  fabricated-citation bait, and says "the tell is the source list, not the number itself." That is
  R21's recognise-and-correct branch applied with the rule stated, and it is stronger than what I
  reviewed. Numbers, URL, and the NIH/CDC/WHO/JAMA source list all re-verified against
  `_raw-web-falsification-churn-evidence.md:137,171`.

**S5 — self-contradiction removed, but the replacement mislabels the evidence (residual R2).**

## MINOR — 11/11 applied and verified

Quotation fidelity: LIFO quote now verbatim including "will" and "(probably not great) average
response time"; "across GitLab" restored; "didn't see / experience value" restored — all three
re-checked against source. · VoC ceiling correctly reattributed to top-2-box r≈.184 ≈ 3.4%, with
tenure's ~4% marked as non-feedback (`_raw-web-lead-cfm-evidence.md:234`). · TARP now states the
primary was never located and the range is convergent secondary paraphrase (`…churn-evidence.md:105`).
· One Interior AI v2 launch, and the levelsio quote is now closer to verbatim. · Pause button now
"an intent-to-build reply… not confirmation it actually shipped" — correct; the tweet is
future-tense. · "93 Dutch service firms across 18 industries" matches `…cfm-evidence.md:136-138`. ·
van Doorn un-spliced into its two real sources (abstract `:269`, discussion `:277`). · Klarna
700-vs-3000 discrepancy now surfaced. · Barres et al. 2025 added.

**All ten newly added permalink dates independently verified** — nine against raw prose, and
lincolnmurphy `1084526744290369537` against the projected JSON (`Sun Jan 13 19:05:00 +0000 2019`).
No fabricated date.

## Assets — 4/4 green, no regression

3/3 Python modules import with self-tests passing. All six `nrr_calc` modes exercised: `grr` → 85.00%
and `arr_bridge_nrr` → 105.00% reproduce pypulate's documented anchors exactly. The odd-length
`--values` case now exits **2** with a clean argparse message (was exit 1 + traceback — confirmed by
running the pre-fix file from `9f0dcc6`). `churn_baseline_check` and `sla_capacity_calc` reproduce
their anchors unchanged.

## No new figures or drift introduced

Full percentage re-sweep across all references: the only figures not present pre-fix are `3.4%` /
`4%` (de Haan, measured-with-method, already in the flagship table) and `70%` (the Support-Engagement
maturity value, verbatim from the raw table). Every never-ship string still absent. "96%" occurrence
count unchanged at five. 15 references still linked from SKILL.md; zero broken links.

## Residuals

**R1 — S4 incompletely propagated to the asset.** `assets/nrr_calc.py:9` still reads "A reported
126% and a reported **131%** computed under different mechanics are not the same quantity." The
reference was fixed; the asset docstring carrying the identical unverified figure was not — even
though B2 *was* propagated to this same file. The fixer's grep checked only the artifacts it had
listed, so this survived. One-line fix: mirror the reference's Snowflake-vs-Datadog wording.

**R2 — fix-introduced evidence-grade error.** `retention-execution.md:96-97` now calls Mathur et al.
(CSCW 2019, peer-reviewed, real n) and the Vonage settlement "the sanctioned recognise-and-correct
strip." R21's recognise-and-correct branch is for figures that are *wrong and circulating*; these are
correct, sourced figures lifted from growth's own file. The self-contradiction is gone, but R14's
grading discipline is now violated in its place. Suggested: "summarised here for continuity; growth's
file owns the argument and its citations."

**R3 (cosmetic, S1 leftovers).** (a) The framing sentence still says "describe and link, never
reproduce verbatim" immediately before a verbatim blockquote — SOURCES.md permits short attributed
excerpts, so the practice is fine and the sentence overstates its own rule. (b) "(researcher's own
summary of the distinction, not GitLab's wording)" leaks build-process vocabulary into reader-facing
content; a reader of the shipped skill has no referent for "the researcher." Prefer "paraphrased
here, not GitLab's wording."

**R4 (cosmetic, MINOR 10 leftover).** `renewals-and-expansion.md:122-123` still carries the two
lincolnmurphy permalinks undated, while the same IDs were dated in `surface-b2b-high-touch.md`. Both
dates are now verified (Jan 13 2019, 18:48 and 19:05 UTC).

**R5 (note, not a finding).** All four over-ceiling files grew: `ai-support-policy` 2876→2939,
`health-and-risk-signals` 2764→2844, `retention-execution` 2521→2583, `support-process-design`
2530→2553 (+381 pack-wide). No new threshold crossed, but F1 moved the wrong way. Lint output is
otherwise byte-identical to the pre-fix run — the same five FAILs, all F2 eval-placeholder items.

## Second gate correction to record

The pause-button fix (MINOR 5) makes the pack contradict synthesis §8's "pause-subscription arc
(2015 idea→2017 ship)". The pack is now **more accurate than the gate** — the Nov 2017 tweet is
future-tense intent ("i'll add a PAUSE button to subscription soon!"), and the raw's own "Confirmation
it got built" header over-reads its own quotation. Recording this alongside the τ-bench correction so
a later reader does not restore the gate's version.
