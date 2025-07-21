'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Generate n Fibonacci numbers using an iterator
''' 

class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):