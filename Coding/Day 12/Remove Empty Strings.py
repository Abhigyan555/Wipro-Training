'''
Name: Abhigyan Maji
ID: 30382
Date: 19 July 2025  
Purpose: Remove Empty Strings
''' 
data = ['hello', '', 'world', '', 'python']
result = list(filter(lambda x: x != '', data))
print(result)
