# Evaluation fixtures

These fixtures test four different questions independently:

- `activation/`: should the skill trigger?
- `traversal/`: did the selected skill read the smallest sufficient reference set?
- `output/`: did the work satisfy its artifact and completion contracts?
- `compression-ablation/`: does a shorter candidate preserve quality relative to the current skill
  and a no-skill baseline?

The suite: 27 activation cases (14 router-row positives, 2 indirect-vocabulary positives, 8
boundary-arrow negatives, 2 adversarial sibling-naming negatives, 1 out-of-family negative), 11
traversal cases (one per flagship path, every expected/forbidden reference verified on disk), 6
output cases (5 artifact-contract checks plus one never-ship forbidden-string sweep), and 3
compression-ablation cases exercising rules at the start, middle, and end of the loaded set. Keep
expected and forbidden reads explicit so routing regressions are diagnosable. The `never-ship-strings`
output case's assertions intentionally quote the banned figures verbatim — that file is not
agent-loaded, so quoting them there is not a shipping violation.
