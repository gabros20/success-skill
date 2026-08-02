# RAW — GitHub channel, worker 2: churn prediction, health scores, retention models

Scope: verify/quantify the Telco-dataset monoculture; read actual notebooks for load-bearing
accuracy numbers; survey serious survival-analysis tooling for candid statements on censoring/
evaluation; survey CLV/BTYD libraries for contractual-vs-non-contractual framing; grep-search for
health-score / NRR / GRR implementations. Every claim below is `owner/repo@ref:path`, read directly
(notebook cells / source / docs), never a README summary alone unless stated.

---

## A. The Telco-dataset monoculture — VERIFIED AND QUANTIFIED

**Quantification.** GitHub code search for the exact IBM Telco Customer Churn CSV filename
(`WA_Fn-UseC_-Telco-Customer-Churn`) returns **3,176 code files** across GitHub
(`gh api search/code -f q="WA_Fn-UseC_-Telco-Customer-Churn"`, `.total_count`, run 2026-08-02).
Sampling 100 hits found **96 unique repositories** in that sample alone — i.e. this one CSV, not
just "a telco dataset," is copy-pasted (not re-derived) into the large majority of churn-prediction
repos on GitHub. Separately, `gh search repos "customer churn prediction" --sort stars --limit 30`
returns a top-30 list where every single repo without exception (Pradnya1208, xiaogp,
mirzayasirabdullahbaig07, pree871, IBM/customer-churn-prediction, Sameer-ansarii, codebrain001,
ThuanNaN, AmirhosseinHonardoust, satz2000, KolatimiDave [different dataset — Expresso, an African
telco], himanshu-03 [explicitly "7,043 customers... Telecommunications company in California"],
Hazrat-Ali9, IBM/icp4d-customer-churn-classifier, Ashinshani, …) is a telecom/telco churn project;
zero are B2B SaaS or subscription-product churn. archd3sai (265★, cited in brief) doesn't even
surface in the top-30-by-stars query for "customer churn prediction" — the space is that flat/dense
with near-duplicate tutorials, not a "long tail off one clear leader."

**A second, distinct canonical dataset exists** (not mentioned in the brief): AWS's own reference
pipeline `awslabs/aws-customer-churn-pipeline@main:data/churn.txt` uses the *other* classic public
telecom-churn dataset — columns `State, Account Length, Area Code, Phone, Int'l Plan, VMail Plan,
Day Mins, Day Calls, Day Charge, Eve Mins, …, CustServ Calls, Churn?` (the "Orange/bigml Telecom
Churn" dataset, ~3,333 rows, distinct from IBM's 7,043-row Telco set). So precisely: **the OSS churn
canon is not one dataset, it is two — both B2C telecom, both from ~2015-2019, both re-used verbatim
rather than refreshed.**

**Per-repo verification (root listings + license files pulled directly):**

| repo | stars | dataset | license (file, not API) |
|---|---|---|---|
| pik1989/MLProject-ChurnPrediction | 158 | IBM Telco (`WA_Fn-UseC_-Telco-Customer-Churn.csv` in root) | **no LICENSE file** (404 on contents/LICENSE) |
| Pradnya1208/Telecom-Customer-Churn-prediction | 113 | IBM Telco (`data.csv`, same schema) | **no LICENSE file** (404) |
| IBM/customer-churn-prediction | 30, **archived** | IBM Telco | Apache-2.0 (file confirmed) |
| cloudera/CML_AMP_Churn_Prediction | 18 | IBM Telco ("Build...model to predict churn using customer telco data") | Apache-2.0 (LICENSE.txt confirmed) |
| awslabs/aws-customer-churn-pipeline | 41 | **Orange/bigml** telecom set (State/Account Length/…) — different from IBM Telco | mit-0 (file confirmed) |
| Azure-Samples/MachineLearningSamples-ChurnPrediction | 36, **archived** | IBM Telco (`CATelcoCustomerChurnModeling.py`) | MIT (LICENSE file confirmed, Microsoft Corporation copyright) |
| archd3sai/Customer-Survival-Analysis-and-Churn-Prediction | 265 | IBM Telco | MIT (LICENSE.md file confirmed, "Arch Desai") |

### Load-bearing numbers — read from the actual notebook, method quoted

**1. `pik1989/MLProject-ChurnPrediction@main:"Churn Analysis - Model Building.ipynb"` — the classic
trap, confirmed line-by-line.**
- Cells 8–14: `train_test_split(x, y, test_size=0.2)` on the raw imbalanced data, then Decision Tree.
  Output (cell 14): accuracy 0.78, but churn-class (label 1) precision 0.63 / recall 0.49 / f1 0.55.
  Markdown cell 15 correctly notes accuracy is "cursed" on an imbalanced set.
- **Cell 16–19: the leak.** `sm = SMOTEENN(); X_resampled, y_resampled = sm.fit_sample(x, y)` is
  applied to the **full dataset x, y BEFORE the train/test split** (cell 16), and only then is
  `train_test_split(X_resampled, y_resampled, test_size=0.2)` run (cell 17). The reported "improved"
  result (cell 19 output): `0.934412265758092` accuracy, precision/recall/f1 ≈ 0.91–0.98 for both
  classes. This is measured on a test set (`xr_test, yr_test`) that (a) is no longer at the ~26%
  real-world churn base rate (it's now ~540/634, near 50/50) and (b) may contain SMOTE-synthesized
  points that were never held out from the resampling process — a direct test-set contamination /
  leakage error, not a legitimate improvement. Same pattern repeated for Random Forest (cells 27–37,
  36–37 giving 0.943), and again with PCA (cells 45–46, 0.724). **The notebook presents 93–94%
  accuracy as the final, better number without ever flagging that the metric was computed on a
  resampled/rebalanced/partially-synthetic test set.** This is exactly the "trap" the brief predicted,
  found verbatim in a 158-star repo used in the author's own tutorial videos (linked from
  `pik1989/MLProject-ChurnPrediction@main:README.md`).

**2. `archd3sai/Customer-Survival-Analysis-and-Churn-Prediction@master:"Churn Prediction Model.ipynb"`
— the honest counter-example, same dataset.**
- Cell 9: `train_test_split(df, test_size=0.2, random_state=111, stratify=df.Churn)` — split BEFORE
  any resampling, and stratified. GridSearchCV (cells 14–37) tuned on `train_x/train_y` only, scoring
  `f1`, best CV f1 ≈ 0.566–0.579 across 4 grids (best_score_ values: 0.5665, 0.5754, 0.5792, 0.5774).
  Cell 42: 5-fold CV f1 on train data = `[0.605, 0.663, 0.622, 0.581, 0.638]`, mean 0.622 (used only
  as an over/underfitting sanity check, correctly labeled "performance on train data itself").
- **Cell 40 stdout — the true held-out test evaluation (1,409 rows, stratified, 374 churners =
  26.5% — matches the dataset's known churn rate):**
  ```
  Classification report :
                precision    recall  f1-score   support
             0       0.87      0.83      0.85      1035
             1       0.59      0.66      0.62       374
      accuracy                           0.79      1409
  Accuracy Score :  0.7877927608232789
  Area under curve :  0.8479681727763569
  ```
  **Accuracy 78.8%, churn-class F1 0.62, AUC 0.848 — on an honest, uncontaminated, correctly
  stratified held-out test set, same dataset the leaky repo used.**

**3. `Pradnya1208/Telecom-Customer-Churn-prediction@main:Scripts/"Customer churn prediction.ipynb"`
— an independent third implementation, methodologically clean, converges on the same ceiling.**
- Cell 51: `train_test_split(X, y, test_size=0.3, random_state=4, stratify=y)`.
- Cell 62 (10-fold CV, multiple algorithms): best CV results — Voting Classifier ROC AUC mean
  **84.93%** (std 1.39), Gradient Boost AUC mean 84.72%, Adaboost AUC mean 84.55%, Accuracy means
  cluster at **80.0–80.2%** across all models.
  ```
                     Algorithm  ROC AUC Mean  ROC AUC STD  Accuracy Mean
  9          Voting Classifier         84.93         1.39          80.23
  8  Gradient boost classifier         84.72         1.42          79.72
  7                   Adaboost         84.55         1.25          80.09
  ```
- Cell 76 (final held-out test evaluation): **Adaboost: Accuracy 0.812, Precision 0.688, Recall
  0.538, F1 0.604, F2 0.563** — best of the five models tried. Voting classifier, Gradient Boost close
  behind (F1 0.599, 0.588).
- Note: this repo's per-model headline visuals live only as PNG screenshots in `output/*.PNG`
  (`Accuracy score comparison.PNG`, `ROC AUC comparison.PNG`, etc.) — the numbers are NOT
  independently re-derivable from the README text, only from re-running or reading the notebook cell
  outputs directly, which is what was done here. A reader skimming the README/images alone gets no
  citable number; the notebook is the only primary source.

**Convergent honest ceiling for this specific dataset, three independent authors, no leakage:**
**accuracy ≈ 78–81%, churn-class F1 ≈ 0.60–0.62, recall ≈ 50–66%, AUC ≈ 0.83–0.85.** This is a real,
reproducible number for "how well can you predict churn from IBM's 7,043-row Telco dataset with
tabular ML" — and it is *not* 93%; 93% is what you get from a specific, identifiable coding error
(resampling before the split) that at least one 158-star, video-tutorial-linked repo teaches as the
improvement step.

### Features that recur (and the B2C→B2B generalization problem)

Across archd3sai's Cox model (`Customers Survival Analysis.ipynb`, cell 59 `cph.print_summary()`)
and the classifiers above, the dominant predictive features are: **Contract type** (`Contract_Two
year` coef −3.70, exp(coef)=0.02 — a two-year contract cuts hazard ~98% vs month-to-month baseline;
`Contract_One year` coef −1.27, exp(coef)=0.28), **tenure**, **payment method**
(`PaymentMethod_Electronic check` coef +0.39 <0.005; `PaymentMethod_Mailed check` coef +0.51 <0.005 —
both *increase* hazard vs the baseline autopay methods), **InternetService_Fiber optic** /
**InternetService_No**, **MonthlyCharges/TotalCharges**. These are the same handful of columns every
repo in section A reaches for (tenure, contract length, payment method, monthly/total charges,
internet service type) because they are the columns the dataset has — not because they were
independently rediscovered as universal churn drivers.

**The B2C-telco→B2B-SaaS generalization question is real and unresolved in the code itself: none of
these features map cleanly onto a B2B SaaS success context.** "Contract length" in Telco is a
literal fixed-term lock-in (month-to-month vs 1yr vs 2yr) — the SaaS analogue (monthly vs annual
plan) is structurally similar and probably DOES transfer as a signal. But "payment method"
(mailed check vs autopay) is a proxy for a B2C consumer's tech-savviness/friction tolerance that has
no clean SaaS equivalent; "InternetService: Fiber optic" is category-specific to telecom access
type and has zero mapping to software. **No repo examined attempts or discusses this
transfer question** — every repo trains and evaluates purely in-domain (Telco→Telco). This absence
is itself the finding: the open-source churn canon has never been asked to generalize outside B2C
telecom, so its recurring "predictive features" list is a property of the one dataset family, not a
demonstrated cross-domain law.

---

## B. Serious survival-analysis libraries — the real tooling, and candid self-documentation

| repo | stars | license (file+manifest verified) | staleness |
|---|---|---|---|
| CamDavidsonPilon/lifelines | 2,600 | MIT (LICENSE + setup.py `license="MIT"` agree) | active, pushed 2026-03 |
| sebp/scikit-survival | 1,314 | **GPL-3.0-or-later** (COPYING file = GPLv3 text; `pyproject.toml` `license = "GPL-3.0-or-later"`, `license-files=["COPYING"]` — file and manifest agree with each other) | active, pushed 2026-08-02 |
| havakv/pycox | 992 | BSD-2-Clause (LICENSE file confirmed) | **stale** — last push 2024-09, `archived:false` but not maintained |
| Novartis/torchsurv | 210 | MIT (LICENSE file, "Novartis Pharmaceuticals Corporation" copyright) | active, pushed 2026-07 |
| loft-br/xgboost-survival-embeddings | 343 | Apache-2.0 (LICENSE file confirmed) | **archived:true** as of this scan (brief's figure of 992★ was pycox's, not xgbse's — verify against brief if reused) |
| soda-inria/hazardous | 121 | MIT (LICENSE file, "Soda team @ Inria") | active, pushed 2026-07 |
| jaredleekatzman/DeepSurv | 704 | MIT | **stale** — last push 2020-08, `archived:false` |
| chl8856/DeepHit | 239 | **no LICENSE file** (API returns null) | stale-ish, pushed 2025-02 |

**Licence verdicts:** lifelines / torchsurv / hazardous / xgbse / pycox → LIFTABLE (permissive,
file-verified). **scikit-survival → CITE-ONLY** — GPLv3 copyleft blocks lifting code/examples into a
permissively-licensed skill deliverable; may cite/describe its concepts and API shape, not copy code.
DeepHit → CITE-ONLY (no license = all rights reserved by default per rule 3d/e). DeepSurv and pycox:
`archived:false` but both dormant 4+ years — treat as historically important, not actively-maintained
tooling (rule: archived:false ≠ alive).

### What lifelines candidly says about itself — directly quotable, and directly contradicts a bad
number found elsewhere in this research

`CamDavidsonPilon/lifelines@master:docs/"Survival Analysis intro.rst"` (censoring, lines 28–61):
> "A common mistake data analysts make is choosing to ignore the right-censored individuals... If
> we are asked to estimate the average lifetime of our population, and we naively decided to *not*
> include the right-censored individuals, it is clear that we would be severely underestimating the
> true average lifespan. Furthermore, if we instead simply took the mean of *all* lifespans,
> including the current lifespans of right-censored instances, we would *still* be underestimating
> the true average lifespan."

This is the textbook statement of the exact error naive churn classifiers make: treating "hasn't
churned yet, as of the data snapshot" as equivalent to "will not churn" (label 0) silently
underestimates true churn propensity for recently-acquired cohorts. **Direct illustration of scale**:
`archd3sai/Customer-Survival-Analysis-and-Churn-Prediction@master:"Customers Survival Analysis.ipynb"`
cell 59, fitting `CoxPHFitter` on the IBM Telco data: `<lifelines.CoxPHFitter: fitted with 7043
observations, 5174 censored>` — **73.5% of the dataset is right-censored** (customers who have not
yet churned as of the snapshot); only 1,869 (26.5%) are observed churn events. Any naive
classification treating the 5,174 censored rows' current label as ground truth "will stay" is
building on a majority-censored population.

`CamDavidsonPilon/lifelines@master:docs/"Survival Regression.rst"` (lines ~1123–1128, model
selection):
> "If censoring is present, it's not appropriate to use a loss function like mean-squared-error or
> mean-absolute-loss. This is because the difference between a censored value and the predicted
> value could be due to poor prediction *or* due to censoring."

On the concordance index / c-index (lines 1166–1178) — **the single most useful sentence found in
this entire research slice for calibrating "what accuracy is honest":**
> "Fitted survival models typically have a concordance index between 0.55 and 0.75 (this may seem
> bad, but even a perfect model has a lot of noise that can make a high score impossible)."

Also (line 1204), on what concordance does NOT tell you:
> "the concordance score evaluates the relative rankings of subject's event times... A model
> maximized for concordance-index does not necessarily give good predicted *times*, but will give
> good predicted *rankings*."

**This directly flags a suspicious number found in the same archd3sai repo**: the CoxPH fit in
`"Customers Survival Analysis.ipynb"` cell 59 output reports **Concordance = 0.93** — well above
lifelines' own stated "typical" 0.55–0.75 ceiling. Cause, visible in the same output: the model
includes `TotalCharges` as a covariate, and `TotalCharges` is (near-)deterministically
`tenure × MonthlyCharges` — i.e. the model is regressing time-to-event against a covariate that is
itself almost a direct proxy for the duration variable being predicted. This is a form of leakage
specific to survival regression (using a covariate that encodes elapsed duration) and produces an
implausibly high, near-tautological concordance score. **Cross-referenced against an honest
comparison point**: `awslabs/aws-customer-churn-pipeline@main:notebook/coxph/"Example_Churn_Surv.ipynb"`
cell 40, using the censoring-adjusted **IPCW concordance** (`sksurv.metrics.concordance_index_ipcw`,
Harrell et al. 1982 generalization) on its own (different) telecom dataset, reports
**concordance = 0.7515** — squarely inside lifelines' stated normal range, computed correctly with a
proper train/test split and no duration-leaking covariate. That AWS notebook is a genuinely
sophisticated reference implementation: it explicitly names right-censoring, plots per-customer
timelines to show censored vs. observed, uses XGBoost-AFT + scikit-survival's IPCW concordance and
Brier score (0.376, cell 40 output), and cites Harrell 1982, Brier 1950, and lifelines/PySurvival as
prior art in its references cell. License: mit-0 (repo-level, file-verified above) — LIFTABLE.

**Net finding for section B**: the tooling and its own documentation are far more epistemically
honest than the tutorial-notebook churn-prediction space in section A — lifelines states plainly
what a "good" c-index looks like and why naive censoring-blind methods are wrong, and that stated
range (0.55–0.75) is precisely calibrated enough to catch a bad number (0.93) in a different,
popular repo built on the very dataset this research is auditing.

---

## C. CLV / BTYD (buy-till-you-die) family — contractual vs. non-contractual, in the code itself

| repo | stars | license (file-verified) |
|---|---|---|
| pymc-labs/pymc-marketing | 1,211 | Apache-2.0 (LICENSE file confirmed) |
| facebookincubator/LTVision | 108, **archived** | LICENSE.md = **standard 3-clause BSD-style** ("BSD License... Copyright (c) Meta Platforms... Neither the name Meta nor the names of its contributors may be used..."). **Note: GitHub's license API field reports "other"** — this is the license-API-lies problem (rule 3a) confirmed again; the actual file text is a normal permissive BSD-3-clause variant. No PATENTS grant file found in root listing (unlike some other Meta OSS repos) — verdict LIFTABLE, but flag the absence of an explicit patent grant as something worth a second look if this were ever actually lifted at scale. |
| Willofd101/ziln_cltv | 38 | MIT (LICENSE file confirmed) |
| GoogleCloudPlatform/tensorflow-lifetime-value | 175 | Apache-2.0 |
| theofilos/BTYD | 21 | **no LICENSE/DESCRIPTION file at all** (repo is just `README.md`, `fix_btyd.R`, `pnbd.R` — a patch on top of the original CRAN `BTYD` R package). CITE-ONLY: no license file = default all-rights-reserved; and per rule (e), even if it had MIT'd its own diff, it would not license the underlying BTYD framework — **cite Fader, Hardie & Lee as the original authors regardless of this repo's own licensing status.** |

**The contractual/non-contractual distinction, found directly in the code's own docstrings** (not
inferred) — this is the single cleanest piece of evidence for "under-taught distinction" in the whole
slice:

`pymc-labs/pymc-marketing@main:pymc_marketing/clv/models/beta_geo.py:14` (module docstring, first
line):
> "Beta-Geometric Negative Binomial Distribution (BG/NBD) model for a **non-contractual** customer
> population across continuous time."

`pymc-labs/pymc-marketing@main:pymc_marketing/clv/models/shifted_beta_geo.py:34` (class docstring):
> "Shifted Beta Geometric (sBG) model for **customers renewing contracts** over discrete time
> periods."
with references (lines ~75–86) directly to:
> [1] Fader, P. S., & Hardie, B. G. (2007). "How to project customer retention." Journal of
> Interactive Marketing, 21(1), 76-90.
> [2] Fader, P. S., & Hardie, B. G. (2010). "Customer-Base Valuation in a **Contractual Setting: The
> Perils of Ignoring Heterogeneity.**" Marketing Science, 29(1), 85-93.

**This is the primary-source citation the charter asks for**: Fader & Hardie's own 2010 paper title
states the exact failure mode (ignoring customer heterogeneity in a contractual setting produces
biased customer-base valuations) — the library's own code structure (separate model class, separate
citation) encodes the taxonomy correctly: BG/NBD and Pareto/NBD (also in the repo,
`pareto_nbd.py`) are for **non-contractual, continuous-time** repeat-purchase settings (the canonical
example used in `docs/source/notebooks/clv/clv_quickstart.ipynb` is an **online music store** —
customers who simply stop buying, with no explicit cancellation event), while `ShiftedBetaGeoModel`
(sBG) is for **contractual, discrete-time** settings (subscriptions with an explicit renewal/lapse
event per period) — which is the B2B-SaaS-relevant case. **FLAG TO D**: Fader & Hardie 2007/2010
papers (URLs embedded in the docstring, both hosted at faculty.wharton.upenn.edu) are the primary
literature D should pull and verify directly — this channel only confirms the code cites them
correctly, not what the papers themselves claim.

**Honest, code-enforced assumption-checking found in the CLV quickstart notebook**
(`pymc-labs/pymc-marketing@main:docs/source/notebooks/clv/clv_quickstart.ipynb`):
- Explicit acknowledged model limitation (markdown cell, quoted near-verbatim): "Note that all
  non-repeat customers have an alive probability of 1, which is one of the quirks of `BetaGeoModel`.
  In many use cases this is still a valid assumption, but if non-repeat customers are a key focus in
  your use case, you may want to try `ParetoNBDModel` instead." — a library plainly documenting a
  known blind spot of its own default model rather than hiding it.
- The Gamma-Gamma monetary-value model's core assumption is stated and then **actually checked in
  the executed notebook**, not just asserted: "The Gamma-Gamma model relies on the important
  assumption that there is no relationship between the monetary value and the purchase frequency. In
  practice we need to check whether the Pearson correlation is less than 0.3" — followed by a code
  cell computing that correlation before proceeding to fit.
- The notebook explicitly frames its own dataset ("purchases from an online music store") as
  "an example of continuous time, non-contractual transactions," reinforcing that the BG/NBD family
  is scoped to that setting by design, not by omission.

No repo in this section contained a headline "our CLV model was X% accurate against actual realized
LTV" validation statement with a number attached — the pymc-marketing notebooks demonstrate
methodology (train/test split via `rfm_train_test_split`, MAP vs. MCMC consistency checks, assumption
checks) but stop short of publishing a backtested accuracy figure. **This itself is worth recording
as absence-evidence**: even the most methodologically careful CLV tooling examined does not ship a
"how accurate was this in practice" number — the field's honesty shows up as documented assumptions
and checks, not as a validated accuracy claim.

---

## D. Health scores + CS-ops math in code — the flagship test

### Search log (for the absence-evidence record)

- `gh search repos "customer health score" --limit 20` → 20 results. **19 of 20 have 0–1 stars.**
  The two with any traction (`PavanPasidu/CustomerHealthScore`, `NoahPG88/customer-health-scores`,
  `Alrx12/Customer-Health-Score`) have exactly 1 star each. Zero repos in this list exceed 1 star.
- `gh search repos "customer success health score" --sort stars --limit 10` → 3 results total, all
  0 stars.
- `gh search repos "churn health score dashboard" --sort stars --limit 10` → **0 results.**
- `gh search repos "RFM segmentation" --sort stars --limit 10` → top hit is
  `TatevKaren/data-science-popular-algorithms` (140★) — a general algorithms-catalog repo where RFM
  is one bullet point among many unrelated topics (recommenders, decision trees, k-means, LDA,
  XGBoost), not a CS/retention-specific tool. Every RFM-segmentation-specific repo below that is a
  student/portfolio e-commerce analytics project (≤28 stars), none B2B-SaaS-specific, none validated
  against actual retention/churn outcomes.
- `gh api search/code -f q="net_revenue_retention"` → 1,348 code hits total; `gh api search/code
  -f q="def calculate_grr"` → 57 hits; `gh api search/code -f q="gross_revenue_retention"` → 240
  hits. **Multiple hits across these searches were Claude-skill / agent-registry repos, not CS
  tooling** — see FLAG TO A below.
- `gh api search/code -f q="health_score weight customer"` → dominated by unrelated projects
  (rental platforms, credit scoring, drone dashboards, ISP intelligence) using "health_score" as a
  generic term, plus more Claude-skill repos, plus several 0-star AI-generated-looking "customer
  churn intelligence platform" portfolio repos with generic marketing-copy descriptions
  (`harikrishna2101/customer-retention-intelligence-portal`, 0★).

**Conclusion on the search: there is no open-source health-score implementation anywhere near the
star-count or maintenance level of the survival libraries in section B or even the tutorial churn
notebooks in section A.** The entire category tops out at 0–1 stars. This is a grep-verified absence,
consistent with the charter's wedge hypothesis — health scoring is not merely under-discussed in
public code, it is essentially unbuilt in public.

### The two most substantive artifacts found — read in full

**1. A real production script, `jwinternheimer/customer-health-score@master:generate_scores.R`**
(identical file set to `bufferapp/customer-health-scores`, both 0★ — appears to be a personal copy
of an actual internal script from Buffer, a real B2B SaaS company, given the `library(buffer)` import
and Redshift/dbt queries against `dbt.updates`/`dbt.profiles` tables). This is the single most
"real" health-score-adjacent artifact found. What it actually does, read line by line:
- Pulls each customer's weekly product-usage counts (`update_count`, i.e. posts scheduled) over the
  trailing 180 days, restricted to paid plans.
- Fits **one univariate logistic-regression trend per customer**:
  `glm(cbind(update_count, update_total) ~ year, family="binomial")` — i.e., it tests whether a
  customer's *usage share over time* is declining, using calendar time as the sole predictor.
- Flags a customer `at_risk` only if the fitted slope `estimate <= -5` **and** `p.value <= 0.05`
  (`get_slopes()`, lines ~103–108).
- **This is not a weighted composite score** (contrary to my prior assumption going in) — it is a
  single-signal statistical significance test on usage-decline trend. But it has no validation step
  anywhere in the file: no comparison of "flagged at_risk" against subsequent actual churn/downgrade
  outcomes, no precision/recall, no chosen-threshold justification for why slope ≤ −5 (an arbitrary,
  uncommented magic number) is the cutoff rather than −3 or −10. It computes and writes scores to a
  table; it never closes the loop by checking whether the score predicted anything.

**2. `twentic/twentic_customer_health_score@main:crm_customer_churn_rfm/models/res_partner.py`** — an
Odoo (real ERP platform) CRM module, "Prevent customer churn using RFM (Recency, Frequency,
Monetary) analysis" (manifest description). **License note**: `__manifest__.py` declares
`'license': 'LGPL-3'`, but the GitHub API license field for the repo returns null/empty — another
instance of API-vs-manifest mismatch (rule 3a/3b), resolved here in favor of the manifest text since
no separate LICENSE file exists in the repo to check against. Reading the actual scoring code:
```python
SCORE_AT_RISK = 40.0       # Below this → create activity
SCORE_HEALTHY = 70.0       # Above this → green
MIN_INVOICES = 3           # Minimum invoices required to compute a score
...
recency_score = ...        # linear decay 100→50 between 1x and 2x avg purchase frequency, →0 beyond 2x
monetary_score = min(100.0, max(0.0, (last_two_avg / overall_avg) * 100.0))
...
rfm_score = (0.6 * recency_score) + (0.4 * monetary_score)   # Combined RFM score (60% recency + 40% monetary)
```
**This is exactly the toy weighted-sum pattern the charter hypothesized, confirmed line-for-line:**
- It calls itself an "RFM" (Recency-Frequency-Monetary) score but **Frequency is not actually
  scored** — `rfm_purchase_frequency` is computed and stored but used only to normalize the decay
  rate of the Recency component; it never enters the weighted sum as its own dimension. The module
  name promises three dimensions and delivers a weighted average of two.
- The 60/40 weighting, the 40/70 risk thresholds, the "≥40% below historical average" monetary alert
  trigger, and the 1×/2× frequency decay breakpoints are all **round-number magic constants with no
  citation, no derivation, and no backtest** anywhere in the ~180-line file.
- `MIN_INVOICES = 3` is commented "so that the metric is statistically meaningful" but no actual
  statistic (confidence interval, significance test, standard error) is computed anywhere in the
  module — "statistically meaningful" is asserted, not implemented.
- Zero validation code: no historical check of whether `rfm_score < 40` actually preceded real churn
  events in this system's own data model.

**Net finding: across the two most substantive artifacts this search could find, one narrowly
legitimate approach exists (a single-signal, statistically-framed usage-decline test with no
outcome validation — Buffer/jwinternheimer) and one textbook toy weighted-sum with arbitrary,
uncited, unvalidated weights and thresholds masquerading under the "RFM" label (twentic Odoo module).
Neither validates its own predictive claim against real outcomes. No repo found anywhere in this
search reports a precision/recall/AUC number for a health score against actual subsequent
churn/expansion/renewal — a claim type that is completely absent from the corpus, in contrast to
section A where churn-classifier accuracy claims are extremely common (if sometimes wrong).**

### NRR / GRR calculators — the one clean positive finding

`0x416d6972/pypulate@main:src/pypulate/kpi/business_kpi.py` (13★, MIT — LICENSE file and
`pyproject.toml` `license = {text = "MIT"}` agree) implements both formulas **correctly and in
textbook-standard form**:

```python
def net_revenue_retention(starting_revenue, expansion_revenue, contraction_revenue, churned_revenue):
    """NRR ... measures the percentage of recurring revenue retained from existing customers
    over a period, including expansion and net of contraction and churn."""
    retained_revenue = starting_arr + expansion_arr - contraction_arr - churned_arr
    # >>> net_revenue_retention(10000, 2000, 500, 1000)
    # 105.0

def gross_revenue_retention(starting_revenue, contraction_revenue, churned_revenue):
    """GRR measures... excluding any expansion. It is capped at 100%..."""
    retained_revenue = starting_arr - contraction_arr - churned_arr
    # >>> gross_revenue_retention(10000, 500, 1000)
    # 85.0
```
Both formulas: (a) are anchored to a **period-start revenue base** (`starting_revenue`), not a
blended/average base — matching the standard definition; (b) **correctly exclude new-logo revenue
entirely** — neither function takes a "new business" parameter, consistent with NRR/GRR being
existing-customer-only metrics by definition; (c) GRR correctly excludes expansion while NRR
correctly includes it. Minor observation: the docstring claims GRR "is capped at 100%" but the code
does not explicitly clip the result — the cap is only true by construction as long as
contraction/churned inputs are non-negative (which the function does not validate), so the docstring
overstates what the code enforces, though for well-formed inputs the math is correct regardless.
**This is the one place in the entire "health/CS-ops math" search where the implementation matches
the textbook definition with no shortcuts** — worth citing as a clean reference point in the pack
(module is small, MIT, easily readable end to end).

### Claude-skill / agent repos surfaced incidentally — FLAG TO A

- `borghei/Claude-Skills` (441★) — "368 AI skills... for every team... business ops"
- `majiayu000/claude-skill-registry` (530★) — general Claude Code skills registry
- `nimrodfisher/data-analytics-skills` (337★) — "comprehensive list of Claude skills... data
  analytics"
- `afumu/wetrace-skill`, `claude-office-skills/skills` — surfaced in `health_score`/NRR code searches
  as containing those terms somewhere (likely in a skill's example/prompt text, not implemented
  logic) — worth A checking whether any ship an actual CS/health-score skill definition.

---

## Licence verdict table (consolidated)

| repo | licence found (file-verified) | verdict |
|---|---|---|
| pik1989/MLProject-ChurnPrediction | none (no LICENSE file, 404) | CITE-ONLY |
| Pradnya1208/Telecom-Customer-Churn-prediction | none (no LICENSE file, 404) | CITE-ONLY |
| IBM/customer-churn-prediction | Apache-2.0 (file confirmed) | LIFTABLE (but archived — verify staleness before reuse) |
| cloudera/CML_AMP_Churn_Prediction | Apache-2.0 (file confirmed) | LIFTABLE |
| awslabs/aws-customer-churn-pipeline | mit-0 (file confirmed) | LIFTABLE |
| Azure-Samples/MachineLearningSamples-ChurnPrediction | MIT (file confirmed) | LIFTABLE (archived, stale since 2019) |
| archd3sai/Customer-Survival-Analysis-and-Churn-Prediction | MIT (LICENSE.md confirmed) | LIFTABLE |
| CamDavidsonPilon/lifelines | MIT (file + setup.py agree) | LIFTABLE |
| sebp/scikit-survival | GPL-3.0-or-later (COPYING + pyproject.toml agree) | CITE-ONLY (copyleft) |
| havakv/pycox | BSD-2-Clause (file confirmed) | LIFTABLE (stale since 2024) |
| Novartis/torchsurv | MIT (file confirmed) | LIFTABLE |
| loft-br/xgboost-survival-embeddings | Apache-2.0 (file confirmed) | LIFTABLE (archived) |
| soda-inria/hazardous | MIT (file confirmed) | LIFTABLE |
| jaredleekatzman/DeepSurv | MIT | LIFTABLE (stale since 2020) |
| chl8856/DeepHit | none (API null, unverified further) | CITE-ONLY |
| pymc-labs/pymc-marketing | Apache-2.0 (file confirmed) | LIFTABLE |
| facebookincubator/LTVision | BSD-3-clause-style (LICENSE.md text; API field says "other" — API is wrong) | LIFTABLE (archived; no PATENTS file found) |
| Willofd101/ziln_cltv | MIT (file confirmed) | LIFTABLE — but underlying ZILN loss method is Wang/Fader/Hardie (Google) 2019; cite the paper, don't imply the repo owns the method |
| GoogleCloudPlatform/tensorflow-lifetime-value | Apache-2.0 | LIFTABLE |
| theofilos/BTYD | none (no file at all) | CITE-ONLY — and regardless of this repo's own status, cite Fader/Hardie/Lee as BTYD's original authors, never this compiler |
| 0x416d6972/pypulate | MIT (file + pyproject.toml agree) | LIFTABLE |
| twentic/twentic_customer_health_score | LGPL-3 (manifest only; API null) | CITE-ONLY (copyleft, per manifest) |
| jwinternheimer/customer-health-score / bufferapp/customer-health-scores | none found in listing | CITE-ONLY |

---

## What we could NOT find (absence evidence)

1. **No open-source health-score library/tool with any star traction.** Every dedicated
   "customer health score" repo found tops out at 1 star (searches: `"customer health score"`,
   `"customer success health score"`, `"churn health score dashboard"` [zero results]). Compare to
   section B's survival libraries (up to 2,600★) or even section A's tutorial notebooks (up to 265★)
   — health scoring specifically has never produced a repo anyone actually uses or stars.
2. **No health-score implementation with a stated/tested accuracy, precision, recall, or AUC against
   real subsequent churn/renewal/expansion outcomes.** Both artifacts read in full (Buffer's
   usage-slope script, the Odoo RFM module) compute and act on a score but never check whether the
   score's predictions were later correct.
3. **No RFM-segmentation repo scoped to B2B/SaaS retention** — every RFM repo found
   (`AmirhosseinHonardoust/*`, `Nte-Daniels/ShopSphere-*`, `orzanai/FLO_CRM_Analytics`,
   `psgpyc/RFM-Segmentation-*`) is e-commerce/retail transactional analytics (Online Retail dataset,
   FLO shoe brand, generic Shopify trackers), not subscription-software customer success.
4. **No CLV/BTYD repo published a backtested "our predicted LTV was within X% of actual realized
   LTV" number** — pymc-marketing and LTVision both demonstrate methodology (assumption checks,
   train/test splits) but stop short of a validated accuracy claim.
5. Searched for and found **zero** matches for a from-scratch, generalizable "cohort-anchored NRR/GRR
   calculator" beyond the single pypulate module — every other NRR/GRR-adjacent code hit in the
   `net_revenue_retention` / `gross_revenue_retention` / `def calculate_grr` searches was either a
   Claude-skill repo (prompt text, not implemented logic — flagged to A above) or an unrelated
   project using the term in passing (financial-analysis agents, portfolio trackers).

---

## FLAG TO D (papers/URLs to verify independently, not verified here beyond "the code cites them")

- Fader, P. S., & Hardie, B. G. (2007). "How to project customer retention." Journal of Interactive
  Marketing, 21(1), 76-90. (cited in pymc-marketing's sBG model docstring)
- Fader, P. S., & Hardie, B. G. (2010). "Customer-Base Valuation in a Contractual Setting: The
  Perils of Ignoring Heterogeneity." Marketing Science, 29(1), 85-93. — the primary source for the
  contractual-vs-non-contractual distinction.
- Harrell, F. et al. (1982) — origin of the concordance/c-index, cited in AWS's coxph notebook.
- Brier, G. (1950) — origin of the Brier score, same notebook.
- Wang, Fader, Hardie (Google, 2019) — origin of the ZILN (zero-inflated lognormal) loss used in
  `Willofd101/ziln_cltv`; verify exact citation/venue.

## FLAG TO A (Claude-skill repos surfaced incidentally during CS/health-score code searches)

- `borghei/Claude-Skills` (441★), `majiayu000/claude-skill-registry` (530★),
  `nimrodfisher/data-analytics-skills` (337★), `afumu/wetrace-skill`, `claude-office-skills/skills` —
  none deep-read by this worker; A should check whether any ship an actual CS/health-score/churn
  skill definition worth comparing against this pack's flagship.
