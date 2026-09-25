# Employer Training Investment Capacity: A Longitudinal UK Study

[![CI](https://github.com/devissaputra/training_investment_capacity/actions/workflows/ci.yml/badge.svg)](https://github.com/devissaputra/training_investment_capacity/actions/workflows/ci.yml)
[![Empirical rebuild](https://github.com/devissaputra/training_investment_capacity/actions/workflows/empirical-rebuild.yml/badge.svg)](https://github.com/devissaputra/training_investment_capacity/actions/workflows/empirical-rebuild.yml)

> **Learning & Development Research Package** · Workforce Development · Training Investment · Official Statistics

A reproducible longitudinal secondary analysis of UK employer training expenditure, training reach, and sector variation using the official Employer Skills Survey 2024 Investment in Training dataset.

![Training investment and reach](assets/research_design.svg)

## Start here

- [Scientific report](REPORT.md)
- [Empirical study protocol](EMPIRICAL_STUDY.md)
- [Paper blueprint](docs/paper_blueprint.md)
- [Research design](docs/research_design.md)
- [Analysis plan](docs/analysis_plan.md)
- [Reproducibility guide](REPRODUCIBILITY.md)
- [Data provenance](data/README.md)
- [Final QA evidence](QA_REPORT.md)

## Core question

> How have real employer training investment intensity and training reach changed over time, and how much sector variation sits behind the national average?

## Official source

| Item | Released value |
|---|---|
| Source | UK Employer Skills Survey 2024 — Investment in Training |
| Publisher | Department for Education / Skills England |
| Rows | 7,848 |
| Coverage | 2011–2024 |
| Release | Official statistics |
| Comparable UK waves used | 2011, 2013, 2015, 2017, 2022, 2024 |
| Source SHA-256 | `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437` |

2019 is intentionally excluded from the UK-wide trend because Scotland did not participate in ESS 2019.

## Main finding

Real spend per employee declined:

```text
£2,410 → £2,250 → £2,240 → £2,220 → £1,960 → £1,700
 2011      2013      2015      2017      2022      2024
```

That is a **29.46% real decline** from 2011 to 2024.

Real spend per trainee declined by **38.69%**, while total real training expenditure declined by **18.53%**.

## The more interesting L&D pattern

From 2022 to 2024:

- real spend per employee: **£1,960 → £1,700**
- real spend per trainee: **£3,250 → £2,710**
- total real expenditure: **£59.0bn → £53.0bn**
- derived trainees/employees reach: **60.22% → 62.85%**

So **training reach increased while real investment intensity fell**.

That is not evidence that training became more efficient. It is evidence that reach and resource intensity are distinct dimensions and should not be collapsed into one headline measure.

![Method](assets/method.svg)

## 2024 sector variation

Spend per employee ranged from:

**£920 — Public Administration**

to

**£2,630 — Construction**

Released sector diagnostics:

- max/min ratio: **2.86×**
- range: **£1,710**
- unweighted median: **£1,570**
- unweighted CV: **0.2623**

The national average therefore hides materially different sector investment environments.

## Research contribution

The package separates three questions that are often blurred together:

1. **Reach** — what share of the workforce appears in the training count?
2. **Investment intensity** — how much real training resource is deployed per employee or trainee?
3. **Distribution** — how much does investment vary across sectors?

This produces a stronger L&D interpretation than simply reporting total training expenditure.

## Survey context

The 2024 Investment in Training follow-up collected expenditure information from 6,210 sites. The official methodology reports that 275 incomplete interviews were excluded, leaving 5,935 sites for analysis.

The published estimates also incorporate weighting and modelled missing expenditure components. This repository analyzes those official aggregate estimates rather than treating them as raw accounting records.

## Claim boundary

**Supported:** real employer training investment intensity declined over the released comparable UK series, reach and spending intensity diverged from 2022 to 2024, and 2024 sector investment intensity was heterogeneous.

**Not supported:** training quality, learning transfer, causal return on investment, individual learning outcomes, or the claim that more spending necessarily produces better learning.

![Evidence boundary](assets/evaluation.svg)

## Reproduce

Offline:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/generate_figures.py
```

Pinned official-source verification:

```bash
python scripts/fetch_and_analyze.py --check
```

Regenerate evidence:

```bash
python scripts/fetch_and_analyze.py --write
python scripts/generate_figures.py
```

## Repository map

- `REPORT.md` — scientific report
- `EMPIRICAL_STUDY.md` — released protocol
- `docs/paper_blueprint.md` — manuscript plan
- `docs/analysis_plan.md` — estimands and diagnostics
- `docs/research_design.md` — design and validity boundaries
- `docs/data_dictionary.md` — evidence definitions
- `data/source_manifest.json` — source identity and fingerprint
- `data/derived/primary_results.csv` — complete UK longitudinal series
- `data/derived/secondary_results.csv` — 13-sector 2024 comparison
- `data/derived/robustness_results.csv` — descriptive sensitivity metrics
- `results/empirical_summary.json` — machine-readable headline evidence
- `scripts/fetch_and_analyze.py` — source-to-output rebuild
- `scripts/generate_figures.py` — reproducible scientific visuals
- `tests/` — scientific and release invariants

## Research integrity

This is a secondary analysis of published official statistics. It is not preregistered, causal, or peer reviewed. Official estimates and repository-derived calculations are explicitly distinguished.
