# Channel C · GitHub — report

Sub-orchestrator: channel C. Date: **2026-08-02**. Crew: 3 sonnet workers + lead slices.
All star counts, licence facts and commit states read live on 2026-08-02.

**Worker/lead raw files (every claim below traces to one of these):**

- [`_raw/_raw-gh-support-stacks.md`](_raw/_raw-gh-support-stacks.md) — worker 1: 7 deep schema reads + 10 licence verifications across open-source helpdesk/ITSM stacks.
- [`_raw/_raw-gh-churn-health.md`](_raw/_raw-gh-churn-health.md) — worker 2: churn-model corpus, survival/CLV libraries, health-score and NRR/GRR search.
- [`_raw/_raw-gh-ai-support-kb.md`](_raw/_raw-gh-ai-support-kb.md) — worker 3: τ-bench family, escalation code, KB/deflection tooling, support handbooks.
- [`_raw/_raw-gh-voc-onboarding-csops.md`](_raw/_raw-gh-voc-onboarding-csops.md) — lead: VoC/feedback boards, in-product onboarding, Parlant, cancel flows, the CS knowledge layer, absence sweeps.

Raw search dumps: `_raw/_scan-gh-1.json` … `_scan-gh-8.json` (each `=== header ===` names the command).

---

## Verdict first

**The niche is open, and this is the emptiest domain the family has surveyed.** GitHub has no
customer-success incumbent, no CS knowledge layer worth inheriting, and — for the pack's flagship
question — no validated health score anywhere in public code. What GitHub *does* have is unusually
good: a **strongly convergent support taxonomy** independently arrived at by systems built 30 years
apart, and a **primary-source evidence base for honest measurement** (a real vendor's production
health score whose arithmetic we can read, a benchmark that quantifies why single-shot success rates
lie, and a support org publicly admitting it cannot measure deflection).

Four load-bearing results:

1. **No incumbent, and the domain does not own its own vocabulary.** The single curated
   awesome-customer-success list has **24 stars** and every post-creation commit is a vendor adding
   its own product. `topic:churn` is dominated by *code*-churn tools and Monero laundering;
   `topic:retention` by *backup* retention. Compare marketing's 42.5k★ incumbent.
2. **The support taxonomy converges hard — 3 status buckets and 3 SLA metrics.** Frappe Helpdesk and
   libredesk *enforce* the 3-category constraint in schema; RT (1996) reached the same shape
   independently. Chatwoot (Ruby, 2019-era) and libredesk (Go, 2024-era) landed on near-identical
   SLA field names. This is the best convergent evidence available for a canonical taxonomy.
3. **Wedge hypothesis 2 (health scores are unvalidated folklore) is CONFIRMED from two independent
   directions** — a grep-verified absence across the whole open-source category, *and* a production
   vendor score we could read line by line that turns out to be an adoption checklist scored out of
   100 with no outcome variable anywhere.
4. **Wedge hypothesis 3 (AI-support policy is under-canonized) is CONFIRMED with a correction.**
   Deflection is genuinely unmeasured — confirmed by GitLab's own published admission. But the
   *policy* layer is not empty: **Parlant (18,225★, Apache-2.0)** is a mature framework for exactly
   the artifacts this pack produces, and nobody has named it as CS infrastructure.

**Licence landscape:** dominated by copyleft and open-core. AGPL is the default for support stacks
(Zammad, FreeScout, Frappe, libredesk, iTop) and for VoC tools (Fider, Formbricks, LogChimp). The
modern SaaS tier has converged on **open-core with an `ee/` carve-out**, which GitHub's API reports
as `NOASSERTION`. **The API was wrong or useless in at least 11 cases across this channel.** Since
we lift *structure and ideas*, not code, almost everything is usable with citation — but the
carve-outs matter for anything quoted verbatim.

---

## 1. The incumbent question: there isn't one

### 1.1 The topic terms are squatted

`gh search repos --topic churn --sort stars` (dump `_scan-gh-6.json`) returns, in rank order:
awesome-fraud-detection-papers (1822), **attractor (410, *code* churn/complexity)**, **code-complexity
(295, *code* churn)**, cognitive-code-analysis (52), then the first actual customer-churn repo at
**44 stars**, with two Monero-churning tools in the top seven. `--topic retention` is worse — the
top eight are all **backup retention policies** (cv4pve-autosnap 561, Butterfly-Backup 123, …); the
first customer-retention repo is `churnkey/sdk` at 20 stars.

### 1.2 The knowledge layer is a vendor directory the vendors edit

`keon/awesome-customer-success` — **24★**, CC0-1.0 (LICENSE opened), the only curated CS list on
GitHub. 202 lines, 19 sections, **exclusively commercial product links with marketing one-liners; no
method, no definition, no number anywhere**. Its commit log is the finding:

```
2026-07-31  Merge pull request #14 from pbbosshat/add-workforce-wave
2026-07-20  Merge pull request #12 from bwook00/patch-1        (adds Runbear)
2026-06-05  Merge pull request #6 from khushi-churnkey/patch-1 (adds Churnkey)
2026-05-22  Merge pull request #5 from nadyyym/add-beton-inspector
```

Every post-creation commit is a vendor adding its own product from a vendor-named account. The
better-structured alternative, `mutedblues/Customer-Success-Management` (39★), has **no licence file
at all** and has been dead since **2020-01-24**.

**This is charter rule 5 (vendor-density) confirmed at the infrastructure layer, not just in blogs.**

### 1.3 What a real CS team actually publishes

Three repos are published by a named vendor's CS team. Two are archived and turn out not to contain
CS methodology at all: `prefect-archive/prefect-recipes` (260★, Apache-2.0, archived 2025) is Prefect
*usage* recipes; `puppetlabs/best-practices` (119★, Apache-2.0, archived 2023) is Puppet
*configuration* best practice. Only `dynatrace-oss/CustomerSuccess` (35★, Apache-2.0, alive) contains
real CS artifacts — and they are dashboards (§4.2).

**Teachable:** what a dev-tools CS team ships publicly is *enablement content*, not process. The
methodology stays internal. That is a fact about the job worth stating in the pack.

### 1.4 Skill-pack repos — FLAG TO CHANNEL A

Sixteen agent-skill repos surfaced across channel C's sweeps. Highlights, with the signal for A:
`gtmagents/gtm-agents` (360★), `zapier/gtm-cheat-codes` (316★), `w95/awesome-claude-corporate-skills`
(132★), `t0ddc3by/claude-for-customer-success` (58★), `LeadMagic/gtm-skills` (33★),
`citizenjosh/customer-success-skills` (11★), `stephenrogan/augmented-csm` (3★, "38 agent skills for
the complete CSM operational surface area"), plus `alphaparkinc/genpark-*` ticket-router /
onboarding / dispute skills. Worker 2 additionally surfaced `majiayu000/claude-skill-registry` (530★),
`borghei/Claude-Skills` (441★), `nimrodfisher/data-analytics-skills` (337★).

**The CS-specific skill layer tops out around 58★**; everything larger is GTM/sales-adjacent or a
generic corporate bundle. Full tables in `_raw-gh-voc-onboarding-csops.md` §7 and
`_raw-gh-churn-health.md` §D.

---

## 2. The convergent support taxonomy (worker 1)

This is the channel's most directly usable content: **independent implementations spanning 1996 to
2026 converge on the same shape**, and two of them enforce it in the schema rather than the docs.

### 2.1 Three status buckets under customizable labels

| stack | mechanism | source |
|---|---|---|
| RT (1996) | `initial` / `active` / `inactive` — named *sets* of literal statuses, plus a transition graph | `bestpractical/rt@stable:etc/RT_Config.pm.in:5406-5560` |
| Zammad | `state_type` CATEGORIES collapse to open / pending / closed | `zammad/zammad@develop:app/models/ticket/state_type.rb:14-28` |
| Frappe Helpdesk | every custom status **must** declare `category` ∈ `Open / Paused / Resolved` | `frappe/helpdesk@develop:.../hd_ticket_status.json` |
| libredesk | `CREATE TYPE conversation_status_category AS ENUM ('open','waiting','resolved')` | `abhinavxd/libredesk@main:schema.sql:26` |

**Canonical shape: something-to-do / something-paused-on-someone-else / something-finished.**
Frappe and libredesk *constrain* admin-defined status names to one of three machine-meaningful
categories — the cleanest available argument that the 3-bucket taxonomy is real and not fashion.

**Frappe's `label_agent` + `label_customer`** as separate fields on the same status is the single
best small idea in the sample: *the same underlying state can be named differently to the agent and
to the customer*. That is a success-pack teaching point about customer-facing language, sourced to a
schema.

**Divergences worth teaching, not smoothing over:**
- Is *resolved* distinct from *closed*? Chatwoot, Zammad, django-helpdesk, libredesk say yes;
  FreeScout says no (closing is terminal).
- How many flavours of "pending"? Zammad has **two** — `pending reminder` (an agent's personal
  snooze) vs `pending action` (genuinely waiting on someone external). Most stacks collapse these.
  **django-helpdesk ships with none by default.**
- django-helpdesk is the only stack enforcing an explicit **transition adjacency table** in code
  (`src/helpdesk/settings.py:148-199`); RT additionally gates individual transitions on distinct
  permissions (`'* -> deleted' => 'DeleteTicket'`).

### 2.2 Three SLA metrics, independently converged

```ruby
# chatwoot/chatwoot@bc7ae88:db/schema.rb:1374-1385  (Ruby, 2019-era)
t.float "first_response_time_threshold"
t.float "next_response_time_threshold"
t.float "resolution_time_threshold"
t.boolean "only_during_business_hours", default: false
```
```sql
-- abhinavxd/libredesk@main:schema.sql:19-22  (Go, 2024-era)
CREATE TYPE "sla_metric" AS ENUM ('first_response', 'resolution', 'next_response');
```

Two codebases, different languages, different decades, **near-identical field names**. Zammad is the
interesting exception with four timers and a model validation that **forbids setting two of them at
once**:

```ruby
# zammad/zammad@develop:app/models/sla.rb:17-20,38-42
def cannot_have_response_and_update
  return if response_time.blank? || update_time.blank?
  errors.add :base, 'Cannot have both response time and update time.'
end
```

### 2.3 The clock stops while waiting on the customer — universally

Every stack that models SLA at all pauses accounting during a customer-wait state, and the pack
should state this as settled design rather than a choice:

- **Frappe** makes it a first-class SLA state: `agreement_status ∈ First Response Due / Resolution
  Due / Failed / Fulfilled / **Paused**`, with `on_hold_since` and `total_hold_time` as the accounting
  fields, and `first_response_failed_by` / `resolution_failed_by` **Duration** fields that quantify
  *how badly* a breach missed, not just that it did.
- **Zammad** puts a `pending_time` column directly on the ticket row (the pause-until instant).
- **libredesk** adds `applied_sla_status ∈ ('pending','breached','met','partially_met')` — the
  `partially_met` value (met first-response, breached resolution) exists nowhere else — and schedules
  a typed **pre-breach warning** (`sla_notification_type ENUM ('warning','breach')`) as distinct from
  the breach.

### 2.4 Priority: one field, except in ITSM

Pure support tools use a single ordinal priority (Chatwoot 4-level, Frappe 4-level, django-helpdesk
5-level, libredesk *free-text with no fixed levels at all*). **GLPI alone implements the ITIL
impact × urgency matrix:**

```php
// glpi-project/glpi@11.0/bugfixes:src/CommonITILObject.php:3329-3333
public static function computePriority($urgency, $impact) {
    return $CFG_GLPI[static::MATRIX_FIELD][$urgency][$impact] ?? (int) round(($urgency + $impact) / 2);
}
```

GLPI also carries 8 live statuses vs a helpdesk's 4-6, because ITSM must model `PLANNED` and
`APPROVAL` — process states that don't exist in customer support. **Teachable: ITSM taxonomy ⊃
support taxonomy; the 5×5 matrix is over-engineering for anyone not doing formal ITSM, and the honest
default is a single field.** This matters directly for the charter's solo/self-serve reader.

### 2.5 The escalation-paths artifact, ready-made

Chatwoot's automation-rule vocabulary is the most quotable template found for the pack's
"escalation paths" deliverable (`chatwoot/chatwoot@bc7ae88:app/models/automation_rule.rb:35-42`):

```ruby
conditions_attributes = %w[content email country_code status message_type browser_language
  assignee_id team_id referer city company_name inbox_id mail_subject phone_number priority
  conversation_language labels private_note]
actions_attributes = %w[send_message add_label remove_label send_email_to_team assign_team
  assign_agent remove_assigned_agent remove_assigned_team send_webhook_event mute_conversation
  send_attachment change_status resolve_conversation open_conversation pending_conversation
  snooze_conversation change_priority send_email_transcript add_private_note]
```

**Naming collision the pack must resolve:** "escalation" means two incompatible things in this
corpus. django-helpdesk implements escalation as an **automatic priority bump** after N days
(`Queue.escalate_days`); everyone else means **SLA-breach notify-and-reassign**. And per §5.3, the
open-source world at large uses "escalation policy" to mean **on-call paging**. Three meanings, one
word.

### 2.6 Process knowledge is not in the repos

Worker 1 checked and found **no repo in the sample carries in-repo prose teaching support process**
(as opposed to installation). Zammad's `doc/` is a developer manual; Chatwoot's docs are off-GitHub.
**The schema *is* the process documentation** — what fields exist encodes what the designers thought
mattered. That is why this channel's contribution is taxonomy rather than practice.

**Monetization boundary worth naming:** FreeScout's OSS core deliberately ships **no priority field,
no SLA model, and no automation engine** (`Modules/` contains only `.gitkeep`) — those are paid
modules. A concrete data point on what open-source support tools omit and sell.

---

## 3. Churn: what honestly predicts, and at what quality (worker 2 + lead)

### 3.1 The open-source churn canon is two B2C telecom datasets

Worker 2 quantified it: `gh api search/code -f q="WA_Fn-UseC_-Telco-Customer-Churn"` returns
**3,176 code files**; a 100-hit sample contained **96 distinct repositories**. Every repo in the
top-30-by-stars for "customer churn prediction" is a telecom project; **zero are B2B SaaS or
subscription-product churn.**

There are **two** canonical datasets, not one — IBM Telco (7,043 rows, ~26.5% churn) and the
Orange/bigml set (3,333 rows, 14.49% churn, used by `awslabs/aws-customer-churn-pipeline`).

### 3.2 The honest ceiling, from three independent implementations

| repo | method | result |
|---|---|---|
| `archd3sai/…@master:"Churn Prediction Model.ipynb"` cell 40 | stratified split before any resampling, GridSearchCV on train only | **accuracy 0.788, churn-class F1 0.62, AUC 0.848** on 1,409 held-out rows |
| `Pradnya1208/…@main:Scripts/"Customer churn prediction.ipynb"` cells 62, 76 | stratified, 10-fold CV | CV ROC-AUC **84.93%**; final Adaboost accuracy 0.812, precision 0.688, **recall 0.538**, F1 0.604 |
| `pik1989/MLProject-ChurnPrediction@main:"Churn Analysis - Model Building.ipynb"` cells 8-14 | honest baseline before the error | accuracy 0.78, churn-class recall 0.49 |

**Convergent honest ceiling: accuracy ≈ 78-81%, churn-class F1 ≈ 0.60-0.62, recall ≈ 50-66%,
AUC ≈ 0.83-0.85.**

### 3.3 The two ways the number gets inflated — both caught in primary sources

**(a) Resampling before the split.** `pik1989/MLProject-ChurnPrediction` (158★, linked from the
author's tutorial videos) applies `SMOTEENN().fit_sample(x, y)` to the **full dataset at cell 16**,
then splits at cell 17, and reports **0.9344 accuracy** at cell 19 as the improvement. The test set is
no longer at the real base rate and may contain synthetic points never held out. **93-94% is a
specific, identifiable coding error being taught as a technique.**

**(b) Accuracy without a base rate.** Lead exhibit: `ReverendBayes/Telecom-Churn-Predictor` (MIT)
headlines **"94.60% Accuracy | … | 0.7423 Recall"**. Counting its own shipped CSV:

```
rows: 3333   Counter({'False': 2850, 'True': 483})   → churn base rate 14.49%
majority-class baseline accuracy = 2850/3333 = 85.51%
```

**A model predicting "nobody churns" scores 85.51%.** The advertised figure is +9.09pp over doing
nothing, and the number that matters — it misses **25.8% of churners** — is listed fourth. The method
is defensible; the *headline ordering* is not.

**Never-ship figure class, found in the wild** (same README): *"Charter Communications… was previously
relying on a spaCy-based model that achieved only ~40% accuracy."* Unverifiable, about a named public
company, and internally impossible (40% is below both the 85.51% do-nothing baseline and a coin
flip). Per charter, flag the **class**: *"our model beats the old one" comparisons where the old
number is unsourced and nonsensical.*

### 3.4 Censoring — the error the whole tutorial corpus makes

`CamDavidsonPilon/lifelines@master:docs/"Survival Analysis intro.rst"`:

> "A common mistake data analysts make is choosing to ignore the right-censored individuals… if we
> instead simply took the mean of *all* lifespans, including the current lifespans of right-censored
> instances, we would *still* be underestimating the true average lifespan."

Scale, from a Cox fit on the canonical dataset
(`archd3sai/…:"Customers Survival Analysis.ipynb"` cell 59):
`<lifelines.CoxPHFitter: fitted with 7043 observations, **5174 censored**>` — **73.5% of the dataset
is customers who have not churned *yet*.** Labelling them "will not churn" is the single most
violated assumption in naive churn classification.

**The calibration sentence** — the most useful line channel C found for the pack
(`lifelines@master:docs/"Survival Regression.rst":1166-1178`):

> "Fitted survival models typically have a concordance index between **0.55 and 0.75** (this may seem
> bad, but even a perfect model has a lot of noise that can make a high score impossible)."

And it immediately catches a bad number: the same archd3sai Cox fit reports **concordance 0.93**,
because it includes `TotalCharges`, which is ≈ `tenure × MonthlyCharges` — a covariate encoding the
duration being predicted. The honest comparison, `awslabs/aws-customer-churn-pipeline@main:notebook/
coxph/"Example_Churn_Surv.ipynb"` cell 40, uses censoring-adjusted **IPCW concordance = 0.7515** —
squarely inside lifelines' stated range.

**Also note** `ragulpr/wtte-rnn` (774★, MIT) — the **most-starred churn-prediction repo on GitHub** —
is a Weibull *time-to-event* framing, not a classifier.

### 3.5 Contractual vs non-contractual — the under-taught distinction, in docstrings

`pymc-labs/pymc-marketing` (Apache-2.0) encodes the taxonomy structurally:

- `pymc_marketing/clv/models/beta_geo.py:14` — *"BG/NBD model for a **non-contractual** customer
  population across continuous time."*
- `pymc_marketing/clv/models/shifted_beta_geo.py:34` — *"Shifted Beta Geometric (sBG) model for
  **customers renewing contracts** over discrete time periods."*

with a citation to Fader & Hardie (2010), *"Customer-Base Valuation in a **Contractual Setting: The
Perils of Ignoring Heterogeneity**"*. **The B2B-SaaS case is the contractual/sBG one**, and most
churn tooling a reader will find is built for the non-contractual case. Also
`jdmaturen/shifted_beta_geometric_py` (62★, Apache-2.0) — a standalone sBG implementation.
Charter clause (e): the Apache licence covers the code, **not** Fader & Hardie's model.

**Honest absence:** no CLV repo examined ships a backtested "predicted vs realized LTV" accuracy
number. The field's honesty shows up as documented assumptions and executed assumption-checks (the
pymc-marketing quickstart computes the Gamma-Gamma frequency/value correlation before fitting), not
as validated accuracy claims.

### 3.6 The B2C→B2B generalization gap

Recurring "predictive features" across the corpus are contract type (`Contract_Two year` coef −3.70,
exp(coef) 0.02), tenure, payment method, internet-service type, monthly/total charges. Worker 2's
judgement, which the report endorses: **these are the columns the dataset *has*, not independently
rediscovered universal churn drivers.** Contract length plausibly transfers to SaaS; "mailed check vs
autopay" is a B2C tech-savviness proxy with no SaaS analogue; "Fiber optic" has none at all.
**No repo examined even discusses the transfer question** — every one trains and evaluates Telco→Telco.

---

## 4. Health scores: wedge hypothesis 2 CONFIRMED, from three directions

*(A third direction landed after this section was written: **§7c**, GitLab's public CS handbook —
the enterprise canon's own health score, which lists backtesting as an unmet goal, lets one manual
field override the weighted model, and keeps churn prediction as a **separate** artifact. Read §4 and
§7c together: §4 is the open-source absence, §7c is the top of the market saying the same thing.)*

### 4.1 The category is unbuilt in public (worker 2, grep-verified)

- `gh search repos "customer health score" --limit 20` → 20 results, **19 of 20 have 0-1 stars**;
  none exceeds 1 star.
- `gh search repos "customer success health score" --sort stars` → 3 results, all 0 stars.
- `gh search repos "churn health score dashboard"` → **0 results.**
- No RFM-segmentation repo scoped to B2B/SaaS retention — all are e-commerce/retail.
- **No repo anywhere reports precision, recall or AUC for a health score against actual subsequent
  churn, renewal or expansion.** Contrast §3, where churn-classifier accuracy claims are everywhere.

The two most substantive artifacts, read in full:

- **`jwinternheimer/customer-health-score@master:generate_scores.R`** (0★, apparently a copy of a real
  Buffer internal script). Not a weighted composite — a per-customer logistic trend test
  `glm(cbind(update_count, update_total) ~ year, family="binomial")`, flagging `at_risk` when
  `estimate <= -5 && p.value <= 0.05`. Statistically framed, but **`-5` is an uncommented magic
  number and nothing ever checks whether flagged customers subsequently churned.**
- **`twentic/twentic_customer_health_score@main:.../res_partner.py`** — the textbook toy:
  `rfm_score = (0.6 * recency_score) + (0.4 * monetary_score)`, thresholds `SCORE_AT_RISK = 40.0`,
  `SCORE_HEALTHY = 70.0`, `MIN_INVOICES = 3`. **It calls itself RFM but never scores Frequency** —
  frequency only normalizes the recency decay. `MIN_INVOICES` is commented "so that the metric is
  statistically meaningful" while no statistic is computed anywhere in the file.

### 4.2 A production vendor health score, arithmetic and all (lead)

The strongest exhibit, because it is neither a toy nor a blog: `dynatrace-oss/CustomerSuccess`
(Apache-2.0, alive), `Platform Adoption/Dynatrace Platform Adoption v1.4.0.json`, tile `Maturity Score`:

```
| fieldsAdd userPts = if(uniqueUsers >= 10, then:25, else:uniqueUsers * 2 + 5)
| fieldsAdd appPts  = if(totalApps  >= 5,   then:25, else:totalApps * 5)
| fieldsAdd apiPts  = if(apiCalls   > 100,  then:25, else:if(apiCalls > 0, then:15, else:0))
| fieldsAdd aiPts   = if(aiCalls    > 50,   then:25, else:if(aiCalls  > 0, then:12, else:0))
| fieldsAdd maturityScore = userPts + appPts + apiPts + aiPts
```

Four equally-weighted 25-point components; every threshold a round hand-picked number; **no outcome
variable anywhere** — nothing is fitted or calibrated against renewal, churn, or support load,
because no outcome is joined. And **every component is something the vendor wants more of**, as its
companion tile's generated advice makes explicit:

```
appAction = concat("Need ", toString(5 - totalApps), " more apps  - drive Notebooks, Workflows, Problems")
aiAction  = if(aiCalls==0, then:"No AI usage detected  - enable Davis Copilot and Analyzers", …)
```

**This is a product-adoption checklist rendered as a number, and the things it rewards are the
vendor's own expansion surface.** A reasonable enablement prompt; a completely unvalidated risk
predictor. The 100-point framing is what invites the confusion.

**The redeeming half, and the pack's honest reframe:** the score always ships paired with
`Maturity Score - Gaps & Actions`. **A score that always arrives with the specific gap and the
specific action is a prioritisation device; the same number alone on a dashboard next to a renewal
date is folklore.** Both halves are in this one file — it can teach the rule and the exception at once.

### 4.3 "At risk" is pure login recency — and at the wrong grain

Same file, `User Lifecycle Cohorts`:

```
| fieldsAdd cohort = if(daysSinceFirstSeen <= 7,  then:"1-New",
                   else:if(daysSinceLastSeen <= 3,  then:"2-Active",
                   else:if(daysSinceLastSeen <= 14, then:"3-At Risk", else:"4-Churned")))
```

**"At risk" = hasn't logged in for 3-14 days. "Churned" = 14+ days.** No revenue, no contract, no
support history. Two caveats the pack should state:

- These are **user**-level cohorts. A churned user is not a churned account (§5.2). Naive rollup
  mislabels healthy accounts with rotating staff.
- The 3d/14d thresholds are unexplained and product-specific. **A recency threshold copied across
  products is the most common way a health signal becomes noise.**

### 4.4 The one clean positive: NRR/GRR done correctly

`0x416d6972/pypulate@main:src/pypulate/kpi/business_kpi.py` (13★, MIT; LICENSE and `pyproject.toml`
agree) implements both to textbook standard: anchored to a **period-start** revenue base, **excluding
new-logo revenue entirely** (neither function accepts a new-business parameter), GRR excluding
expansion while NRR includes it. Minor honesty note: the docstring claims GRR "is capped at 100%"
but the code does not clip — true by construction only for non-negative inputs, which are not validated.

---

## 5. AI support and escalation policy: wedge 3 CONFIRMED, with a correction

### 5.1 pass^k — the mechanism that rebuts every vendor resolution-rate claim

Worker 3 did not trust the README table (frozen at 2024 models, with literal `??` cells) and computed
pass^k from the per-trial JSON in `sierra-research/tau2-bench@main:data/tau2/results/final/*.json`
(commit `c30d59aa…`, `num_trials=4`) using the unbiased estimator C(c,k)/C(n,k):

| agent model | domain | n | pass^1 | pass^2 | pass^3 | pass^4 |
|---|---|---:|---:|---:|---:|---:|
| claude-3-7-sonnet-20250219 | retail | 114 | 0.787 | 0.693 | 0.634 | **0.596** |
| gpt-4.1-2025-04-14 | retail | 114 | 0.741 | 0.642 | 0.579 | **0.526** |
| claude-3-7-sonnet-20250219 | telecom | 114 | 0.493 | 0.374 | 0.307 | **0.254** |
| gpt-4.1-2025-04-14 | telecom | 114 | 0.342 | 0.259 | 0.219 | **0.193** |

**Cite the mechanism, never these numbers.** Single-shot success looks decent; reliability across
repeated attempts on the same policy is substantially worse — retail drops 15-27 relative points by
k=4, telecom falls to 19-25%. **pass^k exists precisely to expose that a single-shot resolution rate
overstates reliability**, which is the canonical rebuttal to any "our AI resolves X% of tickets"
claim that discloses neither n nor k.

**The benchmark's own numbers are provably unstable**: `tau2-bench@main:README.md` warns that a July
2026 v1.0.1 grading update means "results produced with tau2-bench < 1.0.1 are not comparable with
>= 1.0.1", and the companion SABER paper documents **75+ task fixes** to the original airline/retail/
telecom tasks for "incorrect expected actions… impossible constraints… missing fallback behaviors."
**A support-agent benchmark number from 2024-25 is stale by the vendor's own admission.** Anti-staleness
applies here exactly as it did in the ai pack.

### 5.2 Escalation triggers, enumerated from real code — and none is a confidence threshold

The clearest formal statement, from the benchmark's own policy document
(`sierra-research/tau-bench@main:tau_bench/envs/retail/wiki.md`, echoed at
`tau2-bench@main:data/tau2/domains/telecom/main_policy.md:13`):

> "You should transfer the user to a human agent **if and only if** the request cannot be handled
> within the scope of your actions."

That is **scope-boundary escalation**, not confidence-threshold escalation. The full cross-repo
enumeration (worker 3):

1. **Scope boundary** — out of tool/domain capability (τ-bench policy docs).
2. **Explicit user request, or consent to an offered handoff** — the dominant pattern in the two most
   sophisticated implementations. Chatwoot Captain's prompt lists five conditions that may *offer*
   handoff but fires the tool "only after the user explicitly requests… accepts… or a Guardrail…
   requires transfer."
3. **Admin-authored guardrail overrides the consent default** (Chatwoot).
4. **Time-of-day** — `huabeitech/agent-desk` auto-hands off outside business hours with **no**
   confirmation; inside business hours it requires explicit double-confirmation
   (`internal/ai/runtime/graphs/handoff_graph.go`, `hitl.go`).
5. **Repeated failure** — named in Chatwoot's prompt as a reason to *offer*, not to auto-fire.
6. **Pure intent classification** — Rasa's `human_handoff` intent, no other signal.
7. **An LLM triage classifier as a recommendation layer** — agent-desk's `RecommendedNextAction ∈
   {continue_answering, handoff_to_human, prepare_ticket}`, still gated downstream by consent.
8. **Structural pre-gate** — agent-desk's `reply_eligibility.go`: the bot may not speak at all if a
   human is assigned or `ServiceMode=HumanOnly`, plus a **deterministic staged-rollout gate**
   (SHA-256 of `channel;conversation;agent` bucketed 0-99 against `RolloutPercent`), pinning a
   conversation inside or outside the AI rollout for its whole lifetime.

**The load-bearing negative:** *none* of these uses a numeric model-confidence threshold. Every real
trigger is symbolic (intent match, scope check, time-of-day, rollout bucket) or another LLM's
categorical output. **"Escalate when confidence is low" is folklore-shorthand; the pack should say so
and teach the symbolic triggers instead.**

**A ninth trigger pattern was added after this section was written — see §7b.1.** Anthropic's own
reference agent makes the escalation decision a **required typed field** (`redirect_to_agent:
{should_redirect, reason}`) emitted every turn, with three symbolic triggers (no relevant information
/ out of scope / user explicitly asks). It **independently confirms this negative** — no confidence
float — and adds the auditability property none of the eight above have.

Two honest limitations worth carrying: Chatwoot's `HandoffTool` has commented-out "future
enhancement" fields for `team_id`, `priority`, `escalation_level (L1/L2/L3)` — **even Chatwoot has not
built tier-aware routing into Captain**, only a flat handoff primitive. And Rasa's reference bot can
only *simulate* handoff without an externally wired live-agent system.

### 5.3 Two different objects called "escalation"

GitLab's handbook states a support-**org** escalation philosophy that has nothing to do with bot
handoff (`content/handbook/support/support/_index.md`):

> "Escalate early. Visibility across GitLab, up to and including the CEO, is always better earlier
> rather than later."

That is *upward, organizational, for visibility* — not a tiered ladder and not a conversation
transfer. Combined with §2.5's priority-bump-vs-notify split and the SRE paging meaning that owns the
phrase in open source (§6.2), **the pack should name these as distinct objects rather than inherit
one word for all of them.**

### 5.4 Parlant — the AI-support-policy framework nobody has named (lead)

`emcie-co/parlant` — **18,225★**, Apache-2.0 (**LICENSE and `pyproject.toml` agree — the only repo in
the lead slice where they did**), pushed 2026-07-12, topics include `customer-service` **and**
`customer-success`. Self-positioned as *"an open-source alternative to Ada, Decagon, or Sierra"*.

Its primitives are exactly the artifacts this pack produces, which is why it sits on the ai↔success
seam rather than inside ai:

- **Guidelines** — behavioural rules as condition-action pairs, matched per turn.
- **Relationships** — dependency and **exclusion** edges: `await for_beginners.exclude(for_experts)`.
  A support policy needs conflict resolution, and here it is a first-class edge, not prose ordering.
- **Journeys** — *"Multi-turn SOPs… The agent follows the flow but adapts — it can fast-forward
  states, revisit earlier ones."* A playbook as a state machine that may be entered out of order.
- **Canned Responses** — *"Pre-approved response templates that eliminate hallucination at critical
  moments."*
- **Explainability** — OpenTelemetry tracing of every guideline match.

**The bot-boundary mechanism, in its own engine diagram:** after tool-calling the flow branches
`-->|Fluid Output Mode?| D["Generated Message"]` versus `-->|Strict Output Mode?| E["Canned Message"]`.
**Two output modes: compose freely, or emit only pre-approved text.** This is the cleanest statement
in code of the question success owns — *at which moments may the bot compose, and at which must it
only select?* Refunds, cancellations, compliance statements and outage acknowledgements are the
obvious strict moments.

**Grade its evidence carefully.** Parlant's reliability support is an arXiv citation plus named
testimonials (Slice Bank, JPMorgan Chase) and the unsourced line *"deployed in production at the most
stringent organizations, including banks."* Testimonials are not measurement — practitioner-report
grade, and do not repeat the banks claim as fact.

### 5.5 The account/user duality (lead)

`usertour/usertour@HEAD:apps/server/prisma/schema.prisma` models the B2B fact most health scores get
wrong — an explicit membership edge carrying **its own attribute bag**:

```prisma
model BizUserOnCompany { bizCompanyId String; bizUserId String; data Json @db.JsonB
                         @@unique([bizCompanyId, bizUserId]) }
model Segment { bizType Int @default(1); source String? @default("internal"); sourceId String? }
model BizUserOnSegment { … }   model BizCompanyOnSegment { … }
```

Segments target **either** users or companies. **Health, adoption and risk are account-level questions
answered from user-level events, and the rollup needs a real membership edge** — cf. §4.3, where
Dynatrace's cohorts are user-level.

`BizSession` additionally pins onboarding analytics to the **flow version actually shown**
(`versionId`, alongside `progress` and `currentStepId`): change your onboarding and pre/post
completion rates are not comparable unless you segment by version. Enforced in schema, not discipline.

---

## 6. Deflection and VoC measurement

### 6.1 Deflection is not measured — primary-source confirmation

The strongest evidence is an admission, not an absence.
`gitlab-com/content-sites/handbook@:content/handbook/support/knowledge-base/reporting-and-metrics.md`
lists "Ticket Deflection" and "First contact resolution (did customers find what they need without
having to open support)" as metrics they *want*, then states:

> "We are currently working with our metrics team members to build a Dashboard for KCS and Knowledge
> Management. **This is a work in progress.**"

**A company with one of the most extensive public support handbooks on the internet, naming ticket
deflection as a KPI, does not have it instrumented.** Worker 3 additionally searched
`deflection_rate` / `deflection rate` / `deflection` across GitHub code and markdown and found no
on-topic tooling.

**Pack default: "we do not have deflection measurement" is the honest position, and any vendor
deflection percentage is a marketing claim absent a disclosed method.**

What *does* exist is narrower than it looks: `squidfunk/mkdocs-material`'s "Was this page helpful?"
widget ships the UI but not the recording — one GA4 event per page view, with the maintainer's own
docs flagging that **GA4 has no feature to compute an average page rating**, that reporting lags 24h+,
and that **the widget is not shown at all to users who decline the analytics cookie** (a selection bias
baked in by design). It cannot join "read the article" to "did not file a ticket"; it is a proxy for
perceived helpfulness.

Also worth citing: `dotnet/eShopSupport@main:test/EvaluationTests/AnswerScoringEvaluator.cs` — a clean
LLM-as-judge rubric (1-5 scoreLabel, fixed schema, "no penalty for giving extra on-topic information…
Only penalize for missing necessary facts or being misleading"). Useful as a *contrast*: this is what
a method-transparent quality eval looks like, **and it still tells you nothing about whether ticket
volume fell.**

### 6.2 Absence sweeps (lead, grep-verified)

- `gh search repos "quarterly business review"` → top result **1 star** (a joke repo); everything else
  0 stars. **QBR tooling does not exist.** The nearest real artifact is Dynatrace's Tenant Review
  dashboard — i.e. at a mature vendor, a QBR *is* a product-telemetry review.
- `gh search repos "customer playbook automation"` → **zero results.** Playbooks-as-code for CS does
  not exist as open source.
- `gh search repos "escalation policy"` → **every first-page result is on-call/incident paging**
  (PagerDuty, VictorOps, GoAlert, Terraform providers); top result 32★. The support meaning has no
  code representation outside helpdesk automation engines and Parlant.
- `gh search repos --topic voice-of-customer` → top 216★, then a cliff; **nearly every entry created
  or last touched in 2026 and LLM/agent-shaped.** VoC as a tooling category is months old and entirely
  AI-native — there is no established open-source VoC stack to inherit.

### 6.3 The VoC structures that *are* worth lifting

**Formbricks models impressions, so response rate has a denominator**
(`formbricks/formbricks@HEAD:packages/database/schema/main.prisma`): `Display` = the survey was shown;
`Response` = someone answered; `Display.response` is **optional**. A `Display` with `response: null`
is a shown-and-ignored event recorded as first-class data. **You cannot state a response rate unless
you record impressions, and NPS computed only over responders is a self-selected sample.** The same
model carries the fatigue controls as fields: `displayOption ∈ (displayOnce|displayMultiple|
displaySome|respondMultiple)`, `recontactDays`, `displayLimit`, `displayPercentage`, `delay`, plus
`SurveyQuota.countPartialSubmissions`.

**Fider's feedback-board taxonomy** (`getfider/fider@HEAD:app/models/enum/post_status.go`):
`open / started / planned / completed / declined / duplicate / deleted` — with **`declined` and
`duplicate` first-class**, the two dispositions most often left implicit and most damaging to trust
when they are. Terminal states stop accruing demand while in-flight ones do not:

```go
func (i *Post) CanBeVoted() bool {
	return i.Status != enum.PostCompleted && i.Status != enum.PostDeclined && i.Status != enum.PostDuplicate
}
```

`PostResponse{Text, RespondedAt, User, Original}` is the closing-the-loop artifact: **status + written
response + (for duplicates) a pointer to the original.**

**The churn-save flow** (`churnkey/sdk@HEAD:README.md`, MIT): cancellation **reason → matched offer**,
where the offer type is a function of the reason — price → discount, low usage → pause, **missing
feature → no offer, just capture** — then free-text feedback, then an unobstructed confirm. Three
steps, three jobs: diagnose, attempt save, exit cleanly. The reason with no offer is the honest part.
The survey step is simultaneously the **exit-interview**, the highest-signal VoC moment a self-serve
product gets.

### 6.4 Knowledge-base vs documentation — a usable framework

`…/handbook/support/knowledge-base/docs-vs-kb.md`: Knowledge Articles are **reactive**,
ticket-triggered, about a specific broken-in-this-config problem; Documentation is **proactive**,
feature-complete, about intended behaviour. *"When in doubt, create a knowledge article… it can always
be promoted to documentation."* Non-vendor-marketing and directly useful for the KB-strategy job —
cite GitLab, do not claim it as MIT prose (§7).

---

## 7. Licence landscape

**Verdicts live in the raw files** — `_raw-gh-support-stacks.md` (17 repos), `_raw-gh-churn-health.md`
(23), `_raw-gh-ai-support-kb.md` (13), `_raw-gh-voc-onboarding-csops.md` (12). Summary of what matters:

**The API was wrong or useless in at least 11 cases this channel.** Concrete instances:

| repo | API said | LICENSE file actually says |
|---|---|---|
| `polonel/trudesk` | NOASSERTION | clean **Apache-2.0** — worker 1's clearest API-lied case |
| `chatwoot/chatwoot` | NOASSERTION | clean root **MIT** + a separate `enterprise/LICENSE` |
| `facebookincubator/LTVision` | "other" | standard **BSD-3-clause** Meta text |
| `formbricks/formbricks` | NOASSERTION | AGPLv3 + MIT SDK dirs + **commercial EE** dir |
| `usertour/usertour` | NOASSERTION | MIT-Expat **except** ee dirs *and any code controlling feature/permission/role/plan enablement* |
| `logchimp/logchimp`, `laudspeaker/laudspeaker` | NOASSERTION | AGPLv3 + `ee/` carve-outs |
| `Peppermint-Lab/peppermint` | NOASSERTION | AGPLv3 + a **self-referential, internally circular** commercial clause |
| `chaskiq/chaskiq` | NOASSERTION | **AGPL-3.0 + Commons Clause** (source-available, not OSS) |

**Manifest contradictions (charter clause b) fired twice.** `usertour/usertour@HEAD:package.json`
declares a flat `"license": "MIT"` while its LICENSE file carves out enterprise dirs *and* any
plan-enablement code — a reader trusting the API (`NOASSERTION`) or the manifest (`MIT`) is wrong in
opposite directions. `twentic/twentic_customer_health_score` declares `'license': 'LGPL-3'` in
`__manifest__.py` with a null API field and no LICENSE file.

**A licence that self-contradicts:** `laudspeaker/laudspeaker@HEAD:LICENSE` opens `MIT License /
Copyright (c) 2022` and then states content outside `ee/` "is available under the AGPLv3 license as
defined below", with AGPLv3 following. **AMBIGUOUS** — the GeoLift-class defect the charter warns of.

**Thin-licence-on-thick-IP (clause e) fired three times, and one is important.** The GitLab handbook's
root `LICENSE` scopes itself to *"the GitLab Software"* — the Hugo site code, **not the handbook
prose** — and worker 3 found no CC BY-SA notice in-repo despite GitLab's historical public claim.
**Do not treat the handbook prose as MIT; cite and link it.** Also: `theofilos/BTYD` has no licence
file and would not license Fader/Hardie/Lee's framework if it did; τ-bench's MIT covers the files, not
the pass^k methodology or SABER's error taxonomy — cite Yao et al. 2024, Barres et al. 2025, Cuadron
et al. 2026.

**Aliveness (clause d) matters here more than usual.** `astuto/astuto` (2,352★) is **archived**
(last push 2026-01-09) yet still ranks third in `topic:feedback`. `Peppermint-Lab/peppermint` (3,157★)
is **archived**. `loft-br/xgboost-survival-embeddings` is archived. `helpyio/helpy` (2,482★, MIT) has
been dead since **2023-03-08**; `opensupports` since 2024-04-22; `havakv/pycox` since 2024;
`jaredleekatzman/DeepSurv` since 2020 — all with `archived:false`.

**Blocking copylefts for anything beyond citation:** `sebp/scikit-survival` is **GPL-3.0-or-later**
(COPYING and `pyproject.toml` agree) → CITE-ONLY. `chaskiq` carries Commons Clause → CITE-ONLY.
Chatwoot's `enterprise/` (where all of Captain's handoff logic lives) is subscription-gated →
describe the pattern, never copy the code or prompt text.

**A correction that was itself wrong — withdrawn 2026-08-02.** Worker 1's licence table carried a note
claiming the lead's pre-scan listed `glpi-project/glpi` as `gpl-2.0` and was therefore stale. **It did
not, and it was not.** Verified three ways: `_scan-gh-1.json` records `glpi-project/glpi -> gpl-3.0`;
the live API returns `GPL-3.0`; `glpi-project/glpi@main:LICENSE` reads "Version 3, 29 June 2007". The
`gpl-2.0` value belongs to **`bestpractical/rt`**, a neighbouring row — which worker 1 independently
and correctly verified as GPL-2.0 from `COPYING`. Two rows were conflated. A dated correction note is
recorded at source in `_raw-gh-support-stacks.md`; **both licence verdicts (GLPI GPL-3.0, RT GPL-2.0)
stand unchanged** — only the editorial claim about the pre-scan was wrong.

**Net for the pack:** we lift *structure and ideas*, so AGPL/GPL are not obstacles — but every
verbatim quote needs its source named, and the `ee/`-carved repos need the specific directory checked
before quoting anything from them.

---

## 7b. Addendum — two cross-flags verified (2026-08-02, post-report)

### 7b.1 The Anthropic RAG support-agent reference: EXISTS, MIT — but the name channel B relayed is stale

Channel B relayed an X claim (@undefinedKi) that Anthropic published a public RAG support-agent
reference architecture. **Confirmed, with one correction that matters for citation.**

**The repo has been RENAMED.** `anthropics/anthropic-quickstarts` → **`anthropics/claude-quickstarts`**
(17,356★). The old name still resolves via GitHub's redirect, so a stale citation *appears* to work —
which is exactly how a dead reference survives review. **Cite `anthropics/claude-quickstarts`.**

**Licence: LIFTABLE.** `anthropics/claude-quickstarts@main:LICENSE` opened directly — plain MIT,
`Copyright (c) 2023 Anthropic`. No per-directory carve-out in the `customer-support-agent/` tree
(only `README.md` and `package.json` alongside the source).

**It is genuinely RAG, but not self-contained** — an honest limitation to record rather than repeat
the headline. From `customer-support-agent/README.md`:

> "An advanced, fully customizable customer support chat interface powered by Claude and leveraging
> **Amazon Bedrock Knowledge Bases** for knowledge retrieval."

Retrieval is a managed AWS service; the repo ships no vector store, no ingestion pipeline, and no
chunking strategy of its own. It requires an AWS account and a provisioned Bedrock KB to run. **This
is a UI-and-prompt reference, not a retrieval reference** — useful for policy, not for teaching RAG
mechanics (which are the `ai` pack's anyway).

**The load-bearing find: escalation as a typed output contract.** This is the artifact worker 3's
enumeration (§5.2) did not have, and it is first-party.
`customer-support-agent/app/api/chat/route.ts:26-41` constrains the model's response schema:

```ts
user_mood: z.enum(["positive","neutral","negative","curious","frustrated","confused"])
redirect_to_agent: z.object({
  should_redirect: z.boolean(),
  reason: z.string()   // "optional, include only if should_redirect is true"
})
```

**The escalation decision is a required, typed field the model must emit every turn** — not prose, not
a threshold, not an inferred tool call. That makes it loggable and auditable by construction, and it
is a cleaner starting artifact for the pack's "escalation paths" deliverable than any prompt text.

The stated triggers, from the system prompt in the same file (lines 140-146), are three, and all
**symbolic** — consistent with §5.2's finding that no real implementation uses a confidence float:

> (140) "If no information is available or if the information is not relevant for answering the question, you can redirect the user to a human agent"
> (144) "If the question is unrelated to Anthropic's products and services, you should redirect the user to a human agent."
> (146) "If you are unable to help the user **or if the user explicitly asks to talk to a human**, you can redirect them"

**A precision point the pack must not get wrong:** `user_mood` is *recorded alongside* the redirect
decision, **not stated as a trigger for it.** The prompt's worked example pairs
`"user_mood": "frustrated"` with `should_redirect: true`, but no rule says frustration causes
escalation. So this is **the first implementation found that tracks sentiment as a first-class
observed dimension while keeping the escalation rule scope-based** — which is a *better* design than
the sentiment-triggers-handoff pattern vendors describe, and worth teaching as such. Do not report it
as "Anthropic escalates on frustration."

**A first-party support taxonomy, MIT.** `customer-support-agent/app/lib/customer_support_categories.json`
ships 8 categories with keyword sets:

| id | keywords (verbatim, abridged) |
|---|---|
| `account` | ban, appeal, deletion, logging in, phone verification, roles, permissions |
| `billing` | AR, billing details, invoice, receipt, payment method, pricing, refund request, subscription management, taxes |
| `feature` | functionality, tools, capabilities, options, modules |
| `internal` | auto-reply, forward, ignore, spam, other, **sales reroute** |
| `legal` | data privacy, policy, terms of service, usage policy |
| `other` | job inquiry, 3rd party company |
| `technical` | guides, issue, security, downtime, performance, interface, system |
| `usage` | errors, capabilities, quality, techniques, limits, availability |

**The interesting row is `internal`** — a first-class category for contacts that are *not support at
all* (auto-replies, spam, forwards, sales reroutes). Every taxonomy in §2 models what a ticket is
*about*; this one reserves a bucket for **traffic that should leave the support queue entirely**.
That is a real omission in the helpdesk schemas and a cheap, concrete thing for the pack's support-
taxonomy deliverable to include. (`other` covering job inquiries and third-party companies is the
same instinct.) Combined with §2.1's three-bucket status taxonomy, this gives the pack both axes —
*what state is it in* and *what is it about* — from primary sources.

### 7b.2 `t0ddc3by/claude-for-customer-success` — agent architecture, in my lane only

Channel A owns this repo's content and has already ruled it **Apache-2.0 © SuccessCOACHING, the
clearest thin-license-on-thick-IP case of the run — DO NOT LIFT.** That ruling stands and nothing
here reopens it. Noting only the architecture, per the controller's scope.

58★, API reports **NOASSERTION** (channel A resolved the actual licence — another API-useless case
for §7's tally), last push **2026-05-29** (~2 months stale, consistent with A's "unadopted" finding).

The toolchain is more elaborate than a skill pack usually is: `managed-agent-cookbooks/` holds
per-motion agent definitions (`adoption-motion/agent.yaml`, `steering-examples.json`, and a
`subagents/` directory pairing a `.md` and a `.yaml` per subagent — `adoption-gap-identifier`,
`motion-planner`, `product-surface-analyzer`), plus sibling motions including `advocacy/`. Alongside:
`deployment-cookbooks/` (notably **`solo-csm-cookbook.md`**), a formal
`docs/agent-capability-model/claude-for-cs-agent-capability-model.yaml`, per-surface `.mcp.json` files
(`cs-ops/`, `csm/`), and an "AUQ" hook layer (`auq-resilience/hooks/auq_hook.py`, `auq_parser.py`,
`hooks.json`, invoked via `run_auq_hook.sh` from multiple surfaces).

**Relevance to this channel:** it is the only artifact in the corpus that decomposes CS work into
*named motions with typed subagents* rather than documents — the same instinct as Parlant's journeys
(§5.4), expressed as agent config instead of a runtime. Worth one line in the pack as prior art for
"CS work as motions", attributed and not lifted. The existence of a `solo-csm-cookbook.md` is
directly relevant to the charter's §1033 solo/self-serve conditional and is **flagged to A** to read
on the content side — I did not open it (A's lane).

---

## 7c. GitLab's Customer Success handbook — the enterprise canon, and its own best critic

Authorized follow-up pass, lead slice. Full detail: **[`_raw/_raw-gh-gitlab-cs-handbook.md`](_raw/_raw-gh-gitlab-cs-handbook.md)**.
Lives on **GitLab.com, not GitHub** (`gitlab-com/content-sites/handbook`, public REST API, `ref=main`,
read 2026-08-02). **Licence CITE-ONLY** — root `LICENSE` scopes itself to "the GitLab Software", not
the prose; no content licence in-repo (§7, charter clause e). Attribute and link; never reproduce.

`content/handbook/customer-success/` has 31 top-level entries; `csm/` alone recursively lists ~100
files. **This is almost certainly the largest publicly readable CS handbook in existence** — the
charter's enterprise-CSM canon (wedge 1) in its fullest public form, Gainsight-operated throughout,
and therefore canon-with-interest. Its value here is that **it is primary source about its own
limitations.**

### 7c.1 The structural fact that reframes the flagship

**GitLab does not use its health score to predict churn.** Prediction is two separate named models —
`Propensity To Expand (PTE)` and `Propensity To Churn or Contract (PTC)`, both listed **Active** — and
the section disclaims itself first:

> "Predictive Analytics is not a silver bullet. It will not cure all that ails you. Instead, this
> methodology is probabilistic and incorporates health measures to correlate the typical journey of
> 'healthy' customers (expand and renew) with 'unhealthy' customers (downgrade and churn)."

Both models link to `internal.gitlab.com` — **method, features and accuracy are not public and could
not be verified.**

At the most mature public CS org we can inspect, **the health score is a diagnostic and communication
device; churn prediction is a different artifact.** That is the honest answer to "what can a health
score predict" — *it isn't asked to*. Any vendor whose health score **is** the churn prediction is
doing something GitLab deliberately does not.

### 7c.2 Backtesting is a goal, not a result — the second time this handbook admits it

Under "Success criteria", verbatim:

> - "Customer health scoring framework **has been backtested and validated as effective and beneficial**"

It is a *target*, listed beside ">95% of customers have a health score". **Worker 2 found no public
health score reports precision/recall/AUC against outcomes; that absence now holds at the top of the
market, not just among 0-star toys.** And it is the same shape as §6.1's deflection finding — twice,
this handbook's stated ambition is *prove the measurement works*.

### 7c.3 The weighted model is overridden by one human field

GitLab's **P.R.O.V.E.** weighting: Product 50% · Risk 25% · Outcomes 10% · Engagement 10% · VoC 5%
(Gainsight bands: Green 75-100, Yellow 50-74, Red 0-49). All of Risk is `CSM Sentiment`, a
*"qualitative measure that the CSM updates"*. Then:

> "**CSM Sentiment Override of Overall Health Score**: When the CSM Sentiment score becomes red, the
> overall score will automatically become red."

**A customer can score perfectly on the 50%-weighted Product group and still be Red because the CSM
said so.** The weighting is real for green/yellow discrimination and decorative at the red boundary.
Not necessarily wrong — a CSM told the champion is leaving knows what telemetry cannot — but the
number is **a human judgement wearing a weighted-average costume**, and "data-driven health score"
is unfalsifiable in exactly the case the score exists for.

### 7c.4 Missing data silently shifts the score toward opinion

Missing measures are correctly not penalised (*"counted as `NULL` instead of a value (i.e., red)"*).
But the weight is then redistributed:

> "If all product usage stats are missing, then it's entirely reallocated to the other measures …
> **Heavier weighted measures, such as CSM Sentiment, would receive a bigger allocation because it's
> already the largest.**"

**Absent telemetry doesn't lower confidence — it raises subjectivity, automatically and invisibly.**
Made explicit for new accounts: *"Except for CSM Sentiment, all health measures will typically be
NULL for the first 30 days"*. **For a customer's first 30 days the health score is the CSM's opinion
and nothing else** — precisely the window where onboarding risk peaks.

### 7c.5 The machine and the human rubric disagree about ignorance

The scorecard treats missing data as neutral (7c.4). The human triage rubric treats it as risk —
Yellow is *"Potential risk **or significant lack of information leading to uncertainty**"*; Red is
*"…**or overwhelming lack of information, such as unresponsiveness leading up to renewal**"*.

Same handbook, opposite conventions. **The pack should take the human side — ignorance about an
account is a finding, not a gap** — and can cite the internal disagreement as evidence that the
algorithmic convention is a convenience, not a position.

### 7c.6 A published model containing components that don't exist

The PROVE table carries a **Maturity** column. Marked **"Not started"**: Positive Business Outcomes,
Support-CSAT, **NPS Surveys**, Executive Sponsorship, Events, Certifications. **The VoC group is 5% of
the score and three of its four measures are unbuilt** — so "Voice of the customer" is, in practice,
support-ticket counts. Anyone reading the architecture diagram would believe surveys feed the score.
**Cite this whenever a vendor shows a health-score diagram.**

### 7c.7 Support contact scored as a negative — and GitLab is inverting it

Bands: *"Green: 1-5 tickets/month · Yellow: 5-15 · Red: More than 15"* — **zero tickets is not
Green**, and the bands **overlap at 5** (the triage page says "6-15": two pages, two band sets). The
roadmap row for Support-Engagement reads: *"Retain existing methodology, but **tweak to allow more
tickets as a good thing**"*. And the human rubric already encodes the subtler rule — Yellow includes
*"**no ticket(s) opened after being advised by the CSM that Support is the best path to resolution**"*.

**The support-volume↔health relationship is non-monotone, and here is an org discovering that in
public.** Directly relevant to the pack's support ↔ health seam.

### 7c.8 Four practices worth lifting (framework only, cite GitLab)

1. **Every input has an explicit expiry.** Product usage → `NA` after **60 days** (*"we prefer to show
   nothing ('NA') over outdated data"*); CSM Sentiment flagged stale at **90**, forced `NA` at **120**;
   Support measures `NA` after **30**. Different, justified half-lives per signal. **The best
   honesty-preserving practice found in the whole channel** — and the exact thing the Dynatrace
   exhibit (§4.2) lacks entirely.
2. **Thresholds are segmented, not universal.** Meeting cadence is Green ≤35d for priority-1 accounts
   but ≤65d for priority-2; several measures are `N/A for Scale and Tech Touch` — **switched off where
   meaningless rather than scored badly.** The correct counter to §4.3's copied-threshold failure, and
   a direct answer to the charter's §1033 concern.
3. **Relationship breadth is scored.** `Persona engagement`: Green requires **both** Dev Lead and
   Security Lead attending in 3 months; single-threading is a named Yellow risk. Cheap, concrete, and
   one of the few measures here that survives translation to a smaller reader.
4. **A reason taxonomy with tie-breakers.** Two axes — **risk impact** (Churn · Tier Downgrade · Seat
   Churn · **Customer Sentiment (Impact Unknown)** · Competitor · Stage) and **risk reason** (Lack of
   adoption · Product Value/Gaps · Product Quality/Availability · Lack of Engagement/Sponsor · Loss of
   Budget · Corporate Decision · Other) — where each reason carries a disambiguation rule against its
   neighbour (*"If they didn't adopt because they didn't see value, it should be Product Gap"*; Loss of
   Budget *"was not a competitive loss"*). **A category list without tie-breakers is not a taxonomy.**
   Pairs with `churnkey/sdk`'s self-reported cancel reasons (§6.3): two honest reason taxonomies for
   two different motions — self-serve vs assessor-coded.

Two smaller notes worth one line each: escalation here is a **notification ladder by severity**
(Yellow → AE/SA/Regional Manager/Director; Red → **+ VP of Customer Success**) — a concrete instance
of §5.3's third meaning of "escalation". And the terminal `Will Churn` state exists partly because
*"Gainsight does not support a 'grey' color"* — **a vendor tool's palette shaping the taxonomy** —
while requiring four human steps incl. manager agreement to enter, which is good design: make giving
up expensive.

### 7c.9 What it does not support

This is enterprise CS in its purest form and **almost none of the machinery transfers to the solo/
self-serve reader**. What transfers is the **epistemics**: expiry on every signal, segmented
thresholds, ignorance-as-risk, tie-broken reason taxonomies, and the separation of scoring from
prediction. **The pack should lift the epistemics and explicitly decline the machinery** — this
handbook is the best available exhibit of *both* halves of wedge 1. **No accuracy number of any kind
appears anywhere in it.**

**Not read this pass** (recorded as unread, not absent): `product-usage-data/maturity-scoring.md`,
`platform-value-score.md`, `metrics-based-playbooks.md` (GitLab's *other two* scores — likely rich),
`customer-onboarding/index.md`, `csm/qbr/`, `csm/ebr.md`, `csm/renewals/`, `csm/risk-mitigation/`,
`csm/escalations/`, `csm/success-plans/`, `csm/engagement/non-engaged-customer-strategies.md`,
`submitting-customer-feedback.md`, `reporting-and-dashboarding-framework.md`.

---

## 8. Seam flags for the controller (recorded, not assigned)

1. **ai ↔ success — Parlant. RULED by the controller 2026-08-02, recorded in the run ledger:**
   **success owns the support-agent POLICY vocabulary and artifacts** — guidelines (condition→action),
   exclusion edges, bot boundaries, escalation, and strict-vs-fluid composition policy — **citing
   Parlant as the implementation**; **`ai` owns agent mechanics and evaluation** (the τ-bench side,
   §5.1, and the Bedrock-dependent retrieval in §7b.1). Sections 5.2 and 5.4 should be read as
   success-owned content; §5.1 as ai-owned evidence this pack cites but does not own.
2. **growth ↔ success — cancel flows.** Whether a save offer *works* is a growth experiment; the flow,
   the reason taxonomy, the exit-interview capture and running it are success execution.
   (`churnkey/sdk` is the concrete artifact.)
3. **operate ↔ success — "escalation".** The phrase is owned in open source by on-call paging. Add
   agent-desk's staged-rollout gating and off-hours auto-handoff, which are arguably deployment
   controls. The pack should name the support meaning distinctly rather than inherit the SRE one.
4. **product ↔ success — feedback boards.** Fider's status taxonomy is a product-roadmap communication
   device operated by success. The `PostResponse` + `declined`/`duplicate` states are the
   closing-the-loop artifact — likely success's, since it is the customer-facing reply.
5. **marketing ↔ success — app-review mining.** Charter gives marketing the ASO listing and success
   the review *responses*; mining reviews for product evidence (`joeseesun/qiaomu-app-review-insights`,
   216★, MIT) is a third thing, probably success's VoC job feeding product.
6. **AI-assisted human vs autonomous agent.** GitLab's policy governs *humans using AI to draft*
   ("Never generate a customer-facing reply entirely from an LLM… You remain responsible for the
   accuracy and completeness of every response"), which is a different object from an autonomous
   support bot. The pack should not conflate them.
7. **data ↔ success.** Usertour imports segments from Mixpanel/Heap cohorts (`Segment.source`,
   `sourceId`); Dynatrace's adoption metrics are product telemetry. Where the tracking plan ends and
   the health signal begins is a data-pack seam.

---

## 9. Open questions

1. **Is the academic churn literature as thin as the code?** Channel C can say the *open-source* churn
   canon is two B2C telecom datasets and that no public health score is validated. Whether the
   published literature is equally thin is channel D's to answer before the pack over-claims.
2. **Zero-result KB search queries as a VoC signal** — worker 3 found no dedicated open-source tool but
   flagged this as an **open question, not a confirmed absence** (Algolia DocSearch analytics are a
   hosted product). → D, as a vendor-site look.
3. ~~GitLab's `content/handbook/customer-success/` tree was not read.~~ **DONE — see §7c**
   (authorized follow-up, 2026-08-02). Thirteen files/subtrees within it remain unread and are listed
   at the end of §7c; the richest unread items are GitLab's *other two* scores
   (`product-usage-data/maturity-scoring.md`, `platform-value-score.md`). **New open question from
   that pass → D:** GitLab's PTE/PTC propensity models are the one enterprise churn model we came
   close to; their methodology lives at `internal.gitlab.com` and is unverifiable from here. If
   GitLab has said anything about them publicly (blog, talk, conference), that is the single best
   candidate for an evidenced statement about a real enterprise churn model's accuracy.
4. **Chatwoot's Captain prompt and Zammad's CSAT model** were partially unread (Captain is
   subscription-licensed so only describable; Zammad CSAT "not found, not confirmed absent").
5. **Does any AI support agent measure its own escalation *correctness*** (did it hand off when it
   should have)? τ-bench measures task success, eShopSupport measures answer quality; neither measures
   escalation decisions. If nothing does, that is a flagship-adjacent absence worth stating.

---

## 10. What channel C did NOT cover, and why

- **Anything off GitHub.** Chatwoot/Zammad/Formbricks hosted docs sites, Algolia's analytics product,
  the Parlant ARQ paper (arXiv **2503.03669**), and Fader & Hardie (2007, 2010), Harrell (1982),
  Brier (1950), Wang/Fader/Hardie ZILN (2019) — all **flagged to D**, none fetched here.
- **Skill-pack repos** — flagged to A, not investigated (§1.4).
- **Deep reads of second-tier stacks.** RT, Znuny, iTop, uvdesk got licence-and-status verification but
  not schema reads; their SLA/OLA models live in ecosystem add-ons outside the core repos.
- **`uvdesk/core-framework`'s LICENSE was not independently opened** — provisional OSL-3.0 only.
  `riteshbonthalakoti/HELPDESK.AI` likewise API-only → **AMBIGUOUS, re-verify before any lift.**
- **Zammad group capacity limits and Frappe `HD Team` routing fields** — not found, **not confirmed
  absent**. Recorded as unresolved rather than as negative findings.
- **Chatwoot Captain's prompt text** — read and described, deliberately not copied (subscription licence).
