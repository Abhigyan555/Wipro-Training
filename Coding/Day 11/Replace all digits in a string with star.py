'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Replace all digits in a string with *
''' 
import re

def replace_digits_with_star(text):
    return re.sub(r"\d", "*", text)

# Test
text = "Hello123World456"
print(replace_digits_with_star(text))