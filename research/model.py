from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_YEARS = [2011, 2013, 2015, 2017, 2022, 2024]
EXPECTED_SECTOR_COUNT = 13
EXPECTED_SOURCE_SHA256 = "cd9c834d3dc72b4649dc2d152072d1c92282c2373d51d735524f10fa531da437"


def coverage_share(trainees, employees):
    return float(trainees) / float(employees)


def real_change_pct(new, old):
    return (float(new) / float(old) - 1.0) * 100.0


def load_trend():
    with (ROOT / "data/derived/primary_results.csv").open(newline="") as f:
        return list(csv.DictReader(f))


def load_sectors():
    with (ROOT / "data/derived/secondary_results.csv").open(newline="") as f:
        return list(csv.DictReader(f))


def load_robustness():
    with (ROOT / "data/derived/robustness_results.csv").open(newline="") as f:
        return {r["metric"]: float(r["value"]) for r in csv.DictReader(f)}


def load_summary():
    return json.loads((ROOT / "results/empirical_summary.json").read_text())


def load_manifest():
    return json.loads((ROOT / "data/source_manifest.json").read_text())


def trend_diagnostics(rows=None):
    rows = rows or load_trend()
    years = [int(r["year"]) for r in rows]
    per_employee = [float(r["per_employee_gbp_2024_prices"]) for r in rows]
    coverage = [float(r["training_coverage_share"]) for r in rows]

    r11 = rows[0]
    r22 = next(r for r in rows if r["year"] == "2022")
    r24 = rows[-1]

    return {
        "years_match_release": years == EXPECTED_YEARS,
        "2019_excluded": 2019 not in years,
        "per_employee_2024_below_2011": float(r24["per_employee_gbp_2024_prices"]) < float(r11["per_employee_gbp_2024_prices"]),
        "per_employee_2024_below_2022": float(r24["per_employee_gbp_2024_prices"]) < float(r22["per_employee_gbp_2024_prices"]),
        "coverage_2024_above_2022": float(r24["training_coverage_share"]) > float(r22["training_coverage_share"]),
        "per_employee_monotone_nonincreasing": all(per_employee[i] >= per_employee[i + 1] for i in range(len(per_employee) - 1)),
        "coverage_values_in_unit_interval": all(0.0 <= x <= 1.0 for x in coverage),
        "real_change_2011_2024_pct": real_change_pct(r24["per_employee_gbp_2024_prices"], r11["per_employee_gbp_2024_prices"]),
    }


def sector_diagnostics(rows=None):
    rows = rows or load_sectors()
    vals = [float(r["per_employee_gbp"]) for r in rows]
    highest = max(rows, key=lambda r: float(r["per_employee_gbp"]))
    lowest = min(rows, key=lambda r: float(r["per_employee_gbp"]))
    mean = sum(vals) / len(vals)
    variance = sum((x - mean) ** 2 for x in vals) / len(vals)
    ordered = sorted(vals)
    median = ordered[len(ordered) // 2]

    return {
        "sector_count": len(rows),
        "highest_sector": highest["sector"],
        "highest_per_employee": float(highest["per_employee_gbp"]),
        "lowest_sector": lowest["sector"],
        "lowest_per_employee": float(lowest["per_employee_gbp"]),
        "max_min_ratio": float(highest["per_employee_gbp"]) / float(lowest["per_employee_gbp"]),
        "range_gbp": float(highest["per_employee_gbp"]) - float(lowest["per_employee_gbp"]),
        "unweighted_median_gbp": median,
        "unweighted_cv": (variance ** 0.5) / mean,
    }


def validate_bundle():
    trend = load_trend()
    sectors = load_sectors()
    robustness = load_robustness()
    summary = load_summary()
    manifest = load_manifest()

    if len(trend) != len(EXPECTED_YEARS) or len(sectors) != EXPECTED_SECTOR_COUNT:
        return False

    for row in trend:
        if abs(float(row["training_coverage_share"]) - coverage_share(row["trainees"], row["employees"])) > 5e-5:
            return False

    td = trend_diagnostics(trend)
    sd = sector_diagnostics(sectors)
    if not all(
        td[k]
        for k in (
            "years_match_release",
            "2019_excluded",
            "per_employee_2024_below_2011",
            "per_employee_2024_below_2022",
            "coverage_2024_above_2022",
            "per_employee_monotone_nonincreasing",
            "coverage_values_in_unit_interval",
        )
    ):
        return False

    if sd["highest_sector"] != "Construction" or sd["lowest_sector"] != "Public admin.":
        return False

    metrics = summary.get("headline_metrics", {})
    expected = {
        "uk_per_employee_2011_gbp_2024_prices": 2410,
        "uk_per_employee_2024_gbp": 1700,
        "highest_sector_per_employee_2024": 2630,
        "lowest_sector_per_employee_2024": 920,
    }
    if any(float(metrics.get(k, -1)) != float(v) for k, v in expected.items()):
        return False

    if abs(float(metrics.get("real_change_pct_2011_2024", 999)) - (-29.46)) > 0.01:
        return False
    if abs(float(metrics.get("training_coverage_share_2024", -1)) - 0.6285) > 1e-4:
        return False

    expected_robustness = {
        "per_employee_real_change_2011_2024_pct": -29.46,
        "per_trainee_real_change_2011_2024_pct": -38.69,
        "total_training_real_change_2011_2024_pct": -18.53,
        "coverage_change_2011_2024_pp": 8.26,
        "coverage_change_2022_2024_pp": 2.63,
        "sector_per_employee_max_min_ratio_2024": 2.86,
        "sector_per_employee_range_gbp_2024": 1710.0,
        "sector_per_employee_unweighted_median_gbp_2024": 1570.0,
        "sector_per_employee_unweighted_cv_2024": 0.2623,
    }
    for key, value in expected_robustness.items():
        if key not in robustness or abs(robustness[key] - value) > 0.005:
            return False

    if manifest.get("source_sha256") != EXPECTED_SOURCE_SHA256:
        return False
    if manifest.get("source_dataset_rows") != 7848:
        return False
    if manifest.get("raw_data_redistributed") is not False:
        return False

    return True
