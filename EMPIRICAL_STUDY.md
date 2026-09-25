# Empirical Study Protocol

## Study title

**Employer Training Investment Capacity: A Longitudinal UK Study**

## Study type

Repeated cross-sectional secondary analysis of official UK employer statistics.

This document records the released analysis. It is not a preregistration.

## Research questions

**RQ1.** How has real training spend per employee changed across comparable UK survey waves?

**RQ2.** How has real spend per trainee changed?

**RQ3.** Did training reach and real investment intensity move in the same direction from 2022 to 2024?

**RQ4.** How heterogeneous was real training spend per employee across 13 sectors in 2024?

## Source

UK Employer Skills Survey 2024 — Investment in Training.

Released source identity:

- dataset rows: 7,848;
- published 24 July 2025;
- time coverage 2011–2024;
- SHA-256 `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`.

## Comparable UK time series

Use:

```text
2011, 2013, 2015, 2017, 2022, 2024
```

2019 is excluded from the UK-wide trend because Scotland did not participate.

## Primary measures

For each comparable UK wave:

- real training expenditure per employee in 2024 prices;
- real training expenditure per trainee in 2024 prices;
- total real training expenditure;
- published employee count;
- published trainee count;
- derived trainees-to-employees ratio.

## Derived reach measure

```text
training reach proxy = trainees / employees
```

This is a repository-derived descriptive ratio.

It is approximate because the published counts are survey weighted and may be rounded.

It should not be represented as a worker-level probability or a separate official estimate.

## Sector comparison

Use all 13 published UK sectors for 2024.

Report:

- spend per employee;
- spend per trainee;
- maximum;
- minimum;
- max/min ratio;
- range;
- unweighted median;
- unweighted coefficient of variation.

## Released descriptive hypotheses

**H1.** 2024 real training spend per employee is below the 2011 level.

**H2.** 2024 investment intensity differs substantially across sectors.

**H3.** Between 2022 and 2024, the derived training-reach ratio rises while real spend per employee falls.

These are released descriptive expectations and are not preregistered hypothesis tests.

## Survey-estimation context

The official methodology reports:

- 6,210 achieved 2024 Investment in Training interviews;
- 275 incomplete records excluded;
- 5,935 sites retained;
- weighting by site size, sector, training type, and geography;
- modelled missing expenditure components.

The repository does not reproduce the respondent-level survey production process.

## Interpretation rule

Expenditure and reach are analyzed as separate indicators of L&D resource deployment.

Neither is interpreted as direct evidence of:

- training quality;
- skill gain;
- learning transfer;
- causal return;
- latent organizational learning capability.

## Robustness

Triangulate the main interpretation using:

- per-employee real expenditure change;
- per-trainee real expenditure change;
- total real expenditure change;
- training-reach change;
- sector dispersion metrics.

These are descriptive robustness checks, not inferential tests.
