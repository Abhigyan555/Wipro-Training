'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 8 July 2025
    Purpose- Number of days in a month
'''
mm = int(input("Enter month (1-12): "))
yyyy = int(input("Enter year: "))
dd = 1  

months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

days_in_month = [31, 28, 31, 30, 31, 30,
                 31, 31, 30, 31, 30, 31]


if (yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0):
    days_in_month[1] = 29


days = days_in_month[mm - 1]


print(f'\n    {months[mm - 1]} {yyyy}')
print('Su Mo Tu We Th Fr Sa')

# Zeller’s formula 
c = yyyy // 100
y = yyyy % 100
m = mm + 10 if mm <= 2 else mm - 2
y = y - 1 if m >= 11 else y

# Applying Zeller's formula
w = int(dd + (2.6 * m - 0.2) + y + y // 4 + c // 4 - 2 * c) % 7


for _ in range(w):
    print("   ", end="")


for date in range(1, days + 1):
    print(f'{date:2}', end=" ")
    if (w + date) % 7 == 0:
        print() 

print(f'\n Number of days = {days}')