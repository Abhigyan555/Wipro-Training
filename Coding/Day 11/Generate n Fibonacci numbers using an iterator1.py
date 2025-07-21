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
        if self.count >= self.n:
            raise StopIteration
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return result

n = 10
fibonacci_iterator = FibonacciIterator(n)
for num in fibonacci_iterator:
    print(num)
