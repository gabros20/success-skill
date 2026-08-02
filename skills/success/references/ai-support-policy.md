# AI support policy

Purpose: Define the policy layer for an AI support agent — what counts as a resolution, when it must
hand off to a human, which moments require canned text versus free composition, and how to read a
vendor's automation claim honestly. Seam: `ai`'s `references/surface-chat-assistant.md` owns the
turn loop, retrieval, and eval instrumentation; **this file owns what "escalation rate" means** —
the condition, the resolution it's paired against, and the bot-boundary rules `ai`'s eval measures.

Read when:
- Defining when a bot hands off to a human, what "resolved" means, or how strict a reply must be.
- Reading a vendor's resolution/deflection/automation claim honestly.
- Escalation vocabulary, consent-before-handoff design, or bot-boundary/rollout gating.

Skip when:
- Retrieval quality, prompt design, the turn loop, or online-eval mechanics — `ai`'s
  `references/surface-chat-assistant.md`.
- Deterministic envelopes for an unbounded agentic step (spend ceilings, kill switches) — this pack's
  own [overlay-agentic.md](overlay-agentic.md).
- KB article quality or the zero-result/zero-click backlog — →
  [education-and-knowledge-base.md](education-and-knowledge-base.md).

Inputs: whether a human is present every turn, some turns, or none (sets strict-vs-fluid composition
and which triggers apply); the support taxonomy already in use — cite
[support-process-design.md](support-process-design.md) rather than re-deriving it.

Produces: a symbolic escalation-trigger set (never a confidence float); a resolution definition paired
with a renewal/reopen signal; a strict/fluid composition boundary; an honest read of any vendor number.

## Contents
Escalation is symbolic · The typed-field exemplar · Strict vs fluid composition · Resolution-rate
honesty · Reading pass^k against a vendor claim · Klarna as a tier-design lesson · Chatbot promises
bind the company · Validation · Failure modes and handoff

## Escalation is symbolic, never a confidence float

Real implementations converge on one negative: **no production escalation policy fires on a numeric
model-confidence threshold.** Every trigger found is symbolic or another LLM's categorical output,
gated by consent:

1. **Scope boundary** — out of tool/domain capability. Cleanest statement: "You should transfer the
   user to a human agent if and only if the request cannot be handled within the scope of your
   actions" (`sierra-research/tau-bench@main:tau_bench/envs/retail/wiki.md`; same clause at
   `tau2-bench@main:.../telecom/main_policy.md:13`, MIT).
2. **Explicit request, or consent to an offered handoff** — Chatwoot Captain's prompt names five
   conditions that may *offer* a handoff (explicit ask, an accepted offer, a matched guardrail,
   permission needs, repeated failure) but the tool itself is gated to fire only once the user has
   asked, accepted, or an admin guardrail requires it (Chatwoot's assistant logic sits under its
   enterprise/ source-available license — describing the pattern, not quoting the template). Low
   confidence or repeated failure alone is never sufficient on its own.
3. **Admin-authored guardrail** overrides the consent default.
4. **Time-of-day** — `huabeitech/agent-desk` (Apache-2.0) auto-hands-off off-hours with no
   confirmation; in-hours requires explicit double-confirmation.
5. **Repeated failure** — named as grounds to *offer*, never to auto-fire.
6. **Pure intent classification** — Rasa's `human_handoff` intent (Apache-2.0), no other signal;
   this reference bot can only simulate handoff without a wired live-agent system.
7. **LLM triage classifier as a recommendation layer**, still gated by consent downstream.
8. **Structural pre-gate** — a bot may not speak at all if a human is already assigned, or via a
   deterministic staged-rollout hash pinning one conversation inside/outside the AI rollout for its
   whole lifetime. Percentage rollout gating is a bot-boundary control, prior to escalation policy.
9. **A required typed field, emitted every turn** — see below.

Even Chatwoot hasn't built tier-aware routing into its handoff tool — `team_id`/`priority`/
`escalation_level` fields remain commented-out and unimplemented. Ship a flat handoff primitive by
default; treat tier-aware routing as a stated gap.

**Two different objects share the word "escalation."** Always write **customer escalation** for the
bot-to-human sense; the full disambiguation lives in
[support-process-design.md](support-process-design.md) §5.

## The typed-field exemplar

`anthropics/claude-quickstarts` (MIT; renamed from `anthropic-quickstarts` — the old name still
redirects, cite the current one) makes escalation a **required typed field emitted every turn**:

```ts
user_mood: z.enum(["positive","neutral","negative","curious","frustrated","confused"])
redirect_to_agent: z.object({ should_redirect: z.boolean(), reason: z.string() })
```

Loggable and auditable by construction. Its three triggers are all symbolic: no relevant information
retrieved, question unrelated to the product, or the user explicitly asks for a human.

**Precision guard, protected:** `user_mood` is recorded *alongside* the redirect decision — never a
trigger for it. The worked example pairs `frustrated` with `should_redirect: true`, but no rule says
frustration causes escalation. This tracks sentiment as a first-class dimension while keeping the
escalation rule scope-based — better than the sentiment-triggers-handoff pattern vendors describe.
Never report this as "escalates on frustration" — design the same way: log mood, decide on scope. (The
reference is genuinely RAG but not self-contained — it delegates retrieval to a managed AWS knowledge
base; cite it for the escalation contract, not retrieval mechanics, which are `ai`'s. Its `internal`
taxonomy category — a bucket for contacts that aren't support at all — is covered in
[support-process-design.md](support-process-design.md).)

## Strict vs fluid composition

`emcie-co/parlant` (Apache-2.0) names this pack's core design question precisely: after tool-calling,
does the flow branch to a generated message, or a canned one from a pre-approved set?

- **Guidelines** — condition→action rules matched per turn.
- **Relationships** — dependency and **exclusion** edges between guidelines; a support policy needs
  conflict resolution as a first-class edge, not prose ordering.
- **Journeys** — multi-turn SOPs as a state machine the agent may enter out of order.
- **Canned responses** — pre-approved templates that eliminate composition risk at critical moments.

**The split, as a design question:** at which moments may the bot compose freely, and at which must
it only select pre-approved text? Refunds, cancellations, compliance statements, and outage
acknowledgements are the obvious strict moments — default to canned, require an explicit decision to
relax it. Grade Parlant's own reliability evidence carefully: an arXiv citation plus named testimonials
and an unsourced "deployed at the most stringent organizations" line — practitioner-report-adjacent
at best; cite the vocabulary, not the banks claim.

## Resolution-rate honesty

**No source defines "resolution rate" precisely enough to audit.** Non-vendor voices treat deflection
(closed without reaching a human) and resolution (problem actually solved) as different by default;
vendor claims report a number without disclosing how "resolved" was adjudicated. **Intercom Fin's own
published definition is the one fully verified, primary-source definition found**: a resolution counts
when the customer confirms the answer, or **exits without requesting further assistance** — the latter
counted as "assumed resolution." An exit without complaint is not confirmed success, and the vendor's
own naming concedes it. Treat any vendor headline number as inheriting this ambiguity unless it states
which category drove the count.

**Pair resolution with renewal — never ship resolution alone.** A bot told to maximize resolution rate
learns to close tickets, not fix problems, while the number climbs and the customer leaves. Pair
resolution with renewal (resolutions up, renewals down = deflecting, not solving); response speed with
error rate; task completion with human-override rate. One metric alone invites gaming.

**Deflection is unmeasured even at organizations that publish almost everything else about their
support org.** One of the most detailed public support handbooks lists ticket deflection as a wishlist
KPI and states, on its own currently maintained page, that the dashboard to measure it "is a work in
progress." No open-source tool measures true deflection (read an article, did not open a ticket) —
every number found is a proxy the source itself hedges. **Teach zero-result/zero-click KB queries as
the deflection replacement** — observable, no counterfactual problem — mechanics in
[education-and-knowledge-base.md](education-and-knowledge-base.md).

**No single "industry" automation figure ships.** Every headline percentage circulating as *the*
deflection/resolution rate traces back to a set of selected cases wearing an average's clothes;
ship the mechanism (pair resolution with renewal, distinguish confirmed from assumed), never the
number — and do not name the number in order to forbid it, which is how it spreads.

## Reading pass^k against a vendor claim

τ-bench/τ²-bench (`sierra-research/tau-bench`, `tau2-bench`, both MIT — cite Yao et al. 2024, Barres
et al. 2025 (the tau2-bench grading update), and the SABER error-taxonomy paper; MIT licenses the
files, not the methodology) measure whether the same
agent resolves the same task reliably across repeated trials — pass^k, via C(c,k)/C(n,k). **Cite the
mechanism, never the specific published numbers**: the maintainers shipped a grading update warning
that pre-update results aren't comparable, and a companion paper documents 75+ task fixes for
"incorrect expected actions… impossible constraints." A support-agent benchmark number is stale by its
own author's admission.

What pass^k demonstrates regardless of the number: single-shot success routinely looks decent while
reliability across repeated attempts is substantially worse. **This is the canonical rebuttal to any
"our AI resolves X% of tickets" claim that discloses neither n nor k.** Grade every vendor
resolution/deflection number as vendor-claim, always — self-reported figures carry zero independent
verification regardless of how consistently they're repeated.

## Klarna: a tier-design lesson, not a reversal story

**Never tell the Klarna reversal story.** It is triple-refuted: the CEO calls "we failed with AI" a
misquote; his own statements frame the hiring increase as a deliberate human-touch bet running
*alongside* continued AI efficiency, not a reversal; and the original 2024 numbers (the press
release's "700 full-time agents" — a figure Siemiatkowski's own parallel post frames against a
baseline of "3000 full time agents" for the whole customer-service operation, with no source
reconciling the two — plus the $40M profit improvement and the 25% drop in repeat inquiries) have
never been independently audited — every source either repeats the press release or tests the
bot's behavior without auditing the financial claims. An
"always a human if you want" option existed from the original 2024 launch, not as a later addition.

**The lesson to teach is tier design**: which conversations get an automated tier, which get a human
tier, and under what named condition one moves to the other — stated before launch. Cite the
strict/fluid boundary above as the mechanism; do not reach for Klarna as the illustration.

## Chatbot promises bind the company

*Moffatt v. Air Canada*, 2024 BCCRT 149 (Feb 14, 2024): a chatbot told a customer he could apply for a
bereavement fare retroactively; the airline couldn't. Air Canada argued it wasn't liable for the
chatbot's words. The tribunal's rejection, verbatim: "it is still just a part of Air Canada's website…
It makes no difference whether the information comes from a static page or a chatbot." Negligence
finding: Air Canada "did not take reasonable care to ensure its chatbot was accurate" — the correct
answer existing elsewhere on the site did not excuse the wrong one. Damages: $650.88 plus interest.

Applied lesson: a bot's claims carry the same liability exposure as a static page. Curate any
strict-mode content (refund policy, cancellation terms, compliance statements) with this exposure in
mind — the fluid/strict boundary above is where liability risk concentrates, not just a quality knob.

## Validation

- Every escalation trigger is symbolic — no numeric confidence threshold anywhere in the design.
- Sentiment/mood tracking, if present, is a recorded dimension, never a trigger, unless a source
  explicitly ties the two.
- Every resolution/deflection figure carries its method, or is stated as vendor-claim with none.
- The strict/fluid boundary names which specific moments require canned text.
- The Klarna reversal narrative appears nowhere, and no single-figure "industry" deflection or
  resolution percentage appears anywhere — including inside a sentence forbidding it.

## Failure modes and handoff

- **Escalation designed around a confidence score** — no real implementation uses one; redirect to
  the symbolic trigger set above.
- **A vendor number reported without its method** — state vendor-claim and the missing n/k or
  confirmed-vs-assumed split, or don't ship the number.
- **Retelling the Klarna reversal anecdote** — cite the tier-design lesson instead.
- **The real ask is retrieval, the turn loop, or eval instrumentation** — `ai`'s
  `references/surface-chat-assistant.md`; hand off the escalation contract
  and resolution definition so `ai`'s evaluation measures the right event.
- **The real ask is KB quality or the deflection-replacement backlog** — →
  [education-and-knowledge-base.md](education-and-knowledge-base.md).
