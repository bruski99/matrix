#f unction to calculate polygon area using the Shoelace formula
def polygon_area(x, y):
    n = len(x)
    area = 0.0
    j = n - 1
    for i in range(n):
        area += (x[j] + x[i]) * (y[j] - y[i])
        j = i
    return abs(area/2)

# get input for number of vertices and coordinates
n = int(input("Enter number of vertices: "))
x = []
y = []
for i in range(n):
    x_i, y_i = map(float, input(f"Enter x and y coordinates of vertex {i+1}: ").split())
    x.append(x_i)
    y.append(y_i)

# calculate polygon area
area = polygon_area(x, y)

# print result
print(f"The area of the polygon is {area}.")
