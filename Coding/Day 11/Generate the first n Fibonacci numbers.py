'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Generate the first n Fibonacci numbers
''' 
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

n = 10
for num in fibonacci(n):
    print(num, end=' ')
print()
