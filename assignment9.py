
import numpy as np

marks = np.array([60, 70, 80, 90, 100])

print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Median:", np.median(marks))
print("Variance:", np.var(marks))
print("Standard Deviation:", np.std(marks))

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

print("Correlation:", np.corrcoef(x, y)[0, 1])
