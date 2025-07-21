'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Generate even numbers between start and end using generator expression
''' 
start, end = 1, 10
even_numbers = (i for i in range(start, end + 1) if i % 2 == 0)
for num in even_numbers:
    print(num, end=' ')
print()
