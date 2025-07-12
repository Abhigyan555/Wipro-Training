'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 8 July 2025
    Purpose- Maximum count of consecutive zeroes between a range
'''

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

nums = []

for num in range(start, end + 1):

    if num <= 1:
        nums.append(0)
    else:
        prime = True
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
        if prime:
            nums.append(num)
        else:
            nums.append(0)

max_count = 0
count = 0

for n in nums:
    if n == 0:
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0

print("Updated list (non-primes replaced by 0):")
print(nums)

print("Maximum consecutive 0s:", max_count)