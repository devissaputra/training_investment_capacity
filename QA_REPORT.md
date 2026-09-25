# Final QA Report

**Release status: PASS.**

## Source and provenance
- official DfE Employer Skills Survey 2024 Investment in Training dataset verified;
- dataset page records 7,848 rows covering 2011–2024;
- source release date recorded as 2025-07-24;
- source CSV pinned by SHA-256 `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`;
- source row-count and fingerprint are enforced by the rebuild script;
- raw source is not redistributed.

## Comparability and methodology
- comparable UK-wide waves fixed to 2011, 2013, 2015, 2017, 2022, and 2024;
- 2019 exclusion documented because Scotland did not participate in ESS 2019;
- later-survey 2011 re-weighting convention documented;
- 2024 follow-up survey disposition documented: 6,210 expenditure interviews, 275 incomplete cases excluded, 5,935 sites retained;
- official modelling of missing expenditure components documented;
- source-provided 2024-price expenditure measures used directly rather than independently re-inflating historical figures;
- derived trainees/employees ratio explicitly labelled as an approximate descriptive reach measure.

## Numerical consistency
- 2011 real spend per employee: £2,410;
- 2024 real spend per employee: £1,700;
- 2011→2024 real per-employee change: −29.46%;
- 2024 total training expenditure: £53.0bn;
- 2024 highest sector: Construction, £2,630 per employee;
- 2024 lowest sector: Public admin., £920 per employee;
- derived reach ratio: 0.6022 in 2022 and 0.6285 in 2024;
- all headline JSON values reconciled against the complete packaged trend and sector tables.

## Descriptive robustness
- per-trainee real expenditure change, 2011→2024: −38.69%;
- total real training expenditure change, 2011→2024: −18.53%;
- derived reach-ratio change, 2011→2024: +8.26 percentage points;
- derived reach-ratio change, 2022→2024: +2.63 percentage points;
- 2024 sector max/min spend-per-employee ratio: 2.86;
- 2024 sector spend-per-employee range: £1,710;
- 2024 sector unweighted median: £1,570;
- 2024 sector unweighted coefficient of variation: 0.2623.

## Reproducibility and software QA
- `research/model.py` contains reusable calculations, diagnostics, and release validation;
- tests expanded from three lightweight checks to computational, provenance, hypothesis-pattern, sector, robustness, and CSV/JSON-consistency checks;
- standalone rebuild import-path bug fixed;
- `scripts/fetch_and_analyze.py --write` regenerates all committed evidence;
- deterministic line endings and JSON serialization verified;
- GitHub Actions CI passes on Python 3.10, 3.11, and 3.12;
- empirical source-to-output rebuild passes with zero evidence diff;
- complete MIT license restored and recognized by GitHub;
- `.gitignore`, CI workflow, empirical rebuild workflow, and manifest synchronized.

## Interpretation boundary
The study is descriptive and aggregate. Training investment capacity is operationalized through observed expenditure intensity and training reach. The repository does not claim to measure training quality, individual learning, causal returns, or latent organizational capability directly.

## GitHub presentation metadata
The recommended About text and final Topics are recorded in `GITHUB_METADATA.md`. Repository description and Topics are GitHub UI metadata and must be entered separately if the connected GitHub interface does not expose those mutations.
