'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- First 25 prime numbers from a range
'''

num = int(input("Enter a number: "))
count = 0
n = num

while count < 25:
    is_prime = 1
    for i in range(2, n):
        if n % i == 0:
            is_prime = 0
    if n > 1:
        if is_prime == 1:
            print(n, end=" ")
            count = count + 1
    n = n + 1
