'''
Name: Abhigyan Maji
ID: 30382
Date: 14 July 2025
Purpose: Print all Armstrong numbers between 1 and 100000 using numOps module
'''

import numOps

for i in range(1, 100001):
    if numOps.isArmstrong(i):
        print(i, end=' ')
