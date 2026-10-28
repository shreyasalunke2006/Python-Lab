
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
marks = [60, 70, 65, 80, 90]

plt.figure()
plt.plot(days, marks, marker="o")
plt.title("Marks Progress")
plt.xlabel("Day")
plt.ylabel("Marks")
plt.show()

plt.figure()
plt.bar(days, marks)
plt.title("Marks Bar Chart")
plt.xlabel("Day")
plt.ylabel("Marks")
plt.show()

plt.figure()
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
