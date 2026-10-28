
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", a)
print("Matrix B:\n", b)
print("Addition:\n", a + b)
print("Multiplication:\n", np.dot(a, b))
print("Transpose:\n", a.T)
print("Determinant:", np.linalg.det(a))
print("Mean:", np.mean(a))
