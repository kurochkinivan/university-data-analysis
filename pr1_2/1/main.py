import pandas as pd 

df = pd.read_csv('../msft.csv')
df['Date'] = pd.to_datetime(df['Date'])

avg = df['Open'].where(df['Date'].dt.year == 2022).mean()
print(round(avg, 2))