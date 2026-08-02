# Renewals and Expansion

Purpose: Run the renewal workflow and expansion motion honestly — knowing which numbers are
audited but not comparable (NRR/GRR), which are unsourced folklore (usage-threshold expansion
triggers), and where success's ownership of "renewal" stops before it becomes a modeling or sales
job.

Read when:
- A renewal is approaching and someone needs the workflow: risk-tiering, notice timing, who does
  what.
- An expansion signal is being evaluated for whether to act on it.
- Someone quotes an NRR or GRR figure, especially to compare it across companies or periods.
- The advocacy or reference-customer question comes up alongside a renewal or expansion
  conversation.

Skip when:
- The question is the churn/retention/MRR metric-tree entry itself → `product`'s metric tree —
  consume it, don't re-derive it.
- The question is whether to run a retention or resurrection *experiment* → `growth`'s
  retention-and-resurrection.md — this file covers the executed motion, not the test design.
- The question is the pricing tier or commercial-lifecycle model → `product`'s surface-app-saas.md
  — this file operates the workflow that model describes, it doesn't design the tiers.
- The question is CSM/QBR/EBR machinery, a health-score audit, or high-touch account-unit
  mechanics → [surface-b2b-high-touch](surface-b2b-high-touch.md).

Inputs: a renewal date or expansion signal, the account's surface, and — if an NRR/GRR figure is
being reported or compared — which company or definition it came from.

Produces: a renewal workflow scoped to success's actual ownership, an NRR/GRR figure computed
under a stated definition and never silently compared to a differently-defined one
(`assets/nrr_calc.py`), and an advocacy handoff that stops at qualification and consent.

## Contents

- [1. Who owns what in a renewal](#1-who-owns-what-in-a-renewal)
- [2. NRR/GRR: four audited definitions that are not one metric](#2-nrrgrr-four-audited-definitions-that-are-not-one-metric)
- [3. The surviving canon outcome: NNR, without the process](#3-the-surviving-canon-outcome-nnr-without-the-process)
- [4. Renewal mechanics: notice periods and risk tiering](#4-renewal-mechanics-notice-periods-and-risk-tiering)
- [5. Expansion signals: mostly folklore, name it](#5-expansion-signals-mostly-folklore-name-it)
- [6. The sales seam — contested, not settled](#6-the-sales-seam--contested-not-settled)
- [7. Advocacy: success qualifies and consents, marketing produces](#7-advocacy-success-qualifies-and-consents-marketing-produces)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## 1. Who owns what in a renewal

Three verbs, three owners. `product` **models** the commercial lifecycle — trial → paid →
expansion → renewal/churn is named inside product's own shipped `surface-app-saas.md` at the
pricing-tier level. `success` **operates** the renewal workflow — risk-tiering, notice timing, the
account conversation. `sales` **closes** the expansion sale where a negotiation exists. The third
clause is provisional, not settled family doctrine — flag it as such, and see §6.

## 2. NRR/GRR: four audited definitions that are not one metric

Four SEC filings, read directly (not summarizer-paraphrased), each defines "net revenue retention"
with a genuinely different mechanic:

- **Snowflake** (10-K FY2025): a single **two-year snapshot** — the cohort is customers active in
  month one of a trailing two-year window; NRR = that cohort's year-two product revenue ÷ its
  year-one product revenue. No rolling average. Reported 126% as of Jan 31, 2025.
- **Datadog** (10-K FY2020): a **rolling 12-month cohort** — Current Period ARR (12 months later,
  net of contraction/churn, excluding new customers) ÷ Prior Period ARR, then averaged over the
  trailing 12 monthly point-in-time rates. Reported "above 130%" for FY2020 and FY2019.
- **HubSpot** (10-K FY2024): a **monthly cohort**, revenue-weighted average of
  Retained-Subscription-Revenue ÷ Retention-Base-Revenue, then **annualized**. Scoped to
  *subscription* revenue only, excluding services/other. Reported 102.2% / 103.9% / 110.3% across
  three fiscal years (most recent first).
- **Klaviyo** (S-1, 2023): the same rolling-12-month mechanic as Datadog, but explicit that
  reactivated subscriptions within the window count as retained, and explicit that the average is
  ARR-weighted (Datadog's own text is ambiguous on weighting).

All four exclude new-customer revenue and are cohort-based — but the measurement window, revenue
scope, and edge-case handling differ. **A reported 126% (Snowflake's two-year snapshot) and a
reported "above 130%" (Datadog's rolling 12-month average) are not computed the same way and must
never be compared as if they were.** Dave Kellogg's "Lazy NRR is Not NRR" draws
the sharper distinction underneath this: true cohort NRR "resists manipulation," while an
ARR-bridge calculation — starting ARR plus net expansion over one quarter's own starting base — is
a different, more gameable quantity dressed up to look the same. `assets/nrr_calc.py` implements
all four mechanics plus the ARR-bridge/GRR form as selectable modes, self-tested against worked
anchors, never blended in one run. The 100/110/120% tiers ("good/better/best") are a widely-used
heuristic, safe to cite; a benchmarking-service claim that median SaaS NRR softened industry-wide
across 2021–2024 circulates widely but is method-unknown here — not verified to a primary report,
do not cite a specific percentage as measured.

## 3. The surviving canon outcome: NNR, without the process

Across five deep-mined solo operators, the enterprise CS vocabulary — QBR, CSM ratio, health
score, "Customer Success" as a job title — never appears once, not attacked, absent. But the
canon's *outcome* metric survives without its apparatus: Josh Pigford (Baremetrics' founder)
celebrates Net Negative Churn unreservedly as the "SaaS holy grail" — a bootstrapper adopting the
canon's metric while adopting none of its organizational machinery. Teach the outcome vocabulary
(NRR, NNR, "negative churn"); don't assume the enterprise process is required to earn it. A related
definitional-honesty note for any churn count: "a downgrade is not logo churn — it's just a
downgrade," and "a pause is better than a cancel" (jasonlk) — folding downgrades or pauses into
cancellations overstates the loss being reported.

## 4. Renewal mechanics: notice periods and risk tiering

Auto-renewal notice periods cluster at 30/60/90 days — 30 modal in standard SaaS agreements, 60 a
common buyer-protective negotiated target; opt-in (affirmative-action) renewal is achievable
mainly for smaller deals or real bargaining power. This is practitioner/vendor-content consensus,
not verified against a single first-hand playbook — treat it as thin. The contract mechanic itself
(notice period, auto- vs. opt-in) is not gated by team size — it applies to a solo builder's own
terms of service exactly as an enterprise MSA — even though the risk-tiering *practice* built
around it usually assumes a named account owner.

## 5. Expansion signals: mostly folklore, name it

Every "usage signal predicts expansion" claim found in this research is unsourced vendor content —
claims that a usage-threshold crossing, a growing count of engaged stakeholders on an account, or
health-score tracking itself each reliably predicts seat expansion — none cites a study, a company,
an n, or a method. Frame a usage-threshold trigger as plausible and widely believed, not measured;
never cite a specific conversion percentage as evidenced. Which signals are trustworthy at all is upstream of whether
acting on one works — the latter is growth's experimentation territory; success consumes a signal,
it does not validate it.

## 6. The sales seam — contested, not settled

§1's "sales closes the expansion sale" clause is provisional, and it is directly contested by the
canon's own co-author. lincolnmurphy's position is complexity-gated, not role-based: a CSM renews
by default; only genuinely complex renewals route to a dedicated CS-native resource, explicitly
*not* "Account Management carryover" (x.com/lincolnmurphy/status/1084526744290369537 and
x.com/lincolnmurphy/status/1084522527991480325, both Jan 13 2019). Cite both positions in any handoff that touches
this seam; this file does not adjudicate the industry fight.

## 7. Advocacy: success qualifies and consents, marketing produces

No shipped sibling pack currently draws this line, so success settles it as its own ruling:
success identifies and qualifies a referenceable customer and secures explicit consent; `marketing`
— which already owns case studies and testimonials as conversion proof — produces and publishes
the asset. Success does not write or publish the case study; marketing does not solicit or qualify
the customer relationship that makes one possible.

## Validation

- Any reported NRR/GRR figure states which of the four filing definitions (or the ARR-bridge form)
  it uses, and no comparison crosses definitions.
- Expansion-signal claims are labeled plausible-not-measured wherever no method is cited.
- The renewal workflow states product/success/sales ownership explicitly, with the sales clause
  marked provisional.
- Advocacy work stops at qualification and consent; a produced or published asset is marketing's
  handoff, not success's.

## Failure modes and handoff

- Comparing two companies' NRR percentages as if computed identically → apply §2; state the
  definition, decline the comparison.
- Citing a usage-threshold expansion trigger, or a per-CSM/per-rep ratio, as if measured → apply
  §5's folklore label; for the circulating ARR-per-CSM heuristic specifically, route to
  [surface-b2b-high-touch](surface-b2b-high-touch.md) §4, which carries it as a propagation exhibit
  with both sides permalinked — that file is the only place the figure may appear.
- Treating "sales closes the expansion sale" as settled family doctrine → it is provisional (§6);
  state so in any handoff.
- Success drafting or publishing a customer story itself → that's marketing's job once success has
  qualified the customer and secured consent (§7); hand off, don't produce.
- Recommended next: `marketing` for a qualified advocacy handoff; `product` when a renewal reveals
  the commercial-lifecycle model itself needs revision, not just workflow execution.
