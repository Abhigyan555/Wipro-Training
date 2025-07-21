'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Prime or not using function
'''

def is_prime(n):
    if n <= 1:
        print(n, "is not a prime number")
        return
    for i in range(2, n):
        if n % i == 0:
            print(n, "is not a prime number")
            return
    print(n, "is a prime number")

num = int(input("Enter a number: "))
is_prime(num)
