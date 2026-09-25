from __future__ import annotations
import csv, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def coverage_share(trainees,employees):return float(trainees)/float(employees)
def real_change_pct(new,old):return (float(new)/float(old)-1.0)*100.0
def load_trend():
    with (ROOT/'data/derived/primary_results.csv').open() as f:return list(csv.DictReader(f))
def load_sectors():
    with (ROOT/'data/derived/secondary_results.csv').open() as f:return list(csv.DictReader(f))
def load_summary():return json.loads((ROOT/'results/empirical_summary.json').read_text())
def validate_bundle():
    rows=load_trend(); sectors=load_sectors(); r22=next(r for r in rows if r['year']=='2022'); r24=next(r for r in rows if r['year']=='2024')
    return len(rows)==6 and len(sectors)==13 and abs(float(r22['training_coverage_share'])-coverage_share(r22['trainees'],r22['employees']))<1e-4 and float(r24['training_coverage_share'])>float(r22['training_coverage_share'])
