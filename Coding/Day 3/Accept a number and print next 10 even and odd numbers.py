'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- Accept a number and print next 10 even and odd numbers
'''

n = int(input("Enter any number: "))

print("Even:", end=' ')
i = n + 1
cnt = 0
while cnt < 5:
    if i % 2 == 0:
        print(i, end=' ')
        cnt = cnt + 1
    i = i + 1

print()

print("Odd:", end=' ')
i = n + 1
cnt = 0
while cnt < 5:
    if i % 2 != 0:
        print(i, end=' ')
        cnt = cnt + 1
    i = i + 1
