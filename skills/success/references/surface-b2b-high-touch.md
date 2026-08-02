# Surface: B2B High-Touch

Purpose: Operate the CSM-owned, named-account surface honestly — lift the epistemics the
enterprise canon's best public exhibit has quietly worked out, and decline the ratio/ritual
machinery that doesn't survive its own author's scrutiny, stating reasons rather than omitting it.

Read when:
- The account has a named CSM, a service tier, or an account-level health score.
- Someone asks for a CSM-to-account ratio, a QBR cadence, or an EBR structure to adopt.
- A health score's inputs, weighting, or override rules need auditing before trusting a color.
- A renewal or expansion conversation on this surface needs the sales-seam context.

Skip when:
- The account is self-serve with no named owner → surface-selfserve-solo.md is the default.
- The question is the renewal/expansion ownership ruling, NRR/GRR mechanics, or advocacy →
  [renewals-and-expansion](renewals-and-expansion.md) — this file adds only what's specific to a
  named-CSM relationship.
- The question is the health-score flagship's general epistemics (score-vs-prediction, "not
  published, never not measured") → health-and-risk-signals.md — this file is the full-depth
  exhibit those epistemics are drawn from.

Inputs: an account with a named CSM or service tier, and — if declining a machinery request — the
specific practice being asked for.

Produces: a health-score audit against a named exhibit's five failure modes
(`assets/health_score_audit.md`), a reasoned decline of CSM-ratio or QBR-cadence machinery with its
evidence cited, and a renewal/sales-seam note scoped to the high-touch account unit.

## Contents

- [1. Epistemics, not machinery](#1-epistemics-not-machinery)
- [2. The health score in full depth](#2-the-health-score-in-full-depth)
- [3. What to lift](#3-what-to-lift)
- [4. What to decline, with reasons](#4-what-to-decline-with-reasons)
- [5. The account is the unit — sales seam](#5-the-account-is-the-unit--sales-seam)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## 1. Epistemics, not machinery

GitLab's public customer-success handbook — Gainsight-run throughout, ~100 files in the CSM
subtree alone — is the largest publicly readable enterprise CS handbook found in this research
and, being primary-source about its own limitations, the most useful exhibit of both halves of
this surface: almost none of the *machinery* (Gainsight, EBRs, Solution Architects, a VP of
Customer Success in an escalation ladder) transfers to a solo or small team. What transfers is the
*epistemics* — the disciplined habits the machinery produces when honest about its own limits.
Lift the second, decline the first, and say why for each, every time.

## 2. The health score in full depth

GitLab's P.R.O.V.E. model weights five groups: Product 50% (License activation, User engagement,
Use Case), Risk 25% (CSM Sentiment, Opportunity Renewal risk), Outcomes 10% (Success Plan, Verified
Outcomes), Voice of the Customer 5% (Support, Surveys), Engagement 10% (Customer Engagement,
Executive Sponsorship, Events, Certifications). Banding: Green 75–100, Yellow 50–74, Red 0–49.
**Prediction is not this score's job** — churn and expansion are handled by two separate,
internal-only models (Propensity to Churn/Contract, Propensity to Expand); score-vs-prediction as
different artifacts is this surface's clearest confirming exhibit (full argument in
health-and-risk-signals.md). No accuracy number of any kind is published for the score or either
model.

Five honest failure modes worth auditing any adopted score against:

- **A quarter of the score is a human guess that can override everything.** CSM Sentiment is 100%
  of the Risk group; when it turns red, the whole score turns red regardless of the other 75%,
  resuming standard weighting only once sentiment recovers — real for green/yellow discrimination,
  decorative at the boundary that matters most.
- **Missing data increases subjectivity instead of confidence.** A missing measure's weight is
  redistributed to what remains, and the heaviest-weighted measure — CSM Sentiment — gets the
  biggest reallocation, so a no-telemetry account ends up mostly-CSM-opinion on the same 0–100
  scale as a fully instrumented one; every measure but sentiment is null by construction for a
  customer's first 30 days.
- **The handbook disagrees with itself about what missing data means.** The automated score treats
  it as neutral (redistribute); the human triage rubric treats it as risk ("significant lack of
  information leading to uncertainty" is Yellow; "overwhelming lack of information... leading up to
  renewal" is Red). Take the human side — ignorance about an account is a finding, not a gap.
- **A published model can contain components that don't exist.** Three of four Voice-of-Customer
  measures (CSAT, NPS Surveys, two Engagement measures) are marked "Not started" in GitLab's own
  maturity column; "Voice of the customer" is, in practice, support-ticket counts. Check a maturity
  column before trusting an architecture diagram.
- **Support-contact direction can be wrong, and an org can catch it.** Bands score zero tickets
  below Green (Green starts at 1), and the roadmap plans to "allow more tickets as a good thing" —
  the human rubric already flags silence after being told to ask for help as its own yellow signal.
  Support volume and health are non-monotone; this handbook documents an org discovering that in
  public.

## 3. What to lift

Framework only — cite GitLab, never copy its prose:

- **Every input has an expiry.** Usage data stales at 60 days, CSM Sentiment flags at 90/nulls at
  120, support measures at 30 — showing nothing beats showing stale, each signal with its own
  justified half-life.
- **Thresholds are segmented, not universal.** Bands differ by service tier, and several measures
  are marked N/A for Scale and Tech Touch rather than scored badly — the direct answer to whether
  one score fits a self-serve account and a named enterprise one: it doesn't.
- **Relationship breadth is a scored signal.** Persona engagement bands on whether both a Dev Lead
  and a Security Lead attend; the human rubric separately flags "single contact... (single-
  threaded)" as risk — cheap, concrete, and one of the few practices that survives translation.
- **A category list without tie-breakers is not a taxonomy.** GitLab's churn-reason list carries a
  disambiguation rule against its nearest neighbor for each entry — "if they didn't adopt because
  they didn't see value, it should be Product Gap"; "this was not a competitive loss" under Loss of
  Budget. That's what makes a taxonomy usable rather than decorative.
- **An escalation ladder named by severity, not trigger type.** Yellow notifies the account team;
  Red adds the Area Sales Manager, Regional Director, and VP of Customer Success — the
  organizational sense of "customer escalation" (neither SLA-breach nor bot handoff): who must be
  told, by how bad it is. Full disambiguation: `support-process-design.md` §5.

## 4. What to decline, with reasons

- **A CSM-to-account ratio.** The entire literature is enterprise-CSM-team literature by
  definition — Gainsight's own telemetry (17,034 CSMs, median $1.4M ARR-per-CSM, 75th percentile
  $4.2M) is a real, measured dataset, but it's Gainsight's *own customer base*: companies large
  enough to already run a CS platform, systematically excluding solo/self-serve operators. There is
  no honest ratio to adopt below that segment; coverage comes from automation and product signal,
  not headcount.
- **The "$2M ARR per CSM" heuristic — the propagation exhibit, both sides permalinked.** Debunked
  by the canon's own co-author, repeatedly, at the platform where it kept circulating:
  lincolnmurphy, 2016–2017 — "Please STOP perpetuating the $2M/ARR per CSM myth"
  (x.com/lincolnmurphy/status/814160673840267264); "The '$2M ARR per CSM' nonsense is just what
  people want to hear... little connection to actual reality"
  (x.com/lincolnmurphy/status/829780774215757824). Still circulating on a larger platform years
  later, uncited: @saastr, 2019 and 2020 (x.com/saastr/status/1132844104050724864,
  x.com/saastr/status/1213173372068212737). Ship both sides together; never the number alone.
- **QBR/EBR cadence as a fixed ritual.** Murphy's own critique: "You don't have to do QBRs. Period.
  QBRs are not required" — reframed as "Is a QBR part of the Appropriate Experience for your
  customers?" (sixteenventures.com/customer-success-qbr). Decline the fixed cadence; keep the
  question it answers. EBR is a rebrand of the same ritual toward executive framing, not a
  different practice.

## 5. The account is the unit — sales seam

On this surface, retention means the account, not a user-day window: read it as logo retention
(did the account renew — binary per contract cycle) and revenue retention (NRR/GRR, see
[renewals-and-expansion](renewals-and-expansion.md)), never a user-level N-day/rolling/survival
window scaled up — `growth`'s surface-b2b-sales-assisted.md draws the identical distinction from
its side (§6, "Retention means the account, not the user").

The renewal/expansion ownership ruling — product models, success operates, sales closes the sale
where a negotiation exists — is provisional, and directly contested by the canon's own author:
lincolnmurphy's position is complexity-gated, not role-based — a CSM renews by default; only
genuinely complex renewals go to a dedicated CS-native resource, explicitly not "Account Management
carryover" (x.com/lincolnmurphy/status/1084526744290369537). Cite both positions; don't adjudicate
the fight. The handoff itself is a named failure mode for any sales-to-CS transition: "Customers
hate three things: 1. Surprises 2. Unknowns 3. Repeating themselves. Most Sales-to-CS handoffs
manage to hit all three" (lincolnmurphy, x.com/lincolnmurphy/status/2019458553430384815).

## Validation

- Any adopted health score is checked against §2's five failure modes before it's trusted.
- A CSM-ratio or QBR/EBR request is either implemented with §3's epistemics or declined with §4's
  stated reason — never silently ignored.
- The $2M/CSM figure never appears without both permalinked sides.
- Renewal ownership on this surface states the sales clause as provisional, not settled.

## Failure modes and handoff

- Treating GitLab's P.R.O.V.E. weights as a template to copy → they're an exhibit of failure modes
  to check for, not a starting configuration; copying the weighting columns adopts a schema
  without the discipline behind it.
- A stakeholder asks for a CSM ratio and gets silence instead of a reasoned decline → apply §4,
  cite the sample bias explicitly.
- The $2M/CSM number is quoted in a deck without its debunking attached → block it; this is the
  flagship's own class of never-ship figure.
- A renewal handoff from sales lands with no context → apply §5's named failure mode before it
  repeats.
- Recommended next: [renewals-and-expansion](renewals-and-expansion.md) for the ownership ruling
  and NRR mechanics in full; health-and-risk-signals.md for the flagship epistemics argument this
  file supplies evidence for.
