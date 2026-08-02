# When Success Applies

Purpose: Decide whether a distinct success function is worth building yet, before writing a single
onboarding plan, health score, or escalation policy — no source in the CS canon answers this
question, so this pack constructs the gate.

Read when:
- A request assumes a customer-success function should exist and the request has not justified
  that yet — a health score, a CSM-style playbook, or a renewal workflow is being asked for on a
  product that may not need one.
- Someone asks "do we need customer success" or "when do we hire/build for this."
- A request wants CS canon vocabulary (QBR, CSM ratio, health-score tooling) applied to a solo or
  small-team product.

Skip when:
- Success already applies (B2B/high-touch, or the gate below already passed) and the request is
  about a specific job — go straight to [onboarding-and-adoption](onboarding-and-adoption.md),
  [support-process-design](support-process-design.md), [health-and-risk-signals](health-and-risk-signals.md), or the other job references.
- The request is about retention *experimentation* (does a resurrection nudge work) rather than
  execution — that is growth's, not this gate's.

Inputs: what the product charges for, how revenue relates to the customer's own outcomes, team
size, and whether a support/success workflow already exists informally (a shared inbox, a founder
answering email).

Produces: an applies / lighter-weight / not-yet verdict, named and attributed rather than invented,
plus a pointer to whichever sibling packs already cover the gap in the meantime.

## Contents

- [The Existence Gate](#the-existence-gate)
- [What replaces the enterprise canon at solo scale](#what-replaces-the-enterprise-canon-at-solo-scale)
- [Canon outcomes survive; canon process does not](#canon-outcomes-survive-canon-process-does-not)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## The Existence Gate

No source in the CS literature — Gainsight's own book, the CSM-ratio literature, or any vendor
playbook — states when a distinct success function becomes worth having; the entire canon assumes
the function exists and only asks how to staff it (web-research channel, canon section). This pack
does not inherit that assumption. Use **the Existence Gate**, adapted from the one practitioner
sentence that gives it a checkable test — arvidkahl, solo founder (Podscan):

> "Customer Success (compared to mere customer support) is so much more important when your revenue
> scales with your customers revenue." — https://x.com/arvidkahl/status/1351985710325239821 (Jan 20
> 2021)

If the customer's growth increases what they pay (seat expansion, usage-based pricing, a
revenue-share), the CS motion earns its keep: watching account health, planning renewals, and
proactively driving adoption pays for itself because a bigger customer is a better customer. If the
product is flat-rate self-serve — the customer's success does not change what they owe — the honest
answer is lighter: a success function is optional until it visibly earns its cost.

This sharpens the family's own scoping note: "For B2B SaaS, services, enterprise products, or
high-touch products, `/success` is a first-class pack. For simple self-serve consumer products,
`/growth`, `/marketing`, and `/operate` may cover most post-purchase needs until a distinct success
workflow emerges." (`digital-product-skill/docs/product-lifecycle-skill-packs-exploration.md:1033`)
Use the arvidkahl test to decide which side of that line a product sits on, rather than guessing
from company size alone.

**Meanwhile, before the gate opens**: post-purchase needs do not go unowned. `marketing` covers
retention communication and onboarding education until a distinct workflow exists
(`marketing/references/handoff.md:43`); `growth` owns retention *experimentation* regardless of
whether success exists yet (`growth/references/handoff.md:43,49` — provisional, see
[handoff](handoff.md)); `operate` handles incident and decommission comms co-owned with `product`;
and `product` treats churn and support load as guardrail metrics in its own metric tree. A request
that looks like "we need a health score" is often better served, pre-gate, by one of those four
doing its existing job well.

## What replaces the enterprise canon at solo scale

Across five deep-mined solo/small-team operators (robwalling, arvidkahl, tylertringas, Shpigford,
plus a top-up on dvassallo and levelsio), not one used "QBR," "CSM ratio," "health score," or
"Customer Success" as a job title — a total vocabulary absence, not a disagreement (x-practitioners
channel, solo-support raws). The replacement the evidence actually shows is **not** "docs +
automation + product signals," which was this pack's original hypothesis. It is:

1. **Pricing first.** The most repeated, most specific lever in the whole solo territory.
   arvidkahl: "Churn hits much less hard when you have raised prices in between. Podscan had a $50
   plan at some point; now, most users choose the $200 plan… a single new sub makes up for four." —
   https://x.com/arvidkahl/status/2073028608054948002 (Jul 3 2026). robwalling independently: "I wish
   someone would warn startup founders that lower prices usually (i.e. almost always) lead to higher
   churn." — https://x.com/robwalling/status/2055022092811133330 (May 14 2026).
2. **AI tier-1 support second** — a lever the original hypothesis did not name at all. arvidkahl runs
   a "first-level AI CS agent" in production (https://x.com/arvidkahl/status/2081147490170991086, Jul
   25 2026); tylertringas folds a "shared support inbox"
   (https://x.com/tylertringas/status/2074889104823664653, Jul 8 2026) into an agent loop that
   monitors performance and errors, auto-pushes fixes, and reports back in Slack
   (https://x.com/tylertringas/status/2077828747752005676, Jul 16 2026). See
   [surface-selfserve-solo](surface-selfserve-solo.md) for the default-surface treatment of this.

   Even a fully-automated solo support stack keeps one human residue: levelsio still hits a pattern
   automation cannot close — "I wonder how to fix the last part of customer support I still get and
   can't automate: Customer buys 5,000 credits for $350. Then messages me: 'I signed up for $99/mo
   but it charged me $99 and then $350.'… Then they chargeback and I can't win ever anyway." —
   https://x.com/levelsio/status/2035010864487555379 (Mar 20 2026). It survives automation because
   it's a customer-memory/honesty problem, not a lookup problem — a solo-economics point: no amount
   of automation makes this residue zero, and the gate's verdict should say "lighter," never "zero."
3. **Docs-as-deflection returned almost nothing usable** across two independent research passes — an
   honest null, not a finding to route around.

**Ship this as a strong practitioner position with the absence noted, not a resolved fact
(CONTESTED).** Both robwalling and arvidkahl land on pricing as the lever; no practitioner in this
research argued the competing "better support/onboarding reduces churn independent of price"
position at all. That one-sidedness is evidence *for* a reframe, not proof of a settled contest.
Pair it with patio11's `product`-pack-owned mechanism, not success's: "$50 is a much better minimum
buy-in for most B2B services than $20 is. You'll make a lot more money, sure, but you'll enjoy the
reduced support headaches and vastly lower churn even more." —
https://x.com/patio11/status/1261177745330987008 (May 15 2020). Support volume and churn are often
downstream of a pricing decision, not a support-process failure — an honest success pack teaches
when the fix is not its job.

## Canon outcomes survive; canon process does not

Solo operators are not rejecting the CS canon on the merits — the silence itself is the evidence (no
dunks, just absence). What survives is the *outcome vocabulary*: Shpigford celebrates Net Negative
Churn unreservedly as the "SaaS holy grail," adopting a canon *metric* while never adopting the
organizational apparatus (a CSM function, QBR cadence, health-score tooling) the canon wraps around
it. Teach the outcome vocabulary; do not teach the process apparatus as a prerequisite for it.

patio11 independently names the same gap from the outside, with no stake in this pack: customer
support is "generally poorly understood outside of enterprises, and on the cusp of industrial
reorganization" — https://x.com/patio11/status/2011881322541920620 (Jan 15 2026).

## Validation

- The verdict names which side of the arvidkahl test the product is on, not a size-based guess.
- If the request assumes a CS function exists, the gate is answered before any downstream artifact
  (health score, playbook, renewal workflow) is produced.
- The pricing-first correction is presented as CONTESTED, never as a settled fact.
- Any churn or support-load figure quoted here carries its source and its "P" (practitioner-report,
  no published method) grade — never presented as a benchmark.

## Failure modes and handoff

- Building a CS playbook because the product is B2B, without checking whether revenue actually
  scales with the customer's — apply the arvidkahl test explicitly.
- Recommending ticket triage or an onboarding rebuild to fix churn that a pricing or segment
  mismatch is actually causing — route to `product`'s pricing job first per patio11's angle.
- Treating "pricing beats support quality as a churn lever" as resolved instead of one-sided-but-
  unopposed — say so explicitly when citing it.
- Assuming solo builders reject CS outcomes along with CS process — Net Negative Churn survives;
  teach it.
- When the gate says "not yet," silently inventing a success artifact anyway instead of naming which
  sibling (`marketing`, `growth`, `operate`, `product`) already covers the need — see
  [handoff](handoff.md) for the full seam map.
