# function to calculate determinant of a 3x3 matrix
def determinant(mat):
    det = mat[0][0]*(mat[1][1]*mat[2][2]-mat[2][1]*mat[1][2]) - \
          mat[0][1]*(mat[1][0]*mat[2][2]-mat[1][2]*mat[2][0]) + \
          mat[0][2]*(mat[1][0]*mat[2][1]-mat[1][1]*mat[2][0])
    return det

# get input for matrix D
print("Enter values for matrix D:")
D = []
for i in range(3):
    row = []
    for j in range(4):
        row.append(float(input(f"D[{i+1}, {j+1}]: ")))
    D.append(row)

# get input for matrix E
print("\nEnter values for matrix E:")
E = []
for i in range(4):
    row = []
    for j in range(3):
        row.append(float(input(f"E[{i+1}, {j+1}]: ")))
    E.append(row)

# multiply D and E
result = [[0 for j in range(3)] for i in range(3)]
for i in range(3):
    for j in range(3):
        for k in range(4):
            result[i][j] += D[i][k]*E[k][j]

# calculate determinant of result matrix
det_result = determinant(result)

# print result and determinant
print("\nResult matrix:")
for row in result:
    print(row)
print(f"\nDeterminant of result matrix: {det_result}")
