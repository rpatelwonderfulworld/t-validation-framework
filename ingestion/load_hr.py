import pandas as pd


def load_hr():
df = pd.DataFrame({
'employee_id': [301,302,303],
'name': ['Alice','Bob','Charlie'],
'department': ['HR','Finance','ERP']
})
print("HR data loaded")
return df


if __name__ == '__main__':
load_hr()