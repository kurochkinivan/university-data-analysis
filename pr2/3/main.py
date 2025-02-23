import pandas as pd

df = pd.read_csv('../students.csv')

# 1 
info = df.shape[0]
print(info)

# 2
null_var_count = (df.isnull().sum() > 0).sum()
print(null_var_count)

# 3 
rows_after_drop = df.dropna().shape[0]
print(rows_after_drop)

# 4
cols_after_drop = df.dropna(axis=1, thresh=10).shape[1]
print(cols_after_drop)

# 5
avg_female = df['Weight'].where(df['Sex']=='женский').mean()
avg_male = df['Weight'].where(df['Sex']=='мужской').mean()

df['Weight'].fillna(avg_female).where(df['Sex'] == 'женский')
df['Weight'].fillna(avg_male).where(df['Sex'] == 'мужской')

avg_weight = df['Weight'].mean()
avg_weight = round(avg_weight, 2)
print(avg_weight)