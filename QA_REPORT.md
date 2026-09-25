# Final QA Report

**Release status: PASS after correction.**

## Checks completed
- provenance and source identity reviewed;
- licensing/reuse note recorded;
- derived CSV structure checked against the stated sample and estimand;
- `results/empirical_summary.json` reconciled with packaged evidence;
- README/report language reconciled with the numerical results;
- study-specific methods moved into `research/model.py`;
- tests exercise scientific logic and invariants;
- internet rebuild script has no synthetic fallback;
- four SVG assets regenerated as study-specific figures and XML-validated;
- local Markdown links checked;
- citation metadata points to the final repository slug;
- no preregistration claim is made.

## Final empirical finding
Real UK employer training spend per employee fell from £2,410 in 2011 to £1,700 in 2024 (−29.5%). The survey-derived trained-employee share nevertheless rose from about 60.2% in 2022 to 62.8% in 2024. In 2024, spend per employee ranged from £920 in Public Administration to £2,630 in Construction.

## Required interpretation boundary
These are aggregate employer-survey statistics. They do not identify individual workers, training quality, causal returns to training, or service-time/queue mechanisms. The coverage measure is derived as reported trainees divided by reported employees.
