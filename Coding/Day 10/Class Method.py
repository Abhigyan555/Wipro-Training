'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025  
Purpose: Check password strength using static method and demonstrate class/static methods for employee salary management
'''

import datetime

class PasswordUtils:
    @staticmethod
    def isStrong(password):
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password)
        )
        
if __name__ == '__main__':
    password = 'testone'
    print(f"password: {password} is {'Strong' if PasswordUtils.isStrong(password) else 'Weak'}")
    
    password = 'test1One#$'
    print(f"password: {password} is {'Strong' if PasswordUtils.isStrong(password) else 'Weak'}")

class Employee:
    raise_percent = 1.05

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def applyRaise(self):
        self.salary *= self.raise_percent 
        
    @classmethod
    def setRaisePercent(cls, amount):
        cls.raise_percent = amount

    @staticmethod
    def isWorkday(day):
        return day.lower() not in ('saturday', 'sunday')


if __name__ == '__main__':
    emp1 = Employee("Alice", 50000)

    print(f"\nInitial details for {emp1.name}: Salary = {emp1.salary}")

    emp1.applyRaise()

    print(f"After first raise for {emp1.name}: Salary = {emp1.salary:.2f}")

    Employee.setRaisePercent(1.10) 

    emp1.applyRaise()

    print(f"After second raise (with new raise percent) for {emp1.name}: Salary = {emp1.salary:.2f}")

    today = datetime.date.today()
    
    sunday = "Sunday" 
    print(f"\nIs {sunday} a workday? {Employee.isWorkday(sunday)}")

    friday = "Friday"
    print(f"Is {friday} a workday? {Employee.isWorkday(friday)}")
