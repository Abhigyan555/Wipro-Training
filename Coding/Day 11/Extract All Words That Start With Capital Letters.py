'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Extract All Words That Start With Capital Letters
''' 
import re

def extract_capitalized_words(text):
    pattern = r"\b[A-Z]\w*\b"
    return re.findall(pattern, text)

# Test
text = "Hello World, this is a Test."
print(extract_capitalized_words(text))  