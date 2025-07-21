'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Fibonacci series using binary recursion
'''
def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

if __name__ == '__main__':
    print("Generating Fibonacci sequence up to the 10th term:")
    for i in range(10):
        print(f'{i+1}: {fibo(i)}')

    print('\n------------------------------------------')
    