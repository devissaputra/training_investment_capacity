# Scientific Report

## Employer Training Investment Capacity: A Longitudinal UK Study

### Executive summary

Employer training capacity is not captured by a single expenditure total. For Learning and Development decisions, at least three dimensions matter: how much employers spend in real terms, how much spending is available per employee or trainee, and how widely training reaches the workforce.

This study uses the official UK Employer Skills Survey 2024 **Investment in Training** dataset to examine those dimensions from 2011 to 2024. The source dataset contains 7,848 published rows covering investment totals, expenditure per employee, expenditure per trainee, employment, trainee counts, geography, sector, and site size. Historical expenditure values are taken directly from the source's 2024-price series rather than independently re-inflated.

The comparable UK-wide series uses 2011, 2013, 2015, 2017, 2022, and 2024. The 2019 wave is deliberately excluded because Scotland did not participate, so it is not treated as a comparable UK-wide observation.

The main result is a long-run decline in real training investment intensity. UK spend per employee fell from **£2,410 in 2011 to £1,700 in 2024**, a decline of **29.46%**. Spend per trainee fell from **£4,420 to £2,710**, a decline of **38.69%**, while total real expenditure fell from about **£65.1bn to £53.0bn**, a decline of **18.53%**.

The 2022 to 2024 comparison is especially useful for L&D interpretation. Real spend per employee fell from **£1,960 to £1,700**, while the repository-derived trainees-to-employees ratio increased from **60.22% to 62.85%**. The official ESS headline statistic similarly reports that around 63% of employees received training in 2024. The result therefore suggests a period in which training reach was maintained or expanded while real investment intensity fell.

That pattern should not be interpreted automatically as improved training efficiency. The source does not measure learning quality, transfer, return on investment, hours of effective practice, or individual outcomes. A wider reach with lower real spending per employee can reflect many mechanisms, including shorter training, cheaper delivery, different training mixes, changes in workforce composition, or cost compression.

Sector differences are also substantial. In 2024, real training spend per employee ranged from **£920 in Public Administration** to **£2,630 in Construction**, a **2.86×** max-to-min ratio. The unweighted sector median was £1,570 and the unweighted coefficient of variation was 0.2623.

The central contribution is therefore a reproducible L&D evidence package that separates **training reach**, **real investment intensity**, and **sector heterogeneity**. It supports more disciplined questions about training resource capacity without equating spending with learning effectiveness.

### Research questions

1. How has real UK employer training expenditure per employee changed between 2011 and 2024?
2. How has real expenditure per trainee changed over the same comparable survey waves?
3. Did training reach and real spending intensity move in the same direction from 2022 to 2024?
4. How heterogeneous was 2024 training investment intensity across sectors?
5. What can these aggregate official statistics support for L&D decision making, and what remains outside their measurement scope?

### Data source

Canonical source:

**UK Employer Skills Survey 2024 — Investment in Training**

Publisher:

- Department for Education / Skills England
- Explore Education Statistics

Dataset release:

- published: 24 July 2025
- official statistics
- 7,848 rows
- time coverage: 2011 to 2024
- national and regional geographic levels
- filters including sector and site size

The dataset provides both original-price and 2024-price expenditure measures. The released analysis uses the official 2024-price variables for longitudinal expenditure comparisons.

### Survey-estimation context

The 2024 Investment in Training study was a follow-up survey of employers that had reported training.

The official methodology reports:

- 6,210 achieved expenditure interviews;
- 275 incomplete cases excluded;
- 5,935 sites retained for analysis;
- an 80% response rate among complete contacts;
- weighting by employment size, grouped industry sector, training type, and geography;
- modelling of missing expenditure components before published total training expenditure was produced.

This repository analyzes the official aggregate outputs. It does not reconstruct respondent-level weighting, imputation, or expenditure modelling.

### Comparable UK series

The released UK trend contains:

| Year | Spend per employee, 2024 prices | Spend per trainee, 2024 prices | Total training expenditure, £m | Derived training reach |
|---:|---:|---:|---:|---:|
| 2011 | £2,410 | £4,420 | £65,060.71m | 54.59% |
| 2013 | £2,250 | £3,620 | £60,764.48m | 62.29% |
| 2015 | £2,240 | £3,570 | £62,082.66m | 62.71% |
| 2017 | £2,220 | £3,570 | £63,943.44m | 62.05% |
| 2022 | £1,960 | £3,250 | £58,995.47m | 60.22% |
| 2024 | £1,700 | £2,710 | £53,002.56m | 62.85% |

The training-reach column is a repository-derived ratio:

```text
published trainee count / published employee count
```

It is an approximate descriptive indicator because the source counts are survey-weighted and may be rounded. It should not replace the official published employee-trained percentage when that statistic is available.

### Long-run investment-intensity result

Real spend per employee:

```text
£2,410 → £2,250 → £2,240 → £2,220 → £1,960 → £1,700
```

Across the released comparable waves, the sequence is monotonically non-increasing.

The 2011 to 2024 change is:

```text
(1700 / 2410 - 1) × 100 = -29.46%
```

This is consistent with the official ESS finding that 2024 spend per employee was at the lowest level in the series.

### Spend per trainee

Real spend per trainee declined from £4,420 in 2011 to £2,710 in 2024:

```text
-38.69%
```

This is a larger proportional decline than the per-employee measure.

That does not identify whether training became more efficient or less intensive. Spend per trainee is a resource-intensity measure rather than an outcome measure.

### Total real training expenditure

Total UK training expenditure in 2024 was approximately **£53.0bn**, compared with approximately **£65.1bn** in 2011 in 2024 prices.

Released change:

```text
-18.53%
```

The total fell less sharply than spend per trainee because employment levels, trainee counts, and expenditure intensity changed together.

### Reach versus investment intensity

From 2022 to 2024:

- spend per employee fell from £1,960 to £1,700;
- spend per trainee fell from £3,250 to £2,710;
- total real training expenditure fell from £59.0bn to £53.0bn;
- the derived training-reach ratio rose from 60.22% to 62.85%.

This is the most important L&D pattern in the study.

It shows that **reach and investment intensity are different dimensions**.

A larger share of employees can receive training while the real resources available per employee or trainee fall.

The evidence does not reveal why this happened.

Possible explanations such as shorter courses, greater digital delivery, changes in the mix of training, lower unit costs, or changes in workforce composition remain hypotheses for future work.

### Sector heterogeneity

The released 2024 sector comparison contains all 13 source sectors.

| Sector | Spend per employee | Spend per trainee |
|---|---:|---:|
| Construction | £2,630 | £5,350 |
| Business Services | £2,240 | £3,710 |
| Education | £2,050 | £2,540 |
| Primary Sector & Utilities | £1,850 | £3,400 |
| Arts & Other Services | £1,730 | £2,790 |
| Information & Communications | £1,630 | £2,820 |
| Wholesale & Retail | £1,570 | £3,120 |
| Financial Services | £1,420 | £1,720 |
| Manufacturing | £1,410 | £2,920 |
| Health & Social Work | £1,390 | £1,730 |
| Hotels & Restaurants | £1,330 | £2,030 |
| Transport & Storage | £1,320 | £2,140 |
| Public admin. | £920 | £1,690 |

Summary diagnostics:

- maximum / minimum ratio: **2.86×**
- range: **£1,710**
- unweighted median: **£1,570**
- unweighted coefficient of variation: **0.2623**

The sector distribution shows why national averages should not be treated as a universal employer benchmark.

### Learning and Development interpretation

The evidence supports three separate management questions.

**Reach:** How much of the workforce is touched by training?

**Intensity:** How much real resource is deployed per employee or trainee?

**Distribution:** How different is the investment environment across sectors or employer groups?

Those questions should be analyzed separately before making claims about training capacity.

For an L&D leader, declining real spend per employee may justify investigation of:

- training mix;
- learning hours;
- delivery modality;
- internal versus external provision;
- protected learning time;
- manager support;
- transfer conditions;
- completion and participation;
- capability priorities;
- learning outcomes.

The aggregate expenditure series cannot answer those questions by itself.

### What this study supports

The release supports these statements:

- real UK training spend per employee was lower in 2024 than in 2011;
- real spend per trainee was also lower;
- total real training expenditure was lower;
- the derived training-reach ratio was higher in 2024 than in 2022;
- reach and investment intensity therefore moved in different directions over that period;
- 2024 sector investment intensity was heterogeneous.

### What this study does not support

The release does not establish:

- training effectiveness;
- learning transfer;
- employee skill gain;
- return on investment;
- causal effects of spending;
- that lower spending necessarily means worse training;
- that higher spending necessarily means better training;
- worker-level training exposure from aggregate counts;
- latent organizational learning capability.

### Threats to validity

**Construct validity.** Expenditure and reach are resource-deployment indicators, not direct measures of learning quality or capability.

**Survey-estimation validity.** Published figures reflect survey weighting and modelled missing expenditure components.

**Aggregate-data validity.** The repository works with published aggregate estimates and cannot model respondent-level variance or individual exposure.

**Comparability validity.** The UK-wide trend excludes 2019 because Scotland did not participate.

**Derived-ratio validity.** Training reach is derived from rounded, weighted aggregate trainee and employee counts.

**Sector interpretation.** Sector statistics are descriptive and may reflect workforce composition, occupation mix, employer size, regulatory requirements, and other structural differences.

**Causal validity.** The study is descriptive. It does not identify why investment changed.

### Reproducibility

Offline validation:

```bash
python -m pip install -r requirements.txt
pytest -q
python run_demo.py
python scripts/generate_figures.py
```

Pinned-source validation:

```bash
python scripts/fetch_and_analyze.py --check
```

Release regeneration:

```bash
python scripts/fetch_and_analyze.py --write
python scripts/generate_figures.py
```

The source dataset is pinned by:

- dataset UUID;
- row count: 7,848;
- SHA-256: `cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437`.

### Research integrity statement

This is a secondary analysis of published official statistics.

The released analysis was documented after dataset selection and is not a preregistration.

Official published statistics, repository-derived measures, interpretation, and speculation are kept separate throughout the package.
