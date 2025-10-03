from validation.core_validator import validate


def name_not_null(df):
if df['name'].isnull().any():
return "Null employee name found"


def validate_hr(df):
rules = [name_not_null]
return validate(df, rules)