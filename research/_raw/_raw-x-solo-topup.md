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

(dvassallo and levelsio sections below, appended as gathered.)
