'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Extract all vowels from a given String
''' 
given_string = "Hello World"
vowels = [char for char in given_string.lower() if char in 'aeiou']
print(vowels)
