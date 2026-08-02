# Education and Knowledge Base

Purpose: Define what belongs in a knowledge base, keep it from rotting, and replace the
unmeasurable "deflection rate" with an instrument that is actually observable.

Read when:
- Deciding what a knowledge-base article is *for*, or whether something belongs in the KB versus
  product documentation.
- Setting an article review/staleness cadence, or auditing an existing KB for rot.
- Someone proposes measuring "deflection" or a KB's ROI, or cites a vendor deflection percentage.
- Choosing where to invest next: a better AI model, or better source content.

Skip when:
- The question is KB navigation, labeling, or information architecture → cite
  `design/references/information-architecture.md` (nav 2–7 items, flat hierarchy reachable in 2–3
  clicks, plain labels over clever ones, card-sort/tree-test validation) — this file owns what
  belongs in a KB and how honestly to measure it, not how to structure the site around it.
- The question is developer-facing API/SDK documentation → that is the general `docs-writer`
  skill's territory, not this pack's customer-facing KB.
- The question is AI-agent resolution-rate honesty or bot escalation policy →
  [ai-support-policy](ai-support-policy.md).
- The question is ticket taxonomy or SLA metrics → [support-process-design](support-process-design.md).

Inputs: existing help content (or none), any deflection/resolution claim someone wants to ship,
search-analytics access if available.

Produces: a KB scope decision (what belongs, what doesn't), an article-lifecycle policy, and a
deflection-honesty stance backed by an observable backlog instrument instead of a percentage.

## Contents

- [1. What a knowledge-base article is — and isn't](#1-what-a-knowledge-base-article-is--and-isnt)
- [2. Article lifecycle: maintain aggressively or don't ship it](#2-article-lifecycle-maintain-aggressively-or-dont-ship-it)
- [3. Deflection is unmeasurable — the honest replacement](#3-deflection-is-unmeasurable--the-honest-replacement)
- [4. KB quality beats model upgrades — the best first-party evidence found](#4-kb-quality-beats-model-upgrades--the-best-first-party-evidence-found)
- [Validation](#validation)
- [Failure modes and handoff](#failure-modes-and-handoff)

## 1. What a knowledge-base article is — and isn't

No pack in this family defines good help content; it is a grep-verified empty slot (Nielsen's
"help & documentation" heuristic is *scored* by webdesign's design-critique but never defined
anywhere across twelve shipped packs). The cleanest available distinction, worth lifting as a
framework (CITE, attribute GitLab — the prose license is scoped to "the GitLab Software," not the
handbook content, so paraphrase and link; only the one-line tie-breaker below is quoted):

Knowledge articles are reactive — ticket-triggered, for a specific broken-in-this-config problem.
Documentation is proactive — feature-complete, for learning intended behavior (paraphrased, not
GitLab's wording). GitLab's own handbook states the practical tie-breaker directly:

> "When in doubt, create a knowledge article… it can always be promoted to documentation."
> (GitLab support handbook, `support/knowledge-base/docs-vs-kb.md`)

Use this as the scope test: if the content answers "why is *my* setup broken right now," it's a KB
article; if it answers "how does this feature work," it's documentation, and the seam with product
documentation is real, not a formality. When a piece of content could go either way, GitLab's
default direction is the practical answer: write it as a KB article first — promoting it later
costs nothing, and under-scoping the KB starves the reactive layer that a stuck customer actually
needs in the moment.

## 2. Article lifecycle: maintain aggressively or don't ship it

A stale article is worse than a missing one — it actively misdirects a customer who already
trusted it. Anthropic's own shipped kb-article skill states this as a first-party rule and backs
it with a review-cadence table (`anthropics/knowledge-work-plugins@ea31164:customer-support/
skills/kb-article/SKILL.md:266-277,349`, Apache-2.0):

> "Maintain aggressively — a wrong article is worse than no article."

Ship a lifecycle policy alongside every KB, not just a publishing workflow: who owns re-verifying
an article against the current product, on what cadence, and what happens when a support agent
flags an article as wrong in the field (the fastest staleness signal available, and one this pack
should route back to whoever owns the article, not silently patch around in the ticket).

## 3. Deflection is unmeasurable — the honest replacement

**Deflection needs a counterfactual it cannot observe.** The standard method counts KB article
views or help-center sessions that didn't produce a ticket as a "deflection" — but that can't
distinguish a customer who found the answer from one who gave up, switched to email, or came back
later as an unlinked "new" ticket. No tool or benchmark examined runs a controlled measurement (a
held-out group without the article, compared on contact rate); every deflection number in the
industry is a proxy its own vendor hedges.

**This is not an inference from absence — the most transparent public support org in this pack's
research says so about itself, currently.** GitLab's own knowledge-base reporting page lists
"Ticket Deflection" and "First contact resolution" as things it *wants* to measure, in a bulleted
wishlist beside article views and search counts, then states outright: "We are currently working
with our metrics team members to build a Dashboard for KCS and Knowledge Management. **This is a
work in progress.**" (`support/knowledge-base/reporting-and-metrics.md`, CITE-ONLY, prose license
ambiguous). A company that publishes essentially everything else about how its support org runs
does not have deflection instrumented. **Teach "we do not have deflection measurement" as the
default, and grade any vendor's specific deflection-rate percentage as vendor-claim, never as a
fact** — the same discipline this pack applies to health-score and resolution-rate claims
elsewhere.

**The constructive replacement: zero-result and zero-click queries.** Algolia's own search
analytics — checked directly — ship *No results rate*, *No clicks rate*, *Searches without
results*, and *Searches without clicks*; the word "deflection" appears nowhere in that
documentation. The distinction that makes this work: deflection is unobservable because it needs
the counterfactual (would this person have filed a ticket?), but **a docs failure is directly
observed** — a query that returned zero results, or results nobody clicked, is a fact about the
docs, independent of what the customer did next. Teach the zero-result/zero-click backlog, not a
deflection rate: it costs nothing beyond a docs site with search, it measures the *docs* rather
than the support queue (which is exactly why it can be measured at all), and it yields a ranked,
actionable list — these exact phrases failed, in volume order — that a KB owner can work down
directly. Note the seam explicitly: designing a genuine held-out deflection experiment is
`growth`'s method; executing the KB content that experiment would test is this pack's job.

A related, narrower honest limit worth knowing before adopting a "was this helpful?" widget:
mkdocs-material's feedback template ships the UI only, not the recording, and its own maintainer
documentation flags that Google Analytics 4 has no built-in average-rating metric and reports can
lag 24+ hours — and, by construction, a helpfulness click cannot be joined to "did this visitor
later file a ticket." Treat a helpfulness click as a perceived-helpfulness proxy, not a deflection
measurement.

## 4. KB quality beats model upgrades — the best first-party evidence found

The strongest actionable evidence in this pack's research for where to invest next: a founder
reports raising AI-support resolution from roughly 20–25% to 85% by rewriting the knowledge base —
"rewrote our whole knowledgebase, changed how [the support agent] handles tickets, expanded what it
could resolve on its own, added 30+ knowledge base articles in just 2 months"
(x.com/nikolak47/status/2077405086431772785, Jul 15 2026; grade: practitioner-report, first-person,
no independent audit) — **not a model upgrade**. Before reaching for a better AI model or a vendor
switch to fix poor resolution, check KB coverage and correctness first: this is the one concrete,
first-party data point in the corpus that says the content is more often the bottleneck than the
model.

## Validation

- Any content proposed for the KB has been scoped as reactive (KB) or proactive (documentation)
  per §1, not defaulted into the KB by convenience.
- Every shipped KB carries a stated review cadence and an owner, not just a publishing workflow,
  per §2.
- No deflection-rate number is presented as fact anywhere this pack touches; a zero-result/
  zero-click backlog is the instrument offered instead, per §3.
- Before recommending a model or vendor upgrade for poor AI-support resolution, KB coverage and
  article correctness have been checked first, per §4.

## Failure modes and handoff

- **A vendor's deflection or resolution percentage is quoted as a fact** — relabel it vendor-claim
  per §3 and offer the zero-result/zero-click backlog as the honest alternative instrument.
- **A "was this helpful?" widget's click-through is reported as a deflection number** — it is a
  perceived-helpfulness proxy at best; state the join it cannot make, per §3.
- **An article is known to be wrong but stays live because nobody owns re-verifying it** — that is
  the lifecycle failure §2 exists to prevent; assign an owner and cadence before shipping the next
  article.
- **The KB/documentation seam is being redrawn ad hoc** — apply §1's reactive/proactive test rather
  than deciding case by case.
- **A genuine controlled deflection experiment (held-out group, contact-rate comparison) is being
  designed** — that is `growth`'s method; this file executes the content, it doesn't design the
  experiment.
