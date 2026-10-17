# Changelog

All notable changes to **success** are documented here.

The release procedure synchronizes `.codex-plugin/plugin.json`, this changelog, git tag
`v<version>`, and the matching GitHub Release. Runtime `SKILL.md` contains no version metadata.

## [Unreleased]

### Added
- Queue unreleased changes here.

## [0.2.1] — 2026-10-17

### Fixed
- `evals/README.md` suite count: 27 activation cases (8 boundary-arrow negatives) and 11 traversal
  cases, including the AI voice support-line cases.

## [0.2.0] — 2026-10-17

### Added
- [ai-support-policy](skills/success/references/ai-support-policy.md) gains "AI voice support
  lines: disclose first, keep a person reachable" — EU AI Act Art. 50(1)/(5) disclosure at the
  first interaction (applies since 2026-08-02), Art. 50(3) as the flag on mood inferred from the
  caller's audio, the US inbound position (TCPA does not reach inbound answering, per FCC 24-84's
  own text; states still apply), the human path on every call (explicit ask, keypad beside speech,
  context carried, spoken recovery), and Hungary's Fgytv. 17/B. § duties for in-scope service
  lines (five-minute answer, live-voice complaint option first, record all with unique ID, five-year
  retention, free copy within 30 days, notice at call start). Primary texts re-read 2026-10-17;
  legal review required; the five minutes framed as a statutory maximum wait, not a template
  SLA; AI placement behind the human option labelled as the conservative design reading; Annex III
  emotion recognition named; Art. 50 cited to EUR-Lex.
- Router row, Validation item, voice-pipeline and outbound-call handoffs (`ai` `surface-voice.md`,
  `operate`, `marketing`), and one traversal eval.

## [0.1.0] — 2026-08-02

### Added
- Initial release: faceted-router `success` skill — 10 primary jobs × 4 surfaces
  (agentic as additive overlay) + handoff, 15 references, 4 assets.
- Flagship reference: health-and-risk-signals (score-vs-prediction as different artifacts,
  "not published, never not measured", the Observability Question, four-study academic
  convergence, honest ML ceilings with leakage exhibits).
- The Existence Gate (`when-success-applies`): no source anywhere states when a distinct
  success function is worth having; this pack constructs the gate.
- AI-support policy layer: the nine-pattern escalation corpus, consent-first handoff,
  the typed-field-per-turn exemplar, resolution-rate and deflection honesty.
- Runnable, self-testing assets: `nrr_calc.py` (four SEC-verbatim NRR/GRR mechanics),
  `churn_baseline_check.py`, `sla_capacity_calc.py`, `health_score_audit.md`.
- Never-ship strip against the falsified retention/support folklore corpus, enforced by
  `scripts/lint-skill`.
- Behavioral eval suites: activation, traversal, output, compression-ablation.
- Research corpora + synthesis in `research/` (5 channels, date-stamped 2026-08-02).

[0.2.1]: https://github.com/gabros20/success-skill/releases/tag/v0.2.1
[0.2.0]: https://github.com/gabros20/success-skill/releases/tag/v0.2.0
[0.1.0]: https://github.com/gabros20/success-skill/releases/tag/v0.1.0
