'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- Print a Series of Multiples with Starting Number
'''

n = int(input("Enter a number: "))

print(n, end=" ") 

i = 0
while i < 10:
    print(n * (i + 10), end=" ")
    i = i + 1
