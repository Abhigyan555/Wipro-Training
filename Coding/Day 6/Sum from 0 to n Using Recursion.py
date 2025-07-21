"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025
Purpose- To find the sum of numbers from 0 to n using recursion
"""

def sum_to_n(n):
    if n == 0:
        return 0
    return n + sum_to_n(n - 1)

# Input from user
num = int(input("Enter a number: "))
print("Sum from 0 to", num, "is", sum_to_n(num))
