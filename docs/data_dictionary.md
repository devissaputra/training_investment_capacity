# Data Dictionary

## Provenance
See `data/source_manifest.json`. The official 7,848-row DfE source CSV is pinned by SHA-256. Raw source rows are not redistributed.

## `data/derived/primary_results.csv`
Complete comparable UK-wide national trend used in the release.

Columns:
- `year`: comparable ESS survey wave;
- `per_employee_gbp_2024_prices`: source-provided training expenditure per employee in 2024 prices;
- `per_trainee_gbp_2024_prices`: source-provided training expenditure per trainee in 2024 prices;
- `total_training_mn_gbp`: source-provided total training expenditure in £ millions, 2024 prices;
- `employees`: published estimated employees;
- `trainees`: published estimated trainees;
- `training_coverage_share`: repository-derived trainees/employees ratio.

The released years are 2011, 2013, 2015, 2017, 2022, and 2024. 2019 is excluded because Scotland did not participate in ESS 2019 and is not treated by DfE as a comparable UK-wide time-series point.

## `data/derived/secondary_results.csv`
Complete set of 13 published 2024 sectors used in the cross-sector comparison.

Columns:
- `sector`;
- `per_employee_gbp`;
- `per_trainee_gbp`;
- `employees`;
- `trainees`.

## `data/derived/robustness_results.csv`
Compact descriptive diagnostics derived from the two complete tables:
- changes in per-employee, per-trainee, and total real expenditure;
- changes in the derived reach ratio;
- sector max/min ratio, range, unweighted median, and unweighted coefficient of variation.

## `results/empirical_summary.json`
Machine-readable headline results, comparable-year list, and robustness diagnostics. Tests verify agreement with the derived tables.

## Construct boundary
The coverage ratio is a derived descriptive measure based on aggregate counts. Training investment capacity is operationalized through observed expenditure intensity and reach, not direct training quality, learning outcomes, or latent capability.
