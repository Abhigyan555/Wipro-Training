'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- First 30 Mersenne numbers
'''

print("First 30 Mersenne numbers:")

for n in range(1, 31):
    result = 1
    for i in range(n):
        result = result * 2
    mersenne = result - 1
    print(mersenne)