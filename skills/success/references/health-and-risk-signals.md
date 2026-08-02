# Health and risk signals

Purpose: What a health score or churn model can honestly predict, why a correct prediction may
not help, and whether the churn event is observable at all. The pack's flagship.

Read when: building, buying, or interpreting a health score, churn model, or renewal-risk signal;
prioritizing accounts; auditing a score (pair with `assets/health_score_audit.md`).

Skip when: the workflow after a red score (→ `retention-execution.md`); renewal/expansion (→
`renewals-and-expansion.md`); NPS/CSAT/CES construct or method (→ `voice-of-customer.md`).

Inputs: the model's inputs/weights and any validation; the reader's contractual shape —
subscription-with-renewal-date vs. usage-based/no cancellation event.

Produces: a verdict on whether a score/prediction claim is honestly supportable, the gap-and-action
pairing a score needs to be usable, and — on request — a completed `assets/health_score_audit.md`.

## Contents
1. Score-vs-prediction · 2. "Not published, never not measured" · 3. The Observability Question ·
4. Four-study convergence · 5. Honest ceilings · 6. The reframe · 7. Liftable epistemics

---

## 1. Score-vs-prediction: two different artifacts

GitLab — the most transparent enterprise CS org publicly readable — does not ask its health score
to predict churn. The health score (P.R.O.V.E. — five weighted measure groups; full weights,
banding, and failure modes in `surface-b2b-high-touch.md` §2) is one artifact; churn/expansion
*prediction* is delegated to two separate,
internal-only models, **Propensity to Expand (PTE)** and **Propensity to Churn or Contract
(PTC)**, whose method and accuracy are not public. GitLab's own section opens by disclaiming
itself: *"Predictive Analytics is not a silver bullet... this methodology is probabilistic."*
**Score-vs-prediction are different artifacts** even at the org that invested most visibly in
both. Collapsing "health score" and "churn prediction" into one number is something the most
instrumented public example does not do.

## 2. "Not published, never not measured"

No source discloses a health-score or churn-model accuracy figure against real outcomes, at three
hard-to-dismiss levels: **five CS vendors** (Gainsight, ChurnZero, Totango, Vitally, Catalyst)
publish zero AUC/precision/recall/backtest — what circulates instead is exactly the shape a reader
must recognise and correct on sight: pulserevops.com/knowledge/q525 asserts "62% precision, 58%
recall" for a baseline SaaS health score, and its own "Sources" section cites NIH, CDC, WHO, and
JAMA — medical-domain references with nothing to do with a SaaS score. The digits are fabricated-
citation bait, not a measurement; the tell is the source list, not the number itself. The
**open-source corpus**, where every dedicated "health score" repo tops out at 0–1
stars, grep-verified, and its two most substantive artifacts (a Buffer usage-decline script, an
Odoo RFM module) act on a score but never check it against a later outcome; and **GitLab itself**
— an in-house data-science team with drift-detection tooling whose stated evaluation standard is
still qualitative prose: *"Performance is generally measured by how accurate, powerful, and
explainable the model is."* Zero hits for AUC/precision/recall/backtest. Backtesting the score is
a success **criterion** in the handbook, not a result.

**"Not published, never not measured."** Absence of disclosure isn't proof of inaccuracy — say so
every time. But a reader cannot verify any of these scores, and a 1-to-5 star rating with no
stated calibration cannot be audited by the person relying on it.

## 3. The Observability Question

Before scoring anything: **is your churn event even observable?** The BTYD literature — Fader,
Hardie & Lee, *"Counting Your Customers" the Easy Way* (Marketing Science 24(2), 2005), on
Schmittlein, Morrison & Colombo (1987) — draws a distinction the CS canon never makes. In a
**contractual** setting (subscription, renewal date) churn is observed on a known day; in a
**non-contractual** one (usage-based, self-serve) it's unobserved: *"The point at which a customer
becomes inactive is unobserved by the firm... There is no way for an outside observer to know for
sure."* GitLab's PROVE model, like the whole apparatus, is built for the contractual case and
applied to both; a self-serve reader is most likely handed the wrong instrument.

The same authors reject the composite score's *form*, not just its calibration: it predicts only
the next period, needs two periods of data to train, and "ignore[s] the fact that the observed RFM
variables are only imperfect indicators of underlying behavioral traits." Their recommendation —
stochastic (survival/latent-state) models over scoring models — is a direction, not an import: the
authors flag subscriptions as outside their own studied scope. **Ship the distinction; do not ship
BG/NBD as validated for subscriptions.**

## 4. Four-study academic convergence

| Study | Method / n / scope | Finding |
|---|---|---|
| Ascarza 2018, *JMR* 55(1) | 2 randomized field experiments, telecom (4M+ subs) + US membership org | Highest-risk decile improved *least* (95.3%→93.7%); a lower-risk group improved more (71.2%→68.3%); one segment worsened (9.1%→11.9%). Risk-ranking ≠ response-ranking; targeting by risk alone can backfire |
| de Haan et al. 2015, *IJRM* 32(2) | Correlational, 93 Dutch service firms across 18 industries, n=1,375, vs. actual 2-yr retention | Best predictor: tenure r=.199; NPS r=.170; CES r=−.073 (right direction, weak). Ceiling ≈4% of variance |
| van Doorn et al. 2013, *IJRM* 30(3) | Replication Corner, n=11,967, 46 firms (bank/insurance/utility/telecom), vs. financials | Abstract: "equally poor for predicting *future* sales growth and gross margins." Discussion, separately: "there is no single best metric." |
| Fader, Hardie & Lee 2005 (BG/NBD) | Formal probability model, published likelihood, holdout-validated | Contractual/non-contractual split (§3); scoring models rejected for stochastic ones; not validated for subscriptions |

Grade: measured-with-method throughout. **Tenure beats sentiment** — the cheapest variable a
builder already has out-predicts every survey program; **extremes beat averages** — top-2-box
(.184) beat full-scale satisfaction (.151); **feedback metrics are contemporaneous, not
forecasts**. "Measure X and you'll know who will churn" is unsupportable at these sizes. Related:
Verbeke et al. 2012 (*EJOR* 218(1)) — AUC/lift can select a *different* "best" model than profit
does; a statistically better churn model isn't automatically a better business tool.

## 5. Honest ceilings: what the ML actually achieves

On the canonical churn dataset (IBM Telco, 7,043 rows, ~26.5% churn; a second set, 3,333 rows,
14.49% churn, recurs too), three independent, non-leaky implementations converge: **accuracy
≈78–81%, churn-F1 ≈0.60–0.62, recall ≈50–66%, AUC ≈0.83–0.85.** Two mechanisms inflate this to the
93–94% headlines that circulate instead. **Resampling before the split**: a 158-star,
tutorial-linked repo applies SMOTEENN to the full dataset *before* `train_test_split`, reports
93.4% accuracy, never flagging the test set is off the real base rate. **Base-rate theater**:
`ReverendBayes/Telecom-Churn-Predictor` (MIT) headlines "94.60% Accuracy... 0.7423 Recall"; its own
CSV (483 true/2,850 false of 3,333) gives a majority-class baseline of **85.51%** — "nobody
churns" already scores that, so the number that matters (it misses 25.8% of churners) runs fourth,
not first. `assets/churn_baseline_check.py` runs this exact check.

**Censoring compounds both.** 73.5% of Telco hasn't churned *yet* (right-censored); treating that
as "will not churn" underestimates propensity for recent cohorts. Survival models "typically have
a concordance index between 0.55 and 0.75" (lifelines) — a same-dataset Cox fit reporting 0.93 is a
red flag, traced to a duration-leaking covariate (`TotalCharges` ≈ `tenure × MonthlyCharges`);
done correctly (IPCW, censoring-adjusted) on a comparable set: 0.7515, inside the honest range.
`assets/churn_baseline_check.py` flags any concordance outside 0.55–0.75 as a leakage signal.

**Never-ship note, this file's own domain**: a bare percentage with no method is unusable
regardless of source — including this pack's own best-graded anchor (§6).

## 6. The reframe: score plus mandatory gap/action

§1 and §5 point to one teaching: **a health score, alone, next to a renewal date, is folklore.** A
score paired with a stated gap (which input is stale, which measure is off, why it's red) and a
mandatory next action is a **prioritization device** — GitLab's own distinction, scoring and
prediction kept as separate artifacts. Never ship a bare number as a decision.

The clearest primary-source exhibit of both halves is `dynatrace-oss/CustomerSuccess` (Apache-2.0,
LIFTABLE) — a vendor CS team's *published arithmetic*, not a blog claim. Its Maturity Score sums
four equally-weighted 25-point components on hand-picked round thresholds (10 users, 5 apps, …),
each component something the vendor wants more of, with **no outcome variable joined anywhere** —
an unvalidated risk predictor and a perfectly reasonable enablement prompt, in the same 100-point
frame that invites the first reading. What redeems it is its *paired* tile: every score ships with
the specific gap and the specific action ("Need N more users — invite & run enablement sessions").
Grade: measured-with-method as to what the code does; no accuracy claim exists to grade.

Anchor anecdote: Josh Pigford (@Shpigford), founder of Baremetrics — a company whose product *was*
subscription churn analytics, sold for $4M —
[x.com/Shpigford/status/874287345041846281](https://x.com/Shpigford/status/874287345041846281)
(Jun 12 2017), verbatim: *"What did we do to cause our churn to get cut in half? ¯\\\_(ツ)_/¯"* The
founder of a churn-measurement company, running his own best-in-class tooling on his own funnel,
could not attribute a 2× churn improvement — against every incentive to claim credit. If causality
resists attribution there, it resists it for the reader too; that's the honest baseline, not a
failure state. (The same account separately shipped a bare-percentage churn-reduction teaser with
no visible method,
[x.com/Shpigford/status/698193606583173121](https://x.com/Shpigford/status/698193606583173121),
Feb 12 2016 — never quote its number; the figure-class rule catches this pack's own best anchor
too, and naming the figure in order to refuse it would ship it anyway.)

## 7. Liftable epistemics (attributed)

None of GitLab's CS *machinery* (Gainsight, CSMs, EBRs, a VP of CS in the escalation ladder)
transfers to a solo/lean reader. What transfers, at no cost:

- **Input expiry, and segmented thresholds.** Usage data → `NA` after 60 days; CSM Sentiment stale
  at 90, forced `NA` at 120; support measures stale after 30 — *"we prefer to show nothing ('NA')
  over outdated data."* Showing nothing beats stale. Bands also differ by service tier; several
  measures are marked "N/A for Scale and Tech Touch" — meaningless measures are switched off, not
  scored badly.
- **Ignorance is a finding, not a gap.** The scorecard treats missing data as `NULL` →
  redistributed → neutral; the human triage rubric treats it as *risk* ("lack of information
  leading to uncertainty"). Take the human side. A quarter of the score (CSM Sentiment) overrides
  the weighted arithmetic once red, and for a customer's first 30 days the score *is* the CSM's
  opinion, because every other measure is null.
- **Unbuilt components, and non-monotone support volume.** GitLab's own model lists several
  measures "Not started" — two of the VoC group's (5%) three measures are unbuilt, so "VoC" reduces
  to ticket counts in practice; check a vendor's maturity column, not its architecture diagram.
  Ticket count scores as negative in the automated bands, but GitLab is inverting that — the human
  rubric already flags *silence* after being told to contact support as yellow, not just volume.
  Support contact and health aren't a straight line.
- **Reason taxonomies need tie-breakers.** GitLab's risk-reason categories (lack of adoption,
  product gap, loss of budget, corporate decision...) each carry a disambiguation rule against
  their nearest neighbor — **a category list without tie-breakers is not a taxonomy.** Full
  taxonomy detail is `support-process-design.md`'s; this file only flags the rule for a risk
  categorization built into a score.

## Validation

- Every figure carries its method or "method unknown," never a bare percentage.
- A "predicts churn" claim is checked against §1 (is prediction a separate, validated artifact?)
  and the Observability Question (§3) is answered before a score goes to a non-contractual reader.
- Any concordance/AUC/accuracy is sanity-checked against §5, not taken at face value.
- Output pairs the score with a stated gap and required action (§6), never a bare number.

## Failure modes and handoff

- **Wants a single trustworthy accuracy number** — none exists; give §5's ceiling and §6's
  reframe; route to `assets/health_score_audit.md`.
- **"What do we do about a red account"** — → `retention-execution.md` (uplift, not raw risk,
  Ascarza §4). **Renewal timing/forecasting** — → `renewals-and-expansion.md`.
- **Usage-based, no cancellation event** — §3 applies before anything else; don't hand over a
  contractual-shaped scoring template.
