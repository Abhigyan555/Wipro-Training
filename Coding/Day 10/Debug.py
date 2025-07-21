'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025
Purpose:  Debugging Python code using pdb
'''
def sumNumbers(num):
    sum = 0
    for var in range(num+1):
        sum += var 

    return sum 

if __name__ == '__main__':
    res = sumNumbers(10) 
    print(f'Sum: {res}')