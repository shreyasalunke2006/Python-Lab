
import pandas as pd

data = {
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Marks": [85, 90, 75, 95],
    "Age": [20, 21, 19, 20]
}

df = pd.DataFrame(data)

print("Dataset:\n", df)
print("\nFirst 2 rows:\n", df.head(2))
print("\nDataset information:")
df.info()
print("\nStatistics:\n", df.describe())
