'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Armstrong or not using funtion
'''
def is_armstrong(num):
    original = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit * digit * digit
        num = num // 10
    if sum == original:
        print(original, "is an Armstrong number")
    else:
        print(original, "is not an Armstrong number")

n = int(input("Enter a 3-digit number: "))
is_armstrong(n)
