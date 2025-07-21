"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025 
Purpose- Finding out the month name
"""

def monthName(mm):
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    print("Month name is:", months[mm - 1])


mm = int(input("Enter month number (1-12): "))
monthName(mm)