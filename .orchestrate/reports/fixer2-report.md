# Final-fixer report — success-skill

Date: 2026-08-02 · Base: `09db6dc` + quality-review.md · Fixer: fixer2 (final)

---

## 1. Q1 — evidence-null vs empirical-negative contradiction

**Finding:** `references/surface-selfserve-solo.md:30` and `:79` restated `when-success-applies.md`'s
honest null ("docs-as-deflection returned almost nothing usable") as "tested weak in practice" —
violating the pack's own flagship invariant ("say not published, never not measured") in a
different domain, and self-contradicting inside the `:79` table cell against
`education-and-knowledge-base.md:116`'s KB-rewrite-is-the-strongest-lever finding.

**Fix (two lines, `surface-selfserve-solo.md`, zero citation cost):**
- `:30` → "...not a documentation library, which this research found under-evidenced rather than
  effective (an honest null — see [when-success-applies] for the correction)."
- `:79` (job-reshape table) → "The evidence for docs-as-deflection is thin, but KB *correctness* is
  the one first-party lever measured — check KB coverage before a model upgrade."

`when-success-applies.md:100` left untouched, as instructed.

**Verification:** grep confirms "tested weak" no longer appears in either file; both lines now agree
with `when-success-applies.md` and `education-and-knowledge-base.md`.

## 2. Q2 — pointer promises a third claim its target does not ship

**Finding:** `references/retention-execution.md:145-147` claimed `when-success-applies.md` ships
"patio11's minimum-buy-in economics, robwalling's price-to-churn link, and the '10%+ monthly churn
is often a pre-PMF signal' position" — the third item is quoted, bare, unsourced, and appears
nowhere else in the pack; `when-success-applies.md` ships only the first two.

**Fix:** took the report's preferred zero-research option — dropped the third item from the
pointer. `retention-execution.md:145-147` now reads "...patio11's minimum-buy-in economics and
robwalling's price-to-churn link — with its own CONTESTED marking."

**Verification:** grep for `pre-PMF` across `skills/` now returns zero hits.

## 3. Eval suite — built from the report's exact fixture specs

| Suite | Count | Notes |
|---|---:|---|
| `activation/cases.json` | 26 | 14 router-row positives + 2 indirect-vocabulary positives + 7 boundary-arrow negatives + 2 adversarial sibling-naming negatives + 1 out-of-family negative — every prompt/id/should_trigger taken verbatim from the report's tables. (Report's own section header said "24 cases" but its five tables sum to 26; implemented all listed cases per the explicit table contents, which is the authoritative spec.) |
| `traversal/cases.json` | 10 | All `expected_references`/`forbidden_references` paths verified to exist on disk before writing; `gate-first` (route-rule-1 proof) included as specified. |
| `output/cases.json` | 6 | 5 artifact-contract cases + 1 `never-ship-strings` case whose assertions list is the forbidden-string table with file-scoped allowances stated in prose. |
| `compression-ablation/cases.json` | 3 | `ablate-observability`, `ablate-figure-grade`, `ablate-gate` — `preserve` includes `human comprehension` per §15.2 (the template's stub list was missing it). |

`evals/README.md` rewritten to describe the real suite (was: "replace every placeholder case").
No literal `TODO` or `__SKILL` string anywhere in any of the four fixture files (grep-verified).

### Never-ship enforcement added to `scripts/lint-skill`
Inserted after the runtime-scripts executability check (before the eval-schema block):
- `NEVER_SHIP` pattern table (11 patterns) with per-file allow-sets, swept across every `.md` file
  under `skills/`. Independently grep-verified zero unauthorized hits pack-wide.
- Precision-guard regression check: `"not published, never not measured"` (case/comma-tolerant
  regex) must appear in both `SKILL.md` and `references/health-and-risk-signals.md`.
- A guard-leak check: outside those two homes, a bare "not measured" is only legitimate inside the
  pack's separate "widely believed, not measured" TTFV/expansion-signal idiom (used consistently in
  `onboarding-and-adoption.md` and `renewals-and-expansion.md` for an unrelated claim); anything else
  fails. **Deviation from the report's literal text, noted:** the report's illustrative assertion
  string included a comma ("not published,\" never \"not measured") that doesn't match the pack's
  actual R16-protected phrasing (no comma, per `inventory.md` R13/R16, and as shipped in `SKILL.md`'s
  router row and `health-and-risk-signals.md`'s named-concept heading). I matched the check to the
  pack's real, binding phrasing instead of editing three correct files to fit an illustrative string.
  Verified case-insensitively present in both required homes with no content changes needed.
- Heuristic WARN (not FAIL): an hour/day figure sitting near "first/next-response" gets flagged for
  manual review against the capacity-framing rule. Zero hits currently.

Refactored the file-reading loop into a cached `file_texts` dict so the new checks don't re-read
every runtime file per pattern.

## 4. Token cuts

| File | Before | After | Cut |
|---|---:|---:|---:|
| `SKILL.md` | 3,658 | 3,544 | −114 (net, after the +8 app-store-review clause and Q1/Q2 wording) |
| `references/ai-support-policy.md` | 2,939 | 2,852 | −87 |

`SKILL.md` cuts: trimmed the "what makes this pack different" three-incumbent survey to one
sentence (kept the flagship + Observability Question routing signal); halved the "operate
independently" boilerplate to its two operative clauses; trimmed two "Not this skill"/Completion
explanatory halves for the final margin under marketing's shipped 3,548 precedent.

`ai-support-policy.md` cuts: reduced the third statement of the escalation-disambiguation rule to
the rule plus the pointer; trimmed the Purpose-block `ai` seam elaboration to the ownership sentence
plus file path (rationale already lives in Skip-when and `handoff.md`). The nine-item escalation
enumeration was **not touched**, per the report's explicit overturn of the earlier suggestion — it
is a routing fact (`SKILL.md:74`'s "nine real triggers, none numeric").

`retention-execution.md` (+3.2%) and `support-process-design.md` (+2.1%) left untouched — inside the
report's noise band, no trim applied.

## 5. Minors

1. **App-store-review reachability.** Report specified a job-row tweak; applied it — job row 4's ask
   column now reads "...or escalation vocabulary — including the app-store-review channel."
2. **`nrr_calc.py` arity fix.** Added the report's 6-line `ARITY` table/check for the four fixed-arity
   modes, plus an even-length check for `rolling_12mo_weighted` (it silently dropped a trailing odd
   value via `zip`). Probed all five paths: `snowflake_2yr_snapshot --values 126` → clean exit 2;
   `--values 126 100 55` → clean exit 2 (previously silently used the first two, ignored the third);
   `rolling_12mo_weighted --values 100 90 80` → clean exit 2; valid `grr` and `snowflake_2yr_snapshot`
   calls still compute correctly (85.00%, 84.75%).
3. **Abbreviations expanded at first use:** BTYD → "buy-till-you-die", RFM → "recency/frequency/
   monetary", IPCW → "inverse-probability-of-censoring weighting" (all in
   `health-and-risk-signals.md`), CEP → "customer engagement platform" (`handoff.md`).
4. **`voice-of-customer.md:108` cross-ref fix.** Now points directly at
   `growth/references/retention-and-resurrection.md:167` instead of "the experiment-level rule in
   §1" (§1 only paraphrases it).

## 6. CHANGELOG + version sync

Team-lead instruction specified a real `v0.1.0` entry, but `.codex-plugin/plugin.json` still carried
the template default `1.0.0` — unflagged by the quality review because it isn't literally `TODO`.
Checked five sibling packs' shipped `plugin.json` (quality 0.1.2, operate 0.1.1, data 0.1.0,
marketing 0.1.1): the family convention is `0.1.x` for a first release. Bumped
`.codex-plugin/plugin.json` version to `0.1.0` to match both the instruction and the convention, and
`scripts/lint-skill`'s hard requirement that plugin version match the CHANGELOG's latest release
heading. Wrote a real `## [0.1.0] — 2026-08-02` entry (content summary: faceted router 10 jobs × 4
surfaces, flagship, Existence Gate, AI-support policy layer, 4 self-testing assets, never-ship strip
enforcement, eval suites, research corpora). README untouched, as instructed (release-pass scope).

## 7. Verification — final state

```
$ python3 scripts/lint-skill
lint-skill: WARN: SKILL.md exceeds the 3,500-token review threshold (estimated 3544)
lint-skill: WARN: references/ai-support-policy.md exceeds the 2,500-token review threshold (estimated 2852)
lint-skill: WARN: references/health-and-risk-signals.md exceeds the 2,500-token review threshold (estimated 2860)
lint-skill: WARN: references/retention-execution.md exceeds the 2,500-token review threshold (estimated 2565)
lint-skill: WARN: references/support-process-design.md exceeds the 2,500-token review threshold (estimated 2553)
lint-skill: OK — success, 188 SKILL.md lines, ~3544 tokens, 15 direct reference(s)

$ bash scripts/check-sync
[... same 5 WARNs ...]
check-sync: OK — package, routes, references, metadata, eval fixtures, and scripts validated
```

**Zero FAILs.** All 5 WARNs are the token-ceiling adjudication from report §6 — `SKILL.md` now sits
under marketing's shipped 3,548 precedent; the four over-ceiling reference files are the report's
explicit "do not cut" list (Klarna's triple refutation, Air Canada's verbatim tribunal quote, the
nine-item escalation enumeration, and two files inside the noise band).

All three Python assets import cleanly and their CLIs run correctly, including the new arity-error
path (verified via direct execution, not via a synthetic importlib module name — the latter produces
an unrelated `dataclass`/`sys.modules` artifact that is not a bug in the shipped files).

Independent pack-wide never-ship grep (outside `lint-skill`'s own code): zero unauthorized hits
across all `.md` and `.py` files under `skills/success/`.
