# Data Dictionary

## Provenance
See `data/source_manifest.json`. Raw source observations are not silently republished.

## `data/derived/primary_results.csv`
Complete six-wave UK national trend used here; the secondary table contains all 13 reported 2024 sectors.

## `data/derived/secondary_results.csv`
When present and non-empty, this contains a second derived table needed to reproduce a reported comparison. If empty, no second packaged table is required.

## `results/empirical_summary.json`
Machine-readable headline sample sizes, estimates, and the release finding. Values must agree with README text and the derived CSVs.

## Construct boundary
These are aggregate employer-survey statistics. They do not identify individual workers, training quality, causal returns to training, or service-time/queue mechanisms. The coverage measure is derived as reported trainees divided by reported employees.
