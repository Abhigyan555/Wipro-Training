'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 8 July 2025
    Purpose- Update the non prime num as 0
'''
start = int(input("Enter the first number: "))
numbers = []
for num in range(start, start + 100):
    if num <= 1:
        numbers.append(0)
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            numbers.append(num)
        else:
            numbers.append(0)
print("Updated list (non-primes as 0):")
print(numbers)
