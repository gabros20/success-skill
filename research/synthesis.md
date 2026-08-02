# success-skill research synthesis (controller gate)

Date: 2026-08-02 · Author: controller · Status: GATE — writers build from this document.
Inputs: all five channel reports + their 21 raw files (linked from each report) + charter.md.
Reports: skills-ecosystem-report.md (A) · x-practitioners-report.md (B) · github-report.md (C) ·
web-research-report.md (D) · webdesign-lift-report.md (E). Where this document and a report
disagree, the report's raw evidence wins — flag the conflict, don't silently follow either.
Charter corrections: E §4 items 1–6 are ACCEPTED and bind over charter.md's text.

---

## 1. Verdict: the niche is open — by fragmentation, not absence

No incumbent of marketing's kind exists. Three partial incumbents, zero overlap, nobody integrates
(A): coreyhaines31 has REACH (churn-prevention 84.2k installs) but only 2 of our 12 canonical
includes, zero citations; anthropics/knowledge-work-plugins customer-support (23,246★) is OFFICIAL
but tactical-only (triage/escalate/KB-article — zero onboarding/health/renewal/VoC);
t0ddc3by/claude-for-customer-success (81 skills, © SuccessCOACHING) is ARCHITECTURAL but cites
nothing (0 external URLs in 28,988 lines), is enterprise-CSM-only, and is unadopted (~1 install per
skill). C found the same emptiness from the repo side: the sole awesome-customer-success list has
24★ of vendor self-adds; the health-score category tops out at 0–1★.

**The flagship framing constraint (A, controller-adjudicated):** t0ddc3by ALREADY asks "does it
actually predict churn, or does it just classify accounts?" — we may NOT frame the flagship as
"nobody asks this." Our differentiation is: we answer the question WITH evidence, with honest
scope, and integrated across support + AI-agent policy — the only pack that asks it does none of
those, and no pack anywhere does all four.

## 2. The wedge (final form)

Four planks, all evidence-backed:

**P1 — The observability-and-prediction honesty layer (flagship).** Final form of wedge 2, upgraded
by D: *"what a score can predict, why predicting correctly still may not help, and whether your
churn event is even observable."* Evidence spine:
- **GitLab (C):** the most transparent enterprise CS org does NOT ask its health score to predict
  churn — prediction is two separate models (PTE/PTC); backtesting the score is a stated GOAL, not
  a result; the weighted model is decorative at the red boundary (CSM-sentiment override); for a
  customer's first 30 days the score IS the CSM's opinion.
- **The null-result triangle (D+C):** 5 CS vendors → the entire OSS repo corpus → GitLab (in-house
  DS team, drift detection documented, evaluation standard published as qualitative prose): nobody
  publishes churn-model accuracy. **Binding writer guard: say "not published," never "not
  measured."** Assertable form: a reader cannot verify any of these scores; an uncalibrated star
  rating cannot be audited by the person relying on it.
- **Four-study academic convergence (D):** Ascarza 2018 (highest-risk customers respond LESS to
  intervention; one segment backfired +2.8pp) · de Haan 2015 (tenure r=.199 out-predicts every
  feedback metric; best ≈4% of variance) · van Doorn 2013 (metrics predict current, not future) ·
  Fader/Hardie BTYD (contractual vs NON-contractual: in non-contractual settings the churn event
  is not observable — the canon never makes the distinction).
- **Honest ceilings (C):** the one public churn dataset's clean ceiling is acc 78–81% / churn-F1
  0.60–0.62 / AUC 0.83–0.85; the 93–94% headlines are leakage (SMOTEENN-before-split) or
  base-rate theater (94.6% headline vs 85.5% predict-nobody-churns).
- **Anchor anecdote (B):** Shpigford, founder of a churn-analytics company, publicly unable to
  attribute his own 2× churn improvement ("What did we do…? ¯\_(ツ)_/¯", Jun 2017, permalinked).
- **The honest reframe to teach (C):** score + mandatory gap/action = a prioritization device;
  the same number alone next to a renewal date = folklore. Health diagnostics and churn prediction
  are DIFFERENT ARTIFACTS (GitLab's own architecture). Epistemics to lift attributed: input expiry
  dates, segmented thresholds (measures switched OFF for tech-touch, not scored badly),
  ignorance-is-a-finding (take the human rubric's side), reason taxonomies with tie-breakers.

**P2 — The existence gate (wedge 1, sharpened).** No source anywhere says WHEN a success function
is worth having (D) — the pack constructs that gate, anchored on arvidkahl's attributed test: CS
matters "when your revenue scales with your customers revenue," plus §1033's conditional. The gap
is not enterprise-vs-solo but CS-team-with-a-book vs builder-with-users (A): the solo reader is
served by ONE 122-line skill ecosystem-wide. GitLab teaches the other half: lift the epistemics,
explicitly decline the machinery (CSMs/QBRs/EBRs don't transfer; expiry dates and tie-breakers do).
Scope-limiter to ship (B): churn is often a PRICING/VALUE signal, not a support-process failure
(patio11's minimum-buy-in economics; robwalling's price-churn link; "10%+ monthly churn = pre-PMF").
**Mechanism correction (B top-up, _raw-x-solo-support.md):** the solo replacement for CS process is
PRICING first, AI tier-1 support second — NOT docs, as the charter hypothesized. **CONTESTED-mark
the pricing plank (B §13.3):** "pricing beats support-quality as a churn lever" is one-sided —
no opposing practitioner voice was found, which is not the same as the contest being settled.
Ship it as a strong practitioner position with the absence noted, not as a resolved fact. Across 5 deep-mined
solo operators the enterprise vocabulary (QBR/CSM/health score) is never used — not attacked,
absent. And canon OUTCOMES survive while canon PROCESS is discarded (Shpigford celebrates net
negative churn as the "holy grail"). Teach the outcome vocabulary, replace the process. Honest
gaps for build-time: docs-as-deflection, cancellation/win-back tactics, and onboarding-call
execution are under-evidenced from practitioners — the pack's guidance there leans on C's code
evidence and D's method verdicts, labeled accordingly.

**P3 — AI-support policy (wedge 3, confirmed three ways).** The policy layer is success's; ai owns
mechanics/evaluation (controller ruling, recorded; Decagon's president independently asserts it:
"the model isn't the moat, the guardrails are"). Content: the 9-pattern escalation corpus (C) —
zero confidence-float triggers anywhere; consent-first handoff; Anthropic's typed-field-per-turn as
the auditable exemplar (PRECISION GUARD: user_mood is recorded, never a trigger). Resolution-rate
honesty: "resolution rate" is a measurement failure — no source defines it audibly (B); Fin's own
"assumed resolution" counts silent exit (D); τ-bench pass^k is the one measured instrument
(gpt-4o <50%, pass^8 <25% retail) vs vendor 70–90% claims. Deflection: unmeasured even at GitLab
(wishlist KPI); teach zero-result + zero-click queries instead of a deflection rate (D, Algolia
primitives — observable, no counterfactual, ranked backlog). KB-rewrite-beats-model-upgrade
(B, nikolak47: 20–25%→85% via KB + process redesign). Klarna: NEVER tell the reversal story —
triple-refuted; the lesson is tier design.

**P4 — Integration with honest seams (wedge 4).** Every existing artifact covers a disjoint slice;
success unifies onboarding-program + support + health + renewal WITH the family's binding seams
(§4). Support-process primitives from primary sources (C): the 3 canonical status buckets (to-do /
paused-on-someone-else / finished — schema-enforced in 2 systems, convergent across 30 years),
first_response/next_response/resolution SLA metric naming, the "internal / this-isn't-support"
taxonomy bucket, escalation's two meanings (SLA-breach-notify vs priority-bump), GLPI's
matrix-only-if-ITSM lesson. Plus the two grep-verified family orphans (E): the help-content slot
(nobody defines what good help content IS) and the customer-facing response-time promise (operate
owns internal SLOs; nobody owns when a human replies).

## 3. Falsification results → never-ship strip (all six failed as circulated, D)

| Claim | Verdict | Ship rule |
|---|---|---|
| "5% retention → 25–95% profit" | Splice; appears in NO primary | Never ship; teach the trace |
| "5–25× cheaper to retain" | Folklore, chain fully traced; Ipsos debunk | Never ship |
| NPS "best predictor of growth" | Failed replication (Keiningham 2007; ACSI beat it 2/3) | Never ship; cite the replication |
| "96% of unhappy don't complain" | Worst-case TARP slice sold as universal (~5–75% by stake) | Never ship the 96% |
| "80/20 revenue rule" | ~60/20 on FMCG panel; not B2B-transferable | Never ship 80/20 |
| Deflection cost ratios ("$1 vs $6") | No primary exists; HDI spread is 9× | Never ship any single figure |
| CES superiority | Unlabelled bar chart; outcome is intention; falsified on retention | Never ship |
| "76%" (Salesforce/Fin deal thesis) | "examples of…" = selected cases wearing an average's clothes | Never ship — it WILL spread |
| "$2M ARR per CSM" | Debunked by lincolnmurphy at the conference it circulated at; restated by @saastr anyway | Never ship; use as propagation exhibit |
| Vendor deflection/resolution rates (80%, 83%, …) | All self-reported, zero independent verification | Vendor-claim grade only, always labeled |
| **NEW CLASS: unsourced SLA defaults** ("First Response 1 hour (P0)") | A template number becomes a promise made to someone else | Never ship an SLA default without "set from your own capacity" framing |
| Health-score accuracy claims (50–60%/70–85%, "15–30% churn reduction") | Zero disclosure anywhere; fabricated-citation example live (pulserevops) | "Not published," never "not measured" |
| Shpigford "reduce churn by 68%" teaser | Bare % without method — from the corpus's own best-graded source | Never ship; the figure-CLASS rule catches even our anchor author |

Standing rules: the never-ship LIST is not the RULE (flag figure-CLASS); a disclaimed figure is
still a figure; verify the SUBJECT of a metric from its local context (A's KBCM lesson).

## 4. Seam adjudications (controller rulings — writers implement verbatim)

E's seam table (webdesign-lift-report.md §3) is the authoritative two-way inventory. Rulings on the
open questions:

1. **Onboarding (vs design — the sharpest contested seam):** design owns the in-product onboarding
   FLOW ("orient, don't educate": patterns, wizards, empty states, copy, aha-moment metrics);
   success owns the onboarding PROGRAM — implementation/adoption plan, education artifacts outside
   the product (docs, KB, guides, enablement), adoption over time. Success's SKILL.md states this
   explicitly or it reads as a land-grab. Product hands success onboarding acceptance criteria in
   the PRD (time-to-first-value) — success consumes them.
2. **Renewal/expansion (vs product and unbuilt sales):** product owns the commercial lifecycle as
   MODELING (pricing tiers, metric trees, expansion levers); success owns the renewal WORKFLOW and
   expansion/advocacy MOTIONS. In sales-assisted motions the expansion SALE (negotiation, closing)
   is sales's — provisional, flagged; lincolnmurphy's CS-native complexity-gated position is
   recorded as contested vocabulary (B), cite don't adjudicate the industry fight.
3. **VoC/NPS:** design owns NPS definition + survey method; product owns NPS/CSAT as metric-tree
   entries; growth owns "NPS never stands alone as a primary metric." Success consumes all three
   and adds ONLY interpretation (what a score can honestly support — de Haan/Keiningham tier) +
   aggregate VoC trend analysis, which is genuinely unclaimed (A). Formbricks Display-vs-Response
   schema = the self-selection exhibit.
4. **Involuntary churn:** marketing's shipped asset assigns dunning/billing-failure recovery to
   PRODUCT (email-compliance-checklist.md:82). Ruling: honor it. Success requires churn numbers to
   SEPARATE voluntary from involuntary and owns the relationship-side saves; dunning mechanics stay
   product's. Cite the checklist line.
5. **Advocacy:** success qualifies the advocate and secures consent; marketing produces and
   publishes the asset. (E Q1, adopted.)
6. **Community retention:** the marketing fork (organic-social:17–18) resolves to: success owns
   community-as-retention PROGRAM; growth owns any retention experiment run in it. Success's
   handoff states it is closing a previously open route.
7. **Incident/decommission comms:** co-owned product/success ALWAYS (operate says so in 3 files);
   success never claims sole ownership. Operate states fact, impact, and timing; success manages
   the relationship. Customer-facing response-time PROMISES are success's; internal SLOs operate's.
8. **AI-support:** ai owns the support-assistant surface mechanics + evaluation (τ-bench side, RAG);
   success owns policy artifacts: guidelines (condition→action), exclusion edges, bot boundaries,
   strict-vs-fluid composition, escalation policy, deflection honesty. Cite parlant (Apache-2.0)
   as implementation, claude-quickstarts (renamed! cite new name) as the typed-escalation exemplar.
9. **Retention execution:** growth reserved the literal job name `retention-execution` for success
   (growth/handoff.md:66–67). Use that name in the job table. Growth's binary standing-vs-experiment
   classification rule (retention-and-resurrection.md:168–169) gets its third box drawn from
   success's side: standing=operate, experiment-bound=growth, validated-motion-as-relationship=success.
10. **Escalation vocabulary:** always "customer escalation" — the bare word is four-way loaded
    (operate/automation/ai/quality).
11. **Support-ticket PII:** success inherits data's governance constraint (free-text PII) — cite it.
12. **Automation:** refund-approval flagship is a support workflow end-to-end — success owns the
    support process + refund policy, automation owns the gate. State the seam; it's real and
    unstated on disk.

**Sibling PRs queued for release (do NOT edit now):** operate handoff.md:79 (add success to the
customer-facing decommission row — prose and contract disagree); automation process-capture.md:16
(stale "three upstreams" count). Both one-liners.

## 5. Shape recommendation (build phase finalizes)

- **Jobs (~11):** when-success-applies (the existence gate, front door) · onboarding-and-adoption
  (program, not flow) · education-and-knowledge-base (incl. the help-content orphan; cite design's
  IA for structure; article lifecycle/staleness; zero-result/zero-click backlog) ·
  support-process-design (taxonomy w/ tie-breakers + internal bucket, 3 status buckets, SLAs as
  promises + response-time commitments at point of action, customer escalation) ·
  ai-support-policy (P3 — likely co-flagship-grade distinctiveness) · health-and-risk-signals ⭐
  FLAGSHIP (P1) · voice-of-customer (interpretation + aggregate trends) · retention-execution
  (growth's reserved name; churn-save/win-back as sent; pricing-signal scope-limiter) ·
  renewals-and-expansion (workflow + signals; NRR honesty: 4 SEC-verbatim definitions, never
  compare across) · incident-and-account-comms (co-owned, thin) · advocacy-and-references (thin) ·
  handoff. Merge candidates if >11: advocacy into renewals-and-expansion; incident comms into
  support-process.
- **Surfaces:** selfserve-solo DEFAULT (the §1033 honesty is the front door) · b2b-high-touch
  (the canon's home turf, epistemics-not-machinery) · b2b-sales-assisted (renewal/expansion split
  with sales) · agentic/AI-support ADDITIVE. Mobile-subscription: fold app-review-response +
  uninstall into selfserve or a thin overlay — build decides.
- **Named concepts (candidates):** the Existence Gate · "not published, never not measured" ·
  the Observability Question (is your churn event observable?) · score-vs-prediction (different
  artifacts) · "a category list without tie-breakers is not a taxonomy" · the response-time promise.
- **Runnable-asset candidates (growth precedent):** NRR/GRR calculator with the 4 SEC definitions
  as selectable modes + self-test (pypulate MIT as reference impl); churn-baseline honesty check
  (base rate vs headline accuracy); SLA-capacity sanity calculator (solo: what response time can
  one person actually promise across time zones — B top-up feeds this); health-score audit
  checklist (expiry dates? outcome joined? override rules? missing-data convention?).
- **Evidence-grade labeling** (marketing precedent): measured-with-method > practitioner-report >
  vendor-claim, labeled inline throughout.

## 6. Licensing ledger (5-clause rule held; additions)

LIFTABLE (file-verified): parlant (Apache-2.0, LICENSE+pyproject agree) · claude-quickstarts (MIT;
cite RENAMED name — redirects make stale citations pass review) · τ-bench/τ²-bench (MIT) ·
agent-desk (Apache-2.0) · dynatrace-oss/CustomerSuccess (Apache-2.0) · pypulate (MIT) · lifelines
et al. (permissive, per C's table) · trudesk (Apache-2.0 despite API NOASSERTION) · anthropics
knowledge-work-plugins (Apache-2.0). CITE-ONLY: GitLab handbook prose (root license scoped to "the
GitLab Software") · t0ddc3by (Apache-2.0 wrapping SuccessCOACHING IP — clearest
thin-license-on-thick-IP yet) · ncklrs (no LICENSE) · deanpeters (CC BY-NC-SA; API said
NOASSERTION) · scikit-survival (GPL-3) · chaskiq (AGPL+Commons-Clause) · all AGPL support stacks
(structure/idea citation only) · Buffer health-score script (no license). AMBIGUOUS re-check
before any lift: uvdesk, HELPDESK.AI (API-only checks). **6th-clause candidates ADOPTED for this
build:** (f) a dangling LICENSE-file pointer is not a license; (g) registry mirrors are never a
licensing shortcut — resolve upstream. API-lied tally this run: ≥13.

## 7. Method notes for the build phase (family memory candidates)

xrelay: `search "from:X …"` SILENTLY ignores from: — use the typed --from flag; ALWAYS project
`id` (a reconstructed permalink is a fabricated citation that survives review); jasonlk-class
archives time out per-account (targeted searches instead). sec.gov 403s yield to a Chrome UA;
pure.rug.nl serves what research.rug.nl blocks; law-firm mirrors beat CanLII's DataDome; GitLab
handbook has a no-auth public REST API. Worker-completion notifications route to the controller,
not the lead — forward pointers. Verify the SUBJECT of a flagged metric from local context.

## 8. Open corpus items (build-phase pickup, not blockers)

**Late-arriving raw (post-B-close, controller-linked): `_raw/_raw-x-solo-topup.md`** —
levelsio/dvassallo/tylertringas territory closed: pause-subscription arc (2015 idea→2017 ship),
the honestly-hedged churn-causality tweet (19%→10% "I guess" — a MODEL for stating unmeasured
causal claims), custom cancel-flow 40%→13-14% flagged CONFOUNDED, "last part of support I can't
automate" (billing-confusion→chargeback), dvassallo "$1M revenue, all support from personal
email" (clearest tool-adoption threshold found), LIFO support tactic, PayPal ~10× support load
vs Stripe, refund rate 3.96%/0% disputes. Honest nulls: no absolute ticket volumes, no
timezone/on-call statements, no first-hire numbers. Contested ×3 (cancellation friction
dark-pattern-vs-winback; does churn matter solo — levelsio holds both positions; subscription-first
vs structural non-recurring). New xrelay gotcha: --from also silently drops on OR-group queries —
one single-term query per keyword. Writers: treat this raw as part of B's corpus.

Complex Systems podcast (patio11 × destraynor, Jan 2026) — best non-X artifact, unread ·
"76%" method behind the Salesforce/Fin thesis · Klarna Feb-2025 "~700 agents" piece · hnshah's
NPS-critique source doc · GitLab's other two scores (maturity-scoring.md, platform-value-score.md,
13 unread files listed at C §7c) · Reichheld 1990 paid reprint (verdict wouldn't change) · TARP
original (NTIS-era print) · B top-up addendum (folds in on arrival).
