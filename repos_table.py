import requests
import pandas as pd

response = requests.get("https://api.github.com/users/rudrashukla1507/repos")
repos = response.json()

df = pd.DataFrame(repos)
print(df.shape)


print(df[["name", "language", "size"]].sort_values("size", ascending=False)[df["size"]>2])
print(df[["name", "language", "size"]][df["language"] == "Python"])