'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Multiplication table (1-5 × 1-5) as a list of lists.
''' 
multiplication_table = [[i*j for j in range(1, 6)] for i in range(1, 6)]
print(multiplication_table)
