import pandas as pd
import numpy as np

df = pd.read_json("students.json")

arr = np.array(df["marks"])

print(f"{df}\n{arr}\n{arr >= 35}")
print(arr[arr >= 35])
print(len(arr[arr >= 35]))
print(df.sort_values("marks", ascending=False).head(3))