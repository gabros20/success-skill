# _raw-x-solo-topup.md — Channel B (x-practitioners), top-up worker

Territory: closing the gap left by `_raw-x-solo-support.md` — `tylertringas`, `dvassallo`, `levelsio`
(one discretionary add allowed, not yet used). Topics: (1) cancellation/pause/win-back/refund tactics,
(2) first-person ticket-volume + first-hire numbers, (3) one-person coverage craft. Method: `xrelay user
<handle>` to vet, then `xrelay search "<terms>" --from <handle> --fields id,handle,date,text --limit N`
(typed `--from` flag only — inline `from:` + OR silently drops the filter, see charter gotcha). Grading
per charter rule 5: measured-with-method > practitioner-report > vendor-folklore. Status: IN PROGRESS,
appending per-author per charter rule 1 ("nothing lost").

---

## Roster vetted (all three alive, brief was accurate)

- **tylertringas** — 30,620 followers, verified, 31,139 tweets. Bio: "Calm companies" (Calm Fund /
  Earnest Capital lineage), rock climbing, writing. Built/ran Storemapper (bootstrapped SaaS, solo for
  years before selling), then Calm Fund (investor in bootstrapped/calm companies).
- **dvassallo** — 203,338 followers, verified, 54,858 tweets. Sells own info-products/courses
  ("small bets" ethos); ran Nomad List-adjacent and various small SaaS/tools solo.
- **levelsio** (Pieter Levels) — 926,268 followers, verified, 177,733 tweets. Runs Photo AI ($89K/mo),
  Interior AI ($44K/mo), RemoteOK ($27K/mo), Nomad List, and others — solo/tiny-team, extremely public
  about revenue and operations, including refunds.

## METHOD GOTCHA #3 (new, beyond the two briefed) — OR queries silently drop `--from` too

The charter's gotcha says the *inline* `from:handle a OR b` operator silently drops the filter but the
typed `--from` flag is "verified working." **That is only true for single-term queries.** Reproduced
repeatedly against `tylertringas`: `xrelay search "cancel OR refund OR churn" --from tylertringas`
returns pure noise (random global tweets from `robj3d3`, `signulll`, `BrendanKeefe`, `Polymarket`, etc.
— zero `tylertringas` hits) even though the returned `query` field shows `"...OR... from:tylertringas"`
correctly appended. A same-session single-term query (`"churn" --from tylertringas`, `"support" --from
tylertringas`) reliably returns ONLY that author's tweets. **Rule for this run: never combine an OR
group with `--from`; issue one single-term query per keyword instead.** This costs more calls but is
the only reliable pattern found.

---

## 1. Cancellation / pause / win-back / refund tactics

### tylertringas
Queries run (each single-term, `--from tylertringas`): `cancel`, `refund`, `pause`, `churn`. No
`win back` query run standalone (OR-only phrase, skipped per gotcha above — could revisit as a lone
term `winback` if resumed).

- **A real refund-offer outcome, with a number.**
  https://x.com/tylertringas/status/1245075278545793025 (Mar 31 2020):
  > "Amazed. We postponed the @FounderSummit. Over the weekend we offered ticketholders a 70% refund if
  > they wanted (roughly the % of costs we could recover or convert to credit for when we reschedule).
  > Zero requests ☺️🙏"
  Grade: **P**. Not SaaS-subscription churn, but a first-person "we offered X, and Y customers took it"
  data point (0 of N ticketholders asked for the refund) — a rare case where a refund/credit offer's
  actual uptake is stated, not just the offer.
- **Refund philosophy, no method.**
  https://x.com/tylertringas/status/1298613400436649985 (Aug 26 2020): "Willingness to say 'worst case
  is we refund everyone's money' is a superpower." Grade: **P** (aphorism, no outcome data attached).
- **Cancellation dark-patterns, viewed as a customer, not a vendor.**
  https://x.com/tylertringas/status/1387841567877210119 (Apr 29 2021): "Productized service idea: make
  it super easy take legal action and get a full refund + damages from subscription companies that bill
  you for a product you don't use and make it impossible to cancel. I'll be customer #1." Grade: **P**
  (anti-pattern awareness, not a tactic he ran).
- **No pause-instead-of-cancel or win-back content found** for tylertringas across `cancel`/`refund`/
  `pause`/`churn` searches — his cancellation-adjacent material is all refund-policy/dark-pattern
  commentary, not a subscription-pause mechanic. Honest null.

## 2. First-person ticket-volume / first-hire numbers

### tylertringas
Queries run: `tickets`, `emails` (single-term, `--from tylertringas`). **No ticket-volume, hours/day, or
first-hire-at-what-revenue number found.** His "tickets" hits are almost entirely FounderSummit
conference-ticket sales, not support tickets — a keyword-collision null, not just an absence. One
tangential observation (not first-person, about a *different* company's CEO):
https://x.com/tylertringas/status/1102381879091777537 (Mar 04 2019): "I love calm companies. But it's
important to recognize how amazing it is to see the CEO of a $10B co answering support tickets on
Twitter in a matter of minutes 👏👏" — praise for founder-led support at scale, not a number about
himself. Honest null on this topic for tylertringas.

## 3. One-person coverage craft

### tylertringas
- **⭐ The single best coverage-craft tactic found in this whole top-up.**
  https://x.com/tylertringas/status/1287791800443441152 (Jul 27 2020), verbatim:
  > "Solo founder hack: periodically switch to Last In, First Out (LIFO) customer support. Answer the
  > most recent tickets first, so at least some customers will get exceptionally fast support rather
  > than all of them getting the (probably not great) average response time."
  Grade: **P** (a named, reasoned tactic from a former solo SaaS operator — no outcome metric attached,
  but the mechanism and rationale are fully stated). This directly answers "what deliberately-imperfect
  coverage looks like for one person" — he is explicit that this *sacrifices* fairness/average response
  time to buy some customers an excellent experience, a genuinely non-obvious trade-off worth citing.
- **"Calm company" vacation-coverage test (portfolio-level, not first-person-solo).**
  https://x.com/tylertringas/status/1508562153145610240 (Mar 28 2022): "Is your company a calm company?
  Here's our latest test: Our Head of Finance is out on paternity leave. Our Head of Engineering is on a
  1-month vacation. And everything is going just fine 🧘‍♂️" Grade: **P** — this is Calm Fund's own
  ethos/test for whether a business is over-dependent on one person, adjacent to but not the same claim
  as solo-founder support coverage; flag as a philosophy statement, not a solo-support data point.
- **Micro-SaaS idea he floated, never built** (shows the gap he perceived, not a solution he ran):
  https://x.com/tylertringas/status/1018269470933049344 (Jul 14 2018): a "group calendar for remote
  teams" tracking timezones/vacation/"when I'll probably be online" — evidence the *problem* of
  async timezone-coverage visibility was on his mind, not a first-person coverage practice.
- No direct on-call, response-time-SLA, or "what I deliberately don't support" statement found for
  tylertringas. Honest null beyond the LIFO tactic above.

**tylertringas — CLOSED for this top-up.** Queries run across all three topics: `cancel`, `refund`,
`pause`, `churn`, `tickets`, `emails`, `vacation`, plus vetting `user` and a baseline `support` call.

---

### dvassallo
Queries run (single-term, `--from dvassallo`): `refund`, `cancel`, `churn`, `pause`, `support`,
`vacation`.

- **⭐ Best refund tactic found: "Refund everyone who asks, no questions asked."**
  https://x.com/dvassallo/status/1775552090955465127 (Apr 03 2024), verbatim, complete tweet:
  > "Refund everyone who asks. No questions asked."
  Grade: **P** (a stated policy/heuristic — no A/B outcome data attached to this exact tweet).
- **The "110% refund policy" idea** — https://x.com/dvassallo/status/1639694301801349121 (Mar 25 2023):
  > "What would happen if I offer a 110% refund policy? 'If you don't like what you get, you'll get all
  > your money back plus $20. No questions asked.'"
  Grade: **P**, but note it is phrased as a question/thought experiment ("What would happen if…"), NOT
  a report of having run it — do not cite as a tested tactic without a follow-up confirming he shipped
  it. Flagged as **unconfirmed** — a good candidate for a future worker to check his later timeline for
  a follow-up report of outcome.
- **Refund-request volume, first-person, unquantified**:
  https://x.com/dvassallo/status/1266749683772174336 (May 30 2020): "The less glamorous part of the
  info product business... Waking up to angry refund requests." Grade: **P** — confirms refund requests
  are a real, recurring operational cost for a solo info-product seller, no volume number given.
- **Piracy vs. honor-system refund** — https://x.com/dvassallo/status/1288963429567352832 (Jul 30 2020):
  "My info products already run under an honor system. Anyone can buy, download, and get a full refund
  within the same day (no questions asked)." Grade: **P**.
- **Cancellation-timing pattern, first-person product data (not a study, but his own observed
  distribution)** — https://x.com/dvassallo/status/1389487277961736196 (May 04 2021): "Almost all my
  cancellations seem to happen after the first renewal, or just before (not mostly right after). I
  think high churn is common for these products though since many are curious and not fully convinced
  before…" Grade: **P**. Useful shape-of-churn-curve claim for a $99/mo-tier community product.
- **A churn number WITH a rough denominator, for a $99/mo cohort** —
  https://x.com/dvassallo/status/1723064960282952175 (Nov 10 2023): "The churn rate in these $99/mo
  communities is often brutal. Average membership 2-3mo or so. Once a member churns, they think of you
  negatively." Grade: **P**. Second churn-with-magnitude data point in this top-up (compare Shpigford's
  ~15%/mo at $250 ARPU in the sibling file) — both are informal/first-person, not measured-with-method,
  but both give an actual unit (average tenure in months) instead of a bare adjective.
- **The structural alternative to "fix the cancel flow": don't sell subscriptions at all.** Repeated
  stance across years — https://x.com/dvassallo/status/1554004497948708865 (Aug 01 2022): "A
  non-recurring revenue business restarts from $0 every day... No churn. No commitments. No
  obligations. No expectations. It's actually liberating."; reinforced
  https://x.com/dvassallo/status/1609480795546333185 (Jan 01 2023) and
  https://x.com/dvassallo/status/1723074917921661410 (Nov 10 2023): "Nobody ever impulse buys a
  subscription... Nobody likes recurring fees on their bank statement." Grade: **P** (strong, repeated,
  named business-model choice). **Seam/contested-question flag**: this is dvassallo's answer to the
  whole cancellation/churn-reduction literature — skip the subscription model, so there is no
  cancellation flow to optimize. Worth citing as a legitimate alternative the pack should name
  explicitly, not just assume subscription-first.
- **Consumer-side cancellation dark-pattern complaints (NYT/WSJ), repeated 2019–2023**: e.g.
  https://x.com/dvassallo/status/1111008901581828096 (Mar 27 2019), 
  https://x.com/dvassallo/status/1725559280361943511 (Nov 17 2023): "I hate having to go through a
  questionnaire to cancel a subscription. Just let me go!" Grade: **P**, customer-side, not a tactic he
  ran on his own product — but a clear, repeated statement of what NOT to do, from someone who also
  sells subscriptions himself.

**No "pause instead of cancel" or "win-back campaign" content found** for dvassallo across `pause`/
`cancel`/`churn` — his position (see structural-alternative point above) is arguably a reason why: he
doesn't run recurring products in a way that needs a save-flow. Honest null on the specific
pause/win-back mechanic.

### dvassallo — ticket-volume and first-tool/first-hire numbers

- **⭐ The clearest "at what revenue did you get help" number in this whole top-up.**
  https://x.com/dvassallo/status/1736530664608989598 (Dec 17 2023), verbatim:
  > "I'm in a stage in this business where I need a helpscout account. Almost $1M in revenue and all
  > email support happened from my personal email account (until now)."
  Grade: **P**, first-person, with both a revenue magnitude (~$1M) AND the prior-state detail (personal
  email inbox, not even a shared support address) — this is exactly the "when did you professionalize
  support, and at what volume/revenue" data point the charter asked for. No hire is mentioned — the
  upgrade was tooling (Help Scout), not a person; note that distinction if cited.
- No hours/day or ticket-count-per-week figure found for dvassallo. Honest null on the volume metric
  specifically (revenue-threshold number found instead).

### dvassallo — one-person coverage craft

- **⭐ Two-month unsupervised absence, stated as a deliberate feature of the business design.**
  https://x.com/dvassallo/status/1534754556805976065 (Jun 09 2022), verbatim:
  > "Next week I leave for a 2 month vacation to visit family in Malta, and I don't need to ask anyone's
  > permission."
  Grade: **P**. Read together with his non-recurring/honor-system-refund business model above, this is
  the coverage-craft answer for dvassallo specifically: he designs the *business* (info products,
  one-time sales, self-serve refunds) so that a 2-month founder absence doesn't require anyone covering
  support — rather than solving coverage operationally (hiring, shifts, SLAs).
- Repeated "aspire for 300 vacation days/year", "180 days of vacation" lifestyle claims
  (https://x.com/dvassallo/status/1467046934724558848, Dec 04 2021;
  https://x.com/dvassallo/status/1761947827855663303, Feb 26 2024) reinforce the same pattern but are
  general lifestyle philosophy, not support-specific — cite with that caveat.
- No timezone-coverage, response-time-SLA, or explicit "what I don't support" statement found for
  dvassallo. Honest null beyond the vacation/business-design point above.

**dvassallo — CLOSED for this top-up.** Queries run: `refund`, `cancel`, `churn`, `pause`, `support`,
`vacation`.

---

## levelsio (Pieter Levels) — by far the richest source in this whole top-up

Queries run (single-term, `--from levelsio`): `refund`, `cancel`, `churn`, `pause`, `support emails`,
`vacation`, `solo founder`, `hours a day`; plus two `thread` reads to recover full text truncated in
compact projection (per the id-capture rule — never guess a permalink, always re-fetch by id).

### 1. Cancellation / pause / win-back / refund — the multi-year "pause instead of cancel" arc

- **⭐ The pause-subscription idea, its naming debate, and its shipping — a full multi-year arc, all
  first-person, all with permalinks:**
  - The original idea: https://x.com/levelsio/status/679767525723369472 (Dec 23 2015): "Here's a crazy
    idea: automatically pause recurring subscription of users when you detect they aren't actually
    using your app/service."
  - Elaborated same day: https://x.com/levelsio/status/679787749554151424 (Dec 23 2015): "it depends,
    but if someone doesn't read/use something for a month or more you could pause subscription or
    payment."
  - A UX-copy/naming judgment call, same day: https://x.com/levelsio/status/679792473091227648
    (Dec 23 2015): "I'd say Pause, but Unsubscribe is clearer." — he explicitly reasoned about which
    word is clearer to the customer, not just which is kinder to MRR.
  - Confirmation it got built, 2 years later: https://x.com/levelsio/status/933308392021442561
    (Nov 22 2017), reply to a user: "omg i love you :D i'll add a PAUSE button to subscription soon!"
  Grade: **P** throughout (a shipped feature + reasoning, no before/after churn-impact number tied
  specifically to the pause button itself — do not over-claim an effect size that wasn't stated).
- **⭐ A custom cancel-flow rebuild, WITH a before/after churn number (confounded, flag clearly).**
  https://x.com/levelsio/status/1949861989322314094 (Jul 28 2025):
  > "Created my own cancel flow for Photo AI with Claude Code. Before I used Stripe's customer portal
  > for it, and it's good, but you can't do a lot of customization or make it beautiful, so I made my
  > own. Churn for Photo AI is down from 40% to an all time low now around 13-14%, but…" [reply chain
  > continues — capture only the root tweet's claim verbatim above]
  Grade: **P, and explicitly CONFOUNDED** — this is a causal-sounding claim (custom cancel flow →
  churn 40%→13-14%) but levelsio's own parallel churn tweets (below) attribute much of the same period's
  churn improvement to unrelated product-quality work (Hyper Realism model, Interior AI v2). **Do not
  cite this as "a custom cancel flow cut churn by two-thirds"** — cite it as "a practitioner rebuilt his
  cancel flow and separately reports a large churn drop over the same broad period, with multiple
  unlabeled contributing causes."
- **⭐ Churn-recovery-by-discount, explicitly named as one of two causes, with the founder's own
  hedge ("I guess").** Full text via `thread` (compact projection had truncated it):
  https://x.com/levelsio/status/1758514737539596477 (Feb 16 2024), verbatim:
  > "Churn finally dropping, now 19% but at this rate will be below 10% in 3 months. #1 reason is
  > Interior AI v2 launched and it outputs are way better than the first version. Photorealistic
  > interiors that people really like. #2 reason is better churn recovery, offering discounts to avoid
  > canceling. Img 2 is old v1, Img 3 is new v2. So TL;DR I guess improving product is best way to fix
  > churn."
  Grade: **P**, self-graded by the author as uncertain ("I guess") — this is a rare case of a
  practitioner attaching his own epistemic hedge to a churn-causality claim. **Directly usable as a
  worked example of how to state an unmeasured causal claim honestly** — cite the hedge, not just the
  headline.
- **A self-refund button, built in response to a specific customer complaint on Hacker News.**
  https://x.com/levelsio/status/1858555436447752211 (Nov 18 2024):
  > "Saw this thread on HN yesterday, about someone who signed up to Photo AI and didn't use it and
  > wanted a refund and couldn't get it and that's not good. So I've quickly built a [♻️ Self-refund]
  > page on Photo AI. It follows Midjourney's refund policy which seems quite sane for…"
  Grade: **P**. A concrete build-in-response-to-complaint episode with a named reference policy
  (Midjourney's).
- **A refund rate with a full numerator/denominator, plus dispute rate — the best-instrumented refund
  number in this top-up.** https://x.com/levelsio/status/1548335017339719684 (Jul 16 2022):
  > "[a project] is being shutdown by @Stripe again — 3.96% refund rate (59 refunds on 1,489 payments)
  > (which seems fine because I let users self-refund) — 0% dispute rate. Unsure what's happening 🤷‍♂️"
  Grade: **P**, but note the numerator/denominator make this closer to "measured" than most tweets in
  this corpus — still self-reported, no external audit. His own interpretation ("seems fine") is a
  practitioner's threshold judgment, not a benchmark — do not present 3.96% as a target refund rate.
- **A card-testing fraud/refund incident with a dollar figure.**
  https://x.com/levelsio/status/1665625055777398784 (Jun 05 2023): "Had to refund and cancel 240
  customers called Jake Smith from Philippines with $7,000 in card testing payments... Had to block 🇵🇭
  PH payments now sorry." Grade: **P** — an operational fraud-response episode, not a churn/retention
  tactic, but directly relevant to "refunds are in scope" and to support-load reality.
- **An automated dispute-response system (2026), the AI-support-era analog of a refund policy.**
  https://x.com/levelsio/status/2041132289065631988 (Apr 06 2026): "Made an auto-dispute response
  system for Interior AI... It syncs old disputes but also catches new disputes via Stripe webhook and
  then auto submits evidence to try win them, it even includes the interior designs they generated in
  the evidence PDF." Grade: **P**. Directly relevant to charter wedge 3 (AI-support-agent era, deflection
  policy) — here it's chargeback-defense automation specifically, an under-discussed corner of "success"
  automation.
- **The residual, unautomatable support problem, stated with self-aware frustration (2026).** Full text
  via `thread` (compact truncated it): https://x.com/levelsio/status/2035010864487555379 (Mar 20 2026),
  verbatim:
  > "I wonder how to fix the last part of customer support I still get and can't automate: Customer buys
  > 5,000 credits for $350. Then messages me: 'I signed up for $99/mo but it charged me $99 and then
  > $350.' Yes because you bought 5,000 credits for $350. % of people either just lie or they have
  > memory loss. Then they chargeback and I can't win ever anyway. I could make some thing to add a
  > refund if your credits aren't used yet though that might solve it? Annoying!!!!!"
  Grade: **P**. This is the single best "what AI/automation CANNOT yet resolve in support" quote found
  in the whole top-up — a billing-confusion-turned-chargeback pattern that survives heavy automation
  because it's a customer-memory/honesty problem, not a lookup problem. Strong candidate for the
  pack's AI-support-agent-policy section (charter wedge 3) as a worked "here is the edge of deflection."
- **Contested internal tension — levelsio also dismisses churn-worry outright.**
  https://x.com/levelsio/status/1664631132598464514 (Jun 02 2023): "Also: 120 million people turn 18 and
  start spending money every year and become potential customers. Stop worrying about churn." Grade:
  **P**, and worth flagging as in tension with his own extensive churn-tracking/-fixing tweets above —
  see contested-questions section below.
- **Cancellation dark-patterns condemned repeatedly (2023–2024), a convergent stance with dvassallo.**
  Canny: https://x.com/levelsio/status/1853108595627540666 (Nov 03 2024); The Economist:
  https://x.com/levelsio/status/1628340962136305664 (Feb 22 2023); New Relic:
  https://x.com/levelsio/status/1832101176097304605 (Sep 06 2024): "They're ALLEGEDLY forcefully trying
  to reduce churn to 0% by making you msg support to cancel. Private Equity = 😈🤑 evil bankers"; general
  trend callout: https://x.com/levelsio/status/1853203803513995718 (Nov 03 2024): "Make your app
  impossible to cancel to pump your MRR? ... Absolutely desperate." Grade: **P**. Both levelsio and
  dvassallo (see above) independently and repeatedly condemn cancel-friction dark patterns — this is a
  genuine cross-practitioner convergence the pack can cite as two independent named sources.

### 2. First-person ticket-volume / first-hire numbers

- **A comparative support-volume number by payment method.** https://x.com/levelsio/status/657777387866824704
  (Oct 24 2015): "Interesting result of accepting PayPal on my site: PayPal users need about 10x more
  support emails than credit card signups through Stripe." Grade: **P**, relative (10x) not absolute —
  still a genuine first-person operational metric with a comparison baseline, rare in this corpus.
- **The cancel-reason-to-priority-list workflow, a VoC mechanism with a cadence.**
  https://x.com/levelsio/status/1649317613414277120 (Apr 21 2023): "Most useful thing for me I added to
  [Photo AI] is an email I send when customers cancel their plan. I then auto feed those emails into
  GPT-4 to make a list of highest priorities to work on, here's the list for last 2 weeks: [list of
  cancel reasons, truncated in capture]." Grade: **P**. A concrete, repeatable VoC-to-roadmap pipeline
  a solo founder runs, biweekly cadence implied ("last 2 weeks").
  Related, earlier data point: https://x.com/levelsio/status/1670397099597520897 (Jun 18 2023): "cancel
  reasons improving, less feedback quality (that's good cause I improved it a lot) and more about fine
  details now" — confirms he tracks cancel-reason TEXT QUALITY over time as its own signal, not just
  volume.
- **No absolute "N tickets/week" or "N hours/day on support" figure found for levelsio** despite the
  PayPal-multiplier and cancel-reason-workflow findings above — those are the closest proxies. Honest
  null on the specific absolute-volume ask.
- **A stated reason he does NOT do sales/support calls — an opportunity-cost calculation with real
  numbers.** https://x.com/levelsio/status/1666385483935670273 (Jun 07 2023): "At $50k MRR hourly rate
  of solo founder is $284/h (22 days @ 8h). Preparing one call, then doing it, with high risk of
  rescheduling generally takes 3-5 hours. So that costs $852 to $1,420 to acquire one customer for a
  $99/mo plan. No logic in doing calls for most ppl." Grade: **P**. This directly answers "what does a
  solo founder deliberately not support" for a self-serve product — he explicitly costs out why he
  refuses synchronous calls, with real numbers attached.

### 3. One-person coverage craft

- The opportunity-cost-of-calls tweet above (1666385483935670273) is the strongest coverage-craft find
  for levelsio: a stated, numerically justified refusal of a support channel (live calls) for a
  self-serve product.
- Multiple **churn numbers across his product portfolio, same era, giving a natural cross-product
  comparison** (useful context, not a coverage-craft finding per se, kept here since it recurs with
  topic 1): Photo AI ~30%, Interior AI ~20%,
  https://x.com/levelsio/status/1788905506095972494 (May 10 2024): "Only 5% monthly churn" for a third,
  unnamed-in-capture project (shortlink `https://t.co/HDQWMHoORv` did not resolve to a product name in
  this capture — **do not assert which product this is**, flag for a follow-up `media`/link-resolve if
  ever needed) — "Whereas Interior AI is ~20% and Photo AI ~30%. It seems like a sticky product?"
- **No timezone-coverage, explicit response-time SLA, on-call, or vacation-coverage statement found**
  for levelsio in this pass (the one `vacation` hit was a generic observation about US vacation-day
  norms, not about his own coverage). Given he is famously public about his lifestyle/location
  (Portugal, extensive travel), this is a genuine gap worth a targeted follow-up query
  (`"time zone"`, `"async"`, `"reply time"` as single terms) if the channel resumes.

## Practitioner roster (this top-up's three, ready to fold into the channel-wide roster)

- **tylertringas** | 30,620 followers | Built Storemapper (solo SaaS) then Calm Fund (bootstrapped-SaaS
  investor); ran a real support inbox as a solo operator before becoming an investor. Best contribution:
  the LIFO-support tactic (coverage craft).
- **dvassallo** | 203,338 followers | Runs Small Bets (community, sold 50% to Gumroad for $3.6M in 2025
  per his own post), assorted info-products and small SaaS tools, solo. Best contribution: the ~$1M
  revenue-before-Help-Scout threshold, and the "no subscriptions → no cancel-flow problem" structural
  stance.
- **levelsio** | 926,268 followers | Runs Photo AI, Interior AI, RemoteOK, Nomad List, and others,
  solo/tiny-team, radically public about revenue and churn numbers. Best contribution: the whole
  pause-subscription arc (2015 idea → 2017 shipped), the honestly-hedged churn-causality tweet, and the
  "last part of support I can't automate" 2026 quote.

## Contested questions (charter rule 6 — record, do not silently resolve)

1. **Is cancellation friction ever legitimate retention tactic, or always a dark pattern?** levelsio and
   dvassallo BOTH, independently and repeatedly across years, condemn deliberately-hard-to-cancel
   design (Canny, The Economist, New Relic, NYT/WSJ) as adversarial/evil — yet the wider CS canon
   (win-back offers, retention-department routing) explicitly inserts a human touchpoint before
   cancellation completes. `signulll`'s tweet surfaced incidentally in a tylertringas search captures
   the ambiguity well: "you might get a straightforward cancellation or you might be routed to the
   retention department with a special offer you might have to refuse" — the same mechanism (an offer
   before cancel) can read as helpful (win-back) or hostile (friction), and the difference seems to be
   whether cancellation REMAINS one click away after the offer. Not resolved by this top-up; a genuine
   design-ethics line for the pack to draw explicitly rather than assume.
2. **Does churn matter for a solo/self-serve builder, or is it a distraction?** levelsio contains BOTH
   positions in his own timeline: extensive quantified churn-tracking-and-fixing (multiple tweets above)
   AND "Stop worrying about churn" (1664631132598464514) reasoning from a 120M-new-18-year-olds-per-year
   TAM argument. Likely reconciled by product stage/maturity (early ATAM-driven growth vs. mature
   optimization) but he never states that reconciliation himself — flag as unresolved in his own words.
3. **Subscription-first vs. non-recurring-first as the retention strategy.** dvassallo's structural
   stance (skip subscriptions entirely to avoid the whole churn/cancel problem) is a legitimate
   alternative the pack should name, in tension with the rest of the corpus (including levelsio) which
   assumes subscriptions and optimizes churn within them. This is a segment/business-model choice, not
   a universal answer — record as contested rather than picking a side.

## Folklore sightings (charter rule: figure-CLASS, not just known strings)

- No sighting of the specific "5-25× more to acquire than retain" or "5% retention → 25-95% profit"
  strings in this top-up's three authors.
- **A new unsourced-figure CLASS spotted incidentally** (off-topic account, surfaced in a tylertringas
  OR-query before the from-filter-bug was caught, but worth flagging since it's exactly the pattern the
  charter warns about): https://x.com/GeorgecomX/status/2081379129841037510 (Jul 26 2026): "Sundays have
  the highest churn, and moving billing off daytime hours has cut churn by a few percentage points for
  us." Not one of our three authors, not verified, no method — flagging per charter's instruction to
  flag the figure-CLASS (an unsourced "billing-timing cuts churn by X%" claim) even from an incidental,
  non-target source, since this exact genre of claim (operational-tweak → churn-%-point claim, no
  method, no n) is common and worth the pack's skepticism template.

## What could not be found (honest nulls, with queries run)

- **No first-person absolute ticket-volume number** ("N emails/tickets per week", "N hours/day on
  support") from any of the three authors. Closest proxies found: levelsio's PayPal-vs-Stripe 10x
  support-email multiplier, and dvassallo's ~$1M-revenue-before-Help-Scout threshold. Queries tried:
  `tickets`, `emails`, `support emails`, `hours a day` (levelsio); `tickets`, `emails`, `support`
  (dvassallo, tylertringas).
- **No explicit timezone-coverage or on-call statement** from any of the three. Queries tried:
  `vacation` (all three), `solo founder` (levelsio), `hours a day` (levelsio). tylertringas and
  dvassallo's vacation-related tweets are about business-design/lifestyle, not support coverage
  mechanics specifically.
- **No first-hire (a PERSON, not a tool) at-what-revenue number** from any of the three. dvassallo's
  Help Scout adoption at ~$1M revenue is a tooling upgrade, not a hire.
- **tylertringas has no pause/win-back/refund-outcome content** at all beyond general dark-pattern
  awareness and one FounderSummit refund-uptake data point (0 of N requests). Queries tried: `cancel`,
  `refund`, `pause`, `churn`.
- **No fourth author was added.** The three assigned authors were sufficiently productive (especially
  levelsio) that the "at most one better author" discretionary slot was not needed; if the channel wants
  more depth, `csallen` (Starter Story) was flagged as uncovered by the sibling worker file and remains
  open.

## Cross-channel flags

- → **D (web)**: levelsio's self-reported churn magnitudes (Photo AI ~30%→13-14%, Interior AI ~20%,
  a third unidentified product ~5%) and refund rate (3.96%, 59/1,489) are informal but denominator-
  bearing — worth checking against any published AI-SaaS churn benchmark D finds, same pattern as
  Shpigford's numbers flagged in the sibling `_raw-x-solo-support.md`.
- → **controller/lead**: the contested-question #1 above (cancellation friction: dark pattern vs.
  legitimate win-back) is a genuine adjudication point for the health-and-risk-signals /
  churn-prevention sections of the pack — recommend the lead surface it explicitly rather than pick a
  default.

**levelsio — CLOSED for this top-up. Channel B top-up territory (tylertringas, dvassallo, levelsio) —
CLOSED.**
