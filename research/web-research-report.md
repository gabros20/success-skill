# Channel D · web-research — report

Lead: channel D (opus) · Date: 2026-08-02 · Charter: [`charter.md`](charter.md)
Workers: 3 × sonnet. Lead slices done in-session alongside.

## Source files (every claim in this report traces to one of these)

| File | Owner | Contents |
|---|---|---|
| [`_raw/_raw-web-canon-commercial.md`](_raw/_raw-web-canon-commercial.md) | worker 1 | CS canon (Gainsight book, Lincoln Murphy, CSM ratios, QBR, onboarding) + commercial mechanics (4 primary SEC filings on NRR, renewals, expansion, VoC) |
| [`_raw/_raw-web-falsification-churn-evidence.md`](_raw/_raw-web-falsification-churn-evidence.md) | worker 2 | The six falsification strips traced to primaries + health-score/churn-prediction evidence (Ascarza, Verbeke, Keiningham, Grisaffe, Bain, Ipsos) |
| [`_raw/_raw-web-supportops-ai-agents.md`](_raw/_raw-web-supportops-ai-agents.md) | worker 3 | Support-ops craft (taxonomies, SLA, QA rubrics, Erlang, deflection, incident comms, KB) + AI support agents (Klarna timeline, vendor resolution claims, escalation, τ-bench, Air Canada ruling) |
| [`_raw/_raw-web-lead-cfm-evidence.md`](_raw/_raw-web-lead-cfm-evidence.md) | lead (round 1) | CES primary + its peer-reviewed replication (de Haan 2015, van Doorn 2013), the provenance of the CX-statistics canon, customer education, VoC method, feedback loops |
| [`_raw/_raw-web-lead-btyd-followups.md`](_raw/_raw-web-lead-btyd-followups.md) | lead (round 2) | **The BTYD / latent-churn literature (Fader-Hardie)**, Brier 1950, and dispositions on every controller cross-flag (Reichheld closure, Klarna correction, Salesforce/Fin, KBCM, the new SLA never-ship class) |

Downloaded primary artifacts: `/tmp/d2/` (worker 2, 7 PDFs read), `/tmp/dlead/` (lead, 3 PDFs read),
`research/_raw/_scratch-web/` (worker 3's fetched pages, moved out of the research root by the lead —
nothing deleted, per hard rule 1).

---

## VERDICT FIRST

**The falsification strips did not survive contact with their primaries.** Of the six charter strips,
**zero are GROUNDED as commonly stated.** Two are outright folklore with no traceable original
("5–25× cheaper to retain", the "$1 vs $6" deflection ratio); three are real findings that have been
misquoted into universal laws they never claimed to be (Reichheld/Sasser, TARP's "96%", Pareto 80/20);
one — NPS as "best predictor of growth" — was tested by independent academics and **failed replication**.

**The strongest evidence we found is not on the canon's side.** Three peer-reviewed, method-bearing
studies converge on a single uncomfortable conclusion, and they were produced independently across three
decades and three countries:

1. **Ascarza 2018 (JMR, two randomized field experiments, 4M+ subscribers)** — the customers at highest
   churn risk are *not* the best targets for retention effort, and intervening on some segments
   **increased** churn by 2.8 percentage points. This directly falsifies the entire vendor health-score
   playbook of "work the reddest accounts."
2. **de Haan, Verhoef & Wiesel 2015 (IJRM, actual two-year retention, 93 firms)** — **relationship
   length (r = .199) out-predicted every customer-feedback metric**, including top-2-box satisfaction
   (.184), NPS (.170), and CES (−.073). The best predictor of whether a customer stays is how long they
   have already stayed.
3. **Keiningham et al. 2007 (Journal of Marketing, 21 firms, 15,500+ interviews)** — could not replicate
   NPS's claimed superiority; in two of three of Reichheld's own exemplar cases, the older ACSI metric
   had the **higher** R².

**A fourth study, found in round 2, goes deeper than all three.** The **BTYD literature**
(Fader/Hardie/Lee 2005, building on Schmittlein/Morrison/Colombo 1987) makes a distinction the CS canon
never makes — **contractual vs non-contractual** relationships — and states plainly that in the
non-contractual case *"the point at which a customer becomes inactive is unobserved by the firm… a long
hiatus does not necessarily mean that the customer has actually become inactive. **There is no way for an
outside observer to know for sure.**"* Our default reader (solo, self-serve, usage-based) is often in
exactly that world, where **there is no churn event to observe at all**. The same authors reject the
scoring-model form outright: *"we hope that future researchers will continue to use **stochastic models
(instead of scoring models)**."* That is a deeper critique than "health scores are unvalidated" — it says
the *form* is wrong for the question. **New wedge candidate, and nothing in channels A or C found anyone
asking it: which of the two worlds are you in, and does your churn question even have an observable
answer?**

**The wedge these point at is real and it is bigger than "health scores are unvalidated."** It is that
the CS field's central causal claim — *identify at-risk customers, intervene, save revenue* — has been
tested and the middle step does not reliably work. Charter wedge hypothesis 2 is **confirmed and should
be strengthened**: the flagship is not "what a health score can honestly predict" but "**what a health
score can honestly predict, and why predicting correctly still may not help you.**"

**Two further confirmations.** Wedge hypothesis 1 (the canon is enterprise-CSM-team literature) is
confirmed with an unexpectedly sharp instrument: worker 1's "assumes-a-team?" tagging found that **5 of
Gainsight's 10 Laws and 100% of the CSM-ratio literature presuppose headcount a solo builder does not
have**, and the lead found **no source anywhere that establishes when a success function is worth having
at all** — the canon assumes the function exists and only asks how to staff it. Wedge hypothesis 3
(AI-support era under-canonized) is confirmed with the best single artifact of the run: **τ-bench** puts
frontier-model success under 50% on exactly this task class while vendors claim 70–90% resolution.

---

## 1 · FALSIFICATION-STRIP VERDICTS

| # | Claim as circulated | Primary source | Method | Verdict | Primary text read? |
|---|---|---|---|---|---|
| 1 | "5% retention increase → 25–95% profit increase" | Reichheld & Sasser, "Zero Defections", *HBR* Sep–Oct 1990, 68(5):105–111 | Bain client-engagement case illustrations + NPV/CLV arithmetic on 4 named firms. **Not an experiment, not a sample.** | **GROUNDED-BUT-MISQUOTED.** The article's own figures are per-industry and discrete — 85% (one bank's branch system), 50% (an insurance brokerage), 30% (an auto-service chain), 125% (MBNA). The "25–95%" range **appears in no primary text**: it is a splice of a separate, later Bain document's "25%" with the article's 85% rounded up. | **NO** for the 1990 article (paywalled on every route tried) · **YES** for the Bain "25%" document |
| 2 | "It costs 5–25× more to acquire than retain" | **None exists.** HBR 2014 (Amy Gallo) is the modern re-launder point and cites nothing | N/A — an uncited hedge: *"Depending on which study you believe…"* | **FOLKLORE / UNTRACEABLE.** Chain traced: untraceable TARP-adjacent 1980s claim → Hart/Heskett/Sasser HBR 1990 restatement → decades of repetition → Gallo 2014. No link in the chain points to a study. Ipsos (*Loyalty Myths*, 2005) debunks it on three economic grounds. | **YES** (Ipsos primary; Gallo sentence quoted directly) |
| 3 | NPS is "the best predictor of growth" | Reichheld, "The One Number You Need to Grow", *HBR* Dec 2003 | Reichheld/Satmetrix hand-picked exemplar-industry scatterplots, ~50 companies, no regression tables, no held-out validation | **FAILED INDEPENDENT REPLICATION.** Keiningham et al. 2007 (*JM*): *"We find no support for the claim that Net Promoter is the 'single most reliable indicator'…"* and ACSI beat NPS on R² in 2 of 3 reconstructed exemplar cases. | **YES** (Keiningham 2007 + Grisaffe 2007 full text) |
| 4 | "96% of unhappy customers don't complain" | TARP / John Goodman for the White House Office of Consumer Affairs, ~1979–1986 | Multi-industry survey of complaint incidence **by problem type and dollar value** | **GROUNDED-BUT-MISQUOTED.** A real TARP finding underlies it, but 96% is the worst-case (small-ticket/packaged-goods) slice presented as universal. TARP's own breakdown ranges **~5–30%** (mistreatment/quality) to **50–75%** (out-of-pocket monetary loss). The "1st Financial Training Services" attribution is a dead end. | **NO** — original report is NTIS/GPO-era, no digital copy found |
| 5 | "80% of revenue from 20% of customers" | Pareto (1896) → Juran (1950s) for the framing; **Sharp & Romaniuk 2007 / Graham et al. 2017** (Kantar panel, ~600 brands, 40 categories, UK, 1998–2014) for the test | Household-panel decomposition of sales by buyer-frequency decile, replicated across categories/years | **FOLKLORE at 80/20; GROUNDED at ~60/20** — light buyers deliver nearly half of sales, and top-20% membership is unstable year to year. **Domain caveat: this evidence is FMCG, not B2B SaaS**, where genuine concentration can legitimately be tighter. | **Partial** — institute-authored synthesis, underlying PDF non-extractable |
| 6 | "$1 self-serve vs $6–12 agent-assisted" / "10× cheaper to deflect" | **None found.** Nearest method-bearing source is MetricNet/HDI cost-per-ticket benchmarking | HDI/MetricNet: total operating cost ÷ ticket volume, paid enrolled panel, **enterprise IT service desk only** | **FOLKLORE / UNTRACEABLE at the dollar figures.** No primary Forrester or Gartner report located for any version. HDI's own 2014 sample spans **$31.98–$288.99 per ticket** — a 9× internal spread that makes any single "cost per ticket" figure meaningless without its density tier. | **NO** for the ratios; HDI numbers are secondary |
| + | "80% of companies believe they deliver superior CX; 8% of customers agree" | Allen, Reichheld, Hamilton & Markey, "Closing the Delivery Gap", **Bain 2005** | Bain diagnostic survey n=362 companies vs Satmetrix NP database n=375 | **GROUNDED** — real disclosed n on both sides. Caveat Bain discloses but doesn't flag: the two n's are **different, unmatched populations**. The one figure in this whole set that survives. | **YES** (full PDF) |

### 1.1 Two new strips the lead added, with primaries read

| Claim | Source | Verdict |
|---|---|---|
| **CES "outperforms NPS and CSAT at predicting loyalty"** | Dixon, Freeman & Toman, *HBR* Jul–Aug 2010 | **UNSUPPORTED AS PUBLISHED.** The entire claim rests on **an unlabelled bar chart** — no R², no coefficients, no intervals, no n per comparison. Outcome is *intention*, not behavior. Research is by CEB, the vendor of the metric. Then **falsified on actual retention** by de Haan et al. 2015. |
| **"Trained/certified customers retain better" (customer education)** | No measured source exists | **FOLKLORE, and structurally unfixable without an experiment.** Every claim compares customers who *opted into* training against those who didn't — the confound is the entire effect. |

### 1.2 The figure-CLASS rulings (the charter's twice-learned rule: flag the class, not the string)

The specific strings above are less useful to the pack than these classes. **Ship the class.**

1. **The single-proprietary-dataset class.** A large share of the "CX statistics" in circulation — "84% of
   customers say expectations weren't exceeded", "20% of satisfied customers intend to leave", "customers
   are 4× more likely to leave a service interaction disloyal than loyal", "23%/48% told 10+ people",
   "22% of repeat calls involve downstream issues" — all trace to **one 2010 CEB survey of intentions**.
   A listicle citing five of them is citing one source five times. Treat any "X% of customers tell N
   people" or "X% of satisfied customers still leave" as this class until traced.
2. **The bare-uplift class.** Any "X% more/better" attached to adopting a practice, with no comparison
   group named. The lead independently tripped over an unattributed **"40%"** twice in one session
   ("trained customers show 40% higher retention"; "structured feedback triage resolves 40% more
   issues"). Never ship a bare uplift percentage.
3. **The benchmark-table class.** Published "CSAT benchmarks by industry" / "average NPS by industry"
   tables aggregate across incompatible sampling frames, response rates, trigger points, and scales, and
   essentially never publish a response rate. Comparing your number to them is not a comparison.
4. **The vendor-accuracy class.** Health-score and resolution-rate accuracy figures (see §3, §5).
5. **Unsourced SLA defaults** *(proposed by channel A, endorsed and generalized here)*. "First Response:
   1 hour (P0)", "4-hour resolution for critical", "24-hour first reply" — template values in docs,
   blog posts and skill packs that readers adopt as **real customer commitments**. This class is worse
   than an ordinary uncited number: an uncited statistic misleads a reader's *belief*; **an uncited SLA
   default becomes a promise made to someone else**, with contractual and reputational consequence, and
   it is adopted precisely by the readers least equipped to staff it. It also compounds worker 3's FRT
   finding — a first-response target is the metric most prone to being gamed by stopping the clock
   without starting work. **Rule form:** never publish a response-time number as a default; publish the
   *method* for deriving one from your own volume, hours and staffing, and require the reader to state
   the hours it applies within. Any example must be visibly labelled an example, never a recommendation.
   This matters more than it looks — channel E found "customer-facing response-time promises" is one of
   only two genuine orphan slots across all 12 shipped packs, so **success will own this**.

---

## 2 · THE CS CANON AND WHAT IT ASSUMES

Full detail: [`_raw-web-canon-commercial.md`](_raw/_raw-web-canon-commercial.md) §§1–5.

**The Gainsight book (Mehta/Steinman/Murphy, Wiley 2016)** is canon-with-interest exactly as the charter
predicted: two of three authors were Gainsight executives. Its **10 Laws carry zero cited evidence** —
every one is an assertion. Worker 1's most useful output is the per-law portability tagging: **Laws 1, 2,
5, 9, 10 presuppose a CS function with headcount, segmentation infrastructure, and a metrics practice.
Only Laws 3, 4, 7, 8** (churn is the natural tendency · customers expect success · product has to be the
priority · obsessively improve time-to-value) **translate to a solo self-serve builder.** That 4-of-10
subset is a shippable artifact.

**Lincoln Murphy** is the closest thing in the canon to an honestly-portable framework, and carries a
correction we must not get wrong: **his own formula changed.** Current, from his own site: Desired
Outcome = **"Goal + Appropriate Experience"**; the classic "Required Outcome + Appropriate Experience"
the charter asked us to check is his **pre-2024 formulation, superseded on his own site**. Citing the old
version would be citing an outdated Murphy. His QBR position is blunt and useful: *"You don't have to do
QBRs. Period."* — reframed as *"Is a QBR part of the Appropriate Experience for your customers?"*

**CSM ratios are 100% assumes-a-team literature**, and the one number with a real method carries a
disqualifying selection bias: Gainsight's own telemetry over **17,034 CSMs** gives median **$1.4M
ARR/CSM** (75th pct $4.2M) — but the sample is *Gainsight's own customer base*, i.e. companies already
large enough to buy a CS platform. Gainsight's more-quoted "1 CSM per $2M ARR" is, in their own words,
*"my guidepost. I've seen nothing that disputes it"* — **VENDOR-FOLKLORE, self-labelled.**

**Time-to-first-value causing retention is folk wisdom, not research.** Worker 1 found no study behind
any of it, only unsourced vendor figures ("activate within 3 days → 90% more likely to continue", "70%
churn within 90 days due to poor onboarding"). If the pack uses TTFV framing it must say *widely
believed, not measured*. Worker 1 also flags a category error worth ruling on: enterprise implementation
(weeks/months against contractual milestones) and self-serve activation (minutes/session) are conflated
under one "TTFV" number throughout the vendor literature.

**The gap that supports the §1033 conditional.** The lead searched specifically for evidence on *when a
distinct success function becomes worth having* versus being absorbed by docs, product, and automation.
**No source addresses it.** The entire literature assumes the function exists and asks only how to staff
it. The pack will have to **construct** the "do you even need this yet" gate, because the canon does not
contain one. That is not a gap to apologize for — it is the pack's opening.

---

## 3 · HEALTH SCORES AND CHURN PREDICTION — the flagship evidence

Full detail: [`_raw-web-falsification-churn-evidence.md`](_raw/_raw-web-falsification-churn-evidence.md) §3
and [`_raw-web-lead-cfm-evidence.md`](_raw/_raw-web-lead-cfm-evidence.md) §2.

**This is where the pack's flagship lives, and the evidence is unusually good.**

**Ascarza 2018, "Retention Futility" (JMR 55(1):80–98)** — the single most important finding of the run.
Two randomized field experiments (a Middle East telecom with 4M+ subscribers; a US membership
organization). Verbatim: *"customers identified as having the highest risk of churning are not
necessarily the best targets for proactive churn programs."* The measured pattern:
- Highest-risk decile: churn 95.3% control → 93.7% treated (**1.6 pp** reduction)
- A *lower*-risk group: 71.2% → 68.3% (**2.9 pp** — a bigger effect than the highest-risk group)
- One segment **got worse**: 9.1% control → 11.9% treated (**+2.8 pp churn**)

The mechanism is uplift vs risk: risk ranks who will leave, uplift ranks who will *respond*. They are
different orderings, and the CS canon has been optimizing the wrong one for a decade.

**Verbeke et al. 2012 (EJOR 218(1):211–229)** adds the second blade: AUC and top-decile lift — the
metrics a health-score vendor would cite if it cited any — **can select a different "best" model than
profit does**. A statistically better churn model is not automatically a better business tool.

**de Haan, Verhoef & Wiesel 2015 (IJRM 32(2):195–206)** supplies the magnitudes, and the lead read the
correlation table directly. Against **actual two-year retention** (n=1375 firm-responses, 93 firms, 18
industries, bivariate-probit self-selection correction, one-third holdout, Gini/lift/hit-rate):

| Predictor | r with retention |
|---|---|
| **Relationship length (tenure)** | **.199** |
| Top-2-box satisfaction | .184 |
| NPS (official) | .170 |
| Satisfaction (full scale) | .151 |
| CES | −.073 |

Three rulings for the pack fall straight out of this table:
- **Tenure beats sentiment.** The cheapest variable a solo builder already has out-predicts every survey
  programme. An honest health score is behavioural and tenure-weighted first, sentiment second.
- **Extremes beat averages.** Top-2-box (.184) beat full-scale satisfaction (.151). Teaching "track your
  average CSAT" teaches the weaker statistic.
- **The ceiling is low.** The best correlation in the entire study is .199 — roughly 4% of variance. Any
  pack sentence of the form "measure X and you'll know who will churn" is unsupportable at these effect
  sizes. **This is the empirical backbone of the health-score-humility flagship.**

**⚠ CORRECTION ON THE RECORD (lead, 2026-08-02).** A widely repeated secondary source (MeasuringU)
describes the CES result as *"a terrible predictor [that] actually had a negative correlation"*. The
value is right; **the framing is wrong and we must not repeat it.** On the 2010 CES scale, 1 = very low
effort and 5 = very high effort, so a *negative* correlation with retention is the **theoretically
correct direction** — high-effort customers churned more. CES pointed the right way, **weakly**. The
authors' own words: *"the CES significantly correlates with retention, but it is considerably lower than
the correlation of the other CFMs."* Worker 2's file cites the de Haan and van Doorn numbers via that
same MeasuringU page; **the lead's file holds the primaries and supersedes it** — the de Haan values
match, but van Doorn's "r≈.46/.22" as relayed by MeasuringU was **not** found in the primary and should
not be shipped.

**van Doorn, Leeflang & Tijs 2013 (IJRM 30(3):314–318)**, obtained by the lead, is a formally designated
IJRM *Replication Corner* study (n=11,967 responses, 46 firms, banking/insurance/utilities/telecom,
against real financials). It also corrects a footnote that de Haan et al. themselves got slightly wrong.
The honest finding: *"all metrics perform equally well in predicting current gross margins and current
sales revenue growth and equally poor for predicting future sales growth… The NPS is neither superior nor
inferior to other metrics."* And: *"there is no single best metric."*

**Therefore the defensible pack claim is not "feedback metrics don't work."** It is: **customer-feedback
metrics are contemporaneous descriptions, not forecasts, and the choice among them is close to
arbitrary.** Sharper, truer, and more useful than the flattened version.

**Against all of this, the vendors publish nothing.** Worker 2 searched Gainsight, ChurnZero, Totango,
Vitally and Catalyst for a single validated accuracy figure — an AUC, a precision/recall pair, a lift, a
holdout backtest tied to a named dataset. **Found none, across all five.** What circulates instead is a
worked example of laundering worth naming in the pack: a health-score "accuracy" page asserting *"62%
precision, 58% recall"* and *"AUC often 0.7–0.9"* whose own Sources section cites **NIH, CDC, WHO and
JAMA** — medical-domain references that have nothing to do with B2B SaaS health scores.

### 3.1 The BTYD literature — the form of the instrument, not just its accuracy

Full detail: [`_raw-web-lead-btyd-followups.md`](_raw/_raw-web-lead-btyd-followups.md) §1. Sources are
free from the author's own site (brucehardie.com): Fader, Hardie & Lee, **"'Counting Your Customers' the
Easy Way"** (*Marketing Science* 24(2), 2005) and **"RFM and CLV: Using Iso-Value Curves"** (*JMR* 42(4),
2005), both building on Schmittlein, Morrison & Colombo (1987).

**The contractual / non-contractual split is the concept to ship.** In a *contractual* business
(subscription with a renewal date) churn is an observed event on a known day. In a *non-contractual* one
(usage-based, self-serve, no cancellation moment) churn is **latent** — verbatim: *"the time at which
customers become 'inactive' is unobserved."* The CS canon's health-score apparatus is built entirely for
the contractual case and applied indiscriminately to both. Given the §1033 conditional puts a solo
self-serve builder at the centre of this pack, **that is the reader most likely to be handed the wrong
instrument.**

**And the authors reject the instrument's form, not just its calibration.** Their stated objections to
"scoring models (i.e., regression-type models)" — verbatim — are that such models predict only the next
period, require two periods of data (one spent manufacturing a dependent variable), and *"ignore the fact
that the observed RFM variables are only imperfect indicators of underlying behavioral traits."* Their
closing recommendation is explicit: *"stochastic models (instead of scoring models)."* A vendor health
score is exactly a scoring model over recency/frequency-style inputs.

**Scope discipline required.** The authors themselves flag the limit: *"the context here —
noncontractual purchasing — is a limitation… It is not immediately clear how the model components used
here need to be changed to accommodate these other contexts [subscriptions]."* **Ship the distinction;
do not ship BG/NBD as validated for subscription businesses.** Also worth noting for a solo reader:
the BG/NBD paper's own pitch is that *"its parameters can be obtained quite easily in Microsoft Excel"* —
rigour here is not gated behind a CS platform.

**Brier (1950)** — obtained and read (*Monthly Weather Review* 78(1), free from AMS). The oldest paper in
our corpus already names the Goodhart problem for probabilistic scoring: his stated concern is that
*"the verification scheme should influence"* the forecaster, who may end up optimizing *"on the
verification score"* rather than the phenomenon. That is the health-score failure mode exactly — once a
CSM is measured on moving the score, the score stops measuring the customer.

**And the null result now holds at the top of the market, not just among vendors.** Channel C flagged
GitLab's **Propensity-to-Churn (PTC) / Propensity-to-Expand (PTE)** models as the best remaining candidate
for a disclosed enterprise accuracy figure. They are real and publicly described — built by an in-house
Data Science team from Salesforce, Zuora, Bizible and product-usage data, predicting churn/contraction in
the next 3 months, output as a **1-to-5 star rating on the SFDC account record**. **No accuracy figure is
published anywhere reachable**: no AUC, precision/recall, lift, holdout, or base-rate comparison — stars,
not calibrated probabilities.

A second round on GitLab's separately-public **enterprise data-science handbook** (fetched directly)
returns **zero hits for `AUC`, `precision`, `recall`, `validat*`, `backtest`, `lift`, `F1`, `holdout`** —
and does not name PTC or PTE at all. Its entire public evaluation standard is qualitative prose:
*"Performance is generally measured by how **accurate, powerful, and explainable** the model is."*
Meanwhile the tooling section documents *"Monte Carlo for drift detection"* and *"Tableau Server for
model monitoring and on-going performance evaluation."* **The capability is in place; the disclosure is
not.** Routes exhausted (CS handbook, enablement issues, sales playbook, data-science handbook, blog,
talks) — marked **unfound-not-absent**.

That makes three independent probes with the same result — worker 2's five CS vendors, channel C's repo
sweep, and now a public company with a dedicated data-science team and one of the most transparent
handbooks in the industry. **Nobody publishes churn-model accuracy, even when they have the team and the
data to compute it.** *Honest limit: absence of public disclosure is not proof of inaccuracy. The pack must
say "not published," never "not measured" — but it can say plainly that **a reader cannot verify any of
these scores**, and a 1–5 star rating with no stated calibration cannot be audited by the person relying
on it.*

**Survival vs snapshot** (worker 2 §3.4): a snapshot score is a fixed-window binary classifier that
discards *when* churn happens and mis-handles customers still active at the cutoff (right-censoring);
survival models handle censoring and time-varying covariates natively. Given that **tenure is the single
strongest predictor** in the de Haan table, a scoring method that mis-prices tenure is mis-pricing the
best variable it has.

---

## 4 · SUPPORT OPERATIONS — where the craft is real and where it is theatre

Full detail: [`_raw-web-supportops-ai-agents.md`](_raw/_raw-web-supportops-ai-agents.md) §§1.1–1.7.

**QA rubrics: a measured absence, and a second flagship candidate.** The Klaus/Zendesk **IQS** formula is
genuinely specified (*"add all ratings and divide by the maximum score multiplied by the total number of
categories"*), and MaestroQA publishes real sampling practice — **60% of their surveyed customers grade
1–5% of interactions**, with the honest observation that random sampling under-samples hard tickets
(*"the harder tickets… get lost in an avalanche of easy tickets"*; Handy grades only DSAT tickets). But
worker 3 searched the entire fetched QA corpus and found that **the term "inter-rater reliability" does
not appear once, and no source publishes a Cohen's kappa or agreement rate.** Calibration sessions are
prescribed as a ritual and **never validated with a number**. A scoring system nobody has checked for
grader agreement is a scoring system that cannot support the decisions it is used for. Graded honestly as
MEASURED-ABSENCE across the corpus reached — not "nobody anywhere."

**Deflection is the strongest single wedge in support ops.** Worker 3 confirms it is unmeasurable as
normally computed: the standard method counts **KB article views, or help-centre sessions that didn't
produce a ticket**, as deflections — which cannot observe the counterfactual (did they get the answer,
give up, switch to email, or come back later as an unlinked "new" ticket?). *"Deflection rate counts
giving up the same as getting helped."* **No source found runs a controlled measurement** (e.g. a held-out
group without the article, compared on contact rate). Every deflection number in the industry is a proxy
its own author hedges. The honest pack teaching is the experiment design nobody runs — and note the
seam: designing that holdout is growth's method, executing the KB is success's.

**Erlang C does not apply to async support, and the canonical paper says so itself.** Worker 3 pulled the
primary — Gans, Koole & Mandelbaum (*M&SOM* 5(2):79–141, 2003). Erlang C assumes Poisson arrivals,
exponential service times, FCFS, and *"Blocking, abandonment, and retrials are ignored."* Erlang A adds
abandonment. And verbatim on our actual question: *"To the best of our knowledge, no analytical model has
yet been dedicated to truly multi-media contact centers."* The canonical reference concedes the gap. For
a 1–2 person async team **no source was found that translates any of this into practice** — worker 3
correctly refused to assert the likely answer ("nobody uses queuing theory at this scale") without a
citation. Flagged to channel B.

**Incident comms has one hard, citable rule.** Atlassian, primary: *"we recommend **never going more than
one hour without sending an update**. You should also always indicate when to expect the next update."*
Plus *"a zero-tolerance communication plan for any incidents involving security issues or data loss"* and
status-page-as-single-source-of-truth. This is the customer-facing half `operate` cedes.

**And there is a constructive replacement for the deflection rate.** Algolia's own analytics
documentation (checked directly) ships *No results rate*, *No clicks rate*, *Searches without results*
and *Searches without clicks* — and **the word "deflection" appears nowhere in it.** That is the finding,
and it points at the instrument the pack should teach instead:

- **Deflection is unobservable** — it needs the counterfactual (would this person have filed a ticket?).
- **Docs failure is observable** — a query that returned **zero results**, or results **nobody clicked**,
  is a directly observed fact. You know the docs failed that person without knowing what they did next.

So the honest help-content instrument is **zero-result and zero-click queries**, not a deflection rate,
and it has the property our reader needs most: it yields a **ranked, actionable backlog** (these exact
phrases failed, in volume order) at no headcount cost, on any docs site with search. It measures the
*docs*, not the support queue — which is precisely why it can be measured at all.

**SLA design**: the FRT critique is directionally right but only vendor-sourced — *"agents learn to stop
the clock without starting meaningful work"*, and **median over average** because a few slow replies skew
it. The ITIL impact×urgency structure is uncontested but we never reached Axelos's own wording.

---

## 5 · AI SUPPORT AGENTS 2024–26 — the pack's most under-canonized territory

Full detail: [`_raw-web-supportops-ai-agents.md`](_raw/_raw-web-supportops-ai-agents.md) §§2.1–2.5.

**τ-bench is the best measured evidence in the entire channel.** Yao, Shinn, Razavi & Narasimhan,
arXiv:2406.12045, evaluating agents by comparing **final database state against an annotated goal state**
and adding a consistency metric (pass^k). Verbatim: *"even state-of-the-art function calling agents (like
gpt-4o) succeed on <50% of the tasks, and are quite inconsistent (pass^8 <25% in retail)."* Open harness,
public methodology, reproducible. Set that against vendors claiming 70–90% resolution and the gap is the
story. (Note: τ-bench is authored by Sierra, who sell outcome-priced agents — but unlike any vendor
resolution-rate definition, its methodology is public and checkable. τ²-bench exists, not yet read.)

**Klarna, dated and sourced, including what did *not* reverse.** The Feb 27 2024 press release claims
verbatim: *2.3M conversations, two-thirds of chats · "the equivalent work of 700 full-time agents" · "on
par with human agents" on CSAT · "a 25% drop in repeat inquiries" · resolution "in less than 2 mins
compared to 11 mins" · "$40 million USD in profit improvement."* **Method stated: none.** No baseline
period, no definition of "repeat inquiry." And a line easy to miss: *"customers can still choose to
interact with live agents if they'd prefer"* — **the human option was never removed.**

May 2025, Siemiatkowski to Bloomberg: *"I just think it's so critical that you are clear to your customer
that there will be **always a human if you want**."* Klarna is rehiring — into an *"Uber-type customer
service setup"*, gig/flexible, not the prior employment structure.

**The correct reading, and the pack must get this right: this is NOT an AI-abandonment story, and the
narrative is now TRIPLE-refuted.** (1) Klarna's own Feb-2024 release already stated the human option
existed. (2) The May-2025 Bloomberg quote guarantees human *availability*; it does not withdraw AI.
(3) **Channel B found the CEO's own posts** (x.com/klarnaseb/status/2020988556374921683 and
/2019879525002473856) in which **he calls "we failed with AI" a misquote**, describing a 47%-smaller
organization achieved through attrition alongside a *deliberate* customer-service hiring increase framed
as differentiation. This **resolves worker 3's open item** on the much-repeated *"we went too far… the
result was lower quality"* line — the disposition is now stronger than "paywalled and unverified": the
CEO disputes the framing that quote is used to support. Humans returned for the **premium and complex
tier**; AI kept the high-volume tier. **The honest lesson is tier design — which contacts get a human —
not AI failure.**

Caveat on grading: those posts are the CEO's own statements about his own company — primary but
interested. They establish what he claims and they refute the misquote; they do **not** verify the 2024
performance numbers, which **remain unaudited**. An internal inconsistency nobody reconciles: the release
says "700 full-time agents" while Siemiatkowski's same-day post cites a 3,000-agent baseline.

**The market consolidated mid-run, and the detail is damning.** Verified against Salesforce's own press
release (June 15 2026): **Salesforce is acquiring Fin — formerly Intercom, renamed May 2026 — for
approximately $3.6 billion**, closing in Q4 FY2027, bringing "more than 30,000 companies" and a
support-specific proprietary model ("Apex"). The resolution claim is verbatim: *"including **examples
of** AI agents resolving on average **76%** of support volume end-to-end."* **"Including examples of" is
a selected-cases framing wearing an average's clothes** — and the underlying metric is the one worker 3
primary-verified from Fin's own help centre, which counts **"assumed resolution" (a customer exiting
without further comment)** as a resolution. A $3.6B acquisition is priced partly on a headline rate whose
own definition counts silence as success, presented via selected examples. **This is the best worked
example in the channel of why "how to read a vendor resolution claim" is not an academic exercise.**

**Vendor resolution rates are the deflection problem with a price tag.** Intercom Fin's own definition,
primary-verified: *"A resolution is counted when… the customer either confirms the answer was
satisfactory (confirmed resolution), **or exits the conversation without requesting further assistance
(assumed resolution)**."* Silence is billed identically to success — and Intercom's own naming
("assumed") concedes it. Decagon claims 80% average deflection; Ada claims "up to 83%" while **its own
ROI calculator uses a 40% baseline**. **No independent verification exists for any of the five vendors.**

**One AI-side paper with real numbers, but it belongs to `ai`.** Parlant's ARQ paper (arXiv:2503.03669,
abstract fetched directly) reports *"a **90.2%** success rate across 87 test scenarios, outperforming
both Chain-of-Thought reasoning (**86.1%**) and direct response generation (**81.5%**)."* Better
disclosure than any CS vendor manages — but authored by the Parlant team, **evaluated inside their own
framework**, n=87, preprint, no independent replication, and a **4.1-point margin** over chain-of-thought
on a small scenario set. Do not present 90.2% as established. Per the controller's recorded seam ruling
this is MECHANICS (`ai`); the policy-relevant nugget success can take is the named failure mode —
**"guideline re-application"**, i.e. agents drift off their instructions over multi-turn conversations,
so *a guideline stated once at the top of a conversation is not a guideline that holds*. Success cites
the failure mode; `ai` owns the remedy.

**Air Canada is the policy anchor, primary text read in full.** *Moffatt v. Air Canada*, 2024 BCCRT 149
(Feb 14 2024). The tribunal on Air Canada's defence that it wasn't responsible for its chatbot: ***"This
is a remarkable submission… It should be obvious to Air Canada that it is responsible for all the
information on its website. It makes no difference whether the information comes from a static page or a
chatbot."*** And: *"It also does not explain why customers should have to double-check information found
in one part of its website on another part of its website."* Damages $650.88, negligent misrepresentation.
**A support bot's statements are the company's statements.** This is POLICY (success), not mechanics (ai).

---

## 6 · COMMERCIAL MECHANICS — one genuinely well-evidenced finding

Worker 1 pulled **four primary SEC filings** and the result is the most concrete claim in the channel:
**"NRR" names four different calculations.**

- **Snowflake** (10-K FY2025): a **single trailing two-year** window, one-shot ratio; churned cohort
  members *"remain in the calculation and contribute zero product revenue."* Reported 126%.
- **Datadog** (10-K FY2020): **rolling 12-month** cohort, then *averaged* across trailing-12-month
  point-in-time rates. Reported >130%.
- **HubSpot** (10-K FY2024): **monthly** cohort, revenue-weighted, then **annualized** — and scoped to
  *subscription* revenue only.
- **Klaviyo** (S-1 2023): Datadog-like rolling monthly-weighted average, but **explicitly counts
  deactivated-then-reactivated subscriptions as retained** within the window.

Different windows, different scopes, different edge-case handling. **A "126% NRR" and a "131% NRR" are
not the same quantity and must never be compared.** Dave Kellogg's "Lazy NRR" critique names the common
gameable substitute: `(starting ARR + net expansion) / starting ARR` off a quarterly ARR bridge.

**Renewals and expansion are thin.** Notice periods cluster at 30/60/90 days (vendor-legal content
consensus, no primary playbook found). **Every "signal predicts expansion" claim located is unsourced
vendor content** — "80–85% of plan allotment is the strongest seat-expansion signal", "converts at a 65%
rate" — no study, no n, no method behind any of it.

**Tooling gotcha worth propagating to the crew:** **sec.gov rejects a Chrome UA** with a 403 "Undeclared
Automated Tool" page. It requires a declared identity string (`Org email`). Separately, the lead found
that **`research.rug.nl/files/…` is Cloudflare-gated but `pure.rug.nl/ws/files/…` serves the identical
PDF to a plain curl** — same file ID, different host. Both tricks unblocked primaries this run.

---

## 7 · EVIDENCE-GRADE LEDGER (what the pack may lean on, and how hard)

**MEASURED-WITH-METHOD — safe to build on, with scope stated**
- Ascarza 2018 (JMR) — randomized field experiments, risk ≠ uplift · *scope: telecom + membership org*
- de Haan, Verhoef & Wiesel 2015 (IJRM) — CFMs vs actual 2-yr retention · *scope: Dutch B2C services, 2010→2012*
- van Doorn, Leeflang & Tijs 2013 (IJRM Replication Corner) — CFMs vs financials · *scope: 46 NL firms, 4 industries*
- Keiningham et al. 2007 (JM) + Grisaffe 2007 — NPS replication failure + construct critique
- Verbeke et al. 2012 (EJOR) — statistical vs profit-optimal model selection · *scope: telecom*
- Gans, Koole & Mandelbaum 2003 (M&SOM) — Erlang assumptions, and the admitted async gap
- τ-bench (arXiv 2406.12045) — open agent benchmark, <50% success / pass^8 <25% retail
- *Moffatt v. Air Canada*, 2024 BCCRT 149 — full ruling text
- Four SEC filings (Snowflake / Datadog / HubSpot / Klaviyo) — NRR definitions verbatim
- Bain 2005 "Closing the Delivery Gap" — 80%/8%, disclosed n both sides
- **Fader, Hardie & Lee 2005** (*Marketing Science* / *JMR*) — BTYD, contractual vs non-contractual,
  the critique of scoring models · *scope: non-contractual retail; authors explicitly decline to claim
  subscription transfer*
- **Brier 1950** (*Monthly Weather Review*) — probabilistic-forecast scoring, and the 1950 statement of
  the Goodhart problem for scores
- **Salesforce press release, 15 Jun 2026** — Fin (formerly Intercom) acquisition, $3.6B, and the
  *"including examples of… 76%"* hedge, verbatim

**PRACTITIONER-REPORT — usable as craft, not as evidence**
- Lincoln Murphy (Desired Outcome, QBR critique) — cite *current* formulation, date the old one
- MaestroQA sampling practice · Klaus/Zendesk IQS formula
- Atlassian incident-communication cadence · Dave Kellogg on Lazy NRR
- Pragmatic Engineer's first-hand Klarna bot test (the only independent behavioural check found)

**VENDOR-CLAIM / FOLKLORE — cite only as the thing being corrected**
- Gainsight's 10 Laws (zero cited evidence) · "1 CSM per $2M ARR" (self-labelled guidepost)
- Klarna's 2024 headline numbers (no method, never audited)
- All five AI vendors' resolution/deflection rates (no independent verification, any of them)
- All health-score accuracy figures · all expansion-signal figures · all TTFV→retention figures
- All customer-education retention claims (self-selection) · all KB deflection ranges

---

## 8 · OPEN QUESTIONS

**Closed in round 2** (recorded so nobody re-burns the cycle):
- ~~Keiningham et al. 2007 paywalled~~ — **was already stale when flagged.** Worker 2 read it in full.
- ~~Reichheld & Sasser 1990 — try alternate routes~~ — **closed as definitively unavailable.** Semantic
  Scholar's API returns `"openAccessPdf": {"url": "", "status": null}` for the correct record (paperId
  `3cf9e452…`, PubMed 10107082). Combined with worker 2's exhausted routes, the honest disposition is
  **not "we failed to find it" but "no free copy exists"** — a paid HBR reprint is a controller purchase
  decision, not a research gap. The verdict (GROUNDED-BUT-MISQUOTED) does not change either way.
- ~~The Siemiatkowski "we went too far" quote~~ — **superseded** by channel B's primary posts (§5).

**Primary text still not obtained:**
1. **TARP "Consumer Complaint Handling in America" (1979/1986)** — NTIS/GPO-era, Google Books catalog
   records with no preview; Goodman's own commentary host is a parked domain. Needs a library route.
2. **Neslin et al. 2006 "Defection Detection" (JMR)** — read only as cited inside Verbeke 2012.
3. **Sharp & Romaniuk / Graham et al.** underlying PDFs — non-extractable JS shells; the 60/20 figure is
   institute-authored synthesis.
4. **Klarna's S-1/F-1** — never reached. Would settle the headcount question directly.
5. **Harrell 1982** (JAMA, c-index origin) — paywalled, not pursued. **Use channel C's lifelines
   concordance range 0.55–0.75 as the honesty anchor instead**; it does not depend on reading Harrell.
6. Schmittlein/Morrison/Colombo 1987 (original Pareto/NBD) · Wang/Fader/Hardie ZILN ·
   Fisher & Kordupleski 2019 · Ascarza et al. 2018 (*Customer Needs and Solutions*) · τ²-bench ·
   Klaus AutoQA whitepaper · Support Driven's own writing · Axelos's own ITIL priority wording.
7. **KBCM "CSM quota attainment 55–65%" (channel A's flag) — COULD NOT CONFIRM; likely a
   misattribution.** The KeyBanc/Sapphire private-SaaS survey reports **sales** quota attainment
   (*"expanded from ~70% to ~75%"*), not a CSM figure. **Do not cite it.** Settleable in one grep by
   anyone holding the full KBCM PDF; from public materials it does not check out.

**Substantive questions the research raised and did not answer:**
8. Is there any **post-2015, B2B-SaaS** replication of de Haan et al.? Everything we have is Dutch B2C.
9. Does the ~60/20 correction transfer to B2B SaaS at all, where seat-based concentration is structurally
   different from FMCG buyer panels? **Do not import it uncritically.**
10. Does anyone publish a health score validated out-of-sample the way de Haan et al. validate CFMs?
    Worker 2 searched five vendors and found nothing — **if that absence holds, it is the flagship.**
11. What does a solo/2-person async support operation actually do for staffing? No source says.
12. A measured nonresponse-bias study in a *software* CSAT context (we have only healthcare analogues) —
    relevant because de Haan et al. treated their own **15.4%** follow-up rate as needing a formal
    selection correction, while solo builders read 12-response dashboards as fact.

---

## 9 · SEAM FLAGS (recorded with the question attached — not assigned)

- **growth ← the big one.** Ascarza's risk-vs-uplift result is simultaneously (a) the case against
  success's own health-score playbook and (b) a direct methodological precedent for growth's shipped
  feasibility-gate wedge. Both packs want it. **Question:** does success own the *interpretation* ("your
  score can rank risk but not response") while growth owns the *uplift experiment*? That mirrors growth's
  shipped "data owns validity" ruling and looks like the clean cut — controller to confirm.
- **growth ← deflection and education measurement.** The holdout design that would make deflection or
  education claims honest is a retention experiment (growth); building the KB/academy is execution
  (success). **Question:** who states the caveat when success reports a result it didn't design?
- **growth ← NPS.** Growth's corpus already carries Kohavi + Hiten Shah. This channel adds the
  **academic** tier (Keiningham 2007, Grisaffe 2007, van Doorn 2013, de Haan 2015). **Merge, don't
  duplicate** — and prefer this channel's primaries, which are stronger than a conference talk.
- **operate ← incident comms.** Atlassian's material cleanly treats severity as an *input the comms plan
  consumes*. **Question:** does operate own severity-as-technical-classification while success owns only
  its translation into customer message and cadence? Verify against operate's shipped
  `incident-response.md:159` before writing boundary language.
- **ai ← support-bot policy vs mechanics.** Everything in §5 is deliberately POLICY (what counts as a
  resolution, when to escalate, who is liable, how to read a vendor claim). τ-bench is the one blurry
  item — it measures tool-use reliability. **Question:** is `ai` already claiming τ-bench for a mechanics
  purpose? Avoid conflicting treatments.
- **data ← survival vs snapshot.** Censoring and time-varying covariates are data-modeling craft.
  **Question:** does success teach only the CS-specific consequence (why a composite snapshot mis-prices
  tenure for renewal-timing) and point at data for the method?
- **product ← feedback loops.** **Question:** does success own collection, deduplication, and routing —
  the loop's plumbing — with the seam at "a structured, evidence-tagged request lands in product's
  queue," while product owns the prioritization call? Success must not be taught to score roadmaps.
- **marketing / growth ← the 80/20 figure.** The Ehrenberg-Bass evidence is a brand-buying literature, but
  success's "which accounts deserve attention" job depends on it. Reconcile against marketing's and
  growth's existing corpora before asserting a position.
- **legal-adjacent / operate ← renewal notice periods.** Success owns the renewal *workflow*; the notice
  period itself is a contract term. **Question:** where does that land, given no legal pack exists?
- **sales (unbuilt) ← expansion.** Unchanged from the charter, but note: we found **no measured evidence
  that any signal predicts expansion**, so whatever success ships here is craft, not evidence.
