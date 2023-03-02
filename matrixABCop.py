# prompt user to enter values for matrix A
print("Enter values for 2x2 matrix A:")
A = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(float(input(f"a{i+1}{j+1}: ")))
    A.append(row)
print("Matrix A:\n", A)

# prompt user to enter values for matrix B
print("Enter values for 2x2 matrix B:")
B = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(float(input(f"b{i+1}{j+1}: ")))
    B.append(row)
print("Matrix B:\n", B)

# prompt user to enter values for matrix C
print("Enter values for 2x2 matrix C:")
C = []
for i in range(2):
    row = []
    for j in range(2):
        row.append(float(input(f"c{i+1}{j+1}: ")))
    C.append(row)
print("Matrix C:\n", C)

# calculate the result of the three matrices
result = []
for i in range(2):
    row = []
    for j in range(2):
        value = A[i][j] * B[i][j] - C[i][j]
        row.append(value)
    result.append(row)
print("Result:\n", result)
