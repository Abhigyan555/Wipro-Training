"""
Name- Abhigyan Maji  
ID- 30382  
Date- 12 July 2025  
Purpose- To demonstrate multiple recursion
"""

def recur(num):
    if num <= 10:
        print(num, end=' ')
        recur(num + 1)

def recurCaller(lst):
    for i in lst:
        print(i, end=' : ')
        recur(1)
        print()  
if __name__ == '__main__':
    lst = ['a', 'b', 'c', 'd', 'e']
    recurCaller(lst)
    print('\n--------------------------')
