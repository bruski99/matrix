# Define a function to calculate the determinant of a 2x2 matrix
def determinant(matrix):
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]

# Get input from user for matrix A
a = []
print("Enter the values of matrix A (2x2):")
for i in range(2):
    row = []
    for j in range(2):
        val = int(input("Enter value for row "+str(i+1)+" and column "+str(j+1)+": "))
        row.append(val)
    a.append(row)

# Get input from user for matrix B
b = []
print("Enter the values of matrix B (2x2):")
for i in range(2):
    row = []
    for j in range(2):
        val = int(input("Enter value for row "+str(i+1)+" and column "+str(j+1)+": "))
        row.append(val)
    b.append(row)

# Get input from user for matrix C
c = []
print("Enter the values of matrix C (2x2):")
for i in range(2):
    row = []
    for j in range(2):
        val = int(input("Enter value for row "+str(i+1)+" and column "+str(j+1)+": "))
        row.append(val)
    c.append(row)

# Calculate and print the determinant of each matrix
det_a = determinant(a)
det_b = determinant(b)
det_c = determinant(c)

print("Determinant of matrix A is:", det_a)
print("Determinant of matrix B is:", det_b)
print("Determinant of matrix C is:", det_c)
