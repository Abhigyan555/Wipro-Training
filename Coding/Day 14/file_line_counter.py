'''
Name: Abhigyan Maji
ID: 30382
Date: 22 July 2025
Purpose: Function to count the number of lines in a given file.
'''

def countLines(filename):
    with open(filename) as fobj:
        return len(fobj.readlines())
