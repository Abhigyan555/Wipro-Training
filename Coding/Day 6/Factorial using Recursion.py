"""
Name- Abhigyan Maji  
ID- 30382  
Date- 12 July 2025  
Purpose- Factorial using recursion 
"""

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n=int(input("Enter the value: "))
r=factorial(n)
print("Factorial: ",r)
