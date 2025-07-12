''' 
    Name: Abhigyan Maji
    ID:  30382
    Date: 4 July 2025
    Purpose: Extract the Day of Week from Date
'''

dd= int(input("Enter the date: "))
mm= int(input("Enter the month: "))
yyyy = int(input("Enter the year: "))

c = yyyy // 100
y = yyyy % 100

m = mm + 10 if mm <= 2 else mm - 2
y = y - 1 if m >= 11 else y

w = int(dd + (2.6 * m - 0.2) + y + y // 4 + c // 4 - 2 * c) % 7

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print(f"{dd}/{mm}/{yyyy} is a {days[w]}")
