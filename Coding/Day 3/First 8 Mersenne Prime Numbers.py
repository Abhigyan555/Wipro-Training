'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- First 8 Mersenne Prime Numbers
'''

print("First 8 Mersenne Prime Numbers:")
count = 0
n = 2

while count < 8:
    power = 1
    result = 1
    for i in range(n):
        result = result * 2
    mersenne = result - 1

    is_prime = 1
    for j in range(2, mersenne):
        if mersenne % j == 0:
            is_prime = 0

    if is_prime == 1:
        print(mersenne)
        count = count + 1

    n = n + 1
