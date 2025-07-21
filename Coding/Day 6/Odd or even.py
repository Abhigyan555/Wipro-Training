'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Odd or even using funtion
'''
def check_odd_even(n):
    if n % 2 == 0:
        print(n, "is Even")
    else:
        print(n, "is Odd")

num = int(input("Enter a number: "))
check_odd_even(num)
