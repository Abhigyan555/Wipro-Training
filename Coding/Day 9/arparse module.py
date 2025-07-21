'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Validate if the user is eligible to vote based on age using command line arguments using argparse module
'''

import argparse
parse = argparse.ArgumentParser(description='Validating User for voting')
parse.add_argument('name', help='Name of the user')
parse.add_argument('age',type=int, help='Age of the user')
args = parse.parse_args()
 
if args.age >= 18:
    print(f"Hello '{args.name}', Your age is {args.age} So You are eliglible to vote")
else:
    print(f"Hello '{args.name}', Your age is {args.age} So You are NOT eliglible to vote")
 