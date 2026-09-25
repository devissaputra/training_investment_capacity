# Employer Training Investment Capacity: A Longitudinal UK Study

[![CI](https://github.com/devissaputra/training_investment_capacity/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/training_investment_capacity/actions/workflows/ci.yml)

> **Empirical Research Bundle** · **Portfolio Track: Learning & Development Research** · Workforce Development / Training Investment / Official Statistics

Longitudinal secondary analysis of UK Employer Skills Survey training expenditure, training reach, and sector heterogeneity from 2011 to 2024.

![Empirical workflow](assets/architecture.svg)

## Study status

**Completed secondary empirical analysis.** The release uses the Department for Education's 2024 *Investment in Training* open-data table and source-provided expenditure values expressed in 2024 prices. The source CSV is pinned by row count and SHA-256 before analysis. There is no synthetic fallback and the raw source is not republished in this repository.

## Research question

> How have real employer training investment intensity and training reach changed over time, and how heterogeneous is 2024 spending across sectors?

## Design and source

- **Design:** repeated cross-sectional secondary analysis of official UK employer statistics
- **Source:** UK Employer Skills Survey 2024 — Investment in Training
- **Release page:** https://explore-education-statistics.service.gov.uk/find-statistics/employer-skills-survey/2024
- **Dataset page:** https://explore-education-statistics.service.gov.uk/data-catalogue/data-set/a07479d1-e26d-4b66-9ec9-e683917c1388
- **Dataset rows:** 7,848
- **Published:** 2025-07-24
- **Analysis retrieval date:** 2026-09-25
- **Pinned SHA-256:** `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`
- **Reuse:** downloadable government open data; follow the publisher's Open Government Licence and release guidance

### Why 2019 is not in the UK trend

The released UK series uses 2011, 2013, 2015, 2017, 2022, and 2024. **2019 is intentionally excluded** because Scotland did not participate in ESS 2019. DfE therefore does not use 2019 as a UK-wide time-series point.

The 2011 comparison also follows the later ESS convention: DfE notes that 2011 data used in recent reports were re-weighted to the 2+ employee population for comparability.

## Hypotheses

1. **H1:** real training spend per employee in 2024 is below its 2011 level.
2. **H2:** 2024 training investment intensity varies substantially across sectors.
3. **H3:** between 2022 and 2024, the derived training-reach ratio can rise while real expenditure per employee falls.

## Empirical method

The pipeline filters national United Kingdom totals for comparable survey waves, uses the source's published **2024-price** expenditure series, and derives an approximate training-reach ratio as reported trainees divided by reported employees. It also compares all 13 published 2024 sectors using spend per employee and spend per trainee.

The repository does **not** independently re-inflate older expenditure values. The official dataset already provides the historical expenditure series in 2024 prices.

### Survey-estimation boundary

The Investment in Training statistics come from a follow-up survey of employers that reported training. In 2024, expenditure information was collected from **6,210 sites**; **275 incomplete cases were excluded**, leaving **5,935 sites** in the final analysis. The official methodology also documents modelling of missing expenditure components using range- and mean-based procedures. This repository analyzes the resulting published aggregate estimates; it does not reconstruct respondent-level imputation.

![Method](assets/method.svg)

## Headline findings

Real UK employer training spend per employee fell from **£2,410 in 2011 to £1,700 in 2024**, a **29.46% decline** in 2024 prices. The derived trainees-to-employees ratio rose from about **60.22% in 2022 to 62.85% in 2024** while spend per employee declined from £1,960 to £1,700.

In 2024, spend per employee ranged from **£920 in Public admin.** to **£2,630 in Construction**.

### Headline metrics

- real spend per employee, 2011: **£2,410**
- real spend per employee, 2024: **£1,700**
- real change, 2011–2024: **−29.46%**
- total training expenditure, 2011 in 2024 prices: **£65.06bn**
- total training expenditure, 2024: **£53.0bn**
- published trainees, 2024: **19.584m**
- derived training-reach ratio, 2022: **0.6022**
- derived training-reach ratio, 2024: **0.6285**
- 2022–2024 reach change: **+2.63 percentage points**
- highest 2024 sector: **Construction, £2,630 per employee**
- lowest 2024 sector: **Public admin., £920 per employee**

## Descriptive robustness checks

The analysis does not manufacture sampling intervals that are not present in the extracted aggregate table. Instead it checks whether the core interpretation is consistent across several published or directly derived measures:

| Diagnostic | Result |
|---|---:|
| Real spend per employee, 2011→2024 | −29.46% |
| Real spend per trainee, 2011→2024 | −38.69% |
| Real total training expenditure, 2011→2024 | −18.53% |
| Derived reach ratio, 2011→2024 | +8.26 pp |
| Derived reach ratio, 2022→2024 | +2.63 pp |
| 2024 sector max/min spend-per-employee ratio | 2.86× |
| 2024 sector spend-per-employee range | £1,710 |
| 2024 sector unweighted median | £1,570 |
| 2024 sector unweighted coefficient of variation | 0.2623 |

These are descriptive sensitivity checks, not causal estimates or formal hypothesis tests.

![Research evidence](assets/research_design.svg)

## What this study can and cannot claim

**Can claim:** under the official published series, real employer training expenditure intensity is lower in 2024 than in 2011, the 2024 sector distribution is heterogeneous, and the derived trainees-to-employees ratio moved upward from 2022 to 2024 while expenditure per employee moved downward.

**Cannot claim:** that expenditure causes learning outcomes, that higher expenditure means higher training quality, that the aggregate trainee count identifies unique worker-level exposure without measurement limitations, or that the study measures latent organizational training capacity directly.

In this repository, **training investment capacity is operationalized through observed expenditure intensity and training reach**. It is an L&D resource-deployment construct, not a direct measure of organizational capability.

![Finding and boundary](assets/evaluation.svg)

## Reproduce

Offline validation of the packaged release:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
```

Verify the pinned official source and recompute the analysis:

```bash
python scripts/fetch_and_analyze.py
```

Regenerate all derived evidence:

```bash
python scripts/fetch_and_analyze.py --write
```

GitHub Actions provides:
- multi-version offline CI on Python 3.10, 3.11, and 3.12;
- source-to-output rebuild verification against the pinned DfE CSV.

## Research bundle contents

- `README.md` — study overview and bounded findings
- `EMPIRICAL_STUDY.md` — protocol, survey-estimation notes, and validity boundaries
- `data/source_manifest.json` — source identity, fingerprint, comparability notes, and construct boundary
- `data/derived/primary_results.csv` — complete six-wave comparable UK trend
- `data/derived/secondary_results.csv` — all 13 published 2024 sectors
- `data/derived/robustness_results.csv` — descriptive sensitivity diagnostics
- `results/empirical_summary.json` — machine-readable headline results
- `scripts/fetch_and_analyze.py` — checksum-verified source-to-output rebuild
- `research/model.py` — reusable calculations and release validation
- `tests/` — computational, provenance, and scientific-invariant tests
- `.github/workflows/` — CI and empirical rebuild verification
- `docs/` — analysis plan, data dictionary, research design, references, paper blueprint, originality map
- `assets/` — study-specific SVG figures

## Research integrity

This is a secondary analysis of published aggregate official statistics. The analysis plan documents the released analysis and is **not a preregistration**. The repository distinguishes published estimates, derived calculations, interpretation, and limitations so that the L&D conclusions remain interview- and supervisor-defensible.
