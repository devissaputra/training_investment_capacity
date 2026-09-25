# Data Dictionary

## Source fields

The rebuild uses the official Employer Skills Survey Investment in Training CSV.

Core source fields used include:

- `time_period`
- `geographic_level`
- `country_name`
- `site_size`
- `sector`
- `employees`
- `trainees`
- `twentyfour_prices_total_per_employee`
- `twentyfour_prices_total_per_trainee`
- `twentyfour_prices_sum_total_mn`

## `data/derived/primary_results.csv`

Complete comparable UK trend.

Columns:

- `year`
- `per_employee_gbp_2024_prices`
- `per_trainee_gbp_2024_prices`
- `total_training_mn_gbp`
- `employees`
- `trainees`
- `training_coverage_share`

### Training coverage share

```text
trainees / employees
```

This is repository-derived from published survey-weighted counts.

Because the published counts may be rounded, it is an approximate descriptive reach indicator.

## `data/derived/secondary_results.csv`

All 13 published UK sectors in 2024.

Columns:

- sector;
- spend per employee;
- spend per trainee;
- published employees;
- published trainees.

## `data/derived/robustness_results.csv`

Released descriptive diagnostics:

- real per-employee change;
- real per-trainee change;
- total real expenditure change;
- reach change 2011–2024;
- reach change 2022–2024;
- sector max/min ratio;
- sector range;
- sector median;
- sector coefficient of variation.

## `results/empirical_summary.json`

Machine-readable headline evidence, including:

- endpoint investment values;
- long-run real change;
- 2024 total expenditure;
- 2024 trainee count;
- sector extrema;
- 2022 and 2024 reach values;
- robustness diagnostics;
- comparable years;
- interpretation boundary.

## Important distinction

`training_coverage_share` is repository-derived.

It should not be presented as if it were a separately published official ESS percentage without explaining the derivation.
