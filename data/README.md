# Data Provenance and Derived Evidence

## Canonical source

UK Employer Skills Survey 2024 — Investment in Training.

Official Explore Education Statistics dataset:

`https://explore-education-statistics.service.gov.uk/data-catalogue/data-set/a07479d1-e26d-4b66-9ec9-e683917c1388`

## Source identity

- published: 24 July 2025
- rows: 7,848
- time coverage: 2011–2024
- SHA-256: `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`

## Raw-file policy

The source is downloadable government open data.

The raw 7,848-row CSV is not republished in this repository.

## Comparable UK trend

Packaged UK-wide evidence uses:

```text
2011, 2013, 2015, 2017, 2022, 2024
```

2019 is excluded because Scotland did not participate.

## Packaged evidence

- `derived/primary_results.csv` — complete comparable UK longitudinal series
- `derived/secondary_results.csv` — 13-sector 2024 comparison
- `derived/robustness_results.csv` — descriptive robustness diagnostics

## Inflation handling

Historical comparisons use source fields already expressed in 2024 prices.

The repository does not independently apply inflation adjustments.

## Derived reach

`training_coverage_share` is calculated as:

```text
published trainees / published employees
```

It is an approximate descriptive ratio rather than a separately published official percentage.

## Source rebuild

```bash
python scripts/fetch_and_analyze.py --check
```

A source checksum or row-count change causes verification to fail rather than silently changing the release.
