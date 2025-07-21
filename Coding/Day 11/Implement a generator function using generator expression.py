'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Implement a generator function Using generator expression

''' 
start, end, step = 1, 10, 2
my_range = (i for i in range(start, end, step))
for num in my_range:
    print(num, end=' ')
print()
