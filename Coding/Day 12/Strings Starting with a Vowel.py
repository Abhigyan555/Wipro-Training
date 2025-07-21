'''
Name: Abhigyan Maji
ID: 30382
Date: 19 July 2025  
Purpose: Strings Starting with a Vowel
''' 
words = ['apple', 'banana', 'orange', 'grape', 'umbrella']
vowels = 'aeiouAEIOU'
result = list(filter(lambda x: x[0] in vowels, words))
print(result)
