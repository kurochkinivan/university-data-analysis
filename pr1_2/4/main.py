import pandas as pd

df = pd.read_excel('../stocks.xlsx', sheet_name='msft', parse_dates=['Date'], index_col='Date')

df_yearly = df.resample('Y')['Open'].median()
year = df_yearly[df_yearly < 35].index.year
print(year)