# Empirical Study Protocol

## Study
Employer Training Investment Capacity: A Longitudinal UK Study

## Research question
How have real employer training investment intensity and training reach changed over time, and how heterogeneous is 2024 spending across sectors?

## Design and source
Secondary analysis of repeated cross-sectional official UK employer statistics from the Department for Education's *Employer Skills Survey 2024 — Investment in Training* dataset. The release pins the 7,848-row CSV published on 2025-07-24 with SHA-256 `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`. Analysis retrieval date: 2026-09-25.

## Comparable time series
The UK-wide trend uses 2011, 2013, 2015, 2017, 2022, and 2024. ESS 2019 is intentionally excluded because Scotland did not participate, so it is not treated as a comparable UK-wide observation. DfE also notes that 2011 data used in later reports are re-weighted to the 2+ employee population.

## Hypotheses
1. H1: real training spend per employee in 2024 is below its 2011 level.
2. H2: 2024 training investment intensity varies substantially across sectors.
3. H3: between 2022 and 2024, the derived trainees-to-employees ratio rises while real expenditure per employee declines.

## Operationalization and method
Use the source's published 2024-price expenditure variables for comparable national UK rows. Training reach is operationalized as a repository-derived ratio of published trainees to published employees. Sector heterogeneity is summarized using all 13 published 2024 sector rows.

Because the employee and trainee counts are published aggregate survey estimates and may be rounded, the derived coverage ratio is an approximate descriptive indicator rather than a separate official percentage estimate.

## Survey-estimation context
The official Investment in Training methodology reports 6,210 completed 2024 expenditure interviews, with 275 incomplete cases excluded and 5,935 sites retained for analysis. Missing expenditure inputs are handled in the official production process with documented modelling procedures, including range- and mean-based assignments. This repository analyzes the published aggregate output and does not recreate respondent-level modelling.

## Primary empirical result
Real UK employer training spend per employee fell from £2,410 in 2011 to £1,700 in 2024, a 29.46% decline in 2024 prices. The derived trainees-to-employees ratio rose from 60.22% in 2022 to 62.85% in 2024 while spend per employee fell. In 2024, spend per employee ranged from £920 in Public admin. to £2,630 in Construction.

## Descriptive robustness
The same long-run direction appears in multiple investment measures: per-trainee expenditure fell 38.69% and total real training expenditure fell 18.53% from 2011 to 2024. The derived reach ratio increased 8.26 percentage points from 2011 and 2.63 points from 2022. Across the 13 sectors, the 2024 max/min spend-per-employee ratio is 2.86 and the unweighted coefficient of variation is 0.2623.

These diagnostics describe the published aggregate series; they are not formal causal or inferential tests.

## Validity and claim boundary
The statistics do not identify individual workers, training quality, causal returns to training, or latent organizational capability. Expenditure intensity and the derived reach ratio are treated as observable indicators of L&D resource deployment. They should not be interpreted as direct measurements of training effectiveness or organizational learning capacity.

## Reproducibility status
The repository packages all released trend and sector rows, robustness diagnostics, a source fingerprint, a source-to-output regeneration script, release invariants, expanded tests, and GitHub Actions verification. The released analysis was documented after dataset selection and must not be represented as preregistered.
