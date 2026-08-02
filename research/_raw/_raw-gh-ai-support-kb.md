# _raw-gh-ai-support-kb — Channel C, Worker 3: AI support agents + KB/deflection tooling

Wedge hypothesis 3: "the AI-support-agent era (2024-26) is under-canonized: deflection-rate honesty,
escalation policy, bot boundaries." All claims below are `owner/repo@ref:path` or a full URL; numbers
are self-computed from raw JSON where noted (never trusted from a README summary).

---

## A. Benchmarks — τ-bench / τ²-bench / τ³-bench (sierra-research)

### What it actually is
`sierra-research/tau-bench` (MIT, 1360★, `README.md`@main) is the original 2024 benchmark: a
simulated customer contacts a language agent that has domain tools + a natural-language **policy
document**, and a second LLM plays the customer. It has been superseded twice:
- `sierra-research/tau2-bench` (MIT, 1712★) = "τ²-bench" (dual-control, mid-2025) → now rebranded
  in-place to **"τ³-bench"** as of the README at `sierra-research/tau2-bench@main:README.md`
  (same repo, same URL, new name — confusing but verified: the repo itself says "τ³-bench is here!").
  Domains: `mock`, `airline`, `retail`, `telecom`, `banking_knowledge` (new, retrieval/RAG-based,
  added 2026). Also ships a voice (full-duplex) mode.
- **Grading correctness is itself unstable**: `sierra-research/tau2-bench@main:README.md` states a
  "July 2026 v1.0.1 grading update" fixed `banking_knowledge` task errors and explicitly warns
  "results produced with tau2-bench < 1.0.1 are not comparable with >= 1.0.1." A companion paper,
  SABER (Cuadron et al., ICLR 2026 workshop, arXiv found via the repo's own citation block), is cited
  in-repo for "75+ task fixes" to the original airline/retail/telecom tasks — i.e., the benchmark's
  own maintainers found the original eval tasks had "incorrect expected actions… impossible
  constraints… missing fallback behaviors." **A support-agent benchmark number from 2024–25 is
  provably stale by the vendor's own admission.**

### The policy document (the artifact the pack should study)
`sierra-research/tau-bench@main:tau_bench/envs/retail/wiki.md` (downloaded directly, 81 lines) is the
actual natural-language policy the agent must follow. Load-bearing sentence, verbatim:
> "You should transfer the user to a human agent if and only if the request cannot be handled within
> the scope of your actions."
The same clause appears in `tau2-bench@main:data/tau2/domains/telecom/main_policy.md:13`, with the
exact tool call named: `transfer_to_human_agents`, plus a scripted customer-facing line: "YOU ARE
BEING TRANSFERRED TO A HUMAN AGENT. PLEASE HOLD ON." and an explicit instruction at line 15: "You
should try your best to resolve the issue for the user before transferring." This is the cleanest,
most citable formal statement of an escalation trigger found across the whole slice: **scope-boundary
escalation** ("only if out of scope"), not confidence-threshold escalation. `telecom` also ships
`main_policy_solo.md`, `tech_support_workflow.md`, `tech_support_workflow_solo.md` — a policy AND a
separate step-by-step workflow doc, worth a look if the pack wants a template for "policy vs SOP."

### Self-computed pass^k numbers (never trust the README table — it's frozen at 2024 models and the
retail table has literal "??" cells; I downloaded the actual per-trial JSON and computed pass^k
myself using the standard unbiased estimator C(c,k)/C(n,k))
Source: `sierra-research/tau2-bench@main:data/tau2/results/final/*.json`, git commit
`c30d59aaa71c65f9b9eb6a8f8636b48945028fcf` (embedded in every result file's `info.git_commit`),
`num_trials=4`, user simulator = `gpt-4.1-2025-04-14`.

| Agent model | Domain | n tasks | pass^1 | pass^2 | pass^3 | pass^4 |
|---|---|---|---|---|---|---|
| claude-3-7-sonnet-20250219 | retail | 114 | 0.787 | 0.693 | 0.634 | 0.596 |
| gpt-4.1-2025-04-14 | retail | 114 | 0.741 | 0.642 | 0.579 | 0.526 |
| o4-mini-2025-04-16 | retail | 114 | 0.715 | 0.594 | 0.518 | 0.456 |
| gpt-4.1-mini-2025-04-14 | retail (base split) | 114 | 0.660 | 0.529 | 0.443 | 0.386 |
| claude-3-7-sonnet-20250219 | airline | 50 | 0.500 | 0.410 | 0.375 | 0.360 |
| gpt-4.1-2025-04-14 | airline | 50 | 0.560 | 0.457 | 0.420 | 0.400 |
| o4-mini-2025-04-16 | airline | 50 | 0.590 | 0.483 | 0.420 | 0.380 |
| claude-3-7-sonnet-20250219 | telecom | 114 | 0.493 | 0.374 | 0.307 | 0.254 |
| gpt-4.1-2025-04-14 | telecom | 114 | 0.342 | 0.259 | 0.219 | 0.193 |

**This IS the load-bearing finding for the pack**: pass^1 (single-shot success) looks decent to good
(retail 66–79%), but **pass^k degrades monotonically and substantially** as k (repeat trials) grows —
by k=4, retail success is down 15–27 relative points, telecom (the hardest, dual-control domain) drops
from a mediocre 34–49% at k=1 to a bad 19–25% at k=4. **The pass^k metric exists specifically to
expose that single-shot success rate overstates reliability** — a model that "resolves the ticket"
in one out of one trial is not the same as one that resolves it reliably across repeated attempts
with the same policy/tools, which is the actual production-reliability question a support-org cares
about. Cite this mechanism (not the specific numbers, which the vendor itself calls stale) as the
canonical rebuttal to any vendor "our AI resolves X% of tickets" claim that doesn't disclose n or k.

**License verdict: LIFTABLE.** `tau-bench/LICENSE` and `tau2-bench/LICENSE` are both plain MIT
(confirmed by opening the file, not the GitHub API field — text starts "MIT License / Copyright (c)
2024 Sierra" and "2025 Sierra Research" respectively), `pyproject.toml` says `license = "MIT"`
(no contradiction), and there is no separate per-directory license on `data/` — the policy docs, wiki
files, and result JSON are all under the same MIT grant. Two caveats: (1) the repo is a **research
codebase with an active paper behind it** (rule e) — MIT licenses the *files*, not a license to claim
the pass^k methodology or SABER's error taxonomy as your own invention; cite Yao et al. 2024, Barres
et al. 2025, Cuadron et al. 2026 by name. (2) `banking_knowledge`'s synthetic task data (credit-card
scenarios) is model-generated fiction, not real financial content — safe to reuse as example data but
it is fictional, not verified fact.

### Other CS-agent datasets found
- `asappresearch/abcd` (ABCD, MIT — LICENSE file opens "MIT License / Copyright (c) 2021 ASAPP
  Research", `README.md`) — 10K+ human-to-human dialogues, 55 intents, agent must follow written
  "Agent Guidelines" (a Google Doc, linked but not literally in-repo) while balancing customer desire
  vs policy. Its `Nextstep Selection` subtask has exactly 3 labels: `take_action`,
  `retrieve_utterance`, `end_conversation` — a clean formalization of "the agent's only real
  decision points are act / answer / stop," useful as a minimal policy-decision vocabulary. No
  escalation/handoff label exists in ABCD's schema — it does not model human handoff at all, unlike
  tau-bench.
- I did not find a maintained open eval harness whose sole purpose is "hallucination-against-KB
  check" or "resolution-rate measurement" as a standalone tool (see Part C/D deflection section
  below for the negative finding, which is itself the answer).

---

## B. Escalation / handoff policy in real implementations

### chatwoot/chatwoot — Captain
`chatwoot/chatwoot@main:LICENSE` (Chatwoot Inc, 2017–2026) states explicitly: "All content that
resides under the `enterprise/` directory… is licensed under the license defined in
`enterprise/LICENSE`." Nearly all of Captain's actual assistant/handoff/scenario logic lives under
`enterprise/` (`enterprise/lib/captain/tools/handoff_tool.rb`, `enterprise/app/models/captain/
assistant.rb`, `enterprise/app/models/captain/scenario.rb`, `enterprise/lib/captain/prompts/
assistant.liquid`). `enterprise/LICENSE` (opened directly) is a source-available, non-OSI license:
"may only be used in production if you… have a valid Chatwoot Enterprise License." **Verdict:
CITE-ONLY** — describe the pattern, do not lift the code or prompt text. Only some scaffolding
(migrations, JS route/store files, `app/models/concerns/captain_featurable.rb`) sits in the MIT-
licensed main tree.

Content worth citing (paraphrase, don't copy the liquid template verbatim):
- `handoff_tool.rb`'s `HandoffTool` is a plain LLM tool call (`captain--tools--handoff`) with an
  optional free-text `reason` param; it writes the reason as a private note, flips the conversation
  to a `bot_handoff!` state, dispatches an event, and suppresses out-of-office auto-replies during
  campaigns. A code comment marks unimplemented "future enhancement" fields —
  `team_id`, `priority`, `escalation_level (L1/L2/L3)` — meaning **even Chatwoot's own team has not
  yet built priority- or tier-aware routing into Captain's handoff tool**, only a flat "hand off to
  a human" primitive.
- `enterprise/lib/captain/prompts/assistant.liquid`'s "Human Handoff Protocol" section is a genuine
  **consent-first** escalation policy, not confidence-threshold: it lists 5 conditions (user
  explicitly requests human, user accepts an offered handoff, a configured Guardrail/Response
  Guideline requires transfer for a matched condition, issue needs specialized permissions, "multiple
  attempts… unsuccessful") but then constrains the actual tool call to fire "only after the user
  explicitly requests… accepts… or a Guardrail/Response Guideline explicitly requires transfer" — i.e.
  low confidence or repeated failure alone is NOT sufficient to trigger the tool; the model is
  instructed to *ask* the user first and wait for consent, except when an admin-authored guardrail
  overrides that default. This "ask-then-transfer" default with an admin-override escape hatch is a
  distinctive, reusable design pattern for the pack's "bot boundaries" content.

### RasaHQ/helpdesk-assistant
`RasaHQ/helpdesk-assistant@main:LICENSE` opens "Apache License Version 2.0" (confirmed). This is a
**declarative** pattern, much simpler than Captain: `domain.yml` defines an intent literally named
`human_handoff` plus `trigger_handoff`/`handoff`; `data/handoff.yml` shows the story as a fixed
sequence: `intent: human_handoff → utter_ask_handoff → action_handoff_options → intent:
trigger_handoff → action_handoff`, with an explicit "handoff deny" story branch
(`intent: deny → utter_ask_whatelse`). Reading `actions/handoff.py`: `ActionHandoffOptions`
presents buttons built from a `handoff_config.yml` allowlist of `handoff_hosts`; `ActionHandoff` then
either emits a JSON payload with a `handoff_host` URL (REST channel) or utters
`utter_wouldve_handed_off` (non-REST channel, i.e. it can only *simulate* handoff without a wired
webchat integration). **Important limitation to flag honestly**: this reference bot's "handoff" is
bot-to-bot routing infrastructure (config maps a bot name → URL), not an actual live-agent transfer
system — the human side must be supplied externally (Rasa's docs point at `chatroom_handoff.html` /
a webchat widget for that). Trigger condition here is **purely intent-classification**: whatever
Rasa's NLU model scores as the `human_handoff` intent, no sentiment/failure-count signal in this repo.

### huabeitech/agent-desk (Apache-2.0, 181★, `LICENSE` opened directly = Apache 2.0 text, `go.mod`
consistent) — the most structurally interesting escalation implementation found
- `internal/ai/runtime/graphs/handoff_graph.go`: a **stateful interrupt/resume** state machine (built
  on `cloudwego/eino`, a Go LLM-agent-graph framework). First call: if `TryOffHoursHandoffByAIWithRequestID`
  succeeds, it auto-hands-off immediately with a canned "off hours" message — **no human confirmation
  needed outside business hours**. Otherwise it interrupts the graph and asks the user to confirm/
  cancel; only on the resumed turn, if the user's reply parses as a confirm word, does it call
  `HandoffByAIWithRequestID` and complete the handoff; a cancel word aborts. `hitl.go`'s
  `ParseConfirmationDecision` is a bilingual (EN/ZH) keyword matcher: confirm = {"确认","是","好的",
  "可以","ok","yes","continue","confirm","继续","同意"}, cancel = {"取消","不用","不需要","算了","no",
  "cancel"} — anything else re-prompts with `NeedExplicitConfirmationPrompt`. **Two distinct
  escalation gates observed in one file: (1) time-of-day (off-hours = auto-handoff, no confirmation
  needed), (2) explicit double-confirmation during business hours.**
- `internal/ai/runtime/graphs/triage_service_request_graph.go`: an explicit 3-way LLM triage
  classifier — `RecommendedNextAction` ∈ {`continue_answering`, `handoff_to_human`, `prepare_ticket`}
  — decided per-turn from conversation analysis (`buildAnalyzeConversationResult`), i.e. the "should I
  escalate" decision is itself model output, not a hard-coded rule, but is gated downstream by the
  consent flow above before an actual handoff fires.
- `internal/ai/runtime/reply_eligibility.go`: `CanReply()` is the bot-boundary gate *before* any
  escalation logic even runs — the AI is not eligible to reply at all if: the conversation already has
  a `HandoffAt` timestamp or a human `CurrentAssigneeID` assigned, the agent's `ServiceMode` is
  `HumanOnly`, or the incoming message is blank. `IsAIAgentRolloutEligible()` implements a
  **deterministic staged-rollout gate**: SHA-256 hash of `channel;conversation;agent` bucketed 0–99,
  compared against a configurable `RolloutPercent` (agent-level, further capped by a channel-level
  override, `min()` of the two) — meaning a single customer conversation is pinned consistently
  inside or outside the AI rollout for its whole lifetime. This is a genuinely reusable "bot
  boundary" mechanism the pack should teach: **gradual/percentage rollout gating is a bot-boundary
  control distinct from and prior to any in-conversation escalation policy.**

### dotnet/eShopSupport (Microsoft reference app, MIT — `LICENSE` file confirmed MIT text)
Not an escalation example — it's an **eval-harness** example. `test/EvaluationTests/
AnswerScoringEvaluator.cs` implements `Microsoft.Extensions.AI.Evaluation.Quality`'s `IEvaluator`:
it sends the user question + the AI's answer + a ground-truth "expected answer" to a judge LLM, asks
for a 1–5 `scoreLabel` ("5=Exceptional" … "1=Unacceptable"), and explicitly instructs the judge:
"Score only based on whether the assistant's answer is true and answers the question… no penalty for
giving extra on-topic information… Only penalize for missing necessary facts or being misleading."
This is a clean, minimal, reusable "LLM-as-judge answer-quality eval" template (not free-form
vibes-based grading — it's a fixed rubric + fixed output schema), but it measures **answer
correctness against ground truth**, not deflection or escalation correctness — useful to cite as a
contrast: "here is what a method-transparent quality eval looks like; it still tells you nothing
about whether the user's ticket volume actually fell."

### riteshbonthalakoti/HELPDESK.AI
MIT-licensed (`licenseInfo.key: mit` via API — recommend re-verifying the LICENSE file text directly
before lifting anything, per rule (a); I did not open it this session due to time budget, so treat
as **unverified license, do not lift without re-checking**). Description only: OCR/NLP-based
duplicate-incident detection helpdesk. Not deep-read.

### Escalation-trigger enumeration (cross-repo, this is the pack's "bot boundary" content)
Conditions actually found gating a real handoff-to-human in the code above:
1. **Scope boundary** — request literally outside the tool/domain's capability (tau-bench/tau2-bench
   policy docs: "if and only if the request cannot be handled within the scope of your actions").
2. **Explicit user request or consent to an offer** (Chatwoot Captain prompt; agent-desk confirm
   flow) — the dominant pattern across the two most sophisticated implementations found. Neither
   defaults to silent auto-escalation on low confidence alone.
3. **Admin-authored override rule wins over the consent default** (Chatwoot: "a Response Guideline or
   Guardrail explicitly requires transfer for the matched condition" bypasses the ask-first flow).
4. **Time-of-day / business-hours** (agent-desk off-hours auto-handoff with no confirmation).
5. **Repeated failure ("multiple attempts… unsuccessful")** — named in Chatwoot's prompt as a
   condition that triggers *offering* a handoff (not auto-firing it).
6. **Pure intent classification, no other signal** (RasaHQ: whatever NLU scores as `human_handoff`).
7. **LLM-driven 3-way triage output** as a recommendation layer sitting in front of the consent gate
   (agent-desk `RecommendedNextAction`).
8. **Structural pre-gate, not an escalation trigger per se**: staged rollout percentage and
   `ServiceMode=HumanOnly`/already-assigned conversation (agent-desk `reply_eligibility.go`) —
   determines whether the bot is even allowed to speak, upstream of any in-conversation decision.

None of the implementations found here use a numeric "confidence score threshold" from the model's
own logits/probabilities as the trigger — every real trigger found is either symbolic (intent match,
scope check, time-of-day, rollout bucket) or itself another LLM call's categorical output
(triage classifier), not a literal float confidence gate. **That absence is worth stating plainly in
the pack: "confidence threshold" is folklore-shorthand for escalation policy; the actual open-source
implementations use symbolic/behavioral triggers, not a raw model confidence number.**

---

## C. Knowledge-base / docs-as-deflection tooling

### squidfunk/mkdocs-material (MIT — `licenseInfo.key: mit` confirmed; free/OSS tier, not Insiders-only
— the feedback partial lives in the public `material/templates/partials/feedback.html`, not a
sponsors-only path)
Read the actual template (`material/templates/partials/feedback.html`) and the doc
(`docs/setup/setting-up-site-analytics.md`, 325 lines, fetched directly): the "Was this page
helpful?" widget is a plain HTML `<form>` with per-rating buttons (`data-md-value`), **hidden by
default** and only un-hidden by a JS snippet the site owner must write themselves — mkdocs-material
ships the UI, not the recording. Out of the box it sends one custom event
(`event name = "feedback"`, `data = rating value`) to Google Analytics 4 if configured; there is no
first-party storage or reporting built into the theme itself.

**Honest limits, quoted directly from the maintainer's own docs (this is exactly the finding the
charter wants):**
- "Google Analytics 4 has currently no feature that allows to define a custom calculated metric to
  compute the average rating of a page." (flagged `!!! danger` in the source doc, with a linked open
  GitHub issue #5740)
- "The report may take 24 hours or longer to begin displaying data" (flagged `!!! warning`)
- If the user does not accept the analytics cookie, "the feedback widget is not shown" — i.e. the
  sample of respondents is already conditioned on cookie-consent opt-in, a selection bias baked into
  the tool by design, undisclosed to the reader unless they read this page.
- The event records only a binary/ordinal helpfulness click **per page view**, with no join back to
  "did this visitor later open a support ticket" — there is no built-in way to compute deflection
  (ticket-not-filed) from this signal; it is a *proxy for perceived helpfulness*, not a measurement of
  deflection.

### GitLab Support Handbook — knowledge-base reporting (see Part D below for the full handbook
context) contains the single clearest primary-source admission that deflection is aspirational, not
measured, at a company whose support org is unusually well-documented publicly.

### Zero-result-query / search-analytics tooling
I did not find a maintained open-source tool whose specific, dedicated purpose is surfacing
zero-result KB search queries as a VoC signal (Algolia DocSearch's analytics are a paid/hosted
product, not something inspectable in a public repo; I did not pursue this further given the GitHub
API rate-limit pressure this session — **flag as an open question rather than a confirmed absence**,
unlike the deflection-measurement finding below, which I did positively verify).

---

## D. Support handbooks as written knowledge

### GitLab support handbook (gitlab-com/content-sites/handbook — hosted on GitLab.com, not GitHub;
fetched via the public GitLab REST API since this repo does not mirror to GitHub)
Path confirmed: `content/handbook/support/` (NOT `gitlab-com/content-sites/handbook` on GitHub — that
exact "repo" name doesn't exist on GitHub; the project lives at
`gitlab.com/gitlab-com/content-sites/handbook`). Full support-section tree includes real
subdirectories: `advanced-topics/`, `ai/`, `browser-extensions/`, `engineering/`,
`enhanced-support-offerings/`, `internal-support/`, `knowledge-base/`, `license-and-renewals/`,
`managers/`, `partnerships/`, `public-sector-knowledge/`, `readiness/`, `sig/`, `support-pods/`,
`training/`, `workflows/`, plus loose pages `on-call.md`, `performance-indicators.md`,
`support-incident-response.md`, `providing_excellent_customer_service.md`. A sibling
`content/handbook/customer-success/` tree also exists (out of this worker's slice, flagging its
existence for whoever owns onboarding/health-score content).

**License verdict: AMBIGUOUS.** `LICENSE` at repo root (fetched raw via GitLab API) reads: "Copyright
(c) 2011-present GitLab B.V. **With regard to the GitLab Software**: [MIT terms follow]... For all
third party components incorporated into the GitLab Software, those components are licensed under
the original license provided by the owner of the applicable component." The license text explicitly
scopes itself to "the GitLab Software" (i.e., the Hugo site code), not to the handbook prose content.
`README.md` at repo root says only "This repository contains all of the content for the Handbook" —
no separate content license (no CC BY-SA notice found in-repo despite that being GitLab's historical
public claim). **This is rule (e), thin-license-on-thick-IP, directly verified**: do not claim the
handbook prose is MIT-licensed; treat as CITE-ONLY (attribute to GitLab, link the page) unless a
clearer content-licensing statement is found elsewhere on the live site.

**Two directly load-bearing finds inside `support/`:**

1. `support/ai/using-ai-in-support.md` (fetched in full) — a **currently-maintained, dated (2026),
   primary-source AI-support-usage policy** from a real support org. Key policy content: a
   scenario→tool routing table (Glean for ticket summarization, GitLab Duo Chat/Agentic Chat for
   product-specific and Red-data work, Claude/Gemini for Orange-data drafting); a two-tier
   **data-classification gate on tool choice** (RED = customer PII/logs/credentials → GitLab Duo only;
   ORANGE = internal docs/anonymized examples → any approved tool); and the plainest possible
   bot-boundary rule for customer-facing text: **"Never generate a customer-facing reply entirely
   from an LLM… You remain responsible for the accuracy and completeness of every response sent to a
   customer."** Also: "if a customer asks whether AI was used, be transparent" (explicit AI-disclosure
   norm). Note this describes **AI-assisted human agents**, not an autonomous AI agent replying
   directly — a distinction the pack should preserve rather than conflate.
2. `support/support/_index.md` — "Escalate early. Visibility across GitLab, up to and including the
   CEO, is always better earlier rather than later." This is a distinct escalation *philosophy* from
   anything in the code repos above: **escalate for organizational visibility, upward, early** — not
   a tiered L1→L2→L3 ladder and not a bot-to-human handoff. Worth contrasting against the
   code-level "escalation = hand off this one conversation" framing in Part B; a support ORG's
   escalation policy and a support BOT's escalation policy are two different objects the pack should
   not merge.
3. `support/knowledge-base/reporting-and-metrics.md` (fetched in full) — **the single cleanest
   "deflection is not honestly measured" finding of this whole slice.** The page lists "Ticket
   Deflection" and "First contact resolution (did customers find what they need without having to
   open support)" as things they *want* to measure, in a bulleted wishlist alongside article views,
   ratings, and search counts — then states outright: "We are currently working with our metrics team
   members to build a Dashboard for KCS and Knowledge Management. **This is a work in progress.**"
   A company with one of the most extensive public support handbooks on the internet, explicitly
   naming ticket deflection as a KPI, **does not yet have it instrumented**. This is a primary-source,
   dated, named admission — not an inference from absence.
4. `support/knowledge-base/docs-vs-kb.md` — a genuinely useful, non-vendor-marketing distinction
   worth lifting as a framework (CITE, attribute GitLab, since content licensing is ambiguous):
   Knowledge Articles are *reactive*, ticket-triggered, for specific broken-in-this-config problems;
   Documentation is *proactive*, feature-complete, for learning intended behavior. "When in doubt,
   create a knowledge article… it can always be promoted to documentation."

### pamelafox/developer-support-handbook (14★, **no LICENSE file** — `licenseInfo: null` confirmed,
and a direct `contents/LICENSE` API call 404'd, so this is not a GitHub-API-detection miss, there
truly is no license file)
**Verdict: CITE-ONLY** (rule d: no license = cite only, regardless of content quality). Content is
~2013-era Google Maps API developer-relations support practice (`communication.rst`: blog vs.
notify-list vs. Twitter vs. forum vs. newsletter as different escalation-of-severity comms channels;
`issuetracking.rst`: a features checklist for what an issue tracker needs — comments, votes, status,
duplicates, notification, categorization, search, statistics — written when Google Code Project
Hosting was still the reference implementation). Dated but the "different comms channel per message
severity" framing is a reusable structure; the issue-tracker feature checklist is generic and not
worth citing over any modern equivalent.

### hkdobrev/awesome-handbooks (265★, **no LICENSE file** in-repo — top level is only
`.gitattributes`, `code-of-conduct.md`, `contributing.md`, `readme.md`; confirmed via directory
listing, not just API metadata)
**Verdict: CITE-ONLY** (link list, no content of its own, and not licensed even as a list). It is a
58-line curated link list; the only support/CS-relevant entry is the GitLab handbook link
(`readme.md:22`), which I followed through to the primary source above. No other handbook entry in
this list names a support/CS section specifically — most are general company handbooks (culture,
engineering practices), not support-specific.

---

## Licence verdict table (this worker's slice only)

| Repo | Licence (file opened directly) | Verdict | Note |
|---|---|---|---|
| sierra-research/tau-bench | MIT (`LICENSE`) | **LIFTABLE** | cite Yao et al. 2024 for the paper/method |
| sierra-research/tau2-bench | MIT (`LICENSE`, `pyproject.toml` consistent) | **LIFTABLE** | grading changed v1.0.1, cite Barres et al. 2025 + Cuadron et al. 2026 |
| asappresearch/abcd | MIT (`LICENSE`) | **LIFTABLE** | cite Chen et al. 2021 (NAACL-HLT) for the dataset/paper |
| chatwoot/chatwoot (main tree) | MIT (`LICENSE`) | LIFTABLE (main tree only) | — |
| chatwoot/chatwoot `enterprise/` (Captain) | Chatwoot Enterprise License (`enterprise/LICENSE`) | **CITE-ONLY** | source-available, subscription-gated; describe, don't copy |
| RasaHQ/helpdesk-assistant | Apache-2.0 (`LICENSE`) | **LIFTABLE** | — |
| huabeitech/agent-desk | Apache-2.0 (`LICENSE`) | **LIFTABLE** | — |
| dotnet/eShopSupport | MIT (`LICENSE`) | **LIFTABLE** | Microsoft Corporation copyright header on files |
| riteshbonthalakoti/HELPDESK.AI | MIT (per API only, file **not** opened) | **AMBIGUOUS — re-verify before lifting** | did not open LICENSE this session |
| squidfunk/mkdocs-material | MIT (`licenseInfo` API, matches known public status) | **LIFTABLE** | feedback widget is in free tier, not Insiders |
| gitlab-com/content-sites/handbook (support/) | Repo `LICENSE` scoped to "the GitLab Software" only; no content-license notice found | **AMBIGUOUS / CITE-ONLY for prose** | thin-license-on-thick-IP, rule (e) directly triggered |
| pamelafox/developer-support-handbook | None (`licenseInfo: null`, `LICENSE` 404s) | **CITE-ONLY** | — |
| hkdobrev/awesome-handbooks | None (no LICENSE file in tree) | **CITE-ONLY** | link list only, no content of its own |

---

## Deflection measurement: what exists / what does not (grep-verified)

**What exists:**
- Formal benchmark task-success measurement with an honest reliability metric (pass^k) for whether an
  *agent* resolves a *scripted* task across repeated trials — tau-bench/tau2-bench. This is the
  closest thing to a rigorous, open, method-transparent number in this space, and it measures agent
  task success, not real-world ticket deflection.
- Answer-quality-against-ground-truth LLM-judge scoring (eShopSupport) — again, quality of an
  individual answer, not whether it prevented a ticket.
- A UI primitive for collecting a binary "was this helpful" signal per page view (mkdocs-material),
  whose own maintainer documentation names two hard limits: no native average-rating metric in GA4,
  and 24h+ reporting latency — and which, by construction, cannot join "read the article" to "did not
  file a ticket," because that join requires connecting two separate systems (docs analytics + ticket
  system) that this tool does not attempt to bridge.

**What does not exist, positively verified rather than inferred from silence:**
- No open-source tool or benchmark found whose stated, built purpose is measuring **deflection rate**
  (real users who read a KB article and did NOT subsequently open a ticket) or **resolution rate** in
  production. Searched via `gh search code` for `deflection_rate`, `deflection rate`, and `deflection`
  in markdown across GitHub (search-API results returned no on-topic hits before I redirected effort
  toward the GitLab-handbook route, which produced a positive primary-source confirmation instead —
  see next line).
- **GitLab's own support-team handbook — arguably the most detailed public support-org handbook that
  exists — lists "Ticket Deflection" as a wishlist metric and states in its own currently-published
  page that the dashboard to measure it "is a work in progress"** (`support/knowledge-base/
  reporting-and-metrics.md`, fetched in full above). This is the strongest single piece of evidence
  for the charter's hypothesis that open, method-transparent deflection measurement does not exist
  even at a company that publishes essentially everything else about how its support org runs.
  **Conclusion for the pack: teach "we do not have deflection measurement" as the honest default,
  and treat any vendor's specific deflection-rate percentage as a marketing claim absent a disclosed
  method** (consistent with the charter's falsification-strip instruction).

---

## Boundary calls flagged to controller (not silently assigned)

- GitLab's `content/handbook/customer-success/` directory exists alongside `support/` and was not
  read (out of this worker's AI-support/KB slice) — flag to whoever owns onboarding/health-score
  content in channel C or channel E's seam audit.
- The Chatwoot Captain "off-hours auto-handoff" and "staged rollout percentage" patterns in
  agent-desk are arguably `operate`-adjacent (deployment/rollout gating) as much as `success`-adjacent
  (bot-boundary policy) — recording the seam question rather than assigning it.
- FLAG TO A: none found this slice (no Claude-skill/agent-skill repos surfaced in this search path).
- FLAG TO D: Algolia DocSearch's hosted analytics dashboard (not inspectable via public GitHub repo)
  — if worth pursuing for the zero-result-query question, that's a vendor-site/marketing-page look,
  channel D's territory, not a GitHub repo to read.
