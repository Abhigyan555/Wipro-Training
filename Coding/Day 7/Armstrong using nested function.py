'''
Name: Abhigyan Maji
ID: 30382
Date: 14 July 2025
Purpose: Check if a number is Armstrong using nested functions
'''

def isArmstrong(num):
    def cubeSum(n):
        sum = 0
        temp = n
        while temp > 0:
            digit = temp % 10
            sum += digit ** 3
            temp //= 10
        return sum

    return cubeSum(num) == num

# Take input from user
number = int(input("Enter a number: "))

if isArmstrong(number):
    print(number, "is an Armstrong number.")
else:
    print(number, "is not an Armstrong number.")