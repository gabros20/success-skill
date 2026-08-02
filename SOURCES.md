# Sources, licences, and what this skill claims for itself

This pack was built into a genre that is fragmented rather than empty: competent prior art exists,
none of it integrates, and almost none of it cites anything. This file says what was taken, from
whom, under what licence, and what the pack actually adds — rather than implying more.

Every claim is graded at its point of use in the reference file as well as here, on one scale:
**measured-with-method > practitioner-report > vendor-claim**. A vendor figure stays a vendor-claim
even when it is quoted in order to refute it. Full research provenance — five channel reports and
their 21 raw files — lives in [`research/`](research/), gated by
[`research/synthesis.md`](research/synthesis.md).

## 1. The wedge

The niche is **open by fragmentation, not by absence**. Three partial incumbents exist with zero
overlap between them, and nobody integrates:

- **coreyhaines31's churn-prevention skill** has real reach (84.2k installs) but covers 2 of the 12
  canonical customer-success includes and cites nothing.
- **`anthropics/knowledge-work-plugins`** `customer-support` (23,246★, Apache-2.0) is official and
  well-built but tactical only — triage, escalate, KB article — with no onboarding, health,
  renewal, or voice-of-customer surface at all.
- **`t0ddc3by/claude-for-customer-success`** (81 skills, Apache-2.0 wrapping © SuccessCOACHING IP)
  is architecturally the most complete artifact found, and cites **zero external URLs across 28,988
  lines**. It is enterprise-CSM-only and effectively unadopted (~1 install per skill).

**A constraint this pack holds against itself:** `t0ddc3by` *already* asks whether a health score
actually predicts churn or merely classifies accounts. This pack may not claim "nobody asks this."
The differentiation is that this pack **answers** it — with evidence, with honest scope, and
integrated across support and AI-agent policy. The only pack that asks the question does none of
those three, and no pack anywhere does all four.

The same emptiness shows from the repository side: the sole `awesome-customer-success` list carries
24★ of vendor self-adds, and every dedicated health-score repo found tops out at 0–1 stars.

## 2. The four planks, and where each one's evidence comes from

**P1 — the observability-and-prediction honesty layer** (flagship,
`references/health-and-risk-signals.md`). Spine: GitLab's public handbook (its health score does not
predict churn — prediction is two separate internal models); the null-result triangle (five CS
vendors → the entire open-source corpus → GitLab's own in-house data-science team, none of whom
publish a churn-model accuracy figure); four-study academic convergence (below); the honest ML
ceiling on the one public churn dataset with its two inflation mechanisms; and Josh Pigford's anchor
anecdote. **Binding writer guard, carried into the pack verbatim: "not published," never "not
measured."**

**P2 — the existence gate** (`references/when-success-applies.md`). No source anywhere states when a
distinct success function becomes worth having; the canon assumes the function exists and only asks
how to staff it. The gate is constructed here, anchored on the one attributed practitioner sentence
that makes it checkable (arvidkahl). The solo-scale replacement for CS process is **pricing first,
AI tier-1 support second** — explicitly *not* documentation, which is what this pack's own charter
originally hypothesised and what two independent research passes failed to support.

**P3 — AI-support policy** (`references/ai-support-policy.md`). Success owns the policy layer; `ai`
owns mechanics and evaluation. The nine-pattern escalation corpus found **zero** production
implementations firing on a numeric confidence threshold. "Resolution rate" has no auditable
definition anywhere in the corpus.

**P4 — integration with honest seams** (`references/handoff.md` and every file's Skip-when block).
Support-process primitives are taken from primary sources — schemas, not blog posts.

## 3. Licences

Verified by opening the `LICENSE` file directly, not by trusting the GitHub API's license field or a
registry mirror. **The API disagreed with the file in at least 13 cases this run.**

### LIFTABLE — file-verified permissive

| Source | Licence | Used for |
|---|---|---|
| `emcie-co/parlant` | Apache-2.0 (LICENSE + `pyproject.toml` agree) | The strict-vs-fluid composition vocabulary: guidelines, relationships/exclusion edges, journeys, canned responses (`ai-support-policy.md`) |
| `anthropics/claude-quickstarts` | MIT | The typed-field-every-turn escalation exemplar and the eight-category topic taxonomy with its `internal` bucket. **Cite the current name** — it was renamed from `anthropic-quickstarts`, and the old name still redirects, so a stale citation passes review while being wrong |
| `anthropics/knowledge-work-plugins` | Apache-2.0 (root and per-plugin copies byte-identical) | The KB-article "maintain aggressively" rule and review cadence; and — as this pack's *ground-zero never-ship example*, not as endorsed practice — an uncited hardcoded SLA hour table |
| `sierra-research/tau-bench`, `tau2-bench` | MIT | The pass^k reliability mechanism and the cleanest scope-boundary escalation clause found. The MIT licence covers the files, not the methodology — cite Yao et al. 2024 and the companion SABER error-taxonomy paper for that |
| `huabeitech/agent-desk` | Apache-2.0 | The time-of-day escalation trigger with asymmetric confirmation |
| `RasaHQ/helpdesk-assistant` | Apache-2.0 | The pure-intent-classification handoff pattern, and its own limit (it can only simulate handoff) |
| `dynatrace-oss/CustomerSuccess` | Apache-2.0, alive | The **best primary-source exhibit in the corpus for the flagship**: a real vendor CS team's published health-score arithmetic, with four equally-weighted hand-picked-threshold components, no outcome variable joined anywhere, and a paired gap-and-action tile that is exactly the honest reframe this pack teaches |
| `chatwoot/chatwoot` (main tree) | MIT | The three-name SLA threshold schema and the conditions×actions automation-rule template. Its `enterprise/` tree is a different licence — see CITE-ONLY |
| `django-helpdesk/django-helpdesk` | BSD-3-Clause | The automatic priority-bump escalation mechanism, distinct from SLA-breach notify |
| `churnkey/sdk` | MIT (LICENSE opened; API agrees) | The cancellation-flow reason→matched-offer structure, including the case where the honest offer is none |
| `0x416d6972/pypulate` | MIT (LICENSE + `pyproject.toml` agree) | Reference implementation and worked anchors for `assets/nrr_calc.py` |
| `CamDavidsonPilon/lifelines` | MIT | The published 0.55–0.75 concordance sanity band used by `assets/churn_baseline_check.py` |
| `ReverendBayes/Telecom-Churn-Predictor` | MIT | The base-rate-theater exhibit, cited *from its own CSV*: a headline accuracy that a majority-class baseline nearly matches |
| `squidfunk/mkdocs-material` | MIT (free tier, not Insiders) | The was-this-helpful widget's honest limit — it ships the UI, not the recording, and cannot join a click to a later ticket |
| `formbricks/formbricks` (SDK dirs) | MIT within an AGPLv3 repo that also has a commercial `ee/` dir | The Display-vs-Response schema — the self-selection exhibit. Structure and modelling idea only |
| `polonel/trudesk` | Apache-2.0 — **the clearest API-lied case this run** (API said NOASSERTION) | Support-stack structure comparison |

### CITE-ONLY — described and linked, never reproduced

- **GitLab's public handbook** — the single richest exhibit in this pack (the P.R.O.V.E. model and
  its five honest failure modes, input expiry, segmented thresholds, the missing-data disagreement
  between its automated score and its human rubric, the unbuilt VoC components, the non-monotone
  support-volume finding, the deflection-is-a-wishlist-KPI admission, the reactive/proactive
  KB-vs-docs distinction, and the risk-reason taxonomy with tie-breakers). Its root licence is
  scoped to "the GitLab Software," **not the handbook prose** — so this pack describes, links, and
  quotes only short excerpts, and never reproduces the material wholesale.
- **`t0ddc3by/claude-for-customer-success`** — Apache-2.0 wrapping © SuccessCOACHING IP. The
  clearest thin-licence-on-thick-IP case found; cited as an incumbent, nothing lifted.
- **AGPL support stacks** — `zammad/zammad`, `frappe/helpdesk`, `abhinavxd/libredesk`,
  `freescout-help-desk/freescout`. Their **schema shapes and field names** are cited as convergent
  evidence (the three canonical status buckets; the first/next/resolution SLA metric naming; the
  clock pausing on customer-wait as a named state; Frappe's agent-vs-customer status label split).
  Ideas and naming only — no code.
- **`glpi-project/glpi`** — GPL-3.0. Its ITIL impact×urgency priority matrix is cited *structurally*
  as the example of over-engineering unless you are doing formal ITSM.
- **Chatwoot's `enterprise/` tree (Captain)** — source-available. Its handoff-consent pattern is
  **described, never quoted**; an initial draft that reproduced its template text near-verbatim was
  caught and rewritten during composition.
- **`sebp/scikit-survival`** (GPL-3.0-or-later), **chaskiq** (AGPL + Commons Clause), and the
  **Buffer health-score script** (no LICENSE file at all) — referenced as corpus evidence only.
- **Odoo RFM module** — cited as one of the corpus's two most substantive health artifacts, and as
  evidence for the same finding: it acts on a score but never checks it against a later outcome.

### AMBIGUOUS — flagged, and nothing lifted

- **`usertour/usertour`** — `package.json` declares flat MIT while its `LICENSE` carves out "any
  code controlling feature, permission, role and plan enablement" to a commercial licence, and the
  API says NOASSERTION. Three sources, three different answers. Its user/company membership
  modelling is cited as an **idea** in `assets/health_score_audit.md`; no code taken.
- **`laudspeaker/laudspeaker`** — an MIT header on an AGPLv3 body, in one file.
- **`uvdesk`, `HELPDESK.AI`** — API-only checks, never file-verified. **Do not touch** without
  re-verification.
- **`dittofeed/dittofeed`** — clean MIT, but stale at time of research. Liftable, subject to a
  liveness check first.

### The licence clauses this build added

Carried forward from the family's five-clause rule, this build adopted two more:

- **(f) A dangling LICENSE-file pointer is not a licence.** A manifest that names a licence file
  which does not resolve tells you nothing.
- **(g) A registry mirror is never a licensing shortcut.** Resolve upstream, open the file.

And one this pack's own composition proved out: **a package manifest can contradict the LICENSE
file in either direction** — `usertour` hides a carve-out behind a flat `"license": "MIT"`;
`trudesk` reports NOASSERTION for a clean Apache-2.0. Read both, and say so when they disagree.

## 4. Academic and legal sources

Cited by full reference in `references/health-and-risk-signals.md` §4 and
`references/voice-of-customer.md` §2. Grade: measured-with-method throughout.

- **Ascarza (2018)**, *Journal of Marketing Research* 55(1) — two randomized field experiments. The
  highest-risk customers responded *least* to intervention, and one segment got worse. Risk-ranking
  and response-ranking are different orderings; this is why `retention-execution.md` targets by
  uplift.
- **de Haan, Verhoef & Wiesel (2015)**, *IJRM* 32(2) — 93 firms, n=1,375, against actual two-year
  retention. Tenure out-predicts every customer-feedback metric, and the ceiling is roughly 4% of
  variance. CES is the weakest of the four.
- **van Doorn, Leeflang & Tijs (2013)**, *IJRM* 30(3) — n=11,967 across 46 firms. Feedback metrics
  are contemporaneous, not forecasts; no single best metric.
- **Fader, Hardie & Lee (2005)**, *Marketing Science* 24(2), on Schmittlein, Morrison & Colombo
  (1987) — the contractual/non-contractual distinction that the entire CS canon omits, and the
  source of **the Observability Question**. Their own scope excludes subscriptions; the pack ships
  the distinction, not their model, as validated for subscriptions.
- **Verbeke et al. (2012)**, *EJOR* 218(1) — a statistically better churn model can be a worse
  business tool.
- **Keiningham et al. (2007)**, *Journal of Marketing* — the NPS replication failure. **Reichheld
  (2003)**, *HBR*, is cited only as the original claim the replication tested.
- **Dixon, Freeman & Toman (2010)**, *HBR* — the CES claim, cited as unsupported-as-published (an
  unlabelled bar chart, stated intention rather than behavior) and falsified on retention by de
  Haan.
- **Mathur et al. (2019)**, CSCW — cancellation dark patterns. Cited by pointer only;
  `growth`'s monetization file owns this evidence and this pack ships none of it.
- **TARP / John Goodman** (White House Office of Consumer Affairs, ~1979–1986) — the real study
  behind the "unhappy customers don't complain" figure, whose own breakdown ranges widely by what
  the customer stood to lose.
- ***Moffatt v. Air Canada*, 2024 BCCRT 149** — a chatbot's statements bind the company; "it makes
  no difference whether the information comes from a static page or a chatbot."

## 5. Practitioner sources

Every X permalink in this pack was **copied verbatim from a research raw file and grep-verified by
post ID before use.** A reconstructed permalink is a fabricated citation that survives review, so
none was reconstructed. Grade: practitioner-report, first-person, no independent audit — stated
inline at every point of use.

- **@arvidkahl** — the Existence Gate's anchor test; the price-raising-versus-churn observation; a
  first-level AI CS agent running in production; live translation as a one-person coverage answer.
- **@levelsio** — the pause-instead-of-cancel arc across three posts and two years, including the
  UX-naming judgment; the CONFOUNDED cancel-flow rebuild and the hedged causal claim beside it (the
  hedge is cited as a *model* for stating an unmeasured causal claim honestly); PayPal-versus-Stripe
  support load; the costed refusal of synchronous support calls; the billing-confusion residue even
  a fully automated stack keeps.
- **@tylertringas** — the LIFO triage tactic; the shared-inbox-into-agent-loop pattern.
- **@dvassallo** — the clearest tooling-adoption threshold found (a tool, not a hire).
- **@Shpigford** — the flagship's anchor anecdote: the founder of a churn-analytics company, running
  his own tooling on his own funnel, publicly unable to attribute his own 2× churn improvement. His
  own bare-percentage teaser from an earlier year is **refused as a figure in the same paragraph** —
  the figure-class rule catches this pack's own best anchor.
- **@robwalling** — the price-to-churn link, independent of arvidkahl.
- **@patio11** — minimum-buy-in economics; and, from outside this pack's interest, that support is
  poorly understood outside enterprises.
- **@lincolnmurphy** — cited on both sides: the Desired Outcome framework and the QBR-is-optional
  reframe as usable content; the CS-native renewal position as *contested vocabulary this pack does
  not adjudicate*; and his own repeated debunking of the ARR-per-CSM heuristic, paired with
  **@saastr** still circulating it years later — the propagation exhibit, shipped only with both
  sides attached.
- **@nikolak47** — the KB-rewrite-beats-model-upgrade data point.
- **Lincoln Murphy, sixteenventures.com** — the Desired Outcome definition and the QBR critique,
  cited to his own pages. His framework's **current** Goal + Appropriate Experience form is the one
  cited; the pre-2024 formulation is dated explicitly wherever it appears.

## 6. Figures this pack refuses to ship

Six widely circulated claims were traced to their primary sources during research; **all six failed
as circulated.** The refusal list, with the mechanism taught in place of each figure, is in
`research/synthesis.md` §3. The standing rules matter more than the list:

- The never-ship list is not the rule — judge the **figure class**. A bare percentage with no method
  is unusable regardless of who said it.
- **A disclaimed figure is still a figure.** Never name a forbidden number in order to forbid it;
  state the mechanism and point at the primary source. This pack applies that to its own best-graded
  practitioner anchor and to the single industry automation percentage most likely to spread.
- **An unsourced SLA default is a promise made to someone else** — a new never-ship class this build
  identified, whose ground-zero example is a first-party official skill.
- **Vendor deflection, resolution, and health-score accuracy figures are vendor-claims, always**,
  and are labelled as such even when quoted to refute them.
- Verify the **subject** of a metric from its local context before repeating it.

## 7. What this pack claims for itself

Constructed here, not lifted from any source:

- **The Existence Gate** — a checkable test for whether a distinct success function is warranted
  yet, built on an attributed practitioner sentence, because no source in the canon answers the
  question.
- **The Observability Question as a routing gate** — the BTYD contractual/non-contractual
  distinction is the literature's; making it the *first* question asked before any scoring work, and
  applying it to a self-serve reader who would otherwise be handed a contractual-shaped template, is
  this pack's.
- **The definition of what good help content is** — a grep-verified empty slot across twelve shipped
  sibling packs. The reactive/proactive test is GitLab's; adopting it as the family's scope test is
  this pack's.
- **The response-time promise** — `operate` owns internal SLOs; nobody owned the customer-facing
  promise of when a human replies. It surfaced once family-wide, buried in a vertical playbook.
- **The third box** — `growth` classifies a retention mechanic as standing (`operate`'s) or
  experiment-bound (`growth`'s). A validated motion held as an ongoing relationship is the third
  box, drawn here.
- **Aggregate voice-of-customer trend reading** — three siblings define, place, and constrain NPS;
  none reads it as a movement over time. Claimed explicitly rather than by default.
- **The seam rulings** in `references/handoff.md` — including three rows this pack originates because
  `product`, `operate`, and `automation` all cede work to success in prose but shipped before
  success existed, and the resolution of a community-retention fork `marketing` left open on disk.

## 8. What this pack did not do

- It did not measure anything itself. Every figure is someone else's, graded.
- It did not adjudicate the industry's renewal-ownership fight — both positions are cited, and the
  sales clause is marked provisional wherever it appears.
- It did not resolve the pricing-versus-support-quality question. Every practitioner found lands on
  pricing; **no opposing voice was found, which is not the same as the contest being settled** — so
  it ships CONTESTED, as a strong one-sided position with the absence noted.
- It did not audit any vendor's numbers, because none published enough to audit. "Not published" is
  the finding; "not measured" would be a claim this pack cannot support.
- Several corpus items remain unread and are listed honestly in `research/synthesis.md` §8.
