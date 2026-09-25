import pytest

from research.model import (
    EXPECTED_SOURCE_SHA256,
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
    assert coverage_share(60, 100) == 0.6
    assert round(coverage_share(19_583_800, 31_161_400), 4) == 0.6285


def test_real_change():
    assert round(real_change_pct(1700, 2410), 2) == -29.46
    assert round(real_change_pct(2710, 4420), 2) == -38.69


def test_released_years_and_2019_exclusion():
    d = trend_diagnostics()
    assert d["years_match_release"]
    assert d["2019_excluded"]
    assert d["per_employee_monotone_nonincreasing"]


def test_h1_and_h3_descriptive_patterns():
    d = trend_diagnostics()
    assert d["per_employee_2024_below_2011"]
    assert d["per_employee_2024_below_2022"]
    assert d["coverage_2024_above_2022"]


def test_sector_extrema_and_dispersion():
    d = sector_diagnostics()
    assert d["sector_count"] == 13
    assert d["highest_sector"] == "Construction"
    assert d["highest_per_employee"] == 2630
    assert d["lowest_sector"] == "Public admin."
    assert d["lowest_per_employee"] == 920
    assert round(d["max_min_ratio"], 2) == 2.86
    assert d["range_gbp"] == 1710
    assert d["unweighted_median_gbp"] == 1570
    assert round(d["unweighted_cv"], 4) == 0.2623


def test_summary_matches_packaged_tables():
    trend = load_trend()
    sectors = load_sectors()
    summary = load_summary()["headline_metrics"]
    r11 = next(r for r in trend if r["year"] == "2011")
    r24 = next(r for r in trend if r["year"] == "2024")
    hi = max(sectors, key=lambda r: float(r["per_employee_gbp"]))
    lo = min(sectors, key=lambda r: float(r["per_employee_gbp"]))

    assert summary["uk_per_employee_2011_gbp_2024_prices"] == int(float(r11["per_employee_gbp_2024_prices"]))
    assert summary["uk_per_employee_2024_gbp"] == int(float(r24["per_employee_gbp_2024_prices"]))
    assert summary["highest_sector_2024"] == hi["sector"]
    assert summary["highest_sector_per_employee_2024"] == int(float(hi["per_employee_gbp"]))
    assert summary["lowest_sector_2024"] == lo["sector"]
    assert summary["lowest_sector_per_employee_2024"] == int(float(lo["per_employee_gbp"]))


def test_robustness_table():
    r = load_robustness()
    assert r["per_employee_real_change_2011_2024_pct"] == pytest.approx(-29.46, abs=0.01)
    assert r["per_trainee_real_change_2011_2024_pct"] == pytest.approx(-38.69, abs=0.01)
    assert r["total_training_real_change_2011_2024_pct"] == pytest.approx(-18.53, abs=0.01)
    assert r["coverage_change_2011_2024_pp"] == pytest.approx(8.26, abs=0.01)
    assert r["sector_per_employee_max_min_ratio_2024"] == pytest.approx(2.86, abs=0.01)


def test_source_manifest_is_pinned():
    manifest = load_manifest()
    assert manifest["source_sha256"] == EXPECTED_SOURCE_SHA256
    assert manifest["source_dataset_rows"] == 7848
    assert manifest["source_release_published"] == "2025-07-24"
    assert manifest["raw_data_redistributed"] is False


def test_bundle_validation():
    assert validate_bundle()
