import pandas as pd 

df = pd.read_excel(
    '../stocks.xlsx', 
    sheet_name='aapl', 
    skiprows=100, 
    nrows=500,
    names=['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Adj Close'],
    usecols=['Date', 'Open', 'Close', 'Volume'], 
    header=None,
    )
res = df.iloc[119]['Volume']
print(res)
