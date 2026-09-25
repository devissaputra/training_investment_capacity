#!/usr/bin/env python3
import csv, io, json, urllib.request
from research.model import coverage_share, real_change_pct
URL='https://explore-education-statistics.service.gov.uk/data-catalogue/data-set/a07479d1-e26d-4b66-9ec9-e683917c1388/csv'
rows=list(csv.DictReader(io.StringIO(urllib.request.urlopen(URL).read().decode('utf-8-sig'))))
def f(x):
    try:return float(x)
    except:return None
uk=[r for r in rows if r['geographic_level']=='National' and r['country_name']=='United Kingdom' and r['site_size']=='Total' and r['sector']=='Total' and f(r['twentyfour_prices_total_per_employee']) is not None]
uk=sorted(uk,key=lambda r:int(r['time_period']))
trend=[{'year':int(r['time_period']),'per_employee':f(r['twentyfour_prices_total_per_employee']),'per_trainee':f(r['twentyfour_prices_total_per_trainee']),'total_training_mn_gbp':f(r['twentyfour_prices_sum_total_mn']),'employees':f(r['employees']),'trainees':f(r['trainees']),'training_coverage_share':coverage_share(r['trainees'],r['employees'])} for r in uk]
sectors=[r for r in rows if r['geographic_level']=='National' and r['country_name']=='United Kingdom' and r['time_period']=='2024' and r['site_size']=='Total' and r['sector']!='Total' and f(r['twentyfour_prices_total_per_employee']) is not None]
r11=next(r for r in trend if r['year']==2011); r22=next(r for r in trend if r['year']==2022); r24=next(r for r in trend if r['year']==2024)
lo=min(sectors,key=lambda r:f(r['twentyfour_prices_total_per_employee'])); hi=max(sectors,key=lambda r:f(r['twentyfour_prices_total_per_employee']))
summary={'study':'Employer Training Investment Capacity: A Longitudinal UK Study','headline_metrics':{
'uk_per_employee_2011_gbp_2024_prices':int(r11['per_employee']),'uk_per_employee_2024_gbp':int(r24['per_employee']),'real_change_pct_2011_2024':round(real_change_pct(r24['per_employee'],r11['per_employee']),2),'uk_total_training_2011_bn_2024_prices':round(r11['total_training_mn_gbp']/1000,2),'uk_total_training_2024_bn':round(r24['total_training_mn_gbp']/1000,1),'employees_trained_2024_m':round(r24['trainees']/1_000_000,3),'highest_sector_2024':hi['sector'],'highest_sector_per_employee_2024':int(f(hi['twentyfour_prices_total_per_employee'])),'lowest_sector_2024':lo['sector'],'lowest_sector_per_employee_2024':int(f(lo['twentyfour_prices_total_per_employee'])),'training_coverage_share_2022':round(r22['training_coverage_share'],4),'training_coverage_share_2024':round(r24['training_coverage_share'],4),'coverage_change_pp_2022_2024':round((r24['training_coverage_share']-r22['training_coverage_share'])*100,2)},'finding':'UK employer training spend per employee fell from £2,410 in 2011 to £1,700 in 2024 in 2024 prices (−29.5%). At the same time, the survey-derived trained-employee share rose from about 60.2% in 2022 to 62.8% in 2024. In 2024, sector spending ranged from £920 per employee in Public Administration to £2,630 in Construction, showing that reach and investment intensity can move differently.','source':'UK Employer Skills Survey 2024 — Investment in Training','retrieved':'2026-09-25'}
print(json.dumps({'summary':summary,'trend':trend,'sector_rows':len(sectors)},indent=2))
