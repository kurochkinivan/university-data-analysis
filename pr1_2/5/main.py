import pandas as pd 

df = pd.read_json('../data.json')
res = df['Close'].between(85, 90).sum()
print(res)