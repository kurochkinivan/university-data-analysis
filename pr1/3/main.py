import requests
import json
import pandas as pd

url = 'https://dummyjson.com/users'
resp = requests.get(url)
data = resp.json()
users = data["users"]

with open("users.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=4)

df = pd.read_json("users.json")
print(df.head()) 
