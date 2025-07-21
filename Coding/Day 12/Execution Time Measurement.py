'''
Name: Abhigyan Maji
ID: 30382
Date: 19 July 2025  
Purpose: Execution Time Measurement
''' 
import time

def timeIt(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.5f} seconds")
        return result
    return wrapper

@timeIt
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

@timeIt
def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

print(factorial(5))
print(fibo(20))
