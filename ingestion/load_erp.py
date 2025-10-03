import pandas as pd


def load_erp():
df = pd.DataFrame({
'order_id': [1,2,3],
'customer_id': [101,102,103],
'amount': [1000,1500,1200]
})
print("ERP data loaded")
return df


if __name__ == '__main__':
load_erp()