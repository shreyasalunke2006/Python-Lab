
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.DataFrame({
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [40, 50, 60, 75, 90],
    "Attendance": [60, 65, 70, 80, 95]
})

plt.scatter(df["Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()
