'''
Name: Abhigyan Maji
ID: 30382
Date: 14 July 2025
Purpose: NumOps
'''

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def isArmstrong(n):
    temp = n
    digits = len(str(n))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    return total == n

def isPalindrome(n):
    return str(n) == str(n)[::-1]
