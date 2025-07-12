'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 8 July 2025
    Purpose- Print Matrix of Numbers in Rows and Column format
'''
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
num = 1
i = 0
while i < rows:
    row = []
    j = 0
    while j < cols:
        row += [num]
        num += 1
        j += 1
    matrix += [row]
    i += 1

print(matrix)
