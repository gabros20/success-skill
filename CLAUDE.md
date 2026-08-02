# Claude Code repository guide

This is the released `success-skill` (runtime skill `success`, under `skills/success/`). Read
[AGENTS.md](AGENTS.md) for the ownership boundary and non-negotiable invariants — especially: run
the Existence Gate before building any CS apparatus, say **"not published," never "not measured"**
for any health-score or churn-model accuracy claim, ask the Observability Question before scoring
anything, and treat score-vs-prediction as different artifacts. This skill does not own the
in-product onboarding flow (`design`), retention *experiments* (`growth`), pricing/dunning
(`product`), the support assistant's mechanics and evals (`ai`), or internal SLOs (`operate`).

Run `scripts/check-sync` before any release. Keep `SKILL.md` the router; keep versions out of it.
