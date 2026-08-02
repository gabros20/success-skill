# _raw: support-ops craft + AI support agents 2024–2026 (channel D, web-research)

Charter binding: `success-skill/research/charter.md`. Every claim graded MEASURED-WITH-METHOD /
PRACTITIONER-REPORT / VENDOR-CLAIM / VENDOR-FOLKLORE / METHOD-UNKNOWN. Load-bearing numbers carry a
verbatim quote I actually saw + URL. WebFetch summaries were NOT used for any magnitude below —
everything numeric was pulled by curl (Chrome UA) and read as raw text/PDF, or is explicitly marked
as WebSearch-synthesis-only (not first-hand verified).

---

## TERRITORY 1 — SUPPORT OPERATIONS CRAFT

### 1.1 Ticket taxonomies / conversation categorization

- **Claim**: usable taxonomies keep Tier-1 categories mutually exclusive and under ~10 options, with
  an optional Tier-2 subtopic layer.
  Grade: VENDOR-CONTENT (support-tooling vendor blog, practitioner-adjacent but commercially
  interested — SwiftEQ sells a tagging product).
  URL: https://swifteq.com/post/ticket-tagging
  Quote seen (verbatim, via curl): "Keep this list short – fewer than 10 mutually exclusive options
  – to avoid decision fatigue and ensure consistency." (per WebSearch synthesis of the fetched page;
  page content confirmed to load at 200 but I did not re-extract this exact sentence from raw HTML
  before file write — **flag: not independently re-verified against the raw HTML dump**, treat as
  WebSearch-synthesis-grade, not curl-verbatim-grade, despite successful fetch.)
- **Why cardinality/mutual-exclusivity matters**: the failure mode named across multiple vendor posts
  is inter-agent disagreement — "one agent might tag a ticket as 'Login Issue' while another labels
  an identical request 'Account Access Problem,' making aggregated reporting unreliable." This is a
  repeated, plausible, but vendor-sourced claim (Sentisum/Supportbench-adjacent) — no measured
  inter-rater agreement number was found anywhere for tagging (see QA section: nobody measures this
  even for the QA rubric use case, let alone plain tagging). Grade: VENDOR-FOLKLORE.
- **Tag rot / who tags**: could not find a first-hand Support Driven community post (their own site
  search/archives were not reachable in this session — WebSearch surfaced only third-party summaries
  of "Support Driven" philosophy, never Support Driven's own original text). **Open gap**: Support
  Driven primary sourcing failed; territory assignment expected Support Driven writing specifically
  and I did not obtain it first-hand. Flag for another pass or channel B (x-practitioners / community).

### 1.2 SLA design

- **ITIL priority matrix (impact × urgency)**: definition confirmed via multiple secondary
  ITSM-vendor treatments (PagerDuty, NovelVista, TOPdesk, InvGate, FireHydrant) but the PagerDuty page
  itself rendered as JS-shell under curl (no extractable body text — confirmed by direct fetch,
  `pagerduty_priority.html` returned only tracking-script boilerplate, no article text reached before
  hitting client-side rendering). Grade: METHOD-UNKNOWN on the exact ITIL-canon wording; the
  **structural claim is uncontested across sources**: "Incident priority is defined as the
  intersection of impact and urgency of an incident," impact = "extent of business disruption... how
  many users are impacted, whether a critical business service is unavailable," urgency = "how
  quickly the fault needs to be resolved." (WebSearch synthesis of PagerDuty/NovelVista/TOPdesk
  pages, not curl-verbatim.) URL: https://www.pagerduty.com/resources/digital-operations/learn/incident-priority-matrix/
- **FRT critique found (PRACTITIONER-REPORT-adjacent, vendor blog)**: "when FRT is tracked closely
  and tied to performance evaluation, agents learn to stop the clock without starting meaningful
  work" — and the median-vs-average point: "because a few slow replies skew the average, the median
  is often the more honest number." Also: teams computing FRT "against wall-clock time are
  penalizing agents for overnight and weekend gaps entirely outside their control." Grade:
  VENDOR-CONTENT/PRACTITIONER-ADJACENT (source is a support-tooling blog synthesis, not one signed
  practitioner essay — treat as directionally right, not citable as a named author's claim).
  URL search trail: KlickFlow "First Response Time Metrics: Why They Mislead"; Querri "11 First
  Response Time Reporting Mistakes CS Teams Make."
- **Business-hours calendars, percentile vs average targets**: not independently confirmed with a
  primary source in this pass — this is standard SLA-tooling documentation (Zendesk/Freshdesk own
  docs) that I did not reach; flag as open.

### 1.3 QA rubrics — Klaus (Zendesk QA) and MaestroQA

- **Klaus/Zendesk IQS formula — MEASURED-WITH-METHOD (verbatim, curl-fetched, own vendor doc)**:
  "To calculate the IQS for a single conversation, add all ratings and divide by the maximum score
  multiplied by the total number of categories. Repeat this process with a representative sample of
  your tickets to determine the overall IQS for your support team."
  URL: https://www.zendesk.com/blog/customer-service/customer-success/customer-service-internal-quality-score/
  (local copy: `zendesk_iqs.html`, verbatim string located at the "calculate"/"formula" anchors in the
  extracted article body JSON, confirmed present in raw fetched HTML.)
  Grade caveat: this IS the method (arithmetic mean of normalized ratings) — MEASURED-WITH-METHOD for
  the *definition*; the accompanying benchmark number below is VENDOR-CLAIM.
- **IQS "industry benchmark" claim**: "The latest Customer Service Quality Benchmark Report sets the
  2023 IQS benchmark at 88 percent. Additionally, 48 percent of teams use conversation reviews to
  track their IQS." Grade: VENDOR-CLAIM (Zendesk citing its own/Klaus-adjacent benchmark report,
  source report not independently reached — treat 88% as marketing-grade, not measured-with-method
  from our vantage; we saw the citing sentence, not the underlying report's methodology).
  Same URL as above.
- **AutoQA**: "AutoQA is short for automated quality assurance... The platform filters for
  conversations with positive or negative sentiment, identifies interactions most in need of review,
  and supports both manual scoring and AutoQA workflows." Grade: VENDOR-CLAIM (WebSearch synthesis;
  the Klaus AutoQA whitepaper PDF at
  info.klausapp.com/hubfs/The-Future-of-Support-Conversations-Automation-AI-and-AutoQA-Klaus.pdf
  **could not be fetched** — curl timed out / returned no response twice. **Unverified first-hand.**)
- **MaestroQA sampling guidance — PRACTITIONER-REPORT grade (curl-verbatim, own vendor blog, but
  reports a customer-base statistic, not a marketing number)**:
  "While there are no rules around how frequently you should grade, 60% of MaestroQA customers
  surveyed grade between 1-5% of all interactions. The other 40% graded upwards of 5% of all
  interactions, but these tended to be smaller companies with a dedicated QA specialist on the team."
  "There are 3 main factors that determine how frequently you can grade: your team's headcount, the
  average difficulty of a ticket, and the team's ratio of junior:senior agents."
  URL: https://www.maestroqa.com/blog/cx-qa-scorecard-grading (local: `maestro_grading.html`)
  Also: "Some companies, like Handy, choose to grade only DSAT tickets — where the customer had
  indicated unhappiness with the way the ticket was handled" — and a companion post notes random
  sampling risks under-grading hard tickets: "if you randomly sample tickets for grading, it's easy to
  see how the harder tickets... get lost in an avalanche of easy tickets." Handy and WP Engine
  reportedly deviate from random sampling for this reason.
  URL: https://www.maestroqa.com/blog/how-to-build-a-qa-scorecard (local: `maestro_scorecard.html`)
- **Inter-rater reliability — THE WEDGE, CONFIRMED**: across every QA-methodology source fetched
  (Zendesk/Klaus IQS post, both MaestroQA posts, the Zendesk calibration article stub), **the term
  "inter-rater reliability" does not appear once**, and no source I reached publishes a Cohen's-kappa
  or agreement-rate figure for QA scoring. "Calibration sessions" are named as a practice (Zendesk has
  a `/blog/quality-assurance/wem/qa-calibration/` article; MaestroQA has "Call Calibration: What is It
  & What are the Benefits?") but I did not find any of them publish a MEASURED agreement statistic —
  calibration is prescribed as a ritual, never validated with a number. **This confirms wedge
  hypothesis 1/3 from the charter: QA "rubrics" in this industry have never been checked for whether
  two graders agree.** Grade: absence-of-evidence claim, MEASURED-ABSENCE (I positively searched for
  the term across the fetched corpus and found zero hits) — flag as a strong, honest finding, not
  overclaimed as "proof no one anywhere measures this."

### 1.4 Staffing models — Erlang C/A and async/multi-channel

- **PRIMARY SOURCE OBTAINED AND READ**: Gans, N., Koole, G., Mandelbaum, A., "Telephone Call Centers:
  Tutorial, Review, and Research Prospects," *Manufacturing & Service Operations Management* 5(2),
  79–141, 2003. PDF fetched directly (curl, Chrome UA, 200 OK, 2.2MB, valid PDF) from
  https://aviman.technion.ac.il/files/References/CCReview.pdf and converted to text with `pdftotext`
  (local: `gkm2003.pdf` / `gkm2003.txt`, 4707 lines). This is the canonical academic reference the
  charter asked for. Grade: MEASURED-WITH-METHOD (it's the primary academic tutorial itself).
- **Erlang C's assumptions, verbatim (p.14 of the paper, lines ~901–907 of extracted text)**:
  "common practice uses the M/M/N (Erlang C) queueing model to estimate stationary system performance
  of short – half-hour or hour – intervals. In doing so, the call center implicitly assumes constant
  arrival and service rates... Furthermore, the arrival process is assumed to be Poisson, service
  times are assumed to be exponentially distributed and independent of each other... and the service
  discipline is assumed to be first-come, first-served. **Blocking, abandonment, and retrials are
  ignored.**"
- **Erlang A (abandonment), verbatim (§4.2.2)**: "A model that incorporates both busy signals and
  abandonment is the so-called M/M/N/k+G queue. In this model, patience is defined as the maximal
  amount of time that the customer is willing to wait for service; if not served within this time, he
  or she abandons the tele-queue... A special case is the M/M/N/k + M queue, in which patience is
  assumed to be exponentially [distributed]... we shall refer to as 'Erlang A' ('A' for Abandonment...)."
  This matches the charter's framing exactly and is now sourced to the actual paper, not a summary.
- **Async/multi-channel — the paper's OWN honest limitation, verbatim**: "Our survey deals almost
  exclusively with pure telephone services. **To the best of our knowledge, no analytical model has
  yet been dedicated to truly multi-media contact centers**, though a promising framework
  (skills-based routing) and a few models that accommodate IVRs, emails and their blending with
  telephone services, will be described in Section 5." This is the paper's authors admitting, in
  2003, that Erlang-family queueing theory does not have a validated analytical treatment for
  email/chat/async support — i.e., the honest answer to "does Erlang C apply to async support" is:
  **the canonical paper itself says no general model existed even at time of writing**, and I found
  no more recent canonical replacement in this pass (a gap worth flagging, not asserting away).
- **Contact-center framing, verbatim**: "A current trend is the extension of the call center into a
  contact center. The latter is a call center in which agents and IVRs are complemented by services
  in other media, such as email, fax, web pages, or chat (in that order of prevalence)... requests
  for email and fax services can be 'stored' for later response and it is possible that, when
  standardized and well managed, they can be made significantly less costly than telephone services."
  This is the closest the paper gets to endorsing an async model — it notes storability/deferability
  as the key structural difference from synchronous telephony, without offering a queueing formula
  for it.
- **What does a solo/2-person team do instead?** Not answered by GKM 2003 (it predates modern
  helpdesk SaaS entirely). No credible primary source found in this pass that translates Erlang-style
  staffing math into practical guidance for 1–2 person async support. **Open question, flag for
  channel B (x-practitioners) or channel A (skills) — likely the honest answer is "nobody uses queuing
  theory at this scale; it's inbox-triage heuristics," but I did not find a source that says this
  explicitly and I will not assert it as fact.**

### 1.5 Deflection-rate honesty — CONFIRMED FLAGSHIP-WORTHY WEDGE

- **The core honesty problem, stated plainly across independent-feeling (though vendor-published)
  sources**: "Deflection rate measures the share of customer queries that never reached a human queue
  — it is a cost-avoidance metric, while resolution rate measures the share of problems the AI
  actually solved — it is an outcome metric." And: "the core issue is that deflection rate counts
  giving up the same as getting helped, and a chatbot that frustrates customers into closing the tab
  shows excellent deflection numbers and terrible retention." Grade: VENDOR-CONTENT (Twig, an AI
  support vendor, published this — but note the irony/self-interest cuts against inflating deflection,
  since Twig sells on resolution, so the critique is at least incentive-compatible for that vendor).
  URL: https://www.twig.so/blog/deflection-rate-vanity-metric-cx-numbers-that-matter
- **A concrete numeric example of the honesty gap (unverified-method, illustrative not measured)**:
  "A 90% deflection rate can hide a 40% resolution rate. Abandoned tickets count as 'deflected' even
  when the customer left angry." Grade: VENDOR-FOLKLORE (illustrative hypothetical, not a measured
  pair from a named deployment — treat as a plausible worked example, not evidence).
- **How deflection is "usually computed" and why each computation is invalid**: multiple sources
  independently describe the standard (bad) method as counting **KB article views, or help-center
  sessions that didn't end in a ticket, as "deflections"** — which cannot observe the counterfactual
  (did the customer actually get their answer, or did they give up, or go to a different channel like
  email/social, or come back later as a "new" ticket that isn't linked to the original session?).
  "True deflection means the customer found their answer and didn't contact you, not simply that they
  viewed an article." Grade: VENDOR-CONTENT, but this is the SAME honest structural critique the
  charter is looking for — nobody in this literature claims to observe the counterfactual; they all
  proxy it. No source found that runs a controlled/randomized measurement of true deflection (e.g., a
  held-out group without the KB article, compared on contact rate) — **this is itself the finding**:
  the field lacks a MEASURED-WITH-METHOD deflection number; every number found in this research pass
  is a proxy the source itself hedges.
- **Vendor deflection numbers actually claimed (for contrast, all VENDOR-CLAIM, all self-reported,
  zero independent verification found for any of them)**:
  - Decagon: "80% average deflection rate across its customer base" (aggregate marketing claim);
    per-customer case studies: Substack "resolve more than 90% of user questions without human
    intervention"; Fourthwall "resolving over 70% of tickets without a need for human eyes at all";
    Notion "ticket resolution time improved up to 34%... average ask for human rate of 3.4%";
    Rippling "chat deflection from 38% to 50%+ ... a 32% relative improvement." URLs:
    https://decagon.ai/case-studies/substack, /fourthwall, /notion (Rippling case study URL not
    independently re-fetched — sourced via WebSearch synthesis of decagon.ai case-studies index).
  - Ada: claims "resolve over 80%" / "up to 83%" automated resolution; published case studies range
    "70–84%"; **Ada's own ROI calculator uses a conservative 40% baseline** (i.e., Ada's own sales
    tooling implicitly concedes real deployments run far below the marketing headline). Ada's stated
    *definition* of "automated resolution" (via WebSearch synthesis of ada.cx guide — direct curl
    fetch returned HTTP 403, **not independently re-verified against raw HTML**): a conversation
    counts only if the AI agent (1) understood the actual inquiry ("relevant"), (2) gave a correct,
    policy-consistent answer ("accurate"), (3) engaged "appropriately and on brand" ("safe").
  - Zendesk AI: "doesn't publish a global cross-customer resolution benchmark" but cites per-customer
    case-study numbers in the "39%–66% range" on its AI marketing pages (WebSearch synthesis, not
    independently re-fetched from zendesk.com — the specific case-study page was not opened directly
    in this pass).
  - Sierra: "customers are seeing between 50-90% of their customer service interactions completely
    automated" (WebSearch synthesis of Sierra-adjacent secondary coverage, not Sierra's own page
    directly fetched in this pass — flag as not independently verified).
  - **Common thread, stated by independent secondary analysis (grade: VENDOR-FOLKLORE/aggregator,
    not primary, but the pattern itself is the useful finding)**: "vendor case studies cite 50 to 80
    percent automation, but real-world data from independent reviews lands closer to 20 to 45 percent
    for properly tuned deployments" and a cited "independent top-quartile benchmark: 58.7%" — **I
    could not trace this benchmark figure to a primary source**; it appears in secondary
    vendor-comparison-blog content (Lorikeet, an AI-support vendor itself) without a visible
    methodology. Do not treat "58.7%" as verified; it is a number-about-a-number, unsourced past one
    more layer of blog content.
- **Intercom Fin — the one fully-verified, load-bearing, PRIMARY-SOURCE definition in this section
  (curl-fetched directly from fin.ai's own help center, HTTP 200, verbatim text confirmed present in
  raw HTML)**:
  "Resolution definition: A resolution is counted when, following Fin's last answer in a
  conversation, the customer either confirms the answer was satisfactory (confirmed resolution), or
  exits the conversation without requesting further assistance (assumed resolution). Customers can
  confirm a resolution by: Entering an affirmative response such as 'Ok thanks', 'That helped' etc...
  Note: An outcome is only counted when Fin provides an actual answer to a customer's query. If Fin
  merely responds to a greeting, this is not considered an answer..."
  URL: https://fin.ai/help/en/articles/10772642-fin-ai-agent-resolutions (also cross-linked from the
  pricing page https://fin.ai/help/en/articles/13975800-fin-pricing-outcomes). Local copy:
  `fin_resolutions.html`.
  **This is commercially load-bearing**: Intercom bills $0.99 per counted resolution (per WebSearch
  synthesis of Gleap/aimdoc/featurebase secondary pricing writeups, not independently re-fetched from
  Intercom's own pricing page in this pass — the *definition* above is primary/verbatim; the *price*
  figure is secondary and should be re-confirmed against intercom.com directly before shipping).
  **The honesty gap, explicit**: "assumed resolution" — silence/exit — is counted the same as an
  explicit "that helped." This is exactly the KB-deflection problem transplanted into a billing
  metric: exiting without complaint is not the same evidence as confirming success, and Intercom's own
  definition concedes this by naming the category "assumed."

### 1.6 Status pages & incident comms craft (customer-facing half — SEAM with `operate`)

- **PRIMARY SOURCE, curl-fetched, Atlassian's own Incident Management resource site (200 OK, full
  article body extracted from a large JS-hydrated page — confirmed present, not WebFetch-summarized)**:
  URL: https://www.atlassian.com/incident-management/incident-communication
  Verbatim: "For issues that are still currently affecting your customers' ability to use your
  product, we recommend **never going more than one hour without sending an update**. You should also
  always indicate when to expect the next update." And on severity: "Whatever your thresholds are for
  incident severity, it's important to make a clear line in the sand (ideally around some sort of
  measurable metric). If you designate an incident at Sev 1, it's important for anyone on your team to
  be able to know exactly what that means... we recommend a zero-tolerance communication plan for any
  incidents involving security issues or data loss." And on channel choice: "We recommend teams use a
  dedicated status page as their primary incident communication solution... it's important to give
  your customers and colleagues a clear source of truth during an incident."
- **Severity levels (secondary/WebSearch-synthesis of Atlassian's handbook content, not independently
  re-extracted verbatim in this pass — flag)**: SEV1 = customer-facing service down for all customers;
  SEV2 = same service down for a subset; SEV3 = low impact, workaround available. Assessment questions
  cited: impact to customers, what customers are seeing, how many affected, when it started, how many
  support cases opened, other factors (public attention, security, data loss).
- **"What to say before you know the cause" / customer-facing vs internal postmortems**: I searched
  the fetched Atlassian page text directly for "before you know the cause," "internal postmortem," and
  "public postmortem" — **none of these exact phrases were found in the extracted text**, meaning this
  specific sub-question was NOT confirmed from the page I reached (I may have hit a different page in
  the handbook than the one covering blameless/public postmortems specifically — the handbook has a
  separate `/postmortems` section not fetched in this pass). **Flag as unconfirmed, needs a follow-up
  fetch of atlassian.com/incident-management/handbook/postmortems** if this pack wants the exact
  public-vs-internal-postmortem wording.
- **incident.io** — I attempted direct fetches of incident.io/guide/foundations/severities and
  incident.io/blog/incident-communication-best-practices; both returned HTTP 200 but with very short
  (19–44 line) bodies typical of JS-shell-only content — **no article text was extractable by curl**.
  WebSearch synthesis only (not verbatim-verified): "If severities answer 'how bad is this incident?',
  statuses answer 'how close are we to getting back to normal?'" Grade: METHOD-UNKNOWN /
  not-independently-confirmed for incident.io specifically — Atlassian is the stronger source in this
  pass.
- **SEAM FLAG (per charter instruction — do not silently assign)**: the charter states operate's
  `incident-response.md:159` and `decommissioning.md:186` cede "customer-facing incident comms,
  per-account outreach" to product/success. The material above (severity→comms cadence, the "never
  more than one hour" rule, status-page-as-source-of-truth) is squarely the CUSTOMER-COMMS half the
  charter asked success to own. The MECHANICS half (how incident severity is technically classified
  for on-call/paging purposes, postmortem-as-engineering-ritual) plausibly stays with `operate`. I am
  recording the seam question, not resolving it: **does "severity" itself belong to operate (the
  technical classification) while success only owns the translation of that severity into a customer
  message and cadence?** That distinction is clean in the Atlassian material (their comms guide
  clearly treats severity as an input the comms plan consumes, not something success invents) but the
  controller should confirm against operate's shipped `incident-response.md` before finalizing.

### 1.7 Knowledge base / help-content strategy

- **Self-service demand (VENDOR-FOLKLORE, unsourced-past-one-layer)**: "a survey by Higher Logic"
  reportedly found "84% of customers try to solve their issues independently before contacting
  support, and 79% expect businesses to provide self-service tools." I did not reach the Higher Logic
  survey itself — this is a number-about-a-survey found in a secondary aggregator. Not verified.
- **Measured deflection ranges (VENDOR-FOLKLORE, no method given)**: "true deflection from KB/
  self-service commonly ranges 10–30% of potential contacts in mixed-complexity environments, with
  high-performing programs achieving 30–50%..." and KB access "reduce average handle time, often by
  20 to 40 percent." No source publishes the underlying study design for either range. Grade:
  METHOD-UNKNOWN — these read as industry-consensus folk numbers repeated across content-marketing
  posts (umbrex, tidio, capacity, aisera, bolddesk), not a single measured study. **This reinforces
  1.5's finding**: nobody in the reachable literature has a controlled measurement of KB-driven
  deflection; every number is a proxy or an unsourced "commonly cited" range.
- Could not reach a first-hand Intercom/Help Scout "own ops post" on KB structure/staleness in this
  pass (Help Scout's customer-service-metrics page was fetched — 200 OK — but I did not extract its
  KB-specific content before time ran out on this sub-topic; **flag as an incomplete lead**, file
  `helpscout_metrics.html` is saved locally for a follow-up pass if needed).

---

## TERRITORY 2 — AI SUPPORT AGENTS 2024–2026

### 2.1 Klarna — dated timeline, PRIMARY sources only

**2024-02-27 — Original Klarna press release** (fetched directly via curl, HTTP 200, JSON-embedded
article body extracted and confirmed verbatim from the raw page — NOT a WebFetch summary).
URL: https://www.klarna.com/international/press/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month/
Local copy: `klarna_press.html`.

Exact claims, verbatim as they appear in the page's own content JSON:
- "The AI assistant has had **2.3 million conversations, two-thirds of Klarna's customer service
  chats**."
- "It is doing the equivalent work of **700 full-time agents**."
- "It is on par with human agents in regard to **customer satisfaction score**."
- "It is more accurate in errand resolution, **leading to a 25% drop in repeat inquiries**."
- "Customers now **resolve their errands in less than 2 mins compared to 11 mins previously**."
- "It's available in **23 markets, 24/7** and communicates in more than **35 languages**."
- "It's estimated to drive a **$40 million USD in profit improvement to Klarna in 2024**."
- Also present, and easy to miss: "Additionally, customers can still choose to interact with live
  agents if they'd prefer." — i.e., Klarna's own Feb-2024 release already stated an always-available
  human option existed, which matters for the escalation-policy question in §2.3 and for reading the
  2025 "reversal" accurately (see below — what did NOT reverse).
- Stated method for the "$40M profit improvement" and "25% drop in repeat inquiries": **NONE given**.
  The release states the numbers with no methodology, baseline period, or definition of "repeat
  inquiry." This is a VENDOR-CLAIM in the strongest sense — a company press release with no published
  method. Grade: VENDOR-CLAIM.

**2024-02-27 (same day) — Siemiatkowski's own X post**, quoted verbatim by an independent technical
blogger who read it directly (grade: PRACTITIONER-REPORT quoting a PRIMARY statement):
"In our case, customer service has been handled by on average **3000 full time agents** employed by
our customer service / outsourcing partners. Those partners employ **200,000 people**, so in the
short term this will only mean that those agents will work for other customers of those partners.
But in the longer term, as more companies adopt these technologies, we believe society needs to
consider the impact."
URL (secondary, quoting): https://blog.pragmaticengineer.com/klarnas-ai-chatbot/ (Gergely Orosz,
"Klarna's AI chatbot: how revolutionary is it, really?"). **Note the discrepancy worth flagging**:
the press release says the bot does the work of "700 full-time agents," while Siemiatkowski's own X
post the same day references a baseline of "3000 full time agents" for the whole customer-service
operation — these are not necessarily contradictory (700 could be the marginal headcount offset by
the bot out of a base of 3000), but no source I found reconciles the two numbers explicitly. Flag as
an internal-consistency question, not a resolved fact.

**2024-02-27ish — First independent hands-on test** (PRACTITIONER-REPORT, first-hand — the author
signed up and used the bot himself): Gergely Orosz's Pragmatic Engineer piece (same URL as above)
tested the bot directly and reported: "over the course of 15 minutes of probing, I could not get the
chatbot to hallucinate" and observed a live escalation trigger: "My first attempt to get the chatbot
to talk about non-shopping related topics led to a swift handoff to a human agent." He also notes a
prompt-injection example from a third party (Colin Fraser on X) where a user got the bot to generate
code — a documented jailbreak, contra the "safety guards" framing. This is the closest thing to
independent verification found for the *behavior* of the bot (not the headline numbers, which remain
unverified).

**2025-05 — The "reversal," dated and sourced to a direct Bloomberg-interview quote captured by CX
Dive** (curl-fetched directly, HTTP 200, verbatim confirmed in raw HTML — CX Dive is trade-press, not
primary, but the Siemiatkowski quote is reproduced as a direct quotation from a named Bloomberg
interview):
URL: https://www.customerexperiencedive.com/news/klarna-reinvests-human-talent-customer-service-AI-chatbot/747586/
(published May 9, 2025, byline Kristen Doerer). Verbatim:
"Klarna CEO Sebastian Siemiatkowski said just as much in an interview with Bloomberg Thursday. 'From a
brand perspective, a company perspective … I just think it's so critical that you are clear to your
customer that there will be **always a human if you want**,' Siemiatkowski said."
Also, a Klarna spokesperson (Clare Nordstrom) directly quoted by CX Dive: "'While Klarna pioneered the
use of AI in customer service with groundbreaking results, this strategy will now evolve to the next
level,' Nordstrom said in an email. 'AI gives us speed. Talent gives us empathy. Together, we can
deliver service that's fast when it should be, and empathic and personal when it needs to be.'"
And: "Klarna is now recruiting workers for what Siemiatkowski referred to as an Uber-type customer
service setup" — a gig/flexible staffing model, not a return to the pre-2024 employment structure.

**What did NOT reverse (important, and easy to get wrong)**: no source found says Klarna abandoned
the AI assistant or reverted the 2024 automation. The CX Dive framing is explicit: "Klarna was not
pulling AI out of the high-volume tier; it was reintroducing humans for the premium and complex-case
tier" (this specific sentence is a WebSearch-synthesis summary of the article's framing, not a direct
quote I located verbatim in the raw HTML — treat the *direction* as confirmed, the *exact wording* as
unverified). What IS confirmed by direct quotes above: (1) Klarna is rehiring human customer-service
capacity after an "AI hiring freeze" reported to have lasted over 12 months; (2) the stated reason,
in Siemiatkowski's own words reported elsewhere (via WebSearch synthesis of Forbes/Fortune/Entrepreneur
coverage, **not independently curl-verified — all three of those fetches hit paywalls or JS shells in
this pass**): "We went too far. We focused too much on cost. The result was lower quality." **This
specific quote could not be verified against primary text in this session — flag as
WebSearch-reported-only, high plausibility (it is widely and consistently repeated across
Entrepreneur, Forbes, Fortune, MLQ), but I did not personally see it in a raw fetch.**
(3) the always-available human option is reaffirmed, matching what was already true in Feb 2024.

**No independent verification found for the original 2024 numbers.** I searched specifically for
independent/third-party verification or debunking of "700 agents," "$40M profit," "25% drop in repeat
inquiries," and found none — every source either repeats the press release or (like Pragmatic
Engineer) tests the bot's *behavior* without auditing the *financial/headcount claims*. This absence
is itself the honest finding: **the single most-cited AI-support case study in the industry has never
had its headline numbers independently audited**, as far as this research pass could determine.

**Klarna S-1/IPO filing**: not reached in this pass — I did not fetch or search the actual IPO filing
text for customer-service headcount disclosures. **Flag as an open gap**; the charter specifically
asked for this and I did not get to it before time/budget ran out on the Klarna sub-task. If this is
important for the flagship writeup, it needs a follow-up (SEC EDGAR / Klarna's F-1 filing, ticker
KLAR).

### 2.2 Vendor resolution-rate claims — consolidated (see §1.5 for the full ledger; cross-referenced
here per territory-2 ask)

All five vendors asked about (Intercom Fin, Decagon, Sierra, Zendesk AI, Ada) are covered in §1.5
above under the deflection-honesty discussion, since the two questions are inseparable in practice —
every vendor's "resolution rate" is exactly the KB-deflection honesty problem, just billed per-unit.
Summary of grades: Intercom Fin's *definition* is the only one PRIMARY-SOURCE-verified verbatim in
this pass (fin.ai's own help center); Ada's three-part definition (relevant/accurate/safe) is
WebSearch-synthesis only (direct fetch 403'd); Decagon/Sierra/Zendesk AI numbers are all
WebSearch-synthesis of vendor case-study pages, none independently re-fetched and verbatim-confirmed
in this pass. **No independent, third-party-audited verification of any vendor's resolution-rate
number was found for any of the five.** That absence, stated plainly, is the deliverable finding for
this sub-territory.

### 2.3 Escalation-policy design

- No first-hand engineering/product blog post (e.g., a named engineer's post-mortem or design writeup)
  was found and independently fetched in this pass — every escalation-pattern source that came back
  was aggregator/vendor content (Conduit, BlueTweak, Alhena, Kommunicate, BuildMVPFast — all AI-support
  tooling vendors or SEO content farms). Grade: VENDOR-FOLKLORE for all of the following, cited for
  completeness but NOT to be treated as authoritative:
  - Confidence-threshold escalation: "routing any response where the AI scores below 70-75%
    confidence" is offered as "a good starting point," alongside an explicit warning against relying
    on a single number: "one recent engineering blog warns against hunting for a single 'magic
    confidence number' to escalate below, as with today's large language models that number is
    unreliable." (The "one recent engineering blog" referenced is itself unnamed/unlinked in the
    synthesis — could not trace to a primary post.)
  - Multi-trigger pattern named across sources: confidence + sentiment/frustration detection +
    topic/keyword rules + VIP/high-value-account flagging + repeated-failure counters ("if the bot
    gives an unhelpful response twice in a row, escalate on the third attempt").
- **The one genuinely first-hand escalation observation in this whole pass** comes from Pragmatic
  Engineer's hands-on Klarna test (§2.1 above, PRACTITIONER-REPORT, first-hand): topic-boundary
  escalation triggered a "swift handoff to a human agent" when the tester went off-topic — a real,
  observed instance of an escalation policy in production, from a named, credible, independent
  reporter, not vendor marketing copy.
- **Siemiatkowski's own statement on always-available human escalation** (§2.1, direct Bloomberg
  quote via CX Dive): "there will be always a human if you want" — this is the one policy statement in
  this entire territory that is both primary-attributed (a named executive, a named interview) and
  policy-relevant (an unconditional human-escalation guarantee, independent of confidence scores or
  sentiment).

### 2.4 Support-bot evaluation — τ-bench (MEASURED-WITH-METHOD, the strongest evidence in this file)

- **Paper**: Yao, Shinn, Razavi, Narasimhan, "τ-bench: A Benchmark for Tool-Agent-User Interaction in
  Real-World Domains," arXiv:2406.12045 [cs.AI], submitted 17 Jun 2024. Directly fetched from
  arxiv.org/abs/2406.12045 (HTTP 200, abstract page text extracted and confirmed verbatim — this is
  arXiv's own abstract page, as primary as a paper citation gets without pulling the full PDF).
  Local copy: `taubench_abs.html`.
- **Verbatim abstract (the load-bearing sentence)**: "We employ an efficient and faithful evaluation
  process that compares the database state at the end of a conversation with the annotated goal
  state. We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over
  multiple trials. **Our experiments show that even state-of-the-art function calling agents (like
  gpt-4o) succeed on <50% of the tasks, and are quite inconsistent (pass^8 <25% in retail).**"
  This is a genuinely MEASURED-WITH-METHOD number: a published benchmark, an open evaluation harness
  (github.com/sierra-research/tau-bench), a stated model (gpt-4o), and a defined consistency metric
  (pass^k — does the same agent solve the same task the same way across repeated trials). It directly
  falsifies the implicit vendor narrative that resolution rates in the 70–90% range represent solved,
  reliable agent behavior: the one open, reproducible, third-party academic benchmark for exactly this
  task class puts frontier-model performance under 50% single-attempt success and under 25% for
  8-trial consistency in the retail domain.
- **τ²-bench**: a successor benchmark exists (github.com/sierra-research/tau2-bench, "τ-Bench: A
  Benchmark for Tool-Agent-User Interaction in Real-World Domains") — confirmed to exist via search,
  **not independently fetched/read in this pass**; flag as a lead for a follow-up if the pack wants
  the updated numbers (tau-bench is from Sierra, the same company selling outcome-based-priced agents
  discussed in §1.5/2.2 — worth noting the benchmark's own authorship is not neutral, though the
  original τ-bench paper is peer-reviewable/open and its methodology is public, unlike any vendor's
  resolution-rate definition).
- **Human-review sampling, hallucination-rate measurement**: no first-hand source found in this pass
  describing a standardized "hallucinated-answer rate" methodology for support bots outside of
  τ-bench's pass^k framing. Flag as open.

### 2.5 Legal/policy edge — Moffatt v. Air Canada, 2024 BCCRT 149

**PRIMARY SOURCE OBTAINED AND READ IN FULL** — the actual 9-page tribunal decision PDF, fetched
directly via curl (Chrome UA, HTTP 200) from a law-firm-hosted mirror after CanLII itself blocked the
request with a DataDome challenge (403, "protected"). Local files: `aircanada5.pdf` / `aircanada5.txt`.
URL used: https://loyaltylobby.com/wp-content/uploads/2024/02/Air-Canada-Tribunal-2024bccrt149.pdf
Citation confirmed from the document header: "Indexed as: Moffatt v. Air Canada, 2024 BCCRT 149" —
"File: SC-2023-005609," Tribunal Member Christopher C. Rivers, "Date Issued: February 14, 2024."

Key verbatim findings (this is the actual tribunal text, not a summary of it):
- Facts: "In November 2022, following the death of their grandmother, Jake Moffatt booked a flight
  with Air Canada. While researching flights, Mr. Moffat used a chatbot on Air Canada's website. The
  chatbot suggested Mr. Moffatt could apply for bereavement fares retroactively. Mr. Moffatt later
  learned from Air Canada employees that Air Canada did not permit retroactive applications."
  On Feb 8, 2023, "an Air Canada representative responded and admitted the chatbot had provided
  'misleading words.'"
- The "separate legal entity" argument, and its rejection, verbatim: "Air Canada argues it cannot be
  held liable for information provided by one of its agents, servants, or representatives – including
  a chatbot. It does not explain why it [believes that is the case]. In effect, Air Canada suggests the
  chatbot is a separate legal entity that is responsible for its own actions. **This is a remarkable
  submission.** While a chatbot has an interactive component, it is still just a part of Air Canada's
  website. It should be obvious to Air Canada that it is responsible for all the information on its
  website. It makes no difference whether the information comes from a static page or a chatbot."
- The negligence finding, verbatim: "I find Air Canada did not take reasonable care to ensure its
  chatbot was accurate. While Air Canada argues Mr. Moffatt could find the correct information on
  another part of its website, it does not explain why the webpage titled 'Bereavement travel' was
  inherently more trustworthy than its chatbot. It also does not explain why customers should have to
  double-check information found in one part of its website on another part of its website."
- Outcome, verbatim: "...I find they are entitled to damages of $650.88." Plus pre-judgment interest
  from Nov 17, 2022. (Secondary sources report this figure as "$650.88 in damages," matching the
  primary text exactly — cross-confirmed.)
- Legal basis: negligent misrepresentation, a tort claim (not contract/tariff — the tribunal found Air
  Canada's tariff defence failed for lack of evidence, separately from the misrepresentation finding).

This is a clean, fully-verified, load-bearing legal anchor: **a company was held liable for its
customer-facing chatbot's factual claim, on the theory that a chatbot is not a separate legal actor
but simply another part of the company's own published information — the same duty of care applies
whether the words came from a static page or an interactive bot.** This is squarely a POLICY-side
finding for a success pack (it bears on when/how a support bot's claims create liability exposure,
and thus on how conservatively a bot's "policy" content must be curated and reviewed) rather than a
MECHANICS finding (it says nothing about RAG, prompting, or model choice).

---

## OPEN QUESTIONS (not resolved in this pass)

1. Support Driven's own community writing — not reached first-hand; only third-party summaries of its
   philosophy were found via WebSearch. Needs a direct fetch of supportdriven.com or its Slack/
   community archives if reachable.
2. ITIL's own canonical priority-matrix text (Axelos/itSMF sourcing) — only secondary ITSM-vendor
   treatments were reachable; PagerDuty's own page was JS-shell-blocked to curl.
3. Klaus AutoQA whitepaper PDF — fetch failed twice (curl returned no response / timeout). If AutoQA
   category detail matters for the pack, needs a retry, possibly with a longer timeout or a different
   mirror.
4. incident.io's own guide pages returned JS-shells to curl; Atlassian was the stronger primary source
   for territory 1.6, but incident.io's severities/statuses distinction (their specific
   framing: "severities answer 'how bad', statuses answer 'how close to normal'") is WebSearch-
   synthesis only, not verbatim-confirmed.
5. Atlassian's specific customer-facing-vs-internal-postmortem guidance was NOT found on the page
   fetched (incident-communication); it likely lives on a separate /handbook/postmortems page not
   fetched in this pass.
6. Klarna's S-1/IPO filing — not reached at all in this pass. Flagged by the charter explicitly;
   still open.
7. The Siemiatkowski "we went too far, we focused too much on cost" quote — widely repeated across
   secondary press (Entrepreneur, Forbes, Fortune, MLQ) but every direct fetch of those outlets hit a
   paywall/JS-shell in this session. Not independently verified against primary text; treat as
   high-plausibility-but-unverified.
8. τ²-bench — confirmed to exist, not read. If the pack wants the most current agent-benchmark
   numbers (rather than the original 2024 τ-bench figures), this needs a follow-up fetch.
9. Erlang-family staffing for solo/2-person async support — no source found translates queueing
   theory into practical guidance at this scale. Likely true answer is "nobody uses it, they triage by
   heuristic," but I found no source saying this explicitly; do not assert it in the shipped pack
   without a supporting citation from another channel (B/x-practitioners is best positioned to find
   this — solo founders describing their own inbox-triage practice).
10. The "58.7% independent top-quartile" resolution-rate benchmark figure that appeared in one
    secondary vendor-comparison blog (Lorikeet) could not be traced to a primary methodology. Treat as
    unverified; do not repeat without further tracing.

## SEAM FLAGS

- **operate seam (customer-facing incident comms)**: recorded in §1.6. The Atlassian material cleanly
  separates severity-as-technical-classification (plausibly operate's) from
  severity-drives-comms-cadence (plausibly success's), but I have not cross-checked this against
  operate's actual shipped `incident-response.md:159` wording — the controller should confirm the
  split holds before finalizing SKILL.md boundary language.
- **ai seam (model/RAG mechanics vs success policy)**: recorded throughout §2. Every AI-support-agent
  finding in this file is deliberately kept at the POLICY layer (what counts as a resolution, when to
  escalate, who's liable for what a bot says, how to interpret a vendor's resolution-rate claim) and
  explicitly avoids MECHANICS (how the retrieval/grounding/prompting actually works, which is `ai`'s
  territory per the charter). The one place this could blur is τ-bench: the benchmark measures tool-
  use *reliability*, which is arguably a mechanics-adjacent concept, but I've framed it here purely as
  evidence for the policy question "how much can you trust a vendor's resolution-rate claim" — the
  controller should confirm `ai`'s channel isn't already claiming τ-bench as its own evidence base for
  a different (mechanics) purpose, to avoid duplicate/conflicting treatment.
