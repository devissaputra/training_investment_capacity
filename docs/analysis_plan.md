# Analysis Plan

## Status

This document records the released secondary analysis.

It is not a preregistration.

## RQ1: long-run investment intensity

Use comparable UK-wide survey waves:

```text
2011, 2013, 2015, 2017, 2022, 2024
```

Measure real training expenditure per employee using the source-provided 2024-price series.

Report:

- complete six-wave trajectory;
- 2011 endpoint;
- 2024 endpoint;
- percentage change;
- monotonicity of the released series.

## RQ2: spend per trainee

Repeat the long-run comparison using real spend per trainee.

Report:

- complete six-wave trajectory;
- 2011–2024 percentage change.

## RQ3: reach versus intensity

For 2022 and 2024, compare:

- real spend per employee;
- real spend per trainee;
- total real expenditure;
- repository-derived trainees/employees ratio.

The main descriptive question is whether training reach and real investment intensity move in the same direction.

Do not interpret divergence as efficiency without outcome evidence.

## RQ4: 2024 sector heterogeneity

Use all 13 source sectors at United Kingdom / National / Total site-size level.

Report:

- spend per employee;
- spend per trainee;
- maximum;
- minimum;
- range;
- max/min ratio;
- unweighted median;
- unweighted coefficient of variation.

Do not rank sectors as good or bad.

## Derived training-reach measure

```text
training_coverage_share = trainees / employees
```

This is a repository-derived descriptive ratio from weighted published counts.

It is not a respondent-level probability and should not replace an official published percentage when that measure is available.

## Comparability rule

2019 is excluded from the UK-wide longitudinal trend because Scotland did not participate.

The rule is fixed in code and tests.

## Inflation rule

Use the official `twentyfour_prices_*` source fields.

Do not independently re-inflate historical expenditure.

## Robustness diagnostics

Report:

- per-employee real change;
- per-trainee real change;
- total real expenditure change;
- reach change 2011–2024;
- reach change 2022–2024;
- sector max/min ratio;
- sector range;
- sector median;
- sector CV.

These are descriptive diagnostics rather than inferential tests.

## Interpretation boundary

Do not infer:

- training quality;
- learning transfer;
- skill gain;
- causal return;
- latent organizational capability;
- worker-level exposure from aggregate counts.
