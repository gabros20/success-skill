# Fixer 1 report — spec-review findings applied

All findings from `.orchestrate/reports/spec-review.md` applied and verified against named raw/source files before editing. Assets re-run after every touch.

## BLOCKERS

**B1 — tylertringas permalink mismatch.** Verified against `research/_raw/_raw-x-solo-support.md:166-177`: the "shared support inbox" phrase is in tweet `2074889104823664653` (Jul 8 2026); the agent-loop description ("monitors performance/errors, auto-pushes fixes, reports back in Slack") is in the *separate* tweet `2077828747752005676` (Jul 16 2026). "Auto-triages" is in neither.
- `references/when-success-applies.md:87-88` — now cites both permalinks, one per claim; "auto-triages" dropped.
- `references/surface-selfserve-solo.md:33-37` — same split; the correct agent-loop permalink now attached to the agent-loop sentence.

**B2 — HubSpot NRR order reversed.** Verified against `research/_raw/_raw-web-canon-commercial.md:225`: filing text is "Net Revenue Retention 102.2% 103.9% 110.3%" **most-recent-first** (NRR *fell* over time, not rose).
- `references/renewals-and-expansion.md:66-67` — "(oldest to newest)" → "(most recent first)".
- `assets/nrr_calc.py:46` — "oldest first" → "most recent first". Re-ran self-tests (import) and all six CLI modes: all pass, HubSpot-convention anchor still reproduces 110.3%.

## S-MAJOR

**S1 — GitLab paraphrase dressed as quotation.** `research/_raw/_raw-gh-ai-support-kb.md:318-322` quotes only "When in doubt, create a knowledge article… it can always be promoted to documentation." The reactive/proactive sentences are the researcher's own summary. Un-blockquoted the paraphrase into prose, kept only the real quote blockquoted, in `references/education-and-knowledge-base.md:59-64`.

**S2 — VoC group miscounted.** Verified against `research/_raw/_raw-gh-gitlab-cs-handbook.md:172-181`: VoC group has 3 measures total (Support-CSAT Not started, NPS Surveys Not started, Support-Engagement 70%); Executive Sponsorship/Events/Certifications are the separate Engagement group. Fixed the "three of four" miscount to "two of three" in `references/surface-b2b-high-touch.md:76-78`, and the inherited "three-quarters unbuilt" DRIFT in `references/health-and-risk-signals.md:157` to "two of three."

**S3 — pypulate handle.** `0x416d6982` → `0x416d6972` in `assets/nrr_calc.py:55` (confirmed against `SOURCES.md:81` and `_raw-gh-churn-health.md:389,455`).

**S4 — R21 figure-survival rule applied to all three cases:**
- `references/health-and-risk-signals.md:41-42` (pulserevops 62%/58%) — kept, with explicit recognise-and-correct framing plus the permalink (`pulserevops.com/knowledge/q525`, confirmed in `_raw-web-falsification-churn-evidence.md:137,171`) and a line stating the digits are fabricated-citation bait, not a measurement.
- `references/renewals-and-expansion.md:108-110` (expansion folklore 80–85%/65%/20%) — digits dropped, mechanism (three folklore claim-shapes, none sourced) kept.
- `references/renewals-and-expansion.md:73,80` (bare 131%; ~105%→~101%) — 131% replaced with the two already-verified figures earlier in the same file (Snowflake 126%, Datadog "above 130%"); the median-NRR-decline sentence rewritten to keep the claim-shape without the disclaimed digits.

**S5 — self-contradicting "ship none of its content" sentence.** `references/retention-execution.md:95-99` reworded: cites growth's file for the doctrine, and frames the three reproduced data points explicitly as "the sanctioned recognise-and-correct strip," not this file's own evidence — no more self-contradiction.

## MINOR (11/11)

1. Quotation fidelity — fixed all three: tylertringas LIFO quote now verbatim (`support-process-design.md:117-119`), "across GitLab" restored (`:142-143`), "/ experience" restored (`surface-b2b-high-touch.md:100-101`).
2. `voice-of-customer.md:99-101` — 4% reattributed: top-2-box (r≈.184, ~3.4%) named as the feedback-metric ceiling; tenure's ~4% noted as non-feedback. Conclusion unchanged.
3. `voice-of-customer.md:124-126` — no longer "TARP's own breakdown"; now states the primary report was never located and the range is convergent secondary paraphrase.
4. `retention-execution.md:122-124` — "a photorealism model upgrade, a v2 launch" (two things) → "Interior AI v2, with photorealistic outputs" (one launch), per `_raw-x-solo-topup.md:237`.
5. `retention-execution.md:115-117` — "confirmation it shipped" → "an intent-to-build reply... not confirmation it actually shipped," quoting the actual future-tense text.
6. `health-and-risk-signals.md:81` (table) — "93 Dutch B2C firms" → "93 Dutch service firms across 18 industries" (verbatim from `_raw-web-lead-cfm-evidence.md:136-138`).
7. `health-and-risk-signals.md:82` (table) — un-spliced the van Doorn quote into its two actual sources (abstract sentence; separate discussion sentence), no longer joined by an ellipsis as one continuous quote.
8. `ai-support-policy.md:164-169` — "~700 agents" now flags the unreconciled 700-vs-3000 discrepancy from Siemiatkowski's own parallel post (`_raw-web-supportops-ai-agents.md:331-341`).
9. `ai-support-policy.md:146-147` — added Barres et al. 2025 (tau2-bench grading-update paper) alongside Yao et al. 2024 and SABER, per `_raw-gh-ai-support-kb.md:78-79` / `SOURCES.md:74`.
10. Permalink dating — added dates to every previously-undated permalink: `support-process-design.md` (levelsio Oct 24 2015, tylertringas Jul 27 2020, dvassallo Dec 17 2023) and `surface-b2b-high-touch.md` (lincolnmurphy Dec 28 2016 / Feb 9 2017 / Jan 13 2019 / Feb 5 2026, saastr May 27 2019 / Jan 3 2020) — all dates verified against `_raw-x-solo-topup.md` and `_raw-x-cs-canon.md`.
11. `nrr_calc.py` — `monthly_cohort_annualized` now raises a proper `argparse` usage error (`p.error(...)`, exit code 2) on an odd-length `--values` list instead of a bare `ValueError` traceback. Verified: `--mode monthly_cohort_annualized --values 1.02 1.03 1.04` now prints a usage message and errors cleanly.

## Also applied (F6 ruling, outside the numbered findings)
Widened the growth reserved-name citation from `growth/references/handoff.md:66-67` to `growth/references/handoff.md:43,66-67` in `references/retention-execution.md:53` and `references/handoff.md:81` (verified against `growth-skill/skills/growth/references/handoff.md:43,66` directly).

## Post-fix verification
- `python3 -c "import nrr_calc"` — self-tests pass (no assertion errors).
- All six `nrr_calc.py` CLI modes re-run — correct outputs, including HubSpot-convention anchor (110.3%).
- Odd-length `--values` for `monthly_cohort_annualized` now argparse-errors cleanly (exit 2).
- `churn_baseline_check.py` — import + CLI reproduce flagship §5 exactly (unaffected by this pass, re-run as a regression check).
- `sla_capacity_calc.py` — import + CLI reproduce OVERLOADED verdict exactly (unaffected, re-run as a regression check).
- Grepped for both wrong artifacts (`0x416d6982`, `auto-triages`, `oldest first`, `oldest to newest`) pack-wide — zero hits remaining.

Nothing declined. No new figures introduced.
