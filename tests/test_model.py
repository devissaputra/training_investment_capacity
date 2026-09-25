from research.model import coverage_share,real_change_pct,validate_bundle
def test_coverage(): assert coverage_share(60,100)==.6
def test_real_change(): assert round(real_change_pct(1700,2410),2)==-29.46
def test_packaged_trend_and_sectors(): assert validate_bundle()
