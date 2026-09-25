# Research Design

## Research question
How have real employer training investment intensity and training reach changed over time, and how heterogeneous is 2024 spending across sectors?

## Design
Secondary analysis of repeated cross-sectional official UK employer statistics.

## Source
UK Department for Education, Employer Skills Survey 2024, Investment in Training data table. The release pins the 7,848-row CSV and records its SHA-256 in `data/source_manifest.json`.

## Comparable waves
2011, 2013, 2015, 2017, 2022, and 2024.

ESS 2019 is excluded from the UK-wide series because Scotland did not participate. This is a comparability decision documented by DfE, not a discretionary deletion based on the observed result.

## Hypotheses
1. H1: real training spend per employee in 2024 is below 2011.
2. H2: 2024 training investment intensity differs materially across the 13 sectors.
3. H3: between 2022 and 2024, the derived training-reach ratio rises while real spend per employee falls.

## Measures
- source-provided 2024-price expenditure per employee;
- source-provided 2024-price expenditure per trainee;
- source-provided total expenditure;
- derived trainees/employees ratio;
- sector-level expenditure intensity.

## Survey-production context
The 2024 follow-up collected expenditure data from 6,210 sites; 5,935 were retained after incomplete cases were excluded. DfE documents modelling procedures for missing components in producing the published estimates.

## Validity boundary
This design is descriptive and ecological. Aggregate expenditure and trainee estimates do not identify worker-level outcomes or causal mechanisms. The phrase training investment capacity is an operational label for observed resource deployment and reach, not a direct latent-capability measure.
