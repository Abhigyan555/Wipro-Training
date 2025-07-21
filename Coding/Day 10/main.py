'''
Name: Abhigyan Maji
ID: 30382
Date: 17 July 2025
Purpose: Import Manager, Developer, Intern from OOPModel and print their bonuses.
'''

from OOPModel.employeeOne import Manager, Developer, Intern

if __name__ == '__main__':
    # Creating objects with same method name but different behavior
    staff = [
        Manager("Anand", "anand@xyz.com", 90000),
        Developer("Bobby", "bobby@xyz.com", 60000),
        Intern("Chanti", "chanti@xyz.com", 5000)
    ]

    print("=== Employee Bonuses ===")
    for emp in staff:
        # Same method call, different output (polymorphism)
        print(f"{emp.name} bonus: {emp.calculateBonus()}")