'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Check voting eligibility using command-line arguments (name and age) with sys.argv
'''

import sys

if len(sys.argv) < 3:
    print("Insufficient arguments. Usage: python voting.py <name> <age>")
else:
    name = sys.argv[1]
    age = int(sys.argv[2])

    if age >= 18:
        print(f"Hello '{name}', You are eligible to vote")
    else:
        print(f"Hello '{name}', You are NOT eligible to vote")
