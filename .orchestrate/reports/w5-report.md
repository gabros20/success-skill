# W5 report — VoC, retention execution, mobile

Writer: W5 · Date: 2026-08-02

## Files written

- `skills/success/references/voice-of-customer.md` (~1,523 words, budget 2,000 tokens)
- `skills/success/references/retention-execution.md` (~1,635 words, budget 2,200 tokens)
- `skills/success/references/surface-mobile-subscription.md` (~829 words, budget 1,400 tokens; thin
  by design, well under ceiling)

## Row coverage (R18)

- **voice-of-customer.md**: serves inventory §1 row 7. Consumes design's NPS definition
  (`research.md:49`), product's metric-tree placement (`metrics.md:45-53`), and growth's
  never-standalone rule (`retention-and-resurrection.md:167`) by citation only. Adds: the
  Keiningham 2007 / Dixon-Freeman-Toman CES falsifications as never-ship items, the Formbricks
  Display/Response self-selection exhibit, aggregate VoC trend analysis (claimed explicitly as
  unclaimed), a cross-reference to support-process-design.md §2's tie-breaker rule applied to
  feedback-reason taxonomies, the corrected 96%-don't-complain range, and the discovery.md feedback
  loop.
- **retention-execution.md**: serves inventory §1 row 8 and completes the "third box" that
  `handoff.md` (W1) already named and pointed here. Draws the third box explicitly
  (standing=operate / experiment-bound=growth / validated-motion=success, citing
  `growth/handoff.md:66-67` and `retention-and-resurrection.md:168-169`). Covers: the churn-save
  diagnose→attempt→exit structure (churnkey/sdk, MIT), the uplift-vs-risk targeting consequence
  (cites health-and-risk-signals.md §4's Ascarza finding rather than re-deriving it), cancellation
  ethics (cites growth's monetization-and-pricing-experiments.md §5, ships none of it, adds the
  one-click-reachable operative test), the levelsio pause-subscription arc and the CONFOUNDED
  cancel-flow-rebuild number, the voluntary/involuntary split (cites
  `email-compliance-checklist.md:82`), and a pointer (not a restatement) to when-success-applies.md's
  CONTESTED pricing plank.
- **surface-mobile-subscription.md**: serves inventory §1 row 14. App-review responses as a support
  workflow (cites `app-store-optimization.md:18` exactly), why pause-instead-of-cancel only partially
  transfers to native IAP (platform owns the cancellation surface), store-constrained comms, and
  platform-run billing-retry/grace-period as a stricter version of product's dunning ownership.

## Rulings applied

R3 (VoC interpretation-only, three sources cited not restated), R4 (dunning=product, cited at
`email-compliance-checklist.md:82`, twice), R9 (retention-execution reserved name + third box drawn),
R13 (named concepts, no numbered invariants), R14 (evidence grades stated inline — P/practitioner,
never-ship, CONFOUNDED), R15 (never-ship strip self-check below), R16 (CONFOUNDED flag verbatim on
the levelsio cancel-flow number; pricing plank cited as CONTESTED, not restated), R17 (churnkey/sdk
license verified independently: LICENSE file MIT, API agrees — treated as liftable structure, same
standard as synthesis's ledger entries), R19 (all sibling citations by pack+filename+line, never bare
numbers), R20 (all X permalinks copied verbatim from `_raw-x-solo-topup.md`, including the two full
URLs in the pause arc and the CONFOUNDED cancel-flow tweet).

## Never-ship self-check

No instance of: the 5%→25-95% profit claim, the 5-25× retention-cost ratio, NPS-as-best-predictor
presented as true (only as a failed replication), the flat 96% figure (only the corrected range),
80/20, deflection cost ratios, CES superiority presented as true (only as falsified), the "76%"
Salesforce/Fin figure, "$2M ARR per CSM", vendor deflection/resolution rates, unsourced SLA defaults,
health-score accuracy figures, or Shpigford's 68% figure. Confirmed clean by grep against my three
files for each string.

## Open items / notes for the controller

1. **Source outside my explicit assignment, used deliberately.** While locating the Formbricks
   Display/Response schema (required by ruling 3, not pinned to a specific raw file in my brief), I
   found it in `_raw/_raw-gh-voc-onboarding-csops.md` §2.2 — a channel-C raw file not listed for any
   writer in inventory §3's partition table. The same file's §6 (churnkey/sdk, MIT-verified,
   cancel-flow taxonomy) was a strong, precisely-fitting exhibit for retention-execution's "third
   box" content, so I used it too. Flagging in case another writer independently sourced the same
   file for a different angle — no collision found in my grep of already-shipped files, but worth a
   controller check at integration.
2. Confirmed via grep that no other shipped reference file yet cites Keiningham, de Haan, van Doorn,
   Formbricks, levelsio's pause arc, or churnkey — no duplication with W1's when-success-applies.md
   (pricing plank) or W4's health-and-risk-signals.md (Ascarza/de Haan/van Doorn correlation table),
   which I cite rather than restate in both cases.
3. All internal cross-references resolve to files that exist in `skills/success/references/`
   (health-and-risk-signals.md, when-success-applies.md, support-process-design.md — all present from
   other writers' completed work).
