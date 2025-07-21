"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025
Purpose- To reverse a given list using recursion
"""

def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

# Input from user
lst = input("Enter list elements separated by space: ").split()
print("Reversed list:", reverse_list(lst))
