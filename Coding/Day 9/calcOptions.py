'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Perform basic arithmetic operations using command-line arguments (add, subtract, multiply, divide, modulus, power, floor division)
'''

import argparse

# Create parser
parser = argparse.ArgumentParser(description='Performing basic Calculation')

# Define options
parser.add_argument('-a', '--add', nargs=2, type=float, help='Add two numbers')
parser.add_argument('-s', '--sub', nargs=2, type=float, help='Subtract two numbers')
parser.add_argument('-m', '--mul', nargs=2, type=float, help='Multiply two numbers')
parser.add_argument('-d', '--div', nargs=2, type=float, help='Divide two numbers')
parser.add_argument('-f', '--floordiv', nargs=2, type=float, help='Floor division')
parser.add_argument('-p', '--pow', nargs=2, type=float, help='Power: a^b')
parser.add_argument('-r', '--mod', nargs=2, type=float, help='Modulus: a % b')

# Parse arguments
args = parser.parse_args()

# Perform operations
if args.add:
    print(f'Adding {args.add[0]} + {args.add[1]} --> Result: {args.add[0] + args.add[1]}')
if args.sub:
    print(f'Subtracting {args.sub[0]} - {args.sub[1]} --> Result: {args.sub[0] - args.sub[1]}')
if args.mul:
    print(f'Multiplying {args.mul[0]} * {args.mul[1]} --> Result: {args.mul[0] * args.mul[1]}')
if args.div:
    if args.div[1] != 0:
        print(f'Dividing {args.div[0]} / {args.div[1]} --> Result: {args.div[0] / args.div[1]}')
    else:
        print("Error: Division by zero")
if args.floordiv:
    if args.floordiv[1] != 0:
        print(f'Floor Division {args.floordiv[0]} // {args.floordiv[1]} --> Result: {args.floordiv[0] // args.floordiv[1]}')
    else:
        print("Error: Floor division by zero")
if args.pow:
    print(f'Power {args.pow[0]} ** {args.pow[1]} --> Result: {args.pow[0] ** args.pow[1]}')
if args.mod:
    if args.mod[1] != 0:
        print(f'Modulus {args.mod[0]} % {args.mod[1]} --> Result: {args.mod[0] % args.mod[1]}')
    else:
        print("Error: Modulus by zero")
