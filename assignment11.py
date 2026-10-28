
from sklearn.neighbors import KNeighborsClassifier

X = [
    [1, 30],
    [2, 40],
    [3, 50],
    [6, 80],
    [7, 90],
    [8, 95]
]

y = ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

student = [[7, 85]]
prediction = model.predict(student)

print("Study hours:", student[0][0])
print("Previous score:", student[0][1])
print("Predicted result:", prediction[0])
