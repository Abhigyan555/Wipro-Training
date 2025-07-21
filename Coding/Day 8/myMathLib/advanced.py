def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num - 1)

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

