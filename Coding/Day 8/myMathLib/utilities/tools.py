def isEven(num):
    return not num % 2

def isPrime(num):
    flag = True
    for i in range(2, num//2 + 1):
        if num % i == 0:
            flag = False
    return flag

def isArmstrong(num):
    digits, pow = str(num), len(digits)
    sum = 0
    for digit in digits:
        sum += int(digit) ** pow 
    
    return sum == num


