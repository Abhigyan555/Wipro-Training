'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Custom implementation of range(start, end, step) using generator
''' 
def myRange(start, end, step):
    while start < end:
        yield start
        start += step

for i in myRange(1, 10, 2):
    print(i, end=' ')
print()
