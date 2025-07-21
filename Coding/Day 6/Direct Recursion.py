'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Direct Recursion
'''
    def recur(num):
    if num <= 10:
        print(num, end=' ')
        recur(num + 1)
 
if __name__ == '__main__':
    recur(1)
    print('\n-------------------------')