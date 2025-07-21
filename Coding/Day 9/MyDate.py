'''
Name: Abhigyan Maji
ID: 30382
Date: 16 July 2025  
Purpose: Perform calendar-based operations such as leap year check, max days in a month, month name, calendar display, and Julian day calculation
'''

import calendar
from datetime import datetime

class MyDate:
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def isLeap(self):
        return calendar.isleap(self.yyyy)

    def maxDays(self):
        return calendar.monthrange(self.yyyy, self.mm)[1]

    def monthName(self):
        return calendar.month_name[self.mm]

    def printCal(self, newMonth=0, newYear=0):
        if newMonth == 0:
            newMonth = self.mm
        if newYear == 0:
            newYear = self.yyyy
        print(calendar.month(newYear, newMonth))

    def printJulianCal(self, newMonth=0, newYear=0):
        if newMonth == 0:
            newMonth = self.mm
        if newYear == 0:
            newYear = self.yyyy
        cal = calendar.TextCalendar()
        print(cal.formatmonth(newYear, newMonth))

    def julianDay(self):
        dt = datetime(self.yyyy, self.mm, self.dd)
        return dt.timetuple().tm_yday

if __name__ == '__main__':
    d = MyDate(16, 7, 2025)
    print("Leap Year:", d.isLeap())
    print("Max Days:", d.maxDays())
    print("Month Name:", d.monthName())
    print("Julian Day:", d.julianDay())
    d.printCal()
    d.printJulianCal()
