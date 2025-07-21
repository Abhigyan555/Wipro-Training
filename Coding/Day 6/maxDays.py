"""
Name- Abhigyan Maji
ID- 30382
Date- 12 July 2025 
Purpose- Finding the number of days in month  
"""

def isLeap(yyyy):
    return (yyyy % 4 == 0 and yyyy % 100 != 0) or (yyyy % 400 == 0)

def maxDays(mm, yyyy):
    if mm == 2:
        return 29 if isLeap(yyyy) else 28
    elif mm in [4, 6, 9, 11]:
        return 30
    else:
        return 31


mm = int(input("Enter month number (1-12): "))
yyyy = int(input("Enter year: "))
print("Days in month:", maxDays(mm, yyyy))