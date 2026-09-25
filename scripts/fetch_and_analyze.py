#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import urllib.request
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from research.model import (
    coverage_share,
    load_robustness,
    load_sectors,
    load_summary,
    load_trend,
    real_change_pct,
)

MANIFEST_PATH = ROOT / "data/source_manifest.json"
TREND_PATH = ROOT / "data/derived/primary_results.csv"
SECTOR_PATH = ROOT / "data/derived/secondary_results.csv"
ROBUSTNESS_PATH = ROOT / "data/derived/robustness_results.csv"
SUMMARY_PATH = ROOT / "results/empirical_summary.json"
EXPECTED_YEARS = [2011, 2013, 2015, 2017, 2022, 2024]


def number(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def fetch_source():
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    request = urllib.request.Request(
        manifest["direct_data_url"],
        headers={"User-Agent": "training-investment-capacity/1.1"},
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        payload = response.read()

    actual = hashlib.sha256(payload).hexdigest()
    expected = manifest["source_sha256"]
    if actual != expected:
        raise RuntimeError(
            f"Source checksum mismatch: expected {expected}, got {actual}. "
            "Stop rather than silently analyzing a changed data file."
        )

    rows = list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))))
    if len(rows) != manifest["source_dataset_rows"]:
        raise RuntimeError(
            f"Source row-count mismatch: expected {manifest['source_dataset_rows']}, got {len(rows)}."
        )
    return rows, actual


def analyze(rows):
    uk = [
        row
        for row in rows
        if row["geographic_level"] == "National"
        and row["country_name"] == "United Kingdom"
        and row["site_size"] == "Total"
        and row["sector"] == "Total"
        and number(row["twentyfour_prices_total_per_employee"]) is not None
    ]
    uk = sorted(uk, key=lambda row: int(row["time_period"]))

    trend = [
        {
            "year": int(row["time_period"]),
            "per_employee_gbp_2024_prices": number(row["twentyfour_prices_total_per_employee"]),
            "per_trainee_gbp_2024_prices": number(row["twentyfour_prices_total_per_trainee"]),
            "total_training_mn_gbp": number(row["twentyfour_prices_sum_total_mn"]),
            "employees": number(row["employees"]),
            "trainees": number(row["trainees"]),
            "training_coverage_share": coverage_share(row["trainees"], row["employees"]),
        }
        for row in uk
    ]

    years = [row["year"] for row in trend]
    if years != EXPECTED_YEARS:
        raise RuntimeError(
            f"Comparable UK release years changed: expected {EXPECTED_YEARS}, got {years}."
        )

    sector_source = [
        row
        for row in rows
        if row["geographic_level"] == "National"
        and row["country_name"] == "United Kingdom"
        and row["time_period"] == "2024"
        and row["site_size"] == "Total"
        and row["sector"] != "Total"
        and number(row["twentyfour_prices_total_per_employee"]) is not None
    ]
    sectors = [
        {
            "sector": row["sector"],
            "per_employee_gbp": number(row["twentyfour_prices_total_per_employee"]),
            "per_trainee_gbp": number(row["twentyfour_prices_total_per_trainee"]),
            "employees": number(row["employees"]),
            "trainees": number(row["trainees"]),
        }
        for row in sector_source
    ]
    sectors = sorted(sectors, key=lambda row: row["per_employee_gbp"], reverse=True)
    if len(sectors) != 13:
        raise RuntimeError(f"Expected 13 published 2024 sectors, got {len(sectors)}.")

    r11 = next(row for row in trend if row["year"] == 2011)
    r22 = next(row for row in trend if row["year"] == 2022)
    r24 = next(row for row in trend if row["year"] == 2024)
    hi = max(sectors, key=lambda row: row["per_employee_gbp"])
    lo = min(sectors, key=lambda row: row["per_employee_gbp"])

    sector_values = sorted(row["per_employee_gbp"] for row in sectors)
    sector_mean = sum(sector_values) / len(sector_values)
    sector_variance = sum(
        (value - sector_mean) ** 2 for value in sector_values
    ) / len(sector_values)

    robustness = {
        "per_employee_real_change_2011_2024_pct": round(real_change_pct(r24["per_employee_gbp_2024_prices"], r11["per_employee_gbp_2024_prices"]), 2),
        "per_trainee_real_change_2011_2024_pct": round(real_change_pct(r24["per_trainee_gbp_2024_prices"], r11["per_trainee_gbp_2024_prices"]), 2),
        "total_training_real_change_2011_2024_pct": round(real_change_pct(r24["total_training_mn_gbp"], r11["total_training_mn_gbp"]), 2),
        "coverage_change_2011_2024_pp": round((r24["training_coverage_share"] - r11["training_coverage_share"]) * 100, 2),
        "coverage_change_2022_2024_pp": round((r24["training_coverage_share"] - r22["training_coverage_share"]) * 100, 2),
        "sector_per_employee_max_min_ratio_2024": round(hi["per_employee_gbp"] / lo["per_employee_gbp"], 2),
        "sector_per_employee_range_gbp_2024": round(hi["per_employee_gbp"] - lo["per_employee_gbp"], 2),
        "sector_per_employee_unweighted_median_gbp_2024": round(sector_values[len(sector_values) // 2], 2),
        "sector_per_employee_unweighted_cv_2024": round((sector_variance ** 0.5) / sector_mean, 4),
    }

    summary = {
        "study": "Employer Training Investment Capacity: A Longitudinal UK Study",
        "headline_metrics": {
            "uk_per_employee_2011_gbp_2024_prices": int(r11["per_employee_gbp_2024_prices"]),
            "uk_per_employee_2024_gbp": int(r24["per_employee_gbp_2024_prices"]),
            "real_change_pct_2011_2024": robustness["per_employee_real_change_2011_2024_pct"],
            "uk_total_training_2011_bn_2024_prices": round(r11["total_training_mn_gbp"] / 1000, 2),
            "uk_total_training_2024_bn": round(r24["total_training_mn_gbp"] / 1000, 1),
            "employees_trained_2024_m": round(r24["trainees"] / 1_000_000, 3),
            "highest_sector_2024": hi["sector"],
            "highest_sector_per_employee_2024": int(hi["per_employee_gbp"]),
            "lowest_sector_2024": lo["sector"],
            "lowest_sector_per_employee_2024": int(lo["per_employee_gbp"]),
            "training_coverage_share_2022": round(r22["training_coverage_share"], 4),
            "training_coverage_share_2024": round(r24["training_coverage_share"], 4),
            "coverage_change_pp_2022_2024": robustness["coverage_change_2022_2024_pp"],
            "per_employee_real_change_2022_2024_pct": round(real_change_pct(r24["per_employee_gbp_2024_prices"], r22["per_employee_gbp_2024_prices"]), 2),
            "per_trainee_real_change_2022_2024_pct": round(real_change_pct(r24["per_trainee_gbp_2024_prices"], r22["per_trainee_gbp_2024_prices"]), 2),
            "total_training_real_change_2022_2024_pct": round(real_change_pct(r24["total_training_mn_gbp"], r22["total_training_mn_gbp"]), 2),
        },
        "robustness_diagnostics": robustness,
        "comparable_uk_years": EXPECTED_YEARS,
        "finding": (
            "Real UK employer training spend per employee fell from £2,410 in 2011 "
            "to £1,700 in 2024 in 2024 prices. Between 2022 and 2024, the derived "
            "trainees-to-employees ratio rose from 60.22% to 62.85% while real spend "
            "per employee fell 13.27% and real spend per trainee fell 16.62%. In 2024, "
            "sector spending ranged from £920 per employee in Public admin. to £2,630 "
            "in Construction."
        ),
        "source": "UK Employer Skills Survey 2024 - Investment in Training",
        "retrieved": "2026-09-25",
        "release_version": "1.1.0",
        "interpretation_boundary": (
            "Expenditure intensity and training reach are aggregate resource-deployment "
            "indicators. They do not directly measure training quality, learning transfer, "
            "skill gain, causal return on investment, or latent organizational capability."
        ),
    }
    return trend, sectors, robustness, summary


def clean_number(value):
    value = float(value)
    return int(value) if value.is_integer() else value


def write_outputs(trend, sectors, robustness, summary):
    TREND_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)

    trend_fields = [
        "year", "per_employee_gbp_2024_prices", "per_trainee_gbp_2024_prices",
        "total_training_mn_gbp", "employees", "trainees", "training_coverage_share",
    ]
    with TREND_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=trend_fields)
        writer.writeheader()
        for row in trend:
            output = dict(row)
            for key in ("per_employee_gbp_2024_prices", "per_trainee_gbp_2024_prices", "employees", "trainees"):
                output[key] = clean_number(output[key])
            output["total_training_mn_gbp"] = round(output["total_training_mn_gbp"], 2)
            output["training_coverage_share"] = round(output["training_coverage_share"], 4)
            writer.writerow(output)

    sector_fields = ["sector", "per_employee_gbp", "per_trainee_gbp", "employees", "trainees"]
    with SECTOR_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=sector_fields)
        writer.writeheader()
        for row in sectors:
            output = {
                key: clean_number(value) if key != "sector" else value
                for key, value in row.items()
            }
            writer.writerow(output)

    with ROBUSTNESS_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=["metric", "value"])
        writer.writeheader()
        for metric, value in robustness.items():
            writer.writerow({"metric": metric, "value": value})

    SUMMARY_PATH.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def assert_close(a, b, tolerance=5e-5):
    if abs(float(a) - float(b)) > tolerance:
        raise SystemExit(f"FAIL: {a} != {b}")


def check_release(trend, sectors, robustness, summary):
    packaged_trend = load_trend()
    packaged_sectors = load_sectors()
    packaged_robustness = load_robustness()
    packaged_summary = load_summary()

    if len(packaged_trend) != len(trend):
        raise SystemExit("FAIL: packaged trend row count differs")
    for expected, packaged in zip(trend, packaged_trend):
        if int(packaged["year"]) != expected["year"]:
            raise SystemExit("FAIL: trend year differs")
        for key in (
            "per_employee_gbp_2024_prices",
            "per_trainee_gbp_2024_prices",
            "total_training_mn_gbp",
            "employees",
            "trainees",
            "training_coverage_share",
        ):
            assert_close(packaged[key], expected[key])

    if len(packaged_sectors) != len(sectors):
        raise SystemExit("FAIL: packaged sector count differs")
    for expected, packaged in zip(sectors, packaged_sectors):
        if packaged["sector"] != expected["sector"]:
            raise SystemExit("FAIL: sector identity differs")
        for key in ("per_employee_gbp", "per_trainee_gbp", "employees", "trainees"):
            assert_close(packaged[key], expected[key])

    for key, value in robustness.items():
        if key not in packaged_robustness:
            raise SystemExit(f"FAIL: missing robustness metric {key}")
        assert_close(packaged_robustness[key], value, 0.005)

    if packaged_summary != summary:
        raise SystemExit("FAIL: packaged empirical summary differs from source rebuild")

    print("official_dfe_rebuild: PASS")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write", action="store_true", help="Regenerate packaged evidence.")
    parser.add_argument("--check", action="store_true", help="Require source-to-release agreement.")
    args = parser.parse_args()

    rows, sha256 = fetch_source()
    trend, sectors, robustness, summary = analyze(rows)

    if args.write:
        write_outputs(trend, sectors, robustness, summary)

    if args.check:
        check_release(trend, sectors, robustness, summary)

    print(
        json.dumps(
            {
                "source_sha256": sha256,
                "source_rows": len(rows),
                "summary": summary,
                "trend_rows": len(trend),
                "sector_rows": len(sectors),
                "robustness": robustness,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
