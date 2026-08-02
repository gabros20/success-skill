# Retention Execution

Purpose: Send the churn-save, win-back, or renewal-nudge motion a growth test already validated —
as an ongoing part of holding the customer relationship, not as a new experiment. This is the job
`growth` named and reserved for this pack.

Read when:
- A retention or resurrection mechanic has already been tested and validated, and someone needs it
  run on an ongoing basis (a cancellation flow, a win-back sequence, a renewal-risk nudge).
- A customer is cancelling and the cancellation flow, reason capture, or save attempt needs
  designing or auditing.
- Someone asks whether a churn number reflects a support/relationship problem or a pricing problem.
- A circulating "we changed X and churn dropped" claim needs its confound flagged before reuse.

Skip when:
- The mechanic has not been validated yet — designing or reading that test is `growth`'s job, per
  `growth/references/handoff.md:43`.
- The question is which accounts are at risk, or a health score's honesty — see
  [health-and-risk-signals](health-and-risk-signals.md); this file only asks who to act on once a
  signal exists.
- The question is whether success should exist for this product at all, or whether churn is a
  pricing problem before it's a relationship problem — see
  [when-success-applies](when-success-applies.md)'s CONTESTED pricing plank; do not re-litigate it
  here.
- The churn is involuntary (a failed card, a dunning sequence) — that mechanism is `product`'s
  (`marketing/assets/email-compliance-checklist.md:82`); this file covers the relationship side once
  a churn event is confirmed voluntary.
- The question is a habit/streak/persuasion-ethics ruling in general — `growth`'s
  monetization-and-pricing-experiments.md owns that; §4 below only points to it.

Inputs: a growth-validated retention or resurrection readout (or an explicit decision to adapt a
named practitioner exemplar rather than an internal test), the current cancellation/win-back flow if
one exists, and whichever health/risk signal identified the account.

Produces: a running churn-save/win-back/renewal-nudge motion with its reason taxonomy, a
voluntary/involuntary split on the churn numbers behind it, and an explicit ethics check on the
cancellation flow itself.

## Contents

- [1. The third box](#1-the-third-box)
- [2. The churn-save structure: diagnose, attempt, exit cleanly](#2-the-churn-save-structure-diagnose-attempt-exit-cleanly)
- [3. Target by uplift, not risk rank](#3-target-by-uplift-not-risk-rank)
- [4. Cancellation ethics — cite, do not re-adjudicate](#4-cancellation-ethics--cite-do-not-re-adjudicate)
- [5. The pause-instead-of-cancel exemplar, and a confounded number](#5-the-pause-instead-of-cancel-exemplar-and-a-confounded-number)
- [6. Voluntary vs involuntary — split before concluding anything](#6-voluntary-vs-involuntary--split-before-concluding-anything)
- [7. The pricing scope-limiter — a pointer, not a restatement](#7-the-pricing-scope-limiter--a-pointer-not-a-restatement)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## 1. The third box

`growth/references/handoff.md:66-67` reserves the literal job name `retention-execution` for this
pack — it names the slot and builds nothing into it. Growth's own working rule
(`growth/references/retention-and-resurrection.md:168-169`) classifies a retention or resurrection
mechanic into only two boxes: **standing** (`operate`'s) or **experiment-bound** (`growth`'s). This
file draws the third box: a **validated motion, held as an ongoing customer relationship**, is
success's — a churn-save sequence, win-back campaign, or renewal-risk nudge that a growth test
already validated, now running as part of how this pack holds the relationship, not as a system
threshold or a live test.

The consequence: nothing in this file designs a new save offer or tests whether a discount works —
that decision is growth's. This file runs the motion growth already validated, and owns the flow,
the reason taxonomy, and the exit-interview capture around it.

## 2. The churn-save structure: diagnose, attempt, exit cleanly

`churnkey/sdk` (MIT-licensed) encodes a structure worth teaching directly: a cancellation flow that
maps **reason → matched offer**, where the offer type is a function of the stated reason (too
expensive → discount; not using it enough → pause; missing a feature → **no offer, just capture** —
some reasons have no honest save and the flow should record them as churn-with-a-reason rather than
fight them). The flow runs three distinct jobs in order: a reason survey, a matched save attempt,
then an unobstructed confirm step. The reason-survey step doubles as the highest-signal VoC moment a
self-serve product gets — feed it to [voice-of-customer](voice-of-customer.md)'s reason-taxonomy
discipline.

The seam inside this exhibit is exact: whether a given offer *works* (does a 20%-off coupon actually
save more accounts than a pause does) is growth's experiment; the flow, the reason taxonomy, and
running it are this pack's execution. Design a new offer-to-reason mapping only as a growth-readout
result; run and maintain an already-validated mapping here.

## 3. Target by uplift, not risk rank

[health-and-risk-signals](health-and-risk-signals.md) §4 already carries Ascarza 2018's field-
experiment finding that the highest-risk accounts are not necessarily the accounts that respond best
to a save attempt — risk-ranking and response-ranking (uplift) are different orderings, and one
segment in that study got *worse* under intervention. Do not re-derive those numbers here; the
execution consequence is: the account list this file acts on should be uplift-ranked (who responds),
not simply the reddest health-score accounts. Absent an uplift model, the safe default is to not
reflexively spend the heaviest save effort on the single highest-risk segment — that is the specific
error Ascarza's experiments measured.

## 4. Cancellation ethics — cite, do not re-adjudicate

`growth/references/monetization-and-pricing-experiments.md` §5 already ships the dark-patterns
evidence for subscription cancellation flows — Mathur et al. (CSCW 2019, 11.1% of 11,000 crawled
sites carried at least one dark pattern), the **roach motel** pattern name (easy to get in, hard to
get out), and the FTC's 2022 enforcement signal (the Vonage $100M negative-option settlement). Cite
that file; ship none of its content here.

The operative test this file adds: after a save offer is shown, does cancellation remain reachable
in one click? If the offer blocks or hides the exit path, it is the roach-motel pattern regardless of
intent. Two practitioners (levelsio and dvassallo — see §5) independently and repeatedly condemn
deliberately-hard-to-cancel design across years, while the wider CS canon assumes a human retention
touchpoint before cancellation completes. This tension is recorded as an open design-ethics line, not
resolved here — apply the one-click-reachable test rather than picking a side.

## 5. The pause-instead-of-cancel exemplar, and a confounded number

levelsio's pause-subscription idea is a full, first-person, permalinked multi-year arc: the original
idea (https://x.com/levelsio/status/679767525723369472, Dec 23 2015) — automatically pause a
subscription when usage stops, rather than charge an inactive user; a UX-naming judgment the same day
(https://x.com/levelsio/status/679792473091227648) — "I'd say Pause, but Unsubscribe is clearer,"
reasoning about clarity to the customer, not just MRR; and confirmation it shipped two years later
(https://x.com/levelsio/status/933308392021442561, Nov 22 2017). No isolated effect size was ever
stated for the pause button itself — do not invent one.

**A separate exhibit must carry its CONFOUNDED flag whenever cited.**
https://x.com/levelsio/status/1949861989322314094 (Jul 28 2025): a custom-built cancel flow
(replacing Stripe's customer portal) alongside a reported churn drop from 40% to an all-time low of
13–14%. Levelsio's own parallel tweets attribute much of the same period's churn improvement to
unrelated product-quality launches (a photorealism model upgrade, a v2 launch) and to a separate
churn-recovery-by-discount tactic, stated with his own hedge
(https://x.com/levelsio/status/1758514737539596477, Feb 16 2024): "#1 reason is [a product upgrade]…
#2 reason is better churn recovery, offering discounts to avoid canceling… TL;DR **I guess** improving
product is best way to fix churn." **Never cite the cancel-flow rebuild as "cut churn by two-thirds"**
— cite it as a practitioner who rebuilt a cancel flow and separately reports a large churn drop over
the same broad period, with multiple unlabeled contributing causes. The hedge itself ("I guess") is
worth citing directly as a model for stating an unmeasured causal claim honestly.

## 6. Voluntary vs involuntary — split before concluding anything

`marketing/assets/email-compliance-checklist.md:82` assigns dunning and billing-failure recovery to
`product` — a shipped ruling this pack honors rather than re-litigates. Any churn number handed to
this file must separate voluntary cancellations from involuntary (failed-payment) churn before a
retention conclusion is drawn from it; conflating the two attributes a billing-recovery outcome to a
relationship motion, or vice versa. This file owns the relationship-side save (§§2–5) once a churn
event is confirmed voluntary; it does not build or own the billing-retry mechanism itself.

## 7. The pricing scope-limiter — a pointer, not a restatement

[when-success-applies](when-success-applies.md) already ships the full CONTESTED pricing plank —
patio11's minimum-buy-in economics, robwalling's price-to-churn link, and the "10%+ monthly churn is
often a pre-PMF signal" position — with its own CONTESTED marking (a strong, one-sided practitioner
position, not a resolved fact). Before running a save motion, check that file's gate: if the churn is
a pricing/value signal, route to `product`'s pricing job first; do not spend relationship-execution
effort on a problem execution cannot fix.

## Validation

- Every motion this file runs was validated by a growth readout, or is explicitly labeled an adapted
  practitioner exemplar rather than an internal test result.
- Every levelsio number carries its stated grade — CONFOUNDED for the cancel-flow rebuild, hedged
  ("I guess") for the discount-recovery claim — verbatim, never smoothed into a clean causal result.
- The account list a save effort targets is checked against uplift, not raw risk rank (§3).
- A cancellation flow was checked against the one-click-reachable test (§4) before shipping.
- Churn figures behind any retention decision are split voluntary/involuntary (§6) before use.

## Failure modes and handoff

- **Designing a new save offer or testing whether a discount works inside this file** — that is
  growth's experiment; only run what growth already validated (§1).
- **Citing the levelsio cancel-flow rebuild as a clean churn-reduction result** — banned; it is
  CONFOUNDED (§5).
- **Building or altering a dunning/billing-retry sequence here** — that is product's
  (`email-compliance-checklist.md:82`); route it there.
- **Targeting the highest-risk accounts by default for a save effort** — apply the uplift correction
  in §3, citing health-and-risk-signals.md rather than re-deriving it.
- **Shipping a cancellation flow that hides or blocks the exit path after a save offer** — apply
  growth's monetization-ethics file (§4); do not rule on habit/persuasion ethics from this file.
- **Running a save motion before checking whether the churn is actually a pricing problem** — route
  to when-success-applies.md's gate first (§7).
