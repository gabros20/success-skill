# _raw · web (channel D, LEAD SLICE 2) — BTYD / latent-churn literature + controller follow-ups

Author: channel D lead (opus). Date: 2026-08-02. Round 2, after all three workers reported.
Triggered by: controller cross-flags from channels A, B, C.
Method: all PDFs downloaded and text-extracted locally (`pdftotext`). Local copies `/tmp/dlead2/`.

---

## 1. THE BTYD LITERATURE — the rigorous answer to "is this customer still alive?"

Channel C flagged these as "D owns the papers." They turn out to be the most important addition of the
follow-up round, because **they are the academic literature that already solves the exact question a
health score is guessing at** — and they solve it for the self-serve/usage-based case that is our
default reader's situation.

**Sources obtained (brucehardie.com hosts these free — the author's own site, no paywall):**
- `/tmp/dlead2/bgnbd_2004-04-20.pdf` → Fader, Hardie & Lee, **"'Counting Your Customers' the Easy Way:
  An Alternative to the Pareto/NBD Model"** (published *Marketing Science* 24(2), 2005). Index:
  https://www.brucehardie.com/papers.html
- `/tmp/dlead2/rfm_clv_2005-02-16.pdf` → Fader, Hardie & Lee, **"RFM and CLV: Using Iso-Value Curves for
  Customer Base Analysis"** (published *Journal of Marketing Research* 42(4), 2005).
- `/tmp/dlead2/fader_hardie_aggtr0703.pdf` → Fader & Hardie, aggregate-transaction-data note.
- Antecedent (cited throughout, not separately downloaded): Schmittlein, Morrison & Colombo (1987),
  the original Pareto/NBD "Counting Your Customers" paper.

Grade: **MEASURED-WITH-METHOD** (peer-reviewed marketing science, formal probability models with
published likelihood functions, validated against holdout periods on real transaction data).

### 1.1 The distinction the CS canon never makes: CONTRACTUAL vs NON-CONTRACTUAL

This is the load-bearing concept, and it is stated explicitly and repeatedly. Verbatim (RFM/CLV paper):

> "A significant barrier has been our ability to model future revenues appropriately, particularly in
> the case of a **'noncontractual' setting (i.e., where the time at which customers become 'inactive' is
> unobserved)**."

And from the model's stated assumptions, the single best sentence in this whole channel for the
health-score flagship:

> "**The point at which a customer becomes inactive is unobserved by the firm. The only indicator of
> this change in status is an unexpectedly long time since the customer's transaction. And even this is
> an imperfect indicator: a long hiatus does not necessarily mean that the customer has actually become
> inactive. There is no way for an outside observer to know for sure** (hence the need for a model to
> make a 'best guess' about this process)."

And from BG/NBD:
> "This model describes repeat-buying behavior in settings where customer **'dropout' is unobserved**:
> it assumes that customers buy at a steady rate (albeit in a stochastic manner) for a period of time,
> and then become inactive."

**Why this matters enormously for our pack.** The CS canon's entire health-score apparatus is built for
the *contractual* case — a subscription with a renewal date, where churn is an observed event on a known
day. Our default reader (solo, self-serve, usage-based, often no seat contract) frequently lives in the
*non-contractual* case, where **there is no churn event to observe at all** — a customer who stops
showing up has not "churned," they have gone quiet, and quiet is not the same as gone. Applying a
contractual health score to a non-contractual business is a category error, and the academic literature
has been explicit about this distinction since 1987 while the CS vendor literature does not make it.

**This is a genuinely new wedge candidate and it is ours to claim:** *which of the two worlds are you in,
and does your churn question even have an observable answer?* Nothing in channels A or C found any CS
skill or repo that asks this.

### 1.2 The BTYD authors' own critique of scoring models — directly on point for health scores

Verbatim (RFM/CLV paper, on "scoring models (i.e., regression-type models)"):

> "But there are several problems with these models, especially when seeking to develop CLV estimates:
> • **Scoring models attempt to predict behavior in the next period.** But when computing CLV, we are
>   interested not only in period 2; we also need to predict behavior in periods 3, 4, 5, and so on. It
>   is not clear how a regression-type model can be used to forecast the dynamics of buyer behavior well
>   into the future…
> • **Two periods of purchasing behavior are required** — period 1 to define the RFM variables and
>   period 2 to arrive at values of the dependent variable(s)…
> • **The developers of these models ignore the fact that the observed RFM variables are only imperfect
>   indicators of underlying behavioral traits** (Morrison and Silva-Risso 1995). They fail to recognize
>   that different 'slices' of the data will yield different values of the RFM variables and therefore
>   different scoring model parameters."

And their closing recommendation, verbatim:

> "…we hope that future researchers will continue to use **stochastic models (instead of scoring
> models)** to address these new situations."

**Read that against the vendor health score.** A Gainsight/ChurnZero-style composite is precisely a
scoring model over recency/frequency-type inputs, and the peer-reviewed literature's stated position is
that scoring models are the *wrong instrument* for this question — not because they are inaccurate, but
because the observed inputs are imperfect indicators of a latent state and the model doesn't know it.
This is a much deeper critique than "health scores are unvalidated": it says the *form* is wrong.

**Scope limits, stated honestly by the authors themselves** (verbatim):
> "We also recognize that the context here — **noncontractual purchasing** — is a limitation. It is true
> that RFM analyses are generally conducted in such a domain, but the use of CLV goes well beyond it. It
> is worthwhile to consider how similar models and concepts can be applied to **subscriptions**,
> financial services, and other types of business relationships. **It is not immediately clear how the
> model components used here… need to be changed to accommodate these other contexts.**"
> "Another limitation is that we looked at only one cohort for CDNOW."

So: **do not import BG/NBD into a subscription business as if it were validated there.** The authors say
it isn't. The *distinction* transfers; the *model* does not, automatically. Ship the distinction.

### 1.3 Practical note

The BG/NBD paper's own selling point is accessibility — verbatim: *"We show, for instance, how its
parameters can be obtained quite easily in Microsoft Excel."* That is directly relevant to a solo
reader: the rigorous approach here is not out of reach, which weakens any "you need a CS platform for
this" framing.

---

## 2. SCORING-METRIC PRIMARIES (channel C asked D to own the papers)

**Brier (1950) — OBTAINED, PRIMARY TEXT READ.** Glenn W. Brier, "Verification of Forecasts Expressed in
Terms of Probability", *Monthly Weather Review* 78(1), January 1950 (Closed March 5 1950, Issued April 15
1950), U.S. Department of Commerce Weather Bureau. Free from AMS:
https://journals.ametsoc.org/downloadpdf/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.pdf
Local: `/tmp/dlead2/brier1950.pdf` / `brier.txt` (3 pages).

The paper defines "a verification score P" for probabilistic forecasts. Its framing is directly
transferable and worth quoting in the pack for a non-obvious reason — Brier's stated motivation is that
**a scoring system changes the behavior of the forecaster**:
> "…the verification scheme should influence [the forecaster]…"
and he notes the risk that a forecaster ends up optimizing "on the verification score" rather than
on the underlying phenomenon.

That is exactly the health-score failure mode: once a CSM is measured on moving the score, the score
stops measuring the customer. **The oldest paper in our corpus already named the Goodhart problem for
probabilistic scoring in 1950.** Grade: MEASURED-WITH-METHOD (foundational methods paper).

**Harrell (1982) concordance index — NOT OBTAINED.** Harrell, Califf, Pryor, Lee & Rosati, "Evaluating
the Yield of Medical Tests", *JAMA* 247(18):2543–6, 1982. Paywalled at JAMA; not attempted further given
budget. **PRIMARY TEXT NOT OBTAINED.** Channel C's independently-found anchor — lifelines' documented
concordance range of **0.55–0.75** for real survival models — stands as the practical honesty anchor and
does not depend on reading Harrell 1982. Recommend the pack cite the *range* (with C's source) rather
than the 1982 paper we have not read.

**Wang/Fader/Hardie ZILN** — not located this pass. Open.

---

## 3. CONTROLLER FOLLOW-UPS — dispositions

### 3.1 Reichheld & Sasser 1990 — the open item is now CLOSED as definitively unavailable

The controller asked whether another route could reach it before declaring it unverifiable. I checked the
authoritative index rather than guessing. **Semantic Scholar's API returns, for the correct paper record**
(paperId `3cf9e452adceb66ead134d9377ae8155016aa259`, title "Zero defections: quality comes to services.",
year 1990, PubMed 10107082):

```
"openAccessPdf": {"url": "", "status": null, "license": null}
```

**There is no open-access PDF indexed anywhere.** Combined with worker 2's exhausted routes (HBR paywall,
Bain Cloudflare, three dead university mirrors, Scribd/SciSpace JS shells) and my own check of the HBS
faculty record (bibliographic only), the correct disposition is: **not "we failed to find it" but "no
free copy exists."** Obtaining it requires a paid HBR reprint or institutional access — a purchase
decision for the controller, not a research gap.

**Consequence for the pack:** the 85%/50%/30%/125% figures remain convergent-secondary and must be
labelled as such. Given the verdict is *GROUNDED-BUT-MISQUOTED* either way, and given that what we are
shipping is the correction ("the 25–95% range appears in no primary text"), primary access would sharpen
the citation but would not change the ruling.

### 3.2 Keiningham et al. 2007 — this open item was already STALE

The controller's note listed "JM 2007 paywalled" as open. **It is not open.** Worker 2 downloaded and read
the full paper (`/tmp/d2/keiningham_npjm_2007.pdf`), plus Grisaffe 2007. The verbatim key results are in
`_raw-web-falsification-churn-evidence.md` §2.3. No further action needed.

### 3.3 Klarna — channel B's primary tweets UPGRADE our finding (correction at source)

Channel B found Siemiatkowski's own posts (x.com/klarnaseb/status/2020988556374921683 and
/2019879525002473856) in which he calls "we failed with AI" a **misquote**, and describes a 47%-smaller
organization achieved via attrition, with a deliberate customer-service hiring increase framed as
*differentiation alongside AI*, not a retreat from it.

**This resolves worker 3's open item #7** (the "we went too far… the result was lower quality" quote,
which worker 3 correctly flagged as widely-repeated-but-paywalled-and-unverified). The disposition is
now stronger than "unverified": **the CEO disputes the framing the quote is used to support.**

**Corrected reading, triple-supported:** the tidy "Klarna reversed its AI bet" narrative is refuted by
three independent primary sources — (1) Klarna's own Feb-2024 release already said *"customers can still
choose to interact with live agents if they'd prefer"*; (2) the May-2025 Bloomberg quote is about
guaranteeing human availability, not withdrawing AI; (3) the CEO's own posts call the failure framing a
misquote and describe headcount reduction by attrition alongside a deliberate CS hiring increase.
**The pack must not tell the reversal story.** The honest lesson is about *tier design* — which contacts
get a human — not about AI failing.

Note on grading: these are the CEO's own statements about his own company, i.e. primary but interested.
They establish what he claims, and they refute the misquote; they do not independently verify the 2024
performance numbers, which remain unaudited.

### 3.4 Salesforce acquires Fin (formerly Intercom) — VERIFIED PRIMARY, and it matters more than it looks

Controller asked to verify or mark unverified. **Verified against Salesforce's own press release**,
fetched and text-extracted directly (`/tmp/dlead2/sf_fin.html`):
https://www.salesforce.com/news/press-releases/2026/06/15/salesforce-signs-definitive-agreement-to-acquire-fin/
Dated **June 15, 2026**. Verbatim:

> "Salesforce will acquire Fin for approximately **$3.6 billion**, subject to customary purchase price
> adjustments."
> "The transaction is expected to close in the **fourth quarter of Salesforce's fiscal year 2027**…"
> "…an established global customer base of **more than 30,000 companies**."
> "Fin's core offering, its AI Agent, resolves complex customer queries end-to-end, across every channel,
> including live chat, email, WhatsApp, SMS, phone, and Slack."
> "…powered by the company's proprietary AI model, **Apex**, that is purpose-built for customer support."

Two facts the pack needs:
1. **Intercom renamed itself Fin (May 2026).** Any pack text referring to "Intercom Fin" should say
   "Fin (formerly Intercom)". Worker 3's fin.ai citations are current and correct.
2. **The resolution-rate claim is carefully hedged, and the hedge is the story.** Verbatim:
   > "The AI Agent has already demonstrated strong customer outcomes, **including examples of** AI agents
   > resolving on average **76%** of support volume end-to-end."

   *"including examples of"* is not a fleet average — it is a selected-cases framing wearing an
   average's clothes. **And the underlying metric is the one worker 3 primary-verified from Fin's own
   help centre, which counts "assumed resolution" — a customer exiting without further comment — as a
   resolution.** So: a $3.6B acquisition is priced, in part, on a headline rate whose own definition
   counts silence as success, presented via selected examples. This is the single best worked example in
   the whole channel of why the pack's "how to read a vendor resolution claim" teaching is not academic.

### 3.5 KBCM CSM quota attainment "55–65%" — COULD NOT CONFIRM, likely a misattribution

Channel A flagged this as a findable named primary. I searched the KeyBanc/Sapphire private-SaaS survey
materials (Sapphire Ventures press page, PRNewswire and KeyBanc investor-relations releases, the 2024
survey landing page, SaaSletter's benchmark writeup). **The KBCM survey's quota-attainment reporting is
about SALES quota attainment, not CSM quota attainment** — the figure that appears is *"quota attainment
expectations also having expanded from ~70% to ~75%"*. No CSM-specific 55–65% figure was located in any
KBCM material.

**Disposition: do not cite "KBCM CSM quota attainment 55–65%."** Either it is a different source, a
different year, or — most likely — a conflation of a sales-quota figure with a CS context. Reported back
to the controller rather than silently dropped. If someone has the full KBCM PDF, it can be settled in one
grep; from public materials it does not check out.

### 3.6 NEW NEVER-SHIP CLASS accepted from channel A: unsourced SLA defaults

Channel A proposes, and I endorse and generalize: **unsourced SLA defaults** — "First Response: 1 hour
(P0)", "4-hour resolution for critical", "24-hour first reply" — presented as template values in
docs, blog posts, and skill packs, which readers then adopt as **real customer commitments**.

Why this belongs on the never-ship list as a CLASS, and why it is worse than an ordinary uncited number:
an uncited statistic misleads a reader's *belief*; an uncited SLA default becomes a **promise made to
someone else**, with contractual and reputational consequence, and it is adopted precisely by the readers
least equipped to staff it (our default solo reader). It also interacts with worker 3's FRT finding — a
first-response target is the metric most prone to being gamed by stopping the clock without starting work.

**Rule form for the pack:** never publish a response-time number as a default. Publish the *method* for
deriving one from your own volume, hours, and staffing, and require the reader to state the hours it
applies within. Any example must be visibly labelled as an example and never as a recommendation.

This also connects to channel E's finding that "customer-facing response-time promises" is one of only
two genuine orphan slots across all 12 shipped packs — so success will be the pack that owns this, which
makes getting the rule right load-bearing rather than incidental.

---

---

## 3A. FINAL CROSS-FLAG BATCH FROM CHANNEL C (two cheap primaries, both worth it)

### 3A.1 Algolia DocSearch analytics — the CONSTRUCTIVE answer to the deflection gap

Fetched Algolia's own documentation directly (`/tmp/dlead2/a.html`):
https://www.algolia.com/doc/guides/search-analytics/concepts/metrics/ and `/overview/`

**The metrics Algolia actually ships** (verbatim from their metric list): *Total users · Total searches ·
**No results rate** · Click-through rate · Conversion rate · Add-to-cart rate · Purchase rate · Revenue ·
Average order value · **No clicks rate** · Click position · Searches · **Searches without results** ·
**Searches without clicks** · Results · Filters · Geo · Rules.*

Definitions, verbatim:
> "The No Results Rate chart shows the percentage of searches with no results. For a detailed view of the
> searches without any results, go to the Searches without Results tab."
> "The Click-through Rate chart shows the percentage of tracked searches with at least one click event."

**The word "deflection" does not appear anywhere in Algolia's analytics documentation.** That is not a
disappointment — it is the finding, and it *strengthens* worker 3's deflection conclusion rather than
qualifying it away. Algolia sells **search-quality** metrics, not deflection metrics, and is careful not
to claim the latter.

**The distinction to ship, and it converts a purely negative finding into a positive teaching:**

- **Deflection is unobservable.** It requires the counterfactual — would this person have filed a ticket?
  You cannot see it without a holdout. Every deflection number in the industry is a proxy (worker 3 §1.5).
- **Docs FAILURE is observable, cheap, and needs no counterfactual.** A query that returned **zero
  results**, or returned results **nobody clicked**, is a directly observed fact. You know the docs failed
  that person; you do not need to know what they did next.

So the honest instrument for help-content is **zero-result and zero-click queries**, not a deflection
rate — and it has the property our default reader needs most: it produces a **ranked, actionable backlog**
(these exact phrases failed, in volume order) rather than a vanity percentage. It is available on any
docs site with search, at no headcount cost. **Recommend this as the pack's replacement instrument for
"deflection rate," and note it is a measurement of the docs, not of the support queue.**

Grade: **MEASURED-WITH-METHOD for the metric definitions** (vendor's own product documentation, definitions
are precise and self-consistent); **the pedagogical framing above is the lead's synthesis, not Algolia's
claim** — Algolia never positions these as a deflection substitute.

### 3A.2 Parlant ARQ paper (arXiv 2503.03669) — real numbers, but on `ai`'s side of the seam

Fetched the arXiv abstract page directly (`/tmp/dlead2/arq.html`).
**Karov, Zohar & Marcovitz, "Attentive Reasoning Queries: A Systematic Method for Optimizing
Instruction-Following in Large Language Models"**, arXiv:2503.03669.

Verbatim from the abstract:
> "In extensive testing within Parlant, our framework for reliable customer-facing agents in which ARQs
> were born out of necessity, they achieved a **90.2% success rate across 87 test scenarios**,
> outperforming both Chain-of-Thought reasoning (**86.1%**) and direct response generation (**81.5%**).
> ARQs showed particular strength in addressing persistent failure modes like **guideline re-application
> and hallucination prevention**."

**Grade: VENDOR-CLAIM-WITH-DISCLOSED-METHOD.** Genuinely better than the CS-vendor norm — there is a
stated comparison, stated baselines, and a stated n. But: the authors are the Parlant team (C correctly
called it "vendor-of-the-idea"), the evaluation is **conducted inside their own framework**, n=87
scenarios is small, and it is an arXiv preprint with **no independent replication located**. The margin
over chain-of-thought is **4.1 points on 87 scenarios** — well within the range where scenario selection
matters. Do not present 90.2% as an established result.

**Seam disposition:** this is **MECHANICS** (a prompting/reasoning-structure technique), which sits on
`ai`'s side of the ruling the controller already recorded — success owns the *policy vocabulary*
(guidelines, boundaries, escalation, strict-vs-fluid), citing Parlant as the implementation. The one
genuinely policy-relevant nugget is the named failure mode: **"guideline re-application"** — agents drift
off their instructions over multi-turn conversations. That is a policy-design consequence (a guideline
stated once at the top of a conversation is not a guideline that holds), and success can teach it without
touching the ARQ technique itself. **Recommend: success cites the failure mode, `ai` owns the remedy.**

### 3A.3 Lincoln Murphy "Desired Outcome" as the canon's phrasing origin — recorded, no new fetch

C flags Murphy's "desired outcome" as the origin of the whole canon's phrasing. This is consistent with
worker 1's finding and needs no separate verification, but it makes worker 1's **superseded-formula
catch materially more important**: if this phrase is the headwater of the canon's vocabulary, then a pack
citing the *outdated* form ("Required Outcome + AX") propagates a stale version of the field's founding
phrasing. **Cite the current form ("Goal + Appropriate Experience"), from his own site, and date it.**
See `_raw-web-canon-commercial.md` §2.

---

### 3A.4 GitLab PTE/PTC — the best candidate for a disclosed enterprise churn-model accuracy, and it comes up empty

Channel C flagged GitLab's Propensity-to-Expand / Propensity-to-Churn models as the strongest remaining
candidate for an *evidenced* enterprise churn-model accuracy statement. Searched GitLab's public handbook
and their public sales-enablement issue tracker.

**The models are real and publicly described:**
- GitLab's Data Science team publishes Propensity to Buy, **Propensity to Churn (PTC)**, and **Propensity
  to Expand (PTE)** models.
- PTC "takes in data from Salesforce, Zuora, Bizible, and product usage, and predicts which accounts are
  likely to churn or contract in the next 3 months."
- Output is a **1-to-5 star rating on the SFDC account record**.
- A PTC pilot ran in Feb (FY23-Q1); the PTC pilot design is described as mirroring the earlier PTE pilot.
- Sources: https://handbook.gitlab.com/handbook/customer-success/customer-health-scoring/ ·
  https://gitlab.com/gitlab-com/sales-team/field-operations/enablement/-/issues/1213 ·
  GitLab handbook `content/handbook/sales/playbook`.

**What is NOT published anywhere reachable: any accuracy figure.** No AUC, no precision/recall, no lift,
no top-decile performance, no holdout/backtest result, no confusion matrix, no base-rate comparison.
The output is a **1–5 star rating with no stated calibration** — stars, not probabilities.
Grade: **METHOD-PARTIALLY-DISCLOSED, ACCURACY UNDISCLOSED.**

**Why this matters more than another vendor null result.** Worker 2's finding was "no accuracy disclosure
across five CS vendors" — which a skeptic could dismiss as vendors protecting marketing claims. GitLab is
a *different and much harder case*: a public company, with a dedicated in-house Data Science team, running
its own models on its own data, publishing one of the most radically transparent handbooks in the
industry — **and it still publishes no accuracy number for its churn model.** Combined with channel C's
finding that GitLab's *health score* is explicitly not asked to predict churn (prediction is delegated to
these separate PTC/PTE models, which are themselves self-disclaimed as "not a silver bullet") and that
backtesting appears in their handbook as a **success criterion, not a result**, the picture is consistent
top to bottom:

**Nobody publishes churn-model accuracy — not the vendors, not the most transparent enterprise in the
market, not even when they have the team and the data to compute it.** That is the flagship's empirical
foundation, and it now holds across three independent probes (worker 2's five vendors, channel C's repo
sweep finding no repo reports precision/recall/AUC vs real outcomes, and this).

**Honest limit on the claim:** absence of *public* disclosure is not proof the models are inaccurate or
that no internal validation exists. The pack must say "not published," never "not measured." What we can
assert is that **a reader cannot verify any of these scores**, and that a 1–5 star rating with no stated
calibration cannot be audited by the person relying on it.

**SECOND ROUND (controller's final flag: try the separately-public DATA-SCIENCE handbook, blog, talks).**
Done. Fetched https://handbook.gitlab.com/handbook/enterprise-data/organization/data-science/ directly
(2.29 MB, `/tmp/dlead2/gl_ds.html`) and searched the extracted text.

**Zero hits for every performance term: `AUC`, `precision`, `recall`, `validat*`, `backtest`, `lift`,
`F1`, `holdout` — and the page does not even name PTC or PTE.**

What the page *does* publish is process and tooling. Verbatim, the entire public evaluation standard:
> "**Evaluation** Performance is generally measured by how **accurate, powerful, and explainable** the
> model is. Findings are presented to the stakeholders for feedback."

No metric named, no threshold, no number — a qualitative prose criterion. And the tooling section shows
the capability plainly exists, verbatim:
> "Snowflake Feature Store as an open-source Feature Store for Machine Learning models · **Monte Carlo
> for drift detection** · **Tableau Server for model monitoring and on-going performance evaluation**"
plus "JupyterLab & GitLab CI/CD: Model Training, Tuning, and Selection" and Papermill batch scoring.

**This is a stronger result than the first round, and it sharpens the finding.** It is not merely that
GitLab omits a number — **the publicly stated evaluation standard is itself qualitative** ("accurate,
powerful, and explainable"), while the infrastructure to compute a quantitative one (drift detection,
model-performance monitoring) is documented as in place. The gap is disclosure, not capability.

**Routes exhausted for this flag:** CS handbook (round 1), public sales-enablement issue tracker
(round 1), sales playbook tree (round 1), **enterprise data-science handbook (round 2)**, GitLab blog
(round 2), conference-talk search (round 2). **Marked UNFOUND-NOT-ABSENT** per the controller's
instruction — GitLab may well validate these models internally; nothing about them is public.
**Flag CLOSED.**

---

## 4. Open items after this round

1. Harrell 1982 (JAMA, paywalled) — use channel C's lifelines 0.55–0.75 anchor instead.
2. Wang/Fader/Hardie ZILN — not located.
3. Schmittlein, Morrison & Colombo 1987 (the original Pareto/NBD) — cited throughout, not separately
   obtained; the 2004/2005 papers restate its assumptions verbatim, which may be sufficient.
4. Reichheld & Sasser 1990 — closed as "no free copy exists"; a paid reprint is a controller decision.
5. KBCM CSM quota figure — unresolved, likely misattributed (§3.5).

## 5. Seam flags from this round

- **data ← BTYD.** The contractual/non-contractual distinction is a modeling concept. **Question:** does
  success own the *diagnostic* ("which world are you in, and is your churn event observable?") while data
  owns the *estimation*? The diagnostic is a business-shape question and reads as success's; the
  likelihood function plainly is not.
- **growth ← BTYD.** CLV and buyer-behavior models sit close to growth's territory. **Question:** does
  growth already claim CLV? If so, success should take only the latent-churn/aliveness half and cite
  across, since "is this customer still alive" is a relationship question, not a valuation one.
- **ai ← Salesforce/Fin.** The acquisition consolidates the AI-support vendor landscape. Success owns
  reading the *claim*; ai owns the *model* (note Fin's "Apex" is a proprietary support-specific model —
  squarely ai's mechanics territory).
