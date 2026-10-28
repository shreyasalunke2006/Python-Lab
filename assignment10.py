
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([20, 30, 40, 50, 60])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[6]])

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction for 6:", prediction[0])
print("Model Score:", model.score(X, y))
