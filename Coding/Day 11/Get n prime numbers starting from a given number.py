'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Get n prime numbers starting from a given number

''' 

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def primeGenerator(start, n):
    count = 0
    num = start
    while count < n:
        if is_prime(num):
            yield num
            count += 1
        num += 1

start = 100
n = 25
for p in primeGenerator(start, n):
    print(p, end=' ')
print()
