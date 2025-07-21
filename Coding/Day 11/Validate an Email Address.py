'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Validate an Email Address
'''

import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    return False

# Test
print(validate_email("test@example.com"))  
print(validate_email("invalid_email")) 
