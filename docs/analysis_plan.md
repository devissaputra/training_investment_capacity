# Analysis Plan

## Status
This file documents the analysis released in this repository. It is **not a preregistration** and should not be described as one.

## Primary descriptive target
How have real employer training investment intensity and training reach changed over time, and how heterogeneous is 2024 spending across sectors?

## Source and comparability
The source is the official DfE Employer Skills Survey 2024 Investment in Training data table. UK-wide comparable waves are 2011, 2013, 2015, 2017, 2022, and 2024. The 2019 wave is excluded from the UK time series because Scotland did not participate.

The analysis uses the source-provided 2024-price expenditure variables. It does not independently apply an inflation adjustment to nominal expenditure.

## Primary operationalizations
1. real training expenditure per employee;
2. real training expenditure per trainee;
3. real total training expenditure;
4. approximate training-reach ratio = published trainees / published employees;
5. 2024 sector spend per employee and per trainee.

The phrase **training investment capacity** refers here to observed resource-deployment intensity and reach. It does not assert a direct measure of latent organizational capability.

## Hypotheses
1. H1: 2024 real spend per employee is below 2011.
2. H2: 2024 spend per employee is heterogeneous across the 13 published sectors.
3. H3: from 2022 to 2024, the derived reach ratio rises while real spend per employee falls.

## Released descriptive diagnostics
- 2011→2024 percent change in per-employee expenditure;
- 2011→2024 percent change in per-trainee expenditure;
- 2011→2024 percent change in real total expenditure;
- 2011→2024 and 2022→2024 coverage-ratio changes;
- 2024 sector max/min ratio;
- 2024 sector range;
- 2024 unweighted sector median;
- 2024 unweighted sector coefficient of variation.

These diagnostics test the stability of the descriptive interpretation across alternative scale summaries. They are not formal significance tests.

## Survey-estimation context
The 2024 Investment in Training follow-up collected expenditure information from 6,210 sites. The official methodology states that 275 incomplete cases were excluded, leaving 5,935 sites for analysis. Published expenditure totals also incorporate documented modelling of missing inputs. The repository therefore treats the downloaded values as official aggregate estimates, not raw employer accounting records.

## Missingness / exclusions
Suppressed or non-numeric aggregate cells are excluded rather than imputed by this repository. Respondent-level imputation is part of the official survey production methodology and is not repeated here.

## Interpretation boundary
The analysis cannot identify individual workers, training quality, causal returns, training effectiveness, or latent organizational capability. The trainees/employees ratio is derived from published aggregate counts and can differ slightly from an official percentage due to rounding and survey estimation.
