# Reproducibility

## Offline validation

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
```

The test suite verifies:
- released UK years and intentional 2019 exclusion;
- trainees/employees coverage calculations;
- 2011→2024 real expenditure change;
- H1 and H3 descriptive patterns;
- all 13 sectors and 2024 extrema;
- sector dispersion diagnostics;
- CSV/JSON agreement;
- robustness-table values;
- source row count and SHA-256;
- complete bundle validation.

## Full source verification

```bash
python scripts/fetch_and_analyze.py
```

The script downloads the official DfE Investment in Training CSV and requires:
- **7,848 rows**;
- SHA-256 **`cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`**.

If either changes, the rebuild stops instead of silently producing a different release.

## Regenerate the evidence

```bash
python scripts/fetch_and_analyze.py --write
```

This regenerates:
- `data/derived/primary_results.csv`;
- `data/derived/secondary_results.csv`;
- `data/derived/robustness_results.csv`;
- `results/empirical_summary.json`.

## GitHub Actions

`.github/workflows/ci.yml` runs the offline suite on Python 3.10, 3.11, and 3.12.

`.github/workflows/empirical-rebuild.yml` downloads the pinned DfE source, regenerates the evidence, and fails if regenerated files differ from the committed release. It can also be launched manually.

## Reproducibility boundary

External public sources can move or be revised. Pinning the dataset UUID, publication date, row count, and SHA-256 makes such changes visible. A changed fingerprint is a reason to review and version a new release, not to silently accept new bytes.
