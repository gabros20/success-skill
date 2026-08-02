# Falsification strips + churn/health-score evidence ledger (channel D)

Worker: D · web-research. Tools: WebSearch, WebFetch, curl+pdftotext. Crawl4AI not used (broken, per charter).
All downloaded primary/secondary artifacts live under `/tmp/d2/` (list at the end). Per charter hard rule 2:
any number reported as load-bearing is one I have SEEN in downloaded text (verbatim quoted below) or is
explicitly flagged **PRIMARY TEXT NOT OBTAINED — secondary attribution only**.

---

## 1. PART A VERDICT TABLE

| # | Claim | Folklore version | Primary source (author/year/venue) | Method | Scope limits | Verdict | Read primary text? |
|---|---|---|---|---|---|---|---|
| 1 | 5% defection cut → large profit gain | "5% retention increase → 25–95% profit increase" | Reichheld & Sasser, "Zero Defections," HBR Sept–Oct 1990, 68(5):105–111 | Bain client-engagement case illustrations + NPV-style customer-lifetime-value arithmetic (MBNA, one bank branch system, one insurance brokerage, one auto-service chain) — **not a designed experiment or a random/representative sample** | 4 named firms/industries, US, late-1980s Bain client base; "25–95%" is not the article's own range — it is a folk-conflation of a *separate* 1990s Bain client note ("25%," financial services, sourced) with the article's 85%/50%/30% figures (rounded upward to ~95% in circulation) | **GROUNDED-BUT-MISQUOTED** (the underlying mechanism is real Bain case data; the "25–95%" headline figure is a corrupted paraphrase, not the article's own wording; it is a modeled/case-illustrated projection, not a measured population effect) | **NO for the 1990 article itself** (paywalled everywhere I could reach — see §2.1); **YES for the adjacent, textually-confirmed Bain "25%" claim** (see §2.1.4) |
| 2 | Acquisition costs 5–25× retention | "It costs 5–25× more to acquire a customer than to retain one" | No study exists at the "5–25×" figure itself; HBR 2014 "The Value of Keeping the Right Customers" (Amy Gallo) is the modern re-launder point and **cites no source** | N/A — hedge phrase ("depending on which study you believe") with zero footnote | N/A | **FOLKLORE / UNTRACEABLE at the "5–25×" formulation.** The nearest traceable ancestor is a 1980s "5×" claim attributed to TARP-adjacent 1980s consultancies, which Ipsos (Keiningham/Vavra/Aksoy/Wallard, *Loyalty Myths*, 2005) explicitly debunks with a 3-part economic argument | **YES** (Ipsos excerpt PDF, full text obtained; HBR 2014 sentence obtained via WebFetch quote-extraction, no download possible — paywalled) |
| 3 | NPS is "the best predictor of growth" | Same as claim | Reichheld, "The One Number You Need to Grow," HBR Dec 2003 | Reichheld's own analysis: hand-picked "exemplar" industry scatterplots (Satmetrix survey panels, ~50 companies/~12 industries) correlating NP score with revenue growth, no disclosed regression tables, no held-out validation | Small, non-random, Reichheld/Satmetrix-selected industry samples; academic replication (below) with 21 firms says otherwise | **GROUNDED-BUT-MISQUOTED → largely FOLKLORE under independent replication.** Keiningham et al. (2007, JM, n=21 firms/15,500+ interviews) found **no support** for the "single most reliable indicator" claim; ACSI beat NPS on R² in 2 of 3 reconstructed exemplar cases | **YES** (Keiningham et al. 2007 full text; Grisaffe 2007 full text) |
| 4 | "96% of unhappy customers don't complain" (+ "26 silent," "91% just leave") | Same, usually attributed to "1st Financial Training Services" (dead end) | TARP / John Goodman, "Consumer Complaint Handling in America" studies for the White House Office of Consumer Affairs, ~1979–1986, plus Coca-Cola USA–sponsored word-of-mouth studies | Multi-industry survey research on complaint incidence by problem type and dollar value | The "96%" figure is a **flattened average across wildly different problem categories** — TARP's own category breakdown shows complaint rates from ~5–30% (mistreatment/quality/incompetence) up to 50–75% (out-of-pocket monetary loss, large-ticket items) | **GROUNDED-BUT-MISQUOTED** — a real TARP-derived finding exists, but the single "96%"/"1 in 26" number erases a documented, large, and industry/problem-type-dependent range, and the original full report/PDF is not freely available online (dead links, no OCR copy found) | **NO — could not obtain the original TARP report text; only secondary paraphrase (multiple independent aggregator sites converging on the same category breakdown) — PRIMARY TEXT NOT OBTAINED** |
| 5 | "80% of revenue from 20% of customers" | Same | No single canonical academic source for the *retail-CS* framing; nearest rigorous test: Sharp & Romaniuk (2007, Ehrenberg-Bass working paper) and Graham, Sharp, Trinh & Dawes (2017, ~600 brands / 40 categories, Kantar UK panel, 1998–2014) | Household panel purchase-data decomposition of brand sales by buyer-frequency decile, replicated across categories/years/countries | UK/US grocery- and packaged-goods-panel categories predominantly; may not transfer directly to B2B SaaS/subscription revenue concentration, which can legitimately be far more skewed by seat-count | **FOLKLORE at 80/20; GROUNDED at ~60/20** for the fast-moving-consumer-goods domain actually studied — light buyers (bottom ~80%) reliably deliver closer to 40–50% of sales, not 20%, and top-20% membership itself is unstable year to year (regression to the mean) | **Partial** — obtained via WebFetch extraction of the Ehrenberg-Bass Institute's own synthesis page (not the underlying SSRN PDF, which failed to render as text — see downloads list); treat the 60/20 figure and the Graham et al. 2017 citation as **secondary-but-institute-authored**, not independently primary-verified by me |
| 6 | Support-deflection cost ratios ("$X per human ticket vs $Y self-serve," "10× cheaper") | Same | No single traceable primary study for the popular "$1 vs $6" framing; the closest method-bearing sources are MetricNet/HDI cost-per-ticket benchmarks (own proprietary panel data) | MetricNet/HDI: total desktop-support/service-desk operating cost ÷ ticket volume, from a paid benchmarking panel of enrolled IT organizations | IT service-desk/desktop-support context specifically (not general customer support or AI chatbot deflection); costs vary 4–5× by ticket-density tier in HDI's own 2014 sample ($31.98–$179.33 high-density; $56.46–$288.99 medium-density) | **METHOD-KNOWN-BUT-NARROW-SCOPE for MetricNet/HDI** (real benchmarking methodology, but IT-helpdesk-specific, paid-panel, not public raw data); **FOLKLORE/UNTRACEABLE for "$1 self-service vs $6 agent-assisted"** — no primary Forrester report located, only secondary re-citations | **NO for the "$1/$6" figure — PRIMARY TEXT NOT OBTAINED.** MetricNet numbers obtained only via WebSearch synthesis, not a downloaded benchmark report — **treat as secondary attribution only** |
| — | "80% of companies believe they deliver superior CX; 8% of customers agree" | Same | Allen, Reichheld, Hamilton & Markey, "Closing the Delivery Gap," Bain & Company, 2005 | Bain "CustomerLed Growth" diagnostic survey, n=362 companies (self-report) cross-referenced against Satmetrix Net Promoter customer database, n=375 | Company self-perception vs. a *different, non-linked* customer database (not the same companies' own customers necessarily) — a comparison of two separate surveys, not a matched-pairs study | **GROUNDED** — real Bain survey with disclosed n and source line; scope limit (two different survey populations, not perfectly matched) is real but disclosed by Bain itself | **YES** (full Bain PDF downloaded and read) |

---

## 2. PART A DETAIL SECTIONS

### 2.1 Reichheld & Sasser 1990 "Zero Defections" and the 25–95% folklore

**2.1.1 — could not obtain primary 1990 HBR text.** Every route failed:
- `hbr.org/1990/09/zero-defections-quality-comes-to-services` — paywalled; WebFetch returns only the opening two sentences, no numbers.
- `bain.com/insights/zero-defections-quality-comes-to-services-harvard-business-review-hbr/` — Cloudflare JS challenge via curl (saved as `/tmp/d2/bain_zerodef.html`, 5.9KB of challenge-page markup, no article text); WebFetch on the same URL returned only an MBNA anecdote and a suspicious, **internally inconsistent** figure ("boost profits by almost 100%") that contradicts every independently-converging secondary quote below — I am **explicitly discarding that WebFetch-derived "almost 100%" number** per the hard rule against trusting the summarizer for magnitudes.
- Three university-hosted mirror PDFs found by search (`prep.missouri.edu`, `filemaker.journalism.cuny.edu`, `beta.mercycollege.edu`) — all dead (DNS failure or 404; saved failed artifact at `/tmp/d2/rs1990_a2a7d708.pdf`, actually an HTML 404 page).
- Scribd document page (`scribd.com/document/926771193/...`) — landing page only, no extractable body text (`/tmp/d2/scribd_zerodef.html`).
- SciSpace "open access" listing — JS-rendered SPA, no PDF link extractable via curl (`/tmp/d2/scispace_zerodef.html`).

**Verdict on this specific sub-question: PRIMARY TEXT NOT OBTAINED for the 1990 article.** What follows is secondary-only, but unusually convergent — the *same* verbatim sentence appears independently on a citation-quotes blog and was echoed by two different WebSearch aggregations:

> "Reducing defections by just 5% generated 85% more profits in one bank's branch system, 50% more in an insurance brokerage, and 30% more in an auto-service chain." (secondary quote, converging across ≥3 independent aggregator pages; **not primary-verified by me**)
> "MBNA America has found that a 5% improvement in defection rates increases its average customer value by more than 125%." (same caveat)

This is the number the charter asked me to verify — I was **not able to primary-verify it**, but the convergence across independent secondary sources (a dedicated management-quotes archive, WebSearch's own retrieval, and consistency with the Bain-authored 2001 brief below) makes outright fabrication unlikely. Flag as secondary attribution only.

**2.1.2 — the "25–95%" folklore range traced.** I could not find any primary text that states "25% to 95%" as a single range. The likely mechanism: someone conflated (a) a **later, separate, Bain-authored** document's "25%" figure (§2.1.4, textually confirmed) with (b) the 1990 article's 85% figure (rounded up in circulation to "95%"), producing the composite "25–95%" that now circulates as if it were one sentence from one source. A LinkedIn thread comment (quoted via WebFetch, itself secondary) makes the stronger claim that the whole "double your profits" framing originated from "an article from the late 1980s" describing a **single hypothetical 20-year credit-card scenario**, not a cross-industry finding — I could not verify this claim independently and flag it as an unverified third-party allegation, not a confirmed finding.

**2.1.3 — was it measured or modeled?** Neither the primary article nor any secondary description I found describes a controlled experiment or a representative sample. Every account describes **named individual-company cases** (MBNA, "one bank's branch system," "an insurance brokerage," "an auto-service chain") consistent with Bain client-engagement illustrations, i.e., **modeled NPV/customer-lifetime-value arithmetic per case**, not a population-level measured effect. This supports the "modeled, not measured" suspicion in the charter.

**2.1.4 — the Bain-primary confirmation I DID get.** I downloaded a genuine Bain & Company document, "Prescription for cutting costs," by Fred Reichheld (Bain fellow), referencing his 2001 book *Loyalty Rules!* (so datable to ~2001–2002). Saved at `/tmp/d2/bain_prescription_cutting_costs.pdf`; extracted text `/tmp/d2/bain_prescription.txt`. Verbatim:

> "In financial services, for example, a 5% increase in customer retention produces more than a 25% increase in profit."

This is the real origin of the "25%" half of the folklore range — a genuine, Bain-authored, but citation-free ("more than a 25% increase," no study cited within this document) claim, scoped explicitly to **financial services only**, not a universal law. This is the strongest primary evidence in this strip: I read it myself, it is genuinely Reichheld/Bain-authored, and it demonstrates the folklore range is a **splice of two different documents**, not a misreading of one.

**2.1.5 — "The Loyalty Effect" (1996 book).** Not obtained as primary text (Internet Archive listing is a borrow-only scan, its search-inside API returned no matches for my terms). WebSearch synthesis reports the book claims "even a small improvement in customer retention can double profits" and that disloyalty "stunts company growth by 25–50%" — **PRIMARY TEXT NOT OBTAINED, secondary attribution only**, and this book-level claim should NOT be conflated with the 1990 article's per-industry figures (they appear to be a different, later restatement).

### 2.2 "5–25× more expensive to acquire than retain"

Downloaded and read in full: `/tmp/d2/ipsos_loyalty_myth8.pdf` (Ipsos, "Loyalty Myth #8: It Costs Five Times More to Acquire a Customer than to Retain a Customer," excerpt from Keiningham/Vavra/Aksoy/Wallard, *Loyalty Myths*, Wiley 2005). Verbatim on origin:

> "Although it is difficult to determine the exact origins of this platitude, the earliest sources that we can find attribute it to research conducted by the Technical Assistance Research Project (TARP) in Washington, D.C. in the late 1980s. Around the same time, other loyalty pundits claimed exactly the same findings as their own (for example, the Customer Service Institute, Consumer Connections Corp., and ITEM Group). Soon the myth found its way into the pages of prestigious journals and books. In 1990, Total Quality Management group president Christopher Hart and Harvard professors James Heskett and W. Earl Sasser, Jr. lent the statement further credibility in their Harvard Business Review article 'The Profitable Art of Service Recovery.'"

Ipsos's own debunking argument (verbatim, 3 numbered flaws):

> "1. The fundamental financial underpinnings of the argument are either misallocated in terms of acquisition and retention, or the financial effects attributed to retention are false. ... research has shown that none of these things are true [that existing customers spend more, pay full price, and create efficiencies]."
> "2. The assertion ignores the lifecycle of products, services, and institutions. When firms are in their introductory and growth phases allocations to acquire customers will be substantial. ... when products or firms are in the decline phase, allocations required to retain customers will be substantial, making the typical acquisition-retention cost ratio weighted heavily to retention."
> "3. It ignores the fact that a company's customer base is made up of broad mix of customers who vary in their costs to acquire and retain. ... Often the most expensive customers to retain are those who generate the most profits for the firm."

**Chain to HBR 2014 (Amy Gallo, "The Value of Keeping the Right Customers")**: fetched directly; exact sentence (WebFetch quote-extraction of the live paywalled preview, not a downloaded PDF — treat with appropriate caution but this is a direct quote of an actual visible sentence, not a magnitude-summary):

> "Depending on which study you believe, and what industry you're in, acquiring a new customer is anywhere from five to 25 times more expensive than retaining an existing one."

**No citation or footnote accompanies this sentence.** The chain is: TARP-late-1980s (untraceable original) → Hart/Heskett/Sasser 1990 HBR restatement → decades of "loyalty pundit" repetition → Gallo/HBR 2014 restating it as an uncited hedge ("depending on which study you believe"). **Verdict on the chain: FOLKLORE all the way down** — no link in the chain, including the most recent and most-cited one, points to an actual traceable study.

### 2.3 NPS "best predictor of growth"

Downloaded and read in full: `/tmp/d2/keiningham_npjm_2007.pdf` (Keiningham, Cooil, Andreassen & Aksoy, "A Longitudinal Examination of Net Promoter and Firm Revenue Growth," *Journal of Marketing* 71(3), July 2007, 39–51) and `/tmp/d2/grisaffe_2007.pdf` (Grisaffe, "Questions about the Ultimate Question," *J. Consumer Satisfaction, Dissatisfaction and Complaining Behavior* 20:36–53, 2007).

**Method (Keiningham et al. 2007), verbatim abstract:**
> "This article (1) employs longitudinal data from 21 firms and 15,500-plus interviews from the Norwegian Customer Satisfaction Barometer to replicate the analyses used in Net Promoter research and (2) compares Reichheld and colleagues' findings with the American Customer Satisfaction Index. Using industries Reichheld cites as exemplars of Net Promoter, the research fails to replicate his assertions regarding the 'clear superiority' of Net Promoter compared with other measures in those industries."

Sample detail (verbatim): "In total, five industries (representing 17 of the 21 firms..." tracked longitudinally in the Norwegian Customer Satisfaction Barometer (NCSB); NCSB methodology cross-checked against Fornell's ACSI theoretical foundation.

**Reichheld/Satmetrix's own original sample** (verbatim, as characterized by Keiningham et al. quoting Satmetrix 2004): "In total, over 50 companies were included across a dozen target industries, such as airlines, package delivery, and life insurance..." — i.e., the original claim itself rests on a small, non-random, vendor-selected sample, not a general population study.

**Key result (verbatim):**
> "Even more startling, however, in two of the three cases, the R-square of the ACSI–growth relationship is higher than that for the Net Promoter–growth relationship. These results show that Net Promoter cannot be called the better predictor of growth in relation to customer satisfaction for the industries under investigation."
> "We find no support for the claim that Net Promoter is the 'single most reliable indicator of a company's ability to grow' (Netpromoter.com 2006; Nicks 2006)."

**Reichheld's own response (as quoted inside the Keiningham paper), verbatim:**
> "All we did was quantify this common sense in a way that made sense to business leaders—the target audience for my book. These practical leaders have little interest in advanced statistical methods. Frankly, we see little value in continued debate about cause versus correlation, timeframes, or statistical methods." (Reichheld 2006b, as cited in Keiningham et al. 2007)

This is Reichheld's own softening/dismissal of the statistical critique — he does not contest the numbers, he disputes that the debate matters. Keiningham et al. respond: "Unfortunately, the statistics matter."

**Grisaffe 2007 (independently downloaded, `/tmp/d2/grisaffe_2007.pdf`)** — a conceptual (not just empirical) critique, explicitly citing Keiningham et al. 2007 as "A recently published Journal of Marketing paper [that] challenges the validity of Reichheld's claims on empirical grounds." Grisaffe's own contribution is about construct validity (single-item measurement, the arbitrariness of the 0–10/detractor-passive-promoter cutoffs), not a new dataset.

**Other critiques found but NOT primary-downloaded (secondary synthesis only, via MeasuringU's "Has the Net Promoter Score Been Discredited?" article, `measuringu.com/nps-discredited/`, itself a secondary meta-review) — PRIMARY TEXT NOT OBTAINED for these specific numbers:**
- van Doorn, Leeflang & Tijs (Int. J. Research in Marketing, ~2013): reported (per MeasuringU's paraphrase) n=11,967 respondents across Dutch industries; NPS correlated with sales growth r≈.46 and margins r≈.22; "top-box" satisfaction performed comparably (r≈.493) — **numbers not independently verified against the original paper by me.**
- De Haan et al. (2015, ~80,000+ evaluations): top-two-box satisfaction vs. retention r≈.184 vs. NPS r≈.170 — same caveat.
- Fisher & Kordupleski (2019) "Good and bad market research" — referenced in the charter, **not located/downloaded** in this pass.

**Overall verdict on NPS:** what NPS demonstrably does — it is a simple, cheap, widely-adopted single-item proxy that correlates (often strongly, r in the high .9s per MeasuringU's paraphrase of ACSI/NPS correlation) with other satisfaction-family measures. What it does NOT demonstrably do — outperform ACSI or plain top-box satisfaction as a predictor of firm revenue growth in independent academic replication; Reichheld's own "exemplar" industries, when re-analyzed, favor ACSI in 2 of 3 cases.

### 2.4 "96% of unhappy customers don't complain" / TARP

**PRIMARY TEXT NOT OBTAINED.** I could not locate a downloadable copy of Goodman/TARP's "Consumer Complaint Handling in America" (1979/1986) — it exists as a physical NTIS/GPO-era government report and a Google Books catalog listing only (`books.google.com/books/about/Consumer_Complaint_Handling_in_America.html?id=9V-YOwAACAAJ` and `id=FneCtgAACAAJ` — catalog records, no preview text). The Customer Service Reader / TypePad host that WebSearch indexed as hosting Goodman's own commentary is now a dead, parked domain (redirects to networksolutions.com).

What I obtained is **convergent secondary paraphrase** (multiple independent WebSearch aggregations, not a single copy-paste chain) describing TARP's actual, more nuanced finding:

> Complaint rates vary sharply by problem type and dollar value: "packaged goods and other small ticket items" show ~96% not complaining (or complaining only to the retailer); large-ticket items show ~50% complaining to the front line, 5–10% escalating further; "out-of-pocket monetary loss" problems have 50–75% complaint rates, while "mistreatment, quality, and incompetence" problems evoke only 5–30% complaint rates to the front line.

**Verdict: GROUNDED-BUT-MISQUOTED.** A real TARP finding underlies the "96%" figure, but the number that circulates is a flattened, worst-case (small-ticket/packaged-goods) figure presented as a universal law, when TARP's own (secondarily reported) breakdown shows the true rate ranges from ~5% to ~75% depending on category and stakes. I was not able to confirm the exact "26 silent customers per complainer" ratio or the "91% just leave" cousin-claim against primary text at all — treat those as **UNTRACEABLE** pending primary access.

### 2.5 "80% of revenue from 20% of customers"

Obtained via WebFetch extraction of the Ehrenberg-Bass Institute's own page (`marketingscience.info`, static HTML render blocked by their JS framework — the raw file at `/tmp/d2/sharp_pareto.html` and the SSRN download attempt at `/tmp/d2/sharp_6020.pdf` are both non-extractable JS/HTML shells, not readable text — **flagging this as a WebFetch-mediated synthesis, not something I read with my own eyes in a downloaded document**):

> Sharp & Romaniuk (2007), Ehrenberg-Bass working paper "There is a Pareto Law, but not as you know it," and Graham, Sharp, Trinh & Dawes (2017) analyzing Kantar household panel data covering "nearly 600 brands," "40 product categories," across the entire UK market in two periods (1998/2004 and 2009/2014) — found that light buyers (bottom ~80%) deliver "almost half" of a brand's sales over a multi-year window (a ~60/20 pattern), with the ratio closer to ~40/20 at the quarterly level (higher buyer-concentration in short windows, converging toward more even 60/20-ish splits over longer windows as buyer identity churns).

**Verdict: FOLKLORE at "80/20"; GROUNDED (institute-reported, large panel, real methodology) at approximately "60/20"** for FMCG/grocery-panel categories. Important scope caveat for the success-skill pack: this evidence base is **consumer packaged goods**, not B2B SaaS/subscription seat-based revenue, where genuine 80/20-or-tighter concentration is structurally plausible (a few enterprise accounts can legitimately dominate ARR in ways a shampoo brand's buyer panel cannot). **Do not import the 60/20 correction uncritically into a B2B SaaS success pack without flagging this domain mismatch.**

### 2.6 Support-deflection cost ratios

- **MetricNet / HDI cost-per-ticket benchmarks**: real, disclosed methodology ("total monthly operating expense ÷ monthly ticket volume"), obtained via WebSearch synthesis only (no benchmark report PDF downloaded — **PRIMARY TEXT NOT OBTAINED**, secondary attribution). Reported 2014 HDI global desktop-support sample: high-density environments average $84.42/ticket (range $31.98–$179.33); medium-density average $125.13/ticket (range $56.46–$288.99). Scope: **enterprise IT service desk / desktop support specifically**, a paid benchmarking panel of enrolled organizations, not general customer-support or AI-chatbot deflection economics.
- **"$1 self-service vs $6–12 agent-assisted" (commonly attributed to Forrester or Gartner)**: I could not find a primary Forrester report stating this. WebSearch surfaced a *different*, seemingly more specific pairing — "$13.50 agent-assisted vs $1.84 self-service" attributed loosely to "Gartner" via a secondary blog aggregator (`ringly.io`) — **PRIMARY TEXT NOT OBTAINED for either version.** Verdict: **FOLKLORE/UNTRACEABLE at the exact dollar figures**; the qualitative direction (self-service materially cheaper per contact) is plausible and repeatedly asserted across the industry, but I found no primary study for any specific ratio.

### 2.7 Bain "80% of companies think they deliver superior CX, 8% of customers agree"

Downloaded and read in full: `/tmp/d2/bain_closingdeliverygap.pdf` (Allen, Reichheld, Hamilton & Markey, "Closing the Delivery Gap," Bain & Company, 2005). Verbatim:

> "When we recently surveyed 362 firms, we found that 80% believed they delivered a 'superior experience' to their customers. But when we then asked customers about their own perceptions, we heard a very different story. They said that only 8% of companies were really delivering."
> Figure 1 source line: "Source: Bain CustomerLed Growth diagnostic questionnaire, n = 362; Satmetrix Net Promoter database, n = 375."

**Verdict: GROUNDED.** Real, disclosed n on both sides, though note the two n's (362 companies self-reporting; 375 in a separate Satmetrix customer database) are **not the same matched population** — it is a comparison of two different surveys, which Bain discloses but does not caveat as a limitation. Still the strongest-sourced figure in this entire strip set.

### 2.8 Other figure-class flags tripped over (not deep-traced, flagging only)

- **"Customers tell 9–15 people [about a bad experience]"** — appears as a companion figure to the TARP complaint-silence numbers in the same secondary aggregator ecosystem (e.g., "tell 9 to 10 others within a week"); same untraceable-primary status as §2.4. Same seam.
- **"It takes 12 positive experiences to make up for 1 bad one"** — tripped over in general search noise around customer-experience listicles; not traced this pass; smells identical to the TARP-family folklore (round-number, uncited, endlessly recirculated). Flagging for a future pass, not verified either way.
- **`pulserevops.com/knowledge/q525`** (health-score accuracy Q&A) — a live example of the exact laundering failure mode the charter warns about: it asserts specific numbers ("62% precision, 58% recall" baseline SaaS health score; "AUC often ranging from 0.7 to 0.9"; ensemble methods improve AUC "by 5–15 percentage points") with **zero traceable citation**, and its own "Sources" section cites unrelated **medical/health-domain** references (NIH, CDC, WHO, JAMA) that do not support B2B SaaS health-score claims at all. This is a citation-fabrication/mismatch pattern worth naming explicitly in the skill pack as a worked "how laundering happens" example — see Part B below.

---

## 3. PART B — HEALTH SCORES & CHURN PREDICTION EVIDENCE LEDGER

### 3.1 MEASURED-WITH-METHOD

**Ascarza, "Retention Futility: Targeting High-Risk Customers Might Be Ineffective," *Journal of Marketing Research* 55(1), 80–98, 2018.** Downloaded in full: `/tmp/d2/ascarza_2018_retention_futility.pdf` (source: `evaascarza.com/papers/ascarza_18.pdf`, her own faculty page). This is, per the charter's own framing, likely **the single most important finding for this whole skill pack** — confirmed on read.

Method (verbatim abstract): "Combining two field experiments with machine learning techniques, the author demonstrates that customers identified as having the highest risk of churning are not necessarily the best targets for proactive churn programs."

Design: two real field experiments —
- **Study 1: a wireless telecom provider, Middle East** — "more than 4 million subscribers," randomized treatment (68% of sample) receiving a text offering additional account credit vs. control.
- **Study 2: a special-interest membership organization (U.S.)** — randomized "thank you" gift with renewal letter vs. control at renewal time.

Key numeric result (verbatim, exact quote from extracted text):
> "reducing churn among current customers... 4.1 and 8.7 percentage points in churn rate, respectively, if..." [comparing targeting-by-risk vs. targeting-by-uplift approaches across the two studies]
> On the highest-risk decile in Study 1 (R10): "churn rate is 95.3% for control and 93.7% for treatment (i.e., 1.6 percentage points reduction in..."
> A *lower*-risk group: "reducing churn from 71.2% (control) to 68.3% (treatment), corresponding to a 2.9 percentage points reduction" — **a bigger effect than the highest-risk group got.**
> One group actually got **worse** under treatment: "9.1% for control and 11.9% for treatment, corresponding to a 2.8 percentage points increase in churn rate" — i.e., the intervention backfired for that segment.

**This is the core evidentiary case against the vendor "target the reddest accounts" health-score playbook**: the customers most likely to churn are not the customers most responsive to a retention intervention, and treating them can occasionally increase churn. Method: heterogeneous treatment effect / uplift modeling (random forests) applied to genuine randomized field experiments — as rigorous as this literature gets.

**Verbeke, Dejaeger, Martens, Hur & Baesens, "New Insights into Churn Prediction in the Telecommunication Sector: A Profit-Driven Data Mining Approach," *European Journal of Operational Research* 218(1), 211–229, 2012.** Downloaded in full: `/tmp/d2/verbeke_2012_churn.pdf` (ResearchGate-hosted copy). Confirmed methodological content: the paper's central argument is that churn models are typically evaluated with statistical measures (AUC, top-decile lift) that **do not correspond to actual profit-maximizing targeting fractions**, and it proposes a "Maximum Profit" criterion instead; it explicitly builds on and cites **Neslin, Gupta, Kamakura, Lu & Mason, "Defection Detection," JMR 43(2):204–211, 2006** (the "churn-modeling tournament" referenced in the charter) for the lift-profit relationship — I was **not able to independently download Neslin et al. 2006 itself** (`cdr.lib.unc.edu` and `ssrn.com` links both resolved to HTML/paywall shells, not extractable text — **PRIMARY TEXT NOT OBTAINED for Neslin et al. directly**, only as cited inside Verbeke et al., which I did read).

Key methodological point confirmed in Verbeke's own text: using top-decile or top-5% lift as a model-selection criterion "can lead to suboptimal model selection and as a result to a loss of profit, since the lift of a model is a function of the fraction... that is included" — i.e., **statistical accuracy metrics (AUC, lift) and business-relevant metrics (profit) can select different "best" models.** This directly undercuts vendor claims that a high-AUC health score is automatically a good business tool.

### 3.2 PRACTITIONER / METHOD-DISCLOSED-BUT-NARROW

**MetricNet/HDI cost-per-ticket benchmarking** (see §2.6) — real disclosed panel methodology, IT-service-desk-specific, secondary-attribution only (no report PDF obtained).

### 3.3 VENDOR-FOLKLORE / METHOD-UNKNOWN

- **Gainsight / ChurnZero / Totango / Vitally health-score composites** — I could not find any vendor publicly disclosing a validated accuracy figure (AUC, precision/recall, lift, or a holdout-sample backtest) tied to a named methodology or dataset. What circulates instead (`pulserevops.com/knowledge/q525`, read via WebFetch) is a set of **plausible-sounding but entirely uncited round numbers** ("62% precision, 58% recall" baseline; "AUC often 0.7–0.9"; "ensemble methods improve AUC by 5–15pp") whose own citation section points to **unrelated medical-domain sources**, i.e., either an AI-generated content page with fabricated/mismatched citations, or a human-authored page that never had real citations to begin with. **Be blunt, per the charter's own instruction: this is "no method disclosed," full stop.** I could not find a single vendor (Gainsight/ChurnZero/Totango/Vitally/Catalyst) case study in this pass that discloses a measured accuracy number tied to an actual holdout test — this absence, across five well-known vendors, is itself the finding.

### 3.4 Survival analysis vs. snapshot health scores

Obtained via WebSearch synthesis only (no single primary methods paper downloaded this pass — **secondary attribution**, though the underlying statistical concepts (censoring, hazard rate, time-varying covariates) are standard and uncontroversial survival-analysis textbook material, not a contested empirical claim):

- A **snapshot health score** treats churn as a fixed-window binary classification problem (will this account churn in the next N days), discarding information about *when within that window* churn is likely and about customers still active at the observation cutoff.
- **Survival analysis** models time-to-churn directly, explicitly handling **right-censored** observations (customers still subscribed at the end of the observation window — their true "time to churn" is unknown, not zero) and can incorporate **time-varying covariates** (usage trending down over time, not just a snapshot value), producing a hazard-rate estimate rather than a single risk score.
- Practical implication for the skill pack: a health score that is really a static classifier trained on a fixed look-back window will systematically **misprice tenure and recency effects** and cannot cleanly separate "about to churn" from "will eventually churn, but not yet" the way a survival model can. This is a real methodological gap between the academic churn-prediction literature and the vendor snapshot-composite-score template, independent of any specific number.

### 3.5 What I did NOT get to (open, unresolved)

- Neslin et al. 2006 primary text (only as cited inside Verbeke 2012).
- Ascarza et al., "In pursuit of enhanced customer retention management" (Customer Needs and Solutions, 2018) — not located this pass.
- Fisher & Kordupleski (2019) NPS critique — not located this pass.
- van Doorn/Leeflang/Tijs (IJRM 2013) and De Haan et al. (2015) — numbers cited only via MeasuringU's secondary paraphrase, not independently verified.
- Any single Gainsight/ChurnZero/Totango/Vitally/Catalyst **named case study** with a real measured accuracy number — actively searched for, not found (see §3.3; the absence itself is the reportable finding, but a deeper per-vendor pass could still turn one up).
- The original 1979/1986 TARP "Consumer Complaint Handling in America" report — Google Books catalog entries only, no OCR/preview text; would need a physical/library or NTIS route.
- The 1990 Reichheld & Sasser HBR article's own full text — genuinely paywalled everywhere I could reach without a subscription.

---

## 4. SEAM FLAGS

- **Support-deflection cost ratios (§2.6) and MetricNet/HDI benchmarks** straddle **success ↔ operate/automation**: whether "cost per ticket" belongs to success's support-process-design job or to operate's ops-cost-discipline lens is a controller call — I record the evidence, not the assignment.
- **"80/20" customer revenue concentration (§2.5)** straddles **success ↔ growth/marketing**: the Ehrenberg-Bass evidence base is a marketing/brand-buying-behavior literature (not a CS-specific one), but the skill pack's "which accounts deserve health-score attention" job depends directly on it. Growth or marketing may already have drawn this seam — channel D did not check sibling corpora for this specific figure; controller/lead should reconcile against any existing marketing or growth _raw files before asserting a position.
- **NPS predictive-validity findings (§2.3)** straddle **success ↔ growth**: growth's corpus (per the charter) already has "Kohavi 7,600-response power point + Hiten Shah critique" — this pass adds the **academic** critique (Keiningham 2007, Grisaffe 2007) which is a different and stronger evidentiary tier than a conference talk or blog post. Lead should merge, not duplicate.
- **Ascarza "retention futility" (§3.1)** straddles **success ↔ growth**: it is simultaneously an argument against success's own health-score/targeting playbook AND a direct methodological precedent for growth's "feasibility gate" wedge (uplift/heterogeneous-treatment-effect thinking over raw risk scoring). Both packs likely want to cite this; record here that channel D found it independently in the success context and it should not be treated as growth-exclusive.
- **Survival-analysis-vs-snapshot argument (§3.4)** straddles **success ↔ data**: this is fundamentally a data-modeling/methodology question (censoring, time-varying covariates) that data's quality/measurement corpus may already cover in a general form; success's contribution is the CS-specific application (why a Gainsight-style composite score is methodologically weaker than a survival model for renewal-timing decisions).

---

## 5. DOWNLOADS INVENTORY (`/tmp/d2/`)

Successfully obtained and read (primary or vendor-primary text):
- `ipsos_loyalty_myth8.pdf` / `.txt` — Ipsos, "Loyalty Myth #8" excerpt (Keiningham/Vavra/Aksoy/Wallard, *Loyalty Myths*, 2005)
- `keiningham_npjm_2007.pdf` / `.txt` — Keiningham, Cooil, Andreassen & Aksoy, *Journal of Marketing* 2007
- `grisaffe_2007.pdf` / `.txt` — Grisaffe, *JCSDCB* 2007
- `ascarza_2018_retention_futility.pdf` / `.txt` — Ascarza, *JMR* 2018 (from her own faculty site)
- `verbeke_2012_churn.pdf` / `.txt` — Verbeke et al., *EJOR* 2012 (ResearchGate-hosted copy)
- `bain_closingdeliverygap.pdf` / `.txt` — Allen/Reichheld/Hamilton/Markey, Bain 2005
- `bain_prescription_cutting_costs.pdf` / `.txt` — Reichheld/Bain, ~2001–2002

Failed/unusable downloads (kept for the record, per instructions — do not re-attempt these exact URLs without a different route):
- `rs1990_a2a7d708.pdf` — 404 HTML, not the 1990 HBR article
- `bain_zerodef.html` — Cloudflare JS challenge page, not the article
- `scribd_zerodef.html`, `scispace_zerodef.html` — JS-shell landing pages, no body text
- `neslin_2006.pdf`, `neslin_page.html` — HTML/redirect shells, not Neslin et al.'s actual PDF
- `sharp_6020.pdf`, `sharp_pareto.html` — SSRN/Ehrenberg-Bass JS shells, no extractable text (Pareto findings above came from WebFetch's own rendering, not from these files)
- `grisaffe_page.html` — landing page only (superseded by the successful `grisaffe_2007.pdf` download)

Total: 7 primary documents fully read and quoted; 6 dead-end artifacts documented so no future worker re-wastes a cycle on the same URLs.
