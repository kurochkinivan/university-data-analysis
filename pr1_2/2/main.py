import pandas as pd
import numpy as np

df = pd.read_excel('../stocks.xlsx', sheet_name='msft', parse_dates=['Date'], index_col='Date')
df_2011 = df[df.index.year == 2011]

min_close_idx = df_2011.idxmin()['Close']
print(min_close_idx)