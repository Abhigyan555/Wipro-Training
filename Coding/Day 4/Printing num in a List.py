'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 8 July 2025
    Purpose- Printing numbers in a List
'''

start = int(input("Enter the first number: "))

nums = [] 

i = 0
while i < 100:
    nums += [start + i] 
    i = i + 1

# Print the whole list directly
print("The list of 100 numbers:")
print(nums)
