"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025
Purpose- To print the given string in reverse order using recursion
"""

def reverse_string(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string(s[:-1])

# Input from user
text = input("Enter a string: ")
print("Reversed string:", reverse_string(text))
