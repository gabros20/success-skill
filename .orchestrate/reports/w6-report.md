# W6 report — renewals, comms, high-touch, NRR

Writer: W6 · Date: 2026-08-02

## Files written

- `skills/success/references/renewals-and-expansion.md` (~1,579 words, ~2,132 tokens; budget
  1,800, under the 2,500 hard ceiling)
- `skills/success/references/incident-and-account-comms.md` (~826 words, ~1,116 tokens; budget
  1,200 — thin by design, under budget)
- `skills/success/references/surface-b2b-high-touch.md` (~1,759 words, ~2,375 tokens; budget
  1,800, under the 2,500 hard ceiling)
- `skills/success/assets/nrr_calc.py` (runnable; self-tests at import via a module-level
  `_self_test()` call, plus again implicitly on any CLI use; verified by executing all six
  functions through the CLI)

## Row coverage (R18)

- **renewals-and-expansion.md**: serves inventory §1 row 9. Covers ruling 2 (product models,
  success operates, sales closes — provisional), the four SEC-verbatim NRR mechanics (Snowflake
  2-year snapshot, Datadog/Klaviyo rolling-12-month, HubSpot monthly-cohort-annualized) with the
  "never compare across definitions" rule stated as the section's central claim, Dave Kellogg's
  "Lazy NRR is Not NRR" ARR-bridge distinction, NNR as the surviving canon outcome (Shpigford,
  jasonlk's downgrade≠churn/pause>cancel definitional note), renewal notice-period mechanics
  (30/60/90 days, flagged thin), expansion signals as vendor-folklore, the sales-seam contest
  (Murphy's complexity-gated position, cited not adjudicated), and advocacy (ruling 5 — success
  qualifies+consents, marketing produces; noted as success's own ruling since no shipped sibling
  draws this line yet, per E's open question).
- **incident-and-account-comms.md**: serves inventory §1 row 10. Co-ownership (ruling 7) stated
  plainly with both of operate's cession points cited (`incident-response.md:21` and `:159`,
  `decommissioning.md:186`); operate's fact/impact/timing line quoted verbatim; the
  handoff.md:79-vs-decommissioning.md:186 inconsistency flagged as operate's known/queued issue,
  not treated as evidence against success's claim; the customer-promise-vs-internal-SLO split
  drawn, pointing to support-process-design.md for the capacity mechanics rather than restating
  them.
- **surface-b2b-high-touch.md**: serves inventory §1 row 13. Epistemics-not-machinery framing;
  full-depth GitLab P.R.O.V.E. exhibit (weights, banding, five failure modes: CSM-sentiment
  override, missing-data-increases-subjectivity, the handbook's internal ignorance-convention
  disagreement, unbuilt VoC components, non-monotone support-ticket direction); five liftable
  epistemics (input expiry, segmented thresholds, persona-engagement/single-threading signal,
  tie-breaker taxonomy, severity-ladder escalation); CSM-ratio and QBR/EBR machinery declined with
  reasons, including the $2M-ARR-per-CSM propagation exhibit with both sides permalinked
  (lincolnmurphy debunking it in 2016–17, still circulating via @saastr in 2019–2020); the
  account-is-the-unit framing cross-referencing growth's surface-b2b-sales-assisted.md §6; the
  sales-seam contest restated for this surface plus the sales-to-CS handoff-pain quote.
- **nrr_calc.py**: implements all four SEC-verbatim mechanics as selectable modes
  (`snowflake_2yr_snapshot`, `rolling_12mo_point_in_time`/`rolling_12mo_weighted`,
  `monthly_cohort_annualized`) plus `grr`/`arr_bridge_nrr` (pypulate MIT reference implementation,
  cited with its repo path and license-audit pointer). Self-test anchors: Snowflake's reported
  126%, Datadog's reported "above 130%" (both illustrative — real cohort dollar figures aren't
  disclosed, flagged as such in the docstring), HubSpot's 110.3% under the standard compounding
  convention (flagged as an internal-consistency check, not independent verification of an
  undisclosed formula), and pypulate's own worked examples verbatim (NRR-arr-bridge(10000, 2000,
  500, 1000) = 105.0, GRR(10000, 500, 1000) = 85.0). Ran the module directly — self-test passes on
  import and all six CLI modes produce correct output.

## Rulings applied

R2 (renewal ownership stated with the sales clause explicitly provisional, contested by Murphy
cited-not-adjudicated), R5 (advocacy split stated as success's own ruling), R7 (co-ownership always,
operate's verbatim line, promise-vs-SLO split), R13 (bolded named concepts, no numbered invariants
— "never compare NRR across definitions" as the flagship rule of my asset), R14 (evidence grades
inline: MEASURED-WITH-METHOD for the four filings and pypulate, vendor-folklore for expansion
signals and CSM-ratio benchmarks not from the 17,034-CSM dataset, method-unknown for the
median-NRR-decline figure), R15 (never-ship self-check below), R16 ($2M/CSM shipped only as the
propagation exhibit with both permalinks, never standalone; the pricing plank is not mine and was
not touched), R17 (pypulate cited as LIFTABLE MIT reference implementation per the ledger), R18
(row coverage stated above per file), R19 (every sibling citation by pack + filename + line —
`operate/references/incident-response.md:21,159`, `operate/references/decommissioning.md:186`,
`operate/references/handoff.md:79`, `growth/references/surface-b2b-sales-assisted.md §6`,
`product/references/surface-app-saas.md`), R20 (all X permalinks copied verbatim from
`x-practitioners-report.md`/`_raw-x-cs-canon.md` — none reconstructed).

## Never-ship self-check

Grepped my three files for every never-ship string: no instance of the 5%→25-95% profit claim, the
5-25× retention-cost ratio, NPS-as-best-predictor stated as true, the flat 96% figure, 80/20,
deflection cost ratios, CES superiority, the "76%" Salesforce/Fin figure, unsourced SLA defaults, or
health-score accuracy percentages. The "$2M ARR per CSM" figure appears exactly where the rule
requires — as the propagation exhibit in `surface-b2b-high-touch.md`, always paired with both
permalinked debunking/circulation sides, never standalone. No NRR/GRR figure is presented without
its definition stated, and no two definitions are compared against each other anywhere in either
file or the script.

## Open items / notes for the controller

1. Confirmed no duplication with W4's `health-and-risk-signals.md`: it cites GitLab's P.R.O.V.E.
   model, CSM Sentiment, and the escalation ladder at summary/single-line depth as part of the
   flagship epistemics argument; my file carries the full weights table, all five failure modes in
   full, and the complete lift/decline lists, per inventory row 13's explicit "full depth" split.
   Cross-references between the two files point the right direction (mine → theirs for the general
   argument; theirs → mine for depth, per their file's own citation).
2. Confirmed `support-process-design.md` already ships §4 "The response-time promise, and the
   never-ship SLA default" — my cross-reference in `incident-and-account-comms.md` resolves
   correctly and I did not restate its capacity mechanics.
3. All internal cross-references resolve to files present in `skills/success/references/`
   (health-and-risk-signals.md, support-process-design.md, surface-selfserve-solo.md — all shipped
   by other writers).
4. `surface-b2b-high-touch.md` and `renewals-and-expansion.md` sit ~18–33% over their row-specific
   budgets (2,132 and 2,375 tokens vs. 1,800 targets) but both remain under the 2,500 hard ceiling
   stated in inventory §1's header. The overage is concentrated in required verbatim permalinks,
   the SEC-mechanic distinctions, and the $2M/CSM both-sides exhibit — I trimmed connective prose
   twice but declined to cut further at the cost of a required citation or precision guard; flagging
   for the integrator in case tighter trimming is wanted at the family-wide pass.
