'''
Name: Abhigyan Maji
ID: 30382
Date: 14 July 2025
Purpose: Print all Palindrome numbers between 1 and 50000 using numOps module
'''

import numOps

for i in range(1, 50001):
    if numOps.isPalindrome(i):
        print(i, end=' ')
