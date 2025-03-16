import requests
import pandas as pd

# url = 'https://xn--90afdbaav0bd1afy6eub5d.xn--p1ai/search'
url = 'https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/'
resp = requests.get(url)

with open('index.html', 'wb') as f:
    f.write(resp.content)

df = pd.read_html(url)
print(df[0][0:3].iloc[:, 2:])