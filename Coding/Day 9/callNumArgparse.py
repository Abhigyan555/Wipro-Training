'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Create a simple command-line calculator that performs basic arithmetic operations based on user input
'''

import argparse

parser = argparse.ArgumentParser(description='Simple Command Line Calculator')

parser.add_argument('n1', type=float, help='First number')
parser.add_argument('operator', type=str, help='Operator (+, -, *, /, %, //, **)')
parser.add_argument('n2', type=float, help='Second number')

args = parser.parse_args()

if args.operator == '+':
    print("Output:", args.n1 + args.n2)
elif args.operator == '-':
    print("Output:", args.n1 - args.n2)
elif args.operator == '*':
    print("Output:", args.n1 * args.n2)
elif args.operator == '/':
    if args.n2 != 0:
        print("Output:", args.n1 / args.n2)
    else:
        print("Error: Division by zero")
elif args.operator == '%':
    if args.n2 != 0:
        print("Output:", args.n1 % args.n2)
    else:
        print("Error: Modulus by zero")
elif args.operator == '//':
    if args.n2 != 0:
        print("Output:", args.n1 // args.n2)
    else:
        print("Error: Floor division by zero")
elif args.operator == '**':
    print("Output:", args.n1 ** args.n2)
else:
    print("Invalid operator")
