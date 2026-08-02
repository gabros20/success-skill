# _raw: X practitioners — CS canon, health scores, NPS, churn, renewal/expansion (channel B, worker 3)

Tool: `xrelay`. Method: `archive user` (full-fidelity, unwraps retweets) on the two deepest
archives (`lincolnmurphy`, `jasonlk` — attempted), local grep/jq on the JSON for the rest; targeted
`from:<handle>` searches for authors where full archive was infeasible; lead-chasing for two named
tips from the channel brief. All non-retweet (`retweetedBy` absent) unless noted. Dates/permalinks
verbatim below.

## Operational note on tool behavior (for the record)

- `lincolnmurphy` archived cleanly: `archive user lincolnmurphy --limit 800` → 784 tweets, ~1MB,
  saved to `_raw/lincolnmurphy.json`. Zero retweets in the set (all self-authored).
- `jasonlk` (112,989 posts) — **archive timed out 3x** (2min/3min/4min limits, even at `--limit 150`)
  and `user-posts --limit 100` also timed out at 90s. `xrelay user jasonlk` (single call, no
  pagination) succeeded instantly, confirming the account/session is fine — the timeline endpoint
  itself is just slow/heavy for this account, independent of the channel-wide throttle. Fell back to
  targeted `from:jasonlk <keywords>` searches instead (single-page, fast) — lower recall than a full
  archive, but the finds below are real and dated.
- `nickmehta`: `xrelay search "from:nickmehta"` returned **zero tweets** (empty result, no error).
  Confirms the brief's earlier `xrelay user` NULL finding via a second method. **Finding: Gainsight
  CEO Nick Mehta is not reachable on X via this tool — either inactive, protected, or shadow-banned
  from this session's view.** Do not burn more calls on this; flag to channel D if his commentary
  matters (LinkedIn/blog would be the fallback).
- `gregdaines`/`gdaines`: not re-attempted (per brief, already burned/dead). Flagging to channel D:
  chase "Greg Daines, Client Success churn researcher" off-X.
- `ChurnRx`: not re-attempted (dead per brief).
- General topical search (`"health score" churn customer success`, `"health score" (didn't predict OR
  useless OR folklore...)`) reproduced the charter's pollution warning almost exactly: results were
  dominated by fitness-app health-score content, crypto "health score" token gimmicks, and generic
  job-board posts — **zero usable CS signal** from two broad sweeps. `from:<handle>` authority routing
  is confirmed as the only productive instrument for this territory.

---

## 1. Health scores — flagship candidate (wedge hypothesis 2)

### Advocates / adoption
- **John Owen (@jeowen), President/CEO of Airshare (@flyairshare)**, via interviewer
  **@fortworthchris** (podcast-clip account, not jeowen's own words — filtered through the
  interviewer's framing):
  > "I asked John Owen (@jeowen) what data matters most to him. His answer was customer happiness.
  > @flyairshare tracked NPS for years. Recently they moved to a customer health score built from
  > seven criteria. In this clip, John discusses why customer happiness is the ultimate data metric
  > and what their team does when the score isn't up to standards."
  — https://x.com/fortworthchris/status/2065779720046973152 (Jun 13 2026)
  **Chased the thread**: no replies expand on what the seven criteria actually are, whether the
  switch was measured against anything, or what "up to standard" means numerically — it's a video-clip
  teaser, and the substantiating detail (if any) is inside a video I can't transcribe from this tool.
  **This is a named real practitioner (private-jet operator, not a SaaS company) switching FROM NPS
  TO a health score** — valuable because it cuts against the skeptic case, but it is anecdotal
  (single company, no denominator, no pre/post churn comparison, delivered via a promotional
  interview series) — not evidence the switch improved anything.

### Skeptics
- **@hakanozturkhq** (Paris; bio: "Customer Success systems for renewals, QBRs & exec trust. Weekly
  playbooks for 4,300+ CS pros." — 958 followers, content-marketer/consultant in the CS niche, low
  authority but a working insider, not a vendor):
  > "CFO: Where's the 95% health score coming from? Customer Success: Our internal model. CFO: Who
  > built the model?"
  — https://x.com/hakanozturkhq/status/2083914302805750243 (Aug 2 2026)
  This is exactly the skeptic framing the charter wants: a meme calling out that health scores are
  self-certified black boxes with no external validation. No methodology or measured claim attached
  — it's a rhetorical jab, not a study, but it names the right question (who validated the model?).
- **lincolnmurphy** doesn't attack "health score" as a term directly in the archived set (784 tweets,
  0 exact hits on "health score" besides one self-promotional AI-agent-bundle tweet — see §7), but
  his entire body of work is structurally skeptical of any single proxy metric standing in for
  "customer success" (see NPS section below, and the CSM-ratio-myth pattern in §3) — the same
  epistemic objection generalizes to health scores even though he doesn't say the words. Treat as
  **inferred**, not a direct quote — do not cite as if he said "health scores are folklore."

### Verdict on wedge hypothesis 2
**Needs channel D's evidence — not confirmed or refuted by this channel's search.** What I found:
(a) one practitioner switching TO a health score with zero measurement disclosed, (b) one low-reach
skeptic meme questioning model provenance, (c) zero practitioner posts of the form "our health score
didn't predict a single churn" (the exact confession-shaped post the brief hoped for — I did not find
it despite three search angles). The X corpus is thin on this specific question — practitioners talk
ABOUT health scores constantly (as a category/feature to build/sell — confirmed via the polluted
searches, e.g. thekevinjon's "After analyzing 200+ SaaS companies, winners track: Customer Health
Score" vendor-style claim, unsourced, 3 likes) but rarely PUBLISH a retrospective on whether the score
predicted anything. This absence is itself weak evidence for the "folklore" wedge (if it worked
reliably and validatably, someone selling CS services would trumpet the case study) but it is an
absence, not a disconfirmation — recommend the controller weight this on web/GitHub findings (churn
model repos, published methodology) rather than X.

---

## 2. NPS — criticism and defense

### The critic: hnshah (Hiten Shah), primary quote, NOT growth's summary
> "High Net Promoter Score (NPS) does not correlate to high retention. NPS is just one of a few ways
> to understand customers NOT to understand retention. Folks are using NPS as 'one metric to rule
> them all.' That's not how to use it. More here: [link]"
— https://x.com/hnshah/status/1094305710819573761 (Feb 9 2019)

Supporting/earlier hnshah NPS posts (context, not new claims):
- "@ngauthier usage / retention -> do users keep using the tool, how often and why (qualitatively)
  plus customer satisfaction via NPS" — https://x.com/hnshah/status/808698474698928128 (Dec 13 2016)
  — shows hnshah treated NPS as one qualitative-adjacent signal among several even three years
  earlier, consistent with the 2019 critique (not a reversal).
- Curated/shared links (his own text is minimal, worth noting as topic-interest not new argument):
  "How well does NPS predict rebooking for @airbnb?" — https://x.com/hnshah/status/676190018554187776
  (Dec 14 2015); "What's the relationship between NPS and retention?" —
  https://x.com/hnshah/status/1026520864081281025 (Aug 6 2018); "What are the best NPS results for
  B2B SaaS?" — https://x.com/hnshah/status/1087779398072393728 (Jan 22 2019).
  **These are link-shares, not hnshah's own argument** — the 2019 quote above is the one primary
  critique statement; cite that one, not the link-shares, as "hnshah's position."

### The critic-adjacent: lincolnmurphy on NPS (own mailing-list marketing, not a public thread)
- "I just sent an email to my mailing list with the subject: 'NPS sucks... do this instead'... the
  value in this email is HUGE." — https://x.com/lincolnmurphy/status/1063544703524704261 (Nov 16 2018)
- "Tomorrow I'll share... a secret question I've been using with my clients that makes NPS look like
  the garbage metric that it is." — https://x.com/lincolnmurphy/status/1063215860914024448 (Nov 15 2018)
- "My 'expansion comp plan' email had the highest unsubscribe rate by far for 2018. Far more than the
  'nps sucks' one." — https://x.com/lincolnmurphy/status/1072936731056336897 (Dec 12 2018)
  **Credibility caveat: this is a content-marketing funnel, not an argued critique** — Murphy never
  states the actual argument in public tweets, only teases a paid/email-gated "secret question."
  Cite as "a consultant selling an alternative to NPS," not as a substantive methodological critique
  — unlike hnshah's 2019 quote, there is no falsifiable claim here to evaluate.

### The defender: @yarotheslav — LOW CREDIBILITY, flag as such
- "You've seen this popup. It's called 'Net Promoter Score' (NPS). Great for collecting customer
  satisfaction over time." — https://x.com/yarotheslav/status/2083623701451280637 (Aug 1 2026)
- "gem 'testimonials' ships an NPS feature. You can collect user sentiment without any 3rd party
  dependencies!" — https://x.com/yarotheslav/status/2083623703254798579 (Aug 1 2026)
  Account vetted: Yaroslav Shmarov, 3,697 followers, not verified, Ukraine-based, bio is emoji-only
  (no stated CS/CX expertise). **This is a Ruby-gem author promoting his own open-source
  "testimonials" library's NPS feature — self-promotional, not an informed defense of NPS as a
  metric.** Present in the report as "the closest thing to a public NPS defense found on X in this
  sweep," with the caveat that it is not a considered argument — it's a product-marketing tweet that
  happens to use NPS approvingly. The contested question (is NPS defensible) is **NOT well-represented
  on the defender side in this corpus** — this is itself a finding: X skews toward NPS-skeptical
  practitioner takes, defenses are mostly implicit (vendors shipping NPS features) rather than argued.

### Contested question, stated explicitly
Does NPS correlate with retention/growth at all? hnshah (2019, primary): no, doesn't correlate to
high retention, misused as a catch-all. No public X thread found arguing the opposite with method or
data — the "defense" found is a feature-shipping tweet, not an argument. **Channel D should carry
this** (the brief already flags Keiningham et al replication-failure literature as the academic side;
X does not supply an academic-quality NPS defense).

---

## 3. CSM ratios, QBRs, enterprise CS playbook

This produced the single clearest **contested-number** finding of the whole sweep: the "$2M ARR per
CSM" figure is simultaneously treated as industry-standard shorthand AND explicitly, repeatedly,
publicly called a myth by the same authority (lincolnmurphy) over multiple years.

**The figure, repeated as fact:**
- @saastr (SaaStr's own account, not jasonlk personally): "You'll want $500k-$1m in ARR per CSM
  coverage, and as you come up on $2m-$3m, that's just not enough coverage with a few CSM..."
  — https://x.com/saastr/status/1132844104050724864 (May 27 2019)
- @saastr: "In Customer Success, we'll probably need about 20 headcount: Assume $1.5m ARR per CSM."
  — https://x.com/saastr/status/1213173372068212737 (Jan 3 2020)
- @lukesophinos: "A few general SaaS ratios... ✔️$5M ARR per Support Rep ✔️$2M ARR per CSM ✔️$5M ARR
  per Expansion Rep ✔️10:1 Employees to Manager ✔️6:1 Engineers to PM. What else?"
  — https://x.com/lukesophinos/status/1466468241254060034 (Dec 2 2021) — **zero source cited**, framed
  as "general SaaS ratios," textbook unsourced-benchmark-table pattern the charter's falsification
  duty targets (figure-CLASS: unsourced ratio "benchmarks").
- @GregLangdon: "Industry data on the average number of clients that a single Customer Success
  Manager handles, and on ARR per CSM... broken out by market segment: enterprise, mid-market, SMB."
  — https://x.com/GregLangdon/status/1088860159441555456 (Jan 25 2019) — links to a report I did not
  fetch (X-search only); flag to channel D if the underlying source matters.

**The same figure, explicitly debunked by lincolnmurphy — three separate years:**
- "Please STOP perpetuating the $2M/ARR per CSM myth... I've provided an alternative (based on actual
  reality) in this post..." — https://x.com/lincolnmurphy/status/814160673840267264 (Dec 28 2016)
- "Ugh. So #CustomerSuccess myths like $2M ARR per CSM are being perpetuated at #SaaStrAnnual — here's
  a better option:" — https://x.com/lincolnmurphy/status/829735323600957440 (Feb 9 2017)
- "The '$2M ARR per CSM' nonsense is just what people want to hear. It's easy. Simple. Just happens to
  have little connection to actual reality" — https://x.com/lincolnmurphy/status/829780774215757824
  (Feb 9 2017)
- "Any 'definitive' answers to number of accounts per CSM are wrong. You can't do that. This isn't
  Account Management. Evolve or stop talking." — https://x.com/lincolnmurphy/status/923340143922171905
  (Oct 26 2017)
- Earlier, same theme: "one-size-fits-all approaches, ARR per CSM, no customer segmentation, no ops,
  churn focus instead of growth-centric" — https://x.com/lincolnmurphy/status/736400686448005120
  (May 28 2016)

**Read on this**: the "$2M ARR per CSM" number is a textbook case of an industry benchmark that keeps
circulating (SaaStr's own account restated versions of it in 2019 and 2020, THREE YEARS after
Murphy's public debunking in 2016-2017) despite a named, credentialed critic calling it out by name
at the very conference (SaaStrAnnual) where it was being repeated. This is directly useful evidence
for wedge hypothesis 1 (enterprise-CSM-team literature runs on unexamined heuristics) — cite BOTH
sides with both permalinks, do not just cite the number.

No QBR-specific practitioner critique found in this sweep beyond lincolnmurphy's structural framing
(see §4 handoff/renewal notes) — QBR-as-artifact discourse (cadence, content) not covered; flag as an
open question for channel D/A.

---

## 4. Renewals and expansion — the sales seam

Directly relevant to the charter's unbuilt seam: "success owns renewal workflow + expansion SIGNALS;
sales owns the expansion SALE in sales-assisted motions."

lincolnmurphy has a coherent, repeated position (2019, elaborated over several tweets same day —
Jan 13 2019 — reads as a single train of thought, likely a thread/reply chain):
- "Renewals should be part of Customer Success Management, but who does it depends on the customer
  segment. If CSM can push a button to renew, they do it. If it's complex, then dedicated resources.
  Sounds like what you had was just a carryover from traditional Account Management."
  — https://x.com/lincolnmurphy/status/1084526744290369537
- "For complex renewal process, you'll need dedicated resources. So in the same company, some
  customers are renewed by CSM, some will need a dedicated resource, and some in-between."
  — https://x.com/lincolnmurphy/status/1084522527991480325
- "Alignment, yes, but one resource should handle renewal (and expansion), otherwise you'll end up
  with everyone stepping on each other..." — https://x.com/lincolnmurphy/status/1084524227393409024
- "Renewal must be seen as PART of the customer's journey toward success, though. Not something
  extra. Who does it should depend on complexity..." — https://x.com/lincolnmurphy/status/1084523828552912897
- Earlier statement of the general principle: "Expansion AND renewal are part of the customer's
  journey toward success. But you like to hide from — and otherwise avoid talking about — renewals
  with the customer." — https://x.com/lincolnmurphy/status/1092871764311490561 (Feb 5 2019)
- "Expansion is PART of the customer's journey toward success." (hashtagged #CustomerSuccess
  #Sales — his own tagging implies a cross-functional read) — https://x.com/lincolnmurphy/status/1092483228894744578
  (Feb 4 2019)
- Sharper framing: "'Expansion — not simple renewal — is the ultimate indicator of a successful
  customer.'" (quoting his own blog post title) — https://x.com/lincolnmurphy/status/1626657270317604880
  (Feb 17 2023)
- The "Sales-to-CS handoff" pain point, directly on the seam: "Customers hate three things: 1.
  Surprises 2. Unknowns 3. Repeating themselves. Most Sales-to-CS handoffs manage to hit all three."
  — https://x.com/lincolnmurphy/status/2019458553430384815 (Feb 5 2026)

**SEAM FLAG for the controller**: Murphy's practitioner position is complexity-based ownership, not
role-based — the CSM owns renewal by default, but as soon as a renewal is "complex" (implying larger
accounts, negotiated terms, multi-stakeholder), a **dedicated resource** takes over, and he explicitly
says this dedicated resource is NOT sales-flavored "Account Management" carryover but something
CS-native. This actually cuts slightly AGAINST the charter's provisional seam ("sales owns the
expansion SALE in sales-assisted motions") — Murphy would say complex renewal/expansion should still
be a CS-owned specialist, not handed to sales. Record as a contested boundary call, not an
endorsement of either side.

- jasonlk on NRR ceiling for self-serve/SMB — directly relevant to the solo/self-serve honesty
  wedge (hypothesis 1): "'It's often easier to start with SMBs. They self-serve, they close fast,
  they have one stakeholder. But the NRR is brutal at scale. It's hard to even cross 100% NRR from
  true SMBs.'" — https://x.com/jasonlk/status/2083503254743523480 (Aug 1 2026) — note this reads as
  jasonlk quoting/relaying someone else's framing (leading quote mark, no attribution visible in the
  compact text) — treat the claim as "jasonlk amplified this view," not necessarily his own coinage.
- jasonlk, logo churn vs downgrade distinction (useful definitional clarity for the churn-benchmark
  section): "A pause is better than a cancel. A downgrade is much better than a cancel. A downgrade is
  not logo churn. It is just a downgrade." — https://x.com/jasonlk/status/1244999979401240577
  (Mar 31 2020)
- jasonlk on SMB churn being structural: "The hardest segment in B2B: Sales-led SMB sales. You have
  to be wildly, wildly efficient and effective. And you have to further fight the inherent churn in
  SMBs. CAC has to be really, really low..." — https://x.com/jasonlk/status/2081387728437207284
  (Jul 26 2026)

---

## 5. Churn benchmarks — denominator check

Per the falsification duty, most quoted churn figures in this sweep had **no defined denominator**.
Specific findings:
- lincolnmurphy's own "acceptable churn rate" confession is the most valuable find here — not a
  number, but a **first-person account of how an unsourced figure propagates**:
  > "To be clear, they didn't 'ask' me. They googled 'acceptable churn rate' and found a post of mine
  > from years ago where I quoted a VC firm. If they had actually asked me, my response — and maybe
  > their story — would be different. This is how outdated concepts continue to propagate."
  — https://x.com/lincolnmurphy/status/1046814748929609728 (Oct 1 2018)
  **This is a primary-source confession that a "churn benchmark" figure he himself once quoted (from
  an unnamed VC firm, no further citation given even here) is still being googled and treated as
  gospel years later, disconnected from its original (thin) sourcing.** Directly usable for the
  falsification-strip: it is a first-person account of exactly the propagation mechanism the charter
  warns about, though it does NOT give us the actual number or the VC firm's name (Murphy doesn't
  name either here) — would need to find the original blog post to get the number+VC-firm citation;
  flag to channel D as "find Lincoln Murphy's original churn-rate blog post quoting a VC firm" if the
  specific number matters.
- lincolnmurphy's "Churn Classification Quadrant" (Green=good-but-still-bad, Red=really bad) —
  https://x.com/lincolnmurphy/status/996094696962347008 (May 14 2018) — a qualitative framework, not
  a numeric benchmark; useful for "not all churn is the same" framing, no denominator issue since it
  makes no numeric claim.
- jasonlk's logo-churn-vs-downgrade distinction (§4 above) is the clearest **definitional** finding
  in this territory — most churn discourse conflates logo churn, revenue churn, and downgrades; this
  tweet is a clean primary statement that a downgrade ≠ logo churn.
- No practitioner-reported numeric churn rate with an explicit denominator (e.g., "our monthly logo
  churn is X% of accounts") surfaced in this sweep. This absence itself supports the charter's
  suspicion that quoted churn numbers mostly lack denominators — recommend channel D chase actual
  published cohort/benchmark reports (ProfitWell/Paddle, ChartMogul, KeyBanc SaaS survey) since X
  practitioners overwhelmingly discuss churn qualitatively/strategically, not with cited rates.

---

## 6. VoC / customer feedback → product loops

Thin territory in this sweep — the archived corpus (lincolnmurphy, 784 tweets) had almost no direct
"VoC" or product-feedback-loop content; his focus skews to expansion/renewal/growth framing, not
feedback-to-product mechanics. One tangential find on QA/feedback cost:
- "Listening to the recording of a 25 minute call between a CSM and a client to provide feedback
  takes me roughly 4 hours." — https://x.com/lincolnmurphy/status/1047272797909798912 (Oct 2 2018)
  Useful as a cost-of-manual-QA data point (relevant to quality-skill's QA-rubric adjacent territory
  and to the AI-agent-era discourse in §7 — this is exactly the kind of task an AI QA/coaching tool
  claims to automate now).

**Open question, flagged for channel A/D**: does anyone publicly quantify the VoC → product loop
(e.g., "X% of our roadmap came from CS-surfaced feedback")? Not found here.

---

## 7. The CS-is-dead / AI-replacing-CSM discourse (2024-26)

lincolnmurphy is actively engaging this in 2026 (recent, high-relevance to wedge hypothesis 3):
- "Customer Success is at a crossroads. Again. Economy slows down. Cut CS. AI arrives. Replace CS
  with agents. In March 2026, we've got both. There's a better response than defend and justify and
  worry. Next-level your org and ops." — https://x.com/lincolnmurphy/status/2032170317263556679
  (Mar 12 2026) — note this is also a webinar-sales pitch (his consulting business), so the framing
  ("there's a better response") is itself a product pitch — cite the diagnosis, discount the
  solution-tease.
- "Once a customer believes they can replace you with a general-purpose AI tool, you're no longer
  proving value. You're defending your existence. If you're in CS, CX, or running a SaaS company,
  this fight just landed on your desk whether you wanted it or not."
  — https://x.com/lincolnmurphy/status/2021649014631112913 (Feb 11 2026)
- "'Nice product you got there. Sure would be a shame if someone vibe coded a replacement.' That's
  SaaS renewals now. Your customers don't want to build it themselves. They just want you to know
  they could. 'Give me a discount and this whole idea goes away.'"
  — https://x.com/lincolnmurphy/status/2022384728213795278 (Feb 13 2026) — **directly relevant to
  the renewals territory**: AI/vibe-coding as a new renewal-negotiation leverage point, not (yet) an
  actual replacement threat — the threat is used as pricing leverage by customers, per Murphy.
- Self-promotional but relevant: he's giving away "Five AI agents for Customer Success" (The
  Invisible Handoff, The Trust Radar, The Expansion Signal Detector, The Churn Risk Summarizer, The
  Earned Ask) tied to a webinar — https://x.com/lincolnmurphy/status/2035101801905869116 (Mar 20
  2026). Names ("Churn Risk Summarizer") show vendor/consultant-side framing of health-score-adjacent
  AI tooling as of Mar 2026 — useful as a snapshot of what a CS consultant is packaging right now, not
  as evidence any of these agents work.
- Low-reach poll, worth noting as a discourse snapshot not a finding: @success_hacker (0 likes):
  "Where will AI change Customer Success the most? More accounts per CSM / Predicting churn early /
  Killing the busywork / A true thinking partner" — https://x.com/success_hacker/status/2082484380484645088
  (Jul 29 2026) — frames "more accounts per CSM" as an AI-driven possibility, tying back to §3's
  ratio discourse.

**Read**: the CSM-role-contracting question is genuinely contested and live as of 2026 — the
loudest voice (lincolnmurphy) frames it as a threat CS must respond to strategically, not as a
settled "role is disappearing" narrative, and simultaneously monetizes the anxiety (webinars, agent
giveaways). No countervailing "CSM role is fine, AI changes nothing" voice surfaced in this sweep —
absence noted, not a finding of consensus.

---

## Practitioner roster with credibility notes

| Handle | Followers | Role/angle | Receipts vs. selling |
|---|---|---|---|
| lincolnmurphy | 18,060 | Self-described CS inventor, consultant | **Sells consulting/webinars/workshops explicitly in nearly every tweet** — treat all "myth-busting" claims as also marketing (he sells the "better option"). Still the most substantive, longest-running, and most self-consistent voice found (debunked the same $2M/CSM myth across 2016/2017/2017, still coherent in 2026 on AI). Canon-with-interest per the charter's own framing — confirmed. |
| jasonlk | 246,269 | SaaStr founder | High-reach amplifier of SaaS metrics/ratios; often quote-relays others' framings rather than original claims (note the leading-quote-mark NRR tweet). Full-archive access failed (tool timeout on this account specifically); findings here are from targeted search only — lower recall, real but partial. |
| hnshah | 340,317 | Hiten Shah, product/growth figure | One substantive, falsifiable NPS critique (2019) plus years of neutral link-sharing on NPS — genuinely the most "receipts" of anyone found (states a specific claim: NPS doesn't correlate to retention) though the underlying link (not fetched here) would need chasing by channel D to see if it cites a study or is also just his opinion. |
| @fortworthchris | not vetted (interviewer/podcast-clip account) | Business-podcast clipper | Relaying a named practitioner (jeowen), not an authority himself — treat the health-score finding as secondhand/anecdotal by construction. |
| @yarotheslav | 3,697 | Ruby-gem author | Self-promotional NPS-feature tweet; not a considered defense. Low credibility, flagged explicitly above. |
| @hakanozturkhq | 958 | CS content-marketer/consultant, building a CS job board | Low reach but a working CS-niche insider; the health-score skeptic meme is the closest thing to a "who validated this" challenge found on X. |
| @saastr | (SaaStr brand account) | Conference/community brand | Repeated the "$2M ARR/CSM" figure in 2019 and 2020 — three years after Murphy's public debunking of the same figure at the SAME conference. Direct evidence the myth outlives its correction. |
| nickmehta (Gainsight CEO) | n/a | — | **Unreachable via xrelay** (both `user` and `search from:` return null/empty) — confirmed twice by two different methods across this run. Not evidence he's inactive on X generally, just unreachable via this tool/session. |
| gregdaines / gdaines / ChurnRx | n/a | — | Confirmed dead-end handles per prior worker's finding; not re-attempted. Flag `Greg Daines` (Client Success, churn researcher) to channel D as a name to find off-X. |

---

## Contested questions (explicit)

1. **Do health scores predict anything real?** Not resolved by X. One adoption anecdote (no
   measurement disclosed), one skeptic meme (no measurement disclosed either — just a "who built it"
   challenge). No practitioner "our health score failed" confession found despite three search
   angles. **Verdict: needs channel D.**
2. **Does NPS correlate with retention?** hnshah (2019, primary, falsifiable): no. No argued rebuttal
   found on X; the closest "defense" is a self-promotional feature-shipping tweet. Leans toward the
   skeptic side by absence of a counter-argument, but the sample is thin.
3. **Is "$2M ARR per CSM" a real ratio or folklore?** Explicitly and repeatedly called a myth by a
   named authority (lincolnmurphy, 2016-2017) while the SAME figure kept circulating via a bigger
   platform (@saastr, 2019 and 2020) — this is the strongest "figure persists despite public
   correction" case found in this entire sweep. Recommend citing both sides with both dates as a
   worked example of how CS "benchmarks" propagate unexamined.
4. **Who owns complex renewal/expansion — CS or sales?** lincolnmurphy's public position (2019) is
   complexity-gated CS ownership, explicitly rejecting "Account Management carryover" framing — this
   is in tension with (not identical to, but not clearly aligned with either) the charter's
   provisional "sales owns the expansion SALE" seam. Flagged for controller adjudication, not
   resolved here.
5. **Is the CSM role contracting because of AI?** Live, contested, and monetized-by-the-people-
   discussing-it (lincolnmurphy sells "next-level your ops" responses to the same anxiety he
   describes) as of 2026. No settled view found; no "AI changes nothing" counter-voice surfaced.

---

## Folklore / unsourced-figure sightings (never-ship-CLASS)

- **"$2M ARR per CSM"** — repeated as fact by @saastr (2019, 2020) and @lukesophinos (2021, "general
  SaaS ratios," zero citation) despite lincolnmurphy's public 2016-2017 debunking at the very
  conference where it circulated. See §3 and contested question 3 above. Both propagation AND
  correction have permalinks — cite both.
- **"Acceptable churn rate" (unnamed number)** — lincolnmurphy's own 2018 tweet confirms he once
  quoted a VC firm's churn-rate figure in an old blog post, that the specific number is still being
  googled and treated as current guidance years later, and that neither the number nor the VC firm is
  named even in this confession tweet. The **figure-CLASS instance** (an unsourced/thinly-sourced
  churn-rate "acceptable" threshold still propagating) is captured; the actual number was NOT
  recovered in this sweep — flag to channel D: find Murphy's original blog post to get the number +
  VC-firm citation, or flag as untraceable if the post is gone.
- **"After analyzing 200+ SaaS companies, winners track: Customer Health Score..."** —
  @thekevinjon, https://x.com/thekevinjon/status/1961462607652819108 (Aug 29 2025, 3 likes) —
  textbook unsourced-methodology vendor-content pattern (no named companies, no method, no link to
  data) surfaced during the polluted general search; low-reach but a clean example of the genre for
  a "folklore sightings" gallery if the report wants one.
- No sighting of the specific charter-listed strings ("5-25x cheaper to retain," "5% retention →
  25-95% profit," "80% of revenue from 20%," "96% of unhappy customers don't complain," CSAT/CES
  benchmark tables) in this X sweep specifically — either they didn't surface in the queries run, or
  X practitioners in this territory don't quote those exact figures verbatim as often as blogs/decks
  do. Recommend channel D treat this as "not found on X in this pass," not "absent from the
  discourse."

---

## Open questions for the lead / cross-channel flags

- **Seam flag (sales)**: lincolnmurphy's complexity-gated renewal-ownership position (§4) should be
  weighed against whatever channel A/D/skills-ecosystem find for the actual charter seam language —
  it's a real practitioner voice that doesn't cleanly agree with "sales owns the expansion sale."
- **Channel D**: chase hnshah's linked NPS-retention source (not fetched here, link present in the
  2019 tweet's card but not resolved by this tool); chase lincolnmurphy's original "acceptable churn
  rate" blog post for the actual number + VC-firm citation; chase Nick Mehta's actual public
  commentary via LinkedIn/blog since X is a dead end; chase Greg Daines (churn researcher) off-X.
- **Channel A (skills-ecosystem)**: the "$2M ARR per CSM" contested-benchmark case (§3) is a good
  concrete example if the family wants a worked "here's how a CS benchmark actually propagates"
  sidebar.
- Tool-reliability note for future workers: **`archive user` on very-high-volume accounts (100k+
  posts) can time out even at small `--limit` values** — this is a per-account cost, not just
  channel-wide throttle (confirmed: `xrelay user jasonlk` single-call succeeded instantly while
  `archive`/`user-posts` on the same handle timed out repeatedly). For future deep-dives on
  hyper-prolific accounts, budget for `from:<handle> <keyword>` targeted search instead of a full
  archive.

## Source files
- `research/_raw/lincolnmurphy.json` — full archive, 784 tweets, generated via `xrelay archive user
  lincolnmurphy --limit 800`.
- `research/_raw/jasonlk_posts.json` — empty/failed (0 bytes, timeout); left on disk as evidence of
  the failed attempt, not a usable source.
