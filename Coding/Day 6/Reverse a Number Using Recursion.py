"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025
Purpose- To reverse a number using recursion
"""

def reverse_number(n, rev=0):
    if n == 0:
        return rev
    else:
        return reverse_number(n // 10, rev * 10 + n % 10)

# Input from user
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print("Reversed number is:", reversed_num)
