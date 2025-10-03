from validation.core_validator import validate


def invoice_positive(df):
if (df['total_due'] < 0).any():
return "Negative invoice amount found"


def validate_finance(df):
rules = [invoice_positive]
return validate(df, rules)