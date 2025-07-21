'''
Name: Abhigyan Maji
ID: 30382
Date: 14 July 2025
Purpose: Check if a number is a Factorial number using nested functions
'''

def isFactorial(num):
    def factorialSeries():
        fact = 1
        i = 1
        while fact <= num:
            if fact == num:
                return True
            i += 1
            fact *= i
        return False

    return factorialSeries()

# Take input from user
number = int(input("Enter a number: "))

if isFactorial(number):
    print(number, "is a Factorial number.")
else:
    print(number, "is not a Factorial number.")