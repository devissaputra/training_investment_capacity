# Final QA Report

## Release verdict

**Status: PASS. The upgraded research package passes both regular CI and the strict official DfE source-to-release rebuild.**

The scientific narrative is in [REPORT.md](REPORT.md).

## Source verification

Verified against the official Employer Skills Survey 2024 Investment in Training dataset:

- official statistics;
- dataset rows: 7,848;
- time coverage: 2011–2024;
- source SHA-256: `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`;
- raw source redistributed: no.

## Comparability rules

The released UK-wide longitudinal series uses:

- 2011;
- 2013;
- 2015;
- 2017;
- 2022;
- 2024.

2019 is excluded because Scotland did not participate.

## Survey-production context

The official methodology reports:

- 6,210 achieved expenditure interviews;
- 275 incomplete cases excluded;
- 5,935 sites retained;
- weighting by site size, sector, training type, and geography;
- modelling of missing expenditure components.

The repository does not reconstruct respondent-level survey processing.

## Numerical consistency

| Check | Released value | Status |
|---|---:|---|
| 2011 spend per employee | £2,410 | PASS |
| 2024 spend per employee | £1,700 | PASS |
| 2011→2024 change | −29.46% | PASS |
| 2011 spend per trainee | £4,420 | PASS |
| 2024 spend per trainee | £2,710 | PASS |
| 2011→2024 trainee-spend change | −38.69% | PASS |
| Total real expenditure change | −18.53% | PASS |
| 2022 reach proxy | 0.6022 | PASS |
| 2024 reach proxy | 0.6285 | PASS |
| Reach change | +2.63 pp | PASS |
| Highest sector spend/employee | Construction, £2,630 | PASS |
| Lowest sector spend/employee | Public admin., £920 | PASS |
| Sector max/min ratio | 2.86× | PASS |
| Sector CV | 0.2623 | PASS |

## Scientific presentation improvements

The upgraded package:

- adds a complete scientific `REPORT.md`;
- reframes the contribution around **reach versus real investment intensity**;
- expands the paper blueprint into a manuscript structure;
- rebuilds the main visual as an evidence-first longitudinal chart;
- rebuilds the method visual with scientific color;
- adds a 2024 sector-distribution visual;
- makes official versus repository-derived measures explicit;
- strengthens survey-estimation and construct boundaries;
- adds reproducible figure generation;
- requires figure generation in CI;
- changes the public Report MD link from QA evidence to the scientific report;
- upgrades the Learning & Development portfolio copy.

## Claim boundary

A PASS supports the released descriptive evidence.

It does not imply:

- training effectiveness;
- skill gain;
- causal return on investment;
- individual learning outcomes;
- external validation;
- peer review.

## Final interpretation

The strongest defensible result is not merely that UK training expenditure declined.

It is that **real investment intensity declined substantially while training reach did not move in the same direction**, and that sector investment environments remained heterogeneous.

That creates a useful L&D measurement problem without overstating what expenditure data can tell us.
