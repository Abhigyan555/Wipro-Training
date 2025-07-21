'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025  
Purpose: Demonstrate class-level logging using Python's logging module inside a custom class
'''

import logging

class MyClass:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.warning('MyClass Logger initialized')

if __name__ == '__main__':
    obj1 = MyClass()
    obj2 = MyClass()
