from ingestion.load_erp import load_erp
from validation.erp_validation import validate_erp


def test_erp_validation():
df = load_erp()
errors = validate_erp(df)
assert isinstance(errors, list)