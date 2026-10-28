
import pandas as pd

df = pd.DataFrame({
    "Department": ["CE", "CE", "IT", "IT", "CE"],
    "Name": ["A", "B", "C", "D", "E"],
    "Marks": [80, 90, 75, 85, 70]
})

print("Dataset:\n", df)
print("\nAverage marks by department:")
print(df.groupby("Department")["Marks"].mean())

print("\nMaximum marks by department:")
print(df.groupby("Department")["Marks"].max())
