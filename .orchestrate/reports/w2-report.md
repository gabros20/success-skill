# W2 report — support-process-design, education-and-knowledge-base, sla_capacity_calc.py

## Files written

| File | Est. tokens | Budget |
|---|---:|---:|
| `skills/success/references/support-process-design.md` | 2,495 | 2,400 (ceiling 2,500) |
| `skills/success/references/education-and-knowledge-base.md` | 2,136 | 2,200 (ceiling 2,500) |
| `skills/success/assets/sla_capacity_calc.py` | — | runnable, self-testing |

Estimates via `scripts/count-skill-tokens`. `support-process-design.md` needed six trim passes to
land inside the ceiling (first draft was 2,915 — the extra taxonomy/SLA/escalation/priority
material didn't fit the budget on the first pass); nothing citation-bearing was cut, only
redundant phrasing and one repeated framing per section. Both files carry an early `## Contents`
block (215 and 150 lines respectively, both >100).

## Router-row coverage (R18)

- **support-process-design.md** — feeds the support-taxonomy job. Ships both taxonomy axes (3-bucket
  state, schema-enforced; 8-category topic incl. the `internal` off-ramp bucket), the
  tie-breaker doctrine ("a category list without tie-breakers is not a taxonomy"), the convergent
  SLA-metric naming, the response-time-promise doctrine (E's orphan #2), the never-ship SLA-default
  class with its ground-zero example, qualified "customer escalation" vocabulary with both
  mechanisms named, GLPI's ITSM-matrix-is-overkill lesson, and FreeScout's monetization boundary.
- **education-and-knowledge-base.md** — feeds the KB/help-content job. Ships the family's
  first-ever definition of what a KB article is (GitLab's reactive/proactive test, cited not
  copied), an article-lifecycle rule with a first-party citation, the zero-result/zero-click
  deflection replacement (with the Algolia + GitLab + mkdocs-material evidence chain), and the
  KB-rewrite-beats-model-upgrade finding.

Both files' "Read when / Skip when" pairs route to named siblings
(`ai-support-policy.md`, `education-and-knowledge-base.md` / `support-process-design.md`,
`design/references/information-architecture.md`, `operate`'s SLO, `growth`'s deflection-experiment
method, the general `docs-writer` skill) rather than bare filenames.

## Rulings applied

R4 (involuntary churn → product) not touched by this partition (out of scope). R8 (ai/success
support-agent seam) — both files explicitly route AI-agent escalation/bot-boundary/resolution-rate
work to `ai-support-policy.md` and state what stays here (human-process vocabulary the AI layer
inherits). R13 (no numbered invariants, bolded named concepts) — "the Existence Gate" not mine;
this partition's named concepts are "a category list without tie-breakers is not a taxonomy,"
the response-time promise, and the never-ship SLA-default class. R14 (evidence grades inline) —
every schema fact is marked schema-verified/primary-source implicitly via `owner/repo@ref:path`
citation; every X/practitioner claim is explicitly labeled "practitioner-report, first-person, no
independent audit"; GitLab prose is marked CITE-ONLY at first use in both files. R15 (never-ship
strip incl. class rules) — self-check below. R16 (precision guards) — Klarna/user_mood/pricing
guards not touched (out of my files' scope); the unsourced-SLA-default guard is this partition's
own ground-zero example and is stated as a class rule, not a single string. R17 (licensing) —
every lift is tagged LIFTABLE/CITE-ONLY/structure-only inline at first citation: Chatwoot (MIT),
django-helpdesk (BSD-3-Clause), Frappe/Zammad/libredesk (AGPL-3.0, structure/naming only), GLPI
(GPL-3.0, structure-only), Anthropic's claude-quickstarts and knowledge-work-plugins (both MIT/
Apache-2.0, LIFTABLE — including the ticket-triage SLA-table citation, which is used as a
*warning* example, not endorsed practice), GitLab handbook prose (CITE-ONLY, license scoped to
"the GitLab Software" not the prose). R18/R19 — sibling citations use pack+filename (+ anchor
concept), e.g. `design/references/niche-and-vertical-design.md` and
`design/references/information-architecture.md`, never a bare invariant number. R20 — all four X
permalinks (levelsio ×2, tylertringas ×1, dvassallo ×1, nikolak47 ×1) copied verbatim from
`_raw-x-solo-topup.md` and `x-practitioners-report.md` and grep-verified against those files by
tweet ID before use (see command output below).

## Never-ship self-check

Grepped both files for every never-ship string/class in synthesis §3 (5–25×, 5%→25–95%, 96%
don't-complain, 80/20, $1-vs-$6 deflection, $2M ARR/CSM, the 76% Salesforce/Fin figure,
60–90-day/15–30%/68% health-score claims) and for bare hardcoded-SLA patterns (`\d+ ?(hour|day)s?
\(P\d\)`): zero matches in both cases (`grep` exit 1). The one SLA-hour-table reference that does
appear (Anthropic's own ticket-triage skill, `SKILL.md:130-168`) is cited explicitly as the
never-ship class's *ground-zero example of the failure*, not as a usable default — the file states
"never ship an SLA number without 'set this from your own observed capacity' framing" immediately
after citing it. Ran the same permalink IDs against source files:
`grep -n "657777387866824704\|1287791800443441152\|1736530664608989598\|2077405086431772785"` on
`_raw-x-solo-topup.md` and `x-practitioners-report.md` — all four found verbatim, none
reconstructed.

## Asset validation

`sla_capacity_calc.py` runs standalone (`python3 skills/success/assets/sla_capacity_calc.py`),
self-tests on every invocation before doing anything else, and asserts three hand-derivable
anchors (single-window 16h gap, two-window 8h gap, 50-ticket/15-min/1-person/8h utilization
1.5625). It never outputs a recommended SLA number — only a utilization ratio and a coverage-gap
ceiling computed from the caller's own inputs — matching the file's own honesty rule. Verified
four invocations (no args, `--window` single, `--window` double, both overload and
under-capacity `--tickets-per-day` cases); all print expected output and exit 0.

## License ack (Chatwoot Captain heads-up)

Checked: both Chatwoot citations in my files (`db/schema.rb:1374-1385` SLA-policy schema,
`app/models/automation_rule.rb:35-42` core automation rules) are main-tree/MIT, not
`enterprise/`-tree Captain content — no near-verbatim Captain/enterprise fragment in either file.

## Open items

- `education-and-knowledge-base.md` cites `growth`'s deflection-experiment-design method by
  concept only (no filename in hand for growth's relevant reference); the integrator should verify
  the exact growth reference name for a precise cross-link if one exists, or leave the concept-level
  citation as-is if growth doesn't have a single dedicated file for it.
- Both files link to `ai-support-policy.md` (W3's), which did not exist at write time in this
  session — expected until W3 lands; recommend the integrator's R18 link-walk re-check once all
  writers report.
- SKILL.md's router table is untouched (integrator's job per inventory §4); neither file is yet
  linked from it.
- `support-process-design.md`'s escalation section names three distinct "escalation" objects
  (SLA-breach-notify, priority-bump, org-visibility) on top of the four-way family collision —
  flagging in case the integrator wants a single cross-pack disambiguation table somewhere rather
  than each file re-stating the collision count.
