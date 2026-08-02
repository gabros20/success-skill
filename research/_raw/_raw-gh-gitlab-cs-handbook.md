# _raw-gh-gitlab-cs-handbook — GitLab's public Customer Success handbook

Channel C · **lead slice**, follow-up pass authorized by the controller 2026-08-02.
Scope: `content/handbook/customer-success/` in `gitlab-com/content-sites/handbook`.
Companion to worker 3's pass over the sibling `content/handbook/support/` tree
(`_raw-gh-ai-support-kb.md` §D).

**Access note:** this project lives on **GitLab.com, not GitHub** — there is no GitHub mirror.
Read via the public GitLab REST API, no auth required:
`https://gitlab.com/api/v4/projects/gitlab-com%2Fcontent-sites%2Fhandbook/repository/tree?path=content/handbook/customer-success&ref=main&recursive=true`
and `/repository/files/<url-encoded-path>/raw?ref=main`. All reads 2026-08-02, `ref=main`.

**Licence: CITE-ONLY (unchanged).** Worker 3 established that the repo's root `LICENSE` scopes itself
to *"the GitLab Software"* — the Hugo site code — and carries no content licence for the handbook
prose; no CC BY-SA notice exists in-repo. Charter clause (e), thin-licence-on-thick-IP.
**Attribute and link; never present this prose as ours, and never reproduce a page wholesale.**
Quotes below are short excerpts for evidentiary purposes.

---

## 1. Scale, and why it matters

`content/handbook/customer-success/` has **31 top-level entries** — 17 directories, 14 loose pages.
The `csm/` subtree alone recursively lists **~100 files** across `escalations/`, `gainsight/`,
`health-score-triage/`, `qbr/`, `renewals/`, `risk-mitigation/`, `success-plans/`, `segment/`,
`digital-journey/`, `engagement/`, `adoption-landing-zones/`, `csm-onboarding/` and more. Siblings
include `customer-health-scoring/`, `customer-onboarding/`, `product-usage-data/` (10 files, incl.
`maturity-scoring.md`, `platform-value-score.md`, `metrics-based-playbooks.md`),
`renewals-managers/`, `education-services/`, `professional-services-engineering/`, `playbooks/`,
`partners/`, `public-sector/`, `workshops/`.

**This is almost certainly the largest publicly readable customer-success handbook in existence**,
and it is the charter's enterprise-CSM canon (§wedge 1) in its most complete public form. It is
Gainsight-operated throughout — which makes it *canon-with-interest*, exactly as charter rule 5
predicts, but it is also **primary source about its own limitations**, which is what makes it
valuable here.

---

## 2. The health score: GitLab's P.R.O.V.E. model

Source: `content/handbook/customer-success/customer-health-scoring/index.md` (353 lines).

Five weighted groups (verbatim from the "P.R.O.V.E." block, lines 55-59):

```
Product: License activation + User engagement + Use Case: 50% weighting
Risk: CSM Sentiment + Opportunity Renewal risks: 25%
Outcomes: Success Plan + Verified Outcomes: 10%
Voice of the customer (VoC): Support + Surveys: 5%
Engagement: Customer Engagement + Executive Sponsorship + Events + Certifications: 10%
```

Measure-level weights inside **Product** (50%): License utilization 30%, User Engagement 10%,
SCM adoption 15%, CI adoption 15%, DevSecOps adoption 15%, CD adoption 15%.
Banding is Gainsight's: **Green 75-100, Yellow 50-74, Red 0-49**, with
`Calculation: ((Score * Weight) + (Score * Weight)... / (Max Potential Score * Weight))`.

---

## 3. Seven findings that matter for the health-score flagship

### 3.1 Backtesting is listed as an ASPIRATION, not an accomplishment

Under "Direction → Success criteria" (line 19), verbatim:

> - "Customer health scoring framework **has been backtested and validated as effective and
>   beneficial**"

It sits in a bulleted list of *success criteria* alongside ">95% of customers have a health score
(aligned to FY24 Yearlies)" — i.e. these are targets the programme is aiming at. **The most
sophisticated public CS org, running Gainsight, publishes "validate that this works" as a goal
rather than a result.** This is the same shape as worker 3's deflection finding (ticket deflection
listed as a wishlist KPI, dashboard "a work in progress") — **GitLab's handbook is unusually honest
about publishing what it intends rather than what it has achieved, and twice that intention is
"prove the measurement works."**

### 3.2 The health score is NOT the churn predictor — they are separate artifacts

This is the **single most important structural fact** in the pass. Under "Predictive Analytics"
(lines 272-279), the *prediction* problem is handled by two distinct named models, not by the health
score:

| Prediction Type | Model Name | Status |
|---|---|---|
| Expansion | Propensity To Expand (PTE) | Active |
| Churn and Contraction | Propensity To Churn or Contract (PTC) | Active |

Both link to `internal.gitlab.com/handbook/sales/propensity_models/` — **an internal-only URL. Their
method, features and accuracy are not public and could not be verified.**

And the section opens by disclaiming itself (line 274, verbatim):

> "Predictive Analytics is not a silver bullet. It will not cure all that ails you. Instead, this
> methodology is probabilistic and incorporates health measures to correlate the typical journey of
> 'healthy' customers (expand and renew) with 'unhealthy' customers (downgrade and churn)."

**Reading for the pack:** at the most mature public CS org we can inspect, the health score is a
*diagnostic and communication device* and churn *prediction* is a separate ML artifact. The two jobs
are not merged. That is the honest answer to "what can a health score predict": **it is not asked
to.** Any vendor claiming their health score *is* the churn prediction is doing something GitLab
deliberately does not do.

### 3.3 A quarter of the score is an explicit human guess — and it can override everything else

`CSM Sentiment` is 100% of the **Risk** group (25% of the total), described as (line 147):

> "Qualitative measure the CSM updates to indicate their perceived sentiment of the customer …
> For all `CSM-owned` accounts, CSM manually determines red/yellow/green"

Then, decisively (line 163):

> "**CSM Sentiment Override of Overall Health Score**: When the CSM Sentiment score becomes red, the
> overall score will automatically become red. Once the CSM Sentiment moves back to a green or yellow
> score, the standard weighting of measures and groups will be reapplied as usual."

**The weighted arithmetic is overridden by one human field in exactly the case the score exists
for.** A customer can score perfectly on the 50%-weighted Product group and still be Red because the
CSM said so. The elaborate weighting is real for green/yellow discrimination and **decorative at the
red boundary.**

This is not necessarily wrong — a CSM who has just been told the champion is leaving knows something
no telemetry does. But it means **the number is a human judgement wearing a weighted-average
costume**, and the pack should say so plainly. It also makes "our health score is data-driven"
unfalsifiable in the case that matters.

### 3.4 Missing data silently shifts the score toward opinion

Two rules interact badly. First, missing measures are not penalised (line 231):

> "if stats are missing for any health measure, it is counted as `NULL` instead of a value (i.e., red)."

Good. But then (lines 131-136):

> "If an individual measure is missing, the weighting is redistributed to the completed measures. …
> Example 1: If all product usage stats are missing, then it's entirely reallocated to the other
> measures (Engagement, ROI, CSM Sentiment...). **Heavier weighted measures, such as CSM Sentiment,
> would receive a bigger allocation because it's already the largest.**"

**When telemetry is absent, the score does not become less confident — it becomes more subjective,
automatically, without telling anyone.** Combined with 3.3, an account with no usage data has a
health score that is mostly the CSM's opinion, presented on the same 0-100 scale as a fully
instrumented one.

Made explicit for new customers (line 133):

> "Except for CSM Sentiment, all health measures will typically be **NULL for the first 30 days** of
> the customer's onboarding due to insufficient stats and inaccurate results"

**For the first 30 days the health score is, by construction, the CSM's opinion and nothing else** —
precisely the window where onboarding risk is highest. Strong, concrete teaching point.

### 3.5 The machine and the human rubric disagree about what ignorance means

The automated scorecard treats missing data as `NULL` → redistributed → **neutral** (3.4).
The human rubric in `csm/health-score-triage/index.md` treats missing information as **risk**:

- Yellow (line 35): *"Potential risk **or significant lack of information leading to uncertainty**."*
- Red (line 51): *"Specific, known risks … **or overwhelming lack of information, such as
  unresponsiveness leading up to renewal**."*

**Same handbook, opposite conventions.** The human is told "not knowing is a risk state"; the
algorithm is told "not knowing is neutral, redistribute." The pack should take the *human* side —
**ignorance about an account is a finding, not a gap** — and can cite this internal disagreement as
evidence that the automated convention is a modelling convenience rather than a considered position.

### 3.6 A published model containing components that do not exist

The "PROVE Components" table carries a **Maturity** column (lines 255-270). Several measures the
model advertises are marked **"Not started"**:

| Category | Measure | Maturity |
|---|---|---|
| Outcomes | Positive Business Outcomes (PBOs) | **Not started** |
| VoC | Support - CSAT | **Not started** |
| VoC | NPS Surveys | **Not started** |
| Engagement | Executive Sponsorship | **Not started** |
| Engagement | Events | **Not started** |
| Engagement | Certifications | **Not started** |
| VoC | Support - Engagement | 70% |
| Product | User Engagement | 100%; "in progress" |

The whole **VoC group is 5% of the score and three of its four measures are unbuilt** — so the
"Voice of the customer" input to GitLab's customer health score is, in practice, support-ticket
counts. **NPS is in the published model and not implemented.** Anyone reading the PROVE diagram
would reasonably believe surveys feed the score; the maturity column says otherwise. Worth citing
whenever a vendor shows a health-score architecture diagram.

### 3.7 Support contact is scored as a negative — and GitLab is fixing it

Current automated bands (line 150):

> "- Green: 1-5 tickets/month · Yellow: 5-15 tickets/month · Red: More than 15 tickets/month"

Note **0 tickets is not Green** (the green band starts at 1), and the bands **overlap at 5** — a real
spec defect; the human rubric states "6-15" for Yellow (triage page line 43), so **two pages of the
same handbook publish different bands.**

More interesting, the roadmap row for `Support - Engagement` (line 264) says:

> "Retain existing methodology, but **tweak to allow more tickets as a good thing**" — Maturity 70%

**GitLab has concluded its own signal direction was wrong** and is inverting it. The human rubric
already encodes the subtler version — Yellow includes (line 43):

> "Not leveraging technical support services **or** has a large number of cases … (6-15 tickets per
> month, **or no ticket(s) opened after being advised by the CSM that Support is the best path to
> resolution**)"

i.e. **silence after being told to ask for help is also a yellow signal.** The relationship between
support volume and health is non-monotone, and this handbook documents an org discovering that.
Directly relevant to the pack's support ↔ health seam.

---

## 4. Practices worth lifting (framework only — cite GitLab, do not copy prose)

### 4.1 Every input has an explicit expiry

`customer-health-scoring/index.md` §"Clearing stale health measures" (lines 169-178):

- **Product**: usage data → `NA` after **60 days**. Rationale, verbatim: *"This is to prevent
  analysis and actions based on outdated data. In this case, we prefer to show nothing ('NA') over
  outdated data."*
- **CSM Sentiment**: flagged stale at **90 days** (exclamation point on the dashboard), forced to
  `NA` at **120 days**.
- **Support measures**: stale after **30 days**, auto-`NA`.

**Showing nothing beats showing stale** is the rule, and every signal has a different, justified
half-life. This is the best practice found in the whole channel-C corpus for keeping a health signal
honest, and it costs nothing to adopt. Contrast with the Dynatrace exhibit
(`_raw-gh-voc-onboarding-csops.md` §8b), which has no expiry concept at all.

### 4.2 Thresholds are segmented, not universal

`Meeting cadence` (line 153) uses different bands per service tier:

- `CSM Prioritization = 1`: Green ≤ 35 days · Yellow > 35 and ≤ 60 · Red > 60
- `CSM Prioritization = 2`: Green ≤ 65 days · Yellow > 65 and ≤ 90 · Red > 90

Several measures are additionally marked `N/A for Scale and Tech Touch` — i.e. **the model knows
which measures are meaningless for low-touch segments and switches them off** rather than scoring
them badly. Directly answers the charter's §1033 concern: the same score is not applied to
high-touch and self-serve accounts.

This is the correct counter to the failure mode recorded in `_raw-gh-voc-onboarding-csops.md` §8b.3
(Dynatrace's unexplained 3d/14d recency thresholds applied uniformly).

### 4.3 Relationship breadth is a measured signal

`Persona engagement` (line 154), 50% of the Engagement group:

> "Green: **both** Dev Lead and Security Lead are listed as external attendees on a timeline entry in
> the past three months · Yellow: one of the two personas attend · Red: neither"

and Yellow in the human rubric includes *"Working with a single contact at a company
(single-threaded)"*. **Single-threading is a named, scored risk** — a cheap and unusually concrete
signal, and one that survives translation to a solo/self-serve context better than most of this
handbook does.

### 4.4 The churn-reason taxonomy — two axes, with disambiguation rules

`csm/health-score-triage/index.md` separates **what will happen** from **why**:

**Risk impact** (lines 166-171): Customer Churn · Tier Downgrade · Seat Churn · **Customer Sentiment
(Impact Unknown)** · Competitor · Stage Name.
The "Impact Unknown" option is the honest one — it lets a real signal be recorded without inventing
a magnitude.

**Risk reason** (lines 175-199): Lack of adoption · Product Value/Gaps · Product Quality/Availability
· Lack of Engagement/Sponsor · Loss of Budget · Corporate Decision · Other. Each carries a
**disambiguation rule against its nearest neighbour**, which is what makes the taxonomy usable:

> Lack of adoption — *"Customer never adopted the product or specific features so they did not get
> value… **If they didn't adopt because they didn't see / experience value, it should be Product Gap**"*
> Loss of Budget — *"…lost budget due to business contraction, change of priorities, reduction of
> employees, or other. **This was not a competitive loss.**"*
> Corporate Decision — *"…chose a different product **but not because of product gaps, adoption, etc.**
> This would be a top-down decision (e.g., ELA, decision to commit to a single provider)"*

**A category list without tie-breakers is not a taxonomy** — this one has them, and that is the
liftable idea. Compare `churnkey/sdk`'s cancel-reason → offer mapping
(`_raw-gh-voc-onboarding-csops.md` §6): Churnkey's reasons are self-serve and self-reported;
GitLab's are assessor-coded with disambiguation. **Two honest reason taxonomies for two different
motions** — the pack can present both and say which fits which reader.

### 4.5 Escalation as a notification ladder (the third meaning of "escalation")

`csm/health-score-triage/index.md` §"At Risk Communication Guidelines" (lines 205-219):

- **Yellow** → Account Executive, Solution Architect, Regional CSM Manager, CSM Director
- **Red** → all of the above **plus** Area Sales Manager, Regional Director, **VP of Customer Success**

Plus a gate (line 162): *"If a CSM has marked an account as Red and further assistance from Product,
Support or Managers+ is needed, open an Account Escalation."*

This is a concrete instance of the **third** sense of "escalation" flagged in `github-report.md` §5.3
— neither SLA-breach-notify, nor bot-to-human handoff, nor SRE paging, but **who must be told, by
severity**. It pairs with the sibling support handbook's *"Escalate early. Visibility across GitLab,
up to and including the CEO, is always better earlier rather than later."*

### 4.6 A terminal state that exists because the tool has no colour for it

`Will Churn` (line 70), verbatim:

> "Very rarely, a customer reaches a point at which it is accepted by the account team and leadership
> that a customer will contract or churn. **As Gainsight does not support a 'grey' color** (or any
> color outside of the standard green to red health scoring), the `will churn` lifecycle stage can be
> applied in 360º Attributes."

**A vendor tool's colour palette determined where a state lives in the model.** Its promotion also
requires four human steps including manager agreement (lines 72-77) — an accepted-loss state is
deliberately hard to enter. Both details are worth one line each: the first as a caution that tooling
shapes taxonomy, the second as good design (make giving up expensive).

---

## 5. What this does NOT support

- **It is enterprise CS in its purest form.** Gainsight, CSMs, Solution Architects, Account
  Executives, EBRs, Renewal Managers, MEDDPPICC, segment tiers, a VP of Customer Success in the
  escalation ladder. Almost none of the *machinery* transfers to the charter's solo/self-serve
  reader. What transfers is the **epistemics**: expiry on every signal, segmented thresholds,
  ignorance-as-risk, reason taxonomies with tie-breakers, and the separation of scoring from
  prediction. The pack should lift the epistemics and explicitly decline the machinery — this
  handbook is the best available exhibit of *both* halves of wedge 1.
- **No accuracy number of any kind appears.** Not for the health score, not for PTE/PTC (internal-only
  links), not for any measure. Consistent with worker 2's finding that no public artifact reports
  precision/recall/AUC for a health score (`_raw-gh-churn-health.md` §D) — **now confirmed at the
  most sophisticated public CS org, not just among 0-star toys.**
- **Not read this pass** (budget): `product-usage-data/maturity-scoring.md`,
  `platform-value-score.md`, `metrics-based-playbooks.md` (a likely-rich trio — GitLab's *other* two
  scores), `customer-onboarding/index.md`, `csm/qbr/`, `csm/ebr.md`, `csm/renewals/`,
  `csm/risk-mitigation/`, `csm/escalations/`, `csm/success-plans/`,
  `csm/engagement/non-engaged-customer-strategies.md`, `submitting-customer-feedback.md`,
  `reporting-and-dashboarding-framework.md`. Recorded as unread, **not** as absent.

## 6. Cross-references

- Sibling `content/handbook/support/` tree → worker 3, `_raw-gh-ai-support-kb.md` §D (deflection
  admission, docs-vs-KB framework, AI-usage policy, "escalate early").
- Dynatrace Maturity Score exhibit → `_raw-gh-voc-onboarding-csops.md` §8b.
- Health-score absence across open source → `_raw-gh-churn-health.md` §D.
- Cancel-flow reason taxonomy → `_raw-gh-voc-onboarding-csops.md` §6.

**FLAG TO D:** `internal.gitlab.com/handbook/sales/propensity_models/` (PTE/PTC methodology) is
internal-only and unverifiable from here. If GitLab has published anything about those models
externally — blog, talk, conference paper — that is the one thing that would let us say something
evidenced about an *enterprise* churn model's real accuracy. Worth a search.
