'''
Name: Abhigyan Maji
ID: 30382
Date: 14 July 2025
Purpose: Check if a number is Palindrome using nested functions
'''

def isPalindrome(num):
    def reverseNum(n):
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n //= 10
        return rev

    return reverseNum(num) == num

# Take input from user
number = int(input("Enter a number: "))

if isPalindrome(number):
    print(number, "is a Palindrome number.")
else:
    print(number, "is not a Palindrome number.")
