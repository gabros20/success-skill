# Channel B · x-practitioners — report

Sub-orchestrator: channel B lead · 3 sonnet workers + lead slice · captured 2026-08-02 · tool: `xrelay`

**Raw files (every claim in this report traces to one of these):**
- [`_raw/_raw-x-ai-support.md`](_raw/_raw-x-ai-support.md) — 482 lines · worker 1 · the AI-support-agent
  discourse 2024–26, deflection-vs-resolution, Klarna, vendor claims, escalation policy
- [`_raw/_raw-x-cs-canon.md`](_raw/_raw-x-cs-canon.md) — 429 lines · worker 3 · CS canon, health scores,
  NPS, CSM ratios, renewals/expansion, churn benchmarks
- [`_raw/_raw-x-solo-support.md`](_raw/_raw-x-solo-support.md) — 153 lines · worker 2 (robwalling only,
  stalled) **+ lead top-up** (Shpigford, arvidkahl) · solo-founder support reality ·
  **PARTIAL — see §12**
- [`_raw/_raw-x-lead-slice.md`](_raw/_raw-x-lead-slice.md) — 345 lines · lead · method findings, Klarna
  primary, Salesforce/Fin closure, Pylon market data, Decagon, **patio11 support economics**
- [`_raw/lincolnmurphy.json`](_raw/lincolnmurphy.json) — 784-tweet full archive (worker 3's instrument)

Grading key (charter rule 5): **M** measured-with-method · **P** practitioner-report ·
**V** vendor-folklore · **D** discourse-belief only · **U** untraceable.

---

## Verdict

**The strongest theme is not a fact, it is a measurement failure.** The AI-support era runs on a
metric — "resolution rate" — that **no source in this corpus, vendor or practitioner, defines
precisely enough to audit.** Fin's publicly claimed resolution rate ranges across **40 / 64 / 67 /
71 / 73.1 / 75 / 76 / 80+ / 83%** depending on customer, date, and which of at least three different
metrics (resolution rate / automation rate / share-of-volume-handled) is being quoted — and none of
the citations disclose how "resolved" is adjudicated (bot self-report? customer-confirmed? no reopen
within N days?). That absence is the channel's central finding and the strongest available support
for **wedge hypothesis 3**. It also generalises: the same "number with no denominator" pathology
shows up in CSM ratios (§3) and churn benchmarks (§5).

**The biggest surprise is that the industry's most-repeated cautionary tale is contested at the
primary-source level.** "Klarna replaced support with AI, it failed, they rehired humans" is treated
as settled by four independent authors — and Klarna's CEO says in his own posts that the "we failed
with AI" reading is **a misquote**. Both poles are near-primary. Neither is safe to adopt.

**The second surprise is a live incumbent collapse**: Salesforce is acquiring Fin (fka Intercom) for
**$3.6B in cash**, announced Jun 15 2026, closing EOY — confirmed by both lead investors' own
accounts. A direct competitor's CEO predicts the standalone helpdesk gets deprecated. **Any tooling
recommendation this pack ships has a short shelf life**, which is an anti-staleness argument the pack
must build in, not a footnote.

**Third: `patio11` supplies the angle the entire enterprise CS canon misses** — support volume as an
output of *pricing and segmentation*, not a process to optimize. This is the most distinctive
material the channel found and it cuts against the pack's own scope in a useful, honest way.

**On the wedge hypotheses:** H1 **supported, from an unexpected direction** (§7). H2 **NOT resolved
by X — needs channel D** (§1). H3 **strongly supported** (§2, §4).

---

## 1. Health scores (wedge hypothesis 2) — NOT RESOLVED HERE

Worker 3 ran three search angles and reports the honest null. What exists on X:

- **One adoption anecdote**: Airshare (@flyairshare) "tracked NPS for years. Recently they moved to a
  customer health score built from seven criteria" — John Owen, via interviewer @fortworthchris,
  https://x.com/fortworthchris/status/2065779720046973152 (Jun 13 2026). The seven criteria are never
  stated; no pre/post churn comparison; it's a promotional video teaser. **A named practitioner moving
  TO a health score — which cuts against the skeptic case — but with zero measurement disclosed.**
- **One skeptic meme**, and it names exactly the right question — @hakanozturkhq (958 followers, CS
  consultant), https://x.com/hakanozturkhq/status/2083914302805750243 (Aug 2 2026):
  > "CFO: Where's the 95% health score coming from? Customer Success: Our internal model. CFO: Who
  > built the model?"
- **Zero** practitioner posts of the form "our health score didn't predict a single churn," despite
  three search angles.

**Do not cite lincolnmurphy as a health-score skeptic.** Worker 3 checked the 784-tweet archive: he
never attacks the term. His skepticism of single-proxy metrics generalizes, but that is *inference*,
and the raw file marks it as such.

**Verdict: needs channel D.** The absence of published retrospectives is weak evidence for the
folklore reading — if health scores validated cleanly, someone selling CS services would have shipped
the case study — but an absence is not a disconfirmation. **Recommend the controller weight the
flagship decision on D's evidence and C's churn-model repos, not on X.**

### ⭐ But X does supply the flagship's best ILLUSTRATION (found in the lead's top-up)

**Josh Pigford (@Shpigford), founder of Baremetrics — a company whose product WAS subscription
churn analytics, later sold for $4M** — https://x.com/Shpigford/status/874287345041846281 (Jun 12
2017), complete and verbatim:
> "What did we do to cause our churn to get cut in half?  ¯\\_(ツ)_/¯"

Grade: **P**. The founder of a churn-measurement company, instrumenting his own funnel with his own
best-in-class tooling, **publicly could not attribute a 2× improvement in his own churn** — and said
so, against every incentive to claim credit. This is first-person evidence that churn causality
resists attribution even under ideal measurement conditions. **Recommend this as the flagship's
anchor anecdote for "what a health score can honestly predict"**: short, memorable, from a named
credible operator, and it lands the epistemics better than any study will.

He also supplies **the denominator-bearing churn number worker 3 reported did not exist on X** —
https://x.com/Shpigford/status/779016111962619904 (Sep 22 2016): "nearly **15% monthly User Churn**
for the **$250 ARPU** cohort." Metric + cohort + period, all stated. **Use it as a model of how to
state a churn number, not as a benchmark** — it is one company, one cohort, 2016.

## 2. Deflection vs resolution — the richest seam (wedge hypothesis 3)

Every non-vendor voice says deflection ≠ resolution; no vendor defines the difference. Best
articulations, with credibility stated plainly (most are low-reach — they show the *shape* of the
critique, not its traction):

- @ahaanpandit (3,264 followers, @dodopayments), https://x.com/ahaanpandit/status/2045003141645795406
  (Apr 17 2026) — **P (weak)**, the "5 to 10%" is asserted without method:
  > "Deflection rate on those deployments looks clean. Resolution rate on the same tickets is usually
  > 5 to 10%. The rest churn or escalate through a side door. Deflection is cost. Resolution is customer."
- @mumento_mori (16 followers, **8 views** — an articulation, not a signal),
  https://x.com/mumento_mori/status/2082805059075953012 (Jul 30 2026):
  > "AI support bots get graded on deflection rate. So they learn the fastest way to look resolved is
  > to end the chat, not answer it. […] Measure answered, not deflected."
- @alex_prompter (279,203 followers, generalist not support specialist — **D** on domain authority,
  but the sharpest *actionable* pattern in the corpus),
  https://x.com/alex_prompter/status/2082019758350975051 (Jul 28 2026):
  > "**Pair resolution rate with customer renewal rate. If resolutions go up but renewals drop, the
  > agent is deflecting, not solving.** […] One metric alone is an invitation for your agent to game
  > it. Two metrics watching each other is how you keep the optimization real."
  A clean Goodhart countermeasure, directly usable in the pack's health-signals and support-taxonomy
  material regardless of who said it.

**The best first-party evidence in the channel says resolution rate is bottlenecked by KB quality,
not model quality.** @nikolak47 (Nick Velkovski, co-founder/CEO @heyreach_io, "$0 to $16M+ ARR in 3
years" — worker 1 grades him the strongest practitioner in the corpus), rebuilding support and going
from ~20-25% to 85% resolution, https://x.com/nikolak47/status/2077405086431772785 (Jul 15 2026): the
mechanism was "rewrote our whole knowledgebase, changed how Fin handles tickets, expanded what it
could resolve on its own, added 30+ knowledge base articles in just 2 months" — **not a model
upgrade**. This is the single most actionable finding for the pack's KB-requirements job.

**Contested — genuinely unresolved, both sides cite the same mechanism:** Fin frames $0.99
outcome-based pricing as incentive-*aligning*; @slaayeer_eth argues the identical mechanism is
incentive-*breaking* ("your SaaS bill explodes the better your automation works... You literally get
penalized for building a good product"), https://x.com/slaayeer_eth/status/2083889072473252268. The
pricing model itself is confirmed by two unrelated sources; the "bill explodes" consequence is the
critic's framing, not a documented complaint.

**Escalation policy** — the clearest checkable trigger found, though relayed not primary
(@undefinedKi, https://x.com/undefinedKi/status/2077356596103979442): *"Escalate instead of guessing.
Nothing relevant found? Hand the user to a human."* And the under-discussed failure mode, from a
vendor with a stake (@johniosifov, Ender Turing — **V**, but structurally interesting):
*"The AI works. The handoff breaks it… 1 in 3 human agents lacks the customer context needed… That's
not an AI problem. That's an escalation design problem."* Plus his "skill atrophy" hypothesis: when
agents only ever see hard cases, the repetition that built baseline competence disappears.

## 3. The CS canon runs on unexamined numbers — "$2M ARR per CSM"

The channel's cleanest worked example of folklore propagation, and both sides have permalinks.

**Debunked by the canon's own author, repeatedly, 2016–2017** — lincolnmurphy:
> "Please STOP perpetuating the $2M/ARR per CSM myth…" — https://x.com/lincolnmurphy/status/814160673840267264
> "Ugh. So #CustomerSuccess myths like $2M ARR per CSM are being perpetuated at #SaaStrAnnual…" — https://x.com/lincolnmurphy/status/829735323600957440
> "The '$2M ARR per CSM' nonsense is just what people want to hear. It's easy. Simple. Just happens to have little connection to actual reality" — https://x.com/lincolnmurphy/status/829780774215757824

**Still circulating years later on a bigger platform** — @saastr,
https://x.com/saastr/status/1132844104050724864 (2019) and
https://x.com/saastr/status/1213173372068212737 (2020); @lukesophinos,
https://x.com/lukesophinos/status/1466468241254060034 (2021) — "general SaaS ratios," zero citation.

A named authority debunked the figure *at the very conference* that kept publishing it. **Cite both
sides with both dates** — this is a better teaching example than any abstract warning about benchmarks.

**Bonus: a primary-source confession of the propagation mechanism itself.** lincolnmurphy,
https://x.com/lincolnmurphy/status/1046814748929609728 (Oct 1 2018):
> "They googled 'acceptable churn rate' and found a post of mine from years ago where I quoted a VC
> firm. If they had actually asked me, my response — and maybe their story — would be different.
> **This is how outdated concepts continue to propagate.**"
He names neither the number nor the VC firm even here. → channel D: find the original post.

## 4. The market event, and why it dates the pack

**Salesforce–Fin (fka Intercom), $3.6B cash, definitive agreement Jun 15 2026, closing EOY.**
Confirmed by both lead investors in their own accounts: @BessemerVP
https://x.com/BessemerVP/status/2066562901301948909 and @ICONIQCapital
https://x.com/ICONIQCapital/status/2066528974633902181. Deal thesis is a resolution number — "76% of"
inquiries (@ThomasSmale https://x.com/ThomasSmale/status/2066817754653708742; @tkc_0205
https://x.com/tkc_0205/status/2067009261247590676, which adds ~30,000 customers and channel coverage).

**Primary correction on the valuation story** — Eoghan McCabe (Intercom co-founder/CEO) replying to a
public account that anchored on a $1.3bn 2018 valuation,
https://x.com/eoghan/status/2075087239122743550 (Jul 9 2026): *"The company was worth ~$200M when I
took it back."* So the trajectory is **~$200M → $3.6B**, not $1.3bn → $3.6bn. **P** — cleanest primary
number in the channel. It explains why every helpdesk vendor's marketing now leads with a resolution
rate: the category's economics reward that number.

**Market structure, from a competitor with first-party data** — Marty Kausas, CEO of Pylon,
https://x.com/marty_kausas/status/2074905172610818391 (Jun 24 2026):
> "**we'd see Intercom in ~8.3% of deals, making them the second most common helpdesk product we'd
> see after Zendesk.**" … "**The $200M in revenue for the helpdesk is a drop in the bucket for
> Salesforce who makes $10B off their own product (Service Cloud).**" … "the standalone helpdesk will
> probably be deprecated over time."
**P** on the deal-share figure (a class of number nobody publishes), **D** on the predictions (he
hedges them himself), **V-inverse** on the Agentforce swipe. Note he argues *against* his own
short-term interest — he calls reduced competition bad for the industry.

**→ Pack implication:** the #2 helpdesk product is mid-acquisition with a credible deprecation
prediction. **Tool-naming in this pack needs an explicit freshness caveat** (cf. ai-skill's
anti-staleness invariant).

## 5. Churn, renewals, and the sales seam

- **The sales seam is contested by the canon's own author.** lincolnmurphy's position is
  *complexity-gated CS ownership*, not role-based: CSM renews by default; complex renewals go to a
  **dedicated CS-native resource**, explicitly *not* "Account Management carryover"
  (https://x.com/lincolnmurphy/status/1084526744290369537,
  https://x.com/lincolnmurphy/status/1084522527991480325, Jan 13 2019). This **cuts against** the
  charter's provisional "sales owns the expansion SALE" seam. → **controller adjudication needed.**
- **The handoff pain, stated well** — https://x.com/lincolnmurphy/status/2019458553430384815 (Feb 5 2026):
  > "Customers hate three things: 1. Surprises 2. Unknowns 3. Repeating themselves. Most Sales-to-CS
  > handoffs manage to hit all three."
- **Definitional clarity worth lifting** — jasonlk,
  https://x.com/jasonlk/status/1244999979401240577: *"A pause is better than a cancel. A downgrade is
  much better than a cancel. A downgrade is not logo churn. It is just a downgrade."*
- **A self-serve honesty datapoint** — jasonlk, https://x.com/jasonlk/status/2083503254743523480
  (Aug 1 2026): SMBs "self-serve, they close fast, they have one stakeholder. But the NRR is brutal at
  scale. It's hard to even cross 100% NRR from true SMBs." (He appears to be relaying another's
  framing — treat as amplified, not coined.)
- **No practitioner-reported churn rate with an explicit denominator surfaced at all.** Worker 3 flags
  this as supporting the charter's suspicion that quoted churn numbers lack denominators. → channel D
  for cohort/benchmark reports.

## 6. NPS

Primary critic quote, so the pack cites the source rather than growth's summary — hnshah,
https://x.com/hnshah/status/1094305710819573761 (Feb 9 2019):
> "High Net Promoter Score (NPS) does not correlate to high retention. NPS is just one of a few ways
> to understand customers NOT to understand retention. Folks are using NPS as 'one metric to rule them
> all.' That's not how to use it."

**No argued defense of NPS exists on X in this sweep.** The closest is a Ruby-gem author promoting his
library's NPS feature — worker 3 explicitly flags it as *not* a considered defense. That one-sidedness
is itself a finding: X skews NPS-skeptical, and defenses are implicit (vendors shipping the feature)
rather than argued. → the academic defense/critique (Keiningham replication) is channel D's.

**Do not cite lincolnmurphy's "NPS sucks" posts as a critique** — worker 3 checked: they are
content-marketing teasers for an email-gated "secret question," with no argument stated publicly.

## 7. Wedge hypothesis 1 — supported, from an unexpected direction

Worker 2's territory is only partially covered (below), but three independent findings bear on it:

1. **patio11 states the hypothesis himself, with no stake in our pack** — customer support is
   "generally poorly understood **outside of enterprises**, and on the cusp of industrial
   reorganizatio[n]" (https://x.com/patio11/status/2011881322541920620, Jan 15 2026).
2. **The canon's own numbers don't survive contact with its own author** (§3) — the enterprise CS
   playbook demonstrably runs on unexamined heuristics.
3. **But the honest solo answer may not be "support" at all — it may be pricing.** This is the
   channel's most useful challenge to the pack's scope, and it comes from two directions:
   - patio11, https://x.com/patio11/status/1261177745330987008: *"$50 is a much better minimum buy-in
     for most B2B services than $20 is. You'll make a lot more money, sure, but you'll enjoy the
     reduced support headaches and vastly lower churn even more."* One lever — priced in the `product`
     pack — moves revenue, support load, and churn together.
   - robwalling, https://x.com/robwalling/status/2055022092811133330 (May 14 2026): *"I wish someone
     would warn startup founders that lower prices usually (i.e. almost always) lead to higher
     churn."* And https://x.com/robwalling/status/2029970208215945697 (Mar 6 2026): *"founders with
     high MRR but 10%+ monthly churn convincing themselves they have PMF. They don't. […] You're
     basically pre-PMF regardless of revenue."*

   **Together these reframe churn as a pricing/value signal rather than a support-process failure** —
   which means an honest success pack must teach *when churn is not success's problem*. This is a
   scope-limiting finding and the pack is stronger for shipping it than for pretending better ticket
   triage fixes a pricing mistake.

4. **A practitioner-stated CONDITION for when success is first-class — the answer to the charter's
   §1033 problem.** arvidkahl, https://x.com/arvidkahl/status/1351985710325239821 (Jan 20 2021):
   > "Customer Success (compared to mere customer support) is so much more important **when your
   > revenue scales with your customers revenue.**"
   This is the most useful single sentence the channel found for the pack's hardest scoping decision.
   It converts "is success first-class for me?" from a vibe into a checkable test: *does your revenue
   scale with the customer's?* If yes, the CS motion earns its keep; if you are a flat-rate self-serve
   tool, the honest answer is lighter. **Recommend the pack adopt this as a named, attributed
   condition rather than inventing its own.**

5. **The solo × AI intersection is already real, not speculative.** arvidkahl (Podscan, solo),
   https://x.com/arvidkahl/status/2081147490170991086 (Jul 25 2026): "Glad my **first-level AI CS
   agent** took over…" — a solo founder running AI first-level support in production in 2026, exactly
   what wedge 1 × wedge 3 predicts. He also answers "how does one person cover a global base": Crisp
   live translation to handle Japanese customers
   (https://x.com/arvidkahl/status/1976293872926900665).

6. **A boundary the pack should claim explicitly**: patio11's OSS asymmetry — "Companies with $50
   million in the bank send an incredible volume of support requests to people who are worried about
   making their $600 rent" (https://x.com/patio11/status/1067515893335257088) — is the free-tier
   support question a solo builder actually faces. Unpriced support is a transfer from the maintainer
   to the well-capitalized user.

## 8. Contested questions (gold — hand these to the controller intact)

1. **Did Klarna's AI support fail?** Highest-engagement post in the corpus calls it CEO hype that was
   "totally fake" (@mrp, 217 likes / 59,983 views, https://x.com/mrp/status/2073456136238596342 —
   an All-In podcast clip; **the speaker is not identified in the tweet, do not attribute to Sacks**).
   Klarna's CEO says that reading is a misquote (https://x.com/klarnaseb/status/2019879525002473856)
   and that both AI efficiency (47% fewer employees than 2022, via attrition) and increased
   customer-service hiring are true at once (https://x.com/klarnaseb/status/2020988556374921683).
   **Same facts, opposite framings, both near-primary. Strong candidate for a worked "how to read a
   widely-repeated industry story" example** — the popular version resolves the ambiguity in whichever
   direction the teller already believed.
2. **Does a vendor "resolution rate" measure solving or closing?** Unanimous among non-vendors that it
   doesn't; no vendor discloses adjudication method. Unresolvable from X.
3. **Does cheap AI support shrink support budgets or grow support consumption?** Deflection framing
   assumes shrink; Decagon argues the opposite — "If AI makes great support cheap enough to offer
   every customer, companies will not just spend less on support. They will give people more of it"
   (https://x.com/vesting_tv/status/2083649605695135906). If true, deflection is the wrong *objective*,
   not merely a mismeasured metric.
4. **Is the durable layer of an AI support agent the model or the policy wrapper?** Decagon's
   president: "the model isn't the company's moat, **the guardrails wrapped around it are**"
   (https://x.com/PodWireHQ/status/2083335508541984841). **This is a competing vendor independently
   asserting the charter's success-owns-POLICY / ai-owns-mechanics seam.**
5. **Does automation re-humanize or de-humanize support?** Fin claims re-humanized; the skill-atrophy
   argument says the human team's competence floor silently erodes. Could both be true in different orgs.
6. **Who owns complex renewal — CS or sales?** §5. Cuts against the charter's provisional seam.
7. **Is the CSM role contracting because of AI?** Live and contested, and monetized by the loudest
   voice discussing it (lincolnmurphy sells the response to the anxiety he describes). No "AI changes
   nothing" counter-voice surfaced.

## 9. Falsification strip — additions from this channel

The charter's known strings (**5-25×**, **5%→25-95%**, **80/20**, **96% don't complain**, CSAT/CES
tables) did **not** surface on X in this sweep. Record as "not found on X in this pass," not "absent."
New **figure-CLASSES** this channel recommends adding (per the rule that a list is not a rule):

- **Any vendor resolution/deflection percentage without a stated adjudication method.** The concrete
  spread to point at: Fin at 40/64/67/71/73.1/75/**76**/80+/83%. The 76% is now the Salesforce deal
  thesis and *will* spread as a clean fact.
- **Unsourced staffing/coverage ratios** — "$2M ARR per CSM," "$5M ARR per Support Rep," "10:1
  employees to manager" (§3).
- **Secondary citations of analyst-firm numbers with no link** — worker 1 catalogued a single
  212-follower vendor account emitting "331-391% Forrester 3-year ROI," "$80B Gartner projection,"
  "97% adopted / 27% production" with no primary link anywhere.
- **Churn "acceptable rate" thresholds** — traced to a consultant quoting an unnamed VC firm (§3).
- Specific claims **checked and NOT verified**: "79% of organizations running AI voice agents plan to
  replace/upgrade by 2027" (searched, not found on the cited timeline); "Fin handles 2M+
  conversations" (not corroborated); "Hertz 10%→70% deflection in six weeks" (**correction**: this is
  a *Decagon customer claim inside promotional thread-bait*, not an independent Hertz statistic).

## 10. Cross-channel flags

- **→ D (web)**, highest value: get the **Complex Systems podcast episode, patio11 × destraynor,
  Jan 2026, "customer support as a complex system"** (https://x.com/patio11/status/2011881322541920620).
  Two of the best-credentialed people in the territory, mid-AI-transition. Best non-X artifact found.
- **→ D (web)**: Salesforce/Fin press release + any published "76%" methodology; the a16z Decagon
  episode for the guardrails-as-moat quote in full; the Feb-2025 press piece that produced Klarna's
  "~700 agents" figure; hnshah's linked NPS-retention source; lincolnmurphy's original
  "acceptable churn rate" post; **Greg Daines** (churn researcher) — unreachable on X; **Nick Mehta**
  (Gainsight CEO) — unreachable on X by two methods, try LinkedIn/blog.
- **→ C (github)**: verify the claimed **Anthropic public RAG support-agent reference architecture**
  and the "Sierra sells this at $16B" characterization. Lower priority: Decagon's "90% of our AI stack
  on open-source models" — corroborated on the Fin side by @ttunguz, so **two competing AI-support
  vendors moving off frontier models is a pattern worth one check**.
- **→ controller (seams)**: the renewal-ownership conflict (§5) and the success-owns-POLICY seam being
  independently asserted by a vendor (§8.4).

## 11. Method findings (for the next family build)

1. **Topical X search is unusable in this domain.** Four `--product Top` searches returned near-pure
   noise: "AI support agent deflection rate" → Rivet's SQLite engine, an MCP component library,
   Anthropic's petition post; "customer health score" → Shadcn payment animations; "Klarna AI customer
   service humans" → the X Chat API launch. **Cause**: "support," "agent," "health," "score" are
   high-frequency tokens in the AI-tooling discourse that dominates engagement — the same words mean
   something else in the bubble. **Only `from:<handle>` authority routing worked.** Worker 3
   reproduced this independently; `--product People` returned nothing usable.
2. **A context-saving projection that drops the citation key is a correctness hazard.** My ranking
   passes projected to `handle | likes | date | text`, which discards the tweet id. Writing up, I had
   verbatim quotes with no permalinks — and the available failure mode was to emit a plausible
   `x.com/<handle>/status/<id>` URL. **That is a fabrication**: snowflake ids can't be derived from a
   handle and a date, so a reconstructed permalink is a fake citation that looks verifiable and would
   survive review. I marked them `[TWEET ID NOT CAPTURED]` and re-ran with `--fields id,handle,date`
   to recover them by handle+date match. **Rule: always include `id` in any projection.**
3. **`xrelay search "from:<handle> a OR b"` SILENTLY IGNORES the `from:` filter.** A
   `from:Shpigford churn OR support OR cancel` query returned global results — Anthropic's petition
   post, Rivet's SQLite engine, crypto spam — with no error and no empty set. It looks like a
   successful search that simply found off-topic material, which is exactly how a researcher gets
   fooled. **The typed `--from <handle>` flag works correctly**; the same query as
   `search "churn" --from Shpigford` returned 20/20 genuine Shpigford tweets. **Use the flag, never
   the inline operator alongside an OR group.** This one nearly cost the channel its best finding.
4. **`archive user` fails on hyper-prolific accounts as a per-account cost, not channel throttle** —
   `jasonlk` (112,989 posts) timed out at 2/3/4-minute limits even at `--limit 150`, while a
   single-call `xrelay user jasonlk` returned instantly. Budget `from:<handle> <keyword>` search for
   such accounts.
5. **Handle corrections** (each cost a call): `des_traynor` → **`destraynor`**; `nickmehta` → NULL by
   two methods; `gregdaines`/`gdaines`/`ChurnRx` → dead shells.
6. **Read the bio — it can be the finding.** `destraynor`'s bio ("Co-founder of @fin_ai (fka
   @intercom)") is what surfaced the rename, which led to the acquisition, which led to §4.
7. **Verify a magnitude even from a named authority.** patio11's $20-vs-$30 tweet says "LTV of the
   former is easily 5X larger" while its own stated reason describes the *latter* cohort. The sentence
   is internally inconsistent. The raw file quotes it verbatim with the ambiguity flagged and tells
   the pack not to use the numbers as a benchmark — the qualitative claim is the safe part.

## 12. What we did NOT cover, and why

> **CORRECTION 2026-08-02 (after §13's authorized top-up): this section's coverage tail is
> superseded.** `tylertringas` is now COVERED; the top-up also corrected wedge 1's mechanism (the
> solo replacement for CS process is PRICING first and AI tier-1 support second — **not docs**, as
> §7 and the charter assumed). Still genuinely missing: `dvassallo`, `levelsio`, `csallen`, plus
> ticket-volume numbers, cancellation/pause/win-back tactics, and timezone-coverage craft — those
> survived two independent passes and are an honest null, not an untried gap. **Read §13 for the
> current state.**

- **Worker 2's territory (solo-founder support reality) is ~60% covered, after a lead top-up.** The
  worker got `robwalling` and stalled (archive timeouts, then idle). Rather than ship the territory at
  15%, I covered **`patio11`** (support economics — §7), **`Shpigford`** (the flagship anchor + the
  denominator-bearing churn number — §1) and **`arvidkahl`** (the §1033 condition + solo-AI support —
  §7) myself. Those were the three highest-value authors and they carry the territory's load-bearing
  findings. **Still missing: `tylertringas`, `dvassallo`, `levelsio`, `csallen`.** Concretely
  un-mined: first-person ticket-volume reports; cancellation-flow / pause-instead-of-cancel / win-back
  tactics practitioners say actually work; response-time and timezone-coverage craft for one person;
  vacations; docs-as-deflection first-hand accounts. **A short top-up run would close it cheaply** —
  the authors are vetted and listed in the raw file.
- **Sierra, Ada, Gorgias, Zendesk AI, Agentforce**: only touched via others' commentary. "Decagon"
  as a search term collides with a Nigerian personal account, a Japanese art book, and a murder-mystery
  novel — use `@DecagonAI`. Pylon was covered well (its CEO was the best market-structure source).
- **No GitHub or long web-article chains** — channel boundaries respected; flagged to C and D instead.
- **Video/podcast content is a real blind spot.** Two of the most promising leads (the Airshare
  health-score criteria, the Complex Systems episode) live inside audio/video this channel cannot read.

---

# §13 ADDENDUM — authorized top-up (solo territory close-out)

One sonnet worker, bounded to the unfinished solo-founder territory. Raws:
[`_raw/_raw-x-solo-support.md`](_raw/_raw-x-solo-support.md) (now 296 lines — the substantive
close-out) and [`_raw/_raw-x-solo-topup.md`](_raw/_raw-x-solo-topup.md) (23 lines — roster vetting
only). **`tylertringas` covered; `dvassallo` and `levelsio` were vetted but NOT mined.**

## ⚠ It corrected §7 of this report. Wedge 1 confirmed, MECHANISM WRONG.

The charter's H1 predicted the honest solo replacement for the CS canon is **"docs + automation +
product signals."** Across five deep-mined operators over two independent passes, that is **not what
the evidence shows**. The replacement is:

1. **PRICING first** — the most repeated, most specific theme in the whole territory. New primary
   evidence: arvidkahl, https://x.com/arvidkahl/status/2073028608054948002 (Jul 3 2026):
   > "Churn hits much less hard when you have raised prices in between. Podscan had a $50 plan at some
   > point; now, most users choose the $200 plan. I used to have to find 1 new customer to replace an
   > old one. **Now, a single new sub makes up for four.** Massive difference."
   Grade **P** (own numbers, no published method). This plus robwalling's price↔churn link and
   patio11's minimum-buy-in economics make pricing the load-bearing solo lever.
2. **AI tier-1 support second** — a 2024-26 addition the hypothesis doesn't name at all. tylertringas
   (now running a physical climbing gym on an in-house monolith), 2026-07-16,
   https://x.com/tylertringas/status/2077828747752005676: bugs and stability are "a bunch of agent
   loops monitoring performance and errors and automatically pushing fixes… a channel in slack where
   staff can report bugs or request features and agents just check it and create PRs automatically."
   His stack explicitly includes a "**shared support inbox**"
   (https://x.com/tylertringas/status/2074889104823664653). With arvidkahl's "first-level AI CS agent,"
   this is on-call collapsed into automation at a team of ~1-2.
3. **Docs-as-deflection returned almost nothing usable in either pass.** Honest null.

## The vocabulary gap is TOTAL ABSENCE, not disagreement — and that's stronger evidence

Across five operators and hundreds of posts, **not one** used "QBR," "CSM ratio," "health score," or
"Customer Success" as a job function. The canon and solo-founder discourse are two non-overlapping
worlds that never argue with each other. As the worker puts it: if solo builders were rejecting the
canon on the merits you would expect at least a few dunks; you get silence instead.

## But the canon is not rejected wholesale — OUTCOMES survive, PROCESS is discarded

Shpigford celebrates **Net Negative Churn** unreservedly as the "SaaS holy grail" — a bootstrapper
adopting a canon *metric* while never adopting the *organizational apparatus* the canon wraps around
it. **Sharpened claim for the pack**: the canon's PROCESS layer has no solo-scale substitute being
taught anywhere, while its METRICS layer is already understood and used without any of that
apparatus. Teach the outcome vocabulary; replace the process.

## Additions to the falsification strip

- **Shpigford, "3 things we did to reduce churn by 68%"** (blog teaser),
  https://x.com/Shpigford/status/698193606583173121 (Feb 12 2016) — a bare percentage with no method
  visible on X, same shape as the canon figures we flag. **Do not cite the 68% without reading the
  underlying post.** Notable that our own best-graded source emits an unmethodded figure — the
  figure-CLASS rule catches him too, and it should.
- **Named-string null**: none of the charter's known strings appeared anywhere in this roster. Under a
  narrow time-boxed roster this is **not** evidence the folklore is absent from X.

## One contested question is weaker than it looks — flag before anyone leans on it

"Is churn a pricing problem or a support-quality problem?" — robwalling and arvidkahl both land on
pricing, and **nobody in this territory argues the opposing side at all**. That is one-sided evidence
for a reframe, not a resolved two-sided contest. **Check C and D for a counter-claim before treating
"pricing beats support quality as a churn lever" as settled.**

## Still open after two passes

`dvassallo`, `levelsio`, `csallen` unmined. **Cancellation-flow / pause-instead-of-cancel / win-back
tactics, docs-as-deflection first-hand accounts, and onboarding-call execution were NOT found in
either pass** — the single biggest remaining gap against the charter's assigned themes, and it
survived two independent attempts. The pack's guidance there must lean on C's code evidence and D's
method verdicts, labeled as such, rather than on practitioner testimony that does not exist on X.

**Cheap follow-up vein if anyone wants it**: `xrelay search "Support Pro Tip" --from Shpigford` — the
numbering ("Support Pro Tip #937", https://x.com/Shpigford/status/783053318193119232) implies a long
personal series on triage and support craft, unexhausted here and likely the richest concrete
support-craft material in the territory.
