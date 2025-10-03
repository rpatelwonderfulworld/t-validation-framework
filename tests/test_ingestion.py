from ingestion.load_erp import load_erp
from ingestion.load_finance import load_finance
from ingestion.load_hr import load_hr


def test_erp():
df = load_erp()
assert not df.empty


def test_finance():
df = load_finance()
assert not df.empty


def test_hr():
df = load_hr()
assert not df.empty