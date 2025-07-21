'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Find All Dates in Format DD-MM-YYYY
''' 
import re

def find_dates(text):
    pattern = r"\b\d{2}-\d{2}-\d{4}\b"
    return re.findall(pattern, text)

# Test
text = "My birthday is 12-05-1990 and my friend's birthday is 23-08-1995."
print(find_dates(text))  
