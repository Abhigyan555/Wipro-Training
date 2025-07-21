"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025 
Purpose- Finding out the Date
"""

def monthName(mm):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    return months[mm - 1]

def printCalendar(dd, mm, yyyy):
    print("Date is:", dd, monthName(mm), yyyy)


dd = int(input("Enter day: "))
mm = int(input("Enter month (1-12): "))
yyyy = int(input("Enter year: "))
printCalendar(dd, mm, yyyy)