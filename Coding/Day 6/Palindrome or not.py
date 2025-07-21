'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Palindrome or not using funtion
'''
def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        print(n, "is a Palindrome")
    else:
        print(n, "is not a Palindrome")

num = input("Enter a number or word: ")
is_palindrome(num)
