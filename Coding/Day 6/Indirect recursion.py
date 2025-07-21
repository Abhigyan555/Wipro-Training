'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Indirect Recursion
'''
    def funOne(num):
    if num <= 10:
        print(num, end=' ')
        funTwo(num + 1)        
 
def funTwo(num):
    if num <= 10:
        print(num, end=' ')
        funOne(num + 1)        
 
if __name__ == '__main__':
    funOne(1)
    print('\n-------------------------')