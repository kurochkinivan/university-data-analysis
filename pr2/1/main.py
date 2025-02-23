import pandas as pd
import numpy as np

df = pd.read_csv('../BikesData.csv')

# 1
shape = df.shape[0]
print(shape)

# 2
null_var_count = (df.isnull().sum() > 0).sum()
print(null_var_count) 

# 3
temp_null_count = df['Temperature'].isnull().sum()
print(temp_null_count)

# 4
mean_temp = df['Temperature'].mean()
mean_temp = round(mean_temp, 2)
print(mean_temp)

# 5
median_temp = df['Temperature'].median()
print(median_temp)

# 6
df['Temp22'] = df['Temperature'].fillna(22)
mean_temp_2018 = df[df['Date'].str.contains('2018')]['Temp22'].mean()
mean_temp_2018 = round(mean_temp_2018, 2)
print(mean_temp_2018)

# 7
df['Temp_Median'] = df['Temperature'].fillna(median_temp)
count_above_28 = (df['Temp_Median'] > 28).sum()
print(count_above_28)

# 8
np.random.seed(8)  # Фиксируем генератор случайных чисел
random_temps = pd.Series(np.random.choice(df['Temperature'].dropna(), size=len(df)))
df['Temperature_Random'] = df['Temperature'].fillna(random_temps)

temp_1504 = df.loc[1504, 'Temperature_Random']
print(temp_1504)

# 9
def fill_missing_avg(df):
    temp_filled = df['Temperature'].copy()
    missing_indices = df['Temperature'][df['Temperature'].isnull()].index
    
    for idx in missing_indices:
        above = df['Temperature'].shift(1)[idx]
        below = df['Temperature'].shift(-1)[idx]
        
        if pd.notna(above) and pd.notna(below):
            temp_filled[idx] = (above + below) / 2
    
    return temp_filled

df['Temperature_Avg'] = fill_missing_avg(df)
unfilled_count = df['Temperature_Avg'].isnull().sum()
print(unfilled_count)

# 10
df['Date_Hour'] = pd.to_datetime(df['Date'], format='%Y-%m-%d') + pd.to_timedelta(df['Hour'], unit='h')
df['Temperature'] = df['Temperature'].interpolate(method='linear')

temp_39 = df.loc[39, 'Temperature']
print(temp_39)

