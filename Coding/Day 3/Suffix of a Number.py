'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 7 July 2025
    Purpose- Suffix of a number
'''
num_str = input("Enter a number: ")
num = int(num_str)

if 10 <= num % 100 <= 20:
    suffix = "th"
else:
    last_digit = num % 10
    if last_digit == 1:
        suffix = "st"
    elif last_digit == 2:
        suffix = "nd"
    elif last_digit == 3:
        suffix = "rd"
    else:
        suffix = "th"

print(f"{num}{suffix}")