import pandas as pd


def load_finance():
df = pd.DataFrame({
'invoice_id': [201,202,203],
'customer_id': [101,102,103],
'total_due': [500,700,650]
})
print("Finance data loaded")
return df


if __name__ == '__main__':
load_finance()
