# _raw · web (channel D, LEAD SLICE) — customer-feedback-metric evidence, CES provenance, VoC method

Author: channel D lead (opus). Date: 2026-08-02.
Scope: territory not assigned to workers — the Customer Effort Score primary + its peer-reviewed
replication, the provenance of the CX statistics canon, VoC survey method, customer-education evidence.
Method note: every number below was read from a PDF **downloaded and text-extracted locally**
(`pdftotext`), not from a WebFetch summary, per charter rule 2. Local copies under `/tmp/dlead/`.

Files downloaded and extracted:
- `/tmp/dlead/ces_hbr2010.pdf` + `ces.txt` — Dixon, Freeman & Toman, HBR Jul–Aug 2010
- `/tmp/dlead/dehaan2015.pdf` + `dehaan.txt` — de Haan, Verhoef & Wiesel, IJRM 2015 (in-press author version)

---

## 1. Customer Effort Score — the primary source (PRIMARY TEXT READ: YES)

**Source:** Matthew Dixon, Karen Freeman, Nicholas Toman, "Stop Trying to Delight Your Customers",
*Harvard Business Review*, July–August 2010.
Canonical URL: https://hbr.org/2010/07/stop-trying-to-delight-your-customers
Full text obtained from an openly hosted reprint: https://satoriconsultinginc.ca/wp-content/uploads/2020/05/Harvard_Business_Review-Stop_Trying_to_Delight_Your_Customers.pdf
(the reprint carries the line "This article is made available to you with compliments of Corporate
Executive Board" — i.e. it is the CEB-distributed reprint of the real article, not a summary).

### 1.1 The stated method, verbatim (the "About the Research" sidebar)

> "We defined 'loyalty' as customers' intention to continue doing business with a company, increase
> their spending, or say good things about it (or refrain from saying bad things). During a three-year
> period, we surveyed more than 75,000 B2C and B2B customers about their recent service interactions
> in major non-face-to-face channels, including live phone calls, voice prompts, web, chat, and e-mail.
> The companies represent dozens of industries, ranging from consumer electronics and packaged goods
> to banking and travel and leisure, in North America, Europe, South Africa, Australia, and New Zealand.
> We isolated the elements of each interaction that drove customer loyalty, both positively and
> negatively, and controlled for variables including the type of service issue, whether it was handled
> by an in-house or an outside contact center, the rep's tenure with the company, the company's size,
> the customer's personality type, the customer's mood prior to the interaction, switching costs, the
> frequency with which ads were seen or heard, the perceived product quality and value, product price,
> the industry, and the specific company. Finally, we conducted several hundred structured interviews
> in order to understand companies' customer service strategies and operations in detail.
> **Although our research focused exclusively on contact-center interactions, it makes intuitive sense
> that the findings apply to face-to-face encounters as well.**"

**Grade: PRACTITIONER-REPORT / METHOD-PARTIALLY-STATED.** Not MEASURED-WITH-METHOD, for four reasons
that are all visible in the primary text and all load-bearing for our pack:

1. **The outcome is INTENTION, not behavior.** "Loyalty" is explicitly defined as *intention* to
   continue, *intention* to spend more, *intention* to say good things. No repurchase was observed.
2. **The research is by the vendor of the metric.** The Customer Contact Council is "a division of the
   Corporate Executive Board" (now Gartner); CEB sold the CES benchmarking programme. Charter rule 5
   grading applies: this is canon-with-interest, structurally the same situation as Gainsight's book.
3. **No statistics are reported anywhere in the article.** This is the single most important finding
   in this section. The "Introducing the Customer Effort Score" sidebar's key exhibit is a bar chart
   captioned "PREDICTIVE POWER FOR REPURCHASING" with three bars labelled CES, NPS, CSAT and a single
   axis label "HIGH". **There are no numbers on the axis, no R², no coefficients, no confidence
   intervals, no n per comparison.** The entire claim of CES superiority rests on an unlabelled
   ordinal bar chart. Verbatim from the sidebar:
   > "We evaluated the predictive power of three metrics—customer satisfaction (CSAT), the Net Promoter
   > Score (NPS), and a new metric we developed, the Customer Effort Score (CES)—on customer loyalty,
   > defined as customers' intention to keep doing business with the company, increase the amount they
   > spend, or spread positive (and not negative) word of mouth. Not surprisingly, CSAT was a poor
   > predictor. NPS proved better (and has been shown to be a powerful gauge at the company level).
   > **CES outperformed both in customer service interactions.**"
   And the mechanism offered is belief, not evidence:
   > "**We believe** that the superior performance of CES in the service environment derives from two
   > factors: its ability to capture customer impressions at the transactional level (as opposed to NPS,
   > which captures more holistic impressions of a company) and its ability to capture negative
   > experiences…"
4. **HBR is not peer-reviewed.** Neither the data nor the models were ever released.

### 1.2 The CES question and scale, verbatim

> "CES is measured by asking a single question: 'How much effort did you personally have to put forth
> to handle your request?' It is scored on a scale from 1 (very low effort) to 5 (very high effort)."

**SCALE DIRECTION IS LOAD-BEARING** — higher CES = worse. This matters in §2 below, where a widely
repeated secondary source misreads the sign of the replication result.

Note for the pack: the modern "CES 2.0" is a *different instrument* — a 7-point agree/disagree item
("The company made it easy for me to handle my issue") in which higher = better, i.e. the direction is
inverted relative to the 2010 original, and the word "effort" no longer appears in the item. Anyone
comparing a CES number to a 2010-era benchmark is comparing two different scales pointing opposite ways.
(Secondary: https://measuringu.com/customer-effort-score/ — Jeff Sauro, measurement-science practitioner.
PRIMARY TEXT NOT OBTAINED for the CES 2.0 rewording rationale.)

### 1.3 Every number the article actually reports (this is the important provenance finding)

All of the following come from the **same single proprietary CEB dataset** described in §1.1, and all are
reported without any accompanying statistic, interval, or breakdown. Verbatim:

- > "89 of the 100 customer service heads we surveyed said that their main strategy is to exceed
  > expectations." … "84% of customers told us that their expectations had not been exceeded during
  > their most recent interaction."
- > "fully 80% of customer service organizations use customer satisfaction (CSAT) scores as the primary
  > metric"
- > "Twenty percent of the 'satisfied' customers in our study said they intended to leave the company in
  > question; 28% of the 'dissatisfied' customers intended to stay."
- > "Customers are four times more likely to leave a service interaction disloyal than loyal."
- > "Well over half the customers we surveyed reported encountering difficulties of this sort."
- > "22% of repeat calls involve downstream issues related to the problem that prompted the original
  > call, even if that problem itself was adequately addressed the first time around."
- > "81% of the customers who had a hard time solving their problems reported an intention to spread
  > negative word of mouth."
- > "65% are likely to speak negatively" / "23% of customers who had a positive service interaction told
  > 10 or more people about it" / "48% of customers who had negative experiences told 10 or more others"
- Case testimonials, no method: > "Osram Sylvania has lowered its Customer Effort Score from 2.8 to
  2.2—18.5% below the average we see for B2B companies." and a claim of "$1.2 million" in process
  efficiencies at another company.

**FIGURE-CLASS FLAG (charter rule: flag the class, not the string).** A large and under-appreciated
share of the "customer experience statistics" that circulate in CS/support content marketing —
particularly the word-of-mouth-spread figures and the satisfied-but-leaving figures — trace to this one
2010 CEB survey of intentions. They are not independent corroborating data points; they are one
unpublished dataset cited many times. Any listicle presenting several of these as separate evidence is
double-counting a single source. Treat *any* stat of the form "X% of customers tell N people" or "X% of
satisfied customers still leave" as belonging to this class until traced.

Also in this class, and worth a specific mention: the article's own framing that "customer service can
do little to increase loyalty" is a claim about *contact-center interactions only*, generalized by the
authors on the explicit basis that it "makes intuitive sense" (quoted in §1.1). That is an admitted
extrapolation, not a finding.

---

## 2. The peer-reviewed replication that reverses the CES claim (PRIMARY TEXT READ: YES)

**Source:** Evert de Haan, Peter C. Verhoef, Thorsten Wiesel, "The predictive ability of different
customer feedback metrics for retention", *International Journal of Research in Marketing* 32(2), June
2015, 195–206. DOI 10.1016/j.ijresmar.2015.02.004.
Publisher: https://www.sciencedirect.com/science/article/abs/pii/S0167811615000324
**Open full text obtained at: https://pure.rug.nl/ws/files/17052354/In_press_version_IJRM.pdf**
GOTCHA worth recording: `research.rug.nl/files/…` (the portal host) is behind a Cloudflare challenge
and returns an HTML "Just a moment…" page even with a full Chrome header set; **`pure.rug.nl/ws/files/…`
serves the same PDF with a plain curl.** Same file ID, different host.

### 2.1 Design — this is the design the 2010 CES article did not have

> "The data were collected for an annual study on customer performance of Dutch service firms in
> September 2010… In total, 6649 respondents filled out the survey, providing a total of 8924 firm
> evaluations (i.e., 1.34 firm evaluations per respondent) for 93 firms across 18 industries."

> "In November 2012—two years after they answered the initial survey—respondents received a request to
> participate in a follow-up survey. The subsequent survey asked whether the respondents remained
> customers at the firm for which they completed the first questionnaire. Among the 8924 firm responses
> from 6649 unique responders of the first survey, 1308 unique responders also filled out the second
> survey, providing us with 1375 firm responses (i.e., a 15.4% response rate)… From the 1375 firm
> responses, 370 (26.9%) customers churned within the two years between the surveys."

Key design facts:
- **Outcome is self-reported ACTUAL retention two years later**, not intention. This is the crucial
  upgrade over Dixon et al.
- Multi-level probit with a **bivariate-probit self-selection correction** for who answered wave 2.
- Out-of-sample validation on a one-third holdout, judged on **Gini coefficient, top-decile lift, and
  hit rate** — real churn-modelling criteria.
- The paper is explicit that this is what distinguishes it: > "we predict actual future performance, in
  contrast with other studies that investigate only same-period correlations (e.g., Anderson, Fornell,
  & Mazvancheryl, 2004; Keiningham, Cooil, Andreassen, & Aksoy, 2007)."
- **CES coverage limit, verbatim:** > "We also have CES data for 20.5% of the sample; 79.5% of the
  customers had not contacted the firm with a request and thus could not provide a CES."

**Grade: MEASURED-WITH-METHOD.** The strongest single piece of evidence I found in this slice.

### 2.2 Table 5, correlation matrix (n = 1375) — verbatim values, retention column

| Variable | r with retention (2 yrs later) |
|---|---|
| (2) Satisfaction | .151** |
| (3) Top-2-box satisfaction | **.184**\*\* |
| (4) NPS official | .170** |
| (5) NPS value | .159** |
| (6) CESyes (did the customer contact us at all) | .085** |
| (7) CES | **−.073**\*\* |
| (8) **Relationship length** | **.199**\*\* |

(** p < .01. Reproduced from the extracted PDF text.)

### 2.3 CORRECTION TO A WIDELY REPEATED SECONDARY FRAMING — read this before citing CES

A popular secondary source (MeasuringU, https://measuringu.com/customer-effort-score/) describes this
result as: "they found the CES was a terrible predictor and actually had a negative correlation
(r = −.073) with two-year retention." The *value* is correct, but **"actually had a negative
correlation" is misleading about the sign's meaning**, and we must not repeat that framing.

In the 2010 CES scale used by this paper, **1 = very low effort and 5 = very high effort**, so more
effort is worse. A *negative* correlation with retention is therefore the **theoretically correct
direction** — high-effort customers churned more. The finding is not that CES pointed the wrong way;
it is that **CES pointed the right way but weakly**, and much more weakly than satisfaction or NPS.
The authors say so themselves, verbatim:

> "In addition, the CES significantly correlates with retention, but it is considerably lower than the
> correlation of the other CFMs."

This is a live example of the charter's laundering hazard: a secondary source turned "weak but correctly
signed" into "negative, i.e. broken". If our pack states the CES result, it must state it as *weak*, not
*inverted*.

### 2.4 The authors' actual conclusions, verbatim

> "Our results show that the top-2-box customer satisfaction score offers the single-best predictor of
> retention across industries. In general, transforming scales of the CFMs to capture the proportion of
> most satisfied customers (as is done with the top-2-box customer satisfaction) or splitting customers
> up into groups (as is done with the promoters and detractors of the NPS) is preferable to using the
> full scale of the CFMs. In addition, our results show that **the CES in itself has little to no
> predictive power and performs the worst of all CFMs studied.** Which CFM performs best in predicting
> retention is however industry dependent…"

On the sub-sample for whom CES was designed (customers who actually contacted support):
> "Table 9 shows that even for this sub-sample of customers, for whom the CES was especially designed,
> the CES is the only CFM that performs worse than the baseline model in terms of the AIC… Yet, by quite
> a large margin, CES is still the worst-performing CFM. Thus, even for the group for which the CES was
> designed, it is still outperformed by the other CFMs."
(Note their own caveat: n = 282 for the retention equation in that sub-sample — small.)

Out-of-sample:
> "In terms of out-of-sample fit, all models perform better than the baseline model for all three
> out-of-sample fit criteria, with the top-2-box customer satisfaction performing best on both the Gini
> coefficient and the hit rate and the official NPS having the highest top-decile lift."

And a finding directly relevant to whether we should teach a single headline metric:
> "A dashboard of CFMs that measure different dimensions… is preferable to monitoring a single CFM."

### 2.5 THREE FINDINGS HERE THAT SHOULD SHAPE THE PACK

1. **Tenure beat every sentiment metric.** Relationship length correlates .199 with retention — higher
   than top-2-box satisfaction (.184), the official NPS (.170), and roughly 2.7× the CES (−.073 in
   magnitude). The single best cheap predictor of whether a customer stays is **how long they have
   already stayed**. For a solo builder with no survey programme at all, this is liberating and it is
   measured. It also predicts the shape of an honest health score: tenure and behavioural variables
   first, sentiment second.
2. **Extremes beat averages.** Top-2-box outperformed the full-scale mean satisfaction (.184 vs .151),
   and the paper's own summary of its conceptualization is that "the 'part of the scale used' dimension
   is the most important." Teaching "track your average CSAT" is teaching the weaker statistic.
   Verbatim: > "We clearly find that the top-2-box customer satisfaction and the official NPS, which
   focus on the extremes, outperform the CFMs that use the full scale."
3. **Effect sizes here are SMALL in absolute terms.** The best correlation with two-year retention in
   the entire study is .199, and the best CFM is .184 — that is roughly 3.4% of variance. Any pack
   claim of the form "measure X and you will know who will churn" is unsupportable at these magnitudes.
   This is the empirical backbone for the health-score-humility wedge (charter hypothesis 2).

### 2.6 The second replication — OBTAINED, and it does NOT say what the footnote implies

De Haan et al.'s Table 1 footnote states, verbatim:
> "Van Doorn et al. (2013) test predictive power but find no significant effects of the CFMs."

I obtained the primary and **that characterization is too strong** — recording the correction here so we
never ship the footnote's version.

**Source:** Jenny van Doorn, Peter S.H. Leeflang, Marleen Tijs, "Satisfaction as a predictor of future
performance: A replication", *International Journal of Research in Marketing* 30(3), Sept 2013, 314–318.
Published in IJRM's **Replication Corner** (Replication Editor: Donald R. Lehmann) — i.e. this is a
formally designated replication study, which raises its evidentiary weight.
Open full text: https://pure.rug.nl/ws/files/119301784/Satisfaction_as_a_predictor_of_future_performance_A_replication.pdf
(same `pure.rug.nl` trick as §2.1; the `research.rug.nl` host is Cloudflare-gated.)
**PRIMARY TEXT READ: YES.** Local copies `/tmp/dlead/vandoorn2013.pdf`, `vd.txt`.

**Design, verbatim:**
> "A professional market research agency collected data on customer metrics by means of an
> internet-based survey in 2008 which contains 11,967 responses. These responses refer to 46 companies
> in the banking, insurance, utilities and telecom industries. On average, we obtain 260 customer
> responses per company, ranging from 42 respondents for a small firm to 558 customers for a larger one."

Metrics compared: overall satisfaction, top-box satisfaction, multi-item satisfaction, the official NPS,
an "alternative NPS" (adjusted for Dutch respondents scoring lower — they note "an 8 [may already be a
promoter in NL]"), and repurchase/loyalty intentions. Outcomes: **sales revenue growth, gross margins,
and net operating cash flows** — i.e. real firm financials, 2008 and 2009, not survey intentions.
Significance testing between metrics uses partial correlations adjusted for industry, compared with the
Meng, Rosenthal & Rubin (1992) test.

**Findings, verbatim (abstract):**
> "We find that all metrics perform equally well in predicting current gross margins and current sales
> revenue growth and equally poor for predicting future sales growth and gross margins as well as
> current and future net cash flows. **The NPS is neither superior nor inferior to other metrics.**
> Taken together, our study suggests that the predictive capability of customer metrics, such as NPS,
> for future company growth rates is limited."

And from the discussion:
> "We fail to find significant differences between the partial correlations, implying that all our
> metrics predict these outcome measures equally well. **We therefore have to conclude that there is no
> single best metric.**"

> "Taken together, our study suggests that the predictive capability of customer metrics, such as NPS,
> for future sales growth or gross margin is limited. The customer metrics included in this study
> perform equally well in predicting current company performance."

**The correction that matters:** van Doorn et al. did *not* find "no significant effects". They found
the metrics **do** relate to *current* performance, and fail on *future* performance — and that no
metric beats any other. They explicitly contrast themselves with an earlier study on this point:
> "Another notable difference is that Morgan and Rego (2006) fail to find a significant effect of the
> NPS on performance metrics, **while we do.**"

So the honest summary for our pack is: *customer feedback metrics are contemporaneous descriptions, not
forecasts, and the choice among them is close to arbitrary.* That is a more useful and more defensible
claim than "they don't work", and it is exactly the kind of over-flattening the charter warns about.

**Bonus cross-check for the Keiningham strip (worker w2's territory).** Van Doorn et al. quote
Keiningham et al. (2007) directly, with a page cite — useful corroboration that w2's NPS strip lands:
> "…and Aksoy (2007) employ data from the Norwegian customer satisfaction barometer and do not find
> evidence that 'average levels of any of the satisfaction/loyalty metrics … are significantly
> correlated with the relative change in revenue…' (p. 42)."

---

## 3. Customer education / academies — the evidence is self-selection all the way down

Searched for measured evidence that customer education (academies, certification, structured training)
causes retention or adoption. **Result: I found no measured evidence. Every claim located was vendor
content marketing with an uncontrolled comparison.** Representative claims encountered, all
**VENDOR-FOLKLORE / METHOD-UNKNOWN**, sources being LMS and CS-platform vendors (Intellum, WorkRamp,
Thought Industries, Absorb, Gainsight, virtualbadge.io, saasacademyadvisors.com):

- "trained customers show 40% higher retention rates" — no n, no source, no comparison group stated.
- "customers enrolled in online training have an NPS of 8.2 compared to overall scores of 6.7" — note
  this is not even an NPS (NPS is a −100..+100 net score, not an 8.2); the figure is an average rating
  mislabelled as NPS. A metric-name error of this kind is itself a reliability signal about the source.
- "A customer who has invested time in becoming certified is far less likely to churn."

**The structural problem, which is the actual finding worth shipping:** every one of these compares
customers who *opted into* training against those who did not. Opting into training is a direct
expression of the engagement and intent that predicts retention anyway. Without randomization, a
matched control, or at minimum a pre-period-usage control, the entire measured gap is consistent with
pure selection. This is the same confound family as "users who use feature X retain better, therefore
drive users to feature X" — a confound the sibling `growth` pack owns experimentally.

**Pack implication:** we can honestly teach customer education as a *cost and coverage* play (it
answers questions once instead of N times, it scales to a solo operator) without claiming a retention
lift. Claiming the retention lift requires an experiment, and that experiment belongs to growth.
**SEAM FLAG (growth):** "does an education intervention cause retention" is a retention EXPERIMENT
(growth per charter) whose EXECUTION (building and maintaining the academy/docs) is success. Seam
question for the controller: does success get to state the *measurement caveat* itself, or does it hand
the question to growth with a pointer?

---

## 4. VoC survey method — nonresponse and the shape of who answers

Grade: PRACTITIONER / TEXTBOOK. I did not obtain a customer-service-specific measured study of
nonresponse bias in the time available, so the following is recorded at the grade I can defend.

The structural argument, which is uncontroversial in survey methodology: satisfaction surveys suffer
**nonresponse bias** (who chooses to answer differs systematically from who does not) and **extreme
responding** (the very happy and the very angry answer; the ambivalent middle is silent). Both push a
CSAT number away from the population value, and the direction is not fixed — it depends on whether the
disengaged-and-leaving cohort is over- or under-represented among non-responders. Customers who have
already mentally churned are among the least likely to spend time on a survey, which biases a
satisfaction estimate *upward* precisely when you most need it to be accurate.

One genuinely measured, if out-of-domain, anchor exists: **"Evidence of non-response bias in the
Press-Ganey patient satisfaction survey"** (PMC4972948, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4972948/)
— a healthcare-satisfaction-survey study of nonresponse bias. **PRIMARY TEXT NOT OBTAINED.** Flagged as
the best candidate for a measured citation if we want one; healthcare satisfaction surveys are the one
domain where this has been studied properly, and the transfer to SaaS CSAT would need to be stated as
an analogy, not a result.

**The connection to §2 that makes this matter:** de Haan et al.'s own wave-2 response rate was **15.4%**,
and they considered self-selection serious enough to build a bivariate-probit correction for it. If a
peer-reviewed team treats a 15.4% follow-up as requiring an explicit selection model, a solo builder
reading a 12-response CSAT dashboard should be told plainly that they are looking at a sample of the
engaged, not a measurement of the base.

**Never-ship candidate (figure-class):** published "CSAT benchmark tables" and "average NPS by industry"
tables. These aggregate across wildly different sampling frames, response rates, trigger points
(transactional vs relational), and scales, and essentially never publish response rates. Comparing your
number to them is not a comparison. Flag the CLASS, not the specific table.

---

## 5. Touch models / when a success function applies at all (§1033 conditional) — PARTIAL, low grade

Scouted only; handing the depth to no one, so recording what I have with honest grading.

The canonical practitioner segmentation is **high-touch / low-touch / tech-touch (digital)**, with
customers-per-CSM ratios cited from roughly **15:1 at high touch to 1000:1+ at digital touch**, and ACV
bands used as the segmentation cut. All sources located were **VENDOR / METHOD-UNKNOWN** (Gainsight,
Velaris, EverAfter, userflow, CSM Practice, Customer Success Collective). One figure encountered —
"39% of participants set their low-touch threshold at $50k" (CSM Practice, https://csmpractice.com/how-low-can-you-go-customer-success-for-your-smb-segment/)
— is a community-poll number with **no n and no sampling frame stated**; do not ship it.
**PRIMARY TEXT NOT OBTAINED for any ratio figure.** Worker w1 (canon + commercial) was tasked with
CSM ratios and benchmark-report method; defer to that file.

**What I could NOT find, and this is itself the finding:** I found no source that establishes *at what
point a distinct customer-success function becomes worth having*, versus the work being absorbed by
docs, product, and automation. The entire literature assumes the function already exists and asks only
how to staff it. That absence is direct support for charter wedge hypothesis 1 and for the §1033
conditional: the pack will have to *construct* the "do you even need this yet" gate, because the canon
does not contain one. Recording as an open question rather than a claim.

---

## 6. Customer-to-product feedback loops — a canonical Include with no literature behind it

This is one of the pack's 12 canonical Includes, so I checked whether any first-hand or measured
treatment exists. **It does not.** The searchable literature on "turning customer feedback into the
product roadmap" is, without exception in what I surveyed, content marketing by feedback-aggregation
tool vendors: Chattermill, Enterpret, Productboard, Birdie, Fullstory, Quackback, Tendril, customers.life.
Grade for the entire territory: **VENDOR-FOLKLORE / METHOD-UNKNOWN.**

The *process* content they converge on is nonetheless coherent and matches practitioner reality —
centralize feedback from all touchpoints (tickets, calls, interviews, surveys, usage), deduplicate
aggressively, tag against a standardized taxonomy, score against explicit criteria (importance ×
feasibility × strategic alignment), segment by customer value, and close the loop back to the requester.
None of it is validated; all of it is reasonable. We can teach the mechanics as **craft**, not evidence.

**FIGURE-CLASS FLAG — the recurring unsourced "40%".** This search surfaced "companies with structured
feedback triage resolve **40% more** customer issues"; the customer-education search in §3 surfaced
"trained customers show **40% higher** retention". Neither carries an n, a comparison group, or a source.
Note the pattern: an unattributed "40%" uplift attached to whatever practice the vendor sells. Add the
CLASS to the never-ship list — *any* bare "X% more/better" attached to adopting a practice, with no
comparison group named — rather than only the two strings I happened to catch. This directly instantiates
the charter's twice-learned rule that the never-ship LIST is not the RULE.

**SEAM FLAG (product).** The `product` pack's doc evidence map already routes "adoption, support,
satisfaction, and churn evidence → /success", and product cedes adoption. But *prioritizing* a feature
request is a product decision. Question for the controller: does success own the **collection,
deduplication, and routing** of customer feedback (the loop's plumbing) while product owns the
**prioritization call**, with the seam at "a structured, deduplicated, evidence-tagged request lands in
product's queue"? That reads as the clean cut, but success must not be taught to score roadmaps.

## Open questions

1. ~~van Doorn, Leeflang & Tijs (IJRM 2013) — obtain the primary~~ **CLOSED 2026-08-02**, see §2.6.
   Primary obtained; de Haan et al.'s footnote characterization was too strong and is corrected there.
2. Is there a post-2015 replication of de Haan et al. in a B2B SaaS setting? Everything here is Dutch
   B2C services, 2010→2012. Scope limit must travel with the citation.
3. CES 2.0's rewording rationale from a primary CEB/Gartner source (I have only Sauro's observation).
4. A measured nonresponse-bias study in a *software* CSAT/NPS context, not healthcare.
5. Does anyone publish a health score validated out-of-sample (Gini/lift/hit rate) the way de Haan et al.
   validate CFMs? (Worker w2 owns this; if the answer is no, that is the flagship.)

## Seam flags (recorded WITH the question attached; not assigned)

- **growth** — education/onboarding interventions: success EXECUTES (builds the academy, sends the
  message), growth EXPERIMENTS (does it cause retention). Question: who states the selection-bias
  caveat when success reports an education "result"? See §3.
- **growth / data** — health-score model validation (holdout, Gini, lift) is measurement craft. Does
  success teach the honest *interpretation* ("what a score can predict") while data owns validity, by
  analogy to growth's shipped "data owns validity" ruling? See §2.5.
- **product** — "top-2-box beats the mean" and "tenure beats sentiment" are measurement rulings that
  affect any product-side satisfaction dashboard. Question: does success own the CFM choice, or only
  its use in the relationship?
- **marketing** — the word-of-mouth figures in §1.3 (23%/48% told 10+ people) are advocacy/WOM claims
  that marketing may also cite. Question: whoever ships a never-ship list for this figure-class, both
  packs should point at one list.
