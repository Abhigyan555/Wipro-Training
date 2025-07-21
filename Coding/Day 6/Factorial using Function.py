'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Factorial using function
'''
    def factorial(num):
    fact=1

    for i in range(1, num+1):
        fact=fact*i
    return fact 

number=int(input("Enter any number: "))

result=factorial(number)

print("The factorial of %d = %d"%(number,result))
