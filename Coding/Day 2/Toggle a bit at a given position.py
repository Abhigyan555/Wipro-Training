''' 
    Name: Abhigyan Maji
    ID:  30382
    Date: 4 July 2025
    Purpose: Toggle a bit at a given position
'''

n = int(input("Enter number: "))
p = int(input("Enter bit position to toggle: "))
n = n ^ (1 << p)
print("Result:", n)
