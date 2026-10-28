
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Rahul", "Neha"],
    "Marks": [80, np.nan, 70, np.nan]
})

print("Original data:\n", df)

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df = df.drop_duplicates()

print("\nCleaned data:\n", df)
