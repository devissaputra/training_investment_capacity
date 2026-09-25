# Research Design

## Research question
How have real employer training investment intensity and training reach changed over time, and how heterogeneous is 2024 spending across sectors?

## Design
Secondary analysis of repeated cross-sectional official UK employer statistics.

## Source and unit of analysis
Source: UK Employer Skills Survey 2024 — Investment in Training. The operational unit follows the public dataset and is documented in `data/source_manifest.json` and `docs/data_dictionary.md`.

## Hypotheses
1. H1: real training spend per employee in 2024 is below its 2011 level.
2. H2: 2024 training investment intensity varies substantially across sectors.
3. H3: training reach can increase even while real expenditure per employee declines.

## Method
Extract United Kingdom national totals for comparable survey years, use the source’s 2024-price expenditure series, compute trainees divided by employees as the survey-derived training coverage share, and compare 2024 sector-level spend per employee and per trainee.

## Validity boundary
These are aggregate employer-survey statistics. They do not identify individual workers, training quality, causal returns to training, or service-time/queue mechanisms. The coverage measure is derived as reported trainees divided by reported employees.
