'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Perform arithmetic operations using command-line arguments with sys.argv
'''

import sys

if len(sys.argv) < 4:
    print("Insufficient arguments")
else:
    n1 = int(sys.argv[1])
    op = sys.argv[2]
    n2 = int(sys.argv[3])

    if op == '+':
        print("Output:", n1 + n2)
    elif op == '-':
        print("Output:", n1 - n2)
    elif op == '*':
        print("Output:", n1 * n2)
    elif op == '/':
        if n2 != 0:
            print("Output:", n1 / n2)
        else:
            print("Error: Division by zero")
    elif op == '%':
        if n2 != 0:
            print("Output:", n1 % n2)
        else:
            print("Error: Modulus by zero")
    elif op == '//':
        if n2 != 0:
            print("Output:", n1 // n2)
        else:
            print("Error: Floor division by zero")
    elif op == '**':
        print("Output:", n1 ** n2)
    else:
        print("Invalid operator")
