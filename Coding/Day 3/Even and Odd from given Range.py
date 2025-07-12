'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- Suffix of a number
'''

num = int(input("Enter any number: "))


print("Odd:", end=" ")
count = 0
n = num
while count < 5:
    (n % 2 != 0) and (print(n, end=" ") or True) and (count := count + 1)
    n += 1

print()


print("Even:", end=" ")
count = 0
n = num
while count < 5:
    (n % 2 == 0) and (print(n, end=" ") or True) and (count := count + 1)
    n += 1
