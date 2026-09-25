# Analysis Plan

## Status
This file documents the analysis released in this repository. It is **not a preregistration** and should not be described as one.

## Primary estimand / descriptive target
How have real employer training investment intensity and training reach changed over time, and how heterogeneous is 2024 spending across sectors?

## Analysis
Extract United Kingdom national totals for comparable survey years, use the source’s 2024-price expenditure series, compute trainees divided by employees as the survey-derived training coverage share, and compare 2024 sector-level spend per employee and per trainee.

## Specified outputs for this release
1. source/sample size and provenance;
2. primary derived metric(s);
3. comparator, cross-group, cross-time, or frontier contrast where applicable;
4. uncertainty, sensitivity, or error information supported by the source;
5. explicit construct and external-validity limitations.

## Missingness / exclusions

The analysis uses official comparable UK survey rows with numeric published values. Suppressed or non-numeric cells are excluded rather than imputed. Training reach is computed as trainees divided by employees where both official quantities are available.

## Interpretation boundary
These are aggregate employer-survey statistics. They do not identify individual workers, training quality, causal returns to training, or service-time/queue mechanisms. The coverage measure is derived as reported trainees divided by reported employees.
