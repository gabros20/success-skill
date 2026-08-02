# _raw-skills-cs-packs — Channel A / Worker A2

Mandate: inventory the small/mid CS-DEDICATED packs on skills.sh (not the at-scale incumbent question —
that's A1's `_raw-skills-incumbent.md`). Method: `git clone --depth 1` every target repo into
`/tmp/claude-501/skills-a2/<owner>__<repo>`, read files directly (no skills.sh summaries trusted),
open LICENSE files directly, check package manifests. All line numbers below are from the cloned
files at the commit shown per repo. Clone date: 2026-08-02.

---

## Repo-level summary table

| Repo | Clone path | Last commit (date) | LICENSE (file opened directly) | Architecture | CS-relevant skills found |
|---|---|---|---|---|---|
| claude-office-skills/skills | `claude-office-skills_skills` | 2026-01-31 | MIT (`Copyright (c) 2026 Claude Office Skills Contributors`) | flat single SKILL.md | `customer-success/SKILL.md` (601 lines) |
| alirezarezvani/claude-skills | `alirezarezvani_claude-skills` | 2026-07-17 | MIT (`Copyright (c) 2025 Alireza Rezvani`) | SKILL.md + references/ + scripts/ + assets/ | `customer-success-manager` (business-growth), `churn-prevention` (marketing-skill), `deal-desk` (commercial), `cs-onboard`, `chief-customer-officer-advisor`, `org-health-diagnostic` |
| guia-matthieu/clawfu-skills | `guia-matthieu_clawfu-skills` | 2026-04-02 | MIT (`Copyright (c) 2026 Guia`) | flat SKILL.md per skill, worked-example heavy | `customer-success/{churn-prediction, expansion-signals, health-score-monitor, onboarding-orchestrator, qbr-preparation, renewal-management}` + `revops/account-health` |
| ncklrs/startup-os-skills | `ncklrs_startup-os-skills` | 2026-02-26 | **NO LICENSE FILE** — cite only | thin SKILL.md router + `rules/*.md` references (richest architecture found) | `customer-health-analyst`, `renewal-manager`, `cs-strategist`, `support-operations`, `onboarding-specialist`, `qbr-facilitator` |
| gtmagents/gtm-agents | `gtmagents_gtm-agents` | 2026-04-03 | Apache-2.0 | plugin/agents/commands/skills; skills themselves are ~31-line stubs | `renewal-playbooks`, `customer-feedback-taxonomy`, `voice-of-customer` (×2 locations), `escalation-framework`, `deal-desk`, `onboarding-blueprint`, `closed-loop-playbook`, `advocacy-roster-system`, `signal-correlation-workbench` |
| onewave-ai/claude-skills | `onewave-ai_claude-skills` | 2026-07-15 | MIT (`Copyright (c) 2025 OneWave AI`) | SKILL.md + references/ (rubric-heavy, evidence-conscious) | `churn-autopsy`, `renewal-predictor` |
| absolutelyskilled/absolutelyskilled | `absolutelyskilled_absolutelyskilled` | 2026-07-02 | MIT (`Copyright (c) 2026 Absolute`) | N/A | **NONE — see discrepancy note below.** Repo is 11 dev-SDLC skills (`absolute-init/-work/-spec/-ui/-simplify/-docs/-upgrade/-audit/-prune/-debt/-deflake`), zero CS content, confirmed via full `skills.yaml` (`total_skills: 11`, generated 2026-06-24). |
| manojbajaj95/claude-gtm-plugin | `manojbajaj95_claude-gtm-plugin` | 2026-05-18 | MIT (`Copyright (c) 2025 mbajaj`) | flat SKILL.md, "Part 1..9" structure | `customer-success-and-retention` (365 lines) |
| borghei/claude-skills | `borghei_claude-skills` | 2026-07-21 | **Commons Clause v1.0 + MIT** (non-standard — see below) | SKILL.md + references/scripts (near-duplicate of alirezarezvani's pack, see finding) | `customer-success-manager` (TWO copies: `sales-success/` and `business-growth/`) |
| shawnpang/startup-founder-skills | `shawnpang_startup-founder-skills` | 2026-03-16 | MIT (`Copyright (c) 2025 Shawn Pang`) | flat SKILL.md, explicit solo-founder framing | `churn-analysis` (122 lines) |
| mengto/skills | `mengto_skills` | 2026-07-28 | MIT (`Copyright (c) 2026 Meng To`) | N/A — **removed** | `customer-support-verification` **does not exist in HEAD**; HEAD commit message is literally `"Remove private customer support skills"` (2026-07-28, 4 days before this research). The skill existed (skills.sh's 140-install count is plausible pre-removal), was pulled by the author as "private," and is now cite-only-from-skills.sh-metadata, unreadable from source. |
| daffy0208/ai-dev-standards | `daffy0208_ai-dev-standards` | 2025-12-25 | MIT (`Copyright (c) 2025 AI Dev Standards Contributors`); package.json + mcp-server package.json both confirm `"license": "MIT"` | manifest.yaml + SKILL.md, code-building flavor (not just playbooks) | `customer-support-builder` (587 lines), `customer-feedback-analyzer` (469 lines), `knowledge-base-manager` (732 lines) |

**Mandate-vs-repo discrepancy count: 2 of 12 targets are absent from the named repo's current HEAD**
(absolutelyskilled's three named skills never existed per its own generated skills.yaml; mengto's skill
existed and was deliberately removed 4 days before this research). Treat both as **cite-only / do-not-lift**
regardless of skills.sh install counts — there is no source text to verify against.

---

## LICENSE detail (charter rule 3, all 5 clauses)

- **(a) Opened every LICENSE file directly**, not the GitHub API — table above. No API-vs-file
  discrepancies found this round (unlike GeoLift/prior findings cited in the charter).
- **(b) Package manifests**: only daffy0208/ai-dev-standards ships package.json files (root +
  `mcp-servers/knowledge-base-mcp/package.json`), both say `"license": "MIT"` — consistent with the
  repo LICENSE, no conflict.
- **(c) Per-skill licenses**: `daffy0208_ai-dev-standards/skills/customer-support-builder/SKILL.md:4`
  declares `license: Complete terms in LICENSE.txt` — **but no `LICENSE.txt` exists inside that skill
  folder** (checked directly, `find` returned nothing under the skill dir). Only the repo-root MIT
  `LICENSE` exists. This is a dangling per-skill license pointer; the repo-level MIT is the only thing
  that actually governs it. Minor gotcha worth flagging if we ever cite this pack.
- **(d) archived:false ≠ alive / no-license = cite only**: `ncklrs/startup-os-skills` has **no LICENSE
  file at all** — confirmed by direct `ls`/`find` at repo root. Per charter rule 3(d) this whole repo
  (including its unusually well-built `customer-health-analyst` router+references architecture) is
  **cite-only, cannot be lifted**, regardless of how good the content is. This is the single biggest
  licensing loss in the cluster — see flagship note below.
- **(e) thin-license-on-thick-IP / borghei's Commons Clause**: `borghei_claude-skills/LICENSE` full text:
  > "Commons Clause License Condition v1.0 + MIT ... the License does not grant to you, the right to
  > Sell the Software ... 'Sell' means practicing any or all of the rights granted to you under the
  > License to provide to third parties, for a fee or other consideration (including without limitation
  > fees for hosting or consulting/support services related to the Software), a product or service
  > whose value derives, entirely or substantially, from the functionality of the Software."
  > "Software: Claude Skills Library / License: MIT / Licensor: Amin Borghei (borghei)"

  **This matters for a specific reason beyond the license text itself**: `borghei_claude-skills/business-growth/customer-success-manager/` is a near-duplicate of
  `alirezarezvani_claude-skills/business-growth/skills/customer-success-manager/` — identical
  dimension names/weights, identical `python-tools: health_score_calculator.py, churn_risk_analyzer.py,
  expansion_opportunity_scorer.py` metadata line, near-identical script logic (diffed directly: same
  `DIMENSION_WEIGHTS` structure, borghei's version adds an embedded `SAMPLE_DATA` fixture and a
  "Capabilities" section not in alirezarezvani's). One of these copied (or both derive from a shared
  private template/marketplace listing) — **either way, treat this as ONE data point, not two, when
  counting "how many packs independently converge on 30/25/20/25-style weights."** It also means
  borghei has wrapped a Commons-Clause "no commercial resale" condition around content that is,
  functionally, alirezarezvani's plain-MIT design — a live instance of the charter's "thin license on
  borrowed structure" concern, worth flagging even though it's not thick published IP (book/paper) in
  the classic sense.
- Everything else: gtmagents (Apache-2.0, standard, no anomalies), all remaining MIT repos matched
  their own package manifests where present, no GPL/dual-license traps like the GeoLift case found.

---

## Architecture spectrum (flat boilerplate → router+references → code-tool)

1. **Flat, single-file, LLM-boilerplate** (no tell needed — it announces itself):
   `claude-office-skills/skills/customer-success/SKILL.md` (601 lines). YAML frontmatter with
   `capabilities: [onboarding_design, health_scoring, qbr_creation, ...]`, entirely templated content
   with placeholder tokens (`{Company Name}`, `{Feature 1}`) and fabricated "Output Example" numbers
   presented as if real (`$150,000 ROI`, `3.5x ROI`, `NPS improved from 7 to 9`). Zero citations
   anywhere in the file. `manojbajaj95/claude-gtm-plugin/skills/customer-success-and-retention/SKILL.md`
   (365 lines) is the same genre — "Part 1...Part 9" structure, invented conversion-lift numbers with
   no source (see Health Score section below).

2. **Flat SKILL.md but with explicit "what Claude does vs what you decide" / "Skill Boundaries" /
   "escalate to human" scaffolding** — architecturally more honest even though content is still
   boilerplate: the whole `guia-matthieu/clawfu-skills` customer-success cluster (6 skills,
   `health-score-monitor` 535 lines, `churn-prediction` 458, `expansion-signals` 496,
   `qbr-preparation` 421, `onboarding-orchestrator` 355, `renewal-management` 286) plus
   `revops/account-health` (472 lines). Every single one of these 7 files opens with
   `Based on **Gainsight X** and **Y**` and closes with a `## References` list of 3-4 vendor names
   (Gainsight / Totango / ChurnZero / Lincoln Murphy / SaaStr / ProfitWell) — **never a link, page, or
   specific document, just brand-name-dropping**. This is the cleanest, most reproducible instance of
   the charter's vendor-density warning (rule 5) found in this sweep: 7 files, 7 vendor-name reference
   lists, 0 traceable citations.

3. **Router + on-demand references, deepest architecture found**: `ncklrs/startup-os-skills`. Six CS
   skills (`customer-health-analyst`, `renewal-manager`, `cs-strategist`, `support-operations`,
   `onboarding-specialist`, `qbr-facilitator`), each a ~150-200 line SKILL.md pointing into 8-13
   topic-specific `rules/*.md` files (250-350 lines each). This is structurally the closest analog to
   our own faceted-router shape of anything found across all 12 targets. **Undermined by having no
   LICENSE file at all** (cite-only per rule 3d).

4. **Rubric-driven, evidence-conscious, no vendor citations, no fabricated global benchmarks**:
   `onewave-ai/claude-skills` — `churn-autopsy` and `renewal-predictor`. Distinctive trait: instead of
   citing Gainsight/ProfitWell, it teaches internal-rigor standards. Verbatim,
   `onewave-ai_claude-skills/churn-autopsy/references/standards.md:17-18`:
   > "Quantify wherever possible. 'Usage declined' is not acceptable; 'Usage declined 47% over 3 months
   > from X to Y' is."
   > "Compare to benchmarks. A 10% usage decline means nothing without context about what is normal."

   This is the one pack in the cluster that argues FOR sourcing rigor rather than performing it via
   vendor name-drop or fabricated global stat. It does not, however, justify its OWN dimension weights
   (see health-score section).

5. **Code-building flavor** (not a playbook, an app-scaffolding skill): `daffy0208/ai-dev-standards`'s
   three skills build actual support infrastructure (help centers, chatbots, ticketing, KB). Contains
   its own fabricated ratios (see below) but is functionally different from the rest — more product/
   build-tooling territory (a `success` vs `product`/`build` seam question worth flagging to the
   controller, since these skills scaffold code, not operational playbooks).

---

## HEALTH SCORE FINDING (flagship-relevant — precision over coverage per the mandate)

**Short answer: no pack in this cluster empirically justifies its weights against outcome data.
Every single weight table is asserted narrative ("why we picked this %"), not measured. The ONE
partial exception — ncklrs's `health-model-validation.md` — teaches HOW you would validate a model
(with a fully worked, explicitly fictional example), which is a genuinely more honest posture than
the rest, but even it does not defend the STARTING weights, only how you'd recalibrate them later.**

### Every distinct weight table found (verbatim, file:line)

| Source | Weights asserted | Any justification given? |
|---|---|---|
| `claude-office-skills_skills/customer-success/SKILL.md:186-244` | Product engagement 40% / Relationship 25% / Financial 20% / Sentiment 15% | None. Formula given as `scoring_formula: total: (engagement × 0.4) + (relationship × 0.25) + (financial × 0.2) + (sentiment × 0.15)` with zero rationale text anywhere near it. |
| `alirezarezvani_claude-skills/.../customer-success-manager/SKILL.md:113-118` (matches code at `scripts/health_score_calculator.py:24-28`) | Usage 30% / Engagement 25% / Support 20% / Relationship 25% | Narrative only — see next row (the references file is the one place any pack in this whole sweep attempts a "why"). |
| `alirezarezvani_claude-skills/.../references/health-scoring-framework.md:17-85` | Same 30/25/20/25, PLUS sub-weights within each dimension (e.g. Feature Adoption 40% within Usage) | **The only pack with an explicit "Why X% weight" prose line per dimension** — e.g. line 32: `"Why 30% weight: Usage is the most objective, data-driven signal... However, some customers may have seasonal usage patterns, which is why it is not weighted even higher."` This is narrative reasoning, not a cited study or backtest — no source, no sample size, no correlation coefficient given for the CURRENT weights. It DOES prescribe a real backtesting process for recalibration (`references/health-scoring-framework.md:154-160`: "Calculate the average health score of churned customers 90, 60, and 30 days before churn... Adjust thresholds so that churned customers would have been classified as Yellow or Red at least 60 days before churn") — methodologically sound advice, but explicitly a thing YOU do later, not evidence behind the shipped defaults. |
| `borghei_claude-skills/business-growth/customer-success-manager/` | Same 30/25/20/25 (near-duplicate of alirezarezvani's, see licensing note above) | Same as above — not independent. |
| `guia-matthieu_clawfu-skills/skills/customer-success/health-score-monitor/SKILL.md:77-91` | Standard "4-Pillar": Product 30-40% / Support 15-25% / Financial 20-25% / Relationship 20-25% (ranges, "adjust based on your business") | None beyond one-line heuristics ("High-touch: Increase Relationship"). Cites `Based on **Gainsight Health Score Design** and **Totango Customer Success metrics**` (line 25) with no link/method. |
| `guia-matthieu_clawfu-skills/skills/revops/account-health/SKILL.md:86-91` | Product 30% / Support 20% / Financial 25% / Relationship 25% | None. Cites `Based on **Gainsight Customer Health methodology** and **Lincoln Murphy's Customer Success principles**` (line 25), References list at line 453-458 (Gainsight / Lincoln Murphy / ChurnZero / Totango) — again, name-only. |
| `ncklrs_startup-os-skills/skills/customer-health-analyst/rules/health-score-design.md:33-40` | Product Usage 30-40% / Engagement 20-25% / Growth Signals 15-20% / Support Health 15-20% / Financial Health 5-10%, PLUS a business-model-specific table (Self-serve SaaS: Usage 45%/Engagement 15%/Growth 20%/Support 15%/Financial 5%; Enterprise SaaS: 30/30/15/15/10; Usage-based: 50/15/20/10/5; High-touch services: 20/40/15/20/5) | Most differentiated weighting scheme found (varies by business model rather than one-size-fits-all), but still asserted as "typical," no citation, no backtest shown for ANY of the four business-model variants. Also asserts unqualified: **"A well-designed health score predicts customer outcomes 60-90 days before they happen"** (line 11) — no source. |
| `onewave-ai_claude-skills/renewal-predictor/references/confidence-and-scoring.md:6-8` | Engagement 20% / Support 15% / Adoption 20% / NPS_CSAT 10% / Billing 10% / Stakeholder 10% / Usage 15% (7 dimensions) | No justification for the specific weights, BUT this is the only pack that ties **confidence** (not the score itself) to data completeness/consistency rather than claiming predictive accuracy — e.g. "If the account is less than 90 days old, cap confidence at Medium regardless of signal consistency" (line 46) and "Never score a dimension at 0 unless there is affirmative evidence of a problem — absence of data is not evidence of a problem" (line 58). This is the most epistemically honest scoring design in the cluster, even though the base weights are still unvalidated assertion. |
| `manojbajaj95_claude-gtm-plugin/.../customer-success-and-retention/SKILL.md:103-108` | Usage frequency 25% / Feature depth 20% / Engagement 20% / Satisfaction 15% / Growth 10% / Relationship 10% | None. Same file also asserts (line 49): **"Intervention when metrics dip is worth 10x intervention after cancellation request"** — a fabricated ratio with zero citation. |

### The one genuine methodology contribution: `ncklrs_startup-os-skills/skills/customer-health-analyst/rules/health-model-validation.md` (350 lines)

This is the single most sophisticated file found in the whole sweep on the SUBJECT of health-score
rigor — not because its numbers are real (they are explicitly a worked fictional example, "Q4 2024"),
but because it's the only pack that treats "does the score actually predict anything" as a first-class,
measurable question with named metrics:

`health-model-validation.md:39-47` (verbatim table header + rows):
> | Metric | Definition | Target | Red Flag |
> | **Churn Prediction Accuracy** | Predicted churns / Actual churns | >70% | <50% |
> | **Surprise Churn Rate** | Churns with health >60 / Total churns | <20% | >35% |
> | **False Positive Rate** | False at-risk / Flagged at-risk | <30% | >50% |
> | **Score-Outcome Correlation** | Pearson correlation (score, outcome) | >0.5 | <0.3 |
> | **Lift at 10%** | Top decile churn rate / Overall rate | >3x | <2x |
> | **Calibration Error** | Avg(Predicted prob - Actual prob) | <5% | >15% |

It then walks a full fictional worked example (lift-by-decile table, calibration-gap table, segment
accuracy breakdown, "surprise churn" root-cause investigation of one fictional account, drift-monitoring
dashboard) and an explicit anti-pattern list including **"Perfect-seeking — waiting for 100% accuracy vs.
iterating"** and **"Set and forget — never validating after initial launch"** (lines 343-350).
**Caveat that matters for us: this file is cite-only (repo has no LICENSE).** If our flagship
("what a health score can honestly predict") wants this validation-metric vocabulary (churn prediction
accuracy / surprise churn rate / lift-at-decile / calibration error / Pearson correlation), we should
independently source those terms from the actual ML-calibration literature (they're standard classifier
evaluation concepts, not this pack's invention) rather than lift the file itself.

---

## Falsification-strip candidates found this sweep (verbatim, file:line — never previously logged by us)

- `shawnpang_startup-founder-skills/skills/churn-analysis/SKILL.md:83`: **"30-60 day billing pause saves
  15-25% of would-be churners in B2C and 10-15% in B2B."** No source.
- `shawnpang_startup-founder-skills/skills/churn-analysis/SKILL.md:86`: **"A well-designed cancel flow
  saves 10-20% of users who initiate cancellation."** No source.
- `shawnpang_startup-founder-skills/skills/churn-analysis/SKILL.md:89`: **"Involuntary churn accounts for
  20-40% of total churn... A good dunning system recovers 30-50% of failed payments."** No source.
- `shawnpang_startup-founder-skills/skills/churn-analysis/SKILL.md:92`: **"users who left for fixable
  reasons... reactivate at 2-3x the average. Expect 5-15% overall reactivation."** No source.
- `manojbajaj95_claude-gtm-plugin/.../SKILL.md:139`: **"Voluntary churn is typically 50-70% of total.
  Involuntary is 30-50% but easier to fix."** No source (note: these two ranges don't even partition
  cleanly to 100%, a tell that they were generated independently rather than derived from one dataset).
- `manojbajaj95_claude-gtm-plugin/.../SKILL.md:82-85` (Activation Milestones table): fabricated
  conversion-lift-by-milestone numbers presented as fact — `Profile complete +8%`, `First core action
  +15%`, `First value experience +25%`, `3-day active streak +35%` — no source, no defined baseline
  for what the "+" is relative to.
- `ncklrs_startup-os-skills/skills/customer-health-analyst/rules/churn-prediction-modeling.md:11`:
  **"A well-calibrated model can reduce churn by 15-30% by enabling proactive outreach to at-risk
  accounts before they decide to leave."** No source. (Cite-only repo per no-LICENSE rule, but the
  CLAIM itself is a falsification-strip candidate regardless of repo license status.)
- `daffy0208_ai-dev-standards/skills/customer-support-builder/SKILL.md:11`: **"Good self-service systems
  can keep support needs growing at only 10-20x while user base grows 100x."** No source. Same file's
  maturity-stage self-service-rate targets (30% at 100-1K users / 60% at 1K-10K / 80% at 10K+,
  lines ~28-40 range) are likewise asserted without citation.
- `alirezarezvani_claude-skills/.../references/cs-metrics-benchmarks.md:259`: entire benchmark table
  (NRR by segment/industry/stage, GRR, logo churn, TTFV, CSM:account ratios) sourced only as
  **"Industry surveys, SaaS benchmarking reports, customer success community data (2024-2025 data
  cycles)"** — no named survey, no named report. Every number in the file (e.g. "Infrastructure/DevOps
  median NRR 125%", "HealthTech median NRR 112%", Enterprise CSM ratio "10-25 accounts") should be
  treated as unsourced and NOT cited even as a range without independent verification.
- `guia-matthieu_clawfu-skills/skills/revops/account-health/SKILL.md:381`: worked example asserts
  **"Success Probability: 40%"** for a churn-save scenario with the one-line justification "Without new
  champion, save is difficult" — a fabricated point-estimate with no model behind it, presented inside
  an otherwise-reasonable worked example.

---

## What the whole cluster consistently omits

1. **No pack anywhere in this sweep backtests its own weights against real outcome data.** Several
   (alirezarezvani's references file, ncklrs's validation file) describe HOW you would do this, as
   forward-looking advice — none present a completed backtest.
2. **No pack distinguishes "health score" from "churn-risk score" rigorously** — most treat them as the
   same artifact wearing two names (same 4-5 dimensions, same rough weight bands, just relabeled
   "risk" and inverted).
3. **Nobody addresses the AI-support-agent-era wedge** (deflection-rate honesty, bot-vs-human escalation
   policy) — zero mentions of AI chatbots as a POLICY question anywhere in these 12+ repos; daffy0208's
   `customer-support-builder` mentions "AI-powered chatbots" once as a maturity-stage feature (Stage 4,
   10K+ users) with no deflection-rate honesty discussion at all. This directly confirms wedge
   hypothesis #3 is open territory.
4. **Nobody names sample sizes, time windows, or company counts** behind any benchmark table. Every
   NRR/GRR/churn/TTFV number in every pack is presented at the same false precision (single-digit-percent
   medians) regardless of source.
5. **Solo/self-serve honesty is almost entirely absent** — the ONE exception is
   `shawnpang/startup-founder-skills/churn-analysis`, whose description explicitly targets "seed/Series A
   teams managing customers manually without dedicated CS platforms like Gainsight or ChurnZero" (line 11)
   and whose workflow assumes support inboxes/Slack/spreadsheets, not a CS platform. Every other pack in
   this cluster assumes a CSM-staffed portfolio with QBRs, executive sponsors, and dedicated CS tooling —
   confirming wedge hypothesis #1 (the CS canon here is enterprise-CSM-team literature almost without
   exception).
6. **Vendor-density is total and undifferentiated**: Gainsight, Totango, ChurnZero, Lincoln Murphy, and
   SaaStr are cited by name (never linked, never quoted, never dated) across at least 4 of the 12 repos
   (guia-matthieu ×7 files, ncklrs implicitly via "industry standard" language, alirezarezvani, manojbajaj95).
   No pack cites an academic paper, a company's own published cohort data, or anything with a URL.

---

## Source links (repo level, for the record)

- https://github.com/claude-office-skills/skills
- https://github.com/alirezarezvani/claude-skills
- https://github.com/guia-matthieu/clawfu-skills
- https://github.com/ncklrs/startup-os-skills (no LICENSE)
- https://github.com/gtmagents/gtm-agents
- https://github.com/onewave-ai/claude-skills
- https://github.com/absolutelyskilled/absolutelyskilled (no CS content at HEAD)
- https://github.com/manojbajaj95/claude-gtm-plugin
- https://github.com/borghei/claude-skills (Commons Clause + MIT)
- https://github.com/shawnpang/startup-founder-skills
- https://github.com/mengto/skills (CS skill removed 2026-07-28, commit `46abf78`)
- https://github.com/daffy0208/ai-dev-standards
