'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Replace Multiple Spaces with One

''' 
import re

def replace_multiple_spaces(text):
    return re.sub(r"\s+", " ", text)

# Test
text = "Hello   World,   this   is   a   test."
print(replace_multiple_spaces(text))