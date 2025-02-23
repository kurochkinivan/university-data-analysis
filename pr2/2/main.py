import pandas as pd
import numpy as np

df = pd.read_csv('../BikesData.csv')

df['Temperature'] = df['Temperature'].interpolate(method='linear')

# 1
df['Normal Humidity'] = np.where((df['Humidity'] >= 40) & (df['Humidity'] <= 60), 1, 0)

normal_humidity_2018 = df[(df['Date'].str.contains('2018')) & (df['Normal Humidity'] == 1)].shape[0]
print(normal_humidity_2018)

# 2
conditions = [
    (df['Temperature'] < 0),
    (df['Temperature'] >= 0) & (df['Temperature'] < 15),
    (df['Temperature'] >= 15) & (df['Temperature'] < 25),
    (df['Temperature'] >= 25)
]
categories = ['Freezing', 'Chilly', 'Nice', 'Hot']

df['Temperature Category'] = np.select(conditions, categories)

freezing_count = (df['Temperature Category'] == 'Freezing').sum()
print(freezing_count)

# 3
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
freezing_days_2018 = df[(df['Date'].dt.year == 2018) & (df['Temperature Category'] == 'Freezing')] \
    .groupby(df['Date'].dt.date)['Temperature Category'] \
    .apply(lambda x: (x == 'Freezing').sum() > 12) \
    .sum()
print(freezing_days_2018)

# 4
df['Good Weather'] = np.where(
    (df['Temperature Category'] == 'Nice') &
    (df['Normal Humidity'] == 1) &
    (df['Wind speed'] <= 5.4) &
    (df['Rainfall'] == 0) &
    (df['Snowfall'] == 0), 1, 0
)

autumn_2018_good_weather = df[
    (df['Date'].dt.year == 2018) & 
    (df['Seasons'] == 'Autumn') & 
    (df['Good Weather'] == 1)
].shape[0]
print(autumn_2018_good_weather)

# 5.
autumn_2018_good_days = df[
    (df['Date'].dt.year == 2018) & 
    (df['Seasons'] == 'Autumn')
].groupby(df['Date'].dt.date)['Good Weather'].apply(lambda x: x.sum() >= 12).sum()

print(autumn_2018_good_days)
