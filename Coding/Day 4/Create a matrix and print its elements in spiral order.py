'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 8 July 2025
    Purpose- Create a matrix and print its elements in spiral order
'''


r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))


matrix = []
num = 1
for i in range(r):
    row = []
    for j in range(c):
        row.append(num)
        num += 1
    matrix.append(row)


print("\nMatrix:")
for row in matrix:
    for val in row:
        print(f"{val:2}", end=" ")
    print()

# Spiral 
top = 0
bottom = r - 1
left = 0
right = c - 1
spiral = []

while top <= bottom and left <= right:
    # Top row
    for i in range(left, right + 1):
        spiral.append(matrix[top][i])
    top += 1

    # Right column
    for i in range(top, bottom + 1):
        spiral.append(matrix[i][right])
    right -= 1

    # Bottom row
    if top <= bottom:
        for i in range(right, left - 1, -1):
            spiral.append(matrix[bottom][i])
        bottom -= 1

    # Left column
    if left <= right:
        for i in range(bottom, top - 1, -1):
            spiral.append(matrix[i][left])
        left += 1

#
print("\nSpiral order as list:")
print(spiral)
