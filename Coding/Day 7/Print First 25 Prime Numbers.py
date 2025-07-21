'''
Name: Abhigyan Maji
ID: 30382
Date: 14 July 2025
Purpose: Print first 25 prime numbers from a given number using numOps module
'''

import numOps

start = int(input("Enter starting number: "))
count = 0

while count < 25:
    if numOps.isPrime(start):
        print(start, end=' ')
        count += 1
    start += 1
