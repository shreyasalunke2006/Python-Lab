
import pandas as pd

df = pd.DataFrame({
    "Name": ["Amit", "Neha", "Rahul", "Priya"],
    "Marks": [75, 90, 65, 85]
})

print("Original data:\n", df)
print("\nMarks above 75:\n", df[df["Marks"] > 75])
print("\nSorted by marks:\n", df.sort_values("Marks"))
print("\nStudents with marks >= 80:\n",
      df[df["Marks"] >= 80])
