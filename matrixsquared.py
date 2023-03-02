# Define a function to square a 2x2 matrix
def square(matrix):
    result = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix[i][k] * matrix[k][j]
    return result

# Get input from user for matrix C
c = []
print("Enter the values of matrix C (2x2):")
for i in range(2):
    row = []
    for j in range(2):
        val = int(input("Enter value for row "+str(i+1)+" and column "+str(j+1)+": "))
        row.append(val)
    c.append(row)

# Calculate and print the square of matrix C
c_squared = square(c)
print("Square of matrix C is:")
for row in c_squared:
    print(row)
