def validate(df, rules):
errors = []
for rule in rules:
result = rule(df)
if result is not None:
errors.append(result)
return errors