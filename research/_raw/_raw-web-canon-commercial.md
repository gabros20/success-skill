# _raw-web-canon-commercial — channel D (web-research)

Scope: T1 (CS canon + methodology) and T2 (commercial mechanics: NRR/GRR, renewals, expansion, VoC).
Grading: MEASURED-WITH-METHOD / PRACTITIONER-REPORT / VENDOR-FOLKLORE / METHOD-UNKNOWN.
Per charter rule 2: every load-bearing number below was read from downloaded text (SEC filings via curl
+ python3 HTML-strip) or from a direct WebFetch quote-extraction, never trusted from a summarizer alone
for magnitude. SEC filings required a declared UA (`Research research@example.com`) — the bare Chrome UA
the charter suggests for other sites gets a 403 "Undeclared Automated Tool" page from sec.gov; this is
a **gotcha worth flagging to the crew**: SEC wants `<org> <email>`, not a browser UA.

---

## T1 — The CS canon and its methodology

### 1. "Customer Success" (Mehta, Steinman, Murphy; Wiley, 2016) — CANON-WITH-INTEREST

**Authorship / interest**: written by Nick Mehta (Gainsight CEO), Dan Steinman (Gainsight CCO at the
time), and Lincoln Murphy (independent consultant, third author). Gainsight is a customer-success
software vendor; two of three authors were Gainsight executives when it was written. Treat the whole
book as vendor content marketing with real practitioner value, not as evidence.
— PRACTITIONER-REPORT / vendor-interested. Source: https://www.amazon.com/Customer-Success-Innovative-Companies-Recurring/dp/1119167965 (publisher/author metadata); cross-checked against multiple listings (O'Reilly, AbeBooks).

**Origin story (Vantive/Salesforce)**: I could not get first-hand text from the book itself (no legal
full-text access found). Best available secondary account, cross-referenced across a Wikipedia article on
Vantive (software) and CS-history blog posts surfaced in search: Vantive (a CRM vendor, later acquired by
PeopleSoft) is credited with creating one of the first "Customer Success" groups circa 1996–97 under CEO
John Luongo with Marie Alexander leading it, tying CSM compensation to customer outcomes. Salesforce is
credited with later (~2005) building a large "Customers For Life" team focused on retention/adoption/
upsell under similar logic. — PRACTITIONER-REPORT, secondary sourcing only (I did not independently verify
the Vantive/Salesforce claim against a primary contemporaneous 1996–2005 document; this is the book's own
told-and-retold origin myth, repeated by CS blogs). Flag: **not independently verified — trace to primary
if this becomes load-bearing in the skill.** Sources: https://en.wikipedia.org/wiki/Vantive_(software);
secondary CS-history posts (customersuccessassociation.com, smartkarrot.com) surfaced by WebSearch — not
individually fetched/verified.

**The "10 Laws of Customer Success"** — best available verbatim-adjacent source is a 2015 CMSWire
write-up of the PulseCon (Gainsight's own conference) talk unveiling the book's structure, fetched directly
(not summarized-only):
1. "Customer success is a top-down, company-wide commitment"
2. "Know how to sell to the right customer"
3. "The natural tendency for customers is toward churn"
4. "Customers expect success"
5. "Measure and manage your customers"
6. "You can't build loyalty through personal relationships"
7. "Product has to be the priority"
8. "Obsessively improve time-to-value"
9. "Understand the details of churn and retention"
10. "Become metrics-driven"

**Evidence grade: every one of the 10 laws is presented as ASSERTION, not measured claim.** The CMSWire
article contains zero data, citations, or studies backing any law — confirmed by direct read, not just
the WebFetch summary (I inspected the returned extraction structure and it explicitly notes "no
quantitative data ... supporting any of the laws"). Steinman is quoted noting CS "historically lived in a
fuzzy world" — an implicit admission the laws are practitioner heuristics, not research findings.
— VENDOR-FOLKLORE (internally coherent, zero cited evidence). Source: https://www.cmswire.com/cms/customer-experience/10-laws-of-customer-success-pulseconf2015-029173.php
**assumes-a-team?**: YES, unambiguously. Laws 1, 2, 5, 9, 10 presuppose a CS function with headcount,
segmentation/scoring infrastructure, and a metrics practice — none of which a solo self-serve builder has.
Only laws 3, 4, 7, 8 translate cleanly to solo/self-serve (churn tendency, customer expectations, product
primacy, time-to-value) — these four are the honestly-portable subset.

### 2. Lincoln Murphy (sixteenventures.com) — PRACTITIONER-REPORT (his own first-hand pages, fetched directly)

**Customer Success definition** (current, 2024 restatement, verbatim from his own site):
> "When our customer achieves their Desired Outcome through their Relationship with us, leading them to
> stay longer, buy more, and advocate for us."
Source: https://www.sixteenventures.com/customer-success-definition/

**Desired Outcome** (current formula, verbatim): "Goal + Appropriate Experience." Murphy explicitly notes
his OWN framework changed over time: "Before that it was, 'Required Outcome + AX.'" — meaning the classic
"Required Outcome + Appropriate Experience = Desired Outcome" formula the charter asked us to check is
Murphy's PRIOR (pre-2024) formulation, since superseded on his own site by "Goal + AX." **This matters**:
if the skill cites the "Required Outcome + Appropriate Experience" formula, it is citing an outdated
version of Murphy's own thinking — should cite current or explicitly date the older formula.
Source: https://www.sixteenventures.com/customer-success-definition/ (also cross-checked via
https://sixteenventures.com/appropriate-experience-required and https://sixteenventures.com/discover-desired-outcome, not independently re-fetched — WebSearch synthesis only for those two).

**Appropriate Experience (AX)** (verbatim): "Primarily the Interaction Content, Channel(s), and Cadence
that a customer segment requires to 'feel' successful." Source: same page.

**QBR critique** (his own page, fetched directly, verbatim quotes):
> "You don't have to do QBRs. Period. QBRs are not required."
He frames QBRs as a legacy artifact: they "come from a time when we didn't know much about our
customers," and most practitioners "do them wrong anyway ... more of something they're forcing on their
customers" rather than delivering value. His reframe: **"The question should be: Is a QBR part of the
Appropriate Experience for your customers?"** — i.e., QBR-as-ritual is wrong; QBR-as-one-possible-AX-choice
is fine. Source: https://sixteenventures.com/customer-success-qbr

**Health-score critique**: Murphy's critique (via his "Success Vector" alternative post, WebSearch-derived,
not independently re-fetched) is that the traditional Customer Health Score is "too much of a moment-in-time
snapshot; a lagging indicator" and that CS needs "a Key Success Indicator (KSI)" — forward-looking, not
backward-looking. — PRACTITIONER-REPORT, opinion not measured. Source: https://www.sixteenventures.com/success-vector/
(WebSearch-summarized only; flag for re-verification if load-bearing).
**assumes-a-team?**: Murphy's whole framework is explicitly team-agnostic by design — he pitches Desired
Outcome as applying "regardless of company size," and several of his posts target solo/small SaaS founders
directly. This is the CLOSEST thing in the canon to an honestly-portable-to-solo framework. Still, his QBR
and health-score critiques implicitly assume you HAVE a QBR practice or health-score system to critique —
i.e., his critique-target is enterprise CS, even though his prescription (Desired Outcome) is universal.

### 3. CSM ratios / book-of-business sizing

**Gainsight Horizon AI Labs (their own telemetry, fetched directly for methodology)**:
> "We compared a pool of 17,034 CSMs from our US-based customers using anonymized and aggregated data."
> Data source: "Gainsight has thousands of customers and tens of thousands of customer success managers
> that use Gainsight daily, so we have a substantial source of data in our platform."
Result: **median (50th percentile) ARR-per-CSM = $1.4M; 75th percentile = $4.2M.**
— **MEASURED-WITH-METHOD, but with a real selection-bias caveat**: n=17,034 is a genuine, large sample —
but it is Gainsight's OWN CUSTOMER BASE, i.e. companies large/mature enough to have already bought a CS
platform. This systematically excludes solo/self-serve builders and any company too small to run
Gainsight. No time period stated, no segmentation by ACV band published in what I could extract. Grade:
MEASURED-WITH-METHOD (real n, real data source) but SAMPLE IS VENDOR-CUSTOMER-BIASED — do not present as
representative of the whole market, and definitely not representative of solo/self-serve.
Source: https://www.gainsight.com/blog/gainsight-horizon-ai-labs-what-is-the-right-csm-to-customer-ratio/

Separately (from the same overall Gainsight research corpus, WebSearch-derived, not independently
re-fetched): "high touch averaged 22 accounts managed per CSM, mid touch averaged 49 accounts, low touch
averaged 144 accounts" by engagement tier. — METHOD-UNKNOWN in what I could verify (I did not confirm this
specific breakdown came from the same 17,034-CSM dataset or a different, unsourced report). Flag for
re-verification before citing this exact tri-tier number.

**Gainsight's own "$2M ARR per CSM" guidepost (fetched directly for methodology)**: on their explainer
blog, the number is explicitly presented as the author's personal heuristic, not data:
> "I continue to use the 'one CSM per $2M ARR' as my guidepost. I've seen nothing that disputes it in a
> meaningful way."
No survey, no n, no benchmark report cited on that page. Examples given (Marketo ~1:$8M, Gainsight itself
<$1M) are anecdotal, not benchmarked. — **VENDOR-FOLKLORE.** Source:
https://www.gainsight.com/blog/customer-success-csm-ratio/

**Vitally survey** (WebSearch-derived only, not independently fetched): "33% of companies surveyed replied
that one CSM to 10-25 paying customers was their current ratio" — a real survey claim but I did not verify
n, sampling method, or survey instrument directly. — METHOD-UNKNOWN pending direct fetch. Source:
https://www.vitally.io/post/what-is-the-golden-ratio-of-customer-success-managers-to-customers

**Segment-band ranges circulating in practitioner content** (Lyniro, thecscafe — not fetched directly,
WebSearch-synthesized): "1:5–15 enterprise (>$100K ACV), 1:20–75 mid-market, 1:100–500+ SMB with heavy
automation." — VENDOR-FOLKLORE / unsourced ranges, presented without methodology in the search snippets.
**assumes-a-team?**: the entire CSM-ratio literature is, definitionally, enterprise-CSM-team literature —
there is no such thing as a "CSM ratio" question for a solo builder. This whole territory is 100%
assumes-a-team; the honest solo-builder translation is "you have no CSM headcount, so 'coverage' has to
come from docs/automation/product signals" — which is exactly wedge hypothesis #1 in the charter.

### 4. QBR practice — canonical agenda + credible critique, both sides first-hand

**The critique (both practitioner and Gainsight's own guide acknowledge it)**: Murphy's critique above is
the strongest first-hand critique found. Separately, WebSearch turned up widely-repeated practitioner
language ("nobody wants your QBR" as a framing, "self-serving quarterly business reviews will only
alienate your customers") from vendor blogs (ChurnZero, Custify) that were NOT independently fetched —
treat these as PRACTITIONER-REPORT / restated folk wisdom, not verified quotes, since I could not confirm
exact attribution/authorship for the "nobody wants your QBR" phrase to a specific named practitioner.

**EBR rebrand**: multiple vendor glossaries (Totango, SmartKarrot, Matik, ZapScale — WebSearch-synthesized,
not individually fetched) converge on: EBR = "Executive Business Review," a rebrand/reframe of the QBR
toward strategic/executive-level, less-rigid-cadence framing, explicitly as a reaction against QBR-as-
box-checking-ritual. — PRACTITIONER-REPORT, vendor-glossary consensus, not a single authoritative source.
**assumes-a-team?**: YES — the entire QBR/EBR practice assumes a named account owner, a sales-assisted or
enterprise relationship, and a cadence-driven meeting culture. Zero translation to self-serve; this is a
clean "enterprise-only, does not apply to solo/self-serve" boundary call for the skill to make explicitly.

### 5. Onboarding / implementation methodology — TTFV

**Finding: no rigorous first-hand study located.** Every source WebSearch surfaced for "time-to-first-value
predicts retention" was a vendor content-marketing page (ClientSuccess, SundaySky, SaaSFactor, UserIntuition
— none independently fetched for verbatim quotes) making unsourced quantitative claims, e.g. "users who
activate within 3 days are 90% more likely to continue," "70% of SaaS customers churn within 90 days due to
poor onboarding," a case anecdote ("47 minutes to 12 minutes ... 18% retention improvement" — single
company, uncredited). **None of these carry an identifiable study, sample, or method** — this is exactly
the figure-CLASS the charter's falsification-strip rule warns about (a specific-sounding number with no
traceable source). — **VENDOR-FOLKLORE, all of it, as far as I could verify.** This is itself a finding:
TTFV-causes-retention is CS folk wisdom, not demonstrated research, at least not in anything surfaced by
search. If the skill uses TTFV framing, it should be framed as "widely believed, not measured" rather than
cited as fact.
**Enterprise vs self-serve distinction**: none of the sources found cleanly separated SOW/kickoff/milestone
enterprise implementation from self-serve activation — the "TTFV" framing is used identically for both in
the vendor content, which is itself sloppy and worth flagging: enterprise implementation timelines are
measured in weeks/months against contractual milestones; self-serve activation is measured in minutes/
session — conflating the two under one "TTFV" number (as most of this content does) is a category error.

---

## T2 — Commercial mechanics (primary sources)

### 6. NRR/GRR definitions — 4 primary filings, verbatim, downloaded and text-extracted (not WebFetch-summarized)

All four below were fetched via `curl -A 'Research research@example.com'` (SEC requires a declared
identity UA — bare Chrome UA returns a 403 "Undeclared Automated Tool" page, confirmed directly), then
HTML-stripped with python3 `re.sub`, then grep'd for the definitional passage. Every quote below is
verbatim from the extracted text, not a summarizer's paraphrase.

**Snowflake, 10-K FY2025 (period ended Jan 31, 2025)** —
https://www.sec.gov/Archives/edgar/data/1640147/000164014725000052/snow-20250131.htm
> "We monitor our dollar-based net revenue retention rate to measure this growth. To calculate this
> metric, we first specify a measurement period consisting of the trailing two years from our current
> period end. Next, we define as our measurement cohort the population of customers under capacity
> contracts that used our platform at any point in the first month of the first year of the measurement
> period. ... We then calculate our net revenue retention rate as the quotient obtained by dividing our
> product revenue from this cohort in the second year of the measurement period by our product revenue
> from this cohort in the first year of the measurement period. Any customer in the cohort that did not
> use our platform in the second year remains in the calculation and contributes zero product revenue in
> the second year."
Reported figure: "net revenue retention rate, which was 126% as of January 31, 2025." **Mechanic: single
TWO-YEAR window, one-shot ratio, no rolling monthly average.**

**Datadog, 10-K FY2020** —
https://www.sec.gov/Archives/edgar/data/1561550/000156459021009770/ddog-10k_20201231.htm
> "We calculate dollar-based net retention rate as of a period end by starting with the ARR from the
> cohort of all customers as of 12 months prior to such period-end, or the Prior Period ARR. We then
> calculate the ARR from these same customers as of the current period-end, or the Current Period ARR.
> Current Period ARR includes any expansion and is net of contraction or attrition over the last 12
> months, but excludes ARR from new customers in the current period. We then divide the total Current
> Period ARR by the total Prior Period ARR to arrive at the point-in-time dollar-based net retention
> rate[[, and average] the trailing 12-month point-in-time dollar-based net retention rates, to arrive at
> the dollar-based net retention rate.]"
Reported: "As of each of December 31, 2020 and 2019, our dollar-based net retention rate was above 130%."
**Mechanic: rolling 12-MONTH cohort, averaged over trailing-12-month point-in-time rates — materially
different mechanic from Snowflake's single 2-year snapshot.**

**HubSpot, 10-K FY2024** —
https://www.sec.gov/Archives/edgar/data/1404655/000095017025018873/hubs-20241231.htm
> "Net Revenue Retention is a measure of the percentage of recurring revenue retained from Customers ...
> [calculated] by first dividing Retained Subscription Revenue by Retention Base Revenue in the given
> period, calculating the weighted average of these rates using the Retention Base Revenue for the
> period, and then annualizing the resulting rates." Key terms: "Retained Subscription Revenue[:]
> Contractual Monthly Subscription Revenue of the same cohort of Customers as those that comprise the
> Retention Base Revenue at the end of the same month. Retention Base Revenue[:] Contractual Monthly
> Subscription Revenue of our Customers as of the beginning of each month."
Reported (3-year trend in the same filing): "Net Revenue Retention 102.2% 103.9% 110.3%" (most-recent-first
across three fiscal years). **Mechanic: MONTHLY cohort, revenue-weighted average, then ANNUALIZED —
a third distinct mechanic.** Also notable: HubSpot's metric is scoped to *subscription* revenue only
("Contractual Monthly Subscription Revenue"), explicitly excluding professional-services/other revenue.

**Klaviyo, S-1 (2023)** —
https://www.sec.gov/Archives/edgar/data/1835830/000162828023030618/klaviyoincs-1.htm
> "We calculate our Dollar-Based Net Revenue Retention rate, or NRR, by first identifying the cohort of
> customers as of twelve months prior to the date of determination. We then calculate the ARR from this
> customer cohort as of twelve months prior ... (Prior Period ARR), and the ARR from this customer cohort
> as of the date of determination (Current Period ARR). Current Period ARR includes any expansion, price
> increases, and customer subscriptions that are deactivated and subsequently reactivated during the
> applicable twelve-month period and reflects contraction or attrition over the last twelve months from
> this customer cohort, but excludes any ARR from new customers in the current period. We then divide the
> total Current Period ARR by the total Prior Period ARR to arrive at the point-in-time NRR. We then
> calculate the weighted average point-in-time NRR as of the last day of each month in the current
> trailing twelve-month period ... with the weightings determined by the total ARR at the end of each
> period."
**Mechanic: essentially the same rolling-12-month, monthly-weighted-average mechanic as Datadog** — but
notably ALSO explicitly counts "deactivated and subsequently reactivated" subscriptions as retained within
the window, a subtlety not spelled out in the Snowflake/Datadog/HubSpot text I extracted.

**Why this matters (the point of comparing four filings)**: all four call the metric "net revenue
retention," all four exclude new-customer revenue, all four are "dollar-based"/cohort-based — but the
MEASUREMENT WINDOW differs (2-year single snapshot vs rolling 12-month monthly-weighted average), the
SCOPE differs (HubSpot = subscription-only; Snowflake/Datadog/Klaviyo = usage-inclusive "product revenue"/
ARR), and edge-case handling differs (Klaviyo explicit on reactivations; others silent on it in the text I
captured). **A reported "126% NRR" (Snowflake) and a reported "131% NRR" (Datadog, per WebSearch synthesis
for FY2024) are NOT computed the same way and should never be compared as if they were** — this is the
single most concrete, well-evidenced claim in this whole file. Grade: MEASURED-WITH-METHOD (all four are
primary-source, audited-filing definitions — the "definitions differ" claim itself is not folklore, it's
directly demonstrated by the four verbatim quotes above).

**Neutral treatment of the definitional mess / gaming**: Dave Kellogg ("Lazy NRR is Not NRR," fetched
directly): distinguishes cohort-based NRR (his preferred, "resists manipulation... little to no room for
gaming") from what he calls "Lazy NRR" = `(starting ARR + net expansion) / starting ARR` computed off a
quarter's ARR bridge, which "compares net expansion within the current quarter to starting ARR for that
quarter" — a different, more gameable quantity that can be dressed up to look like true cohort NRR. He
gives no named-company examples of the lazy method in the piece — this is a methodological argument, not
a "gotcha" naming names. — PRACTITIONER-REPORT (ex-MicroStrategy/Business Objects/Host Analytics CEO,
well-regarded independent SaaS-metrics blogger, not vendor-employed at time of writing as far as I could
tell) — treat as informed opinion, not audited. Source: https://kellblog.com/2022/10/05/accept-no-imitations-or-subtitutes-lazy-nrr-is-not-nrr/

**SaaS-wide NRR benchmarks** (OpenView/High Alpha, Bessemer, KeyBanc — WebSearch-synthesized only, NOT
independently fetched, method/n unverified in this pass): commonly repeated framings — "100% NRR = good,
110% = better, 120%+ = best" (Bessemer, framed for growth-stage enterprise SaaS per the search synthesis)
and "median NRR sliding from ~105% (2021) to ~101% (2024)" (Benchmarkit/Maxio). — **METHOD-UNKNOWN pending
direct fetch of the primary report PDFs** — flag for re-verification before citing specific numbers; the
qualitative framing (100/110/120 tiers) is safe to cite as a widely-used heuristic, the specific
median-decline numbers are not verified to primary-report text in this pass.

### 7. Renewal mechanics

Sources found (GenieAI, BoldSign, ExpiryEdge, Spendflo, IronMarten, Zylo — legal/procurement-vendor
content, NOT independently fetched, WebSearch-synthesized only): consistent convergence that **auto-renewal
notice periods cluster at 30/60/90 days, with 30 the modal figure in standardized SaaS agreements and 60
a common buyer-protective negotiated target**; opt-in renewal (affirmative action required) is framed as
achievable "for smaller deals or when you have significant bargaining power." — **PRACTITIONER-REPORT /
vendor-content consensus, not a single authoritative primary source, method unverified.** I did not find a
first-hand SaaS company's own renewal playbook document (e.g. an internal ops doc or a named CS leader's
detailed playbook) — this remains thin. Flag: needs a stronger primary source than legal-content-marketing
sites if this becomes load-bearing.
**assumes-a-team?**: renewal *forecasting/risk-tier* practice (assigning renewal-risk tiers, running a
renewal pipeline in a CRM) assumes a CSM or account owner; the underlying CONTRACT MECHANIC (notice period,
auto- vs opt-in) does not — it applies identically to a solo builder's own ToS. Clean split to record.

### 8. Expansion signals

**Finding: every "signal predicts expansion" claim found is unsourced vendor content, no study behind any
of it.** Examples pulled by WebSearch, none independently fetched for verbatim: "active user count reaching
80–85% of plan allotment is the strongest signal for seat expansion," "a department head adding four new
users last week converts to seat expansion at a 65% rate," "companies that track customer health report a
20% increase in upsell opportunities." **None of these cite a study, a company, an n, or a method** — this
is squarely VENDOR-FOLKLORE, another instance of the figure-CLASS the charter warns about (specific-looking
percentages with zero traceable source). If the skill claims "usage-threshold triggers predict expansion,"
it should be framed as plausible-and-widely-believed-but-unmeasured, not cited as evidenced.
— VENDOR-FOLKLORE, all located claims.

### 9. Time-to-value / onboarding→retention evidence (T2 lens, mechanics angle)

Same finding as item 5 above (T1) — restated here because the charter also asks for it under T2's
"published study with a method." **None was found.** The related "rule-based health scores identify ~50-60%
of at-risk accounts correctly, ML models 70-85%" figure (from a renewal-management vendor blog,
digitalapplied.com, WebSearch-synthesized, not fetched) carries the same problem — a specific-sounding
accuracy percentage with no cited validation study, no confusion-matrix, no dataset description.
— VENDOR-FOLKLORE.

### 10. Voice of Customer (VoC) methods

WebSearch surfaced only generic vendor-blog listicle content (HelpScout, HubSpot, CustomerGauge,
SurveySparrow — none independently fetched) converging on: surveys, interviews, social listening, support-
ticket analysis, product usage data as the standard VoC channels, with the B2B-specific note that "the
customer" for VoC purposes should be defined as "the customer organization," not individual users. —
PRACTITIONER-REPORT / vendor-listicle consensus, no first-hand methodological source (e.g. an academic
VoC/Kano-method paper) located in this pass. This territory is under-researched relative to the others in
this file — flag as a gap.

---

## Falsification strip — trace results

- **"Costs 5–25× more to acquire than retain"**: traces to Frederick Reichheld's Bain-era work,
  specifically the lineage of Reichheld & Sasser, "Zero Defections: Quality Comes to Services," HBR,
  Sept–Oct 1990 (https://hbr.org/1990/09/zero-defections-quality-comes-to-services — article located and
  confirmed to exist via HBR/HBS/SSRN/Semantic Scholar cross-listing, but I did NOT get behind HBR's
  paywall to read the original text directly — **this is a gap, flagged**). The specific "5–25×" ratio
  itself does NOT appear verified against the primary 1990 text in what I could access; it is a commonly
  repeated modern paraphrase (per multiple secondary retellings, e.g. stealthagents.com,
  churnkey.co — none fetched directly) that generalizes what the original article actually reported as
  *industry-specific defection-reduction profit effects* (see next item), not a clean acquisition-cost
  multiple. **Verdict: likely a folklorized generalization of a real but different original claim — trace
  incomplete, HBR paywall blocks primary verification, recommend the skill NOT cite "5-25x" as if it
  were the article's own number.**

- **"5% retention increase → 25–95% profit increase"**: the ORIGINAL 1990 Reichheld/Sasser piece (per
  secondary synthesis, not primary-text-verified — same paywall gap) reported **per-industry, per-case
  figures**, not one universal range: "reducing the defection rate just 5% generates 85% more profits in
  one bank's branch system, 50% more in an insurance brokerage, and 30% more in an auto-service chain,"
  plus a named-company anecdote: "when MBNA America ... cut its 10% defection rate in half, profits rose
  ... 125%." **The commonly-cited "25-95%" range appears to be a later compression/generalization of these
  discrete case numbers** (the 1996 Reichheld book "The Loyalty Effect" is credited elsewhere with
  broadening this to a range) — again I could not verify the compression against Reichheld's own later
  text directly. **Verdict: the specific per-case numbers (85%/50%/30%/125%) look real, industry-specific,
  and non-generalizable; the "25-95%" universal range is a secondary flattening of them and should be cited
  with that caveat, not as a universal law.** Source (existence-confirmed, not full-text-read):
  https://hbr.org/1990/09/zero-defections-quality-comes-to-services

- **NPS "best predictor of growth"**: Reichheld's claim (2003 HBR "The One Number You Need to Grow") is
  academically DISPUTED with a real, citable replication study: **Keiningham, Cooil, Andreassen, Aksoy,
  "A Longitudinal Examination of Net Promoter and Firm Revenue Growth," Journal of Marketing, 2007**
  (https://journals.sagepub.com/doi/10.1509/jmkg.71.3.039). Per WebSearch synthesis of the abstract/citing
  sources (I did not access the full paywalled text directly — flag): the study used longitudinal data from
  ~21 firms and 15,500+ interviews (Norwegian Customer Satisfaction Barometer) and "failed to replicate
  [Reichheld's] assertions regarding the 'clear superiority' of Net Promoter" versus other satisfaction
  metrics (e.g. ACSI); NPS was "the best or second-best predictor in only two of five industries studied."
  — **This is a genuine MEASURED-WITH-METHOD academic counter-claim (real n, real journal, real replication
  design) and is the strongest single piece of evidence-grade material in this whole file** for the
  "health-score/single-metric skepticism" wedge. Grade: MEASURED-WITH-METHOD (secondary-verified; full text
  not read — recommend the skill cite this paper by name and let a reader pull the JSTOR/Sage copy rather
  than quoting it verbatim, since I have not read the primary text).

- **"96% of unhappy customers don't complain"**: untraceable / conflated. WebSearch found this exact
  figure attributed inconsistently to "1st Financial Training Services" in some retellings and to "Lee
  Resource" in others (Lee Resource's actual traceable claim, per multiple citing sources, is a DIFFERENT
  number — "for every complaint there are 26 other unhappy customers who stayed silent"). **Verdict:
  untraceable to one identifiable primary source; two distinct claims are being conflated in circulation.
  Kill this figure or cite it as "widely circulated, source disputed/conflated."**

- **"80% of revenue from 20% of customers" (Pareto/SaaS)**: traces cleanly to Vilfredo Pareto (1896 land-
  ownership observation, Italy) via Joseph Juran's 1950s extension of the "universal principle" to business
  ("80% of a company's revenue would come from 20% of its customers"). **Counter-evidence exists**: Byron
  Sharp's empirical marketing research (via "How Brands Grow" lineage) is credited (WebSearch synthesis,
  not directly fetched) with showing the real distribution is closer to "60/20" (20% of customers deliver
  ~60% of revenue, not 80%) across studied consumer brands — meaning the popular "80/20" figure likely
  overstates concentration versus what's been empirically measured, at least in the consumer-brand data
  Sharp's team studied (not necessarily SaaS/B2B). — Verdict: real historical origin (Pareto→Juran), real
  counter-evidence exists (Sharp), but I did NOT independently verify the Sharp figure against his primary
  text — flag if load-bearing.

- **Health-score accuracy claims ("50-60% rule-based, 70-85% ML")**: VENDOR-FOLKLORE, no method found —
  see item 9 above.

- **CSAT/CES benchmark tables**: not specifically chased down in this pass — **open question**, not
  covered; if the skill needs CSAT/CES industry-benchmark numbers, that's an unfinished trace.

- **"10× cheaper to deflect"** (AI-support-agent deflection cost claim): **not located in this pass** —
  open question, did not find a source making this specific claim to evaluate.

---

## Open questions (unresolved by this pass)

1. Did not get behind the HBR paywall for the 1990 Reichheld/Sasser article — the "5-25x" and "25-95%"
   traces are existence-confirmed but not primary-text-verified. Whoever finalizes the falsification strip
   should get the actual PDF (HBR sells reprints; a library/EZproxy access or a Google Scholar cached PDF
   may work).
2. Did not get behind the Journal of Marketing paywall for Keiningham et al. 2007 — same caveat; this is
   the single strongest citable academic counter-claim found and deserves a primary-text read before the
   skill quotes specifics from it.
3. Bessemer/OpenView/KeyBanc SaaS-benchmark NRR-tier numbers (100/110/120% framing; median NRR decline
   2021→2024) were WebSearch-synthesized only, not fetched from the primary PDF reports — needs direct
   verification before citing specific numbers (the qualitative 100/110/120 framing is safe to use as "a
   widely-used heuristic tier system," the median-trend numbers are not verified).
4. Renewal-mechanics and VoC-methods territories are thin — I found only vendor-content-marketing
   consensus, no first-hand practitioner playbook or academic source. If these become load-bearing sections
   of the skill, they need another research pass with better sources (maybe a practitioner's own detailed
   renewal-ops writeup, or an academic VoC/Kano-method paper).
5. The Vantive/Salesforce CS origin story is repeated across several CS-history blogs but I did not
   verify it against a primary 1996-2005-era document — treat as folklore-with-a-plausible-kernel until
   someone traces it properly.
6. Gainsight's "high touch 22 / mid touch 49 / low touch 144 accounts per CSM" tri-tier figure needs
   re-verification — I could not confirm it came from the same 17,034-CSM telemetry dataset as the
   $1.4M/$4.2M ARR figures, or from a separate, less-sourced report.

## Seam flags (straddle another pack — recorded WITH the question, not assigned)

- **CSM ratios / book-of-business sizing is 100% enterprise-CSM-team literature** with zero honest
  solo-self-serve translation existing in the practitioner literature I found. Seam question for the
  controller: does the skill invent the solo-translation itself (wedge hypothesis #1), or is there a
  sibling pack (automation? product?) that already owns "how do I get CSM-equivalent coverage with zero
  headcount"? I did not find prior art for this translation anywhere in this pass.
- **Renewal mechanics (auto-renewal notice periods, opt-in) is fundamentally a CONTRACT/LEGAL question**
  before it's a CS question — seam with whatever pack (if any) owns ToS/contract terms. Success owns the
  *workflow* (who gets notified when, risk tiering); the notice-period LENGTH itself is closer to a legal/
  ops decision. Flag for controller: does this belong partly to operate or a future legal-adjacent pack?
- **Expansion-signal detection (usage-threshold triggers, seat-growth patterns) is a PRODUCT-ANALYTICS /
  DATA problem** before it's a success problem — the signal itself lives in product telemetry; success
  consumes it to decide what to do. Seam with `/data` (instrumentation, telemetry) and `/growth`
  (experimentation on whether acting on the signal works) — charter already notes growth owns retention
  EXPERIMENTATION vs success owns EXECUTION; this territory (which SIGNALS are trustworthy at all) sits
  upstream of that split and nobody in the shipped seam inventory (per the charter's binding-seam-contracts
  section) has explicitly claimed "signal validity" as opposed to "acting on the signal."
- **NPS / health-score skepticism (Keiningham et al.) is also directly relevant to `/growth`'s and
  `/marketing`'s attribution flagships** per the charter's own note ("NPS claims ... growth already flagged
  the trace as open") — this file's Keiningham citation should be treated as confirming/strengthening
  growth's existing flag, not a new independent claim; whoever synthesizes should cross-link rather than
  duplicate.
- **AI-support-agent deflection-rate honesty**: I did not find sourceable material in THIS territory pass
  (T1/T2 as scoped) — this lives more naturally in channel B (x-practitioners) or channel C (github, AI
  support agent frameworks) per the charter's own channel assignment; noting its absence here so the
  synthesis doesn't assume it was covered.
