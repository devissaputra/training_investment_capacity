from research.model import (
    EXPECTED_SECTOR_COUNT,
    EXPECTED_YEARS,
    coverage_share,
    load_manifest,
    load_robustness,
    load_sectors,
    load_summary,
    load_trend,
    real_change_pct,
    sector_diagnostics,
    trend_diagnostics,
    validate_bundle,
)


def test_coverage_share():
    assert coverage_share(50, 100) == 0.5


def test_real_change():
    assert round(real_change_pct(1700, 2410), 2) == -29.46


def test_complete_released_trend():
    rows = load_trend()

    assert [int(row["year"]) for row in rows] == EXPECTED_YEARS
    assert 2019 not in [int(row["year"]) for row in rows]
    assert len(rows) == 6


def test_derived_reach_matches_counts():
    for row in load_trend():
        assert abs(
            float(row["training_coverage_share"])
            - coverage_share(row["trainees"], row["employees"])
        ) < 5e-5


def test_reach_intensity_divergence_2022_2024():
    rows = load_trend()
    r22 = next(row for row in rows if row["year"] == "2022")
    r24 = next(row for row in rows if row["year"] == "2024")

    assert float(r24["training_coverage_share"]) > float(r22["training_coverage_share"])
    assert float(r24["per_employee_gbp_2024_prices"]) < float(r22["per_employee_gbp_2024_prices"])
    assert float(r24["per_trainee_gbp_2024_prices"]) < float(r22["per_trainee_gbp_2024_prices"])
    assert float(r24["total_training_mn_gbp"]) < float(r22["total_training_mn_gbp"])


def test_per_employee_series_is_monotone_nonincreasing():
    diagnostics = trend_diagnostics(load_trend())

    assert diagnostics["per_employee_monotone_nonincreasing"]


def test_sector_distribution():
    rows = load_sectors()
    diagnostics = sector_diagnostics(rows)

    assert len(rows) == EXPECTED_SECTOR_COUNT
    assert diagnostics["highest_sector"] == "Construction"
    assert diagnostics["highest_per_employee"] == 2630
    assert diagnostics["lowest_sector"] == "Public admin."
    assert diagnostics["lowest_per_employee"] == 920
    assert round(diagnostics["max_min_ratio"], 2) == 2.86
    assert diagnostics["range_gbp"] == 1710
    assert diagnostics["unweighted_median_gbp"] == 1570
    assert round(diagnostics["unweighted_cv"], 4) == 0.2623


def test_robustness_table():
    robustness = load_robustness()

    assert robustness["per_employee_real_change_2011_2024_pct"] == -29.46
    assert robustness["per_trainee_real_change_2011_2024_pct"] == -38.69
    assert robustness["total_training_real_change_2011_2024_pct"] == -18.53
    assert robustness["coverage_change_2022_2024_pp"] == 2.63


def test_machine_readable_summary():
    summary = load_summary()
    metrics = summary["headline_metrics"]

    assert metrics["uk_per_employee_2011_gbp_2024_prices"] == 2410
    assert metrics["uk_per_employee_2024_gbp"] == 1700
    assert metrics["training_coverage_share_2022"] == 0.6022
    assert metrics["training_coverage_share_2024"] == 0.6285
    assert metrics["per_employee_real_change_2022_2024_pct"] == -13.27
    assert metrics["per_trainee_real_change_2022_2024_pct"] == -16.62
    assert metrics["total_training_real_change_2022_2024_pct"] == -10.16
    assert summary["release_version"] == "1.1.0"


def test_source_identity():
    manifest = load_manifest()

    assert manifest["source_dataset_rows"] == 7848
    assert (
        manifest["source_sha256"]
        == "cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437"
    )
    assert manifest["comparable_uk_years"] == EXPECTED_YEARS
    assert manifest["raw_data_redistributed"] is False


def test_bundle_validation():
    assert validate_bundle()
