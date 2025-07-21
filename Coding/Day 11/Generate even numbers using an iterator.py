'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Generate even numbers using an iterator
''' 

def evenGenerator(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
            yield i

for i in evenGenerator(1, 20):
    print(i, end=' ')
print()
