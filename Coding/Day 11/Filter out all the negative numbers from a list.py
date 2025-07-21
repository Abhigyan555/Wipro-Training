'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Filter out all the negative numbers from a list.
''' 
nums = [-3, 5, -1, 7, 0]
non_negative_nums = [num if num >= 0 else 0 for num in nums]

print(non_negative_nums)