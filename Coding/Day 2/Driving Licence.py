''' 
    Name: Abhigyan Maji
    ID:  30382
    Date: 4 July 2025
    Purpose: Check the person is eligible for Driving Licence
'''

age = int(input("Enter your age for driving license: "))
if age >= 18:
    print("You are eligible for a driving license.")
    if age >= 45:
        print("License validity: 5 years")
    elif age >= 35:
        print("License validity: 10 years")
    else:
        print("License validity: 20 years")
else:
    print("You are not eligible for a driving license.")
