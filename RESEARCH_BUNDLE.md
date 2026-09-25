# Research Bundle Definition

This repository qualifies as an empirical research bundle because it connects one explicit L&D research question to a named official source, a documented comparability rule, executable source verification, complete derived evidence, descriptive robustness checks, automated tests, CI, and bounded interpretation.

## Question
How have real employer training investment intensity and training reach changed over time, and how heterogeneous is 2024 spending across sectors?

## Empirical core
A six-wave UK-wide real-expenditure trend, derived training-reach ratio, complete 13-sector 2024 comparison, and descriptive robustness diagnostics.

## Main result
Real UK employer training spend per employee fell from £2,410 in 2011 to £1,700 in 2024 in 2024 prices (−29.46%). From 2022 to 2024 the derived trainees/employees ratio rose from 0.6022 to 0.6285 while spend per employee fell. In 2024 sector spend ranged from £920 to £2,630 per employee.

## Robustness
The 2011→2024 decline is also visible in per-trainee expenditure (−38.69%) and total real training expenditure (−18.53%). The 2024 sector max/min ratio is 2.86 and the unweighted sector coefficient of variation is 0.2623.

## Source integrity
The official 7,848-row DfE CSV is pinned with SHA-256 `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`. The rebuild stops on source fingerprint or row-count changes.

## Boundary
The study is descriptive and aggregate. Training investment capacity is operationalized through observed expenditure intensity and reach. It is not a direct measure of training effectiveness, worker-level learning, causal return, or latent organizational capability.

## Release criterion
A release passes only if source identity, comparable years, derived tables, JSON summary, robustness diagnostics, tests, CI, and documentation agree numerically and semantically.
