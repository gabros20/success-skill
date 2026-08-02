# Voice of Customer

Purpose: Interpret NPS/CSAT/CES and free-text feedback honestly — what a score can support, what it
cannot, and how to read it in aggregate over time. This file does not define a metric or run a
survey; three sibling packs already did that.

Read when:
- A VoC score (NPS, CSAT, CES) or a feedback trend is being used to support a retention, health, or
  roadmap decision.
- Someone wants to know whether a single NPS/CSAT number is "good" or means the customer will stay.
- A "customers don't complain" or "NPS predicts growth" style claim is circulating and needs a
  provenance check before it ships.
- Feedback reasons (why a detractor scored low, why someone churned) need categorizing.

Skip when:
- The question is NPS's definition, scale, or survey method → `design`'s
  `references/research.md:49` ships this (0–10 scale, Promoters 9–10/Detractors 0–6, ~385 responses
  = ±5% at 95% confidence) — cite it, do not redefine it here.
- The question is where NPS/CSAT sits in a metric tree → `product`'s `references/metrics.md:45-53`
  already places "NPS / CSAT, Support Ticket Rate" as a Health branch — consume it, do not re-derive.
- The question is whether NPS moved because of a specific tested change → `growth`'s
  `references/retention-and-resurrection.md:167` already rules "NPS never stands alone as a
  retention experiment's primary metric" — this file's aggregate-trend reading never substitutes
  for that experiment-level rule.
- The question is a health score's predictive ceiling or the tenure/CFM correlation table →
  [health-and-risk-signals](health-and-risk-signals.md) §4 owns those numbers; this file only adds
  what none of the four siblings claims: interpretation of a VoC score as an instrument, and reading
  it in aggregate.
- The question is a support-ticket taxonomy → [support-process-design](support-process-design.md).

Inputs: an NPS/CSAT/CES program already defined elsewhere (or a description of what's collected
today), the collection method (in-app, email, in-person), and — if available — how many people were
shown the survey, not just how many answered.

Produces: a verdict on what a specific VoC number or trend can honestly support, a self-selection
check on the collection method, and a reason-taxonomy note for free-text feedback.

## Contents

- [1. What this file adds — and what three siblings already shipped](#1-what-this-file-adds--and-what-three-siblings-already-shipped)
- [2. Never ship: the NPS-growth and CES-superiority claims](#2-never-ship-the-nps-growth-and-ces-superiority-claims)
- [3. Display vs Response: no rate without a denominator](#3-display-vs-response-no-rate-without-a-denominator)
- [4. Aggregate trend analysis — the unclaimed layer](#4-aggregate-trend-analysis--the-unclaimed-layer)
- [5. Feedback-reason taxonomies need tie-breakers too](#5-feedback-reason-taxonomies-need-tie-breakers-too)
- [6. The "96% don't complain" figure, corrected](#6-the-96-dont-complain-figure-corrected)
- [7. The feedback loop into product](#7-the-feedback-loop-into-product)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## 1. What this file adds — and what three siblings already shipped

Three sibling packs already claim NPS before success exists: `design/references/journeys.md:51-53`
and `research.md:49` (definition and survey method), `product/references/metrics.md:45-53` (its
place in the metric tree, next to Support Ticket Rate), and `growth/references/
retention-and-resurrection.md:167` (it never stands alone as an experiment's metric). None of the
three asks what a score can honestly *support* as a decision instrument, and none reads a VoC metric
in **aggregate over time** rather than as a point value — that interpretation layer is genuinely
unclaimed, and this file claims it explicitly, not by default.

## 2. Never ship: the NPS-growth and CES-superiority claims

Two circulating claims failed independent replication and must not ship as fact:

- **"NPS is the best predictor of growth"** (Reichheld, *HBR* Dec 2003, hand-picked exemplar
  scatterplots, ~50 companies, no regression table). Keiningham et al. 2007 (*Journal of Marketing*,
  21 firms, 15,500+ interviews): *"We find no support for the claim that Net Promoter is the 'single
  most reliable indicator'…"* — the older ACSI metric had the higher R² in two of three of
  Reichheld's own exemplar cases.
- **"CES outperforms NPS and CSAT at predicting loyalty"** (Dixon, Freeman & Toman, *HBR* Jul–Aug
  2010). Unsupported as published — the entire claim rests on an unlabelled bar chart with no R²,
  coefficients, or per-comparison n, and the outcome measured was stated *intention*, not behavior.
  It is then falsified on actual two-year retention:
  [health-and-risk-signals](health-and-risk-signals.md) §4 already carries de Haan, Verhoef & Wiesel
  2015's correlation table, where CES is the *weakest* of the four feedback metrics against real
  retention. Cite that table rather than repeating the correlation values here.

Treat any pitch of the form "switch to CES/NPS because it predicts X better" as this class until a
holdout-validated, retention-linked source is named — cite the replication failure, never the
original claim alone.

## 3. Display vs Response: no rate without a denominator

`formbricks/formbricks`'s survey schema models two separate records: a **Display** (the survey was
shown to someone) and an optional **Response** (someone answered). A Display with no linked Response
is a first-class "shown-and-ignored" event, not a discarded one. This is the industry admitting, in
its own data model, what most NPS/CSAT reporting hides: you cannot state a response rate unless you
record impressions, and any score computed only over responders is a self-selected sample — usually
the people motivated enough to answer, which skews toward the extremes (very happy, very angry).

Before quoting an NPS or CSAT number, ask for its denominator: how many people were shown the survey,
not just how many answered. If only the responder count is available, say so explicitly rather than
implying the number represents the customer base.

## 4. Aggregate trend analysis — the unclaimed layer

None of the three claiming siblings tells a reader how to use a VoC metric's *movement over time* as
an organizational signal — each treats it as a point value (a health-tree entry, a definition, an
experiment metric). That reading is this file's job, and the ceiling from
[health-and-risk-signals](health-and-risk-signals.md) §4 sets its limit: the strongest single
customer-feedback correlate of actual retention explains roughly 4% of variance. A single score is
close to noise. What is defensible:

- Track the trend, not the level — a sustained multi-period move (up or down) against a *stable*
  collection method (same tool, same wording, same trigger point) is more informative than any one
  score, because it partially cancels the self-selection bias in §3 (the same kind of respondent
  self-selects each period).
- Never let a trend substitute for the experiment-level rule in §1 — an aggregate NPS trend can
  motivate investigating a retention hypothesis; it cannot, by growth's own shipped rule, stand alone
  as evidence that a specific change caused it.
- Report the trend alongside its denominator (§3) and its collection-method changes — a trend break
  that coincides with a survey-tool or wording change is a measurement artifact, not a customer
  signal, until ruled out.

## 5. Feedback-reason taxonomies need tie-breakers too

[support-process-design](support-process-design.md) §2 ships the rule "a category list without
tie-breakers is not a taxonomy" for support tickets. The same discipline applies to VoC reason codes
(why a detractor scored low, why a churn survey respondent picked a given reason): a reason list with
no rule for the response that names two causes, or none clearly, is not a taxonomy either. Apply that
same file's tie-breaker discipline to feedback reasons rather than inventing a second mechanism here.

## 6. The "96% don't complain" figure, corrected

"96% of unhappy customers don't complain" is a worst-case slice of a real TARP/John Goodman finding
(White House Office of Consumer Affairs, ~1979–1986) presented as universal. TARP's own breakdown
ranges by stake: roughly 5–30% for mistreatment/quality complaints, up to 50–75% for out-of-pocket
monetary loss. Never ship the flat "96%" — teach the range and that it depends on what the customer
lost, not a single constant.

## 7. The feedback loop into product

`product/references/discovery.md:15,75` already names support tickets, forums, and review sites as
discovery input product mines for recurring complaints. VoC's job is to hand that pipeline
structured, denominator-honest signal (§§3–4) — not to re-run product's own discovery process, and
not to report a single low-n verbatim as if it were a validated trend.

## Validation

- Every NPS/CSAT/CES claim cites design's definition, product's metric-tree placement, or growth's
  experiment rule rather than restating them.
- No NPS-growth or CES-superiority claim ships without its replication-failure citation attached.
- A quoted response rate states its denominator (Display count) or states plainly that only the
  responder count is known.
- A VoC claim used for a decision is a multi-period trend, read alongside its collection method — not
  a single score presented as diagnostic.
- The 96% figure, if invoked, is presented as a stake-dependent range, never the flat number.

## Failure modes and handoff

- **A single NPS or CSAT snapshot is used to justify a retention or health decision** — apply §4;
  route to a trend read or decline, citing the ~4% ceiling in health-and-risk-signals.md.
- **"NPS predicts growth" or "CES predicts loyalty" is repeated as settled** — apply §2's replication
  failures before it ships anywhere, including a customer-facing deck.
- **A response rate is quoted without a shown-count denominator** — apply §3; state the gap rather
  than imply a representative sample.
- **A feedback-reason list has no rule for ambiguous or multi-cause responses** — apply §5's
  cross-reference rather than inventing an ad hoc tie-breaker.
- **The question turns out to be about a specific tested change, not an aggregate reading** — route
  to `growth`'s retention-experiment rule; this file does not adjudicate single-test causality.
