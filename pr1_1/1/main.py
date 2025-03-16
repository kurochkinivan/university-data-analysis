import pandas as pd

default_cols = pd.read_csv('titanic.csv', nrows=0).columns

df1 = pd.read_csv('titanic.csv', index_col='PassengerId')
print(df1.head(1))

df2 = pd.read_csv('titanic.csv', nrows=10, usecols=['Name', 'Sex', 'Survived'])
print(df2.head(1))

df3 = pd.read_csv('titanic.csv', header=0, names=default_cols.str.lower())
print(df3.head(1))

df4 = pd.read_csv('titanic.csv', skiprows=100, nrows=8, header=0, names=default_cols)
print(df4.head(1))

df5 = pd.read_csv('titanic.csv', nrows=10, skiprows=[1, 3, 7], index_col='PassengerId')
print(df5)
