import numpy as np

# prompt user to enter values for matrices A, B, and C
print("Enter values for 2x2 matrix A:")
a11 = float(input("a11: "))
a12 = float(input("a12: "))
a21 = float(input("a21: "))
a22 = float(input("a22: "))
A = np.array([[a11, a12], [a21, a22]])

print("Enter values for 2x2 matrix B:")
b11 = float(input("b11: "))
b12 = float(input("b12: "))
b21 = float(input("b21: "))
b22 = float(input("b22: "))
B = np.array([[b11, b12], [b21, b22]])

print("Enter values for 2x2 matrix C:")
c11 = float(input("c11: "))
c12 = float(input("c12: "))
c21 = float(input("c21: "))
c22 = float(input("c22: "))
C = np.array([[c11, c12], [c21, c22]])

# compute the result of A*B*C
result = np.dot(np.dot(A, B), C)

# print the result
print("Result of A*B*C:")
print(result)
