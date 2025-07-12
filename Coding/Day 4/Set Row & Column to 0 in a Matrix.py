'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 8 July 2025
    Purpose- Set entire row and column to 0 if any element is 0
'''


matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

# Store rows and columns to be set to 0
zero_rows = []
zero_cols = []

# Step 1: Find position of 0s
for i in range(3):
    for j in range(3):
        if matrix[i][j] == 0:
            zero_rows.append(i)
            zero_cols.append(j)

# Step 2: Set rows to 0
for i in zero_rows:
    for j in range(3):
        matrix[i][j] = 0

# Step 3: Set columns to 0
for j in zero_cols:
    for i in range(3):
        matrix[i][j] = 0


for row in matrix:
    print(row)
