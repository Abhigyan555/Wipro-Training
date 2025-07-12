'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 8 July 2025
    Purpose- Print Matrix of Numbers in Rows and Column format
'''
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

num = 1
i = 0
while i < rows:
    j = 0
    while j < cols:
        print(num, end=" ")
        num = num + 1
        j = j + 1
    print()
    i = i + 1
