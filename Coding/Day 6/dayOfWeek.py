"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025 
Purpose- Finding out the Days of Week
"""

def dayOfWeek(dd, mm, yyyy):
    if mm < 3:
        mm += 12
        yyyy -= 1
    k = yyyy % 100
    j = yyyy // 100
    day = (dd + 13*(mm+1)//5 + k + k//4 + j//4 + 5*j) % 7
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    print("Day of the week is:", days[day])


dd = int(input("Enter day: "))
mm = int(input("Enter month (1-12): "))
yyyy = int(input("Enter year: "))
dayOfWeek(dd, mm, yyyy)