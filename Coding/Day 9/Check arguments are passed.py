'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Display command-line arguments passed to the script using sys.argv
'''

import sys

if len(sys.argv) > 1:
    print("Arguments passed:", sys.argv[1:])  # skip filename
else:
    print("No arguments Passed")
