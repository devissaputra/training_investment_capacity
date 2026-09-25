# Reproducibility Guide

## Objective

The release supports:

1. offline validation from packaged evidence;
2. strict reconstruction from the pinned official DfE source;
3. deterministic regeneration of the scientific figures.

## Environment

```bash
python -m pip install -r requirements.txt
```

## Offline verification

```bash
pytest -q
python run_demo.py
python scripts/generate_figures.py --out-dir /tmp/training_investment_figures
```

The test suite verifies:

- released comparable UK years;
- intentional 2019 exclusion;
- derived reach calculations;
- 2011→2024 real expenditure change;
- 2022→2024 reach-intensity divergence;
- monotonic non-increase of real spend per employee;
- all 13 sectors;
- sector extrema and dispersion;
- robustness-table values;
- machine-readable summary values;
- source identity;
- complete bundle validation.

## Official-source verification

```bash
python scripts/fetch_and_analyze.py --check
```

The script:

1. downloads the official Investment in Training CSV;
2. verifies the pinned SHA-256;
3. requires exactly 7,848 source rows;
4. reconstructs the six-wave UK trend;
5. reconstructs all 13 sector rows;
6. recomputes robustness diagnostics;
7. rebuilds the machine-readable summary in memory;
8. requires agreement with the packaged release.

There is no synthetic fallback.

## Regenerate release evidence

```bash
python scripts/fetch_and_analyze.py --write
python scripts/generate_figures.py
```

## GitHub Actions

Regular CI runs:

- scientific tests on Python 3.10, 3.11, and 3.12;
- bundle validation;
- scientific figure generation.

The empirical rebuild workflow runs the strict official-source check.

## Source identity

- dataset UUID: `a07479d1-e26d-4b66-9ec9-e683917c1388`
- rows: 7,848
- SHA-256: `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`
- retrieval date: 2026-09-25

## Reproducibility boundary

A successful rebuild confirms this secondary analysis of the pinned aggregate official statistics.

It does not validate training quality, learning transfer, skill gain, or causal return on investment.
