#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import urllib.request
from pathlib import Path

from research.model import coverage_share, real_change_pct

ROOT = Path(__file__).resolve().parents[1]
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
    manifest = json.loads(MANIFEST_PATH.read_text())
    req = urllib.request.Request(
        manifest["direct_data_url"],
        headers={"User-Agent": "training-investment-capacity/1.0"},
    )
    with urllib.request.urlopen(req) as response:
        payload = response.read()

    actual = hashlib.sha256(payload).hexdigest()
    expected = manifest["source_sha256"]
    if actual != expected:
        raise RuntimeError(
            f"Source checksum mismatch: expected {expected}, got {actual}. "
            "Stop rather than silently analyzing a changed data file."
        )

    text = payload.decode("utf-8-sig")
    rows = list(csv.DictReader(io.StringIO(text)))
    if len(rows) != manifest["source_dataset_rows"]:
        raise RuntimeError(
            f"Source row-count mismatch: expected {manifest['source_dataset_rows']}, got {len(rows)}."
        )
    return rows, actual


def analyze(rows):
    uk = [
        r
        for r in rows
        if r["geographic_level"] == "National"
        and r["country_name"] == "United Kingdom"
        and r["site_size"] == "Total"
        and r["sector"] == "Total"
        and number(r["twentyfour_prices_total_per_employee"]) is not None
    ]
    uk = sorted(uk, key=lambda r: int(r["time_period"]))

    trend = [
        {
            "year": int(r["time_period"]),
            "per_employee_gbp_2024_prices": number(r["twentyfour_prices_total_per_employee"]),
            "per_trainee_gbp_2024_prices": number(r["twentyfour_prices_total_per_trainee"]),
            "total_training_mn_gbp": number(r["twentyfour_prices_sum_total_mn"]),
            "employees": number(r["employees"]),
            "trainees": number(r["trainees"]),
            "training_coverage_share": coverage_share(r["trainees"], r["employees"]),
        }
        for r in uk
    ]

    years = [r["year"] for r in trend]
    if years != EXPECTED_YEARS:
        raise RuntimeError(
            f"Comparable UK release years changed: expected {EXPECTED_YEARS}, got {years}. "
            "2019 is intentionally absent because Scotland did not participate in ESS 2019."
        )

    sector_source = [
        r
        for r in rows
        if r["geographic_level"] == "National"
        and r["country_name"] == "United Kingdom"
        and r["time_period"] == "2024"
        and r["site_size"] == "Total"
        and r["sector"] != "Total"
        and number(r["twentyfour_prices_total_per_employee"]) is not None
    ]
    sectors = [
        {
            "sector": r["sector"],
            "per_employee_gbp": number(r["twentyfour_prices_total_per_employee"]),
            "per_trainee_gbp": number(r["twentyfour_prices_total_per_trainee"]),
            "employees": number(r["employees"]),
            "trainees": number(r["trainees"]),
        }
        for r in sector_source
    ]
    sectors = sorted(sectors, key=lambda r: r["per_employee_gbp"], reverse=True)
    if len(sectors) != 13:
        raise RuntimeError(f"Expected 13 published 2024 sectors, got {len(sectors)}.")

    r11 = next(r for r in trend if r["year"] == 2011)
    r22 = next(r for r in trend if r["year"] == 2022)
    r24 = next(r for r in trend if r["year"] == 2024)
    hi = max(sectors, key=lambda r: r["per_employee_gbp"])
    lo = min(sectors, key=lambda r: r["per_employee_gbp"])

    sector_vals = sorted(r["per_employee_gbp"] for r in sectors)
    sector_mean = sum(sector_vals) / len(sector_vals)
    sector_variance = sum((x - sector_mean) ** 2 for x in sector_vals) / len(sector_vals)

    robustness = {
        "per_employee_real_change_2011_2024_pct": round(real_change_pct(r24["per_employee_gbp_2024_prices"], r11["per_employee_gbp_2024_prices"]), 2),
        "per_trainee_real_change_2011_2024_pct": round(real_change_pct(r24["per_trainee_gbp_2024_prices"], r11["per_trainee_gbp_2024_prices"]), 2),
        "total_training_real_change_2011_2024_pct": round(real_change_pct(r24["total_training_mn_gbp"], r11["total_training_mn_gbp"]), 2),
        "coverage_change_2011_2024_pp": round((r24["training_coverage_share"] - r11["training_coverage_share"]) * 100, 2),
        "coverage_change_2022_2024_pp": round((r24["training_coverage_share"] - r22["training_coverage_share"]) * 100, 2),
        "sector_per_employee_max_min_ratio_2024": round(hi["per_employee_gbp"] / lo["per_employee_gbp"], 2),
        "sector_per_employee_range_gbp_2024": round(hi["per_employee_gbp"] - lo["per_employee_gbp"], 2),
        "sector_per_employee_unweighted_median_gbp_2024": round(sector_vals[len(sector_vals) // 2], 2),
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
        },
        "robustness_diagnostics": robustness,
        "comparable_uk_years": EXPECTED_YEARS,
        "finding": (
            "Real UK employer training spend per employee fell from £2,410 in 2011 "
            "to £1,700 in 2024 in 2024 prices (-29.5%). The survey-derived trainees-"
            "to-employees ratio rose from about 60.2% in 2022 to 62.8% in 2024. "
            "In 2024, sector spending ranged from £920 per employee in Public admin. "
            "to £2,630 in Construction."
        ),
        "source": "UK Employer Skills Survey 2024 - Investment in Training",
        "retrieved": "2026-09-25",
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
    with TREND_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=trend_fields)
        writer.writeheader()
        for r in trend:
            out = dict(r)
            for key in ("per_employee_gbp_2024_prices", "per_trainee_gbp_2024_prices", "employees", "trainees"):
                out[key] = clean_number(out[key])
            out["total_training_mn_gbp"] = round(out["total_training_mn_gbp"], 2)
            out["training_coverage_share"] = round(out["training_coverage_share"], 4)
            writer.writerow(out)

    sector_fields = ["sector", "per_employee_gbp", "per_trainee_gbp", "employees", "trainees"]
    with SECTOR_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=sector_fields)
        writer.writeheader()
        for r in sectors:
            out = {k: (clean_number(v) if k != "sector" else v) for k, v in r.items()}
            writer.writerow(out)

    with ROBUSTNESS_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["metric", "value"])
        writer.writeheader()
        for metric, value in robustness.items():
            writer.writerow({"metric": metric, "value": value})

    SUMMARY_PATH.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        action="store_true",
        help="Regenerate packaged derived tables and JSON after source verification.",
    )
    args = parser.parse_args()

    rows, sha256 = fetch_source()
    trend, sectors, robustness, summary = analyze(rows)
    if args.write:
        write_outputs(trend, sectors, robustness, summary)

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
