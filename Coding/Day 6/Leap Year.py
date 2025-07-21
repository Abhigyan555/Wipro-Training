'''
    Name- Abhigyan Maji
    ID- 30382
    Date- 12 July 2025
    Purpose- Leap Year or not using funtion
'''
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a Leap Year")
    else:
        print(year, "is not a Leap Year")

yr = int(input("Enter a year: "))
is_leap_year(yr)
