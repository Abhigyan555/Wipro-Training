'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Generate n Fibonacci numbers using an iterator
''' 
def fibGenerator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for i in fibGenerator(10):
    print(i, end=' ')
print()
