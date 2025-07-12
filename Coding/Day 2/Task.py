# Problem 1
''' 
    Name: Abhigyan Maji
    ID:  30382
    Date: 4 July 2025
    Purpose: 
                Id   Name				 Sal
                1001 Raju Bhai           125000.00  
'''
print("Problem #2:")
id = int(input("Enter ID: "))
name = input("Enter Name: ")
sal = float(input("Enter Salary: "))

print("\nid         name        sal")
print(f"{id:<10}{name:<12}{sal:.2f}")



# Problem 2
''' 
    Name: Abhigyan Maji
    ID:  30382
    Date: 4 July 2025
    Purpose: 
                -------------------------------------------
                    Id   Name				 Sal
                -------------------------------------------
                     1001 Raju Bhai           125000.00      	
                -------------------------------------------  
'''
id = int(input("Enter ID: "))
name = input("Enter Name: ")
sal = float(input("Enter Salary: "))

print("\nid         name        sal")
print("-----------------------------")
print(f"{id:<10}{name:<12}{sal:.2f}")


print("\n")



# Problem 3
''' 
    Name: Abhigyan Maji
    ID: 30382 
    Date: 4 July 2025
    Purpose: 
                 -------------------------------------------
                | Id   |  Name				 |  Sal         |
                 -------------------------------------------
                | 1001 |  Raju Bhai          |  125000.00   |   	
                 -------------------------------------------
'''
id = int(input("Enter ID: "))
name = input("Enter Name: ")
sal = float(input("Enter Salary: "))

print("\nid     |    name   |     sal   |")
print("----------------------------------")

print(f"{id:<6} | {name:^9} | {sal:>10.2f} |")
