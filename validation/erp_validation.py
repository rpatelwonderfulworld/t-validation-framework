from validation.core_validator import validate


def order_positive(df):
if (df['amount'] < 0).any():
return "Negative order amount found"


def validate_erp(df):
rules = [order_positive]
return validate(df, rules)