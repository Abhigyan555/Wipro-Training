'''
Name: Abhigyan Maji
ID: 30382
Date: 18 July 2025  
Purpose: Generate even numbers using an iterator
''' 
class EvenGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        if self.current % 2 == 0:
            result = self.current
            self.current += 1
            return result
        self.current += 1
        return self.__next__()

start = 1
end = 10
even_generator = EvenGenerator(start, end)
for num in even_generator:
    print(num)
